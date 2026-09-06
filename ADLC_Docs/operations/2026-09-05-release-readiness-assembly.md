# Release Readiness Assembly Report

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-release-readiness-assembly.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

Release candidate: **not supplied**. Evidence baseline: source revision `858bdfc`, validated September 5 repository facts/health/Bandit, and the September 6 assessment waves at their approved September 5 filenames. Existing tags v0.1.0 and v0.1.1 are local references, not proof of a requested or deployed release.

## Readiness decision

Recommendation: **hold release sign-off pending a named candidate and current verification evidence**. This is not a conclusion that the existing published site must be stopped. Assessment completion does not establish that findings were repaired, accepted or verified.

## Decision factors

| Signal | State | Evidence | Action required |
|---|---|---|---|
| Critical unresolved findings | None recorded in bounded normalized set | Canonical finding collection | Do not equate limited coverage with absence of unknown critical issues |
| Open findings | 9 unique: 1 high, 6 medium, 2 low | Deduplicated fingerprints; includes prior health/Bandit | Review disposition and release impact |
| False-positive triage | 2 historical Bandit groups | Bandit record | Preserve evidence; not waivers for open issues |
| Blocked assessments/evidence | Remote delivery and specialist scanner lanes; several runtime domains | Assessment decisions and report gaps | Supply evidence only within newly approved scope |
| Freshness | Source unchanged across baseline except docs/security pin; test/build/browser evidence historical or absent | Local Git diff, dated artifacts | Verify candidate-specific checks |
| Waiver validity | Unknown; no register supplied | No risk-acceptance evidence | Do not invent approval from this assessment |
| Artifact/deployment identity | Unknown | Workflow intent only | Link candidate revision to verified artifact and deployment |
| Manifest/index | Partial substitute | Action plan and decisions enumerate reports | Supply formal release input if required by release governance |

## Follow-up actions

| Priority | Action | Owner | Due date | Exit criteria |
|---|---|---|---|---|
| 1 | Name the release candidate and review nine unique open concerns | Release/repository owner | Not supplied | Explicit release-impact dispositions |
| 2 | Obtain candidate-specific test/build/site evidence | Automation maintainer | Not supplied | Verified current results with remaining gaps explicit |
| 3 | Record manual accessibility evidence | Site maintainer | Not supplied | Representative checklist results |
| 4 | Verify remote checks, artifact identity and rollback readiness | Delivery maintainer | Not supplied | Traceable provider evidence and recovery procedure |

No tickets, candidates, specs or waiver approvals were created. The findings are repeated here for assembly with unchanged canonical identities, not nine new discoveries.

## Canonical findings

### Independent content-assurance coverage trails the published library

- Fingerprint: `repository-health:content-assurance:coverage-gap`; high severity, high confidence; disposition: open.
- Observation: The repository contains 222 guides, while the current independent AI-audit ledger covers 39 guides and the freshness ledger covers 33. Ten AI-audit findings remain open, 61 source candidates remain queued, and no guide is marked community-reviewed. Source-validation records and automated checks cover important structural concerns, but they are not substitutes for the independent semantic and freshness layers defined by this repository.
- Evidence: `architecture.data-model.catalogs`; `data/ai-audits.json`; `data/source-freshness.json`; `data/source-candidates.json`.
- Proposed action: Continue risk-ranked independent audit and freshness batches, resolve the ten open findings, and establish an explicit human-review sampling target before treating library-wide quality as assured.
- Proposed owner: content-assurance maintainers; due date not supplied.

### Source-health rows are not unique by source identifier

- Fingerprint: `repository-health:source-health:duplicate-identifiers`; medium severity, high confidence; disposition: open.
- Observation: The source-health ledger contains 3,255 rows for 3,248 registered source IDs. Six IDs are duplicated, including one ID with three rows. The current repository validator reduces health rows to a dictionary keyed by ID before comparing coverage, so duplicates are overwritten and the validator still passes. This can distort aggregate reporting and makes duplicate records invisible to the main consistency gate.
- Evidence: `data/source-health.json`; `scripts/validate_repository.py`; `test.result.repository-validator`.
- Proposed action: Canonicalize source-health output to one record per source ID and make duplicate IDs a schema or repository-validation failure.
- Proposed owner: repository automation maintainers; due date not supplied.

### Core validation and monitoring logic is concentrated in two large modules

- Fingerprint: `repository-health:maintainability:automation-concentration`; medium severity, high confidence; disposition: open.
- Observation: The repository validator and official-study-guide monitor are each approximately two thousand physical lines, with provider routing centralized in the monitor. The adapter README lists nine adapters while the implementation routes 26 adapter keys, so the discoverable extension inventory already trails the code. This concentration increases review load and makes provider additions more likely to create code/documentation drift.
- Evidence: `scripts/validate_repository.py`; `scripts/check_official_study_guides.py`; `adapters/README.md`.
- Proposed action: Split stable validation and provider-routing responsibilities into focused modules and generate or validate the adapter inventory from the canonical registry.
- Proposed owner: repository automation maintainers; due date not supplied.

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

### Accessibility verification has no recorded completion evidence

- Fingerprint: `repository-health:accessibility:manual-evidence-unrecorded`; low severity, high confidence; disposition: open.
- Observation: The repository provides a concrete nine-item manual accessibility checklist, but every item remains unchecked. The local CI definitions validate generated structure and links but do not record keyboard, screen-reader, zoom, responsive, contrast, print, or reduced-motion results. This is an evidence gap, not a finding that the site itself fails accessibility requirements.
- Evidence: `docs/ACCESSIBILITY.md`; `.github/workflows/validate-repository.yml`.
- Proposed action: Execute the documented manual accessibility matrix against a representative site build and retain dated evidence, automating only repeatable checks that complement rather than replace assistive-technology review.
- Proposed owner: site maintainers; due date not supplied.

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

### URL-opening paths do not enforce permitted schemes at the call boundary

- Fingerprint: `bandit:B310:scripts-check-official-study-guides:urlopen`; medium severity, high confidence; disposition: open.
- Observation: Bandit reported three B310 observations in the official-study-guide monitor. The general fetch path and two Oracle guest-session requests call urllib URL opening without an explicit scheme check at those call sites. The inputs are normally official catalog URLs, but a changed or malformed catalog value can reach the fetch boundary, so the scanner cannot establish that file or custom schemes are rejected.
- Evidence: `ADLC_Docs/security/2026-09-05-bandit-raw.json#B310`; `scripts/check_official_study_guides.py:131`; `scripts/check_official_study_guides.py:1906`; `scripts/check_official_study_guides.py:1924`.
- Proposed action: Validate each outbound URL against the intended HTTPS scheme and approved host policy immediately before opening it.
- Proposed owner: repository automation maintainers; due date not supplied.

### Runtime type assumptions rely on assertions removed by optimized Python

- Fingerprint: `bandit:B101:scripts-check-source-health:assert`; low severity, high confidence; disposition: open.
- Observation: Bandit reported two B101 observations in the source-health command. Assertions guard expected dictionary shapes before rendering and output processing. Python removes assertions under optimized execution, so these checks do not provide a durable validation boundary and later operations may fail less clearly if an internal contract changes.
- Evidence: `ADLC_Docs/security/2026-09-05-bandit-raw.json#B101`; `scripts/check_source_health.py:332`; `scripts/check_source_health.py:476`.
- Proposed action: Replace production assertions with explicit contract checks that raise a precise exception or return a controlled validation error.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

No release candidate, canonical assessment manifest/report index, waiver register, current CI run or deployed artifact identity was supplied. This assembly uses the action plan, decisions, validated findings and retained baseline instead; release approval is blocked.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

