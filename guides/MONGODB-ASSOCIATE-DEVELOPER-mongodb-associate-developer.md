---
exam_code: MONGODB-ASSOCIATE-DEVELOPER
vendor_id: mongodb
official_blueprint: https://learn.mongodb.com/courses/mongodb-associate-developer-exam-study-guide
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# MongoDB Associate Developer Study Guide

> **Independent AI-assisted resource — PUBLIC SOURCES REVIEWED; CURRENT OBJECTIVE BODY AND HUMAN REVIEW PENDING.** The September 29, 2026 review adds 40 answered prompts, 38 executed Python prediction checks and a JavaScript syntax-checked shell exercise. No MongoDB server, driver or Atlas lab was executed. See the [coverage record](../docs/SOURCE-VALIDATION.md#mongodb-associate-developer-coverage-record).

**CURRENT BLUEPRINT — retained evidence baseline:** Overview/Document Model 8%, CRUD 51%, Indexes 17%, Data Modeling 4%, Tools 2%, Drivers 18%. These six weights and 18 saved objective statements come from the September 2 evidence baseline. They were **not** confirmed unchanged on September 29. The canonical [study-guide landing page](https://learn.mongodb.com/courses/mongodb-associate-developer-exam-study-guide) lists a free 30-minute guide and enrollment. Its public linked viewer failed, and its document asset returned HTTP 403. No account was accessed or enrollment submitted; the historical snapshots remain intact.

**VERIFY CURRENT — exam contract:** The readable [exam page](https://learn.mongodb.com/pages/mongodb-associate-developer-exam) lists 53 multiple-choice questions, 75 minutes, English, online proctoring, no prerequisite and USD 150. Its five programming-language choices are C#, Java, Node.js, PHP and Python, sharing core database topics. The page does not state a passing percentage. Recheck the selected variant and the [program guide](https://learn.mongodb.com/courses/program-guide) before scheduling; the latter's public landing lists 15 minutes, but its policy body was not retrieved. Retakes, accommodations and other account-specific conditions are not established by a successful URL check.

**Experience target:** Use the earlier developer experience description as preparation advice: practice application CRUD, document modeling and the selected official driver. That description is not a newly verified prerequisite. The public exam page currently lists no formal prerequisite.

**VERIFY CURRENT — release and exam scope:** No dated replacement was identified in the accessible certification pages on September 29. That is a limited observation while the objective body remains unavailable. The current [manual](https://www.mongodb.com/docs/manual/) and [9.0 release notes](https://www.mongodb.com/docs/manual/release-notes/9.0/) mix a “current” navigation label, preview context and “Upcoming” patch headings. A documentation selector does not prove general availability, deployment compatibility or a changed exam version. Record the server, feature compatibility and driver versions used in every real lab.

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

Documents in one collection can have different fields and nested shapes. That flexibility enables iterative application design; it does not eliminate contracts. Producers, consumers, validators, indexes, aggregations, and migrations must still agree on required fields, types, defaults, and versions. In a standard collection, documents require `_id`; supported clients usually generate an `ObjectId` when one is omitted. Time-series collections and sharded uniqueness have additional rules, so do not generalize the standard-collection rule to every deployment.

Embedded documents and arrays preserve data that belongs and is read together. Dot notation reaches nested fields. Array equality, element matching, projection, and update semantics differ from scalar fields, so test them explicitly. A document has a size limit and arrays that grow without bound are unsafe design choices.

Single-document operations are atomic. That makes the document boundary an important consistency boundary: facts that must change together may benefit from embedding, while independently growing or governed entities may require references and sometimes transactions.

`Related item:` A flexible schema is not “schema-free.” JSON Schema validation, typed application models, compatibility tests, and observed production shapes can make flexibility governed rather than accidental.

### Make the type and document boundary observable

Use the [BSON reference](https://www.mongodb.com/docs/manual/reference/bson-types/) and [document rules](https://www.mongodb.com/docs/manual/core/document/) to distinguish an identifier from its text representation, an application date from the internal BSON timestamp, and decimal arithmetic from binary floating point. An ObjectId is only approximately time-ordered: one-second resolution and different client clocks prevent using it as an exact event-time clock. BSON Date represents milliseconds from the epoch; a formatted local time string does not preserve that contract by itself.

Standard documents have a 16 MiB size limit. Track encoded document size and growth, not just the number of array entries. An ever-growing audit history belongs in a separately bounded design even before it approaches that limit. Whole embedded-document equality is sensitive to field order; Python dictionary equality is not a BSON comparison oracle. The [embedded-query page](https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/) did not expose its interactive examples in this review, so the explicit field-order rule here is grounded in the document reference.

**PRACTICAL DEPTH:** The Python workbook below uses integer cents and `Decimal` to check arithmetic. It does not encode BSON, round-trip a Decimal128, validate an ObjectId, or measure a MongoDB document. Use the selected driver's codec tests to establish those properties.

## 2. CRUD — 51%

Use the [multi-insert reference](https://www.mongodb.com/docs/manual/reference/method/db.collection.insertmany/) and [array-update operator table](https://www.mongodb.com/docs/manual/reference/operator/update-array/) to check ordered errors and array mutation choices. CRUD is more than memorizing method names. Read each operation as filter → options → update/projection → returned result → final persisted state. `insertOne` and `insertMany` add documents and return acknowledgement/identifiers according to the driver. Understand duplicate `_id` failure, ordered versus unordered bulk behavior where supported, and why partial progress must be handled deliberately.

`find` returns a cursor while `findOne` returns at most one document. Build filters with equality, comparison, logical, element, existence, and array-aware operators. Dot notation can match fields across array elements; `$elemMatch` requires its conditions to hold for the same element. Exact embedded-document equality is stricter than matching an individual nested field. Projection controls returned fields, with special handling for `_id`; sort, skip, and limit alter result order/window and need a deterministic tie-breaker for stable pagination.

Distinguish replacement from operator updates. A replacement supplies the new document body while preserving the immutable `_id`; `$set` changes named paths. Operators such as `$inc`, `$unset`, `$push`, `$addToSet`, and array positional forms express different state transitions. Predict whether an update matches zero, one, or many documents and whether `matchedCount` can differ from `modifiedCount`.

An upsert inserts when no document matches. Design the filter and update together so the inserted document has the intended identity and required fields. A non-unique business filter can race; use a unique index where uniqueness is part of the invariant and handle duplicate-key outcomes safely.

Use `deleteOne` or `deleteMany` with an intentional filter and verify the deleted count. Protect destructive application paths with authorization, tenant scoping, validation, audit context, and tests for empty or malformed filters. Never practice against production data.

Atomic find-and-modify methods can select and change one document as one operation and optionally return the before or after image. This is useful for counters, claims, and state transitions, but correctness still depends on a filter that encodes the current allowed state. A read followed by an independent write creates a race window.

Aggregation pipelines transform documents through ordered stages. The current blueprint embeds MongoDB Query Language and aggregation behavior inside CRUD/driver objectives rather than publishing a separate weighted aggregation domain. Be able to trace `$match`, `$project`/`$set`, `$unwind`, `$group`, `$sort`, `$limit`, and `$lookup` at the level used in the official learning path, and know that stage order changes both results and efficiency.

`Related item:` Retryable network behavior does not make every business operation idempotent. Generate stable request or operation identifiers and design repeated writes so a retry cannot create a second order, payment, or side effect.

### Predict the result before choosing syntax

The [element-match reference](https://www.mongodb.com/docs/manual/reference/operator/query/elemmatch/), [null/missing guide](https://www.mongodb.com/docs/manual/tutorial/query-for-null-fields/), [projection reference](https://www.mongodb.com/docs/manual/reference/method/db.collection.findone/) and [update reference](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateone/) answer different questions. Keep selection, returned fields and mutation separate.

| Decision | Original counterexample and expected interpretation |
|---|---|
| Separate array predicates or one `$elemMatch`? | A contains red quantity 1 and blue quantity 4. B contains red quantity 4. Separate existential tests for red and quantity at least 4 admit A and B; requiring one element to satisfy both admits B. |
| Membership or exact array? | A scalar red condition can match an array containing red and blue. An exact one-element array condition asks for a different shape and value. |
| Missing, null or falsy scalar? | For scalar fixtures, null equality includes missing and null; `$exists: false` isolates missing; `$type: 10` identifies BSON null. Zero exists and is not null. Array and dotted-path semantics require separate version-specific tests. |
| Filter or projection? | Matching one qualifying array element does not automatically trim the returned array to that element. Choose an array projection deliberately. Ordinary inclusion/exclusion projections have the special `_id` exception. |
| Match, change or insert? | Setting an already equal value can yield one match and zero modifications. An inserting upsert has an inserted identifier with zero existing-document matches; zero modifications alone is not failure. |
| Upsert filter or inserted body? | An equality identity can contribute to an operator-style upsert. A range such as quantity greater than 10 does not invent an inserted quantity. Supply required insert values and enforce business-key uniqueness. |
| Stable order or stable dataset? | Sort by creation time plus a unique tie-breaker. Offset paging can repeat records after earlier inserts; keyset paging avoids that particular shift but is not a snapshot and can repeat a record whose sort key changes. |
| Order count or line count? | The fixture has three open north orders, including an empty order. Unwinding its nonempty item arrays produces three lines from two orders and 8,250 cents. Counting pipeline rows after unwinding answers a different question. |

The [atomicity guidance](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/) supports a guarded single-document transition. For stock of five and a validated request for four, include the tenant, item identity, allowed state and sufficient current quantity in the update filter, then decrement with `$inc`. A second request for four should not match after the first succeeds. Do not use an inventory reservation's insufficient-stock filter with `upsert: true`: a failed reservation should not create another inventory record.

An `updateMany` call does not make its entire batch atomic; each document change is atomic. A transaction can coordinate required changes across documents, but network ambiguity, repeatable transaction callbacks and external side effects still need an application contract. The local replay example deliberately keeps its receipt and stock in one Python state model; two independent MongoDB writes would not inherit that model's indivisibility.

## 3. Indexes — 17%

Indexes trade storage and write work for more efficient supported reads and sorts. Start from observed query shapes: equality predicates, sort, range, projection, selectivity, frequency, and latency target. A single-field index may fit one predicate; a compound index can support prefixes and carefully ordered equality/sort/range needs. Do not create one index per field without considering complete queries and write cost.

MongoDB creates the unique `_id` index. Understand single-field, compound, multikey, and unique behavior at the associate level. An index becomes multikey when it indexes an array; compound multikey designs have restrictions. Unique indexes enforce an invariant across indexed values, with missing/null and shard considerations that must be verified for the actual deployment.

Use `explain("executionStats")` or the relevant tool to compare a collection scan with an index scan. Inspect winning-plan stages, documents and keys examined, returned count, sort behavior, and execution time cautiously. One small warm run is not a benchmark. Generate representative volume/distribution, repeat, and consider cache and concurrency.

Covered queries can return required fields from an index without fetching full documents when the filter/projection and index support it. Extra indexes consume memory/storage and slow writes; duplicate, unused, or low-value indexes create operational cost. Drop only after workload evidence, dependency review, and a rollback plan.

`Related item:` Index choice and data model are coupled. A schema that forces many wide multikey indexes or cross-collection joins may need a document-boundary redesign rather than another index.

### Index candidates are hypotheses

For a tenant's open-order history, a candidate beginning with tenant and status, followed by creation time and the unique tie-breaker, supports an equality-plus-sort hypothesis. If a highly selective amount range dominates, compare a range-before-sort alternative against the sort-before-range choice. The [ESR guidance](https://www.mongodb.com/docs/manual/tutorial/equality-sort-range-guideline/) explicitly permits that tradeoff; the acronym is not an unconditional optimality proof. Its small/large `$in` threshold is also described as version-sensitive.

Before adding a [unique index](https://www.mongodb.com/docs/manual/core/index-unique/), inspect existing violations and define missing/null behavior. A regular unique single-field index treats missing and null as the same null key, allowing only one such indexed document; a partial unique index restricts enforcement to its filter. A unique multikey index constrains keys across documents and does not necessarily remove duplicates inside one array. For a request identity, include the tenant in the intended business key; sharded collections require additional shard-key design.

The [multikey reference](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-multikey/) limits compound indexes to at most one indexed array field per document. It also limits covering: returning the array itself or using `$elemMatch` prevents the documented multikey covering case. An index supporting a predicate is not necessarily a covered query. Save the actual plan, returned identities, keys/documents examined and repeated timings for representative data. No `explain` output or performance result is claimed by this guide's local workbook.

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

### Translate contracts, not just method names

The [official library directory](https://www.mongodb.com/docs/drivers/) distinguishes supported drivers from community libraries such as Mongoose. A framework can be useful, but its validation, hooks and return shapes are additional behavior.

| Contract | Shell / JavaScript-oriented spelling | PyMongo spelling to verify for the selected API |
|---|---|---|
| Update existing matches | `updateOne` / `updateMany` | `update_one` / `update_many` |
| Inspect update result | `matchedCount`, `modifiedCount`, `upsertedId` | `matched_count`, `modified_count`, `upserted_id` |
| Logical values | `true`, `false`, `null` | `True`, `False`, `None` |
| Query operators | `$set`, `$inc`, `$gte` in query/update documents | The same MongoDB operators as string keys inside Python mappings |
| Iterate results | Shell or selected JavaScript cursor API | Synchronous `for` or the documented asynchronous API; do not interchange their await rules |

Read [PyMongo updates](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/update/), [cursors](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/query/cursors/) and [connection pools](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/connection-pools/) together. `maxPoolSize` controls pool capacity, `maxConnecting` controls simultaneous connection establishment, and connection, socket and wait-queue timeouts bound different waits. Raising one number does not remove an overloaded-server or unbounded-work-queue problem. Close partially consumed cursors and avoid materializing an unbounded result set.

**VERIFY CURRENT:** [PyMongo release notes](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/reference/release-notes/) distinguish API and compatibility changes. The reviewed page includes 4.18.1/4.18 entries and records the asynchronous API becoming generally available in 4.13. This is release awareness, not a declaration that every course, exam variant or local environment uses those versions. No driver was installed or connected during this review.

**PRACTICAL DEPTH — typed input:** A query object is not automatically safe if a supposedly scalar client value can itself be an operator object. [OWASP's NoSQL guidance](https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html) supports validation and constrained query construction. Build fixed operators from typed, allowlisted values, and obtain tenant scope from the trusted application identity. A generic “reject dollar signs” check is not a replacement for a schema, authorization and contextual validation. The workbook rejects a nested operator object, Boolean quantity, negative quantity and client-supplied tenant; those tests do not prove authentication or a production access-control system.

## Integrated scenarios

### Scenario 1: Idempotent order intake

An order request has a tenant, stable request ID and validated payload. Define a uniqueness key on tenant plus request ID and retain enough intent to reject reuse of the same key for a different order. A duplicate-key result may be the replay of a prior accepted request, a conflicting payload, or another uniqueness violation: reconcile against the intended record instead of treating every duplicate as success. Keep payment or notification side effects outside a blindly retried callback. Produce a replay trace, changed-payload rejection and denied cross-tenant case. The Python fixture models these decisions sequentially; durable receipts and ambiguous network outcomes remain a real-system lab.

### Scenario 2: Inventory reservation under competing requests

Stock is five; A and B each ask for four. In four of the six possible read-before-write interleavings, a naive read/check/write model accepts both and leaves a stored balance of one. The balance alone looks plausible, but one plus eight accepted units violates the initial stock of five. An indivisible check-and-decrement admits one request in either serial order. In MongoDB, test the guarded filter and `$inc` on one document with real concurrent clients, record successful/missed matches and reconcile reservations. If stock and receipts are separate documents, design their atomicity or recovery together.

### Scenario 3: Array query and customer-history view

Start with the A/B split-element fixture, then add another tenant and an empty item array. Predict exactly which identities match, which fields return and which rows contribute to revenue. A query can be fast and still answer the wrong question. Next test tied creation times, an insertion before an offset and a change to an existing sort key. Compare index candidates only after results are correct; capture plans and write costs at representative scale. Explain whether the application promises a snapshot, a live continuation or eventual reconciliation across pages.

## Hands-on evidence labs

These eight activities are **proposed**, with our time estimates. Use an authorized disposable environment and synthetic data, record versions and costs, and remove only the resources you created after reviewing the evidence. No Atlas project, database service, credentials, permission changes or purchase was used in the review.

1. **BSON/shape matrix (45–75 min):** Round-trip ObjectId, date, Decimal128, null and missing values through the selected driver. Assert types as well as display strings. Measure encoded size; compare ordered embedded-document equality with path predicates.
2. **Query truth table (90–150 min):** Run the A–E fixture below. Expect A/B for separate array predicates, B for `$elemMatch`, and no other tenant. Add projection and scalar null/missing cases, then test arrays separately under the deployed server version.
3. **Write transitions (90–150 min):** Compare replacement with `$set`, a no-op match with a real modification, inserting upsert with an existing match, and ordered/unordered batch errors. Capture result objects and final state; test the guarded reservation with actual concurrent callers.
4. **Aggregation grain (60–90 min):** Reconcile three open north orders, two represented nonempty orders, three lines and 8,250 cents. Test preserving empty arrays and changing stage order. Keep order-level counts separate from line-level measures.
5. **Index experiment (90–150 min):** Compare equality/sort/range alternatives at representative scale. Save returned identities, plan, examined counts, repeated timings and write/storage costs. Add unique null/missing and compound-array rejection cases; do not infer coverage from an index name.
6. **Document boundary (75–120 min):** Model bounded order items and independently growing history. Measure encoded growth, ownership and update contention. Explain where a transaction or explicit reconciliation is needed and what would make you revise the design.
7. **Tool workflow (45–75 min):** In the currently available Atlas/Compass interface, inspect the same scoped fixture as the driver. Save the filter and projection, compare IDs/counts, and redact connection details. UI labels and tier availability require rechecking.
8. **Driver application (120–180 min):** Reuse the documented client/pool, bound relevant waits, close cursors, handle duplicate/timeout outcomes and reject malformed inputs. Test durable replay recovery and changed-payload collisions. Translate to the registered language instead of assuming Python return shapes apply everywhere.

### Executed local prediction workbook

**PRACTICAL DEPTH:** This original standard-library Python program passed **38 checks** on September 29. It evaluates ordinary Python quantifiers, sorting, integer/decimal arithmetic, all six constrained event schedules and a sequential replay model. It never interprets MongoDB Query Language, connects a driver, encodes BSON, queries an index or creates a server. Its supplied tenant labels are trusted fixtures, not authenticated identities. Scalar null tests do not cover array/dotted-path rules. Its indivisible transition is an explicit modeling assumption, not a measured database concurrency result.

```python
import json
from copy import deepcopy
from decimal import Decimal
from itertools import permutations

checks = []


def check(label, actual, expected):
    if actual != expected:
        raise AssertionError((label, actual, expected))
    checks.append(label)


def rejected(label, fn):
    try:
        fn()
    except ValueError:
        checks.append(label)
    else:
        raise AssertionError(label)


orders = [
    {"_id": "A", "tenant": "north", "created": 10, "status": "open",
     "items": [{"sku": "red", "qty": 1, "cents": 1250},
               {"sku": "blue", "qty": 4, "cents": 500}]},
    {"_id": "B", "tenant": "north", "created": 10, "status": "open",
     "items": [{"sku": "red", "qty": 4, "cents": 1250}]},
    {"_id": "C", "tenant": "north", "created": 11, "status": "cancelled",
     "items": [{"sku": "red", "qty": 2, "cents": 1250}]},
    {"_id": "D", "tenant": "south", "created": 12, "status": "open",
     "items": [{"sku": "red", "qty": 8, "cents": 1250}]},
    {"_id": "E", "tenant": "north", "created": 12, "status": "open", "items": []},
]
north = [d for d in orders if d["tenant"] == "north"]
ids = lambda rows: [d["_id"] for d in rows]
independent = [d for d in north
               if any(x["sku"] == "red" for x in d["items"])
               and any(x["qty"] >= 4 for x in d["items"])]
same_element = [d for d in north
                if any(x["sku"] == "red" and x["qty"] >= 4 for x in d["items"])]
check("separate existential predicates admit the split-element counterexample", ids(independent), ["A", "B"])
check("one element satisfying both predicates is more selective", ids(same_element), ["B"])
check("an empty array has no satisfying element", any(x["qty"] >= 4 for x in orders[-1]["items"]), False)
check("tenant restriction excludes another tenant's matching document", "D" in ids(same_element), False)
check("scalar membership differs from whole-array equality", "red" in ["red", "blue"], True)
check("whole-array equality rejects an extra value", ["red", "blue"] == ["red"], False)

scalars = [{"_id": "missing"}, {"_id": "null", "value": None}, {"_id": "zero", "value": 0}]
check("scalar null-or-missing fixture", ids([d for d in scalars if d.get("value") is None]), ["missing", "null"])
check("explicit scalar null fixture", ids([d for d in scalars if "value" in d and d["value"] is None]), ["null"])
check("existence is distinct from truthiness", ids([d for d in scalars if "value" in d]), ["null", "zero"])

key = lambda d: (d["created"], d["_id"])
ordered = sorted(north, key=key)
first = ordered[:2]
check("a total ordering resolves tied creation values", ids(first), ["A", "B"])
check("same snapshot next page", ids([d for d in ordered if key(d) > key(first[-1])][:2]), ["C", "E"])
inserted = {"_id": "0", "tenant": "north", "created": 9, "status": "open", "items": []}
changed = sorted(north + [inserted], key=key)
check("offset pagination repeats a row after an earlier insertion", ids(changed[2:4]), ["B", "C"])
check("keyset continuation skips the new earlier row", ids([d for d in changed if key(d) > key(first[-1])][:2]), ["C", "E"])
moved = deepcopy(north)
moved[0]["created"] = 13
check("changing the sort key can repeat a row even with keyset pagination", ids(sorted([d for d in moved if key(d) > key(first[-1])], key=key)), ["C", "E", "A"])
projected = [{"_id": d["_id"], "status": d["status"]} for d in first]
check("declared output projection contains no nested items", projected, [{"_id": "A", "status": "open"}, {"_id": "B", "status": "open"}])

open_orders = [d for d in north if d["status"] == "open"]
lines = [(d["_id"], x) for d in open_orders for x in d["items"]]
revenue = sum(x["qty"] * x["cents"] for _, x in lines)
check("three open orders include one empty array", len(open_orders), 3)
check("unwound line count is three", len(lines), 3)
check("orders represented by line rows exclude the empty order", len({oid for oid, _ in lines}), 2)
check("line arithmetic preserves integer cents", revenue, 8250)
check("display conversion uses exact decimal arithmetic", str(Decimal(revenue) / Decimal(100)), "82.5")
check("exact decimal input avoids a binary fraction artifact", Decimal("0.1") * Decimal("0.2"), Decimal("0.02"))
check("ordinary addition is not the erroneous documentation example", 0.1 + 0.1, 0.2)


def simulate_split(schedule):
    available, reads, accepted = 5, {}, []
    for action in schedule:
        actor = action[-1]
        if action[0] == "r":
            reads[actor] = available
        elif reads[actor] >= 4:
            available = reads[actor] - 4
            accepted.append(actor)
    return available, accepted


schedules = [s for s in permutations(("rA", "wA", "rB", "wB"))
             if s.index("rA") < s.index("wA") and s.index("rB") < s.index("wB")]
violations = [(s, simulate_split(s)) for s in schedules
              if simulate_split(s)[0] + 4 * len(simulate_split(s)[1]) != 5]
check("all interleavings respect each caller's read-before-write", len(schedules), 6)
check("four split read/write schedules violate inventory conservation", len(violations), 4)
check("over-allocation can occur while stored inventory stays positive", simulate_split(("rA", "rB", "wA", "wB")), (1, ["A", "B"]))
guarded = []
for sequence in permutations(("A", "B")):
    available, accepted = 5, []
    for actor in sequence:
        if available >= 4:
            available -= 4
            accepted.append(actor)
    guarded.append((available, len(accepted)))
check("indivisible guarded transitions preserve inventory in both orders", guarded, [(1, 1), (1, 1)])


def validated_request(value):
    if not isinstance(value, dict) or set(value) != {"sku", "quantity", "request_id"}:
        raise ValueError("unexpected fields")
    if not isinstance(value["sku"], str) or value["sku"] not in {"red", "blue"}:
        raise ValueError("unknown SKU")
    if type(value["quantity"]) is not int or not 1 <= value["quantity"] <= 5:
        raise ValueError("invalid quantity")
    if not isinstance(value["request_id"], str) or not value["request_id"] or len(value["request_id"]) > 40:
        raise ValueError("invalid request ID")
    return dict(value)


request = {"sku": "red", "quantity": 4, "request_id": "r1"}
check("typed allowlisted input accepted", validated_request(request), request)
rejected("operator object is not a SKU string", lambda: validated_request(dict(request, sku={"$ne": None})))
rejected("Boolean is not an integer quantity in this contract", lambda: validated_request(dict(request, quantity=True)))
rejected("negative quantity rejected", lambda: validated_request(dict(request, quantity=-1)))
rejected("client cannot inject a tenant field", lambda: validated_request(dict(request, tenant="south")))

state = {"available": 5, "receipts": {}}


def reserve(trusted_tenant, payload):
    value = validated_request(payload)
    if trusted_tenant != "north":
        raise ValueError("scope denied")
    identity = (trusted_tenant, value["request_id"])
    fingerprint = (value["sku"], value["quantity"])
    if identity in state["receipts"]:
        previous, result = state["receipts"][identity]
        if previous != fingerprint:
            raise ValueError("request ID reused with different intent")
        return result
    success = value["sku"] == "red" and state["available"] >= value["quantity"]
    if success:
        state["available"] -= value["quantity"]
    state["receipts"][identity] = (fingerprint, success)
    return success


check("first request reserves once", reserve("north", request), True)
check("replay returns recorded result", reserve("north", request), True)
check("replay does not reserve again", state["available"], 1)
rejected("same request ID with changed intent rejected", lambda: reserve("north", dict(request, quantity=1)))
rejected("supplied trusted scope is checked separately from query input", lambda: reserve("south", request))
check("new request cannot exceed remaining stock", reserve("north", dict(request, request_id="r2")), False)
check("failed reservation preserves stock", state["available"], 1)

print(json.dumps({"passed": len(checks), "checks": checks,
                  "split_schedules": len(schedules), "violating_schedules": len(violations),
                  "revenue_cents": revenue, "remaining_inventory": state["available"]}, indent=2))
```

The result reports six schedules, four violating schedules, 8,250 cents and one remaining unit. The same-element and pagination counterexamples make useful assertions for the real driver lab. The replay model records declines as well as successes; whether to retain or expire a declined intent is an application policy decision. The model is process-local, sequential and non-durable; it cannot establish crash recovery or coordination across separate MongoDB documents.

### Proposed shell translation — not executed against MongoDB

The following original `mongosh` exercise uses the same synthetic fixture. Its JavaScript syntax was checked with Node; Node does not validate MongoDB methods, server behavior or permissions. It writes only to the two named exercise collections after checking that both are empty. Use a dedicated authorized database, do not share these collections with other writers, and inspect both collections after a failure before deciding how to resume. No cleanup command is executed automatically.

```javascript
const lab = db.getSiblingDB("study_developer");
const orders = lab.getCollection("orders_0929");
const inventory = lab.getCollection("inventory_0929");
if (orders.countDocuments({}) !== 0 || inventory.countDocuments({}) !== 0) {
  throw new Error("Use empty, dedicated exercise collections");
}
orders.insertMany([
  {
    "_id": "A",
    "tenant": "north",
    "created": 10,
    "status": "open",
    "items": [
      {
        "sku": "red",
        "qty": 1,
        "cents": 1250
      },
      {
        "sku": "blue",
        "qty": 4,
        "cents": 500
      }
    ]
  },
  {
    "_id": "B",
    "tenant": "north",
    "created": 10,
    "status": "open",
    "items": [
      {
        "sku": "red",
        "qty": 4,
        "cents": 1250
      }
    ]
  },
  {
    "_id": "C",
    "tenant": "north",
    "created": 11,
    "status": "cancelled",
    "items": [
      {
        "sku": "red",
        "qty": 2,
        "cents": 1250
      }
    ]
  },
  {
    "_id": "D",
    "tenant": "south",
    "created": 12,
    "status": "open",
    "items": [
      {
        "sku": "red",
        "qty": 8,
        "cents": 1250
      }
    ]
  },
  {
    "_id": "E",
    "tenant": "north",
    "created": 12,
    "status": "open",
    "items": []
  }
]);
inventory.insertOne({_id: "red", tenant: "north", available: 5});
printjson(orders.find({tenant: "north", "items.sku": "red", "items.qty": {$gte: 4}}, {_id: 1}).sort({_id: 1}).toArray());
printjson(orders.find({tenant: "north", items: {$elemMatch: {sku: "red", qty: {$gte: 4}}}}, {_id: 1}).toArray());
printjson(orders.aggregate([
  {$match: {tenant: "north", status: "open"}},
  {$unwind: "$items"},
  {$group: {_id: null, cents: {$sum: {$multiply: ["$items.qty", "$items.cents"]}}, lines: {$sum: 1}}}
]).toArray());
for (let attempt = 0; attempt < 2; attempt++) {
  printjson(inventory.updateOne(
    {_id: "red", tenant: "north", available: {$gte: 4}},
    {$inc: {available: -4}}
  ));
}
printjson(inventory.findOne({_id: "red", tenant: "north"}));
```

Expected database observations, still awaiting a real run: the first query returns A/B; the second returns B; aggregation returns 8,250 cents and three lines; the two sequential updates return one match/change followed by zero matches/changes; inventory ends at one. This is a sequential smoke test, not a concurrent workload or an idempotency implementation. Add authenticated tenant tests, actual races, error injection and durable receipt reconciliation in the driver activity.

## Readiness checks

These are original explanation prompts, not recalled certification items.

1. **Which BSON types cannot be safely treated as ordinary JSON strings or numbers?** Preserve native ObjectId, date, decimal and binary/UUID representations, and the distinction among numeric BSON types. A visually similar string is not automatically the same value/type; prove the selected driver's round trip.

2. **Why can differently shaped documents coexist, and where should contracts still be enforced?** Collections allow varied document shapes, but applications, validators, indexes and consumers still need compatible contracts. Test missing, null, old-version and unexpected-field cases instead of assuming flexibility means every shape is valid.

3. **What role does `_id` play, and when is an `ObjectId` generated?** For standard collections, `_id` identifies the document and is immutable; clients usually supply an ObjectId when omitted. Time-series behavior and cluster-wide sharded uniqueness require separate verification. ObjectId order is not exact event time.

4. **Why are unbounded arrays unsafe?** Growth can exceed the document-size limit, increase reads/writes and complicate indexing. Bound the working set and move independently growing history to a design with an explicit lifecycle.

5. **How does a document boundary affect atomicity?** A single-document write is atomic, so colocating facts can simplify an invariant. Separate-document coordination may need a transaction or recovery protocol; `updateMany` alone is not an all-or-nothing batch.

6. **What does an insert result prove, and what does it not prove?** Inspect acknowledgment and inserted identifiers under the configured write concern. An identifier alone does not prove business authorization, duplicate-free external side effects or durability beyond that concern.

7. **How do ordered and unordered multi-insert failure behaviors differ?** An ordered operation stops after an error, leaving possible earlier progress. An unordered operation can continue other writes; neither is a transaction. Inspect the per-operation error/progress evidence before retrying.

8. **When should `findOne` be used instead of iterating `find`?** Use it when at most one returned document is needed, with a filter/sort that identifies the intended choice. If several documents qualify, an unspecified first result is not a business ordering contract.

9. **How do dot notation and `$elemMatch` differ for array predicates?** Separate path conditions can be satisfied by different elements; `$elemMatch` requires a single array element to satisfy its combined criteria. The fixture deliberately makes A a split-element false positive.

10. **Why can exact embedded-document equality surprise you?** Whole-document equality includes structure, values and field order. Path predicates express selected field requirements. Ordinary Python mapping equality does not reproduce BSON's ordered-document comparison.

11. **Which projection rule applies to `_id`?** Ordinary projections choose inclusion or exclusion, with a special exception for `_id`, which otherwise returns by default. Also distinguish document selection from trimming a matching array element.

12. **What makes sort plus pagination deterministic?** Use a unique tie-breaker with the intended sort key. That stabilizes ties for a dataset, not the dataset itself: writes can shift offsets, and changed sort keys can disturb keyset continuation.

13. **How does replacement differ from `$set`?** A replacement supplies the new body and can remove omitted fields, while `$set` changes specified paths. Existing `_id` cannot be changed to another identity; verify validators and required fields.

14. **When can matched count differ from modified count?** An acknowledged no-op can match a document whose values already equal the requested values. Inspect `upserted_id` as well: inserting an upsert is different from matching and modifying an existing document.

15. **How do `$push` and `$addToSet` differ?** `$push` appends, including duplicates; `$addToSet` avoids adding an equal value already present. It does not clean pre-existing duplicates or provide an application-level ordered set contract.

16. **Which positional array update form fits one, all, or filtered elements?** `$` targets the first matching element, `$[]` all array elements and `$[identifier]` elements selected by `arrayFilters`. Their query/upsert restrictions differ; test the exact chosen form.

17. **What does an upsert construct when the filter matches nothing?** For an operator update, equality identity fields and update expressions help form the inserted document. Range predicates do not manufacture field values. Set required insert values deliberately and inspect the returned inserted identity.

18. **How do a unique index and duplicate handling close an upsert race?** A unique business-key index prevents competing inserts from creating multiple documents with the same key. Reconcile a duplicate against the original intent; do not retry every duplicate as a new request or assume every duplicate proves success.

19. **Why is an empty delete filter dangerous at the application boundary?** An empty filter can select the entire collection for `deleteMany`. Construct narrow server-owned identity/tenant predicates, validate them and inspect deleted counts; returning fewer fields does not authorize deletion.

20. **How does atomic find-and-modify avoid a read/write race?** Selection and mutation occur together for the targeted document. Include the allowed current state or sufficient quantity in the filter; an identity-only overwrite can still lose another writer's intent.

21. **How does aggregation stage order change result and cost?** Each stage receives the prior stage's output. Unwinding changes grain, grouping collapses it, and filtering after grouping may ask a different question. Trace exact rows and counts before optimizing.

22. **When must a retry be made business-idempotent?** Whenever repeating an accepted request could repeat an order, reservation, payment or notification. Use a stable intent key and durable result/reconciliation design; driver retry support is not an external-side-effect guarantee.

23. **Which query-shape facts drive compound index order?** Equality fields, sort sequence/direction, range selectivity, projection, cardinality, workload frequency and write cost matter. Compare ESR with a selective ERS alternative using observed plans and result equality.

24. **What is a compound-index prefix?** It is the leading consecutive part of the index's key sequence. Skipping an earlier key changes what the index can efficiently filter/sort; equality constraints on preceding keys matter.

25. **When does an index become multikey?** MongoDB derives multikey behavior when an indexed field contains an array. Compound-array restrictions apply per indexed document, and multikey covering has additional restrictions.

26. **Which metrics in `executionStats` support or weaken an index decision?** Compare returned identities/counts with keys/documents examined, scan/sort/fetch stages and repeated timings. A zero-document-examination result without a useful returned result is not sufficient evidence of a good index.

27. **What is required for a covered query?** The index must supply the query's required fields under the applicable index/sharding rules, allowing no document fetch. Returning a multikey array or using `$elemMatch` prevents the documented multikey covering case.

28. **Which write, storage, and cache costs accompany another index?** Each index adds entries, storage, cache pressure and write maintenance. Measure the actual workload and index usage before removal or addition; a faster isolated read may worsen the overall service.

29. **When does embedding beat referencing?** When bounded related data is commonly read together and a shared atomic update/lifecycle fits. An order's bounded items are a candidate; duplicating an unbounded customer history into every order is not the same decision.

30. **Which growth or ownership facts argue for references?** Independent lifecycle, high/unbounded cardinality, reuse, separate permissions or heavy independent updates can favor references. Include the cost and consistency of assembling the referenced view.

31. **What must govern intentionally duplicated fields?** State the authoritative owner, copied values, acceptable staleness, update/delete propagation, repair mechanism and reconciliation evidence. Duplication without that contract becomes conflicting truth.

32. **How do you find a sample document in the current Atlas tools?** Select the authorized deployment, database and collection in the current tool; apply a saved tenant/identity filter and compare returned identities with the driver. The review did not execute the UI or verify a tier-specific layout.

33. **Why must generated queries be reviewed as code?** Generated operations can target the wrong scope, introduce operators, scan too much data or mutate records. Inspect filter, projection, pipeline and cost before executing; a fluent explanation does not establish correctness.

34. **What does an official driver do between native code and BSON/wire operations?** The driver manages wire operations, connections and conversion between language values and BSON. Framework hooks and models add another layer and should not be confused with the official driver API.

35. **Which parts of a MongoDB URI must you understand and protect?** Understand scheme/hosts or SRV, authentication database, database selection, credential escaping, TLS and options. Do not print or commit a live URI, and do not weaken verification to make a connection succeed.

36. **Why should an application reuse one client and connection pool?** A documented long-lived client reuses pooled connections and avoids per-request setup. Pool capacity, connection creation and wait limits are separate controls; select values from workload evidence.

37. **How do cursor iteration and materialization differ operationally?** Iteration consumes batches while materialization retains the entire result in application memory. Close an abandoned cursor and distinguish synchronous from asynchronous iteration; neither makes a mutable dataset a snapshot automatically.

38. **Which returned write-result fields should your code inspect?** For the operation, inspect acknowledgment, inserted IDs, matched/modified/deleted counts and upsert identity. Use the selected language's names and handle partial/ambiguous failures explicitly.

39. **How do typed allowlists reduce query/operator injection risk?** A scalar field must remain a permitted scalar, not a nested operator object. Constrain keys/types/ranges, construct fixed query operators and add trusted tenant scope separately. Validation and authentication remain different requirements.

40. **Which official pages and selected-language path will you recheck before scheduling?** Recheck the canonical study guide, public exam/program pages, registered-language learning path, relevant server manual and driver release/API documentation. The enrolled objective body, policy interior, live labs and independent human review remain outstanding here.

## Places to learn

This is not a complete list. Choose material for the registered language and identified gaps. Public catalog metadata does not establish lesson quality or current exam alignment. No paid lessons, practice-question interiors, enrollment, trial or purchase was accessed.

The [developer-path directory](https://learn.mongodb.com/pages/mongodb-developer-learning-paths) lists five 20-hour paths and advertises a 50% exam discount on completion; verify eligibility before budgeting. The Python path's visible required cards total 12h45 (765 minutes), with 3h30 of elective learning and a separate 75-minute exam card. Thus visible learning totals 16h15, or 17h30 with that exam card, while the page headline remains 20 hours. These are different published measures, not a calculated promise of completion time or an exam fee waiver.

Pluralsight currently lists seven courses and four labs: course cards total 8h24, labs 2h22, combined 10h46 against an 11-hour headline. Their dates span May 2025 through September 21, 2026. The path emphasizes querying and data analysis, so add the official selected-driver and application consistency work. Paid lesson interiors were not evaluated.

| Resource | Access | Estimated time |
|---|---|---|
| [Associate Developer exam page](https://learn.mongodb.com/pages/mongodb-associate-developer-exam) — current public contract and language choices | Public | Our reading estimate: 10–20 min |
| [Official exam study guide](https://learn.mongodb.com/courses/mongodb-associate-developer-exam-study-guide) — canonical scope; body unavailable in this review | Free enrollment advertised | 30 min listed; current objective body not reverified |
| [Certification program guide](https://learn.mongodb.com/courses/program-guide) — recheck policy before booking | Free enrollment advertised | 15 min listed; interior not reviewed |
| [Python Developer Path](https://learn.mongodb.com/learning-paths/mongodb-python-developer-path) — choose the corresponding registered-language path | Free enrollment | 20-hour headline; Python visible learning cards 16h15; exam card additional |
| [Official developer practice catalog](https://learn.mongodb.com/pages/mongodb-developer-practice-questions) — use explanations and gap analysis | Free enrollment | 1 hr listed for C#/Java/PHP/Python; Node.js card shows no duration in this capture |
| [Manual](https://www.mongodb.com/docs/manual/) and [official drivers](https://www.mongodb.com/docs/drivers/) — exact behavior and API/version contracts | Public | Our selected-reading estimate: 6–12 hr plus tests |
| [OWASP NoSQL Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html) — supplement with typed input and identity tests | Public | Our estimate: 45–90 min plus tests |
| [The Official MongoDB Guide](https://www.oreilly.com/library/view/the-official-mongodb/9781837021970/) — broader reference, subject to current catalog verification | Paid; HTTP 403 | Earlier 8h51 / 374-page / September 2025 metadata not reverified |
| [Query and Modify Data in MongoDB](https://www.pluralsight.com/paths/query-and-modify-data-in-mongodb) — selected data-query/analysis gaps | Paid | 11-hour headline; current seven-course/four-lab cards total 10h46 |
| [MongoDB — The Complete Developer's Guide](https://www.udemy.com/course/mongodb-the-complete-developers-guide/) — compare driver and framework coverage before purchase | Paid; HTTP 403 | Earlier ~17.5-hour / January 2026 metadata not reverified |

Reject guaranteed-pass offers, copied or recalled exam questions, and unexplained answer banks. Prefer original explanations, documented alternatives and reproducible application evidence.
