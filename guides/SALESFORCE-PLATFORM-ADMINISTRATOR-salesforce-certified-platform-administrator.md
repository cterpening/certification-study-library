---
exam_code: SALESFORCE-PLATFORM-ADMINISTRATOR
vendor_id: salesforce
official_blueprint: https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-setup-and-objects/get-started-with-administrator-certification-prep
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Salesforce Certified Platform Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The current public weights, links, exam-integrity boundary and maintenance rule were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#salesforce-platform-administrator-coverage-record).

**Current baseline:** Salesforce’s current Trailhead prep page uses eight domains: Configuration and Setup 15%, Object Manager and Lightning App Builder 15%, Sales and Marketing Applications 10%, Service and Support Applications 10%, Productivity and Collaboration 10%, Data and Analytics Management 17%, Automation 15%, and Agentforce 8%. A Salesforce Admins announcement says this blueprint took effect December 15, 2025.<br>
**Source discrepancy:** The public Help exam guide still displayed a Summer ’25 version label when checked, although its weights include the December 2025 Agentforce refresh. Use the live weights and current product documentation, and verify the registration-page contract before paying. The Help guide listed 60 scored multiple-choice/multiple-select questions, up to five unscored questions, 105 minutes, no prerequisite, and different English/Japanese passing scores.<br>
**Upcoming change:** No later blueprint or retirement announcement was present on the checked certification, prep, or program-overview pages September 2, 2026. Salesforce has a Winter ’27 preview in progress, so recheck close to the appointment.<br>
**Maintenance:** Salesforce says credential holders must complete the certification-specific release maintenance module once per year by its deadline or the credential expires.

## How to use this guide

Learn decisions, dependencies, and evidence—not menu paths alone. For each requirement, identify the data owner, user population, least privilege, declarative control, license/edition constraint, deployment boundary, validation signal, and recovery path. Build the exercises only in an authorized Developer Edition, Trailhead Playground, or disposable sandbox.

The guide is not an exam dump. Its scenarios and checks are original prompts for explaining and performing administrator work. Never use recalled live questions, copied assessment answers, or shared superbadge solutions.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, release, or operational context. It supports the topic but does not assert that Salesforce uses that wording in the public blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Configuration and Setup | 15% | Org/user/security decision record and access test |
| Object Manager and Lightning App Builder | 15% | Data model, record experience, and activation matrix |
| Sales and Marketing Applications | 10% | Lead-to-opportunity and campaign behavior trace |
| Service and Support Applications | 10% | Case-routing, response, escalation, and entitlement trace |
| Productivity and Collaboration | 10% | Activity, mobile, Chatter, and extension access evidence |
| Data and Analytics Management | 17% | Rehearsed data operation plus audience-correct report/dashboard |
| Automation | 15% | Bulk-safe Flow/approval design with fault and rollback evidence |
| Agentforce | 8% | Bounded use case, permissions, instructions, preview, and escalation |

## 1. Configuration and Setup — 15%

Treat Setup as a control plane. Company settings establish locale, currency, fiscal periods, business hours, holidays, default language, and other assumptions consumed by automation and reporting. A technically valid configuration can still be wrong if those business assumptions are wrong. Record who approved them and which downstream calculations or service timers depend on them.

User lifecycle is more than creating a user. Map identity → user license → profile baseline → permission sets and groups → role/territory/reporting position → queues/public groups/teams → login and session controls. Freeze can stop login quickly; deactivation releases some access but has ownership and automation implications; users are not deleted. Prefer minimum profiles plus additive permission sets, and test effective access as the intended persona.

Separate the layers of the sharing model:

- organization-wide defaults establish the restrictive baseline;
- role hierarchy can open upward visibility for many objects;
- sharing rules expand access to defined groups or roles;
- teams, queues, territories, manual sharing, and programmatic sharing solve narrower cases;
- object CRUD and field-level security still constrain what record sharing can expose.

Security controls include MFA and identity verification, login hours/IP ranges, password/session policy, delegated administration, Setup Audit Trail, login history, and connected-app/session review. Diagnose access with a layer-by-layer trace; do not compensate for a missing object permission by making all records public.

`Related item:` Licenses bound the capabilities that permission sets can grant. “Permission assigned” does not prove “feature licensed,” and a UI element being visible does not prove record or field access.

## 2. Object Manager and Lightning App Builder — 15%

Begin with the business entities and lifecycle, then choose standard objects before custom ones when semantics fit. Distinguish lookup from master-detail ownership, sharing, required-parent, roll-up, and delete behavior. Use junction objects for many-to-many relationships and understand that changing relationship or field types can affect data, automation, reports, formulas, integrations, and security.

For fields, reason about data type, precision, requiredness, uniqueness, external IDs, defaults, help text, dependencies, history, encryption, and deletion/restore implications. Formula fields calculate at read time; roll-up summaries aggregate eligible child records in supported relationships. Validation rules reject invalid writes but must allow legitimate integrations, imports, automation, and correction paths.

Record types select business processes, picklist values, and page-layout assignments; they do not grant record access. Page layouts govern detail-page organization and some edit behavior. Lightning pages govern components, regions, visibility, and activation by org/app/record type/profile/form factor. Dynamic Forms can place fields and sections as components, but universal field requirements and data security remain independent.

Build an activation matrix before release: persona × app × record type × desktop/mobile → expected page and actions. Validate with representative users, not only an administrator.

`Related item:` A page visibility filter improves experience, not authorization. Enforce sensitive access with object, field, record, and feature permissions.

## 3. Sales and Marketing Applications — 10%

Trace the lifecycle from campaign member or prospect through lead qualification, conversion, account/contact creation or matching, opportunity progression, products/price books, forecasting, and closure. Know what lead conversion creates, how field mapping behaves, and when a business should work directly with accounts/contacts rather than force every record through Lead.

Sales processes and record types constrain relevant stages; Path can guide users but does not replace data validation. Opportunity stages influence probability, forecast category, reporting, and automation. Products, standard/custom price books, price book entries, quantities, and sales prices form a dependency chain; diagnose inactive/missing currency or price-book context before assuming permissions alone.

Campaigns organize marketing initiatives and member responses. Campaign hierarchy, member status, attribution choices, and influence reporting answer different questions. Lead assignment, scoring, queues, and territory/forecasting features are edition- and configuration-sensitive; verify availability in the target org.

`Related item:` Automation cannot repair an undefined sales process. Agree on ownership, qualification, duplicate policy, stage entry/exit criteria, and reporting definitions before encoding them.

## 4. Service and Support Applications — 10%

Model intake channel → Case → owner/queue → priority and service target → knowledge or resolution → closure. Case assignment routes new or updated work; auto-response communicates receipt; escalation changes visibility or ownership when criteria and age conditions are met. Keep those responsibilities distinct when selecting a tool.

Support processes and record types tailor status and experiences. Queues hold work for eligible members, while Omni-Channel can route work using presence and capacity. Email-to-Case, Web-to-Case, Knowledge, macros, entitlements, milestones, and Einstein/Agentforce service capabilities depend on licensing and setup. Know the high-level purpose and validate current edition details rather than memorizing a universal availability table.

Test the full clock: business hours, holidays, case creation time, assignment, response, escalation, entitlement milestone, agent actions, and closure. Capture both positive and negative paths so an apparently successful notification does not hide incorrect ownership.

`Related item:` A queue is an ownership construct; routing capacity and a service-level clock are separate concerns.

## 5. Productivity and Collaboration — 10%

Activities connect tasks and events to people and records. Distinguish assigned work from scheduled meetings, recurring behavior, shared activities, calendar visibility, and email/logging options. Confirm whether a feature creates a Salesforce record, synchronizes an external system, or merely displays context.

Chatter supports feeds, posts, comments, mentions, groups, files, and record collaboration. Public/private/unlisted group behavior and internal versus external users matter. Files have their own ownership and sharing behavior; putting a component or related list on a page does not automatically grant document access.

For mobile, evaluate navigation, compact layouts, actions, Lightning-page activation, component form-factor support, and offline/connection constraints. AppExchange and AgentExchange extend an org through packaged apps, components, flows, and agents. Assess publisher, package type, permissions, data access, external endpoints, license, upgrade/uninstall behavior, support, and sandbox testing.

`Related item:` Installed package permissions and connected integrations enlarge the trust boundary. Treat installation as a security and lifecycle decision, not a convenience click.

## 6. Data and Analytics Management — 17%

Choose the operation by record count, object support, scheduling/API need, transformation complexity, and required error evidence. The Data Import Wizard is guided and bounded; Data Loader supports larger API-oriented insert/update/upsert/delete/export work. External IDs enable matching for upsert. Always rehearse mapping, ownership, validation, duplicates, automation, and rollback on a small sample.

A safe data run has: source snapshot, row identifier, field mapping, transform rules, dry run/sample, expected creates/updates/rejects, error-file review, reconciliation queries/reports, and recovery plan. Deleting, hard deleting, mass transferring, archiving, exporting, and backing up solve different problems. An export is not a proven restore until recovery is rehearsed.

Duplicate rules decide whether to allow, alert, or block; matching rules define candidate similarity. Validation rules enforce field-level business conditions. Use both deliberately and monitor false positives, integration behavior, and the correction workflow.

Reports begin with a report type and accessible data. Know tabular, summary, matrix, and joined use cases; groupings, filters, cross filters, buckets, row/summary formulas, conditional highlighting, charts, subscriptions, and exports. Dashboards visualize source reports and can run as a specified user or dynamically, subject to licensing and sharing. Folder access, underlying record access, field visibility, and running-user context explain many “missing number” incidents.

`Related item:` A correct query can still produce the wrong business metric when grain, time zone, fiscal period, currency, ownership, or filter semantics are wrong.

## 7. Automation — 15%

Select the narrowest current tool that meets the requirement. Flow covers record-triggered, screen, autolaunched, scheduled, and other orchestration patterns. Assignment and escalation rules, approvals, duplicate/validation rules, roll-ups, and product features have specialized semantics. Do not preserve obsolete Workflow Rules or Process Builder designs as the default for new work.

Translate requirements into trigger, entry criteria, actor/system context, read/write set, branch rules, bulk volume, transaction boundary, recursion/idempotency controls, fault path, notifications, observability, and retry/recovery. Use before-save record-triggered flows for efficient same-record changes when suitable; use after-save when related records or actions require a saved record. Avoid queries or writes inside unbounded loops.

Approval processes define entry, submitters, approver selection, lock behavior, approval/rejection/recall actions, and delegation. Confirm what happens when data changes during approval and how administrators recover stranded work.

Debug with representative personas and bulk data. Test create/update/no-op, invalid data, permission failure, missing related data, multiple matching paths, and downstream failure. Activate versions deliberately and retain a documented rollback.

`Related item:` Order of execution connects validation, flows, assignment, escalation, duplicate controls, Apex, and commits. Diagnose the transaction as a whole instead of treating each automation in isolation.

## 8. Agentforce — 8%

The Administrator domain is foundational, not the Specialist blueprint. Know when a bounded agent is appropriate, what trusted data it may use, which topics/actions/instructions it has, under whose security context it acts, and when it must refuse or escalate. A fluent answer is not proof of authorization or correctness.

Be ready to maintain, update, or install prompts and instructions in Agentforce Builder, inspect permissions, and perform light testing with conversation preview. Test allowed, denied, ambiguous, unsafe, stale-data, missing-permission, and escalation cases. Review trace/evidence without copying sensitive data into notes. Separate instructions (behavior guidance), grounding (context), actions (side effects), and user/agent permissions.

`Related item:` Data quality, sharing, field security, Flow safety, and deployment controls from the other seven domains are prerequisites for responsible agents. Agentforce magnifies weak foundations; it does not bypass them.

## Integrated scenarios

### Scenario 1: Regional sales rollout

A new unit needs distinct opportunity stages, currencies, record experience, access, and dashboards. Produce a license/persona map, role and sharing design, record type/business process, page activation matrix, price-book plan, lead conversion test, forecast/report definitions, deployment sequence, and rollback. Prove that peers cannot see restricted opportunities while managers and approved team members can.

### Scenario 2: Support intake with measurable escalation

Design web/email case intake, duplicate avoidance, assignment queues, response, business-hours escalation, entitlement milestones, knowledge access, mobile actions, and an operations dashboard. Test after-hours intake, absent owner, reopened case, external-user boundaries, and failed notification. Reconcile Case history with routing and dashboard results.

### Scenario 3: Governed automation and agent change

A service agent may summarize an account and initiate a bounded Flow action after verification. Define data minimization, agent user permissions, topic/action filters, prompt/instruction version, Flow transaction and fault behavior, preview cases, sandbox deployment, monitoring, human escalation, and disable/rollback. Confirm that unauthorized fields and actions remain unavailable.

## Hands-on evidence labs

1. **Access matrix (60–90 min):** Create two personas, restrictive defaults, permission sets, one sharing rule, and positive/negative access evidence.
2. **Data model and pages (75–120 min):** Build related custom objects, formulas/validation, record types, layouts, a Lightning page, and an activation matrix.
3. **Sales lifecycle (60–90 min):** Configure a small lead/opportunity process, campaign membership, product/price-book context, and conversion/report evidence.
4. **Case lifecycle (60–90 min):** Configure queues, assignment, response and escalation in a disposable org; record business-hours results.
5. **Data rehearsal (75–120 min):** Import then upsert a synthetic dataset using external IDs; reconcile successes, rejects, duplicates, and rollback.
6. **Analytics audience (60–90 min):** Build report types, grouped/formula reports, and a dashboard; validate as two users with different access.
7. **Bulk-safe Flow (90–150 min):** Implement a record-triggered flow with decisions, related work, fault evidence, bulk test, and rollback note.
8. **Agentforce boundary (60–120 min, where licensed):** Configure or inspect a bounded agent/prompt, permissions, preview cases, action side effects, and escalation. If unavailable, produce a documentation-based design and evidence checklist.

## Readiness checks

Answer without notes, then demonstrate where practical:

1. Which company settings affect dates, service clocks, currency, and reporting?
2. Why can a permission set not grant a feature absent from the user license?
3. What is the difference between freezing and deactivating a user?
4. How do object, field, and record permissions combine?
5. When do role hierarchy, sharing rules, teams, queues, and manual sharing fit?
6. What evidence shows that least privilege works for both allowed and denied cases?
7. When is master-detail unsuitable compared with lookup?
8. How do record types, page layouts, and Lightning-page activation differ?
9. Why is component visibility not a security control?
10. What dependencies must be checked before deleting or changing a field?
11. What does lead conversion create or match, and how is field mapping involved?
12. How do stage, probability, forecast category, and Path differ?
13. What dependencies connect product, price book, price book entry, and opportunity product?
14. What questions do campaign members, hierarchy, and influence answer?
15. How do assignment, auto-response, and escalation rules differ?
16. When do queues and Omni-Channel solve different problems?
17. How do business hours and holidays affect service automation?
18. What evidence proves a Case met its entitlement or escalation behavior?
19. What are the access implications of Chatter groups and Files?
20. Which page/action/navigation choices change the mobile experience?
21. What security and lifecycle questions precede package installation?
22. When should you choose Import Wizard, Data Loader, or an integration?
23. Why is an external ID central to a controlled upsert?
24. How do matching and duplicate rules divide responsibility?
25. What makes an export a tested backup rather than merely a file?
26. How do report type, folder, record sharing, field access, and running user affect results?
27. When do summary, matrix, joined, bucket, and formula features fit?
28. What changes between static-running-user and dynamic dashboards?
29. Which Flow type fits same-record, guided-user, scheduled, and background work?
30. Why should collection work avoid database operations in loops?
31. What must an automation fault path expose to an operator?
32. How do entry criteria and idempotency reduce recursion and duplicate side effects?
33. Which approval decisions cover submitter, approver, locking, rejection, and recall?
34. Why must order of execution be tested as one transaction?
35. What separates an Agentforce instruction, grounding source, topic, and action?
36. Under whose permissions does an agent retrieve data and perform actions?
37. Which preview cases test more than the happy path?
38. When must an agent refuse, verify, or escalate?
39. What annual action keeps the credential active?
40. Which source will you recheck for weights, current release, delivery, price, and maintenance before booking?

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick the formats that close your gaps, confirm that commercial material reflects the current eight-domain/Agentforce blueprint, and spend substantial time performing work in an authorized org.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official certification page](https://trailhead.salesforce.com/credentials/platformadministrator) and [current prep unit](https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-setup-and-objects/get-started-with-administrator-certification-prep) | Public | 15–30 min to baseline | Current identity, weights, policy links, and authoritative refresh point |
| [Official administrator cert-prep trail](https://trailhead.salesforce.com/content/learn/trails/administrator-certification-prep) | Free Trailhead | ~1 hr 20 min | Scenario refresh and interactive checks; not full skill acquisition |
| [Official Administrator Trailmix](https://trailhead.salesforce.com/users/strailhead/trailmixes/prepare-for-your-salesforce-administrator-credential) | Free Trailhead | ~60 hr listed | Broad learning plan with projects and domain weights; select based on gaps |
| [Salesforce Admins blueprint-update article](https://admin.salesforce.com/blog/2026/what-the-salesforce-certified-platform-administrator-exam-update-means-for-admins) | Public | 10–20 min | December 2025 change context and Agentforce expectations |
| [Pluralsight Salesforce Certified Administrator path](https://www.pluralsight.com/paths/salesforce-certified-administrator-update) | Subscription/trial | 13 hr | Structured video path plus practice exam; verify Agentforce coverage |
| [Salesforce Certified Platform Administrator Study Guide](https://www.oreilly.com/library/view/salesforce-certified-platform/9781098165734/) by Mike Wheeler | O’Reilly subscription/book | 13 hr 26 min listed; 20–35 hr with labs/quizzes | Detailed 2025 book, chapter quizzes, and full practice test; supplement current 8% Agentforce domain |
| [Complete Salesforce Certified Platform Administrator Course](https://www.udemy.com/course/salesforce-administrator/) by Mike Wheeler and team | Purchase/subscription | 39 hr 52 min listed | Long-form demos; page says updated August 2026 and includes Agentforce practice |
| [Focus on Force](https://focusonforce.com/) | Paid | 12–25 hr selected study plus several timed sets | Visual study and original practice; use explanations to diagnose gaps, not to memorize answers |

Treat any “guaranteed pass,” live-question, brain-dump, or unexplained answer bank as out of bounds. A legitimate practice source teaches concepts and explains original questions without claiming access to the live exam.
