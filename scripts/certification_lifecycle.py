"""Render a dated view of recorded certification lifecycle facts."""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from html import escape
import re


def cell(value: object) -> str:
    text = " ".join(str(value).split())
    return escape(text, quote=False).replace("|", "&#124;").replace("[", "&#91;")


def link(label: str, url: str) -> str:
    return f"[{cell(label)}](<{url}>)"


def natural_key(value: str) -> list[tuple[int, object]]:
    return [(1, int(part)) if part.isdigit() else (0, part.casefold())
            for part in re.split(r"(\d+)", value)]


def render_lifecycle_page(catalog: dict[str, object]) -> str:
    as_of = date.fromisoformat(catalog["lifecycle_as_of"])
    certifications = catalog["certifications"]
    source_dates = {source["id"]: source["last_verified"]
                    for source in catalog["catalog_sources"]}
    ordered = sorted(certifications, key=lambda row: (
        row["vendor_id"], natural_key(row["exam_code"])))
    events = []
    fact_codes = set()
    coverage = defaultdict(lambda: {"total": 0, "with_fact": 0})
    unresolved = defaultdict(list)
    priority_gaps = []
    for row in ordered:
        lifecycle = row.get("lifecycle", {})
        if not isinstance(lifecycle, dict):
            raise ValueError(f"Invalid lifecycle record for {row['exam_code']}")
        has_fact = bool(lifecycle.get("blueprint_updates") or
                        lifecycle.get("initial_release") or
                        row.get("retirement_date"))
        vendor = row["vendor_id"]
        coverage[vendor]["total"] += 1
        if has_fact:
            fact_codes.add((vendor, row["exam_code"]))
            coverage[vendor]["with_fact"] += 1
        else:
            unresolved[vendor].append(row)
            if row["status"] in {"beta", "legacy"}:
                priority_gaps.append(row)
        checked = (lifecycle.get("checked_on") or
                   "Catalog " + source_dates[row["source_id"]])
        identity = link(f"{row['exam_code']} — {row['title']}", row["official_url"])
        for update in lifecycle.get("blueprint_updates", []):
            events.append((update["effective_on"], identity, "Skills measured as of",
                           update["language"], update["source_url"], checked))
        release = lifecycle.get("initial_release")
        if release:
            events.append((release["date"], identity,
                           "Exam/version " + release["stage"].replace("-", " "),
                           release.get("scope", "Scope not specified"),
                           release["source_url"], checked))
        if row.get("retirement_date"):
            change = "Retirement"
            if row.get("replacement_exam_code"):
                change += " → " + link(row["replacement_exam_code"],
                                       row["replacement_official_url"])
            events.append((row["retirement_date"], identity, change,
                           row.get("retirement_scope", "Scope not specified"),
                           row.get("retirement_source_url", row["official_url"]), checked))
    as_of_text = as_of.isoformat()
    future_events = sorted((event for event in events if event[0] > as_of_text),
                           key=lambda event: (event[0], event[1]))
    past_events = sorted((event for event in events if event[0] <= as_of_text),
                         key=lambda event: (event[0], event[1]), reverse=True)
    lines = [
        "# Certification lifecycle and name history", "",
        f"**Dated view: {as_of.isoformat()}.** Of {len(certifications)} research-inventory "
        f"entries, {len(fact_codes)} have a recorded dated lifecycle event; "
        f"{len(certifications) - len(fact_codes)} still need date "
        "research. This is a generated repository snapshot. The published page "
        "changes when the site is deployed; it is not a live vendor feed.", "",
        "The event tables show only source-backed dates. A missing row means this "
        "inventory has no confirmed dated event for that exam; it does not mean "
        "the exam has never changed. The coverage table below shows the research "
        "gap by vendor.", "",
        "For Microsoft Learn study guides, the skills date is transcribed from "
        "the exact English 'Skills measured as of' heading. It does not by itself "
        "prove that the preceding outline changed on that day. A skills date is "
        "different from the date we checked a page. Initial release refers to the "
        "tracked exam version, not necessarily the credential's first launch. "
        "A beta release is different from general availability. A rename does "
        "not by itself create a new exam or replacement. Language-specific "
        "dates are shown with their language code; do not apply them to every "
        "exam delivery. A catalog check date describes an inventory pass, not "
        "a fresh individual lifecycle check.", "",
        "Conflicting sources and unavailable labs remain visible in study-guide "
        "review notes. More research is needed where noted; useful public "
        "information can still be published. Community corrections should include "
        "a public source and the observed/effective date where known. See "
        "[how to contribute](../CONTRIBUTING.md).", "",
    ]
    for title, selected in (("Upcoming dated changes", future_events),
                            ("Effective and past dates", past_events)):
        lines.extend([f"## {title}", ""])
        if not selected:
            lines.extend(["No source-backed dates in this category.", ""])
            continue
        lines.extend(["| Date | Credential / exam | Event | Scope | Source | Checked |",
                      "|---|---|---|---|---|---|"])
        for event_date, identity, change, scope, url, checked in selected:
            lines.append("| " + " | ".join([
                cell(event_date), identity, change, cell(scope),
                link("Official source", url), cell(checked)]) + " |")
        lines.append("")
    lines.extend(["## Coverage and research queue", "",
                  "A recorded event does not establish complete lifecycle history. "
                  "The remaining count identifies exams for which no dated event "
                  "has been recorded in this inventory. Review the official source "
                  "before treating any row as current.", "",
                  "| Vendor | Inventory entries | With a dated event | Date research remaining | Exams needing date research |",
                  "|---|---:|---:|---:|---|"])
    for vendor, counts in sorted(coverage.items()):
        gaps = ", ".join(link(row["exam_code"], row["official_url"])
                         for row in unresolved[vendor]) or "—"
        lines.append(f"| {cell(vendor)} | {counts['total']} | "
                     f"{counts['with_fact']} | {counts['total'] - counts['with_fact']} | "
                     f"{gaps} |")
    lines.extend(["", "### Priority gaps", "",
                  "These beta or legacy inventory entries have no "
                  "confirmed dated lifecycle event yet. Their status is a "
                  "catalog classification, not a release or retirement date.", ""])
    if priority_gaps:
        for row in priority_gaps:
            lines.append(f"- {link(row['exam_code'], row['official_url'])} "
                         f"({cell(row['vendor_id'])}; {cell(row['status'])})")
    else:
        lines.append("No priority-status gaps in the current inventory.")
    lines.extend(["", "## Known name aliases", "",
                  "The current title and each alias refer to the same vendor/exam "
                  "identity. Try each name when searching an LMS, then reconcile "
                  "results by vendor and exam code. An alias may match older "
                  "course content; check its blueprint version before using it.", "",
                  "| Vendor / exam | Current title | Other recorded names |",
                  "|---|---|---|"])
    for row in ordered:
        if row.get("aliases"):
            lines.append("| " + " | ".join([
                cell(f"{row['vendor_id']} / {row['exam_code']}"),
                cell(row["title"]), "<br>".join(map(cell, row["aliases"]))]) + " |")
    lines.extend(["", "## Evidence notes and next-pass work", ""])
    for row in ordered:
        if row.get("lifecycle", {}).get("notes"):
            lines.append(f"- **{cell(row['exam_code'])}:** "
                         + cell(row["lifecycle"]["notes"]))
            sources = row["lifecycle"].get("source_urls", [])
            if sources:
                lines[-1] += " Sources: " + ", ".join(
                    link(f"evidence {index}", url)
                    for index, url in enumerate(sources, 1)) + "."
    lines.extend(["", "AB-100's current name and announced update are confirmed by "
                  "its [credential page](https://learn.microsoft.com/en-us/credentials/"
                  "certifications/agentic-ai-business-solutions-architect/) and "
                  "[study guide](https://learn.microsoft.com/en-us/credentials/"
                  "certifications/resources/study-guides/ab-100). The saved July "
                  "baseline is discussed in the [dated review](research/"
                  "2026-09-27-ab-100-deep-review.md). The former name is preserved "
                  "in the public inventory's history; its exact rename date is "
                  "not inferred from our review date.", "",
                  "Maintain these records in `config/certification-seeds.json`; "
                  "see [inventory maintenance](https://github.com/cterpening/certification-study-library/blob/main/docs/CERTIFICATION-INVENTORY.md#updating-the-inventory). "
                  "Regenerate this page with `python scripts/generate_certification_lifecycle.py`. "
                  "Advance `lifecycle_as_of` deliberately when refreshing the view. "
                  "The date does not claim every inventory entry was individually rechecked.", ""])
    return "\n".join(lines)
