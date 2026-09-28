from datetime import date
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from sync_learning_resources import prepare_catalog, replace_catalog_entry, resource_body


class LearningResourceSyncTests(unittest.TestCase):
    def setUp(self):
        self.exam = {"code": "AB-1", "title": "Example", "guide_path": "guides/AB-1-example.md"}
        self.guide = "# Guide\n\n## Places to learn\n\n### Articles\n\n[Report](../docs/report.md#evidence) [Local](#labs) [Web](https://example.com/a)\n\n## Final checks\n\nPrivate to guide.\n"
        self.catalog = "# Catalog\n\n## Selected resources by exam\n\n### AB-1 — Example\n\nStale.\n\n### AB-10 — Another\n\nKeep this.\n\n## AWS\n\nKeep AWS.\n"

    def test_copies_only_resource_section_and_rebases_local_links(self):
        body = resource_body(self.guide, self.exam["guide_path"])
        self.assertIn("#### Articles", body)
        self.assertIn("[Report](report.md#evidence)", body)
        self.assertIn("[Local](../guides/AB-1-example.md#labs)", body)
        self.assertIn("[Web](https://example.com/a)", body)
        self.assertNotIn("Final checks", body)

    def test_update_is_idempotent_and_preserves_other_exams_and_vendors(self):
        updated = replace_catalog_entry(self.catalog, self.exam, self.guide)
        self.assertNotIn("Stale.", updated)
        self.assertIn("### AB-10 — Another\n\nKeep this.", updated)
        self.assertTrue(updated.endswith("## AWS\n\nKeep AWS.\n"))
        self.assertEqual(replace_catalog_entry(updated, self.exam, self.guide), updated)

    def test_missing_exam_is_added_in_selected_section_before_next_vendor(self):
        exam = dict(self.exam, code="AB-2")
        updated = replace_catalog_entry(self.catalog, exam, self.guide)
        self.assertLess(updated.index("### AB-2 —"), updated.index("## AWS"))
        self.assertEqual(replace_catalog_entry(updated, exam, self.guide), updated)

    def test_ambiguous_or_missing_source_sections_fail_before_writing(self):
        for guide in ["# No resources", "## Places to learn\n", self.guide + "\n## Places to learn\n\nOther."]:
            with self.subTest(guide=guide), self.assertRaises(ValueError):
                resource_body(guide, self.exam["guide_path"])
        with self.assertRaises(ValueError):
            replace_catalog_entry(self.catalog + "\n### AB-1 duplicate\n", self.exam, self.guide)

    def test_bulk_reviewed_selection_uses_latest_nonfuture_matching_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for part in ["config", "data", "guides", "docs"]:
                (root / part).mkdir()
            (root / self.exam["guide_path"]).write_text(self.guide, encoding="utf-8")
            (root / "docs/LEARNING-RESOURCES.md").write_text(self.catalog, encoding="utf-8")
            (root / "config/exams.json").write_text(json.dumps({"exams": [self.exam]}), encoding="utf-8")
            receipt = {"exam_code": "AB-1", "reviewed_on": "2026-09-27", "guide_sha256": hashlib.sha256(self.guide.encode()).hexdigest()}
            path = root / "data/deep-reviews.json"
            for records, expected in [
                ([receipt], ["AB-1"]),
                ([dict(receipt, reviewed_on="2026-10-01")], []),
                ([dict(receipt, guide_sha256="old")], []),
                ([receipt, dict(receipt, reviewed_on="2026-09-28", guide_sha256="different")], []),
                ([receipt, dict(receipt, reviewed_on="2026-10-01", guide_sha256="future")], ["AB-1"]),
            ]:
                with self.subTest(records=records):
                    path.write_text(json.dumps({"reviews": records}), encoding="utf-8")
                    _, codes = prepare_catalog(root, None, date(2026, 9, 28))
                    self.assertEqual(codes, expected)
            self.assertEqual((root / "docs/LEARNING-RESOURCES.md").read_text(encoding="utf-8"), self.catalog)
            with self.assertRaises(ValueError):
                prepare_catalog(root, ["UNKNOWN"], date(2026, 9, 28))


if __name__ == "__main__":
    unittest.main()
