#!/usr/bin/env python3
"""Collect official-source checks and produce an actionable row for every guide.

Live runs write candidate snapshots only into a new output directory. Accepted
snapshots, source review dates, certification status and guide prose are never
changed. --reports-dir assembles an existing run without making network requests.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

from check_certification_discovery import safe


ROOT = Path(__file__).resolve().parents[1]
REPORT_FILES = {
    "objectives": "objective-report.json",
    "discovery": "certification-discovery-report.json",
    "health": "source-health-report.json",
}


def inventory_hashes() -> dict[str, str]:
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in (
        "config/exams.json", "config/certification-discovery.json", "data/sources.json",
    )}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect(output: Path, mode: str) -> dict[str, int]:
    """Run sequentially so the monitors do not compete against the same host."""
    if output.exists():
        raise ValueError("Live output directory already exists; choose a new directory to avoid stale reports")
    collected_inventory = inventory_hashes()
    output.mkdir(parents=True)
    candidate = output / "objective-snapshots"
    shutil.copytree(ROOT / "data/objective-snapshots", candidate)
    commands = {
        "objectives": ["check_official_study_guides.py", "--write", "--snapshot-dir", str(candidate),
                       "--report", str(output / REPORT_FILES["objectives"])],
        "discovery": ["check_certification_discovery.py", "--mode", mode,
                      "--report", str(output / REPORT_FILES["discovery"]),
                      "--markdown-report", str(output / "certification-discovery-report.md")],
        "health": ["check_source_health.py", "--max-workers", "3",
                   "--report", str(output / REPORT_FILES["health"]),
                   "--markdown-report", str(output / "source-health-report.md")],
    }
    exits = {}
    for name, args in commands.items():
        print(f"Checking {name}; progress in {output / (name + '.log')}", flush=True)
        with (output / f"{name}.log").open("w", encoding="utf-8") as log:
            try:
                completed = subprocess.run(
                    [sys.executable, "-X", "utf8", str(ROOT / "scripts" / args[0]), *args[1:]],
                    cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, timeout=2400,
                    check=False,
                )
                exits[name] = completed.returncode
            except subprocess.TimeoutExpired:
                log.write("\nMonitor exceeded its 40-minute limit.\n")
                exits[name] = 124
    (output / "collection.json").write_text(json.dumps({
        "checked_on": date.today().isoformat(),
        "completed_at": datetime.now(timezone.utc).isoformat(), "exit_codes": exits,
        "inventory_sha256": collected_inventory,
    }, indent=2) + "\n", encoding="utf-8")
    return exits


def build_report(exams: list[dict], sources: list[dict], reports: dict,
                 policy: dict, today: date, collection_errors: list[str] | None = None) -> dict:
    errors = list(collection_errors or [])
    for name in REPORT_FILES:
        if name not in reports:
            errors.append(f"Missing {name} report; this channel was not checked")
    for name in ("health", "discovery"):
        checked = reports.get(name, {}).get("checked_on")
        if name in reports and checked != today.isoformat():
            errors.append(f"{name} report is dated {checked}; expected {today.isoformat()}")

    objective_rows = reports.get("objectives", {}).get("results", [])
    objectives = {row["code"]: row for row in objective_rows}
    if len(objectives) != len(objective_rows):
        errors.append("Duplicate exam codes in objective report")
    health_rows = reports.get("health", {}).get("results", [])
    health = {row["id"]: row for row in health_rows}
    if len(health) != len(health_rows):
        errors.append("Duplicate source IDs in source-health report")
    expected_ids = {row["id"] for row in sources}
    if "health" in reports and set(health) != expected_ids:
        errors.append("Source-health coverage differs from the registered source inventory")
    findings = reports.get("health", {}).get("findings", {})
    changed_sources = {row["id"] for row in findings.get("changed", [])}
    stale_sources = {row["id"] for row in findings.get("stale", [])}
    events = policy.get("events", [])
    known_codes = {exam["code"] for exam in exams}
    for event in events:
        if not set(event["exam_codes"]) <= known_codes:
            raise ValueError(f"Unknown exam in maintenance event {event['id']}")
        date.fromisoformat(event["review_on"])

    rows = []
    for exam in exams:
        code = exam["code"]
        actions = []
        result = objectives.get(code)
        if exam["status"] == "retired":
            objective_status = "retired-baseline-preserved"
        elif result is None:
            objective_status = "not-checked"
            errors.append(f"{code}: no objective result")
        else:
            objective_status = result["status"]
            if result.get("url") != exam["study_guide_url"]:
                errors.append(f"{code}: objective result URL differs from the configured blueprint")
            if objective_status == "error":
                errors.append(f"{code}: {result.get('error', 'objective check failed')}")
        if objective_status not in {"unchanged", "retired-baseline-preserved"}:
            actions.append("Compare candidate objectives and status with the guide; resolve extraction failures explicitly")

        relevant = [s for s in sources if code in s.get("supported_exams", [])]
        source_issues = []
        for source in relevant:
            sid = source["id"]
            status = health.get(sid, {}).get("status", "not-checked")
            if status != "ok" or sid in changed_sources or sid in stale_sources:
                source_issues.append({"id": sid, "url": source["url"], "status": status,
                                      "metadata_changed": sid in changed_sources,
                                      "review_overdue": sid in stale_sources})
        if source_issues:
            actions.append("Review linked-source failures, access blocks and metadata changes")

        due_events = []
        for event in events:
            days = (date.fromisoformat(event["review_on"]) - today).days
            if code in event["exam_codes"] and days <= policy["lookahead_days"]:
                due_events.append(dict(event, days_until_review=days,
                                       timing="due" if days <= 0 else "upcoming"))
        if due_events:
            actions.append("Recheck dated vendor transitions; do not infer retirement or availability from the calendar")
        age = (today - date.fromisoformat(exam["upcoming_change_checked"])).days
        if age >= policy["lifecycle_review_days"] and exam["status"] != "retired":
            actions.append("Refresh credential-page lifecycle evidence; objective matches do not establish availability")
        catalogs = [row for row in reports.get("discovery", {}).get("sources", [])
                    if row["vendor_id"] == exam["vendor_id"] and row["status"] != "unchanged"]
        if catalogs:
            actions.append("Triage vendor catalog signals and any manual catalog review")
        rows.append({
            "code": code, "vendor_id": exam["vendor_id"], "guide_path": exam["guide_path"],
            "official_blueprint": exam["study_guide_url"], "catalog_status": exam["status"],
            "objective_status": objective_status,
            "objective_error": (result or {}).get("error"),
            "objective_sha256": (result or {}).get("current_sha256"),
            "status_sha256": (result or {}).get("current_status_sha256"),
            "source_count": len(relevant), "source_issues": source_issues,
            "catalog_signals": [{"id": s["id"], "status": s["status"]} for s in catalogs],
            "lifecycle_review_age_days": age, "events": due_events, "actions": actions,
        })
    if any(row["status"] == "error" for row in reports.get("discovery", {}).get("sources", [])):
        errors.append("One or more catalog checks failed")
    errors = list(dict.fromkeys(errors))
    return {
        "schema_version": 1, "checked_on": today.isoformat(),
        "scope": "Objective changes, catalog discovery, source health and dated maintenance tasks; not a technical or human review",
        "summary": {"guides": len(rows), "vendors": len({e["vendor_id"] for e in exams}),
                    "objective_outcomes": dict(Counter(row["objective_status"] for row in rows)),
                    "guides_with_actions": sum(bool(row["actions"]) for row in rows),
                    "source_health": reports.get("health", {}).get("summary", {}),
                    "catalog_outcomes": dict(Counter(s["status"] for s in reports.get("discovery", {}).get("sources", []))),
                    "collection_errors": len(errors)},
        "needs_review": bool(errors or any(row["actions"] for row in rows)
                             or reports.get("discovery", {}).get("needs_review")),
        "errors": errors, "exams": rows,
    }


def markdown(report: dict) -> str:
    summary = report["summary"]
    lines = [f"# Certification maintenance — {report['checked_on']}", "",
             f"{summary['guides']} guides across {summary['vendors']} vendors; "
             f"{summary['guides_with_actions']} guides have review tasks.", "",
             "An unchanged extraction is not a full guide validation. Blocked and missing checks remain visible. "
             "Candidate snapshots have not replaced accepted baselines or renewed review dates.", "",
             "## Dated review tasks", "",
             "| Review by | Exams | Task and official evidence |", "|---|---|---|"]
    seen = set()
    for row in report["exams"]:
        for event in row["events"]:
            if event["id"] in seen:
                continue
            seen.add(event["id"])
            lines.append(f"| {event['review_on']} ({event['timing']}) | {', '.join(event['exam_codes'])} | "
                         f"{safe(event['action'])} ([source]({event['url']})) |")
    lines += ["", "## Collection failures", ""]
    lines += [f"- {safe(error)}" for error in report["errors"]] or ["None."]
    lines += ["", "## Every published guide", "",
              "Source flags include access blocks and title changes; they are not all broken links. "
              "See maintenance-report.json for exact URLs, actions, hashes and catalog signals.", "",
              "| Exam | Objectives | Source flags | Catalog signals | Lifecycle review age (days) |",
              "|---|---|---:|---:|---:|"]
    for row in report["exams"]:
        lines.append(f"| [{row['code']}]({row['official_blueprint']}) | {row['objective_status']} | "
                     f"{len(row['source_issues'])} | {len(row['catalog_signals'])} | {row['lifecycle_review_age_days']} |")
    lines += ["", "## Apply a reviewed change", "",
              "1. Open canonical vendor evidence and inspect candidate snapshot diffs; distinguish future scope from current delivery.",
              "2. Update the affected guide, catalog metadata, registered sources and dated evidence together. Keep conflicts explicit.",
              "3. Run repository tests, repository validation, strict site build and generated-site validation.",
              "4. Accept only reviewed baselines with the corresponding guide change. Preserve historical full-review dates.",
              "5. Resolve or move dated tasks only after recording evidence. A passed date never automatically retires an exam.", ""]
    return "\n".join(lines)


def write_snapshot_diff(output: Path) -> None:
    candidate = output / "objective-snapshots"
    if not candidate.exists():
        return
    differences = []
    for path in sorted(candidate.iterdir()):
        if not path.is_file():
            continue
        previous = ROOT / "data/objective-snapshots" / path.name
        before = previous.read_text(encoding="utf-8").splitlines(keepends=True) if previous.exists() else []
        differences.extend(difflib.unified_diff(before, path.read_text(encoding="utf-8").splitlines(keepends=True),
                                              fromfile=f"accepted/{path.name}", tofile=f"candidate/{path.name}"))
    (output / "objective-candidates.diff").write_text("".join(differences), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output-dir", type=Path, help="New directory for a complete live run")
    group.add_argument("--reports-dir", type=Path, help="Assemble existing reports; no network access")
    parser.add_argument("--mode", choices=("weekly", "monthly"), default="monthly")
    args = parser.parse_args()
    output = (args.output_dir or args.reports_dir).resolve()
    if output == ROOT or ROOT / "data" == output or (ROOT / "data") in output.parents:
        parser.error("Output must not be the repository root or trusted data directory")
    if args.output_dir:
        try:
            collect(output, args.mode)
        except ValueError as exc:
            parser.error(str(exc))
    output.mkdir(parents=True, exist_ok=True)
    reports = {}
    errors = []
    for name, filename in REPORT_FILES.items():
        path = output / filename
        if path.exists():
            try:
                reports[name] = read_json(path)
            except (ValueError, OSError) as exc:
                errors.append(f"Invalid {name} report: {exc}")
    receipt = output / "collection.json"
    if receipt.exists():
        collection = read_json(receipt)
        if collection.get("checked_on") != date.today().isoformat():
            errors.append("Collection receipt is not from today; rerun live checks")
        if collection.get("inventory_sha256") != inventory_hashes():
            errors.append("Collection inventory differs from current configuration; recollect affected channels")
        errors.extend(f"{name} exited {code}; inspect {name}.log" for name, code in collection.get("exit_codes", {}).items() if code)
    else:
        errors.append("No collection receipt; objective report freshness is unverified")
    report = build_report(read_json(ROOT / "config/exams.json")["exams"],
                          read_json(ROOT / "data/sources.json")["sources"], reports,
                          read_json(ROOT / "config/certification-maintenance.json"), date.today(), errors)
    (output / "maintenance-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output / "maintenance-report.md").write_text(markdown(report), encoding="utf-8")
    write_snapshot_diff(output)
    print(json.dumps(report["summary"], indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
