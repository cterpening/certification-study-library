from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from objective_workflow_report import changes_body, failure_body


class ObjectiveWorkflowReportTests(unittest.TestCase):
    def test_detected_changes_become_individual_review_checks(self):
        body = changes_body({"results": [
            {"code": "DP-420", "status": "changed", "objectives_changed": True,
             "status_changed": False, "url": "https://example.com/dp-420"},
            {"code": "AZ-104", "status": "unchanged", "url": "https://example.com/az-104"},
        ]}, "https://example.com/run")
        self.assertIn("- [ ] **DP-420** (objectives)", body)
        self.assertIn("https://example.com/run", body)
        self.assertNotIn("AZ-104", body)

    def test_provider_errors_and_manual_limitations_stay_distinct(self):
        text = failure_body(
            {"changed": [], "errors": ["AZ-104"], "manual_review": ["CAD"]},
            {"objectives": {"outcome": "failure"}}, "run",
        )
        self.assertIn("failed for: **AZ-104**", text)
        self.assertIn("manual-review limitations: 1", text)
        self.assertIn("one affected exam at a time", text)

    def test_missing_report_points_to_setup_or_test_failure(self):
        text = failure_body(None, {"tests": {"outcome": "failure"}}, "run")
        self.assertIn("`tests`", text)
        self.assertIn("No objective report was produced", text)
        self.assertNotIn("retrieval/extraction failed for", text)
