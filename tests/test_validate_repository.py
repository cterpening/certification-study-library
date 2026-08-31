import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("repository_validator", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class RepositoryValidationTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
