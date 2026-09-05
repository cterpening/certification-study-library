import importlib.util
from datetime import date
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "prepare_source_freshness_scan.py"
SPEC = importlib.util.spec_from_file_location("source_freshness_preparer", SCRIPT)
preparer = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(preparer)


class SourceFreshnessPreparerTests(unittest.TestCase):
    def test_baseline_is_order_stable_and_changes_with_official_evidence(self) -> None:
        exam = {
            "code": "EX-100",
            "vendor_id": "example",
            "status": "active",
            "study_guide_url": "https://example.com/ex-100",
            "blueprint_last_checked": "2026-09-05",
            "upcoming_change_status": "none-announced",
            "upcoming_change_checked": "2026-09-05",
            "review_status": "source-validated",
        }
        sources = [
            {
                "id": "two",
                "url": "https://example.com/two",
                "authority_class": 2,
                "source_type": "product-documentation",
                "last_checked": "2026-09-05",
            },
            {
                "id": "one",
                "url": "https://example.com/one",
                "authority_class": 1,
                "source_type": "exam-blueprint",
                "last_checked": "2026-09-05",
            },
        ]

        baseline = preparer.source_freshness_baseline_sha256(
            exam, "guide", sources
        )

        self.assertEqual(
            baseline,
            preparer.source_freshness_baseline_sha256(
                exam, "guide", list(reversed(sources))
            ),
        )
        changed = [dict(source) for source in sources]
        changed[0]["url"] = "https://example.com/two-new"
        self.assertNotEqual(
            baseline,
            preparer.source_freshness_baseline_sha256(exam, "guide", changed),
        )
        self.assertNotEqual(
            baseline,
            preparer.source_freshness_baseline_sha256(exam, "changed guide", sources),
        )

    def test_completed_scans_are_bound_to_baseline_rubric_and_latest_date(self) -> None:
        catalog = {
            "batches": [
                {
                    "status": "completed",
                    "rubric_version": 1,
                    "created_on": "2026-09-01",
                    "completed_on": "2026-09-01",
                    "results": [
                        {
                            "exam_code": "EX-100",
                            "baseline_sha256": "abc",
                            "scanned_on": "2026-09-01",
                            "outcome": "current",
                        }
                    ],
                },
                {
                    "status": "completed",
                    "rubric_version": 1,
                    "created_on": "2026-09-05",
                    "completed_on": "2026-09-05",
                    "results": [
                        {
                            "exam_code": "EX-100",
                            "baseline_sha256": "abc",
                            "scanned_on": "2026-09-05",
                            "outcome": "review-required",
                        }
                    ],
                },
                {
                    "status": "in-progress",
                    "rubric_version": 1,
                    "results": [
                        {
                            "exam_code": "EX-200",
                            "baseline_sha256": "def",
                            "scanned_on": "2026-09-05",
                        }
                    ],
                },
            ]
        }

        completed = preparer.completed_current_scans(catalog, date(2026, 9, 5))

        self.assertEqual(date(2026, 9, 5), completed[("EX-100", "abc", 1)])
        self.assertNotIn(("EX-100", "changed", 1), completed)
        self.assertNotIn(("EX-100", "abc", 2), completed)
        self.assertNotIn(("EX-200", "def", 1), completed)

    def test_official_source_filter_excludes_third_party_material(self) -> None:
        sources = [
            {
                "id": "blueprint",
                "authority_class": 1,
                "source_type": "exam-blueprint",
                "access_model": "public",
                "supported_exams": ["EX-1"],
            },
            {
                "id": "docs",
                "authority_class": 2,
                "source_type": "product-documentation",
                "access_model": "public",
                "supported_exams": ["EX-1"],
            },
            {
                "id": "training",
                "authority_class": 3,
                "source_type": "official-training",
                "access_model": "public",
                "supported_exams": ["EX-1"],
            },
            {
                "id": "official-assessment",
                "authority_class": 3,
                "source_type": "independent-assessment",
                "access_model": "public",
                "supported_exams": ["EX-1"],
            },
            {
                "id": "paid-training",
                "authority_class": 3,
                "source_type": "official-training",
                "access_model": "paid",
                "supported_exams": ["EX-1"],
            },
            {
                "id": "expert",
                "authority_class": 2,
                "source_type": "expert-resource",
                "access_model": "public",
                "supported_exams": ["EX-1"],
            },
            {
                "id": "book",
                "authority_class": 4,
                "source_type": "third-party-training",
                "access_model": "public",
                "supported_exams": ["EX-1"],
            },
        ]

        selected = preparer.official_sources_for_exam(sources, "EX-1")

        self.assertEqual(
            ["blueprint", "docs", "training", "official-assessment"],
            [row["id"] for row in selected],
        )

    def test_blocked_and_future_scans_do_not_suppress_recurrence(self) -> None:
        catalog = {
            "batches": [
                {
                    "status": "completed",
                    "rubric_version": 1,
                    "created_on": "2026-09-05",
                    "completed_on": "2026-09-05",
                    "results": [
                        {
                            "exam_code": "EX-100",
                            "baseline_sha256": "abc",
                            "scanned_on": "2026-09-05",
                            "outcome": "blocked",
                        }
                    ],
                },
                {
                    "status": "completed",
                    "rubric_version": 1,
                    "created_on": "2099-01-01",
                    "completed_on": "2099-01-01",
                    "results": [
                        {
                            "exam_code": "EX-200",
                            "baseline_sha256": "def",
                            "scanned_on": "2099-01-01",
                            "outcome": "current",
                        }
                    ],
                },
            ]
        }

        completed = preparer.completed_current_scans(catalog, date(2026, 9, 5))

        self.assertEqual({}, completed)

    def test_only_queued_candidates_are_prepared(self) -> None:
        candidates = [
            {
                "id": status,
                "suggested_exams": ["EX-1"],
                "review_status": status,
            }
            for status in ("queued", "in-review", "rejected")
        ]

        selected = preparer.queued_candidates_for_exam(candidates, "EX-1")

        self.assertEqual(["queued"], [row["id"] for row in selected])


if __name__ == "__main__":
    unittest.main()
