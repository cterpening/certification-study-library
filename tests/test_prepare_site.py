from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


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
        self.assertIn("docs/SSH-DIRECT-EVIDENCE.md", prepare_site.PUBLIC_DOCUMENTS)
        self.assertIn(
            "docs/learning-journeys/frontier-transformation-engineer.md",
            prepare_site.PUBLIC_DOCUMENTS,
        )

    @patch.object(prepare_site, "exam_context")
    def test_stages_only_embedded_svg_at_its_guide_relative_path(self, load_context) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            docs_dir = root / ".site-build/docs"
            folder = root / "guides/diagrams/gh-999"
            folder.mkdir(parents=True)
            svg = folder / "request-flow.svg"
            svg.write_text("<svg/>", encoding="utf-8")
            spec = svg.with_suffix(".json")
            spec.write_text("{}", encoding="utf-8")
            (folder / "unpublished.svg").touch()
            embed = r"![An event reaches the handler \[example\]](diagrams/gh-999/request-flow.svg)"
            guide = "\n".join((
                "---", "![Metadata](diagrams/gh-999/absent.svg)", "---",
                "````markdown", "```", "![Example](diagrams/gh-999/absent.svg)", "````",
                "~~~", "![Example](diagrams/gh-999/absent.svg)", "~~~",
                "<!-- Draft", "![Example](diagrams/gh-999/unpublished.svg)", "-->",
                "    ![Indented code](diagrams/gh-999/absent.svg)", embed, embed,
            ))
            with patch.object(prepare_site, "build_diagram") as check:
                published = prepare_site.stage_guide_diagrams(root, docs_dir, self.exams[0], guide)

            self.assertEqual(published, ["guides/diagrams/gh-999/request-flow.svg"])
            self.assertEqual((docs_dir / published[0]).read_bytes(), svg.read_bytes())
            self.assertEqual([p.name for p in (docs_dir / published[0]).parent.iterdir()], [svg.name])
            load_context.assert_called_once_with("gh-999", root)
            check.assert_called_once_with(spec, check=True, root=root, context=load_context.return_value)

            with patch.object(prepare_site, "build_diagram", side_effect=ValueError("stale SVG")):
                new_output = root / "next-build/docs"
                with self.assertRaisesRegex(ValueError, "stale SVG"):
                    prepare_site.stage_guide_diagrams(root, new_output, self.exams[0], guide)
                self.assertFalse(new_output.exists())

    def test_rejects_invalid_diagram_paths_and_empty_alt(self) -> None:
        examples = [
            "![Trace](diagrams/gh-900/request-flow.svg)",
            "![Trace](diagrams/gh-999/../private.svg)",
            "![Trace](diagrams/gh-999/request-flow.json)",
            "![](diagrams/gh-999/request-flow.svg)",
        ]
        with TemporaryDirectory() as temp:
            for embed in examples:
                with self.subTest(embed=embed), self.assertRaisesRegex(ValueError, "Invalid diagram embed"):
                    prepare_site.stage_guide_diagrams(Path(temp), Path(temp), self.exams[0], embed)

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
        self.assertNotIn('href="#key-terms-and-phrases"', prepared)
        with_terms = prepare_site.prepare_guide_markdown(
            guide + "\n## Key terms and phrases\n", self.exams[0]
        )
        self.assertIn('href="#key-terms-and-phrases"', with_terms)
        self.assertNotIn("Listen to the", prepared)
        for code, anchor in (("AZ-900", "azure-fundamentals-az-900"), ("DP-900", "azure-data-fundamentals-dp-900")):
            with self.subTest(code=code):
                podcast_guide = prepare_site.render_guide_start({**self.exams[0], "code": code}, guide)
                self.assertIn(f'href="../../examples/podcasts/#{anchor}"', podcast_guide)


if __name__ == "__main__":
    unittest.main()
