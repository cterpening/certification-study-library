# Code Quality Review

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-quality-review.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope and review outcome

Local Python automation, catalog contracts and tests. Existing source revision is unchanged from the retained baseline. Spec fidelity: **not assessed**, because this is an assessment of current code rather than a Build-to-Review transition.

## Ranked findings

| Priority | Concern | Assessment treatment |
|---|---|---|
| 1 | Duplicate health records collapse before checks | Correctness: resolve before claiming unique data identity |
| 2 | Schema declarations and validation are not uniformly connected | Correctness/compatibility: define parity before contract changes |
| 3 | Guide-only edits do not invalidate AI-audit completion | Correctness: review before claiming current guide assurance |
| 4 | Central module size and adapter-documentation drift | Maintainability: sequence extraction around preserved behavior |

These are proposed remediation priorities; none is an applied fix or an accepted risk.

## Conventions and simplification

The scripts use standard-library APIs, typed functions, pathlib and unittest. Preserve those conventions. The validator is 1,903 physical lines and the objective monitor 2,202; length is a transparent structural proxy, not a cyclomatic/cognitive score. Optional extraction of responsibilities should follow contract regression coverage rather than change CLI behavior.

## Tests and verification

Provider parsers, freshness logic, audit summaries and site boundaries have tests. The 84-test pass is retained historical evidence from September 5. No new project command was run. Missing duplicate-ID and guide-change cases are discussed in the test-readiness report.

## Security handoff

The retained Bandit URL-opening and production-assert observations are reviewed in the static security lane; no scanner was rerun.

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

### Core validation and monitoring logic is concentrated in two large modules

- Fingerprint: `repository-health:maintainability:automation-concentration`; medium severity, high confidence; disposition: open.
- Observation: The repository validator and official-study-guide monitor are each approximately two thousand physical lines, with provider routing centralized in the monitor. The adapter README lists nine adapters while the implementation routes 26 adapter keys, so the discoverable extension inventory already trails the code. This concentration increases review load and makes provider additions more likely to create code/documentation drift.
- Evidence: `scripts/validate_repository.py`; `scripts/check_official_study_guides.py`; `adapters/README.md`.
- Proposed action: Split stable validation and provider-routing responsibilities into focused modules and generate or validate the adapter inventory from the canonical registry.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

No Build diff or approved implementation specification was supplied. Spec fidelity and must-fix acceptance against a particular change are not assessable. The review prompt is used only for its cataloged static quality lane; security observations route to Wave C.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

