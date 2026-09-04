import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_official_study_guides.py"
SPEC = importlib.util.spec_from_file_location("objective_monitor", SCRIPT)
monitor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(monitor)


class ObjectiveExtractionTests(unittest.TestCase):
    def test_extracts_microsoft_office_assessed_skills(self) -> None:
        body = """
        <html><body><main>
          <h1>Exam MO-110: Microsoft Word (Microsoft 365 Apps)</h1>
          <p>You will have 50 minutes to complete this assessment.</p>
          <h2>Assessed on this exam</h2>
          <p>Manage documents (20–25%)</p>
          <p>Format text (20–25%)</p>
          <p>Manage tables (20–25%)</p>
          <p>Create references (5–10%)</p>
          <h2>Need accommodations?</h2><p>Do not include this.</p>
          <p>Retirement date:</p><p>none</p>
        </main></body></html>
        """
        objectives = monitor.extract_microsoft_office_objectives(body)
        status = monitor.extract_microsoft_office_status(body)
        self.assertIn("Manage documents (20–25%)", objectives)
        self.assertNotIn("Do not include this", objectives)
        self.assertIn("Retirement date: none", status["skills_versions"])

    def test_extracts_ibm_machine_readable_objectives(self) -> None:
        import json

        body = json.dumps(
            {
                "EXAM_SERIES_CODE": "C1000-999",
                "EXAM_TITLE": "Example",
                "EXAM_STATUS": "Live",
                "EXAM_NUMBER_OF_QUESTIONS": 40,
                "EXAM_NUMBER_OF_QUESTIONS_TO_PASS": 28,
                "EXAM_TIME_LIMIT": 60,
                "LAST_MODIFIED_BY_DATE": "2026-08-20 00:00:00",
                "OBJECTIVES": [
                    {
                        "EXAM_OBJECTIVE_TITLE": "Plan",
                        "PERCENTAGE_OF_OBJECTIVE_QUESTIONS": "40",
                        "EXAM_OBJECTIVE_DESCRIPTION": "<ul><li>Choose a design</li></ul>",
                    },
                    {
                        "EXAM_OBJECTIVE_TITLE": "Build",
                        "PERCENTAGE_OF_OBJECTIVE_QUESTIONS": "60",
                        "EXAM_OBJECTIVE_DESCRIPTION": "<ul><li>Verify a deployment</li></ul>",
                    },
                ],
            }
        )
        objectives = monitor.extract_ibm_certification_objectives(body)
        status = monitor.extract_ibm_certification_status(body)
        self.assertIn("Plan (40%)", objectives)
        self.assertIn("- Choose a design", objectives)
        self.assertEqual(
            ["Exam C1000-999; status Live; last modified 2026-08-20"],
            status["skills_versions"],
        )

    def test_extracts_oracle_learning_path_exam_and_skills(self) -> None:
        import json

        payload = {
            "id": "138845",
            "name": "Become a Java SE 21 Developer",
            "description": (
                "<p>Upon completion of this Learning Path:</p><ul>"
                "<li>Gain proficiency with classes and records</li>"
                "<li>Use inheritance and generics</li>"
                "<li>Handle values and dates</li>"
                "<li>Control program flow and exceptions</li>"
                "<li>Work with streams, collections, concurrency, and I/O</li>"
                "<li>Use modules and package code</li></ul>"
                "<p>This course is intended for Java developers.</p>"
            ),
            "totalDuration": "40",
            "containerChildren": [
                {
                    "name": "Java SE 21 Developer Professional (1Z0-830)",
                    "examSeriesCode": "1Z0-830",
                    "duration": "7200",
                }
            ],
        }
        page = "var globalLpData =" + json.dumps(payload) + ";"
        objectives = monitor.extract_oracle_learning_path_objectives(page)
        status = monitor.extract_oracle_learning_path_status(page)
        self.assertIn("Exam: 1Z0-830", objectives)
        self.assertIn("Use modules and package code", objectives)
        self.assertIn("Duration: 120 minutes", status["skills_versions"])

    def test_monitor_skips_retired_exam_with_removed_blueprint(self) -> None:
        import json
        from tempfile import TemporaryDirectory
        from unittest.mock import patch

        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            config = root / "exams.json"
            vendors = root / "vendors.json"
            config.write_text(
                json.dumps(
                    {
                        "exams": [
                            {
                                "code": "OLD-C01",
                                "vendor_id": "example",
                                "title": "Retired example",
                                "status": "retired",
                                "study_guide_url": "https://example.test/removed",
                                "guide_path": "guides/old.md",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            vendors.write_text(
                json.dumps(
                    {
                        "vendors": [
                            {
                                "id": "example",
                                "objective_adapter": "microsoft-learn",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            with patch.object(
                monitor, "fetch", side_effect=AssertionError("must not fetch")
            ):
                result = monitor.monitor(
                    config, root / "snapshots", False, vendors
                )

            self.assertEqual([], result["results"])
            self.assertEqual([], result["changed"])
            self.assertEqual([], result["errors"])

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

    def test_extracts_snowflake_scope_and_lifecycle(self) -> None:
        body = """
        <html><body><main>
          <p>GES-C02</p><h1>SnowPro Specialty: Gen AI</h1>
          <p>The certification validates Gen AI skills in Snowflake.</p>
          <h2>Certification overview</h2><p>This certification will test the ability to:</p>
          <ul><li>Use Cortex AI features and functions</li>
          <li>Build and fine-tune open-source models</li>
          <li>Build document parsing pipelines</li></ul>
          <h2>Candidate</h2><p>1 or more years of Gen AI experience with Snowflake.</p>
          <p>This exam will be retired on December 1, 2027.</p>
          <h2>SnowPro FAQs</h2><p>Do not include this text.</p>
        </main></body></html>
        """

        objectives = monitor.extract_snowflake_objectives(body)
        status = monitor.extract_snowflake_status(body)

        self.assertIn("GES-C02", objectives)
        self.assertIn("Build document parsing pipelines", objectives)
        self.assertNotIn("Do not include this text", objectives)
        self.assertIn("GES-C02", status["skills_versions"])
        self.assertTrue(
            any("December 1, 2027" in item for item in status["upcoming_announcements"])
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

    def test_extracts_isc2_weighted_domains_and_status(self) -> None:
        topics = "".join(
            f"<h2>{domain}.{item} - Topic {domain}-{item}</h2>"
            for domain in range(1, 6)
            for item in range(1, 4)
        )
        body = f"""
        <p>EFFECTIVE DATE: SEPTEMBER 1, 2026</p>
        <h1>Example Certification Exam Outline</h1>
        <p>Length of exam</p><p>2 hours</p>
        <p>Number of items</p><p>100-125</p>
        <p>Passing grade</p><p>700 out of 1000 points</p>
        <p>Domain 1 20%</p><p>Domain 2 20%</p><p>Domain 3 20%</p>
        <p>Domain 4 20%</p><p>Domain 5 20%</p>
        <h2>Domain 1: Principles</h2>{topics}
        <h2>Additional Examination Information</h2>
        """

        objectives = monitor.extract_isc2_objectives(body)
        status = monitor.extract_isc2_status(body)

        self.assertIn("5.3 - Topic 5-3", objectives)
        self.assertIn("EFFECTIVE DATE: SEPTEMBER 1, 2026", status["skills_versions"])
        self.assertIn("Length of exam: 2 hours", status["skills_versions"])

    def test_extracts_nvidia_weighted_blueprint_and_status(self) -> None:
        body = """
        <p>NVIDIA-Certified Associate</p><h1>Example AI</h1><p>(NCA-EXAI)</p>
        <h2>About This Certification</h2><p>Example certification.</p>
        <p>Duration: 1 hour</p><p>Price: $125</p>
        <p>Certification level: Associate</p><p>Subject: Example AI</p>
        <p>Number of questions: 50</p><p>Prerequisites: Basic AI</p>
        <p>Language: English</p><p>Validity: Valid for two years.</p>
        <h2>Exam Blueprint</h2>
        <p>The table below provides an overview.</p>
        <p>Foundations</p><p>40%</p><p>Build foundations</p>
        <p>Development</p><p>30%</p><p>Build applications</p>
        <p>Operations</p><p>30%</p><p>Operate applications</p>
        <h2>Contact Us</h2>
        """

        objectives = monitor.extract_nvidia_objectives(body)
        status = monitor.extract_nvidia_status(body)

        self.assertIn("Foundations\n40%", objectives)
        self.assertIn("NCA-EXAI", status["skills_versions"])
        self.assertIn("Duration: 1 hour", status["skills_versions"])

    def test_extracts_salesforce_weighted_blueprint_and_status(self) -> None:
        body = """
        <h1>Salesforce Certified Example Exam Guide</h1>
        <h2>About the Exam</h2>
        <p>Content: 60 multiple-choice questions</p>
        <p>Time allotted to complete the exam: 105 minutes</p>
        <p>Passing score: 68%</p><p>Version: Summer '26</p>
        <p>Registration fee: USD 200</p><p>Prerequisite: None</p>
        <h2>Exam Outline</h2>
        <h3>Configuration and Setup: 25%</h3><p>Configure users.</p>
        <h3>Data: 25%</h3><p>Manage data.</p>
        <h3>Automation: 25%</h3><p>Build flows.</p>
        <h3>Security: 25%</h3><p>Control access.</p>
        <h2>Recommended Training and Resources</h2>
        <p>You must complete a maintenance module once per year.</p>
        """

        objectives = monitor.extract_salesforce_objectives(body)
        status = monitor.extract_salesforce_status(body)

        self.assertIn("Configuration and Setup: 25%", objectives)
        self.assertIn("Version: Summer '26", status["skills_versions"])
        self.assertIn(
            "You must complete a maintenance module once per year.",
            status["skills_versions"],
        )

    def test_extracts_splunk_track_scope_and_exam_details(self) -> None:
        body = """
        <h2>OVERVIEW</h2>
        <h2>Advance your cybersecurity analytics and insights</h2>
        <p>Use cyber defense tools for continual monitoring.</p>
        <h2>GETTING STARTED</h2>
        <h2>Who should take this exam?</h2>
        <p>Analysts using Splunk Enterprise and Enterprise Security.</p>
        <p>Exam Details:</p>
        <ul>
          <li>Level: Intermediate</li>
          <li>Prerequisites: None</li>
          <li>Length: 75 minutes</li>
          <li>Format: 66 multiple choice questions</li>
          <li>Pricing: $130 USD per exam attempt</li>
          <li>Delivery: Pearson VUE</li>
        </ul>
        <p>Preparation:</p>
        <p>Review the blueprint.</p>
        """

        objectives = monitor.extract_splunk_objectives(body)
        status = monitor.extract_splunk_status(body)

        self.assertIn("Advance your cybersecurity analytics", objectives)
        self.assertNotIn("Who should take", objectives)
        self.assertIn("Length: 75 minutes", status["skills_versions"])
        self.assertEqual([], status["upcoming_announcements"])

    def test_extracts_isaca_job_practice_and_scheduled_update(self) -> None:
        body = """
        <h1>What is covered on the CISM exam?</h1>
        <p>The Certified Information Security Manager exam consists of 150
        questions covering 4 job practice domains.</p>
        <h2>Job practice areas tested for and validated by a CISM certification</h2>
        <h3>17% Domain 1 - Information Security Governance</h3>
        <p>Enterprise Governance</p><p>Organizational Culture</p>
        <h3>20% Domain 2 - Information Security Risk Management</h3>
        <p>Risk Assessment</p><p>Risk Response</p>
        <h3>33% Domain 3 - Information Security Program</h3>
        <p>Program Development</p><p>Program Management</p>
        <h3>30% Domain 4 - Incident Management</h3>
        <p>Readiness</p><p>Operations</p>
        <h3>Supporting tasks</h3><p>Report to stakeholders.</p>
        <h2>Getting ready for the exam</h2>
        <p>The CISM Exam Content Outline will be updated effective 3 November 2026.</p>
        """

        objectives = monitor.extract_isaca_objectives(body)
        status = monitor.extract_isaca_status(body)

        self.assertIn("17% Domain 1", objectives)
        self.assertIn("Supporting tasks", objectives)
        self.assertNotIn("Getting ready", objectives)
        self.assertIn("150 questions", status["skills_versions"][0])
        self.assertIn("3 November 2026", status["upcoming_announcements"][0])

    def test_extracts_python_institute_syllabus_and_status(self) -> None:
        body = """
        <h1>PCEP Certified Entry-Level Python Programmer: EXAM SYLLABUS</h1>
        <p>Exam: PCEP-30-02</p><p>Status: ACTIVE</p>
        <h2>Exam Syllabus</h2><p>Last updated: February 23, 2022</p>
        <p>Aligned with Exam PCEP-30-02</p>
        <h3>Exam Syllabus Contents</h3>
        <p>Block 1: Computer Programming and Python Fundamentals</p>
        <p>Objective 1.1</p><p>Objective 1.2</p><p>Objective 1.3</p>
        <p>Block 2: Control Flow - Conditional Blocks and Loops</p>
        <p>Objective 2.1</p><p>Objective 2.2</p><p>Objective 2.3</p>
        <p>Block 3: Data Collections</p>
        <p>Objective 3.1</p><p>Objective 3.2</p><p>Objective 3.3</p>
        <p>Block 4: Functions and Exceptions</p>
        <p>Objective 4.1</p><p>Objective 4.2</p><p>Objective 4.3</p>
        <p>Download PCEP-30-02 Exam Syllabus in PDF</p>
        <h2>Terms and Policies</h2>
        """

        objectives = monitor.extract_python_institute_objectives(body)
        status = monitor.extract_python_institute_status(body)

        self.assertIn("Block 1: Computer Programming", objectives)
        self.assertIn("Block 4: Functions and Exceptions", objectives)
        self.assertNotIn("Download PCEP", objectives)
        self.assertTrue(
            any("PCEP-30-02" in line for line in status["skills_versions"])
        )
        self.assertEqual([], status["upcoming_announcements"])

    def test_extracts_cpp_institute_embedded_outline(self) -> None:
        body = """
        <p>Exam version:</p><p>CPE-20-01 (Active)</p>
        <h2>Exam Objectives by Block</h2>
        <h3>Block 1 - Basic Concepts</h3><p>One</p><p>Two</p>
        <h3>Block 2 - Data Types</h3><p>Three</p><p>Four</p>
        <h3>Block 3 - Operators</h3><p>Five</p><p>Six</p>
        <h3>Block 4 - Flow Control</h3><p>Seven</p><p>Eight</p>
        <h3>Block 5 - Loops</h3><p>Nine</p><p>Ten</p>
        <h2>MQC Profile</h2><p>After the outline.</p>
        <p>Last updated: July 24, 2025</p>
        <p>Aligned with Exam CPE-20-01</p>
        """
        objectives = monitor.extract_cpp_institute_objectives(body)
        status = monitor.extract_cpp_institute_status(body)
        self.assertIn("Block 4 - Flow Control", objectives)
        self.assertNotIn("MQC Profile", objectives)
        self.assertIn("CPE-20-01 (Active)", status["skills_versions"])

    def test_extracts_js_institute_exam_scope(self) -> None:
        body = """
        <p>Exam Code &amp; Current Exam Versions | JSE-40-01 - Status: Active</p>
        <h2>Exam Scope</h2>
        <h3>Exam block #1: Fundamentals</h3><p>One</p><p>Two</p>
        <h3>Exam block #2: Variables</h3><p>Three</p><p>Four</p>
        <h3>Exam block #3: Operators</h3><p>Five</p><p>Six</p>
        <h3>Exam block #4: Control flow</h3><p>Seven</p><p>Eight</p>
        <h3>Exam block #5: Functions</h3><p>Nine</p><p>Ten</p>
        <h2>Terms &amp; Policies</h2>
        """
        objectives = monitor.extract_js_institute_objectives(body)
        status = monitor.extract_js_institute_status(body)
        self.assertIn("Exam block #4: Control flow", objectives)
        self.assertNotIn("Terms & Policies", objectives)
        self.assertIn("JSE-40-01", status["skills_versions"][0])


if __name__ == "__main__":
    unittest.main()
