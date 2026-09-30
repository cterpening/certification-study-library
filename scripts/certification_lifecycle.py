"""Render a dated view of recorded certification lifecycle facts."""
from __future__ import annotations

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
    lines = [
        "# Certification lifecycle and name history", "",
        f"**Dated view: {as_of.isoformat()}.** This page covers "
        f"{len(certifications)} research-inventory entries, including credentials "
        "that do not yet have a published study guide.", "",
        "Use this page to track recorded exam updates, announced changes, releases, "
        "retirements, replacements and former names. **Not recorded** means that "
        "this inventory does not contain a confirmed value; it does not mean "
        "that no change exists. Dates and known gaps will be filled on later passes.", "",
        "An effective blueprint date is different from the date we checked a "
        "page. Initial release refers to the tracked exam version, not necessarily "
        "the credential's first launch. A beta release is different from general availability. A rename "
        "does not by itself create a new exam or replacement. Language-specific "
        "dates are shown with their language code; do not apply them to every "
        "exam delivery.", "",
        "Latest and next updates are selected per language relative to the dated "
        "view above, not the reader's current date. Multiple announced dates for "
        "one language retain the earliest upcoming date here. Follow the source "
        "and study guide for later changes. Retirement and replacement fields "
        "come from the existing source-backed inventory. A catalog check date "
        "describes that inventory pass, not a fresh individual lifecycle check.", "",
        "Conflicting sources and unavailable labs remain visible in study-guide "
        "review notes. More research is needed where noted; useful public "
        "information can still be published. Community corrections should include "
        "a public source and the observed/effective date where known. See "
        "[how to contribute](../CONTRIBUTING.md).", "",
        "## Dates and replacements", "",
        "| Credential / exam | Latest recorded update | Next recorded update | "
        "Exam/version release | Retirement | Replacement | Checked |",
        "|---|---|---|---|---|---|---|",
    ]
    ordered = sorted(certifications, key=lambda row: (
        row["vendor_id"], natural_key(row["exam_code"])))
    for row in ordered:
        lifecycle = row.get("lifecycle", {})
        if not isinstance(lifecycle, dict):
            raise ValueError(f"Invalid lifecycle record for {row['exam_code']}")
        by_language: dict[str, list[dict[str, str]]] = {}
        for update in lifecycle.get("blueprint_updates", []):
            by_language.setdefault(update["language"], []).append(update)
        past, future = [], []
        for language, updates in sorted(by_language.items()):
            updates = sorted(updates, key=lambda update: update["effective_on"])
            effective = [u for u in updates
                         if date.fromisoformat(u["effective_on"]) <= as_of]
            upcoming = [u for u in updates
                        if date.fromisoformat(u["effective_on"]) > as_of]
            for destination, selected in (
                (past, effective[-1:] or []), (future, upcoming[:1])):
                for update in selected:
                    destination.append(link(
                        f"{update['effective_on']} ({language})",
                        update["source_url"]))
        release = lifecycle.get("initial_release")
        initial = (link(f"{release['date']} ({release['stage']})",
                        release["source_url"]) if release else "Not recorded")
        retirement_label = row.get("retirement_date", "")
        if row.get("retirement_scope"):
            retirement_label += f" ({row['retirement_scope']})"
        retirement = (link(retirement_label, row.get("retirement_source_url", row["official_url"]))
                      if row.get("retirement_date") else "Not recorded")
        replacement = (link(row["replacement_exam_code"],
                            row["replacement_official_url"])
                       if row.get("replacement_exam_code") else "Not recorded")
        checked = (lifecycle["checked_on"] if lifecycle.get("checked_on")
                   else "Catalog " + source_dates[row["source_id"]])
        identity = (link(f"{row['exam_code']} — {row['title']}", row["official_url"])
                    + f"<br>{cell(row['vendor_id'])}; inventory: {cell(row['status'])}")
        lines.append("| " + " | ".join([
            identity, "<br>".join(past) or "Not recorded",
            "<br>".join(future) or "Not recorded", initial,
            retirement, replacement, cell(checked)]) + " |")
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
