---
exam_code: AI-103
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-30
---

# AI-103 Developing AI Apps and Agents on Azure Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official AI-103 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103) is authoritative.

**Current baseline:** Skills measured as of April 16, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 30, 2026.<br>
**Official source:** [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)

## How to use this guide

Start with the service-selection and lifecycle models, then build the labs. For each objective, be able to explain the decision, implement a small Python solution, observe its behavior, and troubleshoot one failure. Use the official blueprint as a coverage checklist; use this guide to connect its individual bullets into complete systems.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| Plan and manage an Azure AI solution | 25–30% | Which service, model, deployment, security, and operating model fits? |
| Implement generative AI and agentic solutions | 30–35% | How do generation, retrieval, tools, memory, orchestration, and evaluation work together? |
| Implement computer vision solutions | 10–15% | How should visual generation, understanding, accessibility, and safety be implemented? |
| Implement text analysis solutions | 10–15% | When should prompts, language tools, speech, or translation be used? |
| Implement information extraction solutions | 10–15% | How does heterogeneous content become grounded, searchable structure? |

The exam role is an Azure AI engineer who writes Python and collaborates across architecture, data science, DevOps, security, and business teams. Expect design and operational judgment in addition to API knowledge.

---

# 1. Build the platform mental model

An AI application is more than a model endpoint. Treat it as a pipeline with independently testable layers:

```text
user or system
   ↓
application and identity boundary
   ↓
orchestration: prompt, workflow, or agent
   ├── model deployment
   ├── tools and APIs
   ├── retrieval and knowledge
   ├── memory or conversation state
   └── safety and approval controls
   ↓
evaluation, tracing, monitoring, and feedback
```

Microsoft Foundry provides a unified environment for projects, models, agents, tools, evaluation, and observability. Azure services such as AI Search, Content Safety, Speech, Translator, and Content Understanding supply specialized capabilities. Your design should make each dependency and trust boundary explicit.

## Choose a capability before choosing a product

| Need | Likely capability | Selection questions |
|---|---|---|
| Generate or transform language/code | Generative model | Quality, latency, context, safety, cost, region, modality |
| Run a constrained local or high-volume task | Small language model | Is task-specific quality sufficient? Can lower latency/cost outweigh generality? |
| Interpret images, video, or audio with text | Multimodal model or specialized tool | Is open-ended reasoning or deterministic extraction needed? |
| Ground an answer in changing enterprise content | Retrieval plus generation | How are documents chunked, secured, updated, ranked, and cited? |
| Perform actions | Agent with tools/functions | What identity, input validation, approval, retry, and audit controls apply? |
| Extract repeatable document fields | Content Understanding or another extraction service | Are layout, OCR, tables, confidence, and custom schema important? |
| Search a knowledge corpus | Azure AI Search | Are lexical, semantic, vector, filtering, enrichment, or hybrid retrieval required? |

The best design can combine specialized tools with models. Do not send every problem to the largest model. A rules engine can enforce deterministic policy, Search can retrieve evidence, Content Understanding can normalize a document, and an LLM can synthesize the final response.

> **Related item:** A model router applies the same architectural principle as any policy-based router: classify the request, select an eligible backend, capture the decision, and provide a fallback. It can optimize cost and latency, but it also creates a new component to evaluate and monitor.

## Choose a model with evidence

Build an evaluation set representing normal, difficult, unsafe, and adversarial cases. Compare candidate models using:

- task quality and groundedness;
- safety and refusal behavior;
- modality and context-window needs;
- throughput, latency, quotas, and regional availability;
- token and infrastructure cost;
- operational features and deployment constraints.

Benchmark the deployed configuration, not an abstract model name. Prompts, retrieval, tools, safety settings, and model version all affect the outcome.

**VERIFY CURRENT:** Model names, versions, regions, quotas, retirement dates, pricing, and deployment types change frequently. Check the model catalog and service documentation when studying and before implementation.

---

# 2. Set up, deploy, secure, and operate Foundry solutions

## Design the Azure infrastructure

Separate concerns even if a small lab uses one resource group:

| Concern | Design decisions |
|---|---|
| Resource organization | Subscription, resource groups, naming, tags, ownership, policy |
| Environments | Development, test, staging, production, promotion boundary |
| Identity | User/developer roles, workload managed identities, service principals, least privilege |
| Network | Public access, private endpoints, managed virtual network, DNS, egress dependencies |
| Secrets | Keyless access where supported, vault use where secrets remain, rotation |
| Data | Storage/search region, encryption, retention, data classification, residency |
| Reliability | Regional dependencies, retry and timeout policy, capacity, degradation plan |
| Observability | Traces, application metrics, evaluation results, safety events, cost data |

Prefer managed identity and role-based access over embedded API keys. A managed identity removes credential distribution, but it does not automatically grant the right access; assign the minimum data-plane and control-plane roles required. Test access using the workload identity, not only an administrator account.

### Network troubleshooting order

When a private solution fails, check:

1. the caller's identity and token audience;
2. role assignments at the effective scope;
3. endpoint and public-network configuration;
4. private endpoint approval and DNS resolution;
5. managed-network outbound rules and dependent services;
6. application timeout, retry, and SDK configuration.

Do not diagnose an authorization failure as a network failure merely because both can surface as a failed request.

> **Related item:** Zero Trust is useful here as an operating model: verify explicitly, grant least privilege, and assume breach. Private networking reduces exposure; it does not replace workload authentication, authorization, validation, logging, or data governance.

## Treat deployments as versioned configuration

A deployment binds an application-facing name to a model/version and capacity configuration. Keep application code insulated from unnecessary provider details, and record the exact evaluated version. Promotion should include:

- infrastructure-as-code validation;
- application and prompt changes under version control;
- repeatable deployment configuration;
- offline evaluation and security tests;
- a small live or shadow test where appropriate;
- an approval and rollback decision;
- post-deployment monitoring.

Prompts, tool schemas, search index definitions, evaluation datasets, safety thresholds, and agent instructions are release artifacts. A code-only pipeline misses much of the system.

> **Related item:** Evaluation gates are the AI equivalent of regression tests, but statistical behavior requires thresholds and distributions rather than one exact expected string. Preserve representative datasets and inspect failures instead of optimizing only a composite score.

## Manage quota, scale, rate limits, and cost

Distinguish these signals:

| Signal | Meaning | Common response |
|---|---|---|
| Rate-limit response | Request or token rate exceeded | Backoff with jitter, reduce concurrency, request capacity, route eligible traffic |
| High latency without throttling | Slow model/tool/retrieval path | Break down trace spans; optimize the slow stage |
| Token growth | Larger prompts, retrieval, history, or output | Trim context, improve retrieval, summarize state, set output limits |
| Search indexing lag | New content not yet retrievable | Inspect data source/indexer status and freshness objective |
| Agent loop growth | Tool errors or weak termination conditions | Add budgets, state checks, bounded retries, and escalation |

Track cost per successful business outcome, not only total tokens. A cheaper call that causes more retries or poor decisions may raise total cost.

## Observe the entire system

A useful trace correlates the request across application, retrieval, model, tool, and response stages. Capture inputs safely, selected model/deployment, retrieved document identifiers, latency breakdown, token use, tool decisions, safety results, and outcome feedback. Apply privacy, retention, access, and redaction controls to telemetry.

Monitor four different things:

- **service health:** errors, throttling, latency, capacity;
- **data and retrieval health:** ingestion freshness, indexing errors, coverage, relevance;
- **model/application quality:** groundedness, task success, fabrications, drift;
- **safety and governance:** harmful content, prompt attacks, prohibited tool use, approval and audit evidence.

> **Related item:** Observability and privacy can conflict. More captured context makes debugging easier but increases sensitive-data exposure. Decide what to log, hash, redact, sample, restrict, and retain before production.

---

# 3. Responsible AI is a lifecycle control

Responsible AI is not one content filter after generation. Apply controls at design, input, retrieval, tool execution, output, deployment, and monitoring stages.

## Threat and control map

| Risk | Example | Controls |
|---|---|---|
| Harmful input/output | Hate, violence, sexual, self-harm content | Classification, thresholds, block/transform/escalate policy |
| Direct prompt attack | User asks agent to ignore policy | Prompt Shields, instruction hierarchy, scope constraints, monitoring |
| Indirect prompt injection | Retrieved page or image contains malicious instructions | Treat content as data, isolate instructions, restrict tools, validate outputs |
| Fabrication | Unsupported answer appears confident | Grounding, citations, groundedness evaluation, abstention, human review |
| Excessive agency | Agent performs irreversible action | Least-privilege tools, preview, limits, approval, idempotency, audit |
| Sensitive-data leakage | Model or trace returns restricted data | Access-aware retrieval, minimization, DLP, redaction, output checks |
| Bias or quality disparity | Performance differs by group or scenario | Representative evaluation, slice analysis, review, mitigation |

Configure Content Safety and guardrails according to the use case and organizational policy. Understand false positives and false negatives. Record exceptions with an owner, rationale, scope, expiry, and compensating control.

### Human oversight modes

Use escalating autonomy:

1. **Suggest:** agent drafts; human performs the action.
2. **Confirm:** agent prepares an action; human approves the exact parameters.
3. **Act within bounds:** agent acts only within defined low-risk limits.
4. **Escalate:** uncertainty, risk, policy match, or repeated failure sends work to a person.

The action's reversibility, financial or safety impact, data sensitivity, confidence, and legal obligation determine the oversight mode—not the model's fluency.

> **Related item:** Model risk management treats each deployed configuration as a governed system with an owner, intended use, validation evidence, limitations, change control, monitoring, and retirement plan. This complements, rather than replaces, technical safety filters.

---

# 4. Build generative applications and retrieval-augmented generation

## Control generation deliberately

Prompts should state the role, task, trusted context, output contract, constraints, and failure behavior. Prefer structured output with schema validation when software consumes the response.

Common parameters affect behavior but do not guarantee truth:

- **temperature/top-p:** alter sampling diversity; change one strategy deliberately rather than randomly tuning both;
- **maximum output tokens:** bounds response length and cost but can truncate a result;
- **stop conditions:** end generation at known delimiters where supported;
- **tool choice:** can constrain, require, or allow a model to select tools.

Validate structured output, enforce application constraints, and retry only failures likely to be transient. Repeating the same unsafe or structurally invalid request without changing anything is not a recovery strategy.

## Understand the RAG pipeline

```text
source → parse/OCR → normalize → chunk → enrich → embed/index
                                              ↓
question → query rewrite → retrieve/filter → rank → prompt → answer/citations
                                              ↓
                                      evaluate and improve
```

Each stage has a distinct failure mode:

| Symptom | Likely layer to inspect |
|---|---|
| New document never appears | Data source, indexer, parsing, indexing status |
| Correct document ranks low | Query, fields, filters, vectorization, hybrid search, semantic ranker |
| Good chunk retrieved but answer wrong | Prompt, context ordering, model behavior, output constraints |
| User sees unauthorized evidence | Retrieval security filter and identity propagation |
| Citations do not support answer | Chunk metadata, citation mapping, groundedness logic |

**Lexical search** matches terms and is strong for exact identifiers. **Vector search** retrieves semantic similarity. **Hybrid search** combines text and vector queries. **Semantic ranking** reranks an initial result set for relevance. They are complementary, not interchangeable synonyms.

Chunking should preserve meaning and useful metadata. Oversized chunks dilute retrieval and consume context; undersized chunks lose relationships. Test chunk size, overlap, document structure, metadata filtering, and top-k choices against real questions.

> **Related item:** Permission-aware RAG requires document authorization at retrieval time. Hiding an unauthorized citation in the final UI does not undo disclosure if the document already entered the model context.

## Evaluate the application, not only the model

Use an evaluation dataset with question, expected traits or evidence, scenario tags, and unacceptable outcomes. Measure retrieval relevance, groundedness, task completion, response quality, safety, latency, and cost. Review disagreement and failure slices manually.

Avoid leaking a fixed evaluation set into prompt tuning until the system overfits it. Maintain held-out or newly sampled cases and monitor live feedback with privacy controls.

---

# 5. Build and operate agents

An agent adds state, tools, and decisions around a model. Define:

- role and bounded goal;
- trusted instructions and prohibited behavior;
- conversation-state and memory policy;
- available tools and JSON schemas;
- authentication and authorization per tool;
- budgets for time, turns, tokens, and tool calls;
- approval and escalation conditions;
- termination and failure behavior;
- telemetry and evaluation criteria.

## Design tools as security-sensitive APIs

Use precise names, descriptions, types, allowed values, and validation. The application—not the language model—must enforce authorization and business rules. Avoid a general-purpose tool when several narrower operations express policy more safely.

For a side-effecting call:

1. validate and normalize arguments;
2. authenticate as the correct workload or user;
3. authorize the requested resource and action;
4. show a preview or request approval when required;
5. use an idempotency key where possible;
6. execute with timeout and bounded retry;
7. return a structured success or error result;
8. record an audit-safe trace.

## Separate conversation state, memory, and knowledge

| Mechanism | Purpose | Risk |
|---|---|---|
| Current conversation | Immediate multi-turn continuity | Context growth and sensitive content |
| Summarized state | Compact durable facts for the active task | Summary errors become future assumptions |
| User memory | Reusable preference or fact across sessions | Consent, accuracy, deletion, access scope |
| Knowledge retrieval | External evidence selected for a request | Freshness, authorization, injection |

Do not treat every conversation detail as durable memory. Define what is stored, why, for how long, how users correct it, and which agents can access it.

## Multi-agent orchestration

Use multiple agents when bounded specialization, independent security boundaries, or parallel work creates clear value. Define the orchestrator's routing, handoff contract, shared state, timeout, retry, and conflict resolution. More agents create more latency, cost, nondeterminism, and failure paths.

Common patterns include supervisor-and-workers, sequential handoff, and event-driven collaboration. Evaluate the full workflow and each component. A final correct answer can conceal repeated waste; a component score alone can miss a broken handoff.

> **Related item:** Distributed-systems practices apply to agents: correlation IDs, deadlines, idempotency, circuit breakers, compensation, bounded retries, and explicit state transitions are often more valuable than another prompt paragraph.

### Diagnose an agent failure by phase

| Phase | Questions |
|---|---|
| Perception/context | Did it receive the right user input, state, and authorized knowledge? |
| Planning/routing | Did it select the correct tool, agent, or workflow? |
| Invocation | Were arguments valid and identity/permissions correct? |
| Execution | Did the external system succeed, time out, or partially act? |
| Interpretation | Did the agent correctly use the tool result? |
| Termination | Did it stop, escalate, or loop? |

---

# 6. Implement computer vision and multimodal workflows

## Generation and editing

Image and video workflows need a prompt/reference input, selected generation controls, output storage, content policy, provenance, and human review appropriate to the use case. Inpainting changes a masked region while preserving the rest; prompt-driven edits may transform broader properties. Video adds temporal consistency and far greater processing/storage cost.

Use reference media only when its rights and consent allow the intended transformation. Validate format, dimensions, size, duration, and output constraints. Preserve original and generated asset identifiers when audit or rollback matters.

## Visual understanding

Multimodal models can caption, compare, answer questions, and reason over visual evidence. Content Understanding can produce structured or Markdown representations from multimodal inputs. Choose based on output contract:

- open-ended explanation or question answering → multimodal generation;
- repeatable fields, regions, layout, or downstream schema → extraction/analyzer pipeline;
- searchable corpus → normalized representation plus Search indexing.

An accessible alt-text workflow should describe information needed for the page's purpose, not inventory every pixel. Decorative images may need empty alternative text; complex diagrams may need a concise label plus a longer description. Include human review for consequential content.

> **Related item:** Accessibility is a product requirement, not simply a captioning feature. Context determines useful alternative text, and generated descriptions still require testing with the interface and assistive-technology workflow.

## Multimodal safety

Inspect both the media and embedded text. An image can contain harmful content, private information, disallowed branding, or text that attempts indirect prompt injection. Keep untrusted visual content subordinate to system instructions and restrict any tools reachable from the analysis flow.

---

# 7. Implement text, speech, and translation solutions

Use generative prompting for flexible extraction, summarization, classification, and structured JSON when the task benefits from contextual reasoning. Use specialized language tools when their capability, predictability, latency, or supported domain is a better fit.

## Text analysis controls

- Define the output schema and allowed labels.
- Include edge cases, negation, multiple languages, and long inputs in evaluation.
- Separate sentiment from intent, tone, safety, and business risk.
- Preserve source spans or citations when reviewers need evidence.
- Treat confidence as one signal, not proof.
- Protect sensitive text in prompts, logs, and evaluation datasets.

For translation, decide whether fidelity, terminology control, conversational fluency, document layout, or streaming speed matters most. Evaluate names, numbers, negation, domain terms, and low-resource languages—not only natural-sounding prose.

## Speech pipeline

```text
audio → speech recognition → language/agent processing → text-to-speech
```

Streaming voice agents also need turn detection, interruption handling, latency budgets, noise testing, transcript protection, and clear disclosure. Custom speech can improve domain recognition but introduces dataset, evaluation, deployment, and lifecycle responsibilities.

> **Related item:** Voice interfaces add a real-time state machine. Barge-in, silence, partial transcripts, retries, and channel failure need explicit behavior even when the language model is working correctly.

---

# 8. Implement information extraction and search

Information extraction converts unstructured or multimodal sources into reliable representations for people, systems, retrieval, and agents.

## Ingestion design

For each source, define:

1. connector and authentication;
2. supported formats and maximum sizes;
3. change/deletion detection and freshness target;
4. OCR, layout, transcription, or video segmentation;
5. enrichment and normalization;
6. chunk and document schema;
7. permissions and metadata filters;
8. failure queue, retry, and reconciliation;
9. quality and coverage checks;
10. retention and source lineage.

Built-in and custom enrichment skills can extract or transform content before indexing. Content Understanding analyzers can produce fields or Markdown suited to downstream reasoning. Preserve page, region, timestamp, source URI, and version metadata when citations or auditability depend on them.

### OCR is a stage, not the finished answer

OCR recognizes text. Layout analysis adds spatial and structural relationships. Field extraction maps evidence to a schema. A multimodal reasoning stage can interpret relationships, but it should not erase the underlying evidence or confidence.

> **Related item:** Data contracts stabilize AI pipelines. Version the normalized schema and downstream expectations so an analyzer or index change does not silently break retrieval, agents, or business automation.

## Search relevance loop

Create a labeled query set, record expected documents, run retrieval, inspect false positives and misses, adjust query/index/chunk/ranking choices, and retest. Measure freshness and security separately from relevance. A highly relevant stale or unauthorized result is still a failure.

---

# 9. Implementation and operational playbook

## Create a deployment manifest

Treat the evaluated AI configuration as a releaseable bundle. A deployment manifest can record:

```yaml
application_version: 2.3.0
model:
  deployment_name: support-router-prod
  model_version: VERIFY-CURRENT
  deployment_type: VERIFY-CURRENT
prompt_bundle: prompts/2.3.0
tool_schema_bundle: tools/1.8.0
search:
  index_schema: support-v5
  embedding_deployment: support-embed-v2
safety_policy: safety/3.1.0
evaluation_set: evals/release-2026-08
release_thresholds:
  groundedness: organization-defined
  task_success: organization-defined
  critical_safety_failures: 0
```

The example deliberately avoids a real model name or threshold: those values must come from the current catalog and the application's evidence. Store hashes or immutable artifact references when possible. Record region, capacity/quota dependency, connected resources, and identity assignments outside the file if the deployment system owns them.

A safe CI/CD flow is:

```text
lint/unit tests
  → infrastructure validation
  → deploy isolated candidate
  → smoke test connectivity and identity
  → offline quality/safety evaluation
  → scan dependencies/configuration
  → approval
  → canary or controlled promotion
  → live monitoring and rollback decision
```

Do not reuse production secrets or private evaluation data in an untrusted pull-request workflow. Use workload federation/managed identities and environment approvals. Make rollback cover prompts, tools, index schemas, guardrails, and agent configuration—not only application code.

> **Related item:** Database and search-index changes have compatibility windows. Use additive schema changes or dual-read/dual-write migration where necessary so the application can roll back without depending on a now-incompatible index.

## Design the Python application boundary

Foundry SDK surfaces change, so isolate provider-specific code behind an adapter. The durable application contract is more important than memorizing a preview method name.

```python
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class GenerationRequest:
    task: str
    evidence: tuple[str, ...]
    correlation_id: str

@dataclass(frozen=True)
class GenerationResult:
    answer: str
    citations: tuple[str, ...]
    deployment: str

class Generator(Protocol):
    def generate(self, request: GenerationRequest) -> GenerationResult: ...
```

The concrete Foundry adapter should use the current documented credential and client, specify a timeout, target a configuration-supplied deployment name, validate structured output, translate provider errors into application error categories, and emit trace spans. The business layer should not handle raw credentials or assume every HTTP error is retryable.

Use `DefaultAzureCredential` carefully: its credential chain is convenient across local and hosted environments, but production should have a predictable managed identity/workload identity and explicit role assignments. Test using that identity. A developer's broad Azure login can conceal missing production access.

### Error taxonomy

| Error | Retry? | Response |
|---|---|---|
| Authentication/authorization | No automatic blind retry | Verify identity, token audience, role, and scope |
| Invalid request/schema | No | Correct request or handle unsupported input |
| Rate limit | Yes, bounded | Respect retry guidance, back off with jitter, control concurrency |
| Transient service/network | Yes, bounded | Retry idempotent work; apply deadline/circuit breaker |
| Safety policy block | No identical retry | Follow product policy: explain, transform safely, or escalate |
| Tool side effect timed out | Not until outcome known | Reconcile by idempotency key/status before retry |

## Engineer a retrieval index

A useful chunk schema commonly needs more than text and an embedding:

| Field | Purpose |
|---|---|
| `chunk_id` | Stable citation and update identity |
| `document_id` | Groups chunks and supports deletion/reconciliation |
| `content` | Searchable/retrievable text or normalized representation |
| `content_vector` | Vector representation when vector search is used |
| `title`, `heading`, `page`, `region` | Human-verifiable citation context |
| `source_uri`, `source_version` | Provenance and freshness |
| `allowed_principals` or security filter key | Retrieval-time authorization |
| `language`, `content_type`, business metadata | Filtering and ranking features |
| `updated_at` | Freshness measurement |

Do not place a large unrestricted principals list on every chunk without evaluating index limits and authorization design. Options include group-based filters, security-trimmed indexes, query-time filters, or separate indexes for hard boundaries. The application must construct security filters from trusted identity claims, never from a user-supplied principal string.

### Retrieval experiment matrix

Run the same labeled queries through:

1. lexical search only;
2. vector search only;
3. hybrid search;
4. hybrid plus semantic ranking where eligible;
5. the chosen method with metadata/security filters and query rewrite.

Measure recall at a chosen cutoff, ranking quality, no-result behavior, latency, and authorized coverage. Then judge generated groundedness separately. A retrieval system can find the correct document while generation misuses it; a fluent model cannot repair evidence it never received.

> **Related item:** Reciprocal rank fusion is used by Azure AI Search to merge independently ranked result lists in hybrid search. You need the mental model—fusion combines signals—not a hand-calculated constant. See the current [hybrid search overview](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview).

## Build a stateful agent as a state machine

Make the orchestration state explicit:

```text
RECEIVED
  → CONTEXT_READY
  → PLAN_OR_ROUTE
  → TOOL_PENDING
      ↘ APPROVAL_REQUIRED → APPROVED or DENIED
  → TOOL_RESULT
  → RESPOND | ESCALATE | FAILED | CANCELLED
```

Persist only what is needed to recover the workflow. A state record can include conversation/thread identifier, current step, attempt count, deadline, tool request hash, idempotency key, approval identity/time, last safe result, and trace correlation. Do not store hidden model reasoning as an application requirement. Store decisions, tool inputs/outputs, evidence, and concise explanations that are appropriate for audit and troubleshooting.

### Tool contract example

```json
{
  "name": "create_support_case",
  "description": "Create a low-severity support case after explicit user confirmation.",
  "input": {
    "summary": "string, 10-500 characters",
    "category": "one of the approved categories",
    "user_confirmation_id": "server-issued identifier"
  },
  "server_controls": [
    "authenticate caller",
    "authorize tenant and action",
    "validate confirmation",
    "enforce severity limit",
    "deduplicate idempotency key",
    "write audit record"
  ]
}
```

The `server_controls` are documentation; the API implementation must enforce them. Returning an error in a structured, model-readable form helps the agent decide whether to correct input, ask the user, or stop.

## Orchestrate multiple models, agents, and rules

| Pattern | Use when | Main risk/control |
|---|---|---|
| Model router | Tasks differ enough to justify eligible models | Misrouting; evaluate routing and fallback |
| Rules then model | Policy can reject/shape work deterministically | Rule drift; version and test the policy |
| Model then validator | Flexible generation must meet a strict contract | Validator gaps; fail closed for critical invariants |
| Supervisor and workers | Bounded specialists need coordinated work | Cost/loops/conflict; budgets and typed handoffs |
| Sequential handoff | Stages have clear ownership and output contracts | Error propagation; validate each boundary |
| Parallel candidates/judging | Independent proposals improve selected quality | Cost and correlated failure; use evidence-based selection |

Multi-agent is not automatically more agentic or more accurate. Use it when separate tools, security boundaries, expertise, or parallelism create measurable value. Keep authorization at each tool/resource and do not assume the orchestrator's trust transfers to every worker.

## Evaluate reflection and self-critique safely

The blueprint includes reflection, self-critique, and chain-of-thought evaluation concepts. Implement them as observable quality-control stages—for example, require a verifier to check citations, a schema validator to reject invalid output, or a separate model/configuration to score an answer against a rubric. Do not require storage or disclosure of private hidden reasoning. Evaluate the final decision, evidence, tool path, explanation, and outcome.

A critique loop needs a maximum iteration count and a stopping rule. Otherwise it can increase latency and cost without improving quality. Compare:

- first-pass outcome;
- outcome after critique/revision;
- additional tokens and latency;
- failure categories improved or introduced;
- whether the evaluator shares the same blind spots as the generator.

> **Related item:** An LLM evaluator is itself a model with variance and bias. Calibrate it against human judgments, use explicit rubrics, and inspect disagreement rather than treating its score as ground truth.

## Create evaluation gates and production feedback

Use multiple slices rather than one aggregate:

| Slice | Example gate |
|---|---|
| Core task | Minimum task-success rate with confidence interval/review |
| Grounding | Citations support claims; critical unsupported claims fail |
| Safety | Zero allowed critical prohibited-action cases |
| Authorization | No restricted item appears for unauthorized test identities |
| Tool behavior | Correct tool/arguments and no duplicate side effects |
| Operations | P95 latency/cost within the product budget |
| Accessibility/language | Required scenarios meet defined rubric |

Production feedback should connect a rating or incident to the configuration version and trace without collecting unnecessary personal data. Sampling for evaluation needs notice, access controls, redaction, retention, and a process for correcting mislabeled cases.

## Implement multimodal and Content Understanding modes

For image/video generation and editing, keep the original input, mask/reference identifiers, prompt/configuration, safety result, output identifier, and human decision when provenance matters. Inpainting constrains change to a masked region; prompt-driven editing may change broader content. Video editing adds frame/temporal consistency and processing-time failure paths. **VERIFY CURRENT:** eligible models and exact editing APIs.

Content Understanding single-task and pro-mode concepts should be selected using complexity and desired orchestration from the current product documentation. Regardless of mode, define analyzer/schema version, input media constraints, asynchronous operation handling, fields or Markdown output, evidence regions/timestamps, confidence/review policy, and cost/latency limits.

For video:

1. validate duration, codec, rights, and safety;
2. segment or use the supported analyzer path;
3. preserve timestamps and detected regions/components;
4. evaluate events across segment boundaries;
5. return evidence-linked results;
6. test missing audio, cuts, overlays, and embedded text attacks.

> **Related item:** Provenance metadata helps a reviewer trace generated or extracted content, but watermarking and metadata can be removed. Use layered disclosure, access, audit, and policy rather than treating one provenance signal as tamper-proof.

## Operate speech as a latency budget

Break end-to-end voice delay into endpointing/turn detection, speech recognition, orchestration/retrieval/tools, generation, and synthesis. Stream partial output where appropriate, but do not speak an unvalidated consequential action as if it completed.

Test accents, languages, code switching, domain vocabulary, background noise, interruption, silence, dropped connections, repeated partial transcripts, and accessibility alternatives. Protect raw audio and transcripts according to their sensitivity. Custom speech introduces training-data rights, deployment versioning, and regression evaluation.

---

# 10. Production architecture and incident drills

## Draw trust boundaries before selecting controls

An AI application crosses more boundaries than the model endpoint. Start with a data-flow diagram:

```text
user/channel
  -> application/API
  -> orchestration or agent
     -> model deployment
     -> search/knowledge
     -> tools and business systems
  -> response

telemetry/evaluation <- every stage
deployment pipeline  -> application, prompts, indexes, agents, policies
```

For every arrow, record the calling identity, authentication method, authorization scope, network path, data classification, logging behavior, timeout, retry rule, and failure owner. This turns “secure the AI” into concrete boundaries.

| Boundary | Minimum design questions |
|---|---|
| User to application | How is the user authenticated, authorized, rate-limited, and separated from other tenants? |
| Application to Foundry/model | Can managed identity or another keyless credential replace a stored key? Which deployment and actions are permitted? |
| Agent to tool | Is the tool allow-listed, schema-validated, least-privileged, idempotent where needed, and approval-gated for high impact? |
| Retrieval to content | Is the user's content entitlement enforced before evidence reaches the model? Can retrieved text contain indirect instructions? |
| Service to telemetry | Which prompt, response, document, identity, or tool fields are sensitive? Who can query or export them? |
| CI/CD to production | Which identity deploys, which immutable artifacts/configurations are promoted, and which evaluations block release? |

Private networking changes reachability; it does not grant data-plane authorization. Managed identity removes application-held credentials; it does not choose least-privilege roles automatically. Content filters detect supported risk categories; they do not validate business authorization or guarantee factual answers. Use controls in combination and verify current Foundry networking constraints in [Microsoft's network-isolation guidance](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link).

### Security review scenario

A private RAG application returns a confidential document to an authenticated employee. Work backward:

1. Preserve the request, trace, retrieved document identifiers, filter expression, user/tenant claims, index version, and deployment version under incident controls.
2. Determine whether the source ACL was wrong, ingestion omitted it, the index did not store it, the query failed to filter, caching crossed identity boundaries, or the tool used an overprivileged service identity.
3. Contain at the narrowest reliable point—for example, disable the affected index/route or block the faulty retrieval version—without deleting evidence.
4. Correct the entitlement path and add a regression case for an allowed and denied user.
5. Reindex or invalidate caches if derived content carries the faulty access state.
6. Review logs, downstream outputs, notifications, and required response obligations.

Prompt wording cannot repair missing authorization. The model must receive only evidence the caller is permitted to use.

> **Related item:** Security trimming is end-to-end data lineage. An access label must survive source ingestion, transformation, chunking, indexing, filtering, citations, caches, and deletion. A break at any stage can become disclosure.

## Debug RAG by separating its quality stages

When an answer is weak, score the stages rather than immediately changing the model:

| Failure class | Evidence to inspect | Likely experiment |
|---|---|---|
| Source coverage | Is the authoritative answer present and current in the corpus? | Add or repair the source, owner, or freshness process |
| Extraction | Did OCR, layout, or transcription preserve the relevant content? | Compare the raw source with structured extraction |
| Chunking | Is the needed evidence split, merged, or stripped of context? | Change chunk boundary, overlap, and metadata strategy |
| Indexing | Are text, vectors, filters, and semantic fields populated with the expected version? | Validate sample documents and rebuild a test index |
| Query transformation | Did rewriting preserve names, dates, codes, exclusions, and intent? | Evaluate the original versus rewritten query |
| Retrieval | Does the relevant chunk appear in candidate results? | Compare keyword, vector, and hybrid retrieval and tune top-k |
| Reranking/filtering | Was good evidence removed by a filter or ranked too low? | Inspect the filter and pre/post-rerank positions |
| Grounding context | Did truncation, ordering, duplication, or token budget obscure evidence? | Change context selection and ordering |
| Generation | Did the answer ignore, distort, or overstate supplied evidence? | Tighten the instruction/output contract and compare deployments |
| Citation rendering | Does the displayed citation point to the exact evidence used? | Validate citation IDs through the full response mapping |

Azure AI Search hybrid search runs full-text and vector queries together and merges ranked results. Keyword retrieval helps exact identifiers and specialized terms; vector retrieval helps semantic similarity. Neither is universally better. Microsoft documents the current mechanics in the [hybrid-search overview](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview).

Build a small judged query set with expected evidence, not only expected prose. Track retrieval metrics separately from answer metrics. If the correct passage never enters the context, a fluent answer score can conceal the real defect. If retrieval is strong but groundedness is weak, index tuning alone is unlikely to fix it.

### Freshness and deletion drill

For an updated or deleted source, trace:

```text
source event -> ingestion job -> extracted representation -> chunks
             -> embeddings/index -> cache/knowledge connection
             -> retrieval result -> response/citation
```

Record expected freshness lag, retry/dead-letter behavior, tombstone or deletion semantics, index alias/version change, and proof that stale evidence stops being retrievable. A successful ingestion job count does not prove the current document version is searchable.

## Design an evaluation set that can reject a release

An evaluation dataset should represent the workload's decisions and risks. Include ordinary cases, rare/high-impact cases, ambiguous requests, unanswerable questions, adversarial instructions, multilingual or modality-specific examples, tool failures, access-denied cases, and regressions from real incidents.

| Evaluation layer | Example measures | Release question |
|---|---|---|
| Retrieval | Evidence recall, relevance, rank, ACL correctness | Did the right permitted evidence enter context? |
| Response quality | Task completion, relevance, groundedness, citation correctness, schema validity | Did the application answer the task using evidence? |
| Safety/security | Harm categories, prompt-attack resistance, data leakage, prohibited tool attempt | Did the system remain within policy under attack and edge cases? |
| Agent behavior | Tool-selection accuracy, argument validity, step success, approval compliance, recovery | Did it take only authorized actions and recover safely? |
| Operations | Latency percentiles, token/tool cost, throttles, timeouts, error rate | Can the version meet its service objective at expected load? |
| Human outcome | Reviewer agreement, escalation quality, user success, correction rate | Is the measured proxy consistent with the business result? |

Define thresholds before seeing the candidate's result. Compare against the approved baseline on identical cases and inspect slice-level regressions; an improved average can hide worse results for a critical language, document type, tool, or risk class. Store dataset version, configuration, model/deployment, evaluator version, code commit, and run output so the decision can be reproduced.

Microsoft Foundry separates evaluation, tracing, and production monitoring while connecting all three across the lifecycle. Its [observability guidance](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai) describes quality, RAG, safety, and agent evaluators, plus preproduction and postproduction use. **VERIFY CURRENT:** evaluator availability, regions, quotas, pricing, and preview status.

> **Related item:** An LLM-based evaluator is another model measurement, not ground truth. Calibrate it against reviewed examples, retain deterministic checks for schemas and policies, and sample disagreements for human adjudication.

## Roll out an agent change as an operational experiment

A change to a model, system instruction, tool, knowledge source, safety configuration, or orchestration rule can alter behavior. Package these as one versioned release unit or record their exact independent versions.

Use a progression appropriate to risk:

1. static and contract tests for code, schemas, permissions, and tool mocks;
2. offline evaluation on fixed and newly added regression sets;
3. isolated integration tests with nonproduction resources;
4. shadow or replay evaluation where privacy and terms permit;
5. limited traffic or user cohort with enhanced monitoring;
6. controlled expansion after quality, safety, cost, and latency gates pass;
7. rapid route-back to the last approved version if a stop condition triggers.

Define stop conditions such as unauthorized tool attempts, access-control failures, safety regression, error/timeout increase, groundedness drop, or cost/latency breach. Rollback must address more than application code: prompts, agent definitions, connections, tool versions, index aliases, model deployments, content filters, and feature flags may all affect behavior.

During an incident, a trace should connect the user request to model calls, retrieval, tool calls, evaluations, and dependencies without giving every operator unrestricted access to sensitive content. Microsoft Foundry tracing can integrate with Application Insights; plan sampling, retention, redaction, access, and correlation before production. See the [agent tracing overview](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept).

## Budget latency and cost across the complete call graph

One user turn may invoke query rewriting, embeddings, search, reranking, a planning model, multiple tools, reflection, a final model, safety checks, speech, and retries. Estimate and measure each stage:

| Stage | Latency/cost lever | Risk of aggressive reduction |
|---|---|---|
| Retrieval | Query count, top-k, reranking, document size | Missing evidence or losing exact matches |
| Generation | Model/deployment, input/output tokens, number of calls | Lower task quality, truncation, or weaker reasoning |
| Agent tools | Parallelism, timeout, retry, cache | Duplicate side effects or stale business data |
| Evaluation/safety | Synchronous versus sampled/asynchronous checks | Undetected unsafe or low-quality behavior |
| Speech/multimodal | Media duration/size, streaming, preprocessing | Worse recognition, incomplete context, inaccessible output |

Set a total service objective, allocate a stage budget, and monitor percentiles rather than only averages. Use bounded retries with a total deadline and idempotency where a tool changes state. A cheaper model that triggers more retries, tool calls, corrections, or human escalation may increase total cost.

---

# 11. Hands-on labs

## Lab 1: Secure Foundry application baseline

Create a development project and deploy an eligible model. Connect a small Python application using keyless authentication where supported. Record the identity, role assignment, endpoint, deployment name, timeout, and trace correlation. Prove that removing the role causes authorization failure and restore it.

## Lab 2: Evidence-grounded RAG

Index a small public document set in Azure AI Search. Compare lexical, vector, hybrid, and semantic-ranking results for at least ten questions. Build answers with citations, add one permission-filter field, and test a user who must not retrieve a restricted document.

## Lab 3: Tool-using agent with approval

Build an agent with one read-only tool and one simulated side-effecting tool. Validate tool arguments, require approval for the second tool, use an idempotency key, and cap turns. Create tests for malformed input, denied access, timeout, repeated request, and prompt injection.

## Lab 4: Evaluation and deployment gate

Create normal, difficult, unsafe, and adversarial cases. Evaluate groundedness, task success, safety, latency, and cost for two configurations. Define a release threshold and document why a single average score would hide important failures.

## Lab 5: Multimodal accessibility workflow

Produce concise alt text and a long description for different public images. Add unsafe-content and embedded-instruction tests. Compare generated output with the image's context and accessibility purpose.

## Lab 6: Document-to-agent pipeline

Run public documents through OCR/layout or Content Understanding, generate structured or Markdown output, index it, and query it through an agent tool. Preserve citations from response to extracted region or page.

---

# 12. Scenario checks and exam distinctions

## Knowledge checks

1. A RAG app returns fluent answers with irrelevant citations. Which pipeline stages do you test before changing the model?
2. A private-endpoint deployment works for an administrator but not the application. How do you distinguish identity, RBAC, DNS, and network causes?
3. An agent sometimes sends the same order twice after a timeout. Which API and orchestration controls are missing?
4. A team wants to store every conversation forever to improve quality. Which privacy, consent, access, and evaluation questions must be answered?
5. A document field is frequently wrong even though OCR text is accurate. Which extraction stages should you inspect?
6. A smaller model is slightly less fluent but meets task quality at much lower latency and cost. What evidence supports or rejects routing this use case to it?

## Distinctions to explain without notes

| Contrast | Remember |
|---|---|
| Model vs deployment | Capability/version versus configured endpoint and capacity |
| Model parameter vs prompt | Sampling/output control versus task/context instructions |
| Lexical vs vector search | Term matching versus semantic similarity |
| Hybrid search vs semantic ranking | Combine retrieval methods versus rerank an initial result set |
| OCR vs layout vs field extraction | Text recognition versus structure versus schema mapping |
| Conversation state vs memory vs knowledge | Active interaction versus retained facts versus external evidence |
| Workflow vs agent | Predetermined steps versus model-mediated decisions within constraints |
| Tool schema vs authorization | Describes valid arguments versus enforces who may act |
| Content filter vs groundedness evaluation | Harm classification versus evidence support |
| Retry vs compensation | Repeat a safe operation versus undo/offset a completed side effect |
| Trace vs audit record | Diagnostic execution detail versus controlled evidence of accountable action |
| SDK adapter vs business logic | Volatile provider client versus stable application contract |
| Index relevance vs answer groundedness | Correct evidence retrieval versus claims supported by that evidence |
| Model critique vs deterministic validation | Probabilistic review versus enforced schema/business invariant |
| Agent trace vs hidden reasoning | Observable decisions/actions/evidence versus private internal computation |
| Runner/retry success vs business success | Technical completion versus intended outcome without duplication |

## Readiness checklist

- [ ] I can choose models, Foundry services, retrieval methods, tools, memory, and knowledge integration.
- [ ] I can design infrastructure, deployment, CI/CD, identity, networking, quotas, scaling, and cost controls.
- [ ] I can implement lifecycle safety, evaluation, tracing, provenance, approvals, and agent constraints.
- [ ] I can build and evaluate RAG, tool-using agents, multi-agent orchestration, and hybrid model/rules workflows.
- [ ] I can implement image/video generation, multimodal understanding, accessibility, and visual safety.
- [ ] I can choose and implement text analysis, speech, and translation approaches.
- [ ] I can ingest, enrich, index, retrieve, and extract content with OCR, Search, and Content Understanding.
- [ ] I can diagnose failures by pipeline stage instead of changing the model first.
- [ ] I can version and promote models, prompts, tools, indexes, safety policy, and evaluation gates as one release.
- [ ] I can isolate current Foundry SDK calls behind a testable Python application boundary.
- [ ] I can design an index schema, security filter, retrieval experiment, and citation path.
- [ ] I can implement agent state, tool contracts, multi-model/agent orchestration, bounded critique, and production feedback.
- [ ] I can draw the complete trust boundary, preserve retrieval authorization, and diagnose RAG quality by stage.
- [ ] I can build slice-aware evaluation gates, plan a controlled agent rollout, and budget latency and cost across the call graph.
- [ ] I know which model, pricing, quota, region, preview, SDK, and product details require current documentation.

## Primary references

- [Official AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)
- [Microsoft Foundry overview](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-ai-foundry)
- [Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)
- [Azure AI Search documentation](https://learn.microsoft.com/en-us/azure/search/)
- [Hybrid search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview)
- [Semantic ranking](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)
- [Azure Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)
- [Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Content Understanding prebuilt analyzers](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/prebuilt-analyzers)
- [Evaluation for generative AI](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai)
- [Foundry network isolation](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link)
- [Foundry guardrails](https://learn.microsoft.com/en-us/azure/ai-foundry/guardrails/how-to-create-guardrails?view=foundry)
- [Foundry SDK overview](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview)
- [Tracing generative AI applications](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/trace-application)
- [Agent tracing overview](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)
- [Azure AI Search vector and hybrid search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)
- [Content Understanding overview](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview)
- [Azure Speech documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)

Recheck model versions, deployment types, SDKs, quotas, pricing, regions, preview status, and product naming before the exam.

---

# Places to learn

This is a curated starting point, not a complete list. You are not meant to consume every resource. Start with the official blueprint, then pick the instructor, format, examples, and hands-on work that help you close specific gaps. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AI-103 course](https://learn.microsoft.com/en-us/training/courses/ai-103t00) | Free self-study; instructor-led options vary | 4 days (official course) | Official objective-aligned starting point and lab sequence |
| [Microsoft — AI-103 Practice Assessment on AI Skills Navigator](https://aiskillsnavigator.microsoft.com/credentials/cert-3fb198f57997226a824aa5f52a1a22af9a4597941b2288ed39371c7a9e6bd7c9) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check; AI Skills Navigator sign-in is required, and the blueprint and product documentation remain authoritative |
| [Microsoft Partner Skilling Hub — LevelUp AI-103](https://www.skilling-hub.com/en-US/listing/o::levelup::2394396) | Partner login required | 10 hours | No additional cost for eligible Microsoft partners; self-paced coverage includes generative apps, agents, tools, knowledge connections, multimodal content, and exam preparation |
| [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/) and [AI Show](https://learn.microsoft.com/en-us/shows/ai-show/) | Free | Select 4–10 hours by gap | Current behavior and public demonstrations; select pages and episodes by objective |
| [O'Reilly — AI-103 Crash Course with Yasir Khan](https://www.oreilly.com/live-events/azure-ai-apps-and-agents-developer-associate-certification-ai-103-crash-course/0642572384906/0642572384890/) | Subscription or event access | About 4 instructional hours plus breaks | Certification-focused walkthrough across all five domains; verify the event occurrence and current baseline |
| [O'Reilly — Hands-On Microsoft Foundry](https://www.oreilly.com/live-events/hands-on-microsoft-foundry/0642572231088/0642572231071/) | Subscription or event access | 4 hours (October 22, 10 a.m.–2 p.m. EDT) | Supporting implementation practice; not a substitute for full blueprint coverage |
| [O'Reilly — Introduction to AI Agents on Azure](https://www.oreilly.com/live-events/introduction-to-ai-agents-on-azure/0642572194079/) | Subscription or event access | 4 hours (published agenda) | Agent concepts and Azure implementation context; the listed live occurrence has ended |
| [Udemy — AI-103 course by Alan Rodrigues](https://www.udemy.com/course/ai-102-microsoft-certified-azure-ai-engineer-associate-d/) | Purchase or subscription | 32 hours 56 minutes | Long-form implementation course shown as updated July 2026; current listing follows AI-103 despite the legacy URL slug |
| [Udemy — AI-103 course by Luke Ginn](https://www.udemy.com/course/ai-103-azure-ai-app-and-agent-developer-complete-course/) | Purchase or subscription | 30 hours 22 minutes | Deep alternative updated August 2026; includes labs and some explicitly marked older lectures, so follow the current sections |
| [Pluralsight — Build a Generative AI Solution with Azure](https://www.pluralsight.com/paths/build-a-generative-ai-solution-with-azure) | Subscription | 3 hours across one course and three labs | Current 2026 implementation practice for a secure Azure OpenAI pipeline, rate limits, monitoring, and data services; supports only part of AI-103 |
| [LinkedIn Learning — Azure AI for Developers: Building AI Agents](https://www.linkedin.com/learning/azure-ai-for-developers-building-ai-agents) | Subscription | 1 hour 53 minutes | Hands-on Python agent foundation released February 2025; frameworks and product surface predate AI-103, so treat it as adjacent skills practice |

No exact Pluralsight certification path or standalone MeasureUp AI-103 practice-test page was verified during the August 31, 2026 review. Whizlabs announced a 100-question AI-103 bank in August 2026, but the reviewed public listing did not expose a stable exam-specific product URL, so it is not linked yet. The free Microsoft assessment above is available; the listed Pluralsight path supports a subset of the objectives. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
