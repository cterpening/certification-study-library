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

Six concerns remain open: assurance coverage, automation concentration, duplicated CI
and dependency-update gaps, missing manual accessibility evidence, Bandit B310 URL
scheme enforcement, and Bandit B101 production assertions. These changes are not a
new security scan, live source review, accessibility attestation or remote CI assessment.
No new independent or human audit has been performed: 39 historical rubric-1 results
remain, zero rubric-2 results exist, 220 guides are ready for audit preparation and two
remain source-gate blocked. Security-boundary remediation is the next bounded code pass;
independent guide audits should resume in small batches, without bypassing source gates.
