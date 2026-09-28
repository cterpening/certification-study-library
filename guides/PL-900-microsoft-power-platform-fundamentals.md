---
exam_code: PL-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# PL-900 Microsoft Power Platform Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 24, 2026 objectives and its cited public sources on September 28, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#pl-900-coverage-record). The [official PL-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900) is authoritative.

**Current baseline:** Skills measured as of July 24, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Official source:** [PL-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900)

## How to use this guide

Power Platform is easiest to remember as one business-solution system: Dataverse stores governed business data, connectors reach services, Power Apps supplies experiences, Power Automate coordinates work, and Copilot Studio creates agents. Learn which component owns each responsibility, then build one small end-to-end solution.

For every scenario, use this requirement-to-solution sequence:

1. **Outcome and users:** What measurable business result is needed, and who performs or owns the work?
2. **System of record:** Does data belong in Dataverse, an existing service, or another governed store?
3. **Experience:** Is the user best served by a canvas app, model-driven app, external site, code app, agent, or existing Microsoft 365 surface?
4. **Process:** Which steps are human decisions, cloud/API automation, desktop/UI automation, or agent-selected tools?
5. **Trust boundary:** Which identity, connection, permission, DLP policy, and environment controls each request and data movement?
6. **Lifecycle evidence:** How is the solution packaged, promoted, monitored, supported, evaluated, and retired?

The product named in the prompt is rarely the whole answer. “Build an approval app” can require an app for the user experience, Dataverse for the request record, a cloud flow for routing, a connector connection for each service, security roles for records, a solution/pipeline for deployment, and monitoring for failures.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

### Living-guide watch — September 28, 2026

Future Dynamics 365, Power Platform, and Dataverse items now move to the [AI at Work roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) through the [September 2026 transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/). Roadmap estimates help with discovery but do not redefine PL-900. Check the [Power Platform deprecation ledger](https://learn.microsoft.com/en-us/power-platform/important-changes-coming) before using older mobile-app, connector, or Power Virtual Agents exercises.

For current agent terminology, use the [GitHub Copilot Harness agent overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview). [Agent 365 GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) is adjacent governance context, not evidence that every individual Power Platform capability is GA. Independent learning sources later in the guide may explain concepts differently; verify product behavior against Microsoft documentation and exclude recalled-question material.

The [September deep-review report](../docs/research/2026-09-28-pl-900-deep-review.md) maps all 37 objectives. The exam baseline is unchanged; the updates below explain current product boundaries and add original practice scenarios. The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/) currently lists a 45-minute assessment.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe the business value of Microsoft Power Platform | 5–10% | How do the services combine to improve a process? |
| Manage the Microsoft Power Platform environment | 20–25% | How are data, security, environments, monitoring, and lifecycle governed? |
| Demonstrate the capabilities of Power Apps | 20–25% | Which app experience fits, and how is it built? |
| Demonstrate the capabilities of Power Automate | 20–25% | Which automation pattern fits, and how is it controlled? |
| Describe features and capabilities of agents in Microsoft Copilot Studio | 20–25% | How are conversational/agent experiences grounded, extended, tested, and governed? |

---

## 1. The Power Platform mental model

| Component | Primary job | Example |
|---|---|---|
| Power Apps | Build business applications | Mobile inspection canvas app or data-centric model-driven app |
| Power Automate | Automate workflows and desktop tasks | Route an approval, synchronize records, or automate a legacy desktop UI |
| Microsoft Dataverse | Governed business data and behavior | Accounts, requests, relationships, security, auditing |
| Microsoft Copilot Studio | Build and manage agents | Employee-support agent grounded in approved knowledge with actions |
| Power Pages | Build external-facing business websites | Supplier or citizen self-service portal |
| Connectors | Standard interface to a service/API | SharePoint, Outlook, SQL, or a custom internal API |
| Power BI | Analyze and visualize data | Operational dashboard and semantic model |

The products create the most value when the process, data, experience, automation, analytics, and agent are designed together. A canvas app can trigger a cloud flow; the flow can update Dataverse; a model-driven app can expose the same records; an agent can retrieve approved data and invoke an action.

Business value should be stated as an outcome rather than “we built an app.” Common value measures include cycle time, error/rework rate, completion rate, cost per case, adoption, user satisfaction, accessibility, containment, and compliance evidence. Establish a baseline and an owner before automation so that faster execution of a bad process is not mistaken for improvement.

Choose the smallest platform combination that meets the need:

| Requirement | Likely starting point | Question before adding more |
|---|---|---|
| Guided, role-aware work on related business records | Model-driven app + Dataverse | Can metadata-driven UI meet the experience need? |
| Highly tailored mobile/task experience | Canvas app | Can the source delegate required queries and can users access it? |
| Event, schedule, approval, or cross-service orchestration | Cloud flow | What identity, retry, duplicate, and failure behavior applies? |
| No supported API for a legacy desktop task | Desktop flow | Is UI automation's fragility and machine/session dependency acceptable? |
| Natural-language knowledge and actions | Copilot Studio agent | What knowledge, tool authority, escalation, and evaluation prove safe value? |
| External authenticated or anonymous self-service | Power Pages | How are website identity and Dataverse table permissions designed? |
| Developer-controlled web UI and code-first toolchain | Code app | Does the extra control justify engineering and lifecycle responsibility? |

Generative AI assists with planning, app creation, formulas, flows, agent instructions, and content. Generated artifacts remain subject to testing, permissions, data policy, accessibility, and lifecycle controls. The current blueprint includes Copilot-assisted and natural-language creation, but exact experiences change quickly. **VERIFY CURRENT:** maker UI, feature availability, licensing, regions, and preview status.

> **Related item:** Low code reduces the amount of custom code, not the need for architecture. A widely used low-code solution needs the same ownership, security review, change control, monitoring, support, and recovery thinking as conventional software.

---

## 2. Dataverse and data integration

### Dataverse concepts

Dataverse stores business data in tables. Standard tables provide reusable concepts; custom tables model organization-specific needs. Columns define values and types. Relationships connect records. Views define tabular presentations; forms define record experiences; business rules apply supported logic without code.

| Item | Purpose |
|---|---|
| Table | Business entity and its records |
| Column | Typed attribute such as date, choice, lookup, currency, or text |
| Choice | Reusable or local set of allowed values |
| Lookup/relationship | Connects one record to another |
| View | Defines columns, sorting, and filtering for a record list |
| Form | Defines how a record is displayed/edited |
| Business rule | Declarative validation or behavior under supported scope |
| Formula column/Power Fx | Calculates values using expression logic |

[Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intro) adds metadata, security, relationships, auditing, APIs, and solution-aware components beyond ordinary storage. It is not automatically the right answer for every list or file. Compare integration, transaction, scale, offline, existing-system, licensing, and governance requirements.

#### Dataverse versus a traditional database

A relational database and Dataverse can both represent tables, columns, keys, and relationships. Dataverse additionally supplies a business-application layer: standard tables, choices and lookups, forms/views, record ownership, role-based privileges, auditing, business rules, calculated/formula behavior, APIs, events, and solution packaging. Makers work through platform metadata and supported APIs rather than assuming direct database administration.

That convenience changes responsibility, not the need for design. Normalize enough to avoid conflicting facts, select ownership deliberately, define required/optional columns, choose one-to-many or many-to-many relationships based on the business, and identify alternate keys/duplicate rules where applicable. Avoid copying authoritative customer or financial data merely because creating a new table is easy.

Forms and views are presentation metadata. A form arranges how one record is viewed or edited; a view defines a filtered/sorted column set for lists. Neither replaces table privileges or row-level access. A business rule can express supported validation or behavior, while Power Fx can calculate values or app behavior; choose the layer that must enforce the rule for every entry path.

Power Fx is a low-code expression language with spreadsheet-like concepts. Formulas are declarative where possible: describe a value or behavior, and the platform recalculates it. Delegation matters in canvas apps: if an operation cannot be delegated to the data source, the client may process only a limited local subset and produce incomplete results. Use the [delegation overview](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview) and test representative volume.

AI can propose tables, columns, relationships, formulas, and apps, but generated structure is a hypothesis. Review names, types, requiredness, ownership, keys, relationship cardinality, duplicate behavior, sensitive-data classification, and whether an existing standard table or system of record should be reused. A plausible schema can still create data fragmentation or grant the wrong users access.

### Connectors and data movement

A connector exposes triggers and actions for a service. Standard and premium classifications affect licensing. Custom connectors wrap APIs not supplied by Microsoft. Connections hold authentication context; connection references allow solution components to point to environment-specific connections.

[Data loss prevention policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention) classify connectors into business, non-business, or blocked groups and constrain which can be combined. A DLP policy governs connector use; it does not classify every field or replace permissions in the source system. It also does not guarantee that a connector action is semantically safe—for example, an authorized business connector can still update the wrong record if flow logic is defective.

Trace integration as **component → connection reference → connection identity → connector/API → source authorization → record**. A maker may own the app while a service account or invoking user owns a connection. Document that execution identity because it determines whose permissions are used, who becomes an operational dependency, and what fails when credentials, consent, or employment changes.

> **Related item:** A connector proves that an integration can call an API; it does not prove the caller should see or change every record. Enforce authorization at Dataverse or the target service as well as in the user experience.

---

## 3. Environments, security, governance, and ALM

An [environment](https://learn.microsoft.com/en-us/power-platform/admin/environments-overview) is a boundary for apps, flows, agents, connections, policies, roles, and optionally a Dataverse database. Use separate environments to isolate lifecycle stages, business units, data/security requirements, geography, or risk. Environment location affects where its resources are hosted. The default environment supports broad personal productivity; it should not become an unmanaged production dependency.

Environment strategy is a portfolio decision. Define who may create environments, which types exist, how production is distinguished from trial/developer work, capacity and region expectations, DLP scope, owner/support metadata, backup/recovery needs, and retirement rules. Separation reduces accidental coupling but adds deployment and administration work.

### Security layers

| Layer | Control |
|---|---|
| Tenant/environment | Admin roles, environment access, managed-environment settings |
| Dataverse | Business units, teams, security roles, row ownership/sharing, column security |
| App/flow/agent | Sharing, co-owner/run-only access, channel and tool permissions |
| Connector/source | Connection identity, API scopes, source-system authorization |
| Data movement | DLP and tenant isolation controls |

Security roles contain privileges such as create, read, write, delete, append, append to, assign, and share at applicable access depths. App sharing does not automatically grant the underlying Dataverse or connector permission required to use the app.

Follow a data request through every layer:

1. Microsoft Entra authenticates the human or workload identity.
2. Environment and product sharing determine whether the identity can enter or use the component.
3. [Dataverse security](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds) evaluates roles, privileges, access depth, ownership, teams, sharing, and column security for the requested operation.
4. For external sources, the connection and target service apply their own identity, consent, scopes, and record permissions.
5. DLP determines whether connectors can be used together under policy; it does not grant access.
6. Audit and telemetry record supported activity for administration and investigation.

Separate maker/admin permission from end-user permission. A maker able to design a table or flow should not automatically read every production record, and an application user does not need customization rights merely to create a business record.

Managed Environments add governance capabilities for environments at scale. The Power Platform admin center supports environment, analytics, capacity, policy, security, and support operations. The CoE Starter Kit is a community-supported Microsoft collection that can help inventory and nurture adoption; it is not a substitute for the platform's native admin/security controls.

Dataverse privilege grants accumulate: assigning a narrow role does not subtract a broader grant from another role or team. Check the combined access before deciding that a user is restricted.

Classic data policies group connectors as Business, Non-Business, or Blocked where blocking is supported. [All applicable classic policies](https://learn.microsoft.com/en-us/power-platform/admin/dlp-combined-effect-multiple-policies) must allow the combination; one policy’s permission cannot override another’s block. [Advanced connector policies](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies) use an allowlist. Mixed mode applies both policy systems; ACP-only mode ignores classic policy evaluation for the scope. Current ACP coverage excludes custom, HTTP, and virtual connectors, so switching modes is not a universal migration shortcut. ACP is applied enforcement, including in mixed mode; it is not a report-only test. These controls restrict connector use and never grant source-data access.

### Solutions and lifecycle

[Solutions](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm) package components for transport and lifecycle. Unmanaged solutions are normally used while developing; managed solutions are normally distributed to downstream test/production environments. Environment variables externalize settings; connection references avoid hard-coding connections. [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) help promote solutions through environments.

```text
developer environment → source control/build → test → approval → production
       unmanaged                              managed downstream
```

Dependencies must be included or deliberately supplied. Test data/configuration separately from solution metadata. Establish owners, deployment identity, rollback path, versioning, and monitoring before a production release.

Follow a release as **author → solution → export/build validation → target pipeline stage → connection/environment configuration → managed deployment → smoke test → monitor**. A successful import proves that components deployed; it does not prove that references point to production resources, users have data permission, a flow is enabled, or the business scenario works. Treat configuration, reference data, and credentials as controlled deployment inputs rather than values embedded in formulas.

> **Related item:** Application lifecycle management includes retirement. Inventory consumers, export required records/evidence, revoke connections, remove sharing, and communicate replacement paths rather than merely deleting an app.

Pipelines move solution components and target configuration, including connection references and environment variables; they do not transport the business rows in Dataverse tables. Check the current pipeline environment and premium-use prerequisites before budgeting a deployment exercise. A developer environment and a production target have different requirements.

### Monitoring and accessibility

Use built-in analytics, flow run history, solution checker, app checker, [Monitor](https://learn.microsoft.com/en-us/power-apps/maker/monitor-overview), agent analytics, audit logs, and source-system telemetry as appropriate. A successful flow run proves that actions completed according to connector responses, not necessarily that the business outcome was correct. Combine technical signals—errors, latency, connector throttling, capacity—with business signals—records completed correctly, approval time, abandonment, and adoption.

[Accessible canvas apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/accessible-apps) require deliberate keyboard behavior, labels, color/contrast, focus order, screen behavior, error messaging, and testing with applicable assistive technologies. Model-driven and other generated experiences also require accessibility and usability validation. Platform accessibility support does not make a custom design automatically accessible, and legal/privacy obligations still depend on the organization's users, data, configuration, and jurisdiction.

---

## 4. Power Apps

### Choose an app type

| Type | Best fit | Tradeoff |
|---|---|---|
| Canvas app | Custom task-oriented layout across supported sources | Maker owns responsive design, delegation, navigation, and accessibility |
| Model-driven app | Process/data-heavy app on Dataverse | UI follows metadata and model; less pixel-level freedom |
| Power Pages site | External audience interacting with business data | Requires website identity, table permissions, content, and external security design |
| Code app | Developer-led web experience using Power Platform capabilities | More code/control and engineering lifecycle responsibility |

The July 2026 blueprint explicitly includes Plan designer, code apps, AI-assisted creation, and “vibe” style generation. [Plans in Power Apps](https://learn.microsoft.com/en-us/power-apps/maker/common/faq-plan-designer) can turn a described business problem into roles, requirements, data, and proposed Power Platform components. [Code apps](https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview) bring code-first web development and framework choice into a managed Power Platform context. The [Power Apps vibe experience](https://learn.microsoft.com/en-us/power-apps/vibe/overview) is an AI-native, prompt-driven experience that can generate requirements, data, logic, UI, and code-app artifacts. **VERIFY CURRENT:** preview status, labels, regions, languages, prerequisites, supported app types, generated components, limits, and ALM behavior are evolving.

These are not four names for the same artifact:

- **Plan designer/plans** explores the business problem and proposes an end-to-end solution model.
- **Canvas apps** give makers formula-driven control over screens and interactions.
- **Model-driven apps** derive much of the experience from Dataverse metadata and processes.
- **Code apps** give developers code-first UI and toolchain control while using supported Power Platform capabilities.
- **Vibe** is an AI-assisted creation experience that currently centers generated solution/app work; its outputs still need the same architecture, security, testing, and lifecycle review.

### Current app-building boundaries

As checked September 28, the Power Apps vibe overview still labels that experience **preview**, excludes the default environment, and lists English with supported regions including the United States, Australia, Asia, and India. Its banner points learners toward app building in Copilot Cowork and Copilot Studio. The [September 10 app-building announcement](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/build-apps-in-copilot-cowork-and-copilot-studio/) describes Cowork access through Frontier and a Copilot Studio public-preview rollout. Treat these as distinct experiences; a new announcement does not make every AI app-building feature generally available.

Plans help turn a business problem into requirements, roles, data, and proposed components. Review those artifacts before implementation. Code apps use a developer toolchain and support ordinary source control, but the current overview excludes **Power Platform Git integration** and secure implicit connections. The listed end-user licensing options include Premium, pay-as-you-go, app passes, or eligible license auto-claim; do not assume one universal license route. Check the environment feature setting and the app’s actual authentication path.

### Canvas apps

Canvas apps start from the desired experience. Screens contain controls; formulas define properties and behavior. Galleries show collections, forms view/edit records, and variables or collections hold state. Prefer direct, readable formulas and reusable components over copying logic across screens.

Common failure modes:

- a nondelegable formula appears correct on small test data but misses production rows;
- a shared app fails because users lack data-source permissions;
- a personal connection makes the maker a hidden production dependency;
- fixed positioning fails on other screen sizes;
- errors are swallowed without recovery or user guidance.

Trace a canvas request as **control event → Power Fx formula → connector → connection identity → source authorization → result → user feedback**. Delegation affects which records are evaluated; connector throttling affects reliability; sharing affects entry; the source decides data access. This helps diagnose a blank gallery more precisely than “Power Apps is broken.”

For a nondelegable query, the usual local row limit is **500**, configurable up to **2,000**. Increasing it cannot make an incomplete scan of a larger source correct. Delegation support depends on both the connector and the complete expression. Test with a qualifying row beyond the local limit.

### Model-driven apps

[Model-driven apps](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-driven-app-overview) start from Dataverse tables, relationships, forms, views, commands, dashboards, and process. They are effective for record-centric work, role-aware navigation, and consistent experiences. Business process flows guide users through stages; they do not replace all workflow automation or enforce every server-side rule.

Plan designer can help turn a business description into a proposed data and solution plan. Treat the output as a draft: validate tables, ownership, relationships, security, duplicate behavior, integration, and lifecycle before building.

> **Related item:** Power Pages is in the business-value objective even though it has no separate build domain in this blueprint. Know its value for external websites and preserve the boundary between site access, web roles/table permissions, Dataverse security, and anonymous versus authenticated design.

---

## 5. Power Automate

### Automation types

| Type | Trigger/control | Example |
|---|---|---|
| Automated cloud flow | Event occurs | When a request is created, notify and route it |
| Instant cloud flow | User manually starts it | Button submits a selected record for review |
| Scheduled cloud flow | Recurrence | Every night reconcile missing records |
| Desktop flow | Robotic process automation on a desktop/UI | Enter data into a legacy application without an API |
| Business process flow | Guides stages in a model-driven process | Qualify and advance a case through defined stages |

A trigger starts a [cloud flow](https://learn.microsoft.com/en-us/power-automate/overview-cloud); actions perform work; conditions and switches branch; loops repeat; variables hold state; scopes group actions. Expressions transform values. [Copilot can draft and modify a flow](https://learn.microsoft.com/en-us/power-automate/create-cloud-flow-using-copilot) from natural language, but makers must verify connector, trigger, condition, identity, error path, and recurrence behavior.

Follow an event-driven flow as **trigger event → trigger filters → connection identity → data retrieval → decision/loop → side effect → status update → run evidence**. Put filters as early as supported, avoid unnecessary loops, and know whether actions execute as the connection owner, invoking user, or another configured identity. A flow that starts successfully can still fail authorization at a later connector.

### Approvals and common integrations

[Approvals](https://learn.microsoft.com/en-us/power-automate/get-started-approvals) can request and record decisions through supported Microsoft experiences. Design who can approve, reassignment/delegation, timeout, escalation, comments/evidence, and what happens if the underlying record changes during the wait.

Teams, Outlook, SharePoint, Forms, and Dataverse are common sources and destinations. A form submission can trigger validation, create a Dataverse record, request approval in Teams, send email, and update status. Keep a stable business record rather than treating a chat message as the only audit evidence.

A cloud-flow run has a [30-day duration limit](https://learn.microsoft.com/en-us/power-automate/limits-and-config), including pending approvals. For longer business processes, Microsoft’s [long-running approval pattern](https://learn.microsoft.com/en-us/power-automate/modern-approvals) stores approval state in Dataverse and separates request creation from response handling. A process can last longer than any one run; make cancellation, expired requests, duplicate responses, and escalation explicit.

### Reliability and desktop automation

Use scopes plus “run after” conditions to create try/catch/finally-like handling. Make operations idempotent when retries could duplicate side effects. Record correlation identifiers and actionable error context. Do not build endless retries around permanent validation or authorization failures.

Desktop flows require machine registration, attended/unattended decisions, credentials, stable selectors, session availability, and recovery. UI automation is more fragile than an API integration; prefer a supported API/connector when it meets the requirement.

[Desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/introduction) operate against desktop and web interfaces, so separate the design-time flow from the runtime machine, Windows session, credential, gateway/network reachability, and target UI. An attended flow runs with user participation; an unattended design has different licensing and machine/session prerequisites. **VERIFY CURRENT:** desktop Copilot/AI Recorder availability, account requirements, regions, versions, licensing, and preview status.

Classify failures before retrying:

| Failure | Better response |
|---|---|
| Temporary connector timeout/throttling | Bounded retry with backoff where safe |
| Invalid input or missing required record | Validate, record actionable context, and route correction |
| Expired connection or denied permission | Stop and alert the connection/service owner |
| Duplicate trigger delivery | Use an idempotency key or check business state before the side effect |
| Desktop selector/UI changed | Capture diagnostic evidence and repair/retest the automation |
| Approval expired or approver unavailable | Apply defined timeout, reassignment, or escalation policy |

> **Related item:** Idempotency means a repeated request has the intended single business effect. It is essential when network timeouts leave the caller unsure whether an action completed.

---

## 6. Copilot Studio agents

The [Copilot Studio overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio) describes a low-code platform for agents and agent flows. An agent combines instructions, generative orchestration, topics, knowledge, tools/actions, channels, identity, analytics, and governance. Start with a bounded outcome and escalation path rather than a broad instruction to “help with anything.”

| Component | Purpose |
|---|---|
| Instructions | Agent role, behavior, limits, and response guidance |
| Topic | Authored conversational path for a recognizable intent/event |
| Knowledge | Approved sources used to ground responses |
| Tool/action | Operation the agent can call, including connector, flow, agent flow, or supported MCP tool |
| Channel | Where users interact, such as Teams or a website |
| Evaluation/analytics | Evidence of quality, usage, failures, and outcomes |

The July 2026 blueprint explicitly includes MCP, agent flows, Agent 365, monitoring, and evaluations. Learn the conceptual roles, and verify exact management surfaces and licensing against current [Copilot Studio documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/).

#### Follow one agent turn

1. A user or event enters through an approved channel and supplies identity/context available to that channel.
2. The runtime applies instructions and orchestration to select a topic, knowledge source, or tool.
3. Knowledge retrieval follows the selected source’s authentication rules. User-authenticated SharePoint retrieval and uploaded files have different access boundaries; verify the source before adding content.
4. The model composes a response or proposes a tool call; tool descriptions and schemas guide selection and arguments.
5. The connector, flow, MCP server, or downstream API performs its own authorization and validation before any side effect.
6. The agent returns a result, asks for clarification/confirmation, or escalates to a human path.
7. Conversation, tool, outcome, error, latency, safety, and adoption signals feed monitoring and evaluation under applicable privacy/retention rules.

Diagnose the first failed boundary. A retrieval miss is not fixed by granting the action more permission; a correct tool selection does not make its arguments authorized; a fluent answer does not prove grounding; a successful call does not prove the business outcome is correct.

### Topics, knowledge, and orchestration

Use topics when deterministic conversational control matters. Use generative answers against approved knowledge for flexible question answering. Generative orchestration can select topics, knowledge, and tools based on instructions and descriptions; precise names/descriptions improve selection.

Knowledge permission behavior must match the source and channel. The [knowledge-source matrix](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio) distinguishes user-authenticated sources from uploaded documents. In the standard harness, [files uploaded to generative-answer nodes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-documents) can inform answers for anyone chatting with the agent, regardless of the original file permissions. Upload only material appropriate for that audience; use a suitable authenticated source for restricted content. Test a user with less access than the maker.

### Tools and MCP

A tool description and schema tell the model how to call a capability. They do not authorize the business action. The connector/API/flow must validate identity, permissions, arguments, and policy. For side effects, consider preview/confirmation, approval, idempotency, timeout, rollback or compensation, and audit. Microsoft's [agent-tools guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-tools) distinguishes integrations including connectors, prompts, REST APIs, agent flows, and MCP.

MCP is a protocol for exposing tools and context to compatible AI clients. It expands integration possibilities and the trust boundary. Review server ownership, authentication, available tools, data destinations, supply chain, logging, and allowed environments.

[Agent flows](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview) can run as agent tools or standalone automation under supported triggers. Preserve the same flow concerns—identity, input/output schema, failure, capacity, idempotency, human review, and monitoring—rather than assuming an agent invocation makes an automation safe.

### Publish, monitor, and evaluate

Test normal, ambiguous, unsupported, unsafe, and unauthorized scenarios. Publish only to approved channels and confirm the channel's authentication and feature behavior. Monitor containment/resolution, escalation, tool success, latency, feedback, safety, cost, and business outcome. [Agent evaluation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro) makes test cases repeatable so changes can be compared; evaluation cases should include expected evidence and unacceptable outcomes, not only preferred wording. **VERIFY CURRENT:** harness, scoring methods, automation, profile behavior, language/region support, and preview status.

The current evaluation documentation applies to the **standard harness**, supports repeatable test sets and user profiles, and describes REST/flow automation. GCC has profile and similarity-method restrictions; Fabric data agents are currently excluded. Test chat and repeatable evaluations serve different purposes. Do not infer that an aggregate score proves correct authorization.

Agent flows also belong to the standard harness. Their control path is rule-based, but an AI action or changing external service can still produce variable results. Converting a solution-aware Power Automate flow to an agent flow changes its billing to Copilot Studio and is currently one-way. Do not use conversion as a casual practice toggle.

### Microsoft Agent 365 boundary

[Microsoft Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) is an organization-level control plane for observing, governing, and securing agents. Its purpose is different from authoring one Copilot Studio agent: registry/visibility, lifecycle and access governance, security/data protections, risk and health signals, and administration span an agent estate. The current overview records commercial general availability from May 1, 2026 and per-user licensing, with at least one qualifying licensed user required to enable the service. Check the feature/service description and tenant configuration before assuming a particular integration is available.

Remember the ownership boundary: Copilot Studio builds and operates an agent; Power Platform environments, solutions, DLP, and connectors govern its platform components; source systems enforce data/action authorization; Agent 365 adds cross-estate observability, governance, and security capabilities. These layers can integrate but do not collapse into one product.

> **Related item:** Agent quality has layers: retrieval may be relevant while the answer is ungrounded; the answer may be correct while the action is unauthorized; the action may succeed while the business outcome is wrong. Diagnose each layer separately.

---

## 7. Objective-to-scenario drill

| Scenario clue | Best starting capability | Boundary to explain |
|---|---|---|
| Tailored field-inspection UI over several supported sources | Canvas app | App sharing, source permissions, delegation, responsive/accessibility design |
| Role-based case management over related Dataverse records | Model-driven app | Forms/views shape experience; security roles and ownership govern data |
| Describe a process and obtain proposed roles, requirements, data, apps, flows, and agents | Plan designer/plans | AI output is a draft architecture, not an approved production solution |
| Build a framework-based web UI from a code-first IDE on Power Platform | Code app | Developer control adds code, dependency, testing, and ALM responsibility |
| External supplier submits and tracks requests | Power Pages | Website identity, web roles/table permissions, data privacy, and Dataverse boundary |
| Email arrival starts record creation and approval | Automated cloud flow | Trigger filtering, connection identity, errors, duplicates, timeout, and stable evidence |
| User selects a record and chooses “Submit” | Instant cloud flow | The invoking experience and run-only/connection configuration matter |
| Reconcile records every night | Scheduled cloud flow | Recurrence, time zone, overlap, idempotency, pagination, and failure alerting |
| Enter data in a legacy UI that has no usable API | Desktop flow | Machine, session, credential, selectors, attended/unattended choice, and fragility |
| Prevent a flow from combining business records with a consumer social connector | DLP policy | DLP controls connector combinations; it grants neither source access nor record permission |
| Transport app, flow, table metadata, and connection references to production | Solution + pipeline | Environment variables/references, managed deployment, dependencies, configuration, and smoke test |
| Answer policy questions and safely initiate a request | Copilot Studio knowledge + tool | Grounding, user access, tool authorization, confirmation, escalation, and evaluation |
| Standardize a live multi-step automation used by an agent | Agent flow | Explicit inputs/outputs and runtime controls remain necessary |
| Inventory, govern, observe, and secure agents across the organization | Microsoft Agent 365 | Estate-level control plane is distinct from building one agent |

#### Integrated scenario: employee equipment request

Decompose an employee request solution end to end:

1. Dataverse holds Request, Item, Approval, and fulfillment status records with deliberate ownership and relationships.
2. A canvas app offers a tailored employee experience; a model-driven app gives operations a record-centric queue. Each user still needs underlying permission.
3. An automated cloud flow validates the request, routes an approval, handles timeout/reassignment, and updates the stable business record. Connection identity and duplicate-trigger behavior are documented.
4. A Copilot Studio agent answers policy questions from approved knowledge and can invoke a bounded “draft request” tool. The tool validates the employee, allowed item, and amount before writing.
5. DLP constrains connector combinations; environments separate development/test/production; a solution, connection references, environment variables, and pipeline support deployment.
6. Technical monitoring finds failed runs and tool calls; business measures track cycle time, completion, exceptions, adoption, and satisfaction; agent evaluations test grounded, unauthorized, ambiguous, and escalation cases.

This is the platform value story: shared governed data, fit-for-purpose experiences, automation, and agents with one explicit security and lifecycle design—not simply the number of artifacts created.

---

## Worked examples

These are original learning scenarios. The calculations were checked locally; no tenant deployment or paid assessment was performed.

### 1. Measure value with a complete process

An equipment request takes 10 minutes manually. An app and flow reduce handling to 4 minutes, but a reviewer still spends 1 minute checking the outcome. The saving is `10 − (4 + 1) = 5 minutes`, or **25 hours for 300 requests**. Excluding the review would overstate the saving by 5 hours. Dataverse holds requests, a canvas app captures them, a cloud flow routes approval, and a model-driven app helps the equipment team manage a queue. An agent is optional if answering policy questions adds value. Time saved is a pilot observation, not a promised financial return.

### 2. A small demo hides a delegation error

Assume a stable source order of 2,500 rows. The 400 eligible requests occupy positions 2,101–2,500. A nondelegable filter over the first 500 or even 2,000 rows returns **zero**, although the correct result is **400**. Raising the cap covers 80% of the source but still misses 100% of the eligible records. A connector-supported server query evaluates the predicate against the full source. Reproduce the failure with a synthetic data set before choosing a formula; a collection containing only the first page cannot repair the missing data.

### 3. Sharing and grants answer different questions

Five employees can open an app. Only three have the required source permissions, so app sharing alone does not make the other two authorized. For one employee, an individual grant covers records `{A, B}` and a team grant covers `{B, C, D}`. Assuming the necessary table privileges, their combined record set is `{A, B, C, D}`—**four distinct records**, not five and not only B. A second narrow role does not revoke C or D. A policy that allows the connectors still does not grant any of these record rights.

### 4. A 45-day approval and repeated delivery

A request may await a decision for 45 days. One waiting cloud-flow run exceeds the 30-day limit by 15 days. Persist the approval/request identity and state, end the creation run, and handle the eventual response in another flow. Before acting, check whether the request is still pending and whether the responder may decide it. For 500 unique requests plus 20 repeat deliveries, the intended outcome is **500 business effects from 520 deliveries**. A simple “look up, then create” can race under concurrency: enforce uniqueness and an atomic state transition at the destination rather than claiming a flow check guarantees exactly-once processing.

### 5. A successful deployment can lack business data

A solution contains five components: a request table definition, a canvas app, a flow, a connection reference, and an environment variable. Development also contains 1,000 sample request rows. Deploying the solution does **not** copy those 1,000 business rows. Provision approved target data separately and bind the connection/environment settings to the correct target. A smoke test should prove that a new test request reaches the intended environment and that an ordinary user has appropriate rights; importing a managed solution alone does not prove either.

### 6. Read evaluation and adoption denominators

An agent passes 72 of 80 routine cases and 10 of 20 edge cases. Its overall score is **82%**, but the groups score **90%** and **50%**. Inspect the failures; even one unauthorized disclosure can fail a security requirement regardless of the average. Separately, 40 weekly active users out of 100 eligible users means **40% adoption**. If 60 of 80 answered sessions resolve the issue, that is **75% of answered sessions**; with 100 total sessions it is **60% of all sessions**. Define eligibility, session handling, and the resolution measure before comparing releases.

## 8. Practice labs

Use synthetic data and an approved development environment. Each lab has a paper/design alternative; live execution requires suitable access, licenses, and feature availability. Keep test artifacts separate from production and remove the lab’s own artifacts afterward.

| Lab | Steps and evidence | Expected result and failure case |
|---|---|---|
| 1. Equipment request model | Define Employee, Item, and Request tables; identify required columns, relationships, owner, and one validation rule. Draw the model or build it in Dataverse. | One employee can make many requests; a missing employee or invalid quantity is handled deliberately. Explain the difference between a form, view, and table. |
| 2. Plan and compare experiences | Write requirements for a mobile request screen and an operations queue. Propose canvas and model-driven experiences; optionally inspect an AI-generated plan. | Explain each choice and review generated relationships/security. Record the actual experience, region, language, and preview status before trying code/vibe generation. |
| 3. Delegation and accessibility | Use example 2’s 2,500-row fixture; compare local versus full-source filtering. In a canvas app, test keyboard navigation, labels, and an error state. | Detect the zero-versus-400 failure. A clean small demo is insufficient; a screen reader must identify the input and error without relying on color alone. |
| 4. Identity and policy | Draw separate app-sharing, Dataverse, connection, and connector-policy decisions for five users. Compare one broad and one narrow grant; evaluate two classic policies. | The allowed outcome satisfies every relevant layer. Explain why mixed ACP mode still enforces restrictions and why custom/HTTP coverage requires attention. |
| 5. Approval lifecycle | Model Pending, Approved, Rejected, Cancelled, and Expired states. Design request and response flows; add a duplicate response and a response after cancellation. | A late response does not revive a cancelled request. Persisted state survives a single run’s lifetime; destination enforcement prevents duplicate effects. |
| 6. Cloud versus desktop | Specify an API-triggered approval and a legacy UI-only task. Identify triggers, actions, connection identity, machine/session needs, and one failure signal. | Choose cloud automation when a suitable API exists; use desktop automation with an explicit runtime plan. Review Copilot-generated actions before saving/running. |
| 7. Deployment and monitoring | Package or diagram example 5’s solution; record development and target connection settings. Define a post-deploy smoke test and a failure alert with an owner. | Components/configuration move, business data needs its own plan. Detect an app accidentally bound to development and avoid placing credentials in ordinary settings. |
| 8. Agent with bounded knowledge and tools | Design a policy agent, one topic, an approved source, and a draft-request tool. Test allowed/denied users, ambiguity, tool rejection, and escalation; calculate example 6’s scores. | Uploaded-file knowledge is appropriate for the entire agent audience. The tool enforces identity and amount limits. Record harness/channel and evaluate both quality and access; do not convert a flow merely to explore billing. |

## 9. Knowledge checks and distinctions

These original questions follow the 37 objective bullets; they are not recalled exam questions.

| # | Question | Answer and reasoning |
|---:|---|---|
| 1 | What business value does a Power App provide? | A task-focused interface that improves a measured process; example 1 includes the remaining review work. |
| 2 | Where does Power Automate add value? | It coordinates repeatable events and actions across systems, including human decisions. |
| 3 | Why choose Dataverse? | Governed relational business data, reusable metadata, security, and logic support apps and automation. |
| 4 | What does a connector provide? | An interface to service operations; a connection supplies the configured identity and credentials. |
| 5 | When does Power Pages fit? | An external business website, with explicit authentication and table-permission design. |
| 6 | Does generated output remove design review? | No. Inspect the requirements, data, access, logic, and failure behavior before use. |
| 7 | When is an agent useful? | For bounded conversational knowledge or tasks with clear authority and escalation. |
| 8 | How does Dataverse differ from a bare relational database? | It combines storage with business metadata, security, logic, and integration with Power Platform. |
| 9 | How should employees and requests relate? | A lookup can express many requests for one employee; define required fields and deletion behavior. |
| 10 | Are views and forms new copies of the data? | No. They present selected records/columns and record interactions over the underlying tables. |
| 11 | Where can business logic live? | Rules, formulas/Power Fx, processes, and extensions have different execution scope; choose one that covers required entry paths. |
| 12 | What must you review after AI creates tables? | Names, types, relationships, required fields, sample data, ownership, and access assumptions. |
| 13 | Why separate development and production? | To control lifecycle, access, data, and changes without coupling experiments to business operations. |
| 14 | Does a narrow role remove a broad Dataverse grant? | No. Grants accumulate; identify and change the broad grant if it is inappropriate. |
| 15 | What supports privacy and accessibility? | Appropriate data access/movement controls plus usable labels, keyboard flow, contrast, and assistive-technology testing. |
| 16 | What should monitoring measure? | Usage, failures, latency, capacity, and business outcomes with clear denominators and ownership. |
| 17 | Do pipelines move all Dataverse business rows? | No. They deploy solutions and target configuration; data movement is separate. |
| 18 | When should you choose a canvas app? | When a tailored task or device experience matters; verify delegation and source access. |
| 19 | When should you choose a model-driven app? | For a Dataverse-centered record/process experience built from tables, forms, views, and navigation. |
| 20 | What does Plan designer contribute? | A reviewable business plan with roles, requirements, data, and proposed solution components. |
| 21 | Does code-app Git support imply Power Platform Git integration? | No. Ordinary developer source control and the platform integration are separate capabilities. |
| 22 | What follows an AI-generated canvas app? | Review formulas, delegation, data connections, accessibility, and permissions; then test realistic cases. |
| 23 | What follows an AI-generated model-driven app? | Review tables, forms, views, relationships, navigation, and security against user tasks. |
| 24 | Is every vibe/app-building experience GA? | No. Check the specific surface and release status; the Power Apps vibe overview remains preview in this review. |
| 25 | Cloud or desktop flow for an API-enabled service? | Usually cloud; use desktop automation when the required operation depends on a UI and account for its runtime. |
| 26 | Can one approval run wait 45 days? | Not within the documented 30-day cloud-run limit. Persist state and separate request/response handling. |
| 27 | What is a trigger versus an action? | The trigger starts the flow; actions do the subsequent work. |
| 28 | How do you use AI to create a cloud flow responsibly? | Specify an event and desired actions, inspect the proposed structure/connections, then test failure and success cases. |
| 29 | What must an AI-assisted desktop flow still handle? | Selectors, input validation, credentials, machine/session requirements, and UI changes or errors. |
| 30 | What makes an agent use case bounded? | A defined audience, allowed knowledge and operations, success criteria, and a handoff path. |
| 31 | What is a topic for? | An authored conversation path with questions, conditions, and controlled actions. |
| 32 | Do uploaded documents preserve their original file permissions? | Do not assume that. Standard-harness uploaded-file answers can be available to all users of the agent. |
| 33 | Does a tool or MCP schema authorize an action? | No. The service and connection must enforce identity, operation scope, input limits, and relevant confirmation. |
| 34 | What changes when publishing to a channel? | The user entry point and its authentication/capability behavior; retest the actual audience there. |
| 35 | How does Agent 365 differ from agent authoring? | It observes, governs, and secures an organizational agent estate. |
| 36 | Is 40 active users automatically good adoption? | Only with the eligible population and time window: 40 of 100 weekly eligible users is 40%. |
| 37 | Does an 82% evaluation score prove readiness? | No. Inspect cohorts, individual failures, access checks, and release criteria; example 6 has only 50% edge-case success. |

| Contrast | Remember |
|---|---|
| Canvas vs model-driven | Experience-first flexible UI versus data/process-first Dataverse UI |
| App sharing vs data permission | Access to app artifact versus access to underlying records/service |
| Dataverse vs connector | Governed business data platform versus service integration interface |
| Trigger vs action | Starts flow versus performs a step |
| Cloud flow vs desktop flow | API/service automation versus UI-based RPA |
| Business process flow vs cloud flow | Guides record stages versus automates service actions |
| Unmanaged vs managed solution | Development ownership versus controlled downstream distribution |
| Environment variable vs secret | Deploy-time configuration value/reference versus protected credential |
| Topic vs knowledge | Authored dialogue/control versus grounded information source |
| Tool schema vs authorization | Describes invocation versus permits operation |
| Analytics vs evaluation | Observed production behavior versus judged quality against cases |

### Readiness checklist

- [ ] I can explain how Power Apps, Automate, Dataverse, Copilot Studio, Pages, connectors, Power BI, and generative AI combine.
- [ ] I can model basic Dataverse tables, columns, relationships, forms, views, roles, and business logic.
- [ ] I can explain environments, DLP, security, monitoring, accessibility, solutions, and pipelines.
- [ ] I can choose canvas, model-driven, Power Pages, or code app by requirement.
- [ ] I can recognize delegation, data permission, connection, and responsive-design failures.
- [ ] I can choose automated, instant, scheduled, desktop, and business process flows.
- [ ] I can design approval, exception, retry, and idempotency behavior.
- [ ] I can explain agent instructions, topics, knowledge, tools, MCP, flows, channels, monitoring, and evaluation.
- [ ] I can separate generative assistance from human ownership and platform security.
- [ ] I checked all **VERIFY CURRENT** items and the current blueprint.

### Primary references

- [Official PL-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900)
- [Power Platform documentation](https://learn.microsoft.com/en-us/power-platform/)
- [Dataverse overview](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intro)
- [Power Apps documentation](https://learn.microsoft.com/en-us/power-apps/)
- [Power Automate documentation](https://learn.microsoft.com/en-us/power-automate/)
- [Copilot Studio documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/)
- [Power Platform ALM](https://learn.microsoft.com/en-us/power-platform/alm/)
- [Power Platform security and governance](https://learn.microsoft.com/en-us/power-platform/admin/security)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — PL-900 course](https://learn.microsoft.com/en-us/training/courses/pl-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Official foundation; the public overview still emphasizes apps, flows, and Power Pages, so use the July 2026 blueprint to check the agent/code/Plan-designer gaps |
| [Microsoft — PL-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/practice/assessment?assessment-type=practice&assessmentId=34&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; start here before buying another assessment |
| [Microsoft Partner Skilling Hub — LevelUp PL-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058317) | Partner login required | Current duration not verified | Public fetch returns a shell; confirm eligible-partner access and the current syllabus after sign-in |
| [Microsoft Learn Power Platform Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/) | Free | Self-paced; current total not published in the fetched overview | Use the credential page to find official preparation and practice; budget lab time separately |
| [Pluralsight — Power Platform Fundamentals (PL-900) and practice exam](https://www.pluralsight.com/paths/microsoft-power-platform-fundamentals-pl-900) | Subscription; practice access depends on plan/library | 8 hours 56 minutes of listed instruction; budget practice separately | Eight listed courses, dated 2024–2025; practice entitlement must be checked; much of the instruction predates the July 2026 agent/code/Plan-designer changes, so use selectively |
| [O'Reilly — Complete PL-900 Masterclass](https://www.oreilly.com/videos/the-complete-masterclass/9781805125044/) | Subscription | Previously listed 16 hours 40 minutes; current listing unverified | Direct access blocked in this review; retain only as an optional older companion, and verify the syllabus before purchase |
| [Udemy — PL-900 Power Platform Fundamentals](https://www.udemy.com/course/pl-900-microsoft-power-platform-fundamentals-r/) | Purchase or subscription | 11 hours 1 minute (public search listing) | Phillip Burton; public listing shows September 2026, 25 sections/132 lectures. Direct fetch blocked; July-objective coverage was not verified inside the paid course |
| [LinkedIn Learning — PL-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-power-platform-fundamentals-pl-900-cert-prep-by-microsoft-press) | Subscription | 6 hours | Craig Zacker course released March 2025; useful for core products but pre-dates the July 2026 agent/code/Plan-designer scope |
| [Power Platform Well-Architected](https://learn.microsoft.com/en-us/power-platform/well-architected/) | Free | Select 3–6 hours by gap | Related-item depth for reliability, security, operational excellence, performance, and experience |
| [Copilot Studio guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/) | Free | Select 3–6 hours by gap | Architecture, governance, security, ALM, testing, and business-value depth beyond fundamentals |
| [MeasureUp — PL-900 practice test](https://www.measureup.com/microsoft-practice-test-pl-900-microsoft-power-platform-fundamentals.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 120 questions; public last update is August 2025, so use the July 2026 blueprint for agent, Plan designer, and code-app deltas |
| [Whizlabs — PL-900 practice and videos](https://www.whizlabs.com/microsoft-power-platform-fundamentals-pl-900/) | Paid course or subscription | About 4–8 hours for assessment and review; course total not verified | Use the practice component for gap detection; current instructional runtime and July 2026 delta coverage were not independently verified |

The assessment products above supplement—not replace—explanatory learning and hands-on Power Platform work. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).

### Articles and additional practice worth considering

- [Build business apps with Copilot Cowork and Copilot Studio](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/build-apps-in-copilot-cowork-and-copilot-studio/) — Ryan Cunningham, September 10, 2026. Useful for comparing emerging app-building surfaces and the need for data connections, review, and governance. Preserve its Frontier/public-preview rollout distinctions; it does not change the exam blueprint or prove access in your tenant.
- [September 2026 Power Platform update](https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-september-2026-feature-update/) — selected app-building and learning sections are useful discovery pointers. Turn an AI-generated app plan into a review exercise, and check each feature’s specific current documentation before adopting a release-status claim.
- [Power CAT Power Series labs](https://aka.ms/PowerSeries/Labs) — Microsoft’s public workshop directory includes cloud-flow, RPA, app, and governance exercises. Start with a fundamentals scenario and inspect its prerequisites first. This review checked the directory listing, not individual instructions or successful execution; the series extends beyond PL-900.

Use the primary documentation for behavior and limits. Course update dates and blog announcements do not by themselves establish complete coverage of the current objectives.
