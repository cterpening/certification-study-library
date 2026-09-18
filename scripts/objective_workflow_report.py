#!/usr/bin/env python3
"""Render actionable objective-monitor PR and failure descriptions."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def pull_request_body(report: dict) -> str:
    changed = ", ".join(report.get("changed", [])) or "See the attached report"
    return (
        f"The objective monitor detected changes to: **{changed}**.\n\n"
        "Review the objective and status snapshot diff against each provider's official "
        "sources. Update the affected guide's baseline, lifecycle warnings, objective map, "
        "weights, terminology, labs, and readiness checklist as needed. Snapshot changes "
        "require content review before merging.\n"
    )


def failure_body(report: dict | None, steps: dict, run_url: str, branch_url: str,
                 pr_error: str = "") -> str:
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
    if steps.get("snapshot_pr", {}).get("outcome") == "failure":
        lines.extend(["", "The snapshot publication step failed. Inspect its logs and the diagnostic artifact.",
                      f"If the branch push succeeded, review or create the pull request here: {branch_url}"])
    if "GitHub Actions is not permitted to create or approve pull requests" in pr_error:
        lines.extend(["", "GitHub rejected PR creation because workflow-created pull requests are disabled. "
                      "An administrator can enable **Settings → Actions → General → Workflow permissions → "
                      "Allow GitHub Actions to create and approve pull requests**, subject to organization policy. "
                      "Alternatively, a maintainer can create the PR from the branch link above. "
                      "Adding `pull-requests: write` alone does not override this setting."])
    lines.extend(["", "The `objective-monitor-report` artifact retains the report and available snapshot patch. "
                  "Review changes against official sources before merging; documented manual-review limitations "
                  "remain separate from unexpected failures.", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("pull-request", "failure"))
    parser.add_argument("--report", type=Path, default=Path("objective-report.json"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pr-error", type=Path, default=Path("objective-pr-error.txt"))
    args = parser.parse_args()
    report = None
    if args.report.exists():
        try:
            report = json.loads(args.report.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            if args.kind == "pull-request":
                raise
    if args.kind == "pull-request":
        if report is None:
            raise ValueError("An objective report is required to describe snapshot changes")
        body = pull_request_body(report)
    else:
        server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
        repository = os.environ["GITHUB_REPOSITORY"]
        run_id = os.environ["GITHUB_RUN_ID"]
        base = f"{server}/{repository}"
        body = failure_body(
            report, json.loads(os.environ.get("WORKFLOW_STEPS", "{}")),
            f"{base}/actions/runs/{run_id}",
            f"{base}/pull/new/automation/objective-update-{run_id}",
            args.pr_error.read_text(encoding="utf-8") if args.pr_error.exists() else "",
        )
    args.output.write_text(body, encoding="utf-8")


if __name__ == "__main__":
    main()
