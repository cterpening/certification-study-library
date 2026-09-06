# Application Style & Conformance Report

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-application-style-conformance.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

Profile: discovery-derived content/static site, using frontend-application only as the closest reference. Standards: accelerator `config/application-standards-contract.json`; rule source: `config/application-standards/style-conformance-rules.json`. Repository policy and current unittest/pip conventions take precedence. These reference rules do not authorize framework/tooling migration.

## Summary

Six rules considered: five applicable, zero full passes, zero demonstrated rule failures, zero accepted exceptions, five blocked/insufficient evidence; one not applicable. Blocked means required evidence is missing, not that a control failed. No numerical conformance score is assigned.

## Rule results

| Rule ID | Domain | Applicability | Severity | Result | Evidence / missing proof | Exception |
|---|---|---|---|---|---|---|
| arch-boundary-contracts | Module boundaries | Applicable | High | blocked | Architecture map and site allowlist observed; comprehensive dependency-direction enforcement not demonstrated | None |
| contract-versioning | API/event contracts | Not applicable | Critical | not applicable | No owned API/event contract; JSON catalog compatibility assessed separately | None |
| secure-config-separation | Configuration | Applicable | High | blocked | Content policy, config, workflows and Bandit visible; no complete historical secret inventory/provider settings | None |
| telemetry-evidence | Logging | Applicable to maintenance commands | Critical | blocked | Structured source reports exist; safe telemetry across error/redirect paths not demonstrated | None |
| test-coverage-behavioral | Testing | Applicable | High | blocked | Tests and prior 84-test result exist; critical gaps and fresh full gate remain unverified | None |
| accessibility-baseline | Accessibility | Applicable | High | blocked | Manual checklist lacks results; HTML structure tests alone insufficient | None |

## Findings generated

No additional failed-rule finding was invented from missing evidence. Reuse the existing accessibility-evidence finding. Data-contract, test and security concerns retain their own canonical findings in companion reports.

## Exceptions

None supplied or accepted. Owner, rationale, scope, review/expiry date, compensating controls, approval reference and ADR linkage would be required for any future exception. Preserving repository conventions over conflicting profile defaults is precedence, not a fabricated exception.

## Notes

A preliminary lookup for a generic report-portfolio configuration returned no file. The prompt explicitly routes to the standards-contract and style-conformance-rules files, which were then read successfully; no rule coverage was lost.

## Canonical findings

### Accessibility verification has no recorded completion evidence

- Fingerprint: `repository-health:accessibility:manual-evidence-unrecorded`; low severity, high confidence; disposition: open.
- Observation: The repository provides a concrete nine-item manual accessibility checklist, but every item remains unchecked. The local CI definitions validate generated structure and links but do not record keyboard, screen-reader, zoom, responsive, contrast, print, or reduced-motion results. This is an evidence gap, not a finding that the site itself fails accessibility requirements.
- Evidence: `docs/ACCESSIBILITY.md`; `.github/workflows/validate-repository.yml`.
- Proposed action: Execute the documented manual accessibility matrix against a representative site build and retain dated evidence, automating only repeatable checks that complement rather than replace assistive-technology review.
- Proposed owner: site maintainers; due date not supplied.

## Limitations and next decision

Five applicable reference rules lack enough combined implementation/runtime evidence for a full pass. No approved standards-exception registry or modernization specification was supplied; frontend rules are mapped selectively to the observed static-site application.

A recovered configuration lookup error is recorded in the finding set; the correct rule sources were subsequently read. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

