#!/usr/bin/env python3
"""Validate catalogs, guide metadata, Markdown fences, and local links."""

from __future__ import annotations

from datetime import date
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
UPCOMING_CHANGE_STATUSES = {
    "none-announced",
    "scheduled",
    "retirement-announced",
}
SOURCE_CANDIDATE_STATES = {"queued", "in-review", "rejected"}
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
IGNORED_MARKDOWN_DIRS = {".git", ".venv", "site", "__pycache__"}
IGNORED_MARKDOWN_FILES = {Path("docs/initialChat.md")}


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


def validate_catalogs(errors: list[str]) -> None:
    exams_data = load_json(ROOT / "config/exams.json", errors)
    collections_data = load_json(ROOT / "config/collections.json", errors)
    candidates_data = load_json(ROOT / "data/source-candidates.json", errors)
    vendors_data = load_json(ROOT / "data/vendors.json", errors)
    sources_data = load_json(ROOT / "data/sources.json", errors)

    exams = exams_data.get("exams", [])
    collections = collections_data.get("collections", [])
    vendors = vendors_data.get("vendors", [])
    sources = sources_data.get("sources", [])
    candidates = candidates_data.get("candidates", [])
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

    exam_codes: set[str] = set()
    guide_paths: set[str] = set()
    exam_by_code: dict[str, dict[str, object]] = {}
    required_exam_fields = {
        "code",
        "vendor_id",
        "title",
        "status",
        "study_guide_url",
        "guide_path",
        "blueprint_last_checked",
        "upcoming_change_status",
        "upcoming_change_checked",
        "review_status",
        "content_basis",
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
        if exam["review_status"] not in REVIEW_STATES:
            errors.append(f"Exam {code} has invalid review status: {exam['review_status']}")
        if exam["upcoming_change_status"] not in UPCOMING_CHANGE_STATUSES:
            errors.append(
                f"Exam {code} has invalid upcoming-change status: "
                f"{exam['upcoming_change_status']}"
            )
        if exam["content_basis"] != "public-sources-only":
            errors.append(f"Exam {code} must use public-sources-only content")
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
        if "> **About related items:**" not in text:
            errors.append(f"Guide {guide_path} is missing its related-item explanation")
        if "# Places to learn" not in text:
            errors.append(f"Guide {guide_path} is missing its Places to learn section")
        if "| Resource | Access | Estimated time |" not in text:
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
        "schemas/collection-catalog.schema.json",
        "schemas/exam-catalog.schema.json",
        "schemas/source-candidate-catalog.schema.json",
        "schemas/source-catalog.schema.json",
        "schemas/vendor-catalog.schema.json",
    ):
        load_json(ROOT / schema, errors)


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
