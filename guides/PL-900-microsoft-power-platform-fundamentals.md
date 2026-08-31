---
exam_code: PL-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# PL-900 Microsoft Power Platform Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** This guide was checked against the July 24, 2026 objectives and its cited public sources on August 31, 2026. It may still contain errors or become outdated. The [official PL-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900) is authoritative.

**Current baseline:** Skills measured as of July 24, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
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

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe the business value of Microsoft Power Platform | 5–10% | How do the services combine to improve a process? |
| Manage the Microsoft Power Platform environment | 20–25% | How are data, security, environments, monitoring, and lifecycle governed? |
| Demonstrate the capabilities of Power Apps | 20–25% | Which app experience fits, and how is it built? |
| Demonstrate the capabilities of Power Automate | 20–25% | Which automation pattern fits, and how is it controlled? |
| Demonstrate the capabilities of Microsoft Copilot Studio agents | 20–25% | How are conversational/agent experiences grounded, extended, tested, and governed? |

---

# 1. The Power Platform mental model

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

# 2. Dataverse and data integration

## Dataverse concepts

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

### Dataverse versus a traditional database

A relational database and Dataverse can both represent tables, columns, keys, and relationships. Dataverse additionally supplies a business-application layer: standard tables, choices and lookups, forms/views, record ownership, role-based privileges, auditing, business rules, calculated/formula behavior, APIs, events, and solution packaging. Makers work through platform metadata and supported APIs rather than assuming direct database administration.

That convenience changes responsibility, not the need for design. Normalize enough to avoid conflicting facts, select ownership deliberately, define required/optional columns, choose one-to-many or many-to-many relationships based on the business, and identify alternate keys/duplicate rules where applicable. Avoid copying authoritative customer or financial data merely because creating a new table is easy.

Forms and views are presentation metadata. A form arranges how one record is viewed or edited; a view defines a filtered/sorted column set for lists. Neither replaces table privileges or row-level access. A business rule can express supported validation or behavior, while Power Fx can calculate values or app behavior; choose the layer that must enforce the rule for every entry path.

Power Fx is a low-code expression language with spreadsheet-like concepts. Formulas are declarative where possible: describe a value or behavior, and the platform recalculates it. Delegation matters in canvas apps: if an operation cannot be delegated to the data source, the client may process only a limited local subset and produce incomplete results. Use the [delegation overview](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview) and test representative volume.

AI can propose tables, columns, relationships, formulas, and apps, but generated structure is a hypothesis. Review names, types, requiredness, ownership, keys, relationship cardinality, duplicate behavior, sensitive-data classification, and whether an existing standard table or system of record should be reused. A plausible schema can still create data fragmentation or grant the wrong users access.

## Connectors and data movement

A connector exposes triggers and actions for a service. Standard and premium classifications affect licensing. Custom connectors wrap APIs not supplied by Microsoft. Connections hold authentication context; connection references allow solution components to point to environment-specific connections.

[Data loss prevention policies](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention) classify connectors into business, non-business, or blocked groups and constrain which can be combined. A DLP policy governs connector use; it does not classify every field or replace permissions in the source system. It also does not guarantee that a connector action is semantically safe—for example, an authorized business connector can still update the wrong record if flow logic is defective.

Trace integration as **component → connection reference → connection identity → connector/API → source authorization → record**. A maker may own the app while a service account or invoking user owns a connection. Document that execution identity because it determines whose permissions are used, who becomes an operational dependency, and what fails when credentials, consent, or employment changes.

> **Related item:** A connector proves that an integration can call an API; it does not prove the caller should see or change every record. Enforce authorization at Dataverse or the target service as well as in the user experience.

---

# 3. Environments, security, governance, and ALM

An [environment](https://learn.microsoft.com/en-us/power-platform/admin/environments-overview) is a boundary for apps, flows, agents, connections, policies, roles, and optionally a Dataverse database. Use separate environments to isolate lifecycle stages, business units, data/security requirements, geography, or risk. Environment location affects where its resources are hosted. The default environment supports broad personal productivity; it should not become an unmanaged production dependency.

Environment strategy is a portfolio decision. Define who may create environments, which types exist, how production is distinguished from trial/developer work, capacity and region expectations, DLP scope, owner/support metadata, backup/recovery needs, and retirement rules. Separation reduces accidental coupling but adds deployment and administration work.

## Security layers

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

## Solutions and lifecycle

[Solutions](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm) package components for transport and lifecycle. Unmanaged solutions are normally used while developing; managed solutions are normally distributed to downstream test/production environments. Environment variables externalize settings; connection references avoid hard-coding connections. [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) help promote solutions through environments.

```text
developer environment → source control/build → test → approval → production
       unmanaged                              managed downstream
```

Dependencies must be included or deliberately supplied. Test data/configuration separately from solution metadata. Establish owners, deployment identity, rollback path, versioning, and monitoring before a production release.

Follow a release as **author → solution → export/build validation → target pipeline stage → connection/environment configuration → managed deployment → smoke test → monitor**. A successful import proves that components deployed; it does not prove that references point to production resources, users have data permission, a flow is enabled, or the business scenario works. Treat configuration, reference data, and credentials as controlled deployment inputs rather than values embedded in formulas.

> **Related item:** Application lifecycle management includes retirement. Inventory consumers, export required records/evidence, revoke connections, remove sharing, and communicate replacement paths rather than merely deleting an app.

## Monitoring and accessibility

Use built-in analytics, flow run history, solution checker, app checker, [Monitor](https://learn.microsoft.com/en-us/power-apps/maker/monitor-overview), agent analytics, audit logs, and source-system telemetry as appropriate. A successful flow run proves that actions completed according to connector responses, not necessarily that the business outcome was correct. Combine technical signals—errors, latency, connector throttling, capacity—with business signals—records completed correctly, approval time, abandonment, and adoption.

[Accessible canvas apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/accessible-apps) require deliberate keyboard behavior, labels, color/contrast, focus order, screen behavior, error messaging, and testing with applicable assistive technologies. Model-driven and other generated experiences also require accessibility and usability validation. Platform accessibility support does not make a custom design automatically accessible, and legal/privacy obligations still depend on the organization's users, data, configuration, and jurisdiction.

---

# 4. Power Apps

## Choose an app type

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

## Canvas apps

Canvas apps start from the desired experience. Screens contain controls; formulas define properties and behavior. Galleries show collections, forms view/edit records, and variables or collections hold state. Prefer direct, readable formulas and reusable components over copying logic across screens.

Common failure modes:

- a nondelegable formula appears correct on small test data but misses production rows;
- a shared app fails because users lack data-source permissions;
- a personal connection makes the maker a hidden production dependency;
- fixed positioning fails on other screen sizes;
- errors are swallowed without recovery or user guidance.

Trace a canvas request as **control event → Power Fx formula → connector → connection identity → source authorization → result → user feedback**. Delegation affects which records are evaluated; connector throttling affects reliability; sharing affects entry; the source decides data access. This helps diagnose a blank gallery more precisely than “Power Apps is broken.”

## Model-driven apps

[Model-driven apps](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-driven-app-overview) start from Dataverse tables, relationships, forms, views, commands, dashboards, and process. They are effective for record-centric work, role-aware navigation, and consistent experiences. Business process flows guide users through stages; they do not replace all workflow automation or enforce every server-side rule.

Plan designer can help turn a business description into a proposed data and solution plan. Treat the output as a draft: validate tables, ownership, relationships, security, duplicate behavior, integration, and lifecycle before building.

> **Related item:** Power Pages is in the business-value objective even though it has no separate build domain in this blueprint. Know its value for external websites and preserve the boundary between site access, web roles/table permissions, Dataverse security, and anonymous versus authenticated design.

---

# 5. Power Automate

## Automation types

| Type | Trigger/control | Example |
|---|---|---|
| Automated cloud flow | Event occurs | When a request is created, notify and route it |
| Instant cloud flow | User manually starts it | Button submits a selected record for review |
| Scheduled cloud flow | Recurrence | Every night reconcile missing records |
| Desktop flow | Robotic process automation on a desktop/UI | Enter data into a legacy application without an API |
| Business process flow | Guides stages in a model-driven process | Qualify and advance a case through defined stages |

A trigger starts a [cloud flow](https://learn.microsoft.com/en-us/power-automate/overview-cloud); actions perform work; conditions and switches branch; loops repeat; variables hold state; scopes group actions. Expressions transform values. [Copilot can draft and modify a flow](https://learn.microsoft.com/en-us/power-automate/create-cloud-flow-using-copilot) from natural language, but makers must verify connector, trigger, condition, identity, error path, and recurrence behavior.

Follow an event-driven flow as **trigger event → trigger filters → connection identity → data retrieval → decision/loop → side effect → status update → run evidence**. Put filters as early as supported, avoid unnecessary loops, and know whether actions execute as the connection owner, invoking user, or another configured identity. A flow that starts successfully can still fail authorization at a later connector.

## Approvals and common integrations

[Approvals](https://learn.microsoft.com/en-us/power-automate/get-started-approvals) can request and record decisions through supported Microsoft experiences. Design who can approve, reassignment/delegation, timeout, escalation, comments/evidence, and what happens if the underlying record changes during the wait.

Teams, Outlook, SharePoint, Forms, and Dataverse are common sources and destinations. A form submission can trigger validation, create a Dataverse record, request approval in Teams, send email, and update status. Keep a stable business record rather than treating a chat message as the only audit evidence.

## Reliability and desktop automation

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

# 6. Copilot Studio agents

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

### Follow one agent turn

1. A user or event enters through an approved channel and supplies identity/context available to that channel.
2. The runtime applies instructions and orchestration to select a topic, knowledge source, or tool.
3. Knowledge retrieval returns evidence the user is permitted to access under the configured source and authentication behavior.
4. The model composes a response or proposes a tool call; tool descriptions and schemas guide selection and arguments.
5. The connector, flow, MCP server, or downstream API performs its own authorization and validation before any side effect.
6. The agent returns a result, asks for clarification/confirmation, or escalates to a human path.
7. Conversation, tool, outcome, error, latency, safety, and adoption signals feed monitoring and evaluation under applicable privacy/retention rules.

Diagnose the first failed boundary. A retrieval miss is not fixed by granting the action more permission; a correct tool selection does not make its arguments authorized; a fluent answer does not prove grounding; a successful call does not prove the business outcome is correct.

## Topics, knowledge, and orchestration

Use topics when deterministic conversational control matters. Use generative answers against approved knowledge for flexible question answering. Generative orchestration can select topics, knowledge, and tools based on instructions and descriptions; precise names/descriptions improve selection.

Knowledge permission behavior must match the source and channel. Test a user with less access than the maker. A correct answer can still be a security failure if it uses content the user should not retrieve.

## Tools and MCP

A tool description and schema tell the model how to call a capability. They do not authorize the business action. The connector/API/flow must validate identity, permissions, arguments, and policy. For side effects, consider preview/confirmation, approval, idempotency, timeout, rollback or compensation, and audit. Microsoft's [agent-tools guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-tools) distinguishes integrations including connectors, prompts, REST APIs, agent flows, and MCP.

MCP is a protocol for exposing tools and context to compatible AI clients. It expands integration possibilities and the trust boundary. Review server ownership, authentication, available tools, data destinations, supply chain, logging, and allowed environments.

[Agent flows](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview) can run as agent tools or standalone automation under supported triggers. Preserve the same flow concerns—identity, input/output schema, failure, capacity, idempotency, human review, and monitoring—rather than assuming an agent invocation makes an automation safe.

## Publish, monitor, and evaluate

Test normal, ambiguous, unsupported, unsafe, and unauthorized scenarios. Publish only to approved channels and confirm the channel's authentication and feature behavior. Monitor containment/resolution, escalation, tool success, latency, feedback, safety, cost, and business outcome. [Agent evaluation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro) makes test cases repeatable so changes can be compared; evaluation cases should include expected evidence and unacceptable outcomes, not only preferred wording. **VERIFY CURRENT:** harness, scoring methods, automation, profile behavior, language/region support, and preview status.

## Microsoft Agent 365 boundary

[Microsoft Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) is an organization-level control plane for observing, governing, and securing agents. Its purpose is different from authoring one Copilot Studio agent: registry/visibility, lifecycle and access governance, security/data protections, risk and health signals, and administration span an agent estate. **VERIFY CURRENT:** availability, prerequisites, licenses, supported agents, registry/onboarding behavior, and integrations.

Remember the ownership boundary: Copilot Studio builds and operates an agent; Power Platform environments, solutions, DLP, and connectors govern its platform components; source systems enforce data/action authorization; Agent 365 adds cross-estate observability, governance, and security capabilities. These layers can integrate but do not collapse into one product.

> **Related item:** Agent quality has layers: retrieval may be relevant while the answer is ungrounded; the answer may be correct while the action is unauthorized; the action may succeed while the business outcome is wrong. Diagnose each layer separately.

---

# 7. Objective-to-scenario drill

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

### Integrated scenario: employee equipment request

Decompose an employee request solution end to end:

1. Dataverse holds Request, Item, Approval, and fulfillment status records with deliberate ownership and relationships.
2. A canvas app offers a tailored employee experience; a model-driven app gives operations a record-centric queue. Each user still needs underlying permission.
3. An automated cloud flow validates the request, routes an approval, handles timeout/reassignment, and updates the stable business record. Connection identity and duplicate-trigger behavior are documented.
4. A Copilot Studio agent answers policy questions from approved knowledge and can invoke a bounded “draft request” tool. The tool validates the employee, allowed item, and amount before writing.
5. DLP constrains connector combinations; environments separate development/test/production; a solution, connection references, environment variables, and pipeline support deployment.
6. Technical monitoring finds failed runs and tool calls; business measures track cycle time, completion, exceptions, adoption, and satisfaction; agent evaluations test grounded, unauthorized, ambiguous, and escalation cases.

This is the platform value story: shared governed data, fit-for-purpose experiences, automation, and agents with one explicit security and lifecycle design—not simply the number of artifacts created.

---

# 8. End-to-end lab

Build a small request-management solution in a developer environment:

1. Model Request and Request Type tables in Dataverse with ownership and status choices.
2. Create a model-driven app for administrators and a small responsive canvas experience for requesters.
3. Add a cloud flow that validates, routes approval, updates status, and handles timeout/failure.
4. Create an agent grounded in public policy documents that can retrieve request status and initiate a safe draft action.
5. Apply an environment strategy, DLP choice, security roles, solution, environment variables, and connection references.
6. Test two roles, nondelegable queries, denied data, repeated flow triggers, prompt injection, accessibility, and rollback.
7. Use analytics/run history to diagnose one introduced failure.

Record every component, owner, identity, connection, data path, license assumption, monitoring signal, and lifecycle decision.

---

# 9. Knowledge checks and distinctions

1. A canvas app is shared, but users cannot read records. Which layer is incomplete?
2. A maker filters 100,000 source records using a nondelegable function. Why did testing with 50 rows hide the problem?
3. An approval waits for a manager who leaves. Which process controls are missing?
4. A DLP policy permits two business connectors. Does that grant the flow access to their data?
5. An agent calls a well-described refund tool. Where must authorization and amount limits be enforced?
6. A managed solution is deployed, but a connection still targets development. Which ALM abstraction was missed?

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

## Readiness checklist

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

## Primary references

- [Official PL-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900)
- [Power Platform documentation](https://learn.microsoft.com/en-us/power-platform/)
- [Dataverse overview](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intro)
- [Power Apps documentation](https://learn.microsoft.com/en-us/power-apps/)
- [Power Automate documentation](https://learn.microsoft.com/en-us/power-automate/)
- [Copilot Studio documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/)
- [Power Platform ALM](https://learn.microsoft.com/en-us/power-platform/alm/)
- [Power Platform security and governance](https://learn.microsoft.com/en-us/power-platform/admin/security)

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — PL-900 course](https://learn.microsoft.com/en-us/training/courses/pl-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation across environment, apps, automation, and agents |
| [Microsoft — PL-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/practice/assessment?assessment-type=practice&assessmentId=34&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; start here before buying another assessment |
| [Microsoft Partner Skilling Hub — LevelUp PL-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058317) | Partner login required | 10 hours | No additional cost for eligible Microsoft partners; use a work account associated with the partner organization |
| [Microsoft Learn Power Platform Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/) | Free | About 10–14 hours | Official modules and practice; build an end-to-end developer-environment project alongside them |
| [Pluralsight — Power Platform Fundamentals (PL-900) and practice exam](https://www.pluralsight.com/paths/microsoft-power-platform-fundamentals-pl-900) | Subscription; practice access depends on plan/library | 9 hours plus about 2–4 hours for assessment/review | Eight-course path whose public page includes a practice exam; much of the instruction predates the July 2026 agent/code/Plan-designer changes, so use selectively |
| [O'Reilly — Complete PL-900 Masterclass](https://www.oreilly.com/videos/the-complete-masterclass/9781805125044/) | Subscription | 16 hours 40 minutes | Broad implementation course published November 2023; use for durable basics, then fill 2026 objectives from Learn |
| [Udemy — PL-900 Power Platform Fundamentals](https://www.udemy.com/course/pl-900-microsoft-power-platform-fundamentals-r/) | Purchase or subscription | About 11 hours | Phillip Burton course shown as updated August 2026; inspect current Copilot Studio and environment coverage |
| [LinkedIn Learning — PL-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-power-platform-fundamentals-pl-900-cert-prep-by-microsoft-press) | Subscription | 6 hours | Craig Zacker course released March 2025; useful for core products but pre-dates the July 2026 agent/code/Plan-designer scope |
| [Power Platform Well-Architected](https://learn.microsoft.com/en-us/power-platform/well-architected/) | Free | Select 3–6 hours by gap | Related-item depth for reliability, security, operational excellence, performance, and experience |
| [Copilot Studio guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/) | Free | Select 3–6 hours by gap | Architecture, governance, security, ALM, testing, and business-value depth beyond fundamentals |
| [MeasureUp — PL-900 practice test](https://www.measureup.com/microsoft-practice-test-pl-900-microsoft-power-platform-fundamentals.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 120 questions; public last update is August 2025, so use the July 2026 blueprint for agent, Plan designer, and code-app deltas |
| [Whizlabs — PL-900 practice and videos](https://www.whizlabs.com/microsoft-power-platform-fundamentals-pl-900/) | Paid course or subscription | About 4–8 hours for assessment and review; course total not verified | Use the practice component for gap detection; current instructional runtime and July 2026 delta coverage were not independently verified |

The assessment products above supplement—not replace—explanatory learning and hands-on Power Platform work. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
