# Runbook Readiness — Static Library Operations

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-runbook-readiness.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Readiness scorecard

Qualitative states follow the Snapshot no-score policy; untested/unknown evidence never becomes Good.

| Area | State | Evidence |
|---|---|---|
| Deploy procedure | Partial | `docs/PUBLISHING.md`; artifact-only Pages workflow; no current deployment result |
| Rollback | Gap in supplied procedure/evidence | Git history available; no time-bounded rollback exercise |
| Monitoring/alerting | Partial | Weekly objective/source-health workflows and issue paths; no runtime/receiver evidence |
| Incident response | Partial | Correction/maintenance issue routes; no severity/escalation/on-call record |
| Backup/recovery | Not assessed | Git revision recovery possible; no restore target or drill |
| Scaling | Not applicable to local app runtime | No owned stateful service or autoscale configuration |
| Secret rotation | Provider evidence unavailable | GitHub job-token and Oracle guest-token mechanisms |
| Certificate renewal | Not assessed | Pages/TLS provider state not queried |
| Health checks | Partial | Content-source checks and static link checks; not deployed availability probes |
| Documentation | Partial | Versioned operating guides; adapter inventory drift |

## What exists

Publishing describes pinned setup, strict build, generated-site validation and the Pages artifact path. Automation documents schedules, maintenance issues, snapshot review, candidate promotion and fresh-context audit/repair separation. Content policy defines public corrections/removals.

## What's missing

Tested rollback/restore evidence, explicit incident ownership/escalation, current workflow results, service objectives and up-to-date adapter coverage. No claim is made that these are absent from all external systems; they are absent from the supplied local evidence.

## Operational procedures status

| Procedure | Documented | Automated definition | Tested evidence |
|---|---|---|---|
| Build and publish | Yes | Yes | Historical statements; current result unavailable |
| Monitor source/objective changes | Yes | Yes | Fixture tests/historical evidence; remote history unavailable |
| Review and accept snapshots | Yes | Human review | No provider review history |
| Revert/redeploy | Partial Git mechanism | No explicit rollback job | Not supplied |
| Restore content/service | Partial Git mechanism | Unknown | Not supplied |
| Respond to inaccurate/private content | Yes | Issue route only | Not supplied |

## Recommended runbook TOC

Extend existing documents with service scope and owners; prerequisite/access checks; deploy verification; rollback/restore decision and procedure; monitoring interpretation; incident escalation; source/guide correction; recovery evidence; dependency review; and a review cadence. No new operational workflow was implemented.

## Priority actions

| Priority | Action | Effort basis |
|---|---|---|
| 1 | Define and exercise a scoped rollback/restore procedure | Needs owner/environment decision; no duration estimate supported |
| 2 | Reconcile shared CI setup and gate definitions | Two duplicated main gates plus different objective-monitor setup |
| 3 | Confirm escalation roles and update adapter inventory | Existing docs can be extended after review |

These are proposed review actions, not an implementation backlog.

## Canonical findings

### CI validation is duplicated and dependency-update coverage is partial

- Fingerprint: `repository-health:ci:duplicated-validation-and-partial-update-coverage`; medium severity, high confidence; disposition: open.
- Observation: The validation and Pages workflows repeat the same unit, repository, strict-build, and site-validation sequence. Dependabot is configured only for GitHub Actions even though the site has three pinned Python dependencies, and workflow actions use mutable major-version references. These local definitions create maintenance drift and supply-chain review work; remote enforcement and run health could not be assessed.
- Evidence: `.github/workflows/validate-repository.yml`; `.github/workflows/deploy-pages.yml`; `.github/dependabot.yml`; `dependency.direct.site`.
- Proposed action: Centralize the shared validation sequence, add governed Python dependency updates, and adopt a documented action-reference policy.
- Proposed owner: delivery maintainers; due date not supplied.

### Core validation and monitoring logic is concentrated in two large modules

- Fingerprint: `repository-health:maintainability:automation-concentration`; medium severity, high confidence; disposition: open.
- Observation: The repository validator and official-study-guide monitor are each approximately two thousand physical lines, with provider routing centralized in the monitor. The adapter README lists nine adapters while the implementation routes 26 adapter keys, so the discoverable extension inventory already trails the code. This concentration increases review load and makes provider additions more likely to create code/documentation drift.
- Evidence: `scripts/validate_repository.py`; `scripts/check_official_study_guides.py`; `adapters/README.md`.
- Proposed action: Split stable validation and provider-routing responsibilities into focused modules and generate or validate the adapter inventory from the canonical registry.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

CI history, on-call/incident records, a rollback test within 90 days, restore drill, service objectives, certificate status and remote token lifecycle were not supplied. Kubernetes probes and cloud auto-scaling do not apply to this local static-site workload.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

