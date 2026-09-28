---
exam_code: AB-620
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-620
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AB-620 Designing and Building Integrated AI Agent Solutions in Copilot Studio Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-620-coverage-record). The [official AB-620 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-620) is authoritative.

**Current baseline:** Official study-guide page last updated April 21, 2026; Microsoft does not publish a separate skills-effective date on that page.<br>
**Exam state:** Active (no longer labeled beta on the credential page) as verified September 28, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Training availability:** The three official self-paced paths are live; the separate three-day AB-620T00-A instructor-led course is listed as available September 30, 2026 (scheduled; not yet delivered).<br>
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

Read Sections 1–7, work through the ten labs, and explain the three scenarios without referring to portal screenshots. Use the official blueprint as the coverage checklist. Product navigation, licensing, limits, preview status, and experience names change; understand the object and dependency model beneath the UI.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

### Living-guide watch — September 28, 2026

The [GitHub Copilot Harness agent overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview) is the current boundary for that rapidly changing authoring experience. Keep it distinct from standard and Copilot chat harnesses, and verify which knowledge, tool, channel, ALM, and governance features each experience supports instead of carrying capabilities across by name.

The [AI at Work roadmap transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) changes where future Power Platform and Dynamics capabilities are announced, not the current AB-620 blueprint. Use the roadmap for discovery and current Learn pages for implementation. The independent courses in Places to learn can add demonstrations; flag any older product vocabulary and map it to the current object model before relying on it.

The [September deep review](../docs/research/2026-09-28-ab-620-deep-review.md) maps all **44 unchanged detailed objectives**. It adds six worked examples, two labs, 48 answered checks, and two blog exercises. Current implementation changes include Activity-protocol prerequisites, harness-specific Fabric integration, preview approval packaging limits, and expanded evaluation methods. No cloud lab was executed during this review.

The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/ai-agent-builder-associate/) currently lists **120 minutes**, English and 12 other languages, and no Practice Assessment. Course release dates and third-party mock-test timing do not define the exam's availability or duration.

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

### The current platform has three harnesses

Current Microsoft documentation distinguishes the **GitHub Copilot**, **standard**, and **Copilot chat** harnesses. Older AB-620 learning material may instead say **classic experience** or **new agent experience**. This matters because the objective list explicitly includes topics, nodes, agent flows, variables, and Adaptive Cards, which align most closely with the structured standard-harness authoring model.

| Signal | Standard harness | GitHub Copilot harness | Copilot chat harness |
|---|---|---|---|
| Primary control | Topics, rules, branches, and structured workflows | Goal-driven reasoning across tools, files, skills, and memory | Enterprise knowledge extension for Microsoft 365 Copilot Chat |
| Best fit | Predictable conversations and repeatable rule-based work | Longer multistep business processes that must adapt | Grounded internal answers in an existing Copilot Chat surface |
| Publishing emphasis | Internal teams or external customers | Internal teams or external customers | Internal teams |
| Volatility to verify | Topic, flow, licensing, and channel support | Tools, skills, memory, files, sandbox, billing, and rollout | Knowledge support, entitlements, publishing, and billing |

Use the [current harness overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview) to identify the runtime before following steps. **VERIFY CURRENT:** capabilities and billing differ by harness and continue to change. For AB-620's published topic objectives, practice the structured topic model even if you also explore the reasoning-heavy harness.

> **Related item:** “Classic” here names the Copilot Studio authoring experience. It is separate from Microsoft Foundry’s classic-versus-current resource/API generations. A connected Foundry agent must also be checked for its own platform generation.

The GitHub Copilot harness is generally available; individual capabilities such as memory and connected agents can still be preview. Agents cannot be transferred between standard and GitHub Copilot harnesses. A structured flow can control the sequence of operations without making its model responses or external-service outcomes deterministic. Also distinguish the harness from the separate GitHub Copilot service and its data handling.

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

In the standard harness, [authentication settings](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication) determine which user variables are available. `Authenticate with Microsoft` does not expose `User.AccessToken` or `User.IsLoggedIn`; switching from manual authentication can therefore break topics that reference them. Authentication changes require publishing. Test the exact channel and setting instead of assuming that a successful Teams sign-in configures every external channel.

[Blocking maker-provided credentials](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-no-maker-authentication) applies to existing and new tools and can interrupt scheduled/background execution because no live user is available to sign in. Both credential modes are available by default at the administrative level; that does not mean every tool defaults to maker credentials. Environment-group rules take precedence over individual settings. The [security scan](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-scan) surfaces configuration warnings; a clean scan does not prove data authorization.

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

**Worked example 1 — channel reachability versus user authorization.** At 10:00, a maker enables the web channel's secure-access setting and changes the agent's user authentication. The [web security procedure](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-web-security) allows up to two hours for secure-access propagation, without publishing; the separate authentication change does require publishing. At 10:20, only 20 of that possible 120-minute interval have elapsed. Neither waiting until 12:00 nor publishing proves that a particular user can access a protected record: test channel access, user identity and backend permissions separately. Keep the Direct Line secret on the server, exchange it for an expiring conversation-scoped token, and test secret rotation and token refresh.

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

The standard-harness [agent-flow FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-faqs) requires a solution flow with the agent-call trigger and response action for this integration. Multiple agents can reuse it. Agent flows created in the Copilot Studio UI cannot currently be copied or shared through co-owner/run-only permissions; desktop flows cannot be called from them. Converting a Power Automate flow changes its management and billing context and is one-way; it does not convert it to a GitHub-harness workflow. Review the [flow overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview) for capacity, testing and license exceptions rather than assuming that a Power Automate entitlement covers every execution path.

**Worked example 2 — prove that human review is reachable.** A preview [advanced approval](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-advanced-approvals) contains an AI stage followed by a human stage. With default routing, 60 AI approvals continue, 30 rejections end the process, and 10 undecided results continue. Only **70 of 100** requests reach the human stage. If policy requires human review of every disposition, configure and test all three paths; drawing a human stage after the AI stage is insufficient. Use distinct approvers across stages and ensure reviewers belong to the environment. File inputs to AI stages require base64 contents; ordinary attachments are not supported. Advanced approvals currently require recreation after solution import and after sharing a flow containing the Human review connector. Record these manual steps in the release checklist; successful solution import does not prove a working approval.

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

The [Adaptive Card node](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-ask-with-adaptive-card) supports schema through 1.6, but Teams and the live chat widget are limited to 1.5; Web Chat supports 1.6 without `Action.Execute`. Test-chat rendering is not a host-compatibility test. Use an interactive node with a submit button for data collection and a Message node for display-only cards. Old cards may remain clickable: bind a submit identifier to the current operation/version and validate it server-side. Disabling a button in the client improves usability but does not prevent replay from another client.

### Use custom prompts and knowledge inside topics

A custom prompt should state task, trusted instructions, input fields, evidence, output contract, safety constraints, and failure behavior. Select a Foundry catalog model only after evaluating quality, modality, latency, availability, and cost. Version prompts and model/deployment configuration with solution artifacts.

The generative answers node can use topic-scoped knowledge and custom data. Topic knowledge takes priority, while broader agent knowledge may act as fallback. This can intentionally narrow answers for a process, but it can also create confusing source precedence. Test expected source use and no-answer behavior.

Use the HTTP request node for a bounded call when appropriate, but design authentication, headers, parameter validation, response schema, timeout, retry, error branches, and sensitive-data handling. For reusable or governed APIs, a REST tool, connector, or MCP layer can provide a stronger lifecycle boundary.

For the [HTTP node](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-http-node), choose a response schema and map status/error values deliberately. The default timeout is 30 seconds. `Raise an error` invokes the error path; `Continue on error` stores error information and continues, so add an explicit failure branch before any success message or dependent action. Retries must account for prior side effects.

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

[Topic variable mapping](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables) controls values received and returned through redirects. Converting a topic variable to a global variable cannot be reversed through the same conversion control. Map contracts explicitly and test a redirected topic both with supplied values and with missing values.

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

For standard-harness [Azure AI Search knowledge](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-azure-ai-search), configure integrated vectorization and, if needed, semantic ranking in Search first. Use a formal data connection, select the one supported vector index, and wait for metadata to reach `Ready`. The article lists several authentication methods in its creation wizard, while its broken-connection recovery advice specifies Entra ID. Keep those contexts separate; do not hand-build an endpoint/key connection or treat a recovery instruction as a blanket ban on every listed wizard option. A private Search endpoint also requires the Power Platform network configuration. Citation URLs must be usable by the intended reader; a citation or an authenticated service connection alone does not establish per-document access control.

**Worked example 3 — authorize and rank before returning knowledge.** A custom search service finds 12 candidate snippets in system A and 10 in B. The caller is permitted to see 9 and 8 respectively. Filter on the server first, leaving **17 authorized candidates**, then rank/deduplicate and return at most **15** for generation; five unauthorized candidates never enter the model context. This illustrative calculation assumes no duplicates. The [custom knowledge trigger](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/custom-knowledge-sources) runs `OnKnowledgeRequested` topics in parallel and applies the 15-snippet cap across their combined results. It is configured in YAML, uses rewritten semantic/keyword queries, and writes `Content` plus optional `Title` and `ContentLocation` to `System.SearchResults`. A rewritten query is search input, not trusted authorization. Test that a high-ranked forbidden snippet cannot displace an authorized result or leak into a citation.

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

The [MCP connection procedure](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent) requires Streamable transport; SSE is no longer supported. Match OAuth discovery/client registration or API-key configuration to the actual server. Standard-harness MCP requires generative orchestration and currently exposes tools and resources; a resource must be returned through a tool. Do not assume every protocol feature, such as prompt templates, is a supported Copilot Studio feature. The [MCP overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp) and current tool UI are the authority for invocation support; the former blanket topic restriction is not retained without current evidence.

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

[Human supervision for computer use](https://learn.microsoft.com/en-us/microsoft-copilot-studio/human-supervision-computer-use) is triggered by probabilistic model behavior. It can miss a desired pause or request unnecessary clarification. Removing all reviewers does not create reliable autonomous operation: a requested pause has nowhere to go and the session fails. An unanswered request pauses until its timeout; inline review requires advanced logging. Verify the connection owner/reviewer routing, and avoid including secrets in responses that may be retained in logs. The [computer-use FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-computer-use) excludes sensitive/high-risk uses such as financial transactions. For a required approval, enforce a separate process/backend gate before the operation; a prompt to “ask first” does not implement that gate.

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

The [child/connected-agent guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents) distinguishes component reuse from an independently managed agent. Topic redirects can return control to their originating topic; Fabric data agents do not support that redirect route. Keep performance recommendations separate from limits: the tools article currently permits up to 128 tools per orchestrator while recommending a much smaller selection, and the multi-agent guidance uses tool-count heuristics for deciding when to split responsibilities. Evaluate routing ambiguity and extra-hop latency rather than splitting at an assumed universal threshold.

### Design delegation behavior

The parent needs a distinct description for when each agent should be invoked. Avoid overlapping descriptions. Define accepted task input, returned artifact, context sharing, permission boundary, timeout, error, retry, and fallback. Test ambiguous intents, unavailable child/connected agent, malformed result, multi-hop loops, and conflicting answers.

Set a completion/handback rule. The orchestrator should not bounce indefinitely between agents. Preserve correlation and identify the agent/tool that produced material evidence.

### Integrate current Foundry agents

Copilot Studio’s [Foundry connection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-foundry-agent) currently supports agents from the new Microsoft Foundry portal; an older Foundry agent can fail with a version error. Supply the project endpoint and agent ID, then use specific metadata so the main agent knows when to delegate.

This is a **preview standard-harness connection**. The current Foundry agent must expose the **Activity protocol**: new agents default to Responses and A2A, which are insufficient for this connector. Enable Activity using REST or the Python SDK; the Foundry portal does not offer that toggle and can still display only Responses/A2A afterward. Missing Activity can produce HTTP 400; an older Foundry agent can instead produce a version-not-found error. Check generation, endpoint, protocol and identity independently before changing prompts.

Treat the Foundry connection as a cross-platform trust boundary: document identities, data shared, model/tool behavior, content controls, latency/cost, observability, and responsibility for evaluation. Mark the feature’s preview status and **VERIFY CURRENT**.

### Integrate Fabric data agents

The current [Fabric data agent tool procedure](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-copilot-studio-tool) applies to the **GitHub Copilot harness**, using the **Fabric IQ Data MCP** tool. Do not substitute its steps for an older standard-harness connected-agent procedure. Prerequisites include a published data agent, qualifying Fabric capacity, required tenant settings, same-tenant/account alignment, the stated licenses, and access to the data agent and its underlying data.

Its credential choice changes the access boundary: **User** uses the caller's permissions; **Maker** lets users obtain data available to the maker even without their own access. Choose and test the intended model explicitly. Save the tool before testing/publishing and use a precise routing description. Review cross-geography processing/storage because responses can leave the Fabric geography. The standard-harness evaluation feature currently excludes Fabric data agents; a testing step in this separate GitHub-harness tool procedure does not remove that limitation.

Do not duplicate business logic in the parent prompt. Let the data agent own semantic/data interpretation and return a bounded, provenance-bearing answer; let the parent own user workflow and final presentation.

### Integrate external agents with A2A

[Copilot Studio A2A guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-agent-to-agent) demonstrates connecting an external endpoint. For production, do not copy a no-authentication development sample. Require a secure hosted endpoint, supported authentication, strict task/artifact schemas, timeout/cancellation, correlation, telemetry, rate limits, versioning, and result validation.

For this connection, enter the agent's communication endpoint rather than its agent-card URL. The Copilot Studio procedure discovers `.well-known/agent.json`; manual metadata is a fallback for discovery, not proof that execution or authentication works. It supports configured no-auth/API-key/OAuth choices; a public development tunnel and a no-auth sample are not production access controls. Do not infer connector protocol-version support from a different Foundry A2A announcement.

A2A connects agents; MCP connects an agent to tools/resources. If an external component only performs bounded operations, an MCP or REST tool may be simpler than representing it as an agent.

### Integrate Azure AI Search and Foundry models

For generative answers backed by Azure AI Search, design ingestion, index schema, vectors, hybrid/semantic retrieval as applicable, filters/security, freshness, and citations before configuring the node. The Foundry connection/model configuration is only one part of the end-to-end RAG path.

For custom prompts using the Foundry model catalog, benchmark the exact model/deployment with the prompt, data, and output schema. Check region, quota, latency, content controls, cost, and fallback compatibility. **VERIFY CURRENT:** model names/versions, availability, and product integration are volatile.

Distinguish managed prompt-catalog choices from [bring-your-own-model prompts](https://learn.microsoft.com/en-us/microsoft-copilot-studio/bring-your-own-model-prompts). The latter currently requires a chat-completions endpoint, exact deployment/base-model names and a governed connection; a Responses endpoint can fail with `ResourceNotFound`. That route does not currently support GPT-5 and later, even if a different managed catalog offers them. Check modality support too: accepting image input is not image generation.

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

The standard-harness [test-set procedure](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create) supports single-response and conversation cases; a single-response set allows up to 100 cases. Generated cases do not prove coverage: source-grounded generation can miss absent information and authorization failures. Cases generated under a test profile can expose that account's data to makers with access to the agent. Use synthetic accounts/data and validate the selected profile's connections. Topic-level knowledge can override agent-level sources, with agent knowledge acting as fallback; test that precedence explicitly using the [generative answers node](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-boost-node).

### Choose the evaluation method deliberately

| Method | Good for | Limitation |
|---|---|---|
| Exact/contains text match | Required code, phrase, field, or refusal | Penalizes valid paraphrase |
| Similarity | Multiple valid phrasings | Can reward semantically close but unsupported content |
| General/quality evaluator | Relevance, groundedness, completeness, abstention | Model-based judgment needs calibration |
| Capability/topic/tool checks | Correct routing and action selection | Does not prove final business outcome |
| Human review | Nuance, safety, high-impact decisions, calibration | Cost, consistency, and reviewer guidance |
| Deterministic integration assertion | API/flow arguments, status, side effect, idempotency | Cannot judge open-ended response quality alone |

The current [evaluation methods](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-overview) include **Content Safety** and **Custom** grading as well as General Quality, Compare Meaning, Tool Use, Keyword Match, Text Similarity and Exact Match. Content Safety checks specified harmful-content categories; it is not a complete authorization, privacy or prompt-injection test. General Quality can penalize abstention even when refusal is the required outcome, so create refusal-specific expected behavior and calibrated custom labels. Check each method's support for single-response versus conversation cases and `Any` versus `All` matching. Missing required expectations can make a case invalid. Keep separate adversarial, security, privacy, and responsible-AI reviews alongside these measurements.

**Worked example 4 — make the denominator visible.** A synthetic run contains 72 Pass, 8 Fail, 12 Invalid and 8 Error cases. For our release worksheet, the graded-only rate is **72/80 = 90%**, graded coverage is **80/100 = 80%**, and demonstrated passes across the intended set are **72/100 = 72%**. These are explicitly defined worksheet metrics, not a reverse-engineered UI formula. Repair invalid cases and operational errors; do not discard them to make a release appear ready. A required authorization test failing also blocks our release even if aggregate quality rises. [Response time](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results) does not affect the built-in pass rate, so apply an independent latency gate. Export evidence before the documented **89-day** results retention expires.

**Worked example 5 — calibrate the custom grader.** Against 100 independently labeled synthetic responses, a grader flags 18 true violations and 6 acceptable responses, while missing 6 violations and correctly accepting 70 responses. Accuracy is **88%**, but violation precision and recall are both **75%**; it misses **6/24 = 25%** of violations. Review the false negatives and label definitions before trusting the aggregate. A grader classifies observed output; it does not enforce backend permissions or guarantee that a future response will be safe.

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

The [environment-level telemetry preview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-environment-level-agent-telemetry) supports both standard and GitHub Copilot harnesses in Managed Environments. New export configurations can take up to 24 hours to deliver telemetry. Current spans are in `dependencies`; older private-preview root events may appear in `requests`. Correlate a turn using `operation_Id` and parent links. This export excludes unauthenticated/multitenant configurations and topic events, lacks standard-harness duration values, and can lose data during transient events. It is not a transactional audit ledger. Keep agent-level `customEvents` queries separate, and do not infer “no executions” from a zero-row query against the wrong table or unsupported configuration.

**Worked example 6 — plan peak throughput separately from credits.** A hypothetical 120-user pilot measures a peak of 18 turns/minute and three model calls per turn: **54 model calls/minute**. Scaling to 2,400 comparable users gives a factor of **20**, or **360 turns and 1,080 model calls/minute** before retries, new channels and campaign bursts. This is an illustrative projection, not measured tenant data or a quota guarantee. The [throughput planning guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/plan-agent-throughput-rate-limits) requires real pilot observations for increase requests. Compare each environment, connector, flow, Dataverse and model limit at the relevant time window; a larger credit balance does not guarantee a higher processing rate.

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

Include advanced approvals' recreation steps in promotion testing. A pipeline transports solution components and the selected artifact; it does not migrate the application's business data or prove that every external credential, connection and preview component is ready. Keep data migration/recovery, manual environment setup, runtime authorization and smoke tests as explicit evidence.

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

**Design:** Authenticated web channel with Direct Line token exchange; Azure AI Search for versioned manuals; REST tool for warranty; computer use on a dedicated machine for legacy diagnostics; a separate enforced approval gate before any device-changing step; escalation creates a support case.

**Controls:** index metadata filters, server-side customer/equipment authorization, REST idempotency, hardened computer-use machine/account, action/time/cost limit, screenshot redaction, injection tests against manual/UI content, safe partial failure.

**Evidence:** retrieval relevance/citations, cross-customer denial, malformed API result, UI-change recovery, approval record, latency/cost, no-answer/escalation, complete distributed trace.

### Scenario 3: Enterprise analytics coordinator

**Goal:** answer business questions and coordinate specialist agents without granting the parent direct access to every system.

**Design:** A main Copilot Studio agent delegates policy to a child agent, governed metrics to a Fabric data agent, and advanced forecasting to a current Foundry agent; an external partner agent connects through authenticated A2A. A deterministic flow packages an approved report.

**Controls:** non-overlapping descriptions, per-agent data/identity boundary, typed task/result, timeout and handback, loop limit, cross-geo/data review, source attribution, independent evaluations, versioned connection/configuration.

**Evidence:** correct delegation matrix, Fabric permission tests, Foundry version compatibility, A2A auth/failure, conflicting-agent response policy, evaluation by component and workflow, pipeline promotion/rollback proof.

For Scenario 3, write the harness and connection type beside every arrow before implementation. Test the current Fabric IQ tool in its documented GitHub-harness environment and the standard-harness Foundry connector separately. Combining their documentation into one apparently supported topology is not integration evidence; validate the chosen end-to-end route and evaluation surface.

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

### Lab 9 — Approval reachability and promotion audit

Start with the 100 synthetic cases in example 2. Draw separate Approve, Reject and Undecided paths; mark every path that reaches a human and every path that can write externally. Define the required invariant and test it in a permitted sandbox, including rejection, missing reviewer, timeout and repeat submission. Export/import a disposable solution and record any advanced-approval recreation needed. Evidence: path matrix, assigned identities, run results and a promotion checklist. This review checked the arithmetic only; it did not create approvals or send messages.

### Lab 10 — Evaluation calibration and throughput worksheet

Use examples 4–6 to calculate graded coverage, demonstrated passes, grader false negatives and projected peak calls. Create synthetic cases for forbidden data, justified refusal, stale-card replay and missing Activity protocol. Define quality, critical-failure, latency and coverage gates independently. If running a sandbox evaluation, verify the test identity and export results with source/model/version context; measure an actual representative pilot before requesting capacity. Evidence: a scored worksheet, labeled cases and a list of unmeasured assumptions. No model or load test was run for this review.

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

### Current implementation boundaries

37. Why can secure web access and a new authentication setting become effective at different times?
38. Does placing a human approval after an AI approval guarantee human review?
39. Why can a successfully imported flow still have an unusable advanced approval?
40. What should happen before 22 retrieved snippets become model context?
41. Why can a current Foundry agent still fail with an Activity-protocol error?
42. How does Fabric tool maker authentication change the reader's access boundary?
43. Does computer-use supervision enforce a mandatory approval policy?
44. Why can a model available in a managed prompt catalog fail in a BYO prompt?
45. What does a 90% graded-only pass rate conceal in example 4?
46. What does 88% grader accuracy conceal in example 5?
47. Why does purchasing more credits not resolve every throughput error?
48. What can a zero-row environment-telemetry query fail to reveal?

## 11. Answers and reasoning

1. The official paths remain topic-centric and classic-based. Identify standard, GitHub Copilot and Copilot chat harnesses explicitly. The GitHub harness is generally available, individual capabilities can be preview, and standard/GitHub agents cannot be transferred between harnesses.
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
21. General Quality measures output quality and can penalize a justified refusal. Current evaluation also offers Content Safety and Custom grading, but neither a high general score nor those graders replace dedicated authorization, privacy, injection and responsible-AI testing.
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

37. Secure web access can take up to two hours to propagate and does not require publishing; the separate authentication change requires publishing. Test both plus data permissions.
38. No. Default rejection can end before the human stage. In example 2 only 70/100 reach it; inspect all decision and error paths.
39. Preview advanced approvals lack normal ALM transfer support and require recreation after import; reviewer membership and sharing also need testing.
40. Filter by caller permissions server-side, then rank/deduplicate. The combined custom-knowledge limit is 15 snippets; never send forbidden candidates to the model for filtering.
41. Current agents default to Responses/A2A. The standard-harness Foundry connector additionally needs Activity enabled through REST/SDK; portal labels alone are insufficient.
42. Maker mode can expose the maker's accessible data to callers without their own permissions. User mode follows the caller. Test the documented harness and identity together.
43. No. Pauses are probabilistic and can be missed. Enforce the approval separately and respect the documented computer-use limitations.
44. BYO prompts have a distinct endpoint and model support contract, currently chat completions and no GPT-5-or-later support. Managed catalog availability does not override it.
45. Only 80/100 cases were graded and 72/100 demonstrated a pass. Invalid/error cases and critical failures still need resolution; latency is a separate gate.
46. Six of 24 actual violations were missed. Precision and recall are 75%; calibrate against independently labeled examples and inspect false negatives.
47. Credits cover consumption/entitlement. Rate limits apply over specific windows and scopes, including downstream dependencies. Use observed peak data and reduce amplification.
48. Wrong table, initial export delay, unsupported unauthenticated/multitenant configuration, omitted topic events or telemetry loss. Check support and correlation before inferring inactivity.

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
- [Harnesses in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview)
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

## Blog reading with practical follow-through

- [Jason Moore — GitHub Copilot harness, skills and richer context](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/new-and-improved-github-copilot-harness-agent-skills-and-richer-context/) (September 2, 2026). Useful for understanding the current harness and release direction. Build a four-column worksheet: feature, harness, GA/preview status, and current implementation evidence. Include memory, connected agents, Fabric tools and environment telemetry. Treat the blog as discovery and the current feature page as implementation authority; do not transfer capabilities across harnesses.
- [Efrat Gilboa and Dikla Dotan-Cohen — Custom graders](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/custom-graders-in-copilot-studio-setting-high-standards-for-agent-evals/) (March 26, 2026). Its layers of general quality, expected outputs, organizational policy and behavior help identify missing tests. Write your own mutually exclusive, exhaustive labels, independently label a small synthetic set, then calculate example 5's confusion matrix. A reported vendor benchmark is not a guarantee for your agent, and grading does not enforce access controls.

## Places to learn

This is a curated starting point, not a complete list. Do **not** consume everything. Select the explanations, demonstrations, labs, and assessment signals that close your gaps, and keep the current official blueprint beside third-party material.

| Resource | Access | Estimated time |
|---|---|---:|
| Three official Microsoft Learn paths | Public | 11 modules; allow 8–12 hours plus exercises (editorial budget) |
| AB-620T00-A instructor-led course | Provider/schedule dependent | 3 days; available September 30, 2026 (scheduled; not yet delivered) |
| Ten labs in this guide | Platform usage may cost money | About 18–34 hours (editorial estimate) |
| Udemy AB-620 course by Kuljot Singh Bakshi | Paid | 9 hours 27 minutes plus labs/review |
| Udemy practice exams by Joshua Ravnjak | Paid | About 6–10 hours including explanation review |
| Microsoft Copilot Studio docs/guidance | Public | Select 4–12 hours by objective gap |

### Official course sequence

- [Design agent conversations and responses using topics](https://learn.microsoft.com/en-us/training/paths/design-agent-conversations-responses-topics-copilot-studio/) — three modules; older recorded runtime 2 hours 17 minutes, not reverified in the current outline.
- [Design and build multi-agent solutions](https://learn.microsoft.com/en-us/training/paths/design-build-multi-agent-solutions-copilot-studio/) — four modules; older recorded runtime 2 hours 54 minutes, not reverified in the current outline.
- [Integrate agents with enterprise systems](https://learn.microsoft.com/en-us/training/paths/integrate-agents-enterprise-systems-copilot-studio/) — four modules; older recorded runtime 3 hours 18 minutes, not reverified in the current outline.
- [AB-620T00-A](https://learn.microsoft.com/en-us/training/courses/ab-620t00) — three instructor-led days, listed as available September 30, 2026 (scheduled; not yet delivered).

The three live paths contain 3 + 4 + 4 = 11 modules. Their earlier recorded total was 8 hours 29 minutes; the current outlines do not expose a verified total runtime. Each currently identifies its modules as classic-experience content. Pair it with the current experience comparison, and do not infer that the future instructor-led course date delays the active exam or the self-paced paths.

### Additional instruction and assessment

- [AB-620: Copilot Studio AI Agent Builder Exam Prep](https://www.udemy.com/course/copilot-studio-ai-agent-builder/) by Kuljot Singh Bakshi — 9 hours 27 minutes, 64 lectures, shown in the indexed public catalog as updated August 2026 (12 sections). It includes hands-on coverage across Foundry, connectors/APIs/MCP, RAG, multi-agent design, Application Insights, evaluation, and ALM; verify current UI/preview behavior.
- [AB-620 Practice Exams: Copilot Studio AI Agent Builder](https://www.udemy.com/course/ab-620-practice-exams-copilot-studio-ai-agent-builder/) by Joshua Ravnjak — six 60-question tests (360 questions), shown as updated August 2026. Originality and exam-difficulty claims are the provider's, not independently audited. Its claimed 100-minute real-exam window conflicts with Microsoft's current 120 minutes; use the official duration. Allow about 6–10 hours for selected timed attempts and explanation/source review; use it as a secondary signal after hands-on work.
- [Copilot Studio documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/) and [architecture/guidance collection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/) — use exact pages by objective and verify whether each applies to classic, new, preview, or both.

Both retained Udemy pages blocked direct retrieval; the metadata above comes from indexed public provider pages checked September 28. No paid lessons/questions were opened. Bounded exact-exam searches did not verify a Pluralsight or LinkedIn Learning course; the other providers previously marked absent were not exhaustively searched again. Microsoft still explicitly reports no Practice Assessment. Broader videos are supporting demonstrations, not a verified AB-620 syllabus.

Avoid products that promise leaked, “actual,” or memorized exam questions. Original practice is useful only when explanations are checked against the current blueprint and Microsoft documentation.
