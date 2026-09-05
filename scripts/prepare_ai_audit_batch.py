#!/usr/bin/env python3
"""Prepare a bounded, evidence-rich manifest for an independent AI guide audit."""

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
DEFAULT_REVIEWS = ROOT / "data/reviews.json"
DEFAULT_SOURCES = ROOT / "data/sources.json"
DEFAULT_SOURCE_HEALTH = ROOT / "data/source-health.json"
DEFAULT_AUDITS = ROOT / "data/ai-audits.json"
DEFAULT_BATCH_SIZE = 10
MAX_BATCH_SIZE = 12


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


def current_source_reviews(
    reviews: Iterable[dict[str, object]],
    exams: Iterable[dict[str, object]],
) -> dict[str, dict[str, object]]:
    checked_by_code = {
        str(exam["code"]): str(exam["blueprint_last_checked"]) for exam in exams
    }
    current: dict[str, dict[str, object]] = {}
    for review in reviews:
        code = str(review.get("exam_code", ""))
        if (
            review.get("review_type") == "source-validation"
            and review.get("outcome") == "passed"
            and str(review.get("reviewed_on", "")) == checked_by_code.get(code)
        ):
            current[code] = review
    return current


def completed_current_audits(
    audit_catalog: dict[str, object],
) -> set[tuple[str, str, int]]:
    completed: set[tuple[str, str, int]] = set()
    raw_batches = audit_catalog.get("batches", [])
    if not isinstance(raw_batches, list):
        return completed
    for batch in raw_batches:
        if not isinstance(batch, dict) or batch.get("status") != "completed":
            continue
        rubric_version = batch.get("rubric_version")
        if not isinstance(rubric_version, int):
            continue
        results = batch.get("results", [])
        if not isinstance(results, list):
            continue
        for result in results:
            if not isinstance(result, dict):
                continue
            completed.add(
                (
                    str(result.get("exam_code", "")),
                    str(result.get("blueprint_snapshot_sha256", "")),
                    rubric_version,
                )
            )
    return completed


def source_indexes(
    sources: Iterable[dict[str, object]],
    health_rows: Iterable[dict[str, object]],
) -> tuple[dict[str, list[dict[str, object]]], dict[str, dict[str, object]]]:
    by_exam: dict[str, list[dict[str, object]]] = {}
    for source in sources:
        supported = source.get("supported_exams", [])
        if not isinstance(supported, list):
            continue
        for code in supported:
            by_exam.setdefault(str(code), []).append(source)
    health_by_id = {
        str(row.get("id")): row
        for row in health_rows
        if isinstance(row, dict) and row.get("id")
    }
    return by_exam, health_by_id


def risk_factors(
    exam: dict[str, object],
    registered_sources: Iterable[dict[str, object]],
    health_by_id: dict[str, dict[str, object]],
    guide_text: str,
) -> tuple[int, list[str]]:
    score = 0
    factors: list[str] = []
    status = str(exam.get("status", ""))
    status_scores = {"changing": 500, "beta": 450, "retired": 350}
    if status in status_scores:
        score += status_scores[status]
        factors.append(f"exam-status:{status}")

    upcoming = str(exam.get("upcoming_change_status", ""))
    upcoming_scores = {"retirement-announced": 400, "scheduled": 300}
    if upcoming in upcoming_scores:
        score += upcoming_scores[upcoming]
        factors.append(f"upcoming-change:{upcoming}")

    health_counts: dict[str, int] = {}
    for source in registered_sources:
        source_id = str(source.get("id", ""))
        health_status = str(health_by_id.get(source_id, {}).get("status", "missing"))
        health_counts[health_status] = health_counts.get(health_status, 0) + 1
    for health_status, points in (("missing", 120), ("error", 120), ("blocked", 40)):
        count = health_counts.get(health_status, 0)
        if count:
            score += points * count
            factors.append(f"source-health:{health_status}:{count}")

    verify_count = guide_text.count("VERIFY CURRENT")
    if verify_count:
        score += min(verify_count, 25) * 3
        factors.append(f"verify-current-markers:{verify_count}")

    if exam.get("review_status") != "community-reviewed":
        score += 10
        factors.append("human-review-pending")
    return score, factors


def build_manifest_item(
    exam: dict[str, object],
    review: dict[str, object],
    sources: list[dict[str, object]],
    health_by_id: dict[str, dict[str, object]],
) -> dict[str, object]:
    guide_path = str(exam["guide_path"])
    guide = ROOT / guide_path
    guide_text = guide.read_text(encoding="utf-8")
    snapshot_path = str(review["blueprint_snapshot_path"])
    snapshot = ROOT / snapshot_path
    actual_hash = sha256(snapshot.read_bytes()).hexdigest()
    recorded_hash = str(review["blueprint_snapshot_sha256"])
    if actual_hash != recorded_hash:
        raise ValueError(f"Current review hash is stale for {exam['code']}")

    score, factors = risk_factors(exam, sources, health_by_id, guide_text)
    status_snapshot_path = snapshot_path.replace(
        "-official-objectives.txt", "-official-status.json"
    )
    registered = []
    for source in sorted(sources, key=lambda item: str(item.get("id", ""))):
        source_id = str(source.get("id", ""))
        health = health_by_id.get(source_id, {})
        registered.append(
            {
                "id": source_id,
                "url": str(source.get("url", "")),
                "authority_class": source.get("authority_class"),
                "source_type": str(source.get("source_type", "")),
                "health_status": str(health.get("status", "missing")),
            }
        )
    return {
        "exam_code": str(exam["code"]),
        "vendor_id": str(exam["vendor_id"]),
        "title": str(exam["title"]),
        "exam_status": str(exam["status"]),
        "upcoming_change_status": str(exam["upcoming_change_status"]),
        "blueprint_last_checked": str(exam["blueprint_last_checked"]),
        "guide_path": guide_path,
        "official_blueprint": str(exam["study_guide_url"]),
        "blueprint_snapshot_path": snapshot_path,
        "blueprint_snapshot_sha256": actual_hash,
        "official_status_snapshot_path": (
            status_snapshot_path if (ROOT / status_snapshot_path).is_file() else None
        ),
        "source_validation_review_id": str(review["id"]),
        "registered_sources": registered,
        "risk_score": score,
        "risk_factors": factors,
        "verify_current_markers": guide_text.count("VERIFY CURRENT"),
    }


def select_items(
    exams: list[dict[str, object]],
    reviews_by_code: dict[str, dict[str, object]],
    sources_by_exam: dict[str, list[dict[str, object]]],
    health_by_id: dict[str, dict[str, object]],
    completed: set[tuple[str, str, int]],
    rubric_version: int,
    size: int,
    explicit_codes: list[str],
) -> list[dict[str, object]]:
    exam_by_code = {str(exam["code"]): exam for exam in exams}
    if explicit_codes:
        unknown = [code for code in explicit_codes if code not in exam_by_code]
        if unknown:
            raise ValueError("Unknown exam codes: " + ", ".join(unknown))
        selected_exams = [exam_by_code[code] for code in explicit_codes]
    else:
        selected_exams = exams

    items: list[dict[str, object]] = []
    for exam in selected_exams:
        code = str(exam["code"])
        review = reviews_by_code.get(code)
        if review is None:
            raise ValueError(f"No current passed source-validation review for {code}")
        item = build_manifest_item(
            exam,
            review,
            sources_by_exam.get(code, []),
            health_by_id,
        )
        audit_key = (code, str(item["blueprint_snapshot_sha256"]), rubric_version)
        if not explicit_codes and audit_key in completed:
            continue
        items.append(item)

    if not explicit_codes:
        items.sort(
            key=lambda item: (
                -int(item["risk_score"]),
                -date.fromisoformat(str(item["blueprint_last_checked"])).toordinal(),
                str(item["vendor_id"]),
                natural_key(item["exam_code"]),
            )
        )
    return items[:size]


def build_manifest(
    batch_id: str,
    items: list[dict[str, object]],
    rubric_version: int,
    explicit: bool,
) -> dict[str, object]:
    return {
        "batch_id": batch_id,
        "generated_on": date.today().isoformat(),
        "rubric_version": rubric_version,
        "audit_mode": "read-only",
        "selection_method": (
            "explicit exam-code pilot or verification batch"
            if explicit
            else "unaudited current-snapshot guides ordered by deterministic risk score"
        ),
        "rubric_path": "docs/AI-AUDIT.md",
        "catalog_paths": {
            "exams": "config/exams.json",
            "certification_seeds": "config/certification-seeds.json",
            "reviews": "data/reviews.json",
            "sources": "data/sources.json",
            "source_health": "data/source-health.json",
            "completed_ai_audits": "data/ai-audits.json",
        },
        "items": items,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--exam-code", action="append", default=[])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--exams", type=Path, default=DEFAULT_EXAMS)
    parser.add_argument("--reviews", type=Path, default=DEFAULT_REVIEWS)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--source-health", type=Path, default=DEFAULT_SOURCE_HEALTH)
    parser.add_argument("--audits", type=Path, default=DEFAULT_AUDITS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not re.fullmatch(r"[a-z0-9-]+", args.batch_id):
        raise ValueError("Batch id must contain lowercase letters, digits, and hyphens")
    if not 1 <= args.size <= MAX_BATCH_SIZE:
        raise ValueError(f"Batch size must be between 1 and {MAX_BATCH_SIZE}")
    if len(args.exam_code) > MAX_BATCH_SIZE:
        raise ValueError(
            f"Explicit batches may contain at most {MAX_BATCH_SIZE} guides"
        )
    if len(args.exam_code) != len(set(args.exam_code)):
        raise ValueError("Explicit batch contains duplicate exam codes")

    exams_data = load_json(args.exams)
    reviews_data = load_json(args.reviews)
    sources_data = load_json(args.sources)
    health_data = load_json(args.source_health)
    audits_data = load_json(args.audits)
    rubric_version = audits_data.get("rubric_version")
    if not isinstance(rubric_version, int):
        raise ValueError("Audit catalog needs an integer rubric_version")

    exams = [item for item in exams_data.get("exams", []) if isinstance(item, dict)]
    reviews = [
        item for item in reviews_data.get("reviews", []) if isinstance(item, dict)
    ]
    sources = [
        item for item in sources_data.get("sources", []) if isinstance(item, dict)
    ]
    health_rows = [
        item for item in health_data.get("sources", []) if isinstance(item, dict)
    ]
    reviews_by_code = current_source_reviews(reviews, exams)
    sources_by_exam, health_by_id = source_indexes(sources, health_rows)
    completed = completed_current_audits(audits_data)
    size = len(args.exam_code) if args.exam_code else args.size
    items = select_items(
        exams,
        reviews_by_code,
        sources_by_exam,
        health_by_id,
        completed,
        rubric_version,
        size,
        args.exam_code,
    )
    manifest = build_manifest(
        args.batch_id, items, rubric_version, bool(args.exam_code)
    )
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
        print(f"AI audit batch preparation failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
