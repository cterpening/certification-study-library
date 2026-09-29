---
exam_code: MONGODB-ASSOCIATE-DATA-MODELER
vendor_id: mongodb
official_blueprint: https://learn.mongodb.com/courses/associate-data-modeler-exam-study-guide
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# MongoDB Associate Data Modeler Study Guide

> **Independent AI-assisted resource — PUBLIC SOURCES REVIEWED; CURRENT OBJECTIVE BODY AND HUMAN REVIEW PENDING.** The September 29, 2026 review adds 40 answered prompts and 34 executed Python prediction checks. No MongoDB deployment or server lab was executed. See the [coverage record](../docs/SOURCE-VALIDATION.md#mongodb-associate-data-modeler-coverage-record).

**CURRENT BLUEPRINT — retained evidence baseline:** Requirements Gathering 10%, Entities 13%, Relationships 8.5%, Workload/Usage 10%, Data Model Design 28%, Modeling for Technical Requirements 10%, Indexing 13%, Monitoring and Evolving Data Models 7.5%. The 15 statements and eight weights remain the September 2 baseline; they were **not** confirmed unchanged in this review. The canonical [study-guide landing](https://learn.mongodb.com/courses/associate-data-modeler-exam-study-guide) lists a free 30-minute guide and enrollment. Its public linked viewer failed, and the published document asset returned 403. No account access or enrollment occurred.

**VERIFY CURRENT — conflicting exam contracts:** The [main exam page](https://learn.mongodb.com/pages/mongodb-associate-data-modeler-exam) lists 75 multiple-choice questions and 110 minutes. The [course exam route](https://learn.mongodb.com/courses/mongodb-associate-data-modeler-exam), still linked from the learning path, lists 70 questions, including 60 scored and 10 unscored, and 105 minutes. Both list English, no prerequisite and USD 150; the main page states online proctoring. Use the main page as the public preparation reference, but confirm the actual appointment before paying. This review does not resolve which contract a booking will apply or establish a passing score or detailed retake policy.

**Experience target:** Practice requirements, JSON/document shapes, queries, aggregation and design tradeoffs. Treat this as preparation advice, not a newly verified prerequisite; the public pages list none.

**VERIFY CURRENT — scope and releases:** The [August 18 certification announcement](https://www.mongodb.com/company/blog/news/introducing-a-more-connected-flexible-path-to-certifications) connects learning paths and skill badges and advertises a full-path completion discount. It does not announce a replacement exam. No dated replacement was identified in the accessible pages, a limited observation while current objective content remains unavailable. The [9.0 release opening](https://www.mongodb.com/docs/manual/release-notes/9.0/) includes Upcoming patch labels despite current/preview manual wording. Check deployed server and feature compatibility versions before using newly documented behavior; the navigation label does not establish availability or exam scope.

## How to use this guide

Choose one realistic application and carry it through the entire design loop: requirements → entities → relationships → workload table → candidate models → indexes → evidence → evolution. Keep the rejected alternatives. A correct answer depends on constraints; “always embed” and “always normalize” are both warning signs.

Use a free Atlas project or an authorized disposable local deployment with synthetic data. Generate enough volume and skew to expose growth and index effects. Capture query shapes, `explain` output, document sizes, validation rules, migration checkpoints, and rollback evidence. Do not use recalled live items, answer dumps, or products advertising “actual questions.”

> **About related items:** A `Related item:` callout adds prerequisite, architecture, security, governance, or operations context. It helps connect an objective to production practice but does not claim MongoDB uses that exact wording in the official study guide.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Requirements Gathering | 10% | Signed-off constraints, priorities, assumptions, and unresolved questions |
| Entities | 13% | Entity/attribute/type/owner catalog with persistence decisions |
| Relationships | 8.5% | Cardinality, skew, lifecycle, and strong/weak entity map |
| Workload/Usage | 10% | Measured read/write/aggregation table with frequency and latency targets |
| Data Model Design | 28% | Compared document models with pattern and anti-pattern reasoning |
| Modeling for Technical Requirements | 10% | Validation, lifecycle, analytics, transaction, and distribution decisions |
| Indexing | 13% | Query-shaped index plan plus explain and write-cost evidence |
| Monitoring and Evolving Data Models | 7.5% | Versioned migration, compatibility, observation, rollback, and cleanup plan |

## 1. Requirements Gathering — 10%

Begin with business operations, not documents. Identify actors, decisions, commands, queries, reports, service-level objectives, correctness rules, retention, residency, privacy, audit, ownership, expected growth, failure behavior, and budget. Separate facts from assumptions. “Fast” is not a requirement until it has a percentile, load, dataset, and environment.

Prioritize operations by business importance and frequency. A rare regulatory export may be critical despite low frequency; a high-volume feed may tolerate eventual consistency. Record the fields each operation reads or changes, filtering and sort requirements, result size, atomicity boundary, acceptable staleness, peak concurrency, and whether a calculation can be precomputed.

Inventory source systems and data quality. Identify identifiers, units, time zones, null/missing meaning, duplicate rules, ownership, update authority, and reconciliation. Ask which service owns each fact and whether a MongoDB copy is authoritative, cached, derived, or historical. Define deletion and correction propagation before duplicating data.

Create testable acceptance criteria: representative documents, workload mix, latency/resource thresholds, maximum document/array growth, recovery objectives, and correctness invariants. Track unanswered questions that could reverse embedding, referencing, precomputation, or index decisions.

`Related item:` Threat modeling belongs in requirements. Tenant isolation, field sensitivity, encryption, least privilege, auditability, and data minimization can change document and collection boundaries even when another shape is faster.

### Turn requirements into a falsifiable workload

The official [schema-design process](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/) and [workload method](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/identify-workload/) begin with operations. The following numbers are original assumptions for a fictional shop, not observed service performance.

| Operation | Assumed demand and result | Correctness and evidence |
|---|---|---|
| Recent order view | 200 reads/s at peak; newest 20 orders for one tenant/customer | Stable ordering, tenant scope and bounded result; measure p95 on representative skew |
| Shipment update | 20 writes/s; one order's permitted state transition | Guard current revision/state; preserve total ordered and shipped units |
| Daily sales tile | 100 reads/s; freshness within 60 seconds | Reconcile derived cents to accepted event identities; record refresh lag |
| Required export | One monthly job, potentially all retained orders | High priority despite low frequency; complete identities, authorized fields and retention boundary |

An average response time cannot establish a p95 target. A count of exported rows cannot establish correct identities. Name the observation and its denominator before choosing a model.

## 2. Entities — 13%

An entity is a distinguishable concept the application must persist. Extract candidate entities from domain language and operations, then identify attributes, identifiers, types, optionality, defaults, lifecycle, and owner. Do not make every input object a collection: request DTOs, calculated views, transient workflow state, and persisted domain facts serve different purposes.

Group entities into coherent domains or bounded contexts. The same word may have different meaning and ownership in sales, fulfillment, identity, and finance. A customer profile owned by identity is not automatically the same aggregate as an order’s historical shipping snapshot. Mark authoritative versus copied fields and name the synchronization rule.

Strong entities have an independent identity and lifecycle. Weak entities depend on an owning entity and may be identified partly by that relationship. Weak, bounded child data often fits embedding because ownership and deletion align; an independently queried or shared child may deserve its own collection. This is a design clue, not an automatic rule.

Choose BSON types deliberately. Preserve dates as dates, identifiers in their intended representation, exact decimals where required, and arrays only where growth is understood. Distinguish missing, explicit `null`, empty collection, and default value because queries, validation, indexes, and updates can treat them differently.

`Related item:` Data contracts should cover semantics as well as shape. A syntactically valid field can still be wrong when currency, unit, time-zone, classification, or ownership meaning is ambiguous.

## 3. Relationships — 8.5%

Map one-to-one, one-to-few, one-to-many, many-to-many, and hierarchical relationships. For each, record direction, ownership, cardinality now and at expected scale, maximum and skewed cases, update rate, access together, consistency needs, and deletion behavior. Average cardinality can hide a small set of tenants whose arrays or documents grow without bound.

Embedding places related data in one document. It favors locality, one-operation reads, and single-document atomic changes when data is owned, bounded, and usually accessed together. Referencing gives independently growing or shared entities their own documents. It reduces duplication and document growth but may require multiple queries, application composition, or `$lookup`.

Model the common access path without making exceptional paths impossible. For many-to-many relationships, decide whether references live on one side, both sides, or in an association collection; consider fan-out, update cost, and traversal direction. For hierarchies, compare parent references, child arrays, materialized paths, and other patterns against depth and query needs.

When duplicating related data, name the source of truth, copied subset, propagation event/job, idempotency key, stale-data tolerance, reconciliation, and privacy deletion behavior. A snapshot such as an order’s purchased price may intentionally never synchronize; a copied display name may.

`Related item:` MongoDB single-document writes are atomic. Document boundaries therefore express both retrieval locality and a concurrency boundary; distributed transactions should solve genuine multi-document invariants, not compensate for an avoidable model mismatch.

### Skew changes the relationship decision

The [relationship method](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/map-relationships/) weighs access and update patterns together. In the workbook, 99 customers have 10 orders each and one has 10,010. The mean is 110, which disguises the large customer. A recent-20 subset stores 1,010 hot references and leaves 9,990 historical references elsewhere. The subset bounds the parent array; it does not bound the archive, enforce deletion, or prove which orders are newest. An order's purchased price is a historical fact; a copied current display name has a different synchronization contract.

## 4. Workload/Usage — 10%

Build a workload table for every significant operation: actor/action, read or write, filter, sort, projection, aggregation/update, returned or changed fields, frequency, peak concurrency, latency target, priority, consistency, and expected growth. Add representative data distribution and skew. Use production telemetry when authorized; otherwise state the assumptions behind synthetic load.

Query shape matters more than collection size alone. `find` by tenant and status sorted by date differs from lookup by `_id`; a monthly aggregate differs from a dashboard refreshed each second. Trace aggregation pipelines stage by stage and identify opportunities to filter early, project less, avoid unnecessary unwinds/lookups, or precompute expensive stable results.

Model writes too. Append-heavy telemetry, frequently changing counters, large document replacements, fan-out updates, and synchronization of duplicates impose different costs. Determine whether arrays remain bounded, whether updates target one document, and whether concurrent operations can safely use operators such as `$inc`, conditional filters, or transactions.

Rank optimization work by business impact. Do not deform the whole model for a low-value rare query if an analytical copy, archive, scheduled computation, or separate read model is more appropriate. Revisit requirements when two top-priority operations demand incompatible shapes.

`Related item:` A workload is a living contract. Store anonymized query-shape metrics and acceptance thresholds so later teams can distinguish an evidence-based design from an undocumented preference.

## 5. Data Model Design — 28%

Generate at least two candidate models and compare them against the workload. Use the principle that data accessed together can be stored together, tempered by bounded growth, ownership, consistency, write amplification, duplication, sharding, and lifecycle. Include example documents and walk through the top reads and writes.

Embedding versus referencing is often selective. Embed a bounded order-line snapshot while referencing the current catalog product; embed recent items and archive older items; keep a canonical entity and duplicate only fields required by a hot read. Avoid treating relational normalization or maximum denormalization as an end in itself.

Know the intent and tradeoffs of common patterns:

- Attribute: turn similarly queried dynamic attributes into consistent key/value elements; consider multikey index size.
- Bucket: group bounded measurements/events by time or count; define close/reopen and late-arrival behavior.
- Computed: store expensive, read-heavy derived values; define refresh, drift, and reconciliation.
- Extended reference: copy a frequently read subset of a referenced entity; govern staleness.
- Subset: keep a hot bounded subset with the parent and move the remainder elsewhere.
- Outlier: preserve a common compact model while treating exceptional large cases separately.
- Polymorphic: keep related types together with discriminators and shared access patterns.
- Schema versioning: support controlled shape evolution and reader compatibility.

Recognize anti-patterns: unbounded arrays, bloated documents, excessive collections, unnecessary indexes, overuse of `$lookup`, inconsistent mixed types, and duplicated facts without ownership. The correction is workload-dependent: bound/archive an array, split a large cold subset, consolidate collections with a discriminator, remove proven-unused indexes, or redesign locality.

Validate assumptions with sample documents at typical and worst-case sizes. Test creation, hot reads, updates, deletion, aggregation, and failure/concurrency. A model that produces a fast demo with 100 uniform documents may fail under real skew, working-set pressure, or write amplification.

`Related item:` Command Query Responsibility Segregation can justify separate write and read representations, but it introduces synchronization, observability, and failure-recovery work. Use it because measured priorities require it, not as a default label.

### Give every pattern a failure case

The [pattern catalog](https://www.mongodb.com/docs/manual/data-modeling/design-patterns/), [application step](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/apply-patterns/), [computed-value overview](https://www.mongodb.com/docs/manual/data-modeling/design-patterns/handle-computed-values/) and [grouping overview](https://www.mongodb.com/docs/manual/data-modeling/design-patterns/group-data/) support the design vocabulary. Their linked implementations are further reading, not completed labs in this review.

| Candidate | Benefit for the shop | Condition that changes the choice |
|---|---|---|
| Embed bounded order lines and address snapshot | Read locality and one-document transition | Unbounded history, shared mutable ownership or excessive document size |
| Reference catalog and retain purchased price | Current product independence with historical price meaning | Readers mistakenly replace purchased price with the current catalog price |
| Recent-order subset | Bounded hot view | No reliable order rule or repair path; historical queries still need an indexed source |
| Computed daily total | Less repeated aggregation | Duplicate events, lost corrections or freshness requirements exceed the refresh design |
| Count/time bucket | Fewer grouped documents | Late arrivals, hot updates or uneven event sizes exceed the chosen bounds |
| Outlier storage | Keeps common documents compact | Readers never follow the overflow marker, silently omitting exceptional data |

The [document reference](https://www.mongodb.com/docs/manual/core/document/) establishes the 16 MiB document limit. The workbook uses a deliberately smaller 12 MiB planning budget, a 1,024-byte base and an assumed 512 bytes per item: at most 24,574 items by that arithmetic. Doubling assumed item size reduces capacity to 12,287. These are **not BSON measurements**; encoding overhead, variable values, indexes and future updates need actual measurement and headroom. A fixed element count alone cannot prove a byte bound.

The [2020 performance article](https://www.mongodb.com/company/blog/technical/performance-best-practices-mongodb-data-modeling-and-memory-sizing) remains useful background for locality and working-set thinking. Its historical Atlas feature and availability language is not a current service guarantee.

## 6. Modeling for Technical Requirements — 10%

Translate explicit constraints into design choices. JSON Schema validation can enforce required fields, BSON types, enums, ranges, and structural rules. Plan validation rollout for existing data and compatible applications; a strict rule enabled before backfill can break production writes.

Use document-level atomicity for invariants that naturally fit together. For multi-document transactions, evaluate necessity, retry behavior, duration, contention, and operational cost. Use idempotent operations and stable identifiers where networks can retry work. Define read and write concerns from correctness and availability needs rather than memorized defaults.

Handle lifecycle deliberately. TTL indexes fit expiring documents where asynchronous deletion semantics are acceptable; they are not an exact scheduler. Archive or online-archive choices affect access, cost, indexes, and compliance. Capped collections, time-series collections, GridFS, encrypted fields, and search/vector features solve particular requirements and should not be substituted casually.

Design for distribution when required. Choose a shard key using cardinality, frequency, monotonicity, query targeting, growth, and hotspot risk. A model and compound indexes must support shard-aware query patterns. Large cross-shard joins or transactions may signal a boundary problem.

Analytics may be computed on demand, stored through a computed pattern, or served from a separate analytical system. Compare freshness, compute cost, update complexity, reconciliation, and governance. Aggregation is part of the workload evidence, not an excuse to ignore document design.

`Related item:` Data governance includes lineage, classification, retention, legal hold, correction, deletion, and access review. Duplicated or archived fields must remain discoverable so a compliance action reaches every authorized copy.

### Validation, consistency and expiry are separate contracts

[JSON Schema validation](https://www.mongodb.com/docs/manual/core/schema-validation/specify-json-schema/) uses MongoDB's documented draft-4-based subset and BSON-specific types. A generic Python predicate or JSON Schema library does not test those server semantics. Structural validity also does not establish an authorized actor or a reconciled historical total.

The [validation-level reference](https://www.mongodb.com/docs/manual/core/schema-validation/specify-validation-level/) distinguishes `strict` and `moderate`. Strict checks inserts and updates, including updates to invalid legacy documents; merely enabling it does not scan or repair all stored documents. Moderate still checks inserts and updates to already valid documents, but does not require an update to an already invalid document to become valid. Choose the validation action separately, and audit/backfill old data explicitly. **VERIFY CURRENT:** The page also describes a 9.0 `constraint` level and preparation/full-scan requirements. Treat that as version-specific further reading, not a feature assumed available in every deployment or required by the retained exam baseline.

Use [single-document atomicity](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/) with an expected current value when a migration must avoid overwriting a concurrent writer. An application read/check followed by an unguarded write has a gap. The workbook's pure function assumes an indivisible revision test; a real database lab must put the guard in the mutation filter and inspect the match result. Multi-document receipts, archives and aggregates require their own transaction or recovery design.

[TTL documentation](https://www.mongodb.com/docs/manual/core/index-ttl/) describes asynchronous background deletion, not exact removal at a deadline. Missing/non-date expiry values may not expire; date arrays use their earliest date. Replicas apply primary-side deletions. Shortening a TTL can create a deletion backlog. The reviewed page contains inconsistent time-series field guidance between sections, so this guide does not prescribe a time-series TTL index recipe. Verify the exact collection type and version before a real lab. An application access cutoff and confirmed physical deletion are separate requirements.

## 7. Indexing — 13%

Derive indexes from complete query shapes. Consider equality predicates, sort, range, projection, selectivity, frequency, and returned count. Compound field order determines usable prefixes and whether a sort can be supported; equality/sort/range guidance is a reasoning aid, not a substitute for `explain` on representative data.

Understand the roles and constraints of `_id`, single-field, compound, multikey, unique, partial, sparse, TTL, wildcard, text/search, hashed, and geospatial indexes at the level relevant to the model. Do not select an index type merely because it exists. Array fields create multikey behavior; unique, partial, collation, shard, and compound-array interactions require exact documentation checks.

Use `explain("executionStats")` to compare candidate designs. Inspect winning stages, keys and documents examined, documents returned, in-memory sort indicators, and execution behavior across representative distributions. A covered query can avoid fetching documents when filter/projection and index align. Small warm tests do not prove production performance.

Every index consumes disk and memory and adds work to writes. Track redundant prefixes, unused indexes, build impact, and index fit as workloads change. Before removal, confirm observation period, hidden/rollback options where supported, downstream consumers, and recovery time.

`Related item:` An index cannot fix an unbounded or badly owned document. When required indexes become numerous, wide, or highly multikey, revisit the schema and workload priorities before adding another one.

### Read an execution plan without overclaiming

The [ESR guidance](https://www.mongodb.com/docs/manual/tutorial/equality-sort-range-guideline/) supports testing equality/sort/range ordering against a selective range-before-sort alternative. For tenant/status equality followed by date ordering, record the complete sort and tie-breaker. For each candidate, compare returned identities before timing. The [unique](https://www.mongodb.com/docs/manual/core/index-unique/) and [multikey](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-multikey/) rules add constraints: one indexed array field per document in a compound multikey index, uniqueness across documents rather than deduplication inside one array, and limited covered-query cases. Returning the array or using `$elemMatch` prevents the documented multikey covering case. A regular single-field unique index also makes missing/null a shared null key; partial filters and sharding change the scope to check.

The [explain reference](https://www.mongodb.com/docs/manual/reference/explain-results/) says `explain` ignores existing plan-cache entries and does not cache its winning plan. `executionTimeMillis` includes selection/execution but excludes network transfer; it is not steady-state end-to-end request latency. `totalDocsExamined` counts examinations, potentially repeated, not distinct documents. `totalKeysExamined` counts index entries; `nReturned` reports returned results. Engine/stage shapes vary. Save the query, data distribution, version, plan and repeated workload timings separately. No plan or database benchmark was executed for this review.

## 8. Monitoring and Evolving Data Models — 7.5%

Observe model health through slow-query evidence, query profiler/diagnostic data used within policy, Atlas Performance Advisor or equivalent tooling, `explain`, index usage, document/array growth, working set, storage, write latency, and application errors. Correlate database symptoms with release and traffic changes. Recommendations are inputs, not automatic commands.

Define triggers for redesign: breached latency/resource SLOs, new priority queries, persistent collection scans, unbounded growth, hot shards, costly synchronization, validation failures, or regulatory changes. Diagnose query, index, model, application, and capacity together. Removing symptoms without understanding causality can move cost elsewhere.

Evolve schemas compatibly. A common expand/migrate/contract flow is: deploy readers that understand old and new shapes; permit/write the new shape; backfill in bounded resumable batches; measure and reconcile; switch reads; then remove old fields and obsolete indexes after rollback windows. Record schema versions when readers need explicit branching.

Make migrations idempotent, checkpointed, rate-limited, observable, and recoverable. Test mixed-version applications, partial progress, retries, rollbacks, secondary effects, validation changes, index builds, and privacy/retention. Preserve evidence that counts and invariants match before cleanup.

`Related item:` Change streams or event-driven synchronization can propagate model changes, but consumers need resume-token handling, idempotency, ordering assumptions, dead-letter/replay controls, and reconciliation. An event is not proof every copy converged.

### Prove migration completeness and rollback representability

The [schema-versioning pattern](https://www.mongodb.com/docs/manual/data-modeling/design-patterns/data-versioning/schema-versioning/) allows mixed shapes. Supporting both shapes means testing both readers, writers and relevant index paths. For a single `shipment` becoming a `shipments` list, preserve identity and unit totals, reject unknown versions and guard stale revisions. Replaying an already migrated record can be a no-op with a current revision; an old revision still requires reconciliation.

A high-water checkpoint of 4 does not prove records 1–4 migrated when 3 failed and 4 succeeded. Keep a contiguous completion frontier or explicit failed identities, then reconcile the intended set. Equal counts can also hide replacing missing identity 3 with unexpected identity 5. Finally, rolling two shipments back into one is not a shape-only reversal: v1 cannot represent the new state without a chosen, potentially lossy business transformation. Stop incompatible writes, reconcile and choose a forward repair or an explicitly designed recovery. Do not discard a shipment to make a rollback command succeed.

## Integrated scenarios

### Scenario 1: Commerce ordering

Use the fictional workload table to compare an order aggregate with a normalized collection-per-entity alternative. Keep bounded purchased line/address facts with the order and reference independently changing catalog data. For the large customer, use a bounded recent subset plus a complete historical source. Deliver an ownership map, two candidate shapes, top read/write traces and a size/growth budget. Evolve one shipment to many with revision guards and identity/unit reconciliation. Demonstrate why a two-shipment order cannot automatically roll back to the single-shipment representation.

### Scenario 2: Multi-tenant learning platform

Keep an enrollment's current progress small; let attempts grow in their own lifecycle. Define which lesson version an attempt addresses and whether a completion is historical or recalculated after edits. A computed dashboard needs tenant-scoped event identities, replay handling, freshness and full reconciliation. In the local arithmetic example, accepted events total 1,800 cents while blind duplicate delivery totals 2,600; substitute completed units for money only after defining correction semantics. Produce a denied cross-tenant query case and projection review in a real authorized lab. Trusted fixture labels alone would not prove isolation.

### Scenario 3: IoT monitoring

Compare one record per measurement, explicit bounded buckets and a native time-series collection against late arrivals and per-device skew. At a chosen cap of 100, 10,010 readings require 101 buckets arithmetically; variable byte size can force more. State close/reopen policy, duplicate identity and late correction handling. Separate an application's visibility cutoff from asynchronous TTL deletion and verified archive completion. Capture actual version-specific behavior before selecting a time-series TTL recipe; the general reference's inconsistent field guidance remains unresolved here.

## Hands-on evidence labs

**Execution boundary:** The Python workbook below was run successfully with 34 checks. It uses only local standard-library objects and arithmetic. It does not emulate MongoDB, encode BSON, execute JSON Schema validation, authenticate tenants, measure performance, persist receipts or test actual concurrency. Its revision check assumes an indivisible transition. The eight following deployment activities are proposed, not completed.

| Lab | Procedure and evidence | Failure or counterexample to include |
|---|---|---|
| 1. Requirements packet | Produce an actor/operation table with filters, sort, projection, frequency, priority, latency percentile, freshness and growth; record assumptions | A rare export remains critical; mean latency cannot prove a percentile |
| 2. Ownership and relationship map | Mark canonical, copied, derived and historical fields; record p50/max cardinality and lifecycle | One high-volume customer invalidates a design based only on the mean |
| 3. Candidate documents | Implement two shapes in an authorized disposable database; trace top reads/writes and actual encoded sizes | Doubling item size breaks a count-only growth estimate |
| 4. Pattern experiment | Build subset, computed, bucket and outlier examples with reconstruction/reconciliation paths | Replay and late arrivals; overflow data must remain visible |
| 5. Technical constraints | Test MongoDB validation action/level and guarded writes using actual server results | Invalid legacy documents, stale revision and repeated request; no broad validation bypass |
| 6. Index experiment | Compare complete query shapes, returned identities, plans and repeated workload latency; record write/storage cost | Skew, multikey restrictions and cache-independent explain behavior |
| 7. Evolution drill | Run mixed readers/writers, bounded backfill, checkpoint reconciliation and recovery | Hole below the high-water mark, unknown version and a lossy reverse transform |
| 8. Operational review | Correlate growth, lag, errors and slow shapes; alter one variable and retain rollback evidence | TTL expiry is asynchronous; an advisor suggestion alone is not a safe change |

### Executed prediction workbook

Save this original program as `modeler_workbook.py` and run it with Python 3. It prints the checks and results. It expects 34 passes, 1,010 hot items, 9,990 archived items, 1,800 computed cents and a checkpoint hole at identity 3. The receipts are process-local, sequential and non-durable; no exactly-once delivery claim follows. The validation decision function illustrates whether a write should be checked, not whether a BSON document passes an actual rule. The final historical-validity fixture demonstrates that configuration alone does not mutate old data.

```python
import copy
import json
import math

checks = []


def check(name, condition):
    assert condition, name
    checks.append(name)


def rejects(name, call):
    try:
        call()
    except ValueError:
        checks.append(name)
    else:
        raise AssertionError(name)


counts = [10] * 99 + [10010]
check("average hides outlier", sum(counts) / len(counts) == 110)
check("maximum differs from average", max(counts) == 10010)
hot_limit = 20
hot = [min(n, hot_limit) for n in counts]
archive = [max(0, n - hot_limit) for n in counts]
check("subset cap", max(hot) == hot_limit)
check("subset conservation", sum(hot) + sum(archive) == sum(counts))
check("archive still needs lifecycle", sum(archive) == 9990)
budget, base_bytes, assumed_item_bytes = 12 * 1024 * 1024, 1024, 512
capacity = (budget - base_bytes) // assumed_item_bytes
check("arithmetic capacity", capacity == 24574)
check("next item crosses assumed budget", base_bytes + (capacity + 1) * assumed_item_bytes > budget)
check("variable size changes bound", (budget - base_bytes) // 1024 == 12287)
check("bucket count is ceiling", math.ceil(10010 / 100) == 101)

events = [("a", 1200), ("b", 800), ("c", -200)]
delivery = events + [events[1]]
check("blind replay overcounts", sum(v for _, v in delivery) == 2600)
receipts = {}


def accept(event_id, amount):
    if type(amount) is not int:
        raise ValueError("integer cents required")
    if event_id in receipts and receipts[event_id] != amount:
        raise ValueError("same identity, changed intent")
    receipts[event_id] = amount


for event in delivery:
    accept(*event)
check("deduplicated computed value", sum(receipts.values()) == 1800)
check("receipt count", len(receipts) == 3)
rejects("changed replay rejected", lambda: accept("b", 900))
rejects("boolean is not a monetary amount", lambda: accept("x", True))
check("rejections preserve total", sum(receipts.values()) == 1800)
drifted_total = 1750
check("reconciliation finds drift", sum(receipts.values()) - drifted_total == 50)


def read_shipments(doc):
    version = doc.get("schemaVersion")
    if version == 1:
        return [copy.deepcopy(doc["shipment"])]
    if version == 2:
        return copy.deepcopy(doc["shipments"])
    raise ValueError("unknown schema version")


def migrate(doc, expected_revision):
    if doc["revision"] != expected_revision:
        raise ValueError("stale revision")
    if doc["schemaVersion"] == 2:
        return copy.deepcopy(doc)
    if doc["schemaVersion"] != 1:
        raise ValueError("unknown schema version")
    candidate = copy.deepcopy(doc)
    candidate["shipments"] = [candidate.pop("shipment")]
    candidate["schemaVersion"] = 2
    candidate["revision"] += 1
    return candidate


def rollback(doc):
    if doc["schemaVersion"] != 2 or len(doc["shipments"]) != 1:
        raise ValueError("v1 cannot represent this state")
    candidate = copy.deepcopy(doc)
    candidate["shipment"] = candidate.pop("shipments")[0]
    candidate["schemaVersion"] = 1
    candidate["revision"] += 1
    return candidate


old = {"_id": "order-1", "schemaVersion": 1, "revision": 7,
       "shipment": {"id": "parcel-1", "units": 3}}
new = migrate(old, 7)
check("migration preserves reader meaning", read_shipments(old) == read_shipments(new))
check("source fixture unchanged", old["schemaVersion"] == 1 and old["revision"] == 7)
check("revision advances", new["revision"] == 8)
check("replay with fresh revision is no-op", migrate(new, 8) == new)
rejects("stale retry rejected", lambda: migrate(new, 7))
rejects("unknown version rejected", lambda: read_shipments({"schemaVersion": 3}))
check("reversible single shipment", read_shipments(rollback(new)) == read_shipments(old))
split = copy.deepcopy(new)
split["shipments"] = [{"id": "parcel-1", "units": 1}, {"id": "parcel-2", "units": 2}]
check("split conserves units", sum(p["units"] for p in split["shipments"]) == 3)
rejects("lossy rollback refused", lambda: rollback(split))
check("failed rollback preserves split", len(split["shipments"]) == 2)

expected_ids = {1, 2, 3, 4}
completed_ids = {1, 2, 4}
checkpoint = max(completed_ids)
check("high checkpoint can hide hole", checkpoint == 4 and expected_ids - completed_ids == {3})
check("counts alone can hide substitution", len({1, 2, 4, 5}) == len(expected_ids))
check("identity reconciliation catches substitution", {1, 2, 4, 5} != expected_ids)


def validation_required(level, operation, old_valid=False):
    if level not in {"strict", "moderate"} or operation not in {"insert", "update"}:
        raise ValueError("unsupported case")
    return level == "strict" or operation == "insert" or old_valid


check("strict checks invalid legacy update", validation_required("strict", "update", False))
check("moderate exempts invalid legacy update", not validation_required("moderate", "update", False))
check("moderate checks valid legacy update", validation_required("moderate", "update", True))
check("both check inserts", all(validation_required(x, "insert") for x in ("strict", "moderate")))
historical_validity = [True, False, True]
check("enabling strict is not historical repair", sum(historical_validity) == 2)

print(json.dumps({"passed": len(checks), "checks": checks,
                  "results": {"mean_items": 110, "maximum_items": 10010,
                              "hot_items": sum(hot), "archived_items": sum(archive),
                              "assumed_capacity": capacity, "computed_cents": sum(receipts.values()),
                              "migration_revision": new["revision"], "checkpoint_hole": [3]}}, indent=2))
```

## Readiness checks

These original prompts are learning checks, not recalled exam items. Answer before reading the explanation.

1. **Can I convert a vague performance request into a measurable workload requirement?**

   Specify a percentile, peak load, dataset/distribution, environment and result shape. Keep an observable acceptance threshold, not just “fast.”

2. **Can I identify missing ownership, lifecycle, consistency, and governance information?**

   Name the owner of each fact, its source, retention/deletion needs, legal or business constraints, staleness allowance and unresolved assumptions that could reverse the design.

3. **Can I rank rare-critical and frequent-noncritical operations correctly?**

   Use business impact as well as frequency. A monthly required export can outrank a cosmetic high-volume tile; optimize both against explicit constraints.

4. **Can I distinguish authoritative, copied, derived, historical, and transient data?**

   Canonical data owns the fact; a synchronized copy follows it; a derived value is recomputed; a purchased-price snapshot preserves history; transient data may need no persistence.

5. **Can I identify persisted entities without creating a collection per object?**

   Separate domain facts from request/view objects. Choose persistence and aggregate boundaries from access, lifecycle and invariants rather than class names.

6. **Can I choose appropriate BSON types and explain missing versus null?**

   Choose date, identifier, numeric and array representations intentionally. Missing, null, zero and empty arrays carry different semantics; test actual BSON/query/validation behavior.

7. **Can I explain strong and weak entities with an ownership example?**

   An order line depends on its owning order and may use an order-plus-line identity. A shared product has an independent lifecycle; weakness is a clue, not a command to embed.

8. **Can I group entities into domains and identify cross-domain copies?**

   Record bounded contexts and the authoritative service. A copied name across contexts needs a propagation and reconciliation policy distinct from a historical snapshot.

9. **Can I map one-to-one, one-to-many, many-to-many, and hierarchy choices?**

   Map both traversal directions, ownership, lifecycle, cardinality and skew. Choose arrays, references or associations from the actual reads and writes, not relationship names alone.

10. **Can I spot cardinality skew hidden by averages?**

   Measure tail and maximum cardinality. The fixture mean is 110 despite a customer with 10,010 orders; a recent-20 subset makes the hot bound explicit.

11. **Can I explain how lifecycle and deletion affect embedding/reference choices?**

   Independently growing or retained children may need references. Embedded deletion can align with ownership, but legal retention or shared ownership may conflict.

12. **Can I govern duplicated fields and reconciliation?**

   Name source, copied fields, update trigger, identity, tolerated lag, reconciliation and deletion. Do not continuously synchronize an intentionally historical price.

13. **Can I produce a complete read query shape rather than a field list?**

   Include tenant/filter operators, sort and tie-breaker, projection, result bound, frequency and distribution. “Index customer” omits much of the contract.

14. **Can I characterize write frequency, contention, amplification, and retries?**

   Measure update shape, touched documents/bytes, concurrent hot keys, retries and fan-out. A cheap read may be bought with expensive synchronized writes.

15. **Can I trace an aggregation and explain how stage order affects work?**

   Track identity and row grain after every stage. An unwind can multiply rows and drop empty arrays; move work only when result semantics remain equivalent.

16. **Can I decide whether to precompute from freshness and cost requirements?**

   Compare refresh cost and lag with repeated query cost. Require event identity, correction handling and a source-of-truth reconciliation before trusting a stored total.

17. **Can I compare two candidate models against the same prioritized workload?**

   Use the same workload, constraints and representative data for both candidates. Include writes, lifecycle and operational cost; record the conditions under which each loses.

18. **Can I explain when embedding improves locality and atomicity?**

   Embedding helps when owned, bounded data is read or changed together. A document boundary can also make a required state transition atomic.

19. **Can I explain when referencing prevents unsafe growth or coupling?**

   Referencing supports independent growth, shared mutable entities and separate lifecycle, at the cost of composition/lookup and consistency work.

20. **Can I use selective duplication rather than all-or-nothing denormalization?**

   Retain only hot copied fields or immutable snapshots where useful. Make the authoritative owner and synchronization meaning visible.

21. **Can I select and justify attribute, bucket, computed, subset, or outlier patterns?**

   Use attribute for similarly queried varying fields, bucket for bounded groups, computed for derived reads, subset for a hot portion and outlier for exceptions; test each failure path.

22. **Can I recognize unbounded arrays, bloated documents, excess collections, and lookup overuse?**

   Look for growth without bounds, large cold fields, collection proliferation, unnecessary lookup work and missing ownership. Diagnose the workload before prescribing a remedy.

23. **Can I describe a polymorphic model and its discriminator/index implications?**

   Use a discriminator/version with defined readers and valid shared fields. Mixed shapes can need different query/index paths; unknown versions must not silently masquerade as known ones.

24. **Can I prove typical and worst-case document growth stays bounded?**

   Measure encoded BSON on typical and worst-case values, then enforce a growth policy. The workbook count is a planning estimate under fixed byte assumptions, not a server size proof.

25. **Can I roll out validation without breaking legacy documents and applications?**

   Deploy compatible readers/writers, audit existing data, backfill safely and choose validation action/level deliberately. Strict checks future writes; moderate can exempt updates to invalid legacy data.

26. **Can I explain when single-document atomicity removes a transaction need?**

   Keep naturally co-owned invariant fields in one document and guard current state in the mutation filter. Separate documents need a deliberate transaction or reconciliation design.

27. **Can I assess TTL, archive, time-series, and analytics requirements precisely?**

   Define visibility deadline, deletion evidence, retention and archive retrieval separately. TTL is asynchronous and collection/version-specific rules matter.

28. **Can I reason about shard-key targeting, distribution, and hotspot risk?**

   Assess cardinality, skew, monotonic insert pressure, query targeting and growth together. A high-cardinality key alone does not prove balanced load or targeted queries.

29. **Can I derive a compound index from equality, sort, range, and projection?**

   Start from equality predicates and required sort/range/projection; compare ESR and selective ERS hypotheses. Validate returned identities and representative plans, then workload timings.

30. **Can I explain prefixes, multikey behavior, uniqueness, and covered queries?**

   Prefixes and sort alignment matter; compound multikey limits and covering restrictions apply. Unique keys constrain a documented scope, including null/missing, partial-filter and sharding behavior.

31. **Can I interpret keys/documents examined and scan/sort evidence?**

   Compare keys examined, examinations of documents and returned results; document examinations can repeat. Explain timing omits network and does not represent an ordinary cached workload.

32. **Can I quantify index storage and write tradeoffs?**

   Record index bytes, build impact, write latency and representative read benefit before/after. A read improvement without write/storage cost is incomplete evidence.

33. **Can I identify when a model change is better than another index?**

   Revisit the model when unbounded data, ownership problems or many wide/multikey indexes dominate. An additional index does not repair an incorrect lifecycle or invariant.

34. **Can I use monitoring recommendations as evidence rather than commands?**

   Correlate recommendation, workload, version and representative measurements. Review change impact and recovery; do not apply an advisor suggestion solely because it exists.

35. **Can I define observable triggers for model evolution?**

   Set explicit triggers for document/array growth, latency, lag, validation errors, hot keys and business requirements, with measurement windows and responsible owners.

36. **Can I sequence an expand/migrate/contract rollout?**

   Expand compatible reads/writes, migrate bounded batches, reconcile identities and invariants, switch usage, then contract after a proven recovery window.

37. **Can I make a backfill bounded, resumable, idempotent, and reconcilable?**

   Use guarded idempotent transformations and a contiguous completion frontier or explicit failures. Checkpoint 4 with missing identity 3 is incomplete; equal counts can hide wrong identities.

38. **Can I test mixed versions, partial failures, retry, and rollback?**

   Test both versions, stale revisions, retries and partial completion. Refuse rollback when the old representation cannot preserve the new business state, such as two shipments in one slot.

39. **Can I preserve retention, privacy, and audit behavior through migration?**

   Track every canonical, copied, derived and archived field through the change. Reconcile access/deletion/retention obligations and audit identities before removing old paths.

40. **Can I defend a design with measured evidence and state when it should change?**

   Present assumptions, rejected alternatives, actual plans/results and explicit limits. State the growth or workload change that would invalidate the chosen design.

## Final preparation

- Reopen the live exam page and enrolled study guide; confirm contract, objectives, delivery, price, accommodations, and policies.
- Complete the official path selectively and repeat practice only after investigating each explanation and weak objective.
- Rebuild one scenario from requirements through evolution without notes and defend the losing alternatives.
- Practice timed reading: extract constraints before choosing a pattern or index.
- Stop using any source that promises recalled live questions, guaranteed passes, or “actual” items.
- Treat passing as one checkpoint; production modeling still requires peer review, representative tests, security/governance review, and measured operations.


## Places to learn

This is not a complete list or a prescription to consume everything. Public outlines and metadata do not prove lesson quality or exam completeness. Publisher times are identified; other ranges are study estimates. No paid lesson, practice-question interior, account enrollment or video playback was used in this review.

| Resource | Access | Estimated time |
|---|---|---|
| [Main exam page](https://learn.mongodb.com/pages/mongodb-associate-data-modeler-exam) and [course route](https://learn.mongodb.com/courses/mongodb-associate-data-modeler-exam): compare the conflicting contracts before booking | Public browser pages; automated routes return shells | 10–15 min review estimate; main 110-minute exam versus course 105 minutes |
| [Official study guide](https://learn.mongodb.com/courses/associate-data-modeler-exam-study-guide): canonical objective resource; current document unavailable here | Free enrollment listed; public viewer failed and document asset returned 403 | Publisher lists 30 min; historical 15 statements require reconciliation |
| [Current certification learning path](https://learn.mongodb.com/learning-paths/mongodb-data-modeling-certification-learning-path) and [earlier path URL](https://learn.mongodb.com/learning-paths/data-modeling-for-mongodb): same visible eight required cards | Public outline; free/account learning; advertised 50% full-path completion discount, eligibility unverified | Publisher headline 8 hr; required cards 515 min (8h35); separate 105-min exam makes 10h20 including exam |
| [Official practice questions](https://learn.mongodb.com/courses/associate-data-modeler-practice-questions): format practice with later explanation review | Free account/enrollment; public landing only read | Publisher lists 1 hr, plus personal review |
| [August 18, 2026 path announcement](https://www.mongodb.com/company/blog/news/introducing-a-more-connected-flexible-path-to-certifications): badge/path context, not replacement scope | Public first-party announcement by Heather Davis and Joel Lord | Publisher lists 4 min |
| [Schema-design process](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/) and [data-modeling overview](https://www.mongodb.com/docs/manual/data-modeling/): use the linked workflow against one application | Public; main overviews and selected child references read | 2–4 hr selected reading/exercise estimate |
| [Validation levels](https://www.mongodb.com/docs/manual/core/schema-validation/specify-validation-level/) and [schema versioning](https://www.mongodb.com/docs/manual/data-modeling/design-patterns/data-versioning/schema-versioning/): plan the legacy-data audit and mixed-reader rollout | Public; version-specific behavior requires deployed verification | 1–2 hr reading/lab estimate |
| [Explain results](https://www.mongodb.com/docs/manual/reference/explain-results/): distinguish plan counters from workload latency | Public; selected plan-cache, engine and counter sections read, no actual plan run | 1–2 hr selected reading/lab estimate |
| [Data modeling and memory sizing](https://www.mongodb.com/company/blog/technical/performance-best-practices-mongodb-data-modeling-and-memory-sizing): historical working-set/locality context by Henrik Ingo and Mat Keep, published January 28 and updated July 22, 2020 | Public article; historical Atlas feature claims not adopted as current guarantees | 45–90 min reading/model-review estimate |
| [High Performance with MongoDB](https://www.oreilly.com/library/view/high-performance-with/9781837022632/): optional book/video depth; current contents unverified | Paid/O’Reilly; public request returned 403, no interior reviewed | Earlier 10h16 and 2025 metadata not reverified |
| [MongoDB Essentials](https://www.oreilly.com/library/view/mongodb-essentials/9781806706099/): optional overview; current contents unverified | Paid/O’Reilly; public request returned 403 | Earlier 1h36 and 2025 metadata not reverified |
| [Schema Design Best Practices video](https://www.youtube.com/watch?v=QAqK-R9HUhc): optional visual format | Public title/footer only retrieved; video not played | Earlier about 10 min not reverified |
| [MongoDB — The Complete Developer’s Guide](https://www.udemy.com/course/mongodb-the-complete-developers-guide/): broad optional application course | Paid/Udemy; public request returned 403, no interior reviewed | Earlier about 17.5 hr not reverified |

The required path cards list CRUD 90, relational-to-document 75, patterns 60, advanced patterns 60, optimization 60, transformation 50, indexing 60 and performance 60 minutes: 515 total. The separate exam card lists 105 minutes, reproducing the course-route discrepancy with the main exam page's 110. These are visible catalog measures, not observed completion times.
