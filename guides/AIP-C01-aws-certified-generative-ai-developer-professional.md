---
exam_code: AIP-C01
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# AIP-C01 AWS Certified Generative AI Developer - Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#aip-c01-coverage-record). The [official AIP-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html) is authoritative.

**Current baseline:** Current standard five-domain AIP-C01 AWS Certified Generative AI Developer - Professional guide; 65 scored plus 10 unscored questions<br>
**Upcoming blueprint change:** None announced on the official exam guide or certification page as of September 1, 2026.<br>
**Important freshness boundary:** AIP-C01 moved from its earlier beta period to a standard exam in March 2026, with the standard scope refreshed for fast-moving services including Amazon Bedrock AgentCore. Use the current `ai-professional-01` guide—not an early beta outline or an unofficial AP1/AIGDP code. Model catalogs, APIs, regions, quotas, pricing, safety features, AgentCore components, Strands, AWS Agent Squad, MCP, and learning products are **VERIFY CURRENT**.<br>
**Official source:** [AWS Certified Generative AI Developer - Professional exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html)

## How to use this guide

AIP-C01 tests whether you can move from a generative-AI proof of concept to a production application: select and abstract models, build governed data and retrieval, implement agents/tools and enterprise integration, layer safety/security, measure quality/cost/latency, and troubleshoot the whole system. AWS explicitly places model development/training, advanced ML techniques, and feature engineering outside the target role, though deployment/lifecycle of customized models and data preparation for FM consumption remain in scope.

AWS targets candidates with two or more years building production applications on AWS or open-source technologies, general AI/ML or data-engineering experience, and one year implementing GenAI solutions. The certification page lists a 180-minute, 75-question, USD 300 exam in English, Japanese, Korean, and Simplified Chinese. The detailed guide identifies 65 scored and 10 unidentified unscored items and a 750 minimum scaled score. Recheck the [live certification page](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/) before scheduling.

For every GenAI scenario, reason through this system:

1. Define user/business outcome, unacceptable harm, data rights, latency, scale, availability, budget, and human-oversight need.
2. Establish an evaluation set and baseline before selecting a model or architecture.
3. Decide what belongs in prompt/context, retrieval, tool/action, structured deterministic code, or model customization.
4. Design identity, network, data lineage, privacy, safety, authorization, and evidence across the whole path.
5. Implement explicit contracts for models, embeddings, chunks, prompts, tools, agent state, output schemas, and fallbacks.
6. Observe quality, grounding, safety, tool behavior, latency, tokens, cost, and business outcomes; test changes continuously.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Foundation Model Integration, Data Management, and Compliance | 31% | How are model, data, vector/retrieval, and prompt decisions designed as a governed system? |
| Implementation and Integration | 26% | How are agents, tools, models, APIs, workflows, and enterprise systems integrated reliably? |
| AI Safety, Security, and Governance | 20% | How are misuse, sensitive data, authorization, traceability, fairness, and policy controlled in depth? |
| Operational Efficiency and Optimization for GenAI Applications | 12% | How are token/model/vector/tool cost, latency, throughput, quality, and business value optimized together? |
| Testing, Validation, and Troubleshooting | 11% | How is probabilistic system quality measured, released, diagnosed, and improved? |

The first three domains are 77% of scored content. Do not study safety or evaluation as an appendix: they constrain the design from the first requirement.

---

## 1. Foundation Model Integration, Data Management, and Compliance — 31%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html) covers requirements/architecture, FM selection, input-data pipelines, vector stores, retrieval, and prompt engineering/governance.

### Start with a use-case and evaluation contract

Define task, users, languages/modalities, knowledge freshness, output format, action authority, latency percentile, traffic/throughput, availability, privacy/residency, safety, explainability, cost per successful outcome, and escalation. A proof of concept should validate a risky hypothesis—not merely show fluent text.

Build a representative evaluation set with normal, rare, ambiguous, adversarial, sensitive, stale, and refusal cases. Record expected facts/evidence, acceptable response ranges, forbidden behavior, tool outcomes, and business metric. Baseline a simple prompt/model and a non-GenAI or deterministic alternative where appropriate. This prevents selecting architecture by demo impression.

Use the [AWS Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) to review lifecycle decisions across operational excellence, security, reliability, performance, cost, sustainability, and responsible AI. It supports architecture judgment; it is not the exam blueprint.

### Select models by measured fit

Compare capability/modalities/language, context/output limits, latency, throughput, quality on your set, safety behavior, customization options, tool/structured-output support, regional availability, compliance/data terms, resilience, and price. Larger models can raise quality on complex tasks but also latency/cost; smaller models can route/classify/extract routine work. Use cascading or routing only if the routing error, observability, and fallback are acceptable.

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) offers managed access to multiple FMs and GenAI building capabilities. SageMaker AI supports customer-managed/custom-model deployment patterns. Abstract the model contract—request/response schema, capabilities, parameters, error normalization, metrics, safety policy, and fallback—without pretending providers are behaviorally interchangeable.

Resilience can include exponential backoff with jitter, timeouts, concurrency/rate limits, circuit breakers, queues for asynchronous work, Cross-Region Inference where supported, provider/model fallback, cached/degraded results, and human escalation. A fallback model must pass safety, data, and quality policy; availability alone is insufficient.

Model customization options range from prompt/RAG through parameter-efficient adaptation, fine-tuning, or other supported methods. Choose only when evaluation shows the simpler layer cannot meet behavior. Version data, model/base, hyperparameters/adapters, prompt, evaluation, container, endpoint/config, approval, and rollback. The target role deploys/manages customization rather than inventing advanced training algorithms.

**Related item:** RAG changes the information supplied at inference; customization changes model behavior/weights or adapters. They can complement one another and solve different failure classes.

### Govern multimodal input data

For text, image, audio, video, or tabular inputs, define source authority/license/consent, owner, classification, lineage, format/size, language, quality, malware/content risk, duplication, update/delete behavior, and retention. Validate schema and content before use. Normalize/segment/transcribe/extract only with traceable transformations; preserve source-to-derived links and deletion propagation.

Model-specific request formats, conversation roles, token/context limits, image/audio constraints, and structured outputs are API contracts. Validate and reject malformed inputs deliberately. Do not silently truncate critical content. Record what was omitted and route oversized work to chunking/summarization/batch workflows according to requirements.

### Design vector stores and retrieval as one system

An embedding maps content/query into a vector space. Similarity depends on embedding model/version, dimension, preprocessing, language/domain, distance metric, and index. Do not change the embedding model for only new records; either maintain compatible versioned indexes or re-embed deliberately.

Choose OpenSearch vector capabilities, Aurora PostgreSQL/pgvector, Bedrock Knowledge Bases with supported stores, or other services from scale, latency, filtering, hybrid search, operations, tenancy, backup, consistency/freshness, and cost. A vector database is not the document authority. Keep source ID/version, chunk offsets, owner, classification, ACL/tenant attributes, timestamps, and lineage.

Chunking controls retrieval units. Compare fixed-size/overlap, sentence/semantic, document-structure/hierarchical, and modality-specific segmentation. Too small loses context; too large dilutes relevance and consumes tokens. Validate with retrieval metrics and end-to-end answer quality, not a universal chunk size.

RAG flow:

1. authorize the user and query scope;
2. normalize/decompose/expand the query only where evaluated;
3. embed with the matching version;
4. retrieve with tenant/ACL/metadata filters;
5. optionally combine keyword/vector results and rerank;
6. assemble bounded, attributed context;
7. prompt the FM to use evidence and abstain when insufficient;
8. validate output/citations and record lineage without leaking sensitive content.

Retrieval freshness needs change detection, reprocessing, re-embedding, upsert/delete, index readiness, reconciliation, and lag monitoring. Event-driven updates improve freshness but need duplicate/order/retry handling; scheduled rebuilds can simplify reconciliation. Test revoked access and deleted source propagation.

**Related item:** Grounding reduces unsupported claims only when retrieval returns relevant, authorized, current evidence and the generation step actually uses it. RAG does not guarantee factuality.

### Version prompts as production artifacts

Define system instructions, role/task, constraints, context delimiters, examples, refusal behavior, output schema, tool contract, parameters, and version. Bedrock Prompt Management/Flows or a governed repository can support reuse/approval. Separate trusted instructions from untrusted user/retrieved/tool content; label and delimit each.

Use zero/few-shot examples, decomposition, structured output, self-check/verification, or chained flows only where evaluation supports them. Avoid requiring private hidden reasoning to be exposed. Prompt changes need regression/safety/cost tests, canary release, audit, and rollback just like code.

---

## 2. Implementation and Integration — 26%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html) covers agents/tools, model deployment, enterprise integration, FM APIs, and application/development patterns.

### Build agents as bounded state machines

An agent loop observes a request/state, plans or selects a next step, invokes a tool, observes the result, and continues until a stop condition. Production design specifies:

- task scope and success/failure definition;
- allowed tools/actions/resources and identity per tool;
- typed input/output schemas and validation;
- working, session, long-term, and enterprise-record state ownership;
- maximum steps, tokens, duration, retries, cost, and recursion;
- idempotency/transaction/compensation for side effects;
- human approval before sensitive or irreversible actions;
- trace, audit, safety filters, and emergency disable.

Bedrock Agents/Flows, AgentCore components, Strands Agents, AWS Agent Squad, Step Functions, Lambda, containers, and custom frameworks can participate according to current capabilities. Names and availability are **VERIFY CURRENT**. Separate orchestration from tool authorization: an FM may propose an action, but deterministic code and IAM must validate caller, parameters, policy, resource scope, state, and approval.

MCP standardizes context/tool integration patterns; it does not make a server trustworthy. Authenticate/authorize, validate schemas, allowlist tools, constrain network/filesystem/data, prevent confused deputy and indirect prompt injection, rate-limit, audit, and pin/review implementations. Use Lambda for suitable stateless/lightweight servers and containers for longer-lived or more complex needs according to runtime requirements.

Multi-agent designs add delegation, message/state contracts, loop/deadlock risk, conflicting goals, cost, latency, and evaluation complexity. Use specialized agents only when measured modular benefit exceeds the coordination surface.

**Related item:** “Autonomous” describes how often the system proceeds without human input, not permission to operate without boundaries, observability, or accountability.

### Choose inference/deployment deliberately

Bedrock on-demand/serverless invocation, provisioned throughput, batch, Cross-Region Inference and supported latency-optimized modes solve different traffic, latency, availability, and cost needs. SageMaker endpoints or container infrastructure fit supported customized/open models when control is required. Confirm model access, region, quotas, concurrency, payload/context, streaming, pricing, and data behavior.

For self-hosted FMs, own image/model artifacts, accelerator type/memory, loading/sharding, quantization compatibility, batching, autoscaling, health/readiness, endpoint security, patching, observability, failover, and cost. Do not default to self-hosting because unit inference appears cheaper at one utilization point.

Use immutable versions and canary/blue-green traffic with an evaluation gate. Model changes can alter tokenization, output schema, safety, tool calls, and retrieval compatibility even when API code does not change.

### Integrate APIs and enterprise workflows

Synchronous invocation fits bounded interactive latency; streaming improves perceived latency but requires partial-output safety, cancellation, backpressure, client reconnection, and final-state handling. Asynchronous queues/batch fit long/large/variable work and require correlation, idempotency, status, retry, DLQ, timeout, and result retention.

API Gateway, Lambda, containers, Step Functions, EventBridge, SQS/SNS, AppSync/WebSockets, and SDKs implement standard distributed-system patterns around the FM. Validate request/auth/quota; do not leak provider errors or prompts; normalize model response and usage; implement retry only for retryable failures; set total time/cost budget; and trace each boundary.

Enterprise integration must map system of record, identity/federation, authorization, data classification/residency, network path, schema/contract, synchronization/CDC, latency, failure semantics, human approval, audit, and rollback. Use events for loose coupling where suitable. Never let a generated value update CRM/ERP/ticket/financial systems without deterministic validation and authorization appropriate to impact.

Create a GenAI gateway only if it provides useful centralized model abstraction, authentication, quotas, safety, routing, cost/usage, logging/redaction, and policy. Avoid a bottleneck that erases model-specific capability or becomes a universal data exfiltration point.

### Deliver GenAI components with CI/CD

Version code, IaC, dependencies, prompt, model/config, embedding/index schema, chunks/transformers, guardrail/policy, tool schemas, evaluation sets, thresholds, dashboards, and runbooks. Build and scan immutable artifacts; deploy to isolated test; run deterministic plus probabilistic evaluation; canary; monitor; promote or roll back.

Amazon Q Developer can assist code/refactoring/testing, but generated changes require source review, tests, security/licensing checks, and ownership. AI assistance does not replace engineering evidence.

---

## 3. AI Safety, Security, and Governance — 20%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html) covers input/output safety, data security/privacy, governance/compliance, and responsible AI.

### Use defense in depth for probabilistic behavior

| Layer | Representative controls |
|---|---|
| Request | authentication, authorization, rate/quota, size/schema/type, PII/content classification |
| Prompt/context | trusted-instruction separation, delimiters, ACL-filtered retrieval, context limits, secret removal |
| Model | approved model/version/parameters, Bedrock Guardrails, provider safety settings, refusal policy |
| Tool/action | allowlist, typed parameters, least-privilege role, state checks, approval, idempotency, transaction limits |
| Output | schema validation, citation/evidence verification, PII/toxicity/policy filters, deterministic business rules |
| Runtime | private endpoints/network, encryption, secrets, logging/redaction, anomaly detection, kill switch |
| Lifecycle | adversarial evaluation, red team, monitoring, incident response, model/prompt/tool retirement |

Prompt injection attempts to make untrusted content override the application's intended control. Treat user input, retrieved documents, websites, tool output, messages, and memory as data—not instructions. Filtering alone is insufficient; enforce authority outside the model. Indirect injection becomes especially dangerous when an agent has tools.

Guardrails can filter denied topics/content, sensitive information, grounding or other supported policy dimensions, but verify current coverage, language/modality, placement, latency, and false positives/negatives. Combine deterministic validation, model-based moderation, grounded evidence, tool boundaries, and humans according to risk.

### Protect identity, data, and privacy

Map principals and data flow from user through API/orchestrator/model, prompt store, logs/traces, vector store, source system, tools, feedback, and evaluation. Apply least-privilege IAM/resource/key policies, temporary credentials, VPC endpoints/private paths where required, encryption, secret management, tenant isolation, and audit.

Minimize sensitive input. Detect/redact/tokenize/mask PII before model use when possible; prevent it from appearing in prompts, embeddings, logs, caches, feedback, or outputs without a governed need. Define residency, retention, deletion, legal basis/consent, data-owner approval, and third-party model/provider terms. Verify deletion across source, chunks, embeddings, caches, backups, and derived evaluation data.

An embedding can reveal semantic information and should inherit source sensitivity. Metadata filters are part of authorization but not a substitute for identity enforcement. Test cross-tenant queries, index mistakes, cache keys, and tool access.

### Make governance executable

Maintain an AI system record: owner, intended/prohibited use, users, risk tier, models/providers/versions, data sources/rights/lineage, prompts, retrieval, tools/agency, safeguards, evaluations/thresholds, limitations, regions, retention, monitoring, incidents, and change approvals. Model cards and system cards communicate limitations and evidence; they do not remove operational controls.

Translate policy to automated pre-deploy tests, guardrail/policy configuration, runtime checks, monitoring, periodic review, and exception workflow. Preserve who approved what version based on which evidence. Track sources/citations and decision/tool logs according to privacy policy.

Responsible AI concerns include fairness, explainability/transparency, privacy/security, robustness/safety, controllability, and accountability. Choose metrics and review groups relevant to the harm; one average quality score cannot prove fairness. Human/LLM-as-judge evaluation needs clear rubric, calibration, disagreement handling, privacy, and judge-bias/model awareness.

**Related item:** Showing internal reasoning text is not reliable explainability and may disclose sensitive information. Prefer source attribution, decision factors, tool/action audit, confidence/uncertainty signals, and documented limitations.

---

## 4. Operational Efficiency and Optimization — 12%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html) covers token/resource cost, performance, retrieval/throughput, and holistic GenAI monitoring.

### Optimize a quality-constrained objective

Track cost per successful/approved task, not merely cost per token. Break down input/output tokens, embedding, vector queries/storage, reranking, guardrails, tool/API calls, agent steps, retries, compute, data transfer, caching, logging, and human review. Relate to quality, safety, latency, completion, escalation, conversion, or labor saved.

Optimization levers include:

- route routine work to a smaller evaluated model and escalate complex/low-confidence cases;
- shorten instructions/context while preserving requirements and evidence;
- improve chunking/filter/reranking so fewer high-value chunks enter context;
- cap output and agent steps/tools; stop loops;
- cache only when identity/tenant, freshness, prompt/model/policy version, safety, and invalidation are correct;
- batch offline work and embedding generation;
- select on-demand versus provisioned capacity from measured utilization and latency;
- parallelize independent steps while respecting quota/cost and partial failure;
- remove redundant judge/model/tool calls.

Prompt caching and semantic caching have different invalidation and privacy risks. A semantic cache can return a plausible but unauthorized or stale answer unless the key includes security and version context.

### Measure latency and throughput end to end

Decompose DNS/network/gateway, queue, orchestration, retrieval, rerank, prompt assembly, time to first token, generation, tool calls, validation, and persistence. Streaming improves perceived response time but not necessarily total time or cost. Measure p50/p95/p99, tokens/second, queue time, concurrency, throttles, retries, error rate, and user abandonment.

Vector performance depends on index/algorithm/parameters, shards/partitions, filters, dimensions, data distribution, refresh, query complexity, cache, and hardware/service capacity. Optimize jointly with recall/relevance; a fast empty or irrelevant result is failure.

### Observe behavior, not just infrastructure

Create privacy-aware traces connecting request, tenant/use case, prompt/model/parameter version, retrieval IDs/scores, guardrail result, agent/tool steps, token/latency/cost, validation, feedback, and outcome. Redact or sample payloads according to policy.

Monitor availability/errors/throttling, latency, tokens/cost, retrieval relevance/latency, grounding/factuality, refusal, unsafe/PII rates, schema validity, agent completion/steps/tool failure, user feedback, business result, and distribution/drift. CloudWatch, Bedrock invocation logging, X-Ray/OpenTelemetry, application logs, cost tools, and evaluation pipelines each cover part of the picture.

Alert on actionable deviation with owner/runbook, not every model variation. Model, data, prompt, retrieval, traffic, user, and tool changes can all shift outcomes.

---

## 5. Testing, Validation, and Troubleshooting — 11%

The official [Domain 5 page](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html) covers multi-perspective evaluation, user feedback, continuous QA, RAG/agent/deployment validation, and system troubleshooting.

### Evaluate components and the complete outcome

Use a versioned dataset split by use case, language, cohort, difficulty, risk, freshness, and adversarial pattern. Prevent test leakage. Define rubric and thresholds before examining candidate outputs.

| Layer | Useful evidence |
|---|---|
| Retrieval | recall/precision or relevance at k, MRR/nDCG where appropriate, filter/ACL correctness, latency, freshness |
| Generation | factuality/groundedness, relevance, completeness, instruction following, fluency, citation correctness |
| Safety | harmful input/output, injection/jailbreak, PII leakage, refusal/helpfulness, tool misuse |
| Agent | task success, valid tool selection/arguments, steps, loop/timeout, state, side-effect correctness, human escalation |
| Operations | availability, error/throttle, latency, tokens/cost, retries, cache, throughput |
| Business/user | acceptance, resolution, conversion, escalation, satisfaction, harm/complaint and human correction |

Exact-match/ROUGE-style metrics can help deterministic or summarization cases but miss semantic and factual quality. Embedding/model-based scores can be biased. LLM-as-judge scales qualitative review but needs rubric, judge version, calibration against humans, order/blind controls, and disagreement analysis. Human evaluation needs trained reviewers, privacy, sampling, adjudication, and inter-rater evidence.

Use offline regression before release, shadow/canary/A-B where ethical and safe, and continuous sampled evaluation after release. A model/prompt winner must meet safety and cost/latency constraints; average improvement cannot hide critical cohort regressions.

### Troubleshoot by isolating the layer

1. Reproduce with sanitized request and record all versions/IDs/timestamps.
2. Validate identity, region, quota, endpoint, API schema, timeout, retry, streaming, and service error.
3. Check tokenization/context length, truncation, roles, delimiters, prompt variables, parameters, and output schema.
4. Inspect source ingestion, transformation, chunking, embedding version/dimension, metadata/ACL, index freshness, query, filters, search/rerank results.
5. Trace agent state, plan/stop, tool choice/arguments, permissions, tool response, idempotency, loops, and human gate.
6. Evaluate guardrail/moderation/input/output validation and possible false positive/negative.
7. Compare golden-set quality and operational metrics before/after the change; rollback or route safely.

For poor RAG answers, separate retrieval failure from generation failure. If the correct source is absent, inspect authorization, ingestion, chunk, embedding, query, filter, index, and rank. If present but unused/misquoted, inspect context assembly, prompt/instructions, context position/volume, model, parameters, citations, and output validation.

For inconsistent output, control model/version/parameters, prompt/order, retrieval results, tool outputs, and random sampling; use schema constraints and validation. Do not promise deterministic natural language where the business requirement actually needs deterministic code.

**Related item:** A golden dataset is a maintained measurement asset, not a frozen truth. Update it through governed review as products, policies, data, users, and risks change, while preserving historical comparability.

---

## Integrated scenarios

### Scenario 1: Regulated support assistant

A support assistant must answer from customer-specific manuals and may draft—but not execute—account changes. Authenticate and tenant-filter every source query, track document rights/version/deletion, use hybrid retrieval/reranking with citations, and refuse insufficient evidence. Redact sensitive inputs/logs, apply guardrails plus deterministic output rules, and keep account-change APIs outside direct model authority; require a human-approved structured request. Evaluate grounding, citation, cross-tenant leakage, injection, PII, refusal/helpfulness, latency, cost, and support resolution before canary release.

### Scenario 2: Agentic incident helper

An agent summarizes telemetry and proposes remediation. Give read-only tools first, typed/allowlisted parameters, short-lived scoped identities, step/time/token budgets, trace, and a stop/escalation condition. Separate untrusted logs from instructions. For an approved action, use deterministic preconditions, change ticket/human approval, idempotent runbook, blast-radius/rate controls, and post-action verification. Measure correct diagnosis, evidence citation, safe tool choice, time saved, false action, and recovery—not conversational fluency.

### Scenario 3: Multimodal claims intake

Images/audio/text enter an asynchronous workflow. Validate file/type/size/malware/consent, transcribe/extract with lineage, classify sensitive data, and store protected originals/derived artifacts under retention policy. Route simple cases to a smaller model and complex cases to a capable multimodal model. Use a queue, idempotent state, human review for low confidence/high impact, and a governed CRM write. Evaluate extraction and business correctness by document/cohort, safety/privacy, tool/schema validity, throughput, backlog, tokens/cost, and deletion propagation.

---

## Practice labs

Use an AWS Builder Lab, organization-approved sandbox, or disposable personal training account. Avoid regulated/production data, set budgets, use least privilege, record resources, and remove billable resources. Model/service access and pricing are **VERIFY CURRENT**.

### Lab 1: Use-case and model decision record — 90–150 minutes

Define outcome, risk, data, latency, scale, availability and budget. Build 30–50 representative cases and compare two available models plus a deterministic baseline on quality, safety, latency, tokens/cost, and limits. Record the decision and fallback.

### Lab 2: Governed multimodal ingestion — 150–240 minutes

Process synthetic text plus image/audio inputs through validation, classification/redaction, transformation, lineage, error quarantine, deletion, and monitoring. Demonstrate malformed, sensitive, duplicate, and revoked-source cases.

### Lab 3: RAG retrieval experiment — 180–300 minutes

Build a small authorized corpus and versioned index. Compare two chunk strategies, embedding choice/dimension, metadata filters, keyword/vector/hybrid retrieval, and optional reranking. Measure retrieval and answer/citation quality, latency, tokens, deletion, and cross-tenant denial.

### Lab 4: Prompt lifecycle and regression — 120–180 minutes

Create a parameterized prompt with trusted/untrusted boundaries and structured output. Version it, test normal/adversarial/refusal/schema cases, canary a change, compare quality/safety/cost, and roll back on a defined threshold.

### Lab 5: Bounded tool-using agent — 180–300 minutes

Implement an agent with one read tool and one simulated write tool. Add typed validation, scoped identity, state, idempotency, step/time/token budget, human approval, injection defense, tracing, and a kill switch. Test duplicate, permission, timeout, malicious tool output, and partial failure.

### Lab 6: Streaming and asynchronous APIs — 150–240 minutes

Implement one streaming interaction and one SQS-backed asynchronous job. Handle authentication, quota, validation, cancellation, backpressure, partial output safety, correlation/status, retry/DLQ, idempotency, timeout, and trace propagation.

### Lab 7: Safety and privacy red team — 150–240 minutes

Create authorized synthetic tests for direct/indirect injection, jailbreak, encoded input, PII, cross-tenant retrieval, excessive agency, unsafe output, and log/cache leakage. Layer input, retrieval, model/guardrail, tool and output controls. Measure false positives/negatives and escalation.

### Lab 8: Continuous evaluation and operations — 180–300 minutes

Build an offline and sampled-online evaluation pipeline with versioned dataset/rubric, human-calibrated judge, retrieval/generation/agent/safety/operational/business metrics, release gate, dashboards, alerts, cost attribution, and rollback. Inject one prompt, retrieval, tool and quota fault and diagnose each.

---

## Knowledge checks

1. First GenAI architecture artifact? **A use-case, risk, data and evaluation contract—not a model choice.**
2. Why baseline deterministic logic? **It can meet some tasks more reliably/cheaply and shows whether GenAI adds value.**
3. Larger FM always better? **No; compare task quality, safety, latency, cost, availability and constraints.**
4. Model abstraction risk? **It can hide provider-specific capabilities, schemas, safety and behavior.**
5. RAG versus customization? **RAG supplies external context at inference; customization changes model behavior.**
6. Vector-store authority? **The original governed source remains authoritative; index entries are derived.**
7. Embedding model changed for new records only? **Vectors may be incompatible; version/rebuild or separate indexes deliberately.**
8. Universal best chunk size? **None; evaluate retrieval/end-to-end quality against document and use case.**
9. Metadata filtering sufficient tenancy? **No; combine identity/authorization, scoped retrieval, store controls and tests.**
10. RAG guarantees truth? **No; source quality, retrieval, context use and output validation can fail.**
11. Prompt is configuration only? **It is a versioned behavioral artifact needing tests, approval, release and rollback.**
12. Agent tool call is authorization? **No; deterministic code/IAM must authorize identity, action, resource and parameters.**
13. Essential agent stop controls? **Step, token, time, retry/cost limits plus explicit completion/escalation.**
14. MCP makes a tool trusted? **No; authenticate, authorize, validate, sandbox/allowlist and audit.**
15. Multi-agent default advantage? **No; use only when specialization benefit exceeds coordination risk/cost.**
16. Streaming main benefit? **Lower perceived time to first output; total work/cost may be unchanged.**
17. Safe write integration? **Typed validation, least privilege, state/preconditions, approval, idempotency and verification.**
18. FM retry every failure? **No; retry only retryable errors within time/cost/idempotency limits.**
19. GenAI gateway value? **Central policy, auth, quota, routing, safety, usage and observability when it does not erase needed capability.**
20. Prompt injection defense? **Treat untrusted content as data and enforce authority outside the model with layered controls.**
21. Guardrail enough? **No; combine authorization, retrieval isolation, deterministic checks, tool boundaries, monitoring and humans.**
22. Embeddings sensitive? **Yes; inherit source classification and access/lifecycle protections.**
23. Deletion scope? **Source, derived chunks/embeddings, caches, logs/feedback and retained copies per policy.**
24. Model card purpose? **Document intended use, limitations, evidence and risks; it is not a runtime control.**
25. Exposed chain-of-thought reliable explanation? **No; prefer evidence attribution, action audit and documented factors/limits.**
26. Cost metric better than token price? **Cost per successful safe business outcome.**
27. Semantic-cache hazard? **Stale, unsafe or cross-tenant answers if authorization/version/freshness are absent from the key.**
28. Optimize context by deletion alone? **No; preserve required evidence and measure quality/safety after pruning/compression.**
29. Fast vector query means good retrieval? **No; jointly measure relevance/recall, filters, freshness and answer quality.**
30. Observe an agent with what? **Request, versions, state, plan/steps, tools/arguments/results, safety, tokens/cost, outcome and approval.**
31. Average quality enough? **No; segment by risk, cohort, language, task, difficulty and adversarial cases.**
32. LLM judge is ground truth? **No; calibrate to humans with rubric, versioning, bias and disagreement analysis.**
33. Offline evaluation enough? **No; combine pre-release regression with safe canary/online monitoring and feedback.**
34. Retrieval failure versus generation failure? **Check whether correct authorized evidence was retrieved before changing the prompt/model.**
35. Context overflow response? **Detect and deliberately chunk/summarize/route; do not silently drop critical content.**
36. Output schema unreliable means? **Use constrained/structured generation where supported plus deterministic validation and retry/escalation.**
37. Agent task success metric? **Correct completed outcome and side effects, not merely a final message.**
38. Safe model update? **Versioned offline gates, compatibility checks, canary/shadow, monitoring and rollback.**
39. Hallucination monitor from production labels absent? **Use grounded/citation checks, sampled review, user correction and maintained golden sets; state limitations.**
40. Production GenAI proof? **Meets measured business, quality, safety, security, latency, reliability, and cost constraints over time.**
41. Why current AIP guide over beta material? **The standard March 2026 scope was refreshed for current services including AgentCore.**
42. Are advanced model training techniques central? **No; the target role integrates production GenAI, while advanced training is explicitly out of scope.**

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Choose one current AIP-C01 route, build the eight evidence labs, and use practice only for diagnosis. This fast-moving exam needs first-party documentation checks even when a course was updated recently.

| Resource | Access | Estimated time |
|---|---|---:|
| Official guide and AWS four-step plan | Public/free-account/subscription mix | 30–45 hours selected study |
| Production GenAI labs/evaluation | Sandbox or subscription | 45–80 hours |
| LinkedIn Learning AIP-C01 Cert Prep | Paid/trial | 30 hours 16 minutes plus labs |
| Tutorials Dojo video and practice route | Paid | 38–55 hours estimated |
| Udemy/Maarek-Kane current course | Paid | 25–45 hours estimated plus labs |
| Udemy/Rahul Trisal architecture route | Paid | 11 hours 22 minutes plus 20–35 hours labs |

- **Official route:** [AWS certification page](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/), [current five-domain guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html), and [AIP-C01 Skill Builder plan](https://skillbuilder.aws/category/exam-prep/generative-ai-developer-professional-AIP-C01) (**about 30–45 hours selected plus labs/evaluation**). The live page offers an official question set and pretest path; entitlements vary.
- **Current broad route:** [LinkedIn Learning / Tutorials Dojo AIP-C01 Cert Prep](https://www.linkedin.com/learning/aws-certified-generative-ai-developer-professional-aip-c01-cert-prep) (**30 hours 16 minutes**, advanced, released March 3, 2026; add current AgentCore/service checks).
- **Course/practice route:** [Tutorials Dojo AIP-C01 video course](https://portal.tutorialsdojo.com/courses/aws-certified-generative-ai-developer-professional-aip-c01-video-course/) (**27+ video hours, 10+ listed labs, 267 lessons and one 75-question test**) plus [practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-generative-ai-developer-professional-aip-c01-practice-exams/) (**about 10–18 hours across randomized, timed, review and domain modes**).
- **Current comprehensive course:** [Udemy/Frank Kane and Stéphane Maarek AIP-C01](https://www.udemy.com/course/ultimate-aws-certified-generative-ai-developer-professional/) (**25–45 hours estimated plus labs**; shown updated August 2026 with two 75-question tests, but stable runtime was not exposed in the review response).
- **Compact architecture/lab route:** [Udemy/Rahul Trisal AIP-C01](https://www.udemy.com/course/aws-certified-generative-ai-developer-professional-r/) (**11 hours 22 minutes**, 40+ listed labs and 60+ scenarios; updated July 2026). It is a focused supplement, not a substitute for professional AWS prerequisites.
- **Architecture reference:** [AWS Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) (**6–12 hours selected review/application**; November 2025 publication, verify current services).
- **Catalog boundary:** no exact current Pluralsight, O'Reilly, Whizlabs, or MeasureUp AIP-C01 product was independently verified on September 1, 2026. Recheck their live catalogs rather than substituting AIF-C01 or generic Bedrock content.

Suggested preparation: an experienced production GenAI developer may need **100–150 hours**; someone still building AWS/application prerequisites may need **180–280 hours** including them.

---

## Source map and freshness notes

The current root and five detailed domain pages define the standard assessment contract. The certification page defines live delivery; the [March 2026 update](https://aws.amazon.com/blogs/training-and-certification/march-2026-new-offerings/) establishes the standard-release refresh and AgentCore boundary; the [in-scope list](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/aip-01-in-scope-services.html) is non-exhaustive. Product documentation supports current behavior; learning vendors support only their catalog claims.

- **VERIFY CURRENT:** model IDs/capabilities/context/pricing, Bedrock APIs, AgentCore, Strands, Agent Squad, MCP features, Knowledge Bases/stores, evaluation, guardrails, Cross-Region Inference, prompt caching, regions and quotas.
- **VERIFY CURRENT:** service data-use/privacy terms, encryption/network integrations, model customization/deployment, tool/trace behavior, and training metadata before production use.
- **Stable system pattern:** outcome/risk contract → measured baseline → governed context/tools → layered controls → versioned delivery → multi-perspective evaluation → continuous observation/improvement.

This guide uses no recalled exam questions or restricted content. The knowledge checks are original and test published concepts rather than reproducing vendor items.
