---
exam_code: MLA-C02
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-01
---

# MLA-C02 AWS Certified Machine Learning Engineer - Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, beta warnings, links, and exam-integrity compliance were checked on September 1, 2026—the day registration opened. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mla-c02-coverage-record). The [official MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html) is authoritative.

**Current baseline:** Initial MLA-C02 four-domain blueprint published September 1, 2026; beta registration is open and English beta delivery begins September 29<br>
**Beta appointment code:** **ME1-C02**. The guide/version is MLA-C02; AWS currently uses ME1-C02 for the beta scheduling code.<br>
**Upcoming blueprint/delivery change:** Beta is 170 minutes, 85 multiple-choice/multiple-response questions, USD 75, and English only. AWS says the standard MLA-C02 version will arrive in early 2027; exact GA dates, standard delivery metadata, learning assets, and any blueprint revision are **VERIFY CURRENT**.<br>
**Important freshness boundary:** This is not a renamed C01. AWS explicitly added vector databases, multimodal data, embeddings, RAG preparation and monitoring, FM data preparation/customization/deployment, Bedrock evaluations and prompt management, human/LLM evaluation, agents/protocols/state/versioning/observability, GPU/AI cost patterns, FM credentials, pipeline vulnerability checks, and Guardrails. Use the official [C01-to-C02 comparison](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/mla-02-comparison.html) to gap-check older material.<br>
**Official source:** [AWS Certified Machine Learning Engineer - Associate MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html)

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

SageMaker Pipelines orchestrates ML processing/training/evaluation/registration. Step Functions coordinates broader AWS and agent/retrieval workflows; MWAA serves Airflow-based estates; CodePipeline with CodeBuild/CodeDeploy/CodeConnections connects repositories and delivery. AWS currently lists CodeCommit in C02 scope, but service availability/onboarding behavior is **VERIFY CURRENT**. Choose by required state, integration, retry/catch, governance and operator skill.

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

Cheaper per-token is not cheaper per correct outcome if it increases retries, escalations or errors. Compare quality-latency-cost Pareto tradeoffs against representative tasks. Budgets and alerts cap surprises; they do not substitute for per-request controls. Capacity planning includes GPUs and containers as well as model service quotas, vector query/index throughput, tool APIs, queueing and downstream databases.

### Protect identities, data, models, prompts and actions

Separate principals for humans, notebooks, data pipelines, training, evaluation, build, deployment, runtime, knowledge sync and tools. Scope `iam:PassRole`, S3/prefixes, KMS, model invocation, prompt/agent/knowledge-base operations, secrets and logs. Evaluate identity policies, resource policies, key policies/grants, SCPs, boundaries and VPC endpoint policies together.

AWS lists IAM credentials and Bedrock API keys as credential choices. Select from environment, workload identity, lifetime, scope, rotation, audit and supported feature. Prefer temporary role credentials for AWS workloads; never embed keys in code/prompts/images. API-key features and constraints are **VERIFY CURRENT**. Tools must derive authorized user/tenant context from trusted application identity, not model text.

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

## Hands-on lab path

Use synthetic/non-sensitive data in a disposable account with budgets. Verify regions, quotas, model access, price and preview/GA status before creating resources, then delete them.

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

This is **not a complete list**, and it is not meant to be consumed in full. Pick one primary path, build the scenarios that expose your gaps, and use legitimate practice for remediation. MLA-C02 material is launch-day content: verify that a provider maps the September 1 detailed skills—not merely the four familiar C01 domain headings. Times are provider-stated where stable and otherwise transparent estimates.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html), detailed domains, and comparison | Public | 4–7 hours for a complete objective/delta map |
| [AWS certification page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) | Public | 10–15 minutes; recheck immediately before booking |
| [AWS MLA-C02 update announcement](https://aws.amazon.com/blogs/training-and-certification/updates-to-aws-certified-machine-learning-engineer-associate-mla-c02/) | Public | 10–20 minutes for audience, dates and beta contract |
| [AWS Official Practice Question Set catalog](https://explore.skillbuilder.aws/learn/course/external/view/elearning/9153/aws-certification-official-practice-question-sets-english) | Free AWS account; some related items subscription | 30 minutes plus 45–90 minutes rationale review; 20 C02-aligned questions listed |
| [SageMaker ML lifecycle](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html) and [Pipelines tutorial](https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html) | Public; AWS usage may cost | 6–12 hours selected reading and lab |
| [Amazon Bedrock user guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) | Public; AWS usage may cost | 12–24 hours selected model, RAG, evaluation, prompt, agent and guardrail labs |
| [AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) | Public | 4–8 hours selected lifecycle review |
| [Pluralsight MLA-C01 path](https://www.pluralsight.com/paths/aws-certified-machine-learning-engineer-associate-mlac01) | Paid/trial | 20 listed hours for retained traditional-ML/MLOps foundation; then close every C02 comparison addition separately |
| [O'Reilly/Sybex MLA-C01 Study Guide](https://www.oreilly.com/library/view/aws-certified-machine/9781394319954/) | Paid/subscription | 13h 10m / 448 pages for retained C01 foundation; not complete C02 preparation |
| [Tutorials Dojo MLA-C02-labeled practice page](https://portal.tutorialsdojo.com/courses/aws-certified-machine-learning-engineer-associate-mla-c02-practice-exams/) | Paid | **Wait/verify before purchase:** page still showed 65-question and C01-labeled internal sets on September 1; recheck until the bank explicitly maps C02 skills |

No exact mature MLA-C02 Pluralsight path, O'Reilly title, LinkedIn Learning course, Whizlabs course, MeasureUp assessment, or trustworthy long-form YouTube course was independently verified on launch day. That gap is useful information: use the official blueprint and product labs now, and recheck vendor catalogs weekly rather than filling it with similarly named or dump-like material.
