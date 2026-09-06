# Documentation and Readiness Report

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-documentation-readiness.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

Repository documentation, contributor instructions, adapter inventory and Brownfield architecture, evaluated 2026-09-06. Decision-debt questions use the categories in accelerator `prompts/adr-workflow.md` as reference; no separate ADR assessment or ADR lifecycle change was executed.

## Readiness findings

| Domain | Status | Evidence | Gap | Recommendation |
|---|---|---|---|---|
| Architecture decisions | Partial | `docs/ARCHITECTURE.md`; Brownfield current/target separation | No ADR index or supplied historical approval record | Capture rationale only for consequential changes; do not reconstruct acceptance |
| Runbook completeness | Partial | `docs/AUTOMATION.md`, `docs/PUBLISHING.md` | Recovery and remote-success evidence absent | Review operational procedure with retained outcomes |
| Ownership | Partial | Contributor workflow and issue forms | Role routing exists without a path-level ownership matrix | Confirm accountable review/operations roles |
| Onboarding | Documented | `CONTRIBUTING.md`; pinned site setup and validation sequence | No evidence of an independent onboarding exercise | Verify a contributor can reproduce the documented steps |
| Knowledge freshness | Drift observed | Nine adapters documented; 26 routed; stale 'Both' wording | Extension inventory understates current surface | Resolve the shared maintainability finding |

## Follow-up actions

| Priority | Action | Owner | Due date | Verification |
|---|---|---|---|---|
| 1 | Reconcile adapter documentation with routing | Automation/documentation maintainer | Not supplied | Every registered adapter is represented |
| 2 | Confirm owner and escalation roles | Repository owner | Not supplied | Discoverable role map without inferring owners from commits |
| 3 | Retain onboarding and recovery exercise evidence when approved | Operations maintainer | Not supplied | Dated result with blocked steps explicit |

The lack of a modern ADR template alone is not a defect. No contradiction between accepted ADRs was asserted because no accepted ADR corpus was supplied.

## Canonical findings

### Core validation and monitoring logic is concentrated in two large modules

- Fingerprint: `repository-health:maintainability:automation-concentration`; medium severity, high confidence; disposition: open.
- Observation: The repository validator and official-study-guide monitor are each approximately two thousand physical lines, with provider routing centralized in the monitor. The adapter README lists nine adapters while the implementation routes 26 adapter keys, so the discoverable extension inventory already trails the code. This concentration increases review load and makes provider additions more likely to create code/documentation drift.
- Evidence: `scripts/validate_repository.py`; `scripts/check_official_study_guides.py`; `adapters/README.md`.
- Proposed action: Split stable validation and provider-routing responsibilities into focused modules and generate or validate the adapter inventory from the canonical registry.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

Named operating/decision owners, remote workflow execution, restore rehearsal and historical architecture-decision approvals are not available from the local document set.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

