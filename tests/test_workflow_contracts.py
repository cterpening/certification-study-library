from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
REMOTE_ACTION = re.compile(r"^\s*uses:\s*[^./\s][^@\s]*@([^\s#]+)", re.MULTILINE)


class WorkflowContractTests(unittest.TestCase):
    def test_validation_and_deployment_share_one_gate(self) -> None:
        for name in ("validate-repository.yml", "deploy-pages.yml"):
            text = (WORKFLOWS / name).read_text(encoding="utf-8")
            self.assertIn("uses: ./.github/actions/validate", text)
            self.assertNotIn("python3 -m unittest discover", text)
            self.assertNotIn("python3 scripts/validate_repository.py", text)
            self.assertNotIn("python3 scripts/validate_site.py", text)

    def test_remote_actions_are_pinned_to_commit_sha(self) -> None:
        paths = [*WORKFLOWS.glob("*.yml"), ROOT / ".github/actions/validate/action.yml"]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for reference in REMOTE_ACTION.findall(text):
                with self.subTest(path=path.name, reference=reference):
                    self.assertRegex(reference, r"^[0-9a-f]{40}$")

    def test_dependabot_covers_python_and_actions(self) -> None:
        text = (ROOT / ".github/dependabot.yml").read_text(encoding="utf-8")
        self.assertIn("package-ecosystem: pip", text)
        self.assertIn("package-ecosystem: github-actions", text)
