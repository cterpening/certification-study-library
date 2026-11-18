from pathlib import Path
import sys
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_genfm_source as exporter
import test_study_pack as pack_tests


class GenFMExportTests(unittest.TestCase):
    def setUp(self):
        # Compose the existing fixture, without inheriting its test methods or
        # importing its TestCase into this module's discovery namespace.
        self.fixture = pack_tests.StudyPackTests(methodName="runTest")
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.package = self.fixture.build("pack")
        self.output = self.root / "genfm"

    def build(self):
        return exporter.build(self.package, self.output, self.root)

    def test_source_preserves_baseline_citations_content_and_uncertainty(self):
        manifest = self.build()
        self.assertEqual(manifest, exporter.check(self.output, self.root))
        source = (self.output / "source.txt").read_text(encoding="utf-8")
        unit = self.fixture.content["units"][0]
        for value in (
            self.fixture.exam["title"], self.fixture.exam["study_guide_url"],
            "Skills measured as of October 1, 2026", self.fixture.exam["guide_path"],
            self.fixture.content["scope_note"], "HUMAN REVIEW PENDING", "VERIFY CURRENT",
            "Access concepts [official-access]: https://example.org/access",
            "Recorded access status: blocked", unit["title"], unit["summary"],
            *unit["key_points"], *unit["objectives"], *unit["guide_sections"],
            unit["scenario"]["question"], unit["scenario"]["answer"],
            unit["visual"]["title"], exporter.visual_description(unit["visual"]),
            *[node["label"] for node in unit["visual"]["nodes"]],
        ):
            with self.subTest(value=value):
                self.assertIn(value, source)
        for turn in unit["dialogue"]:
            self.assertNotIn(turn["text"], source)
        instructions = (self.output / "instructions.txt").read_text(encoding="utf-8")
        self.assertLessEqual(len(instructions), 3000)
        self.assertIn("two hosts", instructions)
        self.assertIn("no hard 15–20 minute limit", instructions)
        self.assertEqual("pack", manifest["package_path"])
        self.assertEqual(
            exporter.text_sha256((self.package / "manifest.json").read_text(encoding="utf-8")),
            manifest["package_manifest_sha256"],
        )

    def test_export_is_deterministic(self):
        self.build()
        second = self.root / "second-genfm"
        exporter.build(self.package, second, self.root)
        self.assertEqual(
            {path.name: path.read_bytes() for path in self.output.iterdir()},
            {path.name: path.read_bytes() for path in second.iterdir()},
        )

    def test_changed_guide_and_registered_sources_invalidate_handoff(self):
        self.build()
        for relative in ("guides/ex-100.md", "data/sources.json"):
            path = self.root / relative
            original = path.read_bytes()
            with self.subTest(relative=relative):
                path.write_bytes(original + b"\n")
                with self.assertRaisesRegex(ValueError, "Study pack is stale"):
                    exporter.check(self.output, self.root)
                path.write_bytes(original)

    def test_export_edits_are_rejected_even_with_resealed_hashes(self):
        self.build()
        manifest_path = self.output / "manifest.json"
        original_manifest = manifest_path.read_text(encoding="utf-8")
        for name in ("source.txt", "instructions.txt"):
            path = self.output / name
            original = path.read_text(encoding="utf-8")
            with self.subTest(name=name):
                path.write_text("Unsupported replacement material.\n", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "artifact was modified"):
                    exporter.check(self.output, self.root)
                manifest = exporter.read_json(manifest_path)
                manifest["artifacts"][name] = exporter.text_sha256(path.read_text(encoding="utf-8"))
                manifest_path.write_text(exporter.json_text(manifest), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "manifest was modified"):
                    exporter.check(self.output, self.root)
                path.write_text(original, encoding="utf-8")
                manifest_path.write_text(original_manifest, encoding="utf-8")

    def test_package_manifest_text_is_bound_to_export(self):
        self.build()
        path = self.package / "manifest.json"
        path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "GenFM export is stale"):
            exporter.check(self.output, self.root)

    def test_paths_cannot_escape_repository_and_existing_output_is_preserved(self):
        self.build()
        before = (self.output / "source.txt").read_bytes()
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.build()
        self.assertEqual(before, (self.output / "source.txt").read_bytes())
        with self.assertRaisesRegex(ValueError, "inside the repository"):
            exporter.build(self.package, self.root.parent / "outside-genfm", self.root)
        with self.assertRaisesRegex(ValueError, "outside the source package"):
            exporter.build(self.package, self.package / "genfm", self.root)
        exporter.load_package(self.package, self.root)
        manifest = exporter.read_json(self.output / "manifest.json")
        for unsafe in ("../outside-pack", "/outside-pack", "C:/outside-pack", "pack/../pack"):
            with self.subTest(unsafe=unsafe):
                manifest["package_path"] = unsafe
                (self.output / "manifest.json").write_text(exporter.json_text(manifest), encoding="utf-8")
                with self.assertRaises(ValueError):
                    exporter.check(self.output, self.root)

    def test_extra_and_missing_export_files_are_rejected(self):
        self.build()
        extra = self.output / "extra.txt"
        extra.write_text("Unexpected", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "inventory"):
            exporter.check(self.output, self.root)
        extra.unlink()
        (self.output / "instructions.txt").unlink()
        with self.assertRaisesRegex(ValueError, "inventory"):
            exporter.check(self.output, self.root)


if __name__ == "__main__":
    unittest.main()
