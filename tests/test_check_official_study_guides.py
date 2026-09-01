import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_official_study_guides.py"
SPEC = importlib.util.spec_from_file_location("objective_monitor", SCRIPT)
monitor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(monitor)


class ObjectiveExtractionTests(unittest.TestCase):
    def test_extracts_skills_section_and_omits_study_resources(self) -> None:
        body = """
        <html><body><main>
          <h2>Skills measured as of August 7, 2026</h2>
          <h3>Skills at a glance</h3>
          <ul>
            <li>Use GitHub Copilot responsibly (15–20%)</li>
            <li>Use GitHub Copilot features (25–30%)</li>
            <li>Understand data and architecture (10–15%)</li>
            <li>Apply prompt engineering (10–15%)</li>
            <li>Improve productivity (10–15%)</li>
            <li>Configure privacy and safeguards (10–15%)</li>
          </ul>
          <h3>Use GitHub Copilot responsibly</h3>
          <p>Describe risks and limitations.</p>
          <p>Validate AI output.</p>
          <h2>Study resources</h2><p>Do not include this text.</p>
        </main></body></html>
        """
        result = monitor.extract_skills_section(body)
        self.assertIn("Skills measured as of August 7, 2026", result)
        self.assertIn("Validate AI output.", result)
        self.assertNotIn("Do not include this text", result)

    def test_ignores_script_and_repeated_lines(self) -> None:
        rows = "".join(f"<li>Objective {number}</li>" for number in range(1, 11))
        body = f"""
        <html><body><script>Skills measured as of fake</script>
        <h2>Skills at a glance</h2><p>Objective 1</p><p>Objective 1</p>
        {rows}<h2>Change log</h2></body></html>
        """
        result = monitor.extract_skills_section(body)
        self.assertNotIn("fake", result)
        self.assertNotIn("Objective 1\nObjective 1", result)

    def test_short_or_missing_section_fails_closed(self) -> None:
        with self.assertRaises(ValueError):
            monitor.extract_skills_section("<html><p>No objectives</p></html>")

    def test_extracts_future_update_announcement_separately(self) -> None:
        body = """
        <html><body><main>
          <p>This exam will be updated on October 15, 2026.</p>
          <h2>Skills measured as of August 2026</h2>
          <ul><li>Objective group</li></ul>
        </main></body></html>
        """
        status = monitor.extract_exam_status(body)
        self.assertEqual(
            ["Skills measured as of August 2026"], status["skills_versions"]
        )
        self.assertEqual(
            ["This exam will be updated on October 15, 2026."],
            status["upcoming_announcements"],
        )

    def test_undated_exam_uses_page_update_only_as_freshness_evidence(self) -> None:
        body = """
        <html><body><main>
          <h2>Skills measured</h2>
          <h3>Audience profile</h3>
          <p>Candidate description.</p>
          <h3>Skills at a glance</h3>
          <p>Plan a solution (30-35%)</p>
          <p>Build a solution (40-45%)</p>
          <p>Test a solution (20-25%)</p>
          <h3>Plan a solution (30-35%)</h3>
          <p>Plan identity.</p><p>Plan security.</p><p>Plan deployment.</p>
          <h2>Study resources</h2>
          <h2>Last updated on</h2><p>2026-04-21</p>
        </main></body></html>
        """

        status = monitor.extract_exam_status(body)

        self.assertEqual(
            [
                "Skills measured (official page last updated 2026-04-21; "
                "no skills effective date published)"
            ],
            status["skills_versions"],
        )
        self.assertEqual([], status["upcoming_announcements"])

    def test_extracts_hashicorp_terraform_associate_objectives(self) -> None:
        rows = "".join(
            f"<tr><td>{number}</td><td>Objective {number}</td></tr>"
            for number in range(1, 31)
        )
        body = f"""
        <html><body><main>
          <h2>Terraform Associate (004)</h2>
          <p>Product version tested: Terraform 1.12</p>
          <p>Practice the exam objectives in a demo environment.</p>
          <h3>Exam objectives</h3>
          <table>{rows}</table>
          <h3>Content differences between the 003 and 004 exams</h3>
          <p>Do not include this text.</p>
          <h2>Terraform Authoring and Operations Professional</h2>
          <p>This exam will be updated on December 1, 2026.</p>
        </main></body></html>
        """
        result = monitor.extract_hashicorp_objectives(body)
        self.assertIn("Terraform Associate (004)", result)
        self.assertIn("Product version tested: Terraform 1.12", result)
        self.assertIn("Objective 30", result)
        self.assertNotIn("Practice the exam objectives", result)
        self.assertNotIn("Do not include this text", result)

        status = monitor.extract_hashicorp_status(body)
        self.assertEqual(
            ["Terraform Associate (004) - Product version tested: Terraform 1.12"],
            status["skills_versions"],
        )
        self.assertEqual([], status["upcoming_announcements"])

    def test_extracts_hashicorp_vault_professional_objectives(self) -> None:
        body = """
        <html><body>
        <h1>Exam content list - Vault Operations Professional</h1>
        <h2>Exam Objective</h2>
        <p>1</p><p>Create a working Vault server configuration</p>
        <p>1a</p><p>Enable and configure secret engines</p>
        <p>1b</p><p>Practice production hardening</p>
        <p>2</p><p>Monitor a Vault environment</p>
        <p>2a</p><p>Monitor and understand Vault telemetry</p>
        <p>3</p><p>Employ the Vault security model</p>
        <p>3a</p><p>Describe secure introduction of Vault clients</p>
        <p>4</p><p>Build fault-tolerant Vault environments</p>
        <p>4a</p><p>Configure a highly available cluster</p>
        <p>5</p><p>Understand hardware security module integration</p>
        <p>6</p><p>Scale Vault for performance</p>
        <p>7</p><p>Configure access control</p>
        <p>8</p><p>Configure Vault Agent</p>
        <p>Sign up for the exam here!</p>
        </body></html>
        """

        objectives = monitor.extract_hashicorp_objectives(body)
        status = monitor.extract_hashicorp_status(body)

        self.assertIn("Create a working Vault server configuration", objectives)
        self.assertNotIn("Sign up for the exam", objectives)
        self.assertEqual(
            ["Exam content list - Vault Operations Professional"],
            status["skills_versions"],
        )

    def test_extracts_databricks_coverage_and_assessment_status(self) -> None:
        body = """
        <html><body><main>
          <h1>Databricks Certified Data Engineer Associate</h1>
          <p>The exam covers:</p>
          <ol>
            <li>Databricks Intelligence Platform - 6%</li>
            <li>Data Ingestion and Loading - 21%</li>
            <li>Data Transformation and Modeling - 22%</li>
            <li>Working with Lakeflow Jobs - 16%</li>
            <li>Implementing CI/CD - 10%</li>
            <li>Troubleshooting, Monitoring, and Optimization - 10%</li>
            <li>Governance and Security - 15%</li>
          </ol>
          <h2>Assessment Details</h2>
          <p>Type: Proctored certification</p>
          <p>Total number of scored questions: 45</p>
          <p>Time limit: 90 minutes</p>
          <p>Question types: Multiple choice</p>
          <p>Languages: English</p>
          <p>Delivery method: Online or test center</p>
          <p>Recommended experience: hands-on data engineering</p>
          <p>Validity period: 2 years</p>
          <h2>Getting Ready for the Exam</h2>
          <p>Do not include this text.</p>
        </main></body></html>
        """

        objectives = monitor.extract_databricks_objectives(body)
        status = monitor.extract_databricks_status(body)

        self.assertIn("Databricks Intelligence Platform - 6%", objectives)
        self.assertIn("Governance and Security - 15%", objectives)
        self.assertNotIn("Do not include this text", objectives)
        self.assertIn("Time limit: 90 minutes", status["skills_versions"])
        self.assertEqual([], status["upcoming_announcements"])

    def test_databricks_extraction_fails_without_weighted_coverage(self) -> None:
        with self.assertRaises(ValueError):
            monitor.extract_databricks_objectives(
                "<h1>Databricks Certified Example</h1>"
                "<p>The exam covers:</p><p>One domain</p>"
                "<h2>Assessment Details</h2>"
            )


if __name__ == "__main__":
    unittest.main()
