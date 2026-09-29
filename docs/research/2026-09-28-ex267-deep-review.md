# EX267 deep review — September 28, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/EX267-red-hat-certified-developer-in-ai.md).

## Scope and unresolved source differences

Read all 43 current [main-page tasks](https://www.redhat.com/en/services/training/ex267-red-hat-certified-developer-in-ai), in twelve groups with 3/4/2/2/6/4/3/4/3/5/3/4 tasks. The exam and AI267 course retain OpenShift AI 3.3 and OpenShift 4.20. Objective and lifecycle monitor hashes are unchanged; accepted snapshots were not replaced.

The EX267V33K section in the [public version PDF](https://training-lms.redhat.com/public_content/redhat/training/Red%20Hat%20Certification%20Exam%20Objectives%20by%20Version.pdf) has 41 matching tasks after normalization. It omits the main page's Identify and allocate resources group: selectors/tolerations and placement of workbenches/model servers on specific nodes. All 43 canonical main-page tasks remain mapped. Same-day directly fetched PDF bytes were reused from EX280; EX267 sections were separately extracted, read and compared.

The exam also names Standard and Advanced serving modes. The [3.3 deployment guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/deploying_models/index) uses RawDeployment and an Advanced settings wizard. Those labels do not establish a mapping to old Serverless/Knative or ModelMesh recipes. Retain the objective and verify the assigned environment. Both source discrepancies remain blocked findings with an October 5 library follow-up, not a vendor transition date or a request to change the exam scope.

## Implementation and support repairs

Reviewed targeted implementation sections in twelve 3.3 books, rather than treating the documentation landing-page index as implementation evidence. Added Hardware Profiles versus legacy accelerator/size selection, connection protocol annotations, registry v1beta1, image publication versus workbench creation, placement diagnostics, modelcar layout/permissions and deployment strategy capacity/downtime.

The [release notes](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/release_notes/index) cover 3.3.6 and label LLM Compressor integration Developer Preview. This remains an exam topic, but its presence in objectives is not a production-support guarantee. The [registry guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_model_registries/index) limits its URI-registered deployment workflow to public OCI repositories; this is not generalized to all direct-serving storage mechanisms.

The [pipeline guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_ai_pipelines/index) supports Python 3.11+/KFP 2.14.3+, two compiler output formats, explicit cache controls and image-specific Elyra. Added hidden mutable-input cautions and the documented UBI 9/RHEL 9 requirement for custom pipeline containers on FIPS clusters. The [LM-Eval guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/evaluating_ai_systems/index) distinguishes platform permission from job requests for internet/code access. The [guardrails guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/enabling_ai_safety_with_guardrails/index) supports separate detector, Orchestrator and gateway checks.

## Original example and actual execution

Added an original two-component KFP graph with typed Dataset, Metrics and Artifact ports. Preparation validates a synthetic binary-prediction dataset and emits canonical bytes plus their digest. Evaluation verifies that digest, scores overall and cohort accuracy, checks the declared population/minimum sizes, and emits evidence that explicitly still requires separate approval. No deployment step exists.

**39 local checks passed** using Python 3.13.14 and KFP 2.14.3. They execute both original component Python bodies with real KFP artifact/metric objects. Cases cover a passing population, 90% overall accuracy hiding a 0% cohort, missing/extra/undersized cohorts, duplicate IDs, field types, malformed thresholds, changed artifact bytes and exact boundaries. The compiler produced both plain PipelineSpec IR and Pipeline/PipelineVersion resources with the same embedded specification, correct dependencies/resources/cache settings, and rejected an incompatible Dataset-to-Model edge. The initial negative-test harness caught the wrong exception class; it was corrected to expect the SDK's InconsistentTypeException, and the complete 39-check suite passed.

These are local function/compiler results. No container image was pulled, no pipeline backend or cluster ran, and no model inference, training, LM-Eval, GPU, S3, database, registry, serving endpoint, TrustyAI service, guardrail deployment or durable restart was executed. The image string is a compilation exercise; deployment requires an approved pinned environment. All eight complete platform labs remain proposed. Synthetic quality thresholds are illustrative and do not establish production fairness or representativeness.

## Blog and learning catalog

Ana Biazetti, Nelesh Singla and Matt Prahl's June 3, 2026 [modular-components article](https://developers.redhat.com/articles/2026/06/03/build-modular-ai-pipelines-openshift-ai-and-reusable-components) informed early validation, narrow interfaces and small-data checks. Original code was independently authored. Its stability labels and agent workflow are not adopted as production guarantees or session instructions. Heather Sherwood's July 8 training announcement is lifecycle context, not current pricing or entitlement evidence.

Retained and strengthened the guide's existing 40 answers. OReilly and Udemy pages blocked rechecking; inherited runtimes are now explicitly unverified. Places to learn is the final section. Repository validation, 176 unit tests, strict site build, generated-site validation, learning catalog consistency and diff checks are recorded in the operational receipt only after execution.
