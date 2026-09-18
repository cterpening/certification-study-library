# Automation and maintenance

## Certification discovery inventory

`config/certification-seeds.json` records the official catalog URL, explicit
selection rule, and last verification date for each discovery scope. Repository
validation checks its structure, requires every published guide to remain in the
inventory, and prevents `CERTIFICATIONS.txt` from drifting from it.

`config/certification-discovery.json` separately defines the broader official
catalogs to inspect, including credentials outside the selected guide inventory.
`scripts/check_certification_discovery.py` compares their public listings against
`data/certification-discovery-baseline.json` and reports added, missing, and changed
observations. It also compares listing URLs and vendor-scoped exam codes with the
seed inventory, published guide sources, and partner reference links. Matches indicate a reference,
not complete guide coverage; unmatched URLs need identity/alias review.

The discovery workflow is configured for Wednesdays at 13:23 UTC. On the first
of each month at 14:23 UTC it also fetches configured announcement/status pages
and produces the broader discovery checklist. Both schedules become active when
the workflow is on the repository's default branch and Actions is enabled.
Reports appear in the run summary and JSON/Markdown artifacts retained 90 days.
The workflow requires only read access and does not depend on permission to create PRs.

The monthly checklist still needs a maintainer or research agent to search official
announcements, inspect additional catalogs and pagination, verify individual
blueprints and eligibility, and classify certificates/badges separately from
certifications. A scheduled fetch does not claim that this review has happened.
See the [September 17 catalog audit](research/2026-09-17-catalog-audit.md) for the
initial findings and catalog coverage limits.

GitHub and Microsoft use the public JSON feeds requested by their current catalog
websites. These are website interfaces, not guaranteed integration APIs. The
Microsoft adapter checks the returned total, unique identities, and next-page
marker; a partial response requires manual review. Required-exam references are
compared as well as credential names, so a new exam under an existing credential
can produce a change. GitHub Applied Skills remain separate from certifications.
The [follow-up review](research/2026-09-17-catalog-follow-up.md) records browser
observations for Cisco, MongoDB, ServiceNow, and IBM. Their scheduled HTML checks
still require manual review; browser evidence is not an accepted HTML baseline.

The [published-exam validation](research/2026-09-17-exam-validation.md) records a
separate check of all 223 published guides. Its evidence ledger is
`ADLC_Docs/operations/2026-09-17-exam-validation.json`. The objective monitor ran
against a temporary copy of `data/objective-snapshots`; accepted snapshots were
preserved. Public PDF, complete HTML, and unsigned browser checks recovered 37
sources outside the monitor. These findings do not turn manual HTTP limitations
into automated passes or renew historical technical-audit dates.

```powershell
python scripts/check_certification_discovery.py --mode weekly
python scripts/check_certification_discovery.py --mode monthly
```

Review the report, then accept selected successful observations explicitly:

```powershell
python scripts/check_certification_discovery.py --mode monthly --only databricks-catalog --write
```

The default commands do not modify the baseline. `--write` preserves failed and
unselected sources. Missing markers, empty/undersized extraction, access-denied
pages, and a catalog shrinking by more than 40% require manual review and cannot
replace a baseline. Network/HTTP errors remain visible and fail the run. A changed
source/extraction configuration requires a new baseline; a missing listing is
never automatically classified as retired. Listing comparisons do not inspect
every linked exam's availability, code, or objective body; use the objective
monitor and source-freshness review for that work. Seed `last_verified` dates are
not advanced by discovery runs, and guides are never silently added or rewritten.

## Objective monitoring

The repository’s weekly objective workflow attempts the official objective page for every configured exam. It selects the adapter registered for that exam's provider in `data/vendors.json`, stores normalized objective and exam-status snapshots under `data/objective-snapshots`, and proposes changes through a pull request.

Some reachable provider pages do not expose their reviewed objective content to a non-browser
HTML extractor. Known exact extraction failures are recorded in
`config/objective-monitor-limitations.json` with a review date, reason, and manual freshness
route. The monitor still requests those pages. Only an exact documented failure becomes a
visible `manual-review` result; a different network, HTTP, or extraction failure remains an
error and fails the workflow. If a provider begins exposing parseable content, normal snapshot
comparison resumes automatically. Manual-review guides remain in the recurring
`docs/SOURCE-FRESHNESS.md` process and are not claimed as continuously machine-validated.

All objective and source-health requests pass through a shared outbound URL policy. The
policy rejects non-HTTPS schemes, embedded credentials, localhost, non-public literal IP
addresses, and non-default HTTPS ports before opening a connection, then validates the
final redirect. Objective retrieval additionally restricts redirects to the configured
site's host or its `www` equivalent. Source-health monitoring permits cross-host redirects
because detecting canonical moves is part of that workflow, but the final destination must
still remain public HTTPS. A rejected destination is evidence for review, not permission to
bypass the guard.

The workflow detects:

- A changed skills-version or tested-product baseline
- A newly announced future update or retirement
- The appearance of more than one published skills version
- Added, removed, or renamed objective groups
- Changed percentage weightings when the provider publishes them
- Added, removed, or reworded objective bullets

## What it deliberately does not automate

It does not rewrite the explanatory study guides. A changed bullet might require:

- New technical research
- Removal of a retired feature
- Updated labs or screenshots
- A terminology migration
- Changes to security or data-handling guidance
- New **VERIFY CURRENT** flags

A generated prose rewrite could look convincing while misunderstanding the exam change. The automation therefore produces evidence and a review task.

## Source catalog health monitoring

The separate weekly source-health workflow checks every approved entry in `data/sources.json`. It records a reviewable baseline in `data/source-health.json` and reports:

- missing pages and request errors;
- redirects and canonical-URL changes;
- changed public page titles;
- changed duration signals found in public HTML or structured metadata;
- catalog entries whose `last_checked` date is older than the configured threshold; and
- providers that block automated requests.

The monitor does not scrape authenticated content, automatically replace a URL, change a runtime, or update `last_checked`. A blocked automated request is informational because a legitimate provider may reject non-browser clients. Missing pages and metadata changes open or update a maintenance issue for human review; the complete JSON and Markdown reports remain workflow artifacts for 30 days.

YouTube title, canonical-URL, and duration metadata are not compared because consent, localization, and bot-handling responses vary by runner region. YouTube entries still receive reachability, HTTP-status, and redirect checks; course titles and runtimes remain deliberate catalog-review fields.

After reviewing and accepting intentional source changes, run the monitor locally with `--write` and commit the refreshed snapshot with the catalog change. Until that review occurs, the monitor may continue reporting the difference.

Use repeated `--only SOURCE_ID` arguments with `--write` for a reviewed subset;
unselected observations are preserved. Duration-signal ordering is ignored, while
changed values still require review. SAML sign-in redirects are reported as blocked
access instead of changes to course metadata; signed login parameters are not retained.

## Official-source freshness discovery

Health monitoring can inspect only URLs the repository already knows. The
separate AI-assisted freshness workflow searches official credential catalogs,
product documentation, release notes, roadmaps, retirement notices, and vendor
announcements for material that is not registered yet. Its findings are recorded
in `data/source-freshness.json`; unreviewed URLs enter
`data/source-candidates.json` rather than being silently promoted.

Prepare a recurring risk-ordered batch with:

```bash
python3 scripts/prepare_source_freshness_scan.py \
  --batch-id freshness-2026-09-12-01 \
  --size 10 \
  --output .site-build/freshness-2026-09-12-01.json
```

The default seven-day recurrence matters even when local files are unchanged,
because a new external page cannot alter a stored hash. A guide or registered
official-source change also creates a new baseline immediately. The agent is
read-only; source promotion and guide repair remain separate review steps. See
[Official-source freshness scans](SOURCE-FRESHNESS.md) for the rubric and result
contract.

## Independent AI-audit batches

The batch preparer selects guides that do not have a completed audit for their current objective-snapshot hash and audit-rubric version. Its default risk order puts changing, beta, retiring, scheduled-change, source-health, and visible `VERIFY CURRENT` evidence first. It emits the complete guide, snapshot, review, and source handoff needed by a fresh-context agent; it does not edit a guide or decide that a finding is fixed.

```bash
python3 scripts/prepare_ai_audit_batch.py \
  --batch-id audit-2026-09-04-01 \
  --size 10 \
  --output .site-build/audit-2026-09-04-01.json
```

Keep normal batches at 10 guides and never exceed 12. Record scrutinized results in `data/ai-audits.json`; repository validation enforces the snapshot hashes, exact check set, finding dispositions, verdict logic, result coverage, and aggregate summary. The complete rubric and repair separation are in [Independent AI guide audits](AI-AUDIT.md).

## First run

The first successful run creates normalized snapshots for all configured exams and opens a pull request. Review the extracted text against each linked official page before merging. Later runs compare against those approved snapshots.

## Required repository settings

1. Enable GitHub Actions.
2. In **Settings → Actions → General**, allow workflows to create pull requests if the organization permits it.
3. Ensure the default `GITHUB_TOKEN` can receive the workflow permissions declared in the workflow.
4. Allow the source-health workflow to create or refresh its `maintenance` label and issue.
5. Protect `main` with a pull-request requirement and normal review.

The `pull-requests: write` workflow permission does not override the repository or
organization setting that prohibits Actions from creating pull requests. If GitHub
rejects PR creation, the objective workflow remains failed and reports the publication
step, run URL, and branch link. A maintainer can create the PR from that branch or an
administrator can enable the setting in item 2. The `objective-monitor-report` artifact
retains the objective report, available snapshot patch, and PR error for 30 days.
Setup/test failures and source-extraction failures are reported separately.

No PAT or external API key is required. The workflow uses the repository-scoped `GITHUB_TOKEN`.

## Delivery and dependency policy

The validation and Pages workflows call the same repository-local composite action at
`.github/actions/validate/action.yml`. That action owns Python setup, dependency installation,
unit tests, repository validation, the strict site build, and generated-site validation.
Change the shared gate once and keep workflow-specific permissions, triggers, artifact upload,
and deployment in their owning workflows.

Third-party GitHub Actions must use a full 40-character commit SHA. Retain the release-major
comment beside the SHA so review remains readable, and let Dependabot propose both Actions and
Python dependency updates. A dependency PR must still pass the shared gate and be reviewed for
release notes, compatibility, provenance, and unexpected transitive changes; an automated PR
is not approval to merge.

## Manual execution

Run **Actions → Check certification objectives → Run workflow** after:

- A GitHub product announcement
- A Microsoft Learn blueprint update
- A guide revision
- An exam scheduling decision

## Local tests

```bash
python3 -m unittest discover -s tests -v
```

The live download may be run locally when the configured official sites are reachable:

```bash
python3 scripts/check_official_study_guides.py --write
```

For a reviewed provider wave, repeat `--exam-code` to refresh only the selected
records before running the full dry-run monitor:

```bash
python3 scripts/check_official_study_guides.py --write \
  --exam-code 1Z0-1085-26 --exam-code 1Z0-1072-26
```

Refresh the approved source-health baseline only after reviewing its findings:

```bash
python3 scripts/check_source_health.py \
  --report source-health-report.json \
  --markdown-report source-health-report.md

# Review both reports, then deliberately update the baseline.
python3 scripts/check_source_health.py --write
```

Automated title and duration detection is a change signal, not proof that the library metadata is wrong. Dynamic pages and regional variants require judgment.

## Review checklist for an objective-change PR

- [ ] Confirm the extraction is genuine and not page-navigation noise.
- [ ] Record the new skills-version, exam version, or tested-product baseline.
- [ ] Check whether the page announces a future update or retirement and update the guide status line.
- [ ] Update the affected guide’s objective map and any provider-published weights; do not invent weights for unweighted blueprints.
- [ ] Add or remove technical coverage.
- [ ] Recheck all product names, paths, permissions, and preview status.
- [ ] Update labs and readiness checklist.
- [ ] Verify links against the relevant provider's official blueprint and product documentation.
- [ ] Run tests and inspect Markdown rendering.
- [ ] Merge the snapshot and guide changes together when practical.

## Optional Copilot-assisted maintenance

An objective-change issue can be assigned to a configured coding agent to prepare a draft guide update. Keep human review mandatory. The agent should receive:

- The changed snapshot diff
- The affected guide path
- A requirement to use official sources
- A prohibition on invented product behavior or exam questions
- Instructions to retain **VERIFY CURRENT** labels
- Required Markdown and link validation
