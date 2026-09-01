---
exam_code: EX267
vendor_id: red-hat
official_blueprint: https://www.redhat.com/en/services/training/ex267-red-hat-certified-developer-in-ai
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# EX267 Red Hat Certified Developer in AI Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ex267-coverage-record). The [official EX267 objectives](https://www.redhat.com/en/services/training/ex267-red-hat-certified-developer-in-ai) are authoritative.

**Current baseline:** Red Hat OpenShift AI 3.3 on Red Hat OpenShift Container Platform 4.20<br>
**Upcoming blueprint change:** None announced when checked September 1, 2026<br>
**Important freshness boundary:** OpenShift AI evolves quickly. Confirm the versions assigned in the Red Hat learning environment, and translate older 2.x or newer documentation to the 3.3/4.20 baseline before following it.<br>
**Assessment style:** Performance based; public objective groups are not weighted

## How to use this guide

EX267 tests whether you can create a repeatable path from a data-science project to a served, monitored AI application. It is not primarily a model-theory exam and it is not an OpenShift cluster-administration substitute. Work at the application and project boundary while understanding the platform objects your choices create.

Use one small system throughout preparation: a model selected from an approved catalog, a versioned notebook and training pipeline, an object-storage connection, a registry entry, a KServe deployment, evaluation evidence, and a small streaming or retrieval-augmented application. For every task, retain evidence:

1. inspect project permissions, quota, nodes, storage, connections, images, runtime, and current workload state;
2. make the smallest safe dashboard, YAML, notebook, SDK, or API change;
3. prove the artifact, model, endpoint, pipeline, metric, or application behaves as required;
4. test a denied, delayed, malformed, or resource-constrained path;
5. restart or recreate the relevant component and prove that declared state, data, and version relationships persist.

Red Hat lists a final “Deploy and Store Models” group that refines capabilities already named under “Deploy and serve models.” This guide maps both groups explicitly to the same model-serving section and labs rather than inventing a separate weight.

## Objective map

| Official task group | What mastery looks like |
|---|---|
| Architecture and fundamentals | Explain the OpenShift/OpenShift AI boundary and place project components in an MLOps or GenAIOps lifecycle |
| Projects and workbenches | Control projects, permissions, images, versions, sizes, custom images, resources, and TensorBoard evidence |
| Data connections | Create least-privilege S3/database connections and prove artifact movement without exposing credentials |
| Resource allocation | Place workloads intentionally with selectors/tolerations and diagnose pending or starved work |
| Deploy and serve models | Choose serving mode, storage, runtime, protocol, resources, and scaling for predictive models or LLMs |
| Model Registry | Package, register, version, query, and deploy models with lineage intact |
| Model and hardware monitoring | Separate model-quality evidence from platform utilization, then act on both |
| Data science pipelines | Build reproducible Elyra/Kubeflow pipelines, artifacts, experiments, and runs |
| Optimize and evaluate | Select responsibly, compress/quantize where justified, and evaluate with repeatable benchmarks |
| Generative AI applications | Build bounded streaming, RAG, agentic, and guardrailed applications |
| Git and model development | Collaborate on notebooks/code and train, load, save, and export models reproducibly |
| Deploy and store models | Revalidate the serving interface, deployment settings, and S3/OCI/PVC storage choices above |

## 1. Architecture, projects, and lifecycle

OpenShift Container Platform supplies Kubernetes scheduling, namespaces/projects, identity, networking, storage, Operators, observability, and policy. OpenShift AI supplies the data-science dashboard and components for workbenches, pipelines, model registry, model serving, evaluation, and related AI workflows. Know which layer owns a failure: an invalid inference protocol is not fixed by adding a cluster role, while a pod blocked by quota or scheduling is not fixed by retraining the model.

MLOps connects source, data, environment, training, evaluation, approval, registration, deployment, monitoring, and feedback. GenAIOps extends that evidence chain to foundation models, prompts, retrieval indexes, evaluations, safety controls, tools, and runtime feedback. A data-science project is the collaboration and isolation boundary in which many of those components meet; it does not by itself prove data rights, model approval, or production readiness.

Create projects with purposeful membership and least privilege. Distinguish the user who experiments, the pipeline identity that reads data and writes artifacts, the registry client, and the serving identity. A broad project-admin grant may make a lab pass while hiding the authorization decision the task expects.

> **Related item:** Supply-chain provenance links Git commits, base images, packages, training data, model artifacts, evaluations, approvals, and deployments. It makes rollback and incident analysis possible even though “software bill of materials” is not a separate published objective.

## 2. Workbenches, images, and collaborative development

A workbench combines an image, image version, size/resource request, storage, environment variables or connections, and project permissions. Select the smallest supported image and size that satisfy the library, accelerator, and workload requirements. Treat image tags as mutable unless digest or release controls prove otherwise. A custom workbench image needs trusted packages, compatible drivers/runtime, a reproducible build, vulnerability review, and a supported notebook interface—not just a container that starts.

Use Git for notebook and application collaboration. Keep large data and model binaries out of ordinary Git history; store code, environment declarations, pipeline definitions, small fixtures, and documentation in Git and maintain pointers/checksums for external artifacts. Clear output and credentials before committing. Prefer small modules and tests over hiding all logic in notebook cells.

TensorBoard can expose training loss, accuracy and other logged series, but the graph is only as reliable as the experiment metadata. Record the source revision, data/version reference, parameters, seed where meaningful, image, hardware, run ID, and artifact destination. Compare runs rather than selecting the most attractive final point without context.

> **Related item:** Reproducibility is stronger than repeatability. A repeated run in the same long-lived workbench can depend on cached state; a reproducible run rebuilds the environment and declared inputs.

## 3. Data connections and artifact boundaries

Connections describe how a workload reaches external storage or databases. For S3-compatible storage, understand endpoint, bucket, region/compatibility details, access key or workload identity, TLS trust, and object prefix. For databases, understand host/service, database/schema, user, secret, TLS, driver, network policy, and connection lifecycle. Keep secrets in connection/secret mechanisms and inject references; never print them in notebooks, pipeline output, Git, or model metadata.

Prove both directions independently: read the expected input and write a uniquely named artifact, then retrieve and checksum it from a clean process. Test a missing object, revoked credential, wrong endpoint, invalid certificate, and unauthorized prefix. “Connection created” is configuration evidence, not data-path evidence.

Choose storage by lifecycle. S3-compatible object storage suits durable, shareable model/data artifacts; an OCI artifact integrates packaging, digest, promotion, and registry controls; a PVC gives filesystem semantics and locality but creates access-mode, capacity, placement, backup, and portability considerations. Record who can mutate each artifact and how a deployment resolves an immutable version.

## 4. Resources, scheduling, and accelerator evidence

Resource requests influence scheduling and guarantees; limits bound use. A node selector constrains placement to labels. A toleration permits—but does not require—placement on a tainted node; it does not create the hardware resource or bypass a missing request. Diagnose a pending workload by reading events, node labels/taints, requested resources, quotas, affinity, storage topology, and available accelerator resources before changing anything.

Allocate expensive accelerators deliberately. Match runtime/model precision, memory, context length, concurrency, batch behavior, and performance goals to the hardware. Monitor GPU/CPU/memory utilization, throttling, queue depth, latency, errors, and saturation. Higher utilization is not automatically better if latency or reliability violates the service objective.

> **Related item:** Capacity planning joins platform telemetry with workload demand. A model-quality regression and a hardware-saturation incident may produce similar user complaints but require different evidence and fixes.

## 5. Model serving with KServe

Know the serving path: client, route/network controls, inference endpoint, serving resource, runtime, model loader/storage, and accelerator. KServe supplies Kubernetes-native model-serving concepts; OpenShift AI presents supported workflows and modes. Standard and Advanced serving modes have different operational and topology implications. Names, supported combinations, autoscaling behavior, protocols, and feature availability are version-sensitive—verify them in the 3.3 documentation and exam environment.

Use OpenVINO for supported predictive-model formats and vLLM for supported large-language-model serving. Configure a custom serving runtime only when a provided runtime does not meet the model/protocol need; define its container, supported formats, command/arguments, ports, resources, probes, security, and storage behavior. A running pod is insufficient. Invoke the endpoint with valid and invalid payloads, verify schema/protocol and response, observe latency/errors/resources, and recreate the deployment.

Deployment settings should follow an explicit contract: immutable model reference, runtime and version, serving mode, protocol, resources/accelerator, replica/scaling policy, network exposure, authentication/authorization, timeouts, environment/secret references, and observability. Make rollback a model/runtime/configuration version change, not a manual repair to a live pod.

> **Related item:** An inference service has two versioned interfaces: its transport/schema contract and its statistical behavior. A backward-compatible JSON response can still be unsafe if the model or prompt changes its meaning.

## 6. Model Registry and lineage

The Model Registry records model identity, versions, artifacts, metadata, and lifecycle relationships. Package model artifacts as OCI artifacts when required and use immutable digests. Register a new version instead of silently overwriting an approved one. Metadata should make the version explainable: source revision, data reference, training run, framework/format, metrics/evaluation, owner, intended use, limitations, approval, and artifact checksum.

Practice dashboard and API workflows. Create and query a registered model, distinguish model identity from model version and artifact, select an exact version, and deploy from that record. Test duplicate names/versions, missing artifacts, unauthorized access, and a registry entry whose artifact digest no longer resolves. The registry is a catalog and governance anchor, not a substitute for the underlying artifact store or evaluation system.

## 7. Monitoring models and platform performance

Separate four evidence classes:

| Evidence | Question | Example response |
|---|---|---|
| Service health | Is inference available and within latency/error objectives? | scale, repair routing/runtime, or roll back |
| Resource health | Is CPU/GPU/memory/storage/network capacity adequate? | right-size, place, batch, limit, or add capacity |
| Data/model quality | Did inputs or outcomes drift or become biased? | investigate cohorts/data, retrain or constrain use |
| Business/safety outcome | Does the application remain useful and safe? | adjust retrieval/prompt/guardrails or suspend flow |

Use TrustyAI for supported bias, drift, evaluation, and guardrail workflows. A metric needs a defined population, reference, threshold, observation window, and response owner. Aggregate accuracy can conceal subgroup harm; drift can be harmless seasonal change or an early warning, not automatic proof of failure. Use OpenShift monitoring and Grafana to correlate model signals with resource and request signals.

Never log raw sensitive prompts, retrieved documents, secrets, or regulated labels merely to improve observability. Design redaction, access, retention, sampling, and incident evidence before production.

## 8. Data science pipelines and experiments

Create a pipeline server and build components with clear inputs, outputs, images, resources, secrets, and artifact locations. Elyra can help author notebook-oriented flows; the Kubeflow Pipelines SDK defines reusable container components and pipelines. The compiled/uploaded definition—not the notebook UI—is the execution contract.

Use Kubernetes features intentionally: service accounts, secrets/configuration references, PVCs, resource requests/limits, node placement, and exit behavior. Components should be independently rerunnable, validate inputs, produce deterministic names or run-scoped outputs, and fail loudly. Cache only when the cache key captures every meaningful input. Treat a pipeline run as a graph of evidence, not a sequence of green icons.

Use experiments to group comparable runs and compare parameters, inputs, metrics, artifacts, duration, resource use, and outcome. Promote only an exact evaluated artifact. Test resume/retry and ensure side effects are idempotent or deduplicated.

> **Related item:** Orchestration handles ordering and retries; data contracts handle meaning. A perfectly orchestrated pipeline can still train on mislabeled, stale, or unauthorized data.

## 9. Model selection, optimization, and evaluation

Select from the OpenShift AI catalog or Hugging Face using task fit, license, provenance, architecture, supported runtime, context/input limits, language/domain evidence, safety history, hardware need, and maintenance status. “Popular” is not an acceptance criterion. Record the exact revision and license terms; model code may require more trust than weights alone.

Compression and quantization with supported LLM Compressor workflows can reduce memory, cost, or latency but may change quality and hardware compatibility. Establish a baseline, change one optimization dimension, measure task and subgroup quality plus throughput/latency/memory, and keep the unoptimized rollback artifact.

Use LMEval with standard or justified custom benchmarks. Prevent train/test contamination, pin prompt/templates and dataset versions, choose metrics before comparison, and retain configuration and result artifacts. A benchmark improvement does not prove production safety; pair offline evaluation with application-level, adversarial, latency, cost, and human-review evidence.

## 10. Generative, retrieval, agentic, and guardrailed applications

A simple streaming application should preserve partial-response UX while handling cancellation, timeout, backpressure, authentication, errors, and final telemetry. For RAG, separate ingestion (extract, normalize, chunk, embed, authorize, index) from request time (authenticate, retrieve, filter/rerank, assemble context, generate, cite, evaluate). Enforce source-level permissions during retrieval; prompting the model not to reveal unauthorized material is not access control.

An agent combines a model with tools and a loop. Give each tool a narrow typed contract, least-privilege identity, validation, timeout, idempotency strategy, and audit record. Bound steps, time, tokens, spend, reachable resources, and data. Require human approval before consequential or irreversible actions and distinguish model text from trusted instructions.

Guardrails are defense in depth: validate input, constrain retrieval and tools, detect unsafe content, protect sensitive data, validate structured output, enforce business authorization outside the model, and monitor outcomes. Test direct and indirect prompt injection, data leakage, malformed tool arguments, denial-of-wallet, unavailable dependencies, and false positive/negative behavior.

> **Related item:** RAG changes the model's context; fine-tuning changes parameters; tools change what the application can do. Diagnose which layer caused the outcome before changing all three.

## Integrated scenarios

### Scenario 1: Governed predictive service

A team trains a churn model from approved object storage. Build a project and least-privilege connection, version code and environment, pipeline preprocessing/training/evaluation, log TensorBoard evidence, package/register the approved artifact, deploy it with OpenVINO, validate endpoint semantics, then monitor resource use and drift. Revoke the data credential after training and prove inference still follows the intended artifact path.

### Scenario 2: Resource-constrained LLM service

An LLM deployment remains pending, then becomes slow under load. Trace selector, toleration, accelerator request, quota, storage and events. Deploy the exact model using vLLM, establish latency/throughput/memory baselines, quantize only after the quality baseline, and compare. Prove rollback to the registered unoptimized version and retain request/resource/evaluation evidence.

### Scenario 3: Guardrailed RAG assistant

Build an application that ingests authorized documents, creates a versioned vector index, retrieves only caller-permitted content, streams cited answers, and invokes one read-only tool. Evaluate retrieval and answer quality, add input/output guardrails and typed validation, test injection and tool failures, and correlate application traces with model-serving and hardware signals.

## Hands-on labs

1. **Project/workbench baseline:** create roles, a sized workbench and persistent storage; clone code, record image/version, restart, and prove permissions and files persist.
2. **Custom image and experiment:** build/import a pinned custom workbench image, run a small training job, emit TensorBoard metadata, and reproduce from a clean workbench.
3. **Connections and artifacts:** use least-privilege S3-compatible and database connections; read/write/checksum artifacts and test bad credentials/TLS/path.
4. **Placement diagnosis:** schedule CPU and accelerator-shaped workloads with selectors/tolerations; deliberately create and diagnose a pending pod without broadening access blindly.
5. **Serving and registry:** register two model versions, deploy exact OpenVINO and vLLM artifacts through appropriate modes/storage, test protocols and invalid input, then roll back.
6. **Pipeline evidence:** author a multi-component pipeline with the SDK or Elyra, pass artifacts, compare experiment runs, test caching and safe retry, and reproduce a chosen result.
7. **Evaluation and monitoring:** run a pinned standard or custom LMEval job, exercise TrustyAI drift/bias evidence, and correlate it with request and hardware dashboards.
8. **Capstone replay:** rebuild one scenario from Git and declared external artifacts, validate RAG or tool boundaries, restart/recreate every component, and produce an evidence/rollback packet.

Use a disposable authorized cluster and small models/datasets. GPU resources and hosted model calls can be scarce or costly; set quotas and budgets and remove lab resources when finished.

## Original knowledge checks

1. Which responsibilities belong to OpenShift versus OpenShift AI?
2. What artifacts extend an MLOps evidence chain into GenAIOps?
3. Why is a project-admin grant weak evidence of correct authorization?
4. Which workbench properties must be recorded to reproduce an experiment?
5. Why can a mutable image tag invalidate a comparison?
6. What belongs in Git, and what belongs in an artifact store?
7. What does TensorBoard show, and what provenance must accompany it?
8. How would you prove a connection beyond its dashboard status?
9. When is S3 preferable to OCI or PVC model storage?
10. What credential evidence must never enter notebook output?
11. How do requests, limits, selectors, and tolerations affect placement differently?
12. Which events would explain an accelerator workload remaining pending?
13. Why can high GPU utilization coexist with a poor service outcome?
14. Trace a request from route to model artifact and response.
15. What must a custom serving runtime declare and prove?
16. Why is a running inference pod insufficient acceptance evidence?
17. Which deployment settings must be versioned for rollback?
18. How do model identity, version, and artifact differ in the registry?
19. Which metadata connects a registry version to training and approval?
20. What failure occurs when registry metadata resolves to a missing artifact?
21. How do service, resource, model-quality, and business signals differ?
22. Why does drift not automatically prove model failure?
23. How can an aggregate metric conceal subgroup harm?
24. What observability data should be redacted or access-controlled?
25. What makes a pipeline component independently rerunnable?
26. When can pipeline caching return an invalid result?
27. How should a retry-safe component handle external side effects?
28. What makes two experiment runs legitimately comparable?
29. Which selection evidence matters beyond model popularity?
30. How would you detect benchmark contamination?
31. What quality and performance evidence should bracket quantization?
32. Why is an offline benchmark not production acceptance?
33. Separate RAG ingestion-time and request-time responsibilities.
34. Where must document authorization be enforced in RAG?
35. What controls bound an agent loop and its tools?
36. Which actions should require human approval?
37. Why are guardrails not a substitute for authorization?
38. How would you test indirect prompt injection safely?
39. Which persisted evidence proves the capstone can be recreated?
40. What must be checked when using a guide written for OpenShift AI 2.x?

## Answers and reasoning

1. OpenShift owns core cluster primitives; OpenShift AI composes supported AI workflows on them.
2. Model/prompt/index/tool versions, evaluations, safety controls, approvals, runtime feedback, and costs.
3. It bypasses least-privilege decisions and can hide the identity actually needed.
4. Source/data references, image and packages, resources, parameters, seed, run ID, metrics, and artifact destination.
5. The same name can resolve to different bits, destroying reproducibility and rollback confidence.
6. Version code/configuration/pipeline definitions and small fixtures; externally store large or sensitive data/models with immutable references.
7. Logged training series; it needs source, data, environment, parameter, run, and artifact context.
8. Read and write a unique artifact, retrieve/checksum it cleanly, and test failure paths.
9. For durable shareable objects; OCI favors digest-based packaging/promotion, while PVC favors filesystem/local access.
10. Secrets, tokens, full connection strings, sensitive records, and unredacted regulated data.
11. Requests drive scheduling, limits bound use, selectors require labels, and tolerations only permit tainted placement.
12. Events plus labels, taints, accelerator availability/request, quota, affinity, and storage topology.
13. Saturation can increase queues/errors/latency or run the wrong-quality workload efficiently.
14. Identify each network, serving-resource, runtime, loader/storage, process, protocol, and response boundary.
15. Image, formats, command, ports, protocol, resources, probes, security, and storage compatibility.
16. The model may not load correctly, protocol/authorization may fail, or output may be unusable.
17. Artifact digest, runtime/mode/protocol, resources, scaling, exposure, identity, config/secrets, and observability.
18. Identity groups the concept, version records a revision, and artifact is the immutable payload/location.
19. Source/data/run references, format, metrics, owner, intended use, limitations, approval, and checksum.
20. Discovery succeeds but reproducible deployment fails; treat it as a lineage/integrity incident.
21. They answer availability, capacity, statistical behavior, and actual usefulness/safety questions respectively.
22. It is a change signal whose materiality must be evaluated against outcomes and context.
23. Majority performance can mask a severe minority-cohort regression.
24. Prompts, retrieved text, labels, secrets, identifiers, tool arguments/results, and regulated data.
25. Declared inputs/outputs/image/resources, validation, durable artifacts, and deterministic or run-scoped side effects.
26. When the key omits code, data, parameters, environment, or another meaningful input.
27. Use idempotent writes, unique run keys, transactions, or explicit deduplication.
28. Pinned data/code/environment/parameters, comparable hardware/metrics, and retained artifacts.
29. Task evidence, license/provenance, runtime support, limits, domain/language fit, safety, resources, and maintenance.
30. Audit dataset lineage and overlap, isolate held-out data, and inspect suspiciously perfect or prompt-sensitive results.
31. Same pinned tasks/subgroups plus accuracy/safety, latency, throughput, memory, hardware, and rollback artifacts.
32. It does not test retrieval, tools, permissions, latency, cost, safety controls, or real user distribution.
33. Ingestion creates authorized indexed evidence; request time authenticates, filters/retrieves, prompts, generates, and cites.
34. In the retrieval/data layer before content becomes model context, with application authorization enforced afterward too.
35. Typed tools, least privilege, input/output validation, timeouts, idempotency, audit, and step/token/time/cost limits.
36. Irreversible, financially material, privileged, external-communication, or safety-critical changes.
37. A probabilistic filter cannot grant or deny deterministic business/data permissions.
38. Use synthetic authorized documents containing hostile instructions and verify they cannot expand tool/data authority.
39. Git revision, environment/image, data/model/index digests, pipeline/run configuration, metrics, approvals, deployment state, and rollback proof.
40. Map every objective to 3.3/4.20 names, APIs, modes, runtimes, storage, security, UI, and supported behavior.

## Version-gap checklist

Before using older 2.x or newer rolling material, verify against the official 3.3/4.20 environment:

- dashboard navigation, component/operator state, CRD/API versions, and terminology;
- Standard versus Advanced serving behavior, KServe topology, supported runtimes/protocols, and scaling;
- model storage, OCI packaging, registry API/metadata, and deployment-from-registry workflow;
- pipeline backend, Elyra/Kubeflow SDK syntax, caching, experiments, and artifact behavior;
- TrustyAI, LMEval, Guardrails Orchestrator, model catalog, and Hugging Face integration;
- accelerator profiles, node placement, monitoring metrics/dashboards, and permissions;
- workbench images, custom-image requirements, connection fields, and security defaults.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Select the explanation, lab, reference, or assessment format that closes your own gaps; spend most preparation time performing and revalidating the public tasks.

| Resource | Access | Estimated time |
|---|---|---:|
| [Red Hat AI267 official course](https://www.redhat.com/en/services/training/ai267-developing-and-deploying-ai/ml-applications-on-red-hat-openshift-ai) | Paid; closest version-matched route | About 4–5 instructor-led days plus 30–60 hours of replay |
| [Red Hat AI067 technical overview](https://www.redhat.com/en/services/training/ai067-red-hat-ai-technical-overview) | Free account; broad orientation | About 3–6 hours |
| [OpenShift AI 3.3 documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3) | Free official reference | 25–50 selected hours while labbing |
| [OpenShift Container Platform 4.20 documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20) | Free official prerequisite/reference | 10–25 selected hours for project, storage, scheduling, security, and monitoring gaps |
| [Red Hat Developer OpenShift AI learning hub](https://developers.redhat.com/learn/openshift-ai) | Free; mixed-version paths | 5–15 selected hours plus labs |
| [Introduction to OpenShift AI](https://developers.redhat.com/learn/openshift-ai/introduction-openshift-ai) | Free one-hour path; account/sandbox requirements | About 1–3 hours with repetition |
| [Scalable Kubernetes Infrastructure for AI Platforms](https://www.oreilly.com/library/view/scalable-kubernetes-infrastructure/9798341608191/) | O'Reilly subscription; Red Hat authors | 1 hour 6 minutes listed plus 3–6 hours applying concepts |
| [LLM on OpenShift AI Deployment Masterclass](https://www.udemy.com/course/llm-on-openshift-ai-deployment-masterclass/) | Paid marketplace course | 2 hours 49 minutes listed plus 5–10 lab hours; verify every workflow against 3.3 |
| [Red Hat 3.3 training/certification update](https://www.redhat.com/en/blog/accelerate-and-upskill-red-hat-ai-training-and-certification) | Free lifecycle context | 10–20 minutes |

No exact current EX267 MeasureUp, Whizlabs, Pluralsight certification path, or independent practice exam was verified. Avoid recalled-task banks and “actual exam” claims. A performance exam is best served by original objective-mapped tasks, clean rebuilds, failure injection, and evidence review.

## Source and freshness notes

- The official exam page controls the name, version baseline, objectives, prerequisites, delivery language, and lifecycle state.
- Product documentation controls supported commands, APIs, modes, permissions, integrations, and operational behavior for 3.3/4.20.
- Training-provider runtimes, prices, schedules, revisions, catalogs, sandbox access, and course availability are volatile; verify before purchase.
- Model licenses, catalog entries, supported formats/runtimes, hardware profiles, limits, and security behavior are also volatile.
- This guide uses only public objectives and original practice prompts. It does not reproduce gated course labs or exam tasks.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.
