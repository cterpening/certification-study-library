# Cloud-Neutral Architecture Quality Review

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-architecture-quality-neutral.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

One public static-content repository, Python automation and MkDocs publication. Cloud overlays: none applicable; cloud certification subjects do not imply deployed Azure/AWS/GCP/IBM resources. Architecture-decision questions reference the ADR debt-review categories already used in documentation readiness; no second ADR score or lifecycle decision is produced.

## Pillar assessment

| Pillar | Result | Evidence | Provider overlay note |
|---|---|---|---|
| Reliability | Partial | Reviewed snapshots, Git history, validation and documented failure handling; duplicate health identity remains | No owned provider workload |
| Security | Partial | Allowlisted site preparation and public-only policy; outbound URL checks require review | Remote GitHub controls unavailable |
| Cost efficiency | Not assessed | Static artifact shape observed; usage/billing/cost goals absent | No provider sizing or savings claim |
| Operational excellence | Partial | Versioned runbooks and four workflows; duplicated gate and adapter drift | Actual workflow operation unknown |
| Performance efficiency | Partial | Historical Lighthouse summary in accessibility docs; no fresh benchmark or capacity target | No throughput/capacity guarantee |

## Findings

The canonical concentration, duplicate identity and CI drift concerns affect shared architectural responsibilities. Preserve public-source and generated-output boundaries. Evaluate cohesive module extraction and consumer compatibility only under a later approved change.

## Architecture decision limits

No approved target platform, deployment change or modernization specification is inferred. Current-state architecture is sufficient to locate review boundaries, but not to claim tested recovery, measured operational maturity or conformance of live services.

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

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

## Limitations and next decision

No owned cloud infrastructure, runtime availability/capacity evidence, cost baseline or recovery rehearsal was supplied. The diagram and workflow files describe local architecture intent, not verified deployed state.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

