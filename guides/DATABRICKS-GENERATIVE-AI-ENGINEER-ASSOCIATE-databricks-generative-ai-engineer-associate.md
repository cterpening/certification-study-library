---
exam_code: DATABRICKS-GENERATIVE-AI-ENGINEER-ASSOCIATE
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/genai-engineer-associate
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# Databricks Certified Generative AI Engineer Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-generative-ai-engineer-associate-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/genai-engineer-associate) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-GENERATIVE-AI-ENGINEER-ASSOCIATE`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official guide for the live version as of March 18, 2026; live six-domain weighted page checked September 1, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026. This blueprint already reflects the March 18, 2026 revision, but agent, MCP, evaluation, serving, AI Gateway, Agent Bricks, AI Search/Vector Search, and Apps interfaces are changing quickly. Verify current names and release stages before implementation.<br>
**Lifecycle status:** Active; valid for two years, with the currently live exam required for recertification.<br>
**Assessment:** 45 scored multiple-choice questions, 90 minutes, USD 200, English/Japanese/Brazilian Portuguese/Korean, online or test-center delivery. The March PDF describes multiple-choice or multiple-selection and online proctoring; the live page controls current public delivery metadata.<br>
**Prerequisite:** None required. The official guide recommends related training and six months of hands-on experience. Working Python, SQL, LLM/prompt basics, retrieval, APIs, testing, identity, Unity Catalog, MLflow, serving, and application operations are practical prerequisites.

## How to use this guide

Build one small, governed agent from source documents to production feedback. Retain the business requirement, prompt version, input/output schema, model and embedding selection evidence, source/chunk lineage, retrieval metrics, tool/MCP permissions, trace, evaluation dataset and scorers, registered application/model version, deployment identity, inference/usage records, human feedback, release gate, and rollback decision.

```text
business outcome + risk -> inputs/outputs -> model + prompt + tools
-> parse/filter/chunk -> governed Delta source -> embeddings + AI Search
-> retrieve/rerank -> agent/RAG response + guardrails -> MLflow trace
-> offline evaluation + SME calibration -> register + deploy + authenticate
-> production quality/latency/cost/safety monitoring -> improve or rollback
```

Application Development and Assembling/Deploying Applications total 52%. Do not study them as isolated APIs: most good decisions connect retrieval quality, model behavior, governance, deployment identity, evaluation evidence, cost, and operations.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes an objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Databricks' published exam objectives.

## Objective map

| Published domain | Weight | Evidence you should be able to produce |
|---|---:|---|
| Design Applications | 14% | Requirement-to-pipeline decomposition, structured prompt, model/task/chain choice, ordered tools, and Agent Bricks selection. |
| Data Preparation | 14% | Source-quality decision, extraction/filtering/chunking pipeline, governed Delta records, retrieval metrics, advanced chunking, and reranking. |
| Application Development | 30% | Framework/model/embedding selection, context-aware prompts, RAG/agent behavior, guardrails, experiments, MLflow Agent Framework, lifecycle reasoning, and Genie-enabled multi-agent design. |
| Assembling and Deploying Applications | 22% | Logged/registered chain, AI Search index, Foundation Model API/batch inference, persistent state, CI/CD, MCP, prompt lifecycle, application UI, and access control. |
| Governance | 8% | Input/output/data guardrails, masking, licensing/provenance, and problematic-content mitigation. |
| Evaluation and Monitoring | 12% | Evaluation design, traces/scorers/judges, inference and usage evidence, production monitoring, cost controls, and calibrated SME feedback. |

---

## 1. Design Applications (14%)

### Convert a business request into an evaluable contract

Start with the decision or user outcome, not a fashionable model. Define users, trusted knowledge, permitted actions, input and output schema, latency/cost target, quality and safety thresholds, freshness, identity boundary, escalation path, and evidence required for release. Decompose the system into deterministic preprocessing, retrieval, generation/reasoning, tools/actions, validation, presentation, and monitoring.

Choose the task that matches the output: summarization for a shorter faithful rendering, classification for a bounded label, extraction for structured fields, retrieval for grounded evidence, generation for open text, and tool/agent execution for external state or multi-step work. A larger general model is not automatically better than a smaller task-appropriate model under latency, cost, privacy, or formatting constraints.

Specify desired inputs and outputs precisely. A support assistant may accept authenticated user context, account ID, question, and conversation state, but return an answer, cited sources, confidence/abstention state, and trace ID. A pipeline description that omits identity or evaluation cannot be made safely production-ready later by adding a prompt sentence.

### Design prompts as versioned interfaces

A robust prompt separates role/instructions, trusted context, user content, constraints, and output schema. State what to do when evidence is missing or conflicting. For structured output, define fields, types, allowed values, null/error behavior, and a validator; an example can clarify format but should not become the only specification.

Treat user-supplied and retrieved text as untrusted data. Delimit it, avoid interpolating it into higher-priority instructions, restrict tools independently of prompt behavior, and validate output/action arguments. Iterate from a measured baseline: change one material component, use the same evaluation set, compare quality/safety/latency/cost, and version the decision.

### Choose chains, tools, agents, and Agent Bricks deliberately

A fixed chain is preferable when steps and allowed transitions are known. Use an agent when the model must choose among tools or adapt a plan; this increases nondeterminism and therefore evaluation, authorization, timeout, loop, and cost requirements. Define each tool with a narrow schema, least privilege, bounded side effects, idempotency where practical, error behavior, and auditable result.

Order tools from information gathering to decision to action. Separate read-only retrieval from state-changing tools and insert approval before high-impact actions. Limit tool count exposed per turn, terminate repeated calls, and handle partial failure instead of letting the model invent success.

The current [Databricks agents documentation](https://docs.databricks.com/aws/en/agents/) distinguishes guided Agent Bricks, custom agents, tools/MCP, Apps, evaluation, and serving. Use a Knowledge Assistant for a managed domain-grounded question-answer pattern, a Supervisor for coordination among specialized agents, and Information Extraction for a defined structured extraction job. Choose a custom agent when orchestration, framework, UI, tool policy, or evaluation needs exceed the managed pattern.

> **Related item:** Agentic architecture shifts correctness from one final string to a trajectory: routing, tool selection, arguments, observations, retries, and final response all need traceable evaluation.

---

## 2. Data Preparation (14%)

### Select and govern sources before tuning retrieval

List the knowledge necessary to answer the intended questions, its owner, authority, update cadence, license, sensitivity, language, format, and access policy. Prefer authoritative current sources over large indiscriminate corpora. A billing table can answer transaction-specific delivery facts better than a generic policy document; retrieval cannot recover information absent from the corpus.

Preserve source URI/object ID, version or modification time, extraction method/version, page/section coordinates, access labels, checksum, and ingestion time. Store parsed documents and chunks in governed Delta tables in Unity Catalog so reprocessing and deletion are reproducible. Apply permissions to source, chunk, index, endpoint, and trace/evaluation data rather than assuming one catalog grant covers every derivative.

### Extract, clean, and chunk according to structure

Choose extraction by source type: an HTML parser for markup, PDF/document library for digital documents, OCR such as Tesseract for scanned images, and format-aware loaders for tables or presentations. Validate encoding, page order, headings, tables, images, repeated headers/footers, OCR confidence, and empty/garbled output. Filter navigation, boilerplate, duplicate text, hidden content, and stale versions that reduce relevance.

Chunk size must fit the embedding input limit and leave the generation model enough context for instructions, query, history, retrieved passages, and response. Larger chunks preserve local context but reduce retrieval specificity and record count; smaller chunks improve precision but may fragment meaning and increase index size. Overlap protects boundary context but increases duplication, cost, and competing results.

Use semantic or heading-aware chunks for prose, parent-child retrieval for a precise match plus broader context, table-aware units for records, and metadata filters for tenant/product/date/language/security. Never split solely by a character count without measuring how it treats the actual document structures.

### Build and evaluate retrieval as its own system

Choose an embedding model based on language/domain fit, context length, dimension, quality, latency, cost, and deployment/governance constraints. The embedding input limit must accommodate chunks; a much larger dimension or model is not free accuracy. Changing the model normally requires re-embedding and a compatible index.

Create an AI Search index—called Mosaic AI Vector Search in the published exam guide—from a governed source, with correct primary key, embedding source, update mode, endpoint/index capacity, and permissions. Test filters and synchronization/freshness. Direct-vector indexes give the application more control over embeddings; Delta Sync patterns reduce pipeline ownership. Verify the current [generative AI platform capabilities](https://docs.databricks.com/aws/en/generative-ai/guide/gen-ai-capabilities) because naming and index options are volatile.

Build a labeled query set including direct facts, paraphrases, ambiguous queries, filters, rare entities, multi-hop needs, no-answer cases, and adversarial/noisy content. Measure recall@k/hit rate, precision, ranking quality such as MRR or NDCG where appropriate, latency, freshness, and downstream answer groundedness. Inspect failures by source, chunk type, language, query class, and permission boundary.

Hybrid lexical/vector retrieval helps exact identifiers and semantic paraphrases. Reranking spends additional latency/cost to reorder candidates with a stronger relevance signal. Use it when first-stage recall is acceptable but ordering is weak; it cannot retrieve a missing candidate. Tune chunking, metadata filters, query rewriting, k, hybrid settings, and reranking with the same evaluation set.

> **Related item:** Retrieval evaluation separates “the right evidence was not retrieved” from “the model ignored or misused good evidence.” Treating both as prompt failures wastes effort.

---

## 3. Application Development (30%)

### Select models and frameworks from constraints and evidence

Use model cards and provider metadata to screen context window, modalities, task strength, language, license, safety, region/data handling, throughput, price, and deprecation. Then test representative prompts. Compare quality and safety alongside p50/p95 latency, token use, concurrency, reliability, and total workflow cost. A benchmark winner may fail a domain, tool-call, structured-output, or governance requirement.

Select LangChain, LangGraph, the OpenAI Agents SDK, another framework, or plain Python based on needed control, ecosystem integrations, state/graph semantics, portability, observability, and team competence. Framework abstractions do not replace understanding messages, schemas, tool calls, retries, and provider limits. Wrap the agent in the supported MLflow interface when you need Databricks tracing/evaluation/deployment compatibility.

### Improve prompts and RAG behavior with controlled experiments

Augment a prompt only with context relevant to the authenticated user and current intent. Use structured metadata and application state to select tenant/product/language/history; do not place all profile data into every prompt. Preserve citations or chunk IDs so the answer can be checked against evidence.

When quality is poor, classify the failure before changing anything:

| Failure | Likely intervention |
|---|---|
| relevant source absent | acquire/fix/source or permission; do not tune prompt |
| relevant source present, chunk missing | extraction/chunking/index/filter/query/retrieval change |
| evidence retrieved but badly ranked | hybrid search, metadata or reranking |
| evidence present but answer ungrounded | prompt/context layout, model, refusal/citation validation |
| correct answer but wrong format | schema, structured output, validator/retry |
| unsafe input/action | layered guardrail and tool authorization |
| slow or costly path | smaller model, caching, routing, token/context/tool limits |

Use an evaluation baseline and change one component at a time. Keep prompt/model/retriever/tool/framework versions in MLflow traces and evaluation results. Qualitative review should identify patterns, but release decisions need repeatable rubrics and representative cases.

### Apply guardrails in layers

Input controls include size/type validation, authentication/authorization, injection detection, content classification, rate limits, and safe handling of untrusted documents. Retrieval controls include row/object permissions, metadata filtering, source allowlists, and output citations. Generation controls include system rules, structured schemas, blocked-content handling, grounding checks, and redaction. Tool controls include least privilege, parameter validation, allow/deny policy, timeouts, budgets, approvals, and audit. Output controls include schema validation, safety classifiers, masking, refusal/fallback, and human escalation.

Do not claim a single prompt “prevents hallucination” or an injection classifier secures tools. Security controls must remain effective if the model behaves incorrectly.

### Develop single- and multi-agent systems with observable state

Use the Agent Framework/MLflow-compatible response interface to capture spans for model calls, retrievers, tools, and routing. Define state ownership, maximum steps, retry policy, timeouts, error/fallback messages, token/cost budget, and deterministic termination. Store only required conversation or working memory and apply retention/access rules.

A multi-agent supervisor should route to specialists with distinct capabilities and permissions. A Genie Space/agent is a strong structured-data specialist when governed tables, semantic definitions, sample queries, and trusted assets support natural-language analytics. A retrieval specialist handles unstructured knowledge; an action agent may require approval. Measure routing and tool results, not just the final fluent synthesis.

Current interfaces are summarized in [Build agents on Databricks](https://docs.databricks.com/aws/en/agents/). Preserve the March blueprint wording when studying, but learn the current ResponsesAgent/Apps and AI Search direction rather than memorizing screenshots.

> **Related item:** Foundation-model adaptation, prompt optimization, RAG, tools, and fine-tuning solve different problems. Frequently changing factual knowledge belongs in governed retrieval or APIs, not model weights.

---

## 4. Assembling and Deploying Applications (22%)

### Package the whole inference contract

A simple chain still needs deterministic input parsing, prompt construction, model/retriever/tool calls, output validation, error/fallback behavior, and trace context. When packaging with MLflow/PyFunc or the current agent interface, retain dependencies, artifacts, input example, signature/schema, configuration references, and model/prompt/retriever versions. Load secrets and credentials through platform identity/secret mechanisms, never model artifacts or browser code.

Register the governed artifact/version in Unity Catalog and use a controlled alias or deployment reference. Test loading in a clean environment, missing/extra inputs, timeouts, partial tool/retrieval failures, hostile content, concurrency, and permissions. Registration proves lineage and discoverability; it does not prove the application is safe or high quality.

### Assemble RAG, AI Search, and inference paths

A RAG application needs source/chunk tables, embedding model, index and endpoint, retriever configuration, generation model/API, prompt, dependency environment, schemas, evaluation set, and identity. Create/query the index with an authenticated principal that has only required source/index privileges; test update lag, deleted records, filters, empty results, dimension/schema compatibility, and capacity.

Use Foundation Model APIs or supported serving for interactive calls. Use SQL `ai_query()` or a batch inference pattern when rows can be processed asynchronously and SQL/data-pipeline integration is useful. Do not turn a batch workload into millions of sequential REST calls. Verify current availability, supported models and return schema before relying on [AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions).

Select standard versus storage-optimized/current AI Search options from corpus scale, write/update frequency, latency/throughput, cost, hybrid/rerank needs, and feature availability. Benchmark with production-like volume and queries; vendor limits and names can change.

### Treat memory and persistent state as governed data

Conversation memory may include recent messages, a summary, user preferences, workflow checkpoints, or tool outputs. Separate ephemeral request state from persistent business facts. Use an appropriate database/table/checkpoint store with keys, optimistic concurrency/idempotency, retention, encryption, access control, deletion, and recovery. Never rely on an LLM to remember an action that must be transactionally correct.

### Build a release pipeline for components, prompts, and indexes

Version code, prompts, schemas, configuration, evaluation sets/scorers, and deployment resources. Use MLflow Prompt Registry/versioning or repository-managed prompts with an explicit dev→test→production promotion record and rollback. Test individual parsers, retrievers, tools, routing, schemas and guardrails; then run end-to-end evaluation and security/latency/cost gates.

Index changes require separate thinking: rebuild or sync in a candidate path, validate record counts/freshness/permissions and retrieval metrics, then switch without leaving the deployed agent incompatible. Promote a prompt or model only with its compatible schemas, tool definitions, dependencies, retriever/index, evaluation evidence, and configuration.

### Integrate MCP according to ownership and trust

Use Databricks-managed MCP servers for supported Databricks data/tools with minimal operational overhead, an external/MCP Service route for a third-party or hosted server with governed connection credentials, and a custom hosted server for proprietary tools you own. The current [MCP Services guidance](https://docs.databricks.com/aws/en/generative-ai/agent-framework/external-connection-tools) describes managed credentials, Unity Catalog permissions, tool restrictions/policies, audit, and usage logging; some features remain preview and must be rechecked.

Evaluate server trust, authentication, credential storage/rotation, exposed tool schemas, destructive operations, data egress, tenant/user identity propagation, timeout/retry, approval, rate/cost limits, audit, and failure isolation. A convenient MCP catalog entry is not permission to expose every tool to every agent.

### Choose a secure user-facing interface

Databricks Apps can host an authenticated chat or workflow UI and a backend that calls agents/models/tools without exposing long-lived tokens in the browser. Separate user identity from app/service identity and deliberately propagate/enforce user permissions where per-user results require them. For Slack, Teams, or another channel, validate identity mapping, tenant/install scope, message/data retention, secret management, interaction timeouts, links/citations, approvals, and safe error messages.

> **Related item:** Authentication answers “who is calling”; authorization answers “what may they access/do”; delegation answers “on whose behalf.” GenAI applications frequently need all three.

---

## 5. Governance (8%)

### Protect data and actions with controls outside the model

Apply Unity Catalog ownership, privileges, row filters, column masks, views, tags/lineage, and audit where applicable. Mask or tokenize sensitive values before they enter prompts when the model does not need the original; redact outputs and traces as an independent control. Test whether permissions remain correct through derived chunks, indexes, tools, serving endpoints, Apps, inference tables, evaluation sets, and exports.

Use guardrails matched to threat: injection and instruction-boundary controls, content moderation, PII/secrets detection, allow/deny topics, grounding/citation validation, schema constraints, tool policy, and human approval. Measure false positives and false negatives by user/task group. A guardrail that blocks all useful work meets neither quality nor performance goals.

### Preserve source provenance and usage rights

Record source owner, license/terms, permitted purpose, attribution, geography, retention/deletion, sensitivity, and whether content may be embedded, used in evaluation, sent to a model provider, or shown to a user. Licensing and privacy obligations survive chunking and embedding. Support source deletion through every derivative and prove it.

For problematic source text—unsafe, biased, obsolete, duplicated, low-quality, injected, or unlawfully collected—prefer correction, exclusion, quarantine, filtering/redaction, scoped replacement, and owner review. Fine-tuning or prompt wording does not legitimize an unsuitable corpus.

> **Related item:** Responsible AI is a lifecycle property with named owners, risk acceptance, evidence, incident handling, and user recourse—not a one-time content filter.

---

## 6. Evaluation and Monitoring (12%)

### Evaluate components and end-to-end behavior

Create representative evaluation records with request, context/identity class, expected behavior or reference when available, source evidence, risk category, and rubric. Evaluate retrieval separately, then response correctness/groundedness/relevance/completeness/style/safety, tool choice/arguments/result use, routing, latency, tokens, and cost. Slice by scenario, language, source, difficulty, risk, and failure type while protecting small/sensitive groups.

Some judges require ground truth/reference answers; others assess criteria such as relevance or guideline adherence without one. Validate automated judges against calibrated human ratings, track judge/model/prompt version, and use custom scorers for business rules. LLM judges are measurement instruments with bias and variance, not unquestionable ground truth.

Use MLflow tracing to inspect the trajectory and [agent evaluation and monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor) to reuse scorers from development in production where appropriate. Compare candidates on confidence intervals or sufficient sample sizes, regression sets, risk thresholds, latency, and cost—not a single average score.

### Monitor production quality, operations, safety, and cost

Inference/payload or trace records should connect timestamp, user/tenant class where allowed, application/model/prompt/index/tool versions, inputs/outputs under privacy rules, retrieved evidence, spans, tokens, latency, errors, feedback, and scorer results. Use inference tables/trace storage and usage/system tables according to current feature support and retention requirements.

Monitor:

- operational health: request volume, p50/p95 latency, errors, timeouts, tool/retrieval failure, capacity;
- quality: groundedness, relevance, task success, tool/routing correctness, abstention and citation validity;
- safety/governance: injection/policy flags, sensitive-data exposure, denied tool actions, permission anomalies;
- cost: input/output tokens, model/endpoint/index/tool consumption by app/tenant/version and rate-limit events;
- change: source freshness, index sync, distribution/query shifts, model/provider/prompt/tool changes;
- feedback: user signals, support incidents, and calibrated SME annotations.

AI Gateway can centralize endpoint governance such as usage tracking, payload/inference logging, rate limits and provider controls where supported. Budgets also require application-side routing, token/context/tool/step limits, caching where safe, batch choice, model selection, and alerts. Cost reduction that silently destroys groundedness is not optimization.

### Turn SME feedback into reliable evidence

Define observable rubric dimensions with anchors and examples, train/calibrate reviewers on a shared set, measure/reconcile disagreement, capture rationale, and periodically recalibrate. Do not simply average contradictory interpretations. Convert adjudicated high-value cases into versioned evaluation data, then use the same definitions for candidate comparison and production review.

Close the loop: issue → trace/failure classification → labeled/adjudicated case → component change → offline regression → staged release → production measurement. Retain who approved the change and rollback threshold.

> **Related item:** Offline evaluation estimates behavior on a curated distribution; online monitoring observes actual traffic. Dataset design, delayed feedback, sampling, and distribution shift determine how confidently one predicts the other.

---

## Integrated decision scenarios

### Scenario A — governed policy assistant

Ingest authoritative policy versions with owner/license/region/security metadata; parse headings/tables, remove navigation, create parent-child chunks, and build an identity-filtered AI Search index. Evaluate retrieval and cited answer groundedness with no-answer and obsolete-policy cases. Deploy an authenticated App, retain traces under privacy controls, monitor permission/citation/quality failures, and require owner approval before new content/index and prompt versions reach production.

### Scenario B — customer-support action agent

The agent retrieves product facts, queries account/order data, and can create a return. Give read tools and the return tool separate least-privilege identities/policies; validate account ownership and arguments outside the model and require user confirmation before the side effect. Trace routing/tool/results, cap loops/time/cost, persist transactional state in the system of record, evaluate injection and duplicate-action cases, and monitor tool denial/errors plus business outcomes.

### Scenario C — analytics supervisor

A supervisor routes policy questions to retrieval, governed metrics to a Genie specialist, and incident summaries to a generation specialist. Define each specialist's scope and permissions, pass only necessary context, reject unsupported cross-tenant requests, and provide sources. Evaluate route selection, structured/unstructured evidence synthesis, partial failure, latency/cost, and final groundedness; use calibrated analysts' feedback to refine routing and rubrics.

## Hands-on lab sequence

1. **Requirement and prompt contract:** Turn one business request into input/output schemas, task/model constraints, tool plan, prompt versions, refusal rules, and a 20-case baseline.
2. **Document pipeline:** Extract digital and scanned documents, clean boilerplate, preserve lineage, compare fixed/semantic/parent-child chunks, and prove delete/reprocess behavior.
3. **Retrieval experiment:** Create an AI Search/Vector Search index; evaluate filters, hybrid/vector retrieval, k, chunking and reranking with hit/precision/ranking/latency evidence.
4. **Agent and guardrails:** Build a traced RAG/tool agent with bounded steps, least-privilege read/action tools, schema validation, injection tests, approval, fallback, and cost limits.
5. **MLflow evaluation:** Create a versioned dataset, built-in/custom scorers and SME rubric; compare two prompt/model/retriever candidates and inspect failing traces.
6. **Lifecycle and MCP:** Version/promote a prompt, connect one managed or external MCP server under restricted tools/credentials, and test timeout, denial, audit, and rollback.
7. **Secure application:** Deploy an authenticated Databricks App or supported agent endpoint; test user/app identity, access, invalid input, concurrency, persistence, and token exposure.
8. **Production loop:** Configure trace/inference/usage monitoring and alerts across quality, safety, latency, errors and cost; collect feedback, create a regression case, stage a fix, and roll it back.

## Readiness checks

### Design and data

- [ ] I can translate a business goal into users, inputs/outputs, evidence, risk, latency, cost, identity and escalation requirements.
- [ ] I can select summarization, classification, extraction, retrieval, generation or tool execution from the desired outcome.
- [ ] I can design a structured prompt and validation/refusal behavior without trusting user/retrieved text as instructions.
- [ ] I can compare fixed chains, tool agents, managed Agent Bricks and custom/multi-agent systems.
- [ ] I can order tools, distinguish read from side effect, and define approval/termination/error behavior.
- [ ] I can choose sources by authority, completeness, freshness, license, sensitivity and user permissions.
- [ ] I can choose extraction tools for HTML, digital documents, scans/OCR and tables and validate their output.
- [ ] I can select chunk size/overlap/semantic/parent-child/table-aware strategies from document and model constraints.
- [ ] I can preserve source/chunk/index lineage and deletion through governed Delta/Unity Catalog assets.
- [ ] I can select an embedding model using context, quality, language, dimension, latency, cost and governance.
- [ ] I can evaluate retrieval with representative queries, hit/recall/precision/ranking, filters, latency and freshness.
- [ ] I can explain when hybrid retrieval and reranking help—and when missing candidates make them ineffective.

### Development and assembly

- [ ] I can select a model using model-card constraints plus representative quality/safety/latency/cost tests.
- [ ] I can justify framework versus plain-Python and fixed versus agentic orchestration choices.
- [ ] I can diagnose source, extraction, retrieval, ranking, prompt, model, format, safety and operations failures separately.
- [ ] I can version and compare prompt/model/retriever/tool changes against the same evaluation set.
- [ ] I can layer input, retrieval, model, tool and output guardrails outside prompt-only defenses.
- [ ] I can implement observable bounded agent state, retries, timeout, budget, fallback and termination.
- [ ] I can route between Genie/structured data, retrieval/unstructured knowledge and action specialists safely.
- [ ] I can package a chain/agent with dependencies, artifacts, schemas, examples, configuration and trace context.
- [ ] I can register a governed version and distinguish registry/prompt alias from runtime deployment state.
- [ ] I can create/query/synchronize an AI Search index and test permissions, deletes, filters, capacity and compatibility.
- [ ] I can choose interactive serving versus SQL/batch inference without row-wise endpoint misuse.
- [ ] I can design governed persistent memory with identity, concurrency, retention, deletion and recovery.
- [ ] I can promote compatible code, prompt, schema, tool, index, model, scorer and deployment versions through tested gates.
- [ ] I can choose managed, external/MCP Service or custom MCP and secure credentials, tools, data egress, audit and failure.
- [ ] I can design an authenticated App/channel without browser tokens and with explicit user/app/delegated authorization.

### Governance, evaluation, and operations

- [ ] I can apply privileges, filters/masks, lineage/audit and identity controls to every derived GenAI asset.
- [ ] I can preserve content provenance, license/purpose/retention and deletion rights through chunks, embeddings and traces.
- [ ] I can mitigate unsafe, biased, obsolete, injected, duplicate or unlawful source material appropriately.
- [ ] I can create a representative, sliced evaluation set for retrieval, answers, tools, routing, safety, latency and cost.
- [ ] I can select reference-dependent versus reference-free judges and validate automated scoring against people.
- [ ] I can build custom scorers and inspect traces rather than trusting one aggregate score.
- [ ] I can monitor operational, quality, safety, cost, freshness/change and feedback signals by deployed version.
- [ ] I can use inference/traces, usage evidence, rate limits and token/tool/model controls to investigate and govern cost.
- [ ] I can calibrate SMEs with anchored rubrics, reconcile disagreement and version adjudicated evaluation cases.
- [ ] I can run issue→trace→label→change→regression→stage→monitor→rollback as an auditable improvement loop.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Pick the resources that match your gaps and learning style; prioritize building and evaluating a working agent over passively watching every course. Durations are vendor totals where publicly visible or planning estimates checked September 1, 2026 and may change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page and March 18, 2026 guide](https://www.databricks.com/learn/certification/genai-engineer-associate) | Free | 2–3 hours to map all objectives and inspect vendor sample format; do not redistribute questions |
| [Databricks Academy](https://customer-academy.databricks.com/) — *Building Retrieval Agents*, *Building Single-Agent Applications*, *Generative AI Application Evaluation and Governance*, and *Deployment and Monitoring* | Free account/customer or partner entitlement varies | 18–35 hours with labs; catalog estimates and availability require sign-in |
| [Databricks agents and GenAI documentation](https://docs.databricks.com/aws/en/agents/) | Free | 12–20 hours selected hands-on across Agent Bricks/custom agents, AI Search, tools/MCP, Apps, evaluation and serving |
| Databricks workspace plus this guide's eight labs | Organizational; portions may work in Free Edition | 30–50 hours including failure, authorization, evaluation, monitoring and rollback experiments |
| [Databricks YouTube](https://www.youtube.com/@Databricks) | Free | 4–8 hours selected recent agent, MLflow, AI Search, Apps and governance sessions |
| [LinkedIn Learning: Learn Databricks GenAI](https://www.linkedin.com/learning/learn-databricks-genai) | Paid/trial | 1 hour 11 minutes video plus 1–3 hours practice; use for concepts and verify March 2026 product/objective alignment |
| [Udemy: Databricks Generative AI Engineer Associate — Olivier Auffret](https://www.udemy.com/course/databricks-certified-generative-ai-engineer-associate-lessons/) | Paid; hands-on course, updated August 2026 when checked | About 12–20 hours including labs; public page exposed section times but not a stable full total |
| [Udemy: Derar Alhussein certification preparation](https://www.udemy.com/course/databricks-certified-genai-engineer-associate/) | Paid; course and hands-on preparation, updated August 2026 when checked | 3 hours 45 minutes video plus 6–12 hours hands-on and review |
| [O'Reilly search: Databricks generative AI](https://www.oreilly.com/search/?q=Databricks%20generative%20AI) | Paid/trial | 6–16 hours selected recent chapters/events; map them to the March blueprint rather than assuming completeness |

Because this blueprint contains recently revised agent, Agent Bricks, MCP, Apps, AI Search/Vector Search, MLflow evaluation, AI Gateway and prompt-management topics, check the official page two weeks before the exam and revalidate documentation release stages. No exact current Pluralsight, Whizlabs or MeasureUp exam-aligned product was independently verified.
