---
exam_code: AI-300
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AI-300 Operationalizing Machine Learning and Generative AI Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ai-300-coverage-record). The [official AI-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300) is authoritative.

**Current baseline:** Official page last updated March 5, 2026; no separate skills-effective date is published.<br>
**Upcoming blueprint change:** None announced as of September 28, 2026.<br>
**Lifecycle status:** Active; no retirement or replacement was announced.<br>
**Exam page:** [Machine Learning Operations Engineer Associate](https://learn.microsoft.com/en-us/credentials/certifications/operationalizing-machine-learning-and-generative-ai-solutions/) · 120-minute assessment · English on the current exam page; course languages are separate.<br>
**Official course:** [AI-300T00 Operationalize machine learning and generative AI solutions](https://learn.microsoft.com/en-us/training/courses/ai-300t00) · four instructor-led days; 12 course languages.<br>
**Practice:** Microsoft directs candidates to the [AI Skills Navigator Practice Assessment](https://aiskillsnavigator.microsoft.com/en-us/certifications/microsoft-certified-associate/machine-learning-operations-engineer); sign-in is required.

**September 28 deep review:** All 58 detailed objectives were mapped across 14 groups; the accepted blueprint is unchanged. Six worked examples, ten labs and 48 explained knowledge checks deepen the release and troubleshooting decisions. The [review report](../docs/research/2026-09-28-ai-300-deep-review.md) records source boundaries and validation. No cloud, model, SDK or paid-course execution was performed.

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

## 1. Design and implement an MLOps infrastructure (15–20%)

**Use the supported toolchain.** Azure ML CLI v1 support ended September 30, 2025; Python SDK v1 support ended June 30, 2026. Existing workflows can continue operating, but that does not restore support. Inventory `azure-cli-ml`/`azureml-core`, migrate to the `ml` extension/`azure-ai-ml`, and rebuild/test environments instead of mixing v1 and v2 examples. The legacy `azureml` name in a different package is not sufficient by itself to identify SDK v1. [SDK/CLI lifecycle](https://learn.microsoft.com/en-us/azure/machine-learning/introduction?view=azureml-api-1)

### Build the Azure Machine Learning resource boundary

An Azure Machine Learning workspace organizes jobs, assets, endpoints, connections and collaboration while depending on Azure Storage, Key Vault, Container Registry and monitoring resources. Start with the [workspace architecture](https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace?view=azureml-api-2) and [secure workspace guidance](https://learn.microsoft.com/en-us/azure/machine-learning/concept-secure-network-traffic-flow?view=azureml-api-2).

Separate dev/test/prod workspaces when access, data, quota, experimentation or blast radius requires it. Define region, dependent resources, public/private network mode, managed network/private endpoints, DNS, outbound rules, encryption, diagnostics, tags/budget and managed identities in IaC.

#### Datastores and data assets

A datastore stores connection information to Azure storage/data source; it is not the data itself. Prefer identity-based access and never embed keys in YAML/source. A data asset supplies a versioned reference/contract (URI file/folder or MLTable) for reproducible jobs. See [datastores](https://learn.microsoft.com/en-us/azure/machine-learning/concept-data?view=azureml-api-2) and [data assets](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-data-assets?view=azureml-api-2).

Version does not freeze a mutable external path. Preserve immutable snapshot/version/hash and schema/quality evidence. Prevent training/test leakage and enforce data classification/retention.

#### Compute targets

- Compute instance: individual interactive development; stop when idle and do not make it a production scheduler.
- Compute cluster: autoscaling CPU/GPU training and batch workloads; choose VM size, min/max nodes, idle scale-down, identity and network.
- Serverless compute: managed per-job compute where supported; verify image/package/network/data access.
- Attached/external compute: use only for a requirement and account for its patching/identity/telemetry boundary.

Size from measured training duration, distributed strategy, memory/GPU utilization, data throughput, quota and cost. Min zero saves idle cost but adds startup latency.

#### Identity and access

Use Microsoft Entra groups and managed identities. Separate workspace administration, data scientist asset/job work, pipeline deployment and endpoint runtime identities. A control-plane role does not automatically grant storage/registry/Key Vault data access. Test positive and negative operations and prefer least-privileged built-in/custom roles. Review [workspace access management](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-assign-roles?view=azureml-api-2).

> **Related item:** A job submitted by a permitted user can execute as a different compute/workspace identity. Trace both submission authorization and runtime access to data, registry and secrets.

### Create reusable workspace assets

An **environment** versions Docker image/build context plus Conda dependencies. Pin packages/base images, scan, test imports and record digest. A **component** defines inputs, outputs, code, command and environment as a reusable pipeline step. A **pipeline** composes components and their data dependencies. See [environments](https://learn.microsoft.com/en-us/azure/machine-learning/concept-environments?view=azureml-api-2) and [components](https://learn.microsoft.com/en-us/azure/machine-learning/concept-component?view=azureml-api-2).

Avoid notebook-only hidden state, mutable `latest` environments and hard-coded workspace paths. Components should be deterministic from declared input/version/parameter, write declared outputs and expose meaningful metrics.

Azure Machine Learning registries share versioned models, components and environments across workspaces/regions. Define promotion ownership, immutability, replication/support and consumer compatibility; registry sharing is not approval by itself. Use [registries](https://learn.microsoft.com/en-us/azure/machine-learning/concept-machine-learning-registries-mlops?view=azureml-api-2).

### Provision with Bicep, CLI and GitHub Actions

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

This is a workflow fragment, not a complete workflow: place steps inside a job with its runner, protected environment and declared variables. The tagged action is illustrative; pin an approved commit in production. `az ml job create` submits a job. A later gate must wait, verify terminal success, read the expected evaluation artifact and reject missing/failed metrics before registration or deployment. Submission success is not training or quality success.

IDs are configuration values rather than credentials, but repository/environment permissions remain sensitive. Add Bicep lint/what-if, policy/security scan, asset validation, evaluation threshold and deployment health/rollback gates.

### Restrict networking and manage Git

Private endpoints/managed virtual network do not automatically solve DNS or dependent-resource access. Map control, data, image/package, identity, monitoring and model endpoints. Provide approved outbound rules/package mirror and a managed self-hosted runner if public GitHub-hosted runners cannot reach private resources.

Use small branches/commits for source, component/YAML, environment lock, tests, prompt and IaC. Store large data/models in versioned managed storage/registry, not Git. PR review is valuable but a solo flow still needs automated validation before direct merge. Never commit secrets, connection strings or production samples.

---

## 2. Implement machine learning model lifecycle and operations (25–30%)

### Make experiments reproducible with MLflow

MLflow tracking records runs, parameters, metrics, tags and artifacts. Azure ML jobs can integrate MLflow without manually managing a tracking server. Log data/version, code commit, environment, seed, feature spec, algorithm/parameters, metrics by split and artifacts. See [MLflow tracking in Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2).

Notebook exploration is appropriate for profiling/hypothesis; production logic belongs in scripts/components with declared arguments, environments and tests. A notebook “Run all” result is not reproducibility evidence.

#### AutoML and hyperparameter tuning

Automated ML explores algorithms/featurization within task, metric, compute, time/trial and validation constraints. It does not choose the business objective or prevent leakage. Inspect the winning pipeline, explainability, latency/size and subgroup behavior. Use [AutoML concepts](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml?view=azureml-api-2).

Sweep jobs search a defined parameter space using random/grid/Bayesian sampling and early termination such as bandit/median/truncation policies. Define primary metric direction, limits, concurrent trials and deterministic evaluation. A validation winner still needs untouched test and responsible-AI checks. See [hyperparameter tuning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2).

#### Distributed training

Use MPI, PyTorch or TensorFlow distributed configuration only after profiling. Align process-per-node, node count, GPU topology, communication backend, data sharding, checkpoint and failure/restart. More GPUs can slow training when input/communication dominates. Measure throughput, scaling efficiency, GPU/CPU/memory/network, convergence and cost.

### Build training pipelines

Typical graph: validate data -> engineer/materialize features -> train -> evaluate -> register conditional candidate. Component caching/reuse requires identical declared inputs/settings and deterministic behavior; mutable external data or hidden dependency makes reuse unsafe.

Reuse requires `is_deterministic=true`, no forced rerun, and matching code snapshot, environment, inputs/parameters, outputs and run settings. Reused nodes display the previous output/logs/metrics. A forced-rerun pipeline's child jobs are not reusable by other jobs. Compare these inputs before assuming a fast run performed new training; a mutable path or external API can return changed data without changing its declared reference. [Pipeline reuse diagnostics](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-debug-pipeline-reuse-issues?view=azureml-api-2)

Package a **feature retrieval specification** with the model artifact when the serving system needs the same feature definitions/source/key/timestamp behavior as training. Prevent online/offline skew, leakage and point-in-time errors; version transformations and feature sources with the model.

For the managed feature-store path, the specification references registered feature-set versions and can span stores. Training uses observation entity keys/timestamps for a point-in-time join; package the generated specification with the model so inference can resolve the same feature contract. A model signature listing column names alone does not capture that retrieval lineage. Record freshness/materialization behavior and availability-time assumptions as well as event time. [Feature retrieval contract](https://learn.microsoft.com/en-us/azure/machine-learning/feature-retrieval-concepts?view=azureml-api-2)

Compare runs on the same evaluation data and business constraints: predictive metric, calibration, subgroup fairness, robustness, latency, memory/size and cost. Do not promote on one aggregate accuracy.

### Register and govern models

An MLflow model packages flavor/signature/dependencies/artifacts; registration creates an immutable versioned model asset. Record stage/status/owner, lineage, intended use, evaluation, approval and compatibility. Archive/deprecate to remove normal selection without erasing evidence required for rollback/audit. Use [MLflow models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow-models?view=azureml-api-2) and [model management](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-models?view=azureml-api-2).

Responsible evaluation covers fitness, subgroup/fairness, error analysis, explainability, privacy/security and harm appropriate to the use. The [Responsible AI dashboard](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2) combines supported analysis but does not make the deployment responsible automatically.

**Dashboard support is narrower than responsible-AI evaluation.** The Azure ML dashboard currently supports tabular regression/classification with registered scikit-learn MLflow implementations, pandas/Parquet input and up to 5,000 visualized points. Its documented limitations exclude AutoML MLflow models and registered AutoML models through the UI. Do not assume every AutoML/deep-learning/generative candidate can enter this dashboard unchanged; select supported tools and retain subgroup evidence independently.

### Deploy online and batch endpoints

Managed online endpoints serve low-latency requests through deployments; batch endpoints process large asynchronous datasets/jobs. Choose from latency/throughput, input size, freshness, concurrency, retry, cost and result-delivery needs. See [online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2) and [batch endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-batch?view=azureml-api-2).

Configure model, code/scoring contract, environment, instance/compute, min/scale, identity, networking, auth, request/response schema, timeout and logging. Test locally where useful, then endpoint smoke, contract, load, security and failure tests. Diagnose image/model mount, init, scoring, schema, identity/network and capacity separately.

#### Progressive rollout and rollback

Deploy candidate with zero/small traffic, send mirrored/synthetic/canary requests, compare quality/latency/error/cost, increase traffic by gate, then retain old deployment until observation completes. Traffic percentage does not guarantee representative users; use explicit cohort/header routing where supported/needed. Roll back traffic immediately on breach, then reconcile in-flight/batch output.

For managed online endpoints, **mirroring copies requests and discards the shadow response from the client path**; it does not route that percentage of users to the candidate. It supports one shadow deployment and at most 50% mirrored traffic; Kubernetes online endpoints do not support it. Mirrored scoring still executes: isolate writes/external tool effects and budget extra capacity. A routed canary exposes candidate responses and needs separate outcome/rollback criteria. [Safe rollout and mirroring](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-safely-rollout-online-endpoints?view=azureml-api-2)

> **Related item:** Model rollback requires compatible feature pipeline, schema and environment—not just a previous model file. Preserve the deployable dependency set.

### Monitor drift and production performance

Distinguish:

- data drift: production feature distribution changes;
- prediction drift: output distribution changes;
- concept drift: relationship between input and ground truth changes;
- data quality/schema: missing/type/range/freshness violations;
- operational: errors, latency, throughput, saturation and cost.

Configure model/data monitoring according to current Azure ML support and collect ground truth when it arrives. A statistical drift alert is a review signal, not proof performance fell. Thresholds need baseline/window, minimum volume, seasonality and owner. See [model monitoring](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-monitoring?view=azureml-api-2).

Enable and verify production data collection before configuring the monitor. Azure ML online-endpoint collection can supply inference inputs/outputs; for batch or external hosting, supply the collected data yourself. Built-in statistical signals primarily target supported tabular tasks; custom signals cover other contracts. Delayed-label performance is a separate join from data drift. Keep reference and production windows disjoint; account for ingestion delay and label availability instead of silently measuring only the easiest early outcomes.

Retrain/alert triggers can be schedule, new approved data, drift/quality threshold or measured performance degradation. Gate retraining with validation, leakage checks, responsible metrics and approval; never automatically promote merely because a job succeeded.

#### Build an actionable production monitor

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

#### Troubleshoot an endpoint from evidence

1. Identify endpoint, deployment, model/environment/code versions, request ID and change window.
2. Separate provisioning failure from container initialization, readiness, request schema, scoring code, identity/network and capacity.
3. Inspect deployment events/logs and invoke with a known contract sample under the actual auth path.
4. Confirm model mount/download, environment imports, input/output signature and external feature/data connectivity.
5. For intermittent failures compare payload size/shape, concurrency, timeout, memory/CPU and downstream throttle.
6. Shift traffic to the healthy deployment when the SLO is at risk; preserve candidate evidence.
7. Correct and rerun smoke, contract, load and quality gates; reconcile batch/ambiguous responses.

Batch endpoints add input enumeration, mini-batch partitioning, retry/error threshold, output aggregation and datastore-write concerns. A completed batch job can still have skipped/failed records; reconcile input IDs to outputs and quarantine.

---

## 3. Design and implement a GenAIOps infrastructure (20–25%)

### Provision current Microsoft Foundry environments

Current material uses **Microsoft Foundry**; older sources may say Azure AI Foundry/Studio. A Foundry resource/project organizes model deployments, connections, agents/apps, evaluations and collaboration. Define subscriptions/resource groups, region, project/environment separation, managed identity/RBAC, connections, Key Vault/storage/search/data dependencies, network isolation, diagnostics, quota and policy as code. Start at [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/).

Use Bicep/CLI with current resource API/provider because the platform evolves. Keep connection targets/config versioned and credentials in identity/secret stores. Private networking must cover model, project, storage/search, registry, monitoring, package/build and deployment paths. Test DNS and least privilege from the actual runtime.

#### Network mode is part of the release contract

Foundry's managed VNet governs **agent outbound access**; inbound private access and dependent-resource identity remain separate decisions. `AllowInternetOutbound` permits internet access; `AllowOnlyApprovedOutbound` restricts destinations through approved rules. Current guidance supports prompt/hosted agents with the Responses API in listed regions. The portal does not create this managed network; use the supported IaC/REST path and verify provisioning/endpoint approval.

Enabling isolation cannot be undone in place, approved-only mode cannot be relaxed to internet mode, and a custom-VNet deployment has no in-place upgrade to managed VNet. FQDN rules use ports 80/443 and a managed firewall with its own cost. Validate these choices before provisioning; a Bicep deployment succeeding does not prove DNS, private endpoint approval or denied egress. [Managed network requirements](https://learn.microsoft.com/en-us/azure/foundry/how-to/managed-virtual-network)

### Select and deploy foundation models

Evaluate model modality, quality on representative data, context/output, structured/tool output, safety, latency, throughput/quota, region/residency, version lifecycle and cost. Use the [Foundry Models overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) and model-specific deployment documentation.

- Serverless API deployment provides managed inference for supported models with provider/billing/region constraints.
- Managed compute deployment gives configuration/control for supported open/custom models with image/compute/scaling operations.
- Azure OpenAI/Foundry Models deployment types may include standard/global/data-zone and provisioned throughput; verify exact model/region.

Provisioned throughput reserves capacity for predictable high-volume demand. Size with measured prompt/output tokens, workload shape and model/version; quota and PTU are not interchangeable. Monitor utilization, latency and spillover/fallback policy. See [provisioned throughput concepts](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/provisioned-throughput).

Quota, deployment capacity and a reservation are different. PTU quota is scoped by subscription, region and deployment type; it does not reserve model-version capacity. A reservation discounts matching usage and also does not guarantee capacity. Size from peak RPM, input/output tokens, cache behavior, model-specific throughput and scale increments, then benchmark. [Sizing methodology](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/provisioned-throughput-sizing)

**Spillover is not an arbitrary fallback model.** Current Azure OpenAI provisioned spillover targets a standard deployment of the same model/version in the same Foundry resource. Deployment-level configuration takes precedence over the per-request header. Supported overflow/error conditions can redirect requests, but the target can fail too; inspect actual serving-deployment/spillover headers and standard-deployment charges. Preserve residency and evaluation requirements across both deployment types. [Spillover behavior](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/spillover-traffic-management)

Version deployment name -> exact model version/config, test new version in parallel, run evaluation/load/safety gates, route progressive traffic and retain rollback. Do not let an automatic model-version upgrade silently change quality without an accepted policy and monitoring.

**Model retirement can change a working release.** Current lifecycle guidance differentiates automatic upgrades for supported Standard deployment types from **manual migration for provisioned deployments**. Fine-tuning has separate training and deployment retirement: ending new training does not necessarily end inference for an existing tuned model. Track the specific model/version/SKU dates and test API, prompt, tool, safety and region compatibility; retaining an old artifact does not keep a retired hosted version callable. [Lifecycle and fine-tuning retirement](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements)

#### Define a model release contract

For each foundation-model deployment record:

- provider/model/version/deployment type, region and content-filter/safety configuration;
- input modalities, context/output and structured/tool-call contract;
- quota/PTU, concurrency, retry/fallback and data-zone/residency constraints;
- representative quality/safety evaluation run and dataset version;
- p50/p95/p99 latency, throughput, token/cost and saturation evidence;
- model-version upgrade policy, deprecation notice owner and rollback target.

A fallback model is a separate quality behavior. Evaluate it and make feature degradation visible rather than silently routing to an untested cheaper/different model. Bounded retries should respect provider retry hints and an overall latency/cost budget; retrying a safety rejection or invalid request is not resilience.

#### Operate prompts and connections

Validate template variables and types before sending. Use structured output/schema validation and a controlled repair/refusal path. Tool definitions are privileged interfaces: narrow operations and parameters, validate model-selected arguments, enforce authorization outside the model and require confirmation for material writes.

Connections reference services/data/model endpoints and credentials/identity. Grant project/runtime only required use, separate development from production, rotate secrets if unavoidable and audit who changed or invoked them. A prompt author should not automatically administer production identities or deployment traffic.

### Version prompts as production artifacts

A prompt artifact includes system/developer instructions, template variables, tool/schema definitions, retrieval configuration, examples, safety/output rules, model/deployment parameters and version. Store text/config in Git, keep secrets/data out, lint required variables and test rendering/injection.

Create prompt variants to test a hypothesis. Evaluate on the same versioned dataset with quality/safety/latency/token cost, including subgroup and adversarial cases. Change one major factor when diagnosing. Promote prompt + model + retrieval + safety bundle rather than a prompt string alone.

> **Related item:** A prompt-only rollback cannot recover behavior if model version, index, tool or content filter changed. Release and observe the complete AI configuration bundle.

---

## 4. Implement generative AI quality assurance and observability (10–15%)

### Build evaluation datasets and mappings

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

#### Match the evaluation API and scenario

The current cloud-evaluation setup uses Python `azure-ai-projects>=2.2.0`, a project endpoint and `AIProjectClient.get_openai_client()` for the evaluation API. Lock and test a compatible environment; a lower bound is not a recommendation to float production dependencies. Do not combine older hub/classic evaluation snippets and current project clients without checking the workflow. The renamed **Foundry User** role has the same ID/core permissions as its previous Azure AI User name. [Cloud evaluation setup](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation)

Choose model/agent generation when testing new behavior, a dataset of precomputed outputs when judging existing results, or stored response/trace evaluation when analyzing recorded interactions. Evaluating stored interactions does not replay the original requests or their tools. For `azure_ai_responses`, the current source accepts inline `file_content`, not `file_id`; these are scenario-specific contracts. [Deployed interaction evaluation](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/cloud-evaluation-deployed-interactions)

Automate offline evaluation in CI/release with minimum/maximum thresholds, confidence/sample minimum, regression comparison and hard safety gates. Custom evaluators must have tested rubric, stable output, failure handling and version.

### Observe applications and agents continuously

Instrument trace from user request through orchestration/agent/tool, retrieval and model call. Record deployment/config version, safe query hash/tenant, model, prompt/retrieval/index version, tool names/status, candidate/citation IDs, token usage, latency, retry/throttle and safety/evaluation results. Avoid raw secrets/PII/prompts unless explicitly governed.

Monitor p50/p95/p99 end-to-end and model/tool latency, throughput, errors, rate limit, tokens and estimated cost, retrieval empty/quality, safety/refusal and agent loop/tool failures. Correlate Azure resource metrics and application traces. Use [Foundry tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) and the [agent monitoring dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard).

Online evaluation uses sampled production interactions with privacy/sampling/latency/cost controls. It complements, not replaces, a stable offline regression set and human/business feedback. Alert with owner/runbook and compare by release cohort.

**Check telemetry eligibility and content before interpreting an empty result.** Current trace evaluation reads `invoke_agent` spans with the required GenAI attributes. Missing input/output message content can produce `score=None` for quality evaluators. Generic HTTP spans and prompt hashes alone do not supply groundedness/relevance evidence. Keep content capture explicitly approved, minimize/redact data, restrict access and retention, and use a curated offline dataset when production content cannot be retained. A missing score is an evaluation failure, not a pass.

Foundry monitoring also needs linked Application Insights and permission to its logs; protected Log Analytics tables can require an additional privileged-reader role. Individual monitor/recurring-evaluation features are marked preview in the current dashboard documentation. A broad GA observability announcement does not change every feature's status. Intelligent trace sampling favors diverse cases and removes duplicates; it supports failure discovery, but its raw pass/fail share is not an unbiased population incident rate.

#### Turn metrics into a release policy

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

#### Debug agent and RAG traces safely

Follow one trace: entry -> agent/orchestrator decision -> retrieval query/filter/candidates -> model input/output metadata -> tool selection/arguments/result -> final response/evaluation. Diagnose repeated tool loops, wrong tool choice, invalid parameters, empty/unauthorized retrieval, rate limit and context overflow separately. Record hashes/IDs instead of sensitive bodies where possible and protect Application Insights access/retention because traces can contain customer data.

---

## 5. Optimize generative AI systems and model performance (10–15%)

### Optimize RAG from a labeled baseline

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

#### Diagnose RAG by stage

- **No relevant candidate:** check ingestion completeness, ACL/metadata, source version, chunking and query embedding/model compatibility.
- **Relevant candidate below top-k:** compare exact ground truth, ANN effort/index, filter placement, lexical path and reranker.
- **Relevant context but wrong answer:** inspect context ordering/token truncation, prompt, model capability and contradictory/stale sources.
- **Correct but expensive/slow:** reduce candidate/context safely, cache approved embeddings/results, parallelize bounded calls, choose model/deployment and tune index after quality baseline.
- **Citation mismatch:** bind citation IDs to supplied chunks and validate generated citations; never allow the model to invent a source URL.
- **Cross-tenant result:** stop release, preserve trace, correct pre-retrieval authorization/index partition and test adversarial ACL cases—not a post-answer filter.

Build an experiment table with one row per configuration bundle and columns for source/index, chunker, embedding, lexical/vector parameters, reranker, prompt/model, quality/safety, latency and cost. This prevents “tuning” from becoming undocumented simultaneous changes.

See [RAG concepts](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation) and [Azure AI Search relevance](https://learn.microsoft.com/en-us/azure/search/search-relevance-overview).

**Keep the search score's meaning.** Hybrid Azure AI Search uses reciprocal rank fusion: each list contributes `1 / (rank + k)` to a document. That RRF constant is distinct from vector top-k. The fused `@search.score` depends on how many lists are combined; semantic reranking produces a separate `@search.rerankerScore`. A cosine or reranker threshold cannot be copied unchanged onto RRF scores. [RRF scoring](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking)

### Fine-tune only for the right problem

Fine-tuning adapts behavior/style/task patterns; it does not reliably inject fresh factual knowledge—use RAG for changing knowledge. Compare prompt/examples/RAG/smaller model before fine-tuning.

Design dataset with licensed/consented representative examples, format/schema, train/validation/test split, deduplication, balance, safety/redaction and provenance. Synthetic data can cover rare cases but may amplify generator bias/artifacts. Label it, validate against real examples, preserve generating model/prompt/version and avoid test contamination.

Advanced methods can include supervised fine-tuning, preference-based alignment or parameter-efficient techniques where the selected platform/model supports them. Choose from task, data, compute, risk and deployment support—not fashion. Track base model/version, dataset/hash, method/hyperparameters, job/checkpoint, metrics and safety.

Manage dev-to-production like any release: register candidate, offline/human/safety evaluation, load/cost test, canary/A-B, monitor drift/quality and retain base/previous deployment rollback. Watch overfitting, catastrophic forgetting, subgroup degradation, memorization/privacy and base-model retirement. Use current [Foundry fine-tuning guidance](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning).

| Method | Training signal | Operational check |
|---|---|---|
| Supervised fine-tuning | validated input/output demonstrations | schema, rights, split isolation and retained-capability tests |
| Direct preference optimization | preferred/rejected responses | consistent preference labels, subgroup coverage and preference leakage |
| Reinforcement fine-tuning | reward/grader feedback | grader calibration, reward gaming, held-out safety and model/access eligibility |

The current guidance describes SFT, DPO and RFT with model-specific support; GPT-5 RFT is gated GA, not generally available to every account on request. LoRA describes parameter-efficient training, not a separate guarantee that every deployment supports a user-selectable adapter. The SFT endpoint's minimum example count is only a validation floor, not evidence of enough representative data or predictable quality improvement.

#### Operate the fine-tuning dataset and checkpoints

Define a schema validator and stable example ID; deduplicate near-duplicates across splits; inspect label/rubric agreement; cap repeated templates; balance important groups and retain an untouched realistic test. Remove secrets and content without allowed training rights. For synthetic rows retain parent/source intent and generating configuration so they can be excluded in analysis.

Monitor training/validation loss and task metrics for divergence, but select a checkpoint from downstream evaluation rather than lowest loss alone. Compare base and candidate on retained capabilities and safety, not only the tuned task. Version inference prompt because a tuned model can require a different instruction format.

Production monitoring should distinguish base/model version, tuned checkpoint and traffic cohort. Define triggers for rollback, retraining and dataset review, and a plan for base-model deprecation or unavailable tuning API. Archive lineage/evaluation even after disabling deployment.

> **Related item:** A higher offline judge score can hide worse latency, cost, safety or subgroup performance. Promotion is a multi-metric policy with explicit non-negotiable guardrails.

---

### Six worked examples

All numbers and outcomes below are synthetic learning cases.

**1. Point-in-time feature retrieval.** A prediction observation is timestamped 12:00. Its entity has a feature value of 3 at 11:50 and 8 at 12:02. An event-time as-of join uses 3; a latest-value join after 12:02 leaks future information into training. If an older event arrived only after 12:00, it also may not have been available to the original prediction. Record both event-time and availability assumptions; the feature specification alone does not repair late-arrival leakage.

**2. Shadow traffic consumes capacity.** At 100 requests/second, mirroring 20% sends 100 to blue and another 20 to green: 120 scoring executions, while all client responses still come from blue. A routed 90/10 canary sends 90 and 10, for 100 total. A shadow call that sends an email or writes a feature store can still have an external effect. Use read-only or isolated dependencies and identify which evidence is safe to collect.

**3. Delayed labels and subgroup harm.** Of 1,000 predictions, only 50 have mature labels. Group A has 45 correct of 45; group B has zero correct of five. Overall labeled accuracy is 90%, label coverage is 5%, and B accuracy is 0%. A release rule of aggregate accuracy at least 85% would hide both the coverage gap and subgroup failure. Delay the performance conclusion, inspect selection bias and enforce a predeclared subgroup/minimum-volume policy.

**4. PTU planning with fictional model parameters.** Peak load is 600 RPM, 800 input tokens and 100 output tokens per call. Assume a measured 25% prompt-cache rate, output/input capacity ratio 4 and 5,000 normalized input TPM per PTU. Input is 480,000 TPM; output is 60,000. Normalized work is `480,000 × 0.75 + 4 × 60,000 = 600,000`, or 120 PTUs before headroom. A fictional 20% margin gives 144; with a fictional increment of ten and minimum twenty, round to **150**. If the cache rate falls to zero, raw demand becomes 144; maintaining the same margin requires **180**. These are not current model quotas/prices or an SLA; substitute actual model/SKU parameters and benchmark.

**5. Evaluation coverage is separate from score.** A 100-case release dataset yields 72 passes, eight failures and twenty evaluator errors/missing results. Pass share among graded cases is `72 / 80 = 90%`, but coverage is 80% and passes over all planned cases are 72%. Do not drop missing scores from a release gate silently. For diversity-selected production traces, the sample ratio also is not a population failure estimate. Keep evaluation availability, per-case outcome and representative sampling as separate evidence.

The following local example checks coverage and outcomes. The illustrative pass threshold is a team choice, not a Microsoft exam or product requirement. Real gates also bind release/dataset/evaluator versions, validate schemas, compare baseline and enforce operational/subgroup limits.

```python
def passes_gate(expected_ids, results, minimum_pass_rate=0.9):
    if not expected_ids or not 0 <= minimum_pass_rate <= 1:
        return False
    ids = [row["id"] for row in results]
    if len(ids) != len(set(ids)) or set(ids) != set(expected_ids):
        return False
    if any(row["outcome"] not in {"pass", "fail"} for row in results):
        return False
    if any(row["severe"] is not False for row in results):
        return False
    return sum(row["outcome"] == "pass" for row in results) / len(results) >= minimum_pass_rate
```

Malformed records raise an error; the caller must treat that as a blocked release, not continue. A gate returning true verifies only these supplied fields, not the truth of a judge or the safety of a deployment.

**6. Hybrid rank fusion.** Using two equally weighted lists and illustrative `k=60`, document A ranks first and sixtieth: `1/61 + 1/120 ≈ 0.02473`. Document B ranks second in both: `2/62 ≈ 0.03226`, so B ranks higher. Neither score is a similarity probability. Changing the number of fused lists changes the score range; tune retrieval using labeled relevance and authorization before choosing a rejection threshold.

### Blog exercises: policies, controls and deployment status

Sarah Bird's June 2 [open evaluation and control article](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) connects policy-based tests with runtime checkpoints and reevaluation. Apply that idea to one original rule: “an agent may read an authorized record but may not update another tenant's record.” Write a positive case, cross-tenant denial, missing-identity case and tool-timeout case. Identify the external authorization check, expected evidence and release blocker. A deterministic control path may call a probabilistic classifier/judge; that does not make its classification infallible. Linked ASSERT/ACS implementations were not executed.

Nick Brady's May 30 [Foundry operations roundup](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-may-2026/) is useful for discovering trace evaluation, managed networking, cost attribution and SDK changes. Build a dated table of feature, exact API, status, region, permission, telemetry/data boundary and rollback. Reconcile each entry with current product documentation; a roundup's “GA” heading does not establish eligibility for every feature, account or region.

---

## 6. Integrated scenarios and labs

### Scenario A: regulated classification model

Version data, feature spec, environment and training component; use MLflow and pipeline to compare AutoML/sweep candidates; gate on test, subgroup/fairness, latency and explainability; register MLflow model; canary managed online deployment; monitor operational/data/prediction and delayed outcome performance; retrain only through the same gates. **Trap:** drift alone auto-promotes a worse model.

### Scenario B: enterprise RAG assistant

Provision private Foundry project/search/data/monitoring with managed identity and IaC; version model/prompt/chunker/embedding/index/safety; evaluate groundedness/relevance/citation/safety/latency/cost; deploy candidate cohort; trace retrieval/tools/model; tune hybrid/top-k/rerank from labeled evidence. **Trap:** post-retrieval ACL filtering leaks candidates and destroys recall.

### Scenario C: high-volume fine-tuned service

Compare prompt/RAG/base with fine-tuning; govern real/synthetic dataset; register evaluation lineage; size provisioned throughput from load; canary new fine-tuned version; monitor tokens, utilization, quality/safety and fallback. **Trap:** model version changes while deployment name stays constant and no bundle/version evidence exists.

The first eight labs describe optional cloud exercises; none were executed in this review. Use synthetic data and an isolated budgeted environment. Labs 9–10 produce offline review artifacts. Keep source, expected outcomes, actual results and cleanup evidence separate.

### Lab 1: secure workspace and IaC

Deploy dev workspace/dependencies/identity/network with Bicep/CLI; create datastore/data/compute; prove allowed/denied paths; run lint/what-if through GitHub OIDC; capture DNS/outbound/diagnostic evidence.

### Lab 2: reusable assets and registry

Create pinned environment and component; version immutable data; compose pipeline; share approved model/component/environment through registry; change hidden/mutable input to demonstrate why lineage/caching fails.

### Lab 3: training, MLflow and tuning

Refactor notebook into script; log code/data/environment/parameters/metrics; compare baseline, AutoML and sweep; run distributed option only after profile; test leakage and reproducibility.

### Lab 4: model governance and deployment

Package feature retrieval spec and MLflow model; evaluate responsible/subgroup metrics; register/archive versions; deploy online and batch; inject schema/init/identity/capacity failures; canary, promote and roll back.

### Lab 5: monitoring and retraining

Generate quality, data/prediction/concept drift and operational issues separately; configure signals/thresholds; trigger alert/retraining candidate; prove validation prevents automatic bad promotion.

### Lab 6: Foundry infrastructure, model and prompt release

Provision dev project/identity/network via IaC; deploy two model versions/deployment types; version prompt bundle in Git; evaluate variants; load test standard/provisioned assumptions; execute progressive release/rollback.

### Lab 7: evaluation and observability

Build mapped versioned evaluation set; run built-in quality and risk/safety plus custom evaluator; calibrate against human labels; automate gates; trace retrieval/agent/tool/model; query latency/tokens/cost/error and debug failure.

### Lab 8: RAG and fine-tuning optimization

Build labeled retrieval set; baseline exact/vector/hybrid; vary chunk/embedding/top-k/threshold/rerank one at a time; A/B safely; create governed synthetic fine-tune supplement; compare base/RAG/fine-tuned on quality/safety/latency/cost and deploy only if justified.

---

### Lab 9: immutable release and capacity decision

Create a manifest for code/data/feature/environment/model/prompt/index/evaluator versions. Mark which references could mutate despite a stable name. Reproduce examples 1, 2 and 4; include rollout overlap, cache loss, quota-versus-capacity and model-retirement constraints. Produce a promotion/hold decision with a compatible rollback target and owners. An artifact is not evidence that a cloud deployment works.

### Lab 10: evaluation failures and policy controls

Execute the local gate with passing, failing, missing, duplicate, severe and malformed records; prove the caller blocks on exceptions. Reproduce examples 3, 5 and 6. Complete the blog's tenant-authorization cases and the feature/status table. Explain what production trace content would be necessary, what must remain private and which quality claims therefore require a curated offline dataset.

---

## 7. Original knowledge checks

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
37. Why can a successful `az ml job create` step still leave an unfit release?
38. What changes a pipeline node from reusable to rerun, and why are mutable references unsafe?
39. Which feature value belongs to the 12:00 observation in example 1?
40. What differs between 20% mirroring and a 10% routed canary in example 2?
41. Why does 90% labeled accuracy in example 3 fail to establish production fitness?
42. Do PTU quota or a reservation guarantee deployable model capacity?
43. How does losing prompt-cache hits change example 4's capacity budget?
44. Why is a missing quality score not a successful evaluation?
45. Does evaluating stored traces execute the original agent and tools again?
46. Why do prompt hashes alone not satisfy trace-based quality evaluation?
47. Can RRF, cosine and semantic reranker scores share a threshold?
48. Why can a retained model artifact fail as a rollback plan after retirement?

### Answer explanations

1. Workspace organizes operations; datastore references storage; data asset versions a reference/contract; environment captures runtime; component declares a reusable step; compute runs work; registry shares assets. They do not all store or freeze the underlying data.
2. The URI can resolve to changed bytes. Preserve a snapshot/version/hash and verify it at consumption; a numbered asset name alone is insufficient.
3. Submitter authorizes job creation; compute/runtime reads data; pipeline automation manages selected assets; endpoint runtime reads its artifacts/features. Grant and test each actual identity at the required data boundary.
4. Storage, registry, Key Vault, identity, package/build, monitoring and model endpoints may need approved paths. Resolve DNS and test from the runner/runtime; a workspace private endpoint does not authorize or connect everything.
5. Bicep provisions resource/dependency/identity/network configuration; ML CLI/YAML manages supported assets, jobs and deployments. Version both and verify their permissions and compatibility.
6. OIDC exchanges short-lived federated tokens without storing a long-lived client secret. The trusted repository/branch/environment subject and Azure role scope still determine who can act.
7. Record immutable code/data/features/environment, parameters/seed, split identities, metrics and artifacts. Capture external dependencies and nondeterminism; logging a final accuracy alone is insufficient.
8. AutoML explores supported model/featurization choices; a sweep searches your declared hyperparameters. Both optimize a validation metric and still need a separate untouched test and business/safety gates.
9. Input, synchronization or communication can dominate, and extra GPUs add cost without proportional throughput. Measure convergence, elapsed time and total resource cost against a smaller baseline.
10. Declare all inputs and environment/code/output/run settings, and ensure identical inputs imply reusable outputs. A mutable external source violates that assumption even if the cache key does not change.
11. It binds the model to feature definitions/versions/retrieval behavior needed at training and inference. Include point-in-time and freshness evidence to avoid skew and future-data leakage.
12. The artifact packages model/flavor/signature/dependencies; registration creates a versioned managed asset; a deployment adds runtime, compute, identity and serving configuration. Each has separate lineage and lifecycle.
13. Subgroup error/fairness, privacy, robustness, safety and operational limits can block promotion. Choose tools that support the candidate; Azure ML's dashboard is not a universal evaluator for every model type.
14. Use online serving for bounded interactive latency; batch for asynchronous large datasets with explicit completion/output reconciliation. Job success does not prove every input produced a valid result.
15. Feature retrieval, schema, environment, scoring code, identity, model availability and dependent resources must work together. Preserve and test the full release bundle.
16. Data drift changes inputs, prediction drift changes outputs, concept drift changes the input/outcome relationship, and operational changes affect service behavior. Each needs different evidence and response.
17. Drift may be harmless seasonality or data damage. Diagnose and evaluate a candidate through the ordinary gates; neither drift nor completed retraining proves improvement.
18. Define project/resource, roles, runtime identity, model/connections, storage/search and telemetry boundaries. Specify inbound and outbound paths separately and test both allowed and denied operations.
19. Serverless APIs provide supported managed inference; managed compute requires more runtime/scale operations; provisioned throughput allocates processing capacity for eligible models. Compare support, demand shape, residency and total cost.
20. A stable deployment alias can point to changed model behavior. Track exact versions and upgrade policy; evaluate replacements and monitor actual serving version.
21. Include prompt variables/examples, tool schemas, retrieval/index, model/version, safety and generation settings, dataset/evaluator and expected contract. A text file alone omits many behavior-changing dependencies.
22. Hold dataset, model, retrieval and evaluator versions fixed and compare per-case results plus safety/latency/cost. If several factors change, label the experiment accordingly and avoid attributing causality to the prompt alone.
23. Define explicit field mappings and required values for the chosen evaluator/scenario; validate missing/empty data and authorization. Dataset generation, precomputed outputs and stored-response/trace evaluation have different contracts.
24. Groundedness asks whether context supports the answer; relevance asks whether it addresses the question; coherence concerns logical organization; fluency concerns language quality. None alone proves task success or authorization.
25. Judge behavior changes with model/prompt/version and may disagree with human/domain judgments. Calibrate labeled cases, record disagreements and retain per-case evidence.
26. Select context-appropriate harm, injection, privacy and tool-abuse cases with severity thresholds and minimum coverage. A severe failure can block despite high average quality; evaluator errors must remain visible.
27. Correlate entry, orchestration, retrieval, model and tool spans with release identity and stable trace/conversation IDs. Record safe metadata and explicitly govern any content needed for evaluation.
28. Sampling changes coverage and may bias ratios; privacy restrictions can remove evaluator-required content. Separate operational metrics, diagnostic traces and approved quality datasets instead of labeling absent data as a pass.
29. Measure authorized relevant candidates first, then context selection and answer/citation correctness. A generator cannot use missing evidence; a good retrieval score does not prove a grounded answer.
30. Larger chunks/top-k can increase context and cost while adding distraction; narrow thresholds or reranking can improve precision but lose recall. Measure by labeled cohort with latency/cost constraints.
31. Lexical search helps exact identifiers/terms and vectors help paraphrases; fusion combines ranked evidence. A separate semantic reranker may reorder results, and its score is not the fused score.
32. Use stable assignment, authorized data, a predeclared primary outcome, sample/coverage requirements and hard safety/operational stops. Retain rollback and evaluate fallback behavior before exposing users.
33. Use retrieval for fresh or source-attributed knowledge. Fine-tuning fits behavior/style/task adaptation with suitable data; it does not reliably keep changing facts current.
34. Retain source rights, generating model/prompt/version, labels and intended coverage; deduplicate across splits and validate against realistic examples. Synthetic diversity does not prove representative production quality.
35. SFT uses demonstrations, DPO preferences, and reinforcement tuning a reward/grader; parameter-efficient methods reduce trained parameters. Verify model/platform/access support and evaluate generalization, safety and grader gaming.
36. Require intended task improvement, retained capabilities, subgroup/safety limits, latency, capacity/cost and compatible retirement/rollback plans. Lowest training loss alone is not a release gate.
37. Submission returns before training/evaluation completes. Wait for terminal status, validate the expected artifacts and enforce quality/coverage/safety/operational gates before promotion.
38. Changed code/environment/inputs/outputs/run settings, nondeterministic components or forced rerun prevent reuse. A hidden mutable source can change without a declared change and yield misleading reused results.
39. Value 3 at 11:50; the 12:02 value is future information. Also check whether the 11:50 event was actually available by prediction time.
40. Mirroring creates 120 executions with 100 blue client responses; a 90/10 canary creates 100 executions with ten candidate responses. Both need capacity/effect controls, but they measure different exposure.
41. Only 5% of predictions have labels and group B has zero correct of five. Diagnose delayed-label selection and subgroup failures before claiming fitness; aggregate accuracy hides them.
42. No. Quota permits an allocation; available model-version capacity determines whether deployment succeeds. A reservation is a billing discount, not held capacity.
43. With no cache, normalized work rises from 600,000 to 720,000 TPM, or 144 raw PTUs. With the fictional 20% margin and ten-unit increment, budget 180 rather than 150.
44. Missing input, unsupported spans or evaluator errors can produce no score. Keep coverage separate and block the release according to the defined policy instead of removing those rows.
45. No. It judges recorded outputs/interactions. Testing current code/model/tool behavior requires an explicit generation/replay experiment with suitable isolation.
46. Current trace quality evaluators need message fields on eligible GenAI spans. Hashes aid correlation but cannot supply semantic content; use approved content or a curated offline evaluation path.
47. No. RRF depends on ranks/list count, vector scores on their metric, and reranker scores on a separate stage. Calibrate each threshold against labeled data and its exact score type.
48. The provider can stop serving a retired version, even if you kept its metadata or fine-tuned artifact. Training and deployment retirement differ; validate a currently available compatible rollback target.


---

## Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Choose one primary path, build the labs and use targeted material for gaps. Times are published when available or labeled estimates. Avoid dumps and recalled/live exam questions.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official AI-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300) | Public | 30–60 min | Authoritative scope and lifecycle |
| [AI-300T00 Microsoft Learn course](https://learn.microsoft.com/en-us/training/courses/ai-300t00) | Public self-study; paid instructor option | 4 days; 20–35 self-study hours plus labs (editorial estimate) | 12 course languages; current syllabus/runtime total not exposed |
| [AI Skills Navigator Practice Assessment](https://aiskillsnavigator.microsoft.com/en-us/certifications/microsoft-certified-associate/machine-learning-operations-engineer) | Free account/sign-in | 45–90 min plus remediation (estimate) | Microsoft-linked diagnostic; sign-in shell only, no questions/results reviewed |
| [Azure MLOps v2 solution accelerator](https://github.com/Azure/mlops-v2) | Public | 8–20 hours selectively (estimate) | Official reference architectures and automation; verify current SDK/IaC |
| [Azure ML examples](https://github.com/Azure/azureml-examples) | Public | 10–30 hours selectively (estimate) | CLI/SDK jobs, pipelines and endpoints |
| [Foundry samples](https://github.com/azure-ai-foundry/foundry-samples) | Public | 8–20 hours selectively (estimate) | Current evaluation, tracing and GenAIOps examples |
| [O'Reilly MLOps/LLMOps Bootcamp](https://www.oreilly.com/live-events/mlopsllmops-bootcamp/0642572182861/0642572243333/) | Paid live/subscription | Historical November 3–5, 2025 event; 10h metadata and agenda | Ammar Mohanna, two sessions; verify recording/new dates; broad lifecycle supplement |
| [Udemy AI-300 MLOps & GenAIOps preparation](https://www.udemy.com/course/ai-300-mlops-genaiops-engineer-exam-preparation/) | Paid; price varies | 3h27, 11 lectures / one section (indexed public outline) | Aseem Mankotia, updated July 2026; 100-minute simulation differs from official 120-minute assessment |
| [Udemy AI-300 practice tests](https://www.udemy.com/course/ai-300-operationalizing-ml-and-generative-ai-practice-tests/) | Paid; price varies | Five 150-question sets plus one 161-question set = 911; 12–25h review (estimate) | VARONTO Academy, updated June 2026; description still says 900, paid content/originality unverified |
| [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor) | Public | 3–10 hours selectively (estimate) | Current Azure ML, Foundry, evaluation and operations sessions |
| [Whizlabs AI-300 catalog](https://www.whizlabs.com/ai-300-microsoft-machine-learning-operations-engineer-associate/) | Paid; public catalog | Indexed 100 videos and 3 quizzes; duration unverified | Two paid tests plus one free; course content and question count unverified |
| This guide's ten labs | Azure access; costs vary | 30–55 cloud hours plus 2–4 offline artifact hours (estimates) | Reproducibility, safe rollout, monitoring, evaluation and optimization evidence |

A Whizlabs AI-300 product is now indexed, correcting the prior missing-product statement. Direct retrieval exposed only a title shell; its indexed outline supplies the counts above. Its multilingual exam claim differs from the official exam page's current English-only listing. Use Microsoft for exam metadata. Bounded Pluralsight/MeasureUp searches did not identify dedicated products; this is not proof that none exist.

Direct Udemy requests were blocked; the public outlines were reviewed through the web index. Paid lessons, lab delivery, question originality and claimed exam difficulty were not verified. O'Reilly's linked event is historical, and access to its recording is unverified. The previous Learn two-path/12h24 total is not reproduced by the current extracted page; the new self-study budget is an editorial estimate. Use the Microsoft-linked diagnostic after signing in, then remediate by objective and lab.

### Practical sequence

1. Map every official objective to an artifact and failure test.
2. Complete the currently available Microsoft course modules or one verified structured course; check its actual syllabus before committing study time.
3. Build Labs 1–5 for MLOps; retain full run-to-deployment/rollback evidence.
4. Build Labs 6–8 for GenAIOps; retain evaluation/tracing/RAG/fine-tuning comparisons, then complete the offline decision records in Labs 9–10.
5. Take the official assessment once and remediate by objective.
6. Recheck blueprint, model/SDK/evaluation/network features and lifecycle before the exam.

---

*This independent guide uses public sources and original synthesis and is not endorsed by Microsoft or any vendor.*
