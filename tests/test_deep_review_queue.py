import copy
from datetime import date
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from prepare_deep_review_queue import build_queue, guide_hash


class DeepReviewQueueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "guide.md").write_text("Example guide\n", encoding="utf-8")
        (self.root / "report.md").write_text("Reviewed\n", encoding="utf-8")
        (self.root / "evidence.json").write_text("{}", encoding="utf-8")
        self.exam = {"code":"MS-1", "vendor_id":"microsoft", "title":"Example", "status":"active",
                     "guide_path":"guide.md", "study_guide_url":"https://example.com/exam"}
        self.program = {"started_on":"2026-09-27", "review_interval_days":30, "reviews":[]}
        self.receipt = {"exam_code":"MS-1", "reviewed_on":"2026-09-27", "guide_sha256":guide_hash(self.root / "guide.md"),
                        "objective_count":1, "outcome":"reviewed", "report_path":"report.md",
                        "evidence_paths":["evidence.json"], "lab_execution":"not-executed", "remaining_limits":[]}

    def queue(self, day=date(2026, 9, 27), events=None):
        return build_queue(self.root, [self.exam], self.program, events or [], day, ["microsoft"])

    def test_missing_receipt_is_pending_even_when_existing_guide_is_source_validated(self):
        self.exam["review_status"]="source-validated"
        self.assertEqual(self.queue()["next_batch"], ["MS-1"])
        self.assertEqual(self.queue()["exams"][0]["state"], "pending")

    def test_receipt_does_not_imply_live_lab_execution(self):
        self.program["reviews"]=[self.receipt]
        row=self.queue()["exams"][0]
        self.assertFalse(row["needs_review"])
        self.assertEqual(row["lab_execution"], "not-executed")

    def test_changed_text_and_age_reopen_review_without_mutating_receipts(self):
        self.program["reviews"]=[self.receipt]
        before=copy.deepcopy(self.program)
        self.assertEqual(self.queue(date(2026,10,28))["exams"][0]["state"], "review-due")
        (self.root / "guide.md").write_text("Changed\n", encoding="utf-8")
        self.assertEqual(self.queue()["exams"][0]["state"], "changed-since-review")
        self.assertEqual(before,self.program)

    def test_blockers_and_due_events_remain_visible(self):
        self.receipt["outcome"]="reviewed-with-blockers"
        self.program["reviews"]=[self.receipt]
        self.assertTrue(self.queue()["exams"][0]["needs_review"])
        self.receipt["outcome"]="reviewed"
        event={"id":"change", "exam_codes":["MS-1"], "review_on":"2026-09-27"}
        self.assertTrue(self.queue(events=[event])["exams"][0]["needs_review"])

    def test_future_receipt_cannot_complete_current_review(self):
        self.receipt["reviewed_on"]="2026-10-01"
        self.program["reviews"]=[self.receipt]
        self.assertEqual(self.queue()["exams"][0]["state"], "pending")

    def test_retired_guide_is_archived_even_when_old_event_is_overdue(self):
        self.exam["status"] = "retired"
        event = {"id":"retirement", "exam_codes":["MS-1"], "review_on":"2026-09-01"}
        report = self.queue(events=[event])
        self.assertEqual(report["exams"][0]["state"], "archived")
        self.assertFalse(report["exams"][0]["needs_review"])
        self.assertEqual(report["next_batch"], [])

    def test_missing_evidence_and_unknown_exam_fail_closed(self):
        self.program["reviews"]=[self.receipt]
        (self.root / "evidence.json").unlink()
        with self.assertRaises(ValueError):self.queue()
        self.receipt["exam_code"]="UNKNOWN"
        with self.assertRaises(ValueError):self.queue()

    def test_vendor_and_batch_constraints(self):
        with self.assertRaises(ValueError):build_queue(self.root,[self.exam],self.program,[],date.today(),["unknown"])
        with self.assertRaises(ValueError):build_queue(self.root,[self.exam],self.program,[],date.today(),["microsoft"],13)


if __name__ == "__main__":
    unittest.main()
