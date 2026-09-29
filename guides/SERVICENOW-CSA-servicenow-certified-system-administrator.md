---
exam_code: SERVICENOW-CSA
vendor_id: servicenow
official_blueprint: https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011554
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# ServiceNow Certified System Administrator (CSA) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 29 review maps 30 current official subtopics, answers 40 original readiness prompts and executes 34 local Python/SQLite checks. Eight instance activities remain proposed. See the [coverage record](../docs/SOURCE-VALIDATION.md#servicenow-csa-coverage-record) and [deep-review evidence](../docs/research/2026-09-29-servicenow-csa-deep-review.md).

**Current baseline:** Platform Overview and Navigation 7%; Instance Configuration 10%; Configuring Applications for Collaboration 20%; Self Service and Automation 20%; Database Management and Platform Security 30%; Data Migration and Integration 13%.<br>
**Exam contract:** The public blueprint lists 60 multiple-choice/multiple-select questions in 90 minutes, delivered through Pearson at a test center or online with OnVUE. Registering is payment; the attempt must be scheduled and completed within 90 days. The result is conditional and may be audited. The cut score is not public and is not always 70%. Verify current fee, language, accommodations, system test, ID and retake rules before purchase.<br>
**Experience target:** ServiceNow recommends database/system-management experience, administrative access or role experience, helpful IT help-desk/process knowledge, and three to six months using or maintaining an instance. It recommends Welcome to ServiceNow and ServiceNow Administration Fundamentals.<br>
**Upcoming change:** The canonical blueprint still says updated January 2026; no dated mainline replacement was identified in the accessible sources. The 2026 delta guide is maintenance material, not a replacement CSA blueprint. Existing holders must check their assigned annual delta and CMP payment obligations; no future window or account-specific due date was verified.<br>
**Access note:** The blueprint and product documentation are public. ServiceNow University course, Personal Developer Instance, official MeasureUp practice, registration, and some labs require an account, entitlement, payment, or eligibility. ServiceNow explicitly warns against dumps, mock-test sites, and guaranteed-pass material; use only the official MeasureUp product for exam-style practice.<br>
**Source-access note:** The complete canonical browser main text supports the scope and contract. The automated extractor still receives an empty body and requires manual review. The old snapshot merged several subtopics; its September 7 evidence is archived, and the current snapshot now preserves all 30 separately. Course shells, three blocked resources and no instance access limit this review.<br>
**Independent-source caution:** The linked community checklist is user-authored and predates the January 2026 blueprint. Use it only as a broad hands-on reminder. It has no authoritative weights or contract, and comments that recommend arbitrary flashcards, mock sites, or repeated third-party questions are not endorsed here.

## How to use this guide

Use a Personal Developer Instance (PDI), official training sandbox, or authorized nonproduction instance. Work each objective as a requirement → configuration choice → security effect → user-visible result → transport/rollback evidence. Practice as an end user, fulfiller, and administrator by impersonating authorized test identities, then prove denied paths.

Documentation can default to a different release than your instance or assigned exam preparation. Current direct browser pages show Brazil, updated September 10, 2026, while indexed results still show Australia. The [Developer Passport announcement](https://www.servicenow.com/community/developer-passport-blog/introducing-the-developer-passport-brazil-release-preview/ba-p/3586556) advertises eleven Brazil preview sessions during September 14–18; neither a document selector nor a preview event proves exam cutover or general availability. Record the release used, compare it with the current blueprint/training assignment, and keep release-specific delta material separate from mainline preparation. Never test risky updates, imports, scripts, plugins, or integrations in production.

> **About related items:** A `Related item:` callout adds prerequisite, architecture, security, operations, or lifecycle context. It helps connect the official objective to production practice but does not claim the phrase is part of the ServiceNow blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Platform Overview and Navigation | 7% | Role-based navigation and record-task trace across primary experiences |
| Instance Configuration | 10% | Controlled personalization/configuration and plugin decision with rollback |
| Configuring Applications for Collaboration | 20% | Lists/forms/tasks/boards/report/notification behavior for distinct personas |
| Self Service and Automation | 20% | Governed knowledge, catalog, flow, and Virtual Agent fulfillment path |
| Database Management and Platform Security | 30% | Schema/import/CMDB/access design with least-privilege and data-quality proof |
| Data Migration and Integration | 13% | UI/server logic, scripts and update-set transport with conflict/rollback tests |

## 1. Platform Overview and Navigation — 7%

**CURRENT BLUEPRINT — named subtopics:** ServiceNow Platform overview; Platform capabilities and services; The ServiceNow Instance; Next Experience Unified Navigation.

The Now Platform provides shared data, workflow, security, experience, integration, analytics, and administration capabilities used by applications. Distinguish an instance from the vendor platform, and an application from a module, table, record, workspace, portal, or service. An instance has its own data/configuration and role-based access; development, test, and production separation supports controlled change.

Understand personas: requester/end user, fulfiller/agent, process owner, developer, and administrator. Each reaches work through experiences such as Next Experience Unified Navigation, workspaces, lists/forms, Employee Center or other portals, dashboards, and search. UI visibility is not authorization. A hidden module or field does not protect its records or API.

Navigate using application/module search, favorites/history, breadcrumbs, record references, list filters, and direct record links. Recognize global versus application navigation and the active scope when developing. Know that a record has a table and `sys_id`, while user-friendly numbers/display values serve different purposes.

Use impersonation only with authorization. It is valuable for reproducing persona behavior and access but must be exited deliberately and audited. Favor a test identity over temporarily granting broad roles to a real user.

`Related item:` ServiceNow is a system of record for operational work in many organizations. Seemingly small configuration changes can affect integrations, reports, notifications, SLAs, automation, compliance evidence, and mobile/workspace experiences.

## 2. Instance Configuration — 10%

**CURRENT BLUEPRINT — named subtopics:** Installing applications and plugins; Personalizing/customizing the instance; Common user interfaces in the Platform.

Separate personalization from configuration and customization. Personalization changes an individual experience; configuration changes supported records/settings; customization commonly introduces bespoke behavior. Choose the least complex supported mechanism that meets the requirement, remains secure, transports predictably, and survives upgrades.

Applications and plugins add capabilities. Review licensing/entitlement, dependencies, supported release, activation path, data impact, roles, security, reversibility, and nonproduction validation. Some activations cannot be undone cleanly. Capture baseline, owner, business approval, implementation evidence, and post-activation tests.

Configure system properties and application settings cautiously. Properties can be global, cached, sensitive, or excluded from update sets. Identify the documented default and scope, test effects, and decide whether the value is configuration to transport or environment-specific data to set separately.

Understand common interfaces and experience boundaries: platform UI, workspaces/UI Builder experiences, portals, catalog, mobile, Virtual Agent, and administrative records. A classic-form behavior may not translate automatically to a workspace. Test the actual target experience and role.

`Related item:` Baseline-versus-custom comparison and upgrade-safe design reduce technical debt. Name why a customization exists, its owner, supported alternative, tests, and retirement condition.

## 3. Configuring Applications for Collaboration — 20%

**CURRENT BLUEPRINT — named subtopics:** Lists, Filters, and Tags; List and Form anatomy; Form Configuration; Form templates and saving options; Advanced Form Configuration; Task Management; Visual Task Boards (VTBs); Visualizations, Dashboards, and Platform Analytics; Notifications.

Lists display records from a table. Build filters using field/operator/value conditions, AND/OR logic, dynamic values, and encoded-query awareness. Use breadcrumbs to inspect logic; test empty/missing values and role scope. Configure columns, sort/group, save or share only as allowed, and avoid expensive unbounded queries.

Forms expose fields, related lists, formatters, sections, views, and actions. The dictionary defines field metadata; form configuration/layout and views decide presentation. Templates prepopulate values but do not enforce security or server-side validity. Reference fields store a target identifier while showing a display value.

Tasks commonly inherit from the Task table, sharing core fields and behavior. Understand assignment groups/users, state, activity, work notes/comments, and application-specific extensions without assuming every task table uses identical states. Visual Task Boards present cards driven by data; they do not replace the underlying records or access rules.

Reports/visualizations answer questions from data; dashboards arrange reusable components for audiences. Choose source, aggregation, grouping, time range, and sharing permissions carefully. Validate that viewers cannot infer restricted information through aggregate or drill-down behavior. Platform Analytics capabilities and labels evolve; use the current release docs.

Notifications combine trigger/event/condition, recipients, content/template, and delivery. Avoid duplicate or noisy messages, expose only authorized data, support localization/accessibility where required, and test with outbound mail controls in nonproduction. Know the difference between notification records, events, and automation that causes them.

`Related item:` A useful collaborative experience needs data quality and ownership. A perfect board or dashboard over ambiguous states and assignments only makes poor process more visible.

## 4. Self Service and Automation — 20%

**CURRENT BLUEPRINT — named subtopics:** Knowledge Management; Service Catalog; Workflow Studio; Virtual Agent.

Knowledge Management organizes articles into knowledge bases with ownership, workflow, versioning, categories, user criteria, feedback, and lifecycle. Distinguish who can read, contribute, publish, and retire. Test anonymous/requester/fulfiller access and attachments. Search usefulness depends on clear titles, metadata, currency, and feedback—not article count.

Service Catalog exposes items, record producers, order guides, variables, variable sets, categories, and fulfillment logic. Model the requester’s question, eligibility, inputs, validation, approvals, tasks, notifications, and outcome. Catalog visibility is not permission to access every resulting record. Minimize requested personal data and avoid secrets in variables.

Workflow Studio is the current workflow-building experience; Flow Designer concepts include triggers, actions, flows, subflows, data pills, conditions, and execution details. Select declarative automation when it fits. Design for retries, duplicate triggers, failure paths, timeouts, least-privilege connections, observability, and idempotent external actions.

Virtual Agent provides conversational topics or AI-supported experiences that can answer, gather input, and trigger work. Define audience, channel, authentication, fallback/handoff, knowledge grounding, confirmation for consequential actions, data minimization, transcript retention, accessibility, and success measures. Do not let generated content bypass ACLs or business validation.

`Related item:` Automation correctness includes “what happens twice.” A retried catalog flow must not create duplicate access, purchase, incident, or external transaction.

## 5. Database Management and Platform Security — 30%

**CURRENT BLUEPRINT — named subtopics:** Data Schema; Application/Access Control; Importing Data; CMDB and CSDM; Security Center; Shared Responsibility Model.

ServiceNow tables contain records and fields; tables can extend other tables and inherit fields/behavior. Understand base versus child tables, dictionary entries, reference relationships, choice fields, many-to-many relationships, and schema maps. Design with ownership, query patterns, lifecycle, reporting, security, and upgrade compatibility—not only form appearance.

Import Sets stage external data before transform maps map it into target tables. Data sources define input; transforms, field maps, coalesce, scripts, and run history control processing. Coalesce selects match keys and can update rather than insert; poor keys create duplicates or overwrite the wrong record. Validate types, mandatory/reference values, reject/quarantine behavior, counts, reconciliation, rollback, and sensitive staging-data cleanup.

Users, groups, and roles support authorization. Prefer roles assigned through governed groups. Access Control Lists (ACLs) enforce table/record/field operations through role, condition, and script logic, with evaluation across applicable rules. Test allowed and denied creates/reads/writes/deletes as real personas. Client scripts, UI policies, hidden fields, and modules are not security controls.

Use least privilege and avoid broad `admin` testing as proof. Understand elevated `security_admin` implications, application access/cross-scope controls at an introductory level, impersonation, and why scripted ACLs must be maintainable and efficient. Debug access in nonproduction with appropriate tools and record the rule that granted or denied access.

The CMDB stores configuration items (CIs) and relationships for operational use; CSDM supplies common modeling guidance. Distinguish a CI from an asset, service, application, or arbitrary record. Data quality needs authoritative sources, identification/reconciliation, ownership, completeness/correctness/compliance measures, and remediation. Importing everything does not create a trustworthy CMDB.

Security Center helps assess and improve instance posture, while ServiceNow’s Shared Responsibility Model separates vendor platform responsibilities from customer configuration, identities, data, integrations, devices, and operations. Apply current hardening guidance, review findings by risk/context, test remediation, and keep emergency access and rollback.

`Related item:` Data classification affects schema, ACLs, encryption, audit, retention, import/export, lower-environment cloning, and report sharing. Identify sensitive fields before building workflows around them.

### Import identity and access decisions

The [coalesce reference](https://www.servicenow.com/docs/r/integrate-applications/system-import-sets/c_ImportSetCoalesce.html) distinguishes matching from validation. Multiple coalesce fields must all match. With no match, the normal transform inserts; if the target contains several matches, only the first is updated. Coalesce alone therefore does not prove uniqueness. Default matching is case insensitive; the case-sensitive and empty-field options change matching behavior. Decide how source identifiers, whitespace, case and nulls are handled before loading data. A composite source-plus-external-ID key can prevent two suppliers' identical local IDs from colliding. Quarantine is an explicit policy to design, not an automatic coalesce guarantee.

Use an input ledger: inserted + updated + unchanged + rejected/conflicting/stale rows must equal the received count, with categories defined to be disjoint. Then compare exact identities and business values. Replaying a batch should preserve the intended final state; unchanged row counts alone can hide corruption. The local workbook deliberately rejects stale revisions and changed payloads at the same revision. It does not reproduce ServiceNow's default transform behavior or CMDB reconciliation.

The [ACL overview](https://www.servicenow.com/docs/r/platform-security/access-control/exploring-access-control-list.html) separates object/operation selection, applicability and access conditions. Within an applicable rule, required checks combine; its required-role list can be satisfied by one listed role. [Record access](https://www.servicenow.com/docs/r/platform-security/access-control/acl-rule-types.html) requires both applicable table and field access. Do not combine every ACL on an instance into one global AND, or assume one passing field rule overrides a failed table decision.

**VERIFY CURRENT — ACL edge cases:** [Deny-Unless](https://www.servicenow.com/docs/r/platform-security/access-control/acl-denial-behavior.html) is evaluated before Allow-If, but its current Pass-row prose both requires an explicit Allow-If and describes a default grant when none matches. This unresolved wording is not a reliable universal default-access formula. Empty/invalid ACLs, no matching ACL, wildcard rules, admin overrides and instance security properties are different cases. The workbook tests a deliberately chosen explicit-access policy, not the complete platform engine. Verify the effective decision in an authorized instance.

For a computed function field, protect its contributing fields too. The [current reference](https://www.servicenow.com/docs/r/platform-security/access-control/acl-function-fields.html) documents additional `read` and `report_view` checks; reporting requires qualifying role-only read ACLs without conditions/scripts as well as relevant report access. Its cached Australia and live Brazil versions each use their selected family name in the transition wording, leaving the exact historical introduction unclear. Test the installed release; do not infer that changing a dashboard's sharing setting grants access to underlying sensitive values.

## 6. Data Migration and Integration — 13%

**CURRENT BLUEPRINT — named subtopics:** UI Policies; Business Rules; System update sets; Scripting in ServiceNow.

UI Policies manage client-visible field behavior such as mandatory, visible, or read-only conditions; client scripts handle supported client-side logic. Business Rules execute server-side around database operations. Select the correct layer: client convenience is not server enforcement, and duplicating logic across both can cause inconsistent behavior.

Understand Business Rule timing—before, after, asynchronous, and display—conceptually. Guard conditions and changed-field checks prevent unnecessary work or recursion. Avoid broad queries in loops. Prefer documented APIs, scoped logic, and reusable Script Includes where appropriate. JavaScript knowledge matters, but platform execution context and APIs determine what is safe.

System update sets capture many configuration changes for movement between instances; they are not full backups and do not capture ordinary transactional data or every configuration class. Use one application scope, clear naming, parent/child strategy if needed, complete sets, retrieve/preview, resolve collisions, commit in dependency order, test, and document backout. Never treat a clean preview as complete regression proof.

Integrations include import/export and web-service or IntegrationHub paths beyond the listed fundamentals. Protect credentials/connections, validate payloads, authenticate/authorize, handle pagination/rate limits/retries, make writes idempotent, monitor failures, and reconcile results. Environment-specific endpoints and secrets should not ride casually in transported configuration.

`Related item:` Automated Test Framework and peer review provide repeatable regression evidence for configuration transport. Tests should cover persona permissions and negative paths, not only an administrator happy path.

### Logic and transport evidence

The [Business Rule reference](https://www.servicenow.com/docs/r/api-reference/business-rules-classic/c_BusinessRules.html) recommends Workflow Studio for new process automation while retaining Business Rules as a CSA topic. A before rule can adjust the current record before its save; calling `current.update()` again can recurse. After rules suit related-object work. Async execution order is not guaranteed, and its script lacks `previous`; change-detection support in the condition builder is a separate detail. The documentation also describes paths that bypass Business Rules, including `setWorkflow(false)`. Server-side logic is therefore not proof that every writer ran it, nor that a script automatically honors ACLs.

[Tracked customizations](https://www.servicenow.com/docs/r/application-development/system-update-sets/customizations-tracked-update-sets.html?contentId=Wesk3KW7yiI5hKC5y~QwUA) include catalog definitions, not submitted orders. Inspect the actual customer updates and dependencies; do not add `update_synch` to force ordinary data into a set. The documentation warns that preview can miss destructive type mismatches, and deleting a column can lose its data. A clean preview is not a recoverability test.

[Planning guidance](https://www.servicenow.com/docs/r/application-development/system-update-sets/get-started-update-sets.html) favors a consistent development → test → production route and small changes. [Working with update sets](https://www.servicenow.com/docs/r/application-development/system-update-sets/using-system-update-sets.html?contentId=Eqec25Xl1X9Pc0s3ZCiPDw) explicitly advises against editing the Update Set reference on a Customer Update record. Re-capture the intended object through the documented process. Keep completed sets immutable in your change procedure and use a subsequent set for fixes.

[Collision resolution](https://www.servicenow.com/docs/r/application-development/system-update-sets/update-set-collisions.html) compares customer-update identity and update time, with special coalescing for particular record types. Its table includes role definitions and groups; the delta guide's broad statement that users/groups/roles are not metadata must not become a universal exclusion rule. This does not prove all memberships or group changes are captured automatically. Inspect the class, actual payload and missing-data runbook. Separately recreating equivalent objects can produce different identifiers and evade collision detection.

Choose either a configured remote retrieval path or a documented [XML export/import path](https://www.servicenow.com/docs/r/application-development/system-update-sets/t_SaveAnUpdateSetAsAnXMLFile.html). Imported XML appears as a retrieved set; importing and committing are distinct actions. For [batches](https://www.servicenow.com/docs/r/application-development/system-update-sets/us-hier-overview.html), the base coordinates the hierarchy. The clone-preparation guidance says to mark only the parent Ignore and leave other sets Complete, a qualification to blanket Ignore advice. No account, privilege elevation, import or commit was performed for this review.

## Integrated scenarios

### Scenario 1: Employee equipment request

**Given:** A requester can order approved equipment, a fulfiller can work assigned tasks, and an auditor can see approved audit data. Supplier cost is restricted. A retry occurs after a downstream operation completed but before its acknowledgment arrived.

**Work the decision:** Use catalog eligibility and variables for the user journey, server checks for valid business input, and effective ACLs for the sensitive record and cost field. An approval must bind to the actual request/version; changed quantity or equipment needs the defined reapproval path. Give the downstream operation a stable business key and preserve its durable receipt. On retry, reconcile that receipt before repeating a purchase. A dashboard or Virtual Agent response must not disclose the restricted cost through a derived value.

**Evidence:** Trace requester → request → approval → task → outcome. Test an eligible requester, an ineligible user, a fulfiller outside assignment, and a report viewer without cost access. Capture duplicate-trigger and changed-payload decisions, a failed fulfillment/handoff path and cleanup. No purchase, external notification or instance execution occurred here.

### Scenario 2: Vendor data import

**Given:** Vendor A and Vendor B both use external asset ID `42`. Eight fixture rows include a duplicate, a blank ID, a changed payload at the same revision, an older update, a valid newer update and a Boolean masquerading as an integer revision.

**Worked result:** The workbook uses `(source, external_id)`, producing two inserts, one update, one unchanged row, two quarantines, one conflict and one stale row: eight accounted for. A ends at revision 2/North, B at revision 1/East. Replaying all eight rows makes zero inserts or updates and preserves the exact records. Matching only `42` would collapse two identities. This chosen revision policy rejects rather than silently overwrites; the ServiceNow transform must be designed and tested separately.

**Evidence to obtain in an instance:** Preflight existing duplicate target keys, case/empty matching settings, reference validity, transform outcomes and exact target records. Separate CMDB identification/reconciliation and asset processes from this synthetic asset table. Retain enough evidence to undo the specific run without removing later legitimate changes, then clean sensitive staging data under the retention policy.

### Scenario 3: Change promotion incident

**Given:** A form, role, field ACL and flow travel together. The form works as admin but the fulfiller fails. A later target-side repair exists before someone proposes backout.

**Worked decision:** Verify schema and role before the dependent ACL and flow, then test the fulfiller's effective table and field permissions. The workbook rejects an omitted dependency, duplicate step and cycle. Its illustrative expected-revision guard moves revision 4 to 5, rejects replay, accepts a later fix at revision 6, and refuses a backout still expecting 5. Blindly restoring the saved value would erase that fix. This is original change-control reasoning, not ServiceNow's collision algorithm.

**Evidence:** Compare actual update payloads, preview findings, excluded data and environment configuration; record the accepted collision resolution. Test both UI and server paths and inspect processing exceptions. Rehearse a specific backout or fix-forward plan in nonproduction, including data restoration when needed. Keep outbound delivery disabled while inspecting notification conditions and recipients.

## Hands-on evidence labs

These eight activities are **proposed**, not executed in ServiceNow. Record instance family, application scope, synthetic records, persona, expected and observed result, relevant configuration/logs and cleanup. Use an authorized nonproduction instance and existing approved access.

1. **Navigation and personas:** Trace one task from a list to its form, reference and related record. Compare requester/fulfiller/admin navigation and permitted operations. Prove that a direct link cannot turn an unauthorized operation into an authorized one. End impersonation and remove test records.
2. **Instance configuration:** Compare a personal list preference with a shared form change. Identify the records changed, scope and capture behavior. Produce a plugin dependency/entitlement/reversibility decision using documentation; activation is optional and requires the environment's normal approval. Restore the shared baseline.
3. **Collaboration:** Use synthetic tasks to verify an AND/OR filter with an empty value, form template, assignment, board and dashboard drill-down. Include a viewer who cannot read a restricted field. Inspect notification trigger, recipient and content evidence with delivery disabled; do not send mail merely to finish the activity.
4. **Self service:** Sketch knowledge lifecycle, catalog eligibility, approval, fulfillment and Virtual Agent handoff. In a permitted sandbox, exercise duplicate trigger, invalid input and failed action paths. Reconcile the durable business result instead of treating a green flow step as the only evidence.
5. **Schema and security:** Draw table inheritance and references, identify sensitive fields and map role/group ownership. Test create/read/write/delete with non-admin identities, including a table-allowed/field-denied case and computed/report exposure. Record actual rule decisions; do not broaden roles to force a pass.
6. **Import and CMDB:** Preflight target uniqueness, source-qualified keys, empty/case behavior, invalid references and duplicate rows. Run a small permitted transform twice, account for every row and compare exact target values. State which results are custom-table behavior and which need CMDB identification/reconciliation. Rehearse scoped rollback and staging cleanup.
7. **Logic boundaries:** Explain why a hidden or mandatory field is insufficient for server validation. Trace a before rule, related-record after action and asynchronous path in the available release. Test an invalid write through an authorized alternate interface, recursion protection, failure and stale revision. Inspect bypass/context assumptions without disabling workflow or security controls.
8. **Promotion:** Assemble a small same-scope change with a dependency inventory and excluded-data runbook. Preview the retrieved set or batch, resolve collisions explicitly, test allowed/denied personas, and rehearse restoration without overwriting later changes. Capture warnings about schema/data loss; restore the sandbox and preserve the evidence.

### Executed local workbook

**PRACTICAL DEPTH:** Run the following with Python 3 and its standard library. It uses an in-memory SQLite table and trusted fixture labels. All 34 checks passed during this review. It does not connect to ServiceNow, authenticate users, execute ACLs or Business Rules, parse update-set XML, perform CMDB reconciliation or deliver notifications. The import policy preserves external-ID case deliberately, unlike default case-insensitive coalesce. It models sequential inputs, not concurrent/distributed writes; real integrations need transactional uniqueness, concurrency and durable receipt designs.

```python
import collections
import copy
import json
import sqlite3

checks = []


def check(name, actual, expected):
    if actual != expected:
        raise AssertionError((name, actual, expected))
    checks.append(name)


# Original import policy: source names normalize; external IDs retain case.
# This is SQLite execution, not ServiceNow coalesce or a CMDB transform.
db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE asset (source TEXT, external_id TEXT, revision INTEGER, '
           'location TEXT, PRIMARY KEY (source, external_id))')


def accept(row):
    source, external_id, revision, location = row
    source, external_id = source.strip().casefold(), external_id.strip()
    if (source not in {'vendora', 'vendorb'} or not external_id
            or type(revision) is not int or revision < 0 or not location.strip()):
        return 'quarantine'
    location = location.strip()
    with db:
        old = db.execute('SELECT revision, location FROM asset WHERE source=? '
                         'AND external_id=?', (source, external_id)).fetchone()
        if old:
            if revision < old[0]:
                return 'stale'
            if revision == old[0]:
                return 'noop' if location == old[1] else 'conflict'
            db.execute('UPDATE asset SET revision=?, location=? '
                       'WHERE source=? AND external_id=?',
                       (revision, location, source, external_id))
            return 'updated'
        db.execute('INSERT INTO asset VALUES (?,?,?,?)',
                   (source, external_id, revision, location))
        return 'inserted'


def state():
    return db.execute('SELECT * FROM asset ORDER BY source, external_id').fetchall()


rows = [(' VendorA ', '42', 1, 'West'), ('vendorB', '42', 1, 'East'),
        ('vendora', '42', 1, 'West'), ('vendora', '', 1, 'West'),
        ('vendora', '42', 1, 'North'), ('vendora', '42', 0, 'Old'),
        ('vendora', '42', 2, 'North'), ('vendora', '99', True, 'South')]
outcomes = collections.Counter(accept(row) for row in rows)
check('all input rows accounted for', sum(outcomes.values()), 8)
check('first-run outcomes', dict(outcomes),
      dict(inserted=2, noop=1, quarantine=2, conflict=1, stale=1, updated=1))
check('source-qualified identity', len(state()), 2)
check('exact final records', state(),
      [('vendora', '42', 2, 'North'), ('vendorb', '42', 1, 'East')])
before = state()
replay = collections.Counter(accept(row) for row in rows)
check('replay has no mutations', replay['inserted'] + replay['updated'], 0)
check('replay retains exact state', state(), before)
check('unknown source quarantined', accept(('other', '42', 4, 'West')), 'quarantine')
check('blank location quarantined', accept(('vendora', '42', 3, ' ')), 'quarantine')
check('same revision changed payload conflicts',
      accept(('vendora', '42', 2, 'East')), 'conflict')
check('rejections leave state intact', state(), before)
check('SQLite integrity', db.execute('PRAGMA integrity_check').fetchone(), ('ok',))
check('ID alone would collapse sources', len({r[1] for r in state()}), 1)


# Trusted fixture labels and a chosen policy, not the ServiceNow ACL engine.
def may_read(roles, active, authenticated, same_region, field_allowed):
    required = bool(set(roles) & {'fulfiller', 'auditor'})
    return required and active and authenticated and same_region and field_allowed


check('fulfiller allowed', may_read({'fulfiller'}, True, True, True, True), True)
check('alternative role allowed', may_read({'auditor'}, True, True, True, True), True)
check('role alone insufficient', may_read({'fulfiller'}, False, True, True, True), False)
check('authentication required', may_read({'fulfiller'}, True, False, True, True), False)
check('record scope required', may_read({'fulfiller'}, True, True, False, True), False)
check('field restriction survives row access',
      may_read({'fulfiller'}, True, True, True, False), False)
check('missing explicit role denied by chosen policy',
      may_read(set(), True, True, True, True), False)
check('derived output requires all contributing permissions', all([True, False]), False)


# A deployment packet has explicit dependencies and an expected base revision.
# This is not an update-set XML parser or a ServiceNow collision simulator.
def ordered(names, dependencies):
    done = set()
    for name in names:
        if name in done or not dependencies[name] <= done:
            return False
        done.add(name)
    return done == set(dependencies)


deps = {'schema': set(), 'role': set(), 'acl': {'schema', 'role'},
        'form': {'schema'}, 'flow': {'schema', 'acl'}}
check('complete dependency order', ordered(['schema', 'role', 'acl', 'form', 'flow'], deps), True)
check('missing dependency rejected', ordered(['schema', 'acl', 'form', 'flow'], deps), False)
check('incomplete packet rejected', ordered(['schema', 'role', 'acl', 'form'], deps), False)
check('duplicate step rejected', ordered(['schema', 'role', 'acl', 'form', 'flow', 'flow'], deps), False)
cyclic = {'schema': {'acl'}, 'acl': {'schema'}}
check('cyclic dependency rejected', ordered(['schema', 'acl'], cyclic), False)
target = {'revision': 4, 'value': 'old'}
packet = {'expected': 4, 'value': 'new'}
backup = copy.deepcopy(target)


def deploy(current, change):
    if current['revision'] != change['expected']:
        return False
    current.update(revision=current['revision'] + 1, value=change['value'])
    return True


check('expected revision applies', deploy(target, packet), True)
check('stale packet rejected', deploy(target, packet), False)
check('post-deployment edit applies', deploy(target, {'expected': 5, 'value': 'later-fix'}), True)
check('blind backout would lose later fix', backup['value'] != target['value'], True)
check('guarded backout rejects later state',
      deploy(target, {'expected': 5, 'value': backup['value']}), False)
check('later fix preserved', target, {'revision': 6, 'value': 'later-fix'})

bank_counts = [6, 12, 26, 23, 33, 20]
blueprint_weights = [7, 10, 20, 20, 30, 13]
check('practice-bank total', sum(bank_counts), 120)
check('blueprint weights total', sum(blueprint_weights), 100)
check('bank distribution differs from blueprint',
      [n * 100 for n in bank_counts] == [w * 120 for w in blueprint_weights], False)
db.close()
print(json.dumps({'passed': len(checks), 'checks': checks, 'first_run': dict(outcomes),
                  'replay': dict(replay), 'final_records': before,
                  'deployment': target, 'practice_bank_total': sum(bank_counts)}, indent=2))
```

Expected output reports `passed: 34`, eight accounted-for initial rows, zero replay mutations, two source-qualified records and preserved deployment revision 6. The final catalog comparison checks distribution only; it computes no exam score or pass threshold.

## Readiness checks

These are original explanation prompts, not reconstructed exam items. Answer aloud, then compare the reasoning and produce the related evidence.

1. **Can I distinguish platform, instance, application, module, table, and record?**

   The platform supplies shared capabilities; an instance is a configured environment. Applications organize capabilities, modules expose navigation, tables define record types and records hold individual entries.

2. **Can I map requester, fulfiller, developer, owner, and admin experiences?**

   Begin with what each persona must accomplish and the data/actions needed. A requester submits, a fulfiller works tasks, an owner governs outcomes, a developer builds and an administrator configures; actual permissions still need evidence.

3. **Can I navigate lists/forms/references without confusing display values and `sys_id`?**

   Follow table and record identity through references. A display value or human-readable number helps users, but can change or duplicate; it is not a substitute for the referenced identifier.

4. **Can I explain why UI visibility is not authorization?**

   Hiding navigation changes the experience. Server authorization must still reject an unauthorized record or operation through other supported entry points.

5. **Can I distinguish personalization, configuration, and customization?**

   A personal preference affects one experience; supported configuration changes shared behavior; bespoke customization adds maintenance obligations. Identify the stored change and affected audience before promotion.

6. **Can I assess plugin entitlement, dependency, security, data, and reversibility?**

   Read the activation requirements and dependencies, then record licensing, scope, data/role effects and a realistic reversal plan. A successful activation is not evidence of safe business behavior.

7. **Can I identify environment-specific properties and transport decisions?**

   List each property or connection with its owner and environment value. Decide what can be transported and what must be supplied separately; secrets and target endpoints need deliberate handling.

8. **Can I test the target workspace/portal rather than assume classic-UI behavior?**

   Run the task in the actual target experience as the intended user. A classic-form script or layout observation does not prove equivalent portal, workspace or mobile behavior.

9. **Can I build and read filters with correct AND/OR and empty-value behavior?**

   Use a truth table with included and excluded examples, including missing values. Check the grouping of AND/OR clauses and confirm the displayed result set for the intended persona.

10. **Can I distinguish dictionary, form layout/configuration, view, and template?**

   The dictionary describes field metadata. Form layout and views control presentation; templates supply initial values. None of those alone establishes effective record authorization.

11. **Can I explain Task inheritance without assuming identical child behavior?**

   Child task tables can inherit shared fields and logic while adding their own behavior. Inspect the actual child state model, assignment and automation instead of copying another task type.

12. **Can I secure reports, dashboards, boards, and drill-downs for their audience?**

   Check underlying row/field access, report operations, computed contributors and drill-down. Sharing a dashboard container is insufficient proof that its content is suitable for the viewer.

13. **Can I design a notification trigger, recipients, content, and duplicate controls?**

   Define the event/condition, intended recipients, permissible fields and duplicate policy. Inspect generated evidence with delivery disabled until a separate authorized delivery test is needed.

14. **Can I govern knowledge read/contribute/publish/retire lifecycle?**

   Name owners, audience, contribution rights, review/publishing controls and retirement criteria. Test that draft or expired content does not leak through search or conversational channels.

15. **Can I choose catalog item, record producer, order guide, and variables appropriately?**

   Choose a catalog item for a requested service/product, a record producer for guided target-record creation, or an order guide for related requests. Variables collect input; server-side processing must still validate it.

16. **Can I map request eligibility, approvals, tasks, outcomes, and failures?**

   Draw eligibility → input → approval → fulfillment → business result, with failure and cancellation branches. Bind approval to the version of the request that is actually fulfilled.

17. **Can I explain trigger, action, flow, subflow, data pill, and execution details?**

   A trigger starts work, actions perform steps, subflows package reusable work and data pills pass context. Inspect execution detail and durable business state to diagnose an apparent success or failure.

18. **Can I design automation for retry, idempotency, timeout, and least privilege?**

   Use stable operation identity, validate repeated payloads and retain receipts. Define timeout, retry and reconciliation paths so an uncertain acknowledgment does not create duplicate business effects.

19. **Can I bound Virtual Agent access, confirmation, handoff, and transcript data?**

   Apply audience and data access rules, confirm consequential actions and provide a human handoff. Bound transcripts and grounding data under the same privacy and retention rules as the underlying process.

20. **Can I distinguish table extension, reference, choice, and many-to-many modeling?**

   Extension represents inherited table behavior; references link records; choices constrain values; a relationship table models many-to-many links. Select based on lifecycle and query needs, not just form convenience.

21. **Can I explain authoritative ownership and lifecycle for a custom table?**

   Identify the system of authority, steward, permitted writers, identifier, retention and recovery requirements. Reconcile changes from secondary sources instead of assuming the newest arrival is authoritative.

22. **Can I stage, transform, coalesce, validate, and reconcile an import?**

   Stage source data, validate it, apply a deliberate match/mapping policy, and reconcile disjoint outcomes and exact target records. Preserve evidence for a scoped reversal and repeat-run check.

23. **Can I explain how a poor coalesce key damages data?**

   A nonunique key can update the first matching target; a missing or inconsistent key can insert duplicates. Source-qualified identity, preflight uniqueness and explicit empty/case policies reduce these risks.

24. **Can I manage users, groups, and roles without uncontrolled direct grants?**

   Prefer governed group-based assignments with an owner and removal process. Record direct exceptions and expiration rather than accumulating permanent broad permissions for troubleshooting.

25. **Can I reason through table/record/field ACL evaluation?**

   Identify the operation and applicable record/table/field rules, then inspect required roles and other conditions. Table and field access both matter; Deny-Unless and default-access edge cases need the installed engine, not a universal shortcut.

26. **Can I prove both allowed and denied operations with non-admin personas?**

   For each operation, pair an allowed persona with a near-miss denied persona and preserve the actual decision. Admin success can mask missing dependencies or excessive privileges.

27. **Can I explain why UI Policy/client script/module hiding cannot secure data?**

   Those mechanisms guide interaction in specific interfaces. A server request may omit the UI entirely; ACLs and appropriate server validation must protect the data and action.

28. **Can I distinguish CI, asset, service, application, and ordinary record?**

   A CI represents an operational configuration item; an asset has financial/lifecycle tracking; services and applications provide different modeling context. Do not put every imported row into the CMDB by default.

29. **Can I define CMDB authority, identification/reconciliation, quality, and ownership?**

   Define authoritative sources, stable identification, reconciliation priorities, ownership and measurable data quality. Test duplicate, stale and conflicting inputs before expanding ingestion.

30. **Can I apply Shared Responsibility to an instance-security scenario?**

   Separate the vendor-operated service from customer-managed identities, configuration, data, integrations and use. Assign each relevant control and recovery task to an accountable owner.

31. **Can I interpret Security Center findings without blindly changing production?**

   Understand the finding, affected scope, prerequisite and business impact. Test remediation in nonproduction and preserve the decision and rollback evidence; a posture score alone is not a production acceptance test.

32. **Can I choose UI Policy, client script, Business Rule, flow, or ACL by context?**

   Use UI mechanisms for interaction, ACLs for authorization, server logic for required data behavior and workflow tools for process orchestration. Verify execution context and alternate entry points.

33. **Can I explain Business Rule timing and avoid recursion/expensive loops?**

   Before logic can change the current record within its save; after logic suits related work; async order is not guaranteed. Avoid current.update recursion, broad queries and assumptions that previous is available in async scripts.

34. **Can I identify what update sets do and do not capture?**

   Update sets carry selected configuration, not a full instance/data backup. Inspect tracked classes and actual payload; role definitions, memberships, environment data and schema changes require individual decisions.

35. **Can I preview, resolve collisions, order dependencies, commit, test, and back out?**

   Resolve dependencies and preview findings, then test the changed behavior and denied paths after commit. Backout must account for later target changes and lost data; sometimes a reviewed fix-forward is safer.

36. **Can I protect integration identities, secrets, retries, and reconciliation?**

   Use scoped identities and managed connections, validate input, and record durable operation IDs/results. Handle partial pages, retries and uncertain outcomes with reconciliation rather than blind repetition.

37. **Can I keep mainline study separate from a release-specific delta guide?**

   The mainline blueprint defines CSA study scope. The 2026 delta guide concerns maintenance; a product family selector or developer preview does not establish an exam transition.

38. **Can I state the current 60-question/90-minute Pearson contract?**

   The current blueprint lists 60 multiple-choice/multiple-select questions and 90 minutes, with Pearson test-center or OnVUE delivery. Recheck the actual booking and delivery requirements before payment.

39. **Can I explain conditional results, undisclosed cut score, and 90-day registration window?**

   Registration starts a 90-day schedule-and-complete window. Results can be audited; the cut score is undisclosed and not universally 70%. Section percentages and practice scores cannot calculate a guaranteed passing result.

40. **Can I explain annual deltas and the CMP fee without calling the credential lifetime-static?**

   Mainline holders must follow assigned annual deltas and CMP obligations. Check the account-specific window and fee rules; neither a past public date nor completing a course establishes current maintenance compliance.

## Final preparation

- Reopen KB0011554 and verify its update date, domains, Pearson contract, registration window, cut-score statement and maintenance terms.
- Study the recommended official courses and redo their labs in a clean authorized instance where access permits.
- Use only ServiceNow’s official MeasureUp practice for exam-style questions; turn each miss into a blueprint/doc/lab task.
- Rebuild one scenario with non-admin allowed and denied tests, controlled transport, and rollback evidence.
- Verify the current release context and do not blend an old course, mainline blueprint, and delta guide.
- Treat certification as a checkpoint; production configuration still requires peer review, security, testing, change control and recovery.


## Places to learn

This is not a complete list. Choose resources to close demonstrated gaps, and keep account-only lessons and practice questions distinct from publicly reviewed metadata. Times below are planning estimates unless a publisher-listed historical value is explicitly identified. No course, exam booking, PDI enrollment, paid lesson or practice-question interior was accessed.

| Use and reading boundary | Resource | Access | Estimated time |
|---|---|---|---:|
| Canonical 30 subtopics and contract; full browser main text reviewed | [Certified System Administrator Mainline Exam Blueprint](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011554) | Public; automated empty body | 20–30 min estimate |
| Correct recommended Welcome link; current course body/duration unavailable | [Welcome to ServiceNow — current recommended course](https://learning.servicenow.com/lxp/en/now-platform/welcome-to-servicenow?course_id=386f3cf847b36a90c00af235126d430c&id=learning_course_prev) | Account/loading shell | Earlier about 3 hr not reverified |
| Recommended Fundamentals course; current lesson duration unavailable | [ServiceNow Administration Fundamentals](https://learning.servicenow.com/lxp?course_id=fbb6cc4847f5dd505cbdaf44846d436a&id=learning_course_prev) | Account/entitlement | Earlier 3 ILT days not reverified |
| Earlier Welcome citation is actually a CSA certification-path route | [ServiceNow CSA certification path — earlier mislabelled Welcome link](https://learning.servicenow.com/lxp/en/now-platform/certified-system-administrator?course_id=931d939697d229587f7070871153af8c&id=learning_content_prev) | Account/loading shell | Not verified |
| Credential navigation; no course interiors | [ServiceNow University Credential Catalog](https://learning.servicenow.com/lxp/en/credentials) | Public shell/account | 10–20 min estimate |
| Select your instance family; homepage is not a full documentation audit | [ServiceNow Product Documentation](https://www.servicenow.com/docs/) | Public shell/browser docs | 10–20 hr selected study estimate |
| PDI and learning entry; no instance obtained | [ServiceNow Developer Program](https://developer.servicenow.com/) | Public entry/account | 1–2 hr setup estimate, availability unverified |
| February 2026 product metadata: 120 questions; no demo/question interiors | [ServiceNow CSA Practice Test](https://www.measureup.com/servicenow-csa-practice-test.html) | Paid; demo advertised, not opened | 2–4 hr study estimate |
| Maintenance guide focused on update sets; qualify capture and batch guidance | [Certified System Administrator Maintenance Exam (Delta) 2026 Study Guide](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0012121) | Public browser main | 30–60 min estimate |
| Scheduling/provider transition; 48-hour center reschedule versus OnVUE until start | [Pearson VUE transition and scheduling FAQ](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0013209) | Public browser main | 15–25 min estimate |
| Annual payment details; public dates do not establish your assigned window | [Certification Maintenance Program payment FAQ](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011114) | Public browser main | 10–20 min estimate |
| Official completion route remained unreadable; verify assigned account tasks | [Completing a mainline certification delta exam](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011292) | Empty body/browser error | Not verified |
| Earlier course-sequencing infographic; current PDF request blocked | [ServiceNow Learning Paths](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/infographic/learning-paths.pdf) | HTTP 403 | Earlier 15–30 min estimate; not reread |
| Paid syllabus/interior unavailable; earlier May 2026 metadata not reverified | [ServiceNow System Administrator Total Exam Prep](https://www.udemy.com/course/ndn-csa-exam-prep/) | Paid/HTTP 403 | Earlier 8 hr 17 min unverified |
| Career context; paid interior and earlier 2025 metadata not reverified | [Navigating Your Career in ServiceNow](https://www.oreilly.com/library/view/navigating-your-career/9798868818714/) | Paid/HTTP 403 | Earlier 2 hr 30 min unverified |
| Official channel landing only; no playback or playlist-quality judgment | [ServiceNow Developers YouTube Channel](https://www.youtube.com/@servicenowdevprogram) | Public video platform | 2–6 hr selected study estimate |
| Tosin D July 2025 checklist; main and first comments only, no attachment | [CSA Certification Study Guide: How to Prepare](https://www.servicenow.com/community/training-and-certifications/csa-certification-study-guide-how-to-prepare/ta-p/3319050) | Public/user-authored | 20–30 min estimate |
| ACL conditions, applicability and scope; main body reviewed, generated summary excluded | [Access control rules overview](https://www.servicenow.com/docs/r/platform-security/access-control/exploring-access-control-list.html) | Public/browser | 30–60 min with exercises |
| Record/table/field evaluation selected section; not every operation audited | [ACL rule types and record/field evaluation](https://www.servicenow.com/docs/r/platform-security/access-control/acl-rule-types.html) | Public/browser | 20–40 min estimate |
| Priority and contradictory default-access wording; live test still required | [Deny-Unless ACL behavior](https://www.servicenow.com/docs/r/platform-security/access-control/acl-denial-behavior.html) | Public/browser | 15–30 min estimate |
| Computed contributors and report access; exact historical transition unclear | [ACLs on function fields](https://www.servicenow.com/docs/r/platform-security/access-control/acl-function-fields.html) | Public/browser | 20–40 min estimate |
| Timing, recursion, bypass/context and Workflow Studio guidance; main body reviewed | [Classic Business Rules](https://www.servicenow.com/docs/r/api-reference/business-rules-classic/c_BusinessRules.html) | Public/browser | 30–60 min estimate |
| Matching, duplicates, empty/case options; indexed primary body reviewed | [Updating records using coalesce](https://www.servicenow.com/docs/r/integrate-applications/system-import-sets/c_ImportSetCoalesce.html) | Public/indexed body | 30–60 min estimate |
| Current short planning guidelines; stable page changed from earlier longer guidance | [Get started with update sets](https://www.servicenow.com/docs/r/application-development/system-update-sets/get-started-update-sets.html) | Public/browser | 15–30 min estimate |
| Batch ancestry and parent-only Ignore qualification | [Working with batched update sets](https://www.servicenow.com/docs/r/application-development/system-update-sets/us-hier-overview.html) | Public/browser | 15–30 min estimate |
| Identity/date comparisons and special coalescing; main body reviewed | [Update set collision resolution](https://www.servicenow.com/docs/r/application-development/system-update-sets/update-set-collisions.html) | Public/browser | 30–45 min estimate |
| Local XML export/import path; no elevation or execution | [Save an update set as a local XML file](https://www.servicenow.com/docs/r/application-development/system-update-sets/t_SaveAnUpdateSetAsAnXMLFile.html) | Public/browser | 15–30 min estimate |
| Capture limits, special handlers and destructive schema caveats | [Customizations tracked by update sets](https://www.servicenow.com/docs/r/application-development/system-update-sets/customizations-tracked-update-sets.html?contentId=Wesk3KW7yiI5hKC5y~QwUA) | Public/browser | 30–45 min estimate |
| Re-capture a wrongly assigned change; do not edit Customer Update reference | [Working with update sets](https://www.servicenow.com/docs/r/application-development/system-update-sets/using-system-update-sets.html?contentId=Eqec25Xl1X9Pc0s3ZCiPDw) | Public/browser | 15–30 min estimate |
| August 13 announcement of eleven September 14–18 preview sessions; no playback | [Developer Passport Brazil release preview](https://www.servicenow.com/community/developer-passport-blog/introducing-the-developer-passport-brazil-release-preview/ba-p/3586556) | Public/vendor program blog | 15–25 min article estimate; video lengths unverified |

The public MeasureUp domain counts are 6/12/26/23/33/20, totaling 120; their proportions differ from the blueprint's 7/10/20/20/30/13 weights. The same product page has generic wording about roughly 150 questions. Use the specific 120-question listing as observed metadata, and verify the purchased version. Its advertised translations are not official exam languages, and its readiness percentages or guarantee are not ServiceNow's cut score. No question quality or coverage completeness is inferred from these counts.

The English CMP payment page lists January 15–April 15, 2026, while other public-language/community references differ by a day. This review does not settle the exact assigned delta deadline or publish a future window. Follow the current task and payment information shown for your credential, and use the official support path if it conflicts.
