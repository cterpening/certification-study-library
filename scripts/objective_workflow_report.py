#!/usr/bin/env python3
"""Render actionable objective-monitor review and failure descriptions."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def changes_body(report: dict, run_url: str) -> str:
    lines = ["# Certification objective changes to review", "", f"Workflow run and candidate diff: {run_url}", "",
             "These are detected differences, not accepted exam updates. Review each official source and "
             "update its guide and snapshot separately. Close this task only after the affected exams have "
             "been reviewed or explicitly deferred with a reason.", ""]
    for row in report.get("results", []):
        if row.get("status") != "changed":
            continue
        kinds = []
        if row.get("objectives_changed"):
            kinds.append("objectives")
        if row.get("status_changed"):
            kinds.append("exam status")
        lines.append(f"- [ ] **{row['code']}** ({', '.join(kinds)}): [official source](<{row['url']}>)")
    lines.append("")
    return "\n".join(lines)


def failure_body(report: dict | None, steps: dict, run_url: str) -> str:
    lines = ["# Certification objective workflow needs attention", "", f"Workflow run: {run_url}", ""]
    failed = [name for name, step in steps.items() if step.get("outcome") == "failure"]
    if failed:
        lines.extend(["Failed steps: " + ", ".join(f"`{name}`" for name in failed), ""])
    if report is None:
        lines.append("No objective report was produced. Inspect setup, tests, and monitor execution in the run logs.")
    else:
        errors = report.get("errors", [])
        if errors:
            lines.append("Objective retrieval/extraction failed for: **" + ", ".join(errors) + "**.")
        else:
            lines.append("Objective retrieval/extraction completed with **zero unexpected errors**.")
        lines.append(f"Detected changes: {len(report.get('changed', []))}; documented manual-review limitations: {len(report.get('manual_review', []))}.")
    lines.extend(["", "The `objective-monitor-report` artifact retains the report and available snapshot patch. "
                  "Review one affected exam at a time against its official source before accepting a snapshot or guide change; documented manual-review limitations "
                  "remain separate from unexpected failures.", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=("failure", "changes"), default="failure")
    parser.add_argument("--report", type=Path, default=Path("objective-report.json"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = None
    if args.report.exists():
        try:
            report = json.loads(args.report.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            pass
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repository = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    run_url = f"{server}/{repository}/actions/runs/{run_id}"
    if args.kind == "changes":
        if report is None:
            raise ValueError("An objective report is required to describe detected changes")
        body = changes_body(report, run_url)
    else:
        body = failure_body(
            report, json.loads(os.environ.get("WORKFLOW_STEPS", "{}")), run_url,
        )
    args.output.write_text(body, encoding="utf-8")


if __name__ == "__main__":
    main()
