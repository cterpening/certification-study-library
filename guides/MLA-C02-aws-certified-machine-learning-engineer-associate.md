---
exam_code: MLA-C02
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-28
---

# MLA-C02 AWS Certified Machine Learning Engineer - Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, beta warnings, links, and exam-integrity compliance were reviewed again on September 28, 2026, including all 107 detailed skills. The GA-date conflict remains unresolved. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mla-c02-coverage-record). The [official MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html) is authoritative.

**Current baseline:** Initial MLA-C02 four-domain blueprint published September 1, 2026; beta registration is open and English beta delivery begins September 29<br>
**Beta appointment code:** **ME1-C02**. The guide/version is MLA-C02; AWS currently uses ME1-C02 for the beta scheduling code.<br>
**Upcoming blueprint/delivery change:** Beta is 170 minutes, 85 multiple-choice/multiple-response questions, USD 75, and English only. The September announcement plans standard MLA-C02 general availability for January 14, 2027, while the credential page still lists GA dates as TBD; standard delivery metadata, learning assets, and any blueprint revision remain **VERIFY CURRENT**.<br>
**Important freshness boundary:** This is not a renamed C01. AWS explicitly added vector databases, multimodal data, embeddings, RAG preparation and monitoring, FM data preparation/customization/deployment, Bedrock evaluations and prompt management, human/LLM evaluation, agents/protocols/state/versioning/observability, GPU/AI cost patterns, FM credentials, pipeline vulnerability checks, and Guardrails. Use the official [C01-to-C02 comparison](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/mla-02-comparison.html) to gap-check older material.<br>
**Official source:** [AWS Certified Machine Learning Engineer - Associate MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html)

## Living-guide watch — September 28, 2026

**Scheduling boundary:** The [September announcement](https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/) plans GA for January 14, 2027. The credential page still shows TBD for GA registration and delivery, so this is an announced plan with unresolved source disagreement. English C01 ends September 28; Japanese, Korean and Simplified Chinese continue until C02 GA. English beta delivery is scheduled to begin September 29 under **ME1-C02**. A future start date is not evidence that delivery has already begun.

**Coverage and resources:** All 107 skills on the four C02 domain pages were reviewed. The automated broad-domain snapshot matches the accepted baseline; it does not track each detailed skill. Provider labels are insufficient: the Tutorials Dojo page now lists C02 domain sections, but still combines 65 questions with 170 minutes, unlike AWS's 85-question beta. Paid-bank coverage remains unverified. See the [review report](../docs/research/2026-09-28-mla-c02-deep-review.md).

**Lab availability:** The [June 30 availability announcement](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/) places the original Amazon Bedrock Agents, now **Agents Classic**, and several SageMaker features in maintenance with July 30 new-customer closure. Do not assume an old action-group or Clarify/Debugger/Model Monitor walkthrough can be created in a new account. Preserve the agent, evaluation and monitoring concepts; select a currently supported implementation and verify account access before a paid lab. AgentCore capabilities have their own contracts and are not a drop-in replacement for every Classic resource.

## How to use this guide

MLA-C02 validates production engineering across both traditional machine learning and generative/agentic AI. AWS targets candidates with at least one year using SageMaker AI, Amazon Bedrock, and related services; at least one year in a related engineering/data role; and experience with traditional ML and GenAI. Architecture strategy across an enterprise remains outside the target role, but implementing an existing architecture safely is central.

The detailed guide describes the standard form as 50 scored plus 15 unidentified unscored questions with a 720 scaled passing score, while noting that its usual pass/fail result statement does not apply to beta. The live [certification page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) says beta has 85 questions and extra time/items for statistical evaluation, with results typically available within five business days. Treat the live page as authoritative for booking and beta delivery.

For every scenario, work through three connected contracts:

1. **Outcome contract:** task, user, error cost, quality threshold, latency, throughput, availability, explainability, safety, compliance, and budget.
2. **Knowledge/model contract:** sources, rights, freshness, schema, split, feature or chunk definition, embedding/model/prompt/version, evaluation set, and approval evidence.
3. **Runtime contract:** identity, tools, state, endpoint or provisioned capacity, scaling, orchestration, tests, observability, cost allocation, rollback, and recovery.

Do not answer “Bedrock” or “SageMaker” from one keyword. Determine whether the problem calls for a managed task API, traditional model, foundation model, RAG system, agent, or a combination, then choose the least complex implementation that meets the contract.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the objective easier to reason about. It is supporting knowledge, not a claim that the item appears verbatim in the official outline.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Data Preparation for ML and AI | 28% | How are structured and multimodal data collected, transformed, embedded/chunked, protected, validated, and made fit for traditional or generative AI? |
| ML Model and Foundation Model Development | 24% | Which approach, model, customization, retrieval, experiment, metric, judge, and approval evidence meet the outcome? |
| Deployment and Orchestration of ML and AI Workflows | 24% | How are models, knowledge bases, prompts, agents, state, infrastructure, tests, versions, releases, updates, and rollback operated? |
| Operating, Monitoring, and Securing ML and AI Solutions | 24% | How are model/RAG/agent behavior, infrastructure, tokens, vectors, cost, credentials, guardrails, audit, and vulnerabilities controlled? |

---

## 1. Data Preparation for ML and AI — 28%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html) contains three tasks: collect/store, transform/engineer/pre-process, and validate quality/manage bias.

### Build a versioned data and rights contract

Define one record/document/image/audio item, entity key, event time, label/outcome, source owner, license/consent, permitted use, classification, residency, retention, deletion, freshness, volume, and expected consumers. Store raw inputs immutably when permitted, derive curated versions reproducibly, and retain lineage from source through feature/chunk/embedding/training/prompt/evaluation artifact.

| Workload need | Common fit | Critical decision |
|---|---|---|
| Durable objects, datasets, artifacts | Amazon S3 | Partition/prefix, format, versioning, lifecycle, encryption, policy, event and consistency workflow |
| POSIX or high-performance file semantics | EFS / appropriate FSx service | Protocol, throughput, latency, shared access, cost, backup and training integration |
| Relational or vector-enabled operational data | RDS/Aurora, including supported pgvector patterns | Transactional versus retrieval load, index, dimension, distance, filtering, availability and scaling |
| Search/vector retrieval | OpenSearch Service | engine/index/mapping, vector dimension/algorithm, metadata filter, recall/latency/cost and lifecycle |
| Serverless vector storage patterns | Supported S3 vector capability | Current feature/region/latency/index contract—**VERIFY CURRENT** |
| Streaming | Kinesis, managed Flink, Kafka path | partition, event time, order, duplicate, checkpoint, replay, late data and backpressure |
| Batch transformation | Glue, EMR/Spark, DataBrew, SageMaker Processing/Data Wrangler | code versus visual, scale, libraries, lineage, schema, error quarantine and ownership |
| Reusable features | SageMaker Feature Store | entity/event time, online/offline need, point-in-time correctness, freshness and governance |

Choose CSV/JSON/Parquet/ORC from producer, schema, access, compression, parallelism and consumer constraints. Columnar formats help analytic/training scans but do not replace small-file management or schema governance. Ingestion must be replayable: immutable landing reference, run/checkpoint, idempotent writes, schema and record counts, quarantine, lineage, and atomic publication.

Text, image, audio, and mixed documents add format, decoding, resolution, language, layout, transcription, sampling, modality alignment, accessibility and licensing concerns. Store original and derived representations separately. A transcript is not equivalent to audio; OCR text is not equivalent to layout; an image caption is a lossy derived label.

### Engineer features, chunks, and embeddings deliberately

Traditional preprocessing includes cleaning, deduplication, missing-value treatment, scaling/standardization, binning, transforms, categorical encoding, tokenization and feature creation. Fit stateful transforms only on training data, persist them, and reuse the same artifact at inference. Split by time/group/entity where deployment requires it; exclude target/future information.

An embedding maps content to a numeric vector so semantic similarity can be searched. Treat embedding model and version, dimension, normalization, input limits, language/modality, chunking, and distance metric as part of the index schema. Changing an embedding model generally requires re-embedding and rebuilding or deliberately versioning indexes; mixing incompatible vectors silently corrupts retrieval.

RAG preparation typically performs extraction → normalization → semantic/layout-aware splitting → metadata and ACL association → embedding → index/write → validation. Chunk size and overlap trade context completeness against noise, token use, duplication, retrieval precision and cost. Preserve stable source/document/chunk IDs, page/section location, source version, timestamps, permissions and deletion lineage. Never rely on post-retrieval filtering alone if an unauthorized vector can be surfaced earlier in the path.

Retrieval is not just nearest-neighbor search. Decide query rewriting/expansion, dense/sparse/hybrid search, metadata filters, top-k, score threshold, reranking, diversity, context assembly and citation. Build a labeled query-relevance set so these can be tuned against Recall@k, precision, ranking metrics, latency and cost.

For FM customization:

- supervised fine-tuning needs validated task examples and prompt-response pairs;
- continued pre-training adapts broader domain knowledge and requires more data/compute/control;
- distillation trains a smaller model from teacher outputs and must evaluate inherited errors/safety;
- prompt/RAG may satisfy the need without changing model weights.

Screen prompt-response pairs for correctness, duplication, leakage, unsafe content, secrets, licensed material, policy violations and train/test contamination. Maintain source and reviewer evidence.

**Related item:** A vector database stores searchable representations; it is not the system of record. Keep authoritative content, access policy, deletion state and provenance outside or alongside the index.

### Validate quality and bias across modalities

Data-quality assertions cover schema, type, range, category, completeness, uniqueness, consistency, freshness, volume, referential integrity and distribution. For unstructured/AI data, add extraction fidelity, language, layout preservation, chunk boundaries, metadata completeness, ACL propagation, embedding success, prompt-response pairing and content-safety checks.

Class imbalance, selection bias, measurement bias, labeling bias and historical bias are distinct. Compare distributions and performance by relevant slices; confirm sample sizes and intended populations. Rebalancing, class weights, augmentation, synthetic data, better collection, label adjudication, thresholds and product/process changes solve different problems. Multimodal balance must consider which text/image/audio combinations are absent or overrepresented.

Masking hides values in a context, redaction removes them, tokenization substitutes controlled values, anonymization seeks to prevent re-identification, and encryption protects confidentiality without removing identity. Choose from the threat and permitted-use model. Validate that derived chunks, embeddings, caches, logs, prompts, evaluation datasets and outputs honor deletion and access—not just the source bucket.

**Related item:** Embeddings can leak semantic or membership information. Treat vector indexes, backups and query logs as sensitive derived data when their sources are sensitive.

---

## 2. ML Model and Foundation Model Development — 24%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html) covers approach selection, training/customization, and traditional/GenAI evaluation.

### Choose the solution class before the product

| Problem | Candidate approach | Avoid when |
|---|---|---|
| Stable deterministic decision | Rules/workflow | Inputs are ambiguous and learned generalization is required |
| Classification/regression/forecast/ranking/anomaly | Traditional ML | Unstructured generative output is the actual requirement |
| OCR/speech/translation/entity/image task | Managed AI service | Domain/control/quality/data terms cannot meet the contract |
| General language or multimodal generation | Foundation model | Deterministic or high-assurance logic should remain code/rules |
| Current/private knowledge answering | RAG | The need is behavior/style adaptation rather than grounded knowledge |
| Repeated specialized behavior | Prompt template, fine-tuning or continued pre-training | Prompt/RAG/tooling already meets quality and cost |
| Goal-directed multistep action | Agent with tools/workflow | A deterministic pipeline is safer, cheaper, more testable and sufficient |

Select an Amazon Bedrock model from modality, context/input/output limits, languages, quality on a representative evaluation set, latency, throughput mode, regional availability, customization support, tool/structured-output behavior, safety, provider terms and cost. Benchmark rather than inferring from parameter count or leaderboard. Compare managed AI APIs, Bedrock FMs, SageMaker/JumpStart or custom models, and existing enterprise services on total ownership.

RAG is appropriate when knowledge changes, citations/provenance matter, or private data should remain external to weights. Fine-tuning is useful for task behavior, style/format or specialized patterns with sufficient high-quality examples. Prompting is cheapest to change; RAG adds retrieval/index operations; tuning adds dataset, compute, version and safety obligations; training from scratch requires exceptional scale and expertise.

Traditional algorithm selection still matters. Frame classification/regression/ranking/forecast/anomaly/clustering, establish a baseline, choose interpretable or complex models from data and risk, and match SageMaker built-in algorithm, script mode/framework or custom container to control needs. C02 retains core MLOps rather than replacing it with GenAI.

### Train and customize reproducibly

Record data/chunk snapshot, split, preprocessing, code, container/dependency, model ID/version, prompt/template, retrieval configuration, hyperparameters, random seed where meaningful, instance/count, distributed strategy, metric/judge definitions, output artifact and approvals. MLflow on SageMaker can track runs/artifacts; Bedrock evaluation and Prompt Management cover supported FM/prompt lifecycle. Product interfaces are volatile—preserve portable evidence.

Traditional training decisions include batch size, learning rate, epochs/steps, loss, optimizer, regularization, early stopping, augmentation, class weights, checkpointing, distributed data/model parallelism and automatic model tuning. Tune on validation, reserve test for final evidence, and constrain search time/cost. Diagnose convergence from loss curves, gradients, data, scaling, learning rate and implementation before adding compute.

Prompt engineering defines role/instructions, relevant context, input delimiters, examples, constraints and output schema. Version system/user templates separately from runtime inputs. Test injection, ambiguity, missing context, adversarial text and tool misuse. Fine-tuning needs learning-rate/epoch/batch decisions, holdout data, catastrophic-forgetting and safety regression checks. Retrieval optimization jointly tunes embedding model, chunking, filters, search, reranking and context assembly—optimizing only answer style can hide failed retrieval.

Combining models may ensemble traditional predictors, route by task, use a small/cheap model for simple inputs, escalate to a capable model, or use one model/judge to validate another. Define routing confidence, failure/fallback, added latency, correlated errors and cost. A judge model is not independent ground truth merely because it is different.

**Related item:** Prompt, retrieval configuration, model ID, guardrail, tool schema and agent instructions are deployable software artifacts. Review, test, version, approve and roll them back like code.

### Evaluate the complete system

Traditional metrics include confusion matrix, precision, recall, F1, ROC/PR curves, calibration, MAE/RMSE and task-specific measures. Choose thresholds from error cost and capacity; slice results; compare model, latency and cost; use shadow/A-B experiments safely.

GenAI evaluation needs a rubric and multiple layers:

- **retrieval:** labeled relevance, Recall@k/precision@k, reciprocal/ranking measures, source/ACL correctness, context coverage, latency and cost;
- **generation:** correctness, groundedness/faithfulness, relevance, completeness, citation fidelity, instruction adherence, format, tone, safety and refusal behavior;
- **agent:** goal completion, tool selection/arguments/results, step count, loops, coordination, state, authorization, recovery and side effects;
- **operations:** latency distributions, input/output/cache tokens, throughput, error/throttle, vector/embedding cost and business outcome.

BLEU measures n-gram overlap and is historically useful in translation; ROUGE emphasizes overlap/recall in summarization; BERTScore and semantic similarity use learned representations. None alone establishes factual correctness or business fitness, and reference metrics can penalize valid alternative wording.

Human evaluation should use a documented rubric, blinded/randomized comparison where practical, qualified reviewers, disagreement/adjudication, sampled high-risk slices, privacy controls and calibration examples. LLM-as-a-judge requires pinned judge model/prompt, order/position-bias checks, structured output, agreement against human labels, cost and failure handling. Do not let the candidate model grade itself as the only gate.

Build gold, adversarial, regression and production-sampled datasets without confidential leakage. Baseline against current system or simple method. Define pass/guardrail thresholds before running the final test. Report confidence and slice failures, not one aggregate score.

**Related item:** Offline quality is necessary but not sufficient. Online behavior can change with user distribution, latency, retrieved data, tools, prompt injection and downstream product decisions.

---

## 3. Deployment and Orchestration of ML and AI Workflows — 24%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html) covers model/FM/agent deployment, infrastructure/retrieval/state, and automated MLOps/LLMOps delivery.

### Select inference, model and capacity mode

For traditional SageMaker inference, compare Batch Transform, real-time, serverless, asynchronous and multi-model endpoints from latency, payload/duration, burst, utilization, compatibility and operations. ECS/EKS/custom hosting adds control and ownership. Benchmark CPU/GPU/accelerator, container, model and traffic together.

For Bedrock, distinguish supported on-demand, provisioned throughput, cross-region or other current inference/profile mechanisms, batch operations and imported/custom model deployment. These features, names, supported models, regions and quotas are **VERIFY CURRENT**. Choose from predictable capacity, latency, geography, data handling and cost—not marketing labels. Custom Model Import brings compatible external model artifacts into supported Bedrock hosting; SageMaker supports broader custom training/hosting control.

An FM application also deploys prompts, guardrails, retrieval configuration, knowledge base, tool schemas, agent instructions, model parameters and application code. Version the whole release manifest. Rolling back only the model while leaving a new prompt or index can preserve the incident.

### Engineer RAG and agents as production systems

An Amazon Bedrock knowledge base connects a data source, parsing/chunking, embeddings, vector store and retrieval/generation configuration. Define incremental synchronization, deletion, ACL/metadata filter propagation, failed-document quarantine, index version, re-embedding and safe cutover. Blue/green indexes or versioned aliases reduce partial-update risk. Retrieval pipelines may add query classification, rewriting, hybrid search, filters, reranking, context selection and citation mapping.

Agents combine a model with instructions, tools/action groups, knowledge, state/memory and orchestration. Prefer explicit deterministic workflows for mandatory order, regulated approval, financial action or bounded compensation. Use an agent where flexible planning is valuable, then constrain it:

- narrowly described, schema-validated tools with least-privilege credentials;
- server-side authorization from verified user/tenant context;
- step/time/token/cost limits and loop detection;
- confirmation or human approval for irreversible/high-impact actions;
- idempotency and compensating/recovery behavior;
- traceable model, prompt, tool, state and result versions;
- protocol input/output validation and trust boundaries.

State may be request context, session history, summarized memory, durable workflow state or external business state. Define owner, key/tenant, consistency, retention, deletion, encryption, size, conflict and recovery. Model-generated summaries are lossy and untrusted; tools must re-authorize against source-of-truth state.

Agent communication protocols are integration contracts, not an authorization system. Validate identity, origin, schema, capability, timeout and result. Do not automatically trust another agent’s assertion or instruction.

**Related item:** An agent’s tool is equivalent to an API exposed to an untrusted planner. Its schema and description guide use; its backend authentication, authorization and validation enforce safety.

### Provision and deliver repeatably

Use CloudFormation/CDK for networks, identities, encryption, repositories, vector infrastructure, endpoints, knowledge bases, build/release components, alarms and budgets where supported. Pin image digests and dependencies, scan images/code, generate provenance/SBOM as required, use non-root minimal containers, restrict secrets and egress, and separate build from runtime roles.

SageMaker Pipelines orchestrates ML processing/training/evaluation/registration. Step Functions coordinates broader AWS and agent/retrieval workflows; MWAA serves Airflow-based estates; CodePipeline with CodeBuild/CodeDeploy/CodeConnections connects repositories and delivery. CodeCommit is in C02 scope; its [official document history](https://docs.aws.amazon.com/codecommit/latest/userguide/history.html) records reopening to new customers on November 25, 2025. Older July 2024 closure advice is stale. Verify region, repository credentials and pipeline connections for the chosen lab. Choose by required state, integration, retry/catch, governance and operator skill.

A release pipeline should test:

- transformation, model and service code;
- data/feature/chunk/embedding/index contracts;
- prompt examples, injection/adversarial behavior and structured outputs;
- retrieval relevance, ACL leakage and citation mapping;
- tool arguments, authorization, idempotency, side effects and failures;
- model/FM quality, safety, latency, throughput and cost gates;
- IaC policy, images/dependencies and secrets;
- canary/shadow, alarm, rollback and recovery.

Version model registry/MLflow artifacts, Bedrock custom models, prompts, agent aliases/versions, guardrails, tools and knowledge-base/index manifests. Promotion should reference immutable versions and require appropriate approval. Automated retraining, fine-tuning, prompt change, agent deployment or knowledge refresh starts validation; it must not bypass it.

RAG refresh cadence follows source freshness and cost. Detect additions, changes, deletions and access-policy changes; process idempotently; publish only after completeness/retrieval/security checks. FM fine-tune releases need data/model lineage and comparison to the current base/custom version. Agent releases need scenario and side-effect regression suites.

### Verify new-account monitoring and evaluation paths

[Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-availability-change.html), [Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-availability-change.html) and [Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-availability-change.html) remain usable by existing customers but are closed to new customers. Their notices describe alternatives including direct bias metrics/SHAP, MLflow, TensorBoard and open-source monitoring with CloudWatch/QuickSight. Select only what the workload needs; a monitoring reference stack needs its own security, cost and validation work.

For agents, the [AWS AgentCore Evaluations article](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) distinguishes controlled on-demand evaluation from sampled production evaluation. Start with deterministic checks for tool identity, arguments and authorized side effects; use a calibrated rubric for answer quality. Sampling misses some incidents, so enforce critical permissions in the application. Pin the evaluator configuration and keep trace collection/minimization, processing geography and cost in the release contract. The article's examples were not deployed here.

### Scale from the actual bottleneck

Traditional endpoints scale on invocation/concurrency/latency/resource metrics. GPU workloads can be memory-, compute-, batch-, network- or startup-bound. FM systems may be constrained by token rate, model capacity, provisioned throughput, account quotas, retries or upstream/downstream limits. RAG can bottleneck at parsing, embedding, indexing, query, reranking or generation. Agents amplify calls through steps and parallelism.

Define end-to-end load, concurrency, timeouts, retry/backoff/jitter, queue/backpressure, circuit breaker, caching, quota and degradation behavior. Scaling a caller without its tool/vector/model dependency can create a retry storm.

---

## 4. Operating, Monitoring, and Securing ML and AI Solutions — 24%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html) covers production behavior, infrastructure/cost, and workload/endpoint security.

### Observe data, retrieval, model and agent separately

| Layer | Useful signals | Representative failure |
|---|---|---|
| Source/preparation | freshness, count, schema, quality, distribution, sync/deletion failures | stale or unauthorized content indexed |
| Embedding/vector | embed errors, dimension/version, index size, filter coverage, query latency | mixed embedding versions or missing ACL metadata |
| Retrieval | Recall@k/precision, score, rerank, no-result, citation/source | relevant source not retrieved or wrong tenant source returned |
| Traditional model | drift, prediction distribution, confidence/calibration, ground-truth performance, slice bias | concept drift lowers recall after labels arrive |
| FM generation | quality rubric, groundedness, refusal/safety, input/output/cache tokens, latency/error/throttle | fluent answer unsupported by context |
| Agent | goal/tool success, step count, loop, coordination, truncated stream, state, human escalation | repeated tool loop or partial side effect |
| Platform/business | CPU/GPU/memory, queue, endpoint, workflow, cost, user outcome | healthy model API but failed customer workflow |

Use CloudWatch metrics/logs/dashboards/alarms and supported generative-AI observability, Bedrock evaluations, AgentCore Observability, X-Ray, CloudTrail and Config as appropriate. Feature names and integration support are volatile. Emit correlation identifiers across application, retrieval, model and tool spans without logging sensitive prompts, context, tool data or responses indiscriminately.

Detect data drift, concept drift, label shift and model-quality degradation separately. For GenAI, also monitor prompt/input population, retrieval corpus/index, answer and safety distribution, judge/rubric stability and model/provider version. Production A/B tests need hypothesis, assignment, safety guardrails, sample/duration, outcome and rollback. Shadow tests reduce direct impact but still incur data/privacy/cost risks.

Agent monitoring needs a trace of plan/decision, model/prompt version, tool request/result metadata, state transition, error/retry, guardrail/approval and final outcome. Detect coordination failures, timeouts, malformed responses, truncated streaming, runaway steps, duplicate actions and silent partial completion. Alert on business-incomplete states, not only exceptions.

**Related item:** Observability data becomes a sensitive AI dataset. Prompts, retrieved passages, model outputs, traces and human feedback need classification, access, retention, redaction and deletion controls.

### Manage unit economics and capacity

Track cost per training run, deployed hour, prediction, document indexed, embedding, retrieved query, input/output token, agent task, tool call and successful business outcome. Allocate with tags/accounts/application metadata while avoiding sensitive labels.

Traditional optimization includes instance/right-sizing, efficient input, distributed strategy, Spot with checkpoints, batch/async modes, endpoint scaling, multi-model fit and eliminating idle resources. FM optimization includes model routing, prompt/context reduction, output limits, caching where safe, batch, provisioned versus on-demand comparison, quota and retry control. RAG optimization includes chunk/index size, embedding reuse, incremental sync, retrieval top-k/reranking and storage lifecycle. Agents require step/tool/token ceilings and prevention of loops/repeated retrieval.

Cheaper per-token is not cheaper per correct outcome if it increases retries, escalations or errors. Compare quality-latency-cost Pareto tradeoffs against representative tasks. Budget alerts are not a hard spending cap. Use them alongside bounded tokens, steps, concurrency and retries; verify the scope and timing of any automated budget action. Capacity planning includes GPUs and containers as well as model service quotas, vector query/index throughput, tool APIs, queueing and downstream databases.

### Protect identities, data, models, prompts and actions

Separate principals for humans, notebooks, data pipelines, training, evaluation, build, deployment, runtime, knowledge sync and tools. Scope `iam:PassRole`, S3/prefixes, KMS, model invocation, prompt/agent/knowledge-base operations, secrets and logs. Evaluate identity policies, resource policies, key policies/grants, SCPs, boundaries and VPC endpoint policies together.

AWS lists IAM credentials and Bedrock API keys as credential choices. Select from environment, workload identity, lifetime, scope, rotation, audit and supported feature. Prefer temporary role credentials for AWS workloads; never embed keys in code/prompts/images. The [current API-key guide](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) recommends short-term keys for production and long-term keys only for exploration. Short-term keys inherit the generating principal’s permissions and expire at the earlier of 12 hours or that session’s expiry. Plan refresh and revocation, and validate the target endpoint/region. A 90-day limit on a long-term service-specific credential does not make it a short-term session token. Tools must derive authorized user/tenant context from trusted application identity, not model text.

Use VPCs/subnets/security groups and supported private endpoints/egress controls; encrypt data/artifacts/indexes/state/logs at rest and in transit; manage secrets; restrict notebooks; and audit API actions. Scan code/dependencies/images with appropriate pipeline tools such as Inspector and supported code-analysis capabilities. Pin/sign artifacts and validate model serialization to reduce supply-chain and replacement attacks.

Threat-model data poisoning, training/test leakage, prompt injection, indirect injection in retrieved documents, jailbreaks, sensitive-data disclosure, model extraction, membership inference, excessive agency, tool injection, confused deputy, insecure output handling, denial/cost exhaustion and cross-tenant retrieval. Layer controls:

- trustworthy source and content validation;
- input classification and size/rate limits;
- strong instructions and separation of untrusted data;
- metadata/ACL enforcement and least-context retrieval;
- Bedrock Guardrails or appropriate safeguards for supported policies;
- schema validation and deterministic post-processing;
- tool allowlists, backend authorization, confirmations and sandboxing;
- output validation, monitoring, human escalation and kill switch.

Guardrails are one layer, not proof of safety. Test supported policy types, languages/modalities, placement, false positive/negative behavior, versioning, latency, logging and fallback. Responsible AI connects accuracy, fairness, explainability, privacy, safety, transparency, human oversight and governance to evidence and owners.

**Related item:** Prompt injection is an authorization design test. If untrusted content can cause a tool to exceed the user’s authority, the defect is not solved by a stronger system prompt alone.

---

## Integrated scenarios

### Scenario 1: Governed support RAG

Support staff query product manuals and customer-specific tickets. Preserve authoritative documents in S3 with version, product, language, customer ACL and deletion metadata. Extract/layout-split, embed and index into a vector store using versioned model/chunk configuration. Evaluate labeled queries for retrieval and answer/citation quality by product/language. Authenticate the user; enforce metadata filters before generation; minimize context; apply safeguards; and return citations. Deploy index/prompt/model/guardrail as one manifest. Monitor source sync/deletion, unauthorized retrieval tests, no-result/recall, groundedness, latency, tokens and escalations. Roll back prompt/model separately or switch index alias atomically.

### Scenario 2: Claims triage plus document agent

A traditional classifier predicts review priority while an agent extracts documents, checks policy and drafts a recommendation; only a human can approve payment. Use leakage-safe historical splits and cost-sensitive metrics for the classifier. Validate OCR/extraction and prompt-response examples. Give the agent narrow read-only evidence tools and a separate draft action; backend identity enforces claim/customer scope. Record state transitions and make tool calls idempotent. Test injection in documents, missing pages, conflicting sources, tool timeout, retry and duplicated request. Monitor classifier drift, extraction quality, agent completion/steps/tool failures, human disagreement, safety and cost. Never let generated text directly issue payment.

### Scenario 3: Multi-model personalization at variable load

A recommendation service combines a traditional ranking model, an FM-generated explanation and a fallback managed service. Establish an offline ranking baseline and online business metric. Deploy the ranker to a measured real-time endpoint; route explanation requests to a Bedrock model selected on quality/latency/cost; cache only non-sensitive stable results. Use feature/event time correctness, model/prompt versions and canary traffic. Set token/output limits and fall back to a templated explanation on throttle or safety failure. Trace each component, allocate cost per successful recommendation, and evaluate user outcomes without mistaking FM fluency for ranking quality.

---

## Worked decisions

The following are original synthetic exercises, with 16 local checks of expected results. They do not validate a hosted model or AWS service.

### Example 1: Retrieval quality depends on the authorized denominator

For a tenant-A query, the authorized relevant document set is {a1, a2, a3, a4}. The three retrieved IDs are {a1, a3, a9}. Recall@3 is **2/4 = 50%** and precision@3 is **2/3 = 66.7%**. A fluent answer cannot repair the two missed documents. Retrieving a tenant-B document is an authorization failure even if a judge scores the final answer highly. Apply trusted tenant filters before retrieval and test the returned IDs as well as generated text.

### Example 2: An extra model call can erase token savings

Consider hypothetical prices, not current AWS rates: primary input $4/million tokens; compressor input $1/million and output $2/million. Reducing 10,000 context tokens to 2,000 changes context cost from **$0.040 to $0.022** (0.010 + 0.004 + 0.008). Reducing them only to 6,000 costs **$0.046**, more than the baseline. Count query/system tokens, final output, retries, retrieval, caching and compute in the real comparison.

The [August 21 AWS compression article](https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/) is a useful pattern to investigate, not a guaranteed saving. Preserve source IDs; check each extracted span against its source and retain qualifying/contradictory evidence. Temperature zero does not establish deterministic or faithful extraction. Benchmark quality against the original authorized evidence as well as the shortened context, and measure end-to-end latency.

### Example 3: Tool success and business success differ

An agent calls `create_draft` for tenant A and operation 123. The backend commits, but the response times out. A retry must reuse the same tenant/operation identity and either return the existing result or report its verified status. A fresh random key can create a second draft. Reusing a key with different payload must fail. A tool response saying “success” does not prove the entire customer goal succeeded; check persisted business state, side effects and the user-visible outcome separately.

### Example 4: Evaluate every layer of a release

On 100 labeled requests, 90 retrieve the required evidence and 81 produce a correct answer. End-to-end correctness is **81%**. If all 81 correct answers are among those 90 retrieval successes, conditional generation correctness is **90%**. Reporting only 90% hides retrieval failures. If 20 sessions contain tool actions and 2 actions violate authorization, reject the release regardless of the average language-quality score. Compare judge disagreement against human labels and repeat stochastic scenarios.

### Example 5: Restore compatible artifacts

Release R1 uses embedding E1, index I1, prompt P1, model M1 and tool schema T1. R2 moves to E2/I2/P2/M2/T2. A vector query from E2 cannot safely search I1 merely because the dimensions match: the vector spaces may differ. A rollback must restore a tested compatible manifest, including access/deletion state. Keep externally committed business actions in their own audited state; reverting a model does not undo them.

## Hands-on lab path

These eight cloud labs are proposed and were not executed in this review. First reproduce the local worked decisions and document expected failures. Use synthetic/non-sensitive data in a disposable account with budgets. Verify regions, quotas, model access, price and preview/GA status before creating resources, then delete them.

1. **Data and multimodal contract:** Inventory synthetic tables, PDFs and images; define rights/classification, schema, IDs, event time, retention, ACL and deletion lineage; inject quality failures.
2. **Feature and RAG preparation:** Build leakage-safe features plus layout-aware chunks/metadata; compare two chunk configurations and document precision/recall/token tradeoffs.
3. **Embedding/vector experiment:** Pin an embedding model/version, create a small index, test filters and labeled queries, then simulate a model-version migration without mixing dimensions.
4. **Traditional and FM selection:** Train a baseline traditional model; compare two supported FMs/prompts on a rubric with latency/tokens/cost; write a build/buy/RAG/tune decision.
5. **Evaluation harness:** Implement deterministic tests, retrieval measures, traditional metrics, structured GenAI rubric, calibrated human review and a judge-model comparison with disagreement reporting.
6. **Versioned RAG/agent:** Create a safe read-only knowledge workflow or agent with schema-validated tool, tenant authorization, step limits, injection tests, state and trace evidence.
7. **Delivery pipeline:** Version data/chunks/embedding/index/model/prompt/guardrail/agent/tool; run quality/security/cost gates; canary a release and prove whole-manifest rollback.
8. **Operations and incident:** Dashboard source/retrieval/model/agent/platform/cost signals; inject stale index, tool timeout, token spike and unauthorized request; diagnose, contain, recover and clean up.

## Original knowledge checks

These are original blueprint-aligned prompts, not recalled beta questions.

1. Which facts belong in a multimodal data-rights contract?
2. When does a vector-enabled relational store fit better than a search-oriented vector engine?
3. Why does changing an embedding model usually require re-indexing?
4. How do chunk size and overlap affect retrieval quality, tokens and cost?
5. What metadata is required for citations, ACLs and deletion?
6. Why is post-retrieval tenant filtering often too late?
7. How does point-in-time feature correctness prevent leakage?
8. Which checks validate prompt-response training pairs?
9. How do masking, redaction, tokenization, anonymization and encryption differ?
10. Why can embeddings remain sensitive after source text is protected?
11. When should a deterministic workflow be preferred to an agent?
12. What requirements distinguish RAG from fine-tuning?
13. Which evidence should drive selection among Bedrock FMs?
14. Why is a leaderboard score insufficient for production model choice?
15. How do underfitting, overfitting and catastrophic forgetting differ?
16. What makes a traditional or FM experiment reproducible?
17. Why must tuning avoid the final test set?
18. What is the risk of routing simple and complex tasks to different models?
19. Which retrieval metrics must be separated from answer-quality metrics?
20. Why do BLEU, ROUGE or BERTScore not prove factual correctness?
21. How should human evaluators be calibrated and disagreements handled?
22. What biases can affect an LLM-as-a-judge?
23. Why should a candidate model not be its only evaluator?
24. Which artifact versions define a complete GenAI release?
25. When does Batch Transform fit better than a persistent endpoint?
26. Which requirements justify provisioned FM capacity?
27. What must be tested when importing a model into AWS?
28. How should a knowledge-base refresh handle deletion and failed documents?
29. Why does an agent tool require backend authorization even with a strong prompt?
30. What state belongs in a session versus durable business storage?
31. Which failures indicate a coordination problem rather than a model-quality problem?
32. How do prompt, agent and fine-tuned-model versions enter CI/CD?
33. Why should automated refresh or retraining stop at an evaluation gate?
34. What can cause GPU scale-out to fail to improve throughput?
35. Which signals expose retrieval failure hidden by a fluent answer?
36. How do data drift, retrieval drift and judge drift differ?
37. What dimensions belong in FM and agent unit economics?
38. When can caching reduce cost without leaking data or serving stale policy?
39. How should IAM credentials and Bedrock API keys be selected and protected?
40. Which controls mitigate indirect prompt injection from retrieved documents?
41. Why is a guardrail not a complete safety architecture?
42. Which evidence supports a kill-switch or rollback decision?

## Answer explanations

1. Record owner, license/consent, permitted use, classification, residency, retention/deletion, entity/time, modality, lineage and access policy.
2. A relational vector extension can fit transactional metadata and SQL joins; a search engine may better fit combined lexical/vector retrieval and search operations. Benchmark required filters and scale.
3. A new model changes the vector space, often its dimension too; re-embed and validate a versioned replacement index rather than mixing representations.
4. Large chunks may retain context but add noise/tokens; overlap reduces boundary losses while duplicating storage and evidence. Tune against labeled queries.
5. Keep stable source/document/chunk IDs, version, page/section, timestamps, trusted tenant/ACL attributes and deletion lineage.
6. Unauthorized content can enter rerankers, logs, caches or model context before late filtering. Enforce policy at retrieval and every downstream boundary.
7. Select features that were valid and available for the original decision, with explicit late-correction and staleness rules.
8. Check rights, correct pairing, label quality, duplicates, secrets, unsafe content, representativeness and separation from evaluation data.
9. Masking changes display, redaction removes content, tokenization substitutes values, anonymization addresses re-identification, and encryption controls readability with keys.
10. Embeddings encode information about the original content and can support inference or linkage; protect the index, query logs and backups accordingly.
11. Prefer a workflow for mandatory order, clear rules, approvals and bounded state transitions; use agent planning only where flexibility has measured value.
12. RAG retrieves current/private evidence and provenance; tuning adapts behavior from examples. Neither automatically solves the other problem.
13. Use representative quality and safety evaluations plus modality, context, latency, region, capacity, customization, terms and total cost.
14. A leaderboard may use a different population, metric, prompt, cost and risk profile from the application.
15. Underfitting fails to learn enough; overfitting fails to generalize; catastrophic forgetting loses earlier capabilities during adaptation.
16. Pin data/splits, code/dependencies, artifacts, model/prompt/retrieval/judge versions, parameters and available seeds; record nondeterminism and repeated outcomes.
17. Using final-test feedback to choose candidates contaminates the estimate; tune on validation, then evaluate the frozen candidate.
18. Routing errors can send difficult or sensitive work to an unsuitable model; evaluate routing confidence, subgroup quality, fallback and compounded latency/cost.
19. Measure authorized relevance, recall/ranking and source freshness separately from answer correctness, groundedness, citations and task completion.
20. Overlap and semantic similarity can reward a plausible but false answer; compare claims with trusted evidence and the task rubric.
21. Use clear examples, qualified reviewers, blinded comparisons where practical, agreement measures and adjudication of disagreements.
22. Judge results can depend on answer order, verbosity, style, model family and rubric wording; test and calibrate these effects.
23. Shared errors and self-preference can hide failures; combine deterministic checks, human labels and independently assessed judgments.
24. Include source/chunk snapshot, embedding/index, model, prompt, guardrail, agent, tools, code, dependencies, policies and evaluator configuration.
25. Use Batch Transform for offline complete-input work with a completion deadline rather than an always-available response.
26. Predictable sustained demand or a capacity requirement may justify provisioned throughput; verify model/mode support and measured utilization economics.
27. Verify architecture/format, tokenizer, license, supported import target, runtime outputs, security and performance on representative inputs.
28. Propagate deletion/access changes, quarantine failed documents, reconcile completeness and publish only a validated index snapshot.
29. Prompts guide a model; trusted backend identity, authorization and validation must constrain actions even when the model is manipulated.
30. Session memory supports conversation; durable business records preserve authoritative, auditable state across retries and sessions.
31. Look for duplicate/missing handoffs, conflicting state, timeouts, tool errors, loops and incomplete streams before blaming language quality.
32. Treat versions as immutable release artifacts with evaluation, approval, staged deployment and compatible rollback.
33. Fresh data or a new model can introduce leakage, regressions or access failures; publication needs evidence and explicit gates.
34. The bottleneck may be memory, input I/O, network synchronization, token quota, warmup or downstream tools; more GPUs do not fix those automatically.
35. Inspect relevance labels, missed sources, unauthorized IDs, source age and citation mismatches; fluency is not retrieval evidence.
36. Data drift changes input population; retrieval drift changes corpus/index/relevance behavior; judge drift changes the measurement system itself.
37. Count all model and embedding calls, input/output/cache tokens, vector/compute/storage, retries, tools, evaluation and human escalation per successful outcome.
38. Use a tenant/permission-aware key with model/prompt/source versions, freshness/deletion rules and an acceptable retention policy; reject stale or cross-tenant hits.
39. Prefer temporary workload identity; if bearer keys are required, use scoped short-term production keys with refresh/revocation and no logging or embedded secrets.
40. Enforce trusted retrieval filters, minimum context, tool authorization, input/output schemas, bounded actions and approval where needed; test malicious source content.
41. A guardrail cannot replace identity, authorization, secure storage, deterministic validation or operational recovery.
42. Use breached quality/security/cost/latency gates and reliable trace/state evidence, with a tested compatible rollback and authority to stop execution.

## Final review checklist

- I can explain the 28/24/24/24 domain weighting and every task in the September 1 blueprint.
- I can map all additions and removals from C01 using the official comparison.
- I can design both a traditional ML lifecycle and a versioned RAG/agent lifecycle.
- I choose data formats, features, chunks, embeddings, vector stores, filters and refresh from requirements.
- I distinguish prompting, RAG, fine-tuning, continued pre-training, distillation and custom training.
- I evaluate traditional models, retrieval, generation and agents with separate measures and calibrated human evidence.
- I version and test model, prompt, guardrail, agent, tool, knowledge/index and application artifacts together.
- I monitor data, vector/retrieval, model/FM, agent, platform, business, security and cost signals separately.
- I can reason through IAM/KMS/VPC/credential, prompt-injection, excessive-agency, supply-chain and cross-tenant boundaries.
- I have rechecked beta code, date, price, duration, questions, result timing and GA status on the live AWS page.

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Pick one primary path, build the scenarios that expose your gaps, and use legitimate practice for remediation. MLA-C02 preparation is still early: verify that a provider maps the September 1 detailed skills—not merely the four familiar C01 domain headings. Times are provider-stated where stable and otherwise transparent estimates.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html), detailed domains, and comparison | Public | 4–7 hours for a complete objective/delta map |
| [AWS certification page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) | Public | 10–15 minutes; recheck immediately before booking |
| [AWS MLA-C02 update announcement](https://aws.amazon.com/blogs/training-and-certification/updates-to-aws-certified-machine-learning-engineer-associate-mla-c02/) | Public | 10–20 minutes for audience, dates and beta contract |
| [AWS Official Practice Question Set catalog](https://explore.skillbuilder.aws/learn/course/external/view/elearning/9153/aws-certification-official-practice-question-sets-english) | Free AWS account; some related items subscription | Allow 30–90 minutes as a planning estimate; sign-in is needed to verify the current C02 set and question count |
| [SageMaker ML lifecycle](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html) and [Pipelines tutorial](https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html) | Public; AWS usage may cost | 6–12 hours selected reading and lab |
| [Amazon Bedrock user guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) | Public; AWS usage may cost | 12–24 hours selected model, RAG, evaluation, prompt, agent and guardrail labs |
| [AWS query-aware compression article](https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/) (August 21, 2026) | Public | 45–90 minutes estimated reading and cost/quality exercise; code not executed |
| [AWS AgentCore Evaluations article](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) (March 31, 2026) | Public | 45–90 minutes estimated reading and evaluation-plan exercise; deployment not executed |
| [AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) | Public | 4–8 hours selected lifecycle review |
| [Pluralsight MLA-C01 path](https://www.pluralsight.com/paths/aws-certified-machine-learning-engineer-associate-mlac01) | Paid/trial | 20 listed hours for retained traditional-ML/MLOps foundation; then close every C02 comparison addition separately |
| [O'Reilly/Sybex MLA-C01 Study Guide](https://www.oreilly.com/library/view/aws-certified-machine/9781394319954/) | Paid/subscription | Allow 15–25 hours as a reading estimate; current edition/length not reverified; retained C01 foundation only |
| [Tutorials Dojo MLA-C02-labeled practice page](https://portal.tutorialsdojo.com/courses/aws-certified-machine-learning-engineer-associate-mla-c02-practice-exams/) | Paid | **Wait/verify before purchase:** September 28 public page has C02 domain sections but still mixes 65 questions with 170 minutes; AWS beta is 85. Verify detailed coverage and original-question provenance; paid bank not inspected |

This review did not establish complete C02 coverage inside any paid course or practice bank. Older C01 catalogs are foundation material; map every C02 addition separately. Public titles, course shells and a renamed exam code do not establish lesson quality or coverage. Avoid recalled-question collections.
