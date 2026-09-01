---
exam_code: DP-800
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-800
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# DP-800 Developing AI-Enabled Database Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dp-800-coverage-record). The [official DP-800 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-800) is authoritative.

**Current baseline:** Skills measured as of March 12, 2026; official English study-guide page last updated March 11, 2026.<br>
**Upcoming blueprint change:** None announced as of August 31, 2026.<br>
**Lifecycle status:** Active; no retirement or replacement was announced on the official pages checked.<br>
**Exam page:** [Microsoft Certified: SQL AI Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/developing-ai-enabled-database-solutions/) · 120-minute assessment · English only on the page checked.<br>
**Official course:** [DP-800T00 Develop AI-enabled database solutions](https://learn.microsoft.com/en-us/training/courses/dp-800t00) · three instructor-led days.<br>
**Practice:** Microsoft's free Practice Assessment is on [AI Skills Navigator](https://aiskillsnavigator.microsoft.com/credentials/cert-f7c226fff388981b97e2bafd239786aba2d62e74bf8e3d50b04d341899bd55f4); sign-in is required to launch it.

## How to use this guide

DP-800 tests database development as a complete system. Trace each design through these chains:

```text
requirement -> platform capability -> schema/object -> query/API -> test evidence
principal -> authentication -> permission/policy -> protected operation -> audit evidence
schema commit -> database project -> build/test -> artifact -> controlled deployment -> drift check
source text -> chunk -> embedding model/version -> vector -> index/search -> retrieval -> grounded answer
symptom -> query/request ID -> plan/wait/telemetry -> root cause -> correction -> measured result
```

Practice on at least two supported SQL platforms where possible. Keep the database engine and compatibility level, service tier, preview/GA status, schema and sample data, execution plans, Query Store evidence, API requests, identity/grant tests, deployment artifact, model/deployment name, embedding dimensions, search metrics and cleanup notes. Product support varies among SQL Server 2025, Azure SQL Database, Azure SQL Managed Instance and SQL database in Microsoft Fabric. Recheck the linked documentation before implementing or booking.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes the objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Microsoft's published exam objectives.

## Objective map

| Published domain | Weight | System question |
|---|---:|---|
| Design and develop database solutions | 35–40% | Can you choose the right relational, JSON, temporal, graph and programmable objects, then write correct modern T-SQL? |
| Secure, optimize, and deploy database solutions | 35–40% | Can you prove least privilege, diagnose performance, deliver schema safely, expose governed APIs and react to change? |
| Implement AI capabilities in database solutions | 25–30% | Can you generate and maintain embeddings, choose exact/approximate/hybrid retrieval and build a secure grounded application? |

---

## 1. Build the operating model

### Distinguish the platforms before selecting a feature

| Platform | Strong fit | Capability questions to verify |
|---|---|---|
| Azure SQL Database | Managed cloud database with database-scoped scaling, identity, monitoring and continuously delivered engine features | service tier/hardware, networking, regional availability, compatibility level, preview state, vector/index/AI support |
| Azure SQL Managed Instance | Managed instance compatibility for migrations and instance-scoped capabilities | update policy, SQL Server 2025 feature availability, networking, instance/database permissions, external connectivity |
| SQL Server 2025 | Customer-managed engine for on-premises, VM, edge or hybrid requirements | edition, cumulative update, compatibility level 170, OS/network, feature enablement, patching and outbound endpoint policy |
| SQL database in Microsoft Fabric | SaaS operational database integrated with Fabric, OneLake and source control | current limitations, capacity, mirroring/analytics endpoint behavior, source-control scope, networking and feature parity |

Azure SQL shares a common engine, but deployment model capabilities differ. Use the current [Azure SQL features comparison](https://learn.microsoft.com/en-us/azure/azure-sql/database/features-comparison?view=azuresql), [SQL database in Fabric overview](https://learn.microsoft.com/en-us/fabric/database/sql/overview), [Fabric SQL limitations](https://learn.microsoft.com/en-us/fabric/database/sql/limitations), and [SQL Server 2025 release notes](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17). Do not transfer syntax or a preview label from one platform to another without checking the Applies to section.

**VERIFY CURRENT:** SQL AI features evolve faster than conventional relational features. Record the platform, region, engine/build, database compatibility level and documentation date with every experiment. Treat preview features as changeable and unsuitable for a production dependency unless the organization accepts their support terms.

> **Related item:** Fabric source control stores database object definitions, not the table data and not every database-level configuration. Its SQL analytics endpoint is a separate read-only analytical surface. A repository sync is therefore neither a backup nor a complete disaster-recovery plan.

### Translate a requirement into evidence

For each feature, be able to state:

1. **Requirement:** data shape, transaction semantics, query pattern, security boundary, latency, recovery and cost.
2. **Decision:** platform, object type, data type, key/index, isolation, interface and AI/search mechanism.
3. **Implementation:** versioned DDL/code/configuration and a non-personal identity.
4. **Evidence:** positive and negative tests, execution plan/telemetry, reconciliation, audit and deployment record.
5. **Failure behavior:** timeout, duplicate, stale vector, policy denial, external-model failure, drift or rollback path.

This keeps an attractive demo from becoming an unsupported production design.

---

## 2. Design and develop database solutions (35–40%)

### Design tables from workload and integrity requirements

Start with grain: one sentence defining what a row represents. Then choose business key, stable primary key, data types, nullability, constraints, temporal/history behavior, write pattern, expected row count/growth and dominant predicates. Microsoft's [SQL Server index design guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17) is a useful decision reference.

#### Choose data types and row shape

- Use the narrowest type that represents the entire valid domain without lossy conversion. Prefer exact numeric types for money-like values when rounding rules require them.
- Define character length from the contract; `nvarchar(max)` is not a harmless default. Large-object values can move off-row and restrict indexing/operators.
- Use `datetime2` for precision and `datetimeoffset` when the offset must be preserved; store a clear canonical time convention.
- Use a native relational column for values with strong type, constraint, join, update or indexing needs. Use JSON for genuinely variable aggregates or externally shaped payloads, not to avoid modeling.
- Define nullable because absence is meaningful, not because the source sometimes omits bad data. Distinguish absent, unknown, empty and zero.
- Consider compression, row width, update frequency and hot-page behavior before choosing a monotonically increasing clustered key.

#### Choose rowstore, columnstore and memory-optimized structures

| Structure | Prefer when | Watch for |
|---|---|---|
| Clustered/nonclustered rowstore | selective lookups, ordered ranges, transactional point writes | excess indexes amplify writes/storage; key order must match useful predicates |
| Clustered columnstore | large scans, aggregation, compression and analytical fact-like workloads | small updates/deletes, rowgroup quality, ordered access and operational latency |
| Nonclustered columnstore | operational rowstore plus selected analytical acceleration | maintenance/write overhead and supported object/features |
| Memory-optimized table | measured latch/locking or high-throughput low-latency need and supported platform | durability, indexes, memory sizing, T-SQL/platform limitations and operations |

Learn rowgroup, segment elimination, delta store and batch-mode implications from the [columnstore index overview](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview?view=sql-server-ver17). An index is justified by a measured workload and plan, not by a rule that every foreign key or predicate needs its own index.

> **Related item:** An embedding vector is usually updated less often than its business row. Separating source content, chunk, model/version and vector metadata can prevent ordinary transactional updates from rewriting a wide vector-bearing row.

### Enforce domain and relationship integrity

- A `PRIMARY KEY` identifies each row and implies uniqueness plus non-nullability. Decide clustered placement separately where the platform permits.
- A `UNIQUE` constraint protects an alternate business key. Define how nullable values should behave.
- A `FOREIGN KEY` prevents orphaned relationships but does not automatically create the supporting child-side performance index.
- A `CHECK` constraint protects a row-local rule such as a range or allowed relationship among columns.
- A `DEFAULT` supplies a value only when an insert omits the column; it does not validate explicit input or repair existing rows.
- A sequence generates numbers independently of a specific table and can serve multiple consumers; numbers can have gaps. An identity property is table-column scoped and can also have gaps. See [sequence numbers](https://learn.microsoft.com/en-us/sql/relational-databases/sequence-numbers/sequence-numbers?view=sql-server-ver17).

Use trusted constraints so the optimizer can reason from them. Treat disable/re-enable and `WITH NOCHECK` as correctness and performance decisions. Validate the existing population before declaring a constraint trusted.

### Partition for management, not automatic speed

Partitioning maps rows through a partition function and scheme. It is useful for large sliding-window management, aligned loading/switching, retention and some query patterns. It does not guarantee faster queries: a predicate must support elimination, indexes often need alignment, and too many partitions increase metadata/maintenance cost. Read [partitioned tables and indexes](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver17).

Define:

- the partition key and boundary semantics (`RANGE LEFT` versus `RANGE RIGHT`);
- future empty partition creation and oldest partition archival/removal;
- aligned indexes and uniqueness-key implications;
- proof of elimination from actual plans and logical reads;
- statistics, compression and maintenance per partition.

> **Related item:** Partitioning is primarily a data-lifecycle and manageability tool. A nonpartitioned table with the right index can outperform a badly partitioned table for selective queries.

### Select specialized table models deliberately

#### Temporal tables

A system-versioned temporal table maintains current rows plus a history table using period columns. `FOR SYSTEM_TIME` supports as-of and interval queries. It fits audit-like reconstruction and point-in-time business analysis, but is not a substitute for database backups or a complete actor/reason audit. Plan history retention, indexes, schema changes, consistency checks and privacy deletion. See [temporal tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal/overview?view=sql-server-ver17).

#### Ledger tables

Ledger adds cryptographic evidence so tampering with database data can be detected. Updatable ledger tables retain history; append-only ledger tables reject updates/deletes. Digest storage and later verification are essential—ledger does not encrypt data, authorize users, prove input truth or replace backup/HA. Use the [ledger overview](https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview?view=sql-server-ver17).

#### Graph tables

Node tables represent entities and edge tables relationships; pseudo-columns identify graph elements. `MATCH` expresses topology patterns. Graph fits variable-depth or relationship-centric traversal where a join-table model becomes awkward, while ordinary relational tables remain better for most fixed relationships and constraints. Learn [SQL graph](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17) and its [architecture](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-architecture?view=sql-server-ver17).

```sql
SELECT p2.Name
FROM Person AS p1, Follows, Person AS p2
WHERE MATCH(p1-(Follows)->p2)
  AND p1.PersonId = @person_id;
```

**Fabric note:** Graph objects may be supported in the operational SQL database while node and edge tables are not mirrored to OneLake. Verify the current Fabric limitation before using graph as an analytics integration boundary.

#### External tables

An external table exposes data that remains outside the database. It fits federation or external lake/object access when supported, but remote availability, credentials, predicate pushdown, transaction consistency, statistics and egress remain part of the design. Check the exact platform/data-source rules in [`CREATE EXTERNAL TABLE`](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-table-transact-sql?view=sql-server-ver17).

### Design native JSON storage and access

SQL can store, validate, construct, query, modify and index JSON. Use the [JSON data documentation](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver17) as the current support matrix.

```sql
CREATE TABLE dbo.OrderEvent
(
    OrderEventId bigint IDENTITY PRIMARY KEY,
    OccurredAt datetime2(3) NOT NULL,
    Payload json NOT NULL
);

SELECT OrderEventId,
       JSON_VALUE(Payload, '$.customer.id') AS CustomerId
FROM dbo.OrderEvent
WHERE JSON_CONTAINS(Payload, '"expedited"', '$.labels') = 1;
```

Understand these families:

- `JSON_VALUE` returns one scalar; `JSON_QUERY` returns an object/array; path strict/lax behavior changes missing/type-error handling.
- `OPENJSON` turns an object/array into rows; an explicit `WITH` schema is safer and more efficient than implicit key/value typing for production transformations.
- `JSON_OBJECT`, `JSON_ARRAY` and `JSON_ARRAYAGG` construct JSON while handling escaping and null behavior intentionally.
- `JSON_MODIFY` updates a property in text-based JSON; native `json` behavior and modify syntax/support must be checked by platform.
- `JSON_CONTAINS` tests containment where currently supported.
- `CREATE JSON INDEX` accelerates selected paths but adds storage/write cost and has platform/preview requirements. Use the current [`CREATE JSON INDEX`](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-json-index-transact-sql?view=sql-server-ver17) page.

**VERIFY CURRENT:** The native `json` type, JSON indexes and newer functions had different GA/preview states across Azure SQL Database, Managed Instance, SQL Server 2025 and Fabric on the checked date. Do not say “SQL Server supports it” without naming the deployment target.

> **Related item:** Persisted computed columns over stable JSON scalar paths plus normal indexes can be a useful alternative where a native JSON index is unavailable. Compare correctness, storage and plan evidence rather than assuming the newest feature is required.

### Create reusable programmable objects

#### Views and functions

- A view provides a reusable relational interface and can limit exposed columns/rows. It stores a query, not data, unless indexed-view requirements are deliberately met.
- A scalar function returns one value. It is convenient but can create row-by-row cost depending on inlining/eligibility and the query.
- An inline table-valued function behaves like a parameterized relational expression and is often easier for the optimizer to integrate.
- A multi-statement table-valued function builds and returns a table variable; understand estimation and performance implications.

Use schema binding only when its dependency constraints and benefits fit. Grant access to a stable view/procedure interface rather than broad base-table rights where ownership chaining and dynamic SQL behavior are understood.

#### Stored procedures and triggers

Stored procedures encapsulate multi-statement operations, parameter handling, transactions and controlled permissions. Use strongly typed parameters, `SET NOCOUNT ON`, explicit transaction boundaries, safe dynamic SQL with `sp_executesql`, predictable result/error contracts and observability.

Triggers run synchronously with the data change. They must handle multirow `inserted`/`deleted` sets, avoid hidden recursive/cascading behavior and remain short. Prefer constraints for row-local integrity and asynchronous change mechanisms for integrations. A trigger failure rolls back the caller's transaction.

```sql
CREATE OR ALTER PROCEDURE dbo.TransferBalance
    @FromAccount bigint,
    @ToAccount bigint,
    @Amount decimal(19,4)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    BEGIN TRY
        BEGIN TRANSACTION;
        -- Validate and update both accounts with an appropriate concurrency design.
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0 ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
```

Review [`TRY...CATCH`](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql?view=sql-server-ver17). Preserve the original error with `THROW` unless the interface deliberately maps it. A catch block does not automatically roll back an open or uncommittable transaction.

### Write set-based analytical and hierarchical queries

#### Common table expressions

A CTE names a query expression for one statement. It improves readability and enables recursion; it does not automatically materialize/calculate once. A recursive CTE needs anchor and recursive members, termination, cycle-aware design and a defensible `MAXRECURSION`. See [CTEs](https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql?view=sql-server-ver17).

#### Window functions

Window functions compute across related rows without collapsing them like `GROUP BY`. Be able to use partition, order and frame deliberately:

```sql
SELECT CustomerId,
       OrderDate,
       Amount,
       ROW_NUMBER() OVER
           (PARTITION BY CustomerId ORDER BY OrderDate, OrderId) AS SequenceNumber,
       SUM(Amount) OVER
           (PARTITION BY CustomerId ORDER BY OrderDate, OrderId
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningAmount
FROM dbo.CustomerOrder;
```

Tie breakers make ranking deterministic. `ROWS` and `RANGE` frames differ. Learn the [`OVER` clause](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql?view=sql-server-ver17) and inspect sorts, memory grants and supporting index order.

#### Correlated subqueries

A correlated subquery references the outer row. It can express `EXISTS`/`NOT EXISTS` clearly, but may execute as an inefficient repeated operation if the optimizer cannot transform it. Compare a semijoin/antijoin, window or pre-aggregation. Prefer `NOT EXISTS` over `NOT IN` when nullable input could produce three-valued-logic surprises.

### Use regular-expression and fuzzy matching functions

Current SQL platforms add functions for validation, extraction, replacement, splitting and matching. Learn the function named in the objective—`LIKE`, regex replace/substr/instr/count/matches/split-to-table—and verify the exact name/signature for the target. The [regular expressions overview](https://learn.microsoft.com/en-us/sql/relational-databases/regular-expressions/overview?view=sql-server-ver17) documents RE2-style behavior and platform requirements.

- Use `LIKE` for simple wildcard patterns and indexes where a useful anchored predicate is possible.
- Use regex for structural patterns, not as a substitute for a proper type or trusted constraint.
- Bound expensive input; regex behavior does not simply inherit SQL collation semantics, and documented large-object limits apply.
- Treat user-supplied patterns as untrusted workload input; enforce length, timeout/resource controls and allowed use cases.

Fuzzy functions such as `EDIT_DISTANCE`, `EDIT_DISTANCE_SIMILARITY` and `JARO_WINKLER_DISTANCE` rank lexical similarity; they do not establish identity. Use [fuzzy string matching](https://learn.microsoft.com/en-us/sql/relational-databases/fuzzy-string-match/overview?view=sql-server-ver17), normalize data, generate a bounded candidate set, set domain-tested thresholds and route uncertain matches for review.

**VERIFY CURRENT:** Fuzzy matching was preview in SQL Server 2025 documentation and did not follow collation semantics as of the checked date. Function availability can differ by deployment target.

> **Related item:** Entity resolution is a decision system, not a distance function. Preserve which fields, normalization, algorithm/version, threshold and reviewer produced a match so false merges can be reversed.

### Use AI-assisted development without outsourcing responsibility

GitHub Copilot can explain, generate, refactor and help troubleshoot SQL in supported tools. Copilot in Fabric adds product-integrated assistance. Start with the [GitHub Copilot SQL overview](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/github-copilot/overview?view=sql-server-ver17) and [Copilot in Fabric FAQ](https://learn.microsoft.com/en-us/fabric/database/sql/copilot-faq).

For every generated change:

1. give only the minimum approved schema/context;
2. state platform/version, correctness, security and performance constraints;
3. review identifiers, joins, null behavior, transaction/isolation, injection, destructive DDL/DML and permissions;
4. execute first with synthetic or masked data in an isolated environment;
5. inspect actual plan, results and tests; commit only reviewed code;
6. never paste secrets, production personal data or unapproved proprietary content into a prompt.

#### Instruction files and MCP endpoints

Repository/database instruction files can supply conventions and architecture context. They are versioned configuration, not a security boundary. Review changes to them because untrusted instructions can redirect an assistant. Current references include [database instructions in SSMS](https://learn.microsoft.com/en-us/ssms/github-copilot/database-instructions), [MCP servers in SSMS](https://learn.microsoft.com/en-us/ssms/github-copilot/mcp-servers), [Fabric data warehouse MCP server](https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehouse-mcp-server), and [Fabric SQL database skills](https://learn.microsoft.com/en-us/fabric/database/sql/skills).

An MCP server exposes tools/resources to an AI client. The client still acts through a configured identity and its database permissions. Apply least privilege, separate read and write capabilities, confirm impactful actions, restrict network/tool configuration, log calls and assume database metadata/results passed to the model are sensitive.

> **Related item:** Prompt injection can arrive through an instruction file, issue, documentation row or retrieved database content—not only the user's chat message. Treat model output and tool arguments as untrusted until policy and code validate them.

---

## 3. Secure, optimize, and deploy database solutions (35–40%)

### Start security with identity and data flow

Draw the path before granting access:

```text
human/workload -> Microsoft Entra authentication -> server/database principal
principal -> role/direct grant -> schema/object/row/column/endpoint
application -> managed identity/token -> database/API/model endpoint
operation -> audit/diagnostic record -> protected monitoring workspace -> alert/review
```

Prefer Microsoft Entra identities and passwordless connections for Azure-hosted workloads. A managed identity removes application-managed credential rotation, but still needs a database user, least-privileged grants and controlled Azure resource assignment. Review [Microsoft Entra authentication for Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview?view=azuresql).

Use database roles for stable job functions, schemas as permission boundaries and explicit grants/denies only with a documented reason. Ownership and ownership chaining can allow access without a direct base-object grant; dynamic SQL may break that chain. Test as the actual principal, including negative operations.

### Protect data at the correct layer

| Control | Protects | Does not by itself protect |
|---|---|---|
| TLS | data in transit between endpoints | authorized endpoint use, data after decryption |
| TDE/storage encryption | database/data files, backups and storage media at rest | privileged query access or application result sets |
| Always Encrypted | selected values from database engine/operators when keys remain client-side | unsupported computations, compromised client/key store, access-pattern metadata |
| Dynamic data masking | casual exposure in query results to non-exempt users | stored data, inference/exfiltration through allowed queries, privileged users |
| Row-level security | rows returned/modified according to a predicate | columns within permitted rows, object discovery or a badly written predicate |
| Object permissions | allowed actions on securables | row/column nuance unless paired with policy/view/mask |
| Auditing | evidence of configured events | preventive authorization or proof that every required event was configured/retained |

The [SQL encryption overview](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-encryption?view=sql-server-ver17) separates encryption boundaries. Use [Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17) when the threat model requires protected columns to remain encrypted from the database system/administrators. Plan column master/encryption key ownership, enclave needs, driver parameterization, supported operations, rotation and recovery.

**Column-level encryption** with database cryptographic functions/keys encrypts selected values while the database engine can decrypt them for an authorized caller. It can reduce plaintext exposure at rest or through broad table reads, but privileged key/control access remains in the database trust boundary. Protect the certificate/asymmetric key that secures a symmetric key, open keys only for the operation, deny unnecessary key permissions, back up keys/certificates and test rotation/restoration. Choose it instead of Always Encrypted only when server-side decrypt/processing and that threat boundary are acceptable.

#### Dynamic data masking

Dynamic data masking changes result presentation for users lacking `UNMASK`; data remains unchanged. Apply default, email, random or partial masks as supported, then test direct selection, joins, filters, aggregates, inference and privileged paths. It is a least-exposure convenience, not an adversarial data-protection boundary. See [dynamic data masking](https://learn.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking?view=sql-server-ver17).

#### Row-level security

RLS binds an inline table-valued security predicate to a table through a security policy. A filter predicate hides rows; a block predicate rejects prohibited writes. Keep predicates schema-bound, deterministic and efficient; index the columns used to resolve tenant/user scope.

```sql
CREATE SCHEMA Security;
GO
CREATE FUNCTION Security.fn_tenant_access(@TenantId int)
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN
    SELECT 1 AS allowed
    WHERE @TenantId = TRY_CONVERT(int, SESSION_CONTEXT(N'tenant_id'));
GO
CREATE SECURITY POLICY Security.TenantPolicy
ADD FILTER PREDICATE Security.fn_tenant_access(TenantId) ON dbo.CustomerOrder,
ADD BLOCK PREDICATE Security.fn_tenant_access(TenantId) ON dbo.CustomerOrder AFTER INSERT
WITH (STATE = ON);
```

The application must set trusted session context on every pooled connection and prevent users from setting another tenant's value. Test read, insert, update across tenant, administrator/bypass paths, connection reuse and plans. Learn [row-level security](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17).

> **Related item:** RLS bugs are often identity-context bugs. If connection pooling carries stale session state or the app can choose its own tenant value, a correct predicate can still enforce the wrong boundary.

### Secure model endpoints and data interfaces

When SQL calls a model or external REST endpoint:

- use a managed identity or a database-scoped credential rather than embedding a token;
- grant only the invocation permission and model deployment/action required;
- allow-list supported HTTPS destinations and control DNS/network egress where the platform permits;
- minimize prompt/context data, classify it, and account for provider logging/retention and regional processing;
- validate output shape and size; enforce timeouts, retry/backoff and cost/rate limits outside a long user transaction;
- audit who invoked which endpoint/model/version without logging raw sensitive prompts unnecessarily.

Secure Data API builder endpoints with identity/provider configuration, entity permissions and field/action restrictions. REST/GraphQL exposure is not authorization by itself. Secure MCP endpoints as tool interfaces: tool descriptions, arguments and results can carry sensitive data or instructions.

Use the broader [SQL security best practices](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-security-best-practices?view=sql-server-ver17) and, for Fabric-specific inheritance and roles, the [Fabric SQL security overview](https://learn.microsoft.com/en-us/fabric/database/sql/security-overview).

### Audit for an answerable question

Define the event question first: who changed a role, read a sensitive object, invoked an endpoint, deployed schema or changed an audit policy? Then configure the platform's auditing/diagnostic categories, destination, retention, access and alert. Store logs outside the database's ordinary administrator boundary where the threat model requires it.

Prove:

- an expected successful and denied operation appears;
- identity, database/object, action, timestamp and correlation fields are usable;
- destination ingestion delay and retention meet policy;
- the audit configuration itself is monitored;
- sensitive statement text/parameters are handled appropriately.

### Configure connection, transaction and concurrency behavior

Application configuration should make behavior explicit: connection target/database, Microsoft Entra authentication mode, encryption and certificate validation, pooling, connect/command timeout, retry policy and application name. Do not retry every error. Retry transient connection/throttling faults with bounded backoff and idempotency; do not blindly replay an ambiguous write.

#### Isolation and versioning

| Isolation choice | Main behavior | Design concern |
|---|---|---|
| Read committed locking | readers can wait behind writers and see committed statements | blocking and lock duration |
| Read committed snapshot | statement-level committed versions reduce reader/writer blocking | temp/version-store pressure and changes from one statement to the next |
| Snapshot | transaction reads a consistent version | update conflicts and version storage |
| Repeatable read | protects rereads of touched keys with locks | phantoms and longer blocking |
| Serializable | range locks prevent phantoms | greatest blocking/deadlock risk |

Keep transactions short, touch resources in consistent order and avoid user/network/model calls inside them. Optimistic concurrency can compare a `rowversion` or original values and handle zero-row updates as conflict. Pessimistic locks may be correct for scarce resources but require timeout/deadlock recovery.

> **Related item:** Database isolation and application idempotency solve different problems. Isolation coordinates concurrent database operations; an idempotency key prevents a client retry from creating a second business operation.

### Diagnose with waits, plans and workload history

Use a consistent investigation sequence:

1. Confirm user impact, scope and time window; capture application/request/query/run identifiers.
2. Check service health, resource saturation, connection failures/throttling and recent deployment/config change.
3. Identify top duration, CPU, reads, writes, waits and regressions through Query Store/Query Performance Insight.
4. Capture actual plan safely; compare estimated versus actual rows, access paths, joins, sorts/hashes, spills, memory grant, parallelism and warnings.
5. Inspect DMVs for current requests, sessions, locks, waits and resource state.
6. Correct the root cause; replay a representative workload and compare latency, logical reads, CPU, waits and plan stability.
7. Retain evidence and monitor for regression.

Use [monitoring with DMVs](https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs?view=azuresql) and [identify query performance issues](https://learn.microsoft.com/en-us/azure/azure-sql/database/identify-query-performance-issues?view=azuresql). DMV state can reset after failover/restart and permissions/platform columns differ; Query Store supplies durable workload history when correctly configured.

#### Read execution plans as explanations

Do not optimize by operator icon alone. Look for:

- large actual/estimated row differences suggesting stale statistics, parameter sensitivity or correlation;
- scan versus seek in context—a scan can be optimal for many rows;
- implicit conversion or non-SARGable expression preventing useful access;
- lookup repeated at high row count;
- sort/hash spill and memory-grant feedback;
- join choice/order and residual predicates;
- missing-index suggestion as hypothesis, not an instruction;
- parallel skew, exchange cost and serial zones;
- scalar/UDF behavior and row goals.

Parameter-sensitive workload correction might be query/schema/statistics redesign, parameter-sensitive plan optimization, recompilation, `OPTIMIZE FOR`, Query Store hint or plan forcing. Each trades compilation cost, stability and generality; prove behavior for multiple parameter shapes.

### Diagnose blocking and deadlocks separately

Blocking is waiting behind an incompatible lock. Identify the head blocker, its transaction, query, wait resource, age and application context. The blocked query is not necessarily the cause. Follow [understand and resolve blocking](https://learn.microsoft.com/en-us/azure/azure-sql/database/understand-resolve-blocking?view=azuresql).

A deadlock is a cycle; the engine chooses a victim. Capture the deadlock graph and map processes, resources, lock modes and statements. Corrections include consistent access order, shorter transactions, useful indexes, appropriate isolation/versioning and retry of the victim only when the transaction is safe to replay. Use [analyze and prevent deadlocks](https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks?view=azuresql).

> **Related item:** Killing a blocker restores capacity but does not correct the transaction design. Retain evidence first where safe, anticipate rollback time, then fix the source of the long transaction.

### Deliver schema through SQL database projects

A SQL database project represents database objects as versioned declarative source, builds a `.dacpac`, validates references and deploys through SqlPackage or supported tooling. SDK-style projects based on `Microsoft.Build.Sql` are the current direction. See [SQL database projects](https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/sql-database-projects?view=sql-server-ver17).

#### Source and branch workflow

1. Import/model the intended schema in a project; do not treat a production database as the only source of truth.
2. Use feature branches and small commits tied to a change. Keep object source, tests and deployment scripts together.
3. Build on every change; run static/code analysis and tests against an ephemeral/integration database.
4. Review generated DDL, compatibility, permissions, data movement and destructive-change warnings.
5. Resolve merge conflicts from the intended final schema, then rebuild and compare. Do not mechanically accept both definitions of one object.
6. Publish one immutable `.dacpac` through environments; vary approved configuration/secrets, not compiled schema.

Reference/static rows such as controlled type codes may be represented in reviewed source and deployed idempotently when they are truly part of the database contract. Give each dataset an owner, stable key and deletion/update policy; test both an empty target and an upgrade from prior values. Do not place environment secrets, mutable business master data or large production extracts in the repository under the label “reference data.”

The [store database schema in Git tutorial](https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/tutorials/store-database-schema-git?view=sql-server-ver17) covers the core model. Pull requests are a useful governance pattern, but the technical requirement is controlled review and validation; a solo repository can enforce the same checks directly before merge/deploy.

#### Test at multiple layers

- **Build/static analysis:** syntax, unresolved reference, compatibility and configured rule failures.
- **Unit/database behavior:** procedure/function results, constraints, null/boundary/error and transaction behavior on controlled data.
- **Contract:** expected columns, types, nullability, keys, permissions, REST/GraphQL schema and model-output schema.
- **Integration:** identity, external endpoint/model, DAB, change mechanism and real supported engine behavior.
- **Migration:** deploy from each supported prior version with realistic size; prove data preservation and duration/locking.
- **Security:** positive and negative principal, row/column policy, secret absence and audit evidence.
- **Performance:** representative distribution/concurrency and plan/latency regression threshold.
- **Recovery:** failed deployment, rollback/forward-fix, backup/restore and post-deploy task replay.

#### Detect drift and deploy safely

[Schema comparison](https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/concepts/schema-comparison?view=sql-server-ver17) can compare project/database/dacpac states. Classify intentional emergency drift, platform-managed differences and unauthorized change. Reconcile intentional changes back to source.

Before publish, generate and review the deployment script/report. Block unapproved data loss; back up or export critical data; control DDL transaction and lock/time budget; use pre/post-deployment scripts sparingly and idempotently; capture artifact hash, target, approver/operator and output. Keep environment secrets in a protected secret store/CI identity, never project source or publish profiles committed with credentials.

Pipeline controls can combine protected branch policy, required build/test/status checks, code owners for sensitive paths, controlled triggers, separation of build and deploy, environment approval, workload-identity authentication, scoped target roles and an immutable artifact. Restrict who can change the pipeline itself. A manual approval without deployment evidence is weaker than a repeatable gate that proves artifact, target, identity, test result and data-loss review.

> **Related item:** A dacpac describes desired schema, not arbitrary data migration logic or every newer object type. Vector indexes, for example, may require a verified post-deployment creation step when current dacpac/bacpac tooling does not support them. Test that step and drift behavior on the exact platform.

### Configure and expose Data API builder

Data API builder (DAB) maps configured database entities to REST and GraphQL without writing a conventional controller. Start with the [DAB overview](https://learn.microsoft.com/en-us/azure/data-api-builder/) and [configuration reference](https://learn.microsoft.com/en-us/azure/data-api-builder/configuration/).

#### Runtime and entity configuration

The runtime config selects data source/connection, host mode, REST and GraphQL paths, authentication provider, CORS, telemetry and other runtime behavior. Keep environment-specific connection material outside source.

An entity maps a table, view or stored procedure; it controls source mapping, exposed actions, role permissions, field inclusion/exclusion, REST/GraphQL naming, relationships and caching. Read [entities configuration](https://learn.microsoft.com/en-us/azure/data-api-builder/configuration/entities) and [runtime configuration](https://learn.microsoft.com/en-us/azure/data-api-builder/configuration/runtime).

```json
{
  "entities": {
    "Product": {
      "source": { "object": "dbo.Product", "type": "table" },
      "rest": true,
      "graphql": true,
      "permissions": [
        { "role": "authenticated", "actions": [ "read" ] }
      ]
    }
  }
}
```

Treat this as a conceptual fragment and validate against the current DAB schema/version. Use an explicit production role model; “anonymous” or “authenticated” alone may be too broad. Limit exposed fields and operations, use database permissions as defense in depth, validate request limits and avoid placing sensitive filter values in logged URLs.

#### REST, GraphQL, relationships and query behavior

- REST supports entity collection/item operations, filtering, ordering, selection, pagination and searching according to current capability. Learn the [REST overview](https://learn.microsoft.com/en-us/azure/data-api-builder/concept/rest/overview).
- GraphQL exposes typed queries/mutations and configured relationships. Prevent unbounded depth/complexity and N+1-style database pressure.
- Relationships declare how source/target fields connect; they do not repair missing relational integrity.
- Stored procedures expose defined operations and results but have different query/composability behavior from tables/views.
- Cache only where staleness, invalidation, tenant/security partitioning and sensitive-data storage are acceptable. Never let one role/tenant receive another's cached representation.
- Pagination must have deterministic ordering; define page-size ceilings and continuation behavior.

Deploy DAB as a versioned application configuration with a managed identity, network restrictions, health probes, safe scaling and telemetry. Run contract, authorization, injection, concurrency, pagination and failure tests against the deployed service.

### Instrument the application and database path

Application Insights captures application requests, dependencies, exceptions, traces and distributed correlation; Log Analytics stores/query telemetry in a workspace. Use [Application Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) and [Log Analytics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview).

Instrument:

- request/operation ID propagated from API through database and model calls;
- endpoint/operation name and result, not raw sensitive payload;
- database dependency duration/failure and safe query identifier;
- external model endpoint/model/deployment/version, latency, status, tokens/cost where available;
- DAB request/auth/throttle/cache behavior;
- business freshness/completeness and embedding coverage/version;
- deployment version/commit and feature flag.

Alert from a user-impact symptom plus a diagnostic signal, with owner and runbook. Example: p95 API latency plus database CPU/waits, or retrieval empty-result rate plus embedding backlog. Avoid high-cardinality dimensions and secret/PII logging.

### Select a change mechanism from semantics

| Mechanism | Returns/does | Strong fit | Main caution |
|---|---|---|---|
| Change Tracking | keys/version for changed rows; read current row separately | synchronization needing latest state, lower capture detail | retention gap, deletes and race-safe synchronization algorithm |
| Change Data Capture | historical row-change data with operation/LSN metadata | incremental ETL/audit-like change feed requiring values | cleanup/retention, capture lag and platform support |
| Change Event Streaming | streams change events to supported event infrastructure | event-driven near-real-time integration | preview/support, ordering/replay/schema and delivery semantics |
| Azure Functions SQL trigger | invokes function from tracked database changes | serverless processing with managed binding | scaling, lease/state, at-least-once/idempotency and poison/failure handling |
| Logic Apps SQL connector | workflow trigger/action over SQL | low-code approvals/integration and connector-supported polling | polling interval, connector limits, identity, duplicates and long workflows |
| DML trigger | synchronous code inside source transaction | small invariant/audit operation requiring same atomic transaction | latency, blocking, recursion and integration availability |

Implement Change Tracking with version capture and a transactionally safe enumeration window; if `CHANGE_TRACKING_MIN_VALID_VERSION` has advanced beyond the consumer's watermark, reinitialize rather than silently missing changes. Review [work with Change Tracking](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/work-with-change-tracking-sql-server?view=sql-server-ver17).

CDC exposes capture tables/functions and cleanup; consumers persist the last successfully committed LSN and handle update before/after semantics. Read [Change Data Capture](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-ver17).

CES publishes changes to an event stream. Design consumer-group/checkpoint, key/order, schema evolution, duplicate/idempotency, retention/replay, backpressure and monitoring. Use the current [Change Event Streaming overview](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/change-event-streaming/overview?view=sql-server-ver17).

> **Current transition — verify before configuring:** As of August 15, 2026, new Azure SQL Database and Fabric SQL database CES stream groups must use the Kafka-based `AzureEventHubs` option. Older AMQP/Kafka option values are deprecated where still accepted on SQL Server 2025 and Managed Instance; new implementations should use the current Kafka option. Follow the official [AMQP deprecation notice](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/change-event-streaming/amqp-deprecation) for target-specific migration steps.

For serverless/low-code consumers, inspect [Azure Functions SQL trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-trigger) and [Azure Logic Apps SQL connector](https://learn.microsoft.com/en-us/azure/connectors/connectors-create-api-sqlazure). Neither removes the need for idempotent processing, persisted progress and reconciliation.

> **Related item:** An event is not “exactly once” because a connector hides retries. Give each business/change event a stable identity, make the sink idempotent, commit progress with output where possible and reconcile source-to-target.

---

## 4. Implement AI capabilities in database solutions (25–30%)

### Design an AI data contract before choosing syntax

A useful AI-ready relational model keeps provenance and lifecycle visible:

```text
Document(DocumentId, source URI, source version/hash, ACL, updated time)
Chunk(ChunkId, DocumentId, ordinal, text, token count, metadata JSON)
Embedding(ChunkId, model/deployment, model version, dimensions, vector, generated time, source hash)
RetrievalRun(query hash, filters, method/index version, candidates/scores, latency)
AnswerRun(model/deployment, prompt version, citations, safety result, token/cost/latency)
```

This permits selective re-embedding, permission-aware retrieval, stale-vector detection, evaluation and rollback. The vector column alone does not show which source or model produced it.

Define:

- business use case and unacceptable answer/failure;
- approved source boundary, classification and row/document ACL;
- chunking method and overlap;
- embedding model/deployment, output type and fixed dimensions;
- freshness/backfill and delete propagation;
- retrieval filters, exact/approximate choice, top-k and hybrid fusion;
- answer model, prompt/output schema, citations and safety controls;
- offline relevance set and online quality/latency/cost signals.

### Configure external model access

An external model object encapsulates supported endpoint/model metadata and credential association so SQL AI functions can call an embedding or completion model. Follow [`CREATE EXTERNAL MODEL`](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-model-transact-sql?view=sql-server-ver17) for exact target syntax and supported providers.

Evaluate the model against the actual operation:

| Dimension | Questions |
|---|---|
| Modality | Does it accept/return the required text, image, audio or other form, and how is nontext content represented before SQL processing? |
| Language | Does measured quality meet the need for every supported language and mixed-language query/document pair? |
| Size/capability | Does a larger model's quality justify its latency, quota and cost; can a smaller approved model meet the structured task? |
| Context/output | Are input/context and output limits sufficient after chunking, prompt and response schema overhead? |
| Structured output | Can it reliably produce a constrained JSON schema, and does application/SQL validation reject malformed or unsafe output? |
| Governance | Are region, retention, content filters, version lifecycle, identity/network and data classification acceptable? |

For multimodal or multilingual choices, build representative evaluation cases rather than extrapolating from an English text demo. Model size is not the same as embedding dimensionality or context window.

Design for:

- a named model deployment and expected output type/dimensions;
- managed identity or protected database-scoped credential;
- least privilege to create/use/alter model objects;
- endpoint network reachability, quota, rate limit, timeout and region/data handling;
- structured output/schema when the completion must be machine-consumed;
- model and prompt version recorded with generated data;
- safe rotation and a test that detects dimension/model mismatch before corrupting the index population.

Never assume the display name identifies immutable model behavior. A deployment can be repointed or upgraded. Pin what the provider supports, run evaluation before change and preserve the provenance required to rebuild.

> **Related item:** Model permissions and database permissions form one chain. A principal allowed to run a procedure that invokes a model may indirectly export selected database data to that endpoint even without direct endpoint credentials.

### Chunk and generate embeddings

Embeddings convert meaning into fixed-length numeric vectors. Similar meanings should be near one another under the selected metric, but scores are model- and corpus-dependent; they are not universal percentages.

Use [`AI_GENERATE_CHUNKS`](https://learn.microsoft.com/en-us/sql/t-sql/functions/ai-generate-chunks-transact-sql?view=sql-server-ver17) where supported to split input with configured strategy/size/overlap, or chunk in the application/ETL layer when format-aware parsing, advanced tokenization or provider portability is needed. Preserve headings, source anchors and ACL metadata. Too-large chunks dilute relevance and consume context; too-small chunks lose meaning and increase vector/count/cost. Measure rather than copy a universal size.

Use [`AI_GENERATE_EMBEDDINGS`](https://learn.microsoft.com/en-us/sql/t-sql/functions/ai-generate-embeddings-transact-sql?view=sql-server-ver17) or a controlled external application to create vectors. The SQL operation still depends on endpoint availability and can be costly; avoid a synchronous model call in a hot user transaction.

```sql
-- Conceptual pattern. Verify exact syntax, preview state, model object and dimensions.
UPDATE c
SET Embedding = AI_GENERATE_EMBEDDINGS(c.ChunkText USE MODEL ApprovedEmbeddingModel),
    EmbeddedAt = SYSUTCDATETIME(),
    SourceHashAtEmbedding = c.SourceHash
FROM dbo.Chunk AS c
WHERE c.Embedding IS NULL
   OR c.SourceHashAtEmbedding <> c.SourceHash;
```

Batch with a durable status such as pending/in-progress/succeeded/failed, bounded concurrency and retry classification. A timeout can be ambiguous; make the update idempotent. Quarantine permanent failures and reconcile counts: eligible chunks, current embeddings, wrong dimensions/model, stale source hash and errors.

### Maintain embeddings when source data changes

Choose a mechanism from scale and latency:

- **Trigger:** record a cheap outbox/work item in the source transaction; do not normally call the external model synchronously from the trigger.
- **Change Tracking:** detect changed keys and read the current content; handle deletes and expired retention window.
- **CDC:** consume detailed value changes/LSN where historical sequencing matters.
- **Azure Functions or Logic Apps:** react/poll through managed integration with idempotency and poison handling.
- **CES:** stream change events where current preview/platform support and semantics meet the need.
- **Microsoft Foundry pipeline/application job:** orchestrate parsing, safety, model call, evaluation and writeback for a richer AI workflow.

Use delete/tombstone processing so deleted or newly restricted text cannot remain retrievable. Re-embed when source hash, chunker, embedding model/version or dimensions change. Blue/green embedding columns/tables let an evaluation approve a new model before switching retrieval and then retiring the old index.

**Current naming:** Current documentation calls the platform **Microsoft Foundry**. Older material may say **Azure AI Foundry** or **Azure AI Studio**. Treat those as historical names and verify that UI, SDK, endpoint and identity instructions still apply. The current [RAG concepts documentation](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation) provides the platform context.

> **Related item:** A database transaction cannot make the external model call and local write atomically commit together. Use an outbox/state machine, stable work key and reconciliation rather than pretending there is a distributed transaction.

### Store vectors with an explicit contract

The native [`vector` data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type?view=sql-server-ver17) stores a fixed dimension and base type. On the checked documentation, maximum dimensions were 1,998 and some base-type/platform combinations remained preview. Verify current limits.

Store alongside the vector:

- model/deployment and version;
- dimensions/base type and distance metric intended;
- source/chunk hash and generated timestamp;
- status/error and tenant/ACL/filter metadata;
- normalized content language/type where relevant.

Prevent mixed dimensions or models in one search population. Vector serialization in drivers/APIs must preserve order, numeric range and dimensionality. Encrypt and authorize vectors according to the source sensitivity; embeddings can leak attributes and are not automatically anonymous.

The [vector functions reference](https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-functions-transact-sql?view=sql-server-ver17) is the current inventory. Know distance/similarity calculation and normalization implications rather than memorizing only syntax.

- `VECTOR_NORMALIZE` produces a unit vector under the supported norm and can make intended cosine/dot-product behavior explicit; do not normalize blindly if the model/metric requires magnitude.
- `VECTORPROPERTY` inspects properties such as dimensions/base type as currently supported; use it to validate data and detect an incompatible model output before indexing/search.
- `VECTOR_DISTANCE` performs exact comparison for the chosen metric.
- `VECTOR_SEARCH` uses the supported approximate search path/index. Its current syntax and platform restrictions are preview-sensitive.

### Choose exact or approximate vector search

**Exact nearest-neighbor (ENN)** calculates distance over all eligible vectors and returns the true nearest values for that metric. It is simple and provides ground truth but becomes expensive as the candidate set grows.

**Approximate nearest-neighbor (ANN)** searches an index to reduce latency/compute with a recall tradeoff. It fits larger, repeated low-latency workloads after relevance testing. SQL's current vector indexes use platform-specific DiskANN support; follow [`CREATE VECTOR INDEX`](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-vector-index-transact-sql?view=sql-server-ver17) and [`VECTOR_SEARCH`](https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-search-transact-sql?view=sql-server-ver17).

```sql
-- Exact conceptual pattern; check the current VECTOR_DISTANCE signature.
SELECT TOP (@k)
       ChunkId,
       ChunkText,
       VECTOR_DISTANCE('cosine', Embedding, @query_vector) AS distance
FROM dbo.Chunk
WHERE TenantId = @tenant_id
ORDER BY distance;
```

Choose distance metric to match model guidance:

- cosine compares direction and is common for text embeddings;
- dot product depends on magnitude unless vectors/model normalize appropriately;
- Euclidean measures straight-line distance.

Lower distance versus higher similarity semantics vary by function. Do not sort the wrong direction. Evaluate top-k recall, precision/nDCG/MRR as appropriate, p50/p95 latency, CPU/IO, index size/build time, write cost and filter selectivity.

#### Current vector-index constraints

**VERIFY CURRENT:** As of August 31, 2026, vector index/search features were preview and support differed across SQL Server 2025, Azure SQL Database and Fabric SQL database. Current documentation described DiskANN as the supported index family and a newer index version for Azure SQL/Fabric. Older syntax/index formats were deprecated. Check before using:

- current `CREATE VECTOR INDEX` syntax and supported metric/type/dimensions;
- minimum populated non-null vector count and required primary/clustered index;
- DML and iterative-filter support for the current index version;
- partitioning and platform restrictions;
- current `SELECT TOP (...) WITH APPROXIMATE`/`VECTOR_SEARCH` syntax;
- rebuild/recreate requirements after format change;
- dacpac/bacpac exclusion and post-deployment recreation.

Build an ENN ground-truth set before tuning ANN. If a selective tenant/category filter is applied after ANN candidate selection, recall can collapse. Prefer supported pre/iterative filtering or search within a properly bounded authorized candidate set, and test worst-case tenants.

> **Related item:** Security filtering must happen before an unauthorized row can become prompt context. Filtering results only after top-k can both leak data and return too few authorized candidates.

### Combine full-text, vector and relational filtering

Full-text search builds language-aware indexes for terms, inflection and proximity; learn [full-text search](https://learn.microsoft.com/en-us/sql/relational-databases/search/full-text-search?view=sql-server-ver17) and its [setup workflow](https://learn.microsoft.com/en-us/sql/relational-databases/search/get-started-with-full-text-search?view=sql-server-ver17).

| Retrieval | Strong at | Weakness |
|---|---|---|
| Relational filters | exact tenant, date, product, status and authorization | semantic meaning |
| Full-text/lexical | exact terminology, identifiers, rare names and phrase/proximity | paraphrases and conceptual similarity |
| Vector | semantic similarity and paraphrase | exact identifiers, model bias, opaque score thresholds |
| Hybrid | combines lexical and semantic candidates | fusion/tuning complexity and duplicate handling |

A practical hybrid query obtains lexical and vector candidate ranks, applies authorized relational filters and combines rankings using reciprocal rank fusion (RRF):

```text
rrf_score(document) = sum(1 / (k + rank_in_each_result_list))
```

RRF works with ranks rather than incomparable raw BM25/distance scores. Choose fusion constant and per-source candidate count through evaluation. SQL may require application/T-SQL composition rather than a single built-in hybrid operator; the [vector search architecture guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/vector-search) and [intelligent SQL search module](https://learn.microsoft.com/en-us/training/modules/design-implement-intelligent-search-with-sql/) provide decision context.

### Build retrieval-augmented generation as a controlled pipeline

RAG retrieves approved external knowledge and includes selected context in a model request. It can improve grounding and freshness but does not guarantee truth.

1. Authenticate the user/workload and resolve permitted tenant/document filters.
2. Normalize the question and generate a query embedding with the same approved embedding model/version.
3. Retrieve lexical/vector candidates with ACL and business filters applied before context assembly.
4. Rerank/deduplicate if required; enforce token/record/source-diversity budgets.
5. Assemble prompt with system policy, question, untrusted labeled context and source identifiers.
6. Invoke the approved completion model with structured output where possible.
7. Validate JSON/schema, citations and safety/business rules; refuse or fall back when evidence is insufficient.
8. Record privacy-safe trace, versions, candidate/citation IDs, latency and cost; collect evaluation feedback.

Test prompt injection inside retrieved documents, conflicting sources, stale/deleted ACLs, no relevant result, adversarial query, partial endpoint failure and invalid model JSON. Keep model-generated SQL read-only/parameterized and policy-checked unless a separately authorized workflow confirms a write.

#### Invoke external REST endpoints from SQL

[`sp_invoke_external_rest_endpoint`](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql?view=sql-server-ver17) makes an HTTPS request to allowed endpoints and returns response details. SQL Server 2025/Managed Instance and Azure SQL/Fabric can differ in enablement and credential handling. Use a managed identity/database-scoped credential, grant `EXECUTE ANY EXTERNAL ENDPOINT` narrowly, parameterize/escape JSON with SQL JSON functions, validate response status/body and avoid holding locks while waiting.

```sql
DECLARE @response nvarchar(max);
DECLARE @payload nvarchar(max) = JSON_OBJECT(
    'messages': JSON_ARRAY(JSON_OBJECT('role':'user', 'content':@approved_prompt))
);

-- Conceptual call: endpoint, credential name, headers and response shape vary.
EXEC sys.sp_invoke_external_rest_endpoint
     @url = @approved_url,
     @method = 'POST',
     @payload = @payload,
     @response = @response OUTPUT;

SELECT JSON_VALUE(@response, '$.response.status.http.code') AS HttpStatus;
```

This creates an outbound-data/exfiltration path. Restrict endpoint/permission and data, and consider an application/service boundary when retries, asynchronous work, secrets, policy, streaming, complex observability or provider portability are important.

> **Related item:** “Inside the database” does not make a model call transactional, private, fast or free. External latency/quota/failure remains external; design the user transaction and recovery accordingly.

---

## 5. Integrated design scenarios

### Scenario A: tenant-safe support RAG

**Requirements:** customer-support agents search only their tenant's current product manuals and tickets; exact error codes matter; responses need citations; source changes appear within 15 minutes.

1. Model document, chunk, embedding and ACL separately; store source/version/hash, tenant and model metadata.
2. Use Change Tracking or an outbox to enqueue changed/deleted rows; a Functions worker chunks and embeds with managed identity.
3. Build full-text plus vector retrieval. Apply tenant/ACL and active-version filters before top-k; fuse lexical and semantic ranks.
4. Invoke the approved completion model with retrieved text labeled untrusted and demand structured answer plus cited chunk IDs.
5. Validate citations belong to retrieved authorized chunks; refuse when evidence score/coverage is inadequate.
6. Monitor change watermark/backlog, embedding coverage/staleness, recall test set, p95 latency, empty results, citation validity and cost.

**Failure trap:** generating embeddings synchronously in a source-table trigger makes the user's transaction depend on the model endpoint. Record durable work in the transaction and process it asynchronously.

### Scenario B: governed database API and deployment

**Requirements:** expose products/orders through REST and GraphQL, hide cost fields, isolate tenants, deploy schema and API configuration through CI/CD with no stored password.

1. Put schema, RLS predicate/policy, views/procedures, DAB config and tests in source control; build a dacpac.
2. Use a managed identity for pipeline and DAB. Grant DAB only approved views/procedures/actions; keep base-table grants minimal.
3. Set tenant context from validated identity claims on every connection and test pooled-connection reuse.
4. Configure DAB roles, excluded fields, relationships, deterministic pagination and request limits; avoid shared tenant-unsafe cache.
5. Generate/review deployment report/script; test migration from current production-sized schema and block data loss.
6. Correlate DAB request, SQL query and deployment version in Application Insights/Log Analytics; audit denied and sensitive operations.

**Failure trap:** removing a field from the GraphQL schema does not protect it if the same principal can query the base table through another connection.

### Scenario C: high-volume operational database with event integration

**Requirements:** point-order workload plus daily analytics, low blocking, event-driven fulfillment and five-year tamper-evidence for approved records.

1. Use narrow rowstore transaction tables and measured covering indexes; add a nonclustered columnstore only after proving analytical benefit/write cost.
2. Select row-versioning isolation where consistency requirements fit; keep transaction boundaries short and use idempotency keys.
3. Use an updatable or append-only ledger design only for rows requiring tamper evidence; externalize and verify digests.
4. Publish order change through current CES or an outbox/CDC architecture based on platform/support. Key events by order and make fulfillment idempotent.
5. Track Query Store regressions, blocking/deadlock graphs, CES lag/failure and source-to-consumer reconciliation.
6. Partition/archive only when lifecycle scale justifies it; test partition elimination and aligned maintenance.

**Failure trap:** ledger detects later tampering but does not prove the original order was valid or prevent an authorized application from inserting a false value.

---

## 6. Hands-on labs

Use disposable databases, synthetic data and a budget. Record platform/build/compatibility level, DDL/code/config, identities, plans/query IDs, API/model requests, metrics, failures, cleanup and links to the exact documentation used.

### Lab 1: relational, JSON, temporal and graph design

1. Model orders, events and relationships with explicit grain, keys, constraints and appropriate types.
2. Compare rowstore and columnstore plans for transactional lookups versus a large aggregation.
3. Store a variable event payload as JSON; extract/project with `OPENJSON`, construct JSON and add a supported JSON access index/computed-column alternative.
4. Create a disposable system-versioned temporal table and answer an as-of query; prove history growth/retention behavior.
5. Create graph node/edge tables and a `MATCH` query; implement the same fixed relationship relationally and compare clarity/constraints.
6. Document platform-specific unsupported/preview features instead of skipping them silently.

### Lab 2: advanced T-SQL and programmable objects

1. Write deterministic ranking/running-total window queries with ties and nulls.
2. Build a recursive hierarchy CTE with cycle/maximum-depth protection.
3. Compare correlated `EXISTS`/`NOT EXISTS` to an equivalent join/pre-aggregation and inspect plans.
4. Implement JSON, regex and fuzzy matching on controlled data; measure false positives and candidate bounding.
5. Create a view, inline TVF and stored procedure with typed parameters and safe error/transaction handling.
6. Write a multirow-safe trigger that only records an outbox row, then explain when it should be replaced.

### Lab 3: identity, encryption and fine-grained access

1. Connect an application/workload with Microsoft Entra managed identity and create the least-privileged database user/role.
2. Implement RLS by tenant and masking for one display field; test two tenants, pooled connection reuse, owner/admin and denied writes.
3. Compare TDE boundary with an Always Encrypted column in a supported client; record which queries/operators work.
4. Grant one procedure/interface without base-table access and test ownership-chain/dynamic-SQL behavior.
5. Produce audit evidence for successful and denied sensitive operations.
6. Threat-model model endpoint, DAB and MCP access paths as possible data export paths.

### Lab 4: plans, Query Store, blocking and deadlocks

1. Generate data with skew and parameter-sensitive selectivity; capture Query Store history and actual plans.
2. Create one non-SARGable query, implicit conversion, bad estimate and spill; correct each one separately and compare logical reads/CPU/latency.
3. Reproduce blocking with a long transaction; identify head blocker and wait resource without guessing.
4. Reproduce a safe deadlock; interpret the graph, make access order/index/transaction correction and verify.
5. Compare a row-versioned isolation option with locking behavior and monitor version-store implications.
6. Save before/after evidence and a rollback condition for any forced plan/hint.

### Lab 5: database project and controlled deployment

1. Create an SDK-style SQL project from a small database; build a dacpac and enable useful analysis rules.
2. Add constraints, RLS, view/procedure and test fixtures on a branch; intentionally create and resolve an object conflict.
3. Deploy to disposable dev, introduce drift, detect it with schema compare and reconcile the intended state.
4. Test a destructive column change against realistic data; generate/review script and enforce a data-loss gate.
5. Publish the same artifact with a non-personal identity to a second environment; record artifact hash and output.
6. Add an idempotent post-deployment task for a currently unsupported artifact such as a vector index, then prove rerun behavior.

### Lab 6: Data API builder and observability

1. Expose approved table/view/procedure entities through REST and GraphQL with explicit roles/actions/fields.
2. Add a relationship, filter/search, deterministic pagination and bounded page size.
3. Test anonymous/authenticated/tenant roles, injection-like input, missing/invalid token and direct database denial.
4. Evaluate caching for a public entity and reject it for tenant-sensitive data unless partitioning/invalidation are proven.
5. Deploy with managed identity and instrument requests, dependencies, exceptions and version in Application Insights.
6. Create a Log Analytics query and alert for p95 latency plus database dependency failures; verify a synthetic incident.

### Lab 7: change processing and embedding maintenance

1. Generate inserts, updates and deletes and consume them separately through Change Tracking and CDC.
2. Persist watermarks safely, simulate retention expiry and prove reinitialization/reconciliation.
3. Implement an outbox/Functions worker that chunks and embeds changed content with idempotent work IDs.
4. Simulate timeout, rate limit, bad dimensions, poison content and deletion; inspect retry/quarantine/tombstone behavior.
5. If eligible, configure current CES to Event Hubs using the nondeprecated option and prove consumer checkpoint/replay/duplicate handling.
6. Compare latency, captured detail, operating state and failure semantics; select one mechanism from requirements.

### Lab 8: vector, hybrid and grounded-answer evaluation

1. Create a synthetic/document corpus with source version, ACL, chunk and model metadata; build a labeled relevance question set.
2. Generate embeddings with a supported model and verify dimensions/completeness/source hashes.
3. Implement ENN cosine retrieval as ground truth; measure relevance and latency.
4. Create a current supported vector index and ANN query where eligible; compare recall/latency at several candidate counts and filters.
5. Add full-text retrieval and RRF; test exact identifiers, paraphrases, conflicting documents and unauthorized high-score rows.
6. Invoke a completion model through an approved application or external REST path; require structured answer and citations.
7. Test prompt injection in retrieved text, no evidence, invalid JSON, endpoint failure and stale/deleted ACL.
8. Record retrieval/answer model and prompt versions, citation validity, relevance, p95 latency and cost; remove endpoints/indexes/resources.

---

## 7. Original knowledge checks

These are original prompts, not recalled exam questions. Answer each with requirement, decision, implementation, evidence, failure mode and correction.

1. Choose Azure SQL Database, Managed Instance, SQL Server 2025 or Fabric SQL database for four different constraints. Which feature assumptions must be rechecked?
2. Define row grain, primary key and alternate business key for an order line. Which constraints express each rule?
3. Compare rowstore, clustered columnstore, nonclustered columnstore and memory-optimized tables for write-heavy and analytical workloads.
4. Why can a foreign key improve integrity without improving the child lookup plan?
5. Compare identity and sequence behavior, including gaps and multi-table use.
6. When does partitioning improve lifecycle operations but fail to improve a query?
7. Compare temporal and ledger guarantees. Which one is neither a backup nor proof that the input was true?
8. When does a graph model improve traversal, and what Fabric integration limitation must be checked?
9. Choose a relational column, JSON text/native type or normalized child table for three variable-data cases.
10. Compare `JSON_VALUE`, `JSON_QUERY`, `OPENJSON`, JSON constructors and `JSON_CONTAINS`.
11. Why can an inline TVF optimize differently from a multi-statement TVF or scalar function?
12. What makes a trigger multirow-safe, and why should an external model call not normally run inside it?
13. Explain anchor, recursive member, termination and cycle protection in a hierarchy CTE.
14. Why do a deterministic window rank and running total require deliberate `ORDER BY` ties and frame?
15. When does `NOT IN` return a surprising result that `NOT EXISTS` avoids?
16. Design a safe fuzzy entity-match pipeline; why is one edit-distance threshold not identity proof?
17. Which review/tests are mandatory before accepting AI-generated SQL?
18. How can a malicious database instruction or retrieved row influence an MCP-enabled assistant?
19. Compare TDE, Always Encrypted, masking, RLS and auditing against one concrete threat model.
20. How can connection pooling break tenant RLS even when the predicate is correct?
21. Why does a managed identity still need database permissions and endpoint restrictions?
22. Compare read committed locking, RCSI, snapshot and serializable for blocking and consistency.
23. Why are automatic retries unsafe for an ambiguous non-idempotent write?
24. Which plan evidence distinguishes bad cardinality, spill, lookup amplification and non-SARGable access?
25. Compare blocking with a deadlock; what evidence and remediation differ?
26. What belongs in SQL project source, the dacpac, protected pipeline configuration and post-deployment tasks?
27. How do schema compare and deployment report help detect drift and destructive change?
28. Design DAB entity roles/fields/actions for public products and tenant orders. Where is defense in depth enforced?
29. Why can caching or GraphQL nesting create security/performance issues even when the API works functionally?
30. Compare Change Tracking, CDC, CES, Functions SQL trigger, Logic Apps and DML trigger for one change-integration need.
31. How does the August 2026 CES Event Hubs transition change a new configuration?
32. Which metadata proves an embedding is current and compatible with a vector column/index?
33. Compare ENN and ANN. How do you measure ANN recall rather than assume it?
34. How do cosine, dot-product and Euclidean semantics affect model/search compatibility and sort direction?
35. Why can post-filtering ANN results violate both recall and tenant security expectations?
36. Design a hybrid RAG evaluation covering exact terms, paraphrase, ACL, prompt injection, citation, latency and cost.

---

## 8. Final readiness checklist

- [ ] I can map every March 12, 2026 objective to a section, lab and evidence artifact.
- [ ] I can distinguish Azure SQL Database, Managed Instance, SQL Server 2025 and Fabric SQL database support without assuming parity.
- [ ] I can design tables, data types, constraints, sequences, partitions and rowstore/columnstore/memory-optimized indexes from workload evidence.
- [ ] I can select and operate temporal, ledger, graph, external and JSON designs with their boundaries.
- [ ] I can build views, functions, procedures and multirow-safe triggers with explicit transaction/error behavior.
- [ ] I can write CTE/window/correlated, JSON, regex, fuzzy and graph queries and inspect their plans/correctness.
- [ ] I can use GitHub Copilot/Copilot in Fabric, instruction files and MCP endpoints with reviewed output and least privilege.
- [ ] I can apply Entra/passwordless identity, encryption, masks, RLS, permissions and auditing at the correct boundary.
- [ ] I can configure safe connections, concurrency/isolation, retry and idempotency.
- [ ] I can use plans, DMVs, Query Store and Query Performance Insight to resolve bottlenecks, blocking and deadlocks.
- [ ] I can build/test/version a SQL project, resolve conflicts, detect drift and safely deploy one dacpac through environments.
- [ ] I can configure, secure, deploy and observe DAB REST/GraphQL entities, relationships, cache, pagination, filter and search.
- [ ] I can select and operate Change Tracking, CDC, current CES, Functions SQL trigger and Logic Apps by semantics.
- [ ] I can configure external models and maintain chunks/embeddings through update/delete/model changes.
- [ ] I can store vectors, choose metric, implement ENN/ANN/vector indexes and verify current preview/platform constraints.
- [ ] I can combine relational, full-text and vector retrieval with RRF and authorization before context assembly.
- [ ] I can invoke external REST/model endpoints securely and validate structured JSON results.
- [ ] I can build/evaluate RAG for grounding, citations, ACL, prompt injection, latency and cost.
- [ ] I have rechecked blueprint, lifecycle, practice link, platform Applies to sections, compatibility levels, preview states and CES transition immediately before the exam.

---

## Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick one current primary path, build the labs, and use targeted references or practice for gaps. Times are page-published when available; otherwise they are clearly labeled estimates. Catalogs, access, duration, price and alignment change. DP-800 is new, so several established vendors did not yet have a dedicated full certification path on the pages found; map broader SQL Server 2025 material to the March 2026 blueprint. Avoid dumps or products claiming recalled/live exam questions.

### Start with Microsoft

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official DP-800 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-800) | Public | 30–60 min | Authoritative objectives, weights and lifecycle |
| [DP-800T00 Microsoft Learn course](https://learn.microsoft.com/en-us/training/courses/dp-800t00) | Public self-study; paid instructor option | 3 instructor-led days; 18h22 displayed Learn paths plus labs | Primary structured coverage of all three domains |
| [Design and develop database solutions](https://learn.microsoft.com/en-us/training/paths/design-develop-database-solutions/) | Public | 7h11 displayed / 4 modules | Schema, objects, T-SQL and AI-assisted development |
| [Secure, optimize, and deploy database solutions](https://learn.microsoft.com/en-us/training/paths/secure-optimize-deploy-database-solutions/) | Public | 7h31 displayed / 4 modules | Security, performance, projects, APIs, monitoring and change |
| [Implement AI capabilities in database solutions](https://learn.microsoft.com/en-us/training/paths/implement-ai-capabilities-database-solutions/) | Public | 3h40 displayed / 3 modules | Models, embeddings, vectors, search and RAG |
| [Microsoft Learning DP-800 course labs](https://microsoftlearning.github.io/mslearn-sql-developer/) | Public; Azure/SQL resources may cost | 12–24 hours for all 11 labs (estimate) | Official hands-on companion; retain evidence and clean up resources |
| [AI Skills Navigator DP-800 Practice Assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-f7c226fff388981b97e2bafd239786aba2d62e74bf8e3d50b04d341899bd55f4) | Free account; sign-in required | 45–90 min per attempt plus review (estimate) | Official readiness diagnostic and gap finding |
| [Microsoft Reactor DP-800 series](https://developer.microsoft.com/en-us/reactor/series/s-1683/) | Public/on demand | About 7 hours for 7 sessions; 3–5 hours selectively (estimate) | Domain-by-domain instruction and demonstrations |
| [Microsoft exam sandbox](https://aka.ms/examdemo) | Public | 20–30 min | Exam interface familiarity, not technical preparation |

### Courses, books and video

| Resource | Access | Estimated time | Best use and freshness note |
|---|---|---:|---|
| [O'Reilly SQL Server 2025 Unveiled](https://www.oreilly.com/library/view/sql-server-2025/9798868818479/) | Paid subscription/book | 10–15 hours selectively (estimate) | Current depth for SQL AI, vector, JSON, regex, CES, REST, security and Fabric; map chapters to DP-800 rather than reading every page |
| [Pluralsight SQL Server 2025 Fundamentals path](https://www.pluralsight.com/paths/sql-server-2025-fundamentals) | Paid/trial depending plan | 6 hours displayed / 5 courses | Current SQL Server 2025 engine, T-SQL, security, performance and hybrid foundation; not a complete DP-800 path |
| [Pluralsight Optimizing Vector Search in SQL Server 2025](https://www.pluralsight.com/courses/sql-server-25-optimize-vector-search) | Paid/trial depending plan | 1h19 displayed | Focused vector data, distance and performance supplement; verify preview syntax |
| [Udemy DP-800 Exam Prep: Microsoft SQL Server AI Developer](https://www.udemy.com/course/dp-800-exam-prep-microsoft-sql-server-ai-developer/) | Paid; price varies | 19h6 displayed / 170 lectures | Dedicated course updated June 2026; compare every preview statement to current Microsoft docs |
| [Microsoft Reactor YouTube channel](https://www.youtube.com/@MicrosoftReactor) | Public | 3–8 hours selectively (estimate) | Search DP-800, SQL Server 2025, vector and AI-enabled SQL; prefer recent sessions |

### Practice, samples and implementation references

| Resource | Access | Estimated time | Best use and caution |
|---|---|---:|---|
| [Microsoft DP-800 Practice Assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-f7c226fff388981b97e2bafd239786aba2d62e74bf8e3d50b04d341899bd55f4) | Free account | 45–90 min per attempt plus remediation (estimate) | Use first as the official diagnostic; do not memorize answers |
| [Whizlabs DP-800 SQL AI Developer Associate](https://www.whizlabs.com/dp-800-microsoft-sql-ai-developer-associate/) | Paid catalog; one free and two paid quizzes listed | 2–4 hours including explanation review (estimate) | Practice supplement; verify objectives and reject recalled/live-question claims |
| [Azure SQL AI samples](https://github.com/Azure-Samples/SQL-AI-samples) | Public | 6–15 hours selectively (estimate) | Official examples for embeddings, vector search and AI-enabled SQL; inspect platform/version prerequisites |
| [Azure SQL database chat with Semantic Kernel](https://github.com/Azure-Samples/azure-sql-db-chat-sk) | Public | 3–6 hours (estimate) | End-to-end database chat/RAG architecture; update dependencies and threat-model before reuse |
| [Azure SQL external REST endpoint samples](https://github.com/Azure-Samples/azure-sql-db-invoke-external-rest-endpoints) | Public | 2–4 hours (estimate) | Endpoint, credential and JSON call patterns; use only approved endpoints and synthetic data |
| [Microsoft SQL Server samples](https://github.com/microsoft/sql-server-samples) | Public | 4–12 hours selectively (estimate) | Relational, performance and engine experimentation; select current 2025-relevant samples |
| This guide's eight labs | Azure/SQL/model resources; costs vary | 24–45 hours (estimate) | Cross-domain implementation, failure, security, deployment and evaluation evidence |

No dedicated MeasureUp DP-800 product was found in the public catalog checked on August 31, 2026. Recheck the vendor later rather than substituting an unrelated exam product. No one practice vendor is authoritative; use explanations to identify a source/documentation gap.

### A practical study sequence

1. Read the official blueprint and map every objective to a platform-supported lab in 30–60 minutes.
2. Complete the three Microsoft Learn paths or one current structured course; do not stack passive courses.
3. Build Labs 1–4 and remediate SQL design, security and performance with exact reference pages.
4. Build Labs 5–8 and retain artifact/deployment, API/telemetry, change/embedding and retrieval-evaluation evidence.
5. Take the official Practice Assessment once; remediate by objective and implementation, not answer memory.
6. Use one ethical third-party practice resource only if its explanations are current and source-based.
7. Recheck the official guide, credential page, Applies to sections, preview notices, model/vector limits and CES transition immediately before the exam.

---

*This independent guide is based only on public sources and original synthesis. It is not affiliated with or endorsed by Microsoft, GitHub, HashiCorp, or any learning vendor.*
