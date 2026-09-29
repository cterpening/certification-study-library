---
exam_code: SALESFORCE-PLATFORM-DEVELOPER
vendor_id: salesforce
official_blueprint: https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Salesforce Certified Platform Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 29, 2026 review manually compared 21 official objectives, answered 40 original prompts and executed 31 local checks. Salesforce org activities and independent human review remain pending. See the [coverage record](../docs/SOURCE-VALIDATION.md#salesforce-platform-developer-coverage-record).

**CURRENT BLUEPRINT — current baseline:** Developer Fundamentals 27%, Process Automation and Logic 28%, User Interface 25%, and Testing, Debugging, and Deployment 20%. Salesforce’s current display title omits the old “I”; Platform Developer I and PD1 remain useful search aliases for this same credential.<br>
**VERIFY CURRENT — version caveat:** The official Help article still labels the exam Summer ’25. Its current browser-rendered outline includes Agentforce for Developers and matches the saved objectives. Keep that exam scope separate from API 67 product behavior, and recheck the exam and versioned documentation before relying on older training.<br>
**Exam contract:** The Help guide lists 60 scored multiple-choice questions, up to five unscored questions, 105 minutes, 68% passing, USD 200 registration, USD 100 retake, and no formal prerequisite. Verify local taxes, languages, delivery, accommodations, version, and checkout details.<br>
**Experience target:** Salesforce describes a typical candidate as having one to two years of development experience and at least six months on Lightning Platform. Platform Administrator is recommended, not required. This credential is the prerequisite for Platform Developer II.<br>
**Upcoming change:** No retirement or dated blueprint replacement was found in the sources reviewed September 29, 2026. The stale seasonal label is itself a revalidation trigger.<br>
**Maintenance:** Complete the certification-specific Trailhead maintenance requirement once per year by its deadline or the credential expires.

> **Source-access note — September 29, 2026:** The browser-rendered Help article matches all 21 saved objectives, their 27/28/25/20 weights, the stated contract and annual maintenance. Direct HTML still contains a loading/CSS shell, so the automated monitor remains **manual review**; no automatic current-source hash match is claimed. The Summer ’25 label remains unchanged. Current product documentation introduces API 67 security behavior that must be taught with its version boundary. Trailmix and Academy captures were blank, and two paid endpoints returned 403; earlier durations for those resources are marked unverified below.

## How to use this guide

Build one small application repeatedly rather than memorizing isolated syntax. Trace requirement → data/access model → declarative/code boundary → transaction → secure UI → tests → source-driven deployment → telemetry and rollback. For each feature, explain why it fits, what platform limit or security context applies, and how failure becomes observable.

Use an authorized Developer Edition, Trailhead Playground, scratch org, or sandbox. The scenarios and checks here are original. Do not use dumps, recalled live questions, copied superbadge solutions, or material marketed as “actual questions.”

> **About related items:** A `Related item:` callout adds prerequisite, architectural, release, or operational context. It supports the topic but does not assert that Salesforce uses that wording in the public blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Developer Fundamentals | 27% | Architecture/data/access decision record and limit-aware boundary |
| Process Automation and Logic | 28% | Bulk-safe Apex plus declarative interaction tests |
| User Interface | 25% | Secure LWC/Flow/Visualforce behavior across allowed and denied personas |
| Testing, Debugging, and Deployment | 20% | Deterministic tests, correlated diagnosis, versioned promotion and rollback |

## 1. Developer Fundamentals — 27%

Salesforce is multitenant: tenants share platform resources while metadata, data, and access remain logically isolated. Governor limits protect shared capacity. Design every transaction with bounded queries, DML, CPU, heap, callouts, asynchronous work, and data volume in mind. Limits are architectural constraints, not errors to catch after production.

The platform maps broadly to model–view–controller: sObjects and data form the model; Lightning Web Components, Flow screens, and Visualforce render views; Apex, platform services, controllers, and event handlers coordinate behavior. Real applications cross layers, so use MVC as a responsibility model rather than forcing every artifact into one box.

Prefer declarative behavior when it expresses the requirement clearly with acceptable scale, transaction, security, testability, source/deployment, and observability. Use Apex when logic, data access, transaction control, reuse, or execution semantics require code. Formulas calculate values; roll-up summaries aggregate eligible children; validation rejects invalid writes; Flow orchestrates supported processes. Mixing tools is normal, but overlapping writers and unclear order are dangerous.

Model durable business entities, cardinality, ownership, access, delete behavior, reporting, and integrations before writing code. Standard and custom objects expose fields and relationships through schema metadata. Lookup and master-detail have different dependency, sharing, ownership, cascade, and roll-up consequences. External IDs support deterministic matching and upsert; uniqueness and case-sensitivity choices matter.

Agentforce for Developers can assist with code, tests, explanation, or supported development work, subject to current product capability. Treat generated output as untrusted: avoid secrets and restricted data, constrain context, inspect dependencies and security, compile and test, review diffs, and retain human accountability. An agent’s plausible answer does not override platform documentation.

`Related item:` CRUD, field-level security, sharing, and execution context are different layers. Apex can run in contexts that do not automatically enforce every user-facing data-access expectation; make the intended sharing and user-mode behavior explicit and test denied cases.

### Version, access and development-assistant boundaries

**PRACTICAL DEPTH:** Record the class/trigger API version, actual running user, class sharing declaration and database access mode before predicting a result. A hidden UI control is not a permission boundary. These are separate decisions:

| Boundary | Evidence to examine |
|---|---|
| Entry-point access | Can this user invoke the Apex class or action at all? |
| Record access | Which records does sharing permit in this execution path? |
| Object and field access | Can the operation read or modify each selected, filtered or written field? |
| Business authorization | Is this user allowed to perform this transition on this record now? |
| Output audience | Does the returned projection or error reveal information the caller should not receive? |

The [current Apex security guide](https://developer.salesforce.com/docs/platform/lwc/guide/apex-security.html) documents user-mode database defaults and default class sharing from API 67, while API 66 and earlier use older defaults. `with sharing` concerns records; it does not itself supply CRUD/FLS enforcement. Prefer explicit declarations and operation modes so review does not depend on remembering an implicit default. LDS supplies platform access handling for supported data paths. Apex class invocation permission is still a separate gate.

The [versioned database release note](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_default_user_mode.htm&language=en_US&release=262&type=5) says user-mode operations enforce the running user's object/field access and sharing, overriding the calling sharing declaration. Explicit system-mode operations bypass CRUD/FLS, while record visibility follows the calling sharing context. It also removes `WITH SECURITY_ENFORCED` at API 67; use the supported user-mode clause and retest denied cases when upgrading.

`stripInaccessible()` supports deliberate field removal for a graceful result or input sanitization. Use the returned sanitized records, review which fields were removed, and decide whether an incomplete result is acceptable. It is not a replacement for the record-sharing or business-authorization policy. Test denial of an object, a selected field, a filtered field and a record separately.

The blueprint still says Agentforce for Developers. [Current developer documentation](https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-set-up-env.html) calls that extension **Agentforce Vibes Extension**, distinct from **Agentforce Vibes IDE**, formerly Code Builder. This naming reference does not expand the exam into agent-platform architecture. For generated code, require a requirement-based test, a version/access review and a human-reviewed diff; a passing generated test can merely repeat the generator's mistake. Installation, authorization and agent execution were not performed in this review.

## 2. Process Automation and Logic — 28%

Apex is strongly typed and object-oriented. Know primitives, sObjects, collections, enums, classes, interfaces, access modifiers, static versus instance state, method signatures, constructors, properties, annotations, and exceptions. Read control flow precisely: conditions, loops, early returns, collection iteration, null handling, and short-circuit evaluation all affect paths and limit use.

SOQL queries records and relationships; SOSL searches text across eligible objects; DML changes records. Bind variables separate values from query structure. Select only needed fields, constrain cardinality, understand parent/child relationship syntax, and never place per-record queries or DML inside an unbounded loop. Use lists, sets, and maps to collect keys, query once, compute in memory, and write in bulk. Database methods expose per-record results when partial success is intentionally selected. An ordinary DML statement is atomic for that operation; catching its failure does not automatically undo every earlier statement. An unhandled transaction failure or deliberate rollback has a wider boundary. Inspect both the operation result and the final transaction outcome.

Triggers receive batches, not single records. Keep entry logic thin, separate reusable service/domain behavior, compare old/new values when relevant, and make repeated execution safe. Do not use a static Boolean as a universal recursion strategy: transactions can contain multiple chunks and legitimate second passes. Prefer changed-field guards, idempotent results, ownership of each field, and explicit transaction design.

Order of execution connects validation, before-save flows, before/after triggers, duplicate and assignment behavior, after-save automation, rollups, commits, and post-commit work. Exact order is release-sensitive. Map every writer and side effect, test the full transaction, and diagnose observed logs rather than relying on a memorized oversimplification.

Choose asynchronous mechanisms by contract. Future methods are limited legacy-style fire-and-forget work; Queueable Apex supports richer job structure and chaining; Batch Apex processes large sets in executions; Schedulable Apex starts work on a schedule. Know what state serializes, which limits reset, how jobs are monitored, and how retries, duplicate delivery, partial work, and callouts are controlled.

Exceptions separate expected business outcomes from system failures. Catch only where you can add context, compensate, translate safely, or recover; do not swallow errors. Preserve record/job/correlation identifiers without exposing secrets. Custom exceptions communicate domain failures, while transaction rollback or savepoints must match the intended atomicity.

Combine Flow and Apex through stable contracts: invocable inputs/outputs, bulk behavior, null/error semantics, security context, versioning, and idempotency. Apex should not duplicate logic that Flow already owns, and Flow should not obscure code-required transaction behavior.

`Related item:` Platform events and callouts are useful application patterns, but the public guide excludes integration design from the expected candidate role. Learn only enough context to recognize transaction boundaries; do not displace the four published domains with advanced integration study.

### Bulk work, repeat behavior and commit boundaries

Use the [bulk-trigger lesson](https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_bulk) to distinguish a collection from a single-record path. Collect distinct lookup keys, fetch related configuration together, calculate desired values and write changed records together. A query outside a loop can still retrieve too many rows; bounding query count does not bound CPU, heap or downstream automation. A 400-record exercise must account for both 200-record trigger batches rather than letting one transaction-wide Boolean skip the second batch.

An unchanged desired value can skip a write. A later configuration change may legitimately require recalculating the same record. Neither guard proves that emails, events or jobs are delivered once. If a side effect needs replay protection, define its operation identity, stored completion state and retry policy separately. A before-trigger field assignment also has a different contract from issuing another DML update on that record.

The [DML lesson](https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_dml) distinguishes statement exceptions and per-record Database results. Keep the outcome associated with its original input and inspect every error. Partial success remains subject to the enclosing transaction; a later fatal failure can remove earlier successful changes. Catch an exception only with a defined response: recover, reject the operation, deliberately roll back to a savepoint, or propagate it.

**VERIFY CURRENT — trigger context:** The [detailed trigger release note](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_triggers_system_mode.htm&language=en_US&release=262&type=5) distinguishes the trigger's `without sharing` context from its database operations: at API 67+, omitted operation modes default to user mode. This is more specific than the [Summer ’26 roundup](https://developer.salesforce.com/blogs/2026/06/the-salesforce-developers-guide-to-the-summer-26-release), whose trigger bullet broadly says sharing/FLS are bypassed. Use the detailed rule, declare operation modes and verify in the target version; this review did not execute Apex. The detailed release text was readable through indexed first-party extraction while direct/browser opens returned shells.

For asynchronous work, separate acceptance from completion. [Queueable guidance](https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_queueable) supplies a job ID for monitoring and supports chaining; capture that ID with the business operation and inspect the eventual outcome. A job that was enqueued is not evidence that the intended records changed. Test the worker's business result as well as the submission path, and bound retries rather than making failed jobs resubmit indefinitely.

## 3. User Interface — 25%

Use Lightning Web Components for modern reusable UI. Understand component files, public properties/methods, reactive state, templates, lifecycle, composition, Lightning Data Service/wire versus imperative calls, and event flow. Data generally travels down through properties and events travel up; avoid hidden coupling across components.

Prefer base components and Lightning Data Service where they meet the requirement because they provide platform integration and important security behavior. Apex controllers must expose only intentional methods, validate inputs, enforce the intended record/object/field access, and return safe errors. Cache only read operations whose results are actually cacheable. Never trust client-side visibility or validation as authorization.

Flow supplies guided UI and orchestration; LWC can host or extend experiences; Apex can supply controlled server behavior. Agentforce actions may invoke supported Apex/Flow contracts, but generated input is untrusted and potentially adversarial. Validate identity, authorization, types, ranges, records, side-effect confirmation, and replay/idempotency before changing data.

Visualforce remains in the published scope. Know standard versus custom controllers, extensions, expressions, view state, page actions, component use, output escaping, and how Visualforce behaves in Lightning Experience. It is often a legacy or specialized surface, not the default for new UI.

Prevent cross-site scripting by using framework escaping and avoiding unsafe DOM sinks; prevent SOQL injection with static queries/binds or strict allowlists for unavoidable dynamic structure; protect state-changing operations from unauthorized invocation; do not expose secrets in markup, JavaScript, URLs, logs, or errors. Test object, field, and record denial—not only the happy path.

`Related item:` Lightning Web Security and Content Security Policy reduce classes of browser risk but do not make arbitrary third-party JavaScript, unsafe DOM manipulation, or insecure Apex safe.

### A secure browser does not make an unrestricted query safe

For a request editor, test the server independently of the UI: omit a required value, add an unexpected field, submit another user's record ID, repeat a completed request and request a disallowed transition. Validate current state at the mutation boundary. Return a stable user-facing error and an operator correlation ID without leaking query text, inaccessible values or credentials.

[LWS's HTML allowlist](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-sanitize-html.html) filters HTML inserted into the DOM; it does **not** sanitize arbitrary input text. A safe display component cannot authorize a later Apex write. Prefer normal template/base-component rendering and test the actual browser sink, URL handling and server action separately.

[Salesforce's CSP documentation](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/content-security-policy-intro.html) requires external JavaScript libraries used by Lightning components to be uploaded as org static resources. Adding a Trusted URL does not by itself permit arbitrary CDN script loading. The March 2026 community article listed below is useful background, but its CDN recommendation and its sample's reliance on `with sharing` need this first-party/version-specific correction. No sample from that article was installed or executed.

For Visualforce, identify whether a standard controller, custom controller or extension supplies data access, then examine output escaping and server-side checks. Keep a migration record of behaviors that must survive a move to LWC; a visual match alone does not prove equivalent access, validation, navigation or accessibility.

## 4. Testing, Debugging, and Deployment — 20%

Apex tests must be isolated, deterministic, assertion-rich, and meaningful beyond coverage. Create only the data needed, use `@testSetup` when shared setup helps, exercise bulk and limit-sensitive paths, call `Test.startTest()`/`Test.stopTest()` deliberately, and assert records, side effects, errors, and authorization behavior. Do not depend on org data unless a narrow platform case requires it. Mock callouts and control asynchronous completion.

Coverage is a deployment gate, not a quality metric. Test positive, negative, boundary, bulk, repeat, exception, mixed-success, recursion/order, and least-privilege paths. Controllers and flows need representative user/context testing as well as Apex classes and triggers. If generated tests only mirror implementation, they can preserve the same mistake; derive assertions from requirements.

Choose tools by evidence need. Salesforce CLI and DX projects support source, org authentication, retrieve/deploy, test, data, and automation workflows. VS Code provides a development surface. Developer Console can inspect logs and execute anonymous code for bounded diagnosis. Setup surfaces expose debug logs, Apex Jobs, Scheduled Jobs, Flow interviews/errors, and deployment results. Names and commands evolve, so verify current CLI help and documentation.

Debug from symptom and correlation ID to transaction/job, user, input, automation path, query/DML/CPU use, exception, and downstream effect. Reproduce with minimal synthetic data. Change one hypothesis at a time, add targeted instrumentation, and remove or reduce verbose logging afterward. A log that ends successfully does not prove the business outcome.

Use source control as the reviewed source of truth. A promotion record should include artifact/version, target org, dependencies, permissions, tests, destructive/manual/data steps, validation, approver, deployment result, post-deploy user journeys, monitoring, and rollback. Sandboxes and scratch orgs serve different fidelity and lifecycle needs. Change sets may fit connected-org metadata movement; Salesforce CLI and packaging support source-driven repeatability.

`Related item:` Metadata deployment does not automatically migrate business data, secrets, certificates, endpoint authorization, or every org-specific setting. Separate and verify those steps.

### Evidence that exposes the wrong implementation

Use a test matrix with **0, 1, 200 and 400 inputs**, missing configuration, equal repeated values, changed configuration, rejected permissions and a later transaction failure. Assert exact persisted values and absent side effects. A test that only checks that no exception occurred cannot prove a bulk calculation or access policy.

The [trigger-testing lesson](https://trailhead.salesforce.com/content/learn/modules/apex_testing/apex_testing_triggers) separates test-data setup from the call under test with `Test.startTest()`/`Test.stopTest()`. Place asynchronous submission inside that boundary and assert the result afterward. Test an entire chain with its supported stack-depth mechanism and limits rather than assuming every possible downstream job ran. The Queueable lesson provides that qualification; the local worksheet below does not execute Salesforce jobs.

For promotion, retain the exact source revision, API versions, target features and permission assignments alongside test results. Repeat representative denied-persona journeys after deployment. Record separate metadata, data and external configuration recovery steps; redeploying old code is not necessarily a reversal of data changes. Winter ’26 maintenance lists a combined Apex/Flow testing activity, but activity completion or a coverage percentage does not replace these requirement-based checks.

## Integrated scenarios

### Scenario 1: Bulk-safe entitlement calculation

Four rate tiers determine entitlement amounts for 400 requests. A per-record configuration query and a transaction-wide recursion flag are suspect. Compare a grouped lookup, both 200-record batches, an identical replay and a changed-rate recalculation. Require the amount totals and the number of changed rows, then inspect Apex limits and other automation in an authorized org. The local worksheet demonstrates 200 versus one configuration SELECT for its first batch; that is not an Apex limit measurement.

### Scenario 2: Guided partner request

A screen Flow, custom LWC editor and invocable Apex action create request lines. One line fails validation after the header changes. Decide whether the business contract permits partial success, rejects the line operation while retaining the header, or requires the entire transaction to roll back. Test actual caller identity, denied fields, another partner's ID and resubmission. Trace every screen/commit boundary before promising rollback; an optional agent front end has the same server contract.

### Scenario 3: Observable asynchronous recalculation

A rate change queues a large recalculation while some requests are edited concurrently. Track operation ID, configuration revision, job ID, attempted/succeeded/failed counts and reconciliation totals. Define stale-input handling, retry eligibility and a terminal failure state. A completed job status must be reconciled with business results. The worksheet is single-connection and synchronous; race handling, queue behavior and real rollback need separate org evidence.

## Hands-on evidence labs

**Proposed org activities — not executed in this review.** Times are our planning estimates. Use an authorized disposable org and synthetic data; preserve configuration/version and before/after evidence.

1. **Data/access contract (60–90 min):** Model three related objects and distinguish ownership, delete behavior, external-ID uniqueness and output audience. Test object, field and record denial independently and explain every permitted output.
2. **Bulk Apex service (120–180 min):** Implement calculation for 0/1/200/400 records. Capture query/DML/CPU evidence, confirm both batches, then replay and change the configuration. Prove unchanged writes are skipped without suppressing legitimate work.
3. **Query/search/data operations (75–120 min):** Compare bound SOQL and SOSL, a field allowlist and an inaccessible filter field. Introduce one invalid record, inspect all Database results and cause a later failure to test the final transaction boundary.
4. **Flow/Apex boundary (90–150 min):** Specify a bulk invocable input/output contract with record correlation, field ownership and errors. Compare fault handling with deliberate rollback and test a screen boundary. Keep version and running-user evidence.
5. **Secure LWC (120–180 min):** Build with LDS or an explicitly secured Apex path. Test hidden controls through direct server calls, unexpected fields, another persona's ID and hostile display text. Verify CSP/static-resource handling and accessible error states.
6. **Visualforce/legacy review (60–90 min):** Trace controller/extension access, escaping and view state. Record preserved behavior for an LWC migration and test an API-version upgrade against old security assumptions.
7. **Testing and diagnosis (120–180 min):** Build positive/negative/bulk/replay/security/async assertions from requirements. Correlate one failing job and transaction to its final records; prove the correction with a test that previously failed.
8. **Source-driven release (90–150 min):** Promote an exact revision with declared dependencies and permissions. Validate both allowed and denied journeys, reconcile data changes and rehearse metadata versus data recovery separately.

### Executed local worksheet: bulk reads and transaction outcomes

Save this block as `platform_developer_workbook.py` and run `python platform_developer_workbook.py` with a standard-library Python installation. It uses original in-memory SQLite fixtures and closes all connections. All **31 checks** passed in this review.

For 400 requests, the first 200 total **69,800 cents**; both batches total **139,850**. Replaying the first batch plans no writes. Changing the first tier from 100 to 110 cents causes 100 legitimate recalculations, yielding **141,840**. SQLite trace callbacks independently count 200 configuration SELECTs versus one. `executemany` still performs individual SQLite writes; it does not demonstrate a Salesforce bulk DML call or governor-limit budget.

The transaction fixtures distinguish partial rows that commit, an atomic operation failure that is caught while an earlier header update remains, and a later failure that rolls back all pending work. Savepoints explicitly implement the chosen SQL policy; SQLite `executemany` does not automatically supply Salesforce DML semantics.

**Execution boundary:** This is not an Apex, SOQL, sharing, FLS, Flow, LWC or Salesforce transaction emulator. Rows supplied to the calculator are trusted synthetic input, not proof of record authorization. It does not test concurrent edits, job delivery, trigger recursion, side-effect idempotency, production performance, Apex compilation or deployment. Use the org activities above to collect that evidence.

```python
import json
import sqlite3

checks = []


def check(label, condition):
    assert condition, label
    checks.append(label)


def prepare(db, records, grouped=True):
    if len({r[0] for r in records}) != len(records):
        raise ValueError('duplicate request key')
    if any(type(r[2]) is not int or r[2] < 0 for r in records):
        raise ValueError('quantity must be a nonnegative integer')
    if not records:
        return [], 0
    reads = 0
    rates = {}
    if grouped:
        tiers = sorted({r[1] for r in records})
        marks = ','.join('?' for _ in tiers)
        rates = dict(db.execute(
            f'SELECT tier, cents FROM rates WHERE tier IN ({marks})', tiers))
        reads += 1
    updates = []
    for key, tier, quantity, current in records:
        if not grouped:
            rates = dict(db.execute(
                'SELECT tier, cents FROM rates WHERE tier = ?', (tier,)))
            reads += 1
        if tier not in rates:
            raise ValueError('unknown tier')
        target = quantity * rates[tier]
        if target != current:
            updates.append((target, key))
    return updates, reads


def apply_updates(db, updates):
    if updates:
        return db.executemany('UPDATE requests SET amount = ? WHERE id = ?', updates).rowcount
    return 0


def transaction_case(mode):
    db = sqlite3.connect(':memory:')
    try:
        db.executescript('''
            CREATE TABLE header(status TEXT NOT NULL);
            INSERT INTO header VALUES ('Draft');
            CREATE TABLE lines(id TEXT PRIMARY KEY, cents INTEGER CHECK(cents >= 0));
        ''')
        db.execute("UPDATE header SET status = 'Reviewed'")
        accepted = []
        fixtures = [('A', 20), ('B', -1), ('C', 30)]
        if mode == 'atomic_statement':
            db.execute('SAVEPOINT operation')
            try:
                db.executemany('INSERT INTO lines VALUES (?, ?)', fixtures)
            except sqlite3.IntegrityError:
                db.execute('ROLLBACK TO operation')
            finally:
                db.execute('RELEASE operation')
        else:
            for item in fixtures:
                db.execute('SAVEPOINT item')
                try:
                    db.execute('INSERT INTO lines VALUES (?, ?)', item)
                except sqlite3.IntegrityError:
                    db.execute('ROLLBACK TO item')
                    accepted.append(False)
                else:
                    accepted.append(True)
                finally:
                    db.execute('RELEASE item')
        if mode == 'later_fatal':
            try:
                raise RuntimeError('synthetic later failure')
            except RuntimeError:
                db.rollback()
        else:
            db.commit()
        return (accepted, db.execute('SELECT status FROM header').fetchone()[0],
                db.execute('SELECT id, cents FROM lines ORDER BY id').fetchall(),
                db.in_transaction)
    finally:
        db.close()


db = sqlite3.connect(':memory:')
try:
    db.executescript('''
        CREATE TABLE rates(tier TEXT PRIMARY KEY, cents INTEGER NOT NULL);
        CREATE TABLE requests(id TEXT PRIMARY KEY, tier TEXT NOT NULL,
                              quantity INTEGER NOT NULL, amount INTEGER NOT NULL);
    ''')
    db.executemany('INSERT INTO rates VALUES (?, ?)',
                   [('T0', 100), ('T1', 150), ('T2', 200), ('T3', 250)])
    db.executemany('INSERT INTO requests VALUES (?, ?, ?, 0)',
                   [(f'R{i:03}', f'T{i % 4}', 1 + i % 3) for i in range(400)])
    db.commit()
    records = db.execute(
        'SELECT id, tier, quantity, amount FROM requests ORDER BY id').fetchall()
    check('400 synthetic requests exist', len(records) == 400)
    check('four distinct configuration keys', len({r[1] for r in records}) == 4)
    first = records[:200]
    traced = []
    db.set_trace_callback(traced.append)
    naive, naive_reads = prepare(db, first, grouped=False)
    naive_sql = list(traced)
    traced.clear()
    grouped, grouped_reads = prepare(db, first)
    grouped_sql = list(traced)
    db.set_trace_callback(None)
    check('same desired result from two read strategies', naive == grouped)
    check('per-record strategy performs 200 SELECTs',
          naive_reads == len([s for s in naive_sql if s.startswith('SELECT')]) == 200)
    check('grouped strategy performs one configuration SELECT',
          grouped_reads == len([s for s in grouped_sql if s.startswith('SELECT')]) == 1)
    check('empty input causes no query or update', prepare(db, []) == ([], 0))
    check('first batch plans 200 changes', len(grouped) == 200)
    check('first batch writes 200 local rows', apply_updates(db, grouped) == 200)
    check('first batch total is 69800 cents',
          db.execute('SELECT SUM(amount) FROM requests').fetchone()[0] == 69800)
    check('other batch still awaits processing',
          db.execute('SELECT COUNT(*) FROM requests WHERE amount = 0').fetchone()[0] == 200)
    current = db.execute(
        'SELECT id, tier, quantity, amount FROM requests ORDER BY id').fetchall()
    replay, _ = prepare(db, current[:200])
    check('replay plans no writes', replay == [])
    check('replay changes no rows', apply_updates(db, replay) == 0)
    second, _ = prepare(db, current[200:])
    check('next batch still processes after first batch', apply_updates(db, second) == 200)
    check('both batches total 139850 cents',
          db.execute('SELECT SUM(amount) FROM requests').fetchone()[0] == 139850)
    db.execute("UPDATE rates SET cents = 110 WHERE tier = 'T0'")
    current = db.execute(
        'SELECT id, tier, quantity, amount FROM requests ORDER BY id').fetchall()
    changed, _ = prepare(db, current)
    check('changed configuration identifies 100 legitimate recalculations', len(changed) == 100)
    apply_updates(db, changed)
    check('new configuration total is 141840 cents',
          db.execute('SELECT SUM(amount) FROM requests').fetchone()[0] == 141840)
    db.commit()
    for label, bad in [
        ('duplicate keys rejected', [current[0], current[0]]),
        ('negative quantity rejected', [('R000', 'T0', -1, 0)]),
        ('Boolean quantity rejected', [('R000', 'T0', True, 0)]),
        ('unknown configuration rejected', [('R000', 'missing', 1, 0)]),
    ]:
        rejected = False
        try:
            prepare(db, bad)
        except ValueError:
            rejected = True
        check(label, rejected)
    check('rejected plans leave persisted result intact',
          db.execute('SELECT SUM(amount) FROM requests').fetchone()[0] == 141840)
    check('bound text is not interpreted as SQL',
          db.execute('SELECT id FROM requests WHERE id = ?',
                     ("R000' OR 1=1 --",)).fetchall() == [])
    check('record count remains 400',
          db.execute('SELECT COUNT(*) FROM requests').fetchone()[0] == 400)
finally:
    db.close()

partial = transaction_case('partial_commit')
atomic = transaction_case('atomic_statement')
fatal = transaction_case('later_fatal')
check('partial operation preserves per-item order', partial[0] == [True, False, True])
check('successful partial rows commit with outer transaction', partial[2] == [('A', 20), ('C', 30)])
check('partial commit retains prior header update', partial[1] == 'Reviewed')
check('atomic operation rejects all its rows', atomic[2] == [])
check('caught operation failure can retain earlier work', atomic[1] == 'Reviewed')
check('later failure removes previously successful partial rows', fatal[2] == [])
check('later failure also restores earlier header', fatal[1] == 'Draft')
check('all fixture transactions are closed', not any(r[3] for r in [partial, atomic, fatal]))
print(json.dumps({'passed': len(checks), 'checks': checks,
                  'configuration_selects': {'per_record': naive_reads, 'grouped': grouped_reads},
                  'final_cents': 141840}, indent=2))
```

## Readiness checks

1. How does multitenancy lead to governor-limit-aware design?

   **Answer:** Shared resources require bounded work per transaction. Budget queries, rows, writes, CPU and heap across all participating automation, then measure bulk cases.
2. Where do data, UI, and control responsibilities sit in the platform’s MVC model?

   **Answer:** Objects/data form the model; LWC, Flow and Visualforce provide views; Apex and platform controllers coordinate behavior. Trace a complete request across these responsibilities.
3. Which facts decide declarative, Apex, or a deliberate combination?

   **Answer:** Choose from required behavior, scale, access, transaction control, testing and maintainability. Give each effect an owner even when Flow and Apex cooperate.
4. How do formula and roll-up fields differ from stored Apex results?

   **Answer:** Formulas derive values and eligible roll-ups aggregate related records; stored Apex results require code to maintain them when relevant inputs change. Test recalculation and output visibility.
5. Which relationship choices affect ownership, sharing, delete, and aggregation?

   **Answer:** Cardinality and dependency affect ownership, sharing, cascades and native roll-up options. Verify the chosen object/relationship behavior instead of assuming all lookups delete alike.
6. Why do external ID, uniqueness, and case choices matter?

   **Answer:** A matching field alone does not define a safe replay policy. Specify uniqueness, case treatment, missing keys and conflicts, then test repeated and changed requests.
7. How will you validate Agentforce-generated development output?

   **Answer:** Inspect the current API version, dependencies, data access and diff. Run independently designed negative/bulk tests; neither generated prose nor generated tests certify correctness.
8. Which access layers must code explicitly honor and test?

   **Answer:** Separate class invocation, record sharing, CRUD/FLS and business authorization. Record the operation mode and API version; test each denial and the returned projection.
9. When does SOQL fit, and when does SOSL fit?

   **Answer:** Use SOQL for structured record/relationship queries and SOSL for supported text search across objects. Check which fields/records may be searched and returned.
10. Why are queries and DML inside record loops unsafe?

   **Answer:** Their work grows with record count and competes with the rest of the transaction. Collect keys, query in groups and write changed records together, while still bounding rows and CPU.
11. When should partial-success Database methods be chosen?

   **Answer:** Use partial success only when individual results are independently acceptable. Correlate each result to input, handle all errors and remember that later transaction rollback can remove successes.
12. What makes a trigger genuinely bulk-safe?

   **Answer:** It processes every input, batches data access, bounds result volume, manages other automation and proves correct outcomes at multiple batch sizes—not merely one record.
13. Why is one static recursion flag unreliable?

   **Answer:** A single flag can suppress the second batch or a legitimate later recalculation. Guard the actual change/effect and test replay, new batches and new configuration.
14. How do changed-field and idempotency guards differ?

   **Answer:** A changed-field guard detects a relevant transition; an idempotency policy controls repeated effects. Desired-value comparison can skip an unchanged write without guaranteeing one email/job.
15. Which writers participate in the complete save transaction?

   **Answer:** Relevant flows, triggers, validation, duplicate/assignment behavior and roll-ups can affect the save. Trace the current order and all field writers in the target org.
16. When do Queueable, Batch, scheduled, and future work fit?

   **Answer:** Queueable fits identifiable asynchronous jobs and chaining; Batch divides larger work into executions; scheduling selects a start time. Existing future methods have a narrower contract. Choose by required behavior and limits.
17. Which asynchronous failures and duplicates must be designed explicitly?

   **Answer:** Handle stale inputs, job failures, partial work and duplicate submission with operation IDs, explicit retry rules and reconciliation. Submission is not completion.
18. When should an exception be caught, translated, or allowed to roll back?

   **Answer:** Catch where you can recover or give a defined rejection; otherwise propagate. A caught statement error may leave earlier work pending, so explicitly choose the rollback boundary.
19. What belongs in a stable invocable Apex contract?

   **Answer:** Specify supported types, required fields, input/output cardinality, record correlation, access context, bulk behavior, version and failure semantics. Validate at the service boundary.
20. How do you prevent Flow and Apex from owning the same effect?

   **Answer:** Name the owner of each write and side effect, map the complete invocation path and test re-entry. Remove overlapping responsibility before adding recursion flags.
21. Which LWC data path fits LDS/wire versus imperative Apex?

   **Answer:** Use LDS/wire for supported reactive platform data; use imperative operations for deliberate invocation or behavior beyond that contract. Server access and cache semantics still need review.
22. Why can component visibility never provide authorization?

   **Answer:** A caller can invoke server operations outside the visible component. Authorize on the server and test forbidden IDs/fields through that path.
23. How do parent/child events and public APIs reduce component coupling?

   **Answer:** Explicit public properties/methods and events make dependencies visible. Keep state ownership clear and send only the data needed across component boundaries.
24. Which input checks are required when an agent invokes an action?

   **Answer:** Validate authenticated identity, record access, field permissions, types/ranges, current business state, intended side effects and replay policy. Agent-supplied IDs do not establish authority.
25. When is Visualforce still relevant to this blueprint?

   **Answer:** It remains explicitly in the official UI objectives. Know controller and extension behavior, escaping and Lightning compatibility even if choosing LWC for new work.
26. How do escaping, binds, and allowlists mitigate different vulnerabilities?

   **Answer:** Escaping controls interpretation at an output sink; bound values separate data from query syntax; allowlists constrain dynamic identifiers or operations. They solve different problems.
27. What does Lightning Web Security not guarantee?

   **Answer:** LWS does not validate arbitrary input or authorize server data access. CSP does not make every external script trusted, and a Trusted URL does not replace the static-resource requirement.
28. Why is code coverage insufficient evidence of quality?

   **Answer:** Executed lines do not prove the right values, access policy or recovery behavior. Assert requirements, denied outcomes and absent side effects.
29. Which tests expose bulk, repeat, order-of-execution, and access defects?

   **Answer:** Include 0/1/200/400 inputs, replay, changed configuration, denied object/field/record access and a failure after earlier successful work. Observe the final records and jobs.
30. What do `Test.startTest()` and `Test.stopTest()` isolate or complete?

   **Answer:** The pair gives the call under test a fresh limits context; submit relevant async work inside it and assert results afterward. Chain testing needs its supported mechanism and limits.
31. How do Salesforce CLI, DX projects, Developer Console, and logs differ?

   **Answer:** CLI/DX provide source, org and automation workflows; the console/logs support bounded diagnosis; the IDE edits code. Capture tool version and actual command output for release evidence.
32. What is the smallest evidence chain for an asynchronous failure?

   **Answer:** Link operation/configuration revision to job ID, execution error and affected records, then reconcile attempted, successful and failed work against the required outcome.
33. Why should verbose debug logging be time-bounded?

   **Answer:** Verbose logs add overhead and may expose data. Capture enough correlation and timing for a defined investigation, restrict access and remove unnecessary tracing afterward.
34. Which environment best matches each test objective?

   **Answer:** Choose disposable environments for isolated source tests and appropriately configured sandboxes for dependency/integration fidelity. An empty scratch org cannot prove production data or permission behavior.
35. What does source-driven deployment add beyond manual configuration?

   **Answer:** It makes the intended artifact reviewable and repeatable. Record dependencies, API versions and target assumptions along with validation and actual deployment results.
36. Which data, secret, permission, and post-deploy steps stay separate from metadata?

   **Answer:** Handle business data, secrets/certificates, external authorization, assignments and manual settings explicitly. Verify post-deploy user journeys and a recovery route for each kind of change.
37. What does the Summer ’25 label/current-product-documentation discrepancy require you to verify?

   **Answer:** Confirm the current exam contract and target runtime separately. The saved 21-objective outline matches, but the seasonal label does not resolve API 67 behavior or training freshness.
38. Which legacy “PD1” resources remain useful, and which gaps make them unsafe alone?

   **Answer:** Older material can teach core syntax and concepts. Reconcile API/security defaults, Flow, tooling and the current four domains; the old title or a course certificate alone proves no current coverage.
39. What annual action keeps the credential current?

   **Answer:** Complete the annual credential-specific maintenance requirement assigned to you by its deadline. The public Winter26 listing is 45 minutes; this review did not access a credential account.
40. Which authoritative pages will you recheck before scheduling?

   **Answer:** Recheck the canonical exam article, current credential/preparation pages and your maintenance/scheduling information. For implementation, inspect current versioned product documentation and org behavior.

## Places to learn

This is **not a complete list** and is not meant to be consumed in full. Choose resources for identified gaps. Current public catalog metadata is distinguished from earlier observations and our planning estimates; paid interiors and practice quality were not verified.

| Resource | Access | Estimated time |
|---|---|---|
| [Official exam guide](https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1) and [credential page](https://trailhead.salesforce.com/credentials/platformdeveloperi) — scope, role boundary and contract | Public; Help requires browser/indexed reading | 25–40 min, our estimate |
| [Study for the Platform Developer Exam](https://trailhead.salesforce.com/content/learn/trails/platform-developer-i-certification-study-guide) — four public prep cards | Free Trailhead | **1 hr 15 min listed**, 10 + 35 + 10 + 20 min; badge interiors not all reviewed |
| [Preparation Trailmix](https://trailhead.salesforce.com/users/strailhead/trailmixes/prepare-for-your-salesforce-platform-developer-i-credential) — broader curriculum | Free Trailhead; current body unavailable | Earlier **31 hr 25 min** observation, **not reverified** |
| [Platform Developer Winter ’26 maintenance](https://trailhead.salesforce.com/content/learn/modules/platform-developer-certification-maintenance-winter-26) and [introductory unit](https://trailhead.salesforce.com/content/learn/modules/platform-developer-certification-maintenance-winter-26/maintain-your-platform-developer-certification-for-winter-26) — release orientation and a separate combined Apex/Flow activity | Free Trailhead; intro read, activity not executed | **45 min listed**, 10-min intro + 35-min activity |
| [DEX450](https://trailheadacademy.salesforce.com/classes/dex450-build-applications-programmatically-on-the-salesforce-platform) — instructor-led development route linked from the exam guide | Paid; current page blank | Earlier **5 days** observation, **not reverified** |
| [Pluralsight Platform Developer I path](https://www.pluralsight.com/paths/salesforce-certified-platform-developer-i-update) — Adam Olshansky's six public course cards and practice-exam listing | Paid; outlines only | **9 hr 58 min** summed cards, rounded **10 hr** header; 2022/2023/2024 card dates; practice time additional |
| [O’Reilly Salesforce Developer I Certification](https://www.oreilly.com/library/view/salesforce-developer-i/9798868803000/) — earlier book listing | Subscription; HTTP 403 | Earlier **4 hr 10 min / 205 pages / 2024** metadata, **not reverified** |
| [Wheeler Platform Developer course](https://www.udemy.com/course/salesforce-developer/) — Anthony and Mike Wheeler listing | Paid; HTTP 403 | Earlier **13 hr 49 min / June 2026** metadata, **not reverified** |
| [Focus on Force catalog](https://focusonforce.com/) — current public certification catalog | Paid; current landing page read, PD course/practice interiors unverified | 15–30 hr selected study, our estimate |
| [Apex Hours LWC security article](https://www.apexhours.com/lwc-security-in-salesforce/) — March 17, 2026 community background; apply the CSP and Apex corrections above | Public; article read, sample not run | 6-min article label; 45–90 min with your sandbox investigation, our estimate |
| [Apex security](https://developer.salesforce.com/docs/platform/lwc/guide/apex-security.html), [bulk triggers](https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_bulk), [DML](https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_dml) and [Queueable](https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_queueable) — first-party technical reading | Public | 2–4 hr selected reading/practice, our estimate |

Reject guaranteed-pass products, “actual question” files, VCE collections and unexplained answer banks. Use original practice and public documentation; no paid question bank or recalled exam content was used in this review.
