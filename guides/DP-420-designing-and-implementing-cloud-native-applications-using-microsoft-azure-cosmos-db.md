---
exam_code: DP-420
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-420
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# DP-420 Designing and Implementing Cloud-Native Applications Using Microsoft Azure Cosmos DB Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dp-420-coverage-record). The [official DP-420 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-420) is authoritative.

**Current baseline:** Skills measured as of July 21, 2026.<br>
**Upcoming blueprint change:** None announced as of August 31, 2026.<br>
**Lifecycle status:** Active; no retirement or replacement was announced on the official pages checked.<br>
**Exam page:** [Azure Cosmos DB Developer Specialty](https://learn.microsoft.com/en-us/credentials/certifications/azure-cosmos-db-developer-specialty/) · 100-minute assessment · annual renewal for the earned specialty certification.<br>
**Official course:** [DP-420T00 Design and implement cloud-native applications with Microsoft Azure Cosmos DB](https://learn.microsoft.com/en-us/training/courses/dp-420t00) · four instructor-led days.<br>
**Practice:** A free Microsoft Practice Assessment is linked from the credential and study-guide pages.

## How to use this guide

DP-420 is a database-development and distributed-systems exam, not a portal tour. For every design, trace this chain:

```text
access pattern -> item boundary -> partition key -> operation/query -> RU and latency
business invariant -> logical partition -> transaction mechanism -> concurrency condition
user location -> region routing -> consistency guarantee -> failure behavior -> recovery evidence
identity -> network path -> data-plane permission -> SDK request -> diagnostic evidence
source change -> change feed/mirroring/connector -> checkpoint -> target effect -> replay behavior
```

Practice with a current Azure Cosmos DB for NoSQL SDK. C# and Java code can appear in the published audience profile, so learn to recognize SDK object lifetimes, request options, partition-key arguments, pagination, diagnostics, and failure handling even if you write labs in only one language. Record prerequisites, item and partition shape, request charge, latency, status/substatus, retry count, correctness evidence, and cleanup cost for every lab.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes the objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Microsoft's published exam objectives.

## Objective map

| Published domain | Weight | Developer question |
|---|---:|---|
| Design and implement data models | 35–40% | Can the item, partition, throughput, SDK, query, transaction, and server-side design satisfy the known access patterns at scale? |
| Design and implement data distribution | 5–10% | Can the region, consistency, failover, routing, and conflict design meet latency, availability, and durability requirements? |
| Integrate an Azure Cosmos DB solution | 5–10% | Can operational changes reach analytics, search, functions, eventing, and derived models through the right current integration? |
| Optimize an Azure Cosmos DB solution | 15–20% | Can you measure RU and latency, then improve query, index, cache, and change-feed behavior without breaking correctness? |
| Maintain an Azure Cosmos DB solution | 25–30% | Can you observe, secure, restore, move, and deploy the solution repeatably? |

---

## 1. Build the mental model first

### Separate the resource, distribution, and request models

The Azure resource hierarchy is account -> database -> container -> item. The container is the principal unit for partitioning and scalable throughput; an item is uniquely addressed by its `id` plus partition-key value. A database can optionally share provisioned throughput among its containers, but a container still owns its partition-key and indexing policies. Start with the [Azure Cosmos DB resource model](https://learn.microsoft.com/en-us/azure/cosmos-db/resource-model) and [partitioning overview](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview).

Keep these boundaries distinct:

- **Management/control plane:** create accounts, regions, databases and containers; set account networking, default consistency, backup, encryption, failover, and throughput; authorize with Azure RBAC.
- **Data plane:** read/query/write items, consume change feed, execute stored procedures, and manage conflicts; authorize with keys or Azure Cosmos DB native data-plane RBAC.
- **Logical partition:** all items sharing a partition-key value. It is the transaction and targeted-routing boundary for the API for NoSQL.
- **Physical partition:** service-managed compute/storage unit holding ranges of partition-key hashes. Throughput is distributed across physical partitions; applications do not pin an item directly to one.
- **Request unit (RU):** normalized cost of database work. Point-read, query, write, indexing, item size, consistency, and replication choices affect consumed capacity and cost.
- **Client path:** SDK -> preferred region/routing cache -> gateway metadata path and gateway or direct data path -> replica. Client CPU, sockets, DNS, retries, serialization, and region placement can dominate end-to-end latency even when server-side latency is healthy.

The [request-unit model](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units) makes operations comparable, but it is not a latency guarantee. Capture both `RequestCharge` and SDK diagnostics.

### Use an evidence-led design loop

1. List read and write operations with frequency, latency, consistency, item count, selectivity, sort, transaction, and retention requirements.
2. Model the JSON returned or changed by each operation; choose embedding, denormalization, references, and container boundaries.
3. Select a partition-key strategy and project per-key storage, request concentration, fan-out, and growth.
4. Estimate storage and RU/s, then choose serverless or provisioned throughput and manual or autoscale behavior where applicable.
5. Select regions, write topology, consistency, conflict behavior, and SDK preferred regions from SLO/RPO requirements.
6. Define identity, network, encryption, key, backup, logging, alert, and deployment controls.
7. Test with realistic data distribution, concurrency, item sizes, query parameters, failure injection, and region distance.
8. Measure request charge, normalized RU, throttles, diagnostics, latency, replication, storage distribution, and recovery.
9. Change one factor, repeat the same workload, and retain before/after evidence.

> **Related item:** NoSQL schema flexibility moves schema responsibility into the application and governance process. A container accepts varied JSON shapes, but clients, indexes, analytical projections, encryption policies, and change consumers still depend on deliberate schemas and version compatibility.

### Recognize the central tradeoffs

| Choice | Usually improves | Usually costs or constrains |
|---|---|---|
| Embed related data | one-request reads, same-item atomic updates | larger items, duplicated data, broader write contention |
| Reference related data | independent lifecycle, smaller items | extra reads/queries, client joins, consistency coordination |
| Highly distributed partition key | write scale and even RU distribution | fan-out for queries that omit the key |
| Co-locating a transaction | atomic batch/stored procedure in one logical partition | potential hot or oversized partition |
| Broad default indexing | query flexibility | write RU and index storage |
| Narrow indexing | lower write/index cost | unsupported or expensive future query shapes |
| Stronger consistency | simpler read correctness | read RU/throughput, latency, availability constraints |
| Multi-region writes | local writes and regional resilience | conflicts, governance, cost, unsupported combinations |
| Continuous backup | self-service point-in-time restore | feature constraints and possible storage/restore cost |
| Fabric mirroring | near-real-time analytics without transactional RUs | Fabric capacity, source eligibility, schema and security constraints |

---

## 2. Design and implement data models (35–40%)

### Model from access patterns, not relational tables

The authoritative starting point is [data modeling in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/modeling-data). Write an access-pattern table before creating containers:

| Operation | Key/filter and sort | Cardinality/size | Frequency and SLO | Correctness boundary |
|---|---|---:|---:|---|
| Get order | tenant + order ID | one item | very high / low latency | latest accepted order state |
| List recent orders | tenant, status, time descending | tens | high | pagination must be stable enough for UI |
| Update order and outbox record | tenant + order | two items | medium | all succeed or all fail |
| Product lookup | SKU | one item | high | product can change independently |
| Global sales report | time/product/region | millions | periodic | analytics can lag |

Then decide:

- **Embed** bounded child data that is read and updated with the parent, fits item-size/growth limits, and shares lifecycle. One item write is atomic.
- **Denormalize** small, read-heavy values into multiple items when eliminating joins is worth the update fan-out. Define the source of truth and repair/replay process.
- **Reference** independently changing, unbounded, many-to-many, or separately secured entities. Budget the extra point reads or queries.
- **Store multiple entity types in one container** when they share distribution/access needs. Use a discriminator such as `type`, collision-safe IDs, and type-aware index paths. Containers are not relational tables.
- **Use separate containers** when partitioning, throughput, retention, indexing, encryption, access control, or lifecycle materially differs. Cross-container transactions are not provided.

Example aggregate:

```json
{
  "id": "order-1842",
  "tenantId": "northwind",
  "type": "order",
  "schemaVersion": 3,
  "status": "paid",
  "placedAt": "2026-08-30T14:22:11Z",
  "customer": { "id": "c-19", "displayName": "A. Customer" },
  "lines": [
    { "sku": "p-7", "nameAtPurchase": "Widget", "quantity": 2, "unitPrice": 12.50 }
  ]
}
```

The copied name and price preserve the order fact; the customer ID remains a reference for the current profile. This is intentional denormalization, not accidental duplication.

### Design keys, uniqueness, TTL, and versioning

#### `id`, partition key, and unique keys

- `id` is a string and is only unique within a logical partition. A point read needs both `id` and the partition-key value.
- Make IDs stable, deterministic where idempotency needs it, and collision-safe across co-located entity types—for example `order|1842` and `outbox|1842|paid`.
- A partition key is chosen when a container is created and cannot be changed in place. Moving to a new key requires a migration/new container or a supported partition-key-change capability whose constraints must be checked.
- A [unique-key policy](https://learn.microsoft.com/en-us/azure/cosmos-db/unique-keys) enforces uniqueness for specified paths within each logical partition, not globally. It is defined at container creation and increases write RU.

Do not call `id` a relational primary key without qualification. In Azure Cosmos DB for NoSQL the address is effectively `(partitionKey, id)`.

#### Transactional TTL

[Time to live](https://learn.microsoft.com/en-us/azure/cosmos-db/time-to-live) can be enabled at the container and overridden per item. A positive item TTL counts seconds from the last-modified timestamp; `-1` means no expiration when TTL is enabled. Expiration is a background delete and consumes otherwise available throughput under provisioned throughput behavior. Use TTL for ephemeral sessions, telemetry windows, caches, or retention rules—not as a precise scheduler.

Distinguish:

- transactional TTL on operational items;
- analytical TTL for analytical-store retention;
- backup retention, which protects recoverability;
- change-feed retention/mode behavior;
- Fabric warehouse time-travel retention.

They solve different problems.

#### Item and schema versioning

Use a `schemaVersion` and readers that can tolerate known old versions. Common strategies:

- **Lazy/read repair:** transform old items when read; cheap rollout, unpredictable migration completion.
- **Write-new/read-both:** new writers emit the new form while readers accept both; useful for rolling deployment.
- **Change-feed migration:** project changed items into a new form/container; gives checkpointed progress but unchanged historical data needs a backfill.
- **Bulk backfill:** deterministic migration at throughput cost; needs idempotency, checkpoints, throttling, reconciliation, and rollback.

Never reuse a property with an incompatible meaning while mixed application versions are running. Version event payloads and derived models separately from stored aggregate versions.

### Choose a partition-key strategy

A good key has high cardinality, distributes both storage and RU demand, appears in important request paths, supports transaction boundaries, and remains stable. Evaluate **distribution and routing**, not cardinality alone.

For each candidate key, estimate:

```text
items/key × average item size × retention = projected logical-key storage
operations/key/second × RU/operation = projected per-key RU demand
requests without complete key × partitions touched = fan-out exposure
items in one invariant = transactional co-location requirement
```

Test skew at peak, not only average. A million dormant tenants do not offset one tenant receiving most writes.

#### Natural, synthetic, and hierarchical keys

| Strategy | Use when | Watch for |
|---|---|---|
| `/tenantId` | most work is tenant-scoped and tenant sizes/load are bounded | large/noisy tenant can dominate one logical partition |
| `/deviceId` | ingestion and reads are device-scoped | fleet-wide time query fans out; hot device remains hot |
| synthetic `tenantId|bucket` | one natural key is too hot/large | callers must derive bucket; reads may query several buckets |
| random/hash suffix | maximum write spreading is required | point routing needs a lookup or deterministic suffix; reads fan out |
| time bucket | retention and time-window access align | current bucket can be hot; boundary and late-arrival logic |
| hierarchical `/tenantId`, `/userId`, `/sessionId` | prefix routing plus subpartition scale fits access patterns | prefix order is fixed; incomplete prefixes can still touch many ranges |

[Synthetic partition keys](https://learn.microsoft.com/en-us/azure/cosmos-db/synthetic-partition-keys) combine fields or append calculated/random suffixes when no single property distributes and routes well. They add application logic and must be reproducible for targeted operations.

[Hierarchical partition keys](https://learn.microsoft.com/en-us/azure/cosmos-db/hierarchical-partition-keys) support up to three levels. A leading-prefix query can route to the subset belonging to that prefix, while deeper components distribute a large tenant. They do not make arbitrary alternate-key queries targeted. Preserve the most important routing hierarchy in prefix order and verify current SDK/feature limitations.

#### Multiple partition-key access needs

One container has one partition-key definition. When two high-volume patterns need unrelated keys, choose deliberately:

- optimize the dominant pattern and accept/measure fan-out for the other;
- maintain a lookup item from alternate key to `(partitionKey, id)`;
- materialize a second container shaped for the alternate pattern through change feed;
- use Fabric mirroring or another analytical integration for broad scans/reporting;
- consider separate aggregates/containers if lifecycle and consistency allow it.

Do not promise synchronous cross-container referential integrity. Derived copies are eventually consistent unless the application coordinates another explicit mechanism.

> **Related item:** Partitioning is simultaneously a scalability, cost, query-routing, and transaction design. A key that makes one query cheap can make an invariant impossible to update atomically; a key that co-locates everything can create an unscalable hot tenant.

### Plan sizing and scaling

#### Estimate throughput and storage

Measure representative operations with realistic item sizes and index policy. A capacity estimate is:

```text
peak RU/s = Σ (operation rate/second × measured RU/operation)
           × headroom for bursts, retries, skew, and change consumers

stored GB = live data + index + derived/lease data + growth and retention margin
```

Use the [Azure Cosmos DB capacity planner](https://cosmos.azure.com/capacitycalculator/) for an initial model, then load-test the actual SDK and data distribution. Reads by `id` plus partition key are typically the cheapest lookup shape; broad queries and large/index-heavy writes cost more. Multi-region cost includes each configured region.

#### Serverless versus provisioned throughput

| Model | Best fit | Key constraints to verify |
|---|---|---|
| Serverless | intermittent, low-volume, unpredictable development or small workloads | supported regions/features, storage and burst limits, per-request billing, no reserved capacity |
| Manual provisioned RU/s | steady predictable utilization and direct control | pay for provisioned capacity even when idle; size for partition distribution |
| Autoscale provisioned throughput | variable production demand with meaningful peaks | configured maximum, billing behavior, hot-partition limits, minimum/maximum rules |
| Database-level shared throughput | several small containers with noncoincident demand | shared pool/noisy neighbors; dedicated-throughput containers are separate |
| Container-level throughput | isolation and independent scale for important container | minimums and cost per container |

Review [serverless](https://learn.microsoft.com/en-us/azure/cosmos-db/serverless), [provisioned throughput](https://learn.microsoft.com/en-us/azure/cosmos-db/set-throughput), [autoscale](https://learn.microsoft.com/en-us/azure/cosmos-db/provision-throughput-autoscale), and [free tier](https://learn.microsoft.com/en-us/azure/cosmos-db/free-tier) before deployment. Free tier is an account-level discount with eligibility constraints, not a separate database engine.

**VERIFY CURRENT:** limits, minimum RU/s, dynamic/autoscale behavior, feature compatibility, regional availability, pricing, free-tier benefit, and large-partition capabilities change. Use the [service quotas and limits](https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits) and pricing page for the target design date.

#### Granular scale and resource governance

Create separate containers when a workload needs independent throughput, partitioning, index, TTL, encryption, or operational ownership. Shared database throughput is useful for small containers, but a single busy container can consume the shared pool. Use Azure Policy, deployment validation, budgets, tags, role scopes, and throughput limits to constrain accidental scale. Monitor per-partition demand because increasing total RU/s does not correct a single hot logical key indefinitely.

### Implement SDK connectivity

The [current .NET SDK best practices](https://learn.microsoft.com/en-us/azure/cosmos-db/best-practice-dotnet) apply a few durable rules:

- create one `CosmosClient` per account for the process lifetime; repeated construction causes connection, CPU, metadata, and socket pressure;
- place the application in the same Azure region as the preferred database region when possible;
- use direct mode for lowest latency where its TCP network requirements are allowed; use gateway mode for HTTPS-only/proxy-constrained paths or emulator limitations;
- configure preferred regions so the SDK can route to nearby healthy replicas;
- avoid blocking asynchronous calls; size application CPU and concurrency before increasing database throughput;
- log SDK diagnostics for slow/failing requests, but do not parse diagnostic strings as a stable contract;
- handle transient failure with the SDK retry behavior and application-level idempotency.

#### Direct versus gateway

| Mode | Data path | Strength | Operational consideration |
|---|---|---|---|
| Direct | SDK opens TCP connections to replicas after gateway metadata/routing calls | lower latency and fewer data-path hops | more connections/ports; firewall/private endpoint must permit required range |
| Gateway | all requests use HTTPS through gateway | proxy/firewall simplicity and lower connection count | added hop and gateway connection limits |

Private endpoints change DNS/routing, not the need to authenticate. Direct mode through Private Link has broader port requirements documented in the [Private Link guide](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints).

#### Local development

The [Azure Cosmos DB emulator](https://learn.microsoft.com/en-us/azure/cosmos-db/emulator) supports local development without Azure cost, but it does not emulate global distribution, scale, all APIs, all consistency/failure behavior, or all service features. The new [Linux-based emulator vNext](https://learn.microsoft.com/en-us/azure/cosmos-db/emulator-linux) supports the API for NoSQL in gateway mode with a documented feature subset. Use it for deterministic unit/integration work; use a controlled Azure test account for RU, direct connectivity, identity/network, multi-region, backup, and production-like performance tests.

### Query with the NoSQL query language

Use the current [Cosmos DB query language documentation](https://learn.microsoft.com/en-us/cosmos-db/query/) rather than assuming full SQL Server semantics. JSON property names are case-sensitive; missing and `null` are different states.

```sql
SELECT VALUE {
    "orderId": c.id,
    "total": ARRAY_SUM(ARRAY(SELECT VALUE l.quantity * l.unitPrice FROM l IN c.lines))
}
FROM c
WHERE c.tenantId = @tenantId
  AND c.type = "order"
  AND IS_DEFINED(c.placedAt)
ORDER BY c.placedAt DESC
```

Know how to:

- project whole items, selected properties, or `VALUE` scalars;
- traverse nested objects and arrays; use `JOIN` as an intra-item array cross-product, not a cross-container relational join;
- use aggregates and `ORDER BY`, including the index requirements of multi-property order/filter patterns;
- use type-checking and array, string, mathematical, and date/time functions;
- parameterize queries rather than concatenate values;
- use [correlated and scalar subqueries](https://learn.microsoft.com/en-us/cosmos-db/query/subquery) to avoid repeated expensive expressions and filter array expansions;
- supply the partition key in query request options when the caller knows it;
- inspect request charge, retrieved/output counts, index utilization/metrics, continuation token, and SDK diagnostics.

A cross-partition query is not automatically wrong. It is wrong when its fan-out, frequency, latency, and RU cost violate requirements. Measure with production-like partition counts and selectivity.

### Implement SDK data access

#### Point operations and queries

Use a point read when both `id` and partition-key value are known. Do not issue `SELECT * WHERE c.id = ...` merely to retrieve an addressable item: the query uses the query engine and can fan out if the key is absent.

For writes:

- **Create** fails if the address exists—useful for duplicate detection.
- **Upsert** creates or replaces—convenient, but can hide whether a create versus replacement was expected.
- **Replace** sends the full item and is appropriate for complete aggregate updates.
- **Patch** changes selected paths and can reduce payload/serialization, but still needs a concurrency and invariant plan. See [partial document update](https://learn.microsoft.com/en-us/azure/cosmos-db/partial-document-update).
- **Delete** requires `id` and partition key; consider dependent denormalized data and change consumers.

#### Optimistic concurrency

Every item has an `_etag`. Read it, calculate a change, and send `If-Match`; a concurrent change produces HTTP 412 rather than silently overwriting it. Decide whether to reload/re-evaluate, surface conflict, or apply a commutative merge. Blind retry of the same stale replacement defeats the invariant. The [transactions and optimistic concurrency](https://learn.microsoft.com/en-us/azure/cosmos-db/database-transactions-optimistic-concurrency) documentation relates ETags to the logical-partition transaction boundary.

#### Transactional batch versus bulk

[Transactional batch](https://learn.microsoft.com/en-us/azure/cosmos-db/transactional-batch) groups supported operations sharing one partition-key value; all commit or roll back. It protects an invariant such as order + outbox item. A failed operation causes the batch to fail; inspect per-operation results.

Bulk mode increases throughput by scheduling many independent operations efficiently across partitions. It does **not** make them one transaction and result ordering/completion must be handled. Prefer current SDK bulk support over the legacy .NET bulk executor library; Microsoft’s [migration guidance](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-migrate-from-bulk-executor-library) documents the current path.

#### Pagination and continuation

Iterators return pages. A continuation token represents query progress, not a durable business cursor or snapshot-isolation promise across arbitrary concurrent changes. Persist only where the selected SDK/query supports it, bind it to the exact query shape and parameters, protect it as application state, and handle expiration/incompatibility. Set a page size to control response shape, not total RU cost magically.

#### Consistency overrides and session tokens

The account defines default consistency. A request can use a supported weaker consistency override, not a stronger guarantee than the account provides. Under session consistency, the SDK session token carries read-your-writes context. If requests move across stateless front ends or client instances and require the same session guarantee, propagate the appropriate token deliberately. Do not expose it as an authorization token.

#### Transient failures and 429s

Classify before retrying:

| Signal | Meaning/action |
|---|---|
| 429 | rate limited; SDK respects server retry-after within configured limits; inspect partition skew and capacity |
| 408 / timeout | outcome can be uncertain; inspect diagnostics, connectivity, CPU, request size and idempotency before retry |
| 412 | ETag precondition failed; reload and re-evaluate business change |
| 409 | conflict such as duplicate ID/unique key or multi-write conflict path; do not treat as generic transient |
| 404 | wrong address, deleted/expired item, stale region/session context, or resource issue; inspect substatus and request context |
| 403 | identity/key/permission/network/account restriction; retry rarely fixes configuration |
| 5xx/503 | service or path issue; bounded backoff, regional resilience, diagnostics, and idempotency apply |

Use exponential backoff with jitter where the SDK does not already own the retry, cap total latency, and make commands idempotent with deterministic IDs, ETags, state machines, or an inbox/outbox pattern. See [429 troubleshooting](https://learn.microsoft.com/en-us/azure/cosmos-db/troubleshoot-request-rate-too-large) and [query troubleshooting](https://learn.microsoft.com/en-us/azure/cosmos-db/troubleshoot-query-performance).

### Implement server-side JavaScript

Azure Cosmos DB supports stored procedures, pre/post triggers, and user-defined functions described in [server-side programming](https://learn.microsoft.com/en-us/azure/cosmos-db/stored-procedures-triggers-udfs) and the [writing guide](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-write-stored-procedures-triggers-udfs).

- A stored procedure runs transactionally within one logical partition. The caller supplies that partition key. It is bounded by execution time and RU availability, so continuation/resume logic may be needed.
- A trigger is not an autonomous database event listener. The client explicitly names a pre- or post-trigger on an operation. Triggers share the operation’s logical-partition scope.
- A UDF is compute-only JavaScript called from a query. Prefer built-in query functions where possible because UDF execution can add cost and cannot use indexes to replace a missing indexed predicate.
- Server-side JavaScript cannot import arbitrary modules. Deploy/version scripts with the application or infrastructure process and test rollback compatibility.

Use transactional batch for straightforward same-key operation groups; use a stored procedure when server-side conditional iteration/logic truly needs the partition transaction. Use change feed for asynchronous effects outside the logical partition.

---

## 3. Design and implement data distribution (5–10%)

### Derive topology from user and failure requirements

Add regions to reduce distance, improve read availability, and/or enable regional write resilience—not because “global” is inherently better. Each region adds replicated storage and throughput cost and changes consistency/failure behavior.

| Requirement | Candidate design | Validate |
|---|---|---|
| local reads, centralized writes | single write region plus read regions | write latency to primary, read routing, failover RTO/RPO |
| local writes in several geographies | multiple write regions | conflicts, supported consistency/features, application reconciliation |
| zero data-loss expectation across regional failure | strong consistency with supported topology | write latency and availability tradeoff, distance restrictions |
| read-your-writes per user/session | session consistency and token continuity | load-balancer/client behavior and token propagation |
| highest availability/lowest read cost | consistent prefix or eventual as semantics allow | stale/order behavior visible to users |

Review [reliability in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/reliability/reliability-cosmos-db) and [global distribution internals](https://learn.microsoft.com/en-us/azure/cosmos-db/global-distribution). Preferred regions tell the SDK where to try; they do not create regions or replace application-tier traffic routing.

### Choose consistency from observable guarantees

The five [consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) are ordered from strongest to weakest:

| Level | Core application guarantee | Typical fit/consideration |
|---|---|---|
| Strong | reads return the latest committed version | strict cross-client correctness; higher read cost/latency and topology constraints |
| Bounded staleness | lag bounded by configured versions or time, with ordering | controlled stale window; read cost similar to strong |
| Session | read-your-writes and ordered guarantees within a session | common user/session workloads; token continuity matters |
| Consistent prefix | reads never see writes out of order, but can lag | ordered feeds where freshness can vary |
| Eventual | no ordering guarantee, replicas converge | counters/feeds where temporary reordering/staleness is acceptable |

Write a testable statement: “After a successful cart write, that user must see it on the next request even after the web request lands on another instance.” That implies session-token handling; “use session consistency” alone does not prove it.

Stronger consistency affects more than correctness. Strong and bounded-staleness reads involve more replicas and therefore have different RU/read-throughput economics. Strong multi-region writes are not a valid combination. Verify current distance/region restrictions and durability behavior.

### Configure failover and application routing

For single-write accounts, configure region priorities and service-managed failover as requirements permit. A manual failover changes the write region intentionally for testing/maintenance. Do not initiate conflicting topology changes during a live regional incident without following current guidance; preserve evidence and understand whether the operation risks data.

Build and rehearse:

1. regional application routing and health probes;
2. SDK preferred-region order and multi-region endpoint discovery;
3. remaining-region throughput capacity;
4. consistency/session behavior through failover;
5. write/read transaction and dependency validation;
6. alerting on availability, replication, SDK failures, and business SLO;
7. failback and post-event reconciliation.

Per-partition automatic failover is a newer resilience capability whose eligibility and behavior should be verified in [current documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/per-partition-automatic-failover); do not confuse it with changing the data model or consistency guarantee.

### Design multi-region writes and conflict resolution

Concurrent writes to the same logical item can conflict. Select a policy from business semantics:

- **Last writer wins:** resolves using `_ts` by default or another numeric path. Simple, but a clock/number winning does not mean the business-correct update won.
- **Custom merge procedure:** server-side resolution implements domain logic within supported constraints.
- **Conflict feed/application resolution:** retain conflicts for an application to reconcile; requires an owner, idempotent processing, backlog monitoring, and deterministic convergence.

Test create/create, replace/replace, delete/update, partition-key identity, offline client, regional outage, replay, and resolution failure. Counter increments, set union, reservations, and balance transfers need domain-specific logic; overwriting the whole item with LWW can lose valid concurrent intent. Use the current [conflict-resolution policy guide](https://learn.microsoft.com/en-us/azure/cosmos-db/conflict-resolution-policies).

> **Related item:** Availability-zone redundancy protects datacenter-level failure inside a region; multiple regions address regional failure; backup addresses corruption/deletion and historical recovery. None substitutes for the others.

---

## 4. Integrate an Azure Cosmos DB solution (5–10%)

### Choose the analytical path intentionally

The July 2026 blueprint names both current and transitional technologies:

| Need | Prefer/consider | Data path and caveat |
|---|---|---|
| current near-real-time Fabric analytics | Azure Cosmos DB Mirroring for Microsoft Fabric | incrementally replicates supported NoSQL data into OneLake/SQL analytics endpoint; requires eligible account, continuous backup, Fabric capacity and supported security/topology |
| existing Synapse Link project | analytical store + Synapse Spark/serverless SQL | analytical copy separated from transactional RU path; reconcile support notice and constraints |
| custom Spark transformations or transactional reads/writes | Azure Cosmos DB Spark connector | select transactional versus analytical endpoint deliberately; Spark jobs consume corresponding resources |
| operational derived views/events | change feed + SDK/Functions | ordered per logical partition, checkpointed consumer; design replay/idempotency |

[Fabric mirroring for Azure Cosmos DB](https://learn.microsoft.com/en-us/fabric/mirroring/azure-cosmos-db-tutorial) replicates changes to OneLake without consuming transactional RUs for the mirrored analytics queries. It is not zero cost: Fabric capacity and other services apply, and the [mirroring limitations](https://learn.microsoft.com/en-us/fabric/mirroring/azure-cosmos-db-limitations) include source-account, backup, multi-write, nested-schema, security, and region constraints.

> **LEGACY / TRANSITIONAL:** Microsoft’s current analytical-store CDC documentation says Azure Synapse Link for Cosmos DB is no longer supported for **new projects** and directs new designs to Fabric mirroring. The DP-420 blueprint still explicitly includes analytical store, Synapse Spark/serverless SQL, the Spark connector, and analytical-store CDC. Learn these for existing deployments and the published objective, but choose Fabric mirroring for a new project unless current requirements/documentation say otherwise. See the [analytical-store overview](https://learn.microsoft.com/en-us/azure/cosmos-db/analytical-store-introduction) and [CDC transition notice](https://learn.microsoft.com/en-us/azure/cosmos-db/get-started-change-data-capture).

#### Fabric mirroring and time travel

For a mirrored source:

1. verify API for NoSQL/account/topology/continuous-backup and Fabric region support;
2. grant the minimum source data permissions and configure network ACL bypass/private access as currently supported;
3. choose database/containers and start mirroring;
4. monitor initial snapshot and replication freshness/row counts;
5. query the SQL analytics endpoint or OneLake with SQL/Spark;
6. validate nested JSON/type evolution and semantic-model behavior;
7. alert on stalled replication and test recovery/reseed consequences.

The blueprint’s “time travel in Warehouse” refers to Fabric SQL analytics endpoint/Warehouse capability, not Cosmos DB point-in-time restore. [Fabric time travel](https://learn.microsoft.com/en-us/fabric/data-warehouse/time-travel) uses historical warehouse table versions for read-only queries within retention; it is not a method to restore the source operational container.

#### Existing analytical-store path

Analytical store is a column-oriented copy populated by auto-sync and governed by analytical TTL. Synapse Spark and serverless SQL can read it without consuming transactional RU/s. Spark can also query/write the transactional store via the OLTP connector—those operations do consume transactional resources. Know which endpoint a notebook uses.

Analytical-store change data capture can drive ADF/Synapse mapping data flows and include deletes according to its mode/configuration. It is distinct from the operational change feed and currently has preview/legacy constraints. Preserve checkpoints and target idempotency.

### Implement event-driven derived models

The [Azure Cosmos DB change feed](https://learn.microsoft.com/en-us/azure/cosmos-db/change-feed) is an ordered record of changes within each logical partition. It is not a single global total order. Default/latest-version mode emphasizes creates and updates; all-versions-and-deletes mode has continuous-backup prerequisites and retention limits.

Use it to:

- denormalize into a query-optimized container;
- update an aggregate/materialized view;
- enforce a cross-item or cross-container relationship asynchronously;
- archive or project operational events;
- feed downstream functions, event hubs, search, or reporting.

#### Change feed processor

The [change feed processor](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/change-feed-processor) coordinates workers through lease documents:

- **monitored container:** source changes;
- **lease container:** ownership, checkpoints, and load balancing;
- **processor name:** identifies a consumer group; separate logical consumers need separate names/leases;
- **instance name:** identifies one worker;
- **delegate/handler:** processes a batch and must be idempotent.

A checkpoint advances after successful delegate completion, but failures, lease movement, or side-effect timing can produce replay. Exactly-once business effects require idempotent target writes/deduplication, not belief that the feed invokes once. Monitor lag/backlog with the [change feed estimator](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-use-change-feed-estimator).

Azure Functions’ Cosmos DB trigger hosts the processor model. Configure source, leases, identity/connection, batch and polling behavior; scale testing must include lease partitioning, downstream capacity, poison/failure handling, and replay. See [Azure Functions change-feed integration](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/change-feed-functions).

#### Common projections

- **Denormalization:** upsert deterministic target ID from source ID/version; prevent an older replay overwriting a newer projection.
- **Referential enforcement:** detect missing/invalid reference and compensate/quarantine; it is eventual, not an atomic foreign key.
- **Aggregation:** store contribution/version or make updates conditionally idempotent; simple `total += value` double-counts replay.
- **Archiving:** retain source identity/version/time and validate target durability before advancing; change feed is not itself long-term backup.

#### Functions and Event Hubs

Use a function trigger for compute tied to change-feed checkpoints. Send durable integration events to Event Hubs when independent consumers, replay retention, partitioned streaming, or decoupling is required. A transactional outbox item written in the same logical-partition batch as the aggregate prevents “database commit but event not recorded”; a change-feed worker publishes that outbox idempotently.

### Integrate Azure AI Search

An [Azure AI Search indexer for Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/search/search-howto-index-cosmosdb) can pull documents and incrementally track changes. Define:

- source container/query and identity/network access;
- stable document key and field mappings;
- index schema, analyzers, vector/enrichment path where required;
- deletion detection strategy—ordinary indexing does not infer every deletion automatically;
- schedule/freshness SLO, high-watermark behavior, errors, and reset/rebuild plan;
- data classification: the search index is another governed copy.

Do not use search as the authoritative transactional read store. Validate source-to-index counts, representative content, deletes, schema changes, throttling, and query relevance.

> **Related item:** An integration is not complete when data merely arrives. Define ordering scope, delivery/replay semantics, checkpoint ownership, poison handling, target idempotency, reconciliation, observability, retention, and security for every hop.

---

## 5. Optimize an Azure Cosmos DB solution (15–20%)

### Optimize from measured request evidence

For a slow or expensive operation, collect:

- operation, `id`, partition-key availability, query text/parameters, page count and item size;
- request charge per page/operation and total;
- output count versus documents/index entries retrieved;
- SDK diagnostics: regions, retries, gateway/direct calls, client CPU and timing;
- index utilization/metrics and current indexing policy;
- normalized RU by physical partition and logical-key distribution;
- server-side versus end-to-end latency and status/substatus;
- concurrency and change from a known baseline.

Then classify: routing/fan-out, poor filter selectivity, missing/wrong index, expensive sort/aggregate, large result/payload, hot key, insufficient throughput, client resource/connectivity, region distance, or downstream latency. Increasing RU/s cannot fix every class.

### Improve query and operation cost

Use this order:

1. Replace query with a point read when the address is known.
2. Supply the complete partition key or useful hierarchical prefix.
3. Return only required fields and bound result sets.
4. Parameterize filters and avoid functions that prevent useful index paths where applicable.
5. Inspect [indexing metrics](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/index-metrics) for recommended used/potential paths.
6. Add the necessary single/composite index, wait for transformation, then retest.
7. Revisit model/partition or create a derived view if the high-value access pattern fundamentally conflicts.
8. Consider cache only for eligible read semantics after correctness and invalidation expectations are clear.

Request charge for the same deterministic query/data/index configuration is a useful regression signal. Compare total RU across all pages—not only page one.

### Define an indexing strategy

The default [indexing policy](https://learn.microsoft.com/en-us/azure/cosmos-db/index-policy) indexes all properties with range indexes. That favors flexible reads but increases write RU and index storage.

#### Policy components

- **Included/excluded paths:** exclude large never-filtered payloads or use an explicit include strategy for stable write-heavy schemas. Remember path syntax and undefined-value behavior.
- **Range indexes:** support equality/range and many order operations on strings/numbers.
- **Composite indexes:** support certain multi-property `ORDER BY` and improve combinations of equality/range/order. Property order and ascending/descending direction matter.
- **Spatial indexes:** support geometry operations for configured paths/types.
- **Vector indexes:** relevant to vector workloads, but only where the current objective/workload requires them; verify feature and policy details.
- **Indexing mode:** consistent is normal; `none` can support bulk load patterns but queries then need a deliberate reindex path.

For a read-heavy container, retain indexes for frequent routes and sorts. For a write-heavy container, exclude unused paths and large opaque subtrees. Never remove an index because a tiny test query still runs: it may scan and become catastrophic at production scale.

When replacing an index, add the new index, wait for online transformation to complete, prove queries use it, then remove the old one. Removing first can break or degrade live queries. Track the transformation described in [managing indexing policies](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-manage-indexing-policy).

### Use integrated cache where semantics permit

The [integrated cache](https://learn.microsoft.com/en-us/azure/cosmos-db/integrated-cache) is available through a dedicated gateway for supported API for NoSQL scenarios. It caches point reads and queries, reducing backend RU for cache hits. Configure maximum integrated cache staleness per request/default and understand that:

- it is not a general application cache or write-through source of truth;
- populated results are dependent on exact query/request shape;
- staleness can be greater than the application accepts if configured poorly;
- dedicated gateway capacity/cost, availability, region placement, private access, and SDK gateway routing matter;
- a cache miss still consumes backend RUs.

Use it for read-heavy, repeatable, staleness-tolerant access. Measure hit behavior, RU reduction, response correctness after writes, and behavior during gateway disruption.

### Design change-feed throughput

Change-feed processing consumes source read RUs and lease-container RUs, plus target-service capacity. Scale by partition-key ranges and lease ownership—not arbitrary duplicate processors with the same identity. Use separate processor names for independent consumers; otherwise instances cooperate on one workload.

Estimate lag and recovery:

```text
backlog drain time ≈ pending work / sustainable successful processing rate
```

Include target throttling, handler time, retries, batch size, source partitions, and lease acquisition. The estimator measures pending work; it does not prove side effects succeeded. Alert on lag plus handler failures and target reconciliation.

---

## 6. Maintain an Azure Cosmos DB solution (25–30%)

### Monitor the whole request path

[Azure Cosmos DB insights](https://learn.microsoft.com/en-us/azure/cosmos-db/insights-overview) surfaces throughput, requests, storage, availability, latency, system, and management signals. Build a layered view:

| Layer | Evidence | What it distinguishes |
|---|---|---|
| application | business success, dependency duration, retries, saturation | user impact and caller behavior |
| SDK | diagnostics, contacted regions, request charge, retry/connection timeline | client versus service path |
| account/container | total requests by code/operation, RU, availability, latency | service-side demand/failure |
| partition | normalized RU, physical/logical partition consumption, storage | hot/skewed keys hidden by averages |
| integration | change-feed lag, leases, function failures, mirror freshness | derived-data health |
| control/security | activity log, diagnostic resource logs, RBAC/network/key changes | configuration and access events |

[Normalized RU consumption](https://learn.microsoft.com/en-us/azure/cosmos-db/monitor-normalized-request-units) is the maximum utilization percentage across partition-key ranges for the interval, not an average of total provisioned RU. One hot range can reach 100% while account-wide consumed RU appears low.

#### Status-code triage

Start from status + substatus + SDK diagnostics + operation context:

- high 429 with balanced partitions: capacity/burst/concurrency or inefficient operations;
- high 429 isolated to one range/key: skew/hot key; more total RU may only postpone the design limit;
- healthy server latency but slow application: client CPU/thread/socket/DNS/proxy/region/downstream path;
- elevated server latency with stable client: service workload/query/index/partition or regional condition;
- 403 after security change: distinguish RBAC data actions, management role, firewall/private DNS, disabled keys, and tenant/token audience;
- replication lag: inspect topology/consistency/region state and application routing before claiming data loss.

Enable resource-specific diagnostic logs to a governed destination and query request/control-plane/audit categories. Logs cost storage/ingestion and can expose identifiers/query details, so apply retention and access control. Alerts need actionable thresholds, window, severity, owner, runbook, and recovery notification—not every metric spike.

### Implement backup and restore

Azure Cosmos DB has [continuous and periodic backup modes](https://learn.microsoft.com/en-us/azure/cosmos-db/online-backup-and-restore):

| Mode | Restore model | Design implication |
|---|---|---|
| Continuous | self-service point-in-time restore within selected supported retention tier; current capabilities include new-account and supported same-account scenarios | one-way migration from periodic; feature/topology/CMK/mirroring constraints; restore permissions and cost |
| Periodic | scheduled platform backups; restoration is requested through Azure support | interval/retention/redundancy configuration; longer operational workflow |

The current [continuous-backup documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/continuous-backup-restore-introduction) describes 7-, 30-, and preview 35-day tiers; treat exact tiers, preview status, support matrix, and prices as **VERIFY CURRENT**. A backup is not a read replica, failover region, change feed, or Fabric time-travel table.

#### Recovery plan

1. Derive RPO/RTO for deletion, corruption, account loss, and region loss separately.
2. Choose backup mode/tier and redundancy; inventory unsupported feature combinations.
3. Grant minimum restore/list-restorable permissions to a controlled recovery identity.
4. Locate deletion events/latest restorable timestamp in the correct region.
5. Restore account, database, or container using a supported current target mode.
6. Reapply or validate resources not restored: network, identities/RBAC, keys/CMK access, diagnostic settings, integrations, scripts, throughput/topology, and application configuration.
7. Reconcile data at the chosen point, run representative business transactions, and validate indexes/change consumers.
8. record actual RPO/RTO and securely remove the test target.

Periodic backup restoration and some continuous restore modes create a new account/resource. Never assume every control-plane setting or external dependency is included. Practice [same-account deleted database/container restore](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-restore-in-account-continuous-backup) only in a disposable environment and within current concurrency/retention rules.

> **Related item:** Multi-region replication rapidly copies valid writes—including damaging application updates. Backup/PITR is the recovery control for corruption or deletion; replication is the availability control for service/region failure.

### Implement layered security

Use the [Azure Cosmos DB security guidance](https://learn.microsoft.com/en-us/azure/cosmos-db/security) as a checklist.

#### Control plane versus data plane

Azure RBAC roles on the account govern management operations but do not automatically grant item read/write. Native Azure Cosmos DB data-plane roles define `dataActions` and scopes down to account/database/container. Conversely, a data-plane reader cannot modify firewall or regions. Test both paths separately.

Prefer Microsoft Entra authentication and managed identity over stored account keys. [Data-plane RBAC](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-connect-role-based-access-control) can grant built-in/custom permissions at an appropriate scope and allows disabling key-based authentication where all clients support it. Data Explorer also needs the correct control-plane visibility and data-plane role—portal access is not proof of item permission.

If legacy clients require keys:

- store them in Key Vault or another approved secret store, never source/configuration logs;
- rotate primary and secondary without downtime and inventory all consumers;
- use read-only keys for readers where supported;
- restrict network access because possession of a key is powerful;
- migrate to Entra/RBAC and consider disabling local authentication.

#### Network and browser controls

- public endpoint + IP firewall restricts source public IPs but still requires authorization;
- virtual-network service endpoints identify allowed subnets while traffic reaches the service endpoint;
- Private Link gives private IP connectivity; private DNS, region-specific records, routing, and direct-mode ports are part of the design;
- disabling public network access prevents unintended public paths;
- CORS only controls which browser origins may call an endpoint; it is not identity, authorization, or a boundary for non-browser clients.

Avoid the broad “allow Azure services” exception unless its cross-customer scope is accepted. [IP firewall guidance](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-configure-firewall) explicitly warns about breadth.

#### Encryption boundaries

- service-managed keys encrypt at rest by default;
- customer-managed keys add a Key Vault-controlled encryption layer and operational dependencies for identity, key permissions, soft delete/purge protection, rotation, regional availability, backup, and recovery;
- Always Encrypted performs property-level client-side encryption so plaintext/key is not exposed to the service; it affects queryability, index policy, SDK support, item size, and key lifecycle.

[Always Encrypted](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-always-encrypted) uses data-encryption keys wrapped by Key Vault keys and a container encryption policy. Deterministic encryption can support equality comparisons for eligible fields but reveals equality patterns; randomized encryption provides stronger pattern protection but prevents equality query. Never encrypt the partition key or required system fields without verifying current support.

CMK protects service-side at-rest encryption; Always Encrypted protects selected values from the service boundary. They are not interchangeable. Test key disable/delete, rotation, restored-account key access, and break-glass recovery.

### Choose and execute data movement

Select from volume, rate, downtime, transform, ordering, delete handling, source/target support, network, identity, checkpoint, and validation requirements:

| Mechanism | Good fit | Important behavior |
|---|---|---|
| current SDK bulk support | controlled app migration/backfill | parallel independent operations; partition and throttle-aware client; own checkpoint/reconciliation |
| Azure Data Factory / Synapse pipeline | scheduled copy and transforms | connector/source/sink support, DIU/integration runtime, schema mapping, retries and parallelism |
| Kafka connector | Kafka ecosystem streaming | source/sink offset, partition mapping, delivery semantics and target idempotency |
| Azure Stream Analytics | streaming query/window transformation | input/output compatibility, late/out-of-order events, partitioning, retries |
| Spark connector | large Spark read/write/transform | transactional versus analytical source, Spark partitioning, RU/capacity pressure |
| IoT Hub custom Cosmos DB endpoint | direct routed device messages | synthetic partition-key template, identity/network and downstream throughput |
| change feed | continuous projection/migration | no historical backfill by itself in latest-version mode; leases/replay/idempotency |
| Fabric mirroring | analytical replica in OneLake | not an operational container-to-container migration |

For bulk movement:

1. inventory source count/size/schema/keys/TTL/system fields and target limits;
2. provision target partition/index/throughput/network/identity before copying;
3. create deterministic IDs and preserve or intentionally transform partition semantics;
4. checkpoint source ranges/pages and make target writes idempotent;
5. throttle to protect production and record rejected/dead-letter items;
6. reconcile counts by partition, hashes/aggregates, representative queries, TTL, permissions, index policy, and business reads;
7. if online, capture changes during the backfill and define a cutover high-water mark;
8. retain rollback and delete neither source nor logs until acceptance.

The older bulk executor library remains documented, but new .NET work should use SDK v3 bulk support. Treat that as a **legacy implementation detail**, not the concept of bulk operations itself.

### Implement DevOps and infrastructure as code

Use declarative deployment for stable desired resource state and imperative commands for operational transitions that should not be re-applied blindly.

| Operation | Preferred pattern |
|---|---|
| account/database/container, regions, consistency, backup, network, throughput, index policy, RBAC | ARM/Bicep (or governed equivalent), parameterized and version-controlled |
| data seeding/migration, conditional restore, one-time failover test, backfill | idempotent imperative workflow with approval/checkpoint/evidence |
| standard -> autoscale throughput migration | explicit CLI/PowerShell operation after compatibility/cost checks |
| regional failover | controlled runbook with health gates, application validation and audit |

The [ARM template examples](https://learn.microsoft.com/en-us/azure/cosmos-db/manage-with-templates) cover multi-region accounts, throughput, analytical store, server-side code, and Entra/RBAC. [Azure PowerShell examples](https://learn.microsoft.com/en-us/azure/cosmos-db/manage-with-powershell) include throughput migration and custom index policy.

#### Safe indexing-policy deployment

1. export/baseline policy and important query metrics;
2. add new required indexes without removing old coverage;
3. deploy and monitor index transformation progress/RU impact;
4. run representative old and new application versions;
5. compare query charge, results and latency;
6. only then remove obsolete indexes in a later change;
7. retain rollback definition and transformation monitoring.

#### Pipeline gates

- lint/validate template and policy-as-code;
- preview/what-if and detect destructive resource recreation;
- deploy to isolated environment;
- run emulator tests plus cloud integration tests for identity/network/RU behavior;
- validate item address, query/index, transactional batch, concurrency and retry paths;
- test change consumer replay and target idempotency;
- confirm diagnostic settings, alerts, backup mode and restore permissions;
- deploy progressively, observe, and preserve rollback.

Do not place items or secrets in ARM templates. Resource deployment success proves desired control-plane state, not application correctness.

---

## 7. Integrated design scenarios

### Scenario A: global multitenant commerce

**Requirements:** customers read/write locally; each order plus outbox event must commit atomically; tenants vary greatly in size; regional outage must preserve service; analytics can lag minutes.

1. Model order and bounded line snapshots in one item; keep mutable catalog separately. Use deterministic IDs and schema version.
2. Use hierarchical partitioning such as tenant/order grouping only after testing prefix routing and per-tenant scale. Co-locate the outbox item under the same complete logical key needed by the transactional batch.
3. Use session consistency and propagate session tokens when the same user moves between stateless app instances.
4. Evaluate multi-region writes only with explicit order-state conflict semantics. If concurrent order mutation is unsafe, a single write-home per order/tenant with failover may be simpler.
5. Process outbox through change feed to Event Hubs with idempotent publication and checkpoint only after accepted side effect.
6. Mirror eligible containers to Fabric for analytics; model nested JSON and continuous-backup/topology limitations before committing.
7. Alert on p95/p99 application latency, 429 by key/range, change-feed lag, conflict backlog and mirror freshness.
8. Test regional routing, duplicate change delivery, stale ETag, restore to a point before an accidental mass update, and reconciliation.

**Failure trap:** a hierarchy beginning with tenant improves tenant routing but does not automatically make all tenant data one transaction. The complete hierarchical key defines the finest logical partition transaction boundary.

### Scenario B: IoT telemetry and device state

**Requirements:** bursty writes, per-device recent history, 30-day retention, fleet-wide analytics, latest state lookup, and replay-safe alerts.

1. Partition telemetry by device plus time bucket or a justified hierarchical/synthetic strategy; load-test the noisiest device and current bucket.
2. Set item/container TTL for 30-day transactional retention; do not assume the delete occurs at the exact second.
3. Maintain latest device state as a deterministic item/projection. Make change-feed updates conditional on source timestamp/version so replay cannot regress state.
4. Use autoscale or measured provisioned throughput for sustained production bursts; serverless only after verifying limits and cost shape.
5. Route IoT Hub messages directly or through event processing with a synthetic key template aligned to the container. Validate identity, firewall, and route errors.
6. Use Fabric mirroring for broad time/fleet analytics when eligible, rather than repeatedly scanning the operational container.
7. Track normalized RU per partition, data size per key, ingestion retries, change lag and expired-data/storage trend.

**Failure trap:** `/deviceId` distributes a large fleet but one malfunctioning device remains a hot logical key. Adding account RU does not remove that single-key concentration.

### Scenario C: secure customer profile service

**Requirements:** profile lookup by tenant/user, selected fields invisible to database operators, no account keys, private access, auditable recovery, and full-text discovery on approved fields.

1. Use `(tenantId,userId)` hierarchical partitioning only if tenant-prefix and exact-user patterns justify it; use deterministic user IDs.
2. Authenticate the managed workload with Entra and a minimum data-plane custom role. Disable key-based auth after every consumer is migrated.
3. Disable public access and configure Private Link/DNS/direct-mode ports. Test negative paths from unapproved networks.
4. Apply Always Encrypted only to sensitive eligible fields; leave partition/id and approved search fields available according to policy. Protect Key Vault permissions and rotation.
5. Feed only approved fields to Azure AI Search, with managed identity, private connectivity, deletion handling and index access governance.
6. Use continuous backup and test restore with CMK/client-encryption/key dependencies. Reapply data-plane roles and private endpoints if the restore target requires them.
7. Audit control changes and diagnostic requests without leaking encrypted plaintext or secrets.

**Failure trap:** customer-managed server-side encryption does not hide plaintext from the database service during processing. Property-level client encryption is the boundary for that requirement.

---

## 8. Hands-on labs

Use a disposable account and budget. Save commands/code, test data generator, before/after metrics, diagnostics, screenshots or query results, failure evidence, and cleanup proof. Do not run destructive/failover/restore experiments against shared production resources.

### Lab 1: model and partition an order workload

1. Write ten concrete access patterns and invariants for orders, customers, products, and recent-order lists.
2. Produce embedded/reference and single/multiple-container alternatives.
3. Generate at least 100,000 items with deliberately skewed tenant sizes.
4. compare `/tenantId`, synthetic bucket, and hierarchical candidates using routed/fan-out queries.
5. Record storage distribution, normalized RU, request charge, page count and latency.
6. Defend the selected model and state the migration trigger if a tenant outgrows it.

### Lab 2: SDK address, concurrency, batch, bulk, and TTL

1. Create one singleton client with current recommended settings and logging.
2. Compare a point read with an ID query using identical item/result.
3. implement create/read/replace/patch/delete and record status, ETag, RU and diagnostics.
4. Cause an ETag 412 with two concurrent writers and implement a correct reload/merge path.
5. Atomically write an aggregate and outbox record in a transactional batch under one key.
6. Bulk-load independent items and prove partial failures are not transactional.
7. Set per-item TTL overrides and observe expiration without assuming exact scheduling.

### Lab 3: query and index experiment

1. Create nested arrays, optional/mixed-type properties and time-ordered items across partitions.
2. Write targeted and cross-partition parameterized queries using arrays, self-join, aggregate, subquery, type checks, strings, math and date functions.
3. Capture every page’s RU, continuation token, output/retrieved counts and index metrics.
4. Add a composite index for a real filter/order pattern; wait for transformation.
5. Exclude a large unqueried payload path and compare write RU/index storage.
6. demonstrate a query that becomes unsupported or expensive when its required index is removed, then restore safely.

### Lab 4: region, consistency, and failure behavior

1. In an approved test account, add a second region and configure SDK preferred regions.
2. Compare permitted consistency levels with a read-after-write harness and record RU/latency.
3. Propagate and omit a session token across two simulated application instances.
4. Perform a planned failover using the documented runbook; validate endpoint routing and business transaction.
5. If multi-write is available, create a controlled conflict and observe the configured resolution.
6. Record achieved RTO/RPO indicators and restore original topology.

### Lab 5: replay-safe change-feed projection

1. Create monitored, lease and materialized-view containers.
2. Run two processor instances with one processor name and observe lease balancing.
3. Use deterministic target IDs/source versions to make the handler idempotent.
4. fail after the target write but before checkpoint, restart, and prove replay does not duplicate/regress data.
5. use the estimator to record lag while stopped and drain rate after restart.
6. add a second consumer with a separate processor name and prove independent checkpoints.

### Lab 6: analytical integration and search

1. Check Fabric-mirroring eligibility before enabling anything.
2. Mirror a test container, monitor initial sync, and reconcile counts/freshness.
3. Query nested JSON through the SQL analytics endpoint and document schema limitations.
4. execute an eligible time-travel query in the Fabric analytical target and explain why it is not source PITR.
5. Create an Azure AI Search indexer for approved fields; update and delete source data.
6. prove incremental update and configured deletion behavior; capture errors and reset/rebuild steps.
7. Document how an existing Synapse Link design differs and the “not for new projects” notice.

### Lab 7: security and observability

1. Give a managed identity a minimum custom data-plane role and a separate operator minimum control-plane role.
2. connect with `DefaultAzureCredential`; prove denied operations remain denied.
3. configure private access and validate DNS plus gateway/direct connectivity; then disable public access.
4. enable diagnostic logs and query requests by status, operation and partition-key RU category.
5. create alerts for sustained normalized RU, 429/failure rate, availability and replication/change lag with action ownership.
6. apply client-side encryption to a supported field in a separate lab container and test allowed/disallowed query shapes.
7. remove temporary roles/endpoints/log destinations safely.

### Lab 8: IaC, migration, backup, and recovery

1. Deploy account/database/container, consistency, regions, backup, network, throughput, index policy, identity and diagnostics through ARM/Bicep.
2. use a checkpointed SDK bulk script to backfill a newly partitioned container while a change consumer captures new writes.
3. reconcile counts and sampled content per partition; execute a rehearsed cutover and rollback.
4. migrate throughput between supported standard/autoscale modes with PowerShell or CLI and record state/cost implications.
5. run a planned regional failover command with health gates.
6. delete a disposable container after noting a restorable time; perform the supported PITR flow.
7. validate restored items, index, TTL, roles, network, keys, integrations and application transaction.
8. destroy only verified lab resources and retain the recovery report.

---

## 9. Original knowledge checks

These are original prompts, not recalled exam questions. Answer with the decision, dependency chain, evidence, failure mode, and corrective action.

1. Why can a high-cardinality partition key still create a hot partition?
2. An item is always fetched by tenant and order ID. Why is a point read preferable to `WHERE id = @id`, and what address must the caller know?
3. When should bounded children be embedded, and what two growth/concurrency signals would make you reference them instead?
4. A tenant may exceed a single logical partition but most queries start with tenant. Compare synthetic buckets with a hierarchical key.
5. Why does a transactional batch require the same partition-key value, and how would you atomically record an outbox message?
6. A bulk import reports 98% success. Why is the container not transactionally consistent, and how do you resume safely?
7. Two writers replace the same profile. Show how `_etag` prevents lost update and why blind retry is wrong.
8. When can an item-level TTL override help, and why is TTL not an exact-time workflow trigger?
9. What does a continuation token guarantee, and what does it not guarantee about a changing result set?
10. Why should `CosmosClient` normally be a singleton, and what diagnostics reveal excessive client creation?
11. Compare direct and gateway mode for a private-endpoint workload behind a restrictive firewall.
12. The average RU use is 30%, but 429s are high. Which partition metric and data distribution evidence do you inspect?
13. State an application requirement suited to each of strong, bounded staleness, session, consistent prefix, and eventual consistency.
14. A session-consistent user does not read their write after switching web servers. What state may need propagation?
15. When do multi-region writes create a business conflict, and why may last-writer-wins be unsafe?
16. Distinguish service-managed failover, manual failover, per-partition automatic failover, and application traffic routing.
17. A Fabric report is stale but source queries are current. Which mirror prerequisites, replication signals and schema constraints do you check?
18. Why is Synapse Link knowledge still in this guide even though it is not recommended for new projects?
19. What is the difference between operational change feed, analytical-store CDC, and Fabric mirroring?
20. A change-feed handler writes its target and crashes before checkpoint. How do you avoid duplicate business effect?
21. Why do two independent projections need separate processor names/lease state?
22. How do included paths, excluded paths and composite indexes change read/write RU tradeoffs?
23. Why add a replacement index before removing the old one in production?
24. When can integrated cache reduce RU, and which staleness/capacity behavior must be tested?
25. Compare control-plane Azure RBAC with Azure Cosmos DB data-plane RBAC and Data Explorer access.
26. Contrast customer-managed keys and Always Encrypted in terms of who can see plaintext and what queries remain possible.
27. Why are replication, backup, change feed, Fabric time travel and TTL five different controls?
28. A restored account contains data but the application fails. Which external/control settings must be revalidated?
29. Choose among SDK bulk, ADF, Kafka, Stream Analytics, Spark, IoT Hub routing and change feed for three different movement patterns.
30. Why is a successful ARM deployment insufficient evidence that the application works?

---

## 10. Final readiness checklist

- [ ] I can map every July 21, 2026 objective to a section, lab, and evidence artifact.
- [ ] I can model embedding, references, denormalization, mixed entity types and schema versions from access patterns.
- [ ] I can defend a natural, synthetic, or hierarchical partition key with storage, RU, routing and transaction evidence.
- [ ] I can choose serverless, manual/autoscale provisioned, database-shared or container-dedicated throughput.
- [ ] I can recognize correct singleton SDK, gateway/direct, region, logging, pagination and retry behavior in C# or Java.
- [ ] I can implement point operations, Patch, ETags, batch, bulk, TTL and query metrics.
- [ ] I can write/recognize NoSQL queries over arrays/nested values, subqueries, functions, aggregation and ordering.
- [ ] I can explain stored procedure, trigger and UDF scope and constraints.
- [ ] I can derive consistency, region, failover, routing and conflict choices from testable requirements.
- [ ] I can distinguish current Fabric mirroring from transitional Synapse Link/analytical-store paths.
- [ ] I can design replay-safe change-feed/Functions projections and an Azure AI Search indexing path.
- [ ] I can tune from RU, diagnostics, index metrics and partition evidence rather than intuition.
- [ ] I can monitor request, latency, replication, security and partition signals with actionable alerts.
- [ ] I can choose/test continuous versus periodic backup and validate a restored workload.
- [ ] I can separate control-plane, data-plane, network, server-side encryption and client-side encryption controls.
- [ ] I can select and reconcile SDK, pipeline, streaming, Spark and IoT movement paths.
- [ ] I can deploy resources/index changes safely with IaC and execute throughput/failover operations through controlled runbooks.
- [ ] I have rechecked the official blueprint, lifecycle, product support notices, limits and vendor-course freshness before booking.

---

## Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick the formats and gaps that work for you: one current primary path, hands-on labs, targeted documentation, and one ethical readiness check are usually more useful than passively completing every course. Times are page-published durations where available; otherwise they are clearly labeled estimates. Catalogs, durations, prices, access, and blueprint alignment change—verify them before purchase. Practice products should teach and explain; do not use brain dumps or material claiming real exam questions.

### Start with Microsoft

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official DP-420 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-420) | Public | 45–75 min for blueprint mapping | Authoritative July 21, 2026 scope, weights, update log and links |
| [DP-420 Microsoft Learn course page](https://learn.microsoft.com/en-us/training/courses/dp-420t00) | Public self-study; paid instructor option | 4 instructor-led days; roughly 25–40 hours self-study plus labs (estimate) | Primary structured path across the published domains |
| [Azure Cosmos DB documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/) | Public | 15–30 hours selectively (estimate) | Current product truth, limits, SDK guidance and deep remediation by objective |
| Microsoft free Practice Assessment, linked on the [credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-cosmos-db-developer-specialty/) | Public; sign-in may be required | 45–90 min per attempt plus review (estimate) | Diagnostic baseline and gap review; explanations are more valuable than memorizing answers |
| [Microsoft exam sandbox](https://aka.ms/examdemo) | Public | 20–30 min | Question-interface familiarity, not technical coverage |
| [Azure Cosmos DB for NoSQL .NET samples](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/samples-dotnet) | Public | 4–12 hours selectively (estimate) | Current .NET SDK patterns to run, alter, instrument and break safely |

### Video and expert learning

| Resource | Access | Estimated time | Best use and freshness note |
|---|---|---:|---|
| [Pluralsight DP-420 path](https://www.pluralsight.com/paths/designing-and-implementing-cloud-native-applications-using-microsoft-azure-cosmos-db-dp-420) | Paid/trial depending plan | 9 hours published, plus labs/review | Five-domain path with a practice exam; page showed course updates through January 2026. Gap-check the July Fabric/time-travel and blueprint additions. |
| [O'Reilly Azure Cosmos DB Developer Specialty course](https://www.oreilly.com/videos/azure-cosmos-db/0636920986164/) | Paid subscription/trial | 4h34m published, plus practice | Mohit Batra, January 2025; broad exam course with quizzes. Reconcile legacy Synapse Link and July 2026 changes. |
| [O'Reilly DP-420 crash course](https://www.oreilly.com/live-events/exam-dp-420-microsoft-azure-cosmos-db-developer-crash-course/0636920079751/) | Paid; schedule/access varies | Four hours published when scheduled | Reza Salehi live overview; verify next event dates and treat older “Core/SQL API” wording as API for NoSQL terminology. |
| [Udemy DP-420 hands-on course](https://www.udemy.com/course/azure-cosmosdb-database/) | Paid; price varies | 6h47m / 64 lectures published, plus labs | Page showed July 2026 update and many demos, but also an older “October 2023 topics” claim; gap-check every July 2026 addition. |
| [Microsoft Azure Cosmos DB YouTube channel](https://www.youtube.com/@AzureCosmosDB) | Public | 3–10 hours selectively (estimate) | Product announcements, engineering explanations and demos; select videos by weak objective and date. |
| [Microsoft Reactor YouTube channel search for Cosmos DB](https://www.youtube.com/@MicrosoftReactor/search?query=Cosmos%20DB) | Public | 2–8 hours selectively (estimate) | Workshops and developer sessions; verify product version and avoid treating any one playlist as full exam alignment. |
| [John Savill Azure Cosmos DB channel search](https://www.youtube.com/@NTFAQGuy/search?query=Cosmos%20DB) | Public | 1–4 hours selectively (estimate) | Supplemental Azure architecture explanations; not a complete DP-420 course. Check video descriptions for linked whiteboards/resources. |

### Books, practice, and labs

| Resource | Access | Estimated time | Best use and caution |
|---|---|---:|---|
| [Microsoft Press DP-420 video by Tim Warner](https://www.microsoftpressstore.com/store/exam-dp-420-designing-and-implementing-cloud-native-9780137951222) | Paid | 11+ hours published | Hands-on 2023 course. Strong foundation, but reconcile all July 2026 objectives, Fabric mirroring, hierarchical keys, and current product notices. |
| [Whizlabs DP-420 training and practice](https://www.whizlabs.com/microsoft-azure-certification-dp-420/) | Paid; offering varies | Approximately 8–15 hours for course/labs/practice (estimate; page did not expose reliable counts) | Additional labs and readiness checks; verify counts, update date and July 2026 alignment before purchase. |
| [MeasureUp DP-420 practice test](https://www.measureup.com/microsoft-practice-test-dp-420-designing-and-implementing-cloud-native-applications-using-microsoft-azure-cosmos-db.html) | Paid; demo available | 2–4 hours per full attempt and explanation review (estimate) | Page listed 120 questions but a June 2022 release and older objective terminology. Use for reasoning practice only after verifying current alignment. |
| [Udemy DP-420 topic catalog](https://www.udemy.com/topic/microsoft-dp-420/) | Paid catalog; price varies | Varies | Compare recent course/practice options, instructor updates, previews and explanations. Reject any product claiming leaked/real exam content. |
| [Azure Cosmos DB design-pattern samples](https://github.com/Azure-Samples/cosmos-db-design-patterns) | Public | 6–15 hours selectively (estimate) | Implement and benchmark patterns such as hierarchical partitioning; turn examples into measured labs rather than copying blindly. |

### A practical study sequence

1. Spend 45–75 minutes mapping the official blueprint to what you can demonstrate today.
2. Complete the Microsoft Learn path or one current structured alternative; do not stack several passive courses.
3. Build Labs 1–5 and retain RU, diagnostics, partition, index, consistency, and replay evidence.
4. Read the exact official docs for every failed experiment and uncertain answer; complete Labs 6–8.
5. Take the free Microsoft Practice Assessment once, review every option, and map gaps back to the July blueprint.
6. Use one paid practice product only if explanations and current-objective alignment add value.
7. Recheck the official study guide, credential page, lifecycle, support notices, limits and pricing immediately before the exam.

---

*This guide is an independent public-source synthesis. It is not affiliated with or endorsed by Microsoft, GitHub, HashiCorp, or any training provider.*
