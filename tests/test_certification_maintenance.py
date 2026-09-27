import copy
from datetime import date
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from run_certification_maintenance import build_report, collect, markdown
from check_certification_discovery import markdown as discovery_markdown
from check_official_study_guides import extract_comptia_status


TODAY = date(2026, 9, 27)
EXAM = {"code": "EX-1", "vendor_id": "example", "status": "active",
        "guide_path": "guides/ex.md", "study_guide_url": "https://example.com/exam",
        "upcoming_change_checked": "2026-09-20"}
SOURCE = {"id": "ex-source", "supported_exams": ["EX-1"], "url": "https://example.com/exam"}
POLICY = {"lookahead_days": 30, "lifecycle_review_days": 30, "events": []}


def reports():
    return {"objectives": {"results": [{"code": "EX-1", "status": "unchanged", "url": EXAM['study_guide_url']}]},
            "health": {"checked_on": TODAY.isoformat(), "results": [{"id": "ex-source", "status": "ok"}],
                       "findings": {}, "summary": {}},
            "discovery": {"checked_on": TODAY.isoformat(), "sources": [], "needs_review": False}}


class MaintenanceTests(unittest.TestCase):
    def test_comptia_duration_label_is_monitored(self):
        page = '<h2>Exam details</h2><p>Exam version: V7</p><p>Exam series code: SY0-701</p>' \
               '<p>Launch date: November 7, 2023</p><p>Duration: 90 minutes</p>' \
               '<p>Number of questions: 90</p><p>Passing score: 750</p>'
        self.assertIn('Duration: 90 minutes', extract_comptia_status(page)['skills_versions'])

    def test_complete_clean_report_has_every_exam_and_does_not_mutate_inputs(self):
        data = reports()
        before = copy.deepcopy(data)
        result = build_report([EXAM], [SOURCE], data, POLICY, TODAY)
        self.assertFalse(result["needs_review"])
        self.assertEqual(result["summary"]["guides"], 1)
        self.assertEqual(data, before)

    def test_missing_and_stale_reports_cannot_be_clean(self):
        for data in ({}, {"health": {"checked_on": "2026-09-01", "results": []}}):
            result = build_report([EXAM], [SOURCE], data, POLICY, TODAY)
            self.assertTrue(result["needs_review"])
            self.assertTrue(result["errors"])
            self.assertEqual(result["exams"][0]["objective_status"], "not-checked")

    def test_retired_exam_keeps_baseline_but_still_checks_sources(self):
        data = reports()
        data["objectives"]["results"] = []
        data["health"]["results"][0]["status"] = "missing"
        result = build_report([dict(EXAM, status="retired")], [SOURCE], data, POLICY, TODAY)
        self.assertFalse(result["errors"])
        self.assertEqual(result["exams"][0]["objective_status"], "retired-baseline-preserved")
        self.assertTrue(result["exams"][0]["source_issues"])

    def test_manual_access_and_unexpected_errors_remain_distinct(self):
        for status in ("manual-review", "error"):
            data = reports()
            data["objectives"]["results"][0].update(status=status, error="provider unavailable")
            data["health"]["results"][0]["status"] = "blocked"
            result = build_report([EXAM], [SOURCE], data, POLICY, TODAY)
            self.assertEqual(bool(result["errors"]), status == "error")
            self.assertEqual(result["exams"][0]["objective_status"], status)
            self.assertTrue(result["needs_review"])

    def test_future_and_overdue_events_do_not_change_exam_status(self):
        policy = dict(POLICY, events=[{"id": "deadline", "exam_codes": ["EX-1"],
                                     "review_on": "2026-09-28", "action": "Recheck availability",
                                     "url": "https://example.com/exam"}])
        for today, timing in ((TODAY, "upcoming"), (date(2026, 9, 29), "due")):
            result = build_report([EXAM], [SOURCE], reports(), policy, today)
            row = result["exams"][0]
            self.assertEqual(row["events"][0]["timing"], timing)
            self.assertEqual(row["catalog_status"], "active")
            self.assertIn("Recheck availability", markdown(result))

    def test_partial_health_report_is_a_collection_error(self):
        data = reports()
        data["health"]["results"] = []
        result = build_report([EXAM], [SOURCE], data, POLICY, TODAY)
        self.assertTrue(result["errors"])
        self.assertEqual(result["exams"][0]["source_issues"][0]["status"], "not-checked")

    def test_old_blueprint_url_cannot_validate_reconfigured_exam(self):
        data = reports()
        data['objectives']['results'][0]['url'] = 'https://example.com/old'
        self.assertTrue(build_report([EXAM], [SOURCE], data, POLICY, TODAY)['errors'])

    def test_existing_live_output_is_rejected_without_overwriting_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            marker = path / "keep.txt"
            marker.write_text("keep")
            with self.assertRaises(ValueError):
                collect(path, "weekly")
            self.assertEqual(marker.read_text(), "keep")

    def test_repository_calendar_has_valid_unique_events_and_exam_references(self):
        root = Path(__file__).resolve().parents[1]
        policy = json.loads((root / "config/certification-maintenance.json").read_text())
        codes = {e["code"] for e in json.loads((root / "config/exams.json").read_text())["exams"]}
        self.assertEqual(len({e["id"] for e in policy["events"]}), len(policy["events"]))
        for event in policy["events"]:
            date.fromisoformat(event["review_on"])
            self.assertTrue(set(event["exam_codes"]) <= codes)
            self.assertTrue(event["url"].startswith("https://"))
            self.assertTrue(event["action"])

    def test_discovery_title_change_is_visible_with_unchanged_exam_reference(self):
        before = {"title": "Architect", "detail": "Required exam references: AB-100", "url": "https://example.com/exam"}
        after = dict(before, title="Architect Expert")
        report = {"checked_on": TODAY.isoformat(), "mode": "weekly", "sources": [
            {"id": "catalog", "status": "changed", "url": "https://example.com", "items": [],
             "changed": [{"before": before, "after": after}]}]}
        rendered = discovery_markdown(report, {})
        self.assertIn("Architect → Architect Expert", rendered)


if __name__ == "__main__":
    unittest.main()
