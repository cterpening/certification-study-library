---
exam_code: MONGODB-ASSOCIATE-DATA-MODELER
vendor_id: mongodb
official_blueprint: https://learn.mongodb.com/courses/associate-data-modeler-exam-study-guide
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# MongoDB Associate Data Modeler Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live exam page, free-enrollment study guide, newly aligned learning path, practice resource, product documentation, and selected learning links were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#mongodb-associate-data-modeler-coverage-record).

**Current baseline:** Requirements Gathering 10%, Entities 13%, Relationships 8.5%, Workload/Usage 10%, Data Model Design 28%, Modeling for Technical Requirements 10%, Indexing 13%, and Monitoring and Evolving Data Models 7.5%.<br>
**Exam contract:** The current public landing page lists 75 multiple-choice questions, 110 minutes, online-proctored delivery, English, no prerequisite, and USD 150. An older course route still exposes a 70-question/105-minute contract; use the current landing page and verify the appointment details before purchase.<br>
**Experience target:** No formal prerequisite is published. MongoDB describes this credential for experienced users familiar with JSON, MongoDB Query API operations and aggregations, data modeling, and simplicity-versus-performance tradeoffs. This is not a database-theory-only exam.<br>
**Upcoming change:** No retirement or dated replacement was found September 2, 2026. MongoDB announced newly connected certification paths and skill badges in August 2026, but not a replacement exam. Recheck the landing page, enrolled study guide, and path before scheduling.<br>
**Access note:** The official objective guide and practice questions are free but require enrollment/account access. The exam contract, learning-path outline, program news, and product documentation are publicly readable. This guide does not infer hidden course content.

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

## 6. Modeling for Technical Requirements — 10%

Translate explicit constraints into design choices. JSON Schema validation can enforce required fields, BSON types, enums, ranges, and structural rules. Plan validation rollout for existing data and compatible applications; a strict rule enabled before backfill can break production writes.

Use document-level atomicity for invariants that naturally fit together. For multi-document transactions, evaluate necessity, retry behavior, duration, contention, and operational cost. Use idempotent operations and stable identifiers where networks can retry work. Define read and write concerns from correctness and availability needs rather than memorized defaults.

Handle lifecycle deliberately. TTL indexes fit expiring documents where asynchronous deletion semantics are acceptable; they are not an exact scheduler. Archive or online-archive choices affect access, cost, indexes, and compliance. Capped collections, time-series collections, GridFS, encrypted fields, and search/vector features solve particular requirements and should not be substituted casually.

Design for distribution when required. Choose a shard key using cardinality, frequency, monotonicity, query targeting, growth, and hotspot risk. A model and compound indexes must support shard-aware query patterns. Large cross-shard joins or transactions may signal a boundary problem.

Analytics may be computed on demand, stored through a computed pattern, or served from a separate analytical system. Compare freshness, compute cost, update complexity, reconciliation, and governance. Aggregation is part of the workload evidence, not an excuse to ignore document design.

`Related item:` Data governance includes lineage, classification, retention, legal hold, correction, deletion, and access review. Duplicated or archived fields must remain discoverable so a compliance action reaches every authorized copy.

## 7. Indexing — 13%

Derive indexes from complete query shapes. Consider equality predicates, sort, range, projection, selectivity, frequency, and returned count. Compound field order determines usable prefixes and whether a sort can be supported; equality/sort/range guidance is a reasoning aid, not a substitute for `explain` on representative data.

Understand the roles and constraints of `_id`, single-field, compound, multikey, unique, partial, sparse, TTL, wildcard, text/search, hashed, and geospatial indexes at the level relevant to the model. Do not select an index type merely because it exists. Array fields create multikey behavior; unique, partial, collation, shard, and compound-array interactions require exact documentation checks.

Use `explain("executionStats")` to compare candidate designs. Inspect winning stages, keys and documents examined, documents returned, in-memory sort indicators, and execution behavior across representative distributions. A covered query can avoid fetching documents when filter/projection and index align. Small warm tests do not prove production performance.

Every index consumes disk and memory and adds work to writes. Track redundant prefixes, unused indexes, build impact, and index fit as workloads change. Before removal, confirm observation period, hidden/rollback options where supported, downstream consumers, and recovery time.

`Related item:` An index cannot fix an unbounded or badly owned document. When required indexes become numerous, wide, or highly multikey, revisit the schema and workload priorities before adding another one.

## 8. Monitoring and Evolving Data Models — 7.5%

Observe model health through slow-query evidence, query profiler/diagnostic data used within policy, Atlas Performance Advisor or equivalent tooling, `explain`, index usage, document/array growth, working set, storage, write latency, and application errors. Correlate database symptoms with release and traffic changes. Recommendations are inputs, not automatic commands.

Define triggers for redesign: breached latency/resource SLOs, new priority queries, persistent collection scans, unbounded growth, hot shards, costly synchronization, validation failures, or regulatory changes. Diagnose query, index, model, application, and capacity together. Removing symptoms without understanding causality can move cost elsewhere.

Evolve schemas compatibly. A common expand/migrate/contract flow is: deploy readers that understand old and new shapes; permit/write the new shape; backfill in bounded resumable batches; measure and reconcile; switch reads; then remove old fields and obsolete indexes after rollback windows. Record schema versions when readers need explicit branching.

Make migrations idempotent, checkpointed, rate-limited, observable, and recoverable. Test mixed-version applications, partial progress, retries, rollbacks, secondary effects, validation changes, index builds, and privacy/retention. Preserve evidence that counts and invariants match before cleanup.

`Related item:` Change streams or event-driven synchronization can propagate model changes, but consumers need resume-token handling, idempotency, ordering assumptions, dead-letter/replay controls, and reconciliation. An event is not proof every copy converged.

## Integrated scenarios

### Scenario 1: Commerce ordering

Design customers, products, carts, orders, payments, shipments, and historical price/address facts. Produce an entity/owner map, relationship cardinalities including high-volume customers, workload table, two candidate order models, snapshot versus synchronized fields, index plan, concurrency invariants, retention/deletion behavior, and a versioned migration from one shipment to split shipments.

### Scenario 2: Multi-tenant learning platform

Model organizations, users, courses, lessons, enrollments, attempts, progress, and analytics. Address tenant boundaries, many-to-many relationships, unbounded attempts, hot dashboards, rare audits, computed progress, compound/multikey indexes, role-sensitive projections, and a migration that adds lesson-version history without breaking old readers.

### Scenario 3: IoT monitoring

Model devices, metadata, measurements, alerts, maintenance, and retention. Compare one-document-per-reading, bucket, and time-series approaches. Include late/out-of-order data, per-device hotspots, TTL/archive semantics, threshold updates, recent-window queries, fleet aggregation, shard considerations, operational monitoring, and rollback from an unsafe bucket size.

## Hands-on practice

1. **Requirements packet:** Interview a fictional stakeholder from one scenario and produce a prioritized workload plus ten unresolved questions whose answers could change the model.
2. **Entity and relationship map:** Identify strong/weak entities, owners, types, cardinality, skew, lifecycle, and duplicated fields. Challenge every proposed collection.
3. **Candidate documents:** Implement at least two shapes for the same domain. Demonstrate top reads/writes and state the losing conditions for each.
4. **Patterns and anti-patterns:** Create bounded examples of four schema patterns, then deliberately create and remediate unbounded-array and bloated-document cases.
5. **Technical constraints:** Add validation and a correctness invariant. Test valid, missing, wrong-type, legacy, concurrent, and retry cases.
6. **Index experiment:** Load representative and skewed data, derive compound indexes, compare execution plans, and measure write/storage cost before and after.
7. **Evolution drill:** Execute an expand/migrate/contract change with checkpoints, mixed readers, reconciliation, rollback, and obsolete-index cleanup.
8. **Operational review:** Use allowed telemetry to identify a slow shape, form competing hypotheses, change one variable, verify the result, and document the ongoing alert/trigger.

## Readiness checks

1. Can I convert a vague performance request into a measurable workload requirement?
2. Can I identify missing ownership, lifecycle, consistency, and governance information?
3. Can I rank rare-critical and frequent-noncritical operations correctly?
4. Can I distinguish authoritative, copied, derived, historical, and transient data?
5. Can I identify persisted entities without creating a collection per object?
6. Can I choose appropriate BSON types and explain missing versus null?
7. Can I explain strong and weak entities with an ownership example?
8. Can I group entities into domains and identify cross-domain copies?
9. Can I map one-to-one, one-to-many, many-to-many, and hierarchy choices?
10. Can I spot cardinality skew hidden by averages?
11. Can I explain how lifecycle and deletion affect embedding/reference choices?
12. Can I govern duplicated fields and reconciliation?
13. Can I produce a complete read query shape rather than a field list?
14. Can I characterize write frequency, contention, amplification, and retries?
15. Can I trace an aggregation and explain how stage order affects work?
16. Can I decide whether to precompute from freshness and cost requirements?
17. Can I compare two candidate models against the same prioritized workload?
18. Can I explain when embedding improves locality and atomicity?
19. Can I explain when referencing prevents unsafe growth or coupling?
20. Can I use selective duplication rather than all-or-nothing denormalization?
21. Can I select and justify attribute, bucket, computed, subset, or outlier patterns?
22. Can I recognize unbounded arrays, bloated documents, excess collections, and lookup overuse?
23. Can I describe a polymorphic model and its discriminator/index implications?
24. Can I prove typical and worst-case document growth stays bounded?
25. Can I roll out validation without breaking legacy documents and applications?
26. Can I explain when single-document atomicity removes a transaction need?
27. Can I assess TTL, archive, time-series, and analytics requirements precisely?
28. Can I reason about shard-key targeting, distribution, and hotspot risk?
29. Can I derive a compound index from equality, sort, range, and projection?
30. Can I explain prefixes, multikey behavior, uniqueness, and covered queries?
31. Can I interpret keys/documents examined and scan/sort evidence?
32. Can I quantify index storage and write tradeoffs?
33. Can I identify when a model change is better than another index?
34. Can I use monitoring recommendations as evidence rather than commands?
35. Can I define observable triggers for model evolution?
36. Can I sequence an expand/migrate/contract rollout?
37. Can I make a backfill bounded, resumable, idempotent, and reconcilable?
38. Can I test mixed versions, partial failures, retry, and rollback?
39. Can I preserve retention, privacy, and audit behavior through migration?
40. Can I defend a design with measured evidence and state when it should change?

## Places to learn

This is not a complete list, and it is not a prescription to consume everything. Start with the official study guide and path, then choose the documentation, video, book, or practice format that closes your measured gaps. Durations are publisher-listed or clearly labeled estimates and can change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Associate Data Modeler exam](https://learn.mongodb.com/pages/mongodb-associate-data-modeler-exam) | Public | 10–15 min | Verify the current 75-question/110-minute contract and official resource links |
| [Official exam study guide](https://learn.mongodb.com/courses/associate-data-modeler-exam-study-guide) | Free enrollment/account | 30 min listed | Canonical objectives and recommended training; recheck after enrolling |
| [MongoDB Data Modeling Path](https://learn.mongodb.com/learning-paths/data-modeling-for-mongodb) | Free; account useful | 8 hr listed | Primary structured route with CRUD, relational-to-document, patterns, optimization, aggregation, indexing, and performance |
| [Official practice questions](https://learn.mongodb.com/courses/associate-data-modeler-practice-questions) | Free account | 1 hr listed plus review | Learn official format and turn every miss into an objective and lab task |
| [August 2026 certification-path update](https://www.mongodb.com/company/blog/news/introducing-a-more-connected-flexible-path-to-certifications) | Public | 5–10 min | Understand the new skill-badge/path alignment and current completion discount |
| [Designing Your Schema](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/) | Public | 1–2 hr selected reading | Canonical workload → relationship → pattern → index process and linked docs |
| [Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/) | Public | 3–6 hr selected reading/labs | Relationships, patterns, anti-patterns, validation, operational factors, and evolution |
| [Explain Results](https://www.mongodb.com/docs/manual/reference/explain-results/) | Public | 1–2 hr lab | Validate query/index/model reasoning with current execution evidence |
| [High Performance with MongoDB](https://www.oreilly.com/library/view/high-performance-with/9781837022632/) | Paid/O’Reilly | 10 hr 16 min listed; select chapters | 2025 MongoDB-authored depth on schema, indexes, workload, architecture, and measurement |
| [MongoDB Essentials](https://www.oreilly.com/library/view/mongodb-essentials/9781806706099/) | Paid/O’Reilly | 1 hr 36 min listed | Concise 2025 MongoDB-team overview including modeling and performance |
| [MongoDB Schema Design Best Practices](https://www.youtube.com/watch?v=QAqK-R9HUhc) | Free/YouTube | About 10 min | Official visual explanation of relationships and workload-led choices |
| [MongoDB — The Complete Developer’s Guide](https://www.udemy.com/course/mongodb-the-complete-developers-guide/) | Paid/Udemy | About 17.5 hr listed; select sections | Broad application practice; reconcile modeling/index behavior with current official docs |

## Final preparation

- Reopen the live exam page and enrolled study guide; confirm contract, objectives, delivery, price, accommodations, and policies.
- Complete the official path selectively and repeat practice only after investigating each explanation and weak objective.
- Rebuild one scenario from requirements through evolution without notes and defend the losing alternatives.
- Practice timed reading: extract constraints before choosing a pattern or index.
- Stop using any source that promises recalled live questions, guaranteed passes, or “actual” items.
- Treat passing as one checkpoint; production modeling still requires peer review, representative tests, security/governance review, and measured operations.
