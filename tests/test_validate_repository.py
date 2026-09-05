import importlib.util
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("repository_validator", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class RepositoryValidationTests(unittest.TestCase):
    def freshness_fixture(self) -> tuple[
        dict[str, object],
        dict[str, dict[str, object]],
        list[dict[str, object]],
        list[dict[str, object]],
        list[dict[str, object]],
    ]:
        exam = {
            "code": "EX-100",
            "vendor_id": "example",
            "guide_path": "guides/EX-100.md",
        }
        source = {
            "id": "official-source",
            "url": "https://example.com/old",
            "authority_class": 2,
            "source_type": "product-documentation",
            "access_model": "public",
            "supported_exams": ["EX-100"],
        }
        candidate = {
            "id": "new-source",
            "url": "https://example.com/new",
            "review_status": "queued",
            "suggested_exams": ["EX-100"],
        }
        health = {
            "id": "official-source",
            "url": "https://example.com/old",
            "status": "ok",
            "final_url": "https://example.com/current",
            "canonical_url": "https://example.com/current",
        }
        checks = {
            name: {"status": "passed", "notes": "Checked official evidence."}
            for name in validator.SOURCE_FRESHNESS_CHECKS
        }
        checks["official_release_channels"]["status"] = "finding"
        finding = {
            "id": "new-source",
            "check": "official_release_channels",
            "category": "new-source",
            "title": "New source",
            "url": "https://example.com/new",
            "source_type": "release-notes",
            "affected_exams": ["EX-100"],
            "catalog_status": "candidate",
            "confidence": "high",
            "evidence": "A current official page was found.",
            "recommendation": "Review it.",
            "disposition": "queued",
            "candidate_id": "new-source",
        }
        result = {
            "exam_code": "EX-100",
            "vendor_id": "example",
            "guide_path": "guides/EX-100.md",
            "baseline_sha256": "a" * 64,
            "scanned_on": "2026-09-05",
            "outcome": "review-required",
            "checks": checks,
            "findings": [finding],
            "notes": "Review needed.",
        }
        batch = {
            "id": "test-batch",
            "title": "Test batch",
            "rubric_version": 1,
            "created_on": "2026-09-05",
            "completed_on": "2026-09-05",
            "status": "completed",
            "scan_mode": "read-only",
            "selection_method": "Test selection.",
            "rubric_path": "docs/SOURCE-FRESHNESS.md",
            "auditor": {
                "kind": "ai-agent",
                "labels": ["test"],
                "independence": "fresh-context",
                "human_review": False,
            },
            "exam_codes": ["EX-100"],
            "results": [result],
            "summary": validator.source_freshness_summary([result]),
        }
        return (
            {"rubric_version": 1, "batches": [batch]},
            {"EX-100": exam},
            [source],
            [candidate],
            [health],
        )

    def validate_freshness_fixture(
        self,
        catalog: dict[str, object],
        exams: dict[str, dict[str, object]],
        sources: list[dict[str, object]],
        candidates: list[dict[str, object]],
        health: list[dict[str, object]],
    ) -> list[str]:
        errors: list[str] = []
        validator.validate_source_freshness(
            catalog, exams, sources, candidates, health, errors
        )
        return errors

    def test_generated_site_source_tree_is_not_revalidated_as_repository_content(self) -> None:
        self.assertIn(".site-build", validator.IGNORED_MARKDOWN_DIRS)

    def test_parses_required_guide_front_matter(self) -> None:
        text = """---
exam_code: GH-900
official_blueprint: https://example.com/gh-900
review_status: ai-generated-draft
---
# Guide
"""
        metadata = validator.parse_front_matter(text)
        self.assertEqual("GH-900", metadata["exam_code"])
        self.assertEqual(
            "https://example.com/gh-900", metadata["official_blueprint"]
        )

    def test_validates_dates_and_public_urls(self) -> None:
        self.assertTrue(validator.valid_date("2026-08-30"))
        self.assertFalse(validator.valid_date("08/30/2026"))
        self.assertTrue(validator.valid_public_url("https://docs.github.com/"))
        self.assertFalse(validator.valid_public_url("docs/private.md"))

    def test_heading_parser_ignores_fenced_code(self) -> None:
        markdown = """# Guide title

## Major section

```bash
# shell comment
## another shell comment
```

### Nested topic
"""
        self.assertEqual([1, 2, 3], validator.markdown_heading_levels(markdown))

    def test_renders_python_friendly_certification_query_seeds(self) -> None:
        certifications = [
            {
                "vendor_id": "example",
                "exam_code": "EX-100",
                "title": "Example Certification",
                "status": "active",
                "review_status": "source-validated",
                "guide_path": "guides/EX-100-example.md",
                "study_guide_url": "https://example.com/ex-100",
            }
        ]

        rendered = validator.render_certification_list(certifications)

        self.assertEqual(
            "vendor_id\texam_code\ttitle\n"
            "example\tEX-100\tExample Certification\n",
            rendered,
        )

    def test_retirement_metadata_is_validated_and_replacement_is_cataloged(self) -> None:
        source = {
            "id": "example-current",
            "vendor_id": "example",
            "catalog_url": "https://example.com/certifications",
            "selection": "Every current example certification.",
            "last_verified": "2026-08-31",
        }
        retiring = {
            "vendor_id": "example",
            "exam_code": "EX-100",
            "title": "Retiring example",
            "official_url": "https://example.com/ex-100",
            "status": "retirement-announced",
            "retirement_date": "2026-09-30",
            "replacement_exam_code": "EX-200",
            "replacement_official_url": "https://example.com/ex-200",
            "source_id": "example-current",
        }
        replacement = {
            "vendor_id": "example",
            "exam_code": "EX-200",
            "title": "Replacement example",
            "official_url": "https://example.com/ex-200",
            "status": "beta",
            "source_id": "example-current",
        }
        errors: list[str] = []

        validator.validate_certification_seed_catalog(
            {"catalog_sources": [source], "certifications": [retiring, replacement]},
            [],
            {"example"},
            errors,
        )

        lifecycle_errors = [
            error for error in errors if not error.startswith("CERTIFICATIONS.txt is stale")
        ]
        self.assertEqual([], lifecycle_errors)

        missing_date = dict(retiring)
        del missing_date["retirement_date"]
        errors = []
        validator.validate_certification_seed_catalog(
            {
                "catalog_sources": [source],
                "certifications": [missing_date, replacement],
            },
            [],
            {"example"},
            errors,
        )
        self.assertTrue(any("needs a retirement_date" in error for error in errors))

    def test_certification_seed_accepts_vendor_codes_that_begin_with_digits(self) -> None:
        source = {
            "id": "example-current",
            "vendor_id": "example",
            "catalog_url": "https://example.com/certifications",
            "selection": "Every selected example certification.",
            "last_verified": "2026-09-01",
        }
        certification = {
            "vendor_id": "example",
            "exam_code": "220-1201",
            "title": "Example component exam",
            "official_url": "https://example.com/220-1201",
            "status": "active",
            "source_id": "example-current",
        }
        errors: list[str] = []

        validator.validate_certification_seed_catalog(
            {"catalog_sources": [source], "certifications": [certification]},
            [],
            {"example"},
            errors,
        )

        code_errors = [error for error in errors if "exam code" in error]
        self.assertEqual([], code_errors)

    def test_ai_audit_summary_counts_verdicts_and_dispositions(self) -> None:
        results = [
            {"verdict": "pass", "findings": []},
            {
                "verdict": "fix-required",
                "findings": [
                    {"status": "open"},
                    {"status": "resolved"},
                    {"status": "accepted-risk"},
                ],
            },
        ]

        self.assertEqual(
            {
                "guide_count": 2,
                "pass": 1,
                "pass_with_notes": 0,
                "fix_required": 1,
                "blocked": 0,
                "open_findings": 1,
                "closed_findings": 2,
            },
            validator.ai_audit_summary(results),
        )

    def test_ai_audit_rejects_pass_verdict_with_material_open_finding(self) -> None:
        snapshot_path = "data/objective-snapshots/gh-900-official-objectives.txt"
        snapshot = Path(__file__).parents[1] / snapshot_path
        checks = {
            name: {"status": "passed", "notes": "Evidence checked."}
            for name in validator.AI_AUDIT_CHECKS
        }
        result = {
            "exam_code": "GH-900",
            "vendor_id": "github",
            "guide_path": "guides/GH-900-github-foundations.md",
            "blueprint_snapshot_path": snapshot_path,
            "blueprint_snapshot_sha256": sha256(snapshot.read_bytes()).hexdigest(),
            "audited_on": "2026-09-04",
            "verdict": "pass",
            "checks": checks,
            "findings": [
                {
                    "id": "gh-900-material-gap",
                    "check": "objective_coverage",
                    "severity": "medium",
                    "category": "scope-gap",
                    "location": "Part 1",
                    "evidence": "A material objective is not explained.",
                    "recommendation": "Add substantive coverage.",
                    "status": "open",
                }
            ],
            "notes": "Fresh-context semantic audit.",
        }
        errors: list[str] = []

        validator.validate_ai_audit_result(
            result,
            "test-batch",
            {
                "GH-900": {
                    "vendor_id": "github",
                    "guide_path": "guides/GH-900-github-foundations.md",
                }
            },
            errors,
        )

        self.assertTrue(any("verdict is inconsistent" in error for error in errors))

    def test_ai_audit_rejects_pass_against_blocked_source_validation(self) -> None:
        snapshot_path = "data/objective-snapshots/gh-900-official-objectives.txt"
        snapshot_hash = sha256(
            (Path(__file__).parents[1] / snapshot_path).read_bytes()
        ).hexdigest()
        result = {
            "exam_code": "GH-900",
            "vendor_id": "github",
            "guide_path": "guides/GH-900-github-foundations.md",
            "blueprint_snapshot_path": snapshot_path,
            "blueprint_snapshot_sha256": snapshot_hash,
            "audited_on": "2026-09-05",
            "verdict": "pass",
            "checks": {
                name: {"status": "passed", "notes": "Evidence checked."}
                for name in validator.AI_AUDIT_CHECKS
            },
            "findings": [],
            "notes": "Fresh-context semantic audit.",
        }
        batch = {
            "id": "test-batch",
            "rubric_version": 1,
            "title": "Test batch",
            "created_on": "2026-09-05",
            "status": "completed",
            "completed_on": "2026-09-05",
            "audit_mode": "read-only",
            "rubric_path": "docs/AI-AUDIT.md",
            "selection_method": "One-guide validator test.",
            "auditor": {
                "kind": "ai-agent",
                "human_review": False,
                "independence": "fresh-context",
                "label": "Test agent",
            },
            "exam_codes": ["GH-900"],
            "results": [result],
            "summary": validator.ai_audit_summary([result]),
        }
        exam = {
            "vendor_id": "github",
            "guide_path": "guides/GH-900-github-foundations.md",
            "blueprint_last_checked": "2026-09-05",
        }
        review = {
            "exam_code": "GH-900",
            "review_type": "source-validation",
            "reviewed_on": "2026-09-05",
            "outcome": "blocked",
            "blueprint_snapshot_path": snapshot_path,
            "blueprint_snapshot_sha256": snapshot_hash,
        }
        errors: list[str] = []

        validator.validate_ai_audits(
            {"rubric_version": 1, "batches": [batch]},
            {"GH-900": exam},
            [review],
            errors,
        )

        self.assertEqual(
            [
                "AI audit batch test-batch/GH-900 cannot pass with a blocked "
                "source-validation record"
            ],
            errors,
        )

    def test_source_freshness_summary_counts_outcomes_and_dispositions(self) -> None:
        results = [
            {"outcome": "current", "findings": []},
            {
                "outcome": "review-required",
                "findings": [
                    {"disposition": "queued"},
                    {"disposition": "applied"},
                    {"disposition": "no-action"},
                ],
            },
            {
                "outcome": "blocked",
                "findings": [{"disposition": "blocked"}],
            },
        ]

        self.assertEqual(
            {
                "exam_count": 3,
                "current": 1,
                "review_required": 1,
                "blocked": 1,
                "queued_findings": 1,
                "applied_findings": 1,
                "no_action_findings": 1,
                "blocked_findings": 1,
            },
            validator.source_freshness_summary(results),
        )

    def test_freshness_rejects_queued_finding_on_passed_check(self) -> None:
        fixture = self.freshness_fixture()
        catalog = fixture[0]
        result = catalog["batches"][0]["results"][0]
        result["checks"]["official_release_channels"]["status"] = "passed"

        errors = self.validate_freshness_fixture(*fixture)

        self.assertTrue(any("conflicts with its check state" in error for error in errors))

    def test_freshness_binds_candidates_and_sources_to_affected_exams(self) -> None:
        fixture = self.freshness_fixture()
        fixture[3][0]["suggested_exams"] = []

        candidate_errors = self.validate_freshness_fixture(*fixture)

        self.assertTrue(
            any("affected exams do not match its candidate" in error for error in candidate_errors)
        )

        applied_fixture = deepcopy(self.freshness_fixture())
        catalog, _, sources, _, _ = applied_fixture
        result = catalog["batches"][0]["results"][0]
        finding = result["findings"][0]
        finding.update(
            {
                "url": "https://example.com/current",
                "catalog_status": "registered",
                "disposition": "applied",
                "source_id": "official-source",
                "resolution": "Applied.",
            }
        )
        del finding["candidate_id"]
        result["checks"]["official_release_channels"]["status"] = "passed"
        result["outcome"] = "current"
        sources[0]["supported_exams"] = []
        catalog["batches"][0]["summary"] = validator.source_freshness_summary([result])

        source_errors = self.validate_freshness_fixture(*applied_fixture)

        self.assertTrue(
            any("affected exams do not match its source" in error for error in source_errors)
        )

    def test_freshness_accepts_registered_canonical_alias(self) -> None:
        fixture = self.freshness_fixture()
        catalog = fixture[0]
        result = catalog["batches"][0]["results"][0]
        finding = result["findings"][0]
        finding.update(
            {
                "url": "https://example.com/current",
                "catalog_status": "registered",
                "disposition": "applied",
                "source_id": "official-source",
                "resolution": "Applied.",
            }
        )
        del finding["candidate_id"]
        result["checks"]["official_release_channels"]["status"] = "passed"
        result["outcome"] = "current"
        catalog["batches"][0]["summary"] = validator.source_freshness_summary([result])

        errors = self.validate_freshness_fixture(*fixture)

        self.assertEqual([], errors)

    def test_freshness_rejects_conflicting_disposition_fields(self) -> None:
        fixture = self.freshness_fixture()
        catalog = fixture[0]
        finding = catalog["batches"][0]["results"][0]["findings"][0]
        finding["source_id"] = "official-source"
        finding["resolution"] = "Contradictory queued resolution."

        queued_errors = self.validate_freshness_fixture(*fixture)

        self.assertTrue(
            any("queued disposition has conflicting fields" in error for error in queued_errors)
        )

        applied_fixture = self.freshness_fixture()
        catalog = applied_fixture[0]
        result = catalog["batches"][0]["results"][0]
        finding = result["findings"][0]
        finding.update(
            {
                "url": "https://example.com/current",
                "catalog_status": "registered",
                "disposition": "applied",
                "source_id": "official-source",
                "resolution": "Applied.",
            }
        )
        result["checks"]["official_release_channels"]["status"] = "passed"
        result["outcome"] = "current"
        catalog["batches"][0]["summary"] = validator.source_freshness_summary([result])

        applied_errors = self.validate_freshness_fixture(*applied_fixture)

        self.assertTrue(
            any("applied disposition has conflicting fields" in error for error in applied_errors)
        )

    def test_freshness_does_not_treat_rejected_candidate_as_queued(self) -> None:
        fixture = self.freshness_fixture()
        catalog = fixture[0]
        fixture[3][0]["review_status"] = "rejected"
        result = catalog["batches"][0]["results"][0]
        finding = result["findings"][0]
        finding["disposition"] = "no-action"
        finding["resolution"] = "Rejected after review."
        del finding["candidate_id"]
        result["checks"]["official_release_channels"]["status"] = "passed"
        result["outcome"] = "current"
        catalog["batches"][0]["summary"] = validator.source_freshness_summary([result])

        errors = self.validate_freshness_fixture(*fixture)

        self.assertTrue(any("catalog status is stale" in error for error in errors))

    def test_canonical_alias_requires_matching_health_url(self) -> None:
        fixture = self.freshness_fixture()
        sources = fixture[2]
        health = fixture[4]
        health[0]["url"] = "https://unrelated.example/source"

        all_aliases, aliases_by_id = validator.registered_url_aliases(sources, health)

        self.assertNotIn("https://example.com/current", all_aliases)
        self.assertEqual({"https://example.com/old"}, aliases_by_id["official-source"])

    def test_freshness_rejects_future_scan_chronology(self) -> None:
        fixture = self.freshness_fixture()
        catalog = fixture[0]
        result = catalog["batches"][0]["results"][0]
        result["scanned_on"] = "2099-01-01"

        errors = self.validate_freshness_fixture(*fixture)

        self.assertTrue(any("scanned_on cannot be in the future" in error for error in errors))
        self.assertTrue(any("scanned_on follows completed_on" in error for error in errors))

    def test_source_freshness_schema_is_applied(self) -> None:
        schema = json.loads(
            (Path(__file__).parents[1] / "schemas/source-freshness-catalog.schema.json").read_text(
                encoding="utf-8"
            )
        )
        errors: list[str] = []

        validator.validate_json_schema(
            {"schema_version": 1, "rubric_version": 1, "batches": [], "extra": True},
            schema,
            "test catalog",
            errors,
        )

        self.assertTrue(any("schema violation" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
