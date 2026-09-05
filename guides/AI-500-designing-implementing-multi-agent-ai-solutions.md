---
exam_code: AI-500
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# AI-500 Designing and Implementing Multi-Agent AI Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ai-500-coverage-record). The [official AI-500 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500) is authoritative.

**Current baseline:** Official study-guide page last updated July 16, 2026; Microsoft does not publish a separate skills-effective date on that page.<br>
**Exam state:** Beta, English only, as verified September 1, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Credential prerequisite:** Microsoft Certified: Azure AI Apps and Agents Developer Associate (AI-103).<br>
**Training availability:** The exam is already in beta; the separate AI-500T00-A instructor-led course is listed as available September 30, 2026.<br>
**Official source:** [AI-500 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500)

## How to use this guide

AI-500 is an expert-level architecture-and-implementation exam. Do not study each agent feature in isolation. For every objective, practice moving through this chain:

```text
business goal
  → deterministic workflow versus agent decision
  → agent boundaries, protocol, tools, memory, and model
  → identity, data, network, and approval controls
  → evaluation, trace, release, rollback, and operating evidence
```

Start with the architecture contract and the four domain maps. Then implement the labs, explain the integrated scenarios without notes, and use the knowledge checks to identify weak decisions. The official blueprint is the coverage checklist; this guide connects its bullets into production systems.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

### Current Microsoft Foundry versus older material

Unless explicitly marked **FOUNDRY (CLASSIC)**, this guide uses the current Microsoft Foundry resource/project model, current SDK/API generation, Responses-based agents, and current Agent Framework vocabulary. Older courses may say Azure AI Studio, Azure AI Foundry, hubs, `azure-ai-projects` 1.x, Assistants, threads, or runs. Those concepts can help with migration, but do not mix their resource model, SDK objects, endpoints, or portal steps into a current implementation. Use Microsoft’s [classic-to-current migration guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic) as the crosswalk.

The official AI-500 learning path includes migration from Foundry Agents v1 to the current v2/Responses model. Treat version recognition as operational knowledge: first identify the platform generation, then apply guidance written for it.

## Exam profile and objective map

The target role designs production-grade, multi-agent solutions and implements them in Python on Azure. The blueprint expects familiarity with Azure compute, networking, storage, data, Microsoft Foundry, Agent Framework, Model Context Protocol (MCP), retrieval-augmented generation (RAG), and LangGraph—not merely prompt writing.

| Official domain | Weight | Central question |
|---|---:|---|
| Architect multi-agent solutions | 15–20% | How should goals become bounded agents, workflows, protocols, identities, state, and operating controls? |
| Develop multi-agent solutions in Azure | 30–35% | How are prompts, context, memory, knowledge, tools, orchestration, frameworks, and middleware implemented? |
| Evaluate, optimize, and monitor multi-agent solutions | 20–25% | How do you prove quality, continuity, reliability, performance, and cost over time? |
| Secure, govern, and deploy multi-agent solutions | 20–25% | How are access, secrets, guardrails, adversarial testing, environments, and releases controlled? |

### Complete objective-to-guide map

| Published objective area | Primary coverage | Practice evidence |
|---|---|---|
| Decompose goals; define workflows, agents, subagents, control loops, human oversight, personas, boundaries, autonomy, tools, protocols, memory, models, and responsible-AI controls | Sections 1–2 | All scenarios; Labs 1–2 |
| Select integration, Zero Trust, state, compute, observability, monitoring, and developer-environment components | Sections 1–2 | Scenarios 1 and 3; Labs 1–3 |
| Engineer prompts, context, fine-tuning, memory, RAG, knowledge, functions, MCP, error handling, result validation, orchestration, scale, frameworks, and middleware | Sections 3–5 | All scenarios; Labs 2–5 |
| Evaluate agents, memory, knowledge, tools, prompts, duration, parallelism, context failures, feedback, reliability, tokens, cost, quotas, and traces | Section 6 | All scenarios; Labs 5–7 |
| Configure resource access, authentication, secrets, Zero Trust, red teaming, guardrails, tests, environment promotion, release strategies, CI/CD, and IaC | Section 7 | All scenarios; Labs 3 and 6–8 |

## 1. Start with an architecture contract

A multi-agent solution is a distributed system whose components can reason probabilistically and invoke tools. Before choosing a framework, record the contract that constrains that freedom.

| Contract element | Questions to answer | Evidence to retain |
|---|---|---|
| Outcome | What measurable result ends the workflow? What is explicitly out of scope? | Acceptance criteria and task-success metric |
| Decomposition | Which steps are deterministic, model-assisted, or delegated to another agent? | Workflow diagram and decision rationale |
| Agent boundary | What does each agent know, decide, and never do? | Persona, instructions, allowed tools, autonomy tier |
| Protocol | What message and artifact shapes cross a boundary? | Versioned schemas, correlation IDs, timeout/error semantics |
| Identity | Which principal authorizes each resource and downstream action? | Identity-to-resource-to-role matrix |
| State | What is session, shared, semantic, or durable business state? | Data classification, ownership, TTL, isolation, recovery plan |
| Safety | Where can input, retrieval, tool, or output cause harm? | Threat model, guardrail policy, approval points |
| Quality | How will task quality and each component be evaluated? | Dataset, evaluators, thresholds, slice results |
| Operations | How will the system expose failure, latency, tokens, cost, and drift? | Trace schema, SLOs, alerts, runbooks |
| Release | What is promoted, compared, approved, and rolled back? | Version manifest, gates, rollout and rollback evidence |

Microsoft’s [multiple-agent reference architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/multiple-agent-workflow-automation) is a useful starting topology, not a substitute for this workload-specific contract.

### Decide whether another agent is justified

Use deterministic code when the next step is known and must be repeatable. Use one agent when a bounded reasoning loop can complete the task with a small tool set. Add another agent only when separation improves one or more of these properties:

- specialization of instructions, model, knowledge, or tools;
- isolation of permissions or sensitive data;
- independent scaling or failure containment;
- reusable ownership boundary;
- parallel work that materially reduces elapsed time;
- review or adversarial separation between producer and checker.

An extra agent also adds prompts, tokens, latency, state transitions, failure modes, and attack surface. “Multi-agent” is not automatically more capable than one well-designed agent plus deterministic functions.

> **Related item:** This is the same coupling-versus-cohesion decision used in service architecture. A separate deployment can isolate ownership and scale, but a network boundary is expensive if the responsibilities are not genuinely independent.

### Decompose goals into observable work

A strong decomposition produces steps with explicit input, output, owner, timeout, retry rule, and completion condition.

```text
request
  → classify and validate                  deterministic policy
  → plan bounded tasks                     coordinator agent
  → retrieve policy evidence               knowledge agent/tool
  → calculate or change system state       deterministic tool
  → review risky recommendation            reviewer agent and/or human
  → compose cited result                   response agent
  → validate schema and policy             deterministic gate
```

Keep business state outside conversational prose when another component must depend on it. Pass a typed artifact such as a task object, evidence list, proposed action, or approval record. Free-form messages are valuable for reasoning but weak as the sole durable contract.

### Define personas, scope, and autonomy

An agent definition should contain:

- purpose and allowed outcomes;
- trusted instruction sources and precedence;
- input and output schemas;
- knowledge sources and freshness expectations;
- allowed tools with parameter constraints;
- stop, abstain, and escalation rules;
- token, time, iteration, concurrency, and cost budgets;
- prohibited actions and data classes;
- human approval boundaries;
- evaluation and monitoring ownership.

Use an autonomy ladder:

1. **Draft:** agent proposes; a person performs the action.
2. **Prepare:** agent produces exact parameters; a person approves execution.
3. **Act within bounds:** agent executes reversible, low-impact actions inside policy.
4. **Escalate:** uncertainty, sensitivity, policy match, or repeated failure stops automation.

Autonomy should follow impact and reversibility, not model fluency.

### Select an orchestration topology

The current [Agent Framework orchestration documentation](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/) describes reusable patterns. Know the tradeoff, not just the name.

| Pattern | Use when | Main risk | Useful control |
|---|---|---|---|
| Sequential | Each stage depends on the prior artifact | Error accumulation and latency | Validate every handoff; checkpoint state |
| Concurrent | Independent specialists can work in parallel | Duplicate cost and conflicting answers | Bounded fan-out and explicit aggregator |
| Handoff | Current specialist can route to a better owner | Ping-pong routing and lost context | Handoff budget, routing reason, shared task ID |
| Group chat | Multiple roles must iteratively collaborate | Long loops and unclear authority | Manager/termination rule and speaker policy |
| Orchestrator–subagent | One coordinator decomposes and synthesizes | Coordinator bottleneck or excess authority | Constrained delegation and typed results |
| Peer-to-peer | Domains negotiate without a central coordinator | Harder global state and debugging | Protocol, idempotency, correlation, circuit breaking |
| Magentic/dynamic planning | Open-ended task needs adaptive decomposition | Unbounded work and unpredictable cost | Budgets, milestones, approval, and replayable trace |

Choose topology from dependency shape, control needs, latency, and failure ownership. A diagram alone is not a design: define who commits durable state and what happens when any message is late, duplicated, invalid, or unavailable.

### Design control loops and human-in-the-loop

A bounded control loop has state and an exit condition:

```text
observe → decide → act/tool → validate → complete | retry | compensate | escalate
```

Cap iterations and wall-clock duration. Distinguish transient retry from “try reasoning again.” Use idempotency keys for retried writes, and compensating actions where a transaction cannot span services. Agent Framework [human-in-the-loop workflows](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop) pause with sufficient state for a person to approve, reject, edit, or supply missing information; the resumed workflow must revalidate that the approval is still applicable.

> **Related item:** A human approval is an authorization event. Record the approver, exact proposed action, time, policy, and decision; do not treat a generic chat response as durable consent.

## 2. Choose protocols, identity, memory, models, and infrastructure

### Separate coordination protocols from tool protocols

Use a protocol only where interoperability is worth another boundary.

| Need | Appropriate contract | Design focus |
|---|---|---|
| Application calls a local function | Typed function/tool schema | Validation, least privilege, errors, idempotency |
| Agent discovers and calls tools or resources from a server | MCP | Capability discovery, authentication, server trust, schema and result validation |
| One independent agent communicates with another | Agent-to-Agent (A2A) endpoint/protocol | Agent card/capability, task identity, authentication, artifact and status semantics |
| Internal workflow components exchange events | Framework message or application event contract | Ordering, duplication, correlation, recovery |

[Azure API Management’s MCP support](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) can expose governed APIs as MCP tools and apply gateway policies. It does not remove the need to authorize the downstream operation or validate tool results. Current Foundry [A2A endpoint support](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/enable-agent-to-agent-endpoint) is preview and fast-changing; **VERIFY CURRENT** capabilities, authentication, and regional availability.

### Apply Zero Trust per agent

Do not give every agent the coordinator’s identity. Map each runtime identity to only the resources and actions its role requires. This limits lateral movement if instructions, retrieved content, or a tool result are compromised.

| Actor | Typical access | Avoid |
|---|---|---|
| Coordinator | Invoke bounded specialist agents; read task state | Direct write access to every business system |
| Retrieval agent | Read permitted search index or data partition | Broad source-storage write or secret access |
| Action agent | Invoke one approved operation | User-wide delegated permissions when app-only scope works |
| Evaluation worker | Read approved test cases and sanitized traces | Production secrets and unrestricted raw personal data |
| Human approver | Review exact action and evidence | Shared accounts or approval without authenticated identity |

Current Foundry [agent identity concepts](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) distinguish platform and application identities. For a user-delegated downstream call, the Microsoft Entra Agent ID [on-behalf-of flow](https://learn.microsoft.com/en-us/entra/agent-id/agent-on-behalf-of-oauth-flow) preserves delegated context. For an application-owned operation, prefer a workload identity and app permission scoped to the operation. API keys identify an application weakly and are difficult to constrain per agent; use them only where the service requires them and protect/rotate them through Key Vault.

> **Related item:** Authentication proves the caller; authorization decides the allowed action. Private networking changes reachability. Guardrails inspect content or behavior. None substitutes for the others.

### Use a multi-tier state and memory model

“Memory” is not one database. Classify it by purpose and lifecycle.

| Tier | Example | Scope and lifecycle | Primary controls |
|---|---|---|---|
| Working context | Current messages, retrieved passages, intermediate artifacts | One model call or short workflow | Token budget, minimization, injection defense |
| Session state | Task progress, tool results, approvals, checkpoints | One conversation/workflow | Tenant key, TTL, concurrency control, replay |
| Shared workflow state | Typed tasks and artifacts used by several agents | Workflow or case | Schema/version, owner, transaction/idempotency |
| Long-term semantic memory | Approved preferences or prior facts retrieved later | User/tenant-defined retention | Consent, provenance, correction, deletion, access-aware retrieval |
| Durable business record | Order, ticket, decision, audit event | System-of-record retention | Transactional integrity, policy, legal hold, recovery |

Do not store a durable business decision only in a vector index or conversation. Preserve authoritative data in its system of record; embeddings are derived retrieval assets that must retain source ID, tenant, version, and deletion linkage.

Design isolation at write and query time. Every memory record needs a tenant/user scope, data classification, provenance, owner, TTL or retention policy, and deletion path. Summaries can reduce context cost but may omit details or introduce summary drift; keep authoritative source references and test whether required entities survive compaction.

### Match model family to task demand

Use evidence rather than a “largest model everywhere” rule. Compare candidates on task quality, modality, context, tool use, structured output, latency, throughput, safety, region, quota, and total cost. Foundry [model benchmarks](https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks) can create a shortlist; evaluate the exact deployed model, prompt, tools, retrieval, and safety configuration on workload cases.

Use a smaller or specialized model for classification, extraction, routing, or high-volume constrained work when it meets the quality threshold. Use a stronger reasoning model where planning difficulty justifies latency and cost. Record fallback behavior: a fallback model may not support the same context window, tool semantics, or structured-output fidelity.

**VERIFY CURRENT:** Model versions, regions, quotas, prices, deployment types, and support status change frequently.

### Design compute and developer environments

Compute selection affects cold start, scale, isolation, networking, GPU/CPU availability, operational burden, and cost. Keep agents stateless where practical; externalize durable state and make work replayable. Bound concurrent fan-out to downstream model/tool quotas, not only compute capacity.

Standardize the developer environment with a dev container or equivalent pinned environment, supported Python version, lock file, linters/tests, Azure CLI and developer CLI where used, and explicit AI coding instructions. Keep local emulators/mocks for deterministic tools, and use separate development resources for real model integration tests. Never place production credentials in a container image or repository.

> **Related item:** Reproducibility includes prompts, tool schemas, model deployment names/versions, evaluation datasets, infrastructure, and safety configuration—not only Python dependencies.

### Build observability into the design

Give the original request, workflow, agent, model call, retrieval, and tool call correlated identifiers. Foundry’s [agent tracing model](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) uses spans across model calls, tools, state, and collaboration.

Capture, subject to privacy controls:

- selected agent, model deployment, prompt/configuration version, and route reason;
- parent/child correlation, start/end time, retries, and termination reason;
- token input/output/cache use, latency, and estimated cost attribution;
- retrieved source IDs and ranking evidence;
- tool name, validated parameters or safe digest, result status, and idempotency key;
- evaluation/safety results, human decisions, and final task outcome.

Reasoning-path logging does not mean exposing hidden chain-of-thought. Store structured decision events, selected routes, tool evidence, summaries, and outcomes that operators are permitted to inspect. Apply redaction, access control, sampling, encryption, and retention because traces can contain sensitive input, output, and tool data.

## 3. Engineer prompts, context, and memory

### Treat prompts as versioned program inputs

A production prompt has a purpose, trusted instruction hierarchy, input schema, output contract, constraints, examples where useful, tool policy, and failure behavior. Test it like code.

Use advanced patterns deliberately:

- **few-shot examples:** demonstrate classifications or output shapes, including difficult boundaries;
- **dynamic injection:** add tenant, task, policy, or retrieved context through clearly delimited fields;
- **defensive prompting:** state that untrusted data cannot override instructions, but back this with tool authorization and output validation;
- **lifecycle management:** version, evaluate, approve, release, observe, and roll back prompt changes.

Do not concatenate raw user or retrieved content into system instructions. Separate trusted instructions from untrusted data, delimit inputs, validate length/type, and keep secrets out of prompts.

### Build context intentionally

Context engineering decides what each call needs and what it must not see. A useful pipeline is:

1. classify the task and authorization scope;
2. select instructions and permissible memory;
3. retrieve scoped evidence;
4. rank/deduplicate and fit the token budget;
5. inject provenance-bearing context;
6. request a typed result or citations;
7. validate output and update approved state.

Context accumulation is easy; controlled context is the skill. Long histories can dilute instructions, increase cost, or exceed the window. Use selective retrieval, rolling summaries, entity/state tables, and checkpoints. Preserve important values in typed state instead of hoping a summary retains them.

### Choose prompting, RAG, memory, or fine-tuning

| Need | Best first move | Why |
|---|---|---|
| Current private facts | RAG/tool retrieval | Keeps changing knowledge outside model weights |
| Conversation/task continuity | Session state and controlled memory | Preserves approved state with lifecycle controls |
| Stable response behavior or format | Prompt/examples and schema validation | Fast to change and evaluate |
| Repeated domain behavior that prompting cannot achieve economically | Fine-tuning candidate | Can adapt behavior after evidence shows a gap |
| Deterministic calculation or action | Tool/function | Source system owns truth and side effect |

Fine-tuning is not a way to keep frequently changing facts current. Define the target behavior, representative and permissioned data, train/validation/test separation, safety review, retraining trigger, and rollback path. Re-evaluate after base-model, data, prompt, or policy changes. Microsoft’s [fine-tuning guidance](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning) is platform-specific and should be checked for current model support.

### Design secure memory operations

For every write, decide whether the item is eligible for memory, whose scope it belongs to, whether the user can inspect/correct/delete it, and when it expires. For every read, enforce authorization before similarity ranking and return provenance. Never allow cross-tenant nearest-neighbor results because a filter was applied after retrieval.

Memory failure modes include:

- **sliding-window amnesia:** an important fact falls outside context;
- **summary drift:** repeated compression changes meaning;
- **vector-only recall:** exact identifiers or relationships are not reliably recovered;
- **entity discontinuity:** two names/IDs for the same entity are not reconciled;
- **stale memory:** newer authoritative state conflicts with an old stored item;
- **poisoned memory:** untrusted input is promoted into durable context.

Mitigate with typed state, provenance, freshness/version checks, hybrid retrieval, entity resolution, write approval, and tests that span long conversations.

> **Related item:** Memory is governed data. Data minimization, residency, retention, legal hold, subject rights, and incident response apply even when the user interface calls it “conversation history.”

## 4. Build knowledge and tools

### Engineer multi-agent RAG

RAG has an ingestion path and a request path:

```text
source → authorize/classify → parse → chunk → enrich → embed → index/version
request → identify caller → filter scope → retrieve → rank → assemble → generate → cite/validate
```

Choose chunk boundaries from document structure and answer granularity. Too small loses context; too large wastes tokens and can reduce retrieval precision. Preserve parent/child relationships, headings, source URL/ID, version, access tags, and timestamps. Test lexical, vector, semantic, and hybrid retrieval on real questions, including questions with no authorized answer.

In a multi-agent design, centralize retrieval policy or make every agent enforce the same authorization contract. A coordinator must not pass evidence to a subagent that the subagent or end user is not allowed to see. Microsoft’s [RAG overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation) explains the pattern; the workload still needs access-aware ingestion and retrieval.

Evaluate retrieval independently with relevance/precision, recall or coverage, ranking quality, authorization correctness, freshness, and citation resolution. Then evaluate grounded response quality. A good answer can hide poor retrieval, and good retrieval can be ruined by synthesis.

### Design function tools

Treat every tool as an API exposed to a potentially mistaken or manipulated caller.

- use a narrow, descriptive name and typed schema;
- validate type, format, range, enumeration, ownership, and current state server-side;
- authorize the effective principal for the exact operation;
- distinguish read, reversible write, and irreversible/high-impact action;
- require preview/confirmation or human approval where risk demands it;
- make retries idempotent or provide compensation;
- return structured success/error data with safe details;
- validate results before another agent trusts them;
- log correlation, caller, policy decision, and outcome without leaking secrets.

Dynamic tool selection can reduce a large tool surface, but the selector must never bypass authorization. Specified/forced tool use can make a workflow more deterministic; it still needs result validation and a failure path.

### Build and govern MCP integrations

An MCP client discovers and invokes capabilities exposed by an MCP server. Before trusting a server, establish its owner, code/configuration source, authentication, allowed tools/resources, data handling, network path, change process, and monitoring. Pin or approve versions where possible and re-evaluate capability changes.

MCP error handling should distinguish invalid model-generated arguments, authentication/authorization failure, transient dependency failure, business rejection, and malformed/untrusted result. Do not feed raw error pages or instructions from a tool result back into privileged context.

Azure Functions and Logic Apps can implement integration operations; API Management can publish and govern eligible API operations as MCP tools. Choose based on code/control needs, connector/workflow needs, and gateway policy needs—not because every integration requires all three.

> **Related item:** MCP standardizes discovery and invocation; it is not an authorization model or a trust guarantee. The server remains a software supply-chain and data-exfiltration boundary.

### Connect existing agents through A2A or MCP

Use MCP when an existing component should expose tools/resources. Use A2A when it behaves as an independently addressable agent with task and artifact semantics. Put an adapter around older agents rather than leaking version-specific conversation objects throughout the new system. Test authentication, capability discovery, timeouts, cancellation, status polling/streaming, duplicate messages, malformed artifacts, and version mismatch.

## 5. Implement orchestration and reusable code

### Select a framework without surrendering architecture

The blueprint names Microsoft Agent Framework, LangChain/LangGraph, and Hugging Face Transformers. Know their role boundaries:

| Technology | Strong fit | Keep explicit |
|---|---|---|
| Microsoft Agent Framework | Azure/.NET/Python agent abstractions, workflows, orchestrations, middleware, HITL | Preview/current API status, persistence, identity, tool policy |
| LangChain | Model/tool/retrieval composition and ecosystem integrations | Versioned interfaces, callbacks, security of integrations |
| LangGraph | Graph/state-machine orchestration, checkpoints, interrupts, durable flows | State schema, node idempotency, resume semantics |
| Hugging Face Transformers | Local/open-model loading, inference, training/fine-tuning components | Hardware, model license, safety, serving, optimization |

Framework convenience does not own your data classification, authorization, evaluation, SLO, or rollback. Wrap framework-specific objects behind application interfaces where replacement or migration matters.

### Make human intervention a workflow state

Store an approval request containing the exact proposed operation, parameters, evidence, risk reason, expiry, and required approver role. On resume:

1. authenticate and authorize the approver;
2. verify the workflow and proposal have not changed;
3. re-check relevant business state and policy;
4. execute with an idempotency key;
5. record the decision and outcome;
6. route rejection, edit, expiry, or edge case explicitly.

### Control caching and concurrency

| Technique | Benefit | Correctness risk |
|---|---|---|
| Prompt-prefix caching | Reduces latency/cost for stable shared prefixes | Sensitive or tenant-specific content in a supposedly shared prefix |
| Semantic cache | Reuses answers for similar requests | Similar wording but different authorization, freshness, or intent |
| Response cache | Fast exact reuse | Stale data, wrong user scope, missing side effects |
| Tool-result cache | Reduces dependency calls | Source state changes or write operation accidentally replayed |

Every cache key needs tenant/identity, configuration/model version, data version or freshness rule, and policy context where those affect the answer. Never cache an authorization decision longer than its valid context.

Parallel work reduces elapsed time only when tasks are independent. Bound task spawning, batch size, concurrency, queue depth, tokens, calls, and time. Apply backpressure before model or tool quotas collapse. Cancel unnecessary branches when the workflow completes, and preserve partial results only if their ownership and reuse are defined.

### Build middleware for cross-cutting policy

Reusable middleware can add correlation IDs, authentication context, authorization checks, safe logging, redaction, retry/timeout policy, exception normalization, metrics, and policy gates. Keep business decisions in the workflow or domain service; keep consistent enforcement in middleware. Define ordering—authorization must occur before a protected call, and redaction must occur before unsafe logging.

## 6. Evaluate, optimize, and operate the system

### Evaluate components and the whole workflow

One overall score cannot explain a multi-agent failure. Build an evaluation matrix.

| Layer | Example measures | Failure question |
|---|---|---|
| Prompt/model | instruction adherence, correctness, structured-output validity, safety | Did the model follow the contract? |
| Retrieval/knowledge | relevance, coverage, freshness, access correctness, citation resolution | Was the right authorized evidence available? |
| Memory/context | entity continuity, required-fact retention, stale/poisoned memory rejection | Did necessary state survive correctly? |
| Tool | argument validity, authorization, success rate, idempotency, result validation | Was the right operation performed safely? |
| Agent | task success, route quality, abstention/escalation, budget compliance | Did the specialist fulfill its bounded role? |
| Workflow | end-to-end success, duration, handoffs, human wait, cost | Did collaboration improve the outcome? |
| Safety/governance | policy violations, attack success, data leakage, audit completeness | Did controls hold under misuse? |

Foundry supports [generative-AI evaluation](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app) and risk/safety evaluators. Use human review in Foundry for subjective, high-impact, ambiguous, or calibration cases. Measure agreement and document reviewer guidance rather than treating one reviewer’s preference as ground truth.

### Test execution behavior

Track wall-clock duration, model/tool latency, queueing, human wait, sequential critical path, parallel fan-out, and rate-limit response. Parallelism can reduce latency but increase cost and throttling. Evaluate under realistic concurrency and failure injection:

- one subagent times out;
- a tool returns a transient error, business rejection, duplicate, or malformed result;
- the retrieval index is stale or partially unavailable;
- a human approval expires;
- a model deployment is throttled;
- a worker resumes from an old checkpoint.

Verify bounded retries, idempotency, fallback compatibility, partial-result policy, circuit breaking, and operator recovery.

### Diagnose continuity failures

For long-session tests, create facts and decisions early, add distracting turns, compact context, change an authoritative value, and verify correct later behavior. Attribute failure to retrieval, selection, compaction, entity mapping, authorization, or generation rather than merely increasing the context window.

| Symptom | Likely cause | Better next test |
|---|---|---|
| Early constraint forgotten | Sliding-window amnesia | Typed state versus larger window |
| Details change after several summaries | Summary drift | Compare summary to checkpointed source |
| Exact ID missed but similar prose found | Vector-only recall | Hybrid/exact lookup and metadata filters |
| Customer aliases split history | Entity discontinuity | Canonical ID and entity-resolution test |
| Old preference overrides new record | Freshness conflict | Version/provenance resolution rule |

### Create continuous-improvement loops safely

Production feedback becomes an input, not an automatic prompt rewrite. Combine:

- curated human judgments;
- task outcome and user feedback;
- deterministic schema/policy checks;
- LLM-as-judge with human calibration and version tracking;
- synthetic cases that expand rare, unsafe, and boundary scenarios;
- semantic comparisons for non-exact valid answers.

Triage failures, label root cause, add representative regression cases, propose a bounded change, evaluate offline, approve, release gradually, and monitor. Keep a holdout set to reduce overfitting to the visible suite.

> **Related item:** An LLM judge is another model-dependent measurement instrument. Track its prompt/model version, bias, agreement with expert reviewers, and failure modes.

### Monitor reliability, tokens, and cost

Define SLOs at the user outcome and critical component levels. Useful signals include task success, refusal/escalation, failed or repeated handoffs, tool errors, loop/termination counts, latency percentiles, platform availability, quota/rate-limit events, token distribution, and cost per successful outcome.

Set hard limits for iterations, tokens, wall time, spawned tasks, concurrent calls, and tool invocations. Alert before a loop becomes a cost incident. Allocate cost by tenant, product, team, environment, workflow, agent, model, and tool as needed for showback/chargeback. A cheap model call that drives retries or human correction may increase cost per successful result.

Foundry’s [agent monitoring dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard) and [trace setup](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) are current implementation starting points. **VERIFY CURRENT:** preview/support differences can vary by agent type and environment.

## 7. Secure, govern, test, and deploy

### Build a resource-access matrix

For each agent/workload, list identity type, resource, operation, scope, role/permission, network path, credential mechanism, and audit source. Current Foundry [RBAC guidance](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) and private-link documentation establish the platform boundary; downstream tools need their own least-privilege controls.

Prefer managed/workload identity where supported. Use delegated OAuth/on-behalf-of only when the downstream action genuinely must represent the user. Avoid impersonation patterns that obscure who or what acted. If a secret or certificate remains necessary, store it in Key Vault, grant minimum data-plane access, rotate it, monitor access, and design applications to reload it safely. Encryption protects stored/transmitted data; it does not authorize use.

### Place guardrails at four intervention points

Microsoft documents [guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points) around the application flow. Use layered controls:

| Point | Examples | Required companion control |
|---|---|---|
| User input | Harm classification, prompt-attack detection, input schema/size | Authentication, rate limit, task policy |
| Before tool call | Tool allowlist, parameter validation, approval | Downstream authorization and idempotency |
| Tool response | Treat output as untrusted, detect injection/data leakage, schema validation | Server trust and result provenance |
| Final output | Harm/privacy/groundedness/policy check, citation validation | Safe fallback, escalation, audit |

Build custom guardrails for domain policy such as prohibited transactions, regulated claims, tenant rules, or required evidence. Generate synthetic normal, edge, adversarial, multilingual, obfuscated, and tool-mediated cases; measure false positives and false negatives. Do not tune only until the test set passes.

### Shift left with adversarial testing

Use the Foundry [AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) as one testing capability, not a guarantee of safety. Include direct/indirect prompt injection, data exfiltration, tool misuse, privilege escalation, cross-tenant access, poisoned memory, denial-of-wallet loops, unsafe output, and evasion attempts. Run only in authorized scope with safe targets and protected test data. Convert important findings into regression tests and verify the mitigation does not break legitimate behavior.

### Design environment promotion and release

Development, test, acceptance/staging, and production should separate identities, data, endpoints, quotas, state, secrets, and approval rights. Promote versioned artifacts rather than editing production interactively:

- application and workflow code;
- infrastructure as code;
- prompt and agent instructions;
- tool schemas and MCP/A2A configuration;
- model deployment/configuration references;
- evaluation datasets, evaluator versions, and thresholds;
- guardrails and policies;
- search/index schema and migration logic;
- dashboards, alerts, and runbooks.

Use unit tests for deterministic functions, schema validators, routing rules, and middleware. Use integration tests for identity, retrieval, model, agent, tool, and network boundaries. Use regression/evaluation suites for probabilistic behavior. A CI/CD gate should validate IaC, run security/static/dependency checks, execute deterministic tests, evaluate quality/safety/cost thresholds, produce an evidence manifest, require approvals, deploy gradually, smoke test, and retain rollback inputs.

| Release approach | Fit | Watch |
|---|---|---|
| Blue-green | Rapid environment switch and rollback | Stateful workflows and duplicated capacity |
| Canary | Small percentage/tenant cohort receives change | Comparable telemetry and sticky workflow version |
| Shadow | New version observes copied inputs without acting | Sensitive data duplication and cost |
| Feature flag | Bounded behavior/tool/prompt enablement | Flag ownership and interaction complexity |

Pin an in-flight workflow to a compatible version or explicitly migrate its state. Rolling back code does not automatically undo an external tool side effect, memory write, index change, or state-schema migration.

## 8. Integrated scenarios

### Scenario 1: Regulated customer-service case

**Goal:** answer account questions and prepare a high-impact change that requires approval.

**Design:** A coordinator validates intent and creates typed tasks. A retrieval agent uses access-aware RAG against approved policy. An account tool reads current state under the user’s delegated context. A change agent can prepare, but not execute, the operation. A human sees the exact action, evidence, and risk; execution revalidates state and uses an idempotency key. A response agent returns citations and the recorded outcome.

**Controls:** per-agent identities, tenant filters before retrieval, untrusted-tool-result guardrail, no secrets in traces, approval expiry, immutable audit record, denial-of-wallet budgets.

**Evidence:** retrieval/citation correctness, unauthorized-query tests, approval record, tool idempotency test, task success, time-to-resolution, human override rate, trace completeness.

**Failure exercise:** inject a policy document that tells the agent to call a transfer tool. The retrieval agent can return it as data; instructions, tool authorization, approval, and server-side policy prevent the action.

### Scenario 2: Software incident investigation

**Goal:** diagnose an incident using telemetry, change history, and runbooks; permit only reversible remediation inside policy.

**Design:** A planner creates parallel log, deployment, dependency, and runbook tasks. Specialists return typed findings with evidence IDs. An aggregator ranks hypotheses. A remediation agent may restart a stateless instance within a narrow scope but prepares higher-impact changes for an operator. Workflow state checkpoints allow resume after a timeout.

**Controls:** read-only identities for investigators, bounded fan-out, query/time/token budgets, tool result schemas, no raw secrets in context, current-state recheck before action, circuit breaker, operator escalation.

**Evidence:** time to useful hypothesis, evidence precision, repeated/failed handoffs, false-remediation rate, tool latency, rate limits, total cost, recovery after one specialist fails.

**Failure exercise:** throttle the model used by one specialist. Verify bounded retry, compatible fallback or partial-result policy, preserved correlation, and no duplicate remediation.

### Scenario 3: Governed knowledge-production workflow

**Goal:** produce a cited technical recommendation from internal and public evidence.

**Design:** A research coordinator delegates source discovery, retrieval, claim extraction, and independent review. Durable claim objects contain source ID, excerpt location/digest, date, confidence, and authorization scope. The writer can use only approved claims. A reviewer checks contradiction, freshness, citation resolution, and unsupported synthesis before publication.

**Controls:** source allowlist, content treated as untrusted, tenant isolation, provenance, author/reviewer separation, current-source check, output guardrail, release approval.

**Evidence:** citation precision/recall, unsupported-claim rate, source freshness, reviewer agreement, context-continuity tests, publication rollback manifest.

**Failure exercise:** update an authoritative source after a summary is cached. Verify the freshness/version key invalidates the cache and the recommendation is re-evaluated.

## 9. Hands-on labs

Use a sandbox subscription and synthetic data. Record architecture, configuration versions, tests, traces, costs, failures, and cleanup. The deliverable matters more than a screenshot of a successful chat.

### Lab 1 — Architecture and trust boundaries

Decompose one business goal into deterministic stages and at least two justified agents. Produce a workflow diagram, typed handoff schemas, autonomy tier, identity/resource matrix, state-tier table, budgets, SLOs, threat model, and failure/recovery plan. Remove any agent that does not create a defensible boundary.

### Lab 2 — Agent Framework orchestration

Implement a sequential or orchestrator–subagent workflow plus one concurrent branch. Add typed results, correlation IDs, termination conditions, time/token/iteration budgets, checkpointing, and one human-intervention state. Simulate timeout and malformed output; prove resume and recovery.

### Lab 3 — Identity and tool authorization

Create two tools with different risk. Give each agent a distinct workload identity and minimum role/scope. Implement server-side parameter and ownership validation, preview for the write tool, approval, idempotency, Key Vault use for any unavoidable secret, and audit events. Demonstrate that a validly authenticated but unauthorized caller is denied.

### Lab 4 — Access-aware RAG and memory

Ingest two synthetic tenants with overlapping terminology. Preserve source, tenant, version, and deletion metadata. Enforce scope before retrieval, compare vector with hybrid retrieval, and require citations. Add session state and approved long-term memory. Test cross-tenant queries, deletion, stale facts, sliding-window amnesia, and summary drift.

### Lab 5 — MCP or governed integration

Expose a narrow synthetic API through an MCP server or API Management-backed MCP interface. Document server trust, authentication, capabilities, schemas, error taxonomy, timeout/retry, result validation, and versioning. Test invalid arguments, unauthorized access, prompt-like instructions in a tool result, transient failure, and duplicate write.

### Lab 6 — Evaluation and red-team suite

Build a versioned dataset covering normal, boundary, no-answer, unsafe, adversarial, multilingual, long-session, and tool-use cases. Evaluate prompt/model, retrieval, memory, tool, agent, workflow, and safety separately. Add calibrated human review and an LLM judge. Run authorized red-team cases and turn two findings into regression tests.

### Lab 7 — Trace, reliability, and cost operations

Instrument application, agents, model calls, retrieval, tools, and approval with correlated spans. Create a dashboard for success, latency, handoffs, errors, tokens, cost, quota, and loops. Redact sensitive fields. Inject throttling, stale retrieval, subagent timeout, and approval expiry; capture detection and runbook recovery.

### Lab 8 — CI/CD and controlled rollout

Package code, IaC, prompts, tool schemas, evaluation assets, guardrails, and dashboards. Build gates for lint/security, unit/integration tests, quality/safety/cost thresholds, and approval. Deploy a canary or blue-green version, pin in-flight state, smoke test, and roll back. Document what rollback cannot undo and the compensating action.

## 10. Knowledge checks

These are original concept checks, not recalled exam questions.

### Architect multi-agent solutions

1. A team proposes five agents because five departments supplied requirements. What evidence would justify five runtime agents?
2. Why should a durable business decision be stored outside conversation text?
3. When is concurrent orchestration better than sequential orchestration?
4. What must a handoff contain besides a natural-language message?
5. How does a per-agent identity reduce lateral movement?
6. Why is a large-context model not a complete memory strategy?
7. What is the difference between A2A and MCP in an architecture decision?
8. What observability can explain a route without logging hidden reasoning?
9. What makes a control loop operationally bounded?

### Develop multi-agent solutions

10. Why should retrieved content be separated from trusted instructions?
11. When is fine-tuning a poor choice for knowledge freshness?
12. What metadata makes an embedding safely governable?
13. Why must authorization occur before vector ranking in a multi-tenant index?
14. What distinguishes a retriable tool failure from a business rejection?
15. What risks remain after an API is published as an MCP tool?
16. When does semantic caching produce an unsafe answer?
17. What state must be revalidated after human approval?
18. Which concerns belong in middleware rather than agent prompts?

### Evaluate, optimize, and monitor

19. Why can a high end-to-end quality score conceal a retrieval defect?
20. How would you test sliding-window amnesia?
21. What is summary drift, and what evidence detects it?
22. Why should an LLM judge be calibrated against human review?
23. Which metric exposes an apparently cheap model that causes expensive retries?
24. Why test both elapsed duration and aggregate agent execution time?
25. What evidence distinguishes model latency from tool latency?
26. What should happen when a workflow reaches its iteration budget?
27. Why must a continuous-improvement pipeline retain a holdout set?

### Secure, govern, and deploy

28. When is on-behalf-of authentication appropriate?
29. Why does a private endpoint not replace authorization?
30. Where should an irreversible tool call be guarded?
31. What is the purpose of testing false positives as well as attack success?
32. Why is a prompt file a release artifact?
33. What can make a rollback incompatible with an in-flight workflow?
34. How does a canary differ from a shadow release?
35. What should an approval record contain?
36. Why can rolling back application code fail to reverse an incident?

## 11. Answers and reasoning

1. Separate agents should create measurable specialization, permission isolation, ownership, failure containment, scaling, parallelism, or review separation. Organization-chart symmetry alone is not evidence.
2. Conversation text is probabilistic context without transactional integrity, schema, stable ownership, or reliable recovery. A system of record should own the decision.
3. When tasks are independent, fan-out is bounded, downstream capacity supports it, and reduced wall time justifies additional cost and aggregation complexity.
4. A task/correlation ID, typed input and expected artifact, authorization scope, deadline, status/error semantics, provenance, and version.
5. A compromised agent can reach only its scoped resources/actions rather than inheriting broad coordinator permissions.
6. Context is temporary and size-limited; it does not provide lifecycle, tenant isolation, provenance, correction, deletion, or durable consistency.
7. MCP exposes tools/resources for discovery and invocation; A2A connects independently addressable agents with task/artifact/status semantics.
8. Structured route decisions, policy/rule identifiers, selected agent/tool, evidence references, correlation, and outcome—without private chain-of-thought.
9. Explicit state, completion/escalation conditions, iteration/time/token/tool budgets, retry categories, and recovery/compensation.
10. Untrusted content may contain instructions. Delimiting it as data helps preserve instruction precedence and supports injection defenses.
11. When facts change frequently. Retrieval or a tool keeps current knowledge external to model weights and easier to govern.
12. Source and version, tenant/user scope, classification, provenance, embedding/model version, timestamps/TTL, and deletion linkage.
13. Post-filtering can retrieve or expose unauthorized neighbors before they are discarded and may leak through traces or generated context.
14. A transient failure may be safely retried with policy and idempotency; a business rejection is a valid negative decision that usually requires changed input or escalation.
15. Server/software trust, identity, authorization, data handling, parameter/result validation, prompt injection, version change, availability, audit, and supply-chain risk.
16. When superficially similar requests differ in identity, tenant, freshness, policy, intent, or required side effects.
17. Approver authorization, proposal version, expiry, relevant business state, current policy, and whether execution is still safe and necessary.
18. Consistent correlation, authentication context, authorization enforcement, safe logging/redaction, timeout/retry, exception normalization, metrics, and common policy gates.
19. The generator can answer familiar test cases despite retrieving irrelevant or unauthorized evidence. Evaluate retrieval and citation separately.
20. Establish an early constraint, extend the session beyond normal context/compaction, and verify later actions against the typed source of truth.
21. Repeated summaries alter or omit meaning. Compare compacted state to checkpointed authoritative facts across long-session tests.
22. The judge has its own bias and model/prompt drift; human agreement tests show whether its scores are useful for this task.
23. Cost per successful business outcome, including retries, fallbacks, failures, and human correction—not cost per single model call.
24. Parallel execution can reduce elapsed time while increasing total compute/model work and cost; both reveal the tradeoff.
25. Correlated spans with separate model, retrieval, queue, and tool timings along the critical path.
26. Stop safely, preserve valid state, emit a clear termination reason, and escalate or return a bounded partial result according to policy.
27. A hidden set detects overfitting to visible evaluation cases and gives a more credible release comparison.
28. When a downstream resource must authorize an action as the signed-in user and the delegated scopes/policy support it.
29. Private networking controls reachability; an authenticated reachable workload can still be overprivileged without authorization.
30. At multiple layers: tool selection, parameter validation, server authorization/current-state policy, human approval where required, execution idempotency, and output/audit handling.
31. A control that blocks legitimate work can be operationally harmful. Measure both missed attacks and unnecessary blocks.
32. It changes system behavior and must be versioned, evaluated, approved, promoted, observed, and rolled back with the rest of the release.
33. State-schema, prompt/tool contract, agent/protocol, or model incompatibility between versions.
34. A canary serves real outcomes to a limited cohort; a shadow observes duplicated traffic but must not act or affect the user.
35. Authenticated approver, exact action/parameters, evidence, risk/policy, proposal version, time/expiry, decision, and resulting execution ID/outcome.
36. The prior version may already have written memory/state, changed an index/schema, or invoked an external side effect; compensation or data migration may be required.

## 12. Readiness checklist

You are approaching readiness when you can, without notes:

- map every official bullet to a design decision, implementation boundary, observable signal, and failure/recovery action;
- justify one agent versus several and select a topology from dependencies and control needs;
- design per-agent identities, tool permission boundaries, secure state tiers, and tenant-safe retrieval;
- explain MCP versus A2A and build typed, validated, failure-aware integrations;
- implement bounded Agent Framework/LangGraph-style orchestration with HITL and resume semantics;
- diagnose memory, retrieval, tool, agent, workflow, safety, performance, and cost failures separately;
- design evaluation and red-team suites with calibrated human evidence and regression gates;
- promote all behavioral artifacts through isolated environments with a gradual rollout and credible rollback;
- recognize **FOUNDRY (CLASSIC)** material and avoid mixing it with the current platform generation;
- confirm the live blueprint, beta status, and platform documentation immediately before the exam.

Microsoft’s [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-500/) currently says an official Practice Assessment is not available and is generally made available within eight weeks after an exam leaves beta. Do not substitute unverified “actual questions” or dumps. Use scenario explanation, labs, the blueprint, and reputable original practice items.

## 13. Primary references

- [Official AI-500 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500)
- [AI-500 exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-500/)
- [Microsoft Certified: Multi-Agent AI Solutions Expert (beta)](https://learn.microsoft.com/en-us/credentials/certifications/multi-agent-ai-solutions-expert/)
- [AI-500T00 course](https://learn.microsoft.com/en-us/training/courses/ai-500t00)
- [Microsoft Foundry overview](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
- [Agent Framework orchestration patterns](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/)
- [Agent Framework human-in-the-loop](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop)
- [Multiple-agent workflow architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/multiple-agent-workflow-automation)
- [Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points)
- [Foundry AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent)
- [API Management MCP overview](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview)
- [Foundry A2A endpoint](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/enable-agent-to-agent-endpoint)
- [Foundry agent identity concepts](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity)
- [Agent ID on-behalf-of flow](https://learn.microsoft.com/en-us/entra/agent-id/agent-on-behalf-of-oauth-flow)

## Places to learn

This is a curated starting point, not a complete list. Do **not** try to consume everything. Pick the explanation style, labs, and assessment signals that close your gaps; keep the current official blueprint beside every third-party resource.

| Resource | Access | Estimated time |
|---|---|---:|
| Four official Microsoft Learn paths | Public | About 14–17 hours plus exercises |
| AI-500T00-A instructor-led course | Provider/schedule dependent | 4 days; available September 30, 2026 |
| O'Reilly *Agentic AI with Microsoft Foundry* | Paid subscription | 8 hours 43 minutes provider reading estimate |
| O'Reilly *Hands-On Microsoft Foundry* | Paid subscription/event | About 4 instructional hours plus breaks per listed occurrence |
| Pluralsight *Building Intelligent Applications* | Paid subscription | 1 hour 2 minutes |
| Microsoft Foundry samples | Public | Select 4–12 hours by lab gap |
| Eight labs in this guide | Azure usage may cost money | About 12–24 hours |
| Udemy AI-500 practice tests | Paid | About 3–6 hours including review |

### Official foundation and labs

- [Architect production-grade multi-agent AI solutions](https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/) — 3 hours 21 minutes across four modules.
- [Build production-grade multi-agent capabilities in Microsoft Foundry](https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/) — 3 hours 48 minutes across four modules.
- [Deploy and govern agentic AI solutions on Azure](https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/) — 3 hours 14 minutes across four modules.
- [Monitor, evaluate, and operate multi-agent AI solutions](https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/) — five modules; Microsoft does not currently publish usable combined duration values, so allow about 4–6 hours plus lab time as a library planning estimate.
- [AI-500T00-A Designing and implementing multi-agent AI solutions](https://learn.microsoft.com/en-us/training/courses/ai-500t00) — four instructor-led days, listed as available September 30, 2026. This future course date is separate from the already-live beta exam.

The first three paths publish 10 hours 23 minutes combined. With the estimated fourth path, plan roughly 14–17 hours of reading/exercises before deeper labs. Add 12–24 hours to implement, break, observe, and explain the eight labs in this guide.

### Broader current-platform instruction

- [Agentic AI with Microsoft Foundry](https://www.oreilly.com/library/view/agentic-ai-with/9781806673957/) — O’Reilly book, April 2026, 360 pages, with a provider reading estimate of 8 hours 43 minutes. It spans MCP/tools, Azure Functions and Logic Apps, multi-agent patterns, evaluation/red teaming, deployment, security, and scaling; use the blueprint to check exact objective coverage.
- [Hands-On Microsoft Foundry](https://www.oreilly.com/live-events/hands-on-microsoft-foundry/0642572231088/0642572231071/) — O’Reilly live course by Razi Rais; about four hours of scheduled instruction plus breaks for one occurrence. Verify a current occurrence and schedule before enrolling.
- [Microsoft Foundry: Building Intelligent Applications](https://www.pluralsight.com/courses/microsoft-foundry-building-intelligent-applications) — Pluralsight, 1 hour 2 minutes, published February 2026. A short current-platform introduction to RAG, agents/workflows, evaluation, and guardrails; it is not a complete AI-500 path.
- [Microsoft Foundry samples](https://github.com/azure-ai-foundry/foundry-samples) — free official sample repository. Select examples that match the current SDK generation and a lab objective; examples can change faster than conceptual documentation.

No complete, current AI-500-specific Pluralsight path, Whizlabs course, MeasureUp practice test, or official Microsoft Practice Assessment was verified on September 1, 2026. That is a current catalog gap, not a claim that one will not appear after beta.

### Optional assessment supplement

- [Udemy AI-500 practice tests by Scott Duffy](https://www.udemy.com/course/ai500-tests/) — four tests of 25 questions (100 total), shown as updated August 2026. Allow about 3–6 hours for timed attempts plus explanation/source review. The listing is new and small, and its claim of an August 22 exam update is not corroborated by Microsoft’s study-guide page, which was last updated July 16 and publishes no separate skills-effective date. Use it only as a secondary readiness signal; resolve every conflict against Microsoft’s blueprint and documentation.

Avoid any provider that advertises leaked, “actual,” or memorized exam questions. Practice should measure whether you can reason from documented behavior, not whether you recognize protected exam content.
