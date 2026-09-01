---
exam_code: DATABRICKS-ASSOCIATE-DEVELOPER-APACHE-SPARK
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/apache-spark-developer-associate
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# Databricks Certified Associate Developer for Apache Spark Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-associate-developer-for-apache-spark-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/apache-spark-developer-associate) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-ASSOCIATE-DEVELOPER-APACHE-SPARK`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official guide for the live version as of October 30, 2025; live seven-domain weighted page checked September 1, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026. The current exam is not the retired “Apache Spark 3.0 — Python/Scala” exam. Recheck the official page two weeks before testing and reject material that still teaches the former 60-question, 120-minute, documentation-aided, language-specific format.<br>
**Lifecycle status:** Active; valid for two years, with the currently live exam required for recertification. Databricks staff confirmed that the [previous Apache Spark 3.0 credential retired in 2025](https://community.databricks.com/t5/certifications/databricks-certified-associate-developer-for-apache-spark-3-0/m-p/118717/highlight/true); this guide targets the replacement certification, not a renewal or conversion claim.<br>
**Assessment:** 45 scored multiple-choice questions, 90 minutes, English, online or test-center delivery, no test aids—including API documentation—according to the detailed guide.<br>
**Prerequisite:** None required. The official guide highly recommends related training and six months of hands-on Apache Spark experience. Basic Python, SQL, schemas/files, distributed-data concepts, and command-line/application troubleshooting are practical prerequisites.

## How to use this guide

Write and diagnose code without relying on API documentation during recall practice. For every operation, predict schema, partitioning, shuffle, laziness/action boundary, null/duplicate behavior, output mode, state, and likely Spark UI/log evidence before running it. Then execute the code on small edge-case fixtures and a larger skewed dataset.

```text
source + explicit schema -> logical DataFrame/SQL transformations
-> analyzed/optimized physical plan -> jobs -> stages at shuffle boundaries
-> tasks per partition on executors -> action/output
-> Spark UI + driver/executor logs + metrics -> correctness/performance decision
```

The DataFrame/Dataset API is 30%, and architecture plus Spark SQL add 40%. Learn API syntax and the distributed execution it creates together; memorized methods without partition, shuffle, schema, and failure reasoning are fragile.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes an objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Databricks' published exam objectives.

## Objective map

| Published domain | Weight | Evidence you should be able to produce |
|---|---:|---|
| Apache Spark Architecture and Components | 20% | Driver/executor/cluster/resources, session and structured APIs, job-stage-task hierarchy, lazy transformations/actions, partitions/shuffles, caching/GC, fault tolerance, and modules. |
| Using Spark SQL | 20% | Schema-aware reads/writes, file/JDBC sources, direct file SQL, modes/partitioned output, tables and temporary views. |
| Developing Apache Spark DataFrame/Dataset API Applications | 30% | Column/row/schema transforms, nulls/dedup/validation, aggregates/dates, joins/unions, I/O, collection, UDF/state, shared variables and broadcast joins. |
| Troubleshooting and Tuning Apache Spark DataFrame API Applications | 10% | Repartition/coalesce/skew/shuffle choices, AQE, Spark UI and driver/executor log diagnosis. |
| Structured Streaming | 10% | Incremental/micro-batch model, fault tolerance, sources/sinks/output modes, windows/aggregates and watermark-aware deduplication. |
| Using Spark Connect to deploy applications | 5% | Spark Connect client/server boundary and local/client/cluster deployment-mode distinctions. |
| Using Pandas API on Apache Spark | 5% | When pandas-like distributed APIs help and how vectorized Pandas UDFs differ from ordinary Python UDFs. |

---

## 1. Apache Spark Architecture and Components (20%)

### Understand where application code and work execute

The driver owns the SparkSession/SparkContext, constructs logical work, requests resources, schedules jobs/stages/tasks, and collects metadata/results. Executors run tasks on partitions, cache data, perform shuffle reads/writes, and return results/status. Worker nodes host executor processes under a cluster manager. CPU cores determine concurrent task slots; executor and overhead memory bound deserialization, execution, caching, shuffle, Python workers, and native/off-heap needs.

Spark helps process data larger than one machine through partitioned parallel work, fault recovery, a unified structured API, and an optimizer. Challenges include serialization/network/shuffle cost, skew/stragglers, many small files/tasks, memory pressure, distributed debugging, startup overhead, and algorithms that do not parallelize well. Distribution is not a speed guarantee for small data.

Deployment mode describes where the driver runs relative to the submitter/cluster. In **client** mode, the driver is in the submitting client process; losing that process can lose the application. In **cluster** mode, the cluster manager launches the driver inside the cluster. In **local** mode, driver and execution threads run in one process/machine for development/testing—there are not distributed executors on a separate cluster.

### Follow the execution hierarchy and laziness

A Spark application contains jobs. An action such as `count`, `collect`, a write, or many display operations triggers a job for the lineage required. A shuffle boundary commonly separates stages. Each stage has tasks, generally one per input/shuffle partition for that stage. Multiple actions can recompute shared lineage unless cached/persisted and materialized.

Transformations return a new logical DataFrame and are lazy; they do not normally scan all data immediately. Narrow transformations can compute each output partition from a small number of input partitions. Wide operations—grouping, distinct, ordering, many joins, repartition—redistribute records and create shuffle boundaries. The optimizer may rewrite or eliminate operations, so use `explain` and the Spark UI rather than assuming one method equals one physical stage.

Fault tolerance comes primarily from immutable lineage/recomputation and persisted/checkpointed state where applicable. A failed task can retry; executor loss can invalidate cached/shuffle data. Driver failure is a different boundary and needs cluster/application restart/recovery configuration. “Spark is fault tolerant” does not mean external side effects or non-idempotent writes are automatically safe.

### Reason about partitions, caching, storage, and memory

Partitions are the units of distributed data and task scheduling. Too few underuse cores and create large tasks; too many add scheduling/shuffle/file overhead. Input layout, source splitability, explicit repartitioning, shuffle configuration, AQE, and output partitioning all affect counts.

`cache()` is a convenience for a default persistence level; `persist(level)` selects memory/disk/serialization behavior. Caching is lazy until an action and benefits reused expensive lineage. It consumes executor storage memory, can evict other blocks, and can make a one-use pipeline slower. `unpersist()` when reuse ends. Garbage collection reclaims JVM objects, but repeated high GC time often signals oversized heaps/objects, excessive allocation, poor serialization, cache pressure, or too few/large partitions—not simply “add more memory.”

DataFrames represent distributed tabular data with named columns and schema. On the JVM a DataFrame is a `Dataset[Row]`; typed Datasets are a Scala/Java construct, while PySpark uses DataFrames. Structured APIs enable Catalyst analysis/optimization and efficient execution; RDDs expose lower-level objects/functions with less relational optimization.

Know the major modules: Core and scheduling; Spark SQL/DataFrames; Structured Streaming; Pandas API on Spark; MLlib; and current related libraries. The exam is Python/DataFrame focused, not an invitation to study every MLlib algorithm.

> **Related item:** A SparkSession is the structured entry point; SparkContext is the lower-level connection to execution. Creating uncontrolled multiple contexts is not normal application isolation.

---

## 2. Using Spark SQL (20%)

### Read with known schemas and explicit source options

Use `spark.read.format(...).options(...).schema(...).load(...)` or format conveniences. An explicit schema avoids inference cost and ambiguity, stabilizes downstream contracts, and defines types/nullability intent. Still validate corrupt/unexpected records, column presence, date/timestamp parsing, delimiters/headers/quotes, and source evolution.

File sources include Parquet, ORC, JSON, CSV, text and Delta when its connector/runtime is available. Columnar Parquet/ORC/Delta support column pruning and predicate pushdown better than row-oriented text formats. JSON/CSV are flexible interchange formats but require parsing and disciplined schemas. Text yields text records rather than magically parsing business fields.

JDBC reads need URL/table or query, driver/authentication, and optionally partition column/bounds/count or predicates for parallelism. Too many partitions can overwhelm the database; one unpartitioned read can bottleneck. Push filters/projections where supported and protect credentials. JDBC writes also require controlled partitions/batches/isolation and idempotent business behavior.

Spark SQL can query supported file paths directly using the provider syntax, but persistent tables/views provide reusable names, metadata and governance. Do not confuse file-level query ability with an automatically governed/optimized table lifecycle.

### Write with deliberate mode, layout, and table semantics

Common DataFrame/SQL save modes are append, overwrite, error/error-if-exists, and ignore. Understand the entire destination behavior before using overwrite; partition overwrite semantics and transactional capabilities depend on source/table/provider/configuration. Append can duplicate data when a job retries without an idempotent key/process.

`partitionBy` creates directory/table partition layout by column on write; it is not the same as `repartition`, which changes in-memory execution partitions. Select low-to-moderate cardinality partition columns that support common pruning; overpartitioning creates tiny directories/files. Sorting within partitions can help locality/compression or downstream access, but global ordering normally shuffles and does not by itself create a guaranteed table read order.

Temporary views expose a DataFrame to SQL within the current session; global temporary views have broader application-session scope through their special database, not permanent catalog lifetime. A persistent table stores catalog metadata and optionally manages data lifecycle depending on table/provider/location. Track whether dropping the table removes data.

Use `createOrReplaceTempView`, `spark.sql`, DataFrame readers/writers and `saveAsTable`/SQL DDL/DML in practice. Validate final schema, row counts, partition/file layout and restart/session behavior—not only whether the cell ran.

> **Related item:** SQL and the DataFrame API generally compile to the same structured engine. Choose the clearest interface and inspect the plan; neither is inherently faster for an equivalent optimized plan.

---

## 3. Developing DataFrame/Dataset API Applications (30%)

### Manipulate columns and rows without losing semantics

Use column expressions, not Python scalar logic over distributed rows. `select` projects/reorders/aliases expressions; `withColumn` adds/replaces one named column; `withColumnRenamed` changes a name; `drop` removes columns; `filter`/`where` keeps rows matching three-valued SQL conditions. Remember null comparisons: use `isNull`/`isNotNull` or null-safe equality where required, not `== None` as ordinary business comparison.

Split strings with `split`, access array elements carefully, and `explode` arrays/maps into multiple rows. Check empty/null collection behavior and row multiplication. Prefer built-in functions because Spark can analyze/optimize/generate code around them; a Python UDF creates serialization and optimization boundaries.

For missing data, `na.drop()` with the default “any” removes a row containing a null in any considered column; “all,” thresholds and subsets change behavior. `na.fill` must respect column types. Validate required ranges, formats, reference values, and cross-field rules explicitly; null removal is not complete data validation.

Deduplicate by the right business key. `distinct` considers all columns; `dropDuplicates(keys)` retains one row per key without expressing which conflicting record wins. Use a window ordered by event/update time and a deterministic tiebreaker when “latest” matters.

### Aggregate and handle dates deliberately

`groupBy(...).agg(...)` can calculate `count`, mean/avg, sums, min/max, exact distinct and approximate distinct. Exact distinct often needs substantial shuffle/state; `approx_count_distinct` trades controlled error for lower resource use. Know whether count includes nulls: `count(*)` counts rows while `count(column)` omits null values.

Use `summary`/`describe` for exploration, not as a substitute for business validation. Convert epoch seconds/milliseconds with the correct function/unit; parse strings with an explicit pattern where possible; extract year/month/day; and account for session time zone, daylight saving, invalid values and timestamp/date truncation.

### Combine DataFrames with correct key and row semantics

An inner join returns matching keys; a left outer join preserves left rows with null right fields where unmatched; cross joins form a Cartesian product and can explode. Multi-key joins require all intended predicates and disambiguated duplicate column names. Null keys do not normally match under ordinary equality.

A broadcast join sends a sufficiently small side to executors, avoiding a large two-sided shuffle. Use an explicit broadcast hint only when measured size and executor memory make it safe; broadcasting a misestimated large table can cause executor OOM. AQE may choose/change strategies from runtime statistics.

`union`/`unionAll` in DataFrame APIs preserve duplicates and normally align columns by position. `unionByName` aligns names and can optionally handle missing columns. Neither automatically deduplicates; apply distinct only when business semantics require it and accept its shuffle.

### Read/write, inspect, and collect safely

Always predict schema before/after casts, expressions, joins and unions. `printSchema()` prints the structure and returns no DataFrame. `show()` displays a limited representation. `collect()` brings every row to driver memory; use only for demonstrably small results. `take`, `head`, `limit().collect()`, iterators, or writing distributed output may reduce—but do not erase—driver/resource risks.

Sort with `orderBy`/`sort` and explicit ascending/descending/null ordering. A global sort creates an ordered result through shuffle but output file/partition observation still needs care. `sortWithinPartitions` does not establish global order.

### Use UDFs and shared variables only when built-ins cannot express the work

Ordinary UDFs transform inputs per row/batch without cross-record state. Stateful streaming operators and their StateStore maintain key-specific state across batches/events and need timeout/watermark/checkpoint/recovery thinking; do not call an ordinary UDF “stateful” because its Python object has a mutable variable.

Broadcast **variables** distribute a read-only value efficiently to tasks and are distinct from broadcast **joins**, a physical join strategy. Accumulators support associative task-side additions visible to the driver, commonly for diagnostics; task retry/speculation can complicate exactly-once business counting, so do not use them as a transactional counter.

Prefer built-in Spark SQL functions, then higher-order functions, then Pandas UDFs/vectorized patterns, and use scalar Python UDFs only when needed. Test nulls, exceptions, type conversion and deterministic behavior.

> **Related item:** DataFrames are immutable logical plans. Reassigning a Python variable to a transformed DataFrame does not mutate the earlier DataFrame or execute it.

---

## 4. Troubleshooting and Tuning DataFrame Applications (10%)

### Tune the partition/shuffle problem you actually observe

`repartition(n, columns...)` reshuffles to create/rebalance partitions and can improve parallelism or key distribution before expensive/repeated work or output. `coalesce(n)` commonly reduces partitions with a narrower operation and is useful after filtering, but can create uneven/oversized partitions. Avoid `coalesce(1)` for substantial output.

Identify skew through task duration/input/shuffle distributions: a few tasks much larger/slower than peers, spills, GC or OOM. Mitigations include filtering earlier, better partition keys/counts, pre-aggregation, broadcast of a truly small side, AQE skew handling, salting heavy keys, and separate handling for known hot values. Each changes cost or semantics; measure it.

Reduce shuffle by projecting/filtering early, using correct join/aggregation strategy, avoiding needless global distinct/sort/repartition, and reusing materialized expensive lineage appropriately. Do not optimize by deleting a correctness-required shuffle.

Adaptive Query Execution uses runtime statistics to coalesce post-shuffle partitions, handle skew and change join strategies where enabled/supported. It improves plans within constraints; it cannot repair bad business keys, an unbounded collection, or corrupt source data.

### Use plan, UI, logs, and metrics in order

Start with the exception and application/job/stage/task timeline. Use `explain` to inspect logical/physical plans, then Spark UI SQL/DAG/stages/tasks/executors/storage/environment tabs. Compare input/output, records, shuffle read/write, spill, task time distribution, locality, executor loss, memory/GC and failed retries.

Driver logs show scheduling/application/collection/driver OOM and application exceptions. Executor logs show task/UDF/native/Python worker failures and executor OOM; obtain them through the Spark UI or cluster manager/log delivery, not by guessing a local path on the driver. Preserve event logs/metrics for completed application investigation.

Driver OOM often follows `collect`, large result metadata, too many tasks/files, or driver-side objects. Executor OOM may follow oversized/skewed partitions, unsafe broadcast, cache pressure, Python/native overhead, or too much task concurrency. Cluster underutilization can reflect too few partitions, serial driver work, slow source, skew, blocked I/O, or resource allocation—not only small cluster size.

> **Related item:** A faster job that silently drops late/duplicate records or changes join/output semantics is a regression. Tune against correctness assertions and repeatable workload evidence.

---

## 5. Structured Streaming (10%)

### Think of a stream as an incrementally maintained table

Structured Streaming applies DataFrame/Dataset operations to an unbounded input and incrementally updates a result, commonly in micro-batches. A trigger controls processing cadence; it is not the event-time window. The engine tracks source progress and state through checkpoints/offset logs/commits. End-to-end exactly-once claims depend on replayable sources, deterministic processing, checkpoint integrity, and an idempotent or transactional sink; arbitrary external side effects can violate them.

Create a streaming DataFrame with `readStream`, define selection/filter/projection/window/aggregation/dedup transformations, and start a query with `writeStream` using format/sink, output mode, checkpoint location, trigger and query name/options. Treat checkpoint identity and query logic/source/sink compatibility carefully across changes.

Output modes:

- **append** emits final/new rows that will not be updated under the query semantics;
- **update** emits rows changed since the last trigger where supported;
- **complete** rewrites the entire result table for an aggregation and can be costly.

Support depends on transformation and sink. Choose from result semantics, not preference.

### Bound state with event time and watermarks

Windowed aggregations group events by event-time windows; processing time is when the engine handles them. Late records arrive after their event time. A watermark expresses how far behind the maximum observed event time the engine may generally wait before evicting old state; it is not a guarantee that every later record is discarded at exactly one boundary.

Streaming deduplication without a watermark/state bound can retain keys indefinitely. With event time and watermark, Spark can eventually remove old state; select keys and delay from duplicate semantics and expected lateness. Test on-time, late-within-threshold, too-late, restart/replay and duplicate records. Monitor state rows/size, input/processing rates, batch duration, watermark and sink progress.

> **Related item:** Stateful UDF/operator behavior, StateStore, watermark, checkpoint and sink idempotency form one recovery contract. Studying only the transformation method misses correctness.

---

## 6. Spark Connect and Deployment Modes (5%)

Spark Connect separates a client from the remote Spark driver through a protocol based on unresolved logical plans and results. It enables thin clients, language/tool integration, remote session isolation and decoupled client/server upgrades within compatibility limits. Code relying on driver JVM internals, SparkContext/RDD access, local files or unsupported APIs may not work the same; check the current [Spark Connect overview](https://spark.apache.org/docs/latest/spark-connect-overview.html).

Do not conflate Connect with `spark-submit` deployment mode. Connect describes client-to-Spark-server interaction. Client, cluster and local describe where the application driver/execution lives. A Connect client can run outside the cluster while the Connect server/driver executes remotely; application resource/configuration and authentication still belong to the remote environment.

Test session configuration, artifacts/dependencies, version compatibility, authentication/network, plan serialization, result collection and disconnect/retry behavior. Keep transformations in supported DataFrame/SQL APIs for portability.

> **Related item:** Moving computation to the cluster does not move local Python files, environment variables or credentials automatically. Make every dependency and data location explicit.

---

## 7. Pandas API on Spark (5%)

[Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/tutorial/pandas_on_spark/index.html) offers a pandas-like API backed by distributed Spark execution. It helps pandas users scale familiar transformations without collecting all data to one process, while retaining Spark plans/partitions/shuffles. It is not identical pandas: default indexes, ordering, type behavior, supported APIs and expensive global operations matter. Inspect execution and avoid conversions to pandas unless the result fits driver memory.

A Pandas UDF exchanges vectorized batches through Arrow and applies pandas operations to Series/DataFrame batches or grouped/iterator forms. Define Python type hints/return schema correctly and handle nulls/batch boundaries. Vectorization can outperform row-wise Python UDFs, but built-in Spark functions usually provide the best optimizer visibility and least serialization.

Pandas API on Spark is a high-level DataFrame API; a Pandas UDF is an extension point inside a Spark plan. Know which problem each solves. Benchmark with realistic rows/width and include serialization/memory/spill—not a tiny local example.

> **Related item:** “Looks like pandas” describes developer ergonomics, not single-machine execution semantics. Any operation requiring one global order/index can cause substantial distributed work.

---

## Integrated decision scenarios

### Scenario A — daily customer-file normalization

Read CSV with an explicit schema and corrupt-record policy, normalize/validate fields with built-ins, parse event dates under a known timezone, quarantine failures, deterministically deduplicate by business key/latest update, broadcast a measured-small reference table, aggregate, and overwrite a controlled date partition. Inspect plan/shuffle/file sizes and validate counts/nulls/duplicates before publishing a persistent table and temp validation view.

### Scenario B — skewed clickstream session metrics

Read events as a streaming DataFrame, extract/project early, apply event-time windows and watermark-aware deduplication, aggregate by product/session class, and write with checkpoint plus a compatible output mode/sink. Load-test one hot product key; inspect state, task skew, shuffle, batch duration and input/processing rates; apply AQE/preaggregation/salting only with correctness comparison and restart/replay tests.

### Scenario C — remote Spark Connect application

A Python client connects to a governed remote Spark service, builds only supported DataFrame/SQL plans, reads a partitioned Parquet/Delta source, joins and writes results without collecting. Package dependencies/config explicitly, authenticate through the remote service, distinguish client location from the remote driver/cluster deployment, and diagnose a slow write through plan, UI and executor logs rather than client-only timing.

## Hands-on lab sequence

1. **Execution anatomy:** Run narrow and wide transformations followed by two actions; map application/job/stage/task, partitions, shuffle and recomputation, then cache/materialize/unpersist and compare.
2. **SQL and I/O:** Read CSV/JSON/Parquet with explicit schemas; query files and temp views; write append/overwrite/partitioned outputs and a table; verify schemas, modes, files and session persistence.
3. **DataFrame correctness:** Implement column, null, explode, validation, deterministic dedup, aggregate/date, join and union cases against adversarial fixtures; predict every schema/row result first.
4. **UDF/shared variables:** Implement the same rule with a built-in, scalar UDF and Pandas UDF; compare plan/runtime/null behavior. Demonstrate a broadcast variable/accumulator and explain retry limitations.
5. **Tune a skewed join:** Generate hot keys, measure tasks/shuffle/spill/GC, then test partitioning, broadcast, preaggregation, AQE and salting with identical result assertions.
6. **Streaming recovery:** Build a windowed aggregate and dedup query with event time, watermark, output mode and checkpoint; inject duplicates/late data, stop/restart and inspect state/progress.
7. **Spark Connect:** Run a supported remote DataFrame/SQL application, test version/dependency/session behavior and one unsupported/local-driver assumption, then diagnose through remote evidence.
8. **Pandas API on Spark:** Port a pandas cleaning task, inspect its Spark plan/partitions, compare built-in/Pandas API/Pandas UDF approaches, and prove no unsafe full-data conversion occurs.

## Readiness checks

### Architecture and SQL

- [ ] I can map driver, worker, executor, CPU/task slots, memory and cluster manager responsibilities.
- [ ] I can compare local, client and cluster modes without confusing them with Spark Connect.
- [ ] I can explain application→job→stage→task and identify shuffle stage boundaries.
- [ ] I can distinguish lazy transformations/actions and predict recomputation across actions.
- [ ] I can distinguish narrow/wide work and relate partitions to task concurrency.
- [ ] I can choose cache/persist/storage level, materialize it and unpersist it with measured reuse.
- [ ] I can explain lineage task recovery versus executor/driver/external-side-effect failure boundaries.
- [ ] I can distinguish DataFrame, JVM Dataset and RDD optimization/typing boundaries.
- [ ] I can recognize Core, SQL/DataFrames, Structured Streaming, Pandas API on Spark and MLlib roles.
- [ ] I can read CSV/JSON/Parquet/ORC/text/Delta/JDBC with explicit schema and source-specific validation.
- [ ] I can configure parallel JDBC reads without overwhelming the source.
- [ ] I can query supported files through SQL and distinguish files, temp/global-temp views and persistent tables.
- [ ] I can choose append/overwrite/error/ignore and explain retry/partition-overwrite risk.
- [ ] I can distinguish write `partitionBy`, execution `repartition`, `coalesce` and sort semantics.

### DataFrame API and tuning

- [ ] I can use select/alias/withColumn/rename/drop/filter/split/explode and predict null/row/schema effects.
- [ ] I can apply `na.drop`/fill and business validation without confusing “any” and “all.”
- [ ] I can distinguish distinct/dropDuplicates from deterministic latest-record selection.
- [ ] I can calculate aggregates and compare exact versus approximate distinct tradeoffs.
- [ ] I can parse/convert/extract dates and timestamps with units, formats and timezone awareness.
- [ ] I can implement inner/left/cross/multi-key joins and reason about null/duplicate columns.
- [ ] I can choose a broadcast join from size/memory evidence and recognize broadcast OOM risk.
- [ ] I can distinguish union/unionAll/unionByName and preserve/deduplicate rows intentionally.
- [ ] I can sort, print schema, show/take/collect and avoid driver-memory mistakes.
- [ ] I can choose built-in, ordinary UDF, Pandas UDF or stateful operator and explain optimization/state.
- [ ] I can distinguish broadcast variables from broadcast joins and explain accumulator retry limits.
- [ ] I can use explain/Spark UI/stage-task metrics/driver-executor logs as one diagnostic chain.
- [ ] I can distinguish driver OOM, executor OOM, skew, spill, GC and cluster-underutilization signatures.
- [ ] I can choose repartition/coalesce and reduce shuffle without changing required semantics.
- [ ] I can explain AQE coalescing, skew and join adaptation—and its limits.

### Streaming, Connect, and pandas

- [ ] I can explain incremental/micro-batch processing, triggers, checkpoints and qualified exactly-once claims.
- [ ] I can create readStream/writeStream queries and choose compatible append/update/complete modes and sinks.
- [ ] I can distinguish event time, processing time, window and trigger.
- [ ] I can explain watermark-aware state eviction and deduplication for late/replayed data.
- [ ] I can test streaming restart, checkpoint compatibility, source replay and sink idempotency.
- [ ] I can explain Spark Connect client/server logical-plan/result behavior and unsupported/local assumptions.
- [ ] I can package/configure/authenticate a remote Connect application and diagnose it on the remote engine.
- [ ] I can choose Pandas API on Spark for pandas ergonomics without assuming single-node behavior.
- [ ] I can create a typed/schema-correct Pandas UDF and compare its Arrow boundary to built-ins/scalar UDFs.
- [ ] I can complete all common API recall exercises without exam-time documentation.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Pick the resources that fit your gaps; spend most time writing, predicting, testing, and diagnosing Spark code. Durations are vendor totals where public or planning estimates checked September 1, 2026 and may change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page and October 30, 2025 guide](https://www.databricks.com/learn/certification/apache-spark-developer-associate) | Free | 2–3 hours to map objectives and inspect vendor sample format; do not redistribute questions |
| [Databricks Academy](https://customer-academy.databricks.com/) — *Introduction to Apache Spark*, *Developing Applications*, *Stream Processing and Analysis*, and *Monitoring and Optimizing Spark Workloads* | Free account/customer or partner entitlement varies | 20–35 hours with labs; catalog totals and availability require sign-in |
| [Apache Spark documentation](https://spark.apache.org/docs/latest/) and [PySpark API](https://spark.apache.org/docs/latest/api/python/) | Free | 12–20 hours selected architecture, SQL/DataFrame, streaming, Connect and pandas/API work |
| Databricks Free Edition/local Spark plus this guide's eight labs | Free/organizational | 25–45 hours including skew, recovery, logs/UI and remote/Connect experiments |
| [Pluralsight: Apache Spark for Data Scientists](https://www.pluralsight.com/paths/apache-spark-for-data-scientists) | Paid/trial; 11 courses and 5 labs | 9 hours listed plus 6–12 hours applied practice; map out-of-scope ML/Graph work and close Connect/deployment gaps |
| [O'Reilly: Learning Spark, 2nd Edition](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/) | Paid/trial; 397-page 2020 book | 9 hours 49 minutes listed plus labs; strong Chapters 2–8, but Spark 3-era and requires current Connect/Pandas/API checks |
| [O'Reilly: High Performance Spark, 2nd Edition](https://www.oreilly.com/library/view/high-performance-spark/9781098145842/) | Paid/trial; June 2026 Spark 4.x book | 10 hours 46 minutes listed; select architecture/skew/tuning/Connect sections—advanced and intentionally broader than the exam |
| [Udemy: Apache Spark 4 hands-on guide — Ansh Lamba](https://www.udemy.com/course/databricks-certified-associate-developer-for-apache-spark-4/) | Paid; updated July 2026 when checked | 20–35 hours planning estimate with exercises; verify exact runtime and October 2025 blueprint mapping |

The current exam has no API documentation aid. Databricks staff state that the official guide's sample questions—not a full official practice exam—are the public readiness sample. No exact current MeasureUp, Whizlabs, or exam-aligned O'Reilly/LinkedIn Learning product was independently verified. Reject resources that advertise recalled/real questions or still teach the retired Spark 3.0 exam format as current.
