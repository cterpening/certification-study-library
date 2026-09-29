---
exam_code: DEA-C02
vendor_id: snowflake
official_blueprint: https://learn.snowflake.com/en/certifications/snowpro-advanced-dataengineer-C02/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# SnowPro Advanced: Data Engineer (DEA-C02) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Reviewed September 29, 2026 against five public abilities and current primary documentation. The original local CDC workbook below passed 40 checks; eight Snowflake account labs remain proposed. See the [deep-review evidence](../docs/research/2026-09-29-dea-c02-deep-review.md) and [coverage record](../docs/SOURCE-VALIDATION.md#dea-c02-coverage-record).

**Current baseline:** DEA-C02 is the active SnowPro Advanced: Data Engineer exam. Snowflake publishes five abilities and recommends two or more years of hands-on data-engineering experience in a production environment.<br>
**Upcoming change:** No future exam update or retirement announcement was present on the checked official page September 29, 2026. Recent streaming product releases below are separate from the exam lifecycle.<br>
**Public scope boundary:** The detailed exam guide is requested through a Snowflake web form. This guide maps the five live public abilities to current product documentation and production evidence; it does not invent inaccessible weights or subobjectives. Reconcile it with the official guide you receive.<br>
**Credential contract:** The public catalog lists Advanced attempts at USD 375. Current SnowPro policy says certifications expire after two years, uses a 0–1000 scale with 750 passing, and documents renewal and retake rules. Confirm price, delivery, languages, policy and accommodations at registration.

The score is scaled, so 750 does not mean 75% correct. Current [program policy](https://learn.snowflake.com/en/pages/snowpro-policies/) requires qualifying renewal before expiry, allows full-exam renewal within six months of expiration, and specifies a seven-day wait after failure with four retakes within twelve months. An expired credential cannot use the continuing-education route. **VERIFY CURRENT:** Neither a training agenda nor a practice-product page establishes this exam's question count, duration or domain weights.

## How to use this guide

DEA-C02 is not “Core with more facts.” Practice choosing and operating a production pipeline under correctness, latency, throughput, security, recovery and cost constraints. Every claim should end in evidence: a contract, graph, query ID/profile, load/task history, lag metric, data-quality result, grant path, lineage record, cost attribution or recovery/replay demonstration.

For each design, state source semantics, expected volume/burst, event/order contract, latency target, schema/data-quality policy, backfill/replay approach, security boundary, failure modes, observable signals, owner and rollback. Implement the smallest authorized version using synthetic data; do not experiment on an employer's production account without change approval.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It supports the topic but is not a claim that Snowflake published the phrase verbatim in DEA-C02's public objective list.

## Public ability map

| Published ability | Production evidence to produce |
|---|---|
| Source data from data lakes, APIs and on-premises | Source-to-target contract, selected ingestion pattern, identity/network path, validation/reconciliation, retry/replay and quarantine evidence |
| Transform, replicate and share data across clouds | Deterministic transformation and state model, cross-account/region/cloud dependency map, governed consumer contract and failover/revocation proof |
| Design end-to-end near-real-time streams | Latency/freshness/error SLO, ordering/duplicate semantics, stream/pipe/task/dynamic-table graph, lag/backpressure/failure/recovery evidence |
| Design scalable compute for data-engineering workloads | Workload isolation, compute/serverless choice, concurrency/size/autoscaling/timeout policy, credit attribution and load-test evidence |
| Evaluate performance metrics | Query and pipeline measurements connected to bottleneck, change, controlled comparison, total-cost effect and rollback |

The public [five-page Data Engineer training datasheet](https://www.snowflake.com/wp-content/uploads/2022/03/standard_de_datasheet.pdf), code 25L03, supports the learning route with ingestion, transformation, orchestration, performance, delivery and observability topics. It specifies three days, a data-engineering background and Foundations-equivalent knowledge; MFA Essentials is recommended. This role-training outline is not the inaccessible detailed exam blueprint. Its older notebook/function names also need current-product verification.

---

## 1. Source data from data lakes, APIs and on-premises systems

### Begin with a source contract

Inventory the source owner, endpoint/storage/catalog, identity, network path, data classification, schema and change semantics. Record expected and peak volume, file/event size, cadence, latency, ordering, duplicate/update/delete behavior, time zones, retention, outage/backfill behavior and allowed extraction load. Define source and target reconciliation before selecting a tool.

For object storage, named external stages plus storage integrations separate Snowflake authorization from embedded credentials. File formats express parsing/compression/null/error behavior. Bulk `COPY INTO` is appropriate for bounded file batches; Snowpipe automates event-driven file ingestion. External tables expose external-file metadata, while Iceberg tables introduce external catalog/storage ownership choices. Choose based on copy versus external ownership, consistency, refresh, governance, performance and recovery—not “lake” as a generic label.

On-premises acquisition usually needs an approved extract/CDC or integration service, network/private-connectivity design, encryption and checkpoint. Do not make a production source directly internet-accessible merely to simplify loading. For APIs, define pagination/cursors, rate limits, authentication/rotation, incremental watermark, response schema/version, retry/backoff, idempotency and a durable raw landing boundary.

Snowflake Openflow, partner connectors, Kafka connectors, Snowpipe Streaming, driver-based loaders and custom applications represent different managed/control boundaries. Assess who operates capture, buffering, schema evolution, secrets, networking, offset/checkpoint and dead-letter/replay behavior. Use supported versions and confirm feature availability by cloud/region.

### Validate and reconcile

Land immutable or reproducibly versioned raw data where appropriate. Validate file/message schema, required keys/types/ranges and business invariants. Quarantine bad records with reason and source identity rather than silently dropping or poisoning the full batch. Record file/event counts, source watermark, accepted/rejected rows, target checksum/aggregate and load history.

Design retries at the unit of idempotency. Snowflake file-load metadata helps avoid repeating recognized file loads, but renamed files, transforms, API pages and business updates need explicit batch/event keys and `MERGE`/replace rules. Test late arrival, duplicate, partial batch, corrected source, outage and backfill. A pipeline is not recoverable until replay produces the intended state without double application.

The [bulk-load metadata rules](https://docs.snowflake.com/en/user-guide/data-load-considerations-load) describe a 64-day history boundary and default skipping of older files whose load status is uncertain. `FORCE` can replay already loaded files; `LOAD_UNCERTAIN_FILES` addresses a different uncertainty. Keep source/file identity, business-event identity and checkpoint identity separate. In a correction, preserve the bad record and issue a new attributable event rather than silently rewriting the meaning of an already consumed offset.

For standard Snowflake tables, [primary, unique and foreign keys are not enforced](https://docs.snowflake.com/en/sql-reference/constraints-overview), while current `NOT NULL` and `CHECK` constraints are enforced. Validate uniqueness and version conflicts in the pipeline. The local SQLite exercise uses enforced keys as part of its own model; it does not demonstrate standard Snowflake enforcement.

**Related item:** Schema evolution can reduce operational friction, but uncontrolled evolution can change contracts or leak fields. Separate tolerated additive changes, breaking changes and quarantined unknowns with ownership and notification.

---

## 2. Transform, replicate and share data across cloud platforms

### Build deterministic transformations

Separate raw/landing, validated/conformed and consumer-serving contracts. Select SQL for set-based transformations, Snowpark for supported language/dataframe workloads, and UDFs/procedures only when their return/action and runtime/security characteristics fit. Version code, dependencies and configuration; parameterize environments; use least-privilege execution roles.

Streams expose change records for a consumer and advance offsets transactionally when consumed in committed DML. Tasks schedule SQL/procedure graphs. Dynamic tables declaratively refresh a query result toward a target lag. They can coexist, but do not combine them without assigning one system of record for state/checkpoint and failure recovery.

The [pipeline overview](https://docs.snowflake.com/en/user-guide/data-pipelines-intro) introduces these choices, but their failure contracts require the detailed references. A [stream](https://docs.snowflake.com/en/user-guide/streams-intro) stores an offset; `SELECT` does not consume it. Committed consuming DML advances across the available changes, including rows excluded by its filter. Rollback leaves its offset in place. Give independent consumers their own offsets and retain enough source history to recover from staleness.

[Dynamic-table target lag](https://docs.snowflake.com/en/user-guide/dynamic-tables-target-lag) is a best-effort freshness goal relative to root sources, with a sixty-second minimum. It is not an exact timer or guaranteed maximum. `DOWNSTREAM` with no downstream refresh consumer does not automatically refresh. Keep an actual-lag signal and an explicit terminal scheduling decision.

Data modeling is workload-driven. Normalize where integrity/reuse matters; dimensional or wide serving models can simplify analytics. Incremental transformations need stable keys, delete handling, late-arrival policy and deterministic conflict rules. `VARIANT`, `FLATTEN`, window functions, aggregates, UDFs and stored procedures must be tested for nulls, type drift, duplicates and scale.

Before [MERGE](https://docs.snowflake.com/en/sql-reference/sql/merge), ensure at most one business-valid source choice per target key. The default nondeterministic-match error does not prevent every duplicate: unmatched duplicate source rows can each insert. Define a source version and equal-version conflict rule; do not use arrival order as an accidental business tie-breaker. A retained deletion tombstone can prevent an older update from resurrecting a record. Define whether a genuinely newer version may reactivate it.

For [task graphs](https://docs.snowflake.com/en/user-guide/tasks-graphs), keep the same owner/database/schema across graph tasks. Suspending a root stops future scheduled runs but does not cancel a running graph. Versioning snapshots task definitions when a root resumes or is executed; a called procedure changed during a run can still introduce new code. Manage procedure deployment as a separate dependency. A finalizer runs after the graph finishes or fails, but is not launched when the root run is skipped.

**VERIFY CURRENT:** Current graph documentation uses `OVERLAP_POLICY`: `NO_OVERLAP`, `ALLOW_CHILD_OVERLAP` and `ALLOW_ALL_OVERLAP`. These control overlap between runs; do not confuse them with independent siblings running within one DAG. Choose safe shared-state semantics before allowing overlap. Retry controls and suspension after repeated failures are distinct; `RETRY LAST` targets recovery from the failed task rather than proving every earlier side effect was rolled back. A graph is not one database transaction.

### Separate replication, sharing and movement

Same-region direct [Secure Data Sharing](https://docs.snowflake.com/en/user-guide/data-sharing-intro) exposes read-only provider data without creating a consumer storage copy; ordinary consumers use their compute. Provider-owned reader accounts change the cost/operation boundary. Listings add discovery/distribution/terms, while cross-region delivery requires separate supported arrangements. Replication and failover groups copy supported objects for continuity. Copy/unload/load creates separately managed data.

Choose the pattern by consumer ownership, freshness, transformation freedom, residency/egress, failure independence, recovery objectives and revocation. Map unsupported objects/integrations, external stages, network/DNS, encryption/key dependencies, identity and orchestration in failover. Test promotion, read/write direction, client routing, reconciliation and failback.

The [replication considerations](https://docs.snowflake.com/en/user-guide/account-replication-considerations) give concrete failure cases. Keep a stream, its source and its consuming destination in a coordinated replication/failover design; independently refreshed state can replay already applied changes. Replication collapses source history at refresh, so arbitrary earlier stream/Time Travel positions are not available after promotion. Replicating an external-stage object does not replicate the external files, and secondary storage trust and auto-ingest notifications require preparation.

For Named Channel recovery after failover, the promoted target may have an older committed offset than the former primary. Retain upstream records beyond the replication interval with a recovery margin; reopen against the promoted account and reconcile from its committed position. An ingestion acknowledgement on the old primary is not proof of replication to the standby. Record the last successful refresh, not just the configured schedule.

Govern collaboration with classification/tags, secure views, row access/masking/privacy policies as appropriate, consumer grants and access history. State what the consumer can infer through joins/aggregation. Revocation should be tested from the consumer session, not assumed because a provider changed a grant.

Use the [access-control model](https://docs.snowflake.com/en/user-guide/security-access-control-overview) to distinguish active role inheritance, ownership and grant authority. Primary-role authority governs object creation; secondary-role read access does not make a deployment identity an appropriate task owner. Verify least-privilege execution, source access and expected consumer denial separately.

**Related item:** Zero-copy clone is valuable for development, test and recovery workflows inside supported boundaries. It is not cross-cloud replication, a consumer share or an independent immutable backup.

---

## 3. Design end-to-end near-real-time streams

### Define time and correctness first

“Real time” needs a measurable definition: source event time, source capture time, Snowflake receipt/commit time, transformation completion and consumer visibility. Pick freshness/latency percentiles and maximum tolerable lag. Define event ordering, duplicates, updates/deletes, watermark, late-data window and exactly-once business outcome separately from transport delivery semantics.

For file arrivals, Snowpipe offers event-driven micro-batch ingestion. For low-latency row streams, Snowpipe Streaming avoids staging files and uses supported SDK/connector channel/offset behavior. Kafka/connectors or Openflow can manage source acquisition. Streams/tasks or dynamic tables can propagate changes into models. Select an end-to-end graph whose checkpoints and observability can be explained.

### Choose channel semantics explicitly

The current [streaming key-concepts entry point](https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-overview) separates channel type, pipe processing, schema, access and monitoring. **VERIFY CURRENT:** [Elastic Channels reached GA September 15, 2026](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-15-snowpipe-streaming-elastic-channels-ga). The documented GA SDK API requires version 1.8.0 or later; the [SDK notes](https://docs.snowflake.com/en/release-notes/clients-drivers/snowpipe-streaming-sdk-2026) date 1.8.0 to August 27. These are distinct SDK and feature-release dates, not evidence that an installed client has already been upgraded.

| Decision | Named Channels | Elastic Channels |
|---|---|---|
| Ordering | Preserved within one channel, not across channels | Not guaranteed |
| Delivery/recovery | Exactly-once ingestion requires client coordination with committed source offsets and replayable input | At least once; ambiguous failures/retries can duplicate accepted rows |
| Producer coordination | Deliberate channel identity and ordered source submission | Multiple producers use a server-managed implicit channel per pipe |
| Progress evidence | Latest committed source offset, with application-defined interpretation | Per-append durable acknowledgement; downstream processing/queryability follow |
| Token meaning | Source offset tracks restart position; REST continuation token tracks request sequence | Append token correlates callbacks; request IDs correlate retries, not deduplication |

[Named Channel offset tokens](https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-channels) are opaque strings stored by Snowflake. The client interprets them and avoids resending committed data; supplying a token does not make Snowflake automatically reject business duplicates. Keep replayable source records until commit, and reuse channel identity on restart. An inactive channel and its offsets can be removed after thirty days. The REST continuation token is a different sequencing mechanism. Client versions can also affect reopen behavior; do not mix classic and current SDK methods from old examples.

For [Elastic Channels](https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-elastic-channels-overview), a successful append Future/callback or REST acknowledgement means Snowflake durably buffered the append. It does not mean rows are already queryable or that every row will pass later processing. Append tokens stay in the SDK's memory and are neither persistent checkpoints nor deduplication keys. Preserve unacknowledged events durably if they must survive producer failure; a RAM buffer cannot do that. Use stable business identities, downstream reconciliation and enabled error logging for row-level processing errors. Longer retention may still be needed for disaster recovery and audit after acknowledgement.

[September 24 Iceberg GA](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-24-snowpipe-streaming-partitioned-iceberg-ga) adds partitioned Snowflake-managed Iceberg v2/v3 tables with both channel types. The announcement excludes externally managed Iceberg tables and Snowpipe Streaming Classic. Do not generalize a new feature across every catalog owner or ingestion architecture.

Separate the data plane from the control plane. The data plane carries files/rows and transformations. The control plane holds source offsets, channel/table metadata, task graphs, configuration, roles, secrets, alerts and deployment state. Losing or duplicating a control-plane checkpoint can change outcomes even if every row remains available.

### Engineer backpressure, failure and replay

Capacity is determined by the slowest sustained stage plus burst buffer. Measure source rate, ingest commit rate, transform throughput, warehouse queue/execution, task duration, dynamic-table refresh/lag and consumer freshness. Define what happens when the source outruns the system: buffer, throttle, scale, shed noncritical work or violate an explicit SLO—never silently lose data.

Quarantine poison messages/records with enough metadata to correct and replay. Set bounded retries and alert on exhausted retries, stalled offset, growing lag, failed task graphs, schema violations and reconciliation drift. Recovery should start from a known checkpoint and reapply idempotently. Test out-of-order and duplicate events, source reset, connector restart, warehouse suspension, downstream failure and a large backfill competing with live traffic.

Streams can become stale if their retention window is exceeded. Tasks can overlap or cascade according to graph/configuration. Dynamic-table refresh behavior depends on mode, target lag and supported query. Verify current service behavior rather than using a generic “streaming” assumption.

A deletion needs an explicit state policy as well as transport acknowledgement. In the local exercise, `(entity, business version)` determines current state, while `(partition, source offset)` determines consumed input. The model retains tombstones, rejects conflicting equal versions, records invalid events in quarantine and advances checkpoints atomically with state/receipts. Its contiguous integer offsets and one-partition-per-entity rule are fictional source contracts, not Snowflake requirements.

**Related item:** A freshness SLO without data-quality SLOs rewards fast wrong answers. Monitor completeness, validity, uniqueness, referential/business rules and reconciliation alongside latency.

---

## 4. Design scalable compute for data-engineering workloads

### Match compute to the workload

Standard virtual warehouses execute SQL and supported workloads; Snowpark-optimized warehouses serve memory-intensive Snowpark patterns. Serverless features provision compute under their own service contract. Consider work unit, CPU/memory/spill, concurrency, startup/cache sensitivity, latency, isolation, predictable schedule, serverless eligibility and credit attribution.

Scale up when individual work needs more resources; scale out with multi-cluster behavior when concurrency causes queueing. Auto-suspend bounds idle consumption; auto-resume aids availability. Resize, minimum/maximum clusters, scaling policy, statement timeouts and resource monitors have different effects. A larger warehouse cannot repair an explosive join, nonselective scan, skewed UDF or serial source/API bottleneck.

Separate ingestion, transformation, backfill, development and BI warehouses when ownership, interference, budget or service levels require it. Give each an owner, tags, role grants, auto-suspend, timeout/monitoring and escalation. Schedule heavy backfill away from latency-critical work or assign isolated capacity. Test concurrency and recovery, not just one warm query.

### Design for elastic but bounded operation

Partition work into restartable units, avoid unnecessary small tasks/files and control parallelism at source, loader and warehouse. Aggregate tiny files where supported/appropriate; avoid huge files that limit parallel load/retry. For Snowpark, understand pushdown, materialization, data movement and package/runtime behavior. For tasks/dynamic tables/serverless services, monitor service-specific history and consumption.

Estimate credits and storage/data-transfer/serverless effects under steady state, peak and backfill. Tag and query usage evidence. Create a stop condition for runaway input, queueing, spill, retry storm or budget threshold. Scalability means meeting SLO under forecast load with controlled failure/cost, not merely accepting more data.

[Resource monitors](https://docs.snowflake.com/en/user-guide/resource-monitors) cover supported warehouse consumption, not every serverless/streaming/storage cost, and suspension can overshoot a quota. Use service-specific consumption and ownership. [Warehouse load](https://docs.snowflake.com/en/user-guide/warehouses-load-monitoring) is time-weighted concurrency, not CPU percent; distinguish overload queueing, provisioning delay and transaction blocking before adding clusters or enlarging a warehouse.

**Related item:** Workload isolation can improve reliability even when it costs slightly more. Optimize against business service level and total cost of failure, not the lowest single-query credit figure.

---

## 5. Evaluate performance metrics and operate the pipeline

### Build a measurement hierarchy

Connect business outcome to consumer SLO, pipeline stage and platform metric. At the pipeline level track source watermark, received/accepted/rejected rows, throughput, end-to-end freshness, stage lag, retries, failure age, reconciliation, data quality and recovery time. At compute/query level track queue, compilation/execution, bytes/partitions scanned, pruning, rows, spill, joins, cache conditions, task/dynamic-table/pipe history and credits.

Use query IDs and tags to join application/pipeline runs to Query History/Profile/Insights and usage. Account Usage and Information Schema views have scope/latency/retention differences. Do not alert on a lagging administrative view as if it were instantaneous. Build run IDs/batch IDs into metadata and logs without exposing secrets or sensitive payloads.

The [September 24 streaming monitoring release](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-24-snowpipe-streaming-monitoring) adds event-table evidence for row counts, server-side processing time, row/channel errors and channel activity. Collection requires the relevant `LOG_EVENT_LEVEL=INFO` setting on the target-table schema, unless inherited, and the querying role needs event-table/view access. A default event table's existence alone does not prove collection is enabled. No logging setting or alert was configured in this review.

Track source event time, durable acknowledgement, target visibility and consumer-model freshness separately. Fast acknowledgements with growing processing errors or stale consumer models fail the end-to-end requirement. Keep rejected/quarantined counts and replay age visible alongside throughput; source-offset advancement by itself is not proof of valid analytical output.

### Diagnose before optimizing

Classify latency: source extraction; network/buffer; ingest; queue; compile; scan/pruning; join/aggregation/window; spill; external function/API; task dependency; consumer. Establish a representative baseline, including cache and concurrency conditions. Change one controlled factor and compare latency distribution, correctness and credits.

Clustering, search optimization, materialized views, query acceleration and warehouse changes solve different patterns with different maintenance/cost. Query rewrite/modeling, pruning and file/batch sizing often matter first. Profile production-shaped data; small lab results can hide skew, selectivity and concurrency.

### Operate as software

Deploy through version control, review, automated tests and environment promotion. Test schema/data contracts, transformations, idempotency/replay, grants/policies, performance thresholds and rollback. Monitor lineage and ownership. Run game days for source outage, bad schema, late data, connector/task failure, regional dependency failure and credential rotation.

An incident runbook should name detection, severity/SLO, stop/contain action, checkpoint, rollback/replay, data correction, consumer communication and evidence preservation. Never delete raw/quarantine/history evidence to make a dashboard green.

**Related item:** FinOps and DataOps join here: cost, delivery reliability, quality, security and developer change flow are one production system, not independent checklists.

---

## Executed local CDC workbook

**PRACTICAL DEPTH:** This original Python 3.13.14 standard-library exercise executed **40 checks** using real in-memory SQLite transactions. Source position and business version are separate. It verifies replay, same-offset conflicts, deletions/tombstones, late updates, equal-version conflicts, quarantine, independent partitions, gap rejection and a fault injected after a state write but before its receipt. A later conflict also rolls back an earlier valid update in the same packet. The final state has ten receipts, two quarantined records, checkpoints `p0=9` and `p1=1`, and two active entities totaling 250 fictional cents.

This is a single-connection application contract, not Snowflake, a streaming SDK, a durable service or a concurrency test. The source is a controlled fixture with contiguous positive integer offsets and one trusted partition per entity; actual Snowflake tokens are opaque strings. Receipts/tombstones never expire during the process. SQLite enforces its keys, unlike standard Snowflake primary keys. All data stays in memory, so terminating the process loses it; transactional rollback is not a demonstrated crash-recovery guarantee. Quarantine and checkpoints are atomic here because they share one SQLite transaction, not because an external pipeline or task graph is automatically atomic. No external effects, network, credentials or account are involved. The validator only implements this small fictional contract.

```python
"""Original offline CDC contract exercise. Not a Snowflake/SDK emulator."""
import json
import sqlite3

checks = 0
db = sqlite3.connect(":memory:", isolation_level=None)
owners = {"A": "p0", "B": "p1"}  # Trusted fixture routing, not authentication.


def check(actual, expected):
    global checks
    if actual != expected:
        raise AssertionError((actual, expected))
    checks += 1


def snapshot():
    return tuple(db.execute(sql).fetchall() for sql in (
        "SELECT * FROM state ORDER BY id",
        "SELECT * FROM receipts ORDER BY partition_id, source_offset",
        "SELECT * FROM checkpoint ORDER BY partition_id",
        "SELECT * FROM quarantine ORDER BY partition_id, source_offset",
    ))


def valid_event(event, partition):
    if not isinstance(event, dict) or set(event) != {"id", "version", "deleted", "cents"}:
        return False
    if not isinstance(event["id"], str) or owners.get(event["id"]) != partition:
        return False
    if type(event["version"]) is not int or event["version"] <= 0:
        return False
    if type(event["deleted"]) is not bool:
        return False
    return (event["cents"] is None if event["deleted"] else
            type(event["cents"]) is int and 0 <= event["cents"] <= 1000000)


def ingest(partition, packet, fail_after_state=False):
    if partition not in {"p0", "p1"}:
        raise ValueError("Unknown partition")
    outcomes = []
    db.execute("BEGIN IMMEDIATE")
    try:
        committed = db.execute(
            "SELECT source_offset FROM checkpoint WHERE partition_id=?", (partition,)
        ).fetchone()[0]
        for offset, event in packet:
            if type(offset) is not int or offset <= 0:
                raise ValueError("Invalid offset")
            encoded = json.dumps(event, sort_keys=True, separators=(",", ":"), allow_nan=False)
            old = db.execute(
                "SELECT payload FROM receipts WHERE partition_id=? AND source_offset=?",
                (partition, offset),
            ).fetchone()
            if old is not None:
                if old[0] != encoded:
                    raise ValueError("Offset payload conflict")
                outcomes.append("replay")
                continue
            if offset != committed + 1:
                raise ValueError("Offset gap")
            if not valid_event(event, partition):
                db.execute("INSERT INTO quarantine VALUES (?, ?, ?, ?)",
                           (partition, offset, encoded, "fixture contract violation"))
                outcome = "quarantined"
            else:
                new = (event["version"], int(event["deleted"]), event["cents"])
                current = db.execute("SELECT version, deleted, cents FROM state WHERE id=?",
                                     (event["id"],)).fetchone()
                if current is not None and new[0] < current[0]:
                    outcome = "stale"
                elif current is not None and new[0] == current[0]:
                    if new != current:
                        raise ValueError("Business version conflict")
                    outcome = "same-version"
                else:
                    db.execute("""INSERT INTO state VALUES (?, ?, ?, ?)
                        ON CONFLICT(id) DO UPDATE SET version=excluded.version,
                        deleted=excluded.deleted, cents=excluded.cents""", (event["id"], *new))
                    if fail_after_state:
                        raise RuntimeError("Injected failure before receipt")
                    outcome = "applied"
            db.execute("INSERT INTO receipts VALUES (?, ?, ?, ?)",
                       (partition, offset, encoded, outcome))
            committed = offset
            db.execute("UPDATE checkpoint SET source_offset=? WHERE partition_id=?",
                       (committed, partition))
            outcomes.append(outcome)
        db.execute("COMMIT")
        return outcomes
    except Exception:
        db.execute("ROLLBACK")
        raise


def event(version, cents, entity="A", deleted=False):
    return dict(id=entity, version=version, deleted=deleted, cents=cents)


def rejected(call, exception, message):
    before = snapshot()
    try:
        call()
    except exception as error:
        check(str(error), message)
    else:
        raise AssertionError("Expected rejection")
    check(snapshot(), before)


try:
    db.executescript("""
        CREATE TABLE state (id TEXT PRIMARY KEY, version INTEGER, deleted INTEGER, cents INTEGER);
        CREATE TABLE receipts (partition_id TEXT, source_offset INTEGER, payload TEXT, outcome TEXT,
                               PRIMARY KEY(partition_id, source_offset));
        CREATE TABLE checkpoint (partition_id TEXT PRIMARY KEY, source_offset INTEGER);
        CREATE TABLE quarantine (partition_id TEXT, source_offset INTEGER, payload TEXT, reason TEXT,
                                 PRIMARY KEY(partition_id, source_offset));
        INSERT INTO checkpoint VALUES ('p0',0), ('p1',0);
    """)
    check(ingest("p0", [(1, event(1, 100))]), ["applied"])
    check(snapshot()[0], [("A", 1, 0, 100)])
    before = snapshot()
    check(ingest("p0", [(1, event(1, 100))]), ["replay"])
    check(snapshot(), before)
    rejected(lambda: ingest("p0", [(1, event(1, 101))]), ValueError, "Offset payload conflict")
    check(ingest("p0", [(2, event(2, None, deleted=True))]), ["applied"])
    check(ingest("p0", [(3, event(1, 100))]), ["stale"])
    check(snapshot()[0], [("A", 2, 1, None)])  # Old update cannot resurrect deletion.
    check(ingest("p0", [(4, {"id": "A", "cents": 150})]), ["quarantined"])
    check(len(snapshot()[3]), 1)
    check(snapshot()[2], [("p0", 4), ("p1", 0)])
    rejected(lambda: ingest("p0", [(5, event(3, 150))], True),
             RuntimeError, "Injected failure before receipt")
    check(ingest("p0", [(5, event(3, 150))]), ["applied"])
    check(snapshot()[0], [("A", 3, 0, 150)])  # Newer reactivation is allowed by this contract.
    check(ingest("p0", [(6, event(3, 150))]), ["same-version"])
    rejected(lambda: ingest("p0", [(7, event(3, 999))]), ValueError, "Business version conflict")
    # A later conflict rolls back an earlier successful update in the same packet.
    rejected(lambda: ingest("p0", [(7, event(4, 200)), (8, event(4, 201))]),
             ValueError, "Business version conflict")
    check(ingest("p0", [(7, event(4, 200)), (8, event(True, 200))]),
          ["applied", "quarantined"])
    check(snapshot()[0], [("A", 4, 0, 200)])
    check(len(snapshot()[3]), 2)
    check(ingest("p1", [(1, event(1, 40, "B"))]), ["applied"])
    check(snapshot()[2], [("p0", 8), ("p1", 1)])
    rejected(lambda: ingest("p1", [(3, event(2, 50, "B"))]), ValueError, "Offset gap")
    rejected(lambda: ingest("p1", [(True, event(2, 50, "B"))]), ValueError, "Invalid offset")
    rejected(lambda: ingest("unknown", []), ValueError, "Unknown partition")
    # Repair is a new source event; preserve the old quarantined record and receipt.
    check(ingest("p0", [(9, event(5, 210))]), ["applied"])
    check(snapshot()[0], [("A", 5, 0, 210), ("B", 1, 0, 40)])
    check(snapshot()[2], [("p0", 9), ("p1", 1)])
    check(len(snapshot()[1]), 10)
    check(len(snapshot()[3]), 2)
    check(db.execute("SELECT SUM(cents) FROM state WHERE deleted=0").fetchone(), (250,))
    before = snapshot()
    check(ingest("p0", [(8, event(True, 200)), (9, event(5, 210))]), ["replay", "replay"])
    check(snapshot(), before)
    print(json.dumps({"receipts": 10, "quarantined": 2, "active_cents": 250,
                      "checkpoints": dict(snapshot()[2])}, sort_keys=True))
    print(f"{checks} local checks passed")
finally:
    db.close()
```

Expected output: ten receipts, two quarantined events, active total 250 cents, the stated partition checkpoints, and `40 local checks passed`. Preserve the failed source event when issuing a correction; do not rewrite an already consumed offset.

## Integrated scenarios

### Scenario 1: Lake and API customer pipeline

Ingest hourly Parquet from a cloud lake and incremental CRM API pages. Define storage/API identities, schemas, watermarks and batch keys; land and reconcile both; transform them deterministically; publish an approved consumer table/share; test API retry, late file, schema addition and replay.

### Scenario 2: Near-real-time event service

Bring synthetic order events through a supported streaming path. Define event/ingest/visible timestamps, duplicates/order/deletes, 95th/99th freshness, bad-record quarantine and backpressure. Propagate changes through a stream/task or dynamic-table design, observe lag/history and recover from a stopped consumer without double applying orders.

### Scenario 3: Cross-region regulated platform

Design separate ingestion/live/backfill compute, governed serving objects, a cross-account share and replication/failover. Map external storage, integrations, identities/network, RPO/RTO and unsupported dependencies. Load test peak plus backfill, test consumer denial/revocation and walk through promotion/failback/reconciliation.

## Hands-on evidence labs

**Proposed, not executed in a Snowflake account.** Use authorized disposable resources, synthetic data, unique names and a small approved budget. Record actual SDK/account settings rather than changing production identity/network policies to make an exercise pass. Retain evidence before removing only the lab's resources.

1. **Source contract and landing:** Define a five-record file and two-partition synthetic API/event source with a duplicate, deletion, late update and malformed record. Specify cursor, version, retention, ownership and extraction limits. Preserve raw input and build a reconciliation table showing every record's disposition. Paper-design unavailable acquisition paths; do not call a production source.
2. **Batch and business identity:** Stage and validate a small file, load accepted/rejected rows and inspect history. Retry identical and renamed input, then a corrected business version. Demonstrate that source-key checks and a tie policy precede MERGE. Compare expected counts/totals and remove staged files/tables. Do not force-load uncertain historical data without reconciliation.
3. **Incremental state and orchestration:** In disposable objects, compare plain stream SELECT, rolled-back consumption and committed filtered consumption. Record offsets/results and prove what a second consumer would see. Configure a small task graph or document a dynamic-table alternative; demonstrate a failed child/retry and explain root suspension, finalizer and overlap behavior. Restore suspended state and remove the graph safely.
4. **Streaming acknowledgement and recovery:** Select an already available supported client and explicitly choose Named or Elastic. Keep replayable synthetic input. For Named, record committed source progress and restart position; for Elastic, correlate durable acknowledgements and later query/error results, then reconcile a duplicate after an ambiguous outcome. If account/client work is unavailable, use the local workbook plus a paper sequence without claiming SDK execution.
5. **Compute and backfill:** Isolate a bounded synthetic backfill from a small live workload. Measure queue cause, execution, spill and warehouse/service consumption. Change one justified control under a stop condition and compare live freshness plus total cost. Avoid an expensive artificial load solely to force queueing; restore configuration and suspend lab compute.
6. **Observability:** Connect source, append/batch, query and consumer identities. Inspect event-table collection/read permissions before expecting streaming telemetry. Capture received/committed/visible counts, processing errors and oldest pending age. Diagnose one controlled fault without erasing the quarantine, then document the corrective signal. An alert design is a paper artifact unless explicitly configured in an authorized lab.
7. **Sharing and disaster recovery:** Draw a same-region provider/consumer access test and separate replication design. Include stream/source/destination state, stage files/trust, pipe notifications and client routing. In an authorized environment, test read/denial/revocation and a supported recovery; otherwise tabletop an old-primary offset of 200 and promoted offset of 100, explaining retained-input reconciliation. Never promote an actual production secondary for this exercise.
8. **Release and recovery evidence pack:** Capture the relevant client version/channel semantics, schema contract, code/procedure versions, grants, known checkpoint, raw/quarantine evidence and rollback/replay procedure. Walk through a newer schema, lost producer memory, inactive-channel offset loss and failed refresh. State what is simulated, what was measured and who must perform any deferred account step.

## Readiness checks

Original study prompts with explanatory answers; these are not exam items.

1. **Can you define a source contract before choosing ingestion technology?**

   Specify ownership, identity, schema, volume/burst, event ordering/deletes, extraction limits, source retention, reconciliation and replay. These requirements determine the ingestion path.

2. **How do stage, storage integration and file format responsibilities differ?**

   A stage identifies files/location, a storage integration governs storage trust, and a file format controls parsing. Permission to query a table does not establish cloud-storage trust.

3. **When do bulk COPY and Snowpipe fit?**

   Bulk COPY fits a controlled file batch; Snowpipe automates file arrivals. Both require parse/error policy, file history and business-level reconciliation.

4. **When does Snowpipe Streaming fit instead?**

   For supported low-latency row ingestion. Choose Named versus Elastic semantics and the actual SDK/API version before assuming ordering or recovery guarantees.

5. **How do external and Iceberg table ownership/catalog choices differ from copied tables?**

   External/Iceberg designs retain distinct storage/catalog ownership and refresh contracts. Copied data has its own Snowflake lifecycle; current partitioned streaming support is specifically for Snowflake-managed Iceberg.

6. **What API pagination, watermark, rate-limit and idempotency state must persist?**

   Persist replayable raw input, source cursor/offset, requested window, identities and committed progress. A process-memory cursor disappears on failure; response arrival is not a committed business checkpoint.

7. **How would you secure an on-premises acquisition path?**

   Use an approved extraction/CDC identity, bounded source load and documented private/network/TLS path. Test reconnection and secret rotation without exposing the source broadly.

8. **What makes a batch load reconciled and replayable?**

   Counts and business totals account for accepted, duplicate, stale and rejected records. Stable identities and version rules make replay reproducible beyond short-lived file-load metadata.

9. **Can you quarantine and later replay a bad record safely?**

   Retain original input, source identity and reason with a durable receipt. Correct through a new attributable event or governed replay policy; preserve the original error evidence.

10. **How do SQL, Snowpark, UDF and procedure roles differ?**

   SQL provides set operations, Snowpark supported language execution, UDFs values/tables and procedures actions. Choose runtime, movement, grants and transaction boundaries explicitly.

11. **How do streams, tasks and dynamic tables differ?**

   Streams expose changes relative to offsets, tasks orchestrate work, and dynamic tables maintain query results toward freshness goals. None automatically makes an entire pipeline atomic.

12. **What keys and delete/late-arrival rules make an incremental model deterministic?**

   Use stable entity identity, authoritative business versions, an equal-version conflict policy and retained tombstones. State whether a newer event can reactivate a deleted entity.

13. **How do sharing, physical movement and replication differ?**

   Same-region direct sharing exposes read-only data without a consumer storage copy; physical movement creates separate data; replication copies supported state for continuity with refresh/dependency limits.

14. **Who supplies compute for a shared query?**

   Ordinary consumers use their own warehouse. Provider-owned reader accounts change who operates/pays; cross-region distribution has a separate cost and availability contract.

15. **What external dependencies can undermine failover?**

   Storage files/trust, integrations/notifications, client routing, identity, procedures, stream/source/destination alignment and upstream retention. Object replication does not configure every dependency.

16. **How do event, ingest, transform and consumer-visible time differ?**

   Event time is source business time; ingestion can include buffering and commit; transformation completes a derived model; consumer visibility is when the required result is available. Measure each interval.

17. **Can you define latency/freshness as percentiles and a maximum?**

   Choose a meaningful population/window, percentile and maximum/oldest-pending bound, with a freshness clock that matches consumer needs. Averages can hide stuck partitions.

18. **What are the ordering and duplicate semantics?**

   Named Channels order within one channel and require source-offset recovery coordination. Elastic is unordered and at least once. Business version conflict/deduplication is a separate model contract.

19. **Where is the durable checkpoint/offset?**

   Identify the system that durably stores committed progress and the replayable input it refers to. Named-channel offsets can expire with inactivity; the local workbook has process-lifetime state only.

20. **What happens under backpressure?**

   Compare sustained stage rates and burst storage. Pause or buffer within an explicit capacity/retention limit, alert on lag and protect critical work; retrying faster can make overload worse.

21. **How is a poison record preserved and replayed?**

   Quarantine with raw input, identity, reason and an observable outcome. In the workbook, quarantine and the offset receipt commit together; the bad event is not silently discarded.

22. **What can cause a stream to become stale?**

   Consumption lag beyond retained change history and destructive source replacement can invalidate an offset. Inspect staleness and plan source replay rather than assuming a permanent message queue.

23. **How will live traffic coexist with a large backfill?**

   Isolate or throttle backfill, retain original identities and use the same conflict policy. Measure live freshness and total cost while competing work runs.

24. **When should compute scale up versus out?**

   Scale up for an individual workload resource constraint; scale out for concurrent overload. Provisioning waits, locks and incorrect joins need different remedies.

25. **When is a Snowpark-optimized warehouse justified?**

   When measured Snowpark memory/resource needs and supported workload characteristics justify it. The label alone is not evidence that ordinary SQL will run faster or cheaper.

26. **How do managed warehouses and serverless consumption differ operationally?**

   With warehouses you size/schedule the compute; serverless services use service-specific behavior and billing. Monitor each consumption source; a warehouse resource monitor does not cover everything.

27. **Why isolate ingestion, transformation, backfill and BI?**

   To control interference, grants, ownership, failure and attribution. Validate the service-level benefit and cost rather than creating a warehouse for every small step.

28. **What stop conditions bound a runaway pipeline?**

   Set meaningful bounds on source extraction, backlog, retry count, task runtime, concurrent work, cost and error rates, with an owner and a safe stop/recovery procedure.

29. **Which pipeline SLOs connect to which metrics?**

   Consumer freshness connects to stage timestamps and oldest pending work; completeness to counts/reconciliation; recovery to retained checkpoints/input; efficiency to measured latency and consumption.

30. **How do freshness and data quality work together?**

   Fast invalid data fails the service. Evaluate completeness, duplicates, stale/corrected events, validity and business totals alongside latency.

31. **Which views/history have data latency or scope boundaries?**

   Account Usage and Information Schema/history have their own scope, retention and freshness. Streaming event collection also needs LOG_EVENT_LEVEL and read access; table existence is not collection proof.

32. **Can you classify a slowdown by source/network/ingest/queue/query/dependency/consumer layer?**

   Find the first delayed or failed stage using correlated identities/timestamps. Separate source/network/buffer, ingestion, queue, query processing and consumer lag before changing compute.

33. **How do pruning, spill, joins, queue and caches appear in evidence?**

   Compare partitions scanned, row multiplication, local/remote spill, queue causes and result/warehouse cache state. Validate output before treating a faster query as an improvement.

34. **When do clustering, search optimization, materialized views and query acceleration differ?**

   Clustering, search optimization, materialized views and query acceleration have different eligible access patterns and maintenance/consumption costs. Choose from measured workload evidence.

35. **How do query tags/run IDs enable attribution?**

   They connect a source/batch/run to queries and consumption. Keep values stable and sanitized; tagging alone does not prove a business result or expose every serverless charge.

36. **What tests belong before promotion?**

   Contract/schema tests, duplicates/late/deletes, grain, grants/denials, replay/rollback, dependency compatibility and bounded performance/cost. Include changed procedure code outside task-definition versioning.

37. **Can you execute rollback and idempotent replay?**

   Prove what committed and what did not. Reapply retained input from a reconciled checkpoint; graph retries do not undo earlier external effects or completed steps.

38. **What evidence belongs in a data incident runbook?**

   Detection/SLO impact, source and run IDs, last valid checkpoint, raw/quarantine records, grants, stop/recovery steps, reconciliation and owner. Preserve evidence even when repairing the dashboard.

39. **Can you map all five live abilities to your own production evidence?**

   Map sourcing, transformation/replication/sharing, near-real-time design, scalable compute and metrics to your own contracts and observed failures/recoveries. Local reasoning checks are partial evidence.

40. **Have you reconciled this guide with the detailed official guide you received?**

   This review mapped only the five live abilities. The detailed guide remains behind a request form; compare the official document you obtain without inventing weights or inaccessible topics.

41. **What does an Elastic append acknowledgement prove?**

   It proves durable buffering, not immediate queryability or successful row processing. Preserve outcome/error evidence and use stable business identities for downstream reconciliation.

42. **Do append tokens or request IDs prevent duplicate ingestion?**

   No. SDK append tokens correlate callbacks and REST request IDs correlate attempts. Neither is a deduplication key; named-channel source offsets are a different recovery mechanism.

43. **How does a tombstone stop a late update from resurrecting a record?**

   A deletion retains its business version. The workbook rejects or ignores older versions, so a delayed update cannot resurrect it; a strictly newer reactivation is allowed by its stated contract.

44. **What happens when the second event in a packet conflicts?**

   A conflicting source-offset payload or equal business version rolls back the whole packet. State, receipts, quarantine and checkpoints remain unchanged, including an earlier successful update.

45. **Does suspending a root task freeze every dependency?**

   A root suspension stops future scheduling while current work continues. Graph definitions are versioned, but a changed called procedure may affect an in-flight run; coordinate that deployment separately.

46. **Does a finalizer prove every scheduled root actually ran?**

   No. A skipped root does not start the finalizer. Alert on skipped/missed runs separately from finalizer success and do not use cleanup as proof of processing.

47. **Why retain source records after the primary has committed them?**

   The last successful replicated state can lag the old primary. Retain source data beyond the refresh interval with margin and recover from the promoted account's committed position.

48. **Which Iceberg targets does the September 24 release support?**

   Current release: partitioned Snowflake-managed Iceberg v2/v3, Named or Elastic. Externally managed Iceberg and Streaming Classic are excluded; verify the actual target and client.

### Check key

- **Ready:** You can design, implement, measure, fail and recover it with production-shaped evidence.
- **Review:** You know the feature but cannot defend semantics, ownership, failure or cost.
- **Gap:** You guessed or memorized an item. Return to current documentation and an authorized lab.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Public metadata was checked September 29, 2026; no paid lessons, recordings or practice questions were accessed. Provider estimates are separated from this guide's optional study budgets. **VERIFY CURRENT:** Confirm exam alignment, expiry, client versions and booking availability before purchasing or enrolling.

| Resource | Access | Estimated time |
|---|---|---|
| [DEA-C02 certification and detailed-guide request](https://learn.snowflake.com/en/certifications/snowpro-advanced-dataengineer-C02/) | Public landing page, guide form. Five public abilities and two-year production-experience recommendation; no form submitted or weights recovered. | 20–40m reading budget; not exam duration. |
| [SnowPro policies](https://learn.snowflake.com/en/pages/snowpro-policies/) | Public validity, renewal, scoring, retake and appointment terms. | 30–60m reading budget. |
| [Official Practice Exams](https://learn.snowflake.com/en/certifications/snowpro-practice-exams/) | Paid portal; Data Engineer practice listed in English. Complete within 24h of purchase; one attempt. Missing that window forfeits the fee and requires waiting until 48h from purchase to re-register. Practice language is not proof of real-exam language availability. | Provider access/completion window: 24h. Optional 3–5h review budget; no questions accessed. |
| [Data Engineer Training](https://learn.snowflake.com/en/courses/ILT-DE) and [25L03 datasheet](https://www.snowflake.com/wp-content/uploads/2022/03/standard_de_datasheet.pdf) | Paid instructor-led role course. Actual five-page outline read, including Foundations-equivalent knowledge, data-engineering background and recommended MFA Essentials. No regional session availability or lab completion verified. | Provider: three days / 24h. Optional 15–30h follow-up practice. |
| [Hands-On Essentials](https://learn.snowflake.com/en/pages/hands-on-essentials-track/) | Six public workshop entries: warehousing, collaboration/cost, applications, lake, engineering and data science. Courses are free; the page says many badges are free, not every badge. Account and graded DORA work required for completion. | No verified aggregate provider duration; 20–40h selective study is a planning budget. |
| [Data-pipeline documentation](https://docs.snowflake.com/en/user-guide/data-pipelines-intro) | Public primary entry point, supplemented by the specific channel/task/replication references above. Current product contracts take precedence over dated course examples. | Optional 10–20h selective reading plus 20–35h authorized practice. |
| [Pluralsight: Snowflake for Data Engineers](https://www.pluralsight.com/paths/snowflake-for-data-engineers) | Paid/trial Data library; seven public course cards dated July–September 2025. Path still marked in production, with SQL/Snowflake prerequisites. Role training, not an explicit complete DEA-C02 exam map. | Header: 8h. Cards: 75+64+56+94+68+75+63 = 495m (8h15m); optional 20–30h practice. |
| [O'Reilly DEA-C02 bootcamp](https://www.oreilly.com/live-events/-/0642572194970/) | Paid live two-session catalog by Dr. Yasir Khan. Full public agenda/prerequisites read; no upcoming booking date verified or trial created. The unrelated Databricks skill footer is not this course's exam identity. | Timed topics total 240m each day, 480m (8h), excluding un-timed breaks/Q&A; provider says times may vary. |
| [Snowflake Data Engineering — Manning](https://www.manning.com/books/snowflake-data-engineering) | Publisher catalog: Maja Ferle, November 2024, ISBN9781633436855, 368 pages; basic SQL/cloud audience. Public description covers ingestion, transformation, orchestration, Snowpark and CI. No full book or paid chapters reviewed. | No publisher reading time verified; optional 15–25h reading and 20–35h practice budget. |
| [Snowflake Data Engineering — O'Reilly listing](https://www.oreilly.com/library/view/snowflake-data-engineering/9781633436855/) | Paid/trial; current HTTP403. Earlier December 2024 platform metadata remains unverified; publisher separately confirms November 2024 publication. | Earlier 11h05m reading estimate unverified; not video/runtime proof. |
| [Advanced Snowflake — O'Reilly](https://www.oreilly.com/library/view/advanced-snowflake/9781098170202/) | Paid/trial or book; current HTTP403. Earlier October 2025 revision and claimed feature coverage could not be reverified. No quality or current completeness endorsement. | Earlier 4h55m estimate unverified; confirm current catalog. |

Choose resources for identified evidence gaps. Reject products promising recalled live questions, dumps or guaranteed passing; a practice result does not establish a production recovery contract.
