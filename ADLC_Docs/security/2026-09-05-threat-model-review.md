# Threat Model Review

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-threat-model-review.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Context

Method: qualitative STRIDE and misuse cases over the content → review → publication flow. Assets: trustworthy guide text, canonical source/catalog/snapshot identity, review/audit evidence, publication artifacts and transient workflow/guest credentials. Entry points: contributed Markdown/JSON, public vendor responses, dependency downloads and workflow invocations.

## Trust boundaries

1. External vendor/third-party text enters local evidence and must not become executable assistant instructions.
2. Candidate sources require review before approved-catalog promotion.
3. AI-generated explanations require source/objective checks and remain human-review pending.
4. Canonical content enters the site only through approved guide paths and document allowlists.
5. CI jobs receive scoped tokens and pass artifacts into Pages deployment; enforcement evidence is local intent only.

## Threat register

| Asset / STRIDE class | Threat | Likelihood | Impact | Existing control | Residual risk |
|---|---|---|---|---|---|
| Source retrieval / spoofing, disclosure | Catalog or redirect steers requests to an unintended scheme/host | Unknown | Wrong evidence or unintended local/network access | Public URL policy, repository checks, request timeouts | B310 boundary enforcement needs review |
| Guide/audit evidence / tampering | Guide changes while prior audit key still appears complete | Not quantified | Unreviewed explanations inherit stale assurance | Blueprint/rubric binding and separate audit ledger | Guide-content key gap |
| Generated prose / misuse | Untrusted source instructions or unsupported claims influence content | Unknown | Misleading/unsafe educational content | Official-source authority, ten-check rubric, separate repair pass | Coverage and human-review gaps |
| Publication / disclosure | Unapproved files enter the public build | Unknown | Private or working material published | Explicit allowlist, resolved paths, tests | Reviewed allowlist changes and runtime evidence still needed |
| Build / tampering, privilege | Dependency/action drift or compromised execution changes artifact | Unknown | Artifact integrity or token exposure | Direct pins, separated Pages job permissions | Mutable refs, incomplete update governance, remote controls unknown |
| Maintenance / denial of service | Remote page stalls or supplies excessive content | Unknown | Monitor delays or resource use | Timeout arguments; source-health response bound | No active resource-limit test; objective fetch bounds unverified |
| Audit / repudiation | Review claim cannot be reproduced against exact content | Not quantified | Unsupported quality assertion | Dated ledgers, hashes and dispositions | Guide-content binding and missing runtime metadata |

## Recommended actions

Review URL scheme/host/redirect rules, audit-content identity and content-assurance coverage first; then strengthen governed dependency/CI evidence. Owners are repository automation, content assurance and delivery maintainers. Due dates are unspecified. No new exploit claim, attack execution or risk acceptance is recorded.

## Canonical findings

### URL-opening paths do not enforce permitted schemes at the call boundary

- Fingerprint: `bandit:B310:scripts-check-official-study-guides:urlopen`; medium severity, high confidence; disposition: open.
- Observation: Bandit reported three B310 observations in the official-study-guide monitor. The general fetch path and two Oracle guest-session requests call urllib URL opening without an explicit scheme check at those call sites. The inputs are normally official catalog URLs, but a changed or malformed catalog value can reach the fetch boundary, so the scanner cannot establish that file or custom schemes are rejected.
- Evidence: `ADLC_Docs/security/2026-09-05-bandit-raw.json#B310`; `scripts/check_official_study_guides.py:131`; `scripts/check_official_study_guides.py:1906`; `scripts/check_official_study_guides.py:1924`.
- Proposed action: Validate each outbound URL against the intended HTTPS scheme and approved host policy immediately before opening it.
- Proposed owner: repository automation maintainers; due date not supplied.

### A guide-only change does not invalidate the default AI-audit completion key

- Fingerprint: `assessment:ai-assurance:guide-content-not-bound`; medium severity, high confidence; disposition: open.
- Observation: completed_current_audits and select_batch key completed work by exam code, blueprint snapshot hash and rubric version. The schema does not bind the result to guide content. Consequently a changed explanation or lab can remain excluded from default selection while its blueprint is unchanged. This is inferred from the key and selection condition; no runtime re-audit was executed.
- Evidence: `scripts/prepare_ai_audit_batch.py:60`; `scripts/prepare_ai_audit_batch.py:236`; `schemas/ai-audit-catalog.schema.json`; `tests/test_prepare_ai_audit_batch.py:43`.
- Proposed action: Bind future audit results and default selection to the reviewed guide revision or content digest.
- Proposed owner: repository automation maintainers; due date not supplied.

### Independent content-assurance coverage trails the published library

- Fingerprint: `repository-health:content-assurance:coverage-gap`; high severity, high confidence; disposition: open.
- Observation: The repository contains 222 guides, while the current independent AI-audit ledger covers 39 guides and the freshness ledger covers 33. Ten AI-audit findings remain open, 61 source candidates remain queued, and no guide is marked community-reviewed. Source-validation records and automated checks cover important structural concerns, but they are not substitutes for the independent semantic and freshness layers defined by this repository.
- Evidence: `architecture.data-model.catalogs`; `data/ai-audits.json`; `data/source-freshness.json`; `data/source-candidates.json`.
- Proposed action: Continue risk-ranked independent audit and freshness batches, resolve the ten open findings, and establish an explicit human-review sampling target before treating library-wide quality as assured.
- Proposed owner: content-assurance maintainers; due date not supplied.

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

## Limitations and next decision

This static STRIDE/misuse-case review did not execute attacks, fetch external sources, inspect provider controls or assess every guide's lab safety. Threat likelihood and residual exploitability remain unmeasured.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

