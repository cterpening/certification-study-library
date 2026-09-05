#!/usr/bin/env python3
"""Prepare a bounded manifest for an official-source freshness agent."""

from __future__ import annotations

import argparse
from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXAMS = ROOT / "config/exams.json"
DEFAULT_SEEDS = ROOT / "config/certification-seeds.json"
DEFAULT_SOURCES = ROOT / "data/sources.json"
DEFAULT_CANDIDATES = ROOT / "data/source-candidates.json"
DEFAULT_HEALTH = ROOT / "data/source-health.json"
DEFAULT_FRESHNESS = ROOT / "data/source-freshness.json"
DEFAULT_BATCH_SIZE = 10
MAX_BATCH_SIZE = 12
DEFAULT_MIN_AGE_DAYS = 7

FIRST_PARTY_SOURCE_TYPES = {
    "architecture-guidance",
    "credential-page",
    "exam-blueprint",
    "hands-on-lab",
    "independent-assessment",
    "lifecycle-announcement",
    "official-announcement",
    "official-certification",
    "official-certification-page",
    "official-documentation",
    "official-guidance",
    "official-learning-path",
    "official-policy",
    "official-practice",
    "official-reference",
    "official-training",
    "official-video",
    "product-documentation",
    "program-policy",
    "release-notes",
    "security-guidance",
}


def load_json(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as source:
        value = json.load(source)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def natural_key(value: object) -> tuple[object, ...]:
    return tuple(
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", str(value))
    )


def official_sources_for_exam(
    sources: Iterable[dict[str, object]], code: str
) -> list[dict[str, object]]:
    return [
        source
        for source in sources
        if code in source.get("supported_exams", [])
        and isinstance(source.get("authority_class"), int)
        and int(source["authority_class"]) <= 3
        and source.get("access_model") == "public"
        and source.get("source_type") in FIRST_PARTY_SOURCE_TYPES
    ]


def queued_candidates_for_exam(
    candidates: Iterable[dict[str, object]], code: str
) -> list[dict[str, object]]:
    return [
        candidate
        for candidate in candidates
        if code in candidate.get("suggested_exams", [])
        and candidate.get("review_status") == "queued"
    ]


def source_freshness_baseline_sha256(
    exam: dict[str, object],
    guide_text: str,
    official_sources: Iterable[dict[str, object]],
) -> str:
    """Bind a scan to the guide and its current registered official evidence."""

    payload = {
        "exam": {
            key: exam.get(key)
            for key in (
                "code",
                "vendor_id",
                "status",
                "study_guide_url",
                "blueprint_last_checked",
                "upcoming_change_status",
                "upcoming_change_checked",
                "review_status",
            )
        },
        "guide_sha256": sha256(guide_text.encode("utf-8")).hexdigest(),
        "official_sources": sorted(
            (
                {
                    key: source.get(key)
                    for key in (
                        "id",
                        "url",
                        "authority_class",
                        "source_type",
                        "last_checked",
                    )
                }
                for source in official_sources
            ),
            key=lambda source: str(source.get("id", "")),
        ),
    }
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return sha256(encoded).hexdigest()


def completed_current_scans(
    catalog: dict[str, object],
    today: date | None = None,
) -> dict[tuple[str, str, int], date]:
    today = today or date.today()
    completed: dict[tuple[str, str, int], date] = {}
    raw_batches = catalog.get("batches", [])
    if not isinstance(raw_batches, list):
        return completed
    for batch in raw_batches:
        if not isinstance(batch, dict) or batch.get("status") != "completed":
            continue
        rubric_version = batch.get("rubric_version")
        if not isinstance(rubric_version, int):
            continue
        try:
            created_on = date.fromisoformat(str(batch.get("created_on", "")))
            completed_on = date.fromisoformat(str(batch.get("completed_on", "")))
        except ValueError:
            continue
        if created_on > completed_on or completed_on > today:
            continue
        raw_results = batch.get("results", [])
        if not isinstance(raw_results, list):
            continue
        for result in raw_results:
            if not isinstance(result, dict):
                continue
            if result.get("outcome") not in {"current", "review-required"}:
                continue
            try:
                scanned_on = date.fromisoformat(str(result.get("scanned_on", "")))
            except ValueError:
                continue
            if scanned_on < created_on or scanned_on > completed_on or scanned_on > today:
                continue
            key = (
                str(result.get("exam_code", "")),
                str(result.get("baseline_sha256", "")),
                rubric_version,
            )
            if key not in completed or scanned_on > completed[key]:
                completed[key] = scanned_on
    return completed


def risk_factors(
    exam: dict[str, object],
    guide_text: str,
    official_sources: Iterable[dict[str, object]],
    health_by_id: dict[str, dict[str, object]],
    last_scan: date | None,
    today: date,
) -> tuple[int, list[str]]:
    score = 0
    factors: list[str] = []
    status = str(exam.get("status", ""))
    status_scores = {"changing": 500, "beta": 450, "retired": 300}
    if status in status_scores:
        score += status_scores[status]
        factors.append(f"exam-status:{status}")
    upcoming = str(exam.get("upcoming_change_status", ""))
    upcoming_scores = {"retirement-announced": 400, "scheduled": 300}
    if upcoming in upcoming_scores:
        score += upcoming_scores[upcoming]
        factors.append(f"upcoming-change:{upcoming}")
    for source in official_sources:
        health_status = str(
            health_by_id.get(str(source.get("id", "")), {}).get("status", "missing")
        )
        if health_status in {"missing", "error"}:
            score += 100
            factors.append(f"official-source-health:{health_status}")
        elif health_status == "blocked":
            score += 25
            factors.append("official-source-health:blocked")
    verify_count = guide_text.count("VERIFY CURRENT")
    if verify_count:
        score += min(verify_count, 25) * 3
        factors.append(f"verify-current-markers:{verify_count}")
    if last_scan is None:
        score += 50
        factors.append("never-freshness-scanned")
    else:
        age = (today - last_scan).days
        score += min(max(age, 0), 90)
        factors.append(f"freshness-scan-age-days:{age}")
    return score, factors


def build_item(
    exam: dict[str, object],
    sources: list[dict[str, object]],
    candidates: list[dict[str, object]],
    health_by_id: dict[str, dict[str, object]],
    catalog_sources: list[dict[str, object]],
    completed: dict[tuple[str, str, int], date],
    rubric_version: int,
    today: date,
) -> dict[str, object]:
    code = str(exam["code"])
    guide_path = str(exam["guide_path"])
    guide_text = (ROOT / guide_path).read_text(encoding="utf-8")
    official_sources = official_sources_for_exam(sources, code)
    baseline = source_freshness_baseline_sha256(exam, guide_text, official_sources)
    last_scan = completed.get((code, baseline, rubric_version))
    score, factors = risk_factors(
        exam, guide_text, official_sources, health_by_id, last_scan, today
    )
    vendor_id = str(exam["vendor_id"])
    return {
        "exam_code": code,
        "vendor_id": vendor_id,
        "title": str(exam["title"]),
        "exam_status": str(exam["status"]),
        "upcoming_change_status": str(exam["upcoming_change_status"]),
        "guide_path": guide_path,
        "official_blueprint": str(exam["study_guide_url"]),
        "baseline_sha256": baseline,
        "last_completed_scan": last_scan.isoformat() if last_scan else None,
        "catalog_entry_points": [
            {
                "id": str(source.get("id", "")),
                "url": str(source.get("catalog_url", "")),
                "selection": str(source.get("selection", "")),
            }
            for source in catalog_sources
            if source.get("vendor_id") == vendor_id
        ],
        "registered_official_sources": [
            {
                "id": str(source.get("id", "")),
                "title": str(source.get("title", "")),
                "url": str(source.get("url", "")),
                "authority_class": source.get("authority_class"),
                "source_type": str(source.get("source_type", "")),
                "last_checked": str(source.get("last_checked", "")),
                "health_status": str(
                    health_by_id.get(str(source.get("id", "")), {}).get(
                        "status", "missing"
                    )
                ),
                "health_final_url": str(
                    health_by_id.get(str(source.get("id", "")), {}).get(
                        "final_url", ""
                    )
                ),
                "health_canonical_url": str(
                    health_by_id.get(str(source.get("id", "")), {}).get(
                        "canonical_url", ""
                    )
                ),
            }
            for source in sorted(
                official_sources, key=lambda source: str(source.get("id", ""))
            )
        ],
        "queued_candidates": [
            {
                "id": str(candidate.get("id", "")),
                "title": str(candidate.get("title", "")),
                "url": str(candidate.get("url", "")),
                "review_status": str(candidate.get("review_status", "")),
            }
            for candidate in queued_candidates_for_exam(candidates, code)
        ],
        "risk_score": score,
        "risk_factors": factors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--min-age-days", type=int, default=DEFAULT_MIN_AGE_DAYS)
    parser.add_argument("--exam-code", action="append", default=[])
    parser.add_argument("--vendor-id", action="append", default=[])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--exams", type=Path, default=DEFAULT_EXAMS)
    parser.add_argument("--seeds", type=Path, default=DEFAULT_SEEDS)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--source-health", type=Path, default=DEFAULT_HEALTH)
    parser.add_argument("--freshness", type=Path, default=DEFAULT_FRESHNESS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not re.fullmatch(r"[a-z0-9-]+", args.batch_id):
        raise ValueError("Batch id must contain lowercase letters, digits, and hyphens")
    if not 1 <= args.size <= MAX_BATCH_SIZE:
        raise ValueError(f"Batch size must be between 1 and {MAX_BATCH_SIZE}")
    if len(args.exam_code) > MAX_BATCH_SIZE:
        raise ValueError(f"Explicit batches may contain at most {MAX_BATCH_SIZE} guides")
    if len(args.exam_code) != len(set(args.exam_code)):
        raise ValueError("Explicit batch contains duplicate exam codes")
    if args.min_age_days < 0:
        raise ValueError("Minimum scan age cannot be negative")

    exams_data = load_json(args.exams)
    seeds_data = load_json(args.seeds)
    sources_data = load_json(args.sources)
    candidates_data = load_json(args.candidates)
    health_data = load_json(args.source_health)
    freshness_data = load_json(args.freshness)
    rubric_version = freshness_data.get("rubric_version")
    if not isinstance(rubric_version, int):
        raise ValueError("Freshness catalog needs an integer rubric_version")

    exams = [item for item in exams_data.get("exams", []) if isinstance(item, dict)]
    sources = [
        item for item in sources_data.get("sources", []) if isinstance(item, dict)
    ]
    candidates = [
        item
        for item in candidates_data.get("candidates", [])
        if isinstance(item, dict)
    ]
    catalog_sources = [
        item
        for item in seeds_data.get("catalog_sources", [])
        if isinstance(item, dict)
    ]
    health_by_id = {
        str(item.get("id")): item
        for item in health_data.get("sources", [])
        if isinstance(item, dict) and item.get("id")
    }
    completed = completed_current_scans(freshness_data)
    today = date.today()

    exam_by_code = {str(exam.get("code")): exam for exam in exams}
    unknown_codes = [code for code in args.exam_code if code not in exam_by_code]
    if unknown_codes:
        raise ValueError("Unknown exam codes: " + ", ".join(unknown_codes))
    known_vendors = {str(exam.get("vendor_id")) for exam in exams}
    unknown_vendors = [vendor for vendor in args.vendor_id if vendor not in known_vendors]
    if unknown_vendors:
        raise ValueError("Unknown vendor ids: " + ", ".join(unknown_vendors))

    selected = [exam_by_code[code] for code in args.exam_code] if args.exam_code else exams
    if args.vendor_id:
        selected = [exam for exam in selected if exam.get("vendor_id") in args.vendor_id]
    items = [
        build_item(
            exam,
            sources,
            candidates,
            health_by_id,
            catalog_sources,
            completed,
            rubric_version,
            today,
        )
        for exam in selected
    ]
    explicit = bool(args.exam_code)
    if not explicit:
        items = [
            item
            for item in items
            if item["last_completed_scan"] is None
            or (
                today - date.fromisoformat(str(item["last_completed_scan"]))
            ).days
            >= args.min_age_days
        ]
        items.sort(
            key=lambda item: (
                -int(item["risk_score"]),
                natural_key(item["exam_code"]),
            )
        )
        items = items[: args.size]

    manifest = {
        "batch_id": args.batch_id,
        "generated_on": today.isoformat(),
        "rubric_version": rubric_version,
        "scan_mode": "read-only",
        "selection_method": (
            "explicit exam-code freshness scan"
            if explicit
            else "due guides ordered by lifecycle and source-volatility risk"
        ),
        "rubric_path": "docs/SOURCE-FRESHNESS.md",
        "agent_contract": {
            "source_policy": "Official first-party public sources only.",
            "required_channels": [
                "official blueprint or credential page",
                "official product documentation",
                "official release notes, roadmap, retirement, or announcement pages",
            ],
            "review_boundary": (
                "Report evidence and candidates; do not silently promote sources or "
                "rewrite guide claims."
            ),
        },
        "items": items,
    }
    rendered = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Source freshness preparation failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
