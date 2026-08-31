from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_site  # noqa: E402


class GeneratedSiteValidationTests(unittest.TestCase):
    def test_accepts_existing_page_asset_and_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "assets").mkdir()
            (site / "assets" / "site.css").write_text("body {}", encoding="utf-8")
            (site / "guide").mkdir()
            (site / "guide" / "index.html").write_text(
                '<h1 id="start">Start</h1>', encoding="utf-8"
            )
            (site / "index.html").write_text(
                '<link href="assets/site.css"><a href="guide/#start">Guide</a>',
                encoding="utf-8",
            )
            self.assertEqual(validate_site.validate_site(site), [])

    def test_reports_missing_page_and_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "guide").mkdir()
            (site / "guide" / "index.html").write_text(
                '<h1 id="start">Start</h1>', encoding="utf-8"
            )
            (site / "index.html").write_text(
                '<a href="missing/">Missing</a>'
                '<a href="guide/#wrong">Wrong anchor</a>',
                encoding="utf-8",
            )
            errors = validate_site.validate_site(site)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("Broken generated link" in error for error in errors))
            self.assertTrue(any("Missing generated anchor" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
