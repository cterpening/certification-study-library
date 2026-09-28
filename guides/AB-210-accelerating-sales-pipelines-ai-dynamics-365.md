---
exam_code: AB-210
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-210
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: review-required
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AB-210 Accelerating Sales Pipelines with AI in Dynamics 365 Study Guide

> **Independent AI-assisted resource — REVIEW REQUIRED; HUMAN REVIEW PENDING.** The September 28, 2026 [deep review](../docs/research/2026-09-28-ab-210-deep-review.md) mapped all 46 detailed objectives against the unchanged official page last updated June 18, 2026. Official custom-field support and Close Agent shutdown contradictions remain unresolved. Worked examples were checked offline; tenant labs were not executed. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-210-coverage-record). The [official AB-210 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-210) is authoritative.

**Current baseline:** Official study guide last updated June 18, 2026; Microsoft publishes no separate skills-effective date.<br>
**Upcoming blueprint change:** None announced, but the exam remains labeled **beta**; scope and product behavior may change before general availability.<br>
**Lifecycle:** The [Dynamics 365 Sales AI Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-sales-ai-consultant-associate/) and 120-minute beta exam are active. As checked September 28, 2026, Microsoft lists English, Chinese (Simplified), French, German, Japanese, Portuguese (Brazil), and Spanish; verify languages during booking because the undated credential page can change. Microsoft says beta results are delayed and the Practice Assessment is not yet available.<br>
**Transition:** AB-210 replaced the retired MB-280 credential in [Microsoft partner skilling changes](https://learn.microsoft.com/en-us/partner-center/announcements/2026-july). This partner mapping does not make the objectives identical; use the AB-210 course and blueprint for its current scope.<br>
**Official source:** [AB-210 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-210)

## How to use this guide

For every seller workflow, trace:

1. the revenue outcome and current lead-to-cash process;
2. the Dataverse records, ownership, relationships and data-quality requirements;
3. the Sales configuration, license/plan, security and Microsoft 365 integration;
4. the Copilot, predictive feature or agent—and why it is appropriate;
5. the trigger, allowed research/action, handoff, exception and human approval;
6. capacity, credits, monitoring, privacy, responsible-AI and operational evidence;
7. whether Power Automate, Power Apps, Power BI, mobile, calling or SMS closes a measured gap.

Build in a trial or nonproduction environment where licensing permits. Use synthetic contacts and opportunities, not real customer data. Feature names, availability, agent prerequisites, capacity meters and Sales-plan entitlements change quickly; verify them in current first-party documentation and your tenant.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

### Living-guide watch — September 28, 2026

The [current Sales agent roster](https://learn.microsoft.com/en-us/dynamics365/sales/ai-agent-overview) is useful for capability discovery but changes faster than the blueprint. Most importantly, Microsoft's [Sales deprecation ledger](https://learn.microsoft.com/en-us/dynamics365/sales/deprecations-sales) says new Sales Close Agent instances stop September 30, 2026 and existing instances are removed October 30, with Sales Development agent named as the migration path. Retain the Close Agent objectives for exam preparation. For a new implementation, evaluate the replacement and its separate prerequisites below; do not assume an automatic configuration or entitlement transfer.

[Consumption-based billing guidance](https://learn.microsoft.com/en-us/dynamics365/sales/copilot-consumption-based-billing) is explicitly preview and documents prepaid and pay-as-you-go capacity plus service loss when quota is exhausted. Learn the durable capacity and monitoring decision, not current prices or preview UI. For future capability discovery use the [AI at Work roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap), and check the [Power Platform deprecation ledger](https://learn.microsoft.com/en-us/power-platform/important-changes-coming) before reproducing an older lab. The [historical 2026 wave 1 plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/sales/dynamics365-sales/planned-features) labels month-only dates as planned; its September multiple-Qualification-Agent entry is not evidence of deployment in your tenant. Independent courses in Places to learn can provide alternate walkthroughs, but must be mapped back to the current blueprint and these lifecycle sources.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Configure Dynamics 365 Sales core features for AI | 15–20% | Is Sales, its data, security, collaboration and product catalog ready? |
| Optimize AI-driven sales | 20–25% | Can you design and operate Copilot, intelligence, assignments, forecasts and agent capacity? |
| Qualify and prioritize leads by using AI | 15–20% | Can you configure scoring and the Qualification Agent with an appropriate autonomy boundary? |
| Develop deals by using intelligent opportunity research | 25–30% | Can you configure opportunity data, pipeline views and the Opportunity, Close and Research agents? |
| Extend and enhance Sales | 10–15% | Can you select mobile, calling, SMS or Power Platform extensions without duplicating core capability? |

---

## 1. Configure Dynamics 365 Sales core features for AI

### Establish deployment prerequisites

Dynamics 365 Sales is a model-driven app on Dataverse. Confirm tenant/environment strategy, geography, licenses, capacity, base language/currency, security and compliance requirements before enabling features. Identify the intended Sales plan and compare current entitlements; do not assume Sales Professional, Enterprise and Premium expose identical intelligence, forecasting, agent or capacity capabilities.

Use separate development/test/production environments for governed configuration and extensions. Package custom tables, columns, forms, views, business process flows, apps, flows and environment-variable references in solutions. Assign least-privilege roles and test with actual seller/manager personas rather than an administrator account.

The core sales model connects accounts, contacts, leads, opportunities, activities, products, price lists, quotes, orders and invoices. AI output depends on complete, timely and correctly owned records. Define required fields, duplicate handling, lifecycle status, relationship ownership and activity capture before asking an agent to reason over the pipeline.

> **Related item:** A polished AI summary cannot repair ambiguous stages, duplicate accounts, missing activities or incorrect opportunity values. CRM process and data governance are prerequisites for useful intelligence.

### Configure mailboxes and collaboration

Mailboxes and server-side synchronization support email, appointments, contacts and tasks. Approve/test mailboxes, choose synchronization methods and understand who can track which items. Timeline configuration determines which activities and notes sellers see on records; configure useful activity types, filters, sorting and creation behavior without turning the timeline into noise.

Microsoft 365 integration choices include:

- **Outlook:** track and relate communications through Dynamics 365 App for Outlook;
- **Exchange/mailboxes:** synchronize approved server-side data;
- **Teams:** collaborate and, when configured, connect records or calling experiences;
- **SharePoint:** external document management while Dataverse holds record metadata;
- **OneDrive:** personal work files, not a substitute for shared governed documents.

Check sharing, retention, sensitivity, consent and access at each boundary. A seller who can see a generated summary may receive information from activities or files they were already permitted to access; excessive source permissions remain a problem.

### Configure security and seller processes

Dataverse security combines business units, security roles, privileges, record ownership, teams, sharing, hierarchy and optional field security. Decide who can create/read/write/assign/share lead, opportunity and activity data; who administers Sales/AI; and which managers see subordinate pipelines. Agents and flows need identities and permissions appropriate to their operations, not broad administrator access.

Business process flows guide stages and required steps; they do not perform every automation. Align stages with the real process, identify the active table/stage and avoid redundant steps. Use business rules for simple UI/data logic, flows for asynchronous or cross-service automation and code only for requirements that configuration cannot meet.

Import/export options include guided file import, Excel/CSV-based work, dataflows, connectors, APIs and migration/integration tools. Choose based on volume, repeatability, transformation, error handling and reconciliation. Preserve identifiers where needed, validate lookups/options/currencies, detect duplicates and reconcile counts and totals. Exporting customer data also creates a protection and lifecycle obligation.

### Build the product and pricing foundation

Products may be individual items, families that organize related products or bundles sold together. Define units and unit groups, default price lists, properties and lifecycle states. Price lists connect products, unit/currency and pricing; opportunities, quotes, orders and invoices need consistent transaction currency and price context.

Understand the difference between organization pricing data and a seller’s manual override. Configure discount lists and pricing policy deliberately. Test multi-currency scenarios, effective dates, inactive products and what happens when a price list lacks the selected product/unit. Opportunity products improve pipeline value and provide commercial detail for agent-driven close activity; free-text estimated revenue may not provide enough commercial detail.

The [price-list procedure](https://learn.microsoft.com/en-us/dynamics365/sales/create-price-lists-price-list-items-define-pricing-products) requires a price list for each transaction currency and connects product, unit and pricing method. Price-list privileges inherit from Product privileges: granting catalog write access can affect pricing as well. Review the chosen rounding rule and cost basis before publishing.

### Worked example 1: markup and margin are different prices

For a synthetic item costing USD 80, a 25% **markup** gives `80 × 1.25 = 100`. A 25% **margin** gives `80 ÷ (1 − 0.25) = 106.666…`, or USD 106.67 with ordinary two-decimal rounding. At USD 100, the margin is only `(100 − 80) ÷ 100 = 20%`. Confirm the configured pricing method and rounding policy in a test quote. These are arithmetic checks, not an executed Dynamics pricing-engine test; discounts and tax are excluded.

---

## 2. Optimize AI-driven sales

### Design an AI-first sales strategy

Start with seller friction and outcome: response latency, poor prioritization, weak activity capture, inconsistent research, stalled deals, inaccurate forecasts or administrative overhead. Map where Copilot assists a person, predictive models score/prioritize and agents monitor/research/engage. Preserve accountable seller or manager decisions for commitments, sensitive outreach and exceptions.

Design the Dataverse model around required decisions. Use standard tables when they fit; add columns/relationships only with ownership, security, validation, reporting and lifecycle defined. Record provenance and confidence for machine-produced insight where available. Separate raw signals, inferred scores, recommendations and accepted business decisions.

Reporting options include built-in views/charts/dashboards, pipeline and forecast experiences, the research canvas and embedded Power BI. Choose the least complex experience that answers the decision. Operational lists need current actionable records; executive trends may need a governed semantic model. Define refresh, filters, security and metric semantics.

### Prepare Copilot and agents

Verify feature/region/language availability, Sales plan, environment settings, AI Hub configuration, admin roles, data readiness, mailbox/collaboration prerequisites, capacity, billing and credits. The [common setup](https://learn.microsoft.com/en-us/dynamics365/sales/prerequisites-for-all-agents) checks Copilot Studio capacity, cross-region processing terms and AI prompts, followed by AI insight cards and AI Agents settings. A disabled Create control can indicate incomplete prerequisites; do not troubleshoot it as a seller-role problem alone. Document which agent can read, research, update or contact; its user population; business hours; escalation; and shutdown owner.

Capacity and credits are operational constraints. Establish expected volume, meters, budgets, alerts, ownership and graceful degradation. Do not publish fixed prices in a design without checking the current tenant/price sheet. **VERIFY CURRENT:** agents, modes, quotas, billing, licensing and preview/GA status are volatile. The [current licensing guidance](https://www.microsoft.com/licensing/guidance/Dynamics-365) describes Copilot Credits, while the older preview billing article still uses messages. Verify the applicable meter, included capacity, allocation and overage path before budgeting; one processed record is not necessarily one credit. Sales Enterprise’s documented 1,500 scored lead/opportunity records per environment per month is separate from its 1,500 sequence-connected records allowance and agent consumption. Professional and Enterprise/Premium entitlements cannot simply be mixed within one environment.

Copilot features such as record summarization should be evaluated for source coverage, factual accuracy, recency and access. Define how sellers verify important claims and report poor output. Enable capabilities only where the organization has a supported purpose and approved data boundary.

### Configure the Sales accelerator

The Sales accelerator creates a prioritized work experience with segments, sequences and a work list. A segment groups records by defined criteria. A sequence defines recommended or automated sales activities over time. Assignment rules/distribution route records to appropriate sellers or teams.

Design segments around mutually understandable business rules; test overlaps and exclusions. Sequences need exit conditions, timing, ownership, failure behavior and consent/compliance for communications. Work assignment requires capacity/availability and deterministic tie-breaking. Monitor whether prioritization improves response and conversion rather than simply creating more activities.

[Assignment rules](https://learn.microsoft.com/en-us/dynamics365/sales/wa-create-and-activate-assignment-rule) use the first matching rule in list order for records created or updated after activation. An existing backlog is not automatically redistributed merely by adding a rule. Round robin rotates eligible sellers; load balancing considers workload. Team assignment does not distribute to individuals. Check seller availability and capacity separately; an unset work schedule is treated as always available. Assignment is polled, so save-to-assignment delay is expected. The deprecated Outlook availability integration is replaced by the Dynamics CRM calendar.

### Worked example 2: capacity and rule order

A seller has a maximum capacity of 40 and owns 28 active leads plus 12 opportunities. If work-assignment capacity is configured only for leads, available capacity is `40 − 28 = 12`, not zero. A new Seattle lead matches both a broad national rule and a Seattle rule. With the national rule first, that rule wins. Put the narrower rule first when that is the intended business policy, then test unavailable sellers and overdue/unassigned records. Do not assume a capacity failure automatically tries every later rule.

### Configure intelligence and insights

- **Conversational intelligence** analyzes calls and conversations for signals, summaries and coaching insights. Configure recording/consent, data handling, languages, access and manager use.
- **Predictive scoring** estimates lead or opportunity quality from historical data. Confirm data sufficiency, excluded leakage fields, training population and outcome; inspect distribution and business performance.
- **Relationship intelligence** derives engagement/relationship signals from permitted communications and activities. It depends on captured data and should not become an unreviewed employee-performance score.
- **Record summarization/Copilot** condenses permitted record/activity context. Verify material facts against the record.
- **Forecasts** organize a hierarchy, time period, measures and categories; premium predictive insight augments, not replaces, seller/manager judgment.
- **Goals and goal metrics** define the target, measure, owner, period and rollup behavior. Ensure the metric answers the intended question.

Fine-tuning a predictive scoring model means configuring/retraining the supported scoring model with appropriate attributes and data—not fine-tuning a generative language model. Check sample size/quality, retraining, performance and whether scores actually improve prioritized outcomes.

The [Sales deprecation ledger](https://learn.microsoft.com/en-us/dynamics365/sales/deprecations-sales) also changes older learning exercises: relationship intelligence uses Exchange server-side synchronization after native Exchange integration was deprecated; forecasting snapshots/history charts are retired; Copilot document summarization is removed while record summaries remain a separate capability. Replace retired sales-usage reports with governed reporting; Microsoft’s sample Power BI report is a starting point that you maintain. Teams channel record-linking is deprecated, so validate the current browser collaboration experience before reproducing old channel-link demos.

> **Related item:** Prediction and generation require different evaluation. A score needs calibration/discrimination and business lift; a summary needs groundedness, completeness and factual accuracy.

---

## 3. Qualify and prioritize leads by using AI

### Configure the lead-to-opportunity experience

Define how leads enter: manual entry, imports, forms/integration or Customer Insights journeys. Validate consent, source, owner, territory, duplicate rules and minimum data. A lead represents an unqualified prospect; qualification commonly creates or links account/contact/opportunity records according to configuration. Do not create duplicate customer masters simply to satisfy a workflow.

Configure forms, views, business process flows and qualification rules for seller clarity. Decide when an opportunity is created and what evidence constitutes qualification. Track reasons for disqualification. Predictive lead scoring helps order attention; it should not silently exclude protected or strategically important prospects.

The [current qualification experience](https://learn.microsoft.com/en-us/dynamics365/sales/define-lead-qualification-experience) separates automatic and seller-controlled record creation. Up to five opportunities can be created from a lead when seller-controlled opportunity creation and the multiple-opportunity option are enabled. Custom apps also need the Opportunity qualify lead Form component for that side-pane experience. Agent handoff, a seller’s acceptance, CRM qualification and an opportunity win are four different events: report each explicitly.

[Predictive lead scoring](https://learn.microsoft.com/en-us/dynamics365/sales/configure-predictive-lead-scoring) needs at least 40 qualified and 40 disqualified leads created **and closed** within the chosen three-month-to-two-year training period. If a business process flow is selected, abandoned instances do not count. Allow for the documented approximate four-hour data synchronization delay. The model scores eligible open leads; it is not a new generative model. Evaluate attributes, outcome labels and the performance report before publishing; periodic retraining is separate from record scoring. [Usage monitoring](https://learn.microsoft.com/en-us/dynamics365/sales/digital-selling-scoring) refreshes daily.

### Worked example 3: enough records is not enough eligible records

Your selected training window contains 44 qualified and 43 disqualified leads. Five qualified leads abandoned the selected process, leaving `44 − 5 = 39` eligible qualified outcomes. The minimum is missed by one, even though the raw total is 87. Expand a legitimate training window or collect more representative outcomes; do not relabel a lost prospect just to enable training. Meeting 40/40 is an eligibility check, not evidence that the model is useful or fair.

### Choose the Sales Qualification Agent mode

The blueprint distinguishes:

- **Research-only:** the agent researches and evaluates leads, drafts outreach and hands results to sellers; it does not autonomously send engagement emails. Choose it when outreach must remain human-controlled, risk is higher, consent is uncertain or the organization is learning.
- **Research and engage:** the agent can research and communicate according to configured rules before handing off qualified prospects. Choose only when data, approved messaging, consent, guardrails, monitoring and escalation support autonomous engagement.

Configure target customer profile/criteria, included leads, data/research sources, engagement settings, handoff and ownership. Establish approved sender identity, contact policy, stop/opt-out, rate and quiet-hour rules. Test normal, edge, hostile and ambiguous inputs with controlled records. For public-web research, use real public company context or Microsoft’s documented sample company and **test inboxes you control**; an invented company with no public information cannot validate web-research quality.

Interpret actions through evidence: what the agent researched, how it assessed fit, whether/when it engaged and why it handed off or stopped. A recommendation is not ground truth. Monitor volume, research success, engagement, handoff, conversion, opt-out/complaints, failures, latency, consumption and subgroup outcomes. Calibrate or stop when results violate thresholds.

The [setup procedure](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sales-qualification-agent) requires an Entra app, a Dataverse application user with the documented AISalesPerson role, allowed connectors and appropriate seller permissions. Engage adds a shared mailbox and server-side synchronization. Even research-only email drafting needs synchronization. The current procedure allows upgrading research-only to engage, not downgrading it. **Stop prevents new intake; in-flight leads can continue to handoff or supervisor review.** Include pending runs, sender identity and escalation in the shutdown plan; the stop button alone does not prove all outbound work has ceased.

[Handoff criteria](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sales-qualification-agent-handoff-criteria) distinguish target-customer fit from BANT: budget, authority, need and timeline. The agent evaluates need and timeline before budget and authority. When both purchase interest and BANT are selected, both must pass; with BANT omitted, purchase-interest signals drive that assessment. Custom criteria can use supported fields or public URLs, but nested relationships are unsupported. Update criteria before deleting referenced custom fields.

### Worked example 4: handoff measures depend on mode

In a synthetic engage-mode cohort of 50 completed assessments, 32 meet purchase-interest criteria, 28 meet BANT criteria, and 22 meet both. With both criteria enabled and no exception cases, **22** meet the configured handoff gate: `22 ÷ 50 = 44%`. Adding 32 and 28 double-counts overlap and incorrectly includes partial matches. Now consider ten research-only leads: Microsoft’s [test procedure](https://learn.microsoft.com/en-us/dynamics365/sales/test-sales-qualification-agent-research-engage) says they hand off after research/drafting regardless of fit. Ten handoffs therefore do not prove ten qualified prospects. Track selection, research completion, fit, handoff acceptance and eventual opportunity outcomes separately. Include excluded leads, opt-outs, unanswered questions and wrong-recipient checks in the pilot.

> **Related item:** Autonomous outreach combines AI risk with communications law, brand and customer-experience risk. Technical permission to send is not the same as organizational authority or recipient consent.

---

## 4. Develop deals by using intelligent opportunity research

### Optimize opportunity management

An opportunity should have customer, owner, stage/status, estimated close date, probability/category, currency, price list and products/revenue suitable for the process. Configure the pipeline view to show actionable stages, values, dates and signals; define edits, grouping and access. Stale dates and inflated values degrade forecasts and agent decisions.

Opportunity products connect commercial scope and pricing. Test unit, quantity, discount, currency, write-in product and recalculation behavior. Quotes formalize proposed terms; orders and invoices represent later lead-to-cash states. Agents may support work but should not bypass pricing approval, credit, legal or fulfillment controls.

### Distinguish opportunity agents

| Agent | Primary role | Human/operational boundary |
|---|---|---|
| Sales Opportunity Agent | Monitors/researches opportunities and surfaces risk or needed attention | Seller validates insight and chooses action |
| Sales Close Agent | Retiring preview for autonomous engagement and low-complexity deal closure | Study historical setup and escalation; assess the separate Sales Development replacement before any deployment |
| Sales Research Agent | Answers/analyzes sales questions and performance in a research canvas | Users verify definitions, filters, source data and inference |

Configure the Sales Opportunity Agent’s eligible pipeline, signals and ownership. Determine how its insights appear and how sellers respond. Monitor false/low-value alerts, coverage and effect on deal progression. The [Opportunity Agent overview](https://learn.microsoft.com/en-us/dynamics365/sales/sales-opportunity-agent) identifies an initial pass over all matching open opportunities before subsequent refreshes. A broad initial scope can consume substantial capacity.

The [current setup](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sales-opportunity-agent) supports up to ten active instances, each with a distinct scope; they share capacity and a single Copilot Studio knowledge base. Predictive opportunity scoring is enabled automatically when needed by the agent, so include scoring readiness in the pilot. Do not apply an older Close Agent page’s generic one-instance wording to current Opportunity Agent configuration.

[Knowledge-source configuration](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sqa-knowledge-source) separates research, outreach and reply sources. Qualification and Opportunity agents share account-research sources: removing one can affect both. For linked document knowledge, use the supported SharePoint option; a connector labelled SharePoint or OneDrive does not establish that OneDrive is supported here. Opportunity instances can filter sources with `agentProfileId`; check General versus Conditional usage before publishing.

> **Unresolved official-source conflict:** The same knowledge article’s custom-field research section says Opportunity Agent does not support custom fields and immediately instructs readers to add them. Keep that capability unverified for a required design until Microsoft clarifies it and a controlled tenant check confirms it. This does not negate separately documented Qualification Agent custom handoff criteria.

### Worked example 5: scope and refresh affect capacity

Assume **hypothetical measured** consumption of 12 credits per initial opportunity and 3 per refresh. An initial scope of 180 opportunities costs `180 × 12 = 2,160`; refreshing 60 opportunities four times adds `60 × 4 × 3 = 720`, for **2,880**. With 3,000 allocated and a 500-credit reserve, the usable budget is 2,500: the plan exceeds it by 380. Another agent consuming 250 raises combined usage to 3,130, exceeding total allocation by 130. Reduce scope/frequency or arrange capacity before expansion. These are sample assumptions, not Microsoft rates or a prediction of billing behavior.

Configure the Sales Close Agent only after opportunity products/pricing, contact data, mailbox, policies and handoff are ready. Understand its actions rather than treating activity as success. Collaborating with the agent means reviewing status, accepting/correcting direction, handling exceptions and preserving accountable approval for commitments.

For the retiring product, learn the [manual setup](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sales-close-agent) sequence: identity/mailbox, product details, target records, email delivery/content, knowledge, simulation, then activation. Its AI-assisted setup instructions are stale: the deprecation ledger removes that assistant after June 2026. The [processing description](https://learn.microsoft.com/en-us/dynamics365/sales/how-sales-close-agent-engage-mode-works) distinguishes an active/pending run, failure and completed engagement; a completed run is not independent proof of booked revenue. Inspect the record timeline and seller-escalation view. Follow-up behavior can close nonresponding deals as lost, so review it before authorizing a cohort. [Configuration edits](https://learn.microsoft.com/en-us/dynamics365/sales/manage-sales-close-agent) affect new processing and do not replay previously processed records.

> **Unresolved Close Agent shutdown conflict:** Its setup page says deactivation allows in-flight records to continue, while its management page says records in process will not be processed after stopping. Do not treat either outcome as proven containment. Validate pending runs and actual outbound behavior in a controlled environment before relying on a shutdown procedure; Qualification Agent's separate documented behavior does not resolve this discrepancy.

The [Close Agent retirement notice](https://learn.microsoft.com/en-us/dynamics365/sales/sales-close-agent) directs customers to create a Sales Development agent. Its [activation procedure](https://learn.microsoft.com/en-us/dynamics365/sales/sales-dev-agent/activate-agent) is currently a separate **preview** involving Microsoft 365/Copilot/Teams licensing, Frontier access, Agent 365 enablement, policy templates and a dedicated agent identity. It explicitly cautions against production use of the preview. Plan a supported continuity path for existing deals and evaluate the replacement in an appropriate pilot; a migration recommendation does not establish production readiness, feature parity or automatic data/configuration transfer.

Use the Sales Research Agent for supported natural-language analysis of sales data. Configure access and relevant data, then use the research canvas to explore pipeline/performance. State time period, hierarchy, currency, status and metric definition. Confirm totals against governed views/reports; a fluent narrative can still reflect incomplete records or an ambiguous question. The [Research Agent overview](https://learn.microsoft.com/en-us/dynamics365/sales/sales-research-agent) describes Show work, connected Dataverse/Fabric sources and supported uploaded files. [Access setup](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sales-research-agent) requires the Sales Research Agent Reader role for ordinary users, a Sales license and capacity. Bing search follows the tenant consent setting; disabling it preserves internal-source use.

### Worked example 6: reconcile currency before accepting a chart

The [Research Agent FAQ](https://learn.microsoft.com/en-us/dynamics365/sales/faqs-sales-research-agent) says connected Dynamics data uses the environment base currency, while uploaded/Fabric data can require currency context. Suppose an uploaded file contains USD 900 and EUR 800. Adding them as “1,700 dollars” is invalid. With an explicitly supplied **hypothetical** rate of USD 1.10 per EUR, the normalized total is `900 + 800 × 1.10 = USD 1,780`. Record rate date, conversion direction, source rows and reporting period, then reconcile Show work to the governed calculation. This example does not assert a live exchange rate or the platform’s transaction-rate calculation.

### Govern agent operations

For every agent define:

- business owner, technical owner and incident contact;
- eligible records/users and least-privilege access;
- data sources, outbound channels and prohibited actions;
- human handoff, approval and override;
- identity, audit, retention and monitoring;
- capacity/credit budget and anomaly alert;
- quality, conversion, safety and experience thresholds;
- version/change approval and rollback/disable procedure.

Evaluate with representative examples before broad use. Monitor not only uptime but correct research, groundedness, appropriate action, timely handoff, customer complaints, bias, security events and business lift. Preserve evidence for why an action occurred when the process requires audit.

---

## 5. Extend and enhance Sales

### Select supporting apps and channels

The Sales mobile app supports work away from a desktop. Configure the intended app, forms/views, quick create, offline behavior where supported, notifications and mobile security. Test device management, authentication, data loss and low-connectivity use.

Teams calling connects seller communications with Sales workflows when tenant, phone system and licensing prerequisites are met. Define recording/transcription, consent, number assignment, storage and access. SMS requires a supported provider/channel, sender numbers, custom-form exposure where needed, consent/opt-out, regional requirements and conversation ownership.

**VERIFY CURRENT:** mobile features, Teams calling integration and SMS providers/prerequisites vary by tenant, region, channel and release wave.

The [Sales mobile overview](https://learn.microsoft.com/en-us/dynamics365/sales/sales-mobile/dynamics-365-sales-mobile-app) excludes China, sovereign/government clouds and on-premises customer engagement. [Mobile prerequisites](https://learn.microsoft.com/en-us/dynamics365/sales/sales-mobile/prereq-sales-mobile) include Organization/Mailbox read access and the mobile privilege. An offline profile or tablet can switch the interface to Unified Interface; test that experience rather than promising identical online/offline screens.

Use the [Teams dialer configuration](https://learn.microsoft.com/en-us/dynamics365/sales/sales-hub-dialer-configure-cif), with Teams/Phone licensing, PSTN connectivity and assigned numbers. Enabling it stops other Channel Integration Framework telephony for the affected users. It supports selected model-driven apps, not canvas apps or custom entities; selected security roles must be associated with the root business unit. The removed **Sales Hub Dialer preview** is a different feature.

[SMS provider setup](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sms-provider) separates provider credentials, incoming callback, delivery-report callback and number ownership. A sent message alone does not verify incoming replies or delivery receipts. Use a number unique to Sales, rather than reusing a number configured for another Dynamics app, and explicitly assign the allowed users/teams. Test opt-out and replies through the supported provider with controlled recipients; country/provider support and consent requirements must be verified for the deployment.

### Extend with Power Platform

- **Power Automate:** orchestrate approvals, notifications and cross-service work. Choose triggers carefully, prevent loops/duplicates, use connection references, retry/error handling and least-privilege identities.
- **Power Apps:** embed a canvas component, custom page or supported control when the standard model-driven experience lacks a focused interaction. Preserve responsive/accessibility and Dataverse security.
- **Power BI:** embed contextual analytics when a governed model and richer visualization are required. Configure row-level security and verify context/filter propagation.

Use native Sales configuration before extension when it meets the need. Extensions introduce dependencies, ALM, support, performance and security obligations. Keep calculations and approvals deterministic when the outcome must be exact; use AI for assistance where uncertainty is accepted and reviewed.

> **Related item:** Copilot Studio can extend Dynamics 365 with custom agents, but AB-210 explicitly tests embedded Power Apps components/controls, flows and Power BI. Do not replace those objective-level distinctions with a generic “build an agent” answer.

---

## Useful blog readings

- [Julie Strauss — Sales Qualification benchmark](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2025/12/11/dynamics-365-sets-the-bar-for-agentic-sales-qualification-on-new-benchmark/) (December 11, 2025; public article, about seven minutes). Use its research/outreach/engagement separation to design a scored test set with source accuracy, recipient correctness and handoff timing. Treat vendor benchmark results as dated experimental claims, not promised conversion lift. Its research-only qualification description is superseded by the current test procedure’s handoff-regardless-of-fit behavior. The linked technical benchmark was not independently reproduced.
- [Paramita Chatterjee — agent-assisted data entry and exploration](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/01/28/agentic-ai-transforming-dynamics-365-sales/) (January 28, 2026; public article, about five minutes). Compare a pasted lead email, suggested fields and a filtered operational view. Review citations and corrections before accepting values; reconcile any chart against its filters. The article illustrates an older UI and preview labels. Current [form-fill guidance](https://learn.microsoft.com/en-us/power-apps/user/form-filling-assistance) moves controls toward Copilot settings and app settings; it excludes secured columns and sensitivity-labelled input files. Do not remove protection to make a demo work. Preview status differs by product and entry point.

Neither article is an exam blueprint or a substitute for configuration evidence. Videos, linked paid materials and tenant demonstrations were not executed in this review.

## Integrated scenarios

### Scenario 1: high-volume inbound qualification

A seller team receives thousands of leads. Clean source/consent/ownership data, define target-customer and qualification criteria, configure predictive scoring and begin with Qualification Agent research-only mode. Monitor accuracy, handoff and subgroup outcomes. Move selected low-risk segments to research-and-engage only after approved messaging, opt-out, mailboxes, capacity, escalation and seller ownership are proven.

### Scenario 2: stalled enterprise opportunities

Require opportunity close dates, products, pricing and recent activities. Configure the pipeline view and Opportunity Agent to surface risk. Study Close Agent follow-up as a retiring blueprint capability; evaluate a supported transition for actual workloads. Pricing or term changes still require accountable approval. Sales Research Agent answers pipeline questions, forecasts organize manager judgment and goals track defined metrics. Compare progression/conversion and customer complaints with the baseline.

### Scenario 3: governed mobile seller extension

Field sellers need mobile updates, Teams calls, quote approval and regional analytics. Configure mobile forms/security, approved calling/recording and a Power Automate approval with idempotency and escalation. Embed Power BI with row-level security. Avoid SMS until the provider, consent and country rules are approved. Package customizations in solutions and test as seller and manager personas.

---

## Hands-on labs

1. **Core environment:** In a nonproduction tenant, document plan/license, environment, roles, mailboxes, timeline, collaboration and a deployment readiness checklist.
2. **Lead-to-cash model:** Create synthetic accounts, contacts, leads and opportunities; configure a business process flow and trace qualification without duplicates.
3. **Catalog and pricing:** Build a family, products, units, multi-currency price lists and opportunity products. Test missing prices, discounts and manual override.
4. **Sales accelerator/intelligence:** Design segments, a sequence and assignment rules; define tests for scoring, relationship insight, conversation data and summaries.
5. **Lead-agent plan:** Compare both modes with included/excluded leads, public company context and controlled test inboxes. Specify credentials, criteria, handoff, opt-out, monitoring and in-flight shutdown checks. Start with a tabletop record when no licensed tenant is available.
6. **Opportunity-agent plan:** Design Opportunity and Research Agent scope, identities, knowledge, budget and evidence. Treat Close Agent as a retiring-product tabletop: map configuration, escalation and continuity to replacement prerequisites without creating a new retiring instance.
7. **Forecast and goals:** Define hierarchy, period, measure, categories, goal metric, dashboards and reconciliation against source opportunities.
8. **Extension:** Design a flow, embedded Power Apps interaction and contextual Power BI report; add mobile/calling/SMS prerequisites and an ALM/security test plan.

9. **Assignment and scoring:** Reproduce examples 2–3 offline, then in a permitted test environment inspect rule order, backlog behavior, seller schedules, excluded training records and delayed data arrival. Record actual eligibility rather than changing labels to meet a minimum.
10. **Evaluation and transition:** Create the blog-derived assessment rubric, compare research-only handoffs with engage-mode gates, reconcile capacity/currency examples, and prepare a September/October Close Agent continuity plan. Keep the Opportunity custom-field contradiction as an unresolved acceptance item.

**Execution record:** This review checked the six synthetic examples and resource arithmetic offline. It did not configure a tenant, send email/SMS, place calls, train a model, run an agent or execute the ten infrastructure labs.

## Knowledge checks

1. Which Dataverse records form the core lead-to-cash chain?
2. Why are process and data quality prerequisites for sales AI?
3. What should be verified before choosing a Dynamics 365 Sales plan?
4. What does a mailbox/server-side synchronization enable?
5. When should SharePoint rather than OneDrive hold record-related documents?
6. How do roles, ownership, teams and sharing combine in the Sales security model?
7. When does a business process flow fit better than a cloud flow?
8. Which controls make a repeatable data import trustworthy?
9. Distinguish products, families and bundles.
10. How do unit, price list and currency affect an opportunity product?
11. What makes a sales workflow “AI-first” without making it AI-only?
12. Which fields and relationships should an AI-ready Sales data model preserve?
13. When do built-in views differ from an embedded Power BI report?
14. Which agent prerequisites should be checked before enablement?
15. Why must capacity, credits and billing be monitored operationally?
16. Distinguish a segment, sequence and assignment rule.
17. Which consent and governance issues accompany conversational intelligence?
18. How should predictive scoring be evaluated?
19. What does relationship intelligence infer, and what caveat applies?
20. How do forecasts differ from goals?
21. What does fine-tuning predictive scoring mean in this context?
22. What should happen during lead qualification?
23. When is Qualification Agent research-only mode appropriate?
24. What additional controls are required for research-and-engage mode?
25. Which evidence helps interpret and monitor Qualification Agent actions?
26. Why can a high lead-engagement volume still be a poor result?
27. Which opportunity fields support useful pipeline intelligence?
28. What is the Sales Opportunity Agent’s primary role?
29. What is the Sales Close Agent’s primary role and boundary?
30. What is the Sales Research Agent/research canvas used for?
31. Why must natural-language sales analysis state period, hierarchy and currency?
32. Which measures belong in an agent operational scorecard?
33. What must be configured for secure mobile access?
34. Which prerequisites and obligations accompany Teams calling and SMS?
35. When should a Power Automate flow, embedded Power App or Power BI report be used?
36. Which evidence justifies expanding an agent from pilot to broader use?
37. Why is 25% margin different from 25% markup?
38. Does a new assignment rule redistribute every existing lead immediately?
39. Why can 44 qualified and 43 disqualified leads still fail model eligibility?
40. Does stopping Qualification Agent cancel every in-flight lead?
41. Does a research-only handoff prove the lead fits the target profile?
42. Why must Opportunity Agent initial scope and shared knowledge be reviewed?
43. Is the Close-to-Development transition an automatic production-ready migration?
44. How should mixed-currency uploaded research data be reconciled?

### Answer checkpoints

1. Leads qualify into linked account/contact/opportunity records; products, quotes, orders, invoices and activities carry the commercial process onward.
2. AI depends on reliable ownership, stages, outcome labels, relationships and timely source data; fluent output cannot repair a broken process.
3. Compare app rights, features, region, capacity, environment compatibility and current licensing, then verify the actual tenant.
4. Approved and tested server-side synchronization connects supported email/calendar data; agent sender identities need their own setup.
5. Use governed shared document libraries for record collaboration; personal file storage and Dataverse record access are different boundaries.
6. Check table privilege, access depth, ownership, team membership, sharing and secured columns using real user personas.
7. A business process flow guides stages; a cloud flow performs asynchronous or cross-service actions. Neither substitutes for security.
8. Stable identifiers, validated mappings/lookups, duplicate handling, error logs and reconciled counts/totals support repeatable imports.
9. Families organize shared product structure; products are sellable items; bundles combine items into an offer.
10. A price-list item combines product and unit in a price-list currency with a pricing method; validate discount and rounding behavior.
11. Start from business outcomes, assign AI an appropriate assist/action role, and preserve accountable decisions and exceptions.
12. Retain customer/product relationships, provenance, stage/outcome definitions, ownership and access controls.
13. Views support operational action on current records; Power BI supports a governed analytic model and its own refresh/security design.
14. Check common AI Hub requirements, agent-specific identity and permissions, allowed connectors, mailbox, region and capacity.
15. Shared consumption and refresh volume can exhaust allocation; budget and fallback decisions must precede rollout.
16. A segment selects records, a sequence guides timed activity, and assignment rules route ownership.
17. Recording/transcription consent, access, retention and appropriate coaching use accompany conversation analysis.
18. Verify eligible labelled history and selected attributes, then inspect performance and business outcomes on representative data.
19. Relationship signals reflect captured communications and activity; missing or biased capture can distort them.
20. Forecasts estimate period outcomes across hierarchy/categories; goals define targets, metrics and rollups.
21. Configure/retrain the supported predictive model; this is distinct from generative language-model fine-tuning.
22. Apply the chosen creation/linking policy, review duplicates and distinguish qualification from agent handoff.
23. Use research-only for seller-controlled engagement; research and draft generation still need supported setup.
24. Engage adds sender/mailbox, criteria, outbound permissions, consent, monitoring and a tested handoff/containment procedure.
25. Inspect selected inputs, sources, run status, drafts/replies, fit assessment, handoff reasons and seller outcomes.
26. Volume can conceal unwanted outreach, incorrect recipients, low acceptance and poor conversion; measure outcomes and complaints.
27. Keep customer, owner, stage, close date, currency, products/prices and activity current and consistent.
28. Opportunity Agent researches and prioritizes deals and surfaces risks; it does not share Qualification Agent’s outreach role.
29. The retiring Close Agent handles low-complexity engagement and closure with escalation; preserve control over commitments and migration.
30. Research Agent supports natural-language analysis and iterative research with inspected sources, visuals and Show work.
31. Those definitions determine which rows and values are being compared; ambiguous context can make a plausible result wrong.
32. Track correctness, coverage, acceptance, latency, usage, exceptions, complaints and downstream conversion with explicit denominators.
33. Verify supported cloud/device, app permissions, synchronization, protection and the actual offline/tablet experience.
34. Calling needs Teams/Phone/PSTN/number setup; SMS needs a supported provider, assigned number, callbacks and recipient controls.
35. Use a flow for orchestration, an embedded app for focused interaction, and Power BI for analytics; test each identity and data boundary.
36. Representative test results, accepted quality thresholds, monitored usage, recovery evidence and accountable owner approval justify expansion.
37. Markup divides profit by cost; margin divides it by selling price. For cost 80, the example yields 100 versus approximately 106.67.
38. No. The documented rule applies to records created or updated after activation and is processed on a polling cycle.
39. Filtered-out or abandoned-process records do not count; the example leaves only 39 eligible qualified outcomes.
40. No. New intake stops, but existing orchestrations can continue; examine pending work and the outbound path.
41. No. The documented research-only workflow hands off after research/drafting regardless of fit.
42. Initial processing spans the configured scope; instances share capacity/knowledge, and shared source edits can affect another agent.
43. No. Existing Close instances are removed October 30; Development activation has separate preview, identity, licensing and Frontier requirements.
44. State currency context and rate/date explicitly, inspect source rows and Show work, and compare against a governed calculation.

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, configure a synthetic lead-to-cash environment, and add resources only for measured gaps.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official AB-210 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-210) | Free | 1–2 hours to map objectives |
| [Configure Sales for AI-powered selling](https://learn.microsoft.com/en-us/training/paths/configure-sales-ai-selling/) | Free | 3 modules; allow 5–8 hours with configuration |
| [Generate and qualify leads using AI](https://learn.microsoft.com/en-us/training/paths/generate-qualify-leads-ai-sales/) | Free | 3 modules; allow 4–7 hours with practice |
| [Win deals with AI-powered sales execution](https://learn.microsoft.com/en-us/training/paths/win-deals-ai-sales/) | Free | 4 modules; allow 6–10 hours with practice |
| [Extend Sales with AI and Power Platform](https://learn.microsoft.com/en-us/training/paths/extend-d365-sales-ai-platforms/) | Free | 3 modules; allow 6–10 hours with a build |
| [AB-210T00-A course](https://learn.microsoft.com/en-us/training/courses/ab-210t00) | Paid/provider-dependent | 3 days |
| [Dynamics 365 Sales documentation](https://learn.microsoft.com/en-us/dynamics365/sales/) | Free | 6–15 hours selected configuration and troubleshooting |
| [Udemy AB-210 by Graeme Gordon](https://www.udemy.com/course/microsoft-dynamics-365-sales-ai-consultant-exam-preparation/) | Paid; price varies | Previously listed around 4 hours; page access-blocked September 28 |
| [Udemy AB-210 by Hamdy Khaled](https://www.udemy.com/course/ab-210-dynamics-365-sales-ai-consultant-2026/) | Paid; price varies | Previously listed 4 hours 54 minutes; page access-blocked September 28 |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Verify current session start/end time after sign-in |

The four official paths previously listed **12 hours 3 minutes** in total; their currently fetched path pages expose 13 modules (3 + 3 + 4 + 3) without those durations, so treat that time as historical. Allow roughly **30–50 hours** with tenant configuration and labs; this is a planning estimate, not an executed-study measurement. The three-day course currently lists seven languages. Both Udemy pages were access-blocked, so current runtime, content quality and assessment originality were not reverified; retain them as candidates to evaluate before purchase. Microsoft says the Practice Assessment is not currently available for this beta exam. No exact current AB-210 path from Pluralsight, O'Reilly, MeasureUp or Whizlabs was independently verified in the September 28 search. The Partner Skilling Hub returned a login shell, not a verified current AB-210 session. Several marketplaces advertise hundreds or thousands of questions or “valid” material; those were deliberately excluded. Reject recalled live questions, pass guarantees and unsupported banks.

## Final readiness checklist

- [ ] I can trace a clean, secured lead-to-cash data and process model.
- [ ] I can configure mailboxes, timelines, roles, Microsoft 365 collaboration and product pricing.
- [ ] I distinguish Copilot, predictive intelligence and each Sales agent.
- [ ] I can design Sales accelerator segments, sequences and assignment rules.
- [ ] I can configure and evaluate scoring, conversational/relationship intelligence, forecasts and goals.
- [ ] I can defend Qualification Agent research-only versus research-and-engage mode.
- [ ] I can explain Opportunity, Close and Research Agent configuration, action evidence and monitoring.
- [ ] I can select mobile, Teams calling, SMS and Power Platform extension patterns.
- [ ] I verify beta status, license/plan, feature availability, capacity, credits and billing immediately before use.
- [ ] I reconcile agent handoffs, CRM qualification, completed runs and booked revenue as separate outcomes.
- [ ] I can explain the Close Agent retirement and the unresolved Opportunity custom-field support boundary.
- [ ] I use original practice and source review without seeking live exam content.
