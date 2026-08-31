#!/usr/bin/env python3
"""Monitor supported public certification objective pages for changes.

This script uses only the Python standard library. It downloads each configured
objective page, selects the vendor adapter registered in ``data/vendors.json``,
extracts the objective section plus any announced update or retirement, and
compares both with committed snapshots. With --write it updates changed snapshots
and emits a machine-readable report for GitHub Actions.
"""

from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


USER_AGENT = "certification-study-library-objective-monitor/1.0"
START_MARKERS = ("Skills measured as of", "Skills at a glance")
END_MARKERS = ("Study resources", "Change log", "Additional resources")
SKILLS_VERSION_PATTERN = re.compile(
    r"\bskills (?:measured|at a glance) "
    r"(?:as of|prior to|from|starting)\b",
    re.IGNORECASE,
)
ANNOUNCEMENT_PATTERNS = (
    re.compile(r"\bthis exam will (?:be updated|retire|be retired)\b", re.IGNORECASE),
    re.compile(
        r"\bthe English language version of this exam will be updated\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\bchanges? .{0,80} will (?:take effect|be effective)\b",
        re.IGNORECASE,
    ),
)
HASHICORP_ASSOCIATE_TITLE = "Terraform Associate (004)"
HASHICORP_OBJECTIVE_END_MARKERS = (
    "Content differences between the 003 and 004 exams",
    "Renewing your certification",
)


class VisibleTextParser(HTMLParser):
    """Collect visible text while omitting script, style, and SVG content."""

    BLOCK_TAGS = {
        "article", "br", "div", "h1", "h2", "h3", "h4", "h5", "h6",
        "li", "main", "p", "section", "table", "td", "th", "tr", "ul", "ol"
    }
    OMIT_TAGS = {"script", "style", "svg", "noscript"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.omit_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.OMIT_TAGS:
            self.omit_depth += 1
        elif not self.omit_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.OMIT_TAGS and self.omit_depth:
            self.omit_depth -= 1
        elif not self.omit_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.omit_depth:
            self.parts.append(data)

    def text(self) -> str:
        return "".join(self.parts)


def fetch(url: str, timeout: int = 45) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def visible_text(page_html: str) -> str:
    parser = VisibleTextParser()
    parser.feed(page_html)
    return html.unescape(parser.text())


def normalize_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.replace("\u00a0", " ").splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if not line:
            continue
        if lines and lines[-1] == line:
            continue
        lines.append(line)
    return lines


def find_first(lines: list[str], markers: Iterable[str], start: int = 0) -> int | None:
    for index in range(start, len(lines)):
        if any(marker.casefold() in lines[index].casefold() for marker in markers):
            return index
    return None


def find_exact(lines: list[str], marker: str, start: int = 0) -> int | None:
    for index in range(start, len(lines)):
        if lines[index].casefold() == marker.casefold():
            return index
    return None


def extract_skills_section(page_html: str) -> str:
    lines = normalize_lines(visible_text(page_html))
    start = find_first(lines, START_MARKERS)
    if start is None:
        raise ValueError("Could not find a skills-measured section")
    end = find_first(lines, END_MARKERS, start + 1)
    if end is None:
        end = len(lines)
    selected = lines[start:end]
    if len(selected) < 10:
        raise ValueError("Extracted objective section was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_exam_status(page_html: str) -> dict[str, list[str]]:
    """Capture baseline labels and explicit future update/retirement notices."""
    lines = normalize_lines(visible_text(page_html))
    skills_versions: list[str] = []
    announcements: list[str] = []
    for line in lines:
        if SKILLS_VERSION_PATTERN.search(line):
            if line not in skills_versions:
                skills_versions.append(line)
        if any(pattern.search(line) for pattern in ANNOUNCEMENT_PATTERNS):
            if line not in announcements:
                announcements.append(line)
    if not skills_versions:
        raise ValueError("Could not find an official skills-version label")
    return {
        "skills_versions": skills_versions,
        "upcoming_announcements": announcements,
    }


def extract_hashicorp_objectives(page_html: str) -> str:
    """Extract the current Terraform Associate objective table."""

    lines = normalize_lines(visible_text(page_html))
    title = find_first(lines, (HASHICORP_ASSOCIATE_TITLE,))
    if title is None:
        raise ValueError("Could not find the Terraform Associate (004) section")
    start = find_exact(lines, "Exam objectives", title + 1)
    if start is None:
        raise ValueError("Could not find HashiCorp exam objectives")
    end = find_first(lines, HASHICORP_OBJECTIVE_END_MARKERS, start + 1)
    if end is None:
        raise ValueError("Could not find the end of HashiCorp exam objectives")
    selected = [HASHICORP_ASSOCIATE_TITLE]
    product_version = find_first(lines, ("Product version tested:",), title + 1)
    if product_version is not None and product_version < start:
        selected.append(
            re.sub(r"tested:\s*", "tested: ", lines[product_version], flags=re.I)
        )
    selected.extend(lines[start:end])
    if len(selected) < 30:
        raise ValueError("Extracted HashiCorp objective section was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_hashicorp_status(page_html: str) -> dict[str, list[str]]:
    """Capture the HashiCorp exam version and explicit future announcements."""

    lines = normalize_lines(visible_text(page_html))
    title = find_first(lines, (HASHICORP_ASSOCIATE_TITLE,))
    if title is None:
        raise ValueError("Could not find the Terraform Associate (004) section")
    product_version = find_first(lines, ("Product version tested:",), title + 1)
    if product_version is None:
        raise ValueError("Could not find the tested Terraform version")
    product_label = re.sub(
        r"tested:\s*", "tested: ", lines[product_version], flags=re.I
    )
    version_label = f"{HASHICORP_ASSOCIATE_TITLE} - {product_label}"
    section_end = find_first(
        lines, ("Terraform Authoring and Operations Professional",), title + 1
    )
    section = lines[title:section_end] if section_end is not None else lines[title:]
    announcements = [
        line
        for line in section
        if any(pattern.search(line) for pattern in ANNOUNCEMENT_PATTERNS)
    ]
    return {
        "skills_versions": [version_label],
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


OBJECTIVE_ADAPTERS = {
    "microsoft-learn": (extract_skills_section, extract_exam_status),
    "hashicorp-developer": (extract_hashicorp_objectives, extract_hashicorp_status),
}


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_config(path: Path, vendor_path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    vendor_data = json.loads(vendor_path.read_text(encoding="utf-8"))
    exams = data.get("exams")
    vendors = vendor_data.get("vendors")
    if not isinstance(exams, list) or not exams:
        raise ValueError("Config must contain a non-empty exams array")
    if not isinstance(vendors, list) or not vendors:
        raise ValueError("Vendor config must contain a non-empty vendors array")
    adapters = {
        str(vendor["id"]): str(vendor["objective_adapter"])
        for vendor in vendors
        if isinstance(vendor, dict)
        and vendor.get("id")
        and vendor.get("objective_adapter")
    }
    required = {"code", "vendor_id", "title", "study_guide_url", "guide_path"}
    for exam in exams:
        missing = required.difference(exam)
        if missing:
            raise ValueError(f"Exam entry missing: {', '.join(sorted(missing))}")
        adapter = adapters.get(str(exam["vendor_id"]))
        if adapter not in OBJECTIVE_ADAPTERS:
            raise ValueError(
                f"Exam {exam['code']} has unsupported objective adapter: {adapter}"
            )
        exam["objective_adapter"] = adapter
    return exams


def snapshot_path(snapshot_dir: Path, code: str) -> Path:
    return snapshot_dir / f"{code.lower()}-official-objectives.txt"


def status_snapshot_path(snapshot_dir: Path, code: str) -> Path:
    return snapshot_dir / f"{code.lower()}-official-status.json"


def monitor(
    config: Path,
    snapshot_dir: Path,
    write: bool,
    vendor_config: Path = Path("data/vendors.json"),
) -> dict[str, object]:
    results: list[dict[str, object]] = []
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    for exam in load_config(config, vendor_config):
        code = exam["code"]
        path = snapshot_path(snapshot_dir, code)
        status_path = status_snapshot_path(snapshot_dir, code)
        result: dict[str, object] = {
            "code": code,
            "title": exam["title"],
            "url": exam["study_guide_url"],
            "guide_path": exam["guide_path"],
            "snapshot_path": str(path),
            "status_snapshot_path": str(status_path),
        }
        try:
            page_html = fetch(exam["study_guide_url"])
            extract_objectives, extract_status = OBJECTIVE_ADAPTERS[
                exam["objective_adapter"]
            ]
            current = extract_objectives(page_html)
            current_status = extract_status(page_html)
            current_status_text = (
                json.dumps(current_status, indent=2, ensure_ascii=False, sort_keys=True)
                + "\n"
            )
            previous = path.read_text(encoding="utf-8") if path.exists() else None
            previous_status = (
                status_path.read_text(encoding="utf-8")
                if status_path.exists()
                else None
            )
            result["previous_sha256"] = digest(previous) if previous is not None else None
            result["current_sha256"] = digest(current)
            result["previous_status_sha256"] = (
                digest(previous_status) if previous_status is not None else None
            )
            result["current_status_sha256"] = digest(current_status_text)
            result["official_status"] = current_status
            result["objectives_changed"] = previous != current
            result["status_changed"] = previous_status != current_status_text
            result["changed"] = bool(
                result["objectives_changed"] or result["status_changed"]
            )
            result["status"] = "changed" if result["changed"] else "unchanged"
            if write and result["objectives_changed"]:
                path.write_text(current, encoding="utf-8", newline="\n")
                result["objectives_written"] = True
            if write and result["status_changed"]:
                status_path.write_text(
                    current_status_text, encoding="utf-8", newline="\n"
                )
                result["status_written"] = True
            if write and result["changed"]:
                result["written"] = True
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            result["status"] = "error"
            result["changed"] = False
            result["error"] = f"{type(exc).__name__}: {exc}"
        results.append(result)
    return {
        "changed": [item["code"] for item in results if item["status"] == "changed"],
        "errors": [item["code"] for item in results if item["status"] == "error"],
        "results": results,
    }


def write_github_outputs(report: dict[str, object], path: Path) -> None:
    changed = report["changed"]
    errors = report["errors"]
    with path.open("a", encoding="utf-8") as output:
        output.write(f"changed={'true' if changed else 'false'}\n")
        output.write(f"changed_exams={','.join(changed)}\n")
        output.write(f"errors={'true' if errors else 'false'}\n")
        output.write(f"error_exams={','.join(errors)}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path("config/exams.json"))
    parser.add_argument(
        "--vendor-config", type=Path, default=Path("data/vendors.json")
    )
    parser.add_argument(
        "--snapshot-dir", type=Path, default=Path("data/objective-snapshots")
    )
    parser.add_argument("--report", type=Path, default=Path("objective-report.json"))
    parser.add_argument("--github-output", type=Path)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = monitor(args.config, args.snapshot_dir, args.write, args.vendor_config)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if args.github_output:
        write_github_outputs(report, args.github_output)
    print(json.dumps(report, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
