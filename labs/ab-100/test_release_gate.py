"""Requirement-based checks for the teaching gate, not service authorization."""

import copy
import json
from pathlib import Path
import unittest

from release_gate import assess_release, outcome_cost


class ReleaseGateTests(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads(Path(__file__).with_name("starter-evidence.json").read_text(encoding="utf-8"))
        self.evidence["results"][1].update(status="pass", trace="synthetic:denied-01")

    def check_blocked(self, evidence):
        self.assertFalse(assess_release("service-case-v1", evidence)["eligible"])

    def test_complete_fixture_is_eligible_for_owner_review(self):
        result = assess_release("service-case-v1", self.evidence)
        self.assertTrue(result["eligible"])
        self.assertEqual((result["passed"], result["planned"], result["coverage"]), (6, 6, 1.0))

    def test_missing_case_cannot_improve_denominator(self):
        del self.evidence["results"][1]
        result = assess_release("service-case-v1", self.evidence)
        self.assertFalse(result["eligible"])
        self.assertEqual((result["passed"], result["planned"]), (5, 6))
        self.assertAlmostEqual(result["coverage"], 5 / 6)

    def test_failed_or_unresolved_required_case_blocks(self):
        for state in ("fail", "error", "timeout", "skipped", "not-run", "PASS", None):
            with self.subTest(state=state):
                self.evidence["results"][1]["status"] = state
                self.check_blocked(self.evidence)

    def test_duplicate_case_blocks(self):
        self.evidence["results"].append(copy.deepcopy(self.evidence["results"][0]))
        self.check_blocked(self.evidence)

    def test_unexpected_case_blocks(self):
        self.evidence["results"].append({"case": "unplanned", "status": "pass", "trace": "synthetic:extra"})
        self.check_blocked(self.evidence)

    def test_wrong_candidate_blocks(self):
        self.evidence["candidate"] = "service-case-v2"
        self.check_blocked(self.evidence)

    def test_unfinished_run_blocks(self):
        self.evidence["run_status"] = "running"
        self.check_blocked(self.evidence)

    def test_missing_trace_blocks(self):
        self.evidence["results"][0]["trace"] = "  "
        self.check_blocked(self.evidence)

    def test_invalid_result_collection_blocks(self):
        for rows in (None, {}, ["pass"]):
            with self.subTest(rows=rows):
                self.evidence["results"] = rows
                self.check_blocked(self.evidence)

    def test_missing_candidate_blocks(self):
        self.evidence["candidate"] = ""
        self.assertFalse(assess_release("", self.evidence)["eligible"])

    def test_pilot_b_worked_answer(self):
        self.assertEqual(outcome_cost(7200, 600, 240),
                         {"acceptance_rate": 0.4, "credits_per_accepted": 30.0})

    def test_zero_acceptances_have_undefined_unit_cost(self):
        self.assertEqual(outcome_cost(7200, 600, 0),
                         {"acceptance_rate": 0.0, "credits_per_accepted": None})

    def test_invalid_counts_are_rejected(self):
        for counts in ((1, 0, 0), (1, 2, 3), (-1, 2, 1), (True, 2, 1), (1, 2.0, 1)):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                outcome_cost(*counts)


if __name__ == "__main__":
    unittest.main()
