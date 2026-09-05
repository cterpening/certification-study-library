#!/usr/bin/env python3
"""Prepare an allowlisted MkDocs source tree from the repository catalogs."""

from __future__ import annotations

from collections import defaultdict
from datetime import date
from html import escape
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUILD_DIR = ROOT / ".site-build"

PUBLIC_DOCUMENTS = (
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "THIRD-PARTY-NOTICES.md",
    "docs/ABOUT.md",
    "docs/ACCESSIBILITY.md",
    "docs/AI-AUDIT.md",
    "docs/ARCHITECTURE.md",
    "docs/AUTOMATION.md",
    "docs/BACKLOG.md",
    "docs/CONTENT-POLICY.md",
    "docs/GUIDE-QUALITY-STANDARD.md",
    "docs/LEARNING-RESOURCES.md",
    "docs/learning-journeys/README.md",
    "docs/learning-journeys/frontier-transformation-engineer.md",
    "docs/partner-ai/README.md",
    "docs/partner-ai/anthropic-claude-certified-architect-foundations.md",
    "docs/partner-ai/openai-ai-foundations.md",
    "docs/PROJECT-BRIEF.md",
    "docs/PUBLISHING.md",
    "docs/ROADMAP.md",
    "docs/SOURCE-INTAKE.md",
    "docs/SOURCE-FRESHNESS.md",
    "docs/SOURCE-QUALITY.md",
    "docs/SOURCE-VALIDATION.md",
)

PROJECT_NAV = (
    ("About this project", "docs/ABOUT.md"),
    ("Changelog", "CHANGELOG.md"),
    ("Project brief", "docs/PROJECT-BRIEF.md"),
    ("Content and exam integrity", "docs/CONTENT-POLICY.md"),
    ("Source quality", "docs/SOURCE-QUALITY.md"),
    ("Source validation", "docs/SOURCE-VALIDATION.md"),
    ("Independent AI audits", "docs/AI-AUDIT.md"),
    ("Official-source freshness", "docs/SOURCE-FRESHNESS.md"),
    ("Add a source", "docs/SOURCE-INTAKE.md"),
    ("Guide quality standard", "docs/GUIDE-QUALITY-STANDARD.md"),
    ("Accessibility", "docs/ACCESSIBILITY.md"),
    ("Architecture", "docs/ARCHITECTURE.md"),
    ("Automation", "docs/AUTOMATION.md"),
    ("Roadmap", "docs/ROADMAP.md"),
    ("Guide backlog", "docs/BACKLOG.md"),
    ("Publishing", "docs/PUBLISHING.md"),
)

REVIEW_LABELS = {
    "ai-generated-draft": "AI-generated draft",
    "source-validated": "Sources + objectives checked — human review pending",
    "community-reviewed": "Community reviewed",
    "review-required": "Review required",
    "retired": "Retired",
}

LEVEL_GROUPS = (
    (
        "beginner",
        "Beginner and foundational",
        "Start here for foundational vocabulary, concepts, and low-prerequisite certifications.",
    ),
    (
        "intermediate",
        "Intermediate, associate, and specialty",
        "Role-based and specialty guides that assume practical product or platform experience.",
    ),
    (
        "expert",
        "Expert and professional",
        "Advanced architecture, leadership, and professional certifications for experienced practitioners.",
    ),
)
LEVEL_LABELS = {
    "beginner": "Beginner",
    "intermediate": "Intermediate",
    "expert": "Expert",
}
LEVEL_ORDER = {level: index for index, (level, _, _) in enumerate(LEVEL_GROUPS)}

REPOSITORY_URL = "https://github.com/cterpening/certification-study-library"

PARTNER_REFERENCES = (
    {
        "provider": "OpenAI",
        "title": "AI Foundations",
        "path": "docs/partner-ai/openai-ai-foundations/",
        "state": "Invite-only certification reference",
        "summary": "Formal access is limited to invited Enterprise/Edu workspaces; the public Academy course is preparation, not the certification.",
    },
    {
        "provider": "Anthropic",
        "title": "Claude Certified Architect, Foundations",
        "path": "docs/partner-ai/anthropic-claude-certified-architect-foundations/",
        "state": "Partner-gated certification reference",
        "summary": "The exam remains in Partner Academy; public Claude Academy courses provide a timed technical preparation path.",
    },
)


def read_json(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def vendor_name(vendor_id: str, vendors: list[dict[str, object]] | None = None) -> str:
    """Resolve a provider label from the vendor catalog."""

    for vendor in vendors or []:
        if vendor.get("id") == vendor_id:
            return str(vendor["name"])
    return vendor_id.replace("-", " ").title()


def natural_sort_key(value: str) -> tuple[tuple[int, object], ...]:
    """Sort codes alphabetically while treating numeric components as numbers."""

    return tuple(
        (1, int(part)) if part.isdigit() else (0, part.casefold())
        for part in re.split(r"(\d+)", value)
        if part
    )


def exam_sort_key(exam: dict[str, object]) -> tuple[object, ...]:
    """Order exams by editorial level, natural exam code, then title."""

    level = str(exam["level"])
    return (
        LEVEL_ORDER[level],
        natural_sort_key(str(exam["code"])),
        str(exam["title"]).casefold(),
    )


def visible_vendors(
    exams: list[dict[str, object]],
    vendors: list[dict[str, object]] | None = None,
) -> list[dict[str, object]]:
    """Return catalog-ordered providers that currently have published guides."""

    used_ids = {str(exam["vendor_id"]) for exam in exams}
    if vendors is None:
        ordered_ids = list(dict.fromkeys(str(exam["vendor_id"]) for exam in exams))
        return [{"id": item, "name": vendor_name(item)} for item in ordered_ids]
    return [vendor for vendor in vendors if str(vendor.get("id")) in used_ids]


def yaml_string(value: str) -> str:
    """Return a JSON-quoted string, which is also valid YAML."""

    return json.dumps(value, ensure_ascii=False)


def markdown_slug(value: str) -> str:
    """Approximate Python-Markdown heading IDs for generated guide links."""

    slug = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE).strip().lower()
    return re.sub(r"[\s\-]+", "-", slug)


def extract_domain_rows(markdown: str) -> list[tuple[str, str]]:
    """Extract the first objective/domain table with weights or an unweighted label."""

    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if not re.match(r"^#{2,3}\s+.*(?:domain|objective).*(?:map|coverage)", line, re.I):
            continue
        rows: list[tuple[str, str]] = []
        for candidate in lines[index + 1 : index + 24]:
            if not candidate.startswith("|"):
                if rows:
                    break
                continue
            cells = [cell.strip() for cell in candidate.strip("|").split("|")]
            if len(cells) < 2 or not (
                re.search(r"\d+\s*[–-]\s*\d+%", cells[1])
                or cells[1].casefold() in {"not published", "unweighted"}
            ):
                continue
            rows.append((cells[0], cells[1]))
        if rows:
            return rows
    return []


def find_first_lab(markdown: str) -> tuple[str, str] | None:
    """Return the first useful lab heading and its generated anchor."""

    fallback: tuple[str, str] | None = None
    for line in markdown.splitlines():
        match = re.match(r"^#{1,3}\s+(.+)$", line)
        if not match or not re.search(r"\b(?:lab|exercise)\b", match.group(1), re.I):
            continue
        title = match.group(1).strip()
        item = (title, markdown_slug(title))
        if re.search(r"\b(?:lab|exercise)\s+\d+", title, re.I):
            return item
        fallback = fallback or item
    return fallback


def active_reading_estimate(markdown: str) -> str:
    """Estimate guide-only active technical reading at 90–130 words per minute."""

    body = re.sub(r"^---.*?---", "", markdown, count=1, flags=re.S)
    words = len(re.findall(r"\b[\w'-]+\b", body))
    low_minutes = max(15, round(words / 130 / 15) * 15)
    high_minutes = max(low_minutes + 15, round(words / 90 / 15) * 15)

    def format_minutes(minutes: int) -> str:
        hours, remainder = divmod(minutes, 60)
        if not hours:
            return f"{remainder} min"
        if not remainder:
            return f"{hours} hr"
        return f"{hours} hr {remainder} min"

    return f"{format_minutes(low_minutes)}–{format_minutes(high_minutes)}"


def render_guide_start(exam: dict[str, object], markdown: str) -> str:
    code = str(exam["code"])
    domains = extract_domain_rows(markdown)
    domain_items = "".join(
        f"<li><span>{escape(name)}</span><strong>{escape(weight)}</strong></li>"
        for name, weight in domains
    )
    if not domain_items:
        domain_items = "<li><span>See the objective map in this guide</span></li>"
    lab = find_first_lab(markdown)
    first_lab = (
        f'<a href="#{escape(lab[1], quote=True)}">{escape(lab[0])}</a>'
        if lab
        else "Use the first hands-on exercise in the guide"
    )
    issue_query = urlencode(
        {
            "template": "content-correction.yml",
            "title": f"[{code} content correction]: ",
        }
    )
    issue_url = f"{REPOSITORY_URL}/issues/new?{issue_query}"
    review_status = str(exam["review_status"])
    review_label = REVIEW_LABELS.get(review_status, review_status)

    return f"""<section class="guide-start" aria-labelledby="guide-start-heading">
  <div class="guide-start__heading">
    <div>
      <p class="page-eyebrow">Study guide at a glance</p>
      <h2 id="guide-start-heading">Start here</h2>
    </div>
    <a class="guide-start__report" href="{escape(issue_url, quote=True)}">Report an issue with {escape(code)}</a>
  </div>
  <div class="guide-start__facts">
    <div><span>Blueprint checked</span><strong>{escape(str(exam['blueprint_last_checked']))}</strong></div>
    <div><span>Review state</span><strong>{escape(review_label)}</strong></div>
    <div><span>Guide-only active reading</span><strong>{escape(active_reading_estimate(markdown))}</strong></div>
  </div>
  <p><strong>Prerequisites:</strong> {escape(str(exam['study_prerequisites']))}</p>
  <div class="guide-start__paths">
    <div><strong>Exam essentials</strong><span>Read the objective map, key distinctions, and readiness checklist.</span></div>
    <div><strong>Deep understanding</strong><span>Work through every domain, including decisions, failure modes, and related items.</span></div>
    <div><strong>Hands-on labs</strong><span>Begin with {first_lab}, then use the remaining labs to produce evidence you can inspect and explain.</span></div>
  </div>
  <details class="guide-start__domains">
    <summary>Official objective domains</summary>
    <ul>{domain_items}</ul>
  </details>
  <p class="guide-start__estimate">The active-reading range uses 90–130 words per minute for technical material. Labs, troubleshooting, note-taking, spaced review, and prerequisite gaps add time; it is not a total preparation promise.</p>
</section>"""


def prepare_guide_markdown(markdown: str, exam: dict[str, object]) -> str:
    """Add generated discovery metadata and navigation to a published guide copy."""

    lines = markdown.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"Guide {exam['code']} is missing front matter")
    try:
        front_matter_end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"Guide {exam['code']} has unclosed front matter") from exc
    description = (
        f"Independent {exam['code']} {exam['title']} study guide with objective "
        "mapping, explanations, labs, readiness checks, and public learning sources."
    )
    lines.insert(front_matter_end, f"description: {yaml_string(description)}")
    markdown = "\n".join(lines) + "\n"
    disclosure = re.search(
        r"^> \*\*Independent AI-assisted resource[^\n]*\n", markdown, re.M
    )
    if not disclosure:
        raise ValueError(f"Guide {exam['code']} is missing its visible disclosure")
    insertion = disclosure.end()
    return markdown[:insertion] + "\n" + render_guide_start(exam, markdown) + "\n\n" + markdown[insertion:]


def ensure_public_source(root: Path, relative_path: str) -> Path:
    """Resolve an allowlisted source without permitting repository escape."""

    source = (root / relative_path).resolve()
    resolved_root = root.resolve()
    if source != resolved_root and resolved_root not in source.parents:
        raise ValueError(f"Public source escapes repository: {relative_path}")
    if not source.is_file():
        raise FileNotFoundError(f"Missing public site source: {relative_path}")
    return source


def render_exam_card(
    exam: dict[str, object],
    *,
    page_prefix: str = "",
    vendors: list[dict[str, object]] | None = None,
    heading_level: int = 3,
) -> str:
    code = escape(str(exam["code"]))
    title = escape(str(exam["title"]))
    vendor_id = str(exam["vendor_id"])
    vendor = escape(vendor_name(vendor_id, vendors))
    level = str(exam["level"])
    level_label = escape(LEVEL_LABELS[level])
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
    <span class="exam-card__tags">
      <span class="level-tag level-tag--{escape(level)}">{level_label}</span>
      <span class="vendor-tag vendor-tag--{escape(vendor_id)}">{vendor}</span>
    </span>
  </div>
  <h{heading_level} class="exam-card__title"><a href="{guide_path}">{title}</a></h{heading_level}>
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


def render_exam_groups(
    exams: list[dict[str, object]],
    *,
    page_prefix: str,
    heading_level: int,
    vendors: list[dict[str, object]] | None = None,
) -> str:
    """Render consistently ordered level groups for any guide listing."""

    sections: list[str] = []
    marker = "#" * heading_level
    for level, label, description in LEVEL_GROUPS:
        level_exams = sorted(
            (exam for exam in exams if exam["level"] == level),
            key=exam_sort_key,
        )
        if not level_exams:
            continue
        cards = "\n".join(
            render_exam_card(
                exam,
                page_prefix=page_prefix,
                vendors=vendors,
                heading_level=heading_level + 1,
            )
            for exam in level_exams
        )
        sections.append(
            f"""{marker} {label}

<p class="level-intro">{description}</p>

<div class="exam-grid">
{cards}
</div>"""
        )
    return "\n\n".join(sections)


def render_collection_card(
    collection: dict[str, object],
    *,
    page_prefix: str = "collections/",
    exams_by_code: dict[str, dict[str, object]] | None = None,
) -> str:
    collection_id = escape(str(collection["id"]), quote=True)
    title = escape(str(collection["title"]))
    summary = escape(str(collection["summary"]))
    exam_codes = collection["exam_codes"]
    if not isinstance(exam_codes, list):
        raise ValueError(f"Collection {collection_id} needs an exam_codes array")
    display_codes = [str(code) for code in exam_codes]
    if exams_by_code is not None:
        display_codes.sort(key=lambda code: exam_sort_key(exams_by_code[code]))
    else:
        display_codes.sort(key=natural_sort_key)
    codes = " · ".join(escape(code) for code in display_codes)

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
    vendors: list[dict[str, object]] | None = None,
) -> str:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for exam in exams:
        grouped[str(exam["vendor_id"])].append(exam)

    track_cards: list[str] = []
    for vendor_record in visible_vendors(exams, vendors):
        vendor_id = str(vendor_record["id"])
        vendor_exams = grouped.get(vendor_id, [])
        label = str(vendor_record["name"])
        codes = " · ".join(
            escape(str(exam["code"]))
            for exam in sorted(vendor_exams, key=exam_sort_key)
        )
        track_cards.append(
            f"""<a class="track-card track-card--{vendor_id}" href="exams/{vendor_id}/">
  <span class="track-card__eyebrow">Browse by provider</span>
  <strong>{escape(label)}</strong>
  <span>{len(vendor_exams)} guides · {codes}</span>
</a>"""
        )

    exams_by_code = {str(exam["code"]): exam for exam in exams}
    collection_cards = "\n".join(
        render_collection_card(collection, exams_by_code=exams_by_code)
        for collection in collections
    )
    reference_cards = render_partner_reference_cards()
    return (
        template.replace("{{GUIDE_COUNT}}", str(len(exams)))
        .replace("{{SOURCE_COUNT}}", str(source_count))
        .replace("{{TRACK_CARDS}}", "\n".join(track_cards))
        .replace("{{REFERENCE_CARDS}}", reference_cards)
        .replace("{{COLLECTION_CARDS}}", collection_cards)
        .replace("{{GENERATED_DATE}}", date.today().isoformat())
    )


def render_partner_reference_cards(page_prefix: str = "") -> str:
    """Render visible, state-labeled cards for non-blueprint partner references."""

    cards = []
    for reference in PARTNER_REFERENCES:
        provider = str(reference["provider"])
        provider_id = provider.casefold().replace(" ", "-")
        cards.append(
            f"""<a class="track-card track-card--{escape(provider_id)}" href="{escape(page_prefix + str(reference['path']), quote=True)}">
  <span class="track-card__eyebrow">{escape(str(reference['state']))}</span>
  <strong>{escape(provider)} — {escape(str(reference['title']))}</strong>
  <span>{escape(str(reference['summary']))}</span>
</a>"""
        )
    return "\n".join(cards)


def render_catalog(
    exams: list[dict[str, object]],
    vendors: list[dict[str, object]] | None = None,
) -> str:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for exam in exams:
        grouped[str(exam["vendor_id"])].append(exam)

    sections: list[str] = []
    for vendor_record in visible_vendors(exams, vendors):
        vendor_id = str(vendor_record["id"])
        vendor = str(vendor_record["name"])
        groups = render_exam_groups(
            grouped.get(vendor_id, []),
            page_prefix="../",
            heading_level=3,
            vendors=vendors,
        )
        sections.append(
            f"""## {vendor} {{#{vendor_id}}}

{groups}"""
        )

    return f"""---
title: Study guide catalog
description: Browse every public-source certification study guide in the library.
hide:
  - toc
  - edit
---

# Study guide catalog

Every guide starts with the official blueprint, carries a visible review state, and links back to its canonical source. A sources-and-objectives check is an AI-assisted quality gate, not an independent human endorsement; only **Community reviewed** records a complete contributor review.

Use global search when you know the concept but not the exam. Use the vendor sections below when you want to work through one certification.

## Certification references

OpenAI and Anthropic are visible here because their credentials matter to partner audiences. They remain references—not objective-mapped guides—until enough of each assessment contract is public to validate scope without reconstructing gated material.

<div class="track-grid">
{render_partner_reference_cards(page_prefix="../")}
</div>

{chr(10).join(sections)}
"""


def render_vendor_catalog(
    vendor_record: dict[str, object],
    exams: list[dict[str, object]],
    vendors: list[dict[str, object]] | None = None,
) -> str:
    vendor_id = str(vendor_record["id"])
    vendor = str(vendor_record["name"])
    groups = render_exam_groups(
        [exam for exam in exams if exam["vendor_id"] == vendor_id],
        page_prefix="../../",
        heading_level=2,
        vendors=vendors,
    )
    return f"""---
title: {vendor} study guides
description: Browse the independent {vendor} certification study guides in the library.
hide:
  - toc
  - edit
---

# {vendor} study guides

Guides are grouped by editorial learning level, then sorted naturally by exam code. These levels are wayfinding aids, not vendor-issued designations. The collections section offers a second, overlapping view based on what you want to learn.

{groups}
"""


def render_collections_index(
    collections: list[dict[str, object]],
    exams_by_code: dict[str, dict[str, object]] | None = None,
) -> str:
    cards = "\n".join(
        render_collection_card(
            collection,
            page_prefix="",
            exams_by_code=exams_by_code,
        )
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
    vendors: list[dict[str, object]] | None = None,
) -> str:
    title = str(collection["title"])
    summary = str(collection["summary"])
    codes = collection["exam_codes"]
    if not isinstance(codes, list):
        raise ValueError(f"Collection {collection['id']} needs an exam_codes array")
    selected_exams = [exams_by_code[str(code)] for code in codes]
    groups = render_exam_groups(
        selected_exams,
        page_prefix="../../",
        heading_level=2,
        vendors=vendors,
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

This collection is a learning lens, not an official sequence or vendor pathway. Guides are grouped by editorial learning level and then sorted naturally by exam code. Start with the guide that best matches your current role and knowledge; use the others to broaden or deepen the same capability area.

{groups}

<p class="page-links"><a href="../../exams/">View every guide</a> · <a href="../">Explore other collections</a></p>
"""


def render_nav(
    exams: list[dict[str, object]],
    collections: list[dict[str, object]] | None = None,
    vendors: list[dict[str, object]] | None = None,
) -> str:
    lines = [
        "nav:",
        "  - Home: index.md",
        "  - Study guides:",
        "      - Browse all: exams/index.md",
    ]

    for vendor_record in visible_vendors(exams, vendors):
        vendor_id = str(vendor_record["id"])
        lines.append(
            f"      - {yaml_string(str(vendor_record['name']))}: exams/{vendor_id}.md"
        )

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
            "  - Partner learning journeys:",
            "      - Overview: docs/learning-journeys/README.md",
            "      - Frontier Transformation Engineer: docs/learning-journeys/frontier-transformation-engineer.md",
            "  - Partner AI references:",
            "      - Overview: docs/partner-ai/README.md",
            "      - OpenAI AI Foundations: docs/partner-ai/openai-ai-foundations.md",
            "      - Anthropic Claude Certified Architect: docs/partner-ai/anthropic-claude-certified-architect-foundations.md",
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
    vendors_data = read_json(root / "data/vendors.json")
    raw_exams = exams_data.get("exams")
    raw_collections = collections_data.get("collections")
    raw_sources = sources_data.get("sources")
    raw_vendors = vendors_data.get("vendors")
    if not isinstance(raw_exams, list) or not raw_exams:
        raise ValueError("config/exams.json needs a non-empty exams array")
    if not isinstance(raw_sources, list):
        raise ValueError("data/sources.json needs a sources array")
    if not isinstance(raw_collections, list) or not raw_collections:
        raise ValueError("config/collections.json needs a non-empty collections array")
    if not isinstance(raw_vendors, list) or not raw_vendors:
        raise ValueError("data/vendors.json needs a non-empty vendors array")
    exams = [exam for exam in raw_exams if isinstance(exam, dict)]
    if len(exams) != len(raw_exams):
        raise ValueError("Every exam entry must be an object")
    collections = [item for item in raw_collections if isinstance(item, dict)]
    if len(collections) != len(raw_collections):
        raise ValueError("Every collection entry must be an object")
    vendors = [item for item in raw_vendors if isinstance(item, dict)]
    if len(vendors) != len(raw_vendors):
        raise ValueError("Every vendor entry must be an object")
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
        guide_markdown = source.read_text(encoding="utf-8")
        destination.write_text(
            prepare_guide_markdown(guide_markdown, exam), encoding="utf-8"
        )
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
        homepage_template, exams, collections, len(raw_sources), vendors
    )
    (docs_dir / "index.md").write_text(homepage, encoding="utf-8")

    catalog_dir = docs_dir / "exams"
    catalog_dir.mkdir()
    (catalog_dir / "index.md").write_text(
        render_catalog(exams, vendors), encoding="utf-8"
    )
    for vendor_record in visible_vendors(exams, vendors):
        vendor_id = str(vendor_record["id"])
        (catalog_dir / f"{vendor_id}.md").write_text(
            render_vendor_catalog(vendor_record, exams, vendors), encoding="utf-8"
        )

    collections_dir = docs_dir / "collections"
    collections_dir.mkdir()
    (collections_dir / "index.md").write_text(
        render_collections_index(collections, exams_by_code), encoding="utf-8"
    )
    for collection in collections:
        (collections_dir / f"{collection['id']}.md").write_text(
            render_collection_page(collection, exams_by_code, vendors),
            encoding="utf-8",
        )

    assets_source = website_dir / "assets"
    shutil.copytree(assets_source, docs_dir / "assets")

    robots_template = (website_dir / "robots.txt.template").read_text(
        encoding="utf-8"
    )
    (docs_dir / "robots.txt").write_text(robots_template, encoding="utf-8")

    overrides_source = website_dir / "overrides"
    shutil.copytree(overrides_source, build_dir / "overrides")

    config_template = (website_dir / "mkdocs.yml.template").read_text(
        encoding="utf-8"
    )
    config = config_template.replace(
        "{{SITE_NAV}}", render_nav(exams, collections, vendors)
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
