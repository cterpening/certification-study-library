# Developer Evidence Appendix — Repository Health Snapshot

## Evidence identity

- Source report: repository-health-2026-09-05
- Source status: partial
- Report mode: snapshot
- Canonical finding count: 5
- Finding-set SHA-256: `40d4db6e2eacd8c2215cbc27bedab74de9e6c27ccd93ee95c8587067da7b9ae4`

This is a presentation view of the identified finding set, not a separate assessment. It does not add findings, change dispositions, or calculate an independent score.

## Coverage

| Measure | Count |
|---|---:|
| critical findings | 0 |
| high findings | 1 |
| medium findings | 3 |
| low findings | 1 |
| info findings | 0 |
| open dispositions | 5 |
| accepted-risk dispositions | 0 |
| mitigated dispositions | 0 |
| false-positive dispositions | 0 |
| blocked dispositions | 0 |
| permission gaps | 4 |
| collection errors | 0 |

## All findings

### Independent content-assurance coverage trails the published library

- Finding ID: `repository-health:content-assurance:coverage-gap`
- Severity / confidence / disposition: high / high / open
- Source report / control: repository-health-2026-09-05 / quality.content-assurance-coverage
- Affected component: guides/ (content-assurance)
- Owner role: content-assurance maintainers

**Finding**

The repository contains 222 guides, while the current independent AI-audit ledger covers 39 guides and the freshness ledger covers 33. Ten AI-audit findings remain open, 61 source candidates remain queued, and no guide is marked community-reviewed. Source-validation records and automated checks cover important structural concerns, but they are not substitutes for the independent semantic and freshness layers defined by this repository.

**Proposed remediation**

Continue risk-ranked independent audit and freshness batches, resolve the ten open findings, and establish an explicit human-review sampling target before treating library-wide quality as assured.
- Prioritize the 183 guides without an AI-audit result and the 189 guides without a freshness result using lifecycle volatility, exam criticality, and change history.
- Resolve or explicitly disposition the ten currently open AI-audit findings before expanding lower-risk coverage.
- Define a review cadence and a bounded human community-review sample with recorded acceptance criteria.
- Verify that the ledgers reconcile to the 222-guide inventory and publish coverage counts without converting them into permanent quality labels.

**Safe evidence references**

| Type | Reference |
|---|---|
| fact | architecture.data-model.catalogs |
| file | data/ai-audits.json |
| file | data/source-freshness.json |
| file | data/source-candidates.json |

### CI validation is duplicated and dependency-update coverage is partial

- Finding ID: `repository-health:ci:duplicated-validation-and-partial-update-coverage`
- Severity / confidence / disposition: medium / high / open
- Source report / control: repository-health-2026-09-05 / operations.automation-friction
- Affected component: .github/ (delivery-maintainability)
- Owner role: delivery maintainers

**Finding**

The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.

**Proposed remediation**

Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Extract the common validation sequence into one reusable workflow or composite local action used by validation and deployment.
- Add a pip Dependabot entry for requirements-site.txt with a review cadence appropriate for the site toolchain.
- Decide and document whether third-party action references must be pinned to full commit SHAs, with an update mechanism that keeps them current.
- Verify both pull-request validation and Pages deployment consume the same validation definition.

**Safe evidence references**

| Type | Reference |
|---|---|
| file | .github/workflows/validate-repository.yml |
| file | .github/workflows/deploy-pages.yml |
| file | .github/dependabot.yml |
| fact | dependency.direct.site |

### Core validation and monitoring logic is concentrated in two large modules

- Finding ID: `repository-health:maintainability:automation-concentration`
- Severity / confidence / disposition: medium / high / open
- Source report / control: repository-health-2026-09-05 / quality.cognitive-load
- Affected component: scripts/ (maintainability)
- Owner role: repository automation maintainers

**Finding**

The repository validator and official-study-guide monitor are each approximately two thousand physical lines, with provider routing centralized in the monitor. The adapter README lists nine adapters while the implementation routes 26 adapter keys, so the discoverable extension inventory already trails the code. This concentration increases review load and makes provider additions more likely to create code/documentation drift.

**Proposed remediation**

Split stable validation and provider-routing responsibilities into focused modules and generate or validate the adapter inventory from the canonical registry.
- Identify cohesive validator domains and extract them behind unchanged command-line behavior and existing tests.
- Move provider registration metadata to one canonical registry consumed by routing and documentation checks.
- Update the adapter documentation to cover all registered adapters and replace the stale two-adapter wording.
- Verify unchanged validator outcomes and add a test that fails when adapter documentation and registry keys diverge.

**Safe evidence references**

| Type | Reference |
|---|---|
| file | scripts/validate_repository.py |
| file | scripts/check_official_study_guides.py |
| file | adapters/README.md |

### Source-health rows are not unique by source identifier

- Finding ID: `repository-health:source-health:duplicate-identifiers`
- Severity / confidence / disposition: medium / high / open
- Source report / control: repository-health-2026-09-05 / quality.source-health-uniqueness
- Affected component: data/source-health.json (data-integrity)
- Owner role: repository automation maintainers

**Finding**

The source-health ledger contains 3,255 rows for 3,248 registered source IDs. Six IDs are duplicated, including one ID with three rows. The current repository validator reduces health rows to a dictionary keyed by ID before comparing coverage, so duplicates are overwritten and the validator still passes. This can distort aggregate reporting and makes duplicate records invisible to the main consistency gate.

**Proposed remediation**

Canonicalize source-health output to one record per source ID and make duplicate IDs a schema or repository-validation failure.
- Choose and document whether source-health is a current snapshot or an append-only history; its current schema and consumers behave like a current snapshot.
- Deduplicate the six affected IDs deterministically while preserving the intended latest observation.
- Add an explicit duplicate-ID check before dictionary construction in the repository validator.
- Add a regression test with duplicate rows and verify the validator fails with a precise diagnostic.

**Safe evidence references**

| Type | Reference |
|---|---|
| file | data/source-health.json |
| file | scripts/validate_repository.py |
| fact | test.result.repository-validator |

### Accessibility verification has no recorded completion evidence

- Finding ID: `repository-health:accessibility:manual-evidence-unrecorded`
- Severity / confidence / disposition: low / high / open
- Source report / control: repository-health-2026-09-05 / quality.accessibility-evidence
- Affected component: docs/ACCESSIBILITY.md (accessibility-assurance)
- Owner role: site maintainers

**Finding**

The repository provides a concrete nine-item manual accessibility checklist, but every item remains unchecked. The local CI definitions validate generated structure and links but do not record keyboard, screen-reader, zoom, responsive, contrast, print, or reduced-motion results. This is an evidence gap, not a finding that the site itself fails accessibility requirements.

**Proposed remediation**

Execute the documented manual accessibility matrix against a representative site build and retain dated evidence, automating only repeatable checks that complement rather than replace assistive-technology review.
- Run the existing checklist against the homepage, catalog, one short guide, and one long guide.
- Record date, browser, viewport, assistive technology, outcome, and any follow-up finding without personal data.
- Add bounded automated accessibility checks for repeatable regressions if they can run within the approved tool and dependency policy.
- Verify all nine checklist areas have current evidence or an explicit blocked/accepted disposition.

**Safe evidence references**

| Type | Reference |
|---|---|
| file | docs/ACCESSIBILITY.md |
| file | .github/workflows/validate-repository.yml |

## Limitations

- Evidence references are locators only. Raw excerpts, absolute paths, sensitive URLs, resource identifiers, personal assignees, and provider payloads are excluded.
- Reproduce and verify within the approved data/tool boundary; a proposed remediation is not implementation authorization.
