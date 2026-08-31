#!/usr/bin/env python3
"""Prepare an allowlisted MkDocs source tree from the repository catalogs."""

from __future__ import annotations

from collections import defaultdict
from datetime import date
from html import escape
import json
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUILD_DIR = ROOT / ".site-build"

PUBLIC_DOCUMENTS = (
    "CONTRIBUTING.md",
    "THIRD-PARTY-NOTICES.md",
    "docs/ARCHITECTURE.md",
    "docs/AUTOMATION.md",
    "docs/CONTENT-POLICY.md",
    "docs/GUIDE-QUALITY-STANDARD.md",
    "docs/LEARNING-RESOURCES.md",
    "docs/PROJECT-BRIEF.md",
    "docs/PUBLISHING.md",
    "docs/ROADMAP.md",
    "docs/SOURCE-INTAKE.md",
    "docs/SOURCE-QUALITY.md",
)

PROJECT_NAV = (
    ("Project brief", "docs/PROJECT-BRIEF.md"),
    ("Content and exam integrity", "docs/CONTENT-POLICY.md"),
    ("Source quality", "docs/SOURCE-QUALITY.md"),
    ("Add a source", "docs/SOURCE-INTAKE.md"),
    ("Guide quality standard", "docs/GUIDE-QUALITY-STANDARD.md"),
    ("Architecture", "docs/ARCHITECTURE.md"),
    ("Automation", "docs/AUTOMATION.md"),
    ("Roadmap", "docs/ROADMAP.md"),
    ("Publishing", "docs/PUBLISHING.md"),
)

VENDOR_LABELS = {
    "github": "GitHub",
    "microsoft": "Microsoft",
}

REVIEW_LABELS = {
    "ai-generated-draft": "AI-generated draft",
    "source-validated": "Source validated",
    "community-reviewed": "Community reviewed",
    "review-required": "Review required",
    "retired": "Retired",
}


def read_json(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def yaml_string(value: str) -> str:
    """Return a JSON-quoted string, which is also valid YAML."""

    return json.dumps(value, ensure_ascii=False)


def ensure_public_source(root: Path, relative_path: str) -> Path:
    """Resolve an allowlisted source without permitting repository escape."""

    source = (root / relative_path).resolve()
    resolved_root = root.resolve()
    if source != resolved_root and resolved_root not in source.parents:
        raise ValueError(f"Public source escapes repository: {relative_path}")
    if not source.is_file():
        raise FileNotFoundError(f"Missing public site source: {relative_path}")
    return source


def render_exam_card(exam: dict[str, object], *, page_prefix: str = "") -> str:
    code = escape(str(exam["code"]))
    title = escape(str(exam["title"]))
    vendor_id = str(exam["vendor_id"])
    vendor = escape(VENDOR_LABELS.get(vendor_id, vendor_id.title()))
    guide_source_path = str(exam["guide_path"]).replace("\\", "/")
    guide_path = escape(page_prefix + guide_source_path.removesuffix(".md") + "/")
    blueprint = escape(str(exam["study_guide_url"]), quote=True)
    reviewed = escape(str(exam["blueprint_last_checked"]))
    review_status = str(exam["review_status"])
    review_label = escape(REVIEW_LABELS.get(review_status, review_status))
    review_class = escape(review_status)
    change_status = str(exam["upcoming_change_status"])
    change_label = (
        "No change announced"
        if change_status == "none-announced"
        else change_status.replace("-", " ").title()
    )

    return f"""<article class="exam-card">
  <div class="exam-card__topline">
    <span class="exam-code">{code}</span>
    <span class="vendor-tag vendor-tag--{escape(vendor_id)}">{vendor}</span>
  </div>
  <h3><a href="{guide_path}">{title}</a></h3>
  <div class="exam-card__meta">
    <span class="review-badge review-badge--{review_class}">{review_label}</span>
    <span>{escape(change_label)}</span>
  </div>
  <p class="exam-card__date">Official objectives checked {reviewed}</p>
  <div class="exam-card__actions">
    <a class="exam-card__primary" href="{guide_path}">Open guide</a>
    <a href="{blueprint}" target="_blank" rel="noopener">Official blueprint ↗</a>
  </div>
</article>"""


def render_collection_card(
    collection: dict[str, object],
    *,
    page_prefix: str = "collections/",
) -> str:
    collection_id = escape(str(collection["id"]), quote=True)
    title = escape(str(collection["title"]))
    summary = escape(str(collection["summary"]))
    exam_codes = collection["exam_codes"]
    if not isinstance(exam_codes, list):
        raise ValueError(f"Collection {collection_id} needs an exam_codes array")
    codes = " · ".join(escape(str(code)) for code in exam_codes)

    return f"""<a class="collection-card collection-card--{collection_id}" href="{page_prefix}{collection_id}/">
  <span class="collection-card__count">{len(exam_codes)} guides</span>
  <strong>{title}</strong>
  <span class="collection-card__summary">{summary}</span>
  <span class="collection-card__codes">{codes}</span>
</a>"""


def render_homepage(
    template: str,
    exams: list[dict[str, object]],
    collections: list[dict[str, object]],
    source_count: int,
) -> str:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for exam in exams:
        grouped[str(exam["vendor_id"])].append(exam)

    track_cards: list[str] = []
    for vendor_id in ("github", "microsoft"):
        vendor_exams = grouped.get(vendor_id, [])
        label = VENDOR_LABELS[vendor_id]
        codes = " · ".join(escape(str(exam["code"])) for exam in vendor_exams)
        track_cards.append(
            f"""<a class="track-card track-card--{vendor_id}" href="exams/{vendor_id}/">
  <span class="track-card__eyebrow">Browse by provider</span>
  <strong>{escape(label)}</strong>
  <span>{len(vendor_exams)} guides · {codes}</span>
</a>"""
        )

    collection_cards = "\n".join(
        render_collection_card(collection) for collection in collections
    )
    return (
        template.replace("{{GUIDE_COUNT}}", str(len(exams)))
        .replace("{{SOURCE_COUNT}}", str(source_count))
        .replace("{{TRACK_CARDS}}", "\n".join(track_cards))
        .replace("{{COLLECTION_CARDS}}", collection_cards)
        .replace("{{GENERATED_DATE}}", date.today().isoformat())
    )


def render_catalog(exams: list[dict[str, object]]) -> str:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for exam in exams:
        grouped[str(exam["vendor_id"])].append(exam)

    sections: list[str] = []
    for vendor_id in ("github", "microsoft"):
        vendor = VENDOR_LABELS[vendor_id]
        cards = "\n".join(
            render_exam_card(exam, page_prefix="../")
            for exam in grouped.get(vendor_id, [])
        )
        sections.append(
            f"""## {vendor} {{#{vendor_id}}}

<div class="exam-grid">
{cards}
</div>"""
        )

    return f"""---
title: Study guide catalog
description: Browse every public-source certification study guide in the library.
hide:
  - toc
  - edit
---

# Study guide catalog

Every guide starts with the official blueprint, carries a visible review state, and links back to its canonical source. These are independent, AI-assisted drafts until their review state says otherwise.

Use global search when you know the concept but not the exam. Use the vendor sections below when you want to work through one certification.

{chr(10).join(sections)}
"""


def render_vendor_catalog(
    vendor_id: str,
    exams: list[dict[str, object]],
) -> str:
    vendor = VENDOR_LABELS[vendor_id]
    cards = "\n".join(
        render_exam_card(exam, page_prefix="../../")
        for exam in exams
        if exam["vendor_id"] == vendor_id
    )
    return f"""---
title: {vendor} study guides
description: Browse the independent {vendor} certification study guides in the library.
hide:
  - toc
  - edit
---

# {vendor} study guides

These guides are grouped by certification provider. The collections section offers a second, overlapping view based on what you want to learn.

<div class="exam-grid">
{cards}
</div>
"""


def render_collections_index(collections: list[dict[str, object]]) -> str:
    cards = "\n".join(
        render_collection_card(collection, page_prefix="")
        for collection in collections
    )
    return f"""---
title: Study collections
description: Browse certification guides by learning focus rather than exam provider.
hide:
  - toc
  - edit
---

# Study collections

Collections connect certifications that teach related capabilities. They are editorial groupings created by this project, not official vendor pathways, and a guide may appear in more than one collection.

<div class="collection-grid collection-grid--catalog">
{cards}
</div>
"""


def render_collection_page(
    collection: dict[str, object],
    exams_by_code: dict[str, dict[str, object]],
) -> str:
    title = str(collection["title"])
    summary = str(collection["summary"])
    codes = collection["exam_codes"]
    if not isinstance(codes, list):
        raise ValueError(f"Collection {collection['id']} needs an exam_codes array")
    cards = "\n".join(
        render_exam_card(exams_by_code[str(code)], page_prefix="../../")
        for code in codes
    )
    return f"""---
title: {yaml_string(title)}
description: {yaml_string(summary)}
hide:
  - toc
  - edit
---

<p class="page-eyebrow">Editorial study collection</p>

# {title}

<p class="collection-lede">{summary}</p>

This collection is a learning lens, not an official sequence. Start with the guide that best matches your current role and knowledge; use the others to broaden or deepen the same capability area.

<div class="exam-grid collection-exams">
{cards}
</div>

<p class="page-links"><a href="../../exams/">View every guide</a> · <a href="../">Explore other collections</a></p>
"""


def render_nav(
    exams: list[dict[str, object]],
    collections: list[dict[str, object]] | None = None,
) -> str:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for exam in exams:
        grouped[str(exam["vendor_id"])].append(exam)

    lines = [
        "nav:",
        "  - Home: index.md",
        "  - Study guides:",
        "      - Browse all: exams/index.md",
    ]

    for vendor_id in ("github", "microsoft"):
        lines.append(f"      - {VENDOR_LABELS[vendor_id]}:")
        lines.append(f"          - Overview: exams/{vendor_id}.md")
        for exam in grouped.get(vendor_id, []):
            label = f"{exam['code']} — {exam['title']}"
            path = str(exam["guide_path"]).replace("\\", "/")
            lines.append(f"          - {yaml_string(label)}: {yaml_string(path)}")

    lines.extend(
        [
            "  - Collections:",
            "      - Explore collections: collections/index.md",
        ]
    )
    for collection in collections or []:
        label = str(collection["title"])
        path = f"collections/{collection['id']}.md"
        lines.append(f"      - {yaml_string(label)}: {yaml_string(path)}")

    lines.extend(
        [
            "  - Places to learn: docs/LEARNING-RESOURCES.md",
            "  - About:",
        ]
    )
    for label, path in PROJECT_NAV:
        lines.append(f"      - {yaml_string(label)}: {yaml_string(path)}")
    lines.extend(
        [
            "      - Contribute: CONTRIBUTING.md",
            "      - License: https://github.com/cterpening/certification-study-library/blob/main/LICENSE",
            "      - Third-party notices: THIRD-PARTY-NOTICES.md",
        ]
    )
    return "\n".join(lines)


def prepare_site(root: Path = ROOT, build_dir: Path | None = None) -> dict[str, object]:
    root = root.resolve()
    build_dir = (build_dir or (root / ".site-build")).resolve()
    if build_dir.parent != root or build_dir.name != ".site-build":
        raise ValueError("The generated site directory must be <repository>/.site-build")

    if build_dir.exists():
        shutil.rmtree(build_dir)
    docs_dir = build_dir / "docs"
    docs_dir.mkdir(parents=True)

    exams_data = read_json(root / "config/exams.json")
    collections_data = read_json(root / "config/collections.json")
    sources_data = read_json(root / "data/sources.json")
    raw_exams = exams_data.get("exams")
    raw_collections = collections_data.get("collections")
    raw_sources = sources_data.get("sources")
    if not isinstance(raw_exams, list) or not raw_exams:
        raise ValueError("config/exams.json needs a non-empty exams array")
    if not isinstance(raw_sources, list):
        raise ValueError("data/sources.json needs a sources array")
    if not isinstance(raw_collections, list) or not raw_collections:
        raise ValueError("config/collections.json needs a non-empty collections array")
    exams = [exam for exam in raw_exams if isinstance(exam, dict)]
    if len(exams) != len(raw_exams):
        raise ValueError("Every exam entry must be an object")
    collections = [item for item in raw_collections if isinstance(item, dict)]
    if len(collections) != len(raw_collections):
        raise ValueError("Every collection entry must be an object")
    exams_by_code = {str(exam["code"]): exam for exam in exams}
    for collection in collections:
        codes = collection.get("exam_codes")
        if not isinstance(codes, list) or not codes:
            raise ValueError(f"Collection {collection.get('id')} needs exam codes")
        unknown_codes = set(str(code) for code in codes).difference(exams_by_code)
        if unknown_codes:
            raise ValueError(
                f"Collection {collection.get('id')} references unknown exams: "
                + ", ".join(sorted(unknown_codes))
            )

    published_sources: list[str] = []
    for exam in exams:
        relative_path = str(exam["guide_path"]).replace("\\", "/")
        source = ensure_public_source(root, relative_path)
        destination = docs_dir / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        published_sources.append(relative_path)

    for relative_path in PUBLIC_DOCUMENTS:
        source = ensure_public_source(root, relative_path)
        destination = docs_dir / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        published_sources.append(relative_path)

    website_dir = root / "website"
    homepage_template = (website_dir / "home.md.template").read_text(encoding="utf-8")
    homepage = render_homepage(
        homepage_template, exams, collections, len(raw_sources)
    )
    (docs_dir / "index.md").write_text(homepage, encoding="utf-8")

    catalog_dir = docs_dir / "exams"
    catalog_dir.mkdir()
    (catalog_dir / "index.md").write_text(render_catalog(exams), encoding="utf-8")
    for vendor_id in ("github", "microsoft"):
        (catalog_dir / f"{vendor_id}.md").write_text(
            render_vendor_catalog(vendor_id, exams), encoding="utf-8"
        )

    collections_dir = docs_dir / "collections"
    collections_dir.mkdir()
    (collections_dir / "index.md").write_text(
        render_collections_index(collections), encoding="utf-8"
    )
    for collection in collections:
        (collections_dir / f"{collection['id']}.md").write_text(
            render_collection_page(collection, exams_by_code), encoding="utf-8"
        )

    assets_source = website_dir / "assets"
    shutil.copytree(assets_source, docs_dir / "assets")

    config_template = (website_dir / "mkdocs.yml.template").read_text(
        encoding="utf-8"
    )
    config = config_template.replace(
        "{{SITE_NAV}}", render_nav(exams, collections)
    )
    (build_dir / "mkdocs.yml").write_text(config, encoding="utf-8")

    manifest = {
        "generated_on": date.today().isoformat(),
        "guide_count": len(exams),
        "collection_count": len(collections),
        "source_count": len(raw_sources),
        "published_sources": sorted(published_sources),
    }
    (build_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    manifest = prepare_site()
    print(
        f"Prepared {manifest['guide_count']} guides and "
        f"{manifest['source_count']} registered sources in .site-build"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
