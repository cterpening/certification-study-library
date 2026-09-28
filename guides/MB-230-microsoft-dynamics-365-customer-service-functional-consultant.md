---
exam_code: MB-230
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# MB-230 Microsoft Dynamics 365 Customer Service Functional Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the March 11, 2026 official objective baseline and cited public sources on September 28, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mb-230-coverage-record). The [official MB-230 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230) is authoritative.

**Current baseline:** Skills measured as of March 11, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Metadata discrepancy:** The credential page still shows October 3, 2025 and future-tense March 11, 2026 text. The study guide presents the March 11 objective set with no later announcement. All 50 detailed objectives retain the same meaning; this review restores two paraphrased bullets and the complete source wording in the repository snapshot.<br>
**Lifecycle:** The [Dynamics 365 Customer Service Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-customer-service-v3/) is active. The exam is 100 minutes, available in seven languages, lists no retirement date, and links a free Practice Assessment. Renewal is every 12 months; the direct practice endpoint returned no substantive text in this review.<br>
**Official source:** [MB-230 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230)

## How to use this guide

For each requirement, trace one complete service transaction:

1. intake channel, customer identity, consent and case-creation trigger;
2. case, related records, timeline, ownership, security and resolution state;
3. knowledge, collaboration, Copilot or agent assistance and human verification;
4. SLA/KPI clock, business calendar, pause/applicability rules and actions;
5. workstream, classification, queue, assignment, capacity and fallback;
6. representative workspace, session, tabs, script, macro and notification;
7. survey trigger, personalization, response correlation and improvement evidence.

Build in a nonproduction environment with synthetic customers. Use solutions for configuration and record dependencies, security roles and connections. Product labels, Copilot/agent behavior, licensing and admin-center experiences change quickly; verify current documentation and tenant availability.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Manage cases in Customer Service | 51–55% | Can you configure a secure case-to-resolution system with knowledge, collaboration, Copilot/agents and enforceable SLAs? |
| Configure representative experience and routing | 25–30% | Can you send each item to an eligible representative and provide the right multi-session tools and context? |
| Extend Customer Service | 15–20% | Can you adapt Dataverse/UI behavior and connect useful, governed feedback to the service lifecycle? |

---

## 1. Manage cases in Customer Service

### Model the case lifecycle

A **case** is the durable service record: customer/account, origin, subject, priority, owner, activities, related cases, entitlement/SLA and resolution. Start with a state model—new, active, waiting, resolved, canceled and any justified status reasons—then define who may transition it and what evidence resolution requires. Parent/child cases coordinate related work; merging removes duplicates. Neither should erase distinct obligations, customers or audit evidence.

Automatic record creation and update rules convert supported incoming activities into records or update existing records. A robust rule defines monitored queue/mailbox, source activity, conditions and ordering, record to create, field mapping, duplicate/correlation behavior, Power Automate steps, failure owner and activity-monitor review. Test malformed sender data, duplicate messages, missing customer matches, inactive rules, connection failures and partial flow completion.

The resolution experience controls the information collected when a case closes. Require resolution type, billable/nonbillable time, description and any business-specific evidence without creating unusable forms. Reopening should preserve history and deliberately address SLA behavior, ownership and follow-up.

Use [modern automatic record creation](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/automatically-create-update-records). Email rules must be linked to a queue and activated; saving leaves the rule in draft. A queue cannot simultaneously belong to single-queue and multiple-queue tracking rules, and changing between those scopes requires a new rule. Modern ARC is not supported on-premises. Record creation and routing are separate steps: a created case is not proof it reached an eligible representative.

### Secure records and shape the timeline

Use security roles for table privileges and record access, teams/business units or sharing for scope, and field security where individual columns need protection. Separate representatives, managers, knowledge authors/publishers and administrators. Test each persona against customer, case, knowledge, survey and AI-generated data; a hidden form control is not authorization.

The timeline aggregates activities, notes and related records. Configure record types, sort/filter behavior, card forms, highlights and commands around representative decisions. Avoid overcrowding it with low-value events. Ensure important content remains accessible, correctly secured and useful in mobile/narrow layouts.

> **Related item:** A queue owns or organizes work; a security role authorizes actions; a timeline presents history. Moving a case to a queue does not grant the recipient permission to read it.

### Govern knowledge from authoring to use

Define knowledge settings, article templates, categories, lifecycle states, versioning, review/approval, expiration and ownership. Configure knowledge-enabled tables and internal search so context, language, status and audience produce useful results. Translated articles are distinct governed variants: relate them, assign language-specific reviewers and manage staleness rather than assuming automatic equivalence.

External/integrated knowledge sources need a connector/search contract: source owner, authentication, indexed scope, permissions, refresh latency, ranking/filtering, citation and outage behavior. A representative must be able to distinguish an approved internal article from an external result.

Use current Copilot and knowledge-agent capabilities for drafting and discovery; do not design a new solution around the retired smart-assist case/article suggestions or the older AI keyword/description feature. Define approved source context, prohibited data, review/publish authority, evaluation set, citation expectations and rollback. Generated text remains a draft until a responsible owner verifies accuracy, policy, language and audience.

#### Search relevance and access are separate

The [knowledge setup guidance](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-knowledge-management-embedded-knowledge-search) identifies the environment as the `KnowledgeArticle` security boundary and directs administrators to table privileges. Draft/internal labels and a hidden result are not a substitute for authorization. Keep secrets and restricted personal data out of article content; test access through the actual surfaces used.

[Knowledge-search filters](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/enable-knowledge-article-search-filters) and [Copilot response filters](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/use-copilot-filters) are different configurations. Copilot can combine representative-selected and automated record-context filters; saved selections can affect later requests. Validate null/missing tags, context changes and filter visibility. [Copilot setup](https://learn.microsoft.com/en-us/dynamics365/customer-service/copilot-enable-help-pane) defines supported fields, sources and feature combinations; a provider available in ordinary search is not automatically a Copilot grounding source.

[External providers](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-search-providers) federate results, with source-content access still required. [Integrated providers](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/add-search-provider) ingest website articles into Dataverse on a refresh schedule. Their sitemap-based ingestion requires static content, suitable XML and `lastmod`; script-loaded pages are not supported. Decide whether content is referenced or copied, how fresh it is and how each copy is governed.

[Customer Knowledge Management Agent](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/admin-km-agent) can harvest resolved cases or closed conversations. Set up its connection references, flows, agent publication and consumption billing, then constrain eligible records and input attributes. A generated article still needs a deliberate review/publish policy; removing customer-specific material is part of that policy.

### Configure Teams collaboration

Embedded Teams chat preserves case context while representatives consult specialists. Configure linking, record sharing, permissions, retention and external-participant boundaries. Suggested contacts can be rule-based or AI-assisted; validate why a person is surfaced and provide manual search when suggestions fail. “Join a Teams call” lets selected users bring a customer into a supported call flow; confirm identity, consent and what case data participants can see.

The collaboration experience should answer: who may start/link chats, which records are shared, how a conversation is retained/discovered, what happens when users lack Dynamics access, and how the decision returns to the case. Teams is a collaboration channel, not the system of record for case disposition.

For [Join a Teams call](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-join-a-teams-call), check the environment collaboration setting, representative Teams access, productivity pane and outbound email where invitations use email. Enable custom experience profiles deliberately. Customers do not need a Teams license. The [runtime guide](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/join-a-teams-call) says joining the meeting does **not** end the existing voice call automatically; the representative must end it. A meeting recording is stored in Microsoft 365 rather than Dataverse. Plan those as separate communication and retention paths.

### Configure Copilot and service agents

**Ask a Question** searches configured knowledge; filters should restrict sources by status, language, audience or other supported metadata. Case, timeline and conversation summaries reduce reading time but need a clear source boundary and representative verification. **Draft a Response** should use approved case/conversation/knowledge context; a fluent response is not proof of correctness.

The Case Management Agent can perform supported case lifecycle work. Define enabled operations, scope, trigger, identity, permissions, human checkpoints, exception/stop rules, audit and success measures. Integrating another agent adds knowledge sources and plug-ins/tools; each tool requires typed inputs/outputs, least privilege, validation, timeout/retry, idempotency, logging and explicit confirmation for material actions. Treat customer content as untrusted: it must never grant tool or data access.

Measure correct resolution, representative correction/acceptance, escalation, latency, unauthorized attempts and downstream errors—not just AI usage. Provide a deterministic manual path when an agent or grounding source is unavailable.

> **Related item:** A Copilot answer assists a human inside a workflow; an agent may select or execute actions. Increased autonomy increases the need for scoped identity, action controls, evaluation and recoverability.

#### Configure an automation level, then verify the action path

[Case resolution setup](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-case-resolution-agent) distinguishes Full, Require agent confirmation, Shadow mode and Disabled by line of business. Fully autonomous processing needs its application user/shared mailbox configuration, along with the documented intent, setup and billing prerequisites. Inbound email or a closed conversation transcript must be associated with the case for the corresponding standard trigger.

[Follow-up and closure rules](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-case-closure) have their own conditions, automation level and wait settings. An unanswered representative email counts as the first follow-up. Do not assume the configured count means that many *additional* agent emails. Test replies, rule ordering and eligibility changes before closure.

Current setup pages label **simulation and shadow mode as preview**, and both consume credits. Simulation uses a disabled line of business and at most 100 selected cases per run; shadow mode observes predicted actions without sending email or changing case records. It is not free and does not demonstrate successful execution of downstream writes. For study, use synthetic examples and the evaluation exercise below. Verify preview terms and the actual tenant before platform use.

The setup page requires review/send in the confirmation mode, while a runtime table uses less precise wording about sending. Treat the configured approval requirement as the intended control and verify the observed tenant behavior; do not copy that table as proof that every action is automatically approved.

### Design enforceable SLAs

An SLA defines service commitments; an **SLA item** describes when a KPI applies and its warning/failure/success behavior; an **SLA KPI** defines the tracked measure; an **SLA KPI instance** is the runtime record for a specific case. Keep those layers distinct.

Configure business hours, holidays, applicable-from time, pause/resume rules and status conditions before choosing durations. Apply the correct SLA by default, entitlement, customer or automation. Item applicability must be mutually understandable; conflicting items and stale calendars produce surprising clocks.

Use Power Automate for warning, failure or success actions that require notifications, assignment, escalation or record updates. Design flows for retries, duplicate triggers, stale case state, least privilege and observable failure. Timer controls display current KPI state on a form; they do not create the underlying SLA logic.

Test exactly-on-boundary cases, after-hours intake, holidays, paused cases, priority changes, SLA reassignment, reopen and flow failure. Monitor active KPI instances and trace from case → applied SLA → item → KPI instance → timer/action evidence.

> **Related item:** Entitlements describe what support a customer may consume; SLAs describe service timing/commitments. They can work together, but the March 2026 blueprint explicitly measures SLA configuration while entitlements are adjacent context.

---

#### Read the clock configuration in order

The [current SLA configuration](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/define-service-level-agreements) uses Unified Interface SLAs. `Applicable From` selects the datetime that starts a KPI; `Applicable When` tests whether an item applies. A missing business-hours schedule means all day, every day. A custom KPI needs the relevant lookup to an SLA KPI instance and a timer mapped to it.

[Pause precedence](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-pause-conditions-sla) runs from entity defaults to KPI overrides to SLA-item overrides, when pause/resume is enabled. Resuming cancels the old KPI instance and creates a new one. Preserve and correlate the history rather than promising one instance ID for the entire case. The allow-pause setting cannot be toggled after an SLA item is first saved.

[Calendar changes](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/change-schedules) do not automatically change existing KPI-instance deadlines. Certain events, including pause/resume or reapplication, recalculate using current schedules. Plan new-case and in-flight behavior separately and test both.

## 2. Configure representative experience and routing

### Trace the unified-routing pipeline

A **workstream** defines intake and distribution behavior for a channel or record type. Classification enriches a work item with attributes such as language, priority or required skills. Route-to-queue rules select an eligible queue. Assignment rules/methods choose a representative who satisfies availability, capacity, presence and skill requirements. Draw and test these as separate stages.

Configure representative/user settings, presence and capacity profiles around actual concurrent work. Capacity settings guide automatic assignment; manual or forced assignment can exceed the limit. Configure realistic work limits and cross-channel behavior. Queues need membership, operating ownership, prioritization, overflow and fallback. Never let unmatched or unassignable work disappear silently.

Basic routing rule sets suit simpler record-to-queue decisions; unified routing supports classification and assignment at broader scale. Skills-based routing matches required skills/proficiencies to representatives. Skill finder models can infer skills from supported text; validate training data, confidence, drift, false matches and manual override. Record routing needs an intake trigger and deterministic behavior for records edited repeatedly.

Test rule order, stop conditions, ties, unavailable queues, full capacity, no matching skill, after-hours intake, reopened work and representative disconnect. Collect current telemetry for classification, route-to-queue and assignment, not merely the final owner. The legacy diagnostics feature is no longer the setup target; see the evidence choices below.

> **Related item:** Routing chooses where work goes; security determines whether the assignee can open and act on it; SLAs measure the service commitment. Validate all three together.

#### Capacity and current evidence choices

[Capacity profiles](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/capacity-profiles) define work limits and reset behavior. Microsoft recommends profiles or unit-based capacity rather than mixing them. Users must be bookable resources. With assignment blocking enabled, reaching the profile limit blocks additional automatic assignments even if another profile has room. Supervisors/manual picks can override capacity and produce negative remaining capacity.

Immediate and end-of-day resets differ. The latter resets consumption after the shift even when previous conversations remain open. Reset frequency cannot be edited after creation. A custom per-user limit affects new work, does not evict existing assignments, and can take up to 15 minutes to synchronize; refresh the representative's browser as directed.

The [deprecation notice](https://learn.microsoft.com/en-us/dynamics365/customer-service/implement/deprecations-customer-service) gives March 31, 2026 as the removal date for legacy routing diagnostics. It also retires the older smart-assist suggestions, AI keywords/descriptions and customer-support swarming; use current Copilot/form-fill and embedded Teams capabilities for the relevant tasks. Old pages that still mention enabling those features are historical guidance.

[Conversation diagnostics in Application Insights](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-conversation-diagnostics) requires a Managed Environment, an export connection and appropriate Azure/Power Platform permissions; ingestion has a cost. Verify the events emitted by the target channel/work type. [Real-time record-routing analytics](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/rr-overview) provides queue, representative and work-item views. It respects Dataverse access; different permissions can produce different totals. Ongoing/backlog views require manual refresh, while summary/queue/representative reports refresh automatically. An aggregate dashboard is not a per-rule execution trace.

### Configure scripts, slugs and macros

Representative scripts guide a consistent sequence of steps. Slugs insert supported runtime context into script text or automated actions. Macros execute repeated UI/record actions. Choose scripts for guidance and judgment; use macros for deterministic repetition.

Validate every slug’s source, type, empty value and sensitive-data boundary. A macro needs prerequisites, idempotency, clear partial-failure messaging and a manual recovery path. Avoid large macros that obscure which action failed. Use solutions and controlled deployment for scripts/macros and regression-test them after form or workspace changes.

[Macros](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/macros) run sequential actions and begin with Start macro execution. The anchor case supplies session context; opening another record in an additional tab does not replace that context. Use `${anchor.incidentid}` for the anchor case and `${Session.CurrentTab.entityId}` with `${Session.CurrentTab.entityName}` when the intended target is the active tab. Validate type and identity before writing. A sequence of UI/flow actions is not automatically one database transaction, and retrying it is not automatically idempotent.

### Shape Copilot Service workspace

The workspace is multi-session. A **session template** controls session structure and anchor/context; an **application tab template** controls pages that open within the session; an **experience profile** assigns a persona-specific collection of channels and productivity capabilities. The **Inbox** presents assigned/personal work and can use custom views.

Design profiles by role instead of enabling every feature for everyone. Configure session/tab templates to preserve record context without unnecessary tabs. Create inbox views with meaningful filters, columns and permissions. Test session creation, multiple simultaneous cases, navigation/context preservation, incoming-work notification, reconnect, closure, keyboard use, screen size and accessibility.

> **Related item:** A model-driven app determines the broader app/navigation/component surface. Workspace templates control the runtime multi-session experience inside that app; they do not replace Dataverse security or routing.

---

[Experience profiles](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/overview) bundle the experience for users who already have the required security roles. A user without a custom assignment receives the out-of-box profile. Create a custom [session template](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/session-templates) rather than editing an out-of-box template; the anchor tab cannot be closed. Configure [Inbox settings](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-inbox) on custom experiences. Accepting a voice item opens a new session even when its card also appears in the Inbox.

## 3. Extend Customer Service

### Configure Dataverse data and UI components

Translate requirements into tables, columns, relationships and ownership before changing forms. Prefer standard tables/columns when their meaning fits. New columns need correct data type, requiredness, search/audit behavior and migration plan. Relationships need cardinality, lookup behavior, cascading rules and deletion implications. Avoid storing the same business fact in multiple places.

Forms shape data entry; views shape record retrieval; model-driven app components determine navigation, tables, dashboards and pages exposed to a persona. Use business rules/Power Automate where appropriate but document where logic runs, permissions, transaction boundary and failure behavior. Deploy through solutions with environment variables/connection references as needed.

Dataverse search requires appropriate tables/columns and honors supported security boundaries. Configure relevance around representative tasks and protect sensitive fields. Email templates need approved content, localization, dynamic-field null handling, ownership and update governance. Alerts and in-app notifications need recipient, urgency, action/deep link, expiry, deduplication and accessibility; alert fatigue is a design failure.

> **Related item:** Forms, views and app navigation improve usability; security roles and column security enforce authorization. Do not use a customized UI as the only data-protection control.

### Close the loop with Customer Voice

Choose a survey trigger tied to a meaningful lifecycle event, such as case resolution or conversation closure. Avoid duplicates on reopen/re-resolution; respect contact preference, consent, language and frequency limits. Use Power Automate when orchestration, conditions or downstream actions are needed.

Personalize with validated variables and branching. Never place sensitive values in URLs or uncontrolled templates. Test missing variables, multilingual text, anonymous/authenticated response behavior, opt-out and delivery failure.

Populate/correlate invitations and responses against the correct case and conversation using stable identifiers. Define who can see raw responses, retention, anonymization and how low scores create controlled follow-up. Aggregate results for improvement while preserving the ability to trace authorized operational action. A survey sent is not a service outcome; response bias and low response rates matter.

---

For [Power Automate survey delivery](https://learn.microsoft.com/en-us/dynamics365/customer-voice/send-survey-flow), `Regarding` associates the invitation/response with a supported record such as the case (`incident`); `Recipient details` associates a Contact. An email address alone is not that record relationship, and the send action returns no result payload. Capture delivery/correlation evidence through the appropriate records rather than assuming an output ID.

[Distribution settings](https://learn.microsoft.com/en-us/dynamics365/customer-voice/distribution-settings) distinguish invitation-based and generic links. A generic/custom non-personalized link produces anonymous responses regardless of the anonymous-response toggle. “One response per person” means one per invitation under its supported configuration, not global deduplication across invitations. Saving invited participants as Contacts is on by default and can update an existing contact. Anonymous response settings do not mean no invitation/contact records exist.

[Personalization variables](https://learn.microsoft.com/en-us/dynamics365/customer-voice/personalize-survey) have separate save-value controls when anonymous responses are enabled. Test the complete distribution route, identifiers and saved fields before describing a survey as anonymous. A feedback workflow should implement its own consent, correlation and repeat-invitation policy.

## Integrated scenarios

### Scenario 1: warranty support by email

An automatic record-creation rule converts an email into a case, maps the customer/product and sends the item through classification, a warranty queue and skills/capacity assignment. The applied SLA uses regional business hours. Copilot summarizes history and filters Ask a Question to published warranty knowledge; the representative verifies a draft reply. A warning flow escalates safely, resolution captures evidence and Customer Voice sends one localized survey linked to the case.

### Scenario 2: complex regulated complaint

A high-priority complaint requires restricted case access, a tailored timeline and linked Teams collaboration with approved specialists. External knowledge is clearly attributed; no AI-generated response is sent without review. The case moves between queues with its service-commitment history traceable; pause/resume can create a successor KPI instance. A pause applies only under the effective configured conditions. Audit evidence explains access, assignment, advice, customer communications and resolution.

### Scenario 3: multi-session product-support team

An experience profile assigns product representatives a session template, contextual tabs, inbox view, script and small idempotent macros. Unified routing uses language and product skills plus realistic capacity. A skill-finder inference has a confidence/manual fallback. Operations tests no-match, full-queue and reconnect paths, then uses routing diagnostics and SLA/response metrics to improve rules without weakening security.

---

## Worked decision exercises

### 1. A business clock is not elapsed wall time

Assume support hours are Monday–Friday, 09:00–17:00, all in one timezone with no clock change. A case starts Friday October 2 at 15:00, with a three-business-hour warning and four-business-hour failure. Monday October 5 is a holiday. Friday consumes two hours, so warning is Tuesday October 6 at **10:00**, and failure at **11:00**. If Tuesday 09:00–10:00 is an eligible pause, warning becomes **11:00**, failure **12:00**. Count that paused hour once. This is an original calendar exercise, not a tenant SLA-engine test; custom calculations and in-flight calendar changes need separate verification.

### 2. A lower limit does not remove assigned work

An immediate-reset profile allows four items; a representative has three. Their custom limit becomes two: remaining capacity is `2 − 3 = −1`, and existing items remain assigned. After two finish, one is still open and remaining capacity is one. A forced assignment can still exceed the limit. In a separate end-of-day example, three old conversations remain open when a five-item consumption allowance resets; accepting five more could leave **eight open conversations**. A daily allowance is not an absolute count of simultaneously open work.

### 3. Count cases and routing attempts separately

Cases A, B and C create work items A1, B1 and C1. A is reassigned twice, closing A1 then A2 and creating A2 then A3. The evidence contains **three cases, five work items and three current work items**. Use the case ID for case totals and each work-item ID for routing history. The [record-routing overview](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/rr-overview) explains why reassignment creates a new conversation while the case stays the same. Also check permissions and refresh time before reconciling dashboards.

### 4. Anchor case versus the selected tab

A session is anchored on case A, but the representative opens account B in another tab. A “resolve case” macro should target A after checking case state and authorization. A macro intended to update the selected account should inspect the current tab's entity name/ID and target B. Merely selecting B does not change the anchor to B. If an email step succeeds but a later update fails, record the completed step and recovery state; replaying the whole macro can send duplicate mail.

### 5. Evaluate recommendations before measuring automation

In a synthetic review of 50 cases, the model proposes 40 actions and reviewers accept 34 without correction: **85% of proposals**, or **68% of all cases**. Two proposals would close a case prematurely: **5% of proposals**. An impressive overall acceptance rate does not clear that failure mode. Break results down by intent, language and action severity, and adjudicate disagreements; human decisions are not automatically a perfect reference. Shadow evaluation cannot establish write permissions, successful email delivery or production execution reliability.

### 6. Survey counts and retry keys

Suppose 120 eligible cases receive one invitation each; 36 respond and 27 responses are favorable. The response rate is **30%** and favorable share among respondents **75%**. Do not describe 75% as the satisfaction of all 120 customers. For a policy of one survey per case, deduplicate using `(case ID, survey ID)` across flow retries and later re-resolution. If policy permits one survey per resolution event, deliberately include that stable event ID instead. A platform limit of one response per invitation does not implement either invitation policy.

## Useful blog reading

- [Shadow Mode in Case Management Agent](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/07/09/shadow-mode-case-management-agent/), Madhuri Somara, Peter Bian and Saurabh Gupta, July 9, 2026: use the side-by-side evaluation idea for exercise 5. Current setup documentation still labels shadow mode preview and metered; the blog's production-oriented language is not a GA/support guarantee.
- [What is new with Service Agent](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/07/15/service-agent-microsoft-365-copilot-customer-service/), Saurabh Gupta and Rushil Vora, July 15, 2026: compare an answer, a draft and an action across Dynamics 365/Microsoft 365. For each action name the identity, record, authority and recovery evidence. Service Agent is distinct from the Case Management Agent; future roadmap items and tool counts are not additional exam objectives.

Both accepted articles were read; no tenant agents, notifications, customer communications or paid services were enabled.

## Hands-on labs

1. **Case lifecycle:** Model intake, duplicate/parent-child/merge, status, ownership, resolution/reopen and evidence; configure or storyboard an automatic record rule and activity-monitor failure.
2. **Security/timeline:** Build a persona matrix and configure a case form/timeline with useful record types, cards and highlights; test representative, manager and knowledge-author access.
3. **Knowledge/collaboration:** Configure article lifecycle, translations, internal/external search and Teams collaboration; evaluate stale, unauthorized and ambiguous-result cases.
4. **Copilot/agents:** Write a source/filter/tool/action contract for Ask a Question, summaries, Draft a Response and Case Management Agent; test injection, unavailable source and unauthorized action.
5. **SLAs:** Configure a KPI, SLA items, calendar, applicability, warning/failure/success flow and timer; test boundary, pause, priority change, reopen and flow retry.
6. **Routing:** Build workstream, classification, queue, capacity, skills/skill-finder and assignment rules; capture supported telemetry and record-routing analytics for no-match, overload and after-hours cases; include permissions and refresh timestamps.
7. **Workspace/productivity:** Create an experience profile, session/application-tab templates, inbox view, script/slugs and two small macros; test multi-session recovery and accessibility.
8. **Extension/feedback:** Add a justified Dataverse column/relationship, form/view/app change, notification and email template; distribute a personalized Customer Voice survey and correlate the response.

9. **Original clock/capacity worksheet:** Reproduce exercises 1–3. Add a different calendar, a pause outside business hours and a reassignment. Label which conclusions are arithmetic and which require tenant evidence.
10. **Evaluation and feedback:** Use synthetic cases to build the proposal/error table in exercise 5 and the invitation/response ledger in exercise 6. Include duplicate triggers, a generic survey link, per-variable save settings and a response from a second invitation.

The local arithmetic/calendar checks were executed during this review. The tenant configuration, Power Automate, telemetry export, Copilot, survey-delivery and communication labs remain unexecuted.

## Knowledge checks

1. What distinguishes a case status, status reason and resolution record?

   **Answer:** Status is the broad state, status reason is the more specific state explanation, and the resolution record captures closure details and evidence.

2. Which inputs and failure paths belong in an automatic record creation/update rule?

   **Answer:** Queue/activity, active rule and conditions, mappings/actions, identity/connections, correlation and failure-monitor ownership. Trace case creation separately from routing.

3. When use parent/child cases versus merge?

   **Answer:** Use parent/child records for distinct related work and merge for genuine duplicates after considering preserved obligations and history.

4. Why does queue membership not replace record authorization?

   **Answer:** A queue organizes work. Table/record privileges authorize access and actions; assignment alone does not confer them.

5. Which timeline configuration improves decision-making without exposing data?

   **Answer:** Choose useful record types, card fields and highlights, then test actual data access for each role. Hiding content is not access control.

6. How do knowledge status, language, category and audience affect search?

   **Answer:** They affect relevance and lifecycle eligibility; none should be assumed to provide individual article security.

7. What must an external knowledge-source contract define?

   **Answer:** Source, access identity, whether data is federated or copied, refresh, language, citation and failure behavior.

8. Which reviews remain necessary for AI-authored knowledge?

   **Answer:** Accuracy, policy, customer-data removal, language, source evidence and authorized publication, including translated versions.

9. How does linked Teams chat preserve case context, and what does it not replace?

   **Answer:** It links collaboration with a record; it does not replace case updates, record authorization or communication-retention design.

10. When should suggested contacts fall back to manual expert discovery?

   **Answer:** When no suitable expert is found, the suggestion is low quality, or permissions/availability prevent using the suggested person.

11. What filters should constrain Ask a Question?

   **Answer:** Configure supported representative and automated context filters, test null tags and source scope, and keep authorization separate.

12. What source and approval boundaries apply to summaries and Draft a Response?

   **Answer:** Use the relevant permitted case/conversation/knowledge context, preserve citations where available, and verify content before sending.

13. Which controls are added when Case Management Agent can act?

   **Answer:** Explicit mode, trigger, application identity, supported tools, permissions, approval path, exception handling, monitoring and rollback/recovery.

14. Why must customer text not authorize an agent tool?

   **Answer:** Customer text is task data, not trusted authority to expand permissions, bypass approval or invoke arbitrary tools.

15. Distinguish SLA, SLA item, SLA KPI and SLA KPI instance.

   **Answer:** SLA is the agreement, item its applicability/action rule, KPI the metric definition and instance the runtime tracking record.

16. How do calendar, applicable-from and pause rules change a KPI clock?

   **Answer:** They determine counted working time and pause precedence. Resuming can replace the KPI instance; correlate the history.

17. What makes a warning/failure Power Automate action recoverable?

   **Answer:** Stable operation identity, current-state checks, least privilege, retry behavior and visible partial failures with an owner.

18. Why is a timer control not the SLA itself?

   **Answer:** It displays the underlying KPI-instance state; the SLA configuration and actions establish the commitment.

19. Trace workstream, classification, queue and assignment.

   **Answer:** Intake into workstream, enrich/classify requirements, select queue, prioritize and assign an eligible representative.

20. How do availability, presence and capacity differ?

   **Answer:** Availability is the overall ability to receive work, presence is the configured current state, and capacity tracks workload allowance.

21. When use basic routing instead of unified routing?

   **Answer:** Use basic rules for simpler record-to-queue decisions; choose unified routing when classification, skills, capacity and richer assignment are needed.

22. How should a skill-finder model be validated?

   **Answer:** Use representative labeled examples across supported languages, inspect wrong/missing skill predictions and retain an override/fallback.

23. What fallback prevents unroutable work from disappearing?

   **Answer:** An owned fallback queue or supported overflow path, with monitoring and explicit handling of no eligible representative.

24. Which diagnostic evidence explains a routing decision?

   **Answer:** Work-item identity, timestamps, classification/queue/assignment outcomes and eligible-representative state from currently supported telemetry; aggregate analytics adds context.

25. Compare scripts, slugs and macros.

   **Answer:** Scripts guide steps, slugs supply runtime values, and macros execute sequential repeatable actions.

26. How should a macro report partial failure?

   **Answer:** Name completed and failed actions, affected records and a safe resume/recovery point; do not blindly replay completed sends.

27. Distinguish experience, session and application-tab templates.

   **Answer:** Experience profiles bundle tools/channels for users; session templates define session structure and anchor; application-tab templates define opened tabs.

28. What belongs in an Inbox custom view?

   **Answer:** Useful assigned-work filters, clear columns and supported channel behavior in a custom experience, with the required permissions.

29. Why test a workspace with multiple sessions and reconnects?

   **Answer:** To catch stale context, wrong-record writes, duplicate actions, lost state and recovery problems across sessions.

30. How do tables, columns and relationships differ from forms and views?

   **Answer:** Tables/columns/relationships model stored data and connections; forms/views shape entry and retrieval in the app.

31. Which relationship/cascade decisions can cause data loss or leakage?

   **Answer:** Cascading delete/share/assign and relationship ownership choices can remove or expose related records; test exact behavior and roles.

32. Why does hiding a field not secure it?

   **Answer:** A user may access the data through another form, API or export. Use appropriate table, record and column controls.

33. What makes an in-app notification actionable without causing alert fatigue?

   **Answer:** A clear recipient, priority, action link, expiry and deduplication policy, with a recovery owner for failed delivery.

34. Which controls prevent duplicate or inappropriate surveys?

   **Answer:** Consent/contact policy, stable invitation keys, eligibility checks and deliberate handling of reopen/re-resolution and retries.

35. How are survey invitations/responses correlated to cases and conversations?

   **Answer:** Use supported Regarding and Contact recipient associations and inspect invitation/response records; anonymous and generic-link paths differ.

36. Which balanced measures show that a service change improved outcomes?

   **Answer:** Measure resolution quality and time, corrections, failures, customer outcomes and response rate together, with stable denominators and comparable cohorts.


37. Can you convert a single-queue ARC rule into multiple-queue scope in place?

   **Answer:** No. Create a new rule and resolve conflicting queue membership; saving also does not activate a rule.

38. Does a draft/internal article label isolate it from all other environment users?

   **Answer:** No. Apply the documented knowledge-table security boundary and test access; do not use search filters as authorization.

39. What changes when an integrated provider replaces a federated provider?

   **Answer:** Content is ingested into Dataverse on a schedule, so copy governance and freshness become explicit concerns.

40. Does joining a Teams meeting end the existing voice call?

   **Answer:** No. End that call explicitly; a meeting recording is a separate Microsoft 365 artifact.

41. What is the SLA pause precedence?

   **Answer:** Enabled SLA-item overrides take precedence over KPI overrides, which take precedence over entity defaults.

42. Does editing a calendar immediately recalculate all active KPI deadlines?

   **Answer:** No. Understand and test the recalculation triggers and treatment of in-flight work.

43. What happens when a new capacity limit is below the assigned workload?

   **Answer:** Existing work stays assigned; remaining capacity can be negative. The limit controls later automatic work after synchronization.

44. Does end-of-day reset mean all old conversations closed?

   **Answer:** No. Capacity consumption can reset while old conversations remain open.

45. Which ID should count a case after two reassignments?

   **Answer:** The case ID. Multiple routing work-item IDs describe its separate assignment attempts.

46. Does selecting an account tab replace the anchor case context?

   **Answer:** No. Distinguish anchor slugs from current-tab entity type and ID.

47. Does shadow mode prove an action will succeed or cost nothing?

   **Answer:** No. It evaluates predictions without executing those writes, and current preview documentation says it consumes credits.

48. Does one response per invitation stop duplicate survey invitations?

   **Answer:** No. Implement an invitation policy with stable idempotency keys and inspect saved identity/correlation settings.
---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build complete case/SLA/routing/workspace journeys, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-230 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230) | Free | 1–2 hours to map objectives |
| [Work with cases](https://learn.microsoft.com/en-us/training/paths/work-with-cases-in-dynamics-365-for-customer-service/) | Free | 5 modules; plan 12–20 hours with tenant practice |
| [Knowledge Management Solutions](https://learn.microsoft.com/en-us/training/paths/work-with-knowledge-management-solutions-in-microsoft-dynamics-365-for-customer-service/) | Free | 3 modules; plan 5–8 hours with practice |
| [Entitlements and SLAs](https://learn.microsoft.com/en-us/training/paths/work-with-entitlements-and-slas-in-microsoft-dynamics-365-for-customer-service/) | Free | 2 modules, also present in the cases path; plan 5–8 hours with clock tests |
| [Route and distribute work](https://learn.microsoft.com/en-us/training/paths/unified-routing-distribute-work/) | Free | 3 modules; plan 8–14 hours with current telemetry/routing practice |
| [Help service reps be more productive](https://learn.microsoft.com/en-us/training/paths/agents-help-customer-service/) | Free | 7 modules; plan 10–16 hours with workspace practice; mixed newer and legacy contexts |
| [Extend Customer Service](https://learn.microsoft.com/en-us/training/paths/extend-customer-service/) | Free | 3 modules; now Extend and analyze Customer Service; plan 4–7 hours with solution work |
| [Create surveys with Customer Voice](https://learn.microsoft.com/en-us/training/paths/create-surveys/) | Free | 6 modules; select relevant material or plan 8–12 hours with automation |
| [MB-230T01-A course](https://learn.microsoft.com/en-us/training/courses/mb-230t01) | Paid/provider-dependent | 4 instructor days; English |
| [Free MB-230 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/mb-230/practice/assessment?assessment-type=practice&assessmentId=72) | Free | 45–90 minutes plus review |
| [Dynamics 365 Customer Service documentation](https://learn.microsoft.com/en-us/dynamics365/customer-service/) | Free | 10–25 hours selected implementation/troubleshooting |
| [Pluralsight: Customer Service Build and Expand](https://www.pluralsight.com/courses/microsoft-dynamics-365-customer-service-build-expand) | Subscription/trial | 47 minutes; Vovwe Enyoyi, May 6, 2026; extension supplement, not a complete exam path |
| [Udemy: Dynamics 365 Customer Service Expert](https://www.udemy.com/course/dynamics-365-customer-service/) | Paid | Public indexed view: 3h38, 15 sections/23 lectures, June 2026; differs from the earlier August/4h16 listing. Direct access blocked; confirm current metadata and objective gaps |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the four-day official-course pattern for planning; verify the signed-in event’s published start/end time |

The seven current paths contain **29 module placements and 25 distinct modules**: the SLA and entitlement modules appear in both cases and SLA paths, case management appears in productivity too, and Customer Voice feedback appears in both extension and survey paths. Public pages no longer expose the earlier duration totals; do not use the old 29h02 sum as current or add overlapping modules twice. Practice-time ranges here are planning estimates, not provider runtimes. Allow roughly **60–100 hours** for a new practitioner to complete a primary route, build the labs and remediate the Practice Assessment. The earlier search did not verify an exact O’Reilly, MeasureUp or Whizlabs MB-230 product; that market-wide search was not repeated in this review. Listings centered on hundreds or thousands of “exam questions” were excluded. Reject recalled live content, “valid questions” and pass guarantees.

Current catalog inspection covers public path/course metadata and selected outlines, not complete lessons. Direct Udemy access was blocked; the browser copy was indexed about two months earlier and conflicts with the prior observation. The partner page returned a login shell, and the assessment endpoint returned no substantive content. Confirm access, current duration and coverage before paying or reserving study time.

## Final readiness checklist

- [ ] I can automate and troubleshoot case intake through resolution/reopen without confusing queues, ownership and security.
- [ ] I can govern internal, translated and external knowledge plus Teams collaboration and AI-assisted drafting.
- [ ] I can configure Copilot/Case Management Agent with filters, scoped tools, human checkpoints, evaluation and fallback.
- [ ] I can explain and test SLA, item, KPI, KPI instance, calendar, applicability, pause and Power Automate behavior.
- [ ] I can trace workstream, classification, queues, capacity, skills/skill finder, assignment and diagnostics.
- [ ] I can configure scripts/slugs/macros and experience/session/app-tab templates around representative work.
- [ ] I can extend Dataverse/forms/views/apps/search/templates/notifications without treating UI changes as security.
- [ ] I can distribute, personalize, correlate and govern Customer Voice feedback.
- [ ] I completed scenarios and labs in a nonproduction environment and recorded failures/recovery evidence.
- [ ] I rechecked the official study guide, lifecycle, Practice Assessment and stale credential-page banner before scheduling.

## Source notes

The March 11, 2026 official study guide is the objective authority. The credential surface retains older October 3, 2025/future-tense update text, so this guide does not use those banners as the baseline. Microsoft Learn and product documentation support product behavior; commercial resources are optional perspectives and were not treated as objective authority. All practice questions in this guide are original and conceptual; no exam dumps or recalled items were used.
