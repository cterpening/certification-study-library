# Component Change-Risk Map

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-component-change-risk-map.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Decision summary

First review: catalog validator and objective monitor, because larger local modules, more observed changes and shared consumers co-occur. Review the site generator next for its publication boundary. No probability, composite score or people/team-productivity conclusion is produced.

## Component boundaries and exclusions

Seven local components were compared: validator, objective monitor, source-health monitor, site preparation, audit preparation, freshness preparation and workflow definitions. Paths are the six corresponding scripts and `.github/workflows/`. Boundaries derive from the architecture map. Guides, large data/snapshot files, generated site output, dependencies, fixtures and ADLC reports are excluded from size/churn comparison. Remaining scripts are unmapped by this bounded sample.

## Method, coverage, and comparability

Git 2.55.0.windows.5: local `git log` through revision `858bdfc`, UTC window 2026-08-07 inclusive to 2026-09-07 exclusive, limited by that existing revision; count commits touching each path and sum numeric `--numstat` additions/deletions. Denominator is seven selected components, not the entire repository. Windows PowerShell text-line counts are physical-line proxies; no complexity analyzer was executed. Initial additions and bulk edits remain included; no rename-following normalization or causal claim.

## Component signal map

| Component | Criticality context | Churn / complexity | Centrality | Ownership continuity | Test gaps / attention |
|---|---|---|---|---|---|
| Validator | Catalog integrity | Elevated relative / 1,903 lines | Reads most catalogs; shared publication gate | Unknown | Duplicate-ID and schema parity concerns; first |
| Objective monitor | Blueprint evidence | Elevated relative / 2,202 lines | 26 routes and upstream source evidence | Unknown | Parser tests present; live and URL-boundary behavior unverified; first |
| Source health | Evidence freshness | Lower relative / 488 lines | Sources → health → reviews/preparers | Unknown | Four fixture tests; duplicate downstream handling gap |
| Site preparation | Public publication | Watch relative / 844 lines | Many catalogs → allowlisted site | Unknown | Allowlist fixtures present; rendered/browser evidence partial |
| Audit preparation | Assurance selection | Lower relative / 359 lines | Guide/blueprint/review → audit handoff | Unknown | Guide-content invalidation missing |
| Freshness preparation | Recurrence | Lower relative / 451 lines | Guide/source baseline → freshness handoff | Unknown | Hash and chronology cases present; current run unavailable |
| Workflows | Delivery/monitoring | Lower relative / no combined size metric | Build, publication and issue/PR orchestration | Unknown | Repeated gate definitions; remote runs unknown |

## Change-churn evidence

| Path/component | Commits touching path | Added lines | Deleted lines | Current physical lines |
|---|---:|---:|---:|---:|
| Validator | 33 | 1,946 | 43 | 1,903 |
| Objective monitor | 31 | 2,312 | 110 | 2,202 |
| Source-health monitor | 2 | 494 | 6 | 488 |
| Site preparation | 15 | 923 | 79 | 844 |
| Audit preparation | 1 | 359 | 0 | 359 |
| Freshness preparation | 1 | 451 | 0 | 451 |
| Workflows | 4 | 264 | 0 | Not aggregated |

A commit touching multiple paths is counted once per path, so counts are not additive unique repository commits. Initial code creation materially contributes to line totals.

## Complexity evidence

Only physical size was measured. The two largest scripts are elevated relative to the other selected scripts; this is not cyclomatic or cognitive complexity. Parser branching, dependency depth and nesting were not quantified.

## Dependency-centrality evidence

Direction: catalogs/guides → validator and site preparation; source/blueprint snapshots → audit/freshness preparers; workflows invoke validation/build/monitor scripts. The validator and site generator have broad data fan-in. Runtime/API edges, numeric graph degree and external consumers remain incomplete. The observed local cross-script import is assessed in the optional component view.

## Ownership-continuity evidence

Owner roles are proposed as automation, content-assurance and delivery maintainers. No CODEOWNERS or approved path-owner matrix was supplied. No contributor names/emails were collected, teams inferred or small cohorts published; continuity is unknown for every component.

## Test-gap evidence

Match each selected script to its corresponding `tests/test_*.py`; workflow definitions have no equivalent locally executed end-to-end proof. Prior test results are September 5 historical evidence. Test proximity/count is not behavioral coverage; the canonical integrity and audit-binding findings identify specific missing cases.

## Privacy and responsible-use review

Only paths, numeric aggregates, a source revision and tool versions were retained. Identity processing was omitted entirely, so cohort suppression is not applicable. Raw author/message/branch/PR fields were excluded. These signals must not be used for individual ranking, competence or staffing judgments.

## Missing or blocked evidence

Current runtime coverage, declared owners and complete directional consumer mapping would refine attention ordering. No incident, defect-rate or elapsed-delivery prediction is made. Repository owner can supply a role map; automation maintainers can supply repeatable critical-path evidence.

## Proposed findings and improvements

Preserve the existing concentration, duplicate-identity, audit-binding and CI-drift fingerprints. Stage any later extraction behind contract/CLI tests. Qualitative attention uses co-occurring signal evidence rather than multiplying churn, size and ownership into a score.

## Assumptions, exclusions, and re-run triggers

Re-run after structural moves, consumer changes, new coverage or owner evidence, or expiry of the comparison window. Historical Git availability and unnormalized bulk changes constrain comparisons.

## Canonical findings

### Core validation and monitoring logic is concentrated in two large modules

- Fingerprint: `repository-health:maintainability:automation-concentration`; medium severity, high confidence; disposition: open.
- Observation: The repository validator and official-study-guide monitor are each approximately two thousand physical lines, with provider routing centralized in the monitor. The adapter README lists nine adapters while the implementation routes 26 adapter keys, so the discoverable extension inventory already trails the code. This concentration increases review load and makes provider additions more likely to create code/documentation drift.
- Evidence: `scripts/validate_repository.py`; `scripts/check_official_study_guides.py`; `adapters/README.md`.
- Proposed action: Split stable validation and provider-routing responsibilities into focused modules and generate or validate the adapter inventory from the canonical registry.
- Proposed owner: repository automation maintainers; due date not supplied.

### Source-health rows are not unique by source identifier

- Fingerprint: `repository-health:source-health:duplicate-identifiers`; medium severity, high confidence; disposition: open.
- Observation: The source-health ledger contains 3,255 rows for 3,248 registered source IDs. Six IDs are duplicated, including one ID with three rows. The current repository validator reduces health rows to a dictionary keyed by ID before comparing coverage, so duplicates are overwritten and the validator still passes. This can distort aggregate reporting and makes duplicate records invisible to the main consistency gate.
- Evidence: `data/source-health.json`; `scripts/validate_repository.py`; `test.result.repository-validator`.
- Proposed action: Canonicalize source-health output to one record per source ID and make duplicate IDs a schema or repository-validation failure.
- Proposed owner: repository automation maintainers; due date not supplied.

### A guide-only change does not invalidate the default AI-audit completion key

- Fingerprint: `assessment:ai-assurance:guide-content-not-bound`; medium severity, high confidence; disposition: open.
- Observation: completed_current_audits and select_batch key completed work by exam code, blueprint snapshot hash and rubric version. The schema does not bind the result to guide content. Consequently a changed explanation or lab can remain excluded from default selection while its blueprint is unchanged. This is inferred from the key and selection condition; no runtime re-audit was executed.
- Evidence: `scripts/prepare_ai_audit_batch.py:60`; `scripts/prepare_ai_audit_batch.py:236`; `schemas/ai-audit-catalog.schema.json`; `tests/test_prepare_ai_audit_batch.py:43`.
- Proposed action: Bind future audit results and default selection to the reviewed guide revision or content digest.
- Proposed owner: repository automation maintainers; due date not supplied.

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

## Limitations and next decision

Identity/contributor analysis was not performed. Declared path ownership, current behavioral coverage, rename-normalized longitudinal comparison and external consumers are unavailable; size and churn do not predict defects.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

