---
exam_code: AI-500
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AI-500 Designing and Implementing Multi-Agent AI Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ai-500-coverage-record). The [official AI-500 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500) is authoritative.

**Current baseline:** Official study-guide page last updated July 16, 2026; Microsoft does not publish a separate skills-effective date on that page.<br>
**Exam state:** Beta, English only, as verified September 28, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
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

### Living-guide watch — September 28, 2026

Microsoft's [certification announcement](https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-multi-agent-ai-solutions-expert-certification/4494122) previously targeted October 2026 general availability without a day. Its direct page returned a content shell in this review; the month remains a historical announcement, not verified release completion. The current credential and exam pages still say **beta**. AI-103 remains the credential prerequisite, and no official Practice Assessment is available. The September 30 course date remains two days in the future. No fixed exam duration was verified.

The [hosted-agent migration guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-hosted-agent-preview) says support for the initial preview backend ended **August 20, 2026**, with no automatic migration. Older hosted-agent samples require an explicit migration review. This [deep-review report](../docs/research/2026-09-28-ai-500-deep-review.md) maps all 55 objectives and records six worked examples, ten labs, 44 answered checks, source limits and offline verification. No cloud lab, SDK deployment, model inference or paid question bank was executed or accessed.

### Current Microsoft Foundry versus older material

Unless explicitly marked **FOUNDRY (CLASSIC)**, this guide uses the current Microsoft Foundry resource/project model, current SDK/API generation, Responses-based agents, and current Agent Framework vocabulary. Older courses may say Azure AI Studio, Azure AI Foundry, hubs, `azure-ai-projects` 1.x, Assistants, threads, or runs. Those concepts can help with migration, but do not mix their resource model, SDK objects, endpoints, or portal steps into a current implementation. Use Microsoft’s [classic-to-current migration guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic) as the crosswalk.

Keep version axes separate: a training path's “v2/Responses” generation label, `azure-ai-projects` **2.3.0+**, a service **v1** API and A2A **1.0** are different things. The migration procedure describes current hosted agents as GA on v1; a package can still have a prerelease version. Record each version independently.

The classic migration page also records **August 26, 2026** retirement/sunset dates for `azure-ai-inference` and the Assistants API. Those dates have passed. Migrate to the documented `openai`/Responses path, verify region support, and validate the current endpoint; changing a package name alone does not migrate state or permissions.

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

For human–AI experience (HAX), show whether the system is drafting, waiting or acting, identify the exact proposed change and evidence, make rejection/edit/escalation accessible, and explain uncertainty in task terms. Preserve a correction route and a clear owner when automation stops. Evaluate whether people can detect a wrong proposal and recover without reconstructing an invisible agent conversation.

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

### Worked example 1 — Parallel latency still consumes shared capacity

Three independent calls take 6, 9 and 5 seconds. Their sequential call time is **20 seconds**; parallel calls followed by a 2-second aggregator take **11 seconds**, excluding queueing and startup. Aggregate call work remains 20 seconds, plus aggregation. At 30 workflows/minute and three calls each, demand is **90 calls/minute** against a synthetic 60-call/minute limit. The quota alone caps admission at **20 workflows/minute before retries**. If aggregation also calls that endpoint, count it too. Parallelism improves the critical path without creating quota.

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

[Azure API Management’s MCP support](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) exposes APIs as tools or proxies an existing server. Its current support is **tools only**, without MCP resources/prompts or workspaces. Check the listed supported tiers; Consumption is not listed. Gateway authentication and downstream authorization are separate, and server-level policies can affect all tool operations.

Current Foundry [incoming A2A support](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/enable-agent-to-agent-endpoint) distinguishes **GA v1.0** from **preview v0.3**. An unversioned request defaults to v0.3. Select 1.0 through the version-specific card/client negotiation or an explicit header/query selector; conflicting header and query versions produce an error. The documented v1.0 implementation uses JSON-RPC and text: do not assume streaming, files, gRPC or HTTP+JSON support from the general protocol.

Even agent-card discovery requires Entra authentication. Use the caller's principal object ID and a role such as **Foundry Agent Consumer** at the required agent/project scope; API keys and anonymous access are unsupported. Project scope covers more agents than a single-agent assignment. Tasks and contexts persist for **60 days after the latest write**, which resets that period; this is separate from a compute idle timeout.

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

### Recognize the current hosted-agent boundary

The current migration procedure gives each agent a dedicated Entra identity **when created/deployed**. Grant its downstream access to that identity; the project's managed identity still handles infrastructure duties such as image pulls. Older identity documentation explicitly describes a legacy Agent Application model with shared draft identity and a publication-time switch. Apply that section only to its stated model.

Replace old framework adapters with protocol libraries and the appropriate framework bridge. Current Agent Framework names include `Agent`, `FoundryChatClient`, `@tool` and `ResponsesHostServer`; confirm installed versions before adapting a sample. The hosted migration requires Projects SDK 2.3.0+ and `azd` 1.23.0+ with the agents extension. Configuration moves into `azure.yaml`; older standalone agent manifest files and manual start/stop/replica management do not carry over unchanged.

Each session has a sandbox; its persistent home/files storage survives idle periods. The default **15-minute compute idle timeout is not a data-deletion policy**. Bind invocation to the agent's dedicated endpoint, record the runtime version and identity, and separately test recovery, storage retention and access. Do not assume a successful redeployment migrated old checkpoints.

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

### Worked example 2 — Reserve space before adding context

For a synthetic 32,000-token window, budget 5,000 instructions, 18,000 retrieved evidence, 6,000 history, 2,000 tool results and 4,000 reserved output tokens. The total is **35,000**, leaving a **3,000-token deficit**. Select fewer passages or compact dispensable history before invoking the model; preserve exact IDs, approvals and authoritative state. A summary that fits but drops the approved amount is still wrong. These are planning numbers, not a tokenizer measurement or a specific model limit.

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

For every write, decide whether the item is eligible for memory, whose scope it belongs to, whether the user can inspect/correct/delete it, and when it expires. For every read, derive the scope from trusted identity and enforce it in the data service before results reach a model, caller or unsafe log. Return provenance. Server-side post-filtering can still enforce that scope; it has different recall behavior from pre-filtering. Filtering in application code after unauthorized content entered a prompt is a different, unsafe design.

[LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/durable-execution) separates thread checkpoints from a cross-thread store. An in-memory saver loses state with the process; production recovery needs a durable backend. A thread ID selects state and does not authenticate its owner. Build the storage key from authenticated tenant and subject, not a display name or client-supplied memory scope. Asynchronously extracted facts may appear after the next turn; test lag, correction and deletion across transcripts, derived facts, profiles and retrieval indexes.

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

### Worked example 3 — Filter mode changes recall, not who is authorized

[Azure AI Search filter modes](https://learn.microsoft.com/en-us/azure/search/vector-search-filters) differ: `preFilter` filters during traversal, `postFilter` filters shard candidates, and preview `strictPostFilter` filters the global top-k. The latter two can return fewer eligible neighbors or miss eligible matches. None lets a caller choose an unauthorized tenant filter.

Suppose a simplified global ranking is `B1, B2, B3, A1, A2`, the caller may read only tenant A, and `k=3`. Strict post-filtering returns **zero**; selecting within the authorized subset returns **A1 and A2**. This deterministic illustration explains the candidate-set problem; it does not execute Search's distributed HNSW algorithm. Avoid interpreting zero results as proof that no authorized answer exists. Separately test that `(tenant-A, subject-7)` and `(tenant-B, subject-7)` address different memory scopes, even if both users display “Alex.”

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

Use MCP when an existing component should expose tools/resources. Use A2A when it behaves as an independently addressable agent with task and artifact semantics. Put an adapter around older agents rather than leaking version-specific conversation objects throughout the new system. Test authentication, capability discovery, timeouts, supported cancellation/status operations, duplicate messages, malformed artifacts, and version mismatch. Test rejection or an explicit fallback for unsupported streaming rather than assuming Foundry implements it.

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

### Implement a model component behind the orchestration boundary

Use [Transformers pipelines](https://huggingface.co/docs/transformers/main_classes/pipelines) for a bounded classifier, extractor or generation component behind a typed application interface. Pin the task, model/tokenizer revision and package versions; record device, input/output limits and label mapping. `revision` can select a commit; `trust_remote_code=True` permits repository code execution and needs a separate code review. Batch size changes require measurement on representative lengths and hardware; padding or memory pressure can make larger batches worse.

For a specialist classifier, validate input, obtain scores, map only known labels to allowed routes, and escalate low-confidence or invalid results. Compare it with a baseline on held-out examples before substituting it for an agent. Local inference, fine-tuning and serving are separate responsibilities from orchestrating other agents. Lab 2 includes an optional implementation exercise; no model weights were downloaded in this review.

### Make human intervention a workflow state

Store an approval request containing the exact proposed operation, parameters, evidence, risk reason, expiry, and required approver role. On resume:

1. authenticate and authorize the approver;
2. verify the workflow and proposal have not changed;
3. re-check relevant business state and policy;
4. execute with an idempotency key;
5. record the decision and outcome;
6. route rejection, edit, expiry, or edge case explicitly.

[LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) resume the interrupted node from its beginning. Work before the interrupt can run again. Preserve stable interrupt ordering and serializable payloads, and avoid swallowing the interrupt in a broad exception handler. Put approval and effects into explicit stages; even an effect after approval can repeat if a later failure causes replay. Checkpointing alone does not provide exactly-once external writes.

### Worked example 4 — Retry after an effect but before acknowledgement

The original Python example below models an external service retaining a deduplication ledger while a caller retries. It performs no network or file writes. The ledger is **in memory in one process**, so this is a replay thought experiment, not crash-durable production code. In a real service, atomically persist the key, payload and outcome with the effect, enforce uniqueness under concurrency, and define key retention/reconciliation. Approval and authentication happen separately.

```python
class FakeActionService:
    def __init__(self):
        self.ledger = {}
        self.effects = []

    def apply(self, key, payload):
        if key in self.ledger:
            saved_payload, receipt = self.ledger[key]
            if saved_payload != payload:
                raise ValueError("Key reused for a different proposal")
            return receipt
        receipt = f"effect-{len(self.effects) + 1}"
        self.effects.append((key, payload))
        self.ledger[key] = (payload, receipt)
        return receipt


service = FakeActionService()
key = ("tenant-A", "workflow-12", "step-3", "proposal-v1")
payload = ("prepare-ticket", "case-7")  # Immutable synthetic data.
receipt = service.apply(key, payload)
assert receipt == "effect-1"
# Imagine the caller lost the acknowledgement and retries the same request.
assert service.apply(key, payload) == receipt and len(service.effects) == 1
conflict_rejected = False
try:
    service.apply(key, ("prepare-ticket", "different-case"))
except ValueError:
    conflict_rejected = True
assert conflict_rejected
other_key = ("tenant-B", "workflow-12", "step-3", "proposal-v1")
assert service.apply(other_key, payload) == "effect-2" and len(service.effects) == 2
```

The outcome is one effect for tenant A despite retry, a rejected changed proposal, and a separate tenant B effect. A local workflow checkpoint is not the external service's ledger. If a downstream system has no atomic deduplication capability, choose reconciliation or compensation and describe its limits.

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

Choose the evaluation target deliberately: the current portal supports agent/model runs as well as datasets containing existing outputs. Dataset evaluation can score stored results without rerunning the agent; it therefore cannot prove current tool authorization or deployment behavior. Review full conversations for continuity and individual turns for a localized defect, and retain human calibration for subjective judgments.

### Worked example 5 — An overall pass hides a critical failure

A synthetic suite contains 900 routine cases, with 891 passing, and 100 critical cases, with 60 passing. Overall success is **951/1,000 = 95.1%**, but the critical slice is **60%**. A release requiring at least 95% overall and 90% on critical cases **fails**. These thresholds are an exercise policy. Preserve counts and severity slices; a run that completes without an exception may still produce the wrong action.

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

The dashboard reads the project's connected Application Insights resource; log views also require workspace access. Its run-success metric records completion and does not establish correctness. Recurring evaluations, red-team scans and alerts are marked preview in the current procedure. Retention/billing follow Application Insights settings; do not infer them from agent conversation retention or treat illustrative latency/success advice as a platform SLA.

### Worked example 6 — Compare cost per valid outcome

Candidate A consumes 50 synthetic cost units and delivers 45 valid outcomes; B consumes 30 units and delivers 20. A costs **1.11 units per valid outcome** and B **1.50**, rounded to two decimals. B spends less overall while costing more per useful result. Include failed runs, retries and attributable human correction consistently, and compare equivalent workloads and quality gates before choosing. These units are not Azure prices.

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

Tool-call and tool-response intervention points are **preview and tool-dependent**. The current list includes Azure AI Search, Azure Functions, OpenAPI, SharePoint Grounding, Fabric Data Agent, Bing Grounding, Bing Custom Search and Browser Automation. For tools outside that list, configured controls at those points **do not take effect**. A generic MCP tool is not automatically covered. Record the actual tool path, support status, blocking versus annotation, failure behavior and independent application/server checks.

Build custom guardrails for domain policy such as prohibited transactions, regulated claims, tenant rules, or required evidence. Generate synthetic normal, edge, adversarial, multilingual, obfuscated, and tool-mediated cases; measure false positives and false negatives. Do not tune only until the test set passes.

### Shift left with adversarial testing

Use the Foundry [AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) as one testing capability, not a guarantee of safety. Include direct/indirect prompt injection, data exfiltration, tool misuse, privilege escalation, cross-tenant access, poisoned memory, denial-of-wallet loops, unsafe output, and evasion attempts. Run only in authorized scope with safe targets and protected test data. Convert important findings into regression tests and verify the mitigation does not break legitimate behavior.

The current red-team agent supports text-based testing. Its agent-target matrix includes supported Foundry prompt/hosted-container agents but excludes workflow and non-Foundry agent targets; documented tool limitations include function tools, non-Azure tools, Browser Automation, connected agents and computer use. This is a different matrix from guardrail moderation support. Agent-specific risk scans run in the cloud; synthetic/mock tool data does not make a target a fully isolated sandbox. Plan separate controlled tests for unsupported paths and report them as untested until run. Attack-success rate describes the tested attacks, not every possible attack or production safety.

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

Start with offline diagrams, synthetic data and mocks; use a separately authorized sandbox subscription for cloud steps, which can incur charges. Record architecture, configuration versions, tests, traces, costs, failures, and cleanup. Only the standard-library replay example and arithmetic/set checks were executed for this review; all cloud/framework/model steps below are proposed learner exercises.

### Lab 1 — Architecture and trust boundaries

Decompose one business goal into deterministic stages and at least two justified agents. Produce a workflow diagram, typed handoff schemas, autonomy tier, identity/resource matrix, state-tier table, budgets, SLOs, threat model, and failure/recovery plan. Remove any agent that does not create a defensible boundary.

### Lab 2 — Agent Framework orchestration

Implement a sequential or orchestrator–subagent workflow plus one concurrent branch. Add typed results, correlation IDs, termination conditions, time/token/iteration budgets, checkpointing, and one human-intervention state. Simulate timeout and malformed output; prove resume and recovery. Optionally implement a Transformers-backed specialist with pinned model/tokenizer revisions, bounded input, label validation and abstention. Compare against a simple baseline, record hardware/batching behavior, and keep any weight download or remote-code decision explicit.

### Lab 3 — Identity and tool authorization

Create two tools with different risk. Give each agent a distinct workload identity and minimum role/scope. Implement server-side parameter and ownership validation, preview for the write tool, approval, idempotency, Key Vault use for any unavoidable secret, and audit events. Demonstrate that a validly authenticated but unauthorized caller is denied.

### Lab 4 — Access-aware RAG and memory

Ingest two synthetic tenants with overlapping terminology. Preserve source, tenant, version, and deletion metadata. Enforce trusted scope in the retrieval service, compare pre/post/strict-post filter recall where supported, compare vector with hybrid retrieval, and require citations. Add session state and approved long-term memory. Test cross-tenant queries, deletion, stale facts, sliding-window amnesia, and summary drift.

### Lab 5 — MCP or governed integration

Expose a narrow synthetic API through an MCP server or API Management-backed MCP interface. Document server trust, authentication, capabilities, schemas, error taxonomy, timeout/retry, result validation, and versioning. Test invalid arguments, unauthorized access, prompt-like instructions in a tool result, transient failure, and duplicate write.

### Lab 6 — Evaluation and red-team suite

Build a versioned dataset covering normal, boundary, no-answer, unsafe, adversarial, multilingual, long-session, and tool-use cases. Evaluate prompt/model, retrieval, memory, tool, agent, workflow, and safety separately. Add calibrated human review and an LLM judge. Record which target/tool combinations the selected red-team service supports. Run only authorized cases, cover unsupported combinations separately, and turn two findings into regression tests. An unsupported or skipped case must not appear as a passed case.

### Lab 7 — Trace, reliability, and cost operations

Instrument application, agents, model calls, retrieval, tools, and approval with correlated spans. Create a dashboard for success, latency, handoffs, errors, tokens, cost, quota, and loops. Redact sensitive fields. Inject throttling, stale retrieval, subagent timeout, and approval expiry; capture detection and runbook recovery.

### Lab 8 — CI/CD and controlled rollout

Package code, IaC, prompts, tool schemas, evaluation assets, guardrails, and dashboards. Build gates for lint/security, unit/integration tests, quality/safety/cost thresholds, and approval. Deploy a canary or blue-green version, pin in-flight state, smoke test, and roll back. Document what rollback cannot undo and the compensating action.

### Lab 9 — Recovery after lost acknowledgement

Run worked example 4 locally. Draw two durable systems: workflow checkpoint store and external action ledger. Place a failure after the effect and before acknowledgement, then after acknowledgement but before workflow checkpoint. Explain which requests replay and who suppresses duplicate effects. Test changed proposal versions, expired approvals and different tenants. For an eventual framework implementation, use a durable checkpointer and verify interrupt/restart semantics with synthetic tools; an in-memory demonstration does not pass that deployment test.

### Lab 10 — Capability and memory evidence matrix

List each MCP/A2A/tool path, version, identity, scope, guardrail coverage, red-team support, retention and test result. Include an unversioned A2A call, conflicting selectors, an unsupported moderation tool, a completed-but-wrong run and two tenants sharing a display name. Add delayed memory extraction, corrected facts, deletion and process restart. Mark offline expectations separately from observed product behavior. Use the two blog exercises below to choose additional failure cases, then identify every unexecuted or unsupported cell.

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
13. How do server-side post-filtering and unsafe application-side filtering differ, and what recall problem can post-filtering introduce?
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

### Current implementation and evidence boundaries

37. Why can an unversioned A2A request still use a preview protocol when v1.0 is GA?
38. Which identity needs downstream access after migration to current hosted agents?
39. Why does a 15-minute idle timeout not prove memory deletion?
40. What can repeat when a LangGraph node resumes after an interrupt?
41. Why can a configured tool-response guardrail fail to inspect a tool's output?
42. Does a successful red-team scan cover every workflow and tool?
43. Why can 95.1% overall evaluation success fail a release gate?
44. What must accompany a memory-provider `user_id` or a workflow `thread_id` to enforce isolation?

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
13. Search can apply a trusted authorization filter server-side after candidate selection and still return only permitted documents; small candidate sets can miss eligible matches. Application filtering after unauthorized evidence reaches prompts/logs is unsafe. Derive filters from trusted identity and test both isolation and recall.
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

37. Foundry defaults requests without a version selector to v0.3. Select v1.0 explicitly or verify card-driven client negotiation; matching header/query values are required when both are present.
38. The dedicated Entra agent identity created at deployment, with the required resource roles. The project managed identity still has separate infrastructure responsibilities; legacy publication-switch instructions have narrower scope.
39. Compute can stop while session files persist. Storage retention/deletion, conversation retention and memory lifecycle need separate policies and evidence.
40. The node restarts from its beginning, so preceding work can repeat. Later failures can also replay effects; use appropriately durable, atomic external idempotency or reconciliation, not checkpoint assumptions.
41. Tool-call/response moderation only applies to supported tools. An enabled policy or annotation does not establish blocking for an unsupported path.
42. No. Record the target/tool support matrix and tested attacks. Unsupported paths and unexecuted scenarios remain coverage gaps; synthetic data is not a complete sandbox boundary.
43. A high-volume routine slice can hide a critical slice's failure: 60% critical success fails the example's 90% critical threshold despite the overall score.
44. An authenticated tenant/subject binding, server-side authorization and scoped storage/query enforcement. A caller-supplied string or display name alone is not proof of identity.

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
| Four official Microsoft Learn paths | Public | 17 modules; allow 14–20 hours as a planning estimate |
| AI-500T00-A instructor-led course | Provider/schedule dependent | 4 days; available September 30, 2026 |
| O'Reilly *Agentic AI with Microsoft Foundry* | Paid subscription | Earlier 8h 43m estimate; current listing access-blocked |
| O'Reilly *Hands-On Microsoft Foundry* | Paid subscription/event | About 4 instructional hours plus breaks per listed occurrence |
| Pluralsight *Building Intelligent Applications* | Paid subscription | 1 hour 2 minutes |
| Microsoft Foundry samples | Public | Select 4–12 hours by lab gap |
| Ten labs in this guide | Offline starts; cloud steps may incur charges | About 16–30 hours, editorial estimate |
| Two Microsoft engineering blog exercises | Public | 45–75 minutes each, editorial estimate |
| Udemy AI-500 practice tests | Paid | About 3–6 hours including review |

### Official foundation and labs

- [Architect production-grade multi-agent AI solutions](https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/) — four modules; the previously recorded 3h 21m total was not exposed in this fetch.
- [Build production-grade multi-agent capabilities in Microsoft Foundry](https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/) — four modules; the previously recorded 3h 48m total was not exposed in this fetch.
- [Deploy and govern agentic AI solutions on Azure](https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/) — four modules; the previously recorded 3h 14m total was not exposed in this fetch.
- [Monitor, evaluate, and operate multi-agent AI solutions](https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/) — five modules; Microsoft does not currently publish usable combined duration values, so allow about 4–6 hours plus lab time as a library planning estimate.
- [AI-500T00-A Designing and implementing multi-agent AI solutions](https://learn.microsoft.com/en-us/training/courses/ai-500t00) — four instructor-led days, listed as available September 30, 2026. This future course date is separate from the already-live beta exam.

The current paths expose **4 + 4 + 4 + 5 = 17 modules**. The former first-three total of 10h 23m is historical, not a current verified runtime. Allow roughly 14–20 hours for path study and 16–30 hours for the ten labs as editorial planning estimates; adapt to your prerequisites and cloud access.

### Broader current-platform instruction

- [Agentic AI with Microsoft Foundry](https://www.oreilly.com/library/view/agentic-ai-with/9781806673957/) — previously cataloged as an April 2026, 360-page book with an 8h 43m reading estimate. The direct listing was access-blocked on September 28; current edition details and paid content were not verified. Check SDK generation and objective coverage before relying on it.
- [Hands-On Microsoft Foundry](https://www.oreilly.com/live-events/hands-on-microsoft-foundry/0642572231088/0642572231071/) — O’Reilly live course by Razi Rais. The public outline contains four 55-minute blocks plus 20 minutes, totaling four instructional hours before breaks, covering agents, memory, integrations and deployment. No current occurrence date or live teaching was verified; check availability before enrolling.
- [Building Intelligent Applications with Microsoft Foundry](https://www.pluralsight.com/courses/microsoft-foundry-building-intelligent-applications) — Pluralsight, Clint Bonnett, 1h 02m, published February 13, 2026; public syllabus inspected, paid lessons not viewed. A short current-platform introduction to RAG, agents/workflows, evaluation, and guardrails; it is not a complete AI-500 path.
- [Microsoft Foundry samples](https://github.com/azure-ai-foundry/foundry-samples) — free official sample repository. Select examples that match the current SDK generation and a lab objective; examples can change faster than conceptual documentation.

No complete, current AI-500-specific Pluralsight path, Whizlabs course, MeasureUp practice test, or official Microsoft Practice Assessment was verified on September 28, 2026. These bounded public searches do not prove absence. Recheck after the course date and beta transition.

### Optional assessment supplement

- [Udemy AI-500 practice tests by Scott Duffy](https://www.udemy.com/course/ai500-tests/) — the public search index advertises four tests of 25 questions (100 total) and an August 2026 update. Direct retrieval was access-blocked; question quality, originality and coverage were not inspected. Allow about 3–6 hours as an editorial attempt/review estimate. The seller’s August 22 exam-update claim remains uncorroborated by Microsoft’s July 16 page, which publishes no separate skills-effective date. Use it only as a secondary readiness signal; resolve every conflict against Microsoft’s blueprint and documentation.

Avoid any provider that advertises leaked, “actual,” or memorized exam questions. Practice should measure whether you can reason from documented behavior, not whether you recognize protected exam content.


### Useful engineering blogs and focused exercises

- [Interactive experiences, memory, and resilient execution](https://devblogs.microsoft.com/agent-framework/interactive-experiences-memory-and-resilient-execution/) — Dan Taylor, September 24, 2026. Read the resilient-hosting section and sketch how response IDs, checkpoint state and stable executor IDs survive a restart. Use Lab 9 to place the lost-acknowledgement failure. The article explicitly leaves external-effect idempotency to the application. Its memory discussion also distinguishes async extraction from immediate availability. Language/runtime features differ; do not assume sample parity or copy a toy approval policy into a consequential tool. Allow 45–75 minutes for the worksheet, not a verified SDK runtime.
- [Native Agent Memory for Microsoft Agent Framework, powered by Azure Cosmos DB](https://devblogs.microsoft.com/cosmosdb/native-agent-memory-for-microsoft-agent-framework-powered-by-azure-cosmos-db/) — Theo van Kraay, July 24, 2026. Treat the Python memory provider as a preview integration. Draw where turns become facts/profiles, then test delayed visibility, correction, deletion and two-tenant isolation. Derive memory scope from authenticated identity. A clean async shutdown draining work does not prove crash recovery, and a retrieved profile is context rather than authorization. If customizing extraction prompts, preserve their schema and evaluate the resulting memory. Allow 45–75 minutes for the design exercise; no Cosmos DB resource or package was executed here.

Both main articles were read. Their code, videos, benchmark claims and deployment behavior were not independently reproduced; the exercises are original learning tasks grounded in the documented boundaries.
