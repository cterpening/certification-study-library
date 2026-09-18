import json
from pathlib import Path
import sys
import unittest
from urllib.error import HTTPError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_certification_discovery import annotate_inventory, canonical, check, compare, extract, merge_baseline, markdown


SOURCE = {"id": "example", "vendor_id": "example", "url": "https://example.com/catalog",
          "cadence": "weekly", "extract": "links", "include": r"/certs/[^/]+$",
          "expected_text": "Credentials", "minimum_items": 1, "scope": "Example catalog"}


class CertificationDiscoveryTests(unittest.TestCase):
    def test_microsoft_feed_requires_complete_unique_results(self):
        source = dict(SOURCE, url="https://learn.microsoft.com/api/contentbrowser/search/credentials",
                      extract="microsoft-json", expected_text="Microsoft", include=r"/credentials/certifications/[^/]+/?$")
        row = {"uid": "certification.example", "locale": "en-us", "credential_types": ["certification"],
               "title": "Microsoft Example", "url": "/credentials/certifications/example/", "exams": [{"uid": "exam.ab-100"}]}
        payload = {"count": 1, "results": [row]}
        items = extract(json.dumps(payload), source)
        self.assertEqual(items[0]["url"], "https://learn.microsoft.com/en-us/credentials/certifications/example")
        self.assertIn("AB-100", items[0]["detail"])
        for bad in ({"count": 2, "results": [row]}, dict(payload, **{"@nextLink": "next-page"}),
                    {"count": 2, "results": [row, row]}, {"count": 1, "results": [{}]},
                    {"count": 1, "results": [dict(row, url="https://other.example/credentials/certifications/example/")]}):
            self.assertEqual(check(source, None, lambda _: json.dumps(bad))["status"], "manual-review")

    def test_exam_transition_changes_even_when_credential_title_and_url_do_not(self):
        source = dict(SOURCE, url="https://learn.microsoft.com/api/contentbrowser/search/credentials",
                      extract="microsoft-json", expected_text="Microsoft", include=r"/credentials/certifications/[^/]+/?$")
        row = {"uid": "certification.example", "locale": "en-us", "credential_types": ["certification"],
               "title": "Microsoft Example", "url": "/credentials/certifications/example/", "exams": [{"uid": "exam.pl-400"}]}
        before = check(source, None, lambda _: json.dumps({"count": 1, "results": [row]}))
        row["exams"].append({"uid": "exam.ab-400"})
        after = check(source, before, lambda _: json.dumps({"count": 1, "results": [row]}))
        self.assertEqual(after["status"], "changed")
        self.assertIn("AB-400", after["changed"][0]["after"]["detail"])
        row["exams"].reverse()
        self.assertEqual(check(source, after, lambda _: json.dumps({"count": 1, "results": [row]}))["status"], "unchanged")

    def test_github_feed_lifecycle_and_contract_failures(self):
        source = dict(SOURCE, url="https://learn.github.com/api/certifications", extract="github-json",
                      expected_text="GitHub", include=r"/credentials/certifications/[^/]+/?$", allowed_hosts=["learn.microsoft.com"])
        row = {"certification": {"id": "COPILOT", "title": "GitHub Copilot", "active": True, "beta": False,
                                 "msLearnUrl": "https://learn.microsoft.com/en-us/credentials/certifications/github-copilot"}}
        before = check(source, None, lambda _: json.dumps([row]))
        row["certification"]["active"] = False
        after = check(source, before, lambda _: json.dumps([row]))
        self.assertEqual(after["status"], "changed")
        self.assertEqual(len(after["items"]), 1)
        for bad in ({"error": "sign in"}, [row, row], [{"certification": {}}]):
            self.assertEqual(check(source, before, lambda _: json.dumps(bad))["status"], "manual-review")

    def test_catalog_normalization_and_untrusted_links(self):
        page = '''<h1>Credentials</h1><script><a href="/certs/hidden">Hidden</a></script>
        <svg/><a href="/certs/a?utm_source=mail"><h3>Credential A</h3><p>Description</p></a>
        <a href="/certs/a#register">A</a><a href="https://other.example/certs/x">External</a>
        <a href="http://example.com/certs/insecure">Insecure</a>'''
        self.assertEqual(extract(page, SOURCE), [{"key": "https://example.com/certs/a",
                         "url": "https://example.com/certs/a", "title": "Credential A"}])
        self.assertEqual(canonical("https://example.com/exam?id=2&utm_campaign=x"), "https://example.com/exam?id=2")

    def test_empty_catalog_and_login_shell_are_not_removals(self):
        for page in ("<h1>Sign in</h1>", "<h1>Credentials</h1><p>Loading...</p>"):
            result = check(SOURCE, None, lambda source: page)
            self.assertEqual(result["status"], "manual-review")
            self.assertNotIn("missing", result)

    def test_link_reorder_is_ignored_but_title_and_membership_changes_are_reported(self):
        page = '<h1>Credentials</h1><a href="/certs/a">A</a><a href="/certs/b">B</a>'
        before = compare(SOURCE, extract(page, SOURCE), None)
        reordered = '<h1>Credentials</h1><a href="/certs/b">B</a><a href="/certs/a">A</a>'
        self.assertEqual(compare(SOURCE, extract(reordered, SOURCE), before)["status"], "unchanged")
        changed = '<h1>Credentials</h1><a href="/certs/a">A beta</a><a href="/certs/c">C</a>'
        result = compare(SOURCE, extract(changed, SOURCE), before)
        self.assertEqual(result["added"][0]["title"], "C")
        self.assertEqual(result["missing"][0]["title"], "B")
        self.assertEqual(result["changed"][0]["after"]["title"], "A beta")

    def test_changed_extractor_requires_a_new_baseline(self):
        before = {"contract": "old", "items": [{"key": "old"}]}
        result = compare(SOURCE, [], before)
        self.assertEqual(result["status"], "baseline-needed")
        self.assertEqual(result["missing"], [])

    def test_suspicious_partial_catalog_is_not_accepted(self):
        rows = [{"key": str(i), "title": str(i), "url": "https://example.com"} for i in range(10)]
        before = compare(SOURCE, rows, None)
        result = compare(SOURCE, rows[:2], before)
        self.assertEqual(result["status"], "manual-review")
        baseline = merge_baseline({"sources": []}, [before])
        self.assertEqual(merge_baseline(baseline, [result]), baseline)

    def test_partial_write_preserves_failed_and_unselected_sources(self):
        baseline = {"schema_version": 1, "sources": [{"id": "failed", "items": [1]}, {"id": "unselected", "items": [2]}]}
        result = compare(SOURCE, [{"key": "a", "url": "https://example.com/a", "title": "A"}], None)
        merged = merge_baseline(baseline, [result, {"id": "failed", "status": "error"}])
        self.assertEqual({row["id"] for row in merged["sources"]}, {"failed", "unselected", "example"})
        self.assertIn(baseline["sources"][0], merged["sources"])
        self.assertEqual(baseline["sources"][1]["items"], [2])

    def test_academy_table_does_not_turn_headers_into_courses(self):
        source = dict(SOURCE, extract="table", column=1, include=r"^(?!Course$).+")
        rows = extract('<h1>Credentials</h1><table><tr><th>Category</th><th>Course</th></tr><tr><td>Build</td><td>Course One</td></tr><tr><td>Build</td><td>Course Two</td></tr></table>', source)
        self.assertEqual([row["title"] for row in rows], ["Course One", "Course Two"])

    def test_retirement_date_change_is_reported_when_exam_code_is_unchanged(self):
        source = dict(SOURCE, extract="table", column=0, include=r"^AA-123$")
        old = '<h1>Credentials</h1><table><tr><td>AA-123</td><td>2026-10-01</td></tr></table>'
        before = compare(source, extract(old, source), None)
        after = compare(source, extract(old.replace('2026-10-01', '2026-12-01'), source), before)
        self.assertEqual(after["status"], "changed")
        self.assertEqual(after["added"], [])

    def test_exam_codes_are_matched_within_vendor_only(self):
        seeds = [{"vendor_id": "aws", "exam_code": "MLA-C01"}]
        rows = [{"vendor_id": vendor, "items": [{"title": "MLA-C01", "url": "https://example.com/"}]}
                for vendor in ("aws", "snowflake")]
        annotate_inventory(rows, {}, seeds)
        self.assertEqual(rows[0]["items"][0]["inventory_matches"], ["MLA-C01"])
        self.assertEqual(rows[1]["items"][0]["inventory_matches"], [])

    def test_http_failure_classification_has_no_signed_url(self):
        for code, state in ((403, "manual-review"), (429, "manual-review"), (404, "error")):
            def failing(source):
                raise HTTPError("https://example.com/?SAMLRequest=SECRET", code, "error", {}, None)
            result = check(SOURCE, None, failing)
            self.assertEqual(result["status"], state)
            self.assertNotIn("SECRET", json.dumps(result))

    def test_monthly_report_requires_broader_review_even_without_deltas(self):
        report = {"checked_on": "2026-09-17", "mode": "monthly", "sources": []}
        result = markdown(report, {"sources": [SOURCE]})
        self.assertIn("Complete this broader search manually", result)
        self.assertIn("site:example.com", result)

    def test_all_registered_vendors_have_weekly_discovery_and_unique_ids(self):
        root = Path(__file__).resolve().parents[1]
        config = json.loads((root / "config/certification-discovery.json").read_text())
        vendors = json.loads((root / "data/vendors.json").read_text())["vendors"]
        ids = [source["id"] for source in config["sources"]]
        self.assertEqual(len(ids), len(set(ids)))
        weekly = {source["vendor_id"] for source in config["sources"] if source["cadence"] == "weekly"}
        self.assertFalse({vendor["id"] for vendor in vendors} - weekly)


if __name__ == "__main__":
    unittest.main()
