from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_visual_assets  # noqa: E402


SVG = (
    b'<svg xmlns="http://www.w3.org/2000/svg" '
    b'xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="-1 -2 18 18">\r\n'
    b'<defs><linearGradient id="paint"><stop offset="0" stop-color="#fff"/>'
    b'</linearGradient><path id="shape" d="M0 0h16v16z"/></defs>'
    b'<use xlink:href="#shape" fill="url(#paint)"/></svg>\r\n'
)


class VisualBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.bundle = self.base / "bundle"
        (self.bundle / "assets").mkdir(parents=True)
        (self.bundle / "notices").mkdir()
        provenance = {
            "publisher": "Example Publisher",
            "source_page": "https://example.test/icons",
            "source_label": "Example icons",
            "review_date": "2026-11-10",
        }
        self.asset_path = self.bundle / "assets" / "example-icon.svg"
        self.asset_path.write_bytes(SVG)
        notice = b"Example attribution.\r\n"
        (self.bundle / "notices" / "NOTICE.txt").write_bytes(notice)
        self.manifest = {
            "schema_version": 1,
            "collection_id": "example-icons",
            **provenance,
            "selection_sha256": "a" * 64,
            "catalog_sha256": "b" * 64,
            "profiles": ["EXAM-1"],
            "assets": [{
                "id": "example-icon",
                "label": "Example icon",
                "path": "assets/example-icon.svg",
                "sha256": hashlib.sha256(SVG).hexdigest(),
                "profiles": ["EXAM-1", "EXAM-2"],
                "source_path": "Icons/Example/icon.svg",
                **provenance,
            }],
            "notices": [{"path": "notices/NOTICE.txt", "sha256": hashlib.sha256(notice).hexdigest()}],
        }
        self.write_manifest()

    def write_manifest(self) -> None:
        (self.bundle / "manifest.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def assert_rejected(self, fragment: str = "") -> None:
        errors = check_visual_assets.check_bundle(self.bundle)
        self.assertTrue(errors, "Invalid bundle was accepted")
        self.assertIn(fragment.lower(), " ".join(errors).lower())

    def test_valid_bundle_preserves_raw_artwork_and_allows_extra_asset_profiles(self) -> None:
        original = {path: path.read_bytes() for path in self.bundle.rglob("*") if path.is_file()}
        self.assertEqual(check_visual_assets.check_bundle(self.bundle), [])
        self.assertEqual({path: path.read_bytes() for path in original}, original)

    def test_checks_asset_and_notice_raw_byte_hashes(self) -> None:
        for relative in ("assets/example-icon.svg", "notices/NOTICE.txt"):
            with self.subTest(relative=relative):
                path = self.bundle / relative
                original = path.read_bytes()
                path.write_bytes(original.replace(b"\r\n", b"\n"))
                self.assert_rejected("SHA-256 mismatch")
                path.write_bytes(original)

    def test_requires_exact_file_inventory(self) -> None:
        extra = self.bundle / "unlisted.txt"
        extra.write_text("unexpected", encoding="utf-8")
        self.assert_rejected("unlisted.txt")
        extra.unlink()
        self.asset_path.unlink()
        self.assert_rejected("missing")

    def test_rejects_unsafe_paths_before_opening_them(self) -> None:
        for value in (
            "../outside.svg", "/outside.svg", "assets/../outside.svg",
            "C:/outside.svg", "assets\\outside.svg", "assets//icon.svg",
            "assets/icon.svg:stream", "notices/NUL.txt", "notices/notice.txt.",
        ):
            with self.subTest(value=value):
                self.manifest["assets"][0]["path"] = value
                self.write_manifest()
                self.assert_rejected("Unsafe relative path")

    def test_checks_metadata_types_dates_and_digest_shape(self) -> None:
        original = deepcopy(self.manifest)
        for key, value in (
            ("schema_version", True), ("schema_version", 2), ("publisher", " "),
            ("collection_id", []), ("review_date", "2026-02-30"),
            ("review_date", "20261110"), ("selection_sha256", "not-a-hash"),
            ("catalog_sha256", 123), ("assets", []), ("notices", []),
        ):
            with self.subTest(key=key, value=value):
                self.manifest = deepcopy(original)
                self.manifest[key] = value
                self.write_manifest()
                self.assert_rejected()
        self.manifest = deepcopy(original)
        self.manifest["assets"][0]["source_path"] = "../untrusted.svg"
        self.write_manifest()
        self.assert_rejected("Unsafe relative path")

    def test_rejects_duplicate_manifest_keys_paths_and_ids(self) -> None:
        manifest_path = self.bundle / "manifest.json"
        manifest_path.write_text('{"schema_version":1,"schema_version":2}', encoding="utf-8")
        self.assert_rejected("Duplicate manifest key")
        duplicate = deepcopy(self.manifest["assets"][0])
        self.manifest["assets"].append(duplicate)
        self.write_manifest()
        self.assert_rejected("Duplicate bundle path")
        duplicate["path"] = "assets/another-icon.svg"
        self.write_manifest()
        self.assert_rejected("Duplicate asset id")

    def test_rejects_invalid_profile_selection(self) -> None:
        original = deepcopy(self.manifest)
        for requested, available in (
            ([], ["EXAM-1"]), (["EXAM-1", "EXAM-1"], ["EXAM-1"]),
            (["EXAM-1"], []), (["EXAM-1"], ["EXAM-2"]),
            (["EXAM-1", "EXAM-3"], ["EXAM-1", "EXAM-2"]),
            (["EXAM-1"], ["EXAM-1", "EXAM-1"]), (["EXAM-1"], [7]),
        ):
            with self.subTest(requested=requested, available=available):
                self.manifest = deepcopy(original)
                self.manifest["profiles"] = requested
                self.manifest["assets"][0]["profiles"] = available
                self.write_manifest()
                self.assert_rejected("profile")

    def test_requires_asset_provenance_to_match_manifest(self) -> None:
        original = deepcopy(self.manifest)
        for key, value in (
            ("publisher", "Different publisher"),
            ("source_page", "https://example.test/different-source"),
            ("source_label", "Different source label"),
            ("review_date", "2026-11-09"),
        ):
            with self.subTest(key=key):
                self.manifest = deepcopy(original)
                self.manifest["assets"][0][key] = value
                self.write_manifest()
                self.assert_rejected(f"provenance mismatch: {key}")

    def test_rejects_case_insensitive_duplicate_source_paths(self) -> None:
        duplicate = deepcopy(self.manifest["assets"][0])
        duplicate.update(id="second-icon", path="assets/second-icon.svg")
        duplicate["source_path"] = duplicate["source_path"].upper()
        (self.bundle / duplicate["path"]).write_bytes(SVG)
        self.manifest["assets"].append(duplicate)
        self.write_manifest()
        self.assert_rejected("Duplicate asset source path")

    def test_rejects_unknown_svg_attributes_with_resealed_hash(self) -> None:
        self.reseal_svg(
            b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" arbitrary="yes"/>'
        )
        self.assert_rejected("unsupported or active SVG attribute arbitrary")

    def test_checks_svg_notice_content_with_matching_hash(self) -> None:
        active = (
            b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18">'
            b'<script>alert(1)</script></svg>'
        )
        for filename in ("active.svg", "active.SVG"):
            with self.subTest(filename=filename):
                relative = f"notices/{filename}"
                path = self.bundle / relative
                path.write_bytes(active)
                self.manifest["notices"].append({"path": relative, "sha256": hashlib.sha256(active).hexdigest()})
                self.write_manifest()
                self.assert_rejected("unsupported or active SVG element")
                path.unlink()
                self.manifest["notices"].pop()

    def test_rejects_non_utf8_xml_declaration(self) -> None:
        for encoding in ("iso-8859-1", "us-ascii", "utf-16"):
            with self.subTest(encoding=encoding):
                self.reseal_svg(f'<?xml version="1.0" encoding="{encoding}"?>'.encode() + SVG)
                self.assert_rejected("only UTF-8 XML encoding")
        self.reseal_svg(b'<?xml version="1.0" encoding="UTF-8"?>' + SVG)
        self.assertEqual(check_visual_assets.check_bundle(self.bundle), [])

    def test_rejects_oversized_svg_with_matching_hash(self) -> None:
        self.reseal_svg(SVG + b" " * check_visual_assets.MAX_SVG_BYTES)
        self.assert_rejected("8 MiB limit")

    def test_rejects_active_svg_even_when_hash_is_resealed(self) -> None:
        for body in (
            '<script>alert(1)</script>', '<path onload="alert(1)"/>',
            '<foreignObject/>', '<animate attributeName="x"/>', '<set attributeName="fill"/>',
            '<use href="https://example.test/image.svg#id"/>', '<use href="data:image/svg+xml,evil"/>',
            '<path fill="url(https://example.test/paint)"/>',
            '<path fill="u&#114;l(https://example.test/paint)"/>',
            '<path fill="u\\72l(https://example.test/paint)"/>',
            '<path fill="u/**/rl(https://example.test/paint)"/>',
            '<style>@import "https://example.test/style.css";</style>',
            '<path style="fill:url(https://example.test/paint)"/>',
            '<g xml:base="https://example.test/"><use href="#paint"/></g>',
        ):
            with self.subTest(body=body):
                self.reseal_svg(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18">{body}</svg>'.encode())
                self.assert_rejected()

    def reseal_svg(self, raw: bytes) -> None:
        self.asset_path.write_bytes(raw)
        self.manifest["assets"][0]["sha256"] = hashlib.sha256(raw).hexdigest()
        self.write_manifest()

    def test_rejects_xml_declarations_that_can_load_external_content(self) -> None:
        for prefix in (
            b'<!DOCTYPE svg [<!ENTITY example "expanded">]>',
            b'<!DOCTYPE svg SYSTEM "https://example.test/svg.dtd">',
            b'<?xml-stylesheet href="https://example.test/style.css"?>',
        ):
            with self.subTest(prefix=prefix):
                self.reseal_svg(prefix + SVG)
                self.assert_rejected()

    def test_requires_positive_finite_viewbox_dimensions(self) -> None:
        for box in ("0 0 0 18", "0 0 -1 18", "0 0 nan 18", "0 0 18 inf", "0 0 18", ""):
            with self.subTest(box=box):
                self.reseal_svg(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{box}"/>'.encode())
                self.assert_rejected("viewBox")

    def test_rejects_file_symlink(self) -> None:
        outside = self.base / "outside.svg"
        outside.write_bytes(SVG)
        self.asset_path.unlink()
        try:
            self.asset_path.symlink_to(outside)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"File symlink creation unavailable: {exc}")
        self.assert_rejected("Symlink/junction/reparse")

    def test_rejects_hard_linked_assets_notices_and_manifest(self) -> None:
        alias = self.base / "outside-alias"
        for path in (self.asset_path, self.bundle / "notices" / "NOTICE.txt", self.bundle / "manifest.json"):
            with self.subTest(path=path.name):
                try:
                    alias.hardlink_to(path)
                except (OSError, NotImplementedError) as exc:
                    self.skipTest(f"Hard-link creation unavailable: {exc}")
                try:
                    self.assert_rejected("Hard-linked file")
                finally:
                    alias.unlink()

    def test_rejects_directory_symlink(self) -> None:
        link = self.bundle / "linked-directory"
        outside = self.base / "outside"
        outside.mkdir()
        try:
            link.symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Directory symlink creation unavailable: {exc}")
        self.assert_rejected("Symlink/junction/reparse")

    @unittest.skipUnless(os.name == "nt", "Windows junction check")
    def test_rejects_windows_directory_junction(self) -> None:
        outside = self.base / "outside"
        outside.mkdir()
        junction = self.bundle / "junction"
        # Arguments are environment values, never inserted into shell source.
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command",
             "New-Item -ItemType Junction -Path $env:VISUAL_TEST_LINK -Target $env:VISUAL_TEST_TARGET | Out-Null"],
            env={**os.environ, "VISUAL_TEST_LINK": str(junction), "VISUAL_TEST_TARGET": str(outside)},
            capture_output=True, text=True, check=False,
        )
        if result.returncode:
            self.skipTest(f"Junction creation unavailable: {result.stderr.strip()}")
        self.addCleanup(junction.rmdir)
        self.assert_rejected("Symlink/junction/reparse")

    def test_cli_works_outside_repository_and_returns_failure_status(self) -> None:
        command = [sys.executable, str(ROOT / "scripts" / "check_visual_assets.py"), "--bundle", str(self.bundle)]
        result = subprocess.run(command, cwd=self.base, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("verified offline", result.stdout)
        self.asset_path.write_bytes(b"tampered")
        result = subprocess.run(command, cwd=self.base, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("SHA-256 mismatch", result.stderr)


if __name__ == "__main__":
    unittest.main()
