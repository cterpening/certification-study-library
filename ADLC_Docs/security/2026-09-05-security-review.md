# Static Security Review

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-security-review.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope and outcome

The current source, publication boundary, monitoring workflows and Bandit evidence were reviewed. Two open Bandit concerns remain reviewable; no remediation or scanner execution occurred. No Build specification was supplied, so this is the catalog's static security assessment rather than a release security sign-off.

## Security domains

| Domain | Observed evidence | Conclusion / limit |
|---|---|---|
| Credentials | GitHub runtime token references and Oracle guest-token flow | Values were not read or retrieved; full inventory remains partial |
| Data boundary | Public-content policy; explicit site allowlist and containment checks | Private overlays and arbitrary documentation are excluded from site preparation |
| Input/injection | URL opening; JSON parsing; resolved publication sources | URL scheme/host/redirect policy needs review; no deployed exploit established |
| AuthN/AuthZ | Workflow-scoped permissions; Pages deploy job permissions | No owned user-authentication API or database; remote protection enforcement unknown |
| Dependencies | Exact direct package pins; mutable action references | Advisory/support/license state unknown without current approved sources |
| Output/exposure | Public metadata reports and error text | Redaction across all error/redirect responses not demonstrated; no exposed secret was observed |

## URL-boundary interpretation

The generic fetch and Oracle helper construct outbound requests from catalog URLs. Repository URL validation permits HTTP/HTTPS, but it is not an in-function enforcement rule or redirect/host proof. The source-health command also uses an injected opener, so Bandit's three direct-call hits are not complete coverage of every network boundary. Review shared scheme/host/redirect behavior; do not interpret B310 as demonstrated exploitation.

## Prioritized handoff

First review permitted outbound destinations and whether public-only retrieval is enforced at every call boundary. Then review durable runtime contract checks and supply-chain/CI setup. There is no PHI or cloud workload evidence requiring healthcare or Azure deployment controls here.

## Canonical findings

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

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

## Limitations and next decision

No exploitation, active network test, historical secret scan, dependency-advisory query or provider-settings collection was performed. Bandit is September 5 retained evidence. Healthcare/cloud governance examples are not applicable requirements for this public static library.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

