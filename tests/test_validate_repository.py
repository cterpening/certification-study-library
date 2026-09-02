import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("repository_validator", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class RepositoryValidationTests(unittest.TestCase):
    def test_generated_site_source_tree_is_not_revalidated_as_repository_content(self) -> None:
        self.assertIn(".site-build", validator.IGNORED_MARKDOWN_DIRS)

    def test_parses_required_guide_front_matter(self) -> None:
        text = """---
exam_code: GH-900
official_blueprint: https://example.com/gh-900
review_status: ai-generated-draft
---
# Guide
"""
        metadata = validator.parse_front_matter(text)
        self.assertEqual("GH-900", metadata["exam_code"])
        self.assertEqual(
            "https://example.com/gh-900", metadata["official_blueprint"]
        )

    def test_validates_dates_and_public_urls(self) -> None:
        self.assertTrue(validator.valid_date("2026-08-30"))
        self.assertFalse(validator.valid_date("08/30/2026"))
        self.assertTrue(validator.valid_public_url("https://docs.github.com/"))
        self.assertFalse(validator.valid_public_url("docs/private.md"))

    def test_heading_parser_ignores_fenced_code(self) -> None:
        markdown = """# Guide title

## Major section

```bash
# shell comment
## another shell comment
```

### Nested topic
"""
        self.assertEqual([1, 2, 3], validator.markdown_heading_levels(markdown))

    def test_renders_python_friendly_certification_query_seeds(self) -> None:
        certifications = [
            {
                "vendor_id": "example",
                "exam_code": "EX-100",
                "title": "Example Certification",
                "status": "active",
                "review_status": "source-validated",
                "guide_path": "guides/EX-100-example.md",
                "study_guide_url": "https://example.com/ex-100",
            }
        ]

        rendered = validator.render_certification_list(certifications)

        self.assertEqual(
            "vendor_id\texam_code\ttitle\n"
            "example\tEX-100\tExample Certification\n",
            rendered,
        )

    def test_retirement_metadata_is_validated_and_replacement_is_cataloged(self) -> None:
        source = {
            "id": "example-current",
            "vendor_id": "example",
            "catalog_url": "https://example.com/certifications",
            "selection": "Every current example certification.",
            "last_verified": "2026-08-31",
        }
        retiring = {
            "vendor_id": "example",
            "exam_code": "EX-100",
            "title": "Retiring example",
            "official_url": "https://example.com/ex-100",
            "status": "retirement-announced",
            "retirement_date": "2026-09-30",
            "replacement_exam_code": "EX-200",
            "replacement_official_url": "https://example.com/ex-200",
            "source_id": "example-current",
        }
        replacement = {
            "vendor_id": "example",
            "exam_code": "EX-200",
            "title": "Replacement example",
            "official_url": "https://example.com/ex-200",
            "status": "beta",
            "source_id": "example-current",
        }
        errors: list[str] = []

        validator.validate_certification_seed_catalog(
            {"catalog_sources": [source], "certifications": [retiring, replacement]},
            [],
            {"example"},
            errors,
        )

        lifecycle_errors = [
            error for error in errors if not error.startswith("CERTIFICATIONS.txt is stale")
        ]
        self.assertEqual([], lifecycle_errors)

        missing_date = dict(retiring)
        del missing_date["retirement_date"]
        errors = []
        validator.validate_certification_seed_catalog(
            {
                "catalog_sources": [source],
                "certifications": [missing_date, replacement],
            },
            [],
            {"example"},
            errors,
        )
        self.assertTrue(any("needs a retirement_date" in error for error in errors))

    def test_certification_seed_accepts_vendor_codes_that_begin_with_digits(self) -> None:
        source = {
            "id": "example-current",
            "vendor_id": "example",
            "catalog_url": "https://example.com/certifications",
            "selection": "Every selected example certification.",
            "last_verified": "2026-09-01",
        }
        certification = {
            "vendor_id": "example",
            "exam_code": "220-1201",
            "title": "Example component exam",
            "official_url": "https://example.com/220-1201",
            "status": "active",
            "source_id": "example-current",
        }
        errors: list[str] = []

        validator.validate_certification_seed_catalog(
            {"catalog_sources": [source], "certifications": [certification]},
            [],
            {"example"},
            errors,
        )

        code_errors = [error for error in errors if "exam code" in error]
        self.assertEqual([], code_errors)


if __name__ == "__main__":
    unittest.main()
