# AI System Assurance Report

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-ai-system-assurance.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

System: AI-assisted study-guide authoring and independent content assurance. Model/runtime baseline: unspecified external assistant sessions; no deployed inference endpoint, model-serving runtime or training dataset exists in the local application inventory. The 39 audit results, 33 freshness results, ten open audit findings and zero community-reviewed guides are observed ledger counts.

## Assurance findings

| Domain | Status | Risk / limitation | Evidence | Recommendation |
|---|---|---|---|---|
| Model/data provenance | Partial | Auditor labels and independence are recorded; exact model/version and rationale absent | Audit schema; source and review catalogs | Retain enough run and content provenance for repeatability |
| Prompt/tool boundaries | Policy observed | Source text may contain untrusted instructions; technical enforcement not demonstrated | `docs/AI-AUDIT.md`, `docs/SOURCE-FRESHNESS.md` | Keep source material as evidence and changes in separately reviewed passes |
| Evaluation coverage | Partial | 39/222 audit and 33/222 freshness records; guide changes do not invalidate audit keys | Ledgers and preparer | Review both canonical findings |
| Safety controls | Stated / partial | Public-source, lab safety and exam-integrity rubrics exist; no separate safety-test artifact | Content policy and ten-check rubric | Retain representative safety-evaluation evidence |
| AI observability | Partial | Findings, summaries, hashes and dispositions present; no service telemetry | Audit/freshness catalogs | Use ledger evidence appropriate to offline content workflow |
| Human oversight | Policy present; execution unknown | AI result must not confer community-reviewed status | Contribution policy; zero community-reviewed records | Define a human sampling/review decision |
| Runtime dependency risk | Not assessed | Assistant availability and reproducibility unknown | No model deployment declaration | Document fallback to public-source/manual review when needed |

## Required follow-up

| Priority | Action | Owner | Due date | Validation evidence |
|---|---|---|---|---|
| 1 | Review outstanding assurance coverage and ten open audit findings | Content assurance maintainer | Not supplied | Ledger reconciliation and bounded human review |
| 2 | Bind reviewed guide content to audit eligibility | Automation maintainer | Not supplied | Guide-only edit triggers new eligibility |
| 3 | Record model/session provenance and safety examples when future audits run | Content assurance maintainer | Not supplied | Reproducible inputs, named rubric and dated outcomes |

No guide was freshly audited, no external vendor fact was revalidated, and no AI result was promoted to human review in this pass.

## Canonical findings

### Independent content-assurance coverage trails the published library

- Fingerprint: `repository-health:content-assurance:coverage-gap`; high severity, high confidence; disposition: open.
- Observation: The repository contains 222 guides, while the current independent AI-audit ledger covers 39 guides and the freshness ledger covers 33. Ten AI-audit findings remain open, 61 source candidates remain queued, and no guide is marked community-reviewed. Source-validation records and automated checks cover important structural concerns, but they are not substitutes for the independent semantic and freshness layers defined by this repository.
- Evidence: `architecture.data-model.catalogs`; `data/ai-audits.json`; `data/source-freshness.json`; `data/source-candidates.json`.
- Proposed action: Continue risk-ranked independent audit and freshness batches, resolve the ten open findings, and establish an explicit human-review sampling target before treating library-wide quality as assured.
- Proposed owner: content-assurance maintainers; due date not supplied.

### A guide-only change does not invalidate the default AI-audit completion key

- Fingerprint: `assessment:ai-assurance:guide-content-not-bound`; medium severity, high confidence; disposition: open.
- Observation: completed_current_audits and select_batch key completed work by exam code, blueprint snapshot hash and rubric version. The schema does not bind the result to guide content. Consequently a changed explanation or lab can remain excluded from default selection while its blueprint is unchanged. This is inferred from the key and selection condition; no runtime re-audit was executed.
- Evidence: `scripts/prepare_ai_audit_batch.py:60`; `scripts/prepare_ai_audit_batch.py:236`; `schemas/ai-audit-catalog.schema.json`; `tests/test_prepare_ai_audit_batch.py:43`.
- Proposed action: Bind future audit results and default selection to the reviewed guide revision or content digest.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

Model selection rationale, precise model/runtime version, adversarial safety-evaluation results and human review evidence are not supplied. This is an assessment of the AI-assisted content production process, not a fresh semantic audit of 222 guides.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

