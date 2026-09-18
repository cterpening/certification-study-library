from datetime import date
from email.message import Message
from io import BytesIO
from pathlib import Path
import sys
import unittest
from tempfile import TemporaryDirectory
import json
from unittest.mock import Mock, patch
from argparse import Namespace


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
    def test_saml_login_is_blocked_without_persisting_signed_parameters(self) -> None:
        result = source_health.fetch_source(
            {"id": "course", "url": "https://training.example.com/course?id=123"},
            timeout=2,
            opener=lambda *_args, **_kwargs: FakeResponse(
                b"<html><title>Sign in</title></html>",
                url="https://login.example.com/login/?SAMLRequest=nonce&Signature=signature",
            ),
        )
        self.assertEqual("blocked", result["status"])
        self.assertEqual("https://login.example.com/login/", result["final_url"])
        self.assertNotIn("signature", json.dumps(result))
        self.assertEqual("", result["canonical_url"])

    def test_duration_order_does_not_create_a_change(self) -> None:
        source = {"id": "exam", "last_checked": "2026-09-17", "url": "https://example.com"}
        result = {**source, "status": "ok", "duration_signals": ["2 Hours", "2 hours"]}
        prior = {**result, "duration_signals": ["2 hours", "2 Hours"]}
        report = source_health.compare_results([source], [result], {"sources": [prior]}, stale_days=90)
        self.assertEqual(0, report["summary"]["changed"])
        result["duration_signals"] = ["3 hours"]
        report = source_health.compare_results([source], [result], {"sources": [prior]}, stale_days=90)
        self.assertEqual(1, report["summary"]["changed"])

    def test_subset_write_preserves_unselected_trusted_observations(self) -> None:
        with TemporaryDirectory() as directory:
            snapshot = Path(directory) / "snapshot.json"
            untouched = {"id": "untouched", "status": "ok", "page_title": "Trusted"}
            snapshot.write_text(json.dumps({"sources": [untouched, {"id": "selected"}]}))
            source = {"id": "selected", "url": "https://example.com", "last_checked": "2026-09-17"}
            refreshed = {**source, "status": "ok", "page_title": "Reviewed"}
            args = Namespace(catalog=Path(directory) / "catalog.json", snapshot=snapshot,
                             only=["selected"], max_workers=1, timeout=1, stale_days=90,
                             write=True, report=None, markdown_report=None, github_output=None)
            args.catalog.write_text(json.dumps({"sources": [source]}))
            with patch.object(source_health, "parse_args", return_value=args), patch.object(
                source_health, "fetch_source", return_value=refreshed
            ), patch("builtins.print"):
                self.assertEqual(0, source_health.main())
            rows = source_health.snapshot_by_id(json.loads(snapshot.read_text()))
            self.assertEqual(untouched, rows["untouched"])
            self.assertEqual(refreshed, rows["selected"])

    def test_markdown_report_rejects_invalid_runtime_contracts(self) -> None:
        for report, message in (
            (
                {"checked_on": "2026-09-06", "summary": [], "findings": {}},
                "summary must be an object",
            ),
            (
                {"checked_on": "2026-09-06", "summary": {}, "findings": []},
                "findings must be an object",
            ),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(
                ValueError, message
            ):
                source_health.render_markdown_report(report)

    def test_fetch_rejects_unsafe_url_before_opening(self) -> None:
        opener = Mock()
        source = {"id": "unsafe", "url": "file:///tmp/source"}
        result = source_health.fetch_source(source, timeout=2.0, opener=opener)
        self.assertEqual("error", result["status"])
        self.assertIn("must use HTTPS", result["error"])
        opener.assert_not_called()

    def test_fetch_rejects_non_public_redirect(self) -> None:
        def opener(_request: object, timeout: float) -> FakeResponse:
            self.assertEqual(timeout, 2.0)
            return FakeResponse(b"not used", url="https://127.0.0.1/source")

        result = source_health.fetch_source(
            {"id": "redirect", "url": "https://example.com/source"},
            timeout=2.0,
            opener=opener,
        )
        self.assertEqual("error", result["status"])
        self.assertIn("non-public IP", result["error"])

    def test_snapshot_rejects_duplicate_ids_even_with_different_observations(self) -> None:
        rows = [{"id": "course", "status": "ok"}, {"id": "course", "status": "blocked"}]
        with self.assertRaisesRegex(ValueError, "Duplicate source id: course"):
            source_health.snapshot_by_id({"sources": rows})

    def test_comparison_rejects_duplicate_new_results(self) -> None:
        rows = [{"id": "course"}, {"id": "course"}]
        with self.assertRaisesRegex(ValueError, "Duplicate source id: course"):
            source_health.compare_results([rows[0]], rows, {"sources": []}, stale_days=90)

    def test_duplicate_catalog_or_baseline_is_rejected_before_network(self) -> None:
        row = {"id": "course", "url": "https://example.com/course"}
        duplicate = {"sources": [row, row]}
        unique = {"sources": [row]}
        args = Namespace(catalog=Path("catalog.json"), snapshot=Path(__file__), only=[])
        for catalog, baseline in ((duplicate, unique), (unique, duplicate)):
            with self.subTest(catalog=catalog), patch.object(
                source_health, "parse_args", return_value=args
            ), patch.object(source_health, "load_json", side_effect=[catalog, baseline]), patch.object(
                source_health, "ThreadPoolExecutor"
            ) as executor:
                with self.assertRaisesRegex(ValueError, "Duplicate source id: course"):
                    source_health.main()
                executor.assert_not_called()

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

    def test_ignores_environment_dependent_youtube_metadata(self) -> None:
        sources = [
            {
                "id": "video",
                "url": "https://www.youtube.com/watch?v=example",
                "last_checked": "2026-08-31",
            }
        ]
        results = [
            {
                "id": "video",
                "url": "https://www.youtube.com/watch?v=example",
                "status": "ok",
                "final_url": "https://www.youtube.com/watch?v=example",
                "page_title": "Regional consent response",
                "canonical_url": "https://consent.youtube.com/",
                "duration_signals": [],
            }
        ]
        previous = {
            "sources": [
                {
                    "id": "video",
                    "status": "ok",
                    "final_url": "https://www.youtube.com/watch?v=example",
                    "page_title": "Actual video title",
                    "canonical_url": "https://www.youtube.com/watch?v=example",
                    "duration_signals": ["1 hour"],
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
        self.assertEqual(0, report["summary"]["changed"])
        self.assertFalse(report["summary"]["needs_review"])


if __name__ == "__main__":
    unittest.main()
