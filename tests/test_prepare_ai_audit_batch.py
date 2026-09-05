import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "prepare_ai_audit_batch.py"
SPEC = importlib.util.spec_from_file_location("ai_audit_batch_preparer", SCRIPT)
preparer = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(preparer)


class AIAuditBatchPreparerTests(unittest.TestCase):
    def test_risk_score_prioritizes_change_and_evidence_problems(self) -> None:
        exam = {
            "status": "changing",
            "upcoming_change_status": "scheduled",
            "review_status": "source-validated",
        }
        sources = [{"id": "one"}, {"id": "two"}]
        health = {"one": {"status": "error"}, "two": {"status": "blocked"}}

        score, factors = preparer.risk_factors(
            exam,
            sources,
            health,
            "VERIFY CURRENT\nVERIFY CURRENT\n",
        )

        self.assertEqual(976, score)
        self.assertEqual(
            [
                "exam-status:changing",
                "upcoming-change:scheduled",
                "source-health:error:1",
                "source-health:blocked:1",
                "verify-current-markers:2",
                "human-review-pending",
            ],
            factors,
        )

    def test_completed_audits_are_bound_to_snapshot_and_rubric(self) -> None:
        catalog = {
            "batches": [
                {
                    "status": "completed",
                    "rubric_version": 2,
                    "results": [
                        {
                            "exam_code": "EX-100",
                            "blueprint_snapshot_sha256": "abc",
                        }
                    ],
                },
                {
                    "status": "in-progress",
                    "rubric_version": 2,
                    "results": [
                        {
                            "exam_code": "EX-200",
                            "blueprint_snapshot_sha256": "def",
                        }
                    ],
                },
            ]
        }

        completed = preparer.completed_current_audits(catalog)

        self.assertIn(("EX-100", "abc", 2), completed)
        self.assertNotIn(("EX-100", "changed", 2), completed)
        self.assertNotIn(("EX-100", "abc", 3), completed)
        self.assertNotIn(("EX-200", "def", 2), completed)

    def test_natural_key_orders_numeric_exam_codes_naturally(self) -> None:
        values = ["EX-100", "EX-20", "EX-3"]

        self.assertEqual(
            ["EX-3", "EX-20", "EX-100"],
            sorted(values, key=preparer.natural_key),
        )


if __name__ == "__main__":
    unittest.main()
