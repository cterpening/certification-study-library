---
exam_code: AI-300
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AI-300 Operationalizing Machine Learning and Generative AI Solutions Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official AI-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300) is authoritative.

**Current baseline:** Official page last updated March 5, 2026; no separate skills-effective date is published.<br>
**Upcoming blueprint change:** None announced as of August 31, 2026.<br>
**Lifecycle status:** Active; no retirement or replacement was announced.<br>
**Exam page:** [Machine Learning Operations Engineer Associate](https://learn.microsoft.com/en-us/credentials/certifications/operationalizing-machine-learning-and-generative-ai-solutions/) · 120-minute assessment · verify current languages.<br>
**Official course:** [AI-300T00 Operationalize machine learning and generative AI solutions](https://learn.microsoft.com/en-us/training/courses/ai-300t00) · four instructor-led days.<br>
**Practice:** Microsoft directs candidates to the [AI Skills Navigator Practice Assessment](https://aiskillsnavigator.microsoft.com/en-us/certifications/microsoft-certified-associate/machine-learning-operations-engineer); sign-in is required.

## How to use this guide

Trace every system through immutable evidence:

```text
code + data + environment + parameters -> run -> metrics/artifacts -> registered version
approved version -> endpoint/deployment -> traffic -> telemetry -> promote/rollback
prompt + model + retrieval + safety config -> evaluation dataset -> metrics -> release
source change -> drift/quality signal -> alert/gate -> retrain/reevaluate -> controlled rollout
```

Retain resource/IaC version, Git commit, data/feature lineage, environment digest, run ID, parameters, metrics, model/prompt/index versions, evaluation dataset/results, endpoint/deployment and traffic, identity/grants, traces/cost and rollback proof. Product names, Foundry SDK surfaces, model versions, quotas, evaluation metrics and monitoring features change quickly; verify linked sources.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in Microsoft's objectives.

## Objective map

| Domain | Weight | Release question |
|---|---:|---|
| Design and implement an MLOps infrastructure | 15–20% | Can reproducible ML assets run securely in a versioned, network-restricted workspace? |
| Implement machine learning model lifecycle and operations | 25–30% | Can training, comparison, registration, rollout, monitoring and retraining be automated safely? |
| Design and implement a GenAIOps infrastructure | 20–25% | Can Foundry resources, models and prompts be provisioned, versioned and scaled for production? |
| Implement generative AI quality assurance and observability | 10–15% | Can quality, safety, latency, cost and traces gate and explain a release? |
| Optimize generative AI systems and model performance | 10–15% | Can retrieval and fine-tuning improve measured outcomes without losing governance? |

---

# 1. Design and implement an MLOps infrastructure (15–20%)

## Build the Azure Machine Learning resource boundary

An Azure Machine Learning workspace organizes jobs, assets, endpoints, connections and collaboration while depending on Azure Storage, Key Vault, Container Registry and monitoring resources. Start with the [workspace architecture](https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace?view=azureml-api-2) and [secure workspace guidance](https://learn.microsoft.com/en-us/azure/machine-learning/concept-secure-network-traffic-flow?view=azureml-api-2).

Separate dev/test/prod workspaces when access, data, quota, experimentation or blast radius requires it. Define region, dependent resources, public/private network mode, managed network/private endpoints, DNS, outbound rules, encryption, diagnostics, tags/budget and managed identities in IaC.

### Datastores and data assets

A datastore stores connection information to Azure storage/data source; it is not the data itself. Prefer identity-based access and never embed keys in YAML/source. A data asset supplies a versioned reference/contract (URI file/folder or MLTable) for reproducible jobs. See [datastores](https://learn.microsoft.com/en-us/azure/machine-learning/concept-data?view=azureml-api-2) and [data assets](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-data-assets?view=azureml-api-2).

Version does not freeze a mutable external path. Preserve immutable snapshot/version/hash and schema/quality evidence. Prevent training/test leakage and enforce data classification/retention.

### Compute targets

- Compute instance: individual interactive development; stop when idle and do not make it a production scheduler.
- Compute cluster: autoscaling CPU/GPU training and batch workloads; choose VM size, min/max nodes, idle scale-down, identity and network.
- Serverless compute: managed per-job compute where supported; verify image/package/network/data access.
- Attached/external compute: use only for a requirement and account for its patching/identity/telemetry boundary.

Size from measured training duration, distributed strategy, memory/GPU utilization, data throughput, quota and cost. Min zero saves idle cost but adds startup latency.

### Identity and access

Use Microsoft Entra groups and managed identities. Separate workspace administration, data scientist asset/job work, pipeline deployment and endpoint runtime identities. A control-plane role does not automatically grant storage/registry/Key Vault data access. Test positive and negative operations and prefer least-privileged built-in/custom roles. Review [workspace access management](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-assign-roles?view=azureml-api-2).

> **Related item:** A job submitted by a permitted user can execute as a different compute/workspace identity. Trace both submission authorization and runtime access to data, registry and secrets.

## Create reusable workspace assets

An **environment** versions Docker image/build context plus Conda dependencies. Pin packages/base images, scan, test imports and record digest. A **component** defines inputs, outputs, code, command and environment as a reusable pipeline step. A **pipeline** composes components and their data dependencies. See [environments](https://learn.microsoft.com/en-us/azure/machine-learning/concept-environments?view=azureml-api-2) and [components](https://learn.microsoft.com/en-us/azure/machine-learning/concept-component?view=azureml-api-2).

Avoid notebook-only hidden state, mutable `latest` environments and hard-coded workspace paths. Components should be deterministic from declared input/version/parameter, write declared outputs and expose meaningful metrics.

Azure Machine Learning registries share versioned models, components and environments across workspaces/regions. Define promotion ownership, immutability, replication/support and consumer compatibility; registry sharing is not approval by itself. Use [registries](https://learn.microsoft.com/en-us/azure/machine-learning/concept-machine-learning-registries-mlops?view=azureml-api-2).

## Provision with Bicep, CLI and GitHub Actions

Deploy workspace/dependencies, identity, network, compute policy and diagnostic settings with Bicep modules; deploy ML assets/jobs/endpoints through versioned Azure CLI v2 YAML/SDK as appropriate. Use the [Azure ML CLI v2](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2) and [Bicep resource reference](https://learn.microsoft.com/en-us/azure/templates/microsoft.machinelearningservices/workspaces).

GitHub Actions should authenticate through OpenID Connect federation rather than a long-lived client secret. Restrict subject to repository/branch/environment, grant scoped roles and use protected environments/approvals. Pin action versions, separate build/evaluate from deploy, promote one immutable artifact and retain logs. See [Azure Login OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect).

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: azure/login@v2
    with:
      client-id: ${{ secrets.AZURE_CLIENT_ID }}
      tenant-id: ${{ secrets.AZURE_TENANT_ID }}
      subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
  - run: az ml job create --file jobs/train.yml --resource-group "$RG" --workspace-name "$WS"
```

IDs are configuration values rather than credentials, but repository/environment permissions remain sensitive. Add Bicep lint/what-if, policy/security scan, asset validation, evaluation threshold and deployment health/rollback gates.

## Restrict networking and manage Git

Private endpoints/managed virtual network do not automatically solve DNS or dependent-resource access. Map control, data, image/package, identity, monitoring and model endpoints. Provide approved outbound rules/package mirror and a managed self-hosted runner if public GitHub-hosted runners cannot reach private resources.

Use small branches/commits for source, component/YAML, environment lock, tests, prompt and IaC. Store large data/models in versioned managed storage/registry, not Git. PR review is valuable but a solo flow still needs automated validation before direct merge. Never commit secrets, connection strings or production samples.

---

# 2. Implement machine learning model lifecycle and operations (25–30%)

## Make experiments reproducible with MLflow

MLflow tracking records runs, parameters, metrics, tags and artifacts. Azure ML jobs can integrate MLflow without manually managing a tracking server. Log data/version, code commit, environment, seed, feature spec, algorithm/parameters, metrics by split and artifacts. See [MLflow tracking in Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2).

Notebook exploration is appropriate for profiling/hypothesis; production logic belongs in scripts/components with declared arguments, environments and tests. A notebook “Run all” result is not reproducibility evidence.

### AutoML and hyperparameter tuning

Automated ML explores algorithms/featurization within task, metric, compute, time/trial and validation constraints. It does not choose the business objective or prevent leakage. Inspect the winning pipeline, explainability, latency/size and subgroup behavior. Use [AutoML concepts](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml?view=azureml-api-2).

Sweep jobs search a defined parameter space using random/grid/Bayesian sampling and early termination such as bandit/median/truncation policies. Define primary metric direction, limits, concurrent trials and deterministic evaluation. A validation winner still needs untouched test and responsible-AI checks. See [hyperparameter tuning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2).

### Distributed training

Use MPI, PyTorch or TensorFlow distributed configuration only after profiling. Align process-per-node, node count, GPU topology, communication backend, data sharding, checkpoint and failure/restart. More GPUs can slow training when input/communication dominates. Measure throughput, scaling efficiency, GPU/CPU/memory/network, convergence and cost.

## Build training pipelines

Typical graph: validate data -> engineer/materialize features -> train -> evaluate -> register conditional candidate. Component caching/reuse requires identical declared inputs/settings and deterministic behavior; mutable external data or hidden dependency makes reuse unsafe.

Package a **feature retrieval specification** with the model artifact when the serving system needs the same feature definitions/source/key/timestamp behavior as training. Prevent online/offline skew, leakage and point-in-time errors; version transformations and feature sources with the model.

Compare runs on the same evaluation data and business constraints: predictive metric, calibration, subgroup fairness, robustness, latency, memory/size and cost. Do not promote on one aggregate accuracy.

## Register and govern models

An MLflow model packages flavor/signature/dependencies/artifacts; registration creates an immutable versioned model asset. Record stage/status/owner, lineage, intended use, evaluation, approval and compatibility. Archive/deprecate to remove normal selection without erasing evidence required for rollback/audit. Use [MLflow models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow-models?view=azureml-api-2) and [model management](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-models?view=azureml-api-2).

Responsible evaluation covers fitness, subgroup/fairness, error analysis, explainability, privacy/security and harm appropriate to the use. The [Responsible AI dashboard](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2) combines supported analysis but does not make the deployment responsible automatically.

## Deploy online and batch endpoints

Managed online endpoints serve low-latency requests through deployments; batch endpoints process large asynchronous datasets/jobs. Choose from latency/throughput, input size, freshness, concurrency, retry, cost and result-delivery needs. See [online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2) and [batch endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-batch?view=azureml-api-2).

Configure model, code/scoring contract, environment, instance/compute, min/scale, identity, networking, auth, request/response schema, timeout and logging. Test locally where useful, then endpoint smoke, contract, load, security and failure tests. Diagnose image/model mount, init, scoring, schema, identity/network and capacity separately.

### Progressive rollout and rollback

Deploy candidate with zero/small traffic, send mirrored/synthetic/canary requests, compare quality/latency/error/cost, increase traffic by gate, then retain old deployment until observation completes. Traffic percentage does not guarantee representative users; use explicit cohort/header routing where supported/needed. Roll back traffic immediately on breach, then reconcile in-flight/batch output.

> **Related item:** Model rollback requires compatible feature pipeline, schema and environment—not just a previous model file. Preserve the deployable dependency set.

## Monitor drift and production performance

Distinguish:

- data drift: production feature distribution changes;
- prediction drift: output distribution changes;
- concept drift: relationship between input and ground truth changes;
- data quality/schema: missing/type/range/freshness violations;
- operational: errors, latency, throughput, saturation and cost.

Configure model/data monitoring according to current Azure ML support and collect ground truth when it arrives. A statistical drift alert is a review signal, not proof performance fell. Thresholds need baseline/window, minimum volume, seasonality and owner. See [model monitoring](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-monitoring?view=azureml-api-2).

Retrain/alert triggers can be schedule, new approved data, drift/quality threshold or measured performance degradation. Gate retraining with validation, leakage checks, responsible metrics and approval; never automatically promote merely because a job succeeded.

### Build an actionable production monitor

Define each monitor as `signal -> baseline/window -> threshold -> minimum volume -> owner -> action -> recovery proof`.

| Signal | Evidence | Likely action |
|---|---|---|
| request error/latency/saturation | endpoint metrics, deployment logs, instance utilization and dependency trace | scale or roll back; correct image/scoring/dependency |
| schema/data quality | missing/type/range/category/freshness checks | quarantine/stop pipeline; repair producer/contract |
| feature/data drift | reference-versus-current distribution by meaningful segment | investigate seasonality/source/process; label and evaluate before retraining |
| prediction drift | score/class distribution and confidence/calibration | investigate input/model/use change; collect outcomes |
| measured model performance | joined prediction and delayed ground truth, including subgroup | retrain/recalibrate/rollback under accepted gate |
| feature skew | training versus online feature value/version/timestamp | repair retrieval specification and backfill/replay |

Ground-truth joins need stable prediction/entity IDs, prediction time, model/feature version and outcome window. Account for delayed, missing and censored labels. Compare cohorts and seasonality; a global mean can hide one harmed group.

### Troubleshoot an endpoint from evidence

1. Identify endpoint, deployment, model/environment/code versions, request ID and change window.
2. Separate provisioning failure from container initialization, readiness, request schema, scoring code, identity/network and capacity.
3. Inspect deployment events/logs and invoke with a known contract sample under the actual auth path.
4. Confirm model mount/download, environment imports, input/output signature and external feature/data connectivity.
5. For intermittent failures compare payload size/shape, concurrency, timeout, memory/CPU and downstream throttle.
6. Shift traffic to the healthy deployment when the SLO is at risk; preserve candidate evidence.
7. Correct and rerun smoke, contract, load and quality gates; reconcile batch/ambiguous responses.

Batch endpoints add input enumeration, mini-batch partitioning, retry/error threshold, output aggregation and datastore-write concerns. A completed batch job can still have skipped/failed records; reconcile input IDs to outputs and quarantine.

---

# 3. Design and implement a GenAIOps infrastructure (20–25%)

## Provision current Microsoft Foundry environments

Current material uses **Microsoft Foundry**; older sources may say Azure AI Foundry/Studio. A Foundry resource/project organizes model deployments, connections, agents/apps, evaluations and collaboration. Define subscriptions/resource groups, region, project/environment separation, managed identity/RBAC, connections, Key Vault/storage/search/data dependencies, network isolation, diagnostics, quota and policy as code. Start at [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/).

Use Bicep/CLI with current resource API/provider because the platform evolves. Keep connection targets/config versioned and credentials in identity/secret stores. Private networking must cover model, project, storage/search, registry, monitoring, package/build and deployment paths. Test DNS and least privilege from the actual runtime.

## Select and deploy foundation models

Evaluate model modality, quality on representative data, context/output, structured/tool output, safety, latency, throughput/quota, region/residency, version lifecycle and cost. Use the [Foundry Models overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) and model-specific deployment documentation.

- Serverless API deployment provides managed inference for supported models with provider/billing/region constraints.
- Managed compute deployment gives configuration/control for supported open/custom models with image/compute/scaling operations.
- Azure OpenAI/Foundry Models deployment types may include standard/global/data-zone and provisioned throughput; verify exact model/region.

Provisioned throughput reserves capacity for predictable high-volume demand. Size with measured prompt/output tokens, workload shape and model/version; quota and PTU are not interchangeable. Monitor utilization, latency and spillover/fallback policy. See [provisioned throughput concepts](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/provisioned-throughput).

Version deployment name -> exact model version/config, test new version in parallel, run evaluation/load/safety gates, route progressive traffic and retain rollback. Do not let an automatic model-version upgrade silently change quality without an accepted policy and monitoring.

### Define a model release contract

For each foundation-model deployment record:

- provider/model/version/deployment type, region and content-filter/safety configuration;
- input modalities, context/output and structured/tool-call contract;
- quota/PTU, concurrency, retry/fallback and data-zone/residency constraints;
- representative quality/safety evaluation run and dataset version;
- p50/p95/p99 latency, throughput, token/cost and saturation evidence;
- model-version upgrade policy, deprecation notice owner and rollback target.

A fallback model is a separate quality behavior. Evaluate it and make feature degradation visible rather than silently routing to an untested cheaper/different model. Bounded retries should respect provider retry hints and an overall latency/cost budget; retrying a safety rejection or invalid request is not resilience.

### Operate prompts and connections

Validate template variables and types before sending. Use structured output/schema validation and a controlled repair/refusal path. Tool definitions are privileged interfaces: narrow operations and parameters, validate model-selected arguments, enforce authorization outside the model and require confirmation for material writes.

Connections reference services/data/model endpoints and credentials/identity. Grant project/runtime only required use, separate development from production, rotate secrets if unavoidable and audit who changed or invoked them. A prompt author should not automatically administer production identities or deployment traffic.

## Version prompts as production artifacts

A prompt artifact includes system/developer instructions, template variables, tool/schema definitions, retrieval configuration, examples, safety/output rules, model/deployment parameters and version. Store text/config in Git, keep secrets/data out, lint required variables and test rendering/injection.

Create prompt variants to test a hypothesis. Evaluate on the same versioned dataset with quality/safety/latency/token cost, including subgroup and adversarial cases. Change one major factor when diagnosing. Promote prompt + model + retrieval + safety bundle rather than a prompt string alone.

> **Related item:** A prompt-only rollback cannot recover behavior if model version, index, tool or content filter changed. Release and observe the complete AI configuration bundle.

---

# 4. Implement generative AI quality assurance and observability (10–15%)

## Build evaluation datasets and mappings

Create representative, boundary, failure, multilingual/domain and adversarial examples. Map dataset fields explicitly to query, response, context, ground truth and metadata. Version source/license/consent, sampling, redaction, expected output/rubric and splits. Prevent evaluation contamination and production personal data leakage.

Metrics:

- groundedness: response supported by provided context;
- relevance: response addresses the query;
- coherence: logically consistent/readable response;
- fluency: linguistic quality;
- retrieval relevance/recall and citation correctness for RAG;
- task-specific exact/rubric score;
- safety categories/severity for harmful content.

Metrics may use model judges and are probabilistic/version-sensitive. Calibrate to human-reviewed examples, record evaluator model/prompt/version and never treat one score as truth. Use [Foundry evaluation](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app) and [risk and safety evaluation](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/risk-safety-evaluators).

Automate offline evaluation in CI/release with minimum/maximum thresholds, confidence/sample minimum, regression comparison and hard safety gates. Custom evaluators must have tested rubric, stable output, failure handling and version.

## Observe applications and agents continuously

Instrument trace from user request through orchestration/agent/tool, retrieval and model call. Record deployment/config version, safe query hash/tenant, model, prompt/retrieval/index version, tool names/status, candidate/citation IDs, token usage, latency, retry/throttle and safety/evaluation results. Avoid raw secrets/PII/prompts unless explicitly governed.

Monitor p50/p95/p99 end-to-end and model/tool latency, throughput, errors, rate limit, tokens and estimated cost, retrieval empty/quality, safety/refusal and agent loop/tool failures. Correlate Azure resource metrics and application traces. Use [Foundry tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) and the [agent monitoring dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard).

Online evaluation uses sampled production interactions with privacy/sampling/latency/cost controls. It complements, not replaces, a stable offline regression set and human/business feedback. Alert with owner/runbook and compare by release cohort.

### Turn metrics into a release policy

Use hard and comparative gates. A hard safety/severe-regression threshold blocks regardless of average quality. Comparative gates can require candidate relevance/groundedness to be no worse than baseline within an accepted margin while latency and cost remain in budget. Define how evaluator failures, missing fields and too-small samples fail closed.

| Evaluation layer | Examples | Main failure it catches |
|---|---|---|
| deterministic contract | JSON/schema, citation IDs, required refusal, tool argument constraints | unusable/malformed or unauthorized action |
| retrieval | recall@k, MRR/nDCG, context precision, ACL correctness | evidence never reaches generator or leaks |
| response quality | groundedness, relevance, task completion, citation correctness | plausible but unsupported/unhelpful output |
| safety/security | harm categories, prompt injection, sensitive disclosure, tool abuse | unacceptable content or action |
| system | latency, throughput, error, tokens/cost, loop/step count | production SLO or economic failure |
| human/business | rubric, escalation, resolution, acceptance by subgroup | proxy metric does not match real outcome |

Retain per-row results, not only averages, so regression examples are explainable. Stratify by language, tenant/use case, complexity and safety category. Freeze a regression set and add newly discovered production failures without letting the candidate train on the final holdout.

### Debug agent and RAG traces safely

Follow one trace: entry -> agent/orchestrator decision -> retrieval query/filter/candidates -> model input/output metadata -> tool selection/arguments/result -> final response/evaluation. Diagnose repeated tool loops, wrong tool choice, invalid parameters, empty/unauthorized retrieval, rate limit and context overflow separately. Record hashes/IDs instead of sensitive bodies where possible and protect Application Insights access/retention because traces can contain customer data.

---

# 5. Optimize generative AI systems and model performance (10–15%)

## Optimize RAG from a labeled baseline

Separate retrieval failure from generation failure. Create labeled queries with relevant source/chunk/citation and measure recall@k, precision@k, MRR/nDCG, groundedness/citation correctness, answer quality, latency and cost.

Tune:

- parsing and chunk size/overlap with document structure;
- embedding model/dimensions and re-embedding version strategy;
- vector metric/index/search effort/top-k;
- metadata/security filters before context;
- lexical + semantic hybrid fusion and reranking;
- similarity/no-evidence threshold and refusal;
- context deduplication/diversity/order/token budget;
- prompt/model parameters.

Changing chunker or embedding model requires versioned re-index/evaluation. Similarity thresholds are model/corpus-specific. Hybrid search improves exact identifiers/rare terms while vector handles paraphrase. A/B tests need stable assignment, guardrails, sufficient sample and primary metric; never expose unauthorized documents as an experiment.

### Diagnose RAG by stage

- **No relevant candidate:** check ingestion completeness, ACL/metadata, source version, chunking and query embedding/model compatibility.
- **Relevant candidate below top-k:** compare exact ground truth, ANN effort/index, filter placement, lexical path and reranker.
- **Relevant context but wrong answer:** inspect context ordering/token truncation, prompt, model capability and contradictory/stale sources.
- **Correct but expensive/slow:** reduce candidate/context safely, cache approved embeddings/results, parallelize bounded calls, choose model/deployment and tune index after quality baseline.
- **Citation mismatch:** bind citation IDs to supplied chunks and validate generated citations; never allow the model to invent a source URL.
- **Cross-tenant result:** stop release, preserve trace, correct pre-retrieval authorization/index partition and test adversarial ACL cases—not a post-answer filter.

Build an experiment table with one row per configuration bundle and columns for source/index, chunker, embedding, lexical/vector parameters, reranker, prompt/model, quality/safety, latency and cost. This prevents “tuning” from becoming undocumented simultaneous changes.

See [RAG concepts](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation) and [Azure AI Search relevance](https://learn.microsoft.com/en-us/azure/search/search-relevance-overview).

## Fine-tune only for the right problem

Fine-tuning adapts behavior/style/task patterns; it does not reliably inject fresh factual knowledge—use RAG for changing knowledge. Compare prompt/examples/RAG/smaller model before fine-tuning.

Design dataset with licensed/consented representative examples, format/schema, train/validation/test split, deduplication, balance, safety/redaction and provenance. Synthetic data can cover rare cases but may amplify generator bias/artifacts. Label it, validate against real examples, preserve generating model/prompt/version and avoid test contamination.

Advanced methods can include supervised fine-tuning, preference-based alignment or parameter-efficient techniques where the selected platform/model supports them. Choose from task, data, compute, risk and deployment support—not fashion. Track base model/version, dataset/hash, method/hyperparameters, job/checkpoint, metrics and safety.

Manage dev-to-production like any release: register candidate, offline/human/safety evaluation, load/cost test, canary/A-B, monitor drift/quality and retain base/previous deployment rollback. Watch overfitting, catastrophic forgetting, subgroup degradation, memorization/privacy and base-model retirement. Use current [Foundry fine-tuning guidance](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning).

### Operate the fine-tuning dataset and checkpoints

Define a schema validator and stable example ID; deduplicate near-duplicates across splits; inspect label/rubric agreement; cap repeated templates; balance important groups and retain an untouched realistic test. Remove secrets and content without allowed training rights. For synthetic rows retain parent/source intent and generating configuration so they can be excluded in analysis.

Monitor training/validation loss and task metrics for divergence, but select a checkpoint from downstream evaluation rather than lowest loss alone. Compare base and candidate on retained capabilities and safety, not only the tuned task. Version inference prompt because a tuned model can require a different instruction format.

Production monitoring should distinguish base/model version, tuned checkpoint and traffic cohort. Define triggers for rollback, retraining and dataset review, and a plan for base-model deprecation or unavailable tuning API. Archive lineage/evaluation even after disabling deployment.

> **Related item:** A higher offline judge score can hide worse latency, cost, safety or subgroup performance. Promotion is a multi-metric policy with explicit non-negotiable guardrails.

---

# 6. Integrated scenarios and labs

## Scenario A: regulated classification model

Version data, feature spec, environment and training component; use MLflow and pipeline to compare AutoML/sweep candidates; gate on test, subgroup/fairness, latency and explainability; register MLflow model; canary managed online deployment; monitor operational/data/prediction and delayed outcome performance; retrain only through the same gates. **Trap:** drift alone auto-promotes a worse model.

## Scenario B: enterprise RAG assistant

Provision private Foundry project/search/data/monitoring with managed identity and IaC; version model/prompt/chunker/embedding/index/safety; evaluate groundedness/relevance/citation/safety/latency/cost; deploy candidate cohort; trace retrieval/tools/model; tune hybrid/top-k/rerank from labeled evidence. **Trap:** post-retrieval ACL filtering leaks candidates and destroys recall.

## Scenario C: high-volume fine-tuned service

Compare prompt/RAG/base with fine-tuning; govern real/synthetic dataset; register evaluation lineage; size provisioned throughput from load; canary new fine-tuned version; monitor tokens, utilization, quality/safety and fallback. **Trap:** model version changes while deployment name stays constant and no bundle/version evidence exists.

## Lab 1: secure workspace and IaC

Deploy dev workspace/dependencies/identity/network with Bicep/CLI; create datastore/data/compute; prove allowed/denied paths; run lint/what-if through GitHub OIDC; capture DNS/outbound/diagnostic evidence.

## Lab 2: reusable assets and registry

Create pinned environment and component; version immutable data; compose pipeline; share approved model/component/environment through registry; change hidden/mutable input to demonstrate why lineage/caching fails.

## Lab 3: training, MLflow and tuning

Refactor notebook into script; log code/data/environment/parameters/metrics; compare baseline, AutoML and sweep; run distributed option only after profile; test leakage and reproducibility.

## Lab 4: model governance and deployment

Package feature retrieval spec and MLflow model; evaluate responsible/subgroup metrics; register/archive versions; deploy online and batch; inject schema/init/identity/capacity failures; canary, promote and roll back.

## Lab 5: monitoring and retraining

Generate quality, data/prediction/concept drift and operational issues separately; configure signals/thresholds; trigger alert/retraining candidate; prove validation prevents automatic bad promotion.

## Lab 6: Foundry infrastructure, model and prompt release

Provision dev project/identity/network via IaC; deploy two model versions/deployment types; version prompt bundle in Git; evaluate variants; load test standard/provisioned assumptions; execute progressive release/rollback.

## Lab 7: evaluation and observability

Build mapped versioned evaluation set; run built-in quality and risk/safety plus custom evaluator; calibrate against human labels; automate gates; trace retrieval/agent/tool/model; query latency/tokens/cost/error and debug failure.

## Lab 8: RAG and fine-tuning optimization

Build labeled retrieval set; baseline exact/vector/hybrid; vary chunk/embedding/top-k/threshold/rerank one at a time; A/B safely; create governed synthetic fine-tune supplement; compare base/RAG/fine-tuned on quality/safety/latency/cost and deploy only if justified.

---

# 7. Original knowledge checks

1. Distinguish workspace, datastore, data asset, environment, component, compute and registry.
2. Why does a versioned data asset pointing to mutable files fail reproducibility?
3. Map submitter, compute, pipeline and endpoint identities to data-plane permissions.
4. Which private workspace flows require DNS/outbound beyond the workspace endpoint?
5. What should Bicep versus Azure ML CLI/YAML deploy?
6. Why is GitHub OIDC safer than a client secret, and what subject/scope still matters?
7. Which evidence makes an MLflow run reproducible?
8. Compare AutoML with hyperparameter sweep and untouched test evaluation.
9. When does distributed training cost more without reducing time?
10. What makes a pipeline component deterministic and safely cacheable?
11. Why package a feature retrieval specification with the model?
12. Compare an MLflow model artifact, registered model version and deployment.
13. Which responsible-AI metrics can block an aggregate-accuracy winner?
14. Choose online versus batch endpoint for two inference SLOs.
15. What must remain compatible for rollback beyond the model file?
16. Distinguish data, prediction, concept and operational drift.
17. Why must drift trigger review/retraining rather than direct promotion?
18. Define a Foundry project boundary and its identity/network dependencies.
19. Compare serverless API, managed compute and provisioned throughput model deployment.
20. How can an automatic foundation-model update break a stable deployment name?
21. What belongs in a versioned prompt release bundle?
22. How do you compare prompt variants without confounding model/retrieval changes?
23. Build a mapped evaluation record for query/context/response/ground truth.
24. Distinguish groundedness, relevance, coherence and fluency.
25. Why must a model judge be versioned and calibrated with humans?
26. Which harmful-content tests and release gates fit a domain?
27. Which trace spans connect retrieval, agent tools and model response?
28. How do sampling/privacy controls affect continuous evaluation?
29. Separate retrieval failure from generation failure using metrics.
30. How do chunk size, top-k, threshold and reranking trade quality/latency/cost?
31. Why combine lexical and semantic search?
32. Design a secure A/B test with rollback and sufficient sample.
33. When is RAG better than fine-tuning for knowledge?
34. Which synthetic-data provenance and validation prevent contamination/artifacts?
35. Compare supervised, preference and parameter-efficient tuning considerations.
36. Which quality, safety, subgroup, latency and cost gates govern a fine-tuned release?

---

# Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Choose one primary path, build the labs and use targeted material for gaps. Times are published when available or labeled estimates. Avoid dumps and recalled/live exam questions.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official AI-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300) | Public | 30–60 min | Authoritative scope and lifecycle |
| [AI-300T00 Microsoft Learn course](https://learn.microsoft.com/en-us/training/courses/ai-300t00) | Public self-study; paid instructor option | 4 days; 12h24 displayed paths plus labs | Primary MLOps/GenAIOps path |
| [AI Skills Navigator Practice Assessment](https://aiskillsnavigator.microsoft.com/en-us/certifications/microsoft-certified-associate/machine-learning-operations-engineer) | Free account/sign-in | 45–90 min plus remediation (estimate) | Official diagnostic |
| [Azure MLOps v2 solution accelerator](https://github.com/Azure/mlops-v2) | Public | 8–20 hours selectively (estimate) | Official reference architectures and automation; verify current SDK/IaC |
| [Azure ML examples](https://github.com/Azure/azureml-examples) | Public | 10–30 hours selectively (estimate) | CLI/SDK jobs, pipelines and endpoints |
| [Foundry samples](https://github.com/azure-ai-foundry/foundry-samples) | Public | 8–20 hours selectively (estimate) | Current evaluation, tracing and GenAIOps examples |
| [O'Reilly MLOps/LLMOps Bootcamp](https://www.oreilly.com/live-events/mlopsllmops-bootcamp/0642572182861/0642572243333/) | Paid live/subscription | Verify current multi-session schedule; roughly 8–16 hours (estimate) | Broad lifecycle supplement, not AI-300-specific; map to Azure objectives |
| [Udemy AI-300 MLOps & GenAIOps preparation](https://www.udemy.com/course/ai-300-mlops-genaiops-engineer-exam-preparation/) | Paid; price varies | Verify displayed duration; 8–16 hours (estimate) | Dedicated 2026 course with labs/practice; independently verify claims |
| [Udemy AI-300 practice tests](https://www.udemy.com/course/ai-300-operationalizing-ml-and-generative-ai-practice-tests/) | Paid; price varies | Six tests / 911 questions; 12–25 hours with review (estimate) | Large question bank; sample selectively, verify explanations, reject dumps |
| [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor) | Public | 3–10 hours selectively (estimate) | Current Azure ML, Foundry, evaluation and operations sessions |
| This guide's eight labs | Azure access; costs vary | 30–55 hours (estimate) | Reproducibility, safe rollout, monitoring, evaluation and optimization evidence |

No dedicated current AI-300 Pluralsight, MeasureUp or Whizlabs product was found on the public pages checked. Recheck later rather than relabeling DP-100/AI-102 content. Use the Microsoft assessment first, then remediate objectives rather than memorize answers.

## Practical sequence

1. Map every official objective to an artifact and failure test.
2. Complete the two Microsoft paths or one current structured course.
3. Build Labs 1–5 for MLOps; retain full run-to-deployment/rollback evidence.
4. Build Labs 6–8 for GenAIOps; retain evaluation/tracing/RAG/fine-tuning comparisons.
5. Take the official assessment once and remediate by objective.
6. Recheck blueprint, model/SDK/evaluation/network features and lifecycle before the exam.

---

*This independent guide uses public sources and original synthesis and is not endorsed by Microsoft or any vendor.*
