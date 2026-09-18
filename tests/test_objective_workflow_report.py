from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from objective_workflow_report import failure_body, pull_request_body


class ObjectiveWorkflowReportTests(unittest.TestCase):
    def test_pr_permission_failure_is_not_reported_as_provider_failure(self):
        text = failure_body(
            {"changed": ["DP-420"], "errors": [], "manual_review": ["CAD"]},
            {"objectives": {"outcome": "success"}, "snapshot_pr": {"outcome": "failure"}},
            "https://example.com/run", "https://example.com/compare",
            "GraphQL: GitHub Actions is not permitted to create or approve pull requests (createPullRequest)",
        )
        self.assertIn("zero unexpected errors", text)
        self.assertIn("workflow-created pull requests are disabled", text)
        self.assertIn("https://example.com/compare", text)
        self.assertNotIn("unknown", text)

    def test_provider_errors_and_manual_limitations_stay_distinct(self):
        text = failure_body(
            {"changed": [], "errors": ["AZ-104"], "manual_review": ["CAD"]},
            {"objectives": {"outcome": "failure"}}, "run", "compare",
        )
        self.assertIn("failed for: **AZ-104**", text)
        self.assertIn("manual-review limitations: 1", text)
        self.assertNotIn("workflow-created pull requests are disabled", text)

    def test_missing_report_points_to_setup_or_test_failure(self):
        text = failure_body(None, {"tests": {"outcome": "failure"}}, "run", "compare")
        self.assertIn("`tests`", text)
        self.assertIn("No objective report was produced", text)
        self.assertNotIn("retrieval/extraction failed for", text)

    def test_large_multi_provider_change_list_is_kept_in_body(self):
        codes = [f"EXAM-{i}" for i in range(100)]
        text = pull_request_body({"changed": codes})
        self.assertTrue(all(code in text for code in codes))
        self.assertIn("each provider's official sources", text)
        self.assertIn("content review before merging", text)
