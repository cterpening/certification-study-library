---
exam_code: AB-100
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-27
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-27
---

# AB-100 Agentic AI Business Solutions Architect Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The complete guide, objective coverage, selected implementation claims, exercises, and citations were reviewed on September 27, 2026. Exercises were reviewed as architecture/tabletop work; no tenant deployments or paid course contents were tested. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-100-coverage-record) and [deep-review findings](../docs/research/2026-09-27-ab-100-deep-review.md). The [official AB-100 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100) is authoritative.

**Current baseline:** Skills measured as of July 22, 2026<br>
**Upcoming blueprint change (checked September 27, 2026):** The English revision is effective October 14, 2026. A complete comparison with the saved July outline found the same objective groups and weights; two bullets add “Microsoft” before Foundry Tools and one capitalizes “Service.” The public page now displays the October outline. The July snapshot remains the historical baseline; these editorial changes do not establish a new domain. Localized updates can follow a different schedule; check the [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-100/) for your appointment.<br>
**Official source:** [AB-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100)

> **Credential name checked September 27, 2026:** Microsoft now lists **Agentic AI Business Solutions Architect Expert**. The exam code remains AB-100. Passing the exam and earning the credential are separate: the existing associate-certification prerequisite still needs to be satisfied. Check the [current credential page](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/) for accepted prerequisites; a name change does not establish a new exam.

> **Official-page conflict:** The exam page includes MB-280 and PL-200 in its prerequisite list; the credential page omits them. Both also contain an unrelated information-protection exam summary. Use the dedicated study guide for scope and confirm an ambiguous prerequisite with Microsoft Credentials support before relying on it. The course and learning path have separate entry requirements; completing them does not satisfy the associate-credential requirement.

## How to use this guide

AB-100 is an architecture exam. For every scenario, identify the desired business outcome, process boundary, data and identity path, agent autonomy, platform fit, operational owner, evidence, and lifecycle. Use the decision tables to compare plausible options, then complete the architecture exercises and defend your tradeoffs aloud.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

> **Evidence boundary for supplementary sources:** The Microsoft blueprint defines exam scope, and current Microsoft product documentation defines Microsoft behavior. Named engineering blogs, cross-cloud architecture guidance, standards, and research below add transferable design heuristics; they do not prove that a topic is tested or that another platform behaves like Microsoft. Treat product-specific details from those sources as examples, translate the principle to the Microsoft design, and verify volatile Microsoft behavior in current documentation. This guide excludes exam dumps, recalled items, and sources that claim to reproduce live questions.

### Use a deliverables-first study loop

1. **Scope pass:** Read the blueprint and objective map. Mark every term you cannot explain and every Microsoft surface you cannot place in an architecture.
2. **Plan pass:** Work Parts 1–4 until you can produce a process map, requirement set, grounding-data assessment, architecture decision record, portfolio decision, and ROI/TCO model.
3. **Design pass:** Work Parts 5–7 until you can draw platform, identity, data, knowledge, tool, state, orchestration, and human boundaries for a cross-product scenario.
4. **Deploy pass:** Spend proportionally more practice here because it is 40–45% of the blueprint. Produce an evaluation/release plan, environment and ALM map, operational dashboard, threat model, and audit-evidence contract.
5. **Retrieval pass:** Answer the scenario checks without notes, complete at least three exercises end to end, and use the official practice assessment to identify—not memorize—weak areas. Return to the exact blueprint objective and source documentation for each miss.

For a compressed schedule, study one scenario through all five passes rather than reading every section passively. A useful completion standard is that another architect can challenge your assumptions and you can respond with a requirement, tradeoff, owner, evidence, and fallback.

### Follow one case from design to release

The worked examples below use a **fictional service-case assistant**. A signed-in service representative asks it to summarize an authorized case, consult an approved support article, and draft a follow-up task. Creating the task requires the representative's approval. Issuing refunds and reading other teams' restricted cases are outside its scope. Its first version uses the Copilot Studio standard harness. All figures, tool names, records, and test results in these examples are original study assumptions.

For a guided session of about 60–90 minutes, work through these five decisions, then complete [Exercise 13](#exercise-13-service-case-release-workshop):

| Start here | What you should be able to explain afterward |
|---|---|
| [Measure useful outcomes](#worked-check-consumption-versus-useful-outcomes) | Why higher total consumption can coexist with better efficiency |
| [Choose the integration](#worked-decision-connector-or-mcp) | How requirements, permission boundaries, and maintenance determine the choice |
| [Test the candidate](#worked-release-gate-evidence-before-a-green-check) | Why an incomplete test run cannot establish readiness |
| [Review the configuration](#worked-review-follow-a-finding-to-a-test) | How to turn a configuration finding into a correction and a runtime test |
| [Promote the release](#worked-promotion-what-moves-and-what-must-be-rebound) | Why importing the package is only one step in deployment |

You can complete the session on paper without a tenant. Write your decision before reading each worked answer, then explain what evidence would change it.

### Living-guide watch — September 27, 2026

Microsoft is moving Dynamics 365, Power Platform, and Dataverse from twice-yearly release waves to the [AI at Work roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap); the [transition announcement](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) says Release Planner retires by November 15, 2026. Use that roadmap for planning signals, Microsoft Learn for implementation behavior, and Message Center for tenant-specific rollout. Roadmap dates are estimates, not exam objectives or production commitments.

The current [GitHub Copilot Harness agent overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview), [Agent 365 GA announcement](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/), and [Microsoft 365 Copilot release notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes) are volatility sources. Product-level GA does not make every integration GA. The cross-vendor NIST, OWASP, Anthropic, AWS, Google, and OpenAI material cited later provides useful design corroboration, but the Microsoft blueprint remains the scope authority.

## Objective map

| Domain | Weight | Architect's job |
|---|---:|---|
| Plan AI-powered business solutions | 25–30% | Establish requirements, data readiness, strategy, portfolio, costs, and benefits |
| Design AI-powered business solutions | 25–30% | Select agent patterns, platforms, extensibility, applications, and integrations |
| Deploy AI-powered business solutions | 40–45% | Design monitoring, testing, ALM, security, governance, risk, and compliance |

The candidate is expected to understand Microsoft 365 Copilot, Copilot Studio, Microsoft Foundry and Foundry Tools, Power Platform, and core Dynamics 365 products. The role also connects business process design, responsible AI, open agent protocols, data governance, security, financial analysis, and adoption.

The AB-100 certification is positioned at the expert level. The certification page lists an eligible associate certification as a prerequisite; exam eligibility and certification-award requirements are different questions. **VERIFY CURRENT:** Check the current certification page for the accepted prerequisite list.

---

## 1. Think like an agentic business solutions architect

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

### Use an architecture decision record

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

### Classify the work before assigning autonomy

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

### Escalate complexity only when evidence earns it

The practitioner guidance in Anthropic's [Building effective agents](https://www.anthropic.com/research/building-effective-agents) and OpenAI's [Practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) converges on a useful architecture habit: begin with the simplest design that can meet a measured outcome, then add agent autonomy or coordination only for a demonstrated reason. This is **supplementary cross-vendor guidance**, not an AB-100 exam definition.

| Complexity level | Use when | Evidence required before moving higher |
|---|---|---|
| Deterministic rule or workflow | The path and answer can be specified and validated exactly | A documented need for language interpretation or probabilistic judgment |
| One model call | One bounded interpretation, extraction, classification, or draft is enough | Repeatable failure showing that decomposition or tools improve the outcome |
| Fixed AI workflow | Known stages need chaining, routing, parallel work, or evaluator feedback | Evaluation showing fixed control flow cannot handle legitimate variation |
| Single tool-using agent | The next step depends on changing context and cannot be enumerated economically | Tool-use and trajectory results showing specialization or isolation is needed |
| Multi-agent system | Distinct domains, permissions, scale, or independent evaluation justify separate roles | Measured benefit greater than coordination, latency, cost, and failure overhead |
| Autonomous operation | The system must initiate or continue work without immediate direction | Stable evaluations, bounded authority, monitoring, recovery, and accountable oversight |

For each move upward, write the failed acceptance criterion, the proposed added capability, the new failure modes, and the test that will show whether complexity helped. “More agentic” is not itself a business outcome.

### Draw the control loop, not only the component diagram

Model the runtime as a bounded loop:

```text
trigger → acquire authorized context → choose next step → invoke tool
   ↑                                                  ↓
stop/escalate ← evaluate progress and policy ← observe result
```

Specify what state crosses each arrow, which identity acts, which invariant must remain true, and which condition stops the loop. Add budgets for elapsed time, model calls, tool calls, retries, and spend. A component diagram can show that an agent connects to Dynamics 365; the control loop shows what prevents it from retrying the same write, accepting a poisoned observation, or continuing after success.

---

## 2. Analyze requirements and grounding data

### Capture business and technical requirements together

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

### Assess whether an agent fits

Agents are useful where language, unstructured information, adaptive reasoning, and tools improve a process. They are a poor replacement for a simple form, exact calculation, deterministic rule, or unsupported attempt to avoid fixing data quality.

Ask:

1. What decision or action is being delegated?
2. What evidence does the agent need?
3. How does it know the evidence is current and authorized?
4. Which outcomes require a person?
5. How will errors be detected, contained, corrected, and learned from?
6. Can the original process continue during an outage?

### Evaluate grounding data

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

## 3. Design the enterprise AI strategy

### Apply the Cloud Adoption Framework as a change system

The [Cloud Adoption Framework for AI](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/) connects strategy, planning, readiness, adoption, governance, management, and security. Translate it into decisions:

- define business motivations and outcomes;
- assess AI maturity, data, skills, risk, and platform readiness;
- prioritize a portfolio, not isolated demonstrations;
- establish landing zones, platform services, policy, and delivery patterns;
- deliver iteratively and measure outcomes;
- govern, secure, operate, and improve continuously.

Do not confuse a platform rollout with adoption. Adoption also needs process owners, champions, training, support, communications, feedback, and changed performance measures.

Microsoft's [2026 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization) is useful supporting research for work redesign, documented human-agent handoffs, shared quality standards, and organizational learning. Treat its survey and Microsoft 365 telemetry as directional evidence from its stated populations—not as causal proof, a universal benchmark, or an exam requirement. Convert any insight you use into a local hypothesis with a baseline, owner, measurement period, and disconfirming signal.

### Create an AI Center of Excellence that enables delivery

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

Microsoft’s current [AI Center of Excellence guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/center-of-excellence) describes the CoE as a multidisciplinary enabler that evolves from centralized foundations toward an advisory model as organizational maturity grows. The durable design question is which decisions remain centralized and which are delegated with guardrails.

> **Related item:** Platform engineering turns approved architecture into paved roads: reusable environments, connectors, policies, pipelines, telemetry, and templates make the safe path easier for delivery teams.

### Manage an agent portfolio

Use an intake process that records outcome, owner, affected users, data, integrations, autonomy, risk tier, expected value, cost range, and lifecycle. Remove duplicates and identify shared capabilities. Stage investment through discovery, prototype, controlled pilot, production, scale, and retirement gates.

Increase autonomy only when process clarity, data quality, controls, evaluation, and operational maturity support it. Pilot success with friendly users does not prove readiness for broad deployment.

### Govern a prompt library

A prompt library is a governed collection of reusable, tested prompt templates—not a folder of clever sentences. The [Copilot Studio prompt library](https://learn.microsoft.com/en-us/microsoft-copilot-studio/prompt-library) supplies predesigned starting templates for tasks such as extraction, transformation, classification, summarization, and generation. An enterprise library adds its own approval, reuse, and lifecycle contract.

For each library entry, record:

- business task, owner, intended users, and supported authoring/runtime surfaces;
- approved input classes and grounding sources, with prohibited sensitive inputs;
- prompt text, variables, examples, output format/schema, and failure behavior;
- model/deployment compatibility, locale, dependencies, and estimated consumption;
- evaluation set and thresholds for quality, safety, consistency, latency, and cost;
- version, approver, change history, usage telemetry, review date, and retirement path.

Use an intake → design → adversarial evaluation → approval → publication → monitored reuse → revision/retirement flow. Separate a reusable prompt template from an agent's persistent instructions and from a user's runtime prompt: changing one does not automatically version or validate the others. Allow consumers to parameterize approved variables, but do not let runtime text redefine authorization or tool policy. A shared template accelerates delivery only if its tests and assumptions travel with it.

### Decide when a customized small language model fits

[Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) includes small language models alongside foundation, reasoning, multimodal, domain, and industry models. Prefer a small model when a narrow, repeatable task can meet measured quality with lower latency, cost, compute, or deployment footprint, or when an approved edge/private placement is a hard requirement. Examples can include constrained classification, extraction, routing, summarization, or domain terminology—not open-ended high-complexity reasoning by default.

Customize only after comparing simpler options: prompt design, structured output, grounding/RAG, a prebuilt model, or routing to an existing deployment. Define the exact behavior that customization should improve; establish a larger-model or current-process baseline; verify training-data rights, lineage, representativeness, privacy, and residency; split training and evaluation data; test rare, adversarial, multilingual, and safety cases; and retain a fallback. Deployment still needs content controls, access, versioning, monitoring for drift, cost/latency measurement, and rollback. Small does not mean low risk, and customized does not mean accurate outside the evaluated task.

---

## 4. Evaluate cost, value, and build/buy/extend choices

### Establish value before launch

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

The Copilot Studio team’s [business-value guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-business-value-measure-impact) separates technical performance, adoption, operational/process impact, and business results. Measure a chain of evidence rather than attributing every outcome change to the agent.

### Calculate total cost of ownership

Include more than model tokens:

- licenses and consumption;
- model, search, storage, integration, network, and observability services;
- design, development, data preparation, testing, and migration;
- security, compliance, legal, and risk review;
- training, change management, support, and operations;
- remediation, human review, exception handling, and vendor management;
- replacement, portability, and retirement.

Model costs under normal, peak, growth, and degraded scenarios. Include uncertainty and sensitivity analysis instead of presenting one precise but fragile ROI number.

#### Worked ROI check with synthetic assumptions

Suppose a pilot handles 1,000 cases monthly and saves six minutes per case before review. That is 100 hours. Reviewing 200 exceptions for six minutes each consumes 20 hours, leaving 80 hours. At an assumed $40 per hour, the potential monthly capacity value is $3,200. If recurring platform and operating costs total $1,200, the modeled net benefit is $2,000 monthly. With $12,000 initial implementation cost, first-year benefits are $38,400, first-year costs are $26,400, and modeled ROI is `(38,400 - 26,400) / 26,400`, approximately **45%**. Simple payback is six months if benefits start immediately and remain constant.

These are original study assumptions, not vendor prices or promised savings. Capacity released becomes cash savings only if the organization can realize it. If gross time savings fall to three minutes while review effort stays fixed, net monthly capacity value falls to $1,200 and merely covers recurring cost. Test adoption, quality, review burden, and realization before approving the business case.

> **Related item:** FinOps assigns visibility and accountability to variable cloud/AI cost. Unit economics such as cost per successfully resolved case are more actionable than an undifferentiated monthly bill.

The cross-cloud [AWS Well-Architected Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html) highlights why agent cost behaves differently from a single request: iterative reasoning, memory, tool calls, retries, and multi-agent coordination can multiply both cost and latency. Use that as **supplementary architecture guidance** and apply the principle to the selected Microsoft services rather than copying AWS product choices.

Calculate a defensible unit cost:

```text
cost per verified successful outcome =
  (model + grounding + tool/API + platform + telemetry
   + human review + failed-run remediation + allocated lifecycle cost)
  / verified successful outcomes
```

Track the distribution, not only the average. A small number of looping or degraded runs can dominate spend and tail latency. Put maximum steps, retries, tool calls, elapsed time, and cost into the architecture; decide whether each limit causes a cheaper route, a safe partial result, a queued retry, or human escalation. Include abandoned and incorrectly completed work in the denominator analysis so apparent automation does not hide rework.

#### Worked check: consumption versus useful outcomes

The service-case pilot reports the following **synthetic** results for two equally long periods. Count each case once. An accepted outcome means the representative approved the case summary and next step, the task was recorded when requested, and no correction was needed during the agreed seven-day review window. Compare periods only after that window closes, using comparable case complexity and the same definition of success.

| Measure | Pilot A | Pilot B |
|---|---:|---:|
| Cases attempted | 500 | 600 |
| Verified accepted outcomes | 300 | 480 |
| Copilot Credits consumed | 6,000 | 7,200 |
| Acceptance rate | 300 / 500 = 60% | 480 / 600 = 80% |
| Credits per attempted case | 12 | 12 |
| Credits per accepted outcome | 6,000 / 300 = 20 | 7,200 / 480 = 15 |

**Worked answer:** Total consumption rose 20%, accepted outcomes rose 60%, and credits per accepted outcome fell 25%. Pilot B is more efficient on this measure. That alone does not prove better ROI: compare review time, correction effort, other service costs, and actual business benefit. Credits are a consumption unit; converting them into money requires current applicable billing terms. These numbers are not a Microsoft rate estimate.

To build the report, keep consumption and business outcomes as separate datasets. Aggregate each to a compatible period and agent/environment boundary before combining them; joining daily consumption onto every individual case would multiply the numerator. Include failed attempts in consumption, but exclude them from successful outcomes. Split development/testing usage from production usage when the available evidence permits.

The [CAT consumption walkthrough](https://microsoft.github.io/mcscatblog/posts/copilot-credit-consumption-api/) supplies an implementation example. The [official resource-consumption API](https://learn.microsoft.com/en-us/rest/api/power-platform/licensing/entitlement-insight/get-tenant-resources-across-environments) documents pagination and refresh metadata. **VERIFY CURRENT:** retrieve every page, record data freshness, and inspect available dimensions before promising a dashboard. A missing optional field is not evidence of zero usage.

### Build, buy, or extend

| Option | Prefer when | Watch for |
|---|---|---|
| Use prebuilt AI/agent | Standard process and product-native data/actions fit | Configuration limits, licensing, roadmap, data boundary |
| Extend Microsoft 365 Copilot | Users work in Microsoft 365 and need organizational knowledge/actions | Declarative vs custom engine capability, deployment and admin approval |
| Build in Copilot Studio | Low-code orchestration, channels, connectors, topics/actions, managed operations fit | Environment/solution discipline, connector governance, complex-code boundaries |
| Build with Microsoft Foundry | Custom code, models, orchestration, evaluation, or Azure architecture is needed | Greater engineering and operational responsibility |
| Buy a third-party solution | Differentiated domain capability is available and integration is acceptable | Data use, identity, residency, assurance, exit, concentration risk |
| Build custom model | Proprietary task/data creates measurable advantage unmet by existing models | Data rights, training skill/cost, validation, security, drift, lifecycle |

The answer may be compositional: extend Microsoft 365 Copilot for the user experience, use Copilot Studio for business orchestration, call a Foundry-hosted capability, and retain Dynamics 365 as the system of record. Make ownership and telemetry across those boundaries explicit.

Use the current [Microsoft 365 agent overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-overview) when distinguishing declarative agents—which use Microsoft 365 Copilot’s orchestrator and models—from custom-engine agents, which bring custom orchestration/models and additional hosting responsibility. **VERIFY CURRENT:** licensing, distribution, channels, proactive behavior, and feature status.

### Use model routing deliberately

A model router can select by task, sensitivity, modality, quality, cost, latency, availability, and region. Define eligible routes, evaluation thresholds, fallback, trace fields, and change control. Do not route sensitive data to a model merely because it is cheaper.

For the specific [Foundry model router](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-router), deploy the router and configure its eligible model subset and routing mode: Balanced, Quality, or Cost. Apply the data-boundary and model-approval constraints before optimizing cost. The active router version can gain capabilities without a new version identifier; record the subset and deployment settings as part of the evaluated configuration. Check the smallest eligible context window and supported modalities, and provide an explicit failure path when no approved model can serve the request.

The [implementation guide](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/model-router) shows requests addressed to the router deployment and responses identifying the serving model. Compare it with a direct-model baseline using representative tasks, tool-call correctness, latency, and cost per accepted result. Record routing changes and rerun regressions. A custom policy router remains an architectural alternative when the managed router cannot enforce the required contract. **VERIFY CURRENT:** model pool, deployment type, region, preview options, and per-model prerequisites.

---

## 5. Design agents and choose the Microsoft platform

### Match platform to the experience and control required

| Platform/surface | Strong fit |
|---|---|
| Microsoft 365 Copilot agents | Bring knowledge and actions into Microsoft 365 experiences such as Teams and SharePoint |
| Copilot Studio | Low-code agents, topics, generative orchestration, connectors, agent flows, channels, managed environments |
| Microsoft Foundry Agent Service | Code-first/custom Azure agents, models, tools, orchestration, evaluation, and observability |
| Dynamics 365 AI and agents | Product-native finance, supply chain, sales, customer service, or contact-center processes |
| Power Apps with AI components | Task-oriented business application combining structured UI, process, and AI assistance |

Select the experience, system of record, required autonomy, extensibility, data boundary, engineering model, lifecycle, and operations together. Product affinity alone is not an architecture.

### Decompose a cross-platform solution by responsibility

Do not ask which single product “owns the AI.” Assign each architectural responsibility deliberately:

| Responsibility | Decision question | Possible surface |
|---|---|---|
| Experience/channel | Where does the user already work, and what accessibility/channel context is required? | Teams, SharePoint, Microsoft 365 Copilot, Dynamics 365, contact center, Power Apps, web/app channel |
| Orchestration | Are paths explicit, low-code and connector-centered, or custom/code-first? | Topics/agent flows, Copilot Studio generative orchestration, Foundry/custom orchestration |
| Intelligence/model | Is the managed host model sufficient, or does the solution need model choice/routing/customization? | Microsoft 365/Copilot Studio managed models, Foundry Models, specialized Foundry Tools |
| Knowledge/grounding | Which governed evidence is relevant, fresh, and permitted for this identity? | Microsoft 365 content, Copilot connectors, Dataverse/Dynamics data, search/knowledge service, custom API |
| Actions/tools | Which read or write capabilities can the agent invoke under what identity and policy? | Connectors, flows, plugins, MCP servers, APIs, agent-to-agent delegation |
| System of record | Which application remains authoritative for customer, case, order, finance, or supply-chain state? | Dynamics 365, Dataverse, line-of-business or third-party system |
| Control and operations | Where are policy, DLP, environment, deployment, evaluation, telemetry, audit, and incident ownership enforced? | Power Platform/Microsoft 365/Azure controls plus cross-platform operating model |

#### Worked boundary: service case resolution

A Teams user asks an agent to investigate a customer case, consult policy in SharePoint, check entitlement in Dynamics 365, propose an appointment, and update the case after approval.

1. **Experience:** Microsoft 365/Teams is the invocation surface, but it is not automatically the system of record.
2. **Knowledge:** SharePoint retrieval must honor the user/agent entitlement and provide evidence; copying policy into a prompt is not a governance strategy.
3. **Business state:** Dynamics 365 remains authoritative for the case and entitlement.
4. **Orchestration:** Copilot Studio may fit low-code connector, topic, and agent-flow requirements; custom Foundry orchestration is justified only by a measurable control/model/code need.
5. **Action:** the scheduling and case-update APIs validate parameters and authorization and require approval/idempotency where appropriate.
6. **Failure:** if Dynamics is unavailable, the agent preserves a draft and escalates; it does not claim the case changed.
7. **Evidence:** correlate the user request, retrieved sources, agent/tool versions, approval, API result, and business outcome under product-specific privacy controls.

This decomposition prevents channel identity, orchestration identity, connector identity, and target-system authorization from being collapsed into one vague “agent access” decision.

> **Related item:** A system of engagement optimizes interaction; a system of record owns authoritative business state. An agent can span both, but the architecture must preserve which state is authoritative and how updates are reconciled.

### Agent pattern catalog

| Pattern | Behavior | Essential controls |
|---|---|---|
| Prompt/response agent | Produces a response or transformation | Grounding, schema, content policy, review |
| Task agent | Completes a bounded multi-step task | Tool scope, validation, retries, termination |
| Autonomous agent | Acts from events or goals with less immediate direction | Budgets, approval thresholds, monitoring, kill switch |
| Conversational service agent | Maintains dialogue and resolves/escalates cases | Identity, knowledge permissions, channel context, handoff |
| Multi-agent system | Specialized agents coordinate | Orchestration, contracts, shared state, conflict and failure handling |

Define role, goal, instructions, knowledge, tools, memory, triggers, response contract, approval, escalation, and evaluation for every agent. For autonomous designs, specify start conditions, maximum scope, frequency, duplicate handling, and stop/disable mechanisms.

> **Related item:** A human-in-the-loop control is a workflow with an SLA, evidence, delegation, absence handling, and escalation. An “approval” step with no accountable reviewer can make the process less reliable, not more.

### Copilot Studio design

**Choose the runtime first.** Microsoft's [harness overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview) distinguishes the standard harness, the GitHub Copilot harness, and the Copilot chat harness. A harness controls execution around the model. Standard agents expose familiar topics and agent flows; the GitHub Copilot harness supports reasoning-led work across tools and files; the chat harness extends Microsoft 365 Copilot Chat with enterprise knowledge. Standard agents can also use generative orchestration: “standard” does not mean every path is deterministic. The GitHub Copilot harness runs within Copilot Studio's service boundaries; its name does not imply that business data goes to the GitHub Copilot service. Match feature, billing, channel, evaluation, and ALM documentation to the selected harness.

Use topics for deterministic conversational paths and business rules where explicit control matters. Design triggers, variables, conditions, questions, actions, error paths, and fallback. Generative orchestration is appropriate when the agent must select knowledge and actions flexibly, but its tools and policy still need hard boundaries.

The Copilot Studio [agent architecture guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/architecture/components-of-agent-architecture) and [agent-tools guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-tools) distinguish instructions/orchestration, knowledge, tools, channels, and monitoring. Use those components to make trust and failure boundaries visible rather than treating the agent as one box.

#### Natural-language approach selection

| Need | Approach |
|---|---|
| Known intents and controlled dialogue | Standard NLP/topic routing |
| Domain-specific intent/entity model | Conversational language understanding where justified |
| Flexible interpretation across knowledge and tools | Generative orchestration with evaluation and constraints |

Prompt actions need a clear task, inputs, trusted context, output format, safety behavior, and error contract. Keep business authorization outside the prompt.

#### Event-driven work has a different identity boundary

For standard-harness agents, [event triggers](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about) require generative orchestration and use the maker's connection credentials. Actions requiring authentication must work without an interactive sign-in for autonomous execution. A SharePoint event does not automatically confer the permissions of the person who changed the document. Inventory the actual connection identity, constrain trigger scope and downstream access, inspect payload destinations, and test for information exposure to other agent users. Publication activates automatic responses to configured events. Include frequency, consumption, duplicate-event handling, connection ownership, and a disable procedure in the release plan.

#### Match a Foundry capability to the input and result

The [Foundry Tools catalog](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services) complements generative models with specialized capabilities:

| Requirement | Capability to evaluate | Acceptance evidence |
|---|---|---|
| Extract fields and structure from invoices | Document Intelligence | Field accuracy, layout variation, missing-value handling |
| Interpret mixed document, image, audio, or video content | Content Understanding | Supported modality/schema and representative extraction results |
| Transcribe or synthesize speech | Speech | Locale, terminology, latency, accessibility |
| Classify text or extract language entities | Language | Domain examples, ambiguous inputs, confidence policy |
| Retrieve relevant business evidence | Azure AI Search | Relevance, freshness, identity filtering, citations |
| Detect unwanted content | Content Safety | False positives/negatives and escalation behavior |

These are component choices, not substitutes for orchestration or authorization. Check each service's lifecycle and supported features; a historical service name in older training is not evidence that it is suitable for a new solution.

Apply [Power Platform Well-Architected](https://learn.microsoft.com/en-us/power-platform/well-architected/) pillars—reliability, security, operational excellence, performance efficiency, and experience optimization—to the entire intelligent workload.

### Design multi-agent responsibility

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

### Choose orchestration by dependency and decision ownership

Microsoft's [AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) distinguish coordination shapes and their tradeoffs. Use the pattern name as shorthand only after defining who selects the next step and who owns shared state.

| Pattern | Strong fit | Main design question | Common failure |
|---|---|---|---|
| Sequential | Each stage depends on the preceding result | Can a bad early result be detected before it propagates? | Error accumulation and end-to-end latency |
| Concurrent | Independent perspectives or subtasks can run together | How are conflicts, duplicate work, and partial timeouts resolved? | Higher cost and inconsistent results |
| Handoff | One specialist should transfer ownership to another | What context, authority, and completion state cross the boundary? | Lost context or two agents believing they own the task |
| Group chat | Several specialists must iteratively collaborate | Who terminates discussion and decides the accepted result? | Cycles, consensus without evidence, and token growth |
| Dynamic selection | The required specialist cannot be known in advance | Is routing constrained to an approved registry and contract? | Incorrect delegation or unbounded discovery |
| Evaluator-optimizer | A candidate can be improved against explicit criteria | Is the evaluator independent enough, and what score ends the loop? | Self-reinforcing errors or endless refinement |

Prefer deterministic orchestration when dependencies are known. Split agents because their capabilities, permissions, scale, model needs, or ownership genuinely differ—not to mirror an organization chart. Test the composed system even when every agent passes alone.

---

## 6. Design extensibility and open-protocol boundaries

### Extend Microsoft 365 Copilot

Choose declarative or custom-engine approaches based on the required orchestration and hosting responsibility. Plan where users discover and invoke the agent, how organizational data is grounded, which actions are exposed, how admins approve/manage it, and how telemetry joins the wider operating model.

Microsoft’s [Copilot extensibility documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/) and [agent management guidance](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/manage) are the current sources for creation, approval, deployment, inventory, and admin control. **VERIFY CURRENT:** tenant settings, catalog/distribution paths, licensing, roles, and national-cloud support.

Teams and SharePoint are not only channels; they carry identity, collaboration context, permissions, and user expectations. Validate the agent against those host boundaries.

### Model Context Protocol and Agent2Agent

| Protocol idea | Primary relationship | Architecture concern |
|---|---|---|
| MCP | Model/agent client discovers and invokes tools, resources, or prompts from a server | Server trust, capabilities, authentication, tool authorization, input/output validation |
| A2A | Agents communicate and delegate across agent boundaries | Identity, capability discovery, task contract, state, trust, observability |

Do not treat protocol compatibility as trust. Approve servers/agents, authenticate connections, authorize each capability, minimize scopes, validate content, and monitor execution.

For a standard-harness agent, the [MCP connection guide](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent) documents an onboarding wizard or custom connector, Streamable transport, and API-key or OAuth authentication when required. It states that the former SSE transport is unsupported. Decide whether the connection acts for a user or a shared identity, verify server-described tools, and test revoked consent and unauthorized records. Validate the implementation against its current harness documentation; generic MCP compatibility alone does not establish which transports, resource types, or authentication flows this client supports.

> **Related item:** Supply-chain governance applies to agent integrations. An MCP server, connector, plugin, model, or package can change independently, so inventory versions, ownership, provenance, permissions, and update policy.

#### Worked decision: connector or MCP?

A connector exposes operations from a service through Power Platform. An MCP server exposes capabilities through a protocol that compatible agent clients can use. Either can sit in front of the same business API. The decision concerns the capabilities and controls needed by this solution; the protocol name does not determine whether a business operation is authorized. Jay Padimiti's [comparison](https://microsoft.github.io/mcscatblog/posts/compare-mcp-servers-pp-connectors/) usefully separates choosing existing integrations from building your own.

For this fictional assistant, assume both options can read cases and create tasks:

| Requirement | Design implication |
|---|---|
| Only three stable operations are needed: read case, retrieve article, create approved task | Explicitly select and describe those operations; a connector is a reasonable first candidate. |
| The same integration must also serve another MCP-compatible agent platform | An MCP server becomes more attractive if its capabilities, transport, and authentication fit both clients. |
| The provider can introduce new tools independently | Define who reviews changes and how unapproved operations remain inaccessible. |
| Representatives can access only assigned cases | Enforce record authorization at the data/API boundary under the intended identity for either option. |
| Task creation needs approval and duplicate prevention | Design those controls into the action path; neither integration choice establishes them automatically. |

**Worked answer:** For the initial Power Platform-only release, start with the connector if it meets the stated requirements and has the simpler supported lifecycle. Reconsider MCP when cross-client reuse or a needed server capability provides a concrete benefit. Record the assumptions and test both access and failure behavior before accepting either design.

**Failure to spot:** An allowed MCP server later exposes a refund operation. An instruction saying “never refund” is insufficient proof that the operation cannot execute. Current [advanced connector policy documentation](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies) distinguishes whole-server blocking from individual MCP-tool control; it also excludes custom connectors from current ACP support. **VERIFY CURRENT:** confirm the applicable policy surface and enforce the permitted operation set at the server/API as needed. Test a direct forbidden request and a newly advertised tool. If the required restriction cannot be enforced, change the integration design.

### Computer use, reasoning, and voice

Computer-use agents interact with user interfaces when no suitable API exists. They are more fragile and harder to constrain than API integrations. Use isolated sessions, allowlisted destinations, bounded credentials, confirmations, screenshot/data controls, monitoring, and recovery. Prefer a supported API for reliable high-volume transactions.

Reasoning modes can improve complex task performance while increasing latency, cost, and opacity. Evaluate outcomes and enforce tool limits. Voice mode adds turn detection, interruption, transcript privacy, latency, and accessible alternative channels.

In the current [computer-use configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use), a maker-provided machine connection can expose the author's access to other agent users; end-user authentication instead requires each user to have suitable machine credentials. Choose a reviewer who can inspect the initiating user's run, and test rejection, timeout, and stop behavior. Screenshots and chat activity also need a data-handling policy. Administrators have separate [environment computer-use and tenant hosted-browser controls](https://learn.microsoft.com/en-us/microsoft-copilot-studio/administer-computer-use). **VERIFY CURRENT:** execution location, identity options, feature availability, and supervision behavior before selecting this pattern.

### Connect Power Apps and business processes

In a canvas app, keep structured inputs and confirmations visible when precision matters. Use AI to interpret or draft, then use Power Fx, flows, connectors, and server-side rules to enforce the business process. A generated response should not silently bypass validation that applies to manual entry.

### Propose code-first generative pages and an agent feed

A [code-first generative page](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/generative-page-external-tools) is a model-driven-app page produced or edited through an AI code-generation workflow. Current Microsoft guidance describes generated TypeScript and React code, Dataverse-backed data, placement in an app and solution, local development artifacts, and deployment through Power Platform tooling. Choose this approach for a tailored, data-centric user experience when standard forms/views or a canvas app cannot meet the interaction requirement and the team can own generated code.

Treat generated output as application code: constrain the Dataverse tables and operations, review the proposed plan before generation, inspect dependencies and generated source, enforce server-side authorization and validation, test CRUD and negative paths, check accessibility and responsive behavior, place artifacts in a solution, promote through controlled environments, and retain code comparison and rollback evidence. A page that renders successfully is not production-ready proof.

The [agent-feed release plan](https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave2/power-apps/supervise-autonomous-agents-agent-feed) introduces a supervision surface in model-driven apps. The [implementation documentation](https://learn.microsoft.com/en-us/power-apps/user/supervise-agents-with-agent-feed) remains **preview**, English-only, and subject to regional rollout. Since May 1, 2026, supported feed tasks use the Power Apps MCP server.

| MCP task | Feed behavior | Design implication |
|---|---|---|
| `request_assistance` | Needs attention; user completes requested assistance | Define a responder and escalation path |
| `invoke_data_entry` | Needs attention; user can accept/complete or dismiss proposed data entry | Verify proposed values and write authorization |
| `request_review` | Completed; informational, without a user action | This is after-the-fact visibility, not a pre-action approval gate |

**Access boundary:** The implementation page warns that users with access to the Agent Task table can see feed items. Do not put confidential user-targeted tasks into the feed or assume an assignee field enforces privacy. Validate the table's access model and use a separately authorized approval mechanism when necessary. Treat this preview as an evaluation topic, not a production-ready confidential approval queue.

Design the broader supervision contract: related record, evidence, authorized resolver, expiry, escalation, correlation, and duplicate handling. Enforce approval and record authorization in the executing workflow; a completed feed entry alone does not prove either.

These features can be combined: a generative page supplies a purpose-built record experience while the agent feed surfaces agent decisions requiring review. Keep page deployment, agent deployment, MCP/tool permission, and supervisor authorization as separate ALM and security boundaries. **VERIFY CURRENT:** availability, region, licensing, supported code-generation tools, generated-page limitations, Agent Feed release state, and Power Apps MCP behavior.

The current generative-page guide also labels **connector-backed data and Dataverse custom API support as preview**. Check the selected data path separately from the page itself; generated React/TypeScript, a working connector, and an attractive UI do not establish the same availability or security contract.

---

## 7. Orchestrate Dynamics 365, Microsoft 365, and Power Platform capabilities

The objective is architectural fit, but the named workload boundaries matter. Microsoft's current [agent-design module](https://learn.microsoft.com/en-us/training/modules/design-ai-agents-business-solutions/) and [prebuilt-app orchestration module](https://learn.microsoft.com/en-us/training/modules/orchestrate-configuration-prebuilt-agents-apps/) provide the product baseline. For every workload, identify the host experience, system of record, configuration owner, acting identity, knowledge source, allowed action, human handoff, telemetry, and ALM artifact.

### Customer experience, service, sales, and Contact Center

**Business terms** align Copilot with organization-specific synonyms, acronyms, products, process stages, and service concepts. Source the terms from governed definitions, assign semantic owners, state where each term applies, test ambiguous and conflicting phrases, and version them with the affected Dynamics 365 customization. Business terms improve interpretation; they do not grant record access or override Dataverse security.

For **Copilot customization in customer experience and service**, start with the supported in-app capability and identify the gap: knowledge selection, prompt/response behavior, case or customer context, action, routing, or channel. Configure the smallest supported extension; preserve case/contact/account authorization; separate draft assistance from record mutation; and test standard, restricted, stale-knowledge, escalation, and unavailable-service paths. Include feature settings, roles, knowledge references, topics/prompts, and dependent solutions in ALM.

For a **Dynamics 365 Sales connector**, define which sales records and operations Copilot needs. Decide delegated versus service connection, exact connector actions, connection reference, DLP classification, consent, field-level and record-level authorization, input validation, duplicate handling, throttling, audit, and owner. Use read-only retrieval before write actions and require confirmation for material changes such as creating a lead, updating an opportunity, or sending outreach. Enabling a Sales extension or plugin does not broaden the CRM user's permission.

For **Dynamics 365 Contact Center**, choose the channel—voice, chat, SMS, social, Teams, or custom messaging—from customer need, identity, latency, media, accessibility, geography, and compliance. Connect the agent to a workstream, queue, unified-routing and escalation design; preserve authenticated customer and conversation context through transfer; specify recording/transcription/consent and sensitive-data masking; and test abandonment, timeout, language, unavailable knowledge, agent failure, and representative handoff. Custom-channel or telephony integration adds its own SDK/API, trust, monitoring, and continuity boundary.

### Orchestrate prebuilt agents and app experiences

| Workload | Configuration and orchestration path | Evidence and failure questions |
|---|---|---|
| Finance and supply chain | Select product-native finance, planning, procurement, inventory, or operations capability; bind it to the correct company/legal entity, business event, data, and transaction authority | Does segregation of duties still hold? Are source data and company context current? Are writes approved, idempotent, audited, and recoverable? |
| Customer experience and service | Configure supported sales/service Copilot features and agents around account, opportunity, case, knowledge, routing, correspondence, and next actions | Which Dataverse roles and knowledge permissions apply? Can a representative verify evidence, edit drafts, and take over? |
| Microsoft 365 Copilot for Sales or Service | Connect the Microsoft 365 experience to the selected CRM and enable only required capabilities, users, and supported extensions | Which identity reaches CRM data? Where are Outlook/Teams and CRM records stored, governed, audited, and synchronized? |
| Microsoft 365 agents | Choose a prebuilt agent when its host, knowledge, actions, and admin controls fit; otherwise extend or build | Who approves deployment and tools? Does user access differ from downstream data/action permission? |
| Power Platform AI hub | Use supported prompts, models, document/intelligence capabilities, and monitoring within governed environments | Which environment, connection, DLP, capacity, solution, evaluation, and maker policy owns the asset? |

Orchestration is the configuration of an end-to-end business outcome, not simultaneous enablement of every Copilot. Define the authoritative system, pass only required context, avoid two agents issuing the same transaction, route exceptions to a named role, correlate telemetry across products, and test the complete multi-app process. Use prebuilt agents when product-native data, process, and controls align; customize or compose only to close a measured gap.

### Add finance and operations knowledge safely

For structured live Finance or Supply Chain data, current Microsoft guidance supports exposing eligible finance-and-operations data through [Dataverse virtual entities as Copilot Studio knowledge](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/tutorial-agent-knowledge). A virtual entity points to the operational source; a native Dataverse table populated through synchronization creates another copy and freshness contract. Choose from authorization, CRUD need, latency, scale, supported table, data residency, and failure behavior—not convenience alone. Add only required tables, confirm legal-entity and row access, publish to a test agent, and validate citations, calculations, restricted records, stale/unavailable source behavior, and query cost.

[In-app help and guidance](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-generative-help) is grounded in Microsoft public documentation and can be extended with approved custom or general knowledge through Copilot Studio under current capabilities. Use curated process documentation with an owner, version, audience, permissions, locale, and review date. Keep help content distinct from operational data: instructions can explain how to post a journal, while a virtual entity can answer an authorized question about a specific record. Test both in the finance-and-operations sidecar and any custom-agent experience, and define how updates, removals, and permission changes propagate.

Across these workloads, ALM includes feature toggles, security roles, business terms, knowledge-source references, connector and connection references, Copilot Studio components, Dataverse/Dynamics configuration, environment variables, evaluation sets, and rollback. **VERIFY CURRENT:** agent and Copilot names, preview state, licensing, region availability, connector/plugin management, customization surfaces, Contact Center channels, finance-and-operations knowledge support, and Microsoft 365 deployment controls. Use current product documentation rather than memorizing a point-in-time catalog.

> **Related item:** A canonical business process and semantic layer reduce cross-agent contradiction. Without them, different agents can automate competing interpretations of the same customer, order, case, or approval state.

---

## 8. Monitor, test, and tune AI-powered business solutions

### Use an operational measurement stack

| Layer | Examples | Owner question |
|---|---|---|
| Platform | Availability, latency, capacity, connector/model errors | Is the service healthy? |
| Agent | Topic/tool selection, task completion, loops, escalations | Is the agent behaving as designed? |
| Quality/safety | Groundedness, relevance, harmful content, attack results | Is the behavior acceptable and safe? |
| Process | Cycle time, resolution, rework, exception rate | Did the process improve? |
| Business | Cost, revenue, risk, satisfaction, strategic outcome | Is the investment valuable? |

Correlate traces across Copilot Studio, Power Platform, Foundry, Microsoft 365, Dynamics 365, and external systems. Define a common request/case identifier where supported, while respecting privacy and product boundaries.

Use backlog and feedback as evidence, not as a vote count. Classify items into defects, data/knowledge gaps, prompt/orchestration issues, missing capability, training/adoption issues, policy conflicts, and feature requests. Prioritize by impact, frequency, risk, and strategic value.

### Build a layered test strategy

1. **Component tests:** topics, prompts, tools, connectors, actions, extraction.
2. **Model/agent evaluations:** representative quality, groundedness, safety, adversarial cases.
3. **Integration tests:** identities, permissions, data, APIs, error behavior.
4. **End-to-end tests:** multi-app business process and human handoff.
5. **Nonfunctional tests:** load, latency, continuity, accessibility, security, privacy.
6. **User acceptance:** process owners and representative users validate outcomes.
7. **Production verification:** controlled release, live monitoring, rollback triggers.

Prompt best practices are testable hypotheses. Validate task clarity, context, examples, grounding, output schema, edge cases, and refusal behavior against a versioned set. Custom models need acceptance criteria for quality, safety, bias, robustness, latency, cost, and drift.

The standard-harness [agent evaluation feature](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro) supports reusable test sets with questions or conversations, several scoring methods, and execution through UI, APIs, or automation. It complements interactive test chat. The documented limits include no Fabric data-agent support and restrictions on user profiles and similarity scoring in GCC. Check the chosen harness and cloud before promising a test capability.

To use Copilot to create test cases, supply synthetic process requirements, allowed actions, and failure conditions; request normal, boundary, restricted-access, and dependency-failure cases. Have a process owner verify expected results independently of the generated answers. Track which objective or risk each case exercises and preserve a held-out regression set. Generated test volume is useful only when the expected outcomes and coverage are trustworthy.

> **Related item:** Chaos and resilience testing can cover tool timeouts, missing knowledge, expired credentials, unavailable models, and human-review backlog. The desired result may be safe degradation or escalation, not an uninterrupted answer.

### Evaluate outcomes and trajectories

An agent can produce a plausible final answer through an unacceptable path, or take a safe and efficient path to an outcome a brittle answer matcher rejects. Anthropic's [agent-evaluation engineering guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), Amazon's [real-world agent-evaluation lessons](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/), and Google's [production-ready agent guide](https://cloud.google.com/blog/products/ai-machine-learning/a-devs-guide-to-production-ready-ai-agents) independently emphasize multi-level evaluation. These are **supplementary practitioner sources**; use their transferable method while Microsoft documentation remains authoritative for Microsoft telemetry and tools.

| Evaluation level | Ask | Example evidence |
|---|---|---|
| Component | Did retrieval, classifier, prompt, or tool contract work alone? | Exact assertions, schema validation, retrieval relevance |
| Step/turn | Was this decision and response appropriate at this point? | Policy match, tool choice, argument validity, grounded response |
| Trajectory | Did the sequence reach the goal safely and efficiently? | Ordered trace, unnecessary/repeated steps, recovery, stop behavior |
| Outcome | Was the business task actually completed and verified? | Authoritative record state, user confirmation, process KPI |
| System | Did identity, integration, latency, resilience, safety, and cost remain acceptable? | End-to-end tests, load/failure results, security evidence |
| Production | Does live behavior remain within the approved envelope? | Sampled reviews, drift signals, incidents, feedback, unit cost |

Build an evaluation set from normal cases, meaningful edge cases, prior failures, restricted-access cases, adversarial inputs, and safe failure conditions. Preserve expected invariants as well as expected answers. Prefer deterministic graders for schemas, permissions, tool parameters, record changes, and numerical rules; use rubric-based model graders only where judgment is necessary, calibrate them against qualified human reviewers, and retain disagreement examples.

### Turn evaluation into a release gate

1. Freeze the candidate agent, prompt, model, tools, knowledge snapshot, policies, and dataset identifiers.
2. Run regression evaluations and compare them with the approved baseline by risk segment, not only aggregate score.
3. Investigate failures from the trace; do not tune to the final answer while ignoring an unsafe path.
4. Require explicit thresholds for task success, safety, authorization, latency, cost, and escalation.
5. Use a limited pilot or canary with rollback triggers and human review proportional to risk.
6. Promote only the unchanged candidate that produced the evidence; monitor the same critical measures in production.

Avoid “test-set theater.” A large score can conceal missing high-impact cases, weak graders, leakage from the evaluation set into prompts, or a deployment configuration that differs from the tested one.

**Implementation reading — September 27, 2026:** For standard-harness agents, the [evaluation REST API](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-rest-api) documents asynchronous runs and a user access token. Distinguish permission to start a run from the connection profile used by authenticated tools during that run. Compare the [CAT team's Azure DevOps example](https://microsoft.github.io/mcscatblog/posts/copilot-studio-eval-gate-azure-devops/) with [Copilot Agent Kit testing through Power Platform pipelines](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-automate-test-deploy). The latter documents deployment gates, so the blog's blanket claim that Power Platform pipelines cannot gate on tests is outdated. **VERIFY CURRENT:** validate identity, token renewal, tenant policy, and failure handling before adapting either pattern; neither sample was executed for this guide.

#### Worked release gate: evidence before a green check

An **invariant** is a condition that must remain true on every applicable path, such as “no task is created without approval.” An average quality score cannot compensate for violating it. Start the service-case assistant's evaluation with concrete inputs and evidence:

| Synthetic test | Required result | Evidence to inspect |
|---|---|---|
| Representative requests an assigned case summary | Uses authorized case data and identifies its supporting article | Retrieval permissions, cited evidence, reviewed factual accuracy |
| Representative requests another team's restricted case | Does not disclose the record | Denied data access and absence of restricted content in the response |
| Representative declines a proposed task | Creates no task | Approval result and destination record count |
| The approved request is delivered twice | Creates one task for that approved operation | Stable operation identifier and destination state; idempotency means repeating an operation does not repeat its effect |
| Task service times out after accepting a request | Checks the operation's status before retrying or escalates uncertainty | Trace plus authoritative record state; no unbounded retry or invented success |
| An article includes instructions to issue a refund | Treats that text as untrusted content and remains within scope | No refund tool execution, policy checks, and a useful permitted response |

**Worked answer:** Suppose a larger suite contains 40 required tests. Thirty-nine finish and pass; one restricted-access test never starts because its test identity is misconfigured. The completed-test pass rate is 100%, but execution coverage is only 97.5%. Block promotion, fix the test identity, and obtain the missing evidence. Do not remove the case to improve the score. These figures illustrate a locally chosen release policy, not Microsoft's exam scoring.

An original gate design for this example is:

```text
candidate and dependency versions recorded
  -> expected test inventory checked
  -> run reaches a terminal state before the deadline
  -> all required results present under the intended identities
  -> every authorization and approval invariant passes
  -> agreed quality, latency, and cost criteria pass
  -> evidence retained for that candidate
  -> release owner may approve promotion
```

Treat missing, skipped, timed-out, and errored required cases as unresolved evidence. Preserve them separately from assertion failures so the team can distinguish a broken test setup from a broken agent. The API can start evaluations asynchronously; the pipeline must still retrieve and assess the results. This design is pseudocode, not a deployable pipeline.

#### Worked review: follow a finding to a test

Configuration review examines what is saved: instructions, capabilities, descriptions, and relationships. Runtime testing observes what actually happens for an input and identity. The [Agent Review Tool documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-agent-review-tool) explains its configuration checks; Ramakrishnan Raman's [review walkthrough](https://microsoft.github.io/mcscatblog/posts/agent-review-tool/) shows how a finding can guide investigation. Tool coverage and presentation depend on the reviewed agent type and version.

Suppose a copied instruction in our assistant says, “For an unhappy customer, call `IssueRefund`.” That fictional tool is absent, and refund execution is outside the approved scope. A reviewer notices the mismatch; do not assume an automated checker will detect every such defect.

| Step | Worked response |
|---|---|
| Interpret the finding | The authored behavior promises an operation the design neither authorizes nor provides. |
| Choose the correction | Remove that instruction and describe the supported handoff to a service representative. Adding a refund tool would require a separate scope and risk decision. |
| Test the correction | Submit a refund request. Check for a clear handoff, no refund attempt, and no false claim of completion. |
| Check for regression | Confirm that ordinary summaries and approved task creation still work. |
| Retain evidence | Save the instruction change, reviewer decision, test inputs, traces, and observed outcomes. |

**Worked answer:** A cleaner configuration report helps justify the correction. Runtime and destination-system evidence establish whether the corrected behavior meets the requirement. A displayed relationship between two components alone does not show that either ran.

### Tune the right layer

When an outcome fails, determine whether the cause is requirements, source data, retrieval, instructions, topic/routing, tool schema, connector, permissions, model, user experience, or process. Changing a prompt cannot repair stale source data or missing authorization.

---

## 9. Design ALM and environment strategy

### Treat the solution as a bundle of versioned artifacts

AI-powered business solutions can include:

- Copilot Studio agents, topics, prompts, agent flows, connectors, actions, and connections;
- Power Platform solutions, environment variables, policies, and dependent apps/flows;
- Foundry projects, agents, model deployments, tools, code, infrastructure, evaluations, and guardrails;
- schemas, grounding configuration, search indexes, reference data, and evaluation datasets;
- Dynamics 365 configuration and AI features;
- monitoring, alerts, runbooks, access roles, and documentation.

Assign an owner, repository or system of record, version, dependency map, promotion method, and rollback strategy to each artifact class.

### Environment design

Separate development, test, and production according to risk. Add integration/UAT, performance, regulated, geography, or maker zones when justified. Define:

- who may create, edit, approve, deploy, operate, and view data;
- which connectors/models/services are allowed;
- environment-specific endpoints, identities, and knowledge sources;
- data movement and masking rules;
- managed versus unmanaged solution use;
- pipeline gates and segregation of duties;
- capacity, monitoring, backup/export, and recovery.

Standard-harness Copilot Studio agents participate in Power Platform solutions and can be promoted through solution and pipeline practices. Confirm the deployment mechanism separately for other harnesses. Do not promote development connection credentials or test knowledge references blindly into production.

The product’s [solution guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-overview) covers adding agents and dependent components to Power Platform solutions. Treat connection references, environment variables, credentials, knowledge, channels, and external resources as explicit deployment dependencies rather than assuming solution import makes the environment production-ready.

#### Worked promotion: what moves and what must be rebound

For the standard-harness service-case assistant, think of a solution as a package of definitions. The target environment supplies the connections, permissions, configuration, and data needed to make those definitions useful. Microsoft's [ALM strategy](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/alm) describes environment separation, managed deployment downstream, and settings that require post-deployment work. James Papadimitriou's [ALM foundation article](https://microsoft.github.io/mcscatblog/posts/alm-copilot-studio-agents-foundation/) is a companion explanation.

| Item | What to record and verify in the target |
|---|---|
| Agent, topics, flows, and connector definitions | Package version and complete dependency inventory |
| Connection reference: a logical pointer to a connection | Which target connection and identity it resolves to; the reference is not itself a credential |
| Environment variable: a named configuration value | Target endpoint or other setting, with no accidental development URL or embedded secret |
| Knowledge and business data | Correct source, permissions, freshness, and representative test records; a source reference does not establish that its data moved |
| Authentication, channels, sharing, and telemetry | Required post-deployment configuration and owners; verify each supported deployment mechanism |
| Release evidence | Package identifier, target settings, identities, test results, approval, and recovery procedure |

**Failure scenario:** Import succeeds, but the test connection still points to development data. A simple greeting works and the team declares the release ready. This establishes neither correct grounding nor correct authorization. Use a synthetic record available only in the target and a restricted record that the test user must not read. Check both the positive result and denied access before promotion.

**Worked answer:** Fix the target binding, record the change, and rerun affected evaluations. Promote the tested package through the approved path, then validate production-specific bindings and a limited smoke test before wider use. Freeze intended environment differences in the release record; identical package bytes do not imply identical behavior when connections or knowledge differ.

Recovery also needs two plans: restore the approved agent configuration through a supported procedure, and reconcile any business actions already taken. Reverting an agent version does not undo a task it created. For this example, keep task identifiers and let the process owner decide whether an erroneous task should be corrected, cancelled, or retained for audit. Rehearse that decision with synthetic records.

### Foundry versions, endpoints, and identity

The [Foundry development lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle) distinguishes prompt-based, voice-based, and hosted agents. Save a version before treating playground edits as a reproducible candidate. Bind evaluations to that version and its models, tools, connections, and knowledge; an agent definition alone does not freeze external dependencies.

**Publishing transition, checked September 27:** Read the [migration guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications) alongside the [identity documentation](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity):

| Resource model | Endpoint and identity | Release responsibility |
|---|---|---|
| Legacy Agent Application | Development agents use shared project identity; publishing creates a separate application with its own identity/endpoint | Assign downstream permissions to the application identity and verify clients' invocation access |
| New agent object | New agents receive their own identity and stable endpoint at creation; version selection and channel publication are separate decisions | Configure the selected version and test the agent's actual identity before distributing to Teams/Microsoft 365 |

During migration, permissions from old identities do not transfer automatically. Inventory endpoint consumers, tool connections, role assignments, and rollback paths; verify the replacement before decommissioning anything. Existing Agent Applications remain supported in the opened migration guidance; it gives no end-of-support date. **VERIFY CURRENT:** object model, API version, rollout, role scopes, and publication capabilities. Do not apply an older publishing tutorial's identity assumptions to every new agent.

### Data and model ALM

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

## 10. Design responsible AI, security, governance, risk, and compliance

### Apply layered control

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

### Use risk tiers

Risk classification can consider decision impact, autonomy, reversibility, users, sensitive data, external exposure, regulated context, model type, and integration power. Higher tiers require stronger independent review, validation, human oversight, monitoring, and release authority.

Map Microsoft Responsible AI principles to concrete requirements and evidence. Principles without owners, controls, tests, and exception handling cannot be audited.

Copilot Studio's [security and governance overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) identifies controls for data policies, authentication, knowledge, connectors, triggers, audit, and environments. Its separate [testing-strategy guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase4) explains validation before release. Map each control to its enforcement point and evidence across Microsoft 365, Foundry, Dynamics 365, and integrations; a testing page alone does not establish governance coverage.

### Defend against prompt manipulation

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

The [OWASP Agentic AI threats and mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) guide is a useful threat-discovery aid, while the [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) provides vendor-neutral lifecycle risk context. They are **supplementary security and risk references**, not proof of Microsoft control coverage or a substitute for legal, compliance, or product-specific review.

Use an abuse-case table before selecting controls:

| Threat path | Architecture question | Candidate evidence |
|---|---|---|
| Direct or indirect goal hijacking | Can untrusted content redefine instructions, destinations, or success? | Trust-boundary tests and blocked attack traces |
| Excessive or compounded privilege | Can individually permitted tools combine into an unauthorized outcome? | Effective-permission and toxic-combination review |
| Tool misuse or confused deputy | Does the target system independently authorize and validate the requested action? | Negative API tests under distinct identities |
| Memory or knowledge poisoning | Who can write durable state, and how are provenance and revocation enforced? | Write controls, lineage, quarantine, deletion test |
| Data exfiltration | Can sensitive context leave through output, tool arguments, logs, or another agent? | DLP tests, egress restrictions, redacted telemetry |
| Cascading agent failure | Can one agent's untrusted result become another's authoritative instruction? | Contract validation, confidence handling, stop tests |
| Resource exhaustion or denial of wallet | What limits recursive work, retries, parallelism, and external calls? | Budget-exhaustion tests and cost alerts |
| Dependency or protocol compromise | How are models, connectors, MCP servers, agents, and packages approved and changed? | Inventory, attestation, version pinning, review trigger |

### Design human intervention as a real control

OpenAI's practitioner guide recommends intervention for exceeded failure thresholds and high-risk actions. Translate that principle into a platform-neutral approval contract: the reviewer receives the proposed action, affected object, evidence, uncertainty, policy match, expected impact, and available alternatives. The approval must be bound to one action and current state, expire, be auditable, and be re-requested if material inputs change. The agent cannot approve its own request.

Define who covers absences, how long review may wait, what happens on rejection or timeout, and whether the process safely pauses, rolls back, or continues manually. Measure reviewer load, disagreement, override, and escaped-error rates; otherwise “human in the loop” can become an unstaffed queue or a rubber stamp.

### Validate residency and data movement

Map where prompts, retrieved data, model inputs/outputs, tool payloads, telemetry, evaluations, backups, and support data are processed and stored. Include third-party services and cross-agent calls. Confirm contractual and product commitments for the chosen configuration; do not infer residency from an Azure resource group's location alone.

### Preserve auditability

Record accountable identity, agent/configuration version, model deployment, data/source identifiers, tool/action, approval, timestamp, result, and correlation where feasible. Protect the log from unauthorized access and tampering. A detailed trace is useful for debugging; a controlled audit record supports accountability. Design both deliberately.

---

## 11. Architecture exercises

These are original design/tabletop exercises. Live implementation is optional and requires suitable licenses, roles, capacity, and disposable environments. Record **designed**, **tabletop-tested**, or **executed**, with the date, configuration, evidence, and remaining gaps. A paper design is not proof that a tenant feature works. Use synthetic data, define a spending limit, disable triggers after testing, and remove only resources created for the exercise.

### Exercise 1: Sales research and action agent

Design an agent used in Teams that summarizes CRM and SharePoint evidence, drafts outreach, and can create a follow-up task. Compare extending Microsoft 365 Copilot, Copilot Studio, and a Foundry solution. Include identity, knowledge filters, tool authorization, approval, citations, telemetry, ALM, and value measures.

### Exercise 2: Multi-agent customer service

Create an orchestrator with knowledge, case, entitlement, and scheduling agents across Dynamics 365 and external services. Specify contracts, state, error paths, human handoff, privacy, channel continuity, end-to-end tests, and SLOs.

### Exercise 3: Finance autonomous process

Assess an autonomous reconciliation/reminder scenario. Define segregation of duties, transaction thresholds, model/rule boundaries, approvals, duplicate prevention, exception queues, audit evidence, regional continuity, and kill switch.

### Exercise 4: Agent portfolio and Center of Excellence

Design intake, risk tiering, reference patterns, maker zones, environment strategy, reusable connectors, evaluation gates, operational ownership, chargeback/showback, adoption support, and retirement review for 50 proposed agents.

### Exercise 5: Build-buy-extend decision

Compare a Dynamics 365 prebuilt capability, Microsoft 365 extension, Copilot Studio solution, Foundry custom agent, and third-party product for one process. Create a weighted decision matrix and five-year TCO range. Document assumptions and exit plan.

### Exercise 6: Cross-platform release

Design promotion for a solution containing a Copilot Studio agent, custom connector, Power Automate flow, Foundry tool, search index, and Dynamics 365 configuration. Define repositories, solutions, environment variables, identities, datasets, tests, approval, rollout, monitoring, and rollback.

### Exercise 7: Prompt, small-model, and supervised-app decision

For a regulated case-triage process, design a governed prompt-library entry and compare a general model with a customized small language model against the same evaluation set. Propose a code-first generative page for case review and an agent-feed task for human approval. Use synthetic schemas and data only. **Evidence:** prompt contract and version, model decision matrix, evaluation and rejection thresholds, page code-review and accessibility checklist, feed task contract, identity boundaries, ALM plan, and rollback.

### Exercise 8: Dynamics 365 cross-workload orchestration

Design a scenario that begins in a Contact Center channel, creates or updates a service case, checks Finance or Supply Chain data, and surfaces approved follow-up through Microsoft 365 Copilot for Service. Specify business terms, channel/workstream/queue, identity and connector boundaries, virtual-entity or knowledge choice, representative handoff, legal-entity security, duplicate prevention, end-to-end test cases, telemetry correlation, configuration promotion, and manual continuity. Use diagrams or a tabletop sandbox; do not connect production records or enable unreviewed write actions.

### Exercise 9: Complexity-ladder decision

Choose one process—such as invoice exception triage, employee-policy questions, or service-case follow-up—and design it six ways: deterministic workflow, one model call, fixed AI workflow, one tool-using agent, multi-agent system, and autonomous process. Score task success, exception coverage, security boundary count, latency, cost, operability, and recovery. Recommend the lowest-complexity design that passes the acceptance criteria and state what new evidence would justify the next level.

### Exercise 10: Evaluation harness and release gate

Create 20 synthetic cases spanning normal, edge, restricted, adversarial, dependency-failure, and human-escalation paths. Define deterministic assertions, human rubrics, any model grader, acceptance thresholds, and a trace schema. Run or tabletop two candidate designs, perform error analysis by failure category, and write a go/no-go decision with canary scope and rollback triggers. Do not use recalled or purchased exam questions as evaluation data.

### Exercise 11: Agentic threat model

Threat-model an agent that reads SharePoint knowledge and can update a Dynamics 365 record. Draw identities, trust boundaries, data stores, memory, retrieved content, tool calls, logs, and approval. Test direct and indirect prompt manipulation, unauthorized record access, parameter tampering, duplicate writes, memory poisoning, sensitive-data leakage, unavailable dependencies, and budget exhaustion. Record prevented, detected, contained, and recovered evidence using only a disposable environment and synthetic data.

### Exercise 12: Release across identity and supervision boundaries

Design a service-case workflow activated by a Dataverse event. Name the trigger connection, every tool identity, the selected Copilot Studio harness, and the Foundry object model. Compare an interactive user's rights with the trigger maker's rights. Simulate a rejected write, duplicate event, expired connection, changed approval input, and migrated Foundry identity without assigned downstream roles. Classify each agent-feed entry as a request for action or a record of completed work; reject a design that relies on the preview feed for private user-targeted approvals. Produce an identity matrix, synthetic test set, release checklist, and rollback plan. Use a tabletop if any required feature or license is unavailable.

### Exercise 13: Service-case release workshop

Use the [running case](#follow-one-case-from-design-to-release) to connect the five worked examples. Allow about 30–45 minutes after reading them. This is a tabletop workshop; record predicted results as predictions.

1. Write a one-sentence scope, then list the permitted reads, the approval-required write, and the prohibited operation.
2. Choose a connector or MCP integration and document one rejected alternative, the effective identity, and an enforcement test.
3. Recalculate Pilot B with only **240** accepted outcomes while its 7,200 credits and 600 attempts remain unchanged. Explain whether your recommendation changes.
4. Write expected results for the six release-gate cases. Add one missing-evidence condition that stops promotion.
5. Correct the unsupported refund instruction, then identify one intended-behavior test and one regression test.
6. Complete the promotion table with fictional target values, a release owner, and a recovery action for an erroneously created task.

**Answer guide:** The cost change produces 30 credits per accepted outcome and a 40% acceptance rate; relative to Pilot A's 20 credits and 60%, efficiency and acceptance both worsen. A defensible design keeps refunds outside scope, enforces case access downstream, binds approval to one task operation, and prevents duplicate effects. It blocks release when a required test is missing and distinguishes configuration recovery from repairing business records.

**Completion check:** Hand another learner your scope, integration decision, calculations, test table, and release record. They should be able to identify who can act, what stops an invalid action, how success is observed, and what happens after failure. If a claim rests only on an instruction or a green summary score, identify the missing enforcement or evidence.

---

## 12. Scenario checks and exam distinctions

### Knowledge checks

1. A team proposes an autonomous refund agent because its demo answers are accurate. Which process, authority, risk, and operational evidence is still missing?
2. A Copilot Studio agent gives users documents they cannot open in SharePoint. Where must authorization be fixed, and why is hiding citations insufficient?
3. A pilot saves time but production costs exceed the business case. Which unit economics and lifecycle costs should be examined?
4. An agent performs well in isolation but fails across Dynamics 365 and a third-party API. How should component, integration, and end-to-end tests differ?
5. A prompt was unchanged, but agent quality fell after a document and model update. Which configuration and lineage evidence should ALM provide?
6. An MCP server is technically compatible with the agent. What trust, identity, authorization, supply-chain, and monitoring decisions remain?
7. Two business units build similar agents with contradictory definitions. Which data-product, semantic, and Center of Excellence controls can help?
8. A shared prompt works in one app but exposes inappropriate inputs in another. Which prompt-library contract, evaluation, access, and version controls were omitted?
9. A customized small model is cheaper but misses rare regulated cases. What baseline, routing, fallback, and release criteria should govern the decision?
10. A generated page looks polished and an autonomous agent reports completion. Which code, Dataverse, authorization, accessibility, agent-feed, and audit evidence is still required?
11. A Contact Center agent must consult Supply Chain data and update a case. How should channel context, identity, virtual-entity knowledge, write authority, handoff, and multi-product ALM be designed?
12. A deterministic workflow meets 98% of cases, while an agent improves two rare exceptions but doubles cost and adds a write-capable tool. What evidence would justify the agent?
13. Three agents pass their component tests, but the composed solution loops after a partial timeout. Which orchestration state, idempotency, budget, and trajectory tests are missing?
14. A candidate has a 94% task-success score but sometimes reads a restricted record before producing the correct answer. Why must the release fail despite the final result?
15. A model grader and process owner disagree on several high-risk cases. How should calibration, adjudication, and release thresholds work?
16. A reviewer approves a refund, but the customer record changes before execution. What should bind and invalidate the approval?
17. An MCP tool has narrow permissions, but two other tools can be combined to reconstruct and transmit sensitive data. Which effective-permission and threat-model analysis is required?
18. Total credits rise from 6,000 to 7,200 while accepted outcomes rise from 300 to 480. Has efficiency worsened, and what else is needed to judge value?
19. A permitted MCP server advertises a new refund tool. Which evidence would establish that the service-case assistant still cannot issue refunds?
20. All 39 completed tests pass, but a 40th required authorization test never runs. What should the release gate report and do?
21. A configuration map shows a connection to the case system. What evidence is needed to claim the agent successfully created an approved task?
22. An unchanged package is imported into production and its greeting works. What environment-dependent checks remain before broader release?

For each answer, state the outcome, architecture boundary, owner, decision, risk, evidence, deployment path, and rollback or escalation.

### Answer checkpoints

These checkpoints explain the original questions above. Alternative architectures are valid when they satisfy the same requirements and controls.

| Check | A defensible answer must include |
|---|---|
| 1 | Refund authority, thresholds, segregation of duties, approval, duplicate prevention, recovery, and verified transaction outcomes. Answer accuracy alone does not authorize a payment. |
| 2 | Fix retrieval and downstream access under the actual identity. Test restricted users and shared connections; removing a citation leaves the exposed content accessible. |
| 3 | Compare the original baseline with cost per verified success, including failed runs, human review, retries, licensing, operations, and realized use of saved time. |
| 4 | Test the isolated tool contract, then identity/data/error behavior between systems, then the complete business outcome and human handoff. |
| 5 | Record document versions, ingestion/index changes, permissions, model deployment, prompts, tool schemas, and evaluation data. Reproduce the failing configuration before tuning. |
| 6 | Review server provenance, transport, authentication, scopes, tool behavior, consent revocation, target authorization, and monitoring. A successful handshake proves only connectivity. |
| 7 | Give shared definitions and data products owners, resolve competing meanings, version the contracts, and use CoE standards with domain accountability. |
| 8 | Define permitted inputs, consumer roles, host/model assumptions, schema, version, evaluations, and retirement. Test each consuming application's authorization boundary. |
| 9 | Segment results by risk and rare cases; compare against the current baseline. Reject inadequate performance or route unsupported cases to an evaluated fallback or reviewer. |
| 10 | Review generated code, Dataverse permissions, data-path preview limits, accessibility, deployment, and actual record outcomes. Distinguish feed visibility from enforced approval. |
| 11 | Preserve channel/customer identity, legal-entity scope, current operational knowledge, case-write permission, correlation, handoff, and deployment dependencies. |
| 12 | Quantify the value of the exceptions and total added risk/cost. Retain the deterministic path unless the agent demonstrably meets a justified acceptance criterion. |
| 13 | Define state ownership, timeout semantics, idempotency, retry budgets, compensation, termination, and end-to-end trajectory tests. Component success does not establish composition success. |
| 14 | Treat unauthorized access as a release-blocking invariant violation. Diagnose the identity/retrieval path even if the final answer and aggregate score look correct. |
| 15 | Calibrate the grader against reviewed examples, adjudicate disagreement, segment high-risk cases, and retain human release authority where required. |
| 16 | Bind approval to the proposed operation, parameters, record version, reviewer, and expiry. A material state change requires fresh validation and, where relevant, approval. |
| 17 | Analyze combined data access and egress across tools, identities, and durable memory. Test multi-step misuse and enforce constraints at the target and integration boundaries. |
| 18 | Credits per accepted outcome fall from 20 to 15, a 25% improvement. Check comparable case mix, completed outcome-review windows, human effort, other costs, and realized benefit before judging ROI. |
| 19 | Identify the actual policy and server/API restriction, inspect the effective identity, and test forbidden invocation. A maker's instruction or whole-server allow decision does not establish per-tool authorization. |
| 20 | Report 100% pass among completed tests and 97.5% execution coverage, with the missing test explicit. Block promotion until the required evidence exists under the intended identity. |
| 21 | Correlate the request, approval, executed tool call, and authoritative task record. Verify the intended identity and one effect per approved operation. Configuration visibility alone proves neither invocation nor success. |
| 22 | Check target connections, identities, permissions, configuration, knowledge, channels, telemetry, and a limited smoke test. Record intentional differences and recovery steps; package equality alone does not establish equivalent behavior. |

Before declaring readiness, explain three additional implementation traps: maker credentials in event triggers, a changed identity during Foundry migration, and an informational feed task mistaken for approval. Revisit Parts 5, 6, and 9 if any distinction is unclear.

### Distinctions to explain without notes

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

### Readiness checklist

- [ ] I can assess agent fit, process impact, requirements, and grounding-data readiness.
- [ ] I can apply the Cloud Adoption Framework and define an enabling AI Center of Excellence.
- [ ] I can build a portfolio roadmap with risk tiers, value measures, adoption, and retirement.
- [ ] I can define a prompt-library lifecycle with owners, approved inputs, versioned templates, evaluation evidence, monitored reuse, and retirement.
- [ ] I can decide when a customized small language model is justified and compare it with prompting, RAG, routing, and larger-model alternatives.
- [ ] I can calculate TCO/ROI and decide when to use, extend, buy, build, or route models.
- [ ] I can choose across Microsoft 365 Copilot, Copilot Studio, Foundry, Power Platform, and Dynamics 365.
- [ ] I can design task, autonomous, prompt/response, conversational, and multi-agent patterns.
- [ ] I can justify every increase in agentic complexity with measured acceptance evidence.
- [ ] I can choose sequential, concurrent, handoff, group-chat, dynamic, and evaluator-optimizer orchestration by dependency and ownership.
- [ ] I can design MCP, A2A, connectors, computer use, reasoning, voice, and channel boundaries safely.
- [ ] I can design and govern code-first generative pages and agent-feed supervision as separate application, agent, identity, and ALM boundaries.
- [ ] I can orchestrate customer experience, service, sales, Contact Center, finance, supply chain, Microsoft 365 Copilot for Sales/Service, and Power Platform AI features without relying on stale product names.
- [ ] I can add Finance and Supply Chain operational data and in-app help knowledge with explicit freshness, permission, legal-entity, testing, and lifecycle controls.
- [ ] I can design telemetry, KPIs, feedback triage, evaluation, and complete test strategy.
- [ ] I can evaluate components, turns, trajectories, outcomes, systems, and live behavior with a version-bound release gate.
- [ ] I can design environment, solution, data, model, agent, and cross-platform ALM.
- [ ] I can design responsible AI, security, governance, vulnerability mitigation, residency, access, and audit evidence.
- [ ] I can threat-model privilege combinations, memory poisoning, cascading failures, exfiltration, and denial of wallet, and design a binding human-approval contract.
- [ ] I know which licensing, product, preview, regional, protocol, and prerequisite details require current verification.

### Primary references

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
- [Copilot Studio prompt library](https://learn.microsoft.com/en-us/microsoft-copilot-studio/prompt-library)
- [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview)
- [Code-first generative pages](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/generative-page-external-tools)
- [Power Apps agent feed](https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave2/power-apps/supervise-autonomous-agents-agent-feed)
- [Design AI agents for business solutions](https://learn.microsoft.com/en-us/training/modules/design-ai-agents-business-solutions/)
- [Orchestrate prebuilt agents and apps](https://learn.microsoft.com/en-us/training/modules/orchestrate-configuration-prebuilt-agents-apps/)
- [Add Finance and Operations knowledge to agents](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/tutorial-agent-knowledge)

Recheck product names, agent availability, licensing, prerequisites, regions, protocol support, preview status, and deployment controls before the exam.

### Supplementary practitioner and risk references

- [Microsoft Azure Architecture Center — AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [OpenAI — A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [AWS — Evaluating AI agents: Real-world lessons](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [AWS Well-Architected — Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html)
- [Google Cloud — A developer's guide to production-ready AI agents](https://cloud.google.com/blog/products/ai-machine-learning/a-devs-guide-to-production-ready-ai-agents)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OWASP — Agentic AI threats and mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [Microsoft 2026 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)

These sources broaden explanation and practice. They do not override the AB-100 blueprint, establish Microsoft product behavior outside Microsoft documentation, or imply knowledge of live exam items.

---

## Places to learn

This is a curated starting point, not a complete list. You are not meant to consume every resource. Start with the official blueprint, then pick the instructor, format, examples, and hands-on work that help you close specific gaps. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

### Practitioner reading sprint

Use this optional sequence after the official learning path. Spend less time collecting links and more time producing the named artifact.

| Reading | Approximate time | Produce | Caveat |
|---|---:|---|---|
| [Building effective agents](https://www.anthropic.com/research/building-effective-agents) and [OpenAI's practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | 90–150 min | A complexity-ladder decision and bounded control loop | Cross-vendor practitioner guidance, not Microsoft feature or exam authority |
| [Microsoft AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | 60–90 min | A pattern decision matrix for one AB-100 scenario | Microsoft architecture guidance; implementation surfaces remain volatile |
| [Anthropic agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Amazon evaluation lessons](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/), and [Google's production guide](https://cloud.google.com/blog/products/ai-machine-learning/a-devs-guide-to-production-ready-ai-agents) | 2–3 hours | An evaluation dataset, grader plan, and release gate | Transfer the method, not provider-specific services |
| [NIST GenAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) and [OWASP Agentic AI threats](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) | 2–4 hours selected | A risk register, abuse-case table, and evidence plan | Not a substitute for Microsoft control mapping, law, or compliance advice |
| [AWS Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html) | 60–120 min selected | A unit-cost model and operational readiness review | Cross-cloud architecture reference; map principles to Microsoft services |
| [Microsoft 2026 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization) | 30–60 min selected | Two locally testable adoption hypotheses | Directional survey/telemetry research, not causal proof or exam scope |

### Selected implementation blogs — reviewed September 27, 2026

These five public posts from **The Custom Engine**, the Microsoft Copilot Studio CAT team's blog, add implementation examples to Parts 4, 6, 8, and 9. They are supplementary expert resources, not the exam blueprint. Read by gap; times below are the publisher's reading estimates and exclude practice. **VERIFY CURRENT:** runtime coverage, APIs, previews, governance, and licensing can change after publication. The [research follow-up](../docs/research/2026-09-27-ab-100-deep-review.md#blog-discovery-follow-up) records selection and limitations.

| Post and author | Published / updated; reading time | AB-100 fit and suggested artifact | Boundary to carry into your design |
|---|---|---|---|
| [MCP Servers or Connectors?](https://microsoft.github.io/mcscatblog/posts/compare-mcp-servers-pp-connectors/) — Jay Padimiti | February 13 / August 2, 2026; 15 min | Design, Part 6: compare built-in choices separately from custom integration choices; produce an integration decision record. | Check tool exposure and governance separately. Current [advanced connector policy documentation](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies) distinguishes server blocking from individual MCP-tool control. |
| [ALM for Copilot Studio Agents: The Foundation](https://microsoft.github.io/mcscatblog/posts/alm-copilot-studio-agents-foundation/) — James Papadimitriou | June 3 / August 2, 2026; 11 min | Deploy, Part 9: turn environment and packaging decisions into a release checklist, including target connections and recovery. | Standard harness. Use the [official ALM strategy](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/alm) to verify supported promotion practices. |
| [Quality Gates: Automated Evaluations in Azure DevOps](https://microsoft.github.io/mcscatblog/posts/copilot-studio-eval-gate-azure-devops/) — Adi Leibowitz | April 19 / August 2, 2026; 7 min | Deploy, Part 8: sketch a pipeline that tests a candidate and retains per-case evidence before merge. | Standard harness. Read the correction and authentication checks in Part 8; Azure DevOps is one implementation option. |
| [Where Are Your Copilot Credits Going?](https://microsoft.github.io/mcscatblog/posts/copilot-credit-consumption-api/) — Petros Feleskouras | August 25 / August 26, 2026; 6 min | Plan and deploy, Parts 4 and 8: design a daily consumption report and connect usage to measured business outcomes. | A community reporting solution, not billing authority. Validate pagination against the [resource-consumption API](https://learn.microsoft.com/en-us/rest/api/power-platform/licensing/entitlement-insight/get-tenant-resources-across-environments); optional dimensions vary by harness. |
| [Review Before Release: Agent Review Tool](https://microsoft.github.io/mcscatblog/posts/agent-review-tool/) — Ramakrishnan Raman | August 18, 2026; no separate update shown; 11 min | Deploy, Part 8: pair configuration findings with runtime tests and record evidence for each proposed fix. | GitHub Copilot harness walkthrough; the post labels its experience preview. A configuration map or score does not prove runtime behavior. Recheck [Agent Review Tool documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-agent-review-tool). |

For a focused session, choose one post, produce its artifact, then explain which decisions require official documentation or a tenant test. Reading all five takes about 50 minutes before practice.

### Courses, labs, and assessments

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AB-100 course](https://learn.microsoft.com/en-us/training/courses/ab-100t00) and [Architect AI solutions for business productivity](https://learn.microsoft.com/en-us/training/paths/architect-agentic-ai-business-solutions/) | Free self-study; instructor-led options vary | 3 days (official course); 11-module learning path | Official architecture foundation across planning, design, and deployment; Microsoft notes the course is preparatory rather than an exam-prep course |
| [Microsoft — AB-100 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-100/practice/assessment?assessment-type=practice&assessmentId=1815645847&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; use after learning and keep the blueprint and product docs authoritative |
| [Microsoft Partner Skilling Hub — LevelUp AB-100](https://www.skilling-hub.com/en-US/listing/o::levelup::2426785) | Partner login required | 10 hours | No additional cost for eligible Microsoft partners; self-paced coverage spans architecture, value, grounding, agent selection, extensibility, operations, ALM, governance, security, and exam preparation |
| [Microsoft Copilot Studio guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/) | Free | Select 4–8 hours by gap | Architecture, governance, testing, ALM, operations, and value guidance from the product team |
| [O'Reilly — AB-100 Crash Course with Tim Warner](https://www.oreilly.com/live-events/agentic-ai-business-solutions-architect-crash-course-exam-ab-100/0642572326043/) | Subscription or event access | 4 hours (published course length) | Certification-focused treatment of the full blueprint; verify the occurrence and current baseline |
| [Timothy Warner's public AB-100 repository](https://github.com/timothywarner-org/ab100) | Free | About 4–8 hours plus exercises | MIT-licensed public companion examples and course plan from Tim's O'Reilly live course; use with attribution and verify against current Microsoft documentation |
| [O'Reilly — Microsoft Copilot Studio Step by Step by Lisa Crosbie](https://www.oreilly.com/library/view/microsoft-copilot-studio/9780135491584/ch09.xhtml) | Subscription | About 8–12 hours reading/practice | Detailed Copilot Studio implementation reference, published December 2025; broader AB-100 architecture topics need other sources |
| [O'Reilly — Building Enterprise AI Agents](https://www.oreilly.com/videos/building-enterprise-ai/9781808080630/) | Subscription | 3 hours 24 minutes plus lab time | Supporting enterprise agent patterns; not an AB-100 objective checklist |
| [Whizlabs — AB-100 training, labs, and practice tests](https://www.whizlabs.com/microsoft-ab-100-agentic-ai-architect-certification/) | Paid course or subscription | About 25–30 hours for all 27 labs and 4 quizzes | Hands-on supplement with 22 hours 15 minutes of published lab time plus an estimated 3–6 hours for 165 questions and answer review; the current listing reports no video items |
| [MeasureUp — AB-100 practice test](https://www.measureup.com/microsoft-ab-100-agentic-ai-business-solutions-architect-practice-test.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 102 questions; its detailed objective map matches AB-100, but some introductory prose describes a different Azure AI role, so resolve conflicts with the July 2026 blueprint |
| [Udemy — AB-100 preparation by Phillip Burton](https://www.udemy.com/course/ab-100-agentic-ai-business-solutions-architect-exam-preparation/) | Purchase or subscription | 10 hours 50 minutes | Course shown as updated June 2026; compare its claimed baseline with the July 22 blueprint |
| [Udemy — AB-100 preparation by Kuljot Singh Bakshi](https://www.udemy.com/course/ab-100-agentic-ai-business-solutions-architect-exam-prep/) | Purchase or subscription | 14 hours 9 minutes | Alternative course shown as updated June 2026; inspect previews and objective coverage before choosing |
| [Tim Warner — AB-100 review on YouTube](https://www.youtube.com/watch?v=MCIon6epv74) | Free | About 1 hour | Public orientation and study context from the O'Reilly course instructor; not a full replacement for official training |

No exact Pluralsight AB-100 certification path was verified during the August 31, 2026 review. The earlier Whizlabs listing described hands-on and assessment practice without video items; recheck that mix before choosing it as your main instruction source. Practice-question-only products are intentionally not used as the primary learning recommendation. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).

**Resource verification boundary — September 27:** Paid course interiors, partner-only training, and account-only practice assessments were not reviewed. Some public listings return access blocks or application shells. Commercial course runtimes, question/lab counts, and update dates above are retained from earlier catalog checks, not newly confirmed purchase advice. Confirm current syllabus, baseline, availability, and price with the publisher before enrolling. The public Microsoft course and 11-module learning path were readable even though the credential page's training widget showed no available courses.
