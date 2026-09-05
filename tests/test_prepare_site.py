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
                "level": "intermediate",
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
        self.vendors = [
            {"id": "github", "name": "GitHub"},
            {"id": "hashicorp", "name": "HashiCorp"},
        ]

    def test_exam_cards_use_built_site_urls(self) -> None:
        card = prepare_site.render_exam_card(self.exams[0], page_prefix="../")
        self.assertIn('href="../guides/GH-999-example/"', card)
        self.assertNotIn("GH-999-example.md", card)
        self.assertIn("Intermediate", card)

    def test_exam_sort_uses_level_then_natural_exam_code(self) -> None:
        exams = [
            dict(self.exams[0], code="GH-10", level="intermediate"),
            dict(self.exams[0], code="GH-1", level="expert"),
            dict(self.exams[0], code="GH-2", level="intermediate"),
            dict(self.exams[0], code="GH-900", level="beginner"),
        ]

        ordered = sorted(exams, key=prepare_site.exam_sort_key)

        self.assertEqual(
            ["GH-900", "GH-2", "GH-10", "GH-1"],
            [str(exam["code"]) for exam in ordered],
        )

    def test_vendor_page_groups_levels_and_sorts_codes(self) -> None:
        exams = [
            dict(self.exams[0], code="GH-10", level="intermediate"),
            dict(self.exams[0], code="GH-2", level="intermediate"),
            dict(self.exams[0], code="GH-900", level="beginner"),
        ]

        page = prepare_site.render_vendor_catalog(self.vendors[0], exams, self.vendors)

        self.assertLess(page.index("Beginner and foundational"), page.index("Intermediate, associate, and specialty"))
        self.assertLess(page.index("GH-2"), page.index("GH-10"))

    def test_navigation_is_generated_from_catalog_entries(self) -> None:
        nav = prepare_site.render_nav(self.exams, self.collections, self.vendors)
        self.assertIn('"GitHub": exams/github.md', nav)
        self.assertNotIn("GH-999 — Example Exam", nav)
        self.assertNotIn("guides/GH-999-example.md", nav)
        self.assertIn('"Examples": "collections/examples.md"', nav)
        self.assertIn("Partner learning journeys:", nav)
        self.assertIn(
            "Frontier Transformation Engineer: docs/learning-journeys/frontier-transformation-engineer.md",
            nav,
        )
        self.assertIn("Partner AI references:", nav)
        self.assertIn(
            "OpenAI AI Foundations: docs/partner-ai/openai-ai-foundations.md",
            nav,
        )
        self.assertIn(
            "Anthropic Claude Certified Architect: docs/partner-ai/anthropic-claude-certified-architect-foundations.md",
            nav,
        )

    def test_navigation_and_homepage_use_registered_vendors(self) -> None:
        terraform_exam = dict(
            self.exams[0],
            code="TERRAFORM-ASSOCIATE-004",
            vendor_id="hashicorp",
            title="Terraform Associate (004)",
        )
        nav = prepare_site.render_nav(
            [terraform_exam], self.collections, self.vendors
        )
        self.assertIn('"HashiCorp": exams/hashicorp.md', nav)
        self.assertNotIn("exams/microsoft.md", nav)
        homepage = prepare_site.render_homepage(
            "{{TRACK_CARDS}} {{REFERENCE_CARDS}} {{GUIDE_COUNT}} {{SOURCE_COUNT}} "
            "{{COLLECTION_CARDS}} {{GENERATED_DATE}}",
            [terraform_exam],
            [],
            1,
            self.vendors,
        )
        self.assertIn("track-card--hashicorp", homepage)
        self.assertIn("TERRAFORM-ASSOCIATE-004", homepage)
        self.assertNotIn("track-card--microsoft", homepage)
        self.assertIn("OpenAI — AI Foundations", homepage)
        self.assertIn("Invite-only certification reference", homepage)
        self.assertIn("public Academy course is preparation, not the certification", homepage)
        self.assertIn("Anthropic — Claude Certified Architect, Foundations", homepage)
        self.assertIn("public Claude Academy courses provide a timed technical preparation path", homepage)

    def test_catalog_keeps_partner_references_separate_from_guides(self) -> None:
        catalog = prepare_site.render_catalog(self.exams, self.vendors)

        self.assertIn("## Certification references", catalog)
        self.assertIn("OpenAI — AI Foundations", catalog)
        self.assertIn("Anthropic — Claude Certified Architect, Foundations", catalog)
        self.assertIn("references—not objective-mapped guides", catalog)

    def test_collection_cards_link_to_generated_collection_page(self) -> None:
        card = prepare_site.render_collection_card(self.collections[0])
        self.assertIn('href="collections/examples/"', card)
        self.assertIn("1 guides", card)
        self.assertIn("GH-999", card)

    def test_collection_card_codes_use_level_then_natural_sort(self) -> None:
        exams = [
            dict(self.exams[0], code="GH-10", level="intermediate"),
            dict(self.exams[0], code="GH-2", level="intermediate"),
            dict(self.exams[0], code="GH-1", level="expert"),
            dict(self.exams[0], code="GH-900", level="beginner"),
        ]
        collection = dict(
            self.collections[0],
            exam_codes=["GH-1", "GH-10", "GH-900", "GH-2"],
        )

        card = prepare_site.render_collection_card(
            collection,
            exams_by_code={str(exam["code"]): exam for exam in exams},
        )

        self.assertIn("GH-900 · GH-2 · GH-10 · GH-1", card)

    def test_collection_page_links_to_guides_from_nested_url(self) -> None:
        page = prepare_site.render_collection_page(
            self.collections[0], {"GH-999": self.exams[0]}
        )
        self.assertIn('href="../../guides/GH-999-example/"', page)
        self.assertIn("not an official sequence", page)

    def test_publication_allowlist_excludes_background_conversation(self) -> None:
        self.assertNotIn("docs/initialChat.md", prepare_site.PUBLIC_DOCUMENTS)
        self.assertIn("docs/AI-AUDIT.md", prepare_site.PUBLIC_DOCUMENTS)
        self.assertIn(
            "docs/learning-journeys/frontier-transformation-engineer.md",
            prepare_site.PUBLIC_DOCUMENTS,
        )

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

    def test_extracts_unweighted_domains_without_inventing_percentages(self) -> None:
        guide = """## Objective map

| Domain | Weight | Coverage |
|---|---:|---|
| Infrastructure as Code | Not published | Part 1 |
| Terraform fundamentals | Not published | Part 2 |
"""
        self.assertEqual(
            prepare_site.extract_domain_rows(guide),
            [
                ("Infrastructure as Code", "Not published"),
                ("Terraform fundamentals", "Not published"),
            ],
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
