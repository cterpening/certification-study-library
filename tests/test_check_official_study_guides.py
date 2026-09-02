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

    def test_extracts_cisco_exam_baseline_and_status(self) -> None:
        body = """
        <html><body><main>
          <h1>200-301 CCNA</h1><h2>Cisco Certified Network Associate</h2>
          <h2>Overview</h2>
          <p>Implementing and Administering Cisco Solutions (200-301 CCNA)
          v1.1 is a 120-minute exam.</p>
          <p>Network fundamentals</p><p>Network access</p>
          <p>IP connectivity</p><p>IP services</p>
          <p>Security fundamentals</p><p>Automation and programmability</p>
          <h3>Languages</h3><p>English, Japanese</p>
          <h3>Duration</h3><p>120 minutes</p>
          <h3>Price</h3><p>$US300</p>
          <h2>Prepare for your exam</h2><p>Cisco U. learning path</p>
          <h2>Get the most from your learning journey</h2>
          <p>Do not include this text.</p>
        </main></body></html>
        """

        objectives = monitor.extract_cisco_objectives(body)
        status = monitor.extract_cisco_status(body)

        self.assertIn("200-301 CCNA", objectives)
        self.assertIn("Automation and programmability", objectives)
        self.assertNotIn("Do not include this text", objectives)
        self.assertIn("Duration: 120 minutes", status["skills_versions"])
        self.assertTrue(
            any("v1.1" in item for item in status["skills_versions"])
        )

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

    def test_extracts_alternate_databricks_coverage_heading(self) -> None:
        body = """
        <h1>Databricks Certified Data Analyst Associate</h1>
        <p>This exam covers:</p>
        <p>Understanding of Databricks Data + AI Platform - 11%</p>
        <p>Managing Data - 8%</p><p>Importing Data - 5%</p>
        <p>Executing queries using Databricks SQL - 20%</p>
        <h2>Assessment Details</h2>
        <p>Type: Proctored certification</p><p>Total number of scored questions: 45</p>
        <p>Time limit: 90 minutes</p><p>Question types: Multiple choice</p>
        <h2>Getting Ready for the Exam</h2>
        """

        objectives = monitor.extract_databricks_objectives(body)

        self.assertIn("Data Analyst Associate", objectives)
        self.assertIn("Databricks SQL - 20%", objectives)

    def test_extracts_aws_weighted_domains(self) -> None:
        body = """
        <h1>AWS Certified Example - Associate (EXA-C01)</h1>
        <p>The exam also validates a candidate's ability to complete the following tasks:</p>
        <p>Build reliable systems.</p><p>Secure workloads.</p>
        <h2>Target candidate description</h2>
        <h2>Content outline</h2>
        <p>Content Domain 1: Design (30% of scored content)</p>
        <p>Content Domain 2: Build (30% of scored content)</p>
        <p>Content Domain 3: Operate (20% of scored content)</p>
        <p>Content Domain 4: Secure (20% of scored content)</p>
        """

        objectives = monitor.extract_aws_objectives(body)
        status = monitor.extract_aws_status(body)

        self.assertIn("Build reliable systems.", objectives)
        self.assertIn("Content Domain 4: Secure (20% of scored content)", objectives)
        self.assertEqual(
            ["AWS Certified Example - Associate (EXA-C01)"],
            status["skills_versions"],
        )

    def test_extracts_comptia_details_and_weighted_summary(self) -> None:
        body = """
        <h1>Example+ Certification</h1><h2>Exam details</h2>
        <p>Exam version: V1</p><p>Exam series code: EX0-001</p>
        <p>Launch date: September 1, 2026</p>
        <p>Retirement: Usually three years after launch</p>
        <h2>Example+ (V1) exam objectives summary</h2>
        <p>Concepts (20%)</p><p>Implementation (25%)</p>
        <p>Operations (25%)</p><p>Troubleshooting (30%)</p>
        """

        objectives = monitor.extract_comptia_objectives(body)
        status = monitor.extract_comptia_status(body)

        self.assertIn("Exam series code: EX0-001", objectives)
        self.assertIn("Troubleshooting (30%)", objectives)
        self.assertEqual(
            ["Retirement: Usually three years after launch"],
            status["upcoming_announcements"],
        )

    def test_extracts_red_hat_performance_objectives(self) -> None:
        rows = "".join(f"<p>Task {number}</p>" for number in range(1, 13))
        body = f"""
        <h1>Red Hat Certified Example | EX999</h1>
        <p>This exam is based on Red Hat Example 1.0.</p>
        <h2>Study points for the exam</h2>{rows}
        <h2>What you need to know</h2>
        """

        objectives = monitor.extract_red_hat_objectives(body)
        status = monitor.extract_red_hat_status(body)

        self.assertIn("Task 12", objectives)
        self.assertIn(
            "This exam is based on Red Hat Example 1.0.",
            status["skills_versions"],
        )

    def test_extracts_linux_foundation_domains(self) -> None:
        tasks = "".join(f"<p>Task {number}</p>" for number in range(1, 8))
        body = f"""
        <h1>Example Certification</h1>
        <h2>Domains &amp; Competencies</h2>
        <p>Domain One20%</p><p>Domain Two20%</p><p>Domain Three20%</p>
        <p>Domain Four20%</p><p>Domain Five20%</p>{tasks}
        <h2>Exam Details &amp; Resources</h2>
        <p>This exam is an online, proctored, performance-based test.</p>
        <p>Duration of Exam 2 hours</p>
        """

        objectives = monitor.extract_linux_foundation_objectives(body)
        status = monitor.extract_linux_foundation_status(body)

        self.assertIn("Domain Five20%", objectives)
        self.assertIn("Duration of Exam 2 hours", status["skills_versions"])

    def test_extracts_google_cloud_capabilities_and_beta_status(self) -> None:
        body = """
        <h1>Professional Example Architect</h1>
        <p>The Professional Example Architect certification assesses your ability to:</p>
        <ul><li>Design solutions</li><li>Build services</li><li>Secure workloads</li>
        <li>Operate systems</li><li>Improve outcomes</li></ul>
        <p>Beta coming in September</p>
        <h2>About this beta certification</h2>
        <p>Length: 3 hours</p><p>Registration fee: $120</p>
        <p>Language: English</p><p>Exam format: 80 questions</p>
        <p>Validity period: 1 year</p><p>Prerequisites: None</p>
        """

        objectives = monitor.extract_google_cloud_objectives(body)
        status = monitor.extract_google_cloud_status(body)

        self.assertIn("Design solutions", objectives)
        self.assertIn("Improve outcomes", objectives)
        self.assertIn("Length: 3 hours", status["skills_versions"])
        self.assertEqual(["Beta coming in September"], status["upcoming_announcements"])


if __name__ == "__main__":
    unittest.main()
