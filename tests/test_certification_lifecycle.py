from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from certification_lifecycle import render_lifecycle_page


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.catalog = {
            "lifecycle_as_of": "2026-09-30",
            "catalog_sources": [{"id": "example-current", "last_verified": "2026-09-01"}],
            "certifications": [{
                "vendor_id": "example", "exam_code": "EX-100", "title": "Current",
                "official_url": "https://example.com/ex", "status": "active",
                "source_id": "example-current", "aliases": ["Former"],
                "lifecycle": {"checked_on": "2026-09-29", "blueprint_updates": [
                    {"effective_on": day, "language": language,
                     "source_url": "https://example.com/blueprint"}
                    for day, language in [("2026-07-22", "en"), ("2026-10-14", "en"),
                                          ("2026-09-30", "ja"), ("2026-11-01", "en")]
                ]}}],
        }

    def test_future_outline_is_not_shown_as_effective_and_languages_stay_separate(self):
        page = render_lifecycle_page(self.catalog)
        upcoming, past = page.split("## Effective and past dates")
        self.assertIn("| 2026-10-14 | [EX-100", upcoming)
        self.assertIn("| 2026-11-01 | [EX-100", upcoming)
        self.assertNotIn("| 2026-10-14 | [EX-100", past)
        self.assertIn("| 2026-07-22 | [EX-100", past)
        self.assertIn("| 2026-09-30 | [EX-100", past)
        self.assertIn("| Skills measured as of | en |", page)
        self.assertIn("| Skills measured as of | ja |", page)
        self.assertIn("| 2026-09-29 |", page)
        self.assertIn("| example / EX-100 | Current | Former |", page)

    def test_advancing_view_moves_update_and_preserves_next_announcement(self):
        self.catalog["lifecycle_as_of"] = "2026-10-14"
        page = render_lifecycle_page(self.catalog)
        upcoming, past = page.split("## Effective and past dates")
        self.assertIn("| 2026-11-01 | [EX-100", upcoming)
        self.assertNotIn("| 2026-10-14 | [EX-100", upcoming)
        self.assertIn("| 2026-10-14 | [EX-100", past)

    def test_unknown_dates_are_not_inferred_from_catalog_review_or_status(self):
        del self.catalog["certifications"][0]["lifecycle"]
        page = render_lifecycle_page(self.catalog)
        self.assertIn("1 still need date research", page)
        self.assertIn("| example | 1 | 0 | 1 | [EX-100](<https://example.com/ex>) |", page)
        self.assertNotIn("| [EX-100", page.split("## Coverage and research queue")[0])
        self.assertNotIn("2026-09-01 | [EX-100", page)
        self.assertNotIn("No retirement", page)

    def test_beta_release_retirement_and_replacement_keep_their_own_sources(self):
        row = self.catalog["certifications"][0]
        row["lifecycle"]["initial_release"] = {
            "date": "2025-10-01", "stage": "beta", "scope": "English only",
            "source_url": "https://example.com/beta"}
        row.update(status="retired", retirement_date="2026-09-01",
                   replacement_exam_code="EX-200",
                   replacement_official_url="https://example.com/new")
        page = render_lifecycle_page(self.catalog)
        self.assertIn("| 2025-10-01 | [EX-100", page)
        self.assertIn("| Exam/version beta |", page)
        self.assertIn("| Exam/version beta | English only |", page)
        self.assertIn("| 2026-09-01 | [EX-100", page)
        self.assertIn("Retirement → [EX-200](<https://example.com/new>)", page)
        row.update(retirement_scope="English only",
                   retirement_source_url="https://example.com/notice")
        page = render_lifecycle_page(self.catalog)
        self.assertIn("| English only | [Official source](<https://example.com/notice>)", page)

    def test_rendering_does_not_mutate_records_and_escapes_table_content(self):
        self.catalog["certifications"][0]["title"] = "Name | <test> [other]"
        before = deepcopy(self.catalog)
        page = render_lifecycle_page(self.catalog)
        self.assertEqual(before, self.catalog)
        self.assertIn("Name &#124; &lt;test&gt; &#91;other]", page)
        self.assertEqual(page, render_lifecycle_page(self.catalog))


if __name__ == "__main__":
    unittest.main()
