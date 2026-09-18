#!/usr/bin/env python3
"""Compare public vendor catalog listings; never promote candidates to credentials."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from hashlib import sha256
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from urllib.request import Request

from url_policy import open_public_https, same_site_hosts, validate_public_https_url


ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 6_000_000
IGNORED = {"script", "style", "noscript", "template", "svg"}
TRACKING = {"gclid", "fbclid", "_gl", "_ga"}


def clean(text: str) -> str:
    return " ".join(text.split())


def canonical(url: str) -> str:
    """Remove fragments and tracking only; retain semantic query parameters."""
    p = urlsplit(url)
    query = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
             if not k.lower().startswith(("utm_", "itm_")) and k.lower() not in TRACKING]
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip("/"),
                       urlencode(sorted(query)), ""))


class CatalogParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ignored: list[str] = []
        self.captures: list[dict] = []
        self.links: list[dict] = []
        self.headings: list[dict] = []
        self.rows: list[list[str]] = []
        self.text: list[str] = []
        self.cells: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in IGNORED:
            self.ignored.append(tag)
        if self.ignored:
            return
        if tag == "tr":
            self.cells = []
        if tag == "a" or re.fullmatch(r"h[1-6]", tag) or tag in {"td", "th"}:
            self.captures.append({"tag": tag, "attrs": dict(attrs), "text": []})

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # Void/self-closing SVGs must not hide the rest of a catalog.
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if not self.ignored:
            self.text.append(data)
            for capture in self.captures:
                capture["text"].append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.ignored:
            if tag == self.ignored[-1]:
                self.ignored.pop()
            return
        for index in range(len(self.captures) - 1, -1, -1):
            item = self.captures[index]
            if item["tag"] != tag:
                continue
            self.captures.pop(index)
            text = item.get("label") or clean(" ".join(item["text"]))
            if tag == "a":
                self.links.append({"url": item["attrs"].get("href") or "", "title": text})
            elif tag in {"td", "th"}:
                self.cells.append(text)
            else:
                self.headings.append({"title": text})
                for parent in self.captures:
                    if parent["tag"] == "a":
                        parent["label"] = text
            break
        if tag == "tr" and self.cells:
            self.rows.append(self.cells)
            self.cells = []


def json_candidates(raw: str, mode: str) -> list[dict]:
    """Read the public feeds used by the vendors' current catalog websites.

    These are website interfaces, not guaranteed integration APIs. Reject
    partial results and contract changes instead of accepting apparent removals.
    """
    try:
        payload = json.loads(raw)
        candidates = []
        if mode == "microsoft-json":
            records = payload["results"]
            if (not isinstance(records, list) or type(payload["count"]) is not int
                    or payload["count"] != len(records) or payload.get("@nextLink")):
                raise ValueError("Microsoft catalog is paginated or incomplete; manual review required")
            identities = [row["uid"] for row in records]
            if len(set(identities)) != len(identities):
                raise ValueError("Duplicate Microsoft catalog identities; manual review required")
            for row in records:
                if row["locale"] != "en-us" or "certification" not in row["credential_types"]:
                    raise ValueError("Unexpected Microsoft catalog scope; manual review required")
                exams = sorted(exam["uid"].removeprefix("exam.").upper() for exam in row["exams"])
                candidates.append({"title": row["title"],
                                   "url": urljoin("https://learn.microsoft.com/en-us/", row["url"].lstrip("/")),
                                   "detail": "Required exam references: " + (", ".join(exams) or "not supplied by catalog")})
        elif mode == "github-json":
            if not isinstance(payload, list):
                raise ValueError("Unexpected GitHub catalog shape; manual review required")
            identities = [row["certification"]["id"] for row in payload]
            if len(set(identities)) != len(identities):
                raise ValueError("Duplicate GitHub catalog identities; manual review required")
            for row in payload:
                cert = row["certification"]
                if type(cert["active"]) is not bool or type(cert["beta"]) is not bool:
                    raise ValueError("Unexpected GitHub lifecycle fields; manual review required")
                candidates.append({"title": cert["title"], "url": cert["msLearnUrl"],
                                   "detail": f"Active: {cert['active']}; beta: {cert['beta']}"})
        for row in candidates:
            if not isinstance(row["title"], str) or not row["title"].strip() or not isinstance(row["url"], str) or not row["url"]:
                raise ValueError("Catalog item missing title or URL; manual review required")
        return candidates
    except (KeyError, TypeError, AttributeError) as exc:
        raise ValueError("Public JSON catalog contract changed; manual review required") from exc


def extract(html: str, source: dict) -> list[dict]:
    mode = source["extract"]
    is_json = mode in {"microsoft-json", "github-json"}
    parser = CatalogParser()
    if is_json:
        candidates = json_candidates(html, mode)
        visible = " ".join(row["title"] for row in candidates)
    else:
        parser.feed(html)
        visible = " ".join(parser.text)
    if not re.search(source["expected_text"], clean(visible), re.I):
        raise ValueError("Expected catalog content missing; possible login, challenge, or page shell")
    if mode == "links":
        candidates = parser.links
    elif mode == "headings":
        candidates = parser.headings
    elif mode == "text":
        candidates = [{"title": clean(text)} for text in parser.text]
    elif mode == "table":
        column = source.get("column", 0)
        candidates = [{"title": row[column], "detail": clean(" | ".join(row))[:500]}
                      for row in parser.rows if len(row) > column]
    hosts = set(source.get("allowed_hosts", [])) | same_site_hosts(urlsplit(source["url"]).hostname or "")
    found: dict[str, dict] = {}
    for candidate in candidates:
        title = candidate["title"][:240]
        url = urljoin(source["url"], candidate.get("url", ""))
        match_value = urlsplit(url).path if mode == "links" or is_json else title
        if not re.search(source["include"], match_value, re.I):
            continue
        if source.get("exclude") and re.search(source["exclude"], match_value, re.I):
            continue
        try:
            validate_public_https_url(url, allowed_hosts=hosts)
        except ValueError:
            if is_json:
                raise ValueError("Public JSON catalog contains an unexpected URL; manual review required")
            continue
        url = canonical(url)
        key = url if mode == "links" or is_json else clean(title).casefold()
        # Link text can be a full card description. Keep it for change detection,
        # but never treat it as a verified exam title, availability, or blueprint.
        entry = {"key": key, "url": url, "title": title or urlsplit(url).path.rsplit("/", 1)[-1]}
        if candidate.get("detail"):
            entry["detail"] = candidate["detail"]
        if key not in found or len(entry["title"]) > len(found[key]["title"]):
            found[key] = entry
    rows = sorted(found.values(), key=lambda item: item["key"])
    if is_json and len(rows) != len(candidates):
        raise ValueError("Public JSON catalog lost or merged listings; manual review required")
    if len(rows) < source["minimum_items"]:
        raise ValueError(f"Only {len(rows)} listings extracted; minimum is {source['minimum_items']}. Manual catalog review required")
    return rows


def fetch(source: dict) -> str:
    hosts = same_site_hosts(urlsplit(source["url"]).hostname or "") | set(source.get("allowed_hosts", []))
    request = Request(source["url"], headers={"User-Agent": "CertificationStudyLibraryDiscovery/1.0"})
    with open_public_https(request, timeout=30, allowed_redirect_hosts=hosts) as response:
        expected_type = "application/json" if source["extract"].endswith("-json") else "text/html"
        if response.headers.get_content_type() != expected_type:
            raise ValueError("Unexpected catalog content type; review the source or extractor")
        raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("Response exceeds catalog size limit; not comparing truncated content")
        return raw.decode(response.headers.get_content_charset() or "utf-8", errors="replace")


def contract(source: dict) -> str:
    return sha256(json.dumps(source, sort_keys=True).encode()).hexdigest()


def compare(source: dict, items: list[dict], previous: dict | None) -> dict:
    result = {"id": source["id"], "vendor_id": source["vendor_id"], "url": source["url"],
              "contract": contract(source), "checked_on": date.today().isoformat(),
              "items": items, "added": [], "missing": [], "changed": []}
    if previous is None or previous.get("contract") != result["contract"]:
        result.update(status="baseline-needed", reason="New source or extraction configuration; review initial listings")
        return result
    before = {item["key"]: item for item in previous["items"]}
    after = {item["key"]: item for item in items}
    if len(after) < len(before) * 0.6:
        result.update(status="manual-review", reason="Catalog shrank by more than 40%; possible incomplete extraction. Baseline retained")
        return result
    result["added"] = [after[key] for key in sorted(after.keys() - before.keys())]
    result["missing"] = [before[key] for key in sorted(before.keys() - after.keys())]
    result["changed"] = [{"before": before[key], "after": after[key]} for key in sorted(before.keys() & after.keys()) if before[key] != after[key]]
    result["status"] = "changed" if any(result[field] for field in ("added", "missing", "changed")) else "unchanged"
    return result


def check(source: dict, previous: dict | None, fetcher=fetch) -> dict:
    try:
        return compare(source, extract(fetcher(source), source), previous)
    except HTTPError as exc:
        state = "manual-review" if exc.code in {401, 403, 429} else "error"
        reason = f"HTTP {exc.code}; official catalog review required"
    except ValueError as exc:
        state, reason = "manual-review", str(exc)
    except (URLError, TimeoutError, OSError) as exc:
        state, reason = "error", f"Fetch failed ({type(exc).__name__}); retry or review official catalog"
    return {"id": source["id"], "vendor_id": source["vendor_id"], "url": source["url"],
            "checked_on": date.today().isoformat(), "status": state, "reason": reason}


def merge_baseline(previous: dict, results: list[dict]) -> dict:
    merged = {row["id"]: row for row in previous.get("sources", [])}
    for row in results:
        if row["status"] in {"changed", "unchanged", "baseline-needed"}:
            merged[row["id"]] = {key: row[key] for key in ("id", "contract", "checked_on", "items")}
    return {"schema_version": 1, "sources": [merged[key] for key in sorted(merged)]}


def inventory_index(root: Path) -> dict[str, list[str]]:
    index: dict[str, set[str]] = {}
    for path, key in [("config/certification-seeds.json", "certifications"), ("config/exams.json", "exams")]:
        for row in json.loads((root / path).read_text(encoding="utf-8"))[key]:
            for field in ("official_url", "study_guide_url"):
                if row.get(field):
                    index.setdefault(canonical(row[field]), set()).add(row["exam_code"] if "exam_code" in row else row["code"])
    # Editorial partner pages are coverage too, but a URL match is not a claim
    # that every credential/course on that page has a published guide.
    for path in (root / "docs/partner-ai").glob("*.md"):
        for url in re.findall(r"\]\((https://[^)]+)\)", path.read_text(encoding="utf-8")):
            index.setdefault(canonical(url), set()).add(f"editorial:{path.stem}")
    return {url: sorted(codes) for url, codes in index.items()}


def annotate_inventory(results: list[dict], urls: dict, seeds: list[dict]) -> None:
    by_vendor: dict[str, list[str]] = {}
    for seed in seeds:
        by_vendor.setdefault(seed["vendor_id"], []).append(seed["exam_code"])
    for row in results:
        codes = by_vendor.get(row["vendor_id"], [])
        for item in row.get("items", []):
            direct = urls.get(item["url"], [])
            # Exam-code matches are vendor-scoped: Snowflake and AWS both use
            # MLA-C01. Do not collapse those into one credential.
            text = item["title"] + " " + item["url"] + " " + item.get("detail", "")
            matched = [code for code in codes if re.search(
                r"(?<![a-z0-9])" + re.escape(code) + r"(?![a-z0-9])", text, re.I)]
            item["inventory_matches"] = sorted(set(direct + matched))
            item["match_basis"] = "url" if direct else "exam-code" if matched else "unmatched"


def safe(text: str) -> str:
    return escape(clean(text)).replace("|", "&#124;").replace("[", "&#91;").replace("]", "&#93;")


def markdown(report: dict, config: dict) -> str:
    lines = [f"# Certification discovery — {report['checked_on']}", "",
             "Catalog observations, not newly certified guides. Missing listings do not prove retirement.",
             "URL or vendor-scoped exam-code matches indicate an existing reference; unmatched listings are candidates, not confirmed gaps.", "",
             "| Source | Result | Listings | Unmatched listings |", "|---|---|---:|---:|"]
    for row in report["sources"]:
        lines.append(f"| {row['id']} | {row['status']} | {len(row.get('items', []))} | {sum(not item['inventory_matches'] for item in row.get('items', []))} |")
    for row in report["sources"]:
        if row["status"] == "unchanged":
            continue
        lines += ["", f"## {row['id']}", "", f"Official source: <{row['url']}>", ""]
        if row.get("reason"):
            lines.append(safe(row["reason"]))
        for field in ("added", "missing", "changed"):
            for item in row.get(field, []):
                if field == "changed":
                    before = item['before'].get('detail', item['before']['title'])
                    after = item['after'].get('detail', item['after']['title'])
                    lines.append(f"- Changed: {safe(before[:220])} → {safe(after[:220])} (<{item['after']['url']}>)")
                else:
                    lines.append(f"- {field.title()}: {safe(item['title'][:180])} (<{item['url']}>)")
    if report["mode"] == "monthly":
        lines += ["", "## Monthly broader review", "",
                  "The scheduled fetch covers configured public catalogs and announcement channels. Complete this broader search manually; a successful fetch does not complete it.", "",
                  "For each vendor: search official announcements for new credentials, exam codes, launch/beta/retirement dates and replacements; inspect newly linked catalogs and pagination; classify certifications versus badges/accreditations/course certificates; open canonical evidence and blueprint; record a dated decision.", ""]
        for source in config["sources"]:
            if source["cadence"] == "weekly":
                host = urlsplit(source["url"]).hostname
                lines.append(f"- [ ] {source['id']}: `site:{host} certification new beta retirement` — {source['scope']}")
    lines += ["", "Full listings, URL matches, and differences are in the JSON artifact. Review evidence before accepting a baseline with --write. No inventory or guide is edited by this check.", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "config/certification-discovery.json")
    parser.add_argument("--baseline", type=Path, default=ROOT / "data/certification-discovery-baseline.json")
    parser.add_argument("--mode", choices=("weekly", "monthly"), default="weekly")
    parser.add_argument("--only", action="append", default=[], help="Source ID; repeat to select multiple sources")
    parser.add_argument("--report", type=Path, default=Path("certification-discovery-report.json"))
    parser.add_argument("--markdown-report", type=Path, default=Path("certification-discovery-report.md"))
    parser.add_argument("--write", action="store_true", help="Accept successfully extracted observations after review; preserves failures and unselected sources")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    sources = config["sources"]
    unknown = set(args.only) - {source["id"] for source in sources}
    if unknown:
        parser.error("Unknown source IDs: " + ", ".join(sorted(unknown)))
    sources = [source for source in sources if (not args.only or source["id"] in args.only)
               and (args.mode == "monthly" or source["cadence"] == "weekly")]
    if not sources:
        parser.error("No sources selected for this mode")
    baseline = json.loads(args.baseline.read_text(encoding="utf-8")) if args.baseline.exists() else {"sources": []}
    previous = {row["id"]: row for row in baseline["sources"]}
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(lambda source: check(source, previous.get(source["id"])), sources))
    if args.write:
        args.baseline.parent.mkdir(parents=True, exist_ok=True)
        args.baseline.write_text(json.dumps(merge_baseline(baseline, results), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    annotate_inventory(results, inventory_index(ROOT), json.loads(
        (ROOT / "config/certification-seeds.json").read_text(encoding="utf-8"))["certifications"])
    report = {"schema_version": 1, "checked_on": date.today().isoformat(), "mode": args.mode,
              "needs_review": args.mode == "monthly" or any(row["status"] != "unchanged" for row in results), "sources": results}
    for path, content in [(args.report, json.dumps(report, ensure_ascii=False, indent=2) + "\n"),
                          (args.markdown_report, markdown(report, config))]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Checked {len(results)} sources; {sum(row['status'] == 'manual-review' for row in results)} need manual extraction review; {sum(row['status'] == 'error' for row in results)} errors. See {args.markdown_report}")
    return 1 if any(row["status"] == "error" for row in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
