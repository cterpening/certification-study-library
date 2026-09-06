# Data-assurance remediation verification — September 6, 2026

The owner's follow-up approval authorizes the bounded implementation in
[the target-specific spec](../../docs/specs/data-assurance-remediation.md).
Original assessment snapshots and persona views remain unchanged historical evidence.
The accelerator is read-only; only target files are changed. No remote settings, CI
history, branch protections, external sources or dependency registries were inspected.

## Batch 1 — catalog contracts and duplicate health records

Implementation and local verification complete on Python 3.13.14.
Committed and pushed as `4d98b19`.

- Apply all ten schemas before semantic processing, including format checks; reject
  missing catalogs and invalid schemas with diagnostics.
- Add the 27 established source categories used by 117 records to the finite schema
  enum. Do not change source records or treat arbitrary categories as valid.
- Reject duplicate health IDs in validation, and duplicate input/baseline IDs in the
  monitor before fetching. Reject duplicate newly fetched results before writing.
- Remove seven older copies across six IDs: `aws-aif-c01-bedrock`,
  `aws-aif-c01-genai-lens`, `kubernetes-v1-35-docs` (two older copies),
  `snowflake-architecture`, `snowflake-practice-exams`, `snowflake-snowpro-policies`.
  All fields except `checked_at` match their retained newest observation. The snapshot
  now has 3,248 rows and 3,248 distinct IDs. No source was fetched or revalidated;
  discarded copies remain in Git history. `generated_on` remains September 5.

Verification passed: 93 unit tests (`python -m unittest discover -s tests -v`),
`python scripts/validate_repository.py`, `python scripts/prepare_site.py`,
`python -m mkdocs build --strict --config-file .site-build/mkdocs.yml`,
`python scripts/validate_site.py`, and `git diff --check`.
The site preparer regenerated only the ignored `.site-build` directory and MkDocs
regenerated `site`; both are recoverable build output. The strict build emitted
existing navigation info and the theme's upstream compatibility notice, not a failure.

Locally mitigated findings: `repository-health:source-health:duplicate-identifiers`
and `assessment:data-contracts:uneven-schema-enforcement`. This record supplements,
and does not rewrite, the original assessment dispositions.

## Batch 2 — guide-bound AI-audit eligibility

Implementation and local verification complete on Python 3.13.14.

- Hash the complete guide text, with universal newline normalization only, and bind
  default completion keys to exam code, blueprint hash, guide hash and rubric version.
- Require valid guide hashes in rubric-2 schema and semantic validation; advance the
  active rubric to 2 without rewriting any rubric-1 batch, finding or result.
- Preserve historical guide hashes even after later edits. Missing/invalid hashes and
  legacy rubric results cannot suppress current audit eligibility.
- Reject duplicate health rows in audit input indexing. Preserve explicit audit
  selection and the current passed source-validation prerequisite.
- The first real-data smoke test exposed a pre-existing default-queue abort on
  AZ-800's blocked review. Default manifests now retain AZ-800 and AZ-802 as explicit
  `blocked_items` while selecting from the 220 ready guides. Explicit blocked requests
  still fail; an all-blocked queue reports blockers rather than claiming coverage.

Verification passed: all 105 unit tests, repository validation, site preparation,
strict MkDocs build, generated-site validation and whitespace checks, using the same
commands as batch 1. Regressions exercise guide-only changes, unchanged text,
CRLF/CR/LF equivalence, whitespace edits, blueprint/rubric changes, explicit selection,
legacy/malformed bindings, schema and semantic enforcement, mixed/all-blocked queues,
and source-gate bypass rejection.

Read-only CLI smoke test:
`python scripts/prepare_ai_audit_batch.py --batch-id remediation-smoke-2026-09-06 --size 10`
returned rubric 2, ten items with valid guide hashes, and the two named source-gate
blockers. No manifest file or completed audit was written. Git comparison confirmed
all four historical batches and 39 results are unchanged; only the active top-level
rubric version changed in `data/ai-audits.json`.

Locally mitigated finding: `assessment:ai-assurance:guide-content-not-bound`.

## Current follow-up status and limitations

Three of the nine consolidated assessment concerns are locally mitigated by these
two batches. The original dated assessment JSONs/reports remain historical snapshots;
this record supplies implementation evidence rather than rewriting their earlier state.

Two concerns remain open: assurance coverage and missing manual accessibility evidence.
These changes are not a
new security scan, live source review, accessibility attestation or remote CI assessment.
No new independent or human audit has been performed: 39 historical rubric-1 results
remain, zero rubric-2 results exist, 220 guides are ready for audit preparation and two
remain source-gate blocked. Security-boundary remediation is the next bounded code pass;
independent guide audits should resume in small batches, without bypassing source gates.

## Batch 3 — outbound public-HTTPS enforcement

Implementation and local verification complete on Python 3.13.14.

- Add one shared URL policy for both network-capable monitors. Reject non-HTTPS schemes,
  embedded credentials, localhost, non-public literal IP addresses, and non-default HTTPS
  ports before calling the opener; validate every final redirect as well.
- Restrict objective-monitor redirects to the configured host or its `www` equivalent.
  Preserve cross-host redirect observation in source-health monitoring while still requiring
  the final destination to be public HTTPS.
- Preserve injected openers in source-health tests and close a response when redirect
  validation fails.
- Add negative tests proving unsafe initial URLs never reach the opener and unsafe or
  unapproved redirects fail closed.

The 44 focused monitor tests passed. A local Bandit 1.9.4 rescan of `scripts\`, excluding
the separately open B101 rule, returned no findings; the single urllib call carries a
targeted B310 suppression immediately after the explicit policy guard. The original raw
September 5 scanner artifact remains unchanged historical evidence.

Locally mitigated finding: `bandit:B310:scripts-check-official-study-guides:urlopen`.

## Batch 4 — durable source-health report contracts

Implementation and local verification complete on Python 3.13.14.

- Replace both production assertions in `check_source_health.py` with explicit mapping
  checks and precise `ValueError` diagnostics. The checks remain active under Python's
  optimized execution mode.
- Use guarded access for the report summary and findings so missing or wrong-shaped
  internal results fail at the reporting boundary.
- Add negative tests for both malformed structures.

The focused source-health tests and all 110 repository tests passed. Bandit 1.9.4 then scanned all production scripts
with no skipped rule and returned no findings. The test-loader assertions remain the
previously triaged non-production false-positive group; the historical scanner artifact
is unchanged.

Locally mitigated finding: `bandit:B101:scripts-check-source-health:assert`.

## Batch 5 — shared delivery gate and dependency governance

Implementation and local verification complete on Python 3.13.14.

- Replace the duplicated validation and Pages command sequences with one repository-local
  composite action. Workflow-specific triggers, permissions, Pages configuration, artifact
  upload, and deployment remain in their owning workflows.
- Add explicit Python setup and pinned dependency installation to the scheduled objective
  monitor so its full test-suite invocation is reproducible on a fresh runner.
- Pin every external action reference in all four workflows and the composite action to the
  exact commit behind its existing major tag. The tag-to-commit values were checked with
  read-only `git ls-remote` queries immediately before editing.
- Add weekly pip coverage to Dependabot alongside GitHub Actions, with Python updates grouped
  for one coherent compatibility review.
- Add three local contract tests that reject duplicated gate commands, mutable external action
  references, or loss of either dependency ecosystem.

All six workflow/action/dependency YAML files parsed locally. The three focused workflow tests
and repository validation passed. Remote Actions execution, branch protections, Dependabot
behavior, and Pages deployment remain provider-state evidence to confirm after push.

Locally mitigated finding:
`repository-health:ci:duplicated-validation-and-partial-update-coverage`.

## Batch 6 — canonical objective-adapter registry

Implementation and focused local verification complete on Python 3.13.14.

- Extract provider registration metadata and its consistency rules from the central validator
  and monitor into `scripts/objective_adapter_registry.py`.
- Require the monitor's implementation map to exactly equal the canonical registry at import
  time; missing and unregistered implementations now fail closed before any network request.
- Require all vendor assignments to use the canonical registry, require every registered
  adapter to have a vendor assignment, and validate the generated documentation block during
  normal repository validation.
- Replace the nine-entry documentation subset and obsolete “both” wording with the complete
  25-adapter inventory covering all 26 vendor catalog entries.
- Add focused regression tests for implementation mismatch and documentation/catalog drift.

The 64 focused adapter, monitor, and repository-validation tests passed, as did repository
validation. The historical finding snapshots remain unchanged.

Locally mitigated finding:
`repository-health:maintainability:automation-concentration`.

## Batch 7 — retained accessibility baseline

Automated and browser evidence is recorded in
`ADLC_Docs/quality/2026-09-06-accessibility-evidence.md`.

- Expand the generated-site validator from H1/skip-link coverage to document language and title,
  main landmarks, working skip targets, unique IDs, image alternatives, enabled form-control and
  button names, and table headers.
- Add a focused regression fixture that independently breaks each new structural rule.
- Validate all 290 generated HTML pages successfully.
- Use Microsoft Edge 152.0.4191.66 and browser device emulation to render the homepage, catalog,
  a short guide, and a long guide at 320, 768, 1024, and 1440 CSS pixels across light/dark
  preferences. All four reported exact requested widths, one main landmark, one H1, and no
  document-level horizontal overflow.

This is a **partial mitigation**, not closure of
`repository-health:accessibility:manual-evidence-gap`. NVDA was unavailable, and no human
keyboard, screen-reader, zoom, contrast, print, or reduced-motion session was performed. The
retained record labels every missing check explicitly rather than inferring conformance from
static or headless evidence.

### Best-effort evidence follow-up — SSH Direct

At the owner's direction, a September 6 network-enabled research pass expanded beyond
the earlier official-source-only scan. Twenty exact sources are now in the candidate
inbox: the initial seven plus thirteen distribution and upstream follow-up sources. A public
evidence/confidence/validation matrix was added at
`docs/SSH-DIRECT-EVIDENCE.md`. The AZ-800 and AZ-802 guides now explain the provisional
Hyper-V/VSOCK/OpenSSH model and a safe versioned validation plan. No candidate was
promoted, no lab was run, and neither blocked review nor historical audit result was
changed. The source gap is better bounded but remains open pending candidate review and
reproduction on a current supported host/guest combination or stronger Microsoft guidance.

The expanded page separates observations for Debian, Ubuntu, RHEL, CentOS Stream, Fedora,
SLES/openSUSE, and Oracle Linux into kernel transport, SSH/socket packaging, security
policy, and verified end-to-end behavior. The general source policy now states that
repository research and validation are always best effort: provide the strongest bounded
useful answer, document discrepancies and unavailable evidence, and retain the gap until
stronger evidence or reproducible validation resolves it. No distribution was marked
supported and no runtime result was inferred from component availability.
