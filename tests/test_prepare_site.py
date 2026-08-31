from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import prepare_site  # noqa: E402


class SitePreparationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.exams = [
            {
                "code": "GH-999",
                "vendor_id": "github",
                "title": "Example Exam",
                "study_guide_url": "https://example.com/blueprint",
                "guide_path": "guides/GH-999-example.md",
                "blueprint_last_checked": "2026-08-31",
                "upcoming_change_status": "none-announced",
                "review_status": "ai-generated-draft",
                "study_prerequisites": "Example prerequisites.",
            }
        ]
        self.collections = [
            {
                "id": "examples",
                "title": "Examples",
                "summary": "Example collection summary.",
                "exam_codes": ["GH-999"],
            }
        ]

    def test_exam_cards_use_built_site_urls(self) -> None:
        card = prepare_site.render_exam_card(self.exams[0], page_prefix="../")
        self.assertIn('href="../guides/GH-999-example/"', card)
        self.assertNotIn("GH-999-example.md", card)

    def test_navigation_is_generated_from_catalog_entries(self) -> None:
        nav = prepare_site.render_nav(self.exams, self.collections)
        self.assertIn("Overview: exams/github.md", nav)
        self.assertIn("GH-999 — Example Exam", nav)
        self.assertIn("guides/GH-999-example.md", nav)
        self.assertIn('"Examples": "collections/examples.md"', nav)

    def test_collection_cards_link_to_generated_collection_page(self) -> None:
        card = prepare_site.render_collection_card(self.collections[0])
        self.assertIn('href="collections/examples/"', card)
        self.assertIn("1 guides", card)
        self.assertIn("GH-999", card)

    def test_collection_page_links_to_guides_from_nested_url(self) -> None:
        page = prepare_site.render_collection_page(
            self.collections[0], {"GH-999": self.exams[0]}
        )
        self.assertIn('href="../../guides/GH-999-example/"', page)
        self.assertIn("not an official sequence", page)

    def test_publication_allowlist_excludes_background_conversation(self) -> None:
        self.assertNotIn("docs/initialChat.md", prepare_site.PUBLIC_DOCUMENTS)

    def test_yaml_string_quotes_punctuation(self) -> None:
        self.assertEqual(prepare_site.yaml_string("A: B"), '"A: B"')

    def test_extracts_weighted_domains_and_first_lab(self) -> None:
        guide = """## Current objective map

| Domain | Weight | Coverage |
|---|---:|---|
| Explain examples | 20–25% | Part 1 |
| Apply examples | 75–80% | Part 2 |

# Part 3: Labs

## Lab 1: Create an example
"""
        self.assertEqual(
            prepare_site.extract_domain_rows(guide),
            [("Explain examples", "20–25%"), ("Apply examples", "75–80%")],
        )
        self.assertEqual(
            prepare_site.find_first_lab(guide),
            ("Lab 1: Create an example", "lab-1-create-an-example"),
        )

    def test_prepares_guide_metadata_navigation_and_feedback(self) -> None:
        guide = """---
exam_code: GH-999
---

# Example guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** Example.

## Current objective map

| Domain | Weight | Coverage |
|---|---:|---|
| Explain examples | 100–100% | Part 1 |

## Lab 1: Create an example
"""
        prepared = prepare_site.prepare_guide_markdown(guide, self.exams[0])
        self.assertIn("description:", prepared)
        self.assertIn("Study guide at a glance", prepared)
        self.assertIn("Report an issue with GH-999", prepared)
        self.assertIn("Example prerequisites.", prepared)
        self.assertIn("Explain examples", prepared)


if __name__ == "__main__":
    unittest.main()
