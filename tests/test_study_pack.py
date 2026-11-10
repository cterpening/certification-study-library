import copy
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
import xml.etree.ElementTree as ET


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_study_pack as builder
import study_material as material


class StudyPackTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.exam = {
            "code": "EX-100", "title": "Example fundamentals", "guide_path": "guides/ex-100.md",
            "study_guide_url": "https://example.org/blueprint", "blueprint_last_checked": "2026-10-28",
        }
        self.write_json("config/exams.json", {"exams": [self.exam]})
        self.write_json("data/sources.json", {"sources": [{"id": "official-access", "title": "Access concepts", "url": "https://example.org/access", "supported_exams": ["EX-100"]}]})
        self.write_json("data/source-health.json", {"sources": [{"id": "official-access", "status": "blocked"}]})
        self.write("guides/ex-100.md", "# Guide\n\n## Access controls\n\nExplain roles and configuration.\n\n## Places to learn\n")
        self.write("data/objective-snapshots/ex-100-official-objectives.txt", "Skills measured as of October 1, 2026\nDescribe access controls\nDescribe configuration policy and\nits scope\n")
        self.write_json("data/objective-snapshots/ex-100-official-status.json", {"skills_versions": ["October 1, 2026"]})
        self.write_json("config/certification-seeds.json", {"certifications": [{"exam_code": "NEW-200", "title": "New exam", "official_url": "https://example.org/new"}]})
        self.write("templates/guide.md", "# New draft\n\nAI-GENERATED DRAFT\n")
        self.content = {
            "schema_version": 1, "exam_code": "EX-100", "language": "en",
            "scope_note": "Selected access concepts; this does not cover the complete exam.",
            "units": [{
                "id": "access-controls", "title": "Choose the control",
                "guide_sections": ["Access controls"],
                "objectives": ["Describe access controls", "Describe configuration policy and its scope"],
                "source_ids": ["official-access"],
                "summary": "Permission and configuration answer different questions.",
                "key_points": ["A role permits an operation.", "A policy evaluates a configuration."],
                "scenario": {"question": "A permitted operator submits a disallowed configuration. What should you inspect?", "answer": "Inspect the applicable policy as well as the role assignment."},
                "visual": {"title": "Control relationships", "nodes": [{"id": "operation", "label": "Resource operation"}, {"id": "role", "label": "Role assignment"}, {"id": "policy", "label": "Configuration policy"}], "edges": [{"from": "role", "to": "operation", "label": "permits"}, {"from": "policy", "to": "operation", "label": "evaluates configuration"}]},
                "dialogue": [{"speaker": "host", "text": "What does a role assignment tell us?"}, {"speaker": "learner", "text": "It describes permissions, not whether a configuration meets policy."}],
            }],
        }
        self.content_path = self.write_json("data/study-content/example.json", self.content)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        return path

    def write_json(self, relative, value):
        return self.write(relative, material.json_text(value))

    def build(self, output="output"):
        builder.build(self.content_path, self.root / output, self.root)
        return self.root / output

    def test_build_is_deterministic_and_preserves_inputs(self):
        before = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        first = self.build("first")
        second = self.build("second")
        self.assertEqual(material.load_package(first, self.root), material.load_package(second, self.root))
        self.assertEqual({p.relative_to(first): p.read_bytes() for p in first.rglob("*") if p.is_file()}, {p.relative_to(second): p.read_bytes() for p in second.rglob("*") if p.is_file()})
        for name, value in before.items():
            self.assertEqual((self.root / name).read_bytes(), value)
        guide = (first / "study-guide.md").read_text(encoding="utf-8")
        self.assertIn("HUMAN REVIEW PENDING", guide)
        self.assertIn("https://example.org/blueprint", guide)
        self.assertIn("https://example.org/access", guide)
        self.assertIn("Diagram in words", guide)

    def test_every_source_change_invalidates_pack(self):
        package = self.build()
        manifest = material.load_package(package, self.root)
        for relative in manifest["input_fingerprints"]:
            with self.subTest(relative=relative):
                path = self.root / relative
                original = path.read_bytes()
                path.write_bytes(original + b"\n")
                with self.assertRaises(ValueError):
                    material.load_package(package, self.root)
                path.write_bytes(original)

    def test_platform_newlines_do_not_invalidate_pack(self):
        package = self.build()
        path = self.root / "guides/ex-100.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        material.load_package(package, self.root)

    def test_changed_artifact_cannot_be_resealed_by_editing_manifest(self):
        package = self.build()
        guide = package / "study-guide.md"
        guide.write_text("Unsupported new content", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "modified"):
            material.load_package(package, self.root)
        manifest = material.read_json(package / "manifest.json")
        manifest["artifacts"]["study-guide.md"] = material.text_sha256(guide.read_text(encoding="utf-8"))
        (package / "manifest.json").write_text(material.json_text(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "manifest"):
            material.load_package(package, self.root)

    def test_manifest_cannot_drop_required_source_binding(self):
        package = self.build()
        manifest = material.read_json(package / "manifest.json")
        del manifest["input_fingerprints"]["guides/ex-100.md"]
        (package / "manifest.json").write_text(material.json_text(manifest), encoding="utf-8")
        with self.assertRaises(ValueError):
            material.load_package(package, self.root)

    def test_added_and_missing_artifacts_are_rejected(self):
        package = self.build()
        extra = package / "untracked.html"
        extra.write_text("extra", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "inventory"):
            material.load_package(package, self.root)
        extra.unlink()
        (package / "flashcards.json").unlink()
        with self.assertRaisesRegex(ValueError, "inventory"):
            material.load_package(package, self.root)

    def test_unknown_or_partial_references_are_rejected(self):
        for field, value in (("objectives", ["access controls"]), ("source_ids", ["unregistered"]), ("guide_sections", ["Missing heading"])):
            with self.subTest(field=field):
                content = copy.deepcopy(self.content)
                content["units"][0][field] = value
                self.write_json("data/study-content/example.json", content)
                with self.assertRaises(ValueError):
                    self.build(field)

    def test_structural_failures_cannot_create_partial_output(self):
        for change in (lambda unit: unit.update(id="../escape"), lambda unit: unit.update(dialogue=[{"speaker": "host", "text": "Only one voice"}]), lambda unit: unit["visual"]["edges"][0].update(to="missing"), lambda unit: unit.update(summary="Read https://invented.example/resource")):
            content = copy.deepcopy(self.content)
            change(content["units"][0])
            self.write_json("data/study-content/example.json", content)
            with self.assertRaises(ValueError):
                self.build()

    def test_blueprint_metadata_cannot_be_mapped_as_an_objective(self):
        self.content["units"][0]["objectives"] = ["Skills measured as of October 1, 2026"]
        self.write_json("data/study-content/example.json", self.content)
        with self.assertRaisesRegex(ValueError, "Unknown objective"):
            self.build()

    def test_podcast_navigation_ids_cannot_collide_with_authored_units(self):
        for reserved in ("introduction", "recap"):
            with self.subTest(reserved=reserved):
                self.content["units"][0]["id"] = reserved
                self.write_json("data/study-content/example.json", self.content)
                with self.assertRaisesRegex(ValueError, "reserved"):
                    self.build()
            self.assertFalse((self.root / "output").exists())

    def test_output_must_be_new(self):
        package = self.build()
        before = (package / "manifest.json").read_bytes()
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.build()
        self.assertEqual((package / "manifest.json").read_bytes(), before)

    def test_external_content_is_rejected(self):
        with TemporaryDirectory() as external:
            path = Path(external) / "content.json"
            path.write_text(material.json_text(self.content), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "inside the repository"):
                builder.build(path, self.root / "output", self.root)

    def test_unsafe_manifest_paths_are_rejected(self):
        package = self.build()
        manifest = material.read_json(package / "manifest.json")
        for path in ("../outside.json", "C:/outside.json", "data\\outside.json", "/outside.json"):
            with self.subTest(path=path):
                manifest["content_path"] = path
                (package / "manifest.json").write_text(material.json_text(manifest), encoding="utf-8")
                with self.assertRaises(ValueError):
                    material.load_package(package, self.root)

    def test_linked_artifact_is_rejected(self):
        package = self.build()
        linked = package / "linked.json"
        try:
            linked.symlink_to(self.content_path)
        except OSError:
            self.skipTest("Host cannot create symlinks")
        with self.assertRaisesRegex(ValueError, "Linked paths"):
            material.load_package(package, self.root)

    def test_linked_output_parent_is_rejected(self):
        target = self.root / "target"
        target.mkdir()
        link = self.root / "link"
        try:
            link.symlink_to(target, target_is_directory=True)
        except OSError:
            self.skipTest("Host cannot create symlinks")
        with self.assertRaisesRegex(ValueError, "Linked paths"):
            self.build("link/output")
        self.assertFalse((target / "output").exists())

    def test_svg_is_accessible_xml_and_escapes_authored_labels(self):
        visual = copy.deepcopy(self.content["units"][0]["visual"])
        visual["nodes"][0]["label"] = "<script> & control"
        svg = material.render_svg(visual)
        element = ET.fromstring(svg)
        self.assertEqual(element.attrib["role"], "img")
        ns = {"svg": "http://www.w3.org/2000/svg"}
        self.assertIsNotNone(element.find("svg:title", ns))
        self.assertIn("<script> & control", element.find("svg:desc", ns).text)
        self.assertIsNone(element.find(".//svg:script", ns))

    def test_prepare_reads_complete_content_and_preserves_blocked_health(self):
        packet = builder.prepare("ex-100", self.root / "packet", self.root)
        self.assertEqual(packet["guide_text"], (self.root / "guides/ex-100.md").read_text(encoding="utf-8"))
        self.assertEqual(packet["source_health"][0]["status"], "blocked")
        self.assertEqual(packet["state"], "pending-authoring-and-review")
        self.assertTrue((self.root / "packet/content.template.json").exists())
        self.assertNotIn("reviewed_on", packet)

    def test_prepare_new_seed_requires_objective_intake(self):
        packet = builder.prepare("NEW-200", self.root / "packet", self.root)
        self.assertEqual(packet["state"], "objective-intake-required")
        self.assertIsNone(packet["objective_text"])
        self.assertIn("AI-GENERATED DRAFT", packet["guide_template"])
        content = copy.deepcopy(self.content)
        content["exam_code"] = "NEW-200"
        self.write_json("data/study-content/new.json", content)
        with self.assertRaisesRegex(ValueError, "published guide"):
            builder.build(self.root / "data/study-content/new.json", self.root / "output", self.root)

    def test_prepare_unknown_exam_is_an_error(self):
        with self.assertRaises(ValueError):
            builder.prepare("UNKNOWN-123", self.root / "packet", self.root)

    def test_duplicate_json_keys_are_rejected(self):
        path = self.write("duplicate.json", '{"exam_code":"one","exam_code":"two"}')
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            material.read_json(path)


if __name__ == "__main__":
    unittest.main()
