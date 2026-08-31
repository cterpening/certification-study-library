from datetime import date
from email.message import Message
from io import BytesIO
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_source_health as source_health  # noqa: E402


class FakeResponse:
    def __init__(self, body: bytes, *, url: str = "https://example.com/course") -> None:
        self._body = BytesIO(body)
        self._url = url
        self.headers = Message()
        self.headers["Content-Type"] = "text/html; charset=utf-8"

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_args: object) -> None:
        return None

    def getcode(self) -> int:
        return 200

    def geturl(self) -> str:
        return self._url

    def read(self, size: int = -1) -> bytes:
        return self._body.read(size)


class SourceHealthTests(unittest.TestCase):
    def test_extracts_title_canonical_and_duration_signals(self) -> None:
        html = """<html><head>
<title>Fallback title</title>
<meta property="og:title" content="Current Course">
<link rel="canonical" href="https://example.com/current-course">
<script type="application/ld+json">{"duration":"PT4H30M"}</script>
</head><body>Four modules take about 5 hours.</body></html>"""
        signals = source_health.extract_page_signals(
            html, "https://example.com/course"
        )
        self.assertEqual(signals["page_title"], "Current Course")
        self.assertEqual(
            signals["canonical_url"], "https://example.com/current-course"
        )
        self.assertIn("PT4H30M", signals["duration_signals"])
        self.assertIn("about 5 hours", signals["duration_signals"])
        self.assertEqual(64, len(signals["signal_fingerprint"]))

    def test_fetch_source_records_redirect_and_signals(self) -> None:
        def opener(_request: object, timeout: float) -> FakeResponse:
            self.assertEqual(timeout, 2.0)
            return FakeResponse(
                b"<html><head><title>Course</title></head></html>",
                url="https://example.com/new-course",
            )

        result = source_health.fetch_source(
            {"id": "course", "url": "https://example.com/course"},
            timeout=2.0,
            opener=opener,
        )
        self.assertEqual("ok", result["status"])
        self.assertEqual("https://example.com/new-course", result["final_url"])
        self.assertEqual("Course", result["page_title"])

    def test_comparison_separates_changes_staleness_and_blocking(self) -> None:
        sources = [
            {
                "id": "course",
                "url": "https://example.com/course",
                "last_checked": "2026-01-01",
            },
            {
                "id": "blocked",
                "url": "https://example.com/blocked",
                "last_checked": "2026-08-01",
            },
        ]
        results = [
            {
                "id": "course",
                "url": "https://example.com/course",
                "status": "ok",
                "final_url": "https://example.com/course",
                "page_title": "New title",
                "canonical_url": "https://example.com/course",
                "duration_signals": ["6 hours"],
            },
            {
                "id": "blocked",
                "url": "https://example.com/blocked",
                "status": "blocked",
                "http_status": 403,
            },
        ]
        previous = {
            "sources": [
                {
                    "id": "course",
                    "status": "ok",
                    "final_url": "https://example.com/course",
                    "page_title": "Old title",
                    "canonical_url": "https://example.com/course",
                    "duration_signals": ["5 hours"],
                }
            ]
        }
        report = source_health.compare_results(
            sources,
            results,
            previous,
            stale_days=90,
            today=date(2026, 8, 31),
        )
        summary = report["summary"]
        self.assertEqual(1, summary["changed"])
        self.assertEqual(1, summary["stale"])
        self.assertEqual(1, summary["blocked"])
        self.assertTrue(summary["needs_review"])


if __name__ == "__main__":
    unittest.main()
