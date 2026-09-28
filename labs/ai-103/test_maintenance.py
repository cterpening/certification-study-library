import json
from pathlib import Path
import unittest

from maintenance import Proposal, WorkOrders, retrieval_metrics


class RetrievalTests(unittest.TestCase):
    def test_five_hand_calculated_cases(self):
        cases = json.loads(Path(__file__).with_name("retrieval-cases.json").read_text(encoding="utf-8"))
        self.assertEqual(len(cases), 5)
        for case in cases:
            with self.subTest(case=case["name"]):
                actual = retrieval_metrics(case["retrieved"], case["relevant"], case["authorized"])
                self.assertAlmostEqual(actual["precision"], case["expected_precision"])
                self.assertEqual(actual["recall"], case["expected_recall"])
                self.assertEqual(actual["unauthorized_ids"], case["expected_breaches"])
                self.assertEqual(actual["abstain"], case["expected_abstain"])

    def test_unauthorized_ground_truth_rejected(self):
        with self.assertRaises(ValueError):
            retrieval_metrics(["restricted"], ["restricted"], [])

    def test_access_breach_cannot_be_hidden_by_good_recall(self):
        result = retrieval_metrics(["D1", "private"], ["D1"], ["D1"])
        self.assertEqual(result["recall"], 1.0)
        self.assertTrue(result["abstain"])
        self.assertEqual(result["eligible_context"], [])


class WorkOrderTests(unittest.TestCase):
    def setUp(self):
        self.orders = WorkOrders()
        self.proposal = Proposal("operation-1", "P-104", "Inspect noisy pump")

    def test_draft_does_not_write(self):
        self.assertEqual(len(self.orders.records), 0)

    def test_submission_without_approval_denied(self):
        with self.assertRaises(PermissionError):
            self.orders.submit(self.proposal, "technician", "P-104")
        self.assertEqual(len(self.orders.records), 0)

    def test_unauthorized_reviewer_denied(self):
        with self.assertRaises(PermissionError):
            self.orders.approve(self.proposal, "technician")

    def test_changed_description_invalidates_approval(self):
        self.orders.approve(self.proposal, "supervisor")
        changed = Proposal("operation-1", "P-104", "Close the order")
        with self.assertRaises(PermissionError):
            self.orders.submit(changed, "technician", "P-104")
        self.assertEqual(len(self.orders.records), 0)

    def test_wrong_asset_rejected_even_with_approval(self):
        wrong = Proposal("operation-1", "P-140", "Inspect noisy pump")
        self.orders.approve(wrong, "supervisor")
        with self.assertRaises(ValueError):
            self.orders.submit(wrong, "technician", "P-104")
        self.assertEqual(len(self.orders.records), 0)

    def test_authorization_is_separate_from_approval(self):
        self.orders.approve(self.proposal, "supervisor")
        with self.assertRaises(PermissionError):
            self.orders.submit(self.proposal, "visitor", "P-104")

    def test_duplicate_delivery_has_one_effect(self):
        self.orders.approve(self.proposal, "supervisor")
        first = self.orders.submit(self.proposal, "technician", "P-104")
        second = self.orders.submit(self.proposal, "technician", "P-104")
        self.assertEqual((first["status"], second["status"]), ("created", "existing"))
        self.assertEqual(len(self.orders.records), 1)

    def test_timeout_requires_reconciliation(self):
        self.orders.approve(self.proposal, "supervisor")
        with self.assertRaises(TimeoutError):
            self.orders.submit(self.proposal, "technician", "P-104", lose_response=True)
        self.assertEqual(self.orders.status("operation-1"), self.proposal)
        self.assertIsNone(self.orders.status("unknown-operation"))
        self.assertEqual(self.orders.submit(self.proposal, "technician", "P-104")["status"], "existing")
        self.assertEqual(len(self.orders.records), 1)

    def test_operation_id_cannot_be_reused_for_changed_content(self):
        self.orders.approve(self.proposal, "supervisor")
        self.orders.submit(self.proposal, "technician", "P-104")
        changed = Proposal("operation-1", "P-104", "Replace pump")
        self.orders.approve(changed, "supervisor")
        with self.assertRaises(ValueError):
            self.orders.submit(changed, "technician", "P-104")
        self.assertEqual(self.orders.status("operation-1"), self.proposal)

    def test_empty_operation_rejected(self):
        empty = Proposal("", "P-104", "Inspect noisy pump")
        self.orders.approve(empty, "supervisor")
        with self.assertRaises(ValueError):
            self.orders.submit(empty, "technician", "P-104")


if __name__ == "__main__":
    unittest.main()
