# Secret & Key Inventory — Local Static Evidence

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-secret-key-inventory.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Summary

Two credential mechanisms are declared in local code/workflows; zero literal credentials were established. A filenames/counts-only search found zero matches for private-key headers, common GitHub token prefixes and AWS access-key ID shapes in tracked non-ADLC content. No root `.env` was present; no tracked `.env`, PEM, private-key or PFX path was returned by the filename inventory. These observations do not establish a secret-free repository.

## Inventory

| Mechanism | Type / storage | Consumers and projection | Rotation / expiry | Risk evidence |
|---|---|---|---|---|
| GitHub job token | Platform-issued runtime token; referenced as `github.token` | Monitoring issue/PR commands receive `GH_TOKEN`; checkout/deploy use action defaults | Provider-managed details not queried | Contents/issues/PR write declarations observed; actual scope/protection unknown |
| Oracle MyLearn guest token | Temporary in-memory value parsed from guest redirect | Objective monitor sends Authorization header for public page data | Docstring states short-lived; lifetime and revocation unverified | No literal token observed; URL/redirect boundary covered by B310 |

No secret values, hashes of secret values or credential-bearing URLs are retained. There is no observed application Key Vault, managed identity, Kubernetes secret or certificate store; those inventory categories are not applicable to the visible workload.

## Findings

The three historical B105 numeric fixture observations remain false positives: passing-score and status counts are not credentials. The raw record is preserved, and no suppression or source change was applied. Unknown rotation evidence was not converted into a fabricated high/low risk score.

## Recommendations

Review whether credential-bearing request and error paths redact temporary tokens. Supply provider-scoped secret/rotation evidence only if a full inventory is requested. Continue preserving the public-only content policy and scan scope boundaries.

## Canonical findings

### Numeric test fixtures trigger password-name heuristics without credentials

- Fingerprint: `bandit:B105:tests:numeric-fixtures`; low severity, medium confidence; disposition: false-positive.
- Observation: Bandit reported three B105 observations on numeric values in test fixtures. One value is an exam passing-score count, and two are aggregate pass-status counts. They are neither strings nor credentials and cannot grant access, so the observations are heuristic false positives.
- Evidence: `ADLC_Docs/security/2026-09-05-bandit-raw.json#B105`; `tests/test_check_official_study_guides.py:43`; `tests/test_validate_repository.py:280`; `tests/test_validate_repository.py:281`.
- Proposed action: No security remediation is indicated; retain the triage and use narrowly scoped scanner annotations only if recurring noise obscures actionable findings.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

The limited current-checkout indicator search is not a comprehensive secret scanner or Git-history review. Remote secret stores, rotation/audit state, provider token scopes and expiry were not queried; credential values and ignored environment contents were excluded.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

