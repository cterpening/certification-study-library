# Test Maturity, Coverage Quality, and Readiness Report

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-test-maturity-readiness.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

The eight test files and eight Python scripts were inspected as local evidence. The retained test baseline is 84 passing unittest tests from 2026-09-05. Git diff from the inventory source revision to this run shows assessment artifacts and the security dependency declaration only; this does not prove a fresh execution result.

## Assessment summary

| Domain | Status | Confidence | Evidence | Gap |
|---|---|---|---|---|
| Unit tests | Substantial local suite | High | `tests/`; provider parsing, freshness, audits, site and validation cases | No newly executed result |
| Integration | Partial | Medium | Temporary site fixtures and configured strict build in CI | No live-provider or current end-to-end run |
| Coverage quality | Partial | High | Negative cases for hashes, chronology and invalid states | Duplicate health IDs and guide-only audit invalidation lack regression cases |
| Mutation testing | Not assessed | High | No mutation output supplied | Mutation score unavailable |
| Contract testing | Partial | High | Schema validation for freshness plus cross-catalog checks | Other schema declarations are not uniformly enforced |
| Reliability signals | Not assessed | High | Only a retained local pass | Flaky rate and consumer/provider parity unproven |

## Improvement plan

| Priority | Action | Owner | Due date | Expected impact |
|---|---|---|---|---|
| 1 | Add duplicate-ID and schema parity cases when fixes are approved | Automation maintainer | Not supplied | Protect canonical data contracts |
| 2 | Exercise guide-only audit invalidation | Content assurance maintainer | Not supplied | Ensure changed teaching content is re-audited |
| 3 | Record representative critical paths and repeatable test evidence | Automation maintainer | Not supplied | Improve confidence without treating raw test counts as coverage |

Preserve unittest and the repository's existing test layout. Missing coverage/mutation tooling is an evidence gap, not a reason to install tooling during this assessment.

## Canonical findings

### Source-health rows are not unique by source identifier

- Fingerprint: `repository-health:source-health:duplicate-identifiers`; medium severity, high confidence; disposition: open.
- Observation: The source-health ledger contains 3,255 rows for 3,248 registered source IDs. Six IDs are duplicated, including one ID with three rows. The current repository validator reduces health rows to a dictionary keyed by ID before comparing coverage, so duplicates are overwritten and the validator still passes. This can distort aggregate reporting and makes duplicate records invisible to the main consistency gate.
- Evidence: `data/source-health.json`; `scripts/validate_repository.py`; `test.result.repository-validator`.
- Proposed action: Canonicalize source-health output to one record per source ID and make duplicate IDs a schema or repository-validation failure.
- Proposed owner: repository automation maintainers; due date not supplied.

### Declared catalog schemas are not uniformly applied

- Fingerprint: `assessment:data-contracts:uneven-schema-enforcement`; medium severity, high confidence; disposition: open.
- Observation: Only the source-freshness catalog is passed to validate_json_schema in main. The other schemas are parsed as JSON, while their catalogs rely on handwritten checks. Those checks cover many business rules but do not establish parity with every declared constraint, creating a compatibility gap when schemas evolve.
- Evidence: `scripts/validate_repository.py:1520`; `scripts/validate_repository.py:1800`; `schemas/source-health.schema.json`.
- Proposed action: Make schema-to-catalog validation explicit while retaining the cross-catalog business rules.
- Proposed owner: repository automation maintainers; due date not supplied.

### A guide-only change does not invalidate the default AI-audit completion key

- Fingerprint: `assessment:ai-assurance:guide-content-not-bound`; medium severity, high confidence; disposition: open.
- Observation: completed_current_audits and select_batch key completed work by exam code, blueprint snapshot hash and rubric version. The schema does not bind the result to guide content. Consequently a changed explanation or lab can remain excluded from default selection while its blueprint is unchanged. This is inferred from the key and selection condition; no runtime re-audit was executed.
- Evidence: `scripts/prepare_ai_audit_batch.py:60`; `scripts/prepare_ai_audit_batch.py:236`; `schemas/ai-audit-catalog.schema.json`; `tests/test_prepare_ai_audit_batch.py:43`.
- Proposed action: Bind future audit results and default selection to the reviewed guide revision or content digest.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

Fresh test execution, coverage/mutation output, CI repetition and flaky-rate evidence are outside this approved static pass. The recorded 84-test result dates from 2026-09-05; no tests were rerun.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

