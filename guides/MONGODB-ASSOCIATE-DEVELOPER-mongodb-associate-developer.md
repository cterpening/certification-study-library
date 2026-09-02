---
exam_code: MONGODB-ASSOCIATE-DEVELOPER
vendor_id: mongodb
official_blueprint: https://learn.mongodb.com/courses/mongodb-associate-developer-exam-study-guide
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# MongoDB Associate Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The current exam landing page, free-enrollment official study guide, language-specific learning paths, practice resources, product documentation, learning links, and integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#mongodb-associate-developer-coverage-record).

**Current baseline:** MongoDB Overview and the Document Model 8%, CRUD 51%, Indexes 17%, Data Modeling 4%, Tools and Tooling 2%, and language-specific Drivers 18%. Choose the C#, Java, Node.js, PHP, or Python variant; the common database concepts remain shared and driver syntax changes.<br>
**Exam contract:** The current public exam page lists 53 multiple-choice questions, 75 minutes, online proctored delivery, English, no prerequisite, and USD 150. MongoDB does not publish a fixed passing percentage. Verify the selected language, accommodations, retake rules, system check, price, and policy before purchase.<br>
**Experience target:** MongoDB describes a developer who can complete day-to-day application operations using MongoDB. Software-engineering experience plus MongoDB training or equivalent hands-on use as an application database is recommended, not a formal prerequisite.<br>
**Upcoming change:** No retirement or dated replacement was found September 2, 2026. MongoDB does not expose an exam-version label on the public landing page, so recheck the official study guide and selected driver path before scheduling.<br>
**Access note:** The detailed official study guide is free but requires enrollment/email capture. The exam contract and learning paths are publicly readable. This guide records that boundary instead of treating a sign-in wall as a broken source.

## How to use this guide

Pick the same language you will select at registration, then build one small application twice: first with `mongosh` to prove MongoDB Query Language behavior, then with the chosen official driver to prove syntax, types, pooling, errors, and cursor handling. For every operation, predict the matched count, modified data, returned shape, index use, and failure before running it.

Use a free Atlas project or an authorized local disposable deployment and synthetic data. Set a budget, restrict network access, create a least-privilege database user, and remove resources when finished. The scenarios and checks are original. Do not use recalled live items, answer dumps, or “actual question” products.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, security, or operational context. It helps the objective make sense in a real application but does not claim that MongoDB uses that wording in the official study guide.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| MongoDB Overview and the Document Model | 8% | BSON/type and flexible-document behavior tests |
| CRUD | 51% | Predicted and observed query/write results, including arrays and concurrency-safe changes |
| Indexes | 17% | Query-shape-to-index decisions with `explain` evidence and write-cost tradeoffs |
| Data Modeling | 4% | Workload-based embed/reference and document-boundary decision |
| Tools and Tooling | 2% | Repeatable Atlas/Data Explorer or Compass inspection workflow |
| Drivers | 18% | One reusable client, correct URI/types/cursors, language-specific CRUD and aggregation tests |

## 1. MongoDB Overview and the Document Model — 8%

MongoDB stores BSON documents in collections inside databases. BSON extends JSON-like structures with types such as `ObjectId`, dates, binary data, `Decimal128`, and distinct numeric representations. Know what your selected driver returns for each type and avoid converting money, time, or identifiers through lossy strings or floating-point values.

Documents in one collection can have different fields and nested shapes. That flexibility enables iterative application design; it does not eliminate contracts. Producers, consumers, validators, indexes, aggregations, and migrations must still agree on required fields, types, defaults, and versions. Every document has a unique `_id`; if the client does not supply one, supported clients commonly generate an `ObjectId`.

Embedded documents and arrays preserve data that belongs and is read together. Dot notation reaches nested fields. Array equality, element matching, projection, and update semantics differ from scalar fields, so test them explicitly. A document has a size limit and arrays that grow without bound are unsafe design choices.

Single-document operations are atomic. That makes the document boundary an important consistency boundary: facts that must change together may benefit from embedding, while independently growing or governed entities may require references and sometimes transactions.

`Related item:` A flexible schema is not “schema-free.” JSON Schema validation, typed application models, compatibility tests, and observed production shapes can make flexibility governed rather than accidental.

## 2. CRUD — 51%

CRUD is more than memorizing method names. Read each operation as filter → options → update/projection → returned result → final persisted state. `insertOne` and `insertMany` add documents and return acknowledgement/identifiers according to the driver. Understand duplicate `_id` failure, ordered versus unordered bulk behavior where supported, and why partial progress must be handled deliberately.

`find` returns a cursor while `findOne` returns at most one document. Build filters with equality, comparison, logical, element, existence, and array-aware operators. Dot notation can match fields across array elements; `$elemMatch` requires its conditions to hold for the same element. Exact embedded-document equality is stricter than matching an individual nested field. Projection controls returned fields, with special handling for `_id`; sort, skip, and limit alter result order/window and need a deterministic tie-breaker for stable pagination.

Distinguish replacement from operator updates. A replacement supplies the new document body while preserving the immutable `_id`; `$set` changes named paths. Operators such as `$inc`, `$unset`, `$push`, `$addToSet`, and array positional forms express different state transitions. Predict whether an update matches zero, one, or many documents and whether `matchedCount` can differ from `modifiedCount`.

An upsert inserts when no document matches. Design the filter and update together so the inserted document has the intended identity and required fields. A non-unique business filter can race; use a unique index where uniqueness is part of the invariant and handle duplicate-key outcomes safely.

Use `deleteOne` or `deleteMany` with an intentional filter and verify the deleted count. Protect destructive application paths with authorization, tenant scoping, validation, audit context, and tests for empty or malformed filters. Never practice against production data.

Atomic find-and-modify methods can select and change one document as one operation and optionally return the before or after image. This is useful for counters, claims, and state transitions, but correctness still depends on a filter that encodes the current allowed state. A read followed by an independent write creates a race window.

Aggregation pipelines transform documents through ordered stages. The current blueprint embeds MongoDB Query Language and aggregation behavior inside CRUD/driver objectives rather than publishing a separate weighted aggregation domain. Be able to trace `$match`, `$project`/`$set`, `$unwind`, `$group`, `$sort`, `$limit`, and `$lookup` at the level used in the official learning path, and know that stage order changes both results and efficiency.

`Related item:` Retryable network behavior does not make every business operation idempotent. Generate stable request or operation identifiers and design repeated writes so a retry cannot create a second order, payment, or side effect.

## 3. Indexes — 17%

Indexes trade storage and write work for more efficient supported reads and sorts. Start from observed query shapes: equality predicates, sort, range, projection, selectivity, frequency, and latency target. A single-field index may fit one predicate; a compound index can support prefixes and carefully ordered equality/sort/range needs. Do not create one index per field without considering complete queries and write cost.

MongoDB creates the unique `_id` index. Understand single-field, compound, multikey, and unique behavior at the associate level. An index becomes multikey when it indexes an array; compound multikey designs have restrictions. Unique indexes enforce an invariant across indexed values, with missing/null and shard considerations that must be verified for the actual deployment.

Use `explain("executionStats")` or the relevant tool to compare a collection scan with an index scan. Inspect winning-plan stages, documents and keys examined, returned count, sort behavior, and execution time cautiously. One small warm run is not a benchmark. Generate representative volume/distribution, repeat, and consider cache and concurrency.

Covered queries can return required fields from an index without fetching full documents when the filter/projection and index support it. Extra indexes consume memory/storage and slow writes; duplicate, unused, or low-value indexes create operational cost. Drop only after workload evidence, dependency review, and a rollback plan.

`Related item:` Index choice and data model are coupled. A schema that forces many wide multikey indexes or cross-collection joins may need a document-boundary redesign rather than another index.

## 4. Data Modeling — 4%

Model for application access patterns, not a generic relational translation. Identify entities, ownership, cardinality, growth, read/write frequency, consistency boundary, lifecycle, security, and the highest-value operations. Store data accessed together together when the tradeoffs fit.

Embedding favors locality, one-read retrieval, and single-document atomic updates. Referencing favors independent lifecycle, reuse, high or unbounded cardinality, and smaller documents, but can require additional queries or `$lookup`. One-to-one, one-to-few, one-to-many, many-to-many, and rapidly growing relationships lead to different choices. Document the rejected alternative and the condition that would make you revisit the model.

`Related item:` Duplication can be intentional. Name the authoritative owner, copied fields, propagation mechanism, acceptable staleness, reconciliation, and delete/privacy behavior; otherwise denormalization becomes unmanaged inconsistency.

## 5. Tools and Tooling — 2%

Know how to locate an Atlas project/cluster, load the supported sample dataset, select database and collection, and inspect or filter a document in Data Explorer. Compass provides a desktop visual workflow, and `mongosh` provides a scriptable shell. Tool labels change faster than query semantics, so focus on the task and verify the current UI.

Keep tool access least-privileged and network-bounded. Save meaningful filters/pipelines in source control or application tests rather than relying on GUI history. Redact connection strings and sample outputs before sharing evidence.

`Related item:` Natural-language query helpers can accelerate exploration, but generated filters and pipelines are untrusted code. Review the target, predicates, cost, and destructive behavior before execution.

## 6. Language-specific Drivers — 18%

An official driver translates language-native calls and values to MongoDB wire operations and BSON. Choose the registered language and know its exact client, database, collection, CRUD, cursor, aggregation, and BSON-type syntax. Do not answer Python questions using remembered Node.js conventions or confuse an ODM such as Mongoose with the official driver contract.

A connection string identifies scheme, hosts or SRV record, credentials, authentication context, database, and options. Percent-encode reserved credential characters and keep secrets outside source. TLS, timeouts, retry behavior, read/write concerns, Stable API, and pool options are operational contracts—set them intentionally and verify supported defaults in the selected driver/version.

Create one long-lived client per application/process as recommended for the driver and reuse its managed connection pool. Opening a client for every request adds latency and connection pressure. Close the client during controlled shutdown. Bound server selection, connection, socket, and operation timeouts; surface errors without leaking secrets.

Driver methods mirror core operations but return language-specific result objects and cursors. Assert acknowledged/inserted/matched/modified/deleted counts and returned documents. Iterate or stream large cursors rather than always materializing them. Use native BSON types for identifiers, dates, and decimals; validate external input before constructing filters or updates.

`Related item:` Query/operator injection can occur when untrusted JSON becomes a filter or update. Construct operations from allowlisted fields and typed values, authorize tenant/record scope separately, and never accept arbitrary operators from a client.

## Integrated scenarios

### Scenario 1: Idempotent order intake

Design an order document and Python, Java, Node.js, PHP, or C# service that creates an order once for a request ID, appends bounded status history, and returns it by customer/date. Produce the embed/reference decision, unique and compound indexes, insert/upsert semantics, duplicate-race handling, stable sorting, pooled client, BSON types, denied cross-tenant test, and retry evidence.

### Scenario 2: Inventory reservation under concurrency

Multiple requests reserve limited stock. Encode sufficient-current-quantity and allowed-state conditions in an atomic update, use `$inc` and an appropriate returned-document option, distinguish matched from modified results, test concurrent attempts, and explain when a multi-document transaction would be justified rather than widening the document.

### Scenario 3: Slow customer-history view

A nested-array query becomes slow as data grows. Capture its filter/sort/projection and baseline `explain`, inspect model/cardinality, compare compound/multikey index and bounded-subset redesigns, verify exact results, measure representative runs, record write/storage cost, deploy safely, and monitor before removing any old index.

## Hands-on evidence labs

1. **BSON and shape matrix (45–75 min):** Insert varied synthetic shapes and BSON types; round-trip them through shell and selected driver with type assertions.
2. **Query behavior table (90–150 min):** Predict and test equality, comparison, logical, nested, array, `$elemMatch`, projection, sort, skip, and limit results.
3. **Write-state transitions (90–150 min):** Exercise insert, replacement, operator update, upsert, multi-update, atomic find-and-modify, delete, and returned count/state evidence.
4. **Aggregation trace (60–90 min):** Build and hand-trace a pipeline using filter, shape, unwind, group, sort, limit, and optional lookup stages.
5. **Index experiment (90–150 min):** Generate representative data; compare no index, single, compound, multikey, unique, and covered behavior with `explain` plus write-cost notes.
6. **Model decision (75–120 min):** Design one-to-few and unbounded relationships, quantify document growth, test embed/reference variants, and document evolution triggers.
7. **Atlas/tool workflow (45–75 min):** Secure a disposable project, load sample data, find the same document in Data Explorer/Compass and shell, and redact evidence.
8. **Driver application (120–180 min):** Reuse one client, configure timeouts, implement typed CRUD/aggregation, iterate a cursor, handle duplicate/timeout errors, and test unauthorized input.

## Readiness checks

1. Which BSON types cannot be safely treated as ordinary JSON strings or numbers?
2. Why can differently shaped documents coexist, and where should contracts still be enforced?
3. What role does `_id` play, and when is an `ObjectId` generated?
4. Why are unbounded arrays unsafe?
5. How does a document boundary affect atomicity?
6. What does an insert result prove, and what does it not prove?
7. How do ordered and unordered multi-insert failure behaviors differ?
8. When should `findOne` be used instead of iterating `find`?
9. How do dot notation and `$elemMatch` differ for array predicates?
10. Why can exact embedded-document equality surprise you?
11. Which projection rule applies to `_id`?
12. What makes sort plus pagination deterministic?
13. How does replacement differ from `$set`?
14. When can matched count differ from modified count?
15. How do `$push` and `$addToSet` differ?
16. Which positional array update form fits one, all, or filtered elements?
17. What does an upsert construct when the filter matches nothing?
18. How do a unique index and duplicate handling close an upsert race?
19. Why is an empty delete filter dangerous at the application boundary?
20. How does atomic find-and-modify avoid a read/write race?
21. How does aggregation stage order change result and cost?
22. When must a retry be made business-idempotent?
23. Which query-shape facts drive compound index order?
24. What is a compound-index prefix?
25. When does an index become multikey?
26. Which metrics in `executionStats` support or weaken an index decision?
27. What is required for a covered query?
28. Which write, storage, and cache costs accompany another index?
29. When does embedding beat referencing?
30. Which growth or ownership facts argue for references?
31. What must govern intentionally duplicated fields?
32. How do you find a sample document in the current Atlas tools?
33. Why must generated queries be reviewed as code?
34. What does an official driver do between native code and BSON/wire operations?
35. Which parts of a MongoDB URI must you understand and protect?
36. Why should an application reuse one client and connection pool?
37. How do cursor iteration and materialization differ operationally?
38. Which returned write-result fields should your code inspect?
39. How do typed allowlists reduce query/operator injection risk?
40. Which official pages and selected-language path will you recheck before scheduling?

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick resources that match your language, gaps, and learning style. Use the current official study guide as the scope authority and treat broad product courses as foundations, not proof of exam alignment.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Associate Developer exam page](https://learn.mongodb.com/pages/mongodb-associate-developer-exam) | Public | 10–20 min | Current contract, language choices, accommodations, registration, and official resource links |
| [Associate Developer Exam Study Guide](https://learn.mongodb.com/courses/mongodb-associate-developer-exam-study-guide) | Free enrollment | ~30 min | Authoritative domain weights/objectives and recommended preparation |
| [MongoDB Python Developer Path](https://learn.mongodb.com/learning-paths/mongodb-python-developer-path) or the equivalent C#/Java/Node.js/PHP path | Free | ~20 hr | Complete document, CRUD, index, aggregation, Atlas, and selected-driver route; completion currently advertises an exam discount |
| [Official developer practice questions](https://learn.mongodb.com/pages/mongodb-developer-practice-questions) | Free enrollment | ~1 hr per chosen language | Vendor-authored format/readiness sample with explanations; study concepts, not item recall |
| [MongoDB Manual](https://www.mongodb.com/docs/manual/) and [official driver documentation](https://www.mongodb.com/docs/drivers/) | Public | 6–12 hr selected | Exact current operator, index, aggregation, BSON, connection, cursor, and language API behavior |
| [The Official MongoDB Guide](https://www.oreilly.com/library/view/the-official-mongodb/9781837021970/) | O’Reilly subscription/book | 8 hr 51 min listed / 374 pages | September 2025 guide by MongoDB subject-matter experts; broader and deeper than this associate exam |
| [Query and Modify Data in MongoDB](https://www.pluralsight.com/paths/query-and-modify-data-in-mongodb) | Paid | ~11 hr listed | Current visual/query, CRUD, aggregation, and text-search practice; select gaps and supplement driver-specific work |
| [MongoDB — The Complete Developer’s Guide](https://www.udemy.com/course/mongodb-the-complete-developers-guide/) by Academind | Paid | ~17.5 hr | Broad CRUD, indexes, aggregation, modeling, and application practice; verify official-driver versus framework syntax |

Reject guaranteed-pass products, “real/actual questions,” VCE files, unexplained answer banks, and copied exam content. Quality practice explains why alternatives fail and points back to documentation and reproducible application evidence.
