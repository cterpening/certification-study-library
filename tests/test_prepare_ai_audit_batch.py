import importlib.util
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "scripts" / "prepare_ai_audit_batch.py"
SPEC = importlib.util.spec_from_file_location("ai_audit_batch_preparer", SCRIPT)
preparer = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(preparer)


class AIAuditBatchPreparerTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        root_patch = patch.object(preparer, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.guide = self.root / "guide.md"
        self.guide.write_bytes(b"# Guide\n\nOriginal content.\n")
        self.snapshot = self.root / "objectives.txt"
        self.snapshot.write_bytes(b"Official objective\n")
        self.exam = {
            "code": "EX-100", "vendor_id": "example", "title": "Example",
            "status": "active", "upcoming_change_status": "none",
            "blueprint_last_checked": "2026-09-05", "guide_path": "guide.md",
            "study_guide_url": "https://example.com/objectives",
        }
        self.review = {
            "id": "review-example", "blueprint_snapshot_path": "objectives.txt",
            "blueprint_snapshot_sha256": sha256(self.snapshot.read_bytes()).hexdigest(),
            "exam_code": "EX-100", "review_type": "source-validation",
            "reviewed_on": "2026-09-05", "outcome": "passed",
        }

    def select(self, completed=None, rubric=2, codes=None):
        return preparer.select_items(
            [self.exam], {"EX-100": self.review}, {}, {}, completed or set(),
            rubric, 10, codes or [],
        )

    def completed_fixture(self):
        return preparer.completed_current_audits({"batches": [{
            "status": "completed", "rubric_version": 2, "results": self.select(),
        }]})

    def test_unchanged_guide_is_excluded_but_guide_only_edit_renews_eligibility(self) -> None:
        completed = self.completed_fixture()
        original_blueprint = self.review["blueprint_snapshot_sha256"]
        self.assertEqual([], self.select(completed))

        self.guide.write_bytes(b"# Guide\n\nCorrected explanation.\n")

        selected = self.select(completed)
        self.assertEqual(1, len(selected))
        self.assertEqual(original_blueprint, selected[0]["blueprint_snapshot_sha256"])
        self.assertEqual(sha256(self.guide.read_bytes()).hexdigest(), selected[0]["guide_content_sha256"])

    def test_platform_newlines_do_not_renew_eligibility_but_whitespace_does(self) -> None:
        completed = self.completed_fixture()
        for newline in (b"\r\n", b"\r"):
            self.guide.write_bytes(newline.join([b"# Guide", b"", b"Original content.", b""]))
            self.assertEqual([], self.select(completed))
        self.guide.write_bytes(b"# Guide\n\nOriginal content. \n")
        self.assertEqual(1, len(self.select(completed)))

    def test_changed_blueprint_or_rubric_renews_eligibility(self) -> None:
        completed = self.completed_fixture()
        self.assertEqual(1, len(self.select(completed, rubric=3)))
        self.snapshot.write_bytes(b"Revised official objective\n")
        self.review["blueprint_snapshot_sha256"] = sha256(self.snapshot.read_bytes()).hexdigest()
        self.assertEqual(1, len(self.select(completed)))

    def test_explicit_selection_can_revisit_unchanged_audit(self) -> None:
        completed = self.completed_fixture()
        self.assertEqual(1, len(self.select(completed, codes=["EX-100"])))

    def test_unbound_or_malformed_results_never_suppress_selection(self) -> None:
        item = self.select()[0]
        for guide_hash in (None, "", "not-a-hash", 123):
            with self.subTest(guide_hash=guide_hash):
                result = dict(item)
                if guide_hash is None:
                    del result["guide_content_sha256"]
                else:
                    result["guide_content_sha256"] = guide_hash
                completed = preparer.completed_current_audits({"batches": [{
                    "status": "completed", "rubric_version": 2, "results": [result],
                }]})
                self.assertEqual(set(), completed)
                self.assertEqual(1, len(self.select(completed)))

    def test_legacy_rubric_results_remain_historical(self) -> None:
        completed = preparer.completed_current_audits({"batches": [{
            "status": "completed", "rubric_version": 1, "results": self.select(),
        }]})
        self.assertEqual(set(), completed)

    def test_main_refuses_new_legacy_rubric_manifests(self) -> None:
        args = SimpleNamespace(
            batch_id="test", size=10, exam_code=[], exams=self.guide,
            reviews=self.guide, sources=self.guide, source_health=self.guide,
            audits=self.guide,
        )
        with patch.object(preparer, "parse_args", return_value=args), patch.object(
            preparer, "load_json", return_value={"rubric_version": 1}
        ):
            with self.assertRaisesRegex(ValueError, "New audits require rubric_version >= 2"):
                preparer.main()

    def test_source_index_rejects_duplicate_health_rows(self) -> None:
        with self.assertRaisesRegex(ValueError, "Duplicate source-health id: source"):
            preparer.source_indexes([], [{"id": "source"}, {"id": "source"}])

    def test_default_manifest_reports_source_gate_blockers_without_aborting_queue(self) -> None:
        blocked_exam = dict(self.exam, code="EX-200")
        blocked_review = dict(self.review, exam_code="EX-200", outcome="blocked")
        args = SimpleNamespace(
            batch_id="test", size=10, exam_code=[], exams=self.guide,
            reviews=self.guide, sources=self.guide, source_health=self.guide,
            audits=self.guide, output=None,
        )
        for include_ready in (True, False):
            with self.subTest(include_ready=include_ready):
                catalogs = [
                    {"exams": [self.exam, blocked_exam] if include_ready else [blocked_exam]},
                    {"reviews": [self.review, blocked_review]},
                    {"sources": []}, {"sources": []}, {"rubric_version": 2, "batches": []},
                ]
                output = StringIO()
                with patch.object(preparer, "parse_args", return_value=args), patch.object(
                    preparer, "load_json", side_effect=catalogs
                ), patch("sys.stdout", output):
                    self.assertEqual(0, preparer.main())
                manifest = json.loads(output.getvalue())
                self.assertEqual(["EX-100"] if include_ready else [], [i["exam_code"] for i in manifest["items"]])
                self.assertEqual(["EX-200"], [i["exam_code"] for i in manifest["blocked_items"]])
                self.assertIn("source-validation", manifest["blocked_items"][0]["reason"])

    def test_explicit_request_cannot_bypass_source_validation_gate(self) -> None:
        with self.assertRaisesRegex(ValueError, "No current passed source-validation review for EX-100"):
            preparer.select_items([self.exam], {}, {}, {}, set(), 2, 10, ["EX-100"])

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

    def test_completed_audits_are_bound_to_guide_snapshot_and_rubric(self) -> None:
        catalog = {
            "batches": [
                {
                    "status": "completed",
                    "rubric_version": 2,
                    "results": [
                        {
                            "exam_code": "EX-100",
                            "blueprint_snapshot_sha256": "abc",
                            "guide_content_sha256": "a" * 64,
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
                            "guide_content_sha256": "b" * 64,
                        }
                    ],
                },
            ]
        }

        completed = preparer.completed_current_audits(catalog)

        self.assertIn(("EX-100", "abc", "a" * 64, 2), completed)
        self.assertNotIn(("EX-100", "changed", "a" * 64, 2), completed)
        self.assertNotIn(("EX-100", "abc", "b" * 64, 2), completed)
        self.assertNotIn(("EX-100", "abc", "a" * 64, 3), completed)
        self.assertNotIn(("EX-200", "def", "b" * 64, 2), completed)

    def test_natural_key_orders_numeric_exam_codes_naturally(self) -> None:
        values = ["EX-100", "EX-20", "EX-3"]

        self.assertEqual(
            ["EX-3", "EX-20", "EX-100"],
            sorted(values, key=preparer.natural_key),
        )


if __name__ == "__main__":
    unittest.main()
