---
exam_code: SALESFORCE-PLATFORM-APP-BUILDER
vendor_id: salesforce
official_blueprint: https://help.salesforce.com/s/articleView?id=005389157&language=en_US&type=1
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Salesforce Certified Platform App Builder Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Salesforce’s new Summer ’26 guide, learning path, delivery details, links, and integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#salesforce-platform-app-builder-coverage-record).

**Current baseline:** Salesforce launched a refreshed Platform App Builder exam August 21, 2026. The corrected current weights are Salesforce Fundamentals 18%, Data Modeling and Management 20%, Business Logic and Process Automation 32%, User Interface 17%, and App Deployment 13%. Do not use the older 23/22/28/17/10 map still present in cached prep pages and older courses.<br>
**Exam contract:** The current official guide lists 60 scored multiple-choice questions, up to five unscored questions, 105 minutes, a 73% passing score, Summer ’26 alignment, USD 200 registration, USD 100 retake, and no prerequisite. Verify local taxes, languages, delivery, accommodations, and current checkout details before purchase.<br>
**Upcoming change:** No change after the August 21 refresh or retirement announcement was present September 2, 2026. Because this baseline is less than two weeks old and Salesforce is previewing Winter ’27, recheck frequently.<br>
**Maintenance:** Salesforce’s current Trailhead policy says certification-specific release maintenance is required once per year by the deadline or the credential expires.

## How to use this guide

Work from requirement to evidence: business process → data model → access model → declarative logic → user experience → deployment → monitoring and rollback. Platform App Builder is broader than assembling screens. Every decision can affect ownership, sharing, automation, reporting, integrations, limits, and later change.

Use only an authorized Trailhead Playground, Developer Edition, or sandbox. The original scenarios and checks below teach decisions; they are not recalled exam items. Do not use dumps, copied live questions, or shared superbadge solutions.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, release, or operational context. It supports the topic but does not assert that Salesforce uses that wording in the public blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Salesforce Fundamentals | 18% | Declarative/programmatic boundary, least-privilege and extension review |
| Data Modeling and Management | 20% | Entity/relationship model, field choices and controlled data movement |
| Business Logic and Process Automation | 32% | Tested Flow/formula/validation/approval behavior with failure evidence |
| User Interface | 17% | Persona/form-factor experience and activation matrix |
| App Deployment | 13% | Versioned dependency-aware promotion and rollback record |

## 1. Salesforce Fundamentals — 18%

Declarative customization uses platform metadata and builders; programmatic customization uses Apex, Lightning Web Components, APIs, or other code when requirements exceed declarative boundaries. “Clicks before code” is a starting preference, not an absolute rule. Compare maintainability, transaction behavior, scale, testability, security context, portability, UI needs, team skills, and limits.

Map access in layers: user license and feature licenses; profile/permission sets for object, field, app, system, and feature permissions; organization-wide defaults; hierarchy, sharing rules, teams, territories, queues, and manual or programmatic sharing for records. Sharing opens record access but cannot supply missing object CRUD. Lightning component visibility and page layouts improve experience but do not secure data.

Report types determine record/relationship availability; filters, groupings, formulas, and buckets shape a report; folders and underlying data permissions shape its audience. Dashboards depend on source reports and a running-user model. Always validate analytical output as the target persona.

AgentExchange/AppExchange packages can add apps, agents, flows, components, permissions, and integrations. Assess publisher trust, package type, licenses, data access, external endpoints, upgrade/uninstall path, support, and sandbox results before installation.

`Related item:` A declarative solution is still software. Give it ownership, version control, tests, deployment evidence, monitoring, and a retirement path.

## 2. Data Modeling and Management — 20%

Start with durable business entities and cardinality. Reuse standard objects when their lifecycle and behavior fit; create custom objects when the concept is genuinely distinct. A lookup can be optional and typically preserves independent ownership; master-detail makes the child dependent, inherits important access behavior, supports native roll-ups, and can cascade delete. Many-to-many models use a junction object, commonly with two master-detail relationships, when that dependency is appropriate.

Field design affects validation, storage, reporting, integrations, and later migration. Consider type, precision, length, requiredness, uniqueness, case sensitivity, defaults, picklist governance, external IDs, encryption, history, and help text. Before changing a field type, inventory existing data, formulas, flows, validation, reports, code, integrations, packages, and information loss.

Formula fields derive a value at read time. Roll-up summaries aggregate eligible child records on the parent in supported master-detail contexts. Cross-object formulas expose related values without copying them. Choose based on ownership of truth, freshness, aggregation, security, performance, and reporting needs.

Data Import Wizard offers guided bounded imports; Data Loader supports API-based insert, update, upsert, delete, and export at larger scale. External objects expose data held outside Salesforce through supported connectivity and have different transaction, relationship, search, reporting, and availability considerations. Rehearse mapping, automation, duplicates, failures, reconciliation, and rollback with synthetic data.

`Related item:` Schema Builder visualizes and can edit metadata, but a convenient canvas does not replace a reviewed data dictionary, ownership model, or migration plan.

## 3. Business Logic and Process Automation — 32%

This is the largest domain. Translate each rule into trigger, criteria, inputs, actor/security context, reads/writes, outputs, side effects, bulk volume, fault behavior, observability, and recovery.

Formula fields calculate values; validation rules reject writes that violate a condition; flows orchestrate screens, records, schedules, events, or background work; Flow Approval processes coordinate reviewed decisions. Do not use automation merely because it can express a rule—select the narrowest mechanism with the correct transaction and user experience.

Choose Flow types deliberately:

- record-triggered flows react to record change; before-save fits efficient same-record updates and after-save fits many related actions;
- screen flows guide user interaction and validation;
- autolaunched flows expose reusable background logic;
- scheduled and schedule-triggered patterns handle time-based populations;
- platform-event and other specialized starts decouple event producers and consumers where supported.

Flow design must be bulk-safe. Operate on collections, avoid queries or writes inside unbounded loops, constrain entry criteria, avoid recursion, make retryable effects idempotent, and use fault connectors or platform error handling. Debug with representative users and datasets. Inspect Flow Interviews/errors, record history, logs or other supported evidence before changing logic.

Flow Approval design includes entry, submitter, approver routing, lock behavior, approval/rejection/recall actions, delegation, timeouts/escalation where supported, and what happens when data changes. Version and activate deliberately.

Agentforce can initiate or assist business processes. Bound its topics/actions, instructions, grounding, permissions, verification, side effects, and escalation. Generative text must not silently become trusted transaction input.

`Related item:` Order of execution connects validation, flows, assignment, duplicates, Apex, workflow-era behavior, and commit. Troubleshoot the whole transaction, not only the visible flow.

## 4. User Interface — 17%

Choose the surface by task and persona. Page layouts arrange fields, related lists, buttons, and actions and participate in record-type/profile assignment. Lightning App Builder composes app, home, and record pages from components. Dynamic Forms places fields/sections as components and supports conditional visibility. Compact layouts, highlights, tabs, list views, utility items, and actions serve different interaction needs.

Custom buttons and links navigate or invoke supported behavior; quick actions can be global or object-specific, with different record context. Screen flows can be embedded or launched from actions. Lightning components may be standard, managed, or custom; declarative builders place and configure them, while programmatic LWC/Apex work belongs to developers when behavior exceeds declarative capabilities.

Design an activation matrix: app × record type × profile/persona × desktop/phone → expected page, layout, fields, components, and actions. Test accessibility, required/read-only behavior, visibility, empty/error states, and performance. Mobile needs deliberate navigation, action, form-factor, offline/connectivity, and component-support review.

`Related item:` Conditional visibility reduces clutter; it does not enforce object, field, record, or action authorization.

## 5. App Deployment — 13%

Application lifecycle management includes intake and acceptance criteria, architecture/security review, development environment, source/version record, testing, release approval, deployment, verification, monitoring, rollback, and retirement. Choose sandbox types based on metadata/data fidelity, capacity, refresh behavior, privacy, integration isolation, test objective, and cost—not by name alone.

Change sets move supported metadata between related orgs. They do not provide a complete universal deployment solution. Identify dependencies, profiles/permission changes, data/configuration steps, destructive changes, tests, manual post-deployment work, and ordering. Validate inbound change sets before deploying, record results, and test as intended personas afterward.

Unmanaged packages are editable snapshots without an upgrade path controlled like managed packages. Managed packages support namespace/protection and provider upgrades for distributed applications. Unlocked packages and Salesforce DX/source-driven approaches support modular internal development. Know the use case and boundaries; confirm current feature behavior in official documentation.

A deployment plan names owner, window, target, artifact/version, prerequisites, test results, backup/recovery, communication, steps, validation queries/user journeys, monitoring, rollback threshold, and evidence location.

`Related item:` Metadata deployment does not automatically migrate business data, secrets, endpoint authorization, certificates, or every org-specific setting.

## Integrated scenarios

### Scenario 1: Partner onboarding application

Design partner applications, review steps, contacts, and required documents. Produce an entity/relationship model, least-privilege matrix, persona-specific pages, validation/formulas, approval Flow, notification/fault behavior, reports, and a sandbox-to-production plan. Explain which requirement would cross into Apex/LWC and why.

### Scenario 2: Equipment inspection process

Users complete a mobile screen flow, attach evidence, and create follow-up work for failed checks. Model equipment, inspection, findings, and work; handle master-detail/lookup tradeoffs, offline/poor connection behavior, bulk updates, duplicate prevention, accessible screens, dashboard grain, and recovery after partial downstream failure.

### Scenario 3: Governed service automation

An Agentforce agent may gather a request and invoke an approved Flow. Define topics/actions, verification, field access, transaction input validation, deterministic branches, human approval, sandbox tests, audit evidence, deployment order, monitoring, and immediate disable/rollback.

## Hands-on evidence labs

1. **Requirements boundary (45–75 min):** Classify ten requirements as configuration, Flow, package, or code and document constraints.
2. **Relationship model (75–120 min):** Build a three-object model with lookup/master-detail choices, formulas, roll-up, and delete/access tests.
3. **Least privilege (60–90 min):** Implement two personas and prove object, field, and record allowed/denied cases.
4. **Data operation (60–90 min):** Import/upsert synthetic data using external IDs; reconcile rejects, automation, duplicates, and rollback.
5. **Flow lifecycle (120–180 min):** Build, bulk-test, fault-test, version, activate, observe, and roll back a record-triggered plus reusable flow.
6. **User experience (75–120 min):** Build record types, layouts, Lightning pages, actions, visibility, and desktop/mobile activation evidence.
7. **Approval and agent boundary (75–120 min):** Design a Flow Approval plus optional licensed Agentforce invocation; test verification and unauthorized cases.
8. **Deployment rehearsal (90–150 min):** Validate a metadata promotion, dependencies, user journeys, reports, monitoring, and rollback in disposable orgs.

## Readiness checks

1. Which facts decide declarative versus programmatic implementation?
2. Why is “clicks before code” not the whole architecture decision?
3. How do licenses, object CRUD, field security, and record sharing combine?
4. Why can component visibility not secure a field?
5. What trust and lifecycle questions precede AgentExchange installation?
6. How do report type, data access, folder, and running user affect analytics?
7. When should a standard object be preferred over a custom object?
8. Which ownership, delete, sharing, and roll-up effects distinguish relationship types?
9. How does a junction object implement many-to-many?
10. What dependencies must be inventoried before a field-type change?
11. When do formula, cross-object formula, and roll-up summary fit?
12. What makes an external object different from imported Salesforce data?
13. Which signals choose Import Wizard versus Data Loader?
14. How do external IDs make upsert deterministic?
15. What is the difference between validation and duplicate control?
16. Which Flow start fits same-record, related-record, guided, scheduled, and event work?
17. Why is before-save often efficient for same-record updates?
18. Which collection practices make Flow bulk-safe?
19. How do entry criteria and idempotency control repeat effects?
20. What evidence should a fault path preserve?
21. How do you diagnose a failed Flow without guessing?
22. Which choices define a Flow Approval lifecycle?
23. What happens to automation when record data changes during approval?
24. Why must order of execution be tested end to end?
25. Which Agentforce boundaries make an invoked Flow safe?
26. How are page layout, Lightning page, and Dynamic Forms responsibilities different?
27. When is an action global versus object-specific?
28. When does a requested component require programmatic work?
29. What belongs in a page activation matrix?
30. Which tests expose mobile/form-factor failure?
31. How do managed, unmanaged, and unlocked package purposes differ?
32. Which sandbox properties matter to each test objective?
33. What can a change set move, and what remains manual or separate?
34. How do you discover missing metadata dependencies?
35. Which validations run immediately after deployment?
36. What objective rollback threshold makes a release safer?
37. What changed in the August 21, 2026 baseline?
38. Which current domain deserves the most practice and why?
39. What annual action keeps the credential current?
40. Which authoritative pages will you recheck before scheduling?

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick resources that fit your gaps and learning style. For any commercial course, confirm it uses the August 21, 2026 **18/20/32/17/13** blueprint and 73% passing score; older 23/22/28/17/10 material needs reconciliation.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Current official Summer ’26 exam guide](https://help.salesforce.com/s/articleView?id=005389157&language=en_US&type=1) and [credential page](https://trailhead.salesforce.com/credentials/platformappbuilder) | Public | 20–30 min | Authoritative objectives, contract, and current credential identity |
| [Prepare for Your Salesforce Platform App Builder Certification](https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-platform-app-builder-certification) | Free Trailhead | ~39 hr 20 min | Broad current hands-on path across all five domains; select weak sections |
| [Platform App Builder Maintenance (Winter ’26)](https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-certification-maintenance-winter-26) | Free Trailhead | ~30 min | Recent Flow, list-view, AI-summary, and screen-preview changes; maintenance context |
| [Salesforce Certified Platform App Builder + Practice Test](https://www.udemy.com/course/salesforce-platform-app-builder/) by Mike Wheeler and team | Paid | 23 hr 35 min listed | Guided application build; listed July 2026, so explicitly reconcile the August blueprint |
| [Salesforce Platform App Builder Certification Training](https://www.oreilly.com/videos/salesforce-platform-app/9781804611197/) | O’Reilly subscription | 12 hr 3 min | Long-form foundational demos; August 2022 content requires current Flow/Agentforce/deployment supplementation |
| [Salesforce Platform App Builder Certification Bootcamp](https://www.oreilly.com/live-events/salesforce-platform-app-builder-certification-bootcamp/0642572176150/) | O’Reilly subscription/live schedule | One live event; verify start/end | Instructor-led scenario and app lifecycle practice; confirm current session and blueprint |
| [Salesforce Ben five-minute overview](https://www.youtube.com/watch?v=q_xsHJDgMfY) | Public YouTube | 5 min | Quick orientation only; published 2023 and therefore not the current weight baseline |
| [Focus on Force Salesforce certification resources](https://focusonforce.com/) | Paid | 10–25 hr selected plus timed practice | Explanations and targeted practice; verify the August 2026 version before purchase |

Reject guaranteed-pass products, “actual question” files, VCE collections, and unexplained answer banks. Good practice content uses original scenarios and teaches why choices fit.
