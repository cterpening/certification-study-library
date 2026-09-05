# Automation and maintenance

## Certification discovery inventory

`config/certification-seeds.json` records the official catalog URL, explicit
selection rule, and last verification date for each discovery scope. Repository
validation checks its structure, requires every published guide to remain in the
inventory, and prevents `CERTIFICATIONS.txt` from drifting from it.

The repository does not yet run a live catalog-set comparison on a schedule.
Until that monitor is implemented, the `last_verified` values represent a human-
reviewed baseline rather than a promise of continuous freshness. The intended
weekly check will report additions, removals, exam-code changes, and lifecycle
changes for review; it will not silently add guides or rewrite the catalog.

## Objective monitoring

The repository’s weekly objective workflow monitors the official objective page for every configured exam. It selects the adapter registered for that exam's provider in `data/vendors.json`, stores normalized objective and exam-status snapshots under `data/objective-snapshots`, and proposes changes through a pull request.

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

No PAT or external API key is required. The workflow uses the repository-scoped `GITHUB_TOKEN`.

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
