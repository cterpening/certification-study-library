import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_guide_diagram import build_diagram
from study_material import render_svg


class GuideDiagramTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.write_json("config/exams.json", {"exams": [
            {"code": "PY-101", "vendor_id": "example-python", "guide_path": "guides/py-101.md"}
        ]})
        self.write_json("data/sources.json", {"sources": [
            {"id": "python-iteration", "title": "Iteration", "url": "https://example.org/iterations",
             "supported_exams": ["PY-101"]},
            {"id": "other-exam-source", "supported_exams": ["PY-202"]},
        ]})
        self.write_json("data/source-health.json", {"sources": []})
        self.write("data/objective-snapshots/py-101-official-objectives.txt",
                   "Explain the roles of iterables\nand iterators\n")
        self.guide = self.write("guides/py-101.md", "# Python\n\n## Iteration ##\n\n~~~~python\n"
                                "~~~\n## Fenced example\n~~~~\n")
        self.relative = "guides/diagrams/py-101/iteration.json"
        self.spec = {
            "exam_code": "PY-101", "guide_section": "Iteration",
            "objective": "Explain the roles of iterables and iterators",
            "source_ids": ["python-iteration"],
            "visual": {
                "title": "Getting an iterator [example]",
                "nodes": [{"id": "values", "label": "List <values>"}, {"id": "it", "label": "Iterator"}],
                "edges": [{"from": "values", "label": "supplies", "to": "it"}],
            },
        }
        self.path = self.write_json(self.relative, self.spec)
        self.output = self.path.with_suffix(".svg")

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
        return path

    def write_json(self, name, value):
        return self.write(name, json.dumps(value))

    def test_repeatable_build_and_guide_embed(self):
        inputs = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        markdown = build_diagram(Path(self.relative), root=self.root)
        first = self.output.read_bytes()
        self.assertTrue(markdown.startswith(r"![Getting an iterator \[example\]](diagrams/py-101/iteration.svg)"))
        self.assertIn("[Open full-size diagram](diagrams/py-101/iteration.svg)", markdown)
        self.assertIn(r"List \<values\> — supplies → Iterator", markdown)
        self.assertIn("https://example.org/iterations", markdown)
        self.assertIn("List <values>", ET.fromstring(first).find("{*}desc").text)
        self.output.unlink()
        build_diagram(self.path, root=self.root)
        self.assertEqual(self.output.read_bytes(), first)
        self.assertEqual({p: p.read_bytes() for p in inputs}, inputs)

    def test_checked_in_starter_shows_its_shared_origin_once(self):
        starter = Path(__file__).resolve().parents[1] / "guides/diagrams/az-900/role-scope.json"
        markdown = build_diagram(starter, check=True)
        self.assertIn("diagrams/az-900/role-scope.svg", markdown)
        root = ET.parse(starter.with_suffix(".svg")).getroot()
        visible_labels = [element.text for element in root.findall(".//{*}text")]
        self.assertEqual(visible_labels.count("One role assignment"), 1)

    def test_repository_diagram_previews_are_reproducible(self):
        directory = Path(__file__).resolve().parents[1] / "guides/diagrams"
        for definition in sorted(directory.glob("*/*.json")):
            with self.subTest(definition=definition):
                build_diagram(definition, check=True)

    def test_independent_prerequisites_converge_on_one_target(self):
        visual = {
            "title": "Job dependencies",
            "nodes": [{"id": name, "label": name} for name in ("build", "test", "publish")],
            "edges": [
                {"from": "build", "to": "publish", "label": "must pass before"},
                {"from": "test", "to": "publish", "label": "must pass before"},
            ],
        }
        for grouped, expected_targets in ((True, 1), (False, 2)):
            with self.subTest(grouped=grouped):
                svg = ET.fromstring(render_svg(visual, group_origins=grouped))
                labels = [element.text for element in svg.findall(".//{*}text")]
                self.assertEqual(labels.count("publish"), expected_targets)
                self.assertEqual(labels.count("build"), 1)
                self.assertEqual(labels.count("test"), 1)
                self.assertEqual(labels.count("must pass before"), 2)
                self.assertEqual(len(svg.findall(".//{*}path[@marker-end]")), expected_targets)
                self.assertEqual(svg.find("{*}desc").text,
                                 "build — must pass before → publish; test — must pass before → publish")

    def test_check_is_read_only_on_current_missing_and_stale_outputs(self):
        with self.assertRaisesRegex(ValueError, "Missing or stale"):
            build_diagram(self.path, root=self.root, check=True)
        self.assertFalse(self.output.exists())
        build_diagram(self.path, root=self.root)
        # Git can check text files out with CRLF on Windows.
        self.output.write_bytes(self.output.read_bytes().replace(b"\n", b"\r\n"))
        stat_before = self.output.stat()
        build_diagram(self.path, root=self.root, check=True)
        self.assertEqual(self.output.stat().st_mtime_ns, stat_before.st_mtime_ns)
        self.spec["visual"]["edges"][0]["label"] = "returns"
        self.write_json(self.relative, self.spec)
        previous = self.output.read_bytes()
        with self.assertRaisesRegex(ValueError, "Missing or stale"):
            build_diagram(self.path, root=self.root, check=True)
        self.assertEqual(self.output.read_bytes(), previous)
        build_diagram(self.path, root=self.root)
        self.assertNotEqual(self.output.read_bytes(), previous)

    def test_bad_source_bindings_cannot_overwrite_the_diagram(self):
        build_diagram(self.path, root=self.root)
        first = self.output.read_bytes()
        for overrides in (
            {"guide_section": "Fenced example"}, {"guide_section": "Missing"},
            {"objective": "roles of iterables"}, {"source_ids": ["other-exam-source"]},
            {"source_ids": []}, {"exam_code": "py-101"}, {"extra": True},
        ):
            with self.subTest(overrides=overrides):
                self.write_json(self.relative, {**self.spec, **overrides})
                with self.assertRaises(ValueError):
                    build_diagram(self.path, root=self.root)
                self.assertEqual(self.output.read_bytes(), first)

    def test_unknown_and_unconnected_nodes(self):
        self.spec["visual"]["edges"][0]["to"] = "undeclared"
        self.write_json(self.relative, self.spec)
        with self.assertRaisesRegex(ValueError, "declared nodes"):
            build_diagram(self.path, root=self.root)
        self.spec["visual"]["edges"][0]["to"] = "it"
        self.spec["visual"]["nodes"].append({"id": "orphan", "label": "Unrepresented"})
        self.write_json(self.relative, self.spec)
        with self.assertRaisesRegex(ValueError, "without a relationship: orphan"):
            build_diagram(self.path, root=self.root)
        self.assertFalse(self.output.exists())

    def test_rejects_noncanonical_paths(self):
        for name in ("guides/diagrams/py-202/iteration.json", "guides/diagrams/py-101/Invalid-Name.json",
                     "examples/diagrams/py-101/iteration.json", "guides/diagrams/py-101/extra/iteration.json"):
            with self.subTest(name=name):
                path = self.write_json(name, self.spec)
                with self.assertRaisesRegex(ValueError, "Expected guides/diagrams"):
                    build_diagram(path, root=self.root)
                self.assertFalse(path.with_suffix(".svg").exists())


if __name__ == "__main__":
    unittest.main()
