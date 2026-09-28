#!/usr/bin/env python3
"""Keep the shared learning catalog aligned with reviewed guide resource sections."""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = "docs/LEARNING-RESOURCES.md"


def section_span(text: str, heading: str, level: int) -> tuple[int, int, int]:
    matches = list(re.finditer(heading, text, re.MULTILINE))
    if len(matches) != 1:
        raise ValueError(f"Expected one section matching {heading!r}; found {len(matches)}")
    match = matches[0]
    following = re.search(r"^#{1," + str(level) + r"} \S", text[match.end():], re.MULTILINE)
    end = match.end() + following.start() if following else len(text)
    return match.start(), match.end(), end


def resource_body(guide: str, guide_path: str) -> str:
    _, start, end = section_span(guide, r"^## Places to learn[ \t]*$", 2)
    body = guide[start:end].strip()
    # Section dividers belong to the guide, not the catalog's next entry.
    body = re.sub(r"\n---\s*$", "", body).rstrip()
    if not body:
        raise ValueError(f"Empty resource section: {guide_path}")

    def rebase(match: re.Match) -> str:
        target = match.group(1)
        if urlsplit(target).scheme or target.startswith(("//", "/")):
            return match.group(0)
        if re.search(r"\s|[<>]", target):
            raise ValueError(f"Review complex local Markdown link manually: {target}")
        local, mark, fragment = target.partition("#")
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(guide_path), local)) if local else guide_path
        rebased = posixpath.relpath(resolved, posixpath.dirname(CATALOG))
        return "](" + rebased + (mark + fragment if mark else "") + ")"

    body = re.sub(r"\]\(([^)]+)\)", rebase, body)
    body = re.sub(r"^(#{3,5}) ", r"#\1 ", body, flags=re.MULTILINE)
    return body


def replace_catalog_entry(catalog: str, exam: dict, guide: str) -> str:
    code = exam["code"]
    heading = r"^### .*?(?<![\w-])" + re.escape(code) + r"(?![\w-]).*$"
    matches = list(re.finditer(heading, catalog, re.MULTILINE))
    if len(matches) > 1:
        raise ValueError(f"Ambiguous catalog entry for {code}")
    body = resource_body(guide, exam["guide_path"])
    source = f"Resource details from the [{code} guide](../{exam['guide_path']}#places-to-learn). Dates, access limitations and estimates below have the same scope as that guide."
    if matches:
        start, body_start, end = section_span(catalog, heading, 3)
        title = catalog[start:body_start]
        return catalog[:start] + title + "\n\n" + source + "\n\n" + body + "\n\n" + catalog[end:]
    _, _, end = section_span(catalog, r"^## Selected resources by exam[ \t]*$", 2)
    entry = f"### {code} — {exam['title']}\n\n{source}\n\n{body}\n\n"
    return catalog[:end].rstrip() + "\n\n" + entry + catalog[end:]


def prepare_catalog(root: Path, codes: list[str] | None, today: date) -> tuple[str, list[str]]:
    exams = {e["code"]: e for e in json.loads((root / "config/exams.json").read_text(encoding="utf-8"))["exams"]}
    if codes is None:
        reviews = json.loads((root / "data/deep-reviews.json").read_text(encoding="utf-8"))["reviews"]
        latest = {}
        for record in sorted(reviews, key=lambda r: r["reviewed_on"], reverse=True):
            if date.fromisoformat(record["reviewed_on"]) <= today:
                latest.setdefault(record["exam_code"], record)
        codes = []
        for code, record in latest.items():
            guide = (root / exams[code]["guide_path"]).read_text(encoding="utf-8")
            if hashlib.sha256(guide.encode("utf-8")).hexdigest() == record["guide_sha256"]:
                codes.append(code)
    unknown = set(codes) - exams.keys()
    if unknown:
        raise ValueError(f"Unknown exam codes: {sorted(unknown)}")
    catalog = (root / CATALOG).read_text(encoding="utf-8")
    selected = sorted(set(codes))
    for code in selected:
        exam = exams[code]
        guide = (root / exam["guide_path"]).read_text(encoding="utf-8")
        catalog = replace_catalog_entry(catalog, exam, guide)
    return catalog, selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--exam-code", action="append", help="Refresh an explicitly selected guide, including work in progress")
    scope.add_argument("--reviewed", action="store_true", help="Only receipts whose date and guide hash match current reviewed content")
    parser.add_argument("--write", action="store_true", help="Write the catalog; default is a read-only drift check")
    args = parser.parse_args()
    try:
        result, codes = prepare_catalog(ROOT, args.exam_code, date.today())
    except (ValueError, KeyError) as exc:
        parser.error(str(exc))
    path = ROOT / CATALOG
    changed = result != path.read_text(encoding="utf-8")
    if args.write and changed:
        path.write_text(result, encoding="utf-8")
    print(json.dumps({"exams": codes, "catalog_changed": changed, "written": changed and args.write}))
    return 1 if changed and not args.write else 0


if __name__ == "__main__":
    raise SystemExit(main())
