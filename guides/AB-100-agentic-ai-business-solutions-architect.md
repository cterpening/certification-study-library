---
exam_code: AB-100
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-30
---

# AB-100 Agentic AI Business Solutions Architect Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official AB-100 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100) is authoritative.

**Current baseline:** Skills measured as of July 22, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 30, 2026.<br>
**Official source:** [AB-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100)

## How to use this guide

AB-100 is an architecture exam. For every scenario, identify the desired business outcome, process boundary, data and identity path, agent autonomy, platform fit, operational owner, evidence, and lifecycle. Use the decision tables to compare plausible options, then complete the architecture exercises and defend your tradeoffs aloud.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Architect's job |
|---|---:|---|
| Plan AI-powered business solutions | 25–30% | Establish requirements, data readiness, strategy, portfolio, costs, and benefits |
| Design AI-powered business solutions | 25–30% | Select agent patterns, platforms, extensibility, applications, and integrations |
| Deploy AI-powered business solutions | 40–45% | Design monitoring, testing, ALM, security, governance, risk, and compliance |

The candidate is expected to understand Microsoft 365 Copilot, Copilot Studio, Microsoft Foundry and Foundry Tools, Power Platform, and core Dynamics 365 products. The role also connects business process design, responsible AI, open agent protocols, data governance, security, financial analysis, and adoption.

The AB-100 certification is positioned at the expert level. The certification page lists an eligible associate certification as a prerequisite; exam eligibility and certification-award requirements are different questions. **VERIFY CURRENT:** Check the current certification page for the accepted prerequisite list.

---

# 1. Think like an agentic business solutions architect

The architect does not begin with “Where can we add a chatbot?” Begin with the process and desired outcome:

```text
business outcome
   ↓
process, people, decisions, exceptions, and controls
   ↓
data, identity, systems of record, and integration
   ↓
agent responsibility and human responsibility
   ↓
platform, model, knowledge, tools, and channels
   ↓
security, governance, ALM, operations, adoption, and value
```

## Use an architecture decision record

For material choices, record:

- context and measurable outcome;
- requirements and constraints;
- options considered;
- selected option and rationale;
- security, privacy, residency, and compliance impact;
- cost and operational impact;
- assumptions and risks;
- validation evidence;
- owner and review trigger.

This prevents a polished demonstration from becoming an unexplained enterprise standard.

## Classify the work before assigning autonomy

| Work characteristic | Likely design implication |
|---|---|
| Deterministic, stable, regulated | Workflow/rules first; tightly bounded AI assistance |
| Ambiguous content synthesis | Generative reasoning with grounded evidence and review |
| Multi-system research | Agent with read tools, identity propagation, traceability |
| Repetitive reversible action | Bounded agent action with policy, monitoring, and recovery |
| Irreversible or high-impact decision | Human approval or human decision; agent provides evidence |
| Highly variable exception handling | Explicit escalation and case-management path |

An agentic-first design does not mean maximum autonomy. It means treating agents as first-class participants with defined responsibilities, tools, constraints, state, and accountability.

> **Related item:** Human-centered process redesign often matters more than automating an existing sequence. Remove unnecessary work, clarify ownership, and design exception paths before using AI to accelerate a flawed process.

---

# 2. Analyze requirements and grounding data

## Capture business and technical requirements together

Use scenarios and measurable acceptance criteria. Include:

- users, channels, accessibility, and languages;
- trigger, inputs, expected outputs, and volume;
- systems of record and actions;
- response-time and availability targets;
- permitted autonomy and approval points;
- legal, compliance, privacy, and residency constraints;
- failure, escalation, and manual-continuity requirements;
- value baseline and success measures;
- owner, support model, and retirement condition.

Separate hard constraints from preferences. A residency or segregation-of-duties requirement eliminates options; a preferred user interface usually ranks them.

## Assess whether an agent fits

Agents are useful where language, unstructured information, adaptive reasoning, and tools improve a process. They are a poor replacement for a simple form, exact calculation, deterministic rule, or unsupported attempt to avoid fixing data quality.

Ask:

1. What decision or action is being delegated?
2. What evidence does the agent need?
3. How does it know the evidence is current and authorized?
4. Which outcomes require a person?
5. How will errors be detected, contained, corrected, and learned from?
6. Can the original process continue during an outage?

## Evaluate grounding data

| Dimension | Question | Example control |
|---|---|---|
| Accuracy | Does the source reflect reality? | Steward review and reconciliation |
| Relevance | Does it answer this process's questions? | Curated scope and retrieval evaluation |
| Timeliness | Is it updated within the decision window? | Freshness objective and ingestion monitoring |
| Cleanliness | Is structure, duplication, labeling, or formatting usable? | Normalization and quality rules |
| Availability | Can the solution reach it reliably and legally? | Connector, network, entitlement, continuity plan |
| Authorization | Should this user/agent see each item? | Identity-aware retrieval and source permissions |
| Lineage | Can the output be traced to source/version? | Metadata, citations, audit trail |

Organize reusable business data with governed semantics, ownership, identifiers, permissions, retention, and stable interfaces so more than one AI system can use it safely. Copying uncontrolled documents into each agent creates divergent knowledge and access rules.

> **Related item:** Data products provide a useful model: a reusable dataset has an accountable owner, consumers, contract, quality measures, access policy, and lifecycle—not merely a storage location.

---

# 3. Design the enterprise AI strategy

## Apply the Cloud Adoption Framework as a change system

The Cloud Adoption Framework for AI connects strategy, planning, readiness, adoption, governance, management, and security. Translate it into decisions:

- define business motivations and outcomes;
- assess AI maturity, data, skills, risk, and platform readiness;
- prioritize a portfolio, not isolated demonstrations;
- establish landing zones, platform services, policy, and delivery patterns;
- deliver iteratively and measure outcomes;
- govern, secure, operate, and improve continuously.

Do not confuse a platform rollout with adoption. Adoption also needs process owners, champions, training, support, communications, feedback, and changed performance measures.

## Create an AI Center of Excellence that enables delivery

An AI Center of Excellence can own or coordinate:

| Capability | Typical outputs |
|---|---|
| Strategy and portfolio | Principles, use-case intake, prioritization, roadmap |
| Architecture and platform | Reference architectures, landing zones, approved patterns |
| Responsible AI and risk | Assessment tiers, control library, review and escalation |
| Data and integration | Grounding patterns, contracts, connectors, identity guidance |
| Engineering and ALM | Templates, evaluation gates, pipelines, reusable components |
| Operations and FinOps | SLOs, telemetry, capacity, cost attribution, incident patterns |
| Adoption and community | Training, champions, maker support, reusable examples |

Use a federated model where central standards and shared services support domain teams that retain process expertise. A purely central team can become a bottleneck; completely decentralized delivery can duplicate risk and cost.

> **Related item:** Platform engineering turns approved architecture into paved roads: reusable environments, connectors, policies, pipelines, telemetry, and templates make the safe path easier for delivery teams.

## Manage an agent portfolio

Use an intake process that records outcome, owner, affected users, data, integrations, autonomy, risk tier, expected value, cost range, and lifecycle. Remove duplicates and identify shared capabilities. Stage investment through discovery, prototype, controlled pilot, production, scale, and retirement gates.

Increase autonomy only when process clarity, data quality, controls, evaluation, and operational maturity support it. Pilot success with friendly users does not prove readiness for broad deployment.

---

# 4. Evaluate cost, value, and build/buy/extend choices

## Establish value before launch

Connect technical signals to business outcomes:

```text
agent quality and reliability
        ↓
process behavior: time, resolution, error, compliance
        ↓
business value: efficiency, quality, revenue, or strategic resilience
```

Choose a small balanced set:

- **adoption:** eligible users, active use, repeat use;
- **quality:** groundedness, successful task completion, error or escalation rate;
- **operations:** availability, latency, tool failures, incident rate;
- **process:** handling time, cycle time, deflection, rework;
- **business:** cost avoided, revenue affected, risk reduced, satisfaction;
- **safety/governance:** policy matches, approval compliance, access violations.

Establish the predeployment baseline and comparison method. Time saved is not automatically value if employees cannot redirect it productively or if quality declines.

## Calculate total cost of ownership

Include more than model tokens:

- licenses and consumption;
- model, search, storage, integration, network, and observability services;
- design, development, data preparation, testing, and migration;
- security, compliance, legal, and risk review;
- training, change management, support, and operations;
- remediation, human review, exception handling, and vendor management;
- replacement, portability, and retirement.

Model costs under normal, peak, growth, and degraded scenarios. Include uncertainty and sensitivity analysis instead of presenting one precise but fragile ROI number.

> **Related item:** FinOps assigns visibility and accountability to variable cloud/AI cost. Unit economics such as cost per successfully resolved case are more actionable than an undifferentiated monthly bill.

## Build, buy, or extend

| Option | Prefer when | Watch for |
|---|---|---|
| Use prebuilt AI/agent | Standard process and product-native data/actions fit | Configuration limits, licensing, roadmap, data boundary |
| Extend Microsoft 365 Copilot | Users work in Microsoft 365 and need organizational knowledge/actions | Declarative vs custom engine capability, deployment and admin approval |
| Build in Copilot Studio | Low-code orchestration, channels, connectors, topics/actions, managed operations fit | Environment/solution discipline, connector governance, complex-code boundaries |
| Build with Microsoft Foundry | Custom code, models, orchestration, evaluation, or Azure architecture is needed | Greater engineering and operational responsibility |
| Buy a third-party solution | Differentiated domain capability is available and integration is acceptable | Data use, identity, residency, assurance, exit, concentration risk |
| Build custom model | Proprietary task/data creates measurable advantage unmet by existing models | Data rights, training skill/cost, validation, security, drift, lifecycle |

The answer may be compositional: extend Microsoft 365 Copilot for the user experience, use Copilot Studio for business orchestration, call a Foundry-hosted capability, and retain Dynamics 365 as the system of record. Make ownership and telemetry across those boundaries explicit.

## Use model routing deliberately

A model router can select by task, sensitivity, modality, quality, cost, latency, availability, and region. Define eligible routes, evaluation thresholds, fallback, trace fields, and change control. Do not route sensitive data to a model merely because it is cheaper.

---

# 5. Design agents and choose the Microsoft platform

## Match platform to the experience and control required

| Platform/surface | Strong fit |
|---|---|
| Microsoft 365 Copilot agents | Bring knowledge and actions into Microsoft 365 experiences such as Teams and SharePoint |
| Copilot Studio | Low-code agents, topics, generative orchestration, connectors, agent flows, channels, managed environments |
| Microsoft Foundry Agent Service | Code-first/custom Azure agents, models, tools, orchestration, evaluation, and observability |
| Dynamics 365 AI and agents | Product-native finance, supply chain, sales, customer service, or contact-center processes |
| Power Apps with AI components | Task-oriented business application combining structured UI, process, and AI assistance |

Select the experience, system of record, required autonomy, extensibility, data boundary, engineering model, lifecycle, and operations together. Product affinity alone is not an architecture.

## Agent pattern catalog

| Pattern | Behavior | Essential controls |
|---|---|---|
| Prompt/response agent | Produces a response or transformation | Grounding, schema, content policy, review |
| Task agent | Completes a bounded multi-step task | Tool scope, validation, retries, termination |
| Autonomous agent | Acts from events or goals with less immediate direction | Budgets, approval thresholds, monitoring, kill switch |
| Conversational service agent | Maintains dialogue and resolves/escalates cases | Identity, knowledge permissions, channel context, handoff |
| Multi-agent system | Specialized agents coordinate | Orchestration, contracts, shared state, conflict and failure handling |

Define role, goal, instructions, knowledge, tools, memory, triggers, response contract, approval, escalation, and evaluation for every agent. For autonomous designs, specify start conditions, maximum scope, frequency, duplicate handling, and stop/disable mechanisms.

> **Related item:** A human-in-the-loop control is a workflow with an SLA, evidence, delegation, absence handling, and escalation. An “approval” step with no accountable reviewer can make the process less reliable, not more.

## Copilot Studio design

Use topics for deterministic conversational paths and business rules where explicit control matters. Design triggers, variables, conditions, questions, actions, error paths, and fallback. Generative orchestration is appropriate when the agent must select knowledge and actions flexibly, but its tools and policy still need hard boundaries.

### Natural-language approach selection

| Need | Approach |
|---|---|
| Known intents and controlled dialogue | Standard NLP/topic routing |
| Domain-specific intent/entity model | Conversational language understanding where justified |
| Flexible interpretation across knowledge and tools | Generative orchestration with evaluation and constraints |

Prompt actions need a clear task, inputs, trusted context, output format, safety behavior, and error contract. Keep business authorization outside the prompt.

Apply Power Platform Well-Architected pillars—reliability, security, operational excellence, performance efficiency, and experience optimization—to the entire intelligent workload.

## Design multi-agent responsibility

For each agent, document:

- capability and non-goals;
- input/output contract;
- identity and tool permissions;
- data and memory scope;
- handoff criteria and state ownership;
- timeout, retry, and compensation;
- audit and evaluation fields;
- human escalation.

A supervisor-worker pattern centralizes routing. Peer/event patterns can reduce central coupling but make state and conflict harder. Choose based on responsibility, not novelty.

---

# 6. Design extensibility and open-protocol boundaries

## Extend Microsoft 365 Copilot

Choose declarative or custom-engine approaches based on the required orchestration and hosting responsibility. Plan where users discover and invoke the agent, how organizational data is grounded, which actions are exposed, how admins approve/manage it, and how telemetry joins the wider operating model.

Teams and SharePoint are not only channels; they carry identity, collaboration context, permissions, and user expectations. Validate the agent against those host boundaries.

## Model Context Protocol and Agent2Agent

| Protocol idea | Primary relationship | Architecture concern |
|---|---|---|
| MCP | Model/agent client discovers and invokes tools, resources, or prompts from a server | Server trust, capabilities, authentication, tool authorization, input/output validation |
| A2A | Agents communicate and delegate across agent boundaries | Identity, capability discovery, task contract, state, trust, observability |

Do not treat protocol compatibility as trust. Approve servers/agents, authenticate connections, authorize each capability, minimize scopes, validate content, and monitor execution.

> **Related item:** Supply-chain governance applies to agent integrations. An MCP server, connector, plugin, model, or package can change independently, so inventory versions, ownership, provenance, permissions, and update policy.

## Computer use, reasoning, and voice

Computer-use agents interact with user interfaces when no suitable API exists. They are more fragile and harder to constrain than API integrations. Use isolated sessions, allowlisted destinations, bounded credentials, confirmations, screenshot/data controls, monitoring, and recovery. Prefer a supported API for reliable high-volume transactions.

Reasoning modes can improve complex task performance while increasing latency, cost, and opacity. Evaluate outcomes and enforce tool limits. Voice mode adds turn detection, interruption, transcript privacy, latency, and accessible alternative channels.

## Connect Power Apps and business processes

In a canvas app, keep structured inputs and confirmations visible when precision matters. Use AI to interpret or draft, then use Power Fx, flows, connectors, and server-side rules to enforce the business process. A generated response should not silently bypass validation that applies to manual entry.

---

# 7. Orchestrate Dynamics 365, Microsoft 365, and Power Platform capabilities

The objective is architectural fit, not memorizing every branded feature. Learn the business boundaries and current product capabilities.

| Workload family | Typical scenarios | Architecture questions |
|---|---|---|
| Sales/customer experience | Account research, opportunity support, correspondence, next actions | CRM permissions, business terms, connector actions, human ownership |
| Customer service/contact center | Knowledge, summarization, routing, response assistance, channel agents | Case context, identity, handoff, quality, recording and compliance |
| Finance | Reconciliation, guidance, collections, process assistance | Financial controls, segregation of duties, approval, audit |
| Supply chain | Planning, order/inventory exception analysis, guidance | Freshness, transaction safety, plant/region continuity |
| Microsoft 365 | Personal/team productivity, organizational knowledge, collaboration | Tenant permissions, agent management, Teams/SharePoint experience |
| Power Platform | Custom apps, workflows, prompts, AI hub, connectors | Environment, DLP, solution/ALM, maker governance |

Business terms and semantic definitions align an agent's language with the organization. Treat them as governed metadata with owners and change control. For connector-based actions, distinguish connection identity, user delegation, service identity, and the target system's authorization.

Use prebuilt agents when product-native data, process, and controls align. Customize or compose only to close a real gap. Unnecessary customization creates upgrade, test, and support obligations.

**VERIFY CURRENT:** Dynamics 365 agent names, preview status, licensing, region availability, customization surfaces, and Microsoft 365 deployment controls change quickly. Use current product documentation rather than memorizing a point-in-time catalog.

> **Related item:** A canonical business process and semantic layer reduce cross-agent contradiction. Without them, different agents can automate competing interpretations of the same customer, order, case, or approval state.

---

# 8. Monitor, test, and tune AI-powered business solutions

## Use an operational measurement stack

| Layer | Examples | Owner question |
|---|---|---|
| Platform | Availability, latency, capacity, connector/model errors | Is the service healthy? |
| Agent | Topic/tool selection, task completion, loops, escalations | Is the agent behaving as designed? |
| Quality/safety | Groundedness, relevance, harmful content, attack results | Is the behavior acceptable and safe? |
| Process | Cycle time, resolution, rework, exception rate | Did the process improve? |
| Business | Cost, revenue, risk, satisfaction, strategic outcome | Is the investment valuable? |

Correlate traces across Copilot Studio, Power Platform, Foundry, Microsoft 365, Dynamics 365, and external systems. Define a common request/case identifier where supported, while respecting privacy and product boundaries.

Use backlog and feedback as evidence, not as a vote count. Classify items into defects, data/knowledge gaps, prompt/orchestration issues, missing capability, training/adoption issues, policy conflicts, and feature requests. Prioritize by impact, frequency, risk, and strategic value.

## Build a layered test strategy

1. **Component tests:** topics, prompts, tools, connectors, actions, extraction.
2. **Model/agent evaluations:** representative quality, groundedness, safety, adversarial cases.
3. **Integration tests:** identities, permissions, data, APIs, error behavior.
4. **End-to-end tests:** multi-app business process and human handoff.
5. **Nonfunctional tests:** load, latency, continuity, accessibility, security, privacy.
6. **User acceptance:** process owners and representative users validate outcomes.
7. **Production verification:** controlled release, live monitoring, rollback triggers.

Prompt best practices are testable hypotheses. Validate task clarity, context, examples, grounding, output schema, edge cases, and refusal behavior against a versioned set. Custom models need acceptance criteria for quality, safety, bias, robustness, latency, cost, and drift.

> **Related item:** Chaos and resilience testing can cover tool timeouts, missing knowledge, expired credentials, unavailable models, and human-review backlog. The desired result may be safe degradation or escalation, not an uninterrupted answer.

## Tune the right layer

When an outcome fails, determine whether the cause is requirements, source data, retrieval, instructions, topic/routing, tool schema, connector, permissions, model, user experience, or process. Changing a prompt cannot repair stale source data or missing authorization.

---

# 9. Design ALM and environment strategy

## Treat the solution as a bundle of versioned artifacts

AI-powered business solutions can include:

- Copilot Studio agents, topics, prompts, agent flows, connectors, actions, and connections;
- Power Platform solutions, environment variables, policies, and dependent apps/flows;
- Foundry projects, agents, model deployments, tools, code, infrastructure, evaluations, and guardrails;
- schemas, grounding configuration, search indexes, reference data, and evaluation datasets;
- Dynamics 365 configuration and AI features;
- monitoring, alerts, runbooks, access roles, and documentation.

Assign an owner, repository or system of record, version, dependency map, promotion method, and rollback strategy to each artifact class.

## Environment design

Separate development, test, and production according to risk. Add integration/UAT, performance, regulated, geography, or maker zones when justified. Define:

- who may create, edit, approve, deploy, operate, and view data;
- which connectors/models/services are allowed;
- environment-specific endpoints, identities, and knowledge sources;
- data movement and masking rules;
- managed versus unmanaged solution use;
- pipeline gates and segregation of duties;
- capacity, monitoring, backup/export, and recovery.

Copilot Studio agents participate in Power Platform solutions and can be promoted through solution and pipeline practices. Do not promote development connection credentials or test knowledge references blindly into production.

## Data and model ALM

Data changes can alter behavior without code changing. Version schemas, preprocessing, curated corpora, embeddings/index definitions, tuning datasets, evaluation sets, and lineage. Define how deletions and permission changes propagate.

For a model or deployment update:

1. record the current baseline and dependency;
2. evaluate the candidate on representative and adversarial cases;
3. validate safety, latency, cost, and tool behavior;
4. use controlled rollout or parallel comparison where appropriate;
5. monitor release criteria;
6. retain a rollback or contingency path.

> **Related item:** Configuration drift is especially dangerous in AI systems because prompts, knowledge, policies, model versions, and connector permissions can change behavior outside an application-code deployment. Inventory and compare all material configuration.

---

# 10. Design responsible AI, security, governance, risk, and compliance

## Apply layered control

| Layer | Representative controls |
|---|---|
| Identity and access | Least privilege, workload/user identity, conditional access, role review |
| Data | Classification, DLP, encryption, residency, retention, permission-aware grounding |
| Model | Approved models, deployment restrictions, tuning-data controls, version/evaluation record |
| Agent | Bounded instructions, tools, memory, autonomy, budgets, approval, kill switch |
| Integration | Connector/MCP/A2A trust, scopes, validation, network controls, secrets |
| Content | Input/output safety, prompt-attack defenses, sensitive-data checks |
| Lifecycle | Risk assessment, testing, approval, monitoring, incident response, retirement |
| Evidence | Trace, audit trail, lineage, model/data/configuration change history |

## Use risk tiers

Risk classification can consider decision impact, autonomy, reversibility, users, sensitive data, external exposure, regulated context, model type, and integration power. Higher tiers require stronger independent review, validation, human oversight, monitoring, and release authority.

Map Microsoft Responsible AI principles to concrete requirements and evidence. Principles without owners, controls, tests, and exception handling cannot be audited.

## Defend against prompt manipulation

- separate trusted instructions from untrusted user and retrieved content;
- restrict tools and data to the minimum necessary;
- propagate user identity and authorization where required;
- validate arguments and outputs outside the model;
- screen direct and indirect attacks;
- require confirmation for consequential actions;
- cap time, tokens, steps, and spend;
- log attack signals and investigate repeated patterns;
- red-team the complete workflow.

> **Related item:** Threat modeling agents adds model-specific paths to familiar application threats. Draw data flows and trust boundaries first; then examine prompt injection, tool abuse, data exfiltration, denial of wallet, memory poisoning, and insecure output handling at each boundary.

## Validate residency and data movement

Map where prompts, retrieved data, model inputs/outputs, tool payloads, telemetry, evaluations, backups, and support data are processed and stored. Include third-party services and cross-agent calls. Confirm contractual and product commitments for the chosen configuration; do not infer residency from an Azure resource group's location alone.

## Preserve auditability

Record accountable identity, agent/configuration version, model deployment, data/source identifiers, tool/action, approval, timestamp, result, and correlation where feasible. Protect the log from unauthorized access and tampering. A detailed trace is useful for debugging; a controlled audit record supports accountability. Design both deliberately.

---

# 11. Architecture exercises

## Exercise 1: Sales research and action agent

Design an agent used in Teams that summarizes CRM and SharePoint evidence, drafts outreach, and can create a follow-up task. Compare extending Microsoft 365 Copilot, Copilot Studio, and a Foundry solution. Include identity, knowledge filters, tool authorization, approval, citations, telemetry, ALM, and value measures.

## Exercise 2: Multi-agent customer service

Create an orchestrator with knowledge, case, entitlement, and scheduling agents across Dynamics 365 and external services. Specify contracts, state, error paths, human handoff, privacy, channel continuity, end-to-end tests, and SLOs.

## Exercise 3: Finance autonomous process

Assess an autonomous reconciliation/reminder scenario. Define segregation of duties, transaction thresholds, model/rule boundaries, approvals, duplicate prevention, exception queues, audit evidence, regional continuity, and kill switch.

## Exercise 4: Agent portfolio and Center of Excellence

Design intake, risk tiering, reference patterns, maker zones, environment strategy, reusable connectors, evaluation gates, operational ownership, chargeback/showback, adoption support, and retirement review for 50 proposed agents.

## Exercise 5: Build-buy-extend decision

Compare a Dynamics 365 prebuilt capability, Microsoft 365 extension, Copilot Studio solution, Foundry custom agent, and third-party product for one process. Create a weighted decision matrix and five-year TCO range. Document assumptions and exit plan.

## Exercise 6: Cross-platform release

Design promotion for a solution containing a Copilot Studio agent, custom connector, Power Automate flow, Foundry tool, search index, and Dynamics 365 configuration. Define repositories, solutions, environment variables, identities, datasets, tests, approval, rollout, monitoring, and rollback.

---

# 12. Scenario checks and exam distinctions

## Knowledge checks

1. A team proposes an autonomous refund agent because its demo answers are accurate. Which process, authority, risk, and operational evidence is still missing?
2. A Copilot Studio agent gives users documents they cannot open in SharePoint. Where must authorization be fixed, and why is hiding citations insufficient?
3. A pilot saves time but production costs exceed the business case. Which unit economics and lifecycle costs should be examined?
4. An agent performs well in isolation but fails across Dynamics 365 and a third-party API. How should component, integration, and end-to-end tests differ?
5. A prompt was unchanged, but agent quality fell after a document and model update. Which configuration and lineage evidence should ALM provide?
6. An MCP server is technically compatible with the agent. What trust, identity, authorization, supply-chain, and monitoring decisions remain?
7. Two business units build similar agents with contradictory definitions. Which data-product, semantic, and Center of Excellence controls can help?

For each answer, state the outcome, architecture boundary, owner, decision, risk, evidence, deployment path, and rollback or escalation.

## Distinctions to explain without notes

| Contrast | Remember |
|---|---|
| AI-assisted vs agentic | Generates/supports work versus pursues bounded goals with state/tools |
| Task agent vs autonomous agent | User-invoked bounded task versus event/goal-driven action with less immediate direction |
| Workflow vs agent | Predetermined control flow versus model-mediated selection within guardrails |
| Prebuilt vs extend vs custom | Product-native capability versus added knowledge/actions versus owned solution |
| Microsoft 365 agent vs Copilot Studio vs Foundry | Productivity host versus low-code orchestration versus code-first Azure control |
| MCP vs A2A | Agent-to-tool/resource protocol versus agent-to-agent collaboration |
| Model quality vs business value | Output performance versus measurable process/organizational outcome |
| Monitoring vs evaluation vs audit | Operational state versus quality judgment versus accountable evidence |
| Prompt test vs end-to-end test | Model interaction versus complete process, data, integration, and human path |
| Environment variable vs secret | Deploy-time configuration reference versus protected credential material |
| Trace vs lineage | Execution path versus origin/change history of data/model/artifact |
| Safety filter vs authorization | Content classification versus permission to access or act |
| Data residency vs data sovereignty | Processing/storage location versus broader legal control and obligations |

## Readiness checklist

- [ ] I can assess agent fit, process impact, requirements, and grounding-data readiness.
- [ ] I can apply the Cloud Adoption Framework and define an enabling AI Center of Excellence.
- [ ] I can build a portfolio roadmap with risk tiers, value measures, adoption, and retirement.
- [ ] I can calculate TCO/ROI and decide when to use, extend, buy, build, or route models.
- [ ] I can choose across Microsoft 365 Copilot, Copilot Studio, Foundry, Power Platform, and Dynamics 365.
- [ ] I can design task, autonomous, prompt/response, conversational, and multi-agent patterns.
- [ ] I can design MCP, A2A, connectors, computer use, reasoning, voice, and channel boundaries safely.
- [ ] I can orchestrate AI features across core Dynamics 365 workload families without relying on stale product names.
- [ ] I can design telemetry, KPIs, feedback triage, evaluation, and complete test strategy.
- [ ] I can design environment, solution, data, model, agent, and cross-platform ALM.
- [ ] I can design responsible AI, security, governance, vulnerability mitigation, residency, access, and audit evidence.
- [ ] I know which licensing, product, preview, regional, protocol, and prerequisite details require current verification.

## Primary references

- [Official AB-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100)
- [Official AB-100 learning path](https://learn.microsoft.com/en-us/training/paths/architect-agentic-ai-business-solutions/)
- [AI Center of Excellence](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/center-of-excellence)
- [Microsoft 365 Copilot extensibility](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/)
- [Microsoft 365 Copilot agents overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-overview)
- [Manage Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/manage)
- [Copilot Studio guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/)
- [Copilot Studio agent architecture](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/architecture/components-of-agent-architecture)
- [Agent design canvas framework](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-design-canvas-framework)
- [Copilot Studio testing strategy](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase4)
- [Power Platform ALM](https://learn.microsoft.com/en-us/power-platform/alm/)
- [Create and manage Copilot Studio solutions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-overview)
- [Measure the impact of agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-business-value-measure-impact)

Recheck product names, agent availability, licensing, prerequisites, regions, protocol support, preview status, and deployment controls before the exam.

---

# Places to learn

This is a curated starting point, not a complete list. You are not meant to consume every resource. Start with the official blueprint, then pick the instructor, format, examples, and hands-on work that help you close specific gaps. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AB-100 course](https://learn.microsoft.com/en-us/training/courses/ab-100t00) and [11-module learning path](https://learn.microsoft.com/en-us/training/paths/architect-agentic-ai-business-solutions/) | Free self-study; instructor-led options vary | 3 days (official course) | Official architecture foundation across planning, design, and deployment; Microsoft notes it is preparatory rather than an exam-prep course |
| [Microsoft Partner Skilling Hub — LevelUp AB-100](https://www.skilling-hub.com/en-US/listing/o::levelup::2426785) | Partner login required | 10 hours | No additional cost for eligible Microsoft partners; self-paced coverage spans architecture, value, grounding, agent selection, extensibility, operations, ALM, governance, security, and exam preparation |
| [Microsoft Copilot Studio guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/) | Free | Select 4–8 hours by gap | Architecture, governance, testing, ALM, operations, and value guidance from the product team |
| [O'Reilly — AB-100 Crash Course with Tim Warner](https://www.oreilly.com/live-events/agentic-ai-business-solutions-architect-crash-course-exam-ab-100/0642572326043/) | Subscription or event access | 4 hours (published course length) | Certification-focused treatment of the full blueprint; verify the occurrence and current baseline |
| [Timothy Warner's public AB-100 repository](https://github.com/timothywarner-org/ab100) | Free | About 4–8 hours plus exercises | MIT-licensed public companion examples and course plan from Tim's O'Reilly live course; use with attribution and verify against current Microsoft documentation |
| [O'Reilly — Microsoft Copilot Studio Step by Step by Lisa Crosbie](https://www.oreilly.com/library/view/microsoft-copilot-studio/9780135491584/ch09.xhtml) | Subscription | About 8–12 hours reading/practice | Detailed Copilot Studio implementation reference, published December 2025; broader AB-100 architecture topics need other sources |
| [O'Reilly — Building Enterprise AI Agents](https://www.oreilly.com/videos/building-enterprise-ai/9781808080630/) | Subscription | 3 hours 24 minutes plus lab time | Supporting enterprise agent patterns; not an AB-100 objective checklist |
| [Whizlabs — AB-100 training, labs, and practice tests](https://www.whizlabs.com/microsoft-ab-100-agentic-ai-architect-certification/) | Paid course or subscription | About 25–30 hours for all 27 labs and 4 quizzes | Hands-on supplement with 22 hours 15 minutes of published lab time plus an estimated 3–6 hours for 165 questions and answer review; the current listing reports no video items |
| [Udemy — AB-100 preparation by Phillip Burton](https://www.udemy.com/course/ab-100-agentic-ai-business-solutions-architect-exam-preparation/) | Purchase or subscription | 10 hours 50 minutes | Course shown as updated June 2026; compare its claimed baseline with the July 22 blueprint |
| [Udemy — AB-100 preparation by Kuljot Singh Bakshi](https://www.udemy.com/course/ab-100-agentic-ai-business-solutions-architect-exam-prep/) | Purchase or subscription | 14 hours 9 minutes | Alternative course shown as updated June 2026; inspect previews and objective coverage before choosing |
| [Tim Warner — AB-100 review on YouTube](https://www.youtube.com/watch?v=MCIon6epv74) | Free | About 1 hour | Public orientation and study context from the O'Reilly course instructor; not a full replacement for official training |

No exact Pluralsight AB-100 certification path was verified during the August 31, 2026 review. The Whizlabs resource above is useful hands-on and assessment practice, but its current listing reports no video items, so pair it with explanatory instruction and the official blueprint. Practice-question-only products are intentionally not used as the primary learning recommendation. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
