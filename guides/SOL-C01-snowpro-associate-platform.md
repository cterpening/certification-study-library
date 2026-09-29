---
exam_code: SOL-C01
vendor_id: snowflake
official_blueprint: https://publish-p93462-e887935.adobeaemcloud.com/content/dam/SnowProAssociateCertificationTransitionSnowflakeUniversityPlatformSkillsBadgeFAQs.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# SnowPro Associate: Platform (SOL-C01) Retired Reference

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The six archived public abilities were mapped to this reference on September 29, 2026, and the actual two-page transition FAQ was fully read. A local CSV/JSON/SQLite workbook passed 45 checks; eight Snowflake labs and independent human review remain pending. See the [deep-review evidence](../docs/research/2026-09-29-sol-c01-deep-review.md) and [coverage record](../docs/SOURCE-VALIDATION.md#sol-c01-coverage-record).

**Status:** Retired May 4, 2026; it can no longer be scheduled<br>
**Replacement:** Snowflake University Platform Skills course + assessment, available from May 5, 2026 as a free, directly issued, non-expiring skills badge<br>
**Important distinction:** The replacement validates the same foundational course knowledge, but Snowflake says it is an educational skills badge—not a SnowPro certification. SnowPro is now reserved for proctored professional exams.<br>
**Official lifecycle source:** [Snowflake's transition FAQ](https://publish-p93462-e887935.adobeaemcloud.com/content/dam/SnowProAssociateCertificationTransitionSnowflakeUniversityPlatformSkillsBadgeFAQs.pdf). The May 4 retirement date and six abilities come from the preserved September 2 landing-page snapshot; the live FAQ establishes the May 5 transition and voucher disablement. Automated objective monitoring intentionally skips retired exams. An empty monitor result is not a newly verified unchanged blueprint; live lifecycle and product sources were checked separately.

## How to use this reference

If you are starting now, do not buy an SOL-C01 voucher or build a plan around taking the retired exam. Use this page as a technical companion to the current free [Platform On-Demand Training](https://learn.snowflake.com/en/courses/OD-SPT/) and its assessment, then consider active COF-C03 SnowPro Core when you need a proctored professional credential.

If you already hold SOL-C01, Snowflake says the credential remains valid until its original expiration date. This reference helps preserve what it represented and lets you extend the same skills through current documentation. Product names, interfaces, AI functions, editions, limits and role behavior can change even though the former exam no longer does.

**VERIFY CURRENT — learning access:** The public OD-SPT listing estimates four hours and advertises 30 days of lab access; check the individual subscription end date. Basic database knowledge is recommended. Complete the assessment after the course. The FAQ says to seek support if the Accredible badge is absent after 24 hours; no account, enrollment, assessment or badge was accessed here.

For every topic, produce evidence in a disposable trial/training account: object tree, query, role/privilege path, load history, warehouse behavior, protected recovery/share behavior, or a Cortex result with cost and safety notes. Avoid practicing broad account-level grants in a shared environment.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appeared verbatim in the retired published objectives or appears in the replacement assessment.

## Preserved public scope map

The preserved September 2 public overview lists six abilities. No live detailed retired blueprint or replacement-assessment syllabus was recovered in this review, so this map is limited to those six archived statements and invents no domain weights. Product explanations and exercises are **PRACTICAL DEPTH**, not newly added retired-exam objectives.

| Public ability | Proof to produce now |
|---|---|
| Set up and navigate the UI and Snowflake Notebooks | Locate account/role/warehouse/database/schema context; run and inspect a worksheet/notebook safely |
| Create databases and stages, and use compute | Build an object hierarchy and stage with least privilege; start/suspend/resize a warehouse and explain cost/concurrency consequences |
| Load structured, semi-structured and unstructured data | Select file format/stage/load path; validate, load, query, inspect history and handle malformed data |
| Understand roles and data access management | Trace user → active role → inherited role → privilege → object, including ownership and managed-access boundaries |
| Understand and manage account structure | Explain organization/account/database/schema/object hierarchy and separate administrative duties |
| Use Snowflake Cortex LLM functions | Select an authorized AI function, define input/output/evaluation, observe consumption and avoid exposing sensitive data |

---

## 1. Navigate Snowflake, notebooks and architecture

### Know the layers and current context

Snowflake separates database storage, compute and cloud services. Persisted Snowflake table data is stored in optimized columnar micro-partitions. Virtual warehouses supply independent compute for SQL and supported code workloads; one warehouse does not share compute resources with another. Cloud services coordinate authentication, metadata, optimization and requests. Separation lets workloads scale and suspend independently, but does not eliminate governance or cost.

Snowsight is the web interface for worksheets, notebooks, data, monitoring and administration according to privilege. Before running anything, identify current account, region, role, secondary-role behavior, warehouse, database and schema. A successful unqualified object reference can target the wrong context; prefer deliberate qualification and a visible context check in labs.

Snowflake Notebooks combine code/SQL, Markdown and results in an interactive environment. Treat a notebook as executable software: pin or record dependencies, separate secrets/configuration, make cells restartable, control data exposure, and distinguish an exploratory result from a reproducible pipeline.

**VERIFY CURRENT — notebook transition:** Snowflake's [behavior-change notice](https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-disable-legacy-notebooks) disables new Legacy Notebook creation from September 1, 2026. Existing legacy notebooks can still run/edit during this phase; the notice plans to end execution/editing in November 2026 while retaining viewing/export/migration. Use [Notebooks in Workspaces migration guidance](https://docs.snowflake.com/en/user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-migrate) for current practice. Old course screenshots or legacy creation commands are not a reliable current workflow. No notebook migration was performed.

The migration guide distinguishes notebook-service Container Runtime compute from SQL/Snowpark work pushed down to a warehouse. A Workspaces notebook file also does not inherit a database/schema merely from being a legacy database object: set context or qualify references deliberately. Include both compute paths when planning lab access and cost.

### Account and object hierarchy

An organization can contain accounts across regions/clouds. An account contains databases, warehouses, roles, users, integrations and other account objects. A database contains schemas; schemas contain tables, views, stages, functions and related schema objects. Storage hierarchy and access-control hierarchy intersect but are not the same tree.

Database and schema provide namespacing, ownership and privilege boundaries. Temporary objects serve session-scoped work; transient and permanent objects differ in data-protection behavior. Object type, edition and current documentation determine supported capabilities.

**PRACTICAL DEPTH — same-name objects:** A [temporary table can shadow a permanent table](https://docs.snowflake.com/en/user-guide/tables-temp-transient) with the same database, schema and name in that session. Fully qualifying that identical name does not bypass the temporary object. Inspect the session/object type and use unique lab names before a write, drop or restore. Session temporary tables disappear at session end; transient tables persist until dropped but have no Fail-safe.

**Related item:** `USE ROLE`, `USE WAREHOUSE`, `USE DATABASE`, and `USE SCHEMA` change session context. They do not grant missing privileges and should not be confused with object creation.

---

## 2. Create data objects, stages and compute

### Tables, views and stages

Create a database/schema/table from an explicit owner role. Tables persist data; views store query definitions and expose results subject to privileges and view behavior. Use columns and data types that express the contract rather than storing everything as text. Constraints and table behavior differ from traditional engines; confirm what Snowflake enforces versus records as metadata.

A stage is a named or implicit location used in file workflows. Internal stages store files managed within Snowflake; external stages refer to supported cloud storage. Named stages make file format, credentials/integration and reuse more manageable than embedding values repeatedly. Prefer storage integrations over long-lived cloud credentials.

File formats describe parsing/serialization behavior such as delimiter, header handling, compression, encoding, nulls and error conditions. A stage does not parse files by itself; `COPY` combines stage/path, target, file format and load options.

**VERIFY CURRENT — constraints:** The [current constraint matrix](https://docs.snowflake.com/en/sql-reference/constraints-overview) says standard tables enforce `NOT NULL` and `CHECK`; primary, unique and foreign keys remain unenforced on standard tables. [April 2026 release notes](https://docs.snowflake.com/en/release-notes/2026/10_12) establish general availability of standard-table CHECK constraints. Hybrid tables enforce their keys and require a primary key; do not transfer SQLite or another database's key behavior to standard Snowflake tables. Validate business uniqueness explicitly, and do not set optimizer reliance on a false relationship.

### Virtual warehouses

A standard virtual warehouse provides compute. Size affects available resources and consumption; auto-suspend limits idle use, and auto-resume improves convenience. Multi-cluster behavior addresses concurrency rather than making one query inherently faster. Resize can help resource-heavy work, but query shape, pruning, caching and data design still matter.

Separate warehouses by workload/owner when isolation, chargeback or service-level behavior matters. Give roles only the usage/operation privileges they require. Monitor query history, load history and warehouse load rather than tuning by intuition. Always clean up or suspend lab compute.

**PRACTICAL DEPTH — cost boundaries:** [Warehouse guidance](https://docs.snowflake.com/en/user-guide/warehouses-considerations) describes a 60-second minimum when a standard warehouse resumes; tuning auto-suspend depends on workload gaps and cache/restart effects. A [resource monitor](https://docs.snowflake.com/en/user-guide/resource-monitors) covers warehouse consumption, not serverless/AI-service spending, and suspension may take time. It is not a precise hard cap for the entire account. Use the documented budget/usage mechanisms for other services and verify actual lab consumption.

**Related item:** Storage and compute separation means dropping or suspending a warehouse does not drop tables. It also means data protection and compute availability are different recovery concerns.

---

## 3. Load and use structured, semi-structured and unstructured data

### Choose the path

Structured data fits declared rows/columns. Semi-structured formats such as JSON, Avro, ORC, Parquet or XML retain nested/flexible structure; Snowflake's `VARIANT`, `OBJECT` and `ARRAY` support common patterns. Unstructured files can be held in stages and referenced with directory/file capabilities. Pick a path based on volume, latency, source control, schema evolution and failure/replay needs.

Bulk file loading commonly follows source → stage → file format → validation → `COPY INTO` table → load history/reconciliation. Snowpipe supports event-driven file ingestion; Snowpipe Streaming supports low-latency row ingestion. The retired introductory scope centered basic stage/file loading, but recognizing adjacent choices prevents using batch `COPY` as a universal answer.

Validate representative files before broad load. Decide how to handle malformed rows, duplicates, late files and schema changes. `COPY` metadata/load history helps explain loaded, skipped or failed files. Preserve source identity and batch/event keys so retry is deterministic.

**PRACTICAL DEPTH — replay is a data contract.** [Bulk-load metadata](https://docs.snowflake.com/en/user-guide/data-load-considerations-load) expires after 64 days; this is a per-table file-load mechanism, not an indefinite business-event ledger. Old files with an uncertain load status are skipped by default under the documented conditions. `LOAD_UNCERTAIN_FILES` permits uncertain files while consulting available metadata; `FORCE` ignores the metadata and can duplicate previously loaded data. Renamed/repackaged files and repeated business events still require identity and reconciliation controls. Read the actual [COPY options](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table) before changing retry behavior.

The executed local workbook below demonstrates a separate application contract: exact file identity/content, event identity/value consistency, and atomic rows-plus-receipt commit. Its SQLite manifest never expires during the process and is not Snowflake COPY metadata. A raw row count without source identity and rejected/duplicate accounting is incomplete evidence.

### Query and transform safely

Parse semi-structured paths deliberately and use `FLATTEN` when arrays/objects need relational rows. Cast types and handle absent versus JSON null versus SQL `NULL`. For unstructured data, keep file privileges, scoped URLs and sensitive content controlled.

**PRACTICAL DEPTH — three different missing-value cases:** A missing JSON path produces SQL `NULL`; an explicit JSON null in a VARIANT is distinct from SQL `NULL` and from the JSON string `"null"`. [IS_NULL_VALUE](https://docs.snowflake.com/en/sql-reference/functions/is_null_value) returns true for JSON null, false for a non-null JSON value and SQL NULL for SQL NULL input. [TRY_PARSE_JSON](https://docs.snowflake.com/en/sql-reference/functions/try_parse_json) also returns SQL NULL for malformed input, so preserve the raw input and parse/error indicator before collapsing all null-looking results into one bucket. The Python workbook distinguishes missing keys/None/string values only; it does not implement VARIANT semantics.

A useful lab proves row counts, rejected records, null/type rules, duplicate behavior and rerun behavior. A query returning rows is not sufficient evidence of a correct pipeline.

**Related item:** Micro-partition pruning reduces scanned data when filters align with metadata. It is automatic; clustering decisions require evidence from real query patterns and scale.

---

## 4. Roles, privileges and data access

### Trace effective authorization

Snowflake combines discretionary access through object ownership, role-based access through roles, and limited user-based grants. Prefer privileges → custom database/account role → parent functional role → user. Database roles scope privileges within one database and must be granted to an account role for activation. Role inheritance flows upward through grants.

For a query, distinguish:

- authentication: how the identity proves itself;
- session role: which role is primary and whether secondary roles contribute;
- `USAGE`: ability to traverse warehouse/database/schema;
- object privilege: for example `SELECT` on a table;
- ownership/grant authority: who controls the object or grants;
- future grants: policy for objects created later, not retroactive magic.

Managed access schemas centralize grant decisions with the schema owner or a role with grant-management authority. This prevents every object owner from independently granting access. Transfer ownership carefully because ownership carries control and existing grants have explicit handling.

**PRACTICAL DEPTH — effective session privileges:** The [access-control overview](https://docs.snowflake.com/en/user-guide/security-access-control-overview) distinguishes the primary role from active secondary roles. Ordinary data access can draw on their aggregate inherited privileges; object creation uses the primary role's grant chain and assigns ownership to it. Database roles are not directly activated. Ownership of a role is not the same as inheriting its privileges, and future grants do not retrofit existing objects. Test the intended role with secondary roles deliberately controlled so an administrative secondary role cannot hide a missing grant. Check direct user grants and PUBLIC paths as applicable.

### Separate duties

System roles carry account-management responsibilities. Build custom roles for business/workload access instead of placing application privileges directly on administrative roles. Separate user/security/account administration, object ownership, data use and warehouse operation. Use service identities and modern authentication appropriate to automation; do not share human passwords.

Prove least privilege with a positive test and a negative test from the intended role. Record the grant chain. `ACCOUNTADMIN` success proves almost nothing about whether the application role is correct.

**Related item:** Object access and warehouse access are independent. A role can see a table but lack compute, or operate a warehouse but lack data access.

---

## 5. Data protection and collaboration

Time Travel can query or restore historical object state within the configured/supported retention. Fail-safe is Snowflake-managed recovery assistance after Time Travel for eligible permanent data; it is not a user-queryable backup or a substitute for tested recovery design. Temporary/transient objects have different protection behavior.

Zero-copy clone initially reuses storage metadata and then diverges through changed micro-partitions. It is useful for isolated development/testing and recovery workflows, but cloned privileges, dependencies, governance and later storage still need review.

Same-region direct Secure Data Sharing lets a provider expose selected database objects to consumers without copying the underlying data into each consumer account. The provider controls the share; the consumer creates a database from it and supplies compute for queries. Imported shared objects are read-only to the consumer. Listings and Marketplace add discovery/distribution patterns; cross-region/cloud delivery has separate replication/fulfillment and cost considerations, so do not generalize a direct share's no-copy description to every delivery path. Reader accounts can support consumers without a Snowflake account, with provider-managed implications.

Design collaboration from owner, approved data, freshness, masking/row policy, region/cloud, consumer role, cost, revocation and audit requirements. A share does not grant arbitrary access to the provider account.

**Related item:** Replication/failover addresses cross-region/account continuity and is distinct from Time Travel, Fail-safe, clone and sharing. Select recovery controls from RPO/RTO and failure scope.

---

## 6. Cortex AI functions

The preserved SOL-C01 overview explicitly included Cortex LLM functions. Current documentation groups evolving AI functions for tasks such as completion, summarization, extraction, classification, translation and other unstructured analytics. Function names, model availability, regions, privileges and consumption change quickly; use the live AI-function documentation rather than retired course screenshots.

**VERIFY CURRENT — three authorization questions:** For an ordinary `AI_COMPLETE` call, check (1) the applicable account-level blanket or per-function privilege, (2) `SNOWFLAKE.CORTEX_USER` or the narrower `SNOWFLAKE.AI_FUNCTIONS_USER` database role through the execution role, and (3) access to the selected model and its regional availability. The [current access guide](https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql-privileges-and-access) distinguishes blanket/per-function grants with OR semantics: removing a narrow grant does not deny access still available through a broad grant. PUBLIC defaults, secondary roles and model application-role inheritance can change an apparent least-privilege result. Function-specific exceptions and Native App contexts need their own checks; this is not a universal formula for every AI feature.

**VERIFY CURRENT — model access transition:** The [phased allowlist-to-RBAC notice](https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-2378) describes changes between August and November 2026. The [2026_07 bundle page](https://docs.snowflake.com/en/release-notes/bcr-bundles/2026_07_bundle) still labels the bundle disabled by default as checked September 29, with later default changes planned. Do not infer that every account already enforces the same behavior from a milestone date. Inspect the account's active bundle state and actual grants. An inherited all-models bootstrap grant through the `SNOWFLAKE.PUBLIC` application role differs from a grant to the account role `PUBLIC`; removing one path may leave another. No account parameters or grants were changed here.

Start with a bounded task and evaluation set. Define input columns, allowed data, expected output schema, quality/safety checks, model/function, latency and consumption. Protect sensitive data, grant the minimum Cortex capabilities, and record model/function version or observable behavior. LLM output is nondeterministic and can be unsupported by source data; validate before business action.

Use SQL to keep governed data near the operation where appropriate, but do not assume “inside Snowflake” removes privacy, residency, prompt-injection, cost or human-review responsibilities. Limit output use and log enough metadata for evaluation without logging protected prompts/results broadly.

**Related item:** Retrieval/grounding, agents and custom model workflows belong to more advanced current capabilities. The retired foundational scope asked for basic Cortex LLM-function use, not full production AI architecture.

---

## Integrated scenarios

### Scenario 1: Safe analyst workspace

Create database/schema/table/view roles, a small warehouse with auto-suspend, and one analyst role. Load a clean CSV through a named stage, grant only traversal/select/warehouse use, run in Snowsight/Notebook, and prove a protected raw table is denied. Capture object and role trees plus cleanup.

### Scenario 2: Semi-structured support events

Load JSON containing nested events and one malformed record. Validate first, quarantine/reject deliberately, query `VARIANT`, flatten nested values, cast timestamps, reconcile file/row counts and rerun without accidental duplication. Explain when Snowpipe would replace batch loading.

### Scenario 3: Governed AI summary

Use synthetic support text and an authorized Cortex AI function. Define expected facts and prohibited data, grant a narrow role, measure a small sample, review unsupported claims/sensitive output and record consumption. Share only an approved view/result, then revoke and prove access removal.

## Hands-on evidence labs

All eight Snowflake labs are proposed. No account, warehouse, notebook, load, grant, share, recovery or Cortex call was executed for this review. Use synthetic data and a disposable authorized training environment, preserve sanitized evidence and clean up the specific resources you created.

1. **Context and notebooks:** Record account/region, primary/secondary roles, warehouse, database and schema. Create a current Workspaces notebook using the documented flow and rerun from a clean state. In an isolated session, explain a temporary table shadowing an identically qualified permanent name; verify object identity before any destructive step. Save the context and repeatability evidence.
2. **Objects and standard compute:** Create a small database/schema/table/view/stage and permitted standard warehouse with an appropriate suspend policy. Record query/load history, sizing and idle/resume observations; separate data persistence from compute operation. Compare expected and observed consumption and document which nonwarehouse services a resource monitor would not cover. Suspend or remove only the disposable compute you own.
3. **Structured load:** Use three tiny named CSV files with a quoted comma, malformed amount, repeated business event and changed bytes under one source identity. Validate and load with deliberate COPY options, then reconcile source, accepted, rejected and repeated rows. Explain metadata retention and the effects of FORCE without performing an uncontrolled reload. Retain original source identity and an explicit rerun decision.
4. **Semi-structured load:** Use separate missing-key, JSON-null, string-"null", empty-array and malformed-JSON fixtures. Inspect parse status, VARIANT path/type and IS_NULL_VALUE results; flatten with parent identity and element position. Prove that a forgiving parser did not silently classify malformed input as a legitimate missing business value.
5. **Least privilege:** Build a small custom role hierarchy under authorized administration. Record role grants separately from role ownership, database-role inheritance and public/direct grant paths. Test read success and denied writes with deliberate secondary-role state; test object creation under the intended primary role. Inspect managed-access grant authority and distinguish existing from future objects.
6. **Protection:** Record table type, effective retention and account edition before changing controlled rows. Demonstrate a supported historical query, clone or restore, compare expected data, and record cleanup. Explain why a temporary session ending or transient retention expiring cannot be repaired through Fail-safe. Preserve an independent source fixture for rebuilding the lab.
7. **Sharing:** In authorized accounts, or as an explicitly labeled paper design if unavailable, map approved objects, provider grants, consumer database/roles, query compute and revocation. Demonstrate consumer read-only behavior where executed. Keep same-region direct sharing separate from any cross-region fulfillment, replication or reader-account operating costs.
8. **Cortex evaluation:** Use a few synthetic support texts and one currently available authorized function/model. Record the account/per-function privilege, database role, model access, bundle state and regional availability. Inspect broad inherited paths before a negative access test. Evaluate factual support, malformed output and sensitive-data handling; measure consumption and remove only lab-specific grants/resources after approved use.

## Executed local loading workbook

**PRACTICAL DEPTH — 45 local checks passed on September 29, 2026**, using Python 3.13.14 and its standard library. Copy the complete block to a file and run normally with Python; `-O` disables these assertions and is unsuitable for the exercise. Everything runs in memory with invented CSV/JSON data. There are no cloud calls, credentials, network connections, filesystem data files or installed dependencies.

The CSV contract requires exact columns, a nonblank event/customer and a bounded nonnegative amount with two decimals. Integer cents avoid floating-point rounding in the reconciliation. A file receipt binds a logical filename to SHA-256 of its bytes. Identical event IDs/values can repeat across files; conflicting values reject the entire new transaction. Rows and the file receipt commit together. An injected failure after an insert proves rollback before retry; the final state is five events, three file receipts and 1,740 cents.

**Limits:** This is SQLite transaction behavior and an original application contract, not Snowflake COPY, Snowflake SQL or a connector test. SQLite enforces the exercise's primary keys; standard Snowflake primary/unique keys do not enforce equivalent uniqueness. The in-memory ledger has no expiry, durable recovery, concurrent writers or external side effects. The small body/row caps bound only these fixtures. SHA-256 identifies bytes, not their trust or authenticity. JSON examples are controlled fixtures using Python's decoder; `field_state` illustrates missing/None/string distinctions without implementing VARIANT, SQL NULL, Snowflake FLATTEN or a complete untrusted-JSON validator.

```python
"""Local ingestion evidence exercise: Python CSV/JSON + in-memory SQLite, not Snowflake."""
import csv
import hashlib
import io
import json
import re
import sqlite3
from decimal import Decimal


def read_csv(body):
    if not isinstance(body, bytes) or len(body) > 8192:
        raise ValueError('Small byte fixture required')
    reader = csv.reader(io.StringIO(body.decode('utf-8'), newline=''), strict=True)
    if next(reader, None) != ['event_id', 'customer', 'amount']:
        raise ValueError('Exact header required')
    records = []
    try:
        for row in reader:
            if len(row) != 3:
                raise ValueError('Three fields required')
            key, customer, amount = row
            if not key.strip() or not customer.strip():
                raise ValueError('Nonblank identity/customer required')
            if not re.fullmatch(r'(0|[1-9][0-9]{0,5})\.[0-9]{2}', amount):
                raise ValueError('Nonnegative bounded amount with two decimals required')
            records.append((key, customer, int(Decimal(amount) * 100)))
            if len(records) > 100:
                raise ValueError('Too many fixture rows')
    except csv.Error as error:
        raise ValueError('Malformed CSV') from error
    return records


def ingest(db, name, body, fail_after=None):
    if not isinstance(name, str) or not name.strip():
        raise ValueError('Named file required')
    rows = read_csv(body)
    digest = hashlib.sha256(body).hexdigest()
    # A single connection/transaction is the entire local evidence boundary.
    with db:
        prior = db.execute('SELECT digest FROM files WHERE name=?', (name,)).fetchone()
        if prior:
            if prior[0] != digest:
                raise ValueError('File identity reused with different bytes')
            return 0
        added = 0
        for key, customer, cents in rows:
            prior = db.execute('SELECT customer,cents FROM events WHERE id=?', (key,)).fetchone()
            if prior is not None:
                if prior != (customer, cents):
                    raise ValueError('Conflicting event identity')
            else:
                db.execute('INSERT INTO events VALUES (?,?,?)', (key, customer, cents))
                added += 1
                if fail_after is not None and added == fail_after:
                    raise RuntimeError('Injected failure before file receipt')
        db.execute('INSERT INTO files VALUES (?,?)', (name, digest))
    return added


def counts(db):
    return (db.execute('SELECT count(*) FROM events').fetchone()[0],
            db.execute('SELECT count(*) FROM files').fetchone()[0])


def field_state(obj, name):
    if name not in obj:
        return 'missing'
    return 'json-null' if obj[name] is None else 'value'


def flatten_events(text):
    # Controlled synthetic JSON only; this is not Snowflake FLATTEN or VARIANT.
    root = json.loads(text)
    if not isinstance(root, dict) or not isinstance(root.get('events'), list):
        raise ValueError('Object with an events array required')
    result = []
    for index, event in enumerate(root['events']):
        if not isinstance(event, dict):
            raise ValueError('Event object required')
        result.append((index, field_state(event, 'note')))
    return result


checks = 0

def check(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1


def rejects(fn, error=ValueError):
    global checks
    try:
        fn()
    except error:
        checks += 1
    else:
        raise AssertionError('Expected rejection')


HEADER = b'event_id,customer,amount\n'
A = HEADER + b'e1,"Acme, Inc",12.30\ne2,Beta,0.10\n'
B = HEADER + b'e2,Beta,0.10\ne3,Gamma,2.00\n'
check(read_csv(A), [('e1', 'Acme, Inc', 1230), ('e2', 'Beta', 10)])
check(read_csv(HEADER), [])
check(read_csv(HEADER + b'e1,A,999999.99\n')[0][2], 99999999)
for row in [b',A,1.00\n', b'e1, ,1.00\n', b'e1,A,-1.00\n', b'e1,A,1\n',
            b'e1,A,1.001\n', b'e1,A,NaN\n', b'e1,A,Infinity\n', b'e1,A,1e2\n',
            b'e1,A,01.00\n', b'e1,A,1000000.00\n', b'e1,A\n', b'e1,A,1.00,extra\n',
            b'e1,"unclosed,1.00\n']:
    rejects(lambda row=row: read_csv(HEADER + row))
rejects(lambda: read_csv(b'event_id,event_id,amount\n'))
rejects(lambda: read_csv(b'\xff'), UnicodeError)
rejects(lambda: read_csv(b' ' * 8193))
rejects(lambda: read_csv(HEADER + b'e1,A,1.00\n' * 101))
with sqlite3.connect(':memory:') as db:
    db.executescript('''
        CREATE TABLE events(id TEXT PRIMARY KEY,customer TEXT NOT NULL,cents INTEGER NOT NULL);
        CREATE TABLE files(name TEXT PRIMARY KEY,digest TEXT NOT NULL);
    ''')
    check(ingest(db, 'a.csv', A), 2)
    check(counts(db), (2, 1))
    check(ingest(db, 'a.csv', A), 0)
    check(counts(db), (2, 1))
    rejects(lambda: ingest(db, 'a.csv', B))
    check(counts(db), (2, 1))
    check(ingest(db, 'b.csv', B), 1)
    check(counts(db), (3, 2))
    check(db.execute('SELECT sum(cents) FROM events').fetchone()[0], 1440)
    rejects(lambda: ingest(db, 'conflict.csv', HEADER + b'e4,D,1.00\ne1,A,1.00\n'))
    check(counts(db), (3, 2))
    check(db.execute('SELECT id FROM events WHERE id=?', ('e4',)).fetchone(), None)
    C = HEADER + b'e4,Delta,1.00\ne5,Echo,2.00\n'
    rejects(lambda: ingest(db, 'c.csv', C, fail_after=1), RuntimeError)
    check(counts(db), (3, 2))
    check(ingest(db, 'c.csv', C), 2)
    check(counts(db), (5, 3))
    check(db.execute('SELECT sum(cents) FROM events').fetchone()[0], 1740)
    rejects(lambda: ingest(db, '', A))
    check(counts(db), (5, 3))
    result = dict(events=5, file_receipts=3, cents=1740, database='SQLite in memory', cloud_calls=0)
# Context manager commits/rolls back transactions but does not close SQLite itself.
db.close()
check(flatten_events('{"events":[{}, {"note":null}, {"note":"null"}]}'),
      [(0, 'missing'), (1, 'json-null'), (2, 'value')])
check(flatten_events('{"events":[]}'), [])
rejects(lambda: flatten_events('{"events":null}'))
rejects(lambda: flatten_events('{"events":[false]}'))
check(field_state({'note': ''}, 'note'), 'value')
check(field_state({'note': 0}, 'note'), 'value')
print(json.dumps(result, sort_keys=True))
print(f'{checks} local checks passed')
```

## Readiness checks

Explain each answer before uncovering it, then produce the relevant evidence. These are original teaching prompts, not exam questions.

1. **Why separate storage, compute and cloud services?** Persistent data can outlive a warehouse while independent compute serves different workloads; cloud services coordinate metadata, authentication and query handling. Separation does not remove access, governance or cost responsibilities.

2. **What persists when a standard warehouse suspends?** Tables and their retained history remain; warehouse compute stops running. Suspension is not data deletion or a guarantee that storage, serverless or AI charges stop.

3. **Which context should you inspect first?** Account/region, primary and secondary roles, warehouse, database and schema. Fully qualify important names and check object type/session state before modifying anything.

4. **What makes a notebook reproducible?** Recorded dependencies and context, explicit inputs, repeatable cell ordering, clear outputs and failure/cleanup behavior. A successful cell in a stateful interactive session is insufficient.

5. **How does the object hierarchy work?** Organizations contain accounts; an account has databases and account objects such as warehouses/roles; databases contain schemas; schemas contain their objects. Privilege inheritance is a separate graph, not this containment tree.

6. **When do qualified names help?** They reduce ambiguity from current database/schema settings. They do not defeat a temporary object shadowing the identical fully qualified permanent name in the same session.

7. **How do tables and views differ?** Tables hold data under their table-type behavior; ordinary views define a query over data. View access, security, dependencies and performance still need review; a view is not automatically a physical copy.

8. **What separates internal and external stages?** Internal stages store managed files; external stages refer to supported cloud storage. Stage location, storage authorization and file-format parsing are separate parts of the load contract.

9. **What does a file format specify?** How to interpret bytes: type, delimiters, quoting, encoding, headers, null handling and related options. It does not prove business uniqueness or completeness.

10. **Why use a storage integration?** It provides a governed authorization path instead of embedding long-lived cloud credentials in scripts. Verify the permitted location, cloud-side policy and Snowflake grants together.

11. **How do size and suspend settings affect cost?** Warehouse size changes resources/consumption; auto-suspend avoids idle use and auto-resume restarts on demand. Account for the documented standard-warehouse resume minimum and workload gaps, not only nominal query duration.

12. **When does scale-out help?** Additional clusters address concurrent workloads/queuing where supported. They do not combine into an automatic speedup for one query; resizing and query optimization answer different constraints.

13. **Why separate loading, analyst and BI warehouses?** To isolate compute contention, ownership and usage evidence. Data grants remain independent; a warehouse boundary alone is not data isolation.

14. **What is the basic load evidence chain?** Identify source files, stage and format; validate; perform the intended load; inspect results/history; reconcile accepted/rejected/duplicate rows and business keys; document repeat behavior and cleanup.

15. **How do bulk COPY, Snowpipe and streaming differ?** Bulk COPY loads staged files in an explicit batch; Snowpipe continuously ingests available staged files; Snowpipe Streaming ingests rows through its supported client/API path. Select by latency/source contract and verify each path’s behavior.

16. **How do missing, JSON null and SQL NULL differ?** A missing JSON path yields SQL NULL, while explicit JSON null is a VARIANT value. The string "null" is another value. Preserve parse status because TRY_PARSE_JSON can also return SQL NULL for malformed input.

17. **When should you flatten nested data?** When array/object elements need relational rows. Keep parent identity and element position, define empty/null behavior and reconcile expansion so counts are not mistaken for original event counts.

18. **What makes a load retry safe?** A documented file/event identity policy plus reconciliation of previous outcomes. COPY metadata has a retention boundary and FORCE can duplicate data; a renamed file is not proof of a new business event.

19. **How do DAC, RBAC and UBAC appear?** Object ownership, grants through roles and direct user grants are distinct access paths. Verify active secondary-role behavior for direct user privileges and avoid assuming one role listing is the entire permission picture.

20. **Which direction does role inheritance flow?** Granting a child role to a parent lets the parent inherit the child’s privileges. Owning a role does not itself inherit that role’s privileges.

21. **Why check traversal, data and compute privileges separately?** A warehouse-backed query needs access to the database/schema, the target data operation and the warehouse. Passing one check does not grant the others; serverless features have their own requirements.

22. **How do database and account roles differ?** Database roles constrain grants within their database and cannot be directly activated as primary/secondary roles. Grant them to an account role whose session use is deliberately controlled.

23. **Who grants access in a managed-access schema?** The schema owner or a role with MANAGE GRANTS controls grants, including future grants. An object owner does not retain the ordinary independent grant authority there.

24. **Why avoid testing application access as ACCOUNTADMIN?** Broad privileges can conceal missing application grants. Test the actual execution role and deliberate secondary-role state; general authorization and special model-administration behavior are not interchangeable.

25. **What makes an authorization test meaningful?** Prove the allowed operation and a deliberately denied write/admin/data operation from the intended identity. Record the complete inherited/public/direct grant paths and account context.

26. **How do Time Travel and Fail-safe differ?** Time Travel supports user history/recovery within supported retention. Fail-safe is Snowflake-managed recovery assistance for eligible permanent data; temporary/transient tables have no Fail-safe, and it is not a queryable backup.

27. **What does zero-copy clone mean?** The clone initially shares underlying storage references; later changes and retention can add storage. Inspect copied grants, dependencies and table-type support rather than assuming all objects or history are identical.

28. **What does the direct-share no-copy statement cover?** A same-region direct share exposes approved provider objects through metadata without a consumer storage copy. Cross-region/cloud delivery has additional mechanisms and costs that must be checked separately.

29. **Who handles shared-data queries?** A full consumer account supplies its query compute and manages consumer access to a read-only imported database. Reader accounts belong to their provider and have separate operating/cost implications.

30. **Why distinguish sharing, cloning and replication?** Sharing provides governed consumption; cloning creates a separate object state for testing/recovery; replication/failover supports continuity across a broader failure scope. Choose from the intended access or recovery outcome.

31. **What must precede an AI call?** A bounded task, allowed inputs, expected output format, evaluation examples, authorized function/model and cost/latency limits. Never pass protected data merely because SQL makes the call convenient.

32. **How do you evaluate AI output?** Compare output with known supporting facts and schema, count unsupported claims and harmful/sensitive disclosures, and inspect meaningful failures. A fluent summary or a single successful example is weak evidence.

33. **Which AI details are volatile?** Function/model availability, region/cross-region behavior, feature state, access grants, model-control bundles and consumption. Check the actual account state as well as current docs.

34. **Why is a Cortex result not automatically trustworthy?** Model output can be unsupported or influenced by untrusted input; service execution and authorization do not establish factual accuracy. Apply validation and the required human review before consequential action.

35. **Why is SOL-C01 no longer a scheduling target?** The preserved official page gives May 4, 2026 retirement; the current FAQ disables vouchers and introduces the University assessment on May 5. The reference preserves former scope rather than advertising an active exam.

36. **How does the new badge differ?** It is a free, non-expiring educational Platform Skills badge earned through the course assessment. Existing Associate certifications keep their original expiry; SnowPro now denotes proctored professional exams.

37. **What changed for legacy notebooks?** New legacy creation stopped September 1, 2026; the notice plans execution/editing removal in November while keeping view/export/migration. Practice the current Workspaces experience and inspect dependencies before migration.

38. **Which standard-table constraints are enforced now?** NOT NULL and CHECK are enforced. Standard-table primary/unique/foreign keys are not enforcement substitutes; hybrid-table rules differ. The April 2026 standard CHECK release makes old only-NOT-NULL notes incomplete.

39. **Does a successful old-file rerun prove deduplication?** No. COPY may skip an uncertain old file, or FORCE may reload it. Distinguish file metadata from business-event identity and examine accepted/rejected/duplicate counts explicitly.

40. **Do secondary roles authorize object creation?** CREATE uses the primary role’s grant chain and assigns ownership to that primary role. Other ordinary operations can use active secondary-role grants; test the operation’s actual authorization rule.

41. **Does removing a narrow Cortex grant guarantee denial?** No. A blanket account privilege, inherited role, PUBLIC path or model bootstrap grant can still authorize it. Inspect all effective paths and feature-specific gates before judging least privilege.

42. **What did the local workbook prove?** 45 checks exercised Python CSV/JSON parsing, integer-cent reconciliation and SQLite rows-plus-receipt transactions, including a conflicting duplicate and injected rollback. It did not run Snowflake SQL, COPY, a warehouse, access grants, recovery, sharing or Cortex.

**Check key:** Ready means you can explain the mechanism and demonstrate it where applicable. Recognizing a term or passing the local exercise does not complete the proposed Snowflake labs.

## Places to learn

This is not a complete list. Use the current replacement course and measured practice gaps to choose additional resources. Public information was checked September 29, 2026. Study budgets are estimates; public course descriptions do not establish lesson quality or completion.

| Resource | Access | Estimated time |
|---|---|---|
| [Platform On-Demand Training, OD-SPT](https://learn.snowflake.com/en/courses/OD-SPT/) | Free; public listing links the Platform Assessment/Badge to course completion; curated labs advertised for 30 days | Four hours provider estimated effort; add practice as needed, not a verified assessment duration |
| [Transition FAQ](https://publish-p93462-e887935.adobeaemcloud.com/content/dam/SnowProAssociateCertificationTransitionSnowflakeUniversityPlatformSkillsBadgeFAQs.pdf) | Public; actual two-page PDF fully read | 15–30m study estimate |
| [Snowflake University catalog](https://learn.snowflake.com/) | Public catalog; course access/enrollment varies | 30–60m planning estimate |
| [Platform training datasheet](https://www.snowflake.com/wp-content/uploads/2024/12/standard_spt_datasheet.pdf) | Public four-page document, course code 25A24; nine modules and historical function names | Half-day instructor-led description; not the replacement assessment runtime |
| [Data Warehousing Workshop, Badge 1](https://learn.snowflake.com/en/courses/uni-essdww101/) | Free separate Hands-On Essentials course; public outline/grading description only | Same page says six hours estimated effort and 8–12h typical completion; keep both observations |
| [Architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts) and [access control](https://docs.snowflake.com/en/user-guide/security-access-control-overview) | Public; selected architecture/role sections read | 4–8h reading plus 6–10h practice, study estimates |
| [Data loading overview](https://docs.snowflake.com/en/user-guide/data-load-overview) and [COPY reference](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table) | Public; choose the relevant load mode, file options and limits | 2–4h reading plus 4–8h practice, study estimates |
| [Secure Data Sharing](https://docs.snowflake.com/en/user-guide/data-sharing-intro) | Public; main provider/consumer/reader-account explanation read; account availability untested | 1–2h reading plus 2–4h lab/design, study estimates |
| [Current Cortex AI Functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions) | Public; function, access, model, feature-state and region details require current checks | 2–4h reading plus 3–6h practice, study estimates |
| [Udemy retired SOL-C01 course](https://www.udemy.com/course/snowpro-associate-platform/) | Paid; current fetch HTTP403, no lessons or current outline reviewed | Earlier 3h19m/April 2026 metadata unverified; no active-exam preparation claim |

The [May 20, 2026 instructor-led event](https://www.snowflake.com/en/webinars/virtual-hands-on-lab/snowflake-platform-training-2026-05-20/) corroborates the beginner training/badge route but registration is closed; it is not an available upcoming class. Its four-hour event window and the older half-day datasheet do not measure the assessment. The active OD-SPT listing independently displays four hours and 30-day lab access. The prior 8–15h figure was a study budget, not an official duration.

Badge 1 is a separate Hands-On Essentials offering, not another name for the Platform Skills replacement. Its page recommends waiting for the course's instructions before creating a trial account. No enrollment, course video, assessment, DORA-graded exercise, commercial lesson or private training file was accessed. Do not buy a retired voucher or use products advertising actual exam questions or guaranteed passes.
