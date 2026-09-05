#!/usr/bin/env python3
"""Validate catalogs, guide metadata, Markdown fences, and local links."""

from __future__ import annotations

from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
REVIEW_STATES = {
    "ai-generated-draft",
    "source-validated",
    "community-reviewed",
    "review-required",
    "retired",
}
EXAM_STATUSES = {"active", "beta", "changing", "retired"}
EXAM_LEVELS = {"beginner", "intermediate", "expert"}
UPCOMING_CHANGE_STATUSES = {
    "none-announced",
    "scheduled",
    "retirement-announced",
}
SOURCE_CANDIDATE_STATES = {"queued", "in-review", "rejected"}
SOURCE_ACCESS_MODELS = {"public", "free-account", "partner-restricted", "paid"}
OBJECTIVE_ADAPTERS = {
    "microsoft-learn",
    "microsoft-office-specialist",
    "ibm-certification",
    "oracle-learning-path",
    "hashicorp-developer",
    "databricks-certification",
    "aws-exam-guide",
    "comptia-certification",
    "red-hat-exam",
    "linux-foundation-certification",
    "google-cloud-certification",
    "cisco-certification",
    "snowflake-certification",
    "isc2-certification",
    "nvidia-certification",
    "salesforce-certification",
    "mongodb-certification",
    "servicenow-certification",
    "palo-alto-networks-certification",
    "fortinet-certification",
    "splunk-certification",
    "isaca-certification",
    "python-institute-certification",
    "cpp-institute-certification",
    "js-institute-certification",
}
SOURCE_VALIDATION_CHECKS = {
    "official_objectives_mapped",
    "material_claims_sourced",
    "volatile_claims_labeled",
    "links_and_local_references_valid",
    "exam_integrity_policy_passed",
}
AI_AUDIT_CHECKS = {
    "official_scope",
    "objective_coverage",
    "material_claim_support",
    "exam_contract_integrity",
    "technical_coherence",
    "volatility_and_lifecycle",
    "lab_safety_and_feasibility",
    "readiness_check_quality",
    "review_evidence_accuracy",
    "duplication_and_contamination",
}
AI_AUDIT_CHECK_STATES = {"passed", "failed", "blocked", "not-applicable"}
AI_AUDIT_VERDICTS = {"pass", "pass-with-notes", "fix-required", "blocked"}
AI_AUDIT_SEVERITIES = {"info", "low", "medium", "high", "critical"}
AI_AUDIT_FINDING_STATES = {"open", "resolved", "accepted-risk", "dismissed"}
AI_AUDIT_CATEGORIES = {
    "scope-gap",
    "unsupported-claim",
    "technical-error",
    "stale-content",
    "source-mismatch",
    "exam-contract",
    "lab-safety",
    "readiness-check",
    "review-evidence",
    "duplication",
    "cross-vendor-contamination",
    "accessibility",
    "other",
}
AI_AUDIT_MAX_BATCH_SIZE = 12
GUIDE_METADATA = {
    "exam_code",
    "vendor_id",
    "official_blueprint",
    "content_basis",
    "generation_method",
    "authority",
    "review_status",
    "last_verified",
    "upcoming_change_status",
    "upcoming_change_checked",
}
IGNORED_MARKDOWN_DIRS = {".git", ".site-build", ".venv", "site", "__pycache__"}
IGNORED_MARKDOWN_FILES = {Path("docs/initialChat.md")}
CERTIFICATION_LIST_PATH = ROOT / "CERTIFICATIONS.txt"
CERTIFICATION_LIST_COLUMNS = (
    "vendor_id",
    "exam_code",
    "title",
)
CERTIFICATION_SEED_STATUSES = {
    "active",
    "beta",
    "legacy",
    "retirement-announced",
    "retired",
}


def markdown_heading_levels(markdown: str) -> list[int]:
    """Return Markdown heading levels while ignoring fenced code examples."""

    levels: list[int] = []
    fence_marker: str | None = None
    for line in markdown.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)[0]
            if fence_marker is None:
                fence_marker = marker
            elif fence_marker == marker:
                fence_marker = None
            continue
        if fence_marker is not None:
            continue
        heading = re.match(r"^(#{1,6})\s+", line)
        if heading:
            levels.append(len(heading.group(1)))
    return levels


def render_certification_list(certifications: object) -> str:
    """Render stable query seeds for downstream enrichment scripts."""
    lines = ["\t".join(CERTIFICATION_LIST_COLUMNS)]
    if not isinstance(certifications, list):
        return "\n".join(lines) + "\n"

    catalog_keys = (
        "vendor_id",
        "exam_code",
        "title",
    )
    for certification in certifications:
        if not isinstance(certification, dict):
            continue
        values = []
        for key in catalog_keys:
            value = certification.get(key, "")
            text = value if isinstance(value, str) else str(value)
            values.append(
                text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
            )
        lines.append("\t".join(values))
    return "\n".join(lines) + "\n"


def validate_certification_seed_catalog(
    seed_data: dict[str, object],
    exams: list[object],
    vendor_ids: set[str],
    errors: list[str],
) -> None:
    """Validate the broader research inventory and its generated TSV export."""
    catalog_sources = seed_data.get("catalog_sources", [])
    certifications = seed_data.get("certifications", [])
    if not isinstance(catalog_sources, list) or not catalog_sources:
        errors.append(
            "config/certification-seeds.json must contain a non-empty "
            "catalog_sources array"
        )
        return
    if not isinstance(certifications, list) or not certifications:
        errors.append(
            "config/certification-seeds.json must contain a non-empty "
            "certifications array"
        )
        return

    source_vendors: dict[str, str] = {}
    for source in catalog_sources:
        if not isinstance(source, dict):
            errors.append("Each certification seed catalog source must be an object")
            continue
        source_id = source.get("id")
        vendor_id = source.get("vendor_id")
        if not isinstance(source_id, str) or not source_id:
            errors.append("Each certification seed catalog source needs an id")
            continue
        if source_id in source_vendors:
            errors.append(f"Duplicate certification seed source id: {source_id}")
            continue
        if vendor_id not in vendor_ids:
            errors.append(
                f"Certification seed source {source_id} uses unknown vendor: "
                f"{vendor_id}"
            )
        if not valid_public_url(source.get("catalog_url")):
            errors.append(
                f"Certification seed source {source_id} needs a public catalog URL"
            )
        if not isinstance(source.get("selection"), str) or not source["selection"]:
            errors.append(
                f"Certification seed source {source_id} needs a selection rule"
            )
        if not valid_date(source.get("last_verified")):
            errors.append(
                f"Certification seed source {source_id} has an invalid "
                "last_verified date"
            )
        source_vendors[source_id] = str(vendor_id)

    seed_keys: set[tuple[str, str]] = set()
    replacement_refs: list[tuple[str, str, str]] = []
    for certification in certifications:
        if not isinstance(certification, dict):
            errors.append("Each certification seed must be an object")
            continue
        vendor_id = certification.get("vendor_id")
        exam_code = certification.get("exam_code")
        title = certification.get("title")
        source_id = certification.get("source_id")
        if not isinstance(vendor_id, str) or vendor_id not in vendor_ids:
            errors.append(
                f"Certification seed {exam_code} uses unknown vendor: {vendor_id}"
            )
            continue
        if not isinstance(exam_code, str) or not re.fullmatch(
            r"[A-Z0-9][A-Z0-9-]+", exam_code
        ):
            errors.append(f"Invalid certification seed exam code: {exam_code}")
            continue
        key = (vendor_id, exam_code)
        if key in seed_keys:
            errors.append(f"Duplicate certification seed: {vendor_id}/{exam_code}")
        seed_keys.add(key)
        if not isinstance(title, str) or not title:
            errors.append(f"Certification seed {exam_code} needs a title")
        if not valid_public_url(certification.get("official_url")):
            errors.append(f"Certification seed {exam_code} needs an official URL")
        status = certification.get("status")
        if status not in CERTIFICATION_SEED_STATUSES:
            errors.append(f"Certification seed {exam_code} has an invalid status")
        retirement_date = certification.get("retirement_date")
        if status in {"retirement-announced", "retired"}:
            if not valid_date(retirement_date):
                errors.append(
                    f"Certification seed {exam_code} needs a retirement_date "
                    f"when status is {status}"
                )
        elif retirement_date is not None:
            errors.append(
                f"Certification seed {exam_code} has retirement_date without a "
                "retirement lifecycle status"
            )
        replacement_code = certification.get("replacement_exam_code")
        replacement_url = certification.get("replacement_official_url")
        if (replacement_code is None) != (replacement_url is None):
            errors.append(
                f"Certification seed {exam_code} must provide replacement_exam_code "
                "and replacement_official_url together"
            )
        elif replacement_code is not None:
            if not isinstance(replacement_code, str) or not re.fullmatch(
                r"[A-Z][A-Z0-9-]+", replacement_code
            ):
                errors.append(
                    f"Certification seed {exam_code} has an invalid replacement exam code"
                )
            elif not valid_public_url(replacement_url):
                errors.append(
                    f"Certification seed {exam_code} needs a public replacement URL"
                )
            else:
                replacement_refs.append((vendor_id, exam_code, replacement_code))
        if not isinstance(source_id, str) or source_id not in source_vendors:
            errors.append(
                f"Certification seed {exam_code} references unknown source: "
                f"{source_id}"
            )
        elif source_vendors[source_id] != vendor_id:
            errors.append(
                f"Certification seed {exam_code} and source {source_id} use "
                "different vendors"
            )

    for vendor_id, exam_code, replacement_code in replacement_refs:
        if (vendor_id, replacement_code) not in seed_keys:
            errors.append(
                f"Certification seed {exam_code} references replacement "
                f"{replacement_code}, which is not in the seed catalog"
            )

    published_keys = {
        (str(exam.get("vendor_id")), str(exam.get("code")))
        for exam in exams
        if isinstance(exam, dict)
    }
    missing_published = published_keys.difference(seed_keys)
    if missing_published:
        errors.append(
            "Certification seed catalog is missing published guides: "
            + ", ".join(
                f"{vendor_id}/{exam_code}"
                for vendor_id, exam_code in sorted(missing_published)
            )
        )

    expected_certification_list = render_certification_list(certifications)
    try:
        actual_certification_list = CERTIFICATION_LIST_PATH.read_text(
            encoding="utf-8"
        )
    except OSError as exc:
        errors.append(f"Unable to read CERTIFICATIONS.txt: {exc}")
    else:
        if actual_certification_list != expected_certification_list:
            errors.append(
                "CERTIFICATIONS.txt is stale; run "
                "python scripts/generate_certification_list.py"
            )


def load_json(path: Path, errors: list[str]) -> dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"Expected a JSON object in {path.relative_to(ROOT)}")
        return {}
    return data


def valid_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def valid_public_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def parse_front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def validate_source_candidates(
    candidates: object,
    source_ids: set[str],
    source_urls: set[str],
    exam_codes: set[str],
    errors: list[str],
) -> None:
    if not isinstance(candidates, list):
        errors.append("data/source-candidates.json must contain a candidates array")
        return

    candidate_ids: set[str] = set()
    candidate_urls: set[str] = set()
    required = {
        "id",
        "title",
        "url",
        "added_on",
        "suggested_exams",
        "reason",
        "review_status",
    }
    for candidate in candidates:
        if not isinstance(candidate, dict):
            errors.append("Each source candidate must be an object")
            continue
        candidate_id = candidate.get("id", "<unknown>")
        missing = required.difference(candidate)
        if missing:
            errors.append(
                f"Source candidate {candidate_id} missing fields: "
                + ", ".join(sorted(missing))
            )
            continue
        if not isinstance(candidate_id, str) or not re.fullmatch(
            r"[a-z0-9-]+", candidate_id
        ):
            errors.append(f"Source candidate has invalid id: {candidate_id}")
            continue
        if candidate_id in candidate_ids:
            errors.append(f"Duplicate source candidate id: {candidate_id}")
        if candidate_id in source_ids:
            errors.append(f"Source candidate id already approved: {candidate_id}")
        candidate_ids.add(candidate_id)

        title = candidate.get("title")
        reason = candidate.get("reason")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"Source candidate {candidate_id} needs a title")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"Source candidate {candidate_id} needs a reason")
        if not valid_date(candidate.get("added_on")):
            errors.append(f"Source candidate {candidate_id} has invalid added_on")

        url = candidate.get("url")
        if not valid_public_url(url):
            errors.append(f"Source candidate {candidate_id} has an invalid URL")
        elif url in source_urls:
            errors.append(f"Source candidate URL is already approved: {candidate_id}")
        elif url in candidate_urls:
            errors.append(f"Duplicate source candidate URL: {candidate_id}")
        else:
            candidate_urls.add(str(url))

        suggested_exams = candidate.get("suggested_exams")
        if not isinstance(suggested_exams, list):
            errors.append(f"Source candidate {candidate_id} needs suggested_exams")
        else:
            if len(suggested_exams) != len(set(suggested_exams)):
                errors.append(
                    f"Source candidate {candidate_id} has duplicate suggested exams"
                )
            unknown = set(suggested_exams).difference(exam_codes)
            if unknown:
                errors.append(
                    f"Source candidate {candidate_id} references unknown exams: "
                    + ", ".join(sorted(unknown))
                )

        status = candidate.get("review_status")
        if status not in SOURCE_CANDIDATE_STATES:
            errors.append(
                f"Source candidate {candidate_id} has invalid review status: {status}"
            )
        if status == "rejected":
            if not valid_date(candidate.get("reviewed_on")):
                errors.append(
                    f"Rejected source candidate {candidate_id} needs reviewed_on"
                )
            review_notes = candidate.get("review_notes")
            if not isinstance(review_notes, str) or not review_notes.strip():
                errors.append(
                    f"Rejected source candidate {candidate_id} needs review_notes"
                )


def validate_reviews(
    reviews: object,
    exam_by_code: dict[str, dict[str, object]],
    guide_text_by_code: dict[str, str],
    source_id_by_url: dict[str, str],
    health_by_id: dict[str, dict[str, object]],
    errors: list[str],
) -> None:
    if not isinstance(reviews, list):
        errors.append("data/reviews.json must contain a reviews array")
        return

    review_ids: set[str] = set()
    passed_source_reviews: dict[str, list[dict[str, object]]] = {}
    required = {
        "id",
        "exam_code",
        "guide_path",
        "review_type",
        "reviewed_on",
        "outcome",
        "blueprint_snapshot_path",
        "blueprint_snapshot_sha256",
        "objective_coverage",
        "checks",
        "link_evidence",
    }
    for review in reviews:
        if not isinstance(review, dict):
            errors.append("Each guide review must be an object")
            continue
        review_id = review.get("id", "<unknown>")
        missing = required.difference(review)
        if missing:
            errors.append(
                f"Guide review {review_id} missing fields: "
                + ", ".join(sorted(missing))
            )
            continue
        if not isinstance(review_id, str) or not re.fullmatch(
            r"[a-z0-9-]+", review_id
        ):
            errors.append(f"Guide review has invalid id: {review_id}")
            continue
        if review_id in review_ids:
            errors.append(f"Duplicate guide review id: {review_id}")
        review_ids.add(review_id)

        code = review.get("exam_code")
        exam = exam_by_code.get(str(code))
        if exam is None:
            errors.append(f"Guide review {review_id} references unknown exam: {code}")
            continue
        if review.get("guide_path") != exam.get("guide_path"):
            errors.append(f"Guide review {review_id} has the wrong guide path")
        if not valid_date(review.get("reviewed_on")):
            errors.append(f"Guide review {review_id} has an invalid reviewed_on date")
        if review.get("review_type") not in {"source-validation", "community-review"}:
            errors.append(f"Guide review {review_id} has an invalid review type")
        if review.get("outcome") not in {"passed", "blocked"}:
            errors.append(f"Guide review {review_id} has an invalid outcome")

        coverage = review.get("objective_coverage")
        if not isinstance(coverage, list) or not coverage:
            errors.append(f"Guide review {review_id} needs objective coverage")
        else:
            for item in coverage:
                if not isinstance(item, dict) or not isinstance(
                    item.get("objective_group"), str
                ) or not item.get("objective_group"):
                    errors.append(
                        f"Guide review {review_id} has invalid objective coverage"
                    )
                    break
                sections = item.get("guide_sections")
                if not isinstance(sections, list) or not sections:
                    errors.append(
                        f"Guide review {review_id} has empty guide-section coverage"
                    )
                    break

        checks = review.get("checks")
        if not isinstance(checks, dict) or set(checks) != SOURCE_VALIDATION_CHECKS:
            errors.append(f"Guide review {review_id} has incomplete checks")
        elif review.get("outcome") == "passed" and not all(
            value is True for value in checks.values()
        ):
            errors.append(f"Passed guide review {review_id} has a failed check")

        raw_snapshot = review.get("blueprint_snapshot_path")
        if not isinstance(raw_snapshot, str):
            errors.append(f"Guide review {review_id} has an invalid snapshot path")
        else:
            snapshot = (ROOT / raw_snapshot).resolve()
            if ROOT != snapshot and ROOT not in snapshot.parents:
                errors.append(f"Guide review {review_id} snapshot escapes repository")
            elif not snapshot.is_file():
                errors.append(f"Guide review {review_id} snapshot is missing")
            else:
                actual_hash = sha256(snapshot.read_bytes()).hexdigest()
                if actual_hash != review.get("blueprint_snapshot_sha256"):
                    errors.append(
                        f"Guide review {review_id} blueprint snapshot hash changed"
                    )

        guide_text = guide_text_by_code.get(str(code), "")
        guide_urls = {
            target.strip().strip("<>")
            for target in MARKDOWN_LINK.findall(guide_text)
            if target.startswith(("http://", "https://"))
        }
        unregistered = guide_urls.difference(source_id_by_url)
        if unregistered:
            errors.append(
                f"Guide review {review_id} has unregistered sources: "
                + ", ".join(sorted(unregistered))
            )
        health_rows = [
            health_by_id.get(source_id_by_url[url], {})
            for url in guide_urls
            if url in source_id_by_url
        ]
        expected_evidence = {
            "unique_external_links": len(guide_urls),
            "reachable": sum(row.get("status") == "ok" for row in health_rows),
            "access_blocked": sum(
                row.get("status") == "blocked" for row in health_rows
            ),
            "missing_or_error": sum(
                row.get("status") in {"missing", "error"} for row in health_rows
            ),
        }
        if review.get("link_evidence") != expected_evidence:
            errors.append(f"Guide review {review_id} link evidence is stale")

        if (
            review.get("review_type") == "source-validation"
            and review.get("outcome") == "passed"
        ):
            passed_source_reviews.setdefault(str(code), []).append(review)

    for code, exam in exam_by_code.items():
        if exam.get("review_status") not in {"source-validated", "community-reviewed"}:
            continue
        current = [
            review
            for review in passed_source_reviews.get(code, [])
            if review.get("reviewed_on") == exam.get("blueprint_last_checked")
        ]
        if not current:
            errors.append(
                f"{code} is {exam.get('review_status')} without a current passed "
                "source-validation record"
            )


def ai_audit_summary(results: list[object]) -> dict[str, int]:
    """Return the exact aggregate stored alongside an AI-audit batch."""

    valid_results = [result for result in results if isinstance(result, dict)]
    findings: list[dict[str, object]] = []
    for result in valid_results:
        raw_findings = result.get("findings", [])
        if isinstance(raw_findings, list):
            findings.extend(
                finding for finding in raw_findings if isinstance(finding, dict)
            )
    return {
        "guide_count": len(valid_results),
        "pass": sum(result.get("verdict") == "pass" for result in valid_results),
        "pass_with_notes": sum(
            result.get("verdict") == "pass-with-notes" for result in valid_results
        ),
        "fix_required": sum(
            result.get("verdict") == "fix-required" for result in valid_results
        ),
        "blocked": sum(
            result.get("verdict") == "blocked" for result in valid_results
        ),
        "open_findings": sum(
            finding.get("status") == "open" for finding in findings
        ),
        "closed_findings": sum(
            finding.get("status") in {"resolved", "accepted-risk", "dismissed"}
            for finding in findings
        ),
    }


def validate_ai_audit_result(
    result: object,
    batch_id: str,
    exam_by_code: dict[str, dict[str, object]],
    errors: list[str],
) -> str | None:
    """Validate one semantic-audit result and return its exam code when usable."""

    if not isinstance(result, dict):
        errors.append(f"AI audit batch {batch_id} contains a non-object result")
        return None
    code = result.get("exam_code")
    label = f"AI audit result {batch_id}/{code}"
    exam = exam_by_code.get(str(code))
    if exam is None:
        errors.append(f"{label} references an unknown exam")
        return str(code)
    if result.get("vendor_id") != exam.get("vendor_id"):
        errors.append(f"{label} has the wrong vendor")
    if result.get("guide_path") != exam.get("guide_path"):
        errors.append(f"{label} has the wrong guide path")
    if not valid_date(result.get("audited_on")):
        errors.append(f"{label} has an invalid audited_on date")

    raw_snapshot = result.get("blueprint_snapshot_path")
    if not isinstance(raw_snapshot, str):
        errors.append(f"{label} has an invalid snapshot path")
    else:
        snapshot = (ROOT / raw_snapshot).resolve()
        expected_parent = (ROOT / "data/objective-snapshots").resolve()
        if expected_parent not in snapshot.parents:
            errors.append(f"{label} snapshot is outside data/objective-snapshots")
        elif not snapshot.is_file():
            errors.append(f"{label} snapshot is missing")
        else:
            actual_hash = sha256(snapshot.read_bytes()).hexdigest()
            if actual_hash != result.get("blueprint_snapshot_sha256"):
                errors.append(f"{label} blueprint snapshot hash changed")

    checks = result.get("checks")
    check_states: dict[str, object] = {}
    if not isinstance(checks, dict) or set(checks) != AI_AUDIT_CHECKS:
        errors.append(f"{label} has incomplete checks")
    else:
        for check_name, check in checks.items():
            if not isinstance(check, dict):
                errors.append(f"{label} check {check_name} must be an object")
                continue
            status = check.get("status")
            check_states[check_name] = status
            if status not in AI_AUDIT_CHECK_STATES:
                errors.append(f"{label} check {check_name} has an invalid status")
            notes = check.get("notes")
            if not isinstance(notes, str) or not notes.strip():
                errors.append(f"{label} check {check_name} needs evidence notes")

    findings = result.get("findings")
    usable_findings: list[dict[str, object]] = []
    finding_ids: set[str] = set()
    if not isinstance(findings, list):
        errors.append(f"{label} findings must be an array")
    else:
        for finding in findings:
            if not isinstance(finding, dict):
                errors.append(f"{label} contains a non-object finding")
                continue
            usable_findings.append(finding)
            finding_id = finding.get("id")
            if not isinstance(finding_id, str) or not re.fullmatch(
                r"[a-z0-9-]+", finding_id
            ):
                errors.append(f"{label} has an invalid finding id: {finding_id}")
            elif finding_id in finding_ids:
                errors.append(f"{label} has duplicate finding id: {finding_id}")
            else:
                finding_ids.add(finding_id)
            if finding.get("check") not in AI_AUDIT_CHECKS:
                errors.append(f"{label}/{finding_id} references an invalid check")
            if finding.get("severity") not in AI_AUDIT_SEVERITIES:
                errors.append(f"{label}/{finding_id} has an invalid severity")
            if finding.get("category") not in AI_AUDIT_CATEGORIES:
                errors.append(f"{label}/{finding_id} has an invalid category")
            finding_status = finding.get("status")
            if finding_status not in AI_AUDIT_FINDING_STATES:
                errors.append(f"{label}/{finding_id} has an invalid status")
            for field in ("location", "evidence", "recommendation"):
                value = finding.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{label}/{finding_id} needs {field}")
            resolution = finding.get("resolution")
            if finding_status == "open" and resolution is not None:
                errors.append(f"{label}/{finding_id} is open but has a resolution")
            elif finding_status in {"resolved", "accepted-risk", "dismissed"} and (
                not isinstance(resolution, str) or not resolution.strip()
            ):
                errors.append(f"{label}/{finding_id} needs a resolution")

    for check_name, status in check_states.items():
        if status not in {"failed", "blocked"}:
            continue
        if not any(
            finding.get("check") == check_name and finding.get("status") == "open"
            for finding in usable_findings
        ):
            errors.append(f"{label} {check_name} needs an open finding")

    verdict = result.get("verdict")
    if verdict not in AI_AUDIT_VERDICTS:
        errors.append(f"{label} has an invalid verdict")
    else:
        states = set(check_states.values())
        open_findings = [
            finding for finding in usable_findings if finding.get("status") == "open"
        ]
        open_severities = {finding.get("severity") for finding in open_findings}
        all_clear = states.issubset({"passed", "not-applicable"})
        has_material_open = bool(
            open_severities.intersection({"medium", "high", "critical"})
        )
        consistent = (
            (verdict == "pass" and all_clear and not open_findings)
            or (
                verdict == "pass-with-notes"
                and all_clear
                and bool(open_findings)
                and open_severities.issubset({"info", "low"})
            )
            or (
                verdict == "fix-required"
                and "blocked" not in states
                and ("failed" in states or has_material_open)
            )
            or (verdict == "blocked" and "blocked" in states)
        )
        if not consistent:
            errors.append(f"{label} verdict is inconsistent with checks/findings")

    notes = result.get("notes")
    if not isinstance(notes, str) or not notes.strip():
        errors.append(f"{label} needs notes")
    return str(code)


def validate_ai_audits(
    audit_data: dict[str, object],
    exam_by_code: dict[str, dict[str, object]],
    reviews: object,
    errors: list[str],
) -> None:
    """Validate bounded AI-audit batches without conflating them with human review."""

    rubric_version = audit_data.get("rubric_version")
    if not isinstance(rubric_version, int) or rubric_version < 1:
        errors.append("data/ai-audits.json needs a positive integer rubric_version")
    batches = audit_data.get("batches")
    if not isinstance(batches, list):
        errors.append("data/ai-audits.json must contain a batches array")
        return
    review_rows = reviews if isinstance(reviews, list) else []
    current_review_by_code = {
        str(review.get("exam_code")): review
        for review in review_rows
        if isinstance(review, dict)
        and review.get("review_type") == "source-validation"
        and review.get("outcome") == "passed"
        and review.get("reviewed_on")
        == exam_by_code.get(str(review.get("exam_code")), {}).get(
            "blueprint_last_checked"
        )
    }

    batch_ids: set[str] = set()
    for batch in batches:
        if not isinstance(batch, dict):
            errors.append("Each AI audit batch must be an object")
            continue
        batch_id = batch.get("id")
        if not isinstance(batch_id, str) or not re.fullmatch(r"[a-z0-9-]+", batch_id):
            errors.append(f"AI audit batch has an invalid id: {batch_id}")
            continue
        if batch_id in batch_ids:
            errors.append(f"Duplicate AI audit batch id: {batch_id}")
        batch_ids.add(batch_id)
        label = f"AI audit batch {batch_id}"
        batch_rubric = batch.get("rubric_version")
        if not isinstance(batch_rubric, int) or batch_rubric < 1:
            errors.append(f"{label} has an invalid rubric version")
        elif isinstance(rubric_version, int) and batch_rubric > rubric_version:
            errors.append(f"{label} uses a future rubric version")
        if not isinstance(batch.get("title"), str) or not batch["title"].strip():
            errors.append(f"{label} needs a title")
        if not valid_date(batch.get("created_on")):
            errors.append(f"{label} has an invalid created_on date")
        status = batch.get("status")
        if status not in {"planned", "in-progress", "completed"}:
            errors.append(f"{label} has an invalid status")
        completed_on = batch.get("completed_on")
        if status == "completed" and not valid_date(completed_on):
            errors.append(f"{label} needs a valid completed_on date")
        elif status != "completed" and completed_on is not None:
            errors.append(f"{label} cannot have completed_on before completion")
        if batch.get("audit_mode") != "read-only":
            errors.append(f"{label} must use read-only audit mode")
        if batch.get("rubric_path") != "docs/AI-AUDIT.md":
            errors.append(f"{label} has the wrong rubric path")
        if not isinstance(batch.get("selection_method"), str) or not batch[
            "selection_method"
        ].strip():
            errors.append(f"{label} needs a selection method")
        auditor = batch.get("auditor")
        if not isinstance(auditor, dict):
            errors.append(f"{label} needs an auditor disclosure")
        else:
            if (
                auditor.get("kind") != "ai-agent"
                or auditor.get("human_review") is not False
            ):
                errors.append(f"{label} has an invalid auditor disclosure")
            if auditor.get("independence") not in {"fresh-context", "same-context"}:
                errors.append(f"{label} has an invalid independence disclosure")
            if not isinstance(auditor.get("label"), str) or not auditor[
                "label"
            ].strip():
                errors.append(f"{label} needs an auditor label")

        exam_codes = batch.get("exam_codes")
        if not isinstance(exam_codes, list) or not exam_codes:
            errors.append(f"{label} needs exam codes")
            selected_codes: list[str] = []
        else:
            selected_codes = [code for code in exam_codes if isinstance(code, str)]
            if len(selected_codes) != len(exam_codes):
                errors.append(f"{label} exam codes must be strings")
            if len(exam_codes) > AI_AUDIT_MAX_BATCH_SIZE:
                errors.append(f"{label} exceeds {AI_AUDIT_MAX_BATCH_SIZE} guides")
            if len(selected_codes) != len(set(selected_codes)):
                errors.append(f"{label} contains duplicate exam codes")
            unknown = set(selected_codes).difference(exam_by_code)
            if unknown:
                errors.append(
                    f"{label} references unknown exams: " + ", ".join(sorted(unknown))
                )

        results = batch.get("results")
        if not isinstance(results, list):
            errors.append(f"{label} results must be an array")
            usable_results: list[object] = []
        else:
            usable_results = results
        result_codes = [
            code
            for result in usable_results
            if (
                code := validate_ai_audit_result(
                    result, batch_id, exam_by_code, errors
                )
            )
        ]
        for result in usable_results:
            if not isinstance(result, dict):
                continue
            result_code = str(result.get("exam_code"))
            current_review = current_review_by_code.get(result_code)
            if current_review is None:
                errors.append(
                    f"{label}/{result_code} lacks a current source-validation record"
                )
                continue
            for field in (
                "blueprint_snapshot_path",
                "blueprint_snapshot_sha256",
            ):
                if result.get(field) != current_review.get(field):
                    errors.append(
                        f"{label}/{result_code} {field} does not match the "
                        "current source-validation record"
                    )
        if len(result_codes) != len(set(result_codes)):
            errors.append(f"{label} contains duplicate result exam codes")
        if not set(result_codes).issubset(set(selected_codes)):
            errors.append(f"{label} has results outside its selected exam codes")
        if status == "completed" and set(result_codes) != set(selected_codes):
            errors.append(
                f"{label} does not have exactly one result per selected guide"
            )
        expected_summary = ai_audit_summary(usable_results)
        if batch.get("summary") != expected_summary:
            errors.append(f"{label} summary is stale or incorrect")


def validate_catalogs(errors: list[str]) -> None:
    certification_seeds_data = load_json(
        ROOT / "config/certification-seeds.json", errors
    )
    exams_data = load_json(ROOT / "config/exams.json", errors)
    collections_data = load_json(ROOT / "config/collections.json", errors)
    audits_data = load_json(ROOT / "data/ai-audits.json", errors)
    candidates_data = load_json(ROOT / "data/source-candidates.json", errors)
    reviews_data = load_json(ROOT / "data/reviews.json", errors)
    vendors_data = load_json(ROOT / "data/vendors.json", errors)
    sources_data = load_json(ROOT / "data/sources.json", errors)

    exams = exams_data.get("exams", [])
    collections = collections_data.get("collections", [])
    vendors = vendors_data.get("vendors", [])
    sources = sources_data.get("sources", [])
    candidates = candidates_data.get("candidates", [])
    reviews = reviews_data.get("reviews", [])
    if not isinstance(exams, list) or not exams:
        errors.append("config/exams.json must contain a non-empty exams array")
        return
    if not isinstance(vendors, list) or not vendors:
        errors.append("data/vendors.json must contain a non-empty vendors array")
        return
    if not isinstance(sources, list) or not sources:
        errors.append("data/sources.json must contain a non-empty sources array")
        return
    if not isinstance(collections, list) or not collections:
        errors.append("config/collections.json must contain a non-empty collections array")
        return

    vendor_ids: set[str] = set()
    for vendor in vendors:
        if not isinstance(vendor, dict):
            errors.append("Each vendor entry must be an object")
            continue
        vendor_id = vendor.get("id")
        if not isinstance(vendor_id, str) or not vendor_id:
            errors.append("Each vendor needs a non-empty id")
        elif vendor_id in vendor_ids:
            errors.append(f"Duplicate vendor id: {vendor_id}")
        else:
            vendor_ids.add(vendor_id)
        if not valid_public_url(vendor.get("certification_url")):
            errors.append(f"Invalid certification URL for vendor: {vendor_id}")
        adapter = vendor.get("objective_adapter")
        if not isinstance(adapter, str) or not adapter:
            errors.append(f"Vendor {vendor_id} needs an objective_adapter")
        elif adapter not in OBJECTIVE_ADAPTERS:
            errors.append(
                f"Vendor {vendor_id} has unsupported objective_adapter: {adapter}"
            )

    validate_certification_seed_catalog(
        certification_seeds_data, exams, vendor_ids, errors
    )

    exam_codes: set[str] = set()
    guide_paths: set[str] = set()
    exam_by_code: dict[str, dict[str, object]] = {}
    guide_text_by_code: dict[str, str] = {}
    required_exam_fields = {
        "code",
        "vendor_id",
        "title",
        "level",
        "status",
        "study_guide_url",
        "guide_path",
        "blueprint_last_checked",
        "upcoming_change_status",
        "upcoming_change_checked",
        "review_status",
        "content_basis",
        "study_prerequisites",
    }
    for exam in exams:
        if not isinstance(exam, dict):
            errors.append("Each exam entry must be an object")
            continue
        missing = required_exam_fields.difference(exam)
        code = exam.get("code", "<unknown>")
        if missing:
            errors.append(f"Exam {code} missing fields: {', '.join(sorted(missing))}")
            continue
        if not isinstance(code, str) or not code:
            errors.append("Each exam needs a non-empty code")
            continue
        if code in exam_codes:
            errors.append(f"Duplicate exam code: {code}")
        exam_codes.add(code)
        exam_by_code[code] = exam
        if exam["vendor_id"] not in vendor_ids:
            errors.append(f"Exam {code} references unknown vendor: {exam['vendor_id']}")
        if exam["status"] not in EXAM_STATUSES:
            errors.append(f"Exam {code} has invalid status: {exam['status']}")
        if exam["level"] not in EXAM_LEVELS:
            errors.append(f"Exam {code} has invalid level: {exam['level']}")
        if exam["review_status"] not in REVIEW_STATES:
            errors.append(f"Exam {code} has invalid review status: {exam['review_status']}")
        if exam["upcoming_change_status"] not in UPCOMING_CHANGE_STATUSES:
            errors.append(
                f"Exam {code} has invalid upcoming-change status: "
                f"{exam['upcoming_change_status']}"
            )
        if exam["content_basis"] != "public-sources-only":
            errors.append(f"Exam {code} must use public-sources-only content")
        if not isinstance(exam["study_prerequisites"], str) or not exam[
            "study_prerequisites"
        ].strip():
            errors.append(f"Exam {code} needs study_prerequisites")
        if not valid_date(exam["blueprint_last_checked"]):
            errors.append(f"Exam {code} has invalid blueprint_last_checked")
        if not valid_date(exam["upcoming_change_checked"]):
            errors.append(f"Exam {code} has invalid upcoming_change_checked")
        if not valid_public_url(exam["study_guide_url"]):
            errors.append(f"Exam {code} has invalid study-guide URL")

        guide_path = exam["guide_path"]
        if not isinstance(guide_path, str):
            errors.append(f"Exam {code} has a non-string guide path")
            continue
        if guide_path in guide_paths:
            errors.append(f"Duplicate guide path: {guide_path}")
        guide_paths.add(guide_path)
        guide = ROOT / guide_path
        if not guide.is_file():
            errors.append(f"Missing configured guide: {guide_path}")
            continue

        text = guide.read_text(encoding="utf-8")
        guide_text_by_code[code] = text
        metadata = parse_front_matter(text)
        missing_metadata = GUIDE_METADATA.difference(metadata)
        if missing_metadata:
            errors.append(
                f"Guide {guide_path} missing metadata: "
                f"{', '.join(sorted(missing_metadata))}"
            )
            continue
        expected = {
            "exam_code": code,
            "vendor_id": str(exam["vendor_id"]),
            "official_blueprint": str(exam["study_guide_url"]),
            "content_basis": str(exam["content_basis"]),
            "review_status": str(exam["review_status"]),
            "last_verified": str(exam["blueprint_last_checked"]),
            "upcoming_change_status": str(exam["upcoming_change_status"]),
            "upcoming_change_checked": str(exam["upcoming_change_checked"]),
        }
        for key, value in expected.items():
            if metadata.get(key) != value:
                errors.append(
                    f"Guide {guide_path} metadata {key} does not match catalog"
                )
        if metadata.get("generation_method") != "AI-assisted synthesis":
            errors.append(f"Guide {guide_path} has an unknown generation method")
        if metadata.get("authority") != "unofficial":
            errors.append(f"Guide {guide_path} must identify itself as unofficial")
        if "Independent AI-assisted resource" not in text:
            errors.append(f"Guide {guide_path} is missing its visible AI disclosure")
        heading_levels = markdown_heading_levels(text)
        if heading_levels.count(1) != 1:
            errors.append(
                f"Guide {guide_path} must contain exactly one level-one heading"
            )
        if "> **About related items:**" not in text:
            errors.append(f"Guide {guide_path} is missing its related-item explanation")
        if "# Places to learn" not in text:
            errors.append(f"Guide {guide_path} is missing its Places to learn section")
        places_to_learn = text.split("# Places to learn", 1)[-1]
        has_timed_resource_table = "| Resource | Access | Estimated time |" in text
        has_timed_resource_list = bool(
            re.search(
                r"(?m)^- .*\*\*[^*]*(?:minutes?|hours?|days?)\*\*",
                places_to_learn,
            )
        )
        if not (has_timed_resource_table or has_timed_resource_list):
            errors.append(f"Guide {guide_path} is missing learning-resource time estimates")
        if "not a complete list" not in text:
            errors.append(f"Guide {guide_path} must say its learning list is incomplete")
        if "Downstream mirrors may append" in text:
            errors.append(f"Guide {guide_path} contains obsolete mirror boilerplate")

    source_ids: set[str] = set()
    source_urls: set[str] = set()
    blueprint_urls: dict[str, str] = {}
    for source in sources:
        if not isinstance(source, dict):
            errors.append("Each source entry must be an object")
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id:
            errors.append("Each source needs a non-empty id")
            continue
        if source_id in source_ids:
            errors.append(f"Duplicate source id: {source_id}")
        source_ids.add(source_id)
        if not valid_public_url(source.get("url")):
            errors.append(f"Source {source_id} has an invalid URL")
        else:
            source_urls.add(str(source.get("url")))
        authority = source.get("authority_class")
        if not isinstance(authority, int) or not 1 <= authority <= 6:
            errors.append(f"Source {source_id} has an invalid authority class")
        access_model = source.get("access_model")
        if access_model not in SOURCE_ACCESS_MODELS:
            errors.append(f"Source {source_id} has an invalid access model")
        if not valid_date(source.get("last_checked")):
            errors.append(f"Source {source_id} has an invalid last_checked date")
        supported = source.get("supported_exams")
        if not isinstance(supported, list):
            errors.append(f"Source {source_id} needs a supported_exams array")
            continue
        unknown = set(supported).difference(exam_codes)
        if unknown:
            errors.append(
                f"Source {source_id} references unknown exams: "
                f"{', '.join(sorted(unknown))}"
            )
        if source.get("source_type") == "exam-blueprint":
            if authority != 1:
                errors.append(f"Blueprint source {source_id} must be authority class 1")
            for code in supported:
                if code in blueprint_urls:
                    errors.append(f"Multiple blueprint sources registered for {code}")
                blueprint_urls[code] = str(source.get("url"))

    for code, exam in exam_by_code.items():
        if blueprint_urls.get(code) != exam.get("study_guide_url"):
            errors.append(f"Missing matching canonical blueprint source for {code}")

    collection_ids: set[str] = set()
    collected_exam_codes: set[str] = set()
    for collection in collections:
        if not isinstance(collection, dict):
            errors.append("Each collection entry must be an object")
            continue
        collection_id = collection.get("id")
        if not isinstance(collection_id, str) or not collection_id:
            errors.append("Each collection needs a non-empty id")
            continue
        if collection_id in collection_ids:
            errors.append(f"Duplicate collection id: {collection_id}")
        collection_ids.add(collection_id)
        if not isinstance(collection.get("title"), str) or not collection["title"]:
            errors.append(f"Collection {collection_id} needs a title")
        if not isinstance(collection.get("summary"), str) or not collection["summary"]:
            errors.append(f"Collection {collection_id} needs a summary")
        collection_exams = collection.get("exam_codes")
        if not isinstance(collection_exams, list) or not collection_exams:
            errors.append(f"Collection {collection_id} needs exam codes")
            continue
        if len(collection_exams) != len(set(collection_exams)):
            errors.append(f"Collection {collection_id} contains duplicate exam codes")
        unknown = set(collection_exams).difference(exam_codes)
        if unknown:
            errors.append(
                f"Collection {collection_id} references unknown exams: "
                f"{', '.join(sorted(unknown))}"
            )
        collected_exam_codes.update(str(code) for code in collection_exams)

    ungrouped = exam_codes.difference(collected_exam_codes)
    if ungrouped:
        errors.append(
            "Every exam must appear in at least one collection; missing: "
            + ", ".join(sorted(ungrouped))
        )

    validate_source_candidates(
        candidates, source_ids, source_urls, exam_codes, errors
    )

    for schema in (
        "schemas/certification-seed-catalog.schema.json",
        "schemas/ai-audit-catalog.schema.json",
        "schemas/collection-catalog.schema.json",
        "schemas/exam-catalog.schema.json",
        "schemas/review-catalog.schema.json",
        "schemas/source-candidate-catalog.schema.json",
        "schemas/source-catalog.schema.json",
        "schemas/source-health.schema.json",
        "schemas/vendor-catalog.schema.json",
    ):
        load_json(ROOT / schema, errors)

    source_health_path = ROOT / "data/source-health.json"
    health_by_id: dict[str, dict[str, object]] = {}
    if source_health_path.is_file():
        health_data = load_json(source_health_path, errors)
        health_sources = health_data.get("sources", [])
        if not isinstance(health_sources, list):
            errors.append("data/source-health.json needs a sources array")
        else:
            health_by_id = {
                str(item["id"]): item
                for item in health_sources
                if isinstance(item, dict) and item.get("id")
            }
            health_ids = {
                str(item.get("id"))
                for item in health_sources
                if isinstance(item, dict) and item.get("id")
            }
            missing_health = source_ids.difference(health_ids)
            unknown_health = health_ids.difference(source_ids)
            if missing_health:
                errors.append(
                    "Source-health snapshot is missing: "
                    + ", ".join(sorted(missing_health))
                )
            if unknown_health:
                errors.append(
                    "Source-health snapshot contains unknown sources: "
                    + ", ".join(sorted(unknown_health))
                )

    source_id_by_url = {
        str(source.get("url")): str(source.get("id"))
        for source in sources
        if isinstance(source, dict) and source.get("url") and source.get("id")
    }
    validate_reviews(
        reviews,
        exam_by_code,
        guide_text_by_code,
        source_id_by_url,
        health_by_id,
        errors,
    )
    validate_ai_audits(audits_data, exam_by_code, reviews, errors)


def validate_markdown(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        relative = path.relative_to(ROOT)
        if relative in IGNORED_MARKDOWN_FILES or any(
            part in IGNORED_MARKDOWN_DIRS for part in relative.parts
        ):
            continue
        text = path.read_text(encoding="utf-8")
        fences = sum(1 for line in text.splitlines() if line.startswith("```"))
        if fences % 2:
            errors.append(f"Unbalanced code fences: {relative}")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not local_target:
                continue
            resolved = (path.parent / local_target).resolve()
            if ROOT != resolved and ROOT not in resolved.parents:
                errors.append(
                    f"Local link escapes repository in {relative}: "
                    f"{raw_target}"
                )
            elif not resolved.exists():
                errors.append(
                    f"Broken local link in {relative}: {raw_target}"
                )


def main() -> int:
    errors: list[str] = []
    validate_catalogs(errors)
    validate_markdown(errors)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
