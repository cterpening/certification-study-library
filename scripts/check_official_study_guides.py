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
HASHICORP_BLUEPRINTS = (
    {
        "title": "Exam Content List - Terraform Authoring and Operations Pro",
        "start": ("Exam objective and sub-topics",),
        "end": ("Cloud provider study resources",),
    },
    {
        "title": "Exam content list - Vault Associate (003)",
        "start": ("Objective ID",),
        "end": ("* API was added to objective", "Continue studying"),
    },
    {
        "title": "Exam content list - Vault Operations Professional",
        "start": ("Exam Objective",),
        "end": ("Sign up for the exam here!",),
    },
)
DATABRICKS_OBJECTIVE_STARTS = ("The exam covers:", "This exam covers:")
DATABRICKS_OBJECTIVE_END = "Assessment Details"


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
        # Newly launched Microsoft exams sometimes publish an undated
        # "Skills measured" section. Keep the page-update date as freshness
        # evidence without misrepresenting it as the exam's effective date.
        skills_heading = find_exact(lines, "Skills measured")
        updated_heading = find_exact(lines, "Last updated on")
        updated_value = (
            lines[updated_heading + 1]
            if updated_heading is not None and updated_heading + 1 < len(lines)
            else ""
        )
        if skills_heading is not None and re.fullmatch(
            r"\d{4}-\d{2}-\d{2}", updated_value
        ):
            skills_versions.append(
                "Skills measured (official page last updated "
                f"{updated_value}; no skills effective date published)"
            )
        else:
            raise ValueError("Could not find an official skills-version label")
    return {
        "skills_versions": skills_versions,
        "upcoming_announcements": announcements,
    }


def extract_hashicorp_objectives(page_html: str) -> str:
    """Extract a supported HashiCorp certification objective table."""

    lines = normalize_lines(visible_text(page_html))
    title = find_first(lines, (HASHICORP_ASSOCIATE_TITLE,))
    if title is not None:
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
    else:
        selected = []
        for blueprint in HASHICORP_BLUEPRINTS:
            title_index = find_exact(lines, str(blueprint["title"]))
            if title_index is None:
                continue
            start = find_first(lines, blueprint["start"], title_index + 1)
            if start is None:
                raise ValueError("Could not find HashiCorp exam objectives")
            end = find_first(lines, blueprint["end"], start + 1)
            if end is None:
                raise ValueError(
                    "Could not find the end of HashiCorp exam objectives"
                )
            selected = [str(blueprint["title"]), *lines[start:end]]
            break
        if not selected:
            raise ValueError("Could not find a supported HashiCorp exam section")
    if len(selected) < 20:
        raise ValueError("Extracted HashiCorp objective section was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_hashicorp_status(page_html: str) -> dict[str, list[str]]:
    """Capture a HashiCorp baseline and explicit future announcements."""

    lines = normalize_lines(visible_text(page_html))
    title = find_first(lines, (HASHICORP_ASSOCIATE_TITLE,))
    if title is not None:
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
    else:
        title_index = None
        version_label = ""
        for blueprint in HASHICORP_BLUEPRINTS:
            title_index = find_exact(lines, str(blueprint["title"]))
            if title_index is not None:
                version_label = str(blueprint["title"])
                break
        if title_index is None:
            raise ValueError("Could not find a supported HashiCorp exam section")
        section = lines[title_index:]
    announcements = [
        line
        for line in section
        if any(pattern.search(line) for pattern in ANNOUNCEMENT_PATTERNS)
        or "expected launch" in line.casefold()
    ]
    return {
        "skills_versions": [version_label],
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def databricks_exam_title(lines: list[str], before: int) -> str:
    """Return the closest Databricks credential title before a section."""

    candidates = [
        line
        for line in lines[:before]
        if line.startswith("Databricks Certified")
        and "Image:" not in line
        and len(line) < 140
    ]
    if not candidates:
        raise ValueError("Could not find the Databricks certification title")
    return candidates[-1]


def databricks_objective_start(lines: list[str]) -> int | None:
    """Return the first supported Databricks weighted-coverage heading."""

    starts = [
        index
        for marker in DATABRICKS_OBJECTIVE_STARTS
        if (index := find_exact(lines, marker)) is not None
    ]
    return min(starts) if starts else None


def extract_databricks_objectives(page_html: str) -> str:
    """Extract the weighted coverage map from a Databricks exam page."""

    lines = normalize_lines(visible_text(page_html))
    start = databricks_objective_start(lines)
    if start is None:
        raise ValueError("Could not find the Databricks exam coverage section")
    end = find_exact(lines, DATABRICKS_OBJECTIVE_END, start + 1)
    if end is None:
        raise ValueError("Could not find the end of Databricks exam coverage")
    selected = [databricks_exam_title(lines, start), *lines[start:end]]
    if len(selected) < 5 or not any("%" in line for line in selected):
        raise ValueError("Extracted Databricks objective section was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_databricks_status(page_html: str) -> dict[str, list[str]]:
    """Capture public Databricks assessment details and future notices."""

    lines = normalize_lines(visible_text(page_html))
    start = databricks_objective_start(lines)
    if start is None:
        raise ValueError("Could not find the Databricks exam coverage section")
    assessment = find_exact(lines, DATABRICKS_OBJECTIVE_END, start + 1)
    ready = find_exact(lines, "Getting Ready for the Exam", (assessment or start) + 1)
    if assessment is None or ready is None:
        raise ValueError("Could not find Databricks assessment details")
    title = databricks_exam_title(lines, start)
    detail_prefixes = (
        "Type:",
        "Total number of scored questions:",
        "Time limit:",
        "Question types:",
        "Languages:",
        "Delivery method:",
        "Recommended experience:",
        "Validity period:",
    )
    details = [
        line
        for line in lines[assessment + 1 : ready]
        if line.casefold().startswith(tuple(item.casefold() for item in detail_prefixes))
    ]
    if len(details) < 4:
        raise ValueError("Databricks assessment details were unexpectedly short")
    section = lines[start:ready]
    announcements = [
        line
        for line in section
        if any(pattern.search(line) for pattern in ANNOUNCEMENT_PATTERNS)
        or "exam will change" in line.casefold()
        or "exam starting on" in line.casefold()
    ]
    return {
        "skills_versions": [f"{title} — public certification page", *details],
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


OBJECTIVE_ADAPTERS = {
    "microsoft-learn": (extract_skills_section, extract_exam_status),
    "hashicorp-developer": (extract_hashicorp_objectives, extract_hashicorp_status),
    "databricks-certification": (
        extract_databricks_objectives,
        extract_databricks_status,
    ),
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
