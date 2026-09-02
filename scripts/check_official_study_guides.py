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
AWS_DOMAIN_PATTERN = re.compile(
    r"^Content Domain \d+: .+\(\d+% of scored content\)$", re.IGNORECASE
)
COMPTIA_DETAIL_PREFIXES = (
    "Exam version:",
    "Exam series code:",
    "Launch date:",
    "Retirement:",
    "Number of questions:",
    "Type of questions:",
    "Length of test:",
    "Passing score:",
    "Languages:",
)
RED_HAT_OBJECTIVE_STARTS = ("Study points for the exam", "Exam Objectives")
RED_HAT_OBJECTIVE_ENDS = ("What you need to know", "Readiness")
LINUX_FOUNDATION_OBJECTIVE_START = "Domains & Competencies"
LINUX_FOUNDATION_OBJECTIVE_END = "Exam Details & Resources"


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
        payload = response.read()
        try:
            return payload.decode(charset)
        except UnicodeDecodeError:
            # Some public vendor pages declare UTF-8 while retaining Windows
            # punctuation bytes. Preserve readable objective snapshots rather
            # than silently replacing apostrophes and dashes with U+FFFD.
            for fallback in ("utf-8", "cp1252"):
                if fallback.casefold() == charset.casefold():
                    continue
                try:
                    return payload.decode(fallback)
                except UnicodeDecodeError:
                    continue
            return payload.decode(charset, errors="replace")


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


def extract_aws_objectives(page_html: str) -> str:
    """Extract AWS exam identity, capability summary, and weighted domains."""

    lines = normalize_lines(visible_text(page_html))
    titles = [
        line
        for line in lines
        if line.startswith("AWS Certified ")
        and re.search(r"\([A-Z]{2,4}-[A-Z]\d{2}\)$", line)
    ]
    domains = [line for line in lines if AWS_DOMAIN_PATTERN.match(line)]
    if not titles or len(domains) < 3:
        raise ValueError("Could not find the AWS certification title and domains")
    capability_start = find_first(lines, ("The exam also validates a candidate's ability to complete the following tasks:",))
    capability_end = find_first(lines, ("Target candidate description", "Target Candidate Description"), (capability_start or 0) + 1)
    capabilities = (
        lines[capability_start:capability_end]
        if capability_start is not None and capability_end is not None
        else []
    )
    return "\n".join([titles[0], *capabilities, *domains]).strip() + "\n"


def extract_aws_status(page_html: str) -> dict[str, list[str]]:
    """Capture the AWS exam identity and explicit future lifecycle notices."""

    lines = normalize_lines(visible_text(page_html))
    titles = [
        line
        for line in lines
        if line.startswith("AWS Certified ")
        and re.search(r"\([A-Z]{2,4}-[A-Z]\d{2}\)$", line)
    ]
    if not titles:
        raise ValueError("Could not find the AWS certification title")
    announcements = [
        line
        for line in lines
        if any(pattern.search(line) for pattern in ANNOUNCEMENT_PATTERNS)
        or "registration for the beta" in line.casefold()
        or "last day to take" in line.casefold()
    ]
    return {
        "skills_versions": [titles[0]],
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_comptia_objectives(page_html: str) -> str:
    """Extract public CompTIA exam metadata and weighted objective summary."""

    lines = normalize_lines(visible_text(page_html))
    detail_index = find_exact(lines, "Exam details")
    objective_indexes = [
        index
        for index, line in enumerate(lines)
        if "exam objectives summary" in line.casefold()
        or re.search(r"\(V\d+\) exam objectives$", line, re.IGNORECASE)
    ]
    if detail_index is None or not objective_indexes:
        raise ValueError("Could not find CompTIA exam details and objectives")
    objective_index = objective_indexes[-1]
    details = [
        line
        for line in lines[detail_index + 1 : objective_index]
        if line.casefold().startswith(
            tuple(prefix.casefold() for prefix in COMPTIA_DETAIL_PREFIXES)
        )
    ]
    objectives = lines[objective_index:]
    weighted = [line for line in objectives if re.search(r"\(\d+%\)$", line)]
    if not any(line.startswith("Exam series code:") for line in details) or len(weighted) < 4:
        raise ValueError("Extracted CompTIA objective section was unexpectedly short")
    return "\n".join([*details, *objectives]).strip() + "\n"


def extract_comptia_status(page_html: str) -> dict[str, list[str]]:
    """Capture the CompTIA version, code, launch, and retirement baseline."""

    lines = normalize_lines(visible_text(page_html))
    details = [
        line
        for line in lines
        if line.casefold().startswith(
            tuple(prefix.casefold() for prefix in COMPTIA_DETAIL_PREFIXES)
        )
    ]
    if not any(line.startswith("Exam series code:") for line in details):
        raise ValueError("Could not find the CompTIA exam series code")
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": [
            line for line in details if line.casefold().startswith("retirement:")
        ],
    }


def extract_red_hat_objectives(page_html: str) -> str:
    """Extract the current public performance-task list from a Red Hat exam page."""

    lines = normalize_lines(visible_text(page_html))
    starts = [
        index for index, line in enumerate(lines) if line in RED_HAT_OBJECTIVE_STARTS
    ]
    if not starts:
        raise ValueError("Could not find Red Hat exam objectives")
    start = starts[-1]
    end = find_first(lines, RED_HAT_OBJECTIVE_ENDS, start + 1)
    if end is None:
        raise ValueError("Could not find the end of Red Hat exam objectives")
    versions = [
        line
        for line in lines[:start]
        if line.startswith("This exam is based on")
        or line.startswith("Objectives listed for this exam are based on")
    ]
    selected = [*versions, *lines[start:end]]
    if len(selected) < 12:
        raise ValueError("Extracted Red Hat objective section was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_red_hat_status(page_html: str) -> dict[str, list[str]]:
    """Capture Red Hat product-version baselines and version-selection notices."""

    lines = normalize_lines(visible_text(page_html))
    titles = [line for line in lines if re.search(r"\| EX\d{3}$", line)]
    versions = [
        line
        for line in lines
        if line.startswith("This exam is based on")
        or line.startswith("Objectives listed for this exam are based on")
    ]
    if not titles or not versions:
        raise ValueError("Could not find the Red Hat exam and product baseline")
    announcements = [
        line
        for line in lines
        if any(pattern.search(line) for pattern in ANNOUNCEMENT_PATTERNS)
        or "multiple versions of this exam" in line.casefold()
    ]
    return {
        "skills_versions": [titles[0], *list(dict.fromkeys(versions))],
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_linux_foundation_objectives(page_html: str) -> str:
    """Extract Linux Foundation/CNCF domains and public task competencies."""

    lines = normalize_lines(visible_text(page_html))
    start = find_exact(lines, LINUX_FOUNDATION_OBJECTIVE_START)
    end = find_exact(lines, LINUX_FOUNDATION_OBJECTIVE_END, (start or 0) + 1)
    if start is None or end is None:
        raise ValueError("Could not find Linux Foundation domains and competencies")
    selected = lines[start:end]
    weighted = [line for line in selected if re.search(r"\d+%$", line)]
    if len(weighted) < 5 or len(selected) < 12:
        raise ValueError("Extracted Linux Foundation objectives were unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_linux_foundation_status(page_html: str) -> dict[str, list[str]]:
    """Capture format, duration, software version, validity, and prerequisites."""

    lines = normalize_lines(visible_text(page_html))
    status_markers = (
        "This exam is an online",
        "The exam is based on",
        "Duration of Exam",
        "Certification Valid for",
        "Software Version:",
        "There are no prerequisites",
        "candidates must have taken and passed",
    )
    details = [
        line
        for line in lines
        if line.casefold().startswith(tuple(marker.casefold() for marker in status_markers))
        or any(marker.casefold() in line.casefold() for marker in status_markers[-2:])
    ]
    if not details:
        raise ValueError("Could not find Linux Foundation assessment details")
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": [],
    }


def extract_google_cloud_objectives(page_html: str) -> str:
    """Extract the stable role-level capability list from a certification page."""

    lines = normalize_lines(visible_text(page_html))
    start = next(
        (
            index
            for index, line in enumerate(lines)
            if "assesses your" in line.casefold()
            or line.casefold().endswith("exam assesses")
        ),
        None,
    )
    if start is None:
        raise ValueError("Could not find the Google Cloud capability-list heading")
    end_markers = (
        "Register",
        "View FAQs",
        "Beta coming",
        "About this certification",
        "About this beta certification",
    )
    selected: list[str] = []
    for line in lines[start + 1 :]:
        if any(line.startswith(marker) for marker in end_markers):
            break
        selected.append(line)
    selected = [line for line in selected if line]
    if len(selected) < 4:
        raise ValueError("Google Cloud capability list was unexpectedly short")
    return "\n".join([lines[start], *selected]).strip() + "\n"


def extract_google_cloud_status(page_html: str) -> dict[str, list[str]]:
    """Capture current delivery, lifecycle, beta, and update signals."""

    lines = normalize_lines(visible_text(page_html))
    detail_prefixes = (
        "Length:",
        "Registration fee:",
        "Language:",
        "Languages:",
        "Exam format:",
        "Exam delivery method:",
        "Validity period:",
        "Prerequisites:",
        "Recommended experience:",
    )
    details = [line for line in lines if line.startswith(detail_prefixes)]
    if not details:
        raise ValueError("Could not find Google Cloud certification details")
    announcements = [
        line
        for line in lines
        if "beta coming" in line.casefold()
        or "registration for" in line.casefold()
        or "new version" in line.casefold()
        or "exam was updated" in line.casefold()
        or any(pattern.search(line) for pattern in ANNOUNCEMENT_PATTERNS)
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_cisco_objectives(page_html: str) -> str:
    """Capture Cisco's public exam baseline and preparation scope.

    Cisco publishes detailed blueprints through a JavaScript-rendered Learning
    Network page or a Cisco Public PDF. The stable exam landing page remains a
    useful independent monitor for the live exam/version, high-level scope,
    delivery details, and official preparation route. Detailed PDF objectives
    are still snapshotted and mapped during each guide's source validation.
    """

    lines = [
        line.replace("individual\u2019s", "individual's")
        for line in normalize_lines(visible_text(page_html))
    ]
    start = next(
        (
            index
            for index, line in enumerate(lines)
            if re.match(r"^\d{3}-\d{3}\b", line)
            or line in {"CCNA", "CCNA Automation"}
        ),
        None,
    )
    if start is None:
        raise ValueError("Could not find Cisco exam identity")
    end = find_first(
        lines,
        ("Get the most from your learning journey", "We're here to help"),
        start + 1,
    )
    if end is None:
        end = len(lines)
    selected = lines[start:end]
    if len(selected) < 10:
        raise ValueError("Extracted Cisco exam baseline was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_cisco_status(page_html: str) -> dict[str, list[str]]:
    """Capture version, delivery, lifecycle, and explicit future Cisco signals."""

    lines = normalize_lines(visible_text(page_html))
    labels = {"Languages", "Duration", "Price", "Prerequisites", "Valid for"}
    details: list[str] = []
    for index, line in enumerate(lines):
        if re.search(r"\bv\d+(?:\.\d+)?\b", line, re.IGNORECASE):
            details.append(line)
        if line in labels and index + 1 < len(lines):
            details.append(f"{line}: {lines[index + 1]}")
        if re.match(r"^(Cost|Languages?|Duration|Prerequisites|Valid for):", line):
            details.append(line)
    if not details:
        identity = next(
            (line for line in lines if re.match(r"^\d{3}-\d{3}\b", line)),
            None,
        )
        if identity is None:
            raise ValueError("Could not find Cisco exam status details")
        details.append(identity)
    announcement_markers = (
        "will be updated",
        "will retire",
        "last day of testing",
        "goes live",
        "will be available",
    )
    announcements = [
        line
        for line in lines
        if any(marker in line.casefold() for marker in announcement_markers)
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_snowflake_objectives(page_html: str) -> str:
    """Capture a SnowPro exam page's public scope and candidate baseline."""

    lines = normalize_lines(visible_text(page_html))
    start = next(
        (
            index
            for index, line in enumerate(lines)
            if re.match(r"^(?:SOL|COF|DEA|GES)-C\d{2}$", line)
        ),
        None,
    )
    if start is None:
        raise ValueError("Could not find Snowflake exam identity")
    end = find_first(lines, ("SnowPro FAQs", "Frequently Asked Questions"), start + 1)
    if end is None:
        end = len(lines)
    selected = lines[start:end]
    if len(selected) < 8:
        raise ValueError("Extracted Snowflake certification scope was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_snowflake_status(page_html: str) -> dict[str, list[str]]:
    """Capture SnowPro version, experience, and explicit lifecycle signals."""

    lines = normalize_lines(visible_text(page_html))
    details = [
        line
        for line in lines
        if re.match(r"^(?:SOL|COF|DEA|GES)-C\d{2}$", line)
        or re.search(r"\b(?:months?|years?)\b.*\b(?:experience|knowledge)\b", line, re.I)
    ]
    if not details:
        raise ValueError("Could not find Snowflake certification status details")
    markers = (
        "is retiring",
        "being replaced",
        "will retire",
        "will be retired",
        "launched on",
        "will be launching",
        "will be released",
    )
    announcements = [
        line for line in lines if any(marker in line.casefold() for marker in markers)
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_isc2_objectives(page_html: str) -> str:
    """Capture an ISC2 outline's weighted domains and public subtopics."""

    lines = normalize_lines(visible_text(page_html))
    start = next(
        (
            index
            for index, line in enumerate(lines)
            if "Certification Exam Outline" in line
            or "Certification Exam Outline Summary" in line
        ),
        None,
    )
    if start is None:
        raise ValueError("Could not find ISC2 exam-outline identity")
    about = next(
        (
            index
            for index, line in enumerate(lines[start + 1 :], start + 1)
            if line.startswith("About ")
        ),
        start + 1,
    )
    first_domain = next(
        (
            index
            for index, line in enumerate(lines[about + 1 :], about + 1)
            if line.startswith("Domain 1:")
        ),
        None,
    )
    if first_domain is None:
        raise ValueError("Could not find ISC2 domain details")
    end_markers = (
        "Additional Examination Information",
        "How is AI Security Incorporated",
        "Quick Links",
    )
    end = min(
        (
            index
            for index, line in enumerate(lines[first_domain + 1 :], first_domain + 1)
            if line.startswith(end_markers)
        ),
        default=len(lines),
    )
    selected = [lines[start], *lines[about:end]]
    weighted = [line for line in selected if re.search(r"\b\d+(?:\.\d+)?%$", line)]
    detailed = [line for line in selected if re.match(r"^\d+\.\d+\s+-\s+", line)]
    if len(weighted) < 5 or len(detailed) < 10:
        raise ValueError("Extracted ISC2 outline was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_isc2_status(page_html: str) -> dict[str, list[str]]:
    """Capture the ISC2 effective baseline, delivery, and experience contract."""

    lines = normalize_lines(visible_text(page_html))
    prefixes = (
        "Effective Date:",
        "EFFECTIVE DATE:",
        "Length of exam",
        "Number of items",
        "Item format",
        "Passing grade",
        "Exam language availability",
        "Language availability",
        "Testing center",
    )
    details: list[str] = []
    labels = {prefix.casefold() for prefix in prefixes[2:]}
    for index, line in enumerate(lines):
        if line.startswith(prefixes[:2]):
            details.append(line)
        elif re.match(
            r"^(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER) \d{1,2}, \d{4}$",
            line,
        ):
            details.append(line)
        elif line.casefold() in labels and index + 1 < len(lines):
            details.append(f"{line}: {lines[index + 1]}")
        elif line.startswith(prefixes[2:]):
            details.append(line)
    experience = next(
        (
            line
            for line in lines
            if line.startswith("Candidates must have a minimum")
            or line.startswith("No work experience")
        ),
        None,
    )
    if experience:
        details.append(experience)
    if not details:
        raise ValueError("Could not find ISC2 exam status details")
    announcement_markers = (
        "effective september",
        "will be based on a new",
        "will take effect",
        "will be updated",
        "will retire",
    )
    announcements = [
        line
        for line in lines
        if any(marker in line.casefold() for marker in announcement_markers)
        and not line.startswith(("Effective Date:", "EFFECTIVE DATE:"))
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_nvidia_objectives(page_html: str) -> str:
    """Capture an NVIDIA certification's public weighted blueprint."""

    lines = normalize_lines(visible_text(page_html))
    code_index = next(
        (
            index
            for index, line in enumerate(lines)
            if re.match(r"^\(NC(?:A|P)-[A-Z0-9]+\)$", line)
        ),
        None,
    )
    if code_index is None or code_index < 2:
        raise ValueError("Could not find NVIDIA certification identity")
    blueprint = next(
        (
            index
            for index, line in enumerate(lines[code_index + 1 :], code_index + 1)
            if line == "Exam Blueprint"
            and any(
                "table below" in candidate.casefold()
                for candidate in lines[index + 1 : index + 5]
            )
        ),
        None,
    )
    if blueprint is None:
        raise ValueError("Could not find NVIDIA exam blueprint")
    end = next(
        (
            index
            for index, line in enumerate(lines[blueprint + 1 :], blueprint + 1)
            if line in {"Get Certified", "Contact Us", "Stay Informed"}
        ),
        len(lines),
    )
    selected = [*lines[code_index - 2 : code_index + 1], *lines[blueprint:end]]
    weights = [line for line in selected if re.fullmatch(r"\d+%", line)]
    if len(weights) < 3:
        raise ValueError("Extracted NVIDIA blueprint was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_nvidia_status(page_html: str) -> dict[str, list[str]]:
    """Capture NVIDIA exam delivery, prerequisites, validity, and lifecycle."""

    lines = normalize_lines(visible_text(page_html))
    prefixes = (
        "Duration:",
        "Price:",
        "Certification level:",
        "Subject:",
        "Number of questions:",
        "Hands-on lab:",
        "Scoring:",
        "Prerequisites:",
        "Language:",
        "Validity:",
    )
    details = [line for line in lines if line.startswith(prefixes)]
    code = next(
        (line for line in lines if re.match(r"^\(NC(?:A|P)-[A-Z0-9]+\)$", line)),
        None,
    )
    if code:
        details.insert(0, code.strip("()"))
    if len(details) < 6:
        raise ValueError("Could not find NVIDIA exam status details")
    announcements = [
        line
        for line in lines
        if "coming soon" in line.casefold()
        or "will retire" in line.casefold()
        or "will be retired" in line.casefold()
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_salesforce_objectives(page_html: str) -> str:
    """Capture weighted objectives from Salesforce Help or Trailhead prep."""

    lines = normalize_lines(visible_text(page_html))
    start = next(
        (
            index
            for index, line in enumerate(lines)
            if line in {"Exam Outline", "This exam covers these key topics, each making up a certain percentage of the exam."}
        ),
        None,
    )
    if start is None:
        raise ValueError("Could not find Salesforce exam objectives")
    end_markers = {
        "Preparing for the Exam",
        "Recommended Training and Resources",
        "Exam Logistics and Policies",
    }
    end = next(
        (
            index
            for index, line in enumerate(lines[start + 1 :], start + 1)
            if line in end_markers
        ),
        len(lines),
    )
    selected = lines[start:end]
    weights = [line for line in selected if re.search(r"\b\d+%$", line)]
    if len(weights) < 4:
        raise ValueError("Extracted Salesforce blueprint was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_salesforce_status(page_html: str) -> dict[str, list[str]]:
    """Capture Salesforce exam delivery, release, and maintenance signals."""

    lines = normalize_lines(visible_text(page_html))
    prefixes = (
        "Content:",
        "Time allotted",
        "Passing score:",
        "Version:",
        "Registration fee:",
        "Retake fee:",
        "Delivery options:",
        "References:",
        "Prerequisite:",
        "Language offerings:",
    )
    details = [line for line in lines if line.startswith(prefixes)]
    maintenance = next(
        (
            line
            for line in lines
            if "maintenance modules" in line.casefold()
            or "maintenance module" in line.casefold()
        ),
        None,
    )
    if maintenance:
        details.append(maintenance)
    if not details:
        raise ValueError("Could not find Salesforce exam status details")
    announcement_markers = (
        "will retire",
        "retiring",
        "will be updated",
        "effective",
    )
    announcements = [
        line
        for line in lines
        if any(marker in line.casefold() for marker in announcement_markers)
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_mongodb_objectives(page_html: str) -> str:
    """Capture MongoDB's public exam identity and any exposed domain/objective lines.

    MongoDB publishes exam contracts on public landing pages while the detailed
    30-minute study guides use free enrollment. Preserve exposed sections when
    available and otherwise monitor the exact study-guide identity rather than
    attempting to cross an authentication boundary.
    """

    lines = normalize_lines(visible_text(page_html))
    selected = [
        line
        for line in lines
        if re.search(r"\b(?:domain|section|objective)\s+\d+", line, re.I)
        or "Exam Study Guide" in line
        or "Exam Guide" in line
        or line.startswith("MongoDB Associate")
    ]
    selected = list(dict.fromkeys(selected))
    if not selected:
        raise ValueError("Could not find MongoDB study-guide identity or objectives")
    return "\n".join(selected).strip() + "\n"


def extract_mongodb_status(page_html: str) -> dict[str, list[str]]:
    """Capture public MongoDB exam-contract and lifecycle signals."""

    lines = normalize_lines(visible_text(page_html))
    labels = {
        "TEST FORMAT",
        "ITEM FORMAT",
        "DELIVERY FORMAT",
        "TIME ALLOTTED",
        "PREREQUISITES",
        "COST",
        "EXAM PRICE",
        "LANGUAGE",
        "EXAM AVAILABLE",
    }
    details: list[str] = []
    for index, line in enumerate(lines):
        if line.upper() in labels:
            details.append(line)
            if index + 1 < len(lines):
                details.append(lines[index + 1])
    if not details:
        details = [line for line in lines if "30 Minutes" in line or line == "FREE"]
    if not details:
        raise ValueError("Could not find MongoDB exam status details")
    announcements = [
        line
        for line in lines
        if any(
            marker in line.casefold()
            for marker in ("will retire", "retiring", "updated learning path", "available beginning")
        )
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


def extract_servicenow_objectives(page_html: str) -> str:
    """Capture the weighted scope from a public ServiceNow mainline blueprint."""

    lines = normalize_lines(visible_text(page_html))
    start = next(
        (index for index, line in enumerate(lines) if line == "Exam Scope"),
        None,
    )
    if start is None:
        raise ValueError("Could not find ServiceNow Exam Scope")
    end = next(
        (
            index
            for index in range(start + 1, len(lines))
            if lines[index] in {"Exam Registration", "Exam Structure"}
        ),
        len(lines),
    )
    selected = lines[start:end]
    weights = [line for line in selected if re.fullmatch(r"\d+(?:\.\d+)?%", line)]
    if len(weights) < 4:
        raise ValueError("Extracted ServiceNow blueprint was unexpectedly short")
    return "\n".join(selected).strip() + "\n"


def extract_servicenow_status(page_html: str) -> dict[str, list[str]]:
    """Capture ServiceNow revision, delivery, scoring, and maintenance signals."""

    lines = normalize_lines(visible_text(page_html))
    details = [
        line
        for line in lines
        if line.startswith("Updated ")
        or line.startswith("The exam duration is ")
        or line.startswith("The exam consists of ")
        or "Pearson test center" in line
        or "cut score" in line.casefold()
        or "maintenance exams" in line.casefold()
        or "Certification Maintenance Program" in line
        or "90 days" in line
    ]
    if not details:
        raise ValueError("Could not find ServiceNow exam status details")
    announcements = [
        line
        for line in lines
        if any(
            marker in line.casefold()
            for marker in ("will retire", "retiring", "effective", "available from")
        )
    ]
    return {
        "skills_versions": list(dict.fromkeys(details)),
        "upcoming_announcements": list(dict.fromkeys(announcements)),
    }


OBJECTIVE_ADAPTERS = {
    "microsoft-learn": (extract_skills_section, extract_exam_status),
    "hashicorp-developer": (extract_hashicorp_objectives, extract_hashicorp_status),
    "databricks-certification": (
        extract_databricks_objectives,
        extract_databricks_status,
    ),
    "aws-exam-guide": (extract_aws_objectives, extract_aws_status),
    "comptia-certification": (extract_comptia_objectives, extract_comptia_status),
    "red-hat-exam": (extract_red_hat_objectives, extract_red_hat_status),
    "linux-foundation-certification": (
        extract_linux_foundation_objectives,
        extract_linux_foundation_status,
    ),
    "google-cloud-certification": (
        extract_google_cloud_objectives,
        extract_google_cloud_status,
    ),
    "cisco-certification": (extract_cisco_objectives, extract_cisco_status),
    "snowflake-certification": (
        extract_snowflake_objectives,
        extract_snowflake_status,
    ),
    "isc2-certification": (extract_isc2_objectives, extract_isc2_status),
    "nvidia-certification": (extract_nvidia_objectives, extract_nvidia_status),
    "salesforce-certification": (
        extract_salesforce_objectives,
        extract_salesforce_status,
    ),
    "mongodb-certification": (
        extract_mongodb_objectives,
        extract_mongodb_status,
    ),
    "servicenow-certification": (
        extract_servicenow_objectives,
        extract_servicenow_status,
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
        # A retired exam's last verified baseline is intentionally frozen. Its
        # former landing page may disappear, so lifecycle/reference links are
        # checked by the source-health workflow instead of this live-objective
        # monitor.
        if exam.get("status") == "retired":
            continue
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
