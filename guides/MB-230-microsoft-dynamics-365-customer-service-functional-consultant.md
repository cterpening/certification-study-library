---
exam_code: MB-230
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# MB-230 Microsoft Dynamics 365 Customer Service Functional Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the March 11, 2026 official objective baseline and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mb-230-coverage-record). The [official MB-230 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230) is authoritative.

**Current baseline:** Skills measured as of March 11, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Metadata discrepancy:** The exam and credential surfaces still display October 3, 2025 or future-tense March 11, 2026 text. Use the newer dated objective set in the study guide; recheck all three official surfaces before scheduling.<br>
**Lifecycle:** The [Dynamics 365 Customer Service Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-customer-service-v3/) is active. The exam is 100 minutes, available in seven languages, has no retirement date, and offers a free Practice Assessment.<br>
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

### Secure records and shape the timeline

Use security roles for table privileges and record access, teams/business units or sharing for scope, and field security where individual columns need protection. Separate representatives, managers, knowledge authors/publishers and administrators. Test each persona against customer, case, knowledge, survey and AI-generated data; a hidden form control is not authorization.

The timeline aggregates activities, notes and related records. Configure record types, sort/filter behavior, card forms, highlights and commands around representative decisions. Avoid overcrowding it with low-value events. Ensure important content remains accessible, correctly secured and useful in mobile/narrow layouts.

> **Related item:** A queue owns or organizes work; a security role authorizes actions; a timeline presents history. Moving a case to a queue does not grant the recipient permission to read it.

### Govern knowledge from authoring to use

Define knowledge settings, article templates, categories, lifecycle states, versioning, review/approval, expiration and ownership. Configure knowledge-enabled tables and internal search so context, language, status and audience produce useful results. Translated articles are distinct governed variants: relate them, assign language-specific reviewers and manage staleness rather than assuming automatic equivalence.

External/integrated knowledge sources need a connector/search contract: source owner, authentication, indexed scope, permissions, refresh latency, ranking/filtering, citation and outage behavior. A representative must be able to distinguish an approved internal article from an external result.

AI can suggest articles, keywords or descriptions and Copilot/knowledge agents can help draft new content. Define approved source context, prohibited data, review/publish authority, evaluation set, citation expectations and rollback. Generated text remains a draft until a responsible owner verifies accuracy, policy, language and audience.

### Configure Teams collaboration

Embedded Teams chat preserves case context while representatives consult specialists. Configure linking, record sharing, permissions, retention and external-participant boundaries. Suggested contacts can be rule-based or AI-assisted; validate why a person is surfaced and provide manual search when suggestions fail. “Join a Teams call” lets selected users bring a customer into a supported call flow; confirm identity, consent and what case data participants can see.

The collaboration experience should answer: who may start/link chats, which records are shared, how a conversation is retained/discovered, what happens when users lack Dynamics access, and how the decision returns to the case. Teams is a collaboration channel, not the system of record for case disposition.

### Configure Copilot and service agents

**Ask a Question** searches configured knowledge; filters should restrict sources by status, language, audience or other supported metadata. Case, timeline and conversation summaries reduce reading time but need a clear source boundary and representative verification. **Draft a Response** should use approved case/conversation/knowledge context; a fluent response is not proof of correctness.

The Case Management Agent can perform supported case lifecycle work. Define enabled operations, scope, trigger, identity, permissions, human checkpoints, exception/stop rules, audit and success measures. Integrating another agent adds knowledge sources and plug-ins/tools; each tool requires typed inputs/outputs, least privilege, validation, timeout/retry, idempotency, logging and explicit confirmation for material actions. Treat customer content as untrusted: it must never grant tool or data access.

Measure correct resolution, representative correction/acceptance, escalation, latency, unauthorized attempts and downstream errors—not just AI usage. Provide a deterministic manual path when an agent or grounding source is unavailable.

> **Related item:** A Copilot answer assists a human inside a workflow; an agent may select or execute actions. Increased autonomy increases the need for scoped identity, action controls, evaluation and recoverability.

### Design enforceable SLAs

An SLA defines service commitments; an **SLA item** describes when a KPI applies and its warning/failure/success behavior; an **SLA KPI** defines the tracked measure; an **SLA KPI instance** is the runtime record for a specific case. Keep those layers distinct.

Configure business hours, holidays, applicable-from time, pause/resume rules and status conditions before choosing durations. Apply the correct SLA by default, entitlement, customer or automation. Item applicability must be mutually understandable; conflicting items and stale calendars produce surprising clocks.

Use Power Automate for warning, failure or success actions that require notifications, assignment, escalation or record updates. Design flows for retries, duplicate triggers, stale case state, least privilege and observable failure. Timer controls display current KPI state on a form; they do not create the underlying SLA logic.

Test exactly-on-boundary cases, after-hours intake, holidays, paused cases, priority changes, SLA reassignment, reopen and flow failure. Monitor active KPI instances and trace from case → applied SLA → item → KPI instance → timer/action evidence.

> **Related item:** Entitlements describe what support a customer may consume; SLAs describe service timing/commitments. They can work together, but the March 2026 blueprint explicitly measures SLA configuration while entitlements are adjacent context.

---

## 2. Configure representative experience and routing

### Trace the unified-routing pipeline

A **workstream** defines intake and distribution behavior for a channel or record type. Classification enriches a work item with attributes such as language, priority or required skills. Route-to-queue rules select an eligible queue. Assignment rules/methods choose a representative who satisfies availability, capacity, presence and skill requirements. Draw and test these as separate stages.

Configure representative/user settings, presence and capacity profiles around actual concurrent work. Capacity prevents overload only when work items consume realistic units and all channels participate consistently. Queues need membership, operating ownership, prioritization, overflow and fallback. Never let unmatched or unassignable work disappear silently.

Basic routing rule sets suit simpler record-to-queue decisions; unified routing supports classification and assignment at broader scale. Skills-based routing matches required skills/proficiencies to representatives. Skill finder models can infer skills from supported text; validate training data, confidence, drift, false matches and manual override. Record routing needs an intake trigger and deterministic behavior for records edited repeatedly.

Test rule order, stop conditions, ties, unavailable queues, full capacity, no matching skill, after-hours intake, reopened work and representative disconnect. Diagnostics should explain classification, route-to-queue and assignment, not merely show the final owner.

> **Related item:** Routing chooses where work goes; security determines whether the assignee can open and act on it; SLAs measure the service commitment. Validate all three together.

### Configure scripts, slugs and macros

Representative scripts guide a consistent sequence of steps. Slugs insert supported runtime context into script text or automated actions. Macros execute repeated UI/record actions. Choose scripts for guidance and judgment; use macros for deterministic repetition.

Validate every slug’s source, type, empty value and sensitive-data boundary. A macro needs prerequisites, idempotency, clear partial-failure messaging and a manual recovery path. Avoid large macros that obscure which action failed. Use solutions and controlled deployment for scripts/macros and regression-test them after form or workspace changes.

### Shape Copilot Service workspace

The workspace is multi-session. A **session template** controls session structure and anchor/context; an **application tab template** controls pages that open within the session; an **experience profile** assigns a persona-specific collection of channels and productivity capabilities. The **Inbox** presents assigned/personal work and can use custom views.

Design profiles by role instead of enabling every feature for everyone. Configure session/tab templates to preserve record context without unnecessary tabs. Create inbox views with meaningful filters, columns and permissions. Test session creation, multiple simultaneous cases, navigation/context preservation, incoming-work notification, reconnect, closure, keyboard use, screen size and accessibility.

> **Related item:** A model-driven app determines the broader app/navigation/component surface. Workspace templates control the runtime multi-session experience inside that app; they do not replace Dataverse security or routing.

---

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

## Integrated scenarios

### Scenario 1: warranty support by email

An automatic record-creation rule converts an email into a case, maps the customer/product and sends the item through classification, a warranty queue and skills/capacity assignment. The applied SLA uses regional business hours. Copilot summarizes history and filters Ask a Question to published warranty knowledge; the representative verifies a draft reply. A warning flow escalates safely, resolution captures evidence and Customer Voice sends one localized survey linked to the case.

### Scenario 2: complex regulated complaint

A high-priority complaint requires restricted case access, a tailored timeline and linked Teams collaboration with approved specialists. External knowledge is clearly attributed; no AI-generated response is sent without review. The case moves between queues without losing the original KPI instance, and a pause is applied only for the configured customer-waiting state. Audit evidence explains access, assignment, advice, customer communications and resolution.

### Scenario 3: multi-session product-support team

An experience profile assigns product representatives a session template, contextual tabs, inbox view, script and small idempotent macros. Unified routing uses language and product skills plus realistic capacity. A skill-finder inference has a confidence/manual fallback. Operations tests no-match, full-queue and reconnect paths, then uses routing diagnostics and SLA/response metrics to improve rules without weakening security.

---

## Hands-on labs

1. **Case lifecycle:** Model intake, duplicate/parent-child/merge, status, ownership, resolution/reopen and evidence; configure or storyboard an automatic record rule and activity-monitor failure.
2. **Security/timeline:** Build a persona matrix and configure a case form/timeline with useful record types, cards and highlights; test representative, manager and knowledge-author access.
3. **Knowledge/collaboration:** Configure article lifecycle, translations, internal/external search and Teams collaboration; evaluate stale, unauthorized and ambiguous-result cases.
4. **Copilot/agents:** Write a source/filter/tool/action contract for Ask a Question, summaries, Draft a Response and Case Management Agent; test injection, unavailable source and unauthorized action.
5. **SLAs:** Configure a KPI, SLA items, calendar, applicability, warning/failure/success flow and timer; test boundary, pause, priority change, reopen and flow retry.
6. **Routing:** Build workstream, classification, queue, capacity, skills/skill-finder and assignment rules; capture diagnostics for no-match, overload and after-hours cases.
7. **Workspace/productivity:** Create an experience profile, session/application-tab templates, inbox view, script/slugs and two small macros; test multi-session recovery and accessibility.
8. **Extension/feedback:** Add a justified Dataverse column/relationship, form/view/app change, notification and email template; distribute a personalized Customer Voice survey and correlate the response.

## Knowledge checks

1. What distinguishes a case status, status reason and resolution record?
2. Which inputs and failure paths belong in an automatic record creation/update rule?
3. When use parent/child cases versus merge?
4. Why does queue membership not replace record authorization?
5. Which timeline configuration improves decision-making without exposing data?
6. How do knowledge status, language, category and audience affect search?
7. What must an external knowledge-source contract define?
8. Which reviews remain necessary for AI-authored knowledge?
9. How does linked Teams chat preserve case context, and what does it not replace?
10. When should suggested contacts fall back to manual expert discovery?
11. What filters should constrain Ask a Question?
12. What source and approval boundaries apply to summaries and Draft a Response?
13. Which controls are added when Case Management Agent can act?
14. Why must customer text not authorize an agent tool?
15. Distinguish SLA, SLA item, SLA KPI and SLA KPI instance.
16. How do calendar, applicable-from and pause rules change a KPI clock?
17. What makes a warning/failure Power Automate action recoverable?
18. Why is a timer control not the SLA itself?
19. Trace workstream, classification, queue and assignment.
20. How do availability, presence and capacity differ?
21. When use basic routing instead of unified routing?
22. How should a skill-finder model be validated?
23. What fallback prevents unroutable work from disappearing?
24. Which diagnostic evidence explains a routing decision?
25. Compare scripts, slugs and macros.
26. How should a macro report partial failure?
27. Distinguish experience, session and application-tab templates.
28. What belongs in an Inbox custom view?
29. Why test a workspace with multiple sessions and reconnects?
30. How do tables, columns and relationships differ from forms and views?
31. Which relationship/cascade decisions can cause data loss or leakage?
32. Why does hiding a field not secure it?
33. What makes an in-app notification actionable without causing alert fatigue?
34. Which controls prevent duplicate or inappropriate surveys?
35. How are survey invitations/responses correlated to cases and conversations?
36. Which balanced measures show that a service change improved outcomes?

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build complete case/SLA/routing/workspace journeys, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-230 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230) | Free | 1–2 hours to map objectives |
| [Work with cases](https://learn.microsoft.com/en-us/training/paths/work-with-cases-in-dynamics-365-for-customer-service/) | Free | 6 hours 39 minutes listed; 12–20 hours with tenant practice |
| [Knowledge Management Solutions](https://learn.microsoft.com/en-us/training/paths/work-with-knowledge-management-solutions-in-microsoft-dynamics-365-for-customer-service/) | Free | 2 hours 38 minutes listed; 5–8 hours with practice |
| [Entitlements and SLAs](https://learn.microsoft.com/en-us/training/paths/work-with-entitlements-and-slas-in-microsoft-dynamics-365-for-customer-service/) | Free | 2 hours 1 minute listed; 5–8 hours with clock/failure tests |
| [Route and distribute work](https://learn.microsoft.com/en-us/training/paths/unified-routing-distribute-work/) | Free | 4 hours 11 minutes listed; 8–14 hours with routing diagnostics |
| [Help service reps be more productive](https://learn.microsoft.com/en-us/training/paths/agents-help-customer-service/) | Free | 6 hours 38 minutes listed; 10–16 hours with workspace practice |
| [Extend Customer Service](https://learn.microsoft.com/en-us/training/paths/extend-customer-service/) | Free | 1 hour 12 minutes listed; 4–7 hours with solution work |
| [Create surveys with Customer Voice](https://learn.microsoft.com/en-us/training/paths/create-surveys/) | Free | 5 hours 43 minutes listed; select relevant modules or allow 8–12 hours with automation |
| [MB-230T01-A course](https://learn.microsoft.com/en-us/training/courses/mb-230t01) | Paid/provider-dependent | 4 days |
| [Free MB-230 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/mb-230/practice/assessment?assessment-type=practice&assessmentId=72) | Free | 45–90 minutes plus review |
| [Dynamics 365 Customer Service documentation](https://learn.microsoft.com/en-us/dynamics365/customer-service/) | Free | 10–25 hours selected implementation/troubleshooting |
| [Pluralsight: Customer Service Build and Expand](https://www.pluralsight.com/courses/microsoft-dynamics-365-customer-service-build-expand) | Subscription/trial | 47 minutes; current extension-focused supplement, not a complete exam path |
| [Udemy: Dynamics 365 Customer Service Expert](https://www.udemy.com/course/dynamics-365-customer-service/) | Paid | 4 hours 16 minutes; updated August 2026, but gap-check routing, workspace and Customer Voice against the official blueprint |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the four-day official-course pattern for planning; verify the signed-in event’s published start/end time |

The seven selected official paths total **29 hours 2 minutes** before hands-on work; some modules are adjacent to the current blueprint, so select deliberately. Allow roughly **60–100 hours** for a new practitioner to complete a primary route, build the labs and remediate the Practice Assessment. No exact current O’Reilly, MeasureUp or Whizlabs MB-230 product was independently verified on September 1, 2026. Listings centered on hundreds or thousands of “exam questions” were excluded. Reject recalled live content, “valid questions” and pass guarantees.

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

The March 11, 2026 official study guide is the objective authority. The credential and exam surfaces contain older October 3, 2025/future-tense update text, so this guide does not use those banners as the baseline. Microsoft Learn and product documentation support product behavior; commercial resources are optional perspectives and were not treated as objective authority. All practice questions in this guide are original and conceptual; no exam dumps or recalled items were used.
