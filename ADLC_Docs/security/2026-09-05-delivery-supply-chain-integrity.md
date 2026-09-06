# Delivery and Supply-Chain Integrity Report

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-delivery-supply-chain-integrity.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

Local workflow and package declarations at the source revision; no specific release window or release candidate was supplied.

## Control assessment

| Domain | State | Evidence / risk | Required decision |
|---|---|---|---|
| Pipeline hardening | Partial | Validation and Pages repeat four checks; deploy separates permissions and excludes PR publication | Centralize verification without weakening it |
| Branch protection | Not assessed | CONTRIBUTING/AUTOMATION state review intent; remote rules absent | Obtain protection/required-check evidence |
| Artifact provenance | Not assessed | Pages upload/deploy references visible; no retained attestations/signature proof | Define and retain appropriate build-to-revision evidence |
| SBOM coverage | Not assessed | No supplied SBOM or transitive lock | Inventory dependencies before making completeness claims |
| Dependency health | Partial | Three site pins plus Bandit pin; action-only Dependabot | Govern pip updates and action references |
| Runtime support | Unknown | Python 3.13 in main validation workflows; current support sources not queried | Verify against approved lifecycle evidence |

## Setup and privilege observations

The objective-monitor workflow runs the complete test suite on runner-provided Python without declaring setup-python or installing requirements-site.txt. That differs from the validation workflows, whose suite includes schema-dependent tests. A fresh runner's outcome is unverified; this is a reproducibility concern linked to the shared CI finding. Write permissions in the monitor are used for snapshot branches, issues and PRs; no pull-request trigger is declared there.

## Remediation backlog

Assessment recommendations only—no backlog candidates or work items created. Review shared validation/setup, pip update coverage and an action-reference policy first; verify both validation and deployment use the intended gate. Owner: delivery maintainer; due date unspecified. Remote provenance and enforcement remain separate evidence requests.

## Canonical findings

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

## Limitations and next decision

Remote branch protections/rulesets, required checks, Pages environment settings, successful CI/deploy history, provenance, SBOMs, package advisories and current support evidence remain unavailable. A successful assessment commit/push is not CI/deployment verification.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

