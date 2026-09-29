---
exam_code: SALESFORCE-PLATFORM-ADMINISTRATOR
vendor_id: salesforce
official_blueprint: https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-setup-and-objects/get-started-with-administrator-certification-prep
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Salesforce Certified Platform Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 29, 2026 [deep review](../docs/research/2026-09-29-salesforce-platform-administrator-deep-review.md) maps all eight monitored domains and adds 30 executed local checks. Salesforce org activities remain proposed.

**CURRENT BLUEPRINT:** The [canonical prep unit](https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-setup-and-objects/get-started-with-administrator-certification-prep) retains the eight weights below. The [Salesforce Admins announcement](https://admin.salesforce.com/blog/2026/what-the-salesforce-certified-platform-administrator-exam-update-means-for-admins) dates the refresh to December 15, 2025. Neither the objective snapshot nor the annual-maintenance snapshot changed.

**VERIFY CURRENT — source discrepancy:** The [Help exam guide](https://help.salesforce.com/s/articleView?id=005298966&type=1&language=en_US) still labels the exam Summer ’25 while including the refreshed domains. Direct retrieval returned a loading shell; its English article was readable through the [Korean-locale route](https://help.salesforce.com/s/articleView?id=005298966&language=ko&type=1). It lists 60 multiple-choice questions plus up to five unscored, 105 minutes, English/Japanese passing scores of 68%/65%, and no prerequisite. Six months of experience is a recommendation. Fees shown are USD 200 for an attempt and USD 100 for a retake, plus tax. Verify the actual booking terms; the [Academy exam listing](https://trailheadacademy.salesforce.com/certificate/exam-platform-admin---Plat-Admn-201) exposed no readable details in this review.

**Upcoming change:** No later blueprint or retirement announcement was found in the checked certification, prep, and update sources on September 29. Product release notes are separate from exam-scope announcements; the API 68 Flow change below does not prove a new exam version or availability in every org.

**Maintenance:** Complete the certification-specific Trailhead maintenance badge annually by its deadline. The official guidance says missed requirements cause expiration; consult your credential record for its actual due date.

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

User lifecycle is more than creating a user. Map identity → user license → profile baseline → permission sets and groups → role/territory/reporting position → queues/public groups/teams → login and session controls. Usernames must be unique. Freeze can stop login quickly; deactivation releases some access but has ownership and automation implications; users are not deleted. Prefer minimum profiles plus additive permission sets, and test effective access as the intended persona.

Separate the layers of the sharing model:

- organization-wide defaults establish the restrictive baseline;
- role hierarchy can open upward visibility for many objects;
- sharing rules expand access to defined groups or roles;
- teams, queues, territories, manual sharing, and programmatic sharing solve narrower cases;
- object CRUD and field-level security still constrain what record sharing can expose.

Security controls include MFA and identity verification, login hours/IP ranges, password/session policy, delegated administration, Setup Audit Trail, login history, and connected-app/session review. Diagnose access with a layer-by-layer trace; do not compensate for a missing object permission by making all records public.

`Related item:` Licenses bound the capabilities that permission sets can grant. “Permission assigned” does not prove “feature licensed,” and a UI element being visible does not prove record or field access.

**PRACTICAL DEPTH — effective grants:** Salesforce recommends task-focused [permission sets and persona groups](https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_objects). A [muting permission set](https://trailhead.salesforce.com/content/learn/modules/permission-set-groups/mute-permissions-in-permission-set-groups) limits its own group: the same permission from a profile, direct assignment, or another group remains effective. Muting can also affect dependent permissions. Trace every grant and review recalculated effective access before declaring a restriction successful.

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

**PRACTICAL DEPTH — results and transactions:** An [external-ID upsert](https://developer.salesforce.com/docs/platform/api-rest/guide/resources-sobject-upsert.html) can create or update. Matching policy and key quality therefore matter before a retry. The [sObject Collections API](https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-sobjects-collections-upsert.html) accepts up to 200 records of one type, returns ordered per-record results, and defaults `allOrNone` to false. A well-formed request can return HTTP 200 with item failures. Inspect each result and reconcile persisted data; do not apply these particular request limits or transaction options to every import tool. Replaying the same values also does not prove that triggered side effects are idempotent.

## 7. Automation — 15%

Select the narrowest current tool that meets the requirement. Flow covers record-triggered, screen, autolaunched, scheduled, and other orchestration patterns. Assignment and escalation rules, approvals, duplicate/validation rules, roll-ups, and product features have specialized semantics. Do not preserve obsolete Workflow Rules or Process Builder designs as the default for new work.

Translate requirements into trigger, entry criteria, actor/system context, read/write set, branch rules, bulk volume, transaction boundary, recursion/idempotency controls, fault path, notifications, observability, and retry/recovery. Use before-save record-triggered flows for efficient same-record changes when suitable; use after-save when related records or actions require a saved record. Avoid queries or writes inside unbounded loops.

Approval processes define entry, submitters, approver selection, lock behavior, approval/rejection/recall actions, and delegation. Confirm what happens when data changes during approval and how administrators recover stranded work.

Debug with representative personas and bulk data. Test create/update/no-op, invalid data, permission failure, missing related data, multiple matching paths, and downstream failure. Activate versions deliberately and retain a documented rollback.

`Related item:` Order of execution connects validation, flows, assignment, escalation, duplicate controls, Apex, and commits. Diagnose the transaction as a whole instead of treating each automation in isolation.

**PRACTICAL DEPTH — fault handling:** A [Flow fault path](https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/roll-back-changes-after-an-error) can allow earlier changes to persist. Screen flows can use Roll Back Records; record-triggered flows can use Custom Error to reject the triggering change and roll back the current transaction. Place necessary rollback before an error screen. A later rollback cannot undo an earlier transaction already committed at a screen boundary. Notification and recovery are separate decisions.

**VERIFY CURRENT — API 68:** The [Winter ’27 versioned change](https://help.salesforce.com/s/articleView?id=platform.automate_flow_versioned_updates_68.htm&language=en_US&type=5) adds **User Context–Enforces User Permissions** for screen and autolaunched flows configured for API 68.0 or later. Ordinary user context can inherit a system-context caller's elevated permissions; the new option enforces the running user's access. Check the flow version, option, caller and actual user. This setting neither changes that identity into the customer chatting with an agent nor establishes customer-specific authorization by itself.

## 8. Agentforce — 8%

The Administrator domain is foundational, not the Specialist blueprint. Know when a bounded agent is appropriate, what trusted data it may use, which topics/actions/instructions it has, under whose security context it acts, and when it must refuse or escalate. A fluent answer is not proof of authorization or correctness.

Be ready to maintain, update, or install prompts and instructions in Agentforce Builder, inspect permissions, and perform light testing with conversation preview. Test allowed, denied, ambiguous, unsafe, stale-data, missing-permission, and escalation cases. Review trace/evidence without copying sensitive data into notes. Separate instructions (behavior guidance), grounding (context), actions (side effects), and user/agent permissions.

`Related item:` Data quality, sharing, field security, Flow safety, and deployment controls from the other seven domains are prerequisites for responsible agents. Agentforce magnifies weak foundations; it does not bypass them.

**PRACTICAL DEPTH — verified identity and access:** The current [Service agent access guide](https://help.salesforce.com/s/articleView?id=ai.agent_user.htm&language=en_US&type=5) distinguishes an identified contact from a logged-in site user. Unidentified and verified-contact conversations can still run as the dedicated agent user, with internal-user sharing defaults. The documented authenticated route requires the supported Enhanced Chat/Experience Cloud configuration and credential-based verification. A context variable naming a contact does not restrict data access: actions must apply the trusted verified identity to their record selection as well as respect effective permissions. A nonempty verification filter alone does not prove that a query excludes other customers. Confirm agent type and channel before generalizing these rules.

## Integrated scenarios

### Scenario 1: Regional sales rollout

A new unit needs distinct opportunity stages, currencies, record experience, access, and dashboards. Produce a license/persona map, role and sharing design, record type/business process, page activation matrix, price-book plan, lead conversion test, forecast/report definitions, deployment sequence, and rollback. Prove that peers cannot see restricted opportunities while managers and approved team members can. A good explanation distinguishes the role/sharing result from CRUD and field permissions; changing a page assignment cannot repair a denied record. Reconcile a known opportunity under both dashboard audiences.

### Scenario 2: Support intake with measurable escalation

Design web/email case intake, duplicate avoidance, assignment queues, response, business-hours escalation, entitlement milestones, knowledge access, mobile actions, and an operations dashboard. Test after-hours intake, absent owner, reopened case, external-user boundaries, and failed notification. Reconcile Case history with routing and dashboard results. A response email proves neither correct assignment nor compliance with a service clock. Retain timestamps, owner changes and the configured calendar; a deliberately failed notification must remain visible in the evidence.

### Scenario 3: Governed automation and agent change

A service agent may summarize an account and initiate a bounded Flow action after verification. Define data minimization, agent user permissions, topic/action filters, prompt/instruction version, Flow transaction and fault behavior, preview cases, sandbox deployment, monitoring, human escalation, and disable/rollback. Confirm that unauthorized fields and actions remain unavailable. A verified contact still requires per-customer scoping when the action runs as a broad agent user. Test an action that updates one record and fails on a second; decide explicitly whether partial completion is acceptable.

## Hands-on evidence labs

**PRACTICAL DEPTH:** Eight proposed org activities, not executed in this review. Use synthetic records and an authorized disposable org. Preserve before/after evidence, disable outbound delivery unless separately authorized, and remove the exercise configuration after verification. Times are study estimates.

| Activity | Procedure and acceptance evidence |
|---|---|
| 1. Access matrix, 60–90 min | Create two personas, restrictive defaults and one sharing rule. Test CRUD, field and record access independently. Mute a group permission, then demonstrate how a direct grant affects it; restore the original assignments. |
| 2. Model and pages, 75–120 min | Build two related custom objects, a validation rule, record types and app/page assignments. Test required-parent and deletion behavior with disposable records; record desktop/mobile and persona results. |
| 3. Sales lifecycle, 60–90 min | Trace a synthetic lead through conversion and an opportunity through stages. Verify campaign membership, mappings and price-book/currency dependencies. Include a duplicate and a missing dependency. |
| 4. Case lifecycle, 60–90 min | Route synthetic cases to queues and evaluate response/escalation rules with a test business-hours calendar. Include an after-hours case and failed delivery; compare owner history and elapsed service time. |
| 5. Data rehearsal, 75–120 min | Back up the sample, map external IDs, rehearse create/update/reject cases and rerun accepted values. Reconcile error files with stored rows and side effects; demonstrate the selected recovery method. |
| 6. Analytics audience, 60–90 min | Build a report type, grouped report and dashboard. Compare two users against known records, fields and folders; distinguish running-user scope from filters. |
| 7. Flow failure, 90–150 min | Build same-record and related-record work with appropriate triggers. Test a batch and a downstream failure. Compare a handled fault with an explicit current-transaction rollback, and document version/context. |
| 8. Agent boundary, 60–120 min | Where licensed, preview allowed, denied, missing-verification and wrong-customer requests. Inspect the actual action user and scoped query. Without access, produce a design only; do not label it an executed agent test. |

## Executed local workbook

The following original Python program ran with Python 3.13.14 and standard-library SQLite: **30 checks passed**. Save it as `admin_workbook.py` and run `python admin_workbook.py`. It uses two in-memory databases, fixed synthetic CSV and fixed trusted-session fixtures; it needs no Salesforce account or network.

The import example distinguishes persisted successes, rejected rows and rolled-back rows. It tests a retry, repeated input keys, malformed values and SQL-looking text treated as data. Its permission-set arithmetic and customer filtering are explanatory models. They do not implement Salesforce permission dependencies, licensing, sharing, authentication, Flow, API response formats or side-effect handling. Unique keys and repeated-key rejection are explicit local policies; no Salesforce duplicate-rule behavior is inferred. The “trusted” session map stands in for an already verified identity source and is not authentication code. No concurrency, crash recovery or production scaling was tested.

```python
import csv
import io
import json
import re
import sqlite3

checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def database():
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE customer (external_id TEXT PRIMARY KEY, '
               'name TEXT NOT NULL, seats INTEGER NOT NULL CHECK (seats >= 0))')
    db.execute('INSERT INTO customer VALUES (?, ?, ?)', ('C1', 'North', 2))
    db.commit()
    return db


def snapshot(db):
    return db.execute('SELECT * FROM customer ORDER BY external_id').fetchall()


def load_csv(db, text, atomic=False):
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames != ['external_id', 'name', 'seats']:
        raise ValueError('unexpected header')
    rows = list(reader)
    outcomes = []
    seen = set()
    db.execute('BEGIN')
    try:
        for number, row in enumerate(rows, 1):
            db.execute('SAVEPOINT one_row')
            try:
                if set(row) != {'external_id', 'name', 'seats'} or None in row.values():
                    raise ValueError('malformed row')
                key, name, raw = row['external_id'], row['name'], row['seats']
                if not key.strip() or not name.strip():
                    raise ValueError('missing key or name')
                if key in seen:
                    raise ValueError('repeated input key')
                seen.add(key)
                if not re.fullmatch(r'[0-9]+', raw):
                    raise ValueError('seats must be a nonnegative integer')
                existed = db.execute('SELECT 1 FROM customer WHERE external_id=?',
                                     (key,)).fetchone() is not None
                db.execute('INSERT INTO customer VALUES (?, ?, ?) '
                           'ON CONFLICT(external_id) DO UPDATE '
                           'SET name=excluded.name, seats=excluded.seats',
                           (key, name, int(raw)))
                outcomes.append({'row': number, 'state': 'updated' if existed else 'created'})
            except (ValueError, sqlite3.Error, OverflowError) as error:
                db.execute('ROLLBACK TO one_row')
                outcomes.append({'row': number, 'state': 'rejected', 'reason': str(error)})
            finally:
                db.execute('RELEASE one_row')
        if atomic and any(r['state'] == 'rejected' for r in outcomes):
            db.rollback()
            for result in outcomes:
                if result['state'] != 'rejected':
                    result['state'] = 'rolled_back'
        else:
            db.commit()
    except BaseException:
        db.rollback()
        raise
    return outcomes


header = 'external_id,name,seats\n'
incoming = header + 'C1,North,3\nC2,South,5\nC3,West,-1\n'
partial = database()
results = load_csv(partial, incoming)
check('three source rows reconciled', len(results) == 3)
check('independent successes and reject retained',
      [r['state'] for r in results] == ['updated', 'created', 'rejected'])
check('accepted values present', snapshot(partial) == [('C1', 'North', 3), ('C2', 'South', 5)])
check('business total uses accepted rows', partial.execute('SELECT SUM(seats) FROM customer').fetchone()[0] == 8)
before = snapshot(partial)
repeat = load_csv(partial, incoming)
check('same values replay without extra rows', snapshot(partial) == before)
check('replay create becomes update', [r['state'] for r in repeat] == ['updated', 'updated', 'rejected'])

atomic_db = database()
original = snapshot(atomic_db)
atomic_results = load_csv(atomic_db, incoming, atomic=True)
check('atomic failure restores original data', snapshot(atomic_db) == original)
check('rolled-back rows not counted as saved',
      [r['state'] for r in atomic_results] == ['rolled_back', 'rolled_back', 'rejected'])
check('transaction closed after rollback', not atomic_db.in_transaction)
fixed = incoming.replace('C3,West,-1', 'C3,West,1')
good = load_csv(atomic_db, fixed, atomic=True)
check('corrected atomic batch commits', [r['state'] for r in good] == ['updated', 'created', 'created'])
check('corrected total is nine', atomic_db.execute('SELECT SUM(seats) FROM customer').fetchone()[0] == 9)
before = snapshot(atomic_db)
duplicate = load_csv(atomic_db, header + 'C1,North,10\nC1,North,11\n', atomic=True)
check('repeated source key rejected', duplicate[1]['state'] == 'rejected')
check('earlier update rolled back with repeated key', snapshot(atomic_db) == before)
malformed = load_csv(atomic_db, header + ',Missing,4\nC4,East,1.5\nC5,Extra,2,unexpected\n')
check('blank key decimal and extra column rejected', all(r['state'] == 'rejected' for r in malformed))
check('invalid inputs preserve data', snapshot(atomic_db) == before)
try:
    load_csv(atomic_db, 'wrong,header\nx,y\n')
except ValueError:
    check('header rejected before transaction', not atomic_db.in_transaction)
else:
    raise AssertionError('header accepted')
quoted = 'C6,"Example, Inc.",2\n'
check('CSV quoting handled', load_csv(atomic_db, header + quoted)[0]['state'] == 'created')
check('quoted name preserved', atomic_db.execute('SELECT name FROM customer WHERE external_id=?', ('C6',)).fetchone()[0] == 'Example, Inc.')
sql_name = "x'); DROP TABLE customer;--"
load_csv(atomic_db, header + 'C7,' + sql_name + ',0\n')
check('SQL-looking name stays data', atomic_db.execute('SELECT name FROM customer WHERE external_id=?', ('C7',)).fetchone()[0] == sql_name)
check('table remains usable', len(snapshot(atomic_db)) == 5)


def effective(profile, direct, groups):
    permissions = set(profile) | set(direct)
    for granted, muted in groups:
        permissions |= set(granted) - set(muted)
    return permissions


group = ({'read', 'edit'}, {'edit'})
check('group mute removes its own edit grant', effective(set(), set(), [group]) == {'read'})
check('direct grant survives group mute', 'edit' in effective(set(), {'edit'}, [group]))
check('profile grant survives group mute', 'edit' in effective({'edit'}, set(), [group]))
check('other group grant survives group mute', 'edit' in effective(set(), set(), [group, ({'edit'}, set())]))
check('muting did not edit the underlying set', group[0] == {'read', 'edit'})

records = [{'id': 'R1', 'contact': 'K1'}, {'id': 'R2', 'contact': 'K2'}]
trusted_sessions = {'verified-a': 'K1', 'verified-b': 'K2'}


def visible(session, readable_ids):
    contact = trusted_sessions.get(session)
    if contact is None:
        return []
    return [r['id'] for r in records if r['contact'] == contact and r['id'] in readable_ids]


check('missing verified identity yields no private rows', visible('unknown', {'R1', 'R2'}) == [])
check('broad agent access still scoped to verified customer', visible('verified-a', {'R1', 'R2'}) == ['R1'])
check('second customer sees only own row', visible('verified-b', {'R1', 'R2'}) == ['R2'])
check('customer identity does not grant missing record access', visible('verified-a', {'R2'}) == [])
check('chat-supplied contact is not a verified session', visible('K2', {'R1', 'R2'}) == [])

partial.close()
atomic_db.close()
print(json.dumps({'passed': len(checks), 'checks': checks, 'partial_seats': 8,
                  'corrected_atomic_seats': 9}, sort_keys=True))
```

Interpret the receipt: partial processing saves two rows totaling eight seats; the same failing atomic batch saves nothing new. After correcting the negative seat value, the atomic batch totals nine seats. Replaying values preserves the fixture's rows, but a real flow might still send another notification. The later quoting tests add records, so nine is the corrected-batch checkpoint rather than the final database total.

## Readiness checks

These original prompts and answer notes support explanation, not recall of live exam content. Demonstrate the relevant org behavior where available.

1. **Which company settings affect dates, service clocks, currency, and reporting?** Locale/time zone, business hours and holidays, fiscal-year settings, currencies and language establish different business assumptions. Trace each calculation to its governing setting.

2. **Why can a permission set not grant a feature absent from the user license?** Licensing establishes eligible capabilities; a permission grant cannot supply a missing entitlement. Check the feature, user license and applicable permission-set license.

3. **What is the difference between freezing and deactivating a user?** Freezing blocks login without releasing the user license; deactivation changes active-user availability and requires ownership/automation follow-up. Preserve audit history; users are not deleted.

4. **How do object, field, and record permissions combine?** For an ordinary user-context read, require object Read, readable fields and access to that record. Elevated execution modes and broad administrative grants require separate analysis.

5. **When do role hierarchy, sharing rules, teams, queues, and manual sharing fit?** Choose by the population and lifecycle: management visibility, rule-based cohorts, account/opportunity/case collaboration, shared ownership or a one-off share. Check the object supports the chosen mechanism.

6. **What evidence shows that least privilege works for both allowed and denied cases?** Run the same operation as the permitted and denied personas and retain the expected result, actual result and grant trace. An administrator-only test is insufficient.

7. **When is master-detail unsuitable compared with lookup?** Choose lookup when records need independent lifecycle/ownership or optional association. Assess master-detail parent requirements, sharing and cascade effects before using it.

8. **How do record types, page layouts, and Lightning-page activation differ?** Record types choose processes/picklists and layout assignments; layouts arrange details/actions; Lightning activation chooses the page for an app/persona/form factor. None replaces record security.

9. **Why is component visibility not a security control?** Hidden components do not remove data access through other pages or APIs. Test authorization at the object, field and record layers.

10. **What dependencies must be checked before deleting or changing a field?** Inventory stored data, formulas, reports, flows, validation, integrations and packages, then rehearse a reversible change with evidence of affected behavior.

11. **What does lead conversion create or match, and how is field mapping involved?** Conversion associates the prospect with an account/contact and can create an opportunity; matching, optional opportunity creation and field mapping affect results. Test the actual conversion configuration.

12. **How do stage, probability, forecast category, and Path differ?** Stage expresses process state; probability and forecast category support projections; Path presents guidance. Validate the mappings instead of treating the labels as interchangeable.

13. **What dependencies connect product, price book, price book entry, and opportunity product?** A product needs a usable entry in the relevant price book and currency before an opportunity line can select it. Check activity status and opportunity context.

14. **What questions do campaign members, hierarchy, and influence answer?** Members track participating leads/contacts and response; hierarchy groups initiatives; influence expresses an attribution model. Agree on the reporting definition.

15. **How do assignment, auto-response, and escalation rules differ?** Assignment selects ownership, auto-response acknowledges intake and escalation acts on age/criteria. A delivered acknowledgment proves neither correct ownership nor a satisfied clock.

16. **When do queues and Omni-Channel solve different problems?** A queue holds eligible work for members; Omni-Channel adds configured routing, availability and capacity. Validate product and license support.

17. **How do business hours and holidays affect service automation?** Service timers use their configured business-hours and holiday calendars. Wall-clock duration alone cannot prove an escalation was early or late.

18. **What evidence proves a Case met its entitlement or escalation behavior?** Compare configuration with case timestamps, status/owner history and milestone evidence under the correct calendar. Include a deliberately missed or failed path.

19. **What are the access implications of Chatter groups and Files?** Group membership and visibility govern collaboration, while Files have their own sharing. Check internal/external personas and the actual file audience.

20. **Which page/action/navigation choices change the mobile experience?** Navigation, actions, compact layouts, component form-factor support and page activation shape mobile behavior. Recheck the actual client and record context.

21. **What security and lifecycle questions precede package installation?** Review publisher, permissions, external connections, data use, licensing, dependencies, upgrades and uninstall/recovery in a sandbox before installation.

22. **When should you choose Import Wizard, Data Loader, or an integration?** Compare supported objects, volume, transformations, scheduling, API needs and result/recovery evidence. A tool name alone does not specify transaction behavior.

23. **Why is an external ID central to a controlled upsert?** A stable external ID identifies the intended target across runs. Reconcile creates and updates and reject ambiguous or conflicting input according to an explicit policy.

24. **How do matching and duplicate rules divide responsibility?** Matching rules identify candidate duplicates; duplicate rules decide the resulting warning/block/allow behavior. Test both false positives and missed matches.

25. **What makes an export a tested backup rather than merely a file?** A backup needs a tested restoration method, dependencies, permissions and agreed recovery objectives. A successfully downloaded file proves only export.

26. **How do report type, folder, record sharing, field access, and running user affect results?** A report type defines available relationships/fields; folder access exposes the report; data permissions and execution audience determine what it can show. Filters further narrow results.

27. **When do summary, matrix, joined, bucket, and formula features fit?** Summary groups one hierarchy; matrix groups rows and columns; joined reports compare blocks. Buckets categorize values and formulas calculate agreed metrics at the appropriate grain.

28. **What changes between static-running-user and dynamic dashboards?** A specified running user supplies a dashboard data perspective; a dynamic dashboard uses the viewer where supported. Test the audience and current licensing limits.

29. **Which Flow type fits same-record, guided-user, scheduled, and background work?** Before-save record-triggered flows fit suitable same-record changes; screen flows guide users; scheduled flows run planned work; autolaunched flows support background invocation. Related work often needs after-save execution.

30. **Why should collection work avoid database operations in loops?** Repeated queries/writes in loops consume shared transaction resources. Collect records and operate on collections where appropriate, then verify realistic bulk behavior.

31. **What must an automation fault path expose to an operator?** Expose a useful failure identifier and affected work without unnecessary sensitive data. Decide whether to preserve or roll back partial changes; logging alone does not undo them.

32. **How do entry criteria and idempotency reduce recursion and duplicate side effects?** Restrict entry to relevant transitions and give repeatable operations stable business keys. Verify external side effects separately because identical field values do not ensure a no-op.

33. **Which approval decisions cover submitter, approver, locking, rejection, and recall?** Specify who can submit, how approvers are selected, who can edit locked records, and the actions for approval, rejection and recall. Rehearse absence/delegation and recovery.

34. **Why must order of execution be tested as one transaction?** Multiple automations and validations can interact before commit. A handled failure can change which earlier work persists; identify transaction boundaries and actual results.

35. **What separates an Agentforce instruction, grounding source, topic, and action?** Instructions guide behavior, grounding supplies context, topics/subagents route work and actions perform operations. Names vary across builder versions; permissions remain a separate control.

36. **Under whose permissions does an agent retrieve data and perform actions?** Inspect agent type, channel and execution context. A verified contact can still use the dedicated agent user; supported authenticated-site configurations can use the site user. Enforce customer scoping in actions.

37. **Which preview cases test more than the happy path?** Include denied fields, another customer, missing/invalid verification, ambiguous requests, unavailable tools, stale context and downstream errors. Preserve trace and expected outcomes.

38. **When must an agent refuse, verify, or escalate?** Refuse disallowed work, obtain verification before private actions and escalate cases outside the defined scope or with unresolved ambiguity. Do not trust identity supplied in chat.

39. **What annual action keeps the credential active?** Complete the credential-specific annual maintenance badge by the deadline in the credential record. Do not substitute an unrelated badge.

40. **Which source will you recheck for weights, current release, delivery, price, and maintenance before booking?** Recheck the canonical prep unit, Help exam guide, actual booking experience and maintenance record. Treat the retained Summer 25 label and unreadable Academy metadata as unresolved.
## Places to learn

This is not a complete list. Choose material that fills a demonstrated gap, then practice in an authorized org. Public listing metadata does not establish lesson quality or complete current blueprint coverage. Estimates explicitly marked “planning” are ours.

| Resource | Access | Estimated time |
|---|---|---|
| [Certification page](https://trailhead.salesforce.com/credentials/platformadministrator) and [prep unit](https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-setup-and-objects/get-started-with-administrator-certification-prep) — identity, eight weights and policy links | Public | Prep unit lists 5 min; 15–30 min planning for baseline checks |
| [Official cert-prep trail](https://trailhead.salesforce.com/content/learn/trails/administrator-certification-prep) — three modules; supplement Agentforce and practical gaps | Free Trailhead; account for completion | Listed 1 hr 20 min, not full skill acquisition |
| [Credential-linked Administrator Trailmix](https://trailhead.salesforce.com/users/00550000006yDdKAAU/trailmixes/prepare-for-your-salesforce-administrator-credential) — current link; both this and the [earlier alias](https://trailhead.salesforce.com/users/strailhead/trailmixes/prepare-for-your-salesforce-administrator-credential) returned empty extracted bodies | Free Trailhead; contents not verified here | Earlier ~60 hr figure not reverified |
| [Salesforce Admins update](https://admin.salesforce.com/blog/2026/what-the-salesforce-certified-platform-administrator-exam-update-means-for-admins) — January 22, 2026 article explaining the December refresh | Public | 10–20 min planning |
| [Object access](https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_objects), [muting](https://trailhead.salesforce.com/content/learn/modules/permission-set-groups/mute-permissions-in-permission-set-groups) and [Flow rollback](https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/roll-back-changes-after-an-error) — selected technical lessons; follow prerequisites for activities | Public lessons; account/org for completion | Listed 25 + 15 + 30 min; additional practice time |
| [Pluralsight Administrator path](https://www.pluralsight.com/paths/salesforce-certified-administrator-update) — eight public course cards and a practice-exam listing; no separate Agentforce-titled course shown | Core Tech subscription; trial advertised, not used | Header 13 hr; cards total 13 hr 14 min |
| [Platform Administrator Study Guide, Mike Wheeler](https://www.oreilly.com/library/view/salesforce-certified-platform/9781098165734/) — catalog endpoint returned HTTP 403; edition/interior claims unverified | O’Reilly subscription/book | Earlier 13 hr 26 min listing not reverified |
| [Mike Wheeler Administrator course](https://www.udemy.com/course/salesforce-administrator/) — HTTP 403; update date and Agentforce coverage unverified | Purchase/subscription, verify terms | Earlier 39 hr 52 min not reverified |
| [Focus on Force catalog](https://focusonforce.com/) — Administrator study/practice links present, but both linked product endpoints failed retrieval | Commercial; current terms and interior not verified | No verified duration; 12–25 hr planning only for selected study |

Pluralsight's introduction card is dated September 30, 2022; its seven domain cards are dated May 11, 2026. Those dates and titles do not establish treatment of the current Agentforce domain or API 68 behavior. Focus on Force's catalog presents an associate-certification requirement for Administrator, whereas the official Help article says **no prerequisite**; use the official rule. No paid lessons, quizzes or practice-question quality were evaluated, and no purchases or trial registrations were made.

Avoid recalled live questions, leaked content and copied assessment or superbadge answers. Use original practice to diagnose concepts, and validate claims against the official source.
