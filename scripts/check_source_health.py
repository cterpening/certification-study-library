#!/usr/bin/env python3
"""Check registered source reachability and reviewable public metadata changes."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timezone
from hashlib import sha256
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = ROOT / "data/sources.json"
DEFAULT_SNAPSHOT = ROOT / "data/source-health.json"
MAX_RESPONSE_BYTES = 2_000_000
USER_AGENT = (
    "CertificationStudyLibrarySourceMonitor/1.0 "
    "(+https://github.com/cterpening/certification-study-library)"
)
DURATION_PATTERN = re.compile(
    r"\b(?:about\s+|approximately\s+)?\d+(?:\.\d+)?\s*"
    r"(?:hours?|hrs?|minutes?|mins?)"
    r"(?:\s*(?:and\s*)?\d+\s*(?:minutes?|mins?))?\b",
    re.IGNORECASE,
)
UNSTABLE_METADATA_HOSTS = {"youtube.com", "www.youtube.com", "youtu.be"}


def normalize_text(value: object) -> str:
    return re.sub(r"\s+", " ", unescape(str(value))).strip()


class PageSignalParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.in_json_ld = False
        self.json_ld_parts: list[str] = []
        self.json_ld_documents: list[str] = []
        self.canonical_url = ""
        self.meta_title = ""
        self.visible_text_parts: list[str] = []
        self.ignored_depth = 0

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = {key.lower(): value or "" for key, value in attrs}
        lowered = tag.lower()
        if lowered in {"script", "style", "noscript", "template", "svg"}:
            self.ignored_depth += 1
        if lowered == "title":
            self.in_title = True
        elif lowered == "link" and "canonical" in attributes.get("rel", "").lower():
            self.canonical_url = normalize_text(attributes.get("href", ""))
        elif lowered == "meta":
            property_name = attributes.get("property", "").lower()
            name = attributes.get("name", "").lower()
            if property_name == "og:title" or name == "twitter:title":
                self.meta_title = normalize_text(attributes.get("content", ""))
        elif (
            lowered == "script"
            and attributes.get("type", "").lower() == "application/ld+json"
        ):
            self.in_json_ld = True
            self.json_ld_parts = []

    def handle_endtag(self, tag: str) -> None:
        lowered = tag.lower()
        if lowered == "title":
            self.in_title = False
        elif lowered == "script" and self.in_json_ld:
            self.in_json_ld = False
            document = "".join(self.json_ld_parts).strip()
            if document:
                self.json_ld_documents.append(document)
            self.json_ld_parts = []
        if lowered in {"script", "style", "noscript", "template", "svg"}:
            self.ignored_depth = max(0, self.ignored_depth - 1)

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_json_ld:
            self.json_ld_parts.append(data)
        elif self.ignored_depth == 0:
            self.visible_text_parts.append(data)


def collect_structured_durations(value: object, found: set[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            lowered = str(key).lower()
            if "duration" in lowered or lowered == "timerequired":
                if isinstance(child, (str, int, float)):
                    normalized = normalize_text(child)
                    if normalized:
                        found.add(normalized)
            collect_structured_durations(child, found)
    elif isinstance(value, list):
        for child in value:
            collect_structured_durations(child, found)


def extract_page_signals(html_text: str, final_url: str) -> dict[str, object]:
    parser = PageSignalParser()
    parser.feed(html_text)
    title = parser.meta_title or normalize_text("".join(parser.title_parts))
    visible_text = normalize_text(" ".join(parser.visible_text_parts))
    duration_signals: set[str] = {
        normalize_text(match.group(0))
        for match in DURATION_PATTERN.finditer(visible_text)
    }
    for document in parser.json_ld_documents:
        try:
            structured = json.loads(document)
        except json.JSONDecodeError:
            continue
        collect_structured_durations(structured, duration_signals)
    durations = sorted(duration_signals, key=str.casefold)[:30]
    canonical_url = parser.canonical_url or final_url
    signal_payload = {
        "page_title": title,
        "canonical_url": canonical_url,
        "duration_signals": durations,
    }
    fingerprint = sha256(
        json.dumps(signal_payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return {**signal_payload, "signal_fingerprint": fingerprint}


def classify_http_error(status: int) -> str:
    if status in {401, 403, 407, 429, 451}:
        return "blocked"
    if status in {404, 410}:
        return "missing"
    return "error"


def comparable_signal_fields(url: str) -> tuple[str, ...]:
    """Return stable fields worth comparing for the source's public host."""
    hostname = (urlparse(url).hostname or "").lower()
    if hostname in UNSTABLE_METADATA_HOSTS:
        # YouTube consent, localization, and bot-handling responses vary by runner
        # region even when the video URL is healthy. Reachability and redirects
        # remain useful; page title, canonical URL, and duration do not.
        return ("final_url",)
    return ("final_url", "page_title", "canonical_url", "duration_signals")


def fetch_source(
    source: dict[str, object],
    *,
    timeout: float,
    opener: Callable[..., object] = urlopen,
) -> dict[str, object]:
    source_id = str(source["id"])
    url = str(source["url"])
    checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.5",
            "Accept-Language": "en-US,en;q=0.8",
        },
    )
    base: dict[str, object] = {
        "id": source_id,
        "url": url,
        "checked_at": checked_at,
        "status": "error",
        "http_status": None,
        "final_url": url,
        "content_type": "",
        "page_title": "",
        "canonical_url": "",
        "duration_signals": [],
        "signal_fingerprint": "",
        "error": "",
    }
    try:
        response = opener(request, timeout=timeout)
        with response:
            status = int(response.getcode() or 200)
            final_url = str(response.geturl())
            content_type = str(response.headers.get("Content-Type", ""))
            body = response.read(MAX_RESPONSE_BYTES + 1)
        if len(body) > MAX_RESPONSE_BYTES:
            body = body[:MAX_RESPONSE_BYTES]
        encoding_match = re.search(r"charset=([^;\s]+)", content_type, re.I)
        encoding = encoding_match.group(1).strip("\"'") if encoding_match else "utf-8"
        html_text = body.decode(encoding, errors="replace")
        signals = (
            extract_page_signals(html_text, final_url)
            if "html" in content_type.lower() or "<html" in html_text[:1000].lower()
            else {}
        )
        base.update(
            {
                "status": "ok" if 200 <= status < 400 else classify_http_error(status),
                "http_status": status,
                "final_url": final_url,
                "content_type": content_type,
                **signals,
            }
        )
    except HTTPError as exc:
        base.update(
            {
                "status": classify_http_error(exc.code),
                "http_status": exc.code,
                "final_url": str(exc.geturl() or url),
                "error": normalize_text(exc.reason),
            }
        )
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        base["error"] = normalize_text(exc)
    return base


def load_json(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def snapshot_by_id(snapshot: dict[str, object]) -> dict[str, dict[str, object]]:
    entries = snapshot.get("sources", [])
    if not isinstance(entries, list):
        return {}
    return {
        str(entry["id"]): entry
        for entry in entries
        if isinstance(entry, dict) and "id" in entry
    }


def compare_results(
    sources: list[dict[str, object]],
    results: list[dict[str, object]],
    previous_snapshot: dict[str, object],
    *,
    stale_days: int,
    today: date | None = None,
) -> dict[str, object]:
    today = today or date.today()
    previous = snapshot_by_id(previous_snapshot)
    source_by_id = {str(source["id"]): source for source in sources}
    broken: list[dict[str, object]] = []
    blocked: list[dict[str, object]] = []
    changed: list[dict[str, object]] = []
    stale: list[dict[str, object]] = []

    for result in results:
        source_id = str(result["id"])
        status = result.get("status")
        if status in {"missing", "error"}:
            broken.append(result)
        elif status == "blocked":
            blocked.append(result)

        prior = previous.get(source_id)
        if prior and status == "ok" and prior.get("status") == "ok":
            fields = [
                field
                for field in comparable_signal_fields(str(result.get("url", "")))
                if result.get(field) != prior.get(field)
            ]
            if fields:
                changed.append(
                    {
                        "id": source_id,
                        "url": result.get("url"),
                        "changed_fields": fields,
                        "previous": {field: prior.get(field) for field in fields},
                        "current": {field: result.get(field) for field in fields},
                    }
                )

        source = source_by_id[source_id]
        last_checked = date.fromisoformat(str(source["last_checked"]))
        age_days = (today - last_checked).days
        if age_days > stale_days:
            stale.append(
                {
                    "id": source_id,
                    "url": source["url"],
                    "last_checked": source["last_checked"],
                    "age_days": age_days,
                }
            )

    return {
        "checked_on": today.isoformat(),
        "summary": {
            "total": len(results),
            "ok": sum(1 for item in results if item.get("status") == "ok"),
            "blocked": len(blocked),
            "broken": len(broken),
            "changed": len(changed),
            "stale": len(stale),
            "baseline_missing": not bool(previous),
            "needs_review": bool(broken or changed or stale),
        },
        "findings": {
            "broken": broken,
            "changed": changed,
            "stale": stale,
            "blocked": blocked,
        },
        "results": results,
    }


def render_markdown_report(report: dict[str, object]) -> str:
    summary = report["summary"]
    findings = report["findings"]
    assert isinstance(summary, dict) and isinstance(findings, dict)
    lines = [
        "# Source catalog health report",
        "",
        f"Checked: **{report['checked_on']}**",
        "",
        "| Result | Count |",
        "|---|---:|",
    ]
    for label in ("total", "ok", "blocked", "broken", "changed", "stale"):
        lines.append(f"| {label.replace('_', ' ').title()} | {summary[label]} |")

    def add_table(
        title: str,
        entries: object,
        detail: Callable[[dict[str, object]], str],
    ) -> None:
        if not isinstance(entries, list) or not entries:
            return
        lines.extend(["", f"## {title}", "", "| Source | Detail |", "|---|---|"])
        for entry in entries[:50]:
            if not isinstance(entry, dict):
                continue
            source_id = str(entry.get("id", "unknown"))
            url = str(entry.get("url", ""))
            lines.append(f"| [{source_id}]({url}) | {detail(entry)} |")
        if len(entries) > 50:
            lines.extend(["", f"_Showing 50 of {len(entries)} findings._"])

    add_table(
        "Broken or missing",
        findings.get("broken"),
        lambda item: (
            f"{item.get('status')} / HTTP {item.get('http_status') or 'n/a'} — "
            f"{item.get('error') or 'review required'}"
        ),
    )
    add_table(
        "Reviewable metadata changes",
        findings.get("changed"),
        lambda item: ", ".join(
            str(value) for value in item.get("changed_fields", [])
        ),
    )
    add_table(
        "Stale catalog checks",
        findings.get("stale"),
        lambda item: (
            f"last checked {item.get('last_checked')} ({item.get('age_days')} days)"
        ),
    )
    add_table(
        "Blocked automated requests",
        findings.get("blocked"),
        lambda item: (
            f"HTTP {item.get('http_status') or 'n/a'}; verify manually before "
            "treating as broken"
        ),
    )
    lines.extend(
        [
            "",
            "Blocked requests are informational because many legitimate providers reject automated clients. Metadata changes are review prompts, not automatic catalog edits.",
            "",
        ]
    )
    return "\n".join(lines)


def write_github_output(path: Path, summary: dict[str, object]) -> None:
    with path.open("a", encoding="utf-8") as output:
        for key in ("needs_review", "broken", "changed", "stale", "blocked"):
            output.write(f"{key}={str(summary[key]).lower()}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--snapshot", type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument("--write", action="store_true", help="Replace the trusted snapshot")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--markdown-report", type=Path)
    parser.add_argument("--github-output", type=Path)
    parser.add_argument("--only", action="append", default=[])
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--max-workers", type=int, default=8)
    parser.add_argument("--stale-days", type=int, default=90)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    catalog = load_json(args.catalog)
    raw_sources = catalog.get("sources")
    if not isinstance(raw_sources, list):
        raise ValueError("Source catalog needs a sources array")
    sources = [source for source in raw_sources if isinstance(source, dict)]
    if args.only:
        requested = set(args.only)
        sources = [source for source in sources if source.get("id") in requested]
        missing_ids = requested.difference(str(source.get("id")) for source in sources)
        if missing_ids:
            raise ValueError("Unknown source IDs: " + ", ".join(sorted(missing_ids)))

    previous_snapshot = (
        load_json(args.snapshot) if args.snapshot.is_file() else {"sources": []}
    )
    results: list[dict[str, object]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
        futures = {
            executor.submit(fetch_source, source, timeout=args.timeout): source
            for source in sources
        }
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: str(item["id"]))

    report = compare_results(
        sources,
        results,
        previous_snapshot,
        stale_days=args.stale_days,
    )
    snapshot = {
        "$schema": "../schemas/source-health.schema.json",
        "schema_version": 1,
        "generated_on": report["checked_on"],
        "sources": results,
    }
    if args.write:
        args.snapshot.write_text(
            json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    if args.report:
        args.report.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    if args.markdown_report:
        args.markdown_report.write_text(
            render_markdown_report(report), encoding="utf-8"
        )
    summary = report["summary"]
    assert isinstance(summary, dict)
    if args.github_output:
        write_github_output(args.github_output, summary)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Source health check failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
