---
exam_code: AB-620
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-620
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# AB-620 Designing and Building Integrated AI Agent Solutions in Copilot Studio Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-620-coverage-record). The [official AB-620 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-620) is authoritative.

**Current baseline:** Official study-guide page last updated April 21, 2026; Microsoft does not publish a separate skills-effective date on that page.<br>
**Exam state:** Active (no longer labeled beta on the credential page) as verified September 1, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Training availability:** The three official self-paced paths are live; the separate three-day AB-620T00-A instructor-led course is listed as available September 18, 2026.<br>
**Official source:** [AB-620 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-620)

## How to use this guide

AB-620 sits between advanced low-code building and professional integration. Study each objective as a complete production path:

```text
audience and outcome
  → channel, identity, environment, and governance boundary
  → instructions, topics, knowledge, tools, and agents
  → deterministic flow or generative orchestration
  → evaluation, telemetry, solution packaging, and promotion
```

Read Sections 1–7, implement the eight labs, and explain the three scenarios without referring to portal screenshots. Use the official blueprint as the coverage checklist. Product navigation, licensing, limits, preview status, and experience names change; understand the object and dependency model beneath the UI.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Exam profile and objective map

The target candidate is a professional developer or advanced builder who integrates enterprise agents. Expected prerequisites include Power Fx, Dataverse, Power Platform environments and solutions, Microsoft 365 Copilot, Microsoft Foundry, Adaptive Cards, RAG, MCP, A2A, prompt engineering, REST APIs, and basic Copilot Studio agents with instructions, knowledge, tools, and topics.

| Official domain | Weight | Central question |
|---|---:|---|
| Plan and configure agent solutions | 30–35% | How should audience, identity, governance, flows, topics, responses, state, and tools fit together? |
| Integrate and extend agents in Copilot Studio | 40–45% | Which knowledge, connector, API, MCP, computer-use, multi-agent, Fabric, Foundry, and Azure integration is appropriate? |
| Test and manage agents | 20–25% | How are quality, telemetry, solution dependencies, configuration, and controlled promotion managed? |

### Complete objective-to-guide map

| Published objective area | Primary coverage | Practice evidence |
|---|---|---|
| Plan enterprise integration, identity, channels, deployment, responsible AI, security/governance, reusable components, and internal/external audience design | Sections 1–2 | All scenarios; Labs 1–2 |
| Create and monitor agent flows with HITL, connectors, inputs/outputs, and error handling | Section 3 | Scenarios 1 and 3; Labs 2–3 |
| Configure topics, formatting, tools, prompts, knowledge, HTTP, generative answers, Adaptive Cards, and variables | Section 3 | All scenarios; Labs 2–3 |
| Connect Copilot/Power Platform connectors, Azure AI Search, computer use, MCP, custom connectors, and REST APIs | Section 4 | Scenarios 1–2; Labs 4–5 |
| Design multi-agent collaboration with child, connected, Foundry, Fabric, and A2A agents | Section 5 | Scenarios 2–3; Lab 6 |
| Configure Azure AI Search with Foundry, Foundry model-catalog prompts, and Application Insights monitoring | Sections 4–6 | Scenarios 2–3; Labs 4 and 7 |
| Create test sets, select evaluation methods, and review results | Section 6 | All scenarios; Lab 7 |
| Package agents in solutions, use environment variables, and implement/extend Power Platform Pipelines | Section 7 | All scenarios; Lab 8 |

## 1. Establish the correct Copilot Studio experience

### The current platform has two authoring experiences

Microsoft’s official AB-620 learning paths currently say their modules are based on the **classic experience**, while Microsoft also has a **new agent experience** in production-ready preview. This matters because the objective list explicitly includes topics, nodes, agent flows, variables, and Adaptive Cards—the classic authoring model.

| Signal | Classic experience | New agent experience (preview) |
|---|---|---|
| Primary control | Topic canvas, triggers, nodes, branches; classic or generative orchestration | Instructions and reasoning in a consolidated agent surface |
| Component navigation | Separate topics, knowledge, tools/actions, agents, settings | Identity, knowledge, tools, skills, and settings together |
| Deterministic conversation | Mature explicit topic flow | No explicit topic-flow equivalent for every step |
| Evaluation/monitoring | Existing evaluation and analytics surfaces | Integrated Evaluate and Monitor tabs |
| Conversion | Existing classic agents remain classic | No migration/conversion path to or from classic |

Use the [classic-versus-new experience page](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/classic-vs-new) to identify the surface before following steps. **VERIFY CURRENT:** the new experience, new workflows, features, and navigation are volatile. For AB-620’s published topic objectives, practice in the classic experience even if you also explore the new one.

> **Related item:** “Classic” here names the Copilot Studio authoring experience. It is separate from Microsoft Foundry’s classic-versus-current resource/API generations. A connected Foundry agent must also be checked for its own platform generation.

### Build an architecture contract before a canvas

Use Microsoft’s [Copilot Studio architecture overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/architecture-overview) as a component map, then capture workload-specific decisions.

| Decision | Questions | Evidence |
|---|---|---|
| Outcome and audience | What job is completed? Internal employee, known customer, anonymous visitor, or background process? | Success criteria, exclusions, personas |
| Channel | Teams, Microsoft 365 Copilot, SharePoint, web, mobile/custom app, or autonomous trigger? | Channel/authentication compatibility matrix |
| Orchestration | Generative selection, deterministic topic, agent flow, or a combination? | Conversation and action diagrams |
| Grounding | Which sources, whose permissions, how current, what citation/fallback behavior? | Knowledge inventory and access tests |
| Actions | Connector, flow, REST API, MCP, computer use, or another agent? | Integration decision and permission matrix |
| State | Which variables are turn/topic/global/user state, flow data, Dataverse data, or system-of-record state? | Typed data contract and lifecycle |
| Security | Who authenticates, whose connection executes, what data crosses boundaries? | Identity/data-flow/threat model |
| Quality | What must be correct, grounded, safe, fast, and available? | Test sets, thresholds, human review plan |
| Delivery | Which components/configuration are promoted together? | Solution/dependency manifest and pipeline |

Do not use generative behavior for a step merely because an agent is involved. Use explicit topics or flows for regulated wording, required questions, deterministic validation, approvals, or transactional sequencing. Use generative orchestration where flexible intent recognition, knowledge synthesis, or selection among well-described capabilities adds value.

## 2. Plan identity, channels, governance, and reusable components

### Plan enterprise integration as trust boundaries

For each dependency, record:

- source/target system and data classification;
- read versus write and reversibility;
- user-delegated versus maker/workload identity;
- connector/API/MCP/agent protocol and network path;
- authorization enforcement point;
- retry, timeout, idempotency, and compensation;
- telemetry, ownership, SLA, and failure route;
- environment-specific endpoint, connection reference, and secret/configuration.

Separate **knowledge** from **tools**. Knowledge grounds an answer; a tool retrieves live data or performs an operation. The same system might be used through either path, but their access, freshness, output, and testing semantics differ.

### Choose the identity strategy before building tools

[Copilot Studio user authentication](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication) determines whether the user is anonymous, authenticated by Microsoft, or authenticated manually through Entra ID or another OAuth 2.0 provider. Authentication changes take effect after publishing.

Then choose each tool’s effective identity:

| Identity path | Use when | Primary risk/control |
|---|---|---|
| End-user connection | Access and action must follow each user’s downstream permissions | Require sign-in; test users with different privileges; handle consent |
| Maker-provided connection | Shared service operation is intentionally performed under a controlled maker/service connection | Avoid personal maker accounts; scope privilege; govern use; rotate and monitor |
| Service principal/workload identity behind API | Application owns a bounded integration | Least-privilege app permissions; credentialless/federated auth where possible |
| Manual OAuth token in topic | A channel/provider requires explicit OAuth flow | Protect token variables; validate scopes/audience; do not log tokens |

Microsoft’s [automatic security scan](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-scan) warns about no authentication, maker-provided credentials, and organization-wide sharing. A warning is not a security design. Administrators can also [restrict maker-provided credentials](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication).

> **Related item:** User authentication, agent sharing, connector identity, data-source authorization, and channel transport security are separate gates. Passing one does not imply the others.

### Design channels and deployment together

An agent is published before it is made available through selected channels. Microsoft’s [channel guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/channels) includes Teams, Microsoft 365 Copilot, SharePoint, Power Pages, and custom clients/Direct Line.

For every channel test:

- supported authentication mode and user identity variables;
- who can discover/use the agent;
- Adaptive Card schema and rendering differences;
- file, rich media, citation, and conversation behavior;
- handoff/escalation support;
- locale, accessibility, and client constraints;
- transcript/telemetry and data-location implications;
- rate, capacity, licensing, and support ownership.

For web/Direct Line clients, [web channel security](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security) can require secrets or tokens. Never embed a Direct Line secret in browser/mobile code; exchange it server-side for a bounded token. **VERIFY CURRENT:** security-setting propagation and channel features can change.

### Plan responsible AI and governance as lifecycle controls

Use a risk register spanning instructions, user input, knowledge, tool arguments, tool results, connected agents, final responses, autonomous triggers, computer use, and telemetry. Controls include purpose/scope, authentication, least privilege, data policies, content/safety controls, grounding/citations, approval/handoff, evaluation, monitoring, and incident response.

Power Platform environments are the isolation and lifecycle boundary for Copilot Studio. Microsoft’s [zoned governance strategy](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2) applies different environment/data/channel/feature controls according to risk. Align:

- personal/productivity experimentation;
- team/department shared agents;
- enterprise production agents;
- external/public or high-impact agents.

Use security groups, roles, data policies, approved connectors, maker restrictions, channel controls, publishing approval, tenant settings, Purview/Microsoft 365 controls, inventory, and monitoring in proportion to the zone.

### Plan reusable components

Reuse can reduce drift but expands blast radius. Candidates include agent flows, prompts, custom connectors, REST tools, MCP servers, knowledge integrations, child/connected agents, Adaptive Card schemas, topics, and evaluation sets.

Define the component’s owner, supported inputs/outputs, authentication assumptions, data classifications, version policy, consumers, environment dependencies, tests, and deprecation process. A shared tool’s wrapper can be configured differently per agent; test both the underlying component and each agent-specific description/mapping.

> **Related item:** A reusable component is a product. Treat schema/tool-description changes as contracts because generative orchestration uses metadata to decide whether and how to invoke it.

## 3. Implement agent flows, topics, responses, and state

### Create bounded agent flows

An agent flow is appropriate for repeatable multistep work, transformations, approvals, and integrations. Define typed inputs and outputs from the start. Each input should have a name, type, requirement, validation rule, and safe default; each output should be meaningful to the calling topic/agent.

```text
agent/topic
  → validated flow inputs
  → connector/API/business steps
  → success | known business rejection | transient failure | escalation
  → typed result and safe diagnostic
```

Configure connection references rather than embedding environment-specific connections. Handle nulls, schema mismatch, downstream rejection, timeout, throttling, duplicate invocation, and partial completion. Do not return secrets or raw stack traces to the agent.

Human-in-the-loop flows should preserve the exact proposal, evidence, approver identity/role, expiry, decision, and final execution. Revalidate business state after approval. Use idempotency for retried writes and compensation when a partially completed flow cannot be rolled back transactionally.

Monitor run success, duration, retry/throttle patterns, connector errors, approval wait/expiry, input/output validation, and business outcomes. A healthy flow run can still produce a poor agent result if tool descriptions or output mapping are wrong.

### Use topics for explicit conversational control

A topic contains triggers and nodes representing part of the conversation. Use it when you need deterministic routing, required questions, validation, a specific tool/flow call, structured escalation, or channel-specific output.

A robust topic:

1. has narrow trigger intent and avoids overlap;
2. validates required inputs and clarifies ambiguity;
3. uses typed variables with deliberate scope;
4. calls tools/flows with explicit mappings;
5. handles success, rejection, no result, timeout, and failure;
6. formats a channel-appropriate response;
7. ends, redirects, or escalates explicitly;
8. produces traceable outcome data.

Tools may be available to generative orchestration at agent level or called explicitly from a topic. Explicit calls give sequence control; generative selection gives flexibility. Do not combine both accidentally and create duplicate side effects.

### Design response formatting and Adaptive Cards

Use Markdown/plain text for portable information and Adaptive Cards for structured presentation or input. Define card version, supported host/channel features, fallback, validation, accessibility labels, button/action behavior, and how submitted values map to variables. Test every target client; host rendering and supported schema features differ.

Never treat client validation as the authorization boundary. Validate submitted IDs/choices server-side, bind them to the current user and proposal, and re-check state before a write.

### Use custom prompts and knowledge inside topics

A custom prompt should state task, trusted instructions, input fields, evidence, output contract, safety constraints, and failure behavior. Select a Foundry catalog model only after evaluating quality, modality, latency, availability, and cost. Version prompts and model/deployment configuration with solution artifacts.

The generative answers node can use topic-scoped knowledge and custom data. Topic knowledge takes priority, while broader agent knowledge may act as fallback. This can intentionally narrow answers for a process, but it can also create confusing source precedence. Test expected source use and no-answer behavior.

Use the HTTP request node for a bounded call when appropriate, but design authentication, headers, parameter validation, response schema, timeout, retry, error branches, and sensitive-data handling. For reusable or governed APIs, a REST tool, connector, or MCP layer can provide a stronger lifecycle boundary.

### Manage variables as application state

Know the scope and owner of each value:

| State | Appropriate use | Avoid |
|---|---|---|
| Node/topic variable | Local collection and calculation | Assuming another topic can read it without mapping |
| Global/agent variable | Conversation-wide context | Durable business record or secret storage |
| System/user variable | Channel, activity, authenticated-user context | Assuming every authentication mode exposes the same token fields |
| Flow input/output | Typed integration contract | Passing an unvalidated free-form object |
| Environment variable | Endpoint/configuration that differs by environment | Per-user or changing transaction state |
| Dataverse/system of record | Durable governed business data | Temporary conversational detail without retention need |

Use Power Fx for calculations, conditions, records, tables, string handling, and mappings. Handle blank/error/type conversion explicitly. Names should communicate scope and purpose.

> **Related item:** Conversation variables are convenient state, not a transactional database. If a decision must survive restart, support concurrent updates, or be audited, write it to a governed system of record.

## 4. Connect knowledge and tool ecosystems

### Choose the integration pattern from the job

[Copilot Studio’s tool catalog](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent) includes connectors, agent flows, prompts, REST APIs, MCP, and computer use.

| Need | Likely choice | Important boundary |
|---|---|---|
| Existing supported service action | Prebuilt Power Platform connector | Connection identity, data policy, operation limits |
| Organization-specific API reused across Power Platform | Custom connector | OpenAPI/action schema, certification/sharing, auth lifecycle |
| Direct bounded API exposed to one agent | REST API tool | OpenAPI correctness, auth, server-side validation |
| Multi-step deterministic automation or approval | Agent flow | Inputs/outputs, connection refs, errors, idempotency |
| Standardized discoverable tools/resources used by agents | MCP server | Server trust, tool selection, OAuth/API key, version/data policy |
| No suitable API; GUI task | Computer use | Dedicated machine/account, supervision, visual uncertainty, cost |
| Flexible knowledge synthesis | Knowledge source/RAG | authorization, freshness, relevance, citations |
| Specialized reasoning/data domain | Child or connected agent | delegation contract, identity, quality, observability |

The least complex option meeting security, reuse, and lifecycle requirements is usually best.

### Connect enterprise knowledge safely

Distinguish three broad patterns:

- **Copilot connectors/indexed enterprise content:** ingestion produces searchable content; plan crawl, schema, permissions, freshness, deletion, and index governance.
- **Power Platform connector real-time knowledge:** query the source at request time under configured connection behavior; plan latency, availability, user sign-in, and result shape.
- **Azure AI Search:** retrieve from a configured vector/search index; plan index pipeline, chunking, metadata, authorization, freshness, relevance, and citations.

Microsoft’s [Copilot Studio RAG guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/retrieval-augmented-generation) warns that Azure AI Search integration is not automatically user-delegated security trimming. Enforce allowed content in index design/query architecture; do not assume the end user’s source permissions are applied.

For a custom search endpoint, the [custom knowledge-source pattern](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/custom-knowledge-sources) uses `OnKnowledgeRequested` and expects result fields such as content, location, and title. Validate rewritten queries, authorization, result provenance, no-answer behavior, and injection-resistant handling of source content.

> **Related item:** RAG correctness has two independent stages: retrieval must return the right authorized evidence, then generation must synthesize it accurately. Evaluate both.

### Configure connectors and REST APIs as tools

Use precise names/descriptions because the orchestrator uses metadata for selection. Define typed input/output schemas. For writes, provide preview/confirmation where risk warrants it and return a business result the agent can interpret without exposing internal errors.

Server-side checks must validate:

- effective caller and permission;
- target ownership/tenant;
- allowed operation, fields, ranges, and current state;
- idempotency/replay;
- downstream response schema and provenance.

An OpenAPI description improves discovery and parameter generation but does not make an endpoint safe. Apply API gateway/service authorization, quotas, logging, schema validation, and threat controls.

### Configure MCP tools deliberately

When adding an [MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-components-to-agent), inspect its tools/resources, authenticate the connection, and disable unneeded tools. If “allow all” is turned off, newly added server tools remain off—useful change control.

Establish server ownership, source/deployment trust, transport security, authentication (OAuth 2.0/API key where supported), tool scopes, data handling, error semantics, versioning, availability, audit, and incident process. Power Platform data policies can govern MCP connectivity because Copilot Studio uses connector infrastructure.

Do not expect a topic to call an MCP server directly where current documentation says it cannot; use the supported agent-level orchestration path and **VERIFY CURRENT** as capabilities change.

### Use computer use only where its risk is justified

[Computer use](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use) operates a Windows web/desktop interface through visual reasoning and virtual input. Prefer an API/connector/flow when available: APIs provide typed contracts, better authorization, lower ambiguity, and more predictable testing.

For computer use:

- dedicate and harden the machine/account;
- minimize application/data access;
- write bounded instructions and allowed URLs/apps;
- control downloads/uploads, clipboard, credentials, notifications, and popups;
- require supervision/approval for consequential steps;
- define time/action/cost limits and safe stop;
- test UI changes, unexpected dialogs, injection-like on-screen content, and partial completion;
- retain permitted screenshots/action evidence without leaking sensitive data.

**VERIFY CURRENT:** models, harness, licensing, per-step cost, availability, limitations, and generative-orchestration requirements are volatile. Do not memorize the current model list or price.

## 5. Design multi-agent and Azure integrations

### Choose child versus connected agents

| Pattern | Boundary | Good fit | Main design concern |
|---|---|---|---|
| Child agent | Lightweight component inside parent context | Group focused instructions, knowledge, and tools for one task | Inputs/outputs, trigger description, parent coupling |
| Connected Copilot Studio agent | Independently managed agent connected to orchestrator | Reuse across solutions/teams | Environment, sharing, auth, lifecycle and version |
| Foundry agent | Pro-code/specialized current Foundry agent | Custom model/tool/RAG implementation | Current Foundry version, project endpoint/agent ID, identity/data flow |
| Fabric data agent | Fabric-governed data reasoning exposed as a tool | Questions over lakehouse/warehouse/semantic/KQL data | Capacity, underlying data permissions, cross-geo/settings |
| External A2A agent | Agent exposing an A2A endpoint | Cross-platform interoperability | Endpoint trust, auth, agent card/task/artifact contract |

A child agent is not a standalone deployment. It is useful for cohesive specialization without an independent ownership boundary. A connected agent creates operational reuse but requires explicit lifecycle and access coordination.

### Design delegation behavior

The parent needs a distinct description for when each agent should be invoked. Avoid overlapping descriptions. Define accepted task input, returned artifact, context sharing, permission boundary, timeout, error, retry, and fallback. Test ambiguous intents, unavailable child/connected agent, malformed result, multi-hop loops, and conflicting answers.

Set a completion/handback rule. The orchestrator should not bounce indefinitely between agents. Preserve correlation and identify the agent/tool that produced material evidence.

### Integrate current Foundry agents

Copilot Studio’s [Foundry connection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-foundry-agent) currently supports agents from the new Microsoft Foundry portal; an older Foundry agent can fail with a version error. Supply the project endpoint and agent ID, then use specific metadata so the main agent knows when to delegate.

Treat the Foundry connection as a cross-platform trust boundary: document identities, data shared, model/tool behavior, content controls, latency/cost, observability, and responsibility for evaluation. Mark the feature’s preview status and **VERIFY CURRENT**.

### Integrate Fabric data agents

A [Fabric data agent used as a Copilot Studio tool](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-copilot-studio-tool) evaluates requests using Fabric and underlying data-source permissions. Validate capacity/tenant settings, supported sources, user license, authentication mode, instructions, data permissions, source/result quality, evaluation, and channel behavior.

Do not duplicate business logic in the parent prompt. Let the data agent own semantic/data interpretation and return a bounded, provenance-bearing answer; let the parent own user workflow and final presentation.

### Integrate external agents with A2A

[Copilot Studio A2A guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-agent-to-agent) demonstrates connecting an external endpoint. For production, do not copy a no-authentication development sample. Require a secure hosted endpoint, supported authentication, strict task/artifact schemas, timeout/cancellation, correlation, telemetry, rate limits, versioning, and result validation.

A2A connects agents; MCP connects an agent to tools/resources. If an external component only performs bounded operations, an MCP or REST tool may be simpler than representing it as an agent.

### Integrate Azure AI Search and Foundry models

For generative answers backed by Azure AI Search, design ingestion, index schema, vectors, hybrid/semantic retrieval as applicable, filters/security, freshness, and citations before configuring the node. The Foundry connection/model configuration is only one part of the end-to-end RAG path.

For custom prompts using the Foundry model catalog, benchmark the exact model/deployment with the prompt, data, and output schema. Check region, quota, latency, content controls, cost, and fallback compatibility. **VERIFY CURRENT:** model names/versions, availability, and product integration are volatile.

## 6. Evaluate and monitor agent performance

### Build test sets from requirements and risks

Each test case should contain prompt/conversation, user profile/auth context, prerequisite state, expected behavior or reference, acceptance criteria, method, and risk/category. Cover:

- primary intents and rephrases;
- multi-intent and long-context conversations;
- no-answer/out-of-scope and escalation;
- knowledge freshness, authorization, citations, and contradiction;
- correct topic/tool/agent selection;
- flow success/rejection/timeout/schema error;
- unsafe/adversarial input and indirect injection in knowledge/tool results;
- different users, channels, environments, and locales;
- performance, capacity, and partial dependency failure.

Microsoft’s [evaluation checklist](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/evaluation-checklist) recommends starting from core scenarios, baselining, expanding systematically, and operating continuous quality improvement.

### Choose the evaluation method deliberately

| Method | Good for | Limitation |
|---|---|---|
| Exact/contains text match | Required code, phrase, field, or refusal | Penalizes valid paraphrase |
| Similarity | Multiple valid phrasings | Can reward semantically close but unsupported content |
| General/quality evaluator | Relevance, groundedness, completeness, abstention | Model-based judgment needs calibration |
| Capability/topic/tool checks | Correct routing and action selection | Does not prove final business outcome |
| Human review | Nuance, safety, high-impact decisions, calibration | Cost, consistency, and reviewer guidance |
| Deterministic integration assertion | API/flow arguments, status, side effect, idempotency | Cannot judge open-ended response quality alone |

Copilot Studio’s [agent evaluation overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro) explicitly says evaluation measures correctness/performance rather than AI ethics or safety. Keep separate adversarial, security, privacy, and responsible-AI reviews.

Review aggregate and per-case results, transcripts/activity maps, resources used, tool arguments/results, user profile, and version. Diagnose instruction, topic routing, knowledge retrieval, prompt/model, tool, connected agent, channel, or data failures separately. Rerun the same baseline after a change and retain important failures as regressions.

### Monitor with native analytics and Application Insights

[Application Insights telemetry](https://learn.microsoft.com/en-us/microsoft-copilot-studio/telemetry-overview) supplements Copilot Studio analytics. Current documentation distinguishes agent-level telemetry and preview environment-level OpenTelemetry-aligned telemetry.

Monitor:

- sessions, engagement, resolution, escalation, abandonment, and user feedback;
- topic/tool/agent selection, flow runs, failures, latency, and dependency calls;
- authentication/authorization failures and suspicious usage;
- knowledge/citation coverage and evaluation regressions;
- token/credit/capacity use, rate limits, and cost per successful outcome;
- channel/client differences and release/version correlation.

Apply redaction, access control, retention, sampling, and workspace ownership to telemetry. Correlate the agent turn to flow/API/MCP/Foundry/Fabric dependencies without logging access tokens, secrets, or unnecessary personal data.

> **Related item:** A dashboard proves that telemetry exists. An operating model defines thresholds, ownership, alert routing, investigation steps, remediation, and the release decision that follows.

## 7. Implement ALM with solutions, environment variables, and pipelines

### Package the complete dependency graph

Use [Copilot Studio solutions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-overview) to transport agents and related components. Add the agent to a custom solution and inspect dependencies such as topics/components, flows, prompts, custom connectors, connection references, environment variables, Dataverse objects, and security roles.

Do not develop production work in the default solution as the lifecycle container. Use unmanaged solutions in development and managed solutions in downstream environments according to organizational ALM policy. Record solution publisher, semantic version, ownership, dependencies, upgrade/removal behavior, and post-import steps.

### Separate configuration from solution logic

Use environment variables for values that differ across development, test, acceptance/staging, and production: API base URLs, resource IDs, feature switches, queue names, or non-secret configuration. Use connection references for connector bindings. Put secrets in an appropriate secret store/connection mechanism, not plain environment-variable values.

Validate after import:

- environment-variable current values;
- connection-reference ownership and authorization;
- flow activation and run-only permissions;
- agent authentication/sharing and channel configuration;
- knowledge/index endpoints and permissions;
- connected agent IDs/endpoints;
- App Insights and governance settings;
- test profiles and test data isolation.

### Implement and extend Power Platform Pipelines

[Power Platform Pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) deploy solutions through defined stages. A credible agent pipeline includes:

1. solution and dependency validation;
2. unpack/source control/static analysis where used;
3. import into isolated test;
4. connection/configuration setup without exposing secrets;
5. flow activation and smoke/integration tests;
6. automated agent evaluation against a stable set;
7. security, data-policy, channel, and responsible-AI gates;
8. approval and production deployment;
9. post-deploy smoke/evaluation/telemetry check;
10. rollback/recovery and evidence retention.

Pipeline extensibility can add pre/post deployment steps. Keep extension identities least privileged and never place personal access tokens or client secrets in source or solution artifacts. Treat prompt, topic, knowledge configuration, tool description, agent connections, evaluations, and telemetry configuration as release behavior—not merely the solution ZIP.

### Design rollback for stateful integrations

An older solution version may not be compatible with changed environment variables, connector schemas, external APIs, connected agents, indexes, or in-flight flows. A rollback cannot undo a completed tool action or erase a bad durable write. Define compatible versioning, backups/exports, traffic/channel switch, flow cancellation, data correction/compensation, and communication.

## 8. Integrated scenarios

### Scenario 1: Internal HR service agent

**Goal:** answer policy questions and prepare a leave request requiring manager approval.

**Design:** Teams channel with Microsoft authentication; security-trimmed internal knowledge for policy; a deterministic leave topic collects dates and validates them; an agent flow calls the HR connector and creates an approval; Adaptive Card displays the exact request; Dataverse/system of record holds transaction state.

**Controls:** end-user identity for policy/HR access, DLP-approved connectors, no maker personal connection, approval expiry, idempotency, citation/no-answer policy, limited transcript access.

**Evidence:** authorized/unauthorized knowledge tests, topic/tool route, null/date boundary tests, approval/rejection/timeout, duplicate-submit prevention, channel card accessibility, evaluation baseline, flow/Application Insights correlation.

### Scenario 2: Customer equipment-support agent

**Goal:** troubleshoot equipment, search product knowledge, query warranty status, and automate a legacy diagnostic UI only when no API exists.

**Design:** Authenticated web channel with Direct Line token exchange; Azure AI Search for versioned manuals; REST tool for warranty; computer use on a dedicated machine for legacy diagnostics; human approval before any device-changing step; escalation creates a support case.

**Controls:** index metadata filters, server-side customer/equipment authorization, REST idempotency, hardened computer-use machine/account, action/time/cost limit, screenshot redaction, injection tests against manual/UI content, safe partial failure.

**Evidence:** retrieval relevance/citations, cross-customer denial, malformed API result, UI-change recovery, approval record, latency/cost, no-answer/escalation, complete distributed trace.

### Scenario 3: Enterprise analytics coordinator

**Goal:** answer business questions and coordinate specialist agents without granting the parent direct access to every system.

**Design:** A main Copilot Studio agent delegates policy to a child agent, governed metrics to a Fabric data agent, and advanced forecasting to a current Foundry agent; an external partner agent connects through authenticated A2A. A deterministic flow packages an approved report.

**Controls:** non-overlapping descriptions, per-agent data/identity boundary, typed task/result, timeout and handback, loop limit, cross-geo/data review, source attribution, independent evaluations, versioned connection/configuration.

**Evidence:** correct delegation matrix, Fabric permission tests, Foundry version compatibility, A2A auth/failure, conflicting-agent response policy, evaluation by component and workflow, pipeline promotion/rollback proof.

## 9. Hands-on labs

Use nonproduction tenants/environments and synthetic data. Keep an evidence log with design, object IDs/names, configuration version, test result, telemetry, failure exercise, and cleanup.

### Lab 1 — Architecture, identity, and channel plan

Choose an internal or external scenario. Produce audience/outcome, channel/auth matrix, environment zone, data-flow diagram, identity-to-resource matrix, responsible-AI risk register, component reuse decision, SLOs, and deployment/rollback plan. Identify classic versus new authoring requirements.

### Lab 2 — Topic, variables, and Adaptive Card

Build a classic-experience topic with narrow triggers, required questions, Power Fx validation, topic/global/system variables, one Adaptive Card, a safe cancel path, and channel-specific fallback. Test blank, invalid, adversarial, and duplicate input plus two target clients.

### Lab 3 — Agent flow with human approval

Create a solution-aware agent flow with typed inputs/outputs, connector actions, connection reference, approval, timeout, error categories, idempotency, and structured result. Add it to the topic and monitor runs. Demonstrate rejection, expiry, transient failure, and schema mismatch recovery.

### Lab 4 — Enterprise knowledge and Azure AI Search

Compare one indexed/connector knowledge source with an Azure AI Search or synthetic custom-search source. Preserve metadata and authorization scope. Build positive, no-answer, stale, ambiguous, and cross-user tests. Evaluate retrieval evidence/citations separately from response quality.

### Lab 5 — REST, MCP, and computer-use decision

Implement a safe synthetic operation as a REST/custom connector or MCP tool. Document why. Configure authentication, tool selection, schemas, validation, errors, and audit. Design (or sandbox) the equivalent computer-use workflow, then compare correctness, security, latency, cost, and maintainability.

### Lab 6 — Multi-agent collaboration

Build a parent plus child agent and connect one independently managed agent where licensing permits, or mock its contract. Use distinct descriptions, typed inputs/outputs, correlation, timeout, failure/fallback, and loop bound. Document how Foundry, Fabric, and A2A variants change identity/data/lifecycle responsibility.

### Lab 7 — Evaluation and telemetry

Create a test set spanning core, rephrased, no-answer, unsafe, routing, knowledge, tool, multi-user, and dependency-failure cases. Select text/similarity/quality/human/deterministic methods. Baseline and rerun after a controlled change. Connect Application Insights, redact sensitive data, and build a runbook from one alert.

### Lab 8 — Solution and pipeline promotion

Package agent, topic, flow, connector/tool, connection reference, environment variables, and evaluation assets. Import through development/test/production-like environments with different endpoints/identities. Add validation/evaluation/approval gates, perform post-deploy checks, and rehearse rollback plus compensation for a completed action.

## 10. Knowledge checks

These are original concept checks, not recalled exam questions.

### Plan and configure agent solutions

1. Why should AB-620 candidates recognize the classic and new agent experiences?
2. When is a deterministic topic preferable to generative orchestration?
3. What four identity decisions are separate when an agent calls a connector?
4. Why can a secure Teams sign-in still produce overprivileged downstream access?
5. What makes an agent flow safe to retry?
6. When should a conversation variable become a Dataverse/system-of-record field?
7. What must be tested for an Adaptive Card across channels?
8. Why does reuse increase blast radius?
9. How should responsible-AI controls differ between an informational and an autonomous agent?

### Integrate and extend agents

10. When is a knowledge source different from a tool against the same system?
11. What risk exists when Azure AI Search retrieval is not delegated/security-trimmed per user?
12. Why is an OpenAPI document insufficient security for a REST tool?
13. When is MCP preferable to a direct API tool?
14. What should happen when an MCP server publishes a new tool?
15. Why should computer use be behind an available API integration?
16. When is a child agent better than a connected agent?
17. What additional checks apply to a Foundry agent connection?
18. Why is an unauthenticated development A2A sample unsuitable for production?

### Test and manage agents

19. Why should retrieval and response generation be evaluated separately?
20. When is exact text match better than semantic similarity?
21. Why is general-quality evaluation not a safety test?
22. What evidence explains a correct answer produced through the wrong tool?
23. Which telemetry should correlate an agent turn with a failed flow?
24. Why should solution import be followed by configuration validation?
25. What belongs in an environment variable versus a connection reference?
26. Why can solution rollback fail to undo an incident?
27. What makes an automated evaluation a useful pipeline gate?

### Cross-domain scenarios

28. An agent uses a maker’s ERP connection for all users. What must be decided first?
29. A topic and generative orchestration both call the same write tool. What is the risk and fix?
30. A Fabric agent and Foundry agent return conflicting answers. What architecture is missing?
31. A web agent uses a Direct Line secret in JavaScript. What should replace it?
32. A flow succeeds but the agent tells the user it failed. Where do you diagnose?
33. An evaluation score rises while user resolution falls. What should you do?
34. A new environment imports the agent but its flow is off. What ALM gap does this reveal?
35. An Azure AI Search answer cites another tenant’s document. Where must the control be fixed?
36. A UI change causes computer use to select a destructive button. Which controls limit impact?

## 11. Answers and reasoning

1. The official paths/objectives are topic-centric and currently classic-based, while the new preview uses a different instruction-first architecture and cannot convert agents between experiences.
2. When the sequence, required questions, validation, wording, approval, or transaction must be explicit and repeatable.
3. End-user authentication, agent sharing/authorization, connection identity (user versus maker/service), and the downstream system’s authorization.
4. Teams proves the user, but a maker-provided connector can execute under a broader shared identity unless constrained.
5. Validated typed inputs, idempotency key/state check, categorized transient failures, bounded retries, and compensation for partial work.
6. When it must survive sessions, support concurrency/audit/recovery, or act as authoritative business state.
7. Schema/version support, rendering, accessibility, input/action behavior, validation, authentication/user binding, and fallback.
8. A shared change can affect many agents; ownership, versioning, consumer tests, and deprecation are required.
9. Increase identity, permission, approval, action bounds, adversarial testing, monitoring, and recovery controls with autonomy and impact.
10. Knowledge supplies evidence for synthesis; a tool performs live retrieval/action with explicit parameters, result, and side-effect semantics.
11. The index may return documents the current user is not allowed to see. Authorization/filtering must occur before evidence enters context.
12. It describes operations and schemas; the service must still authenticate, authorize, validate, rate-limit, log, and protect state.
13. When standardized discovery/versioned capabilities reused by several agents justify a governed server lifecycle.
14. With selective tool control, keep it disabled until reviewed; otherwise the agent’s capability surface can expand unexpectedly.
15. GUI automation is visually probabilistic, slower, harder to authorize/test, and more vulnerable to UI changes and on-screen manipulation.
16. When specialization belongs inside one parent lifecycle and does not need independent deployment, reuse, identity, or ownership.
17. Current-versus-old Foundry generation, project endpoint/agent ID, identity, data flow, permissions, tools/models, preview status, quality, telemetry, and lifecycle.
18. It exposes an agent publicly without caller verification or authorization; use secured hosting/authentication and production controls.
19. A good generator can mask poor/unauthorized retrieval; good evidence can also be synthesized incorrectly.
20. For required codes, phrases, fields, refusals, or deterministic outputs where paraphrase is not acceptable.
21. Microsoft states evaluation covers correctness/performance; ethics, abuse, security, privacy, and safety require dedicated tests/review.
22. Activity map/trace showing selected topic/tool/agent, inputs, source/result, and final output.
23. Shared correlation/operation ID, agent/session/turn, flow run ID, dependency span, version/environment, error, duration, and safe user context.
24. Connections, current environment-variable values, flow activation, permissions, sharing, channels, indexes, and telemetry are environment-bound.
25. Configuration value such as endpoint/resource ID goes in an environment variable; connector binding/credentials belong to a connection reference/connection.
26. External actions, data writes, in-flight runs, indexes, and incompatible schemas/configuration persist beyond the solution version.
27. Stable representative cases, explicit methods/thresholds, isolated test identity/data, reproducible version evidence, and a reviewed failure policy.
28. Whether actions should represent each user or an intentionally bounded service identity; then scope and govern that identity.
29. Duplicate side effects. Choose one invocation path or enforce idempotency plus an explicit routing contract.
30. A source/authority and conflict-resolution contract with provenance, freshness, confidence, abstention, and escalation.
31. A server-side exchange of the secret for a bounded Direct Line token; the secret stays off the client.
32. Correlate the flow result/output schema and topic/tool mapping with the orchestration trace and response branch.
33. Inspect cases and production outcomes, check evaluator drift/overfitting, add outcome-grounded cases, and do not promote on the composite score alone.
34. Missing post-import configuration/activation validation and deployment checklist or automated post-step.
35. At ingestion/query authorization and metadata filtering before retrieval; output filtering is too late.
36. Dedicated least-privilege machine/account, bounded instructions/allowed apps, approval before impact, action/time limits, monitoring, safe stop, and recovery/compensation.

## 12. Readiness checklist

You are approaching readiness when you can:

- map every published bullet to an object, dependency, decision, test, signal, and recovery path;
- identify classic versus new Copilot Studio instructions and implement the topic objectives in the applicable experience;
- design channel, authentication, sharing, connection identity, data policy, and downstream authorization together;
- implement topics, variables, Adaptive Cards, prompts, generative answers, HTTP, and agent flows with explicit failures;
- choose among knowledge, connector, custom connector, REST, flow, MCP, computer use, child agent, connected agent, Foundry, Fabric, and A2A;
- build access-aware RAG and evaluate retrieval separately from generation;
- construct representative test sets and select deterministic, similarity, quality, and human methods appropriately;
- correlate Copilot Studio, flow, API, MCP, Foundry/Fabric/A2A, and Application Insights evidence;
- package all dependencies and configuration in a solution and promote them through a gated pipeline;
- explain why rollback may require configuration restoration, state migration, or business compensation;
- recheck the official blueprint and every **VERIFY CURRENT** platform boundary before the exam.

The [AI Agent Builder Associate credential page](https://learn.microsoft.com/en-us/credentials/certifications/ai-agent-builder-associate/) currently says no Microsoft Practice Assessment is available. Do not use recalled, leaked, or “actual exam” questions. Readiness should come from documented behavior, hands-on evidence, and original scenario practice.

## 13. Primary references

- [Official AB-620 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-620)
- [AI Agent Builder Associate credential page](https://learn.microsoft.com/en-us/credentials/certifications/ai-agent-builder-associate/)
- [AB-620T00-A course](https://learn.microsoft.com/en-us/training/courses/ab-620t00)
- [Classic versus new agent experience](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/classic-vs-new)
- [Copilot Studio architecture overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/architecture-overview)
- [User authentication](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication)
- [Channel guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/channels)
- [Zoned governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2)
- [Agent tools](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent)
- [RAG guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/retrieval-augmented-generation)
- [MCP tools and resources](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-components-to-agent)
- [Computer use](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use)
- [Foundry agent connection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-foundry-agent)
- [Fabric data agent connection](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-copilot-studio-tool)
- [A2A connection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-agent-to-agent)
- [Agent evaluation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro)
- [Application Insights telemetry](https://learn.microsoft.com/en-us/microsoft-copilot-studio/telemetry-overview)
- [Copilot Studio solutions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-overview)
- [Power Platform Pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines)

## Places to learn

This is a curated starting point, not a complete list. Do **not** consume everything. Select the explanations, demonstrations, labs, and assessment signals that close your gaps, and keep the current official blueprint beside third-party material.

| Resource | Access | Estimated time |
|---|---|---:|
| Three official Microsoft Learn paths | Public | 8 hours 29 minutes plus exercises |
| AB-620T00-A instructor-led course | Provider/schedule dependent | 3 days; available September 18, 2026 |
| Eight labs in this guide | Platform usage may cost money | About 14–28 hours |
| Udemy AB-620 course by Kuljot Singh Bakshi | Paid | 9 hours 27 minutes plus labs/review |
| Udemy original practice exams by Joshua Ravnjak | Paid | About 6–10 hours including explanation review |
| Microsoft Copilot Studio docs/guidance | Public | Select 4–12 hours by objective gap |

### Official course sequence

- [Design agent conversations and responses using topics](https://learn.microsoft.com/en-us/training/paths/design-agent-conversations-responses-topics-copilot-studio/) — 2 hours 17 minutes, three modules.
- [Design and build multi-agent solutions](https://learn.microsoft.com/en-us/training/paths/design-build-multi-agent-solutions-copilot-studio/) — 2 hours 54 minutes, four modules.
- [Integrate agents with enterprise systems](https://learn.microsoft.com/en-us/training/paths/integrate-agents-enterprise-systems-copilot-studio/) — 3 hours 18 minutes, four modules.
- [AB-620T00-A](https://learn.microsoft.com/en-us/training/courses/ab-620t00) — three instructor-led days, listed as available September 18, 2026.

The three live paths total 8 hours 29 minutes before hands-on work. Each currently identifies its modules as classic-experience content. Pair it with the current experience comparison, and do not infer that the future instructor-led course date delays the active exam or the self-paced paths.

### Additional instruction and assessment

- [AB-620: Copilot Studio AI Agent Builder Exam Prep](https://www.udemy.com/course/copilot-studio-ai-agent-builder/) by Kuljot Singh Bakshi — 9 hours 27 minutes, 64 lectures, shown as updated June 2026. It includes hands-on coverage across Foundry, connectors/APIs/MCP, RAG, multi-agent design, Application Insights, evaluation, and ALM; verify current UI/preview behavior.
- [AB-620 Practice Exams: Copilot Studio AI Agent Builder](https://www.udemy.com/course/ab-620-practice-exams-copilot-studio-ai-agent-builder/) by Joshua Ravnjak — six 60-question tests (360 original questions), shown as updated August 2026. Allow about 6–10 hours for selected timed attempts and explanation/source review; use it as a secondary signal after hands-on work.
- [Copilot Studio documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/) and [architecture/guidance collection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/) — use exact pages by objective and verify whether each applies to classic, new, preview, or both.

No exact current AB-620 Pluralsight path, O'Reilly certification course, Whizlabs package, MeasureUp practice test, Partner Skilling Hub listing, or Microsoft Practice Assessment was verified on September 1, 2026. That is a present catalog gap, not a prediction that none will appear. No exact John Savill or Microsoft Reactor AB-620 course was verified; broader Copilot Studio videos are supporting demonstrations only.

Avoid products that promise leaked, “actual,” or memorized exam questions. Original practice is useful only when explanations are checked against the current blueprint and Microsoft documentation.
