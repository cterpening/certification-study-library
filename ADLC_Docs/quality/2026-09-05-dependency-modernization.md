# Dependency Modernization Assessment

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-dependency-modernization.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Decision summary

Modernization posture: **proceed after evidence**, with exact target selection blocked. Highest lifecycle/vulnerability concern: unknown, because current official support/advisory evidence is unavailable. License review need: unknown. First bounded step is a governed dependency inventory and reproducible test/build baseline, not a guessed upgrade.

## Evidence coverage and limitations

Direct declarations and CI references are observed. Transitives, current installed/deployed versions, support windows, advisories, licenses, compatibility matrices and rollback exercises remain unknown. Historical Bandit is source analysis, not a dependency vulnerability audit.

## Inventory summary

| Class | Observed declaration | Version provenance | Limitation |
|---|---|---|---|
| Runtime | Python 3.13 in validation/source-health/Pages setup | Workflow intent | Objective workflow uses runner default; deployed patch unknown |
| Site/build packages | jsonschema 4.26.0, MkDocs 1.6.1, MkDocs Material 9.7.7 | `requirements-site.txt` | Direct pins; transitives unrecorded |
| Security tooling | Bandit 1.9.4 | `requirements-security.txt`; prior install record | Separate local scanner environment; not a dependency-audit pass |
| Actions | checkout, setup-python, artifact and Pages actions | Major-version refs in four workflows | Mutable refs; remote resolved commits unknown |
| Containers / IaC / database | None declared in bounded inventory | Local file inventory | Not applicable here |

## Component identity coverage

All dependency classes: **needs-evidence**. The validated facts contain no component keys, so no modernization-specific identities were minted. The names/versions above are manifest observations only; they are not substituted for canonical componentKey fields.

## Support-lifecycle decisions

Every current dependency/runtime support state is **unknown** pending dated official evidence. No target version is recommended. The approved install's historical Bandit version does not establish current support for every package.

## Vulnerability and license decisions

No advisory or exploitability claim is established. No licensing obligations or legal verdict are inferred from package names. The shared CI/update-coverage finding is a governance/maintenance concern, distinct from demonstrated vulnerability.

## Compatibility and blast radius

A change to Python/jsonschema affects validation; a MkDocs/Material change affects generated navigation/theme/build; action changes affect delivery and monitoring. Exact compatibility is unproven without canonical inventory and a current build/test baseline. Verify consumers separately from package version selection.

## Sequenced modernization plan

| Proposed sequence | State | Entry evidence | Verification / rollback | Owner |
|---|---|---|---|---|
| Inventory and baseline | needs-evidence | Canonical component keys, transitives, support policy | Validate facts; retain reproducible existing pins/results | Automation maintainer |
| Update governance | human-decision-required | Agreed pip cadence/action-reference policy | Check PR and deployment parity; restore prior configuration if needed | Delivery maintainer |
| Compatible package changes | blocked | Official supported target and compatibility evidence | Targeted tests plus strict site build; revert pins/artifact | Automation maintainer |
| Major transitions | blocked | Separate rationale, consumers and rollback plan | Isolated acceptance/recovery evidence | Repository owner |

No unrelated major transitions, upgrades or target-platform decisions are bundled into this assessment.

## Blocked decisions and evidence requests

Request corrected component-inventory evidence before exact dependency correlation. Support/vulnerability/license conclusions need approved dated sources; a fresh build and compatibility evidence are needed before selecting an upgrade. These are evidence requests, not instructions to access a registry now.

## Proposed findings and handoff

Reuse the canonical CI/dependency governance concern. It covers missing pip update automation, mutable action references and duplicated gate definitions; its existence does not prove any installed package is vulnerable.

## Assumptions, exclusions, and re-run triggers

Re-run after manifest/runtime change, canonical component inventory, new advisory/license evidence or an approved target decision. No installed dependency was added, removed or resolved during this pass.

## Canonical findings

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

## Limitations and next decision

Validated repository facts use contract 1.1.0 but contain no componentInventory. Exact component-key correlation therefore needs evidence. No registry/advisory/license/support lookup, package resolution or installed/deployed inventory was performed.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

