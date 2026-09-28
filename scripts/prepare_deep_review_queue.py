#!/usr/bin/env python3
"""Prepare content-review work without confusing monitor checks with completed reviews."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, timedelta
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MICROSOFT_VENDORS = ("microsoft", "microsoft-office")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def guide_hash(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def validate_records(root: Path, exams: list[dict], program: dict) -> None:
    known = {e["code"]: e for e in exams}
    seen = set()
    for record in program["reviews"]:
        key = (record["exam_code"], record["reviewed_on"], record["guide_sha256"])
        if key in seen or record["exam_code"] not in known:
            raise ValueError(f"Duplicate or unknown deep-review record: {key}")
        seen.add(key)
        date.fromisoformat(record["reviewed_on"])
        for relative in [record["report_path"], *record["evidence_paths"]]:
            path = (root / relative).resolve()
            if root.resolve() not in path.parents or not path.is_file():
                raise ValueError(f"Missing or escaping review evidence: {relative}")
        if not record["evidence_paths"] or not record["objective_count"]:
            raise ValueError(f"Review needs objective and evidence records: {key}")


def build_queue(root: Path, exams: list[dict], program: dict, events: list[dict],
                today: date, vendors: list[str], size: int = 3) -> dict:
    if not 1 <= size <= 12:
        raise ValueError("Review batch size must be between 1 and 12")
    if set(vendors) - {e["vendor_id"] for e in exams}:
        raise ValueError("Unknown vendor filter")
    validate_records(root, exams, program)
    latest = {}
    for record in sorted(program["reviews"], key=lambda r: r["reviewed_on"], reverse=True):
        if date.fromisoformat(record["reviewed_on"]) <= today:
            latest.setdefault(record["exam_code"], record)
    rows = []
    for exam in exams:
        if exam["vendor_id"] not in vendors:
            continue
        record = latest.get(exam["code"])
        current_hash = guide_hash(root / exam["guide_path"])
        age = (today - date.fromisoformat(record["reviewed_on"])).days if record else None
        if exam["status"] == "retired":
            state = "archived"
        elif not record:
            state = "pending"
        elif record["guide_sha256"] != current_hash:
            state = "changed-since-review"
        elif record["outcome"] == "reviewed-with-blockers":
            state = "reviewed-with-blockers"
        elif age >= program["review_interval_days"]:
            state = "review-due"
        else:
            state = "reviewed"
        scheduled = [dict(e, days=(date.fromisoformat(e["review_on"]) - today).days)
                     for e in events if exam["code"] in e["exam_codes"]]
        upcoming = [e for e in scheduled if e["days"] <= 30]
        later_events = [e for e in scheduled if not record or e["review_on"] > record["reviewed_on"]]
        nearest = min((e["days"] for e in later_events if e["days"] <= 30), default=None)
        reasons = [state]
        priority = {"pending": 300, "changed-since-review": 250, "review-due": 150,
                    "reviewed-with-blockers": 100, "reviewed": 0, "archived": 0}[state]
        if nearest is not None and state != "archived":
            priority += 400 - min(max(nearest, 0), 30) * 5
            reasons.append(f"dated-event:{nearest} days")
        if exam["status"] in {"beta", "changing"}:
            priority += 75
            reasons.append(f"exam-status:{exam['status']}")
        # A receipt covers the review dates on or before its own date. Keep those
        # events and unresolved blockers visible without scheduling the same work
        # on every monitor run. A later event, changed guide, or interval expiry
        # makes the guide eligible again; this does not resolve a blocker.
        due_event = any(e["days"] <= 0 for e in later_events)
        needs_review = state != "archived" and (state != "reviewed" or due_event)
        ready_for_review = state != "archived" and (
            state in {"pending", "changed-since-review", "review-due"}
            or due_event or (age is not None and age >= program["review_interval_days"]))
        next_review_on = None
        if ready_for_review:
            next_review_on = today.isoformat()
        elif state != "archived" and record:
            interval_date = date.fromisoformat(record["reviewed_on"]) + timedelta(days=program["review_interval_days"])
            next_review_on = min([interval_date, *[date.fromisoformat(e["review_on"]) for e in later_events]]).isoformat()
        rows.append({"exam_code": exam["code"], "title": exam["title"], "vendor_id": exam["vendor_id"],
                     "guide_path": exam["guide_path"], "official_blueprint": exam["study_guide_url"],
                     "current_guide_sha256": current_hash, "state": state, "needs_review": needs_review,
                     "ready_for_review": ready_for_review, "next_review_on": next_review_on,
                     "reviewed_on": record["reviewed_on"] if record else None,
                     "report_path": record["report_path"] if record else None,
                     "lab_execution": record["lab_execution"] if record else "not-recorded",
                     "remaining_limits": record["remaining_limits"] if record else [],
                     "priority": priority, "reasons": reasons, "events": upcoming})
    rows.sort(key=lambda r: (-r["priority"], r["exam_code"]))
    selected = [r for r in rows if r["ready_for_review"]][:size]
    return {"schema_version": 1, "generated_on": today.isoformat(), "program_started_on": program["started_on"],
            "scope": "Recorded deep reviews in this program, separate from historical source validation, live labs and automated monitoring.",
            "summary": {"guides": len(rows), "states": dict(Counter(r["state"] for r in rows)),
                        "needs_review": sum(r["needs_review"] for r in rows),
                        "ready_for_review": sum(r["ready_for_review"] for r in rows)},
            "next_batch": [r["exam_code"] for r in selected], "exams": rows}


def render(report: dict, public: bool = False) -> str:
    lines = ["# Microsoft deep-review progress", "", f"As of {report['generated_on']}; program started {report['program_started_on']}.", "",
             report["scope"], "", f"{report['summary']['guides']} guides; {report['summary']['needs_review']} have review work or unresolved blockers; {report['summary']['ready_for_review']} are eligible for review now.", "",
             "Next batch: " + (", ".join(report["next_batch"]) or "none due") + ".", "",
             "A reviewed guide can still have unexecuted labs. Blockers stay visible. Recently reviewed guides wait for a later dated event or the review interval; changed guide text returns immediately. Events dated on or before the latest review remain visible in the work packet but do not repeatedly schedule that same review. Set a later review date for an unresolved event that needs another check.", "",
             "| Exam | Deep-review state | Reviewed | Next eligible review | Lab execution |", "|---|---|---|---|---|"]
    for row in report["exams"]:
        label = f"[{row['exam_code']}](../{row['guide_path']})" if public else row["exam_code"]
        lines.append(f"| {label} | {row['state']} | {row['reviewed_on'] or 'Pending'} | {row['next_review_on'] or 'Archived'} | {row['lab_execution']} |")
    lines += ["", "## Completion rule", "",
              "Read the entire guide and map each detailed objective; inspect official lifecycle, product and release evidence; evaluate useful supplementary articles; apply supported corrections and learning examples; register sources and limitations; run the shared validation gate; then record a review receipt and commit/push that exam's changes.", "",
              "A successful URL check, unchanged objective extraction, or generated work packet never creates a completed receipt. Human review and live lab execution are separate claims. Open each linked guide's review report for unresolved limitations; reviewed-with-blockers records completed research with outstanding evidence gaps, not a clean validation pass.", ""]
    return "\n".join(lines)


def write_queue(root: Path, output: Path, today: date, vendors: list[str], size: int = 3) -> dict:
    exams = load(root / "config/exams.json")["exams"]
    program = load(root / "data/deep-reviews.json")
    events = load(root / "config/certification-maintenance.json")["events"]
    report = build_queue(root, exams, program, events, today, vendors, size)
    output.mkdir(parents=True, exist_ok=True)
    (output / "review-queue.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output / "review-queue.md").write_text(render(report), encoding="utf-8")
    sources = load(root / "data/sources.json")["sources"]
    candidates = load(root / "data/source-candidates.json")["candidates"]
    packets = []
    for code in report["next_batch"]:
        row = next(r for r in report["exams"] if r["exam_code"] == code)
        packets.append(dict(row,
            registered_sources=[s for s in sources if code in s.get("supported_exams", [])],
            queued_candidates=[s for s in candidates if code in s.get("suggested_exams", []) and s["review_status"] == "queued"],
            required_review=["complete guide and detailed objective mapping", "official lifecycle, product documentation and release channels",
                             "useful named blogs with dates, strengths, limitations and corroboration", "original learning examples, labs and answer checkpoints",
                             "source/catalog/review/evidence updates", "validation, then one certification commit and push"],
            lab_boundary="Record offline, tabletop and vendor-service execution separately. Do not claim missing credentials or unexecuted infrastructure as tested."))
    (output / "next-batch.json").write_text(json.dumps(packets, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--vendor-id", action="append")
    parser.add_argument("--size", type=int, default=3)
    parser.add_argument("--publish-status", action="store_true", help="Explicitly refresh the checked-in Microsoft progress page")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    if output == ROOT or ROOT / "data" == output or ROOT / "data" in output.parents:
        parser.error("Use a separate report output directory")
    vendors = args.vendor_id or list(MICROSOFT_VENDORS)
    report = write_queue(ROOT, output, date.today(), vendors, args.size)
    if args.publish_status:
        if set(vendors) != set(MICROSOFT_VENDORS):
            parser.error("The public Microsoft progress page requires microsoft and microsoft-office")
        (ROOT / "docs/MICROSOFT-REVIEW-STATUS.md").write_text(render(report, public=True), encoding="utf-8")
    print(json.dumps({"summary": report["summary"], "next_batch": report["next_batch"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
