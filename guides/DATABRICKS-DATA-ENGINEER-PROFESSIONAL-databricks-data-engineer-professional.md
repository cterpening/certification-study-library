---
exam_code: DATABRICKS-DATA-ENGINEER-PROFESSIONAL
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/data-engineer-professional
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# Databricks Certified Data Engineer Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-data-engineer-professional-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/data-engineer-professional) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-DATA-ENGINEER-PROFESSIONAL`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official exam guide for the live version as of July 3, 2026; live weighted page checked September 1, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026. Recheck the official guide two weeks before the appointment, as Databricks requests.<br>
**Lifecycle status:** Active; valid for two years, with the currently live exam required for recertification.<br>
**Assessment:** 59 scored multiple-choice questions, 120 minutes, USD 200, no test aids or API documentation, online or test-center delivery; English, Japanese, Brazilian Portuguese, and Korean listed.<br>
**Prerequisite:** None required. The official guide highly recommends related training and one year of hands-on experience performing its data-engineering tasks.<br>
**Scope posture:** This is a production-engineering guide. Be able to explain correctness, state, security, observability, cost, deployment and recovery—not only write a successful notebook cell.

## How to use this guide

Build one evolving system rather than ten isolated demos. For every pipeline, retain source contract, schema, checkpoint/state, target grain, quality results, code/package revision, bundle target, run/update IDs, identity, grants, cost/performance evidence, failure artifacts and cleanup.

```text
contract -> governed acquisition -> replayable bronze -> tested transformations
-> quality/quarantine -> CDC and consumer model -> shared or federated access
-> orchestrated deployment -> observability and alert -> repair/recovery evidence
-> retention/privacy proof -> measured cost and performance improvement
```

Weights are study-budget signals, not form guarantees. Python/SQL development, transformation and debugging/deployment total 42%, but professional answers must connect those to security, governance and production evidence.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes an objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Databricks' published exam objectives.

## Objective map

| Published domain | Weight | Professional decision or artifact |
|---|---:|---|
| Developing Code for Data Processing using Python and SQL | 22% | Modular project, dependency boundary, batch/stream pipeline, CDC/control flow and automated tests. |
| Data Ingestion & Acquisition | 7% | Format/source contract, append behavior, schema/state and replay. |
| Data Transformation, Cleansing, and Quality | 10% | Efficient transformation with explicit quality/quarantine evidence. |
| Data Sharing and Federation | 5% | Governed D2D/open sharing or federated access with ownership and failure boundaries. |
| Monitoring and Alerting | 10% | System/query/Spark/event/API evidence plus actionable notification or data-quality alert. |
| Cost & Performance Optimisation | 13% | Measured layout, plan, compute, maintenance and incremental-processing decision. |
| Ensuring Data Security and Compliance | 10% | Least privilege, sensitive-data transformation and provable retention/purge behavior. |
| Data Governance | 7% | Discoverable metadata and correct Unity Catalog inheritance/ownership. |
| Debugging and Deploying | 10% | Evidence-led repair and environment-aware bundle/Git CI/CD. |
| Data Modelling | 6% | Scalable Delta and dimensional design with deliberate clustering/partition choices. |

---

## 1. Developing code for data processing using Python and SQL (22%)

### Design a deployable Python project

A professional project separates pure business transformations from I/O, orchestration and environment configuration. A useful shape is:

```text
src/project/
  contracts.py       # schemas and configuration models
  transforms.py      # DataFrame -> DataFrame functions
  quality.py         # expectations and quarantine rules
  pipelines.py       # read/write composition
tests/unit/
tests/integration/
resources/           # job and pipeline definitions
databricks.yml       # bundle identity, includes, variables and targets
pyproject.toml       # package/dependency/test configuration
```

[Declarative Automation Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) package resource configuration, files and environment targets for validate/deploy/run workflows. Keep environment-specific workspace paths, catalogs, schemas, service principals and permissions in target configuration—not hard-coded inside transformations. The official guide uses “Declarative Automation Bundles” and notes the former Databricks Asset Bundles/DABs name.

### Control third-party dependencies

Choose PyPI packages, wheels or source archives from repeatability and support requirements. Pin direct dependencies deliberately, build an immutable wheel, scan provenance/license/vulnerabilities, test against the target runtime, and install at a supported scope. The [library documentation](https://docs.databricks.com/aws/en/libraries/) distinguishes compute, job-task and notebook approaches. Diagnose installation failures through repository reachability, authentication, Python/runtime/ABI compatibility, transitive conflicts, init order and driver/executor availability.

Do not use a notebook `%pip install latest-package` as the production definition. Capture resolution in `pyproject.toml`/lock or build metadata, publish to a controlled artifact repository, and prove a clean-environment install.

### Choose native expressions before UDFs

Prefer built-in Spark SQL/DataFrame expressions because the optimizer can understand them. A scalar Python UDF crosses serialization/runtime boundaries; a Pandas UDF uses Arrow/vectorized batches and can be a better fit for supported vectorized logic, but still adds type, memory and dependency constraints. Review [Pandas UDF behavior](https://docs.databricks.com/aws/en/udf/pandas) and declare input/output schemas.

> **Related item:** A UDF decision is not only about syntax. It affects optimizer visibility, serialization, executor memory, library deployment, error handling and whether the logic can be expressed portably in SQL.

### Build batch and streaming pipelines with explicit state

[Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/) manages declarative batch/stream data flows, dependencies, updates, event logs and data-quality expectations. [Structured Streaming](https://docs.databricks.com/aws/en/structured-streaming/) offers lower-level control over source, sink, trigger, checkpoint, watermark and `foreachBatch` behavior. Choose declarative pipelines for managed data-flow semantics and expectations; choose Structured Streaming when custom state/control/integration requirements justify the responsibility.

Auto Loader (`cloudFiles`) incrementally discovers cloud files and stores discovery/schema progress. Checkpoint and schema state are production assets. Deleting or reusing them can cause replay, duplicates or data loss depending on sink idempotency.

### Implement CDC and append flows deliberately

`AUTO CDC` replaces the older `APPLY CHANGES` name in current Lakeflow documentation. It sequences change events into a target and supports SCD patterns. Define keys, sequence column, deletion/truncation semantics, ignored columns and out-of-order behavior; prove duplicates and late events. Review [AUTO CDC APIs](https://docs.databricks.com/aws/en/ldp/cdc).

A streaming table is incrementally updated from a stream; a materialized view maintains query results. Streaming tables strongly fit append/change streams, while materialized views fit declarative derived results with managed refresh. Confirm source compatibility, latency, update mode and full-refresh consequences.

### Orchestrate control flow without assuming transactionality

Lakeflow Jobs supports task dependencies, run-if outcomes, `if/else`, `for each`, retries and parameters. Successful upstream tasks are not automatically rolled back if a later task fails. Make task effects idempotent or compensatable, persist commit/evidence boundaries and use [job control flow](https://docs.databricks.com/aws/en/jobs/control-flow) intentionally.

Choose compute/configuration per task: high-memory needs do not justify oversizing every task; retries are unsafe for non-idempotent side effects; an optimization or automatic setting needs a measured purpose. Jobs can be created through UI, CLI or REST APIs, but the deployed definition should have one controlled source of truth.

### Test transformations and systems

- Unit-test pure DataFrame transforms with small, adversarial fixtures. `assertDataFrameEqual` compares data; `assertSchemaEqual` protects structure.
- Test nulls, duplicates, empty input, bad types, late/out-of-order events, timezone boundaries and skewed keys.
- Integration-test source, checkpoint, target, identity, dependency and bundle wiring in an isolated catalog/schema.
- Verify exactly-once claims at the application boundary by replaying the same input and comparing target state.
- Use a debugger locally or in supported Databricks tooling for code paths; use event/run/Spark evidence for distributed behavior.

The [PySpark testing guidance](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html) documents the built-in equality helpers.

---

## 2. Data ingestion and acquisition (7%)

### Model source behavior before selecting a reader

| Source/format | Important contract |
|---|---|
| Delta | table version, schema, change data, concurrent writers and retention |
| Parquet/ORC/Avro | schema, partitions/blocks, compression and evolution |
| JSON/XML | record boundary, nested fields, malformed data and schema drift |
| CSV/text | delimiter, quoting, header, encoding, line endings and types |
| Binary | metadata and content ownership; parsing occurs downstream |
| Message bus | offsets, event time, ordering, retention and replay |
| Cloud files | discovery mode, arrival order, checkpoint, schema state and archive/cleanup |

The Spark [data-source documentation](https://spark.apache.org/docs/latest/sql-data-sources.html) is the engine reference; Databricks source/connector support and runtime behavior remain the operational authority.

An append-only pipeline promises it will not mutate earlier source events, not that every upstream system is append-only. Land immutable raw records with source identity, event/ingest time and provenance; deduplicate or apply CDC in a later controlled layer. For a single design that accepts historical batch plus continuing stream, ensure both paths use compatible schema, identifiers and target semantics.

> **Related item:** Event-time watermarking bounds state for late data; it is not an ingestion completeness guarantee. Record the accepted lateness and what happens to events beyond it.

---

## 3. Transformation, cleansing and quality (10%)

### Write efficient transformations with known semantics

Use projections and selective filters early, avoid unnecessary Python boundaries, and make join cardinality explicit. Broadcast only a genuinely bounded side. A window has partition and ordering semantics; an aggregate collapses grain. Validate before optimizing:

```python
def build_daily_sales(lines, products):
    valid = lines.filter("quantity > 0 AND net_unit_price >= 0")
    return (valid.join(products.select("product_id", "category"), "product_id")
                 .groupBy("order_date", "category")
                 .agg(F.sum(F.col("quantity") * F.col("net_unit_price")).alias("revenue")))
```

Test unmatched product keys, duplicates, nulls and overflow/precision. Avoid `collect()` for production-scale data and arbitrary repartitioning without plan evidence.

### Quarantine rather than silently coerce

Lakeflow expectations can warn, drop or fail an update depending on policy. Quarantine patterns route invalid records with original payload, rule ID, reason, source position, detected timestamp and reprocessing status. With Auto Loader in classic jobs, implement equivalent valid/invalid branches and preserve checkpoint semantics.

Define which defects block publication versus permit degraded operation. Measure total, valid, invalid and duplicate counts; reconcile `input = accepted + quarantined` when the policy supports it. Protect quarantine access because invalid rows often contain sensitive fields.

> **Related item:** A dead-letter location without an owner, remediation SLA and replay path is a data graveyard—not a quality system.

---

## 4. Data sharing and federation (5%)

### Select D2D, open sharing or federation

[Delta Sharing](https://docs.databricks.com/aws/en/delta-sharing/) supports Databricks-to-Databricks sharing and an open protocol for external recipients. A provider controls share contents and recipient access; the recipient queries live shared data without owning the provider's files. D2D can use Databricks identities/objects; open sharing uses recipient credentials/tokens that require secure rotation and revocation.

[Lakehouse Federation](https://docs.databricks.com/aws/en/query-federation/) uses governed connections and foreign catalogs to query supported external systems without first ingesting them. Choose it when freshness and no-copy access outweigh remote latency, pushdown limitations and source-capacity dependency.

| Requirement | Starting point |
|---|---|
| Share live governed assets outward | Delta Sharing |
| Databricks recipient with native collaboration | D2D sharing |
| Non-Databricks recipient | Open sharing protocol |
| Query an operational system in place | Federation |
| Repeated heavy transformation, isolation or strict SLA | Ingest/materialize with an owned freshness contract |

Record data owner, recipient, objects/columns, update/freshness, revoke path, audit evidence and egress/cost. Do not confuse a share with copying or federation with replication.

---

## 5. Monitoring and alerting (10%)

### Build observability by layer

- [System tables](https://docs.databricks.com/aws/en/admin/system-tables/) expose supported account/workspace operational data for billing, audit, compute, jobs, pipelines and query history. Scope, region availability, retention and schema vary; query them through Unity Catalog permissions.
- Query Profile explains SQL operators, scans, joins, shuffle and skew.
- Spark UI explains jobs/stages/tasks, executor work, shuffle, spill, skew and memory pressure.
- Jobs/Pipelines UI and REST API expose run/update state and lifecycle.
- The [pipeline event log](https://docs.databricks.com/aws/en/ldp/monitor-event-logs) supplies update, flow, expectation, progress and error evidence.

Correlate by run/update/query identifiers and time window. A billing spike without workload attribution, or a failed task without source/checkpoint state, is incomplete evidence.

### Alert on an actionable condition

A SQL alert evaluates a query result against a threshold. For data quality, write a stable query such as invalid ratio, freshness lag or reconciliation difference; define schedule, threshold, empty/error behavior, notification destination, owner, deduplication and runbook. Job notifications cover lifecycle/performance events; they do not replace business-data alerts.

Avoid alerting on every transient symptom. Route warnings and failures differently, include environment/resource/run links, and test delivery plus recovery. Review [job notifications](https://docs.databricks.com/aws/en/jobs/notifications) because destinations and system-destination behavior are volatile.

> **Related item:** Monitoring tells you what happened; an SLO says what acceptable service means; an alert should identify an actionable breach before the user discovers it.

---

## 6. Cost and performance optimisation (13%)

### Diagnose the bottleneck before choosing a lever

Use a controlled loop: reproduce, capture plan/profile/Spark evidence, identify the dominant scan/shuffle/skew/spill/remote/queue/driver condition, change one factor, compare correctness and cost. Bigger compute can reduce elapsed time while increasing total cost and cannot correct a Cartesian join or single hot key.

### Understand table maintenance and layout

Unity Catalog managed tables reduce manual lifecycle and maintenance burden and enable managed features such as predictive optimization where eligible. External tables retain external data-lifecycle responsibility.

- **Deletion vectors** can mark changed/deleted rows without rewriting whole data files for supported operations; later maintenance materializes changes.
- **Data skipping** uses file statistics to avoid reading irrelevant files; selective predicates and useful layout make it effective.
- **File pruning** avoids irrelevant partitions/files. High-cardinality or tiny partitioning creates metadata and small-file costs.
- **Liquid clustering** incrementally clusters by chosen keys and is generally more flexible than fixed partitions or Z-order for eligible Delta tables.
- **Predictive optimization** can automate maintenance on eligible managed tables; verify account/runtime/region and cost behavior.

Use [liquid clustering](https://docs.databricks.com/aws/en/delta/clustering), [deletion vectors](https://docs.databricks.com/aws/en/delta/deletion-vectors), and [predictive optimization](https://docs.databricks.com/aws/en/optimizations/predictive-optimization) as current sources.

### Apply CDF and incremental processing from a contract

[Change Data Feed](https://docs.databricks.com/aws/en/delta/delta-change-data-feed) records row-level changes after enablement within table-history retention. It can drive incremental downstream work and address some full-read latency limitations. It does not contain changes from before enablement and is not an indefinite archive. Persist downstream progress and define behavior after the starting version ages out.

> **Related item:** Checkpoint state tracks a streaming query; CDF exposes table changes; `AUTO CDC` applies ordered changes to a target. They are related but not interchangeable state mechanisms.

---

## 7. Ensuring data security and compliance (10%)

### Layer least privilege

- Workspace ACLs protect notebooks, folders, jobs, pipelines and other workspace objects.
- Unity Catalog privileges protect catalogs, schemas, tables, views, volumes, functions and other securables.
- Compute policies and `CAN USE`-style permissions constrain execution resources.
- Secrets should be referenced through supported secret management and never logged, embedded in bundles or returned as data.
- Row filters and column masks enforce supported table-level dynamic policies; ABAC can centralize tag-driven policy where eligible.

The [Unity Catalog access-control overview](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/) maps privileges, ownership, ABAC, filters/masks and workspace bindings. Grant to account groups/workload identities and separate deployer, runtime owner and data consumer.

### Distinguish privacy transformations

| Technique | Effect | Boundary |
|---|---|---|
| Hashing | One-way digest; vulnerable to dictionary/linkage depending on input/salt | often pseudonymization, not guaranteed anonymity |
| Tokenization | Replaces value with controlled token; mapping may permit reversal | mapping store becomes highly sensitive |
| Suppression | Removes/redacts fields or rows | can reduce utility and leave linkage through other fields |
| Generalization | Coarsens values such as age band or region | assess re-identification across combined quasi-identifiers |
| Masking | Changes value shown to a principal/context | source may remain present and accessible to privileged users |

Build PII detection/classification before masking, cover batch and streaming paths, quarantine detection uncertainty, and test unauthorized identities. Privacy is not achieved by printing “REDACTED” in one notebook.

### Prove retention and purge

Define data classes, legal/business retention, authoritative locations, replicas/shares/caches/checkpoints/backups, delete trigger, execution SLA and evidence. Delete or anonymize eligible records in tables; propagate to downstream materializations; revoke shared access; account for time travel and file cleanup. Aggressive `VACUUM` can break readers and recovery, while deleting a catalog entry alone may not delete external data.

**VERIFY CURRENT:** retention, predictive maintenance, fine-grained controls, serverless identity and regional compliance behavior change. Validate in the actual cloud/account and involve legal/privacy owners.

---

## 8. Data governance (7%)

### Make data discoverable and govern inheritance

Add meaningful catalog/schema/table/column descriptions, ownership, tags, domain, sensitivity, quality/freshness expectation and certification only through a controlled stewardship process. Use lineage for impact and discovery, but treat it as supported captured evidence rather than an exhaustive dependency database.

Unity Catalog privileges inherit downward from catalog/schema grants; metastore grants and ownership have broader effects. To select a table, a principal normally requires `USE CATALOG`, `USE SCHEMA` and `SELECT`, whether directly or inherited. Avoid redundant grants and group sprawl; record the intended effective access, then test it. Review the current [privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/privileges).

> **Related item:** Metadata tags support discovery and ABAC; certification communicates steward-reviewed trust; neither automatically grants access or guarantees a metric's business definition.

---

## 9. Debugging and deploying (10%)

### Triage failures from symptom to state

1. Identify environment, resource, run/update/task/query ID, code/bundle revision and principal.
2. Read the first causal error, not only the final wrapper.
3. Check job/pipeline events, cluster/driver/executor logs, system tables, Query Profile and Spark UI as appropriate.
4. Determine the commit boundary: which tasks/tables/external side effects succeeded?
5. Preserve evidence, correct the smallest root cause, repair from a safe task boundary or rerun idempotently, then reconcile outputs.

[Job repair](https://docs.databricks.com/aws/en/jobs/repair-job-failures) can rerun failed/skipped tasks and optionally dependent tasks with parameter overrides. It does not undo successful side effects. Parameters used for recovery must be auditable and must not bypass quality/security controls.

For pipeline failures, inspect event-log error context, flow progress, expectations, source offsets/files, schema/checkpoint state and Spark evidence. A full refresh can replace state/data and is not a generic retry.

### Deploy from version control

Use Git folders for collaborative development and source synchronization, but deploy production resources through reviewed CI/CD and a bundle or equivalent declarative contract. A robust flow runs formatting/static checks, unit tests, bundle validation, security/dependency checks, isolated integration deployment/tests, approval and production deployment with a workload identity.

Keep secrets out of Git and CI logs. Use environment targets and least-privilege service principals. Tag deployed resources with revision/environment and retain validation/deployment evidence. Review current [CI/CD guidance](https://docs.databricks.com/aws/en/dev-tools/ci-cd/).

> **Related item:** CI validates and packages change; CD applies it to an environment. Git synchronization alone is neither a release approval nor a reproducible infrastructure deployment.

---

## 10. Data modelling (6%)

### Design Delta tables from workload and lifecycle

Declare grain, business keys, surrogate keys, change semantics, access predicates, retention and ownership. Use Delta for transaction/history/schema/table features, then select managed/external lifecycle. Avoid encoding every consumer into one wide mutable table.

Partitioning works best for low-cardinality columns commonly used for pruning and with enough data per partition; overpartitioning creates tiny files/directories. Liquid clustering supports evolving multi-column access patterns without fixed directory partitions and can replace many partition/Z-order designs for eligible tables. Measure rather than copying a column choice from an unrelated workload.

### Build dimensional models for analytics

A fact table has a declared event/snapshot grain and foreign keys to conformed dimensions. Measures may be additive, semi-additive or non-additive. Dimensions carry descriptive context and can preserve history with slowly changing patterns. Use unknown members or an explicit unmatched-key workflow to prevent silent fact loss.

Medallion layers and dimensional modeling answer different questions: bronze/silver/gold describe progressive quality/serving boundaries; star schemas describe consumer relationships and grain. A gold layer can contain multiple dimensional marts.

> **Related item:** Physical layout (partitioning/clustering), logical model (facts/dimensions) and incremental semantics (append/merge/CDC) are three separate decisions that must agree with the workload.

---

## Integrated decision scenarios

### Scenario A — regulated customer-event platform

Cloud files and a message bus supply historical and live customer events. Define immutable identifiers, schema/checkpoint/watermark state and Auto Loader/stream contracts. Land replayable bronze, quarantine malformed/PII classification failures, apply AUTO CDC into conformed customer history, and publish dimensional marts. Enforce least privilege, masks and privacy transformations; design purge across tables, CDF consumers, shares and history. Deploy via bundle and prove replay, denied access, late data and purge evidence.

### Scenario B — low-latency shared supply data

Internal sources use Delta while a partner database is federated and an external consumer needs open sharing. Compare federation versus ingestion based on latency/source load/SLA, create a governed connection, validate pushdown, and publish only approved objects via Delta Sharing. Monitor query/source cost and share access. Materialize repeated results only with an owned freshness process and revoke/test recipient credentials.

### Scenario C — failing and expensive production pipeline

An hourly pipeline exceeds SLA and fails after a downstream task side effect. Correlate job run, pipeline event log, query profile, Spark stages and billing/system tables. Identify skew/shuffle and a non-idempotent external write. Repair from a proven boundary, add a commit ledger/idempotency key, fix join/layout after a controlled comparison, add SLO/data-quality alerts and deploy through tested CI/CD. Prove totals and cost, not just faster completion.

## Hands-on lab sequence

1. **Project and tests:** Package two DataFrame transforms in a wheel; pin dependencies and add null/duplicate/empty/skew fixtures using DataFrame/schema equality helpers.
2. **Batch plus stream acquisition:** Process historical files then new arrivals through Auto Loader/Structured Streaming; record schema/checkpoint state and prove replay behavior.
3. **Declarative CDC and quality:** Build a Lakeflow pipeline with expectations, quarantine and AUTO CDC/SCD behavior; test duplicates, deletes and out-of-order events.
4. **Sharing/federation:** Create a written or real connection/foreign catalog and share/recipient design; test pushdown/failure and revoke access.
5. **Observability:** Correlate system table, job/pipeline event, Query Profile and Spark UI evidence; implement and test one quality alert and one run notification.
6. **Cost/performance:** Benchmark a representative query before/after one layout, join or compute change under controlled cache/data conditions; record cost and correctness.
7. **Privacy/governance:** Build group grants, row/column protection, discoverability metadata and a retention/purge evidence matrix; test authorized and denied paths.
8. **Deployment and repair:** Define dev/test/prod bundle targets and CI checks, deploy to isolation, inject a downstream failure, repair safely and reconcile side effects.

## Readiness checks

### Code, acquisition and quality

- [ ] I can separate pure transforms, I/O, configuration, resources and tests in a package/bundle project.
- [ ] I can select PyPI, wheel or source installation and diagnose version/ABI/repository/executor problems.
- [ ] I can choose native expressions, Python UDF or Pandas UDF from optimizer and runtime tradeoffs.
- [ ] I can select Structured Streaming versus Lakeflow Declarative Pipelines and state what I own.
- [ ] I can explain streaming tables versus materialized views.
- [ ] I can design AUTO CDC keys, sequence, delete and out-of-order behavior.
- [ ] I can build Jobs control flow without assuming cross-task rollback.
- [ ] I can make retry and repair safe through idempotency/commit boundaries.
- [ ] I can test DataFrame data/schema and pipeline integration with adversarial cases.
- [ ] I can define format-specific source, schema, offset/checkpoint and replay contracts.
- [ ] I can build one historical-plus-live append flow without silently duplicating data.
- [ ] I can choose efficient SQL/DataFrame joins, windows and aggregations at a declared grain.
- [ ] I can quarantine bad data with owner, reason, evidence and replay.

### Sharing, observation and optimization

- [ ] I can distinguish D2D sharing, open Delta Sharing and Lakehouse Federation.
- [ ] I can document provider/recipient/connection identity, freshness, revocation and audit.
- [ ] I can select system tables, Query Profile, Spark UI, logs, event log, API or CLI evidence.
- [ ] I can write an actionable data-quality alert with threshold, owner and runbook.
- [ ] I can configure run notifications without treating them as business-data monitoring.
- [ ] I can diagnose scan, shuffle, skew, spill, queue, driver and remote-source bottlenecks.
- [ ] I can explain deletion vectors, data skipping, pruning, liquid clustering and predictive optimization.
- [ ] I can choose partitions/clustering from real access patterns and measure the outcome.
- [ ] I can use CDF without treating it as an indefinite archive.
- [ ] I can compare performance with controlled cache, data, compute and correctness.

### Security, governance, deployment and modeling

- [ ] I can separate workspace ACLs, Unity Catalog privileges, compute use and secrets.
- [ ] I can apply and test row filters/column masks and state ABAC/support boundaries.
- [ ] I can distinguish hashing, tokenization, suppression, generalization and masking.
- [ ] I can design a batch/stream PII control and protect its quarantine.
- [ ] I can prove purge across managed/external data, downstream copies, sharing and retained history.
- [ ] I can make catalogs/tables/columns discoverable with governed metadata.
- [ ] I can calculate effective permissions through catalog/schema inheritance and ownership.
- [ ] I can triage from IDs/revision/principal to causal distributed evidence.
- [ ] I can repair a job without assuming successful side effects roll back.
- [ ] I can distinguish Git development from tested bundle-based CI/CD deployment.
- [ ] I can deploy with environment targets, workload identity and no secret leakage.
- [ ] I can declare Delta-table grain, lifecycle, incremental semantics and physical layout separately.
- [ ] I can design fact/dimension keys, history and measure additivity.
- [ ] I can explain how medallion layers and dimensional models coexist.

## Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick the route that closes measured gaps, then spend substantial time building, breaking, observing, repairing and redeploying a system. Durations are planning estimates checked September 1, 2026 and may change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page and July 3, 2026 exam guide](https://www.databricks.com/learn/certification/data-engineer-professional) | Free | 2–3 hours to map every objective and inspect the vendor sample format; do not reproduce questions |
| [Databricks Academy](https://customer-academy.databricks.com/) — *Advanced Data Engineering with Databricks* plus four named self-paced courses | Free account, customer/partner entitlement varies | 30–50 hours with labs; verify course visibility and runtime after sign-in |
| [Databricks Free Edition](https://www.databricks.com/learn/free-edition) or an authorized workspace | Free account/organizational | 25–45 hours for the eight labs and failure experiments; some enterprise features require another environment |
| [Databricks documentation](https://docs.databricks.com/aws/en/introduction/) | Free | 10–18 hours selected reproduction across pipelines, Jobs, governance, performance and deployment |
| [Databricks YouTube](https://www.youtube.com/@Databricks) | Free | 4–8 hours selected recent Data + AI Summit, engineering, Lakeflow, Unity Catalog and performance sessions |
| [Whizlabs: Databricks Data Engineer Professional](https://www.whizlabs.com/databricks-certified-data-engineer-professional/) | Paid; training/practice product | Public stable totals were not exposed; budget 8–18 hours and verify July 2026 alignment after sign-in |
| [Udemy search: Data Engineer Professional](https://www.udemy.com/courses/search/?q=databricks%20data%20engineer%20professional) | Paid marketplace | 10–25 hours if a course demonstrably maps to the July 2026 guide; verify instructor, update, outline and avoid dump-focused listings |
| [O'Reilly search: Databricks data engineering](https://www.oreilly.com/search/?q=Databricks%20data%20engineering) | Paid/trial | 8–20 hours selected current book/video/live material; map exact chapters to the blueprint and verify publication date |

Use vendor sample questions only through the official guide, and use ethical practice tests to identify weak domains rather than memorize recalled content. Recheck the live weights, linked PDF, renamed products, course catalog and all **VERIFY CURRENT** controls near the appointment.
