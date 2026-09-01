---
exam_code: DATABRICKS-DATA-ENGINEER-ASSOCIATE
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/data-engineer-associate
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# Databricks Certified Data Engineer Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-data-engineer-associate-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/data-engineer-associate) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-DATA-ENGINEER-ASSOCIATE`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official exam guide effective May 4, 2026; live weighted coverage page checked September 1, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026. Databricks asks candidates to recheck the official exam guide close to the appointment.<br>
**Lifecycle status:** Active; valid for two years, with the currently live exam required for recertification.<br>
**Assessment:** 45 scored multiple-choice questions, 90 minutes, USD 200, no test aids, online or test-center delivery; English, Japanese, Brazilian Portuguese, and Korean were listed.<br>
**Prerequisite:** None required. The official PDF recommends related training and six months of hands-on Databricks experience. SQL, basic Python/PySpark, ETL, cloud storage, and identity knowledge make the labs more useful.<br>
**Code convention:** The official page says SQL is used where possible and Python otherwise.

## How to use this guide

Treat the seven percentages as a study-budget signal, not a promise about an individual form. Start with ingestion and transformation, which together account for 43%, then prove that the result can be orchestrated, deployed, diagnosed, optimized, and governed.

```text
source contract -> ingestion state -> bronze evidence -> validated silver
-> consumer-shaped gold -> job/pipeline trigger -> monitored run
-> least-privilege access -> repeatable bundle deployment -> recovery proof
```

For every exercise, retain the input schema, target name, checkpoint or ingestion state, code revision, run ID, principal, grants, data-quality result, row counts, failure evidence, and cleanup. Product names, release states, runtime requirements, pricing, and serverless availability change rapidly; recheck the cited documentation in the cloud where you practice.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes the objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Databricks' published exam objectives.

## Objective map

| Published domain | Weight | What you must be able to decide or do |
|---|---:|---|
| Databricks Intelligence Platform | 6% | Relate architecture, Delta Lake, Unity Catalog, and compute characteristics to a workload. |
| Data Ingestion and Loading | 21% | Select and implement batch, streaming, incremental, connector, file, and client-driven ingestion. |
| Data Transformation and Modeling | 22% | Clean, join, reshape, aggregate, validate, tune, and publish silver/gold objects. |
| Working with Lakeflow Jobs | 16% | Build task graphs, control flow, triggers, retry behavior, and operational evidence. |
| Implementing CI/CD | 10% | Use Git folders during development and Declarative Automation Bundles for repeatable environment-aware delivery. |
| Troubleshooting, Monitoring, and Optimization | 10% | Move from run history and Spark evidence to a measured correction. |
| Governance and Security | 15% | Choose object lifecycle and apply least-privilege and fine-grained Unity Catalog controls. |

---

## 1. Databricks Intelligence Platform (6%)

### Keep the planes and responsibilities separate

- The **control plane** hosts Databricks-managed services such as the workspace experience and orchestration control. The **compute plane** executes the workload. Exact networking and customer-managed boundaries differ by cloud and compute type.
- **Delta Lake** is the table/storage layer that adds a transaction log, ACID behavior, schema controls, history, and scalable batch/stream processing over cloud object storage.
- **Unity Catalog** is the governance layer for identities, the `catalog.schema.object` namespace, discovery, permissions, lineage, auditing, managed/external data, connections, functions, models, and other governed assets.
- The workspace is a collaboration and operations boundary, not the complete governance hierarchy. A catalog can be bound to workspaces; data privileges and workspace permissions solve different problems.

Start with the current [Databricks platform documentation](https://docs.databricks.com/aws/en/introduction/) and [Unity Catalog overview](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). Be able to trace a notebook query from user or workload identity through compute, Unity Catalog authorization, the table transaction log, and cloud storage.

### Select compute from requirements

| Requirement | Likely starting point | Verify before choosing |
|---|---|---|
| Interactive SQL and BI concurrency | SQL warehouse, often serverless where available | startup, concurrency, channel, auto-stop, data-source/network support, cost |
| Scheduled ETL task graph | serverless jobs or job compute | language/library needs, run isolation, startup, policy, identity, supported features |
| Interactive Python/SQL development | notebook compute | sharing/access mode, idle termination, policy, runtime and library compatibility |
| Declarative incremental pipeline | Lakeflow Spark Declarative Pipelines compute | serverless/classic eligibility, update mode, source and feature support |
| Specialized runtime or unsupported serverless dependency | governed classic compute | access mode, runtime, node family, library and network requirements |

Serverless reduces infrastructure decisions, but does not remove data, identity, dependency, cost, or observability decisions. Classic compute exposes more configuration and therefore more ways to create an unsupported or expensive design. Evaluate runtime support, CPU/memory, autoscaling, Photon eligibility, startup, isolation, library compatibility, network reachability, and the DBU plus cloud-infrastructure cost model.

> **Related item:** An autoscaling cluster cannot split one oversized partition or move driver-only work to executors. Compute selection follows the execution plan and bottleneck; it does not substitute for inspecting them.

---

## 2. Data Ingestion and Loading (21%)

### Choose by source behavior and ownership

| Mechanism | Strong fit | State and failure questions |
|---|---|---|
| `COPY INTO` | idempotent incremental file loading for straightforward batch arrivals | Which files were previously loaded? What schema/format options and validation mode apply? |
| Auto Loader (`cloudFiles`) | scalable incremental file discovery and streaming ingestion | Where are checkpoint and schema state? How are new/type-changing fields handled? Can arrivals be out of order? |
| Lakeflow Connect managed connector | supported database, SaaS, file, or streaming source where Databricks should manage more ingestion plumbing | connector release state, gateway/staging/connection, CDC semantics, schedule, destination, schema evolution |
| Standard/community/partner connector | broader source support or more customization | maintenance owner, secrets, offset/replay behavior, compatibility and support boundary |
| JDBC/ODBC/REST client in a notebook/job | bounded custom extraction or API integration | pagination/watermark, rate limit, retry, duplicate prevention, secret handling, landing versus direct table write |
| local upload/UI | tiny ad hoc learning or exploration | size, reproducibility, provenance, security; not a production ingestion strategy |

The official objectives explicitly include batch, streaming, incremental, local files, Lakeflow Connect standard and managed connectors, `COPY INTO`, Auto Loader, and JDBC/ODBC/REST clients. Use the current [Lakeflow Connect concepts](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/) because connectors have different release states and architectures.

### Implement file ingestion deliberately

`COPY INTO target FROM source FILEFORMAT = ...` tracks previously loaded files and is a simple choice for repeatable incremental batch loads. Understand target existence, source access, validation, schema and format options, and how a forced reload differs from normal idempotent behavior. Review the [COPY INTO reference](https://docs.databricks.com/aws/en/sql/language-manual/delta-copy-into).

Auto Loader exposes the `cloudFiles` Structured Streaming source. Its state is not just the target table: checkpoint and schema locations are operational assets. The [Auto Loader overview](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/) describes directory listing and file-notification modes; current guidance recommends managed file events for most suitable workloads. File notification improves discovery scale but does not guarantee arrival order.

```python
raw = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", schema_path)
    .option("rescuedDataColumn", "_rescued_data")
    .load(source_path)
)
```

Schema inference guesses a starting contract; schema evolution decides what happens when input changes; enforcement and rescue prevent silent corruption. Make an explicit choice among failing, adding columns, rescuing unexpected fields, quarantining bad records, or controlled type widening. Never equate “the stream ran” with “the data is acceptable.” Compare expected versus actual schema, parse errors, rescued-data rates, duplicates, missing keys, freshness, and source-to-target counts. Use current [schema-evolution guidance](https://docs.databricks.com/aws/en/data-engineering/schema-evolution).

### Land semi-structured and unstructured data safely

- Parse nested JSON into typed structs; select nested fields, use `explode` for arrays only when the intended output grain is clear, and preserve the raw payload or source pointer for replay.
- Do not infer a production schema from a tiny or unrepresentative sample.
- Record source file, ingestion timestamp, batch/run ID, and source business key where appropriate.
- Separate transport success from semantic quality. A valid JSON object can still violate the business contract.
- Use a Unity Catalog volume for governed non-tabular files where file semantics are required; use a table for queryable records.

> **Related item:** Exactly-once processing is an end-to-end property. A checkpoint can prevent a streaming engine from reprocessing known offsets, but an API retry, changed source file, non-idempotent side effect, or lost target transaction can still duplicate or omit business effects.

---

## 3. Data Transformation and Modeling (22%)

### Make bronze, silver, and gold responsibilities testable

- **Bronze** preserves source fidelity, provenance, and replayability. Avoid destructive cleansing that makes source reconciliation impossible.
- **Silver** applies types, keys, deduplication, normalization, quality rules, reference joins, late-data handling, and quarantine. “Clean” must be expressed as tests.
- **Gold** serves a consumer grain and contract: dimensional facts/dimensions, aggregates, features, or another product-specific model.

Medallion names are a useful pattern, not mandatory object types. A silver table without an owner, contract, quality result, and recovery path is not trustworthy merely because it is named `silver`.

### Transform in SQL and PySpark

Be fluent with equivalent operations: select/alias/cast, `withColumn`, filter, null handling, conditional logic, strings/dates, nested-field access, `explode`, grouping, `count`, approximate distinct counts, averages and descriptive summaries. Know why transformations are lazy and actions trigger execution.

For joins, reason about output grain before syntax:

| Operation | Main risk or decision |
|---|---|
| inner join | unmatched rows disappear; prove whether that is intended |
| left join | right-side duplication can multiply the left grain; unmatched values become null |
| cross join | Cartesian growth; use only with a bounded intentional design |
| broadcast join | avoid large shuffle for a genuinely small relation; measure and respect threshold/memory |
| union | aligns by position unless using a name-aware form; schemas and duplicates need explicit handling |
| deduplication | define duplicate key and winner ordering; `distinct` is not a business survivorship rule |

```python
from pyspark.sql import functions as F, Window

w = Window.partitionBy("order_id").orderBy(F.col("source_updated_at").desc())
silver = (
    bronze
    .withColumn("amount", F.col("amount").cast("decimal(18,2)"))
    .withColumn("winner", F.row_number().over(w))
    .filter((F.col("winner") == 1) & F.col("order_id").isNotNull())
    .drop("winner")
)
```

Validate row count, key uniqueness, null/type rules, accepted ranges, referential integrity, aggregation reconciliation, and rejected-record behavior. Test empty inputs, duplicate keys, malformed nested data, late arrivals, missing reference rows, and a rerun.

### Publish the right object

- A **table** persists data and supports independent lifecycle and reuse.
- A **view** stores a query and computes on read; use for an interface or security/logic layer where read-time work is acceptable.
- A **materialized view** persists derived results and refreshes them through managed pipeline behavior; use when repeated computation and acceptable freshness justify it.
- A **streaming table** incrementally processes streaming input and retains pipeline state.

Choose from latency, refresh, cost, write/read semantics, lineage, ownership, and recovery—not from the object name alone.

### Tune only after locating the bottleneck

Inspect the plan and Spark UI. A large shuffle may suggest better filtering before a join, different join order, valid broadcast, key repartitioning, or skew treatment. Spill may require less per-partition state, better partition sizing, or more memory. A slow driver may indicate excessive `collect`, result materialization, task scheduling, or metadata work.

Know the intent of `spark.sql.shuffle.partitions`, `spark.default.parallelism`, executor/driver memory, and `spark.sql.autoBroadcastJoinThreshold`, but avoid memorizing universal values. Change one hypothesis at a time and remeasure duration, throughput, shuffle read/write, spill, task distribution, failure rate, and cost.

Current Databricks guidance favors [liquid clustering](https://docs.databricks.com/aws/en/delta/clustering) and [predictive optimization](https://docs.databricks.com/aws/en/optimizations/predictive-optimization) for suitable Unity Catalog managed tables. Clustering improves data skipping/layout; it does not repair a bad join, tiny-file-producing application, missing filter, or incorrect model.

> **Related item:** Partition count is both parallelism and per-task-size control. Too few partitions create long/large tasks; too many create scheduler and file overhead. The right value comes from measured data size, operators, skew, compute, and target file behavior.

---

## 4. Working with Lakeflow Jobs (16%)

A Lakeflow Job is an orchestration definition; a task is a unit of work; a trigger decides when a run starts. The current [Lakeflow Jobs overview](https://docs.databricks.com/aws/en/jobs) covers time- and event-based triggers and the job/task/trigger model.

### Build a graph with explicit contracts

- Use notebook, Python/script, SQL, pipeline, dashboard, dbt, JAR, or other supported task types according to the workload—not one giant notebook.
- Declare dependencies so independent tasks can run in parallel and dependent tasks cannot race.
- Pass small control values between tasks; persist substantive datasets in governed storage.
- Assign a stable run-as service principal for production and grant only what the graph needs.
- Define parameters, timeout, retry, notification, concurrency, and compute behavior.

Control flow includes retry policies, `Run if` dependency outcomes, if/else branching, and for-each loops. Retries suit transient failures only when the task is idempotent or compensating. A permanent schema or permission error should fail clearly. Cleanup/notification tasks may need `All done` or failure-specific conditions. Review [job control flow](https://docs.databricks.com/aws/en/jobs/control-flow).

### Select a trigger from the freshness contract

- A schedule is simple for predictable periodic processing but may poll when no data changed.
- A file-arrival trigger reduces idle runs for file-driven work; account for arrival batching and event limitations.
- A table-update trigger aligns downstream work with upstream table change; verify supported tables and update semantics.
- Continuous mode suits a continuously operating workload, with different retry/cost behavior.
- A manual/API trigger fits externally coordinated or operator-approved execution.

Separate **event observed**, **run started**, **data complete**, and **consumer published** timestamps. A successful scheduled run can still publish stale or incomplete data.

> **Related item:** Orchestration retry and streaming checkpoint recovery operate at different layers. Restarting a job task should reuse or intentionally replace the correct checkpoint and must not create two writers for the same state or target.

---

## 5. Implementing CI/CD (10%)

### Use Git folders for development, bundles for delivery

Databricks Git folders (formerly Repos) support interactive source-control work: clone, branch, edit, commit, pull, push, and collaborate through the remote provider. Current guidance says Git folders are for interactive development; production CI/CD should use versioned artifacts and workload identity with [Declarative Automation Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) (formerly Databricks Asset Bundles).

A bundle normally contains source plus a `databricks.yml` graph of jobs, pipelines, artifacts, variables, permissions, and targets. Understand:

```text
source + tests + bundle config
-> validate
-> build immutable/versioned artifact
-> deploy as non-human identity to dev target
-> integration test
-> approve/promote same revision to production target
-> observe, reconcile, and roll forward/back by policy
```

- `databricks bundle validate` resolves and checks configuration for a target.
- `databricks bundle deploy` creates or updates declared workspace resources.
- `databricks bundle run` invokes a deployed resource for testing or operation.
- Variables and target overrides hold environment differences; they should not fork business logic.
- State and resource identity prevent every deployment from becoming a disconnected duplicate.

Keep secrets out of Git and bundle files. Authenticate CI with an approved workload identity, constrain its workspace and Unity Catalog permissions, and protect the production branch/environment. Test code, configuration, permissions, resource references, and a real run. See [CI/CD on Databricks](https://docs.databricks.com/aws/en/dev-tools/ci-cd/).

> **Related item:** A pull request proves that a change was reviewed; it does not prove that the deployed artifact came from that commit. Retain commit SHA, artifact version, bundle target, deployment identity, deployment output, resource IDs, and post-deploy test evidence.

---

## 6. Troubleshooting, Monitoring, and Optimization (10%)

### Triage from outside inward

1. Confirm the intended job, parameters, trigger, run-as principal, code revision, target environment, and input freshness.
2. Use run history and the task graph to locate the first failed, blocked, skipped, retried, or unusually slow task.
3. Read the specific error and distinguish startup, library, authentication/authorization, input/schema, application, resource, or downstream-service failure.
4. For Spark execution, inspect the job/stage DAG, task-time distribution, shuffle read/write, spill, skew, failed tasks, executor loss, and driver/executor memory.
5. Compare with a known-good run and the change history.
6. Apply the smallest evidence-supported correction, rerun safely, reconcile outputs, and document prevention.

Do not increase memory reflexively. Driver OOM often comes from `collect`, large result display, broadcast materialization, or metadata/listing. Executor OOM may arise from oversized/skewed partitions or state. A long stage with one straggler suggests skew; uniformly slow tasks suggest I/O, CPU, serialization, or insufficient parallelism. High shuffle and spill point to operator/partition/join choices.

Use the [Spark UI guide](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/) to connect symptoms to stages and tasks. For jobs, preserve run duration, queue/startup, task attempts, output, notifications, and repair history. Monitor application correctness as well as infrastructure: row counts, duplicates, rejected records, freshness, latency, throughput, target version, and consumer SLO.

Optimization has a before/after contract. Record workload, data version/volume, compute, runtime, plan, duration, cost proxy, shuffle/spill, file count/size, and correctness result. Liquid clustering and predictive optimization are table-layout/maintenance tools; they do not eliminate workload-level measurement.

> **Related item:** A green job is an orchestration result, not a data-quality result. A production run can succeed after reading zero files, filtering every row, writing duplicates, or publishing the wrong partition unless those conditions are asserted.

---

## 7. Governance and Security (15%)

### Choose managed versus external lifecycle

| Asset | Databricks/Unity Catalog role | Drop/lifecycle implication |
|---|---|---|
| managed table or volume | governs metadata and underlying data lifecycle at managed storage | dropping removes governed object and data according to platform behavior |
| external table or volume | governs an explicitly registered external path while another owner retains file lifecycle | dropping registration does not normally delete underlying files |

External does not mean ungoverned. Avoid overlapping paths, bypass access through raw cloud credentials, and unclear ownership. Prefer the three-level namespace and stable owner groups.

### Apply privilege hierarchy and separation of duties

Unity Catalog authorization combines ownership and privileges on securables. A reader commonly needs `USE CATALOG`, `USE SCHEMA`, and `SELECT`; writers need the appropriate modification and traversal privileges; creators need the relevant `CREATE` privilege on a parent. Exact privileges depend on the object and action, so use the current [privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/privileges).

```sql
GRANT USE CATALOG ON CATALOG prod_sales TO `grp_sales_readers`;
GRANT USE SCHEMA ON SCHEMA prod_sales.gold TO `grp_sales_readers`;
GRANT SELECT ON TABLE prod_sales.gold.daily_revenue TO `grp_sales_readers`;
```

Grant to account groups and service principals, not individuals. Assign ownership to durable groups. `GRANT`, `REVOKE`, and where supported `DENY` have different semantics; check the applicable hierarchy and privilege model rather than assuming a cloud-IAM rule maps directly. Validate with a positive test and a negative test from the actual user or workload identity.

### Select the fine-grained control

- A **dynamic view** can join, reshape, filter, or mask through query logic and is useful as a curated interface.
- A table **row filter** returns whether each row is visible; a **column mask** returns the visible value for a column. These are table-specific controls.
- **ABAC** attaches centrally managed policies to governed tags and is recommended by current Databricks guidance for consistent controls across many tables.

The [Unity Catalog access-control overview](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/) explains how privileges, ABAC, table controls, and workspace bindings complement one another. Current [row-filter and column-mask guidance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/) includes runtime, operation, sharing, API, time-travel, clone, and performance limitations. Treat ABAC and fine-grained controls as volatile: verify runtime support and restrictions before relying on them.

Separate policy author, tag steward, data owner, platform admin, and workload identity where risk requires it. Protect policy UDFs and governed tags, log administrative changes, and test direct table access, view access, each persona, null/unexpected values, and write paths.

> **Related item:** Fine-grained controls do not protect a copy exported to an ungoverned location. Combine least privilege, storage isolation, egress controls, lineage/audit, retention, and downstream handling with row/column policy.

---

## Integrated scenarios

### Scenario 1: governed incremental orders

Files arrive out of order in cloud storage and occasionally add a field. Use an external volume and Auto Loader with a durable checkpoint and schema location. Preserve bronze provenance and rescued data. In silver, cast types, reject missing keys, deduplicate by order ID plus source update time, and reconcile accepted/rejected counts. Publish a gold daily aggregate. Orchestrate quality and publish tasks so gold cannot run after a failed validation. Grant the ETL principal write access and analysts read access only to gold. A valid answer connects file discovery, schema evolution, replay, business deduplication, task dependencies, grants, and evidence.

### Scenario 2: reusable multi-environment pipeline

Develop code in a Git folder on a feature branch. Package the transformation, tests, job, permissions, and target variables in a Declarative Automation Bundle. CI validates and tests, builds a versioned artifact, deploys to development using workload identity, runs integration/replay/negative-access tests, then promotes the same revision to production after approval. Do not put secrets or environment-specific business logic in Git. Retain commit, artifact, deploy and run evidence.

### Scenario 3: slow and unsafe consumer table

A job is green but late; one Spark task runs much longer, the target has duplicates, and analysts can see sensitive columns. Stop treating this as one “performance” issue. Use the Spark UI to prove skew, define a deterministic duplicate winner, revalidate the consumer grain, then measure a join/repartition correction. Apply least-privilege gold access plus a suitable mask or ABAC policy, including negative tests and runtime checks. Reconcile correctness before claiming the optimization succeeded.

## Hands-on labs

1. **Platform and compute:** Run the same bounded SQL/DataFrame workload on two eligible compute options. Record startup, duration, execution evidence, isolation, supported features, and cost considerations; justify the choice.
2. **`COPY INTO`:** Load a small file set twice, prove normal idempotent behavior, add one file, validate the increment, and test a malformed-record path.
3. **Auto Loader:** Ingest JSON with checkpoint/schema state, add a column and a malformed record, inspect rescued/quarantined data, restart, and prove no accidental duplicate business effects.
4. **Silver and gold:** Parse nested JSON, explode one array at a defined grain, join a reference table, deduplicate deterministically, validate quality, and publish one table plus one view or materialized view with a written rationale.
5. **Lakeflow Job:** Build a DAG with parallel preparation, conditional validation, publish, and failure notification/cleanup. Test retryable and permanent failures and inspect run history.
6. **Bundle delivery:** Put a job and its code into a bundle with development/production targets. Validate and deploy to a safe environment, run a smoke test, and record resource identity and revision.
7. **Evidence-led tuning:** Introduce a skewed join, locate the straggler/shuffle in Spark UI, make one supported correction, and compare correctness, duration, shuffle/spill, and task distribution.
8. **Unity Catalog security:** Create managed and external test assets, grant through groups, test `GRANT`/`REVOKE`, add a row filter or column mask where supported, perform positive/negative tests, then clean up without deleting unintended external data.

## Readiness checklist

- [ ] I can trace identity, compute, Unity Catalog, Delta Lake, and cloud storage for a query.
- [ ] I can choose compute from workload, runtime, library, isolation, startup, and cost needs.
- [ ] I can distinguish `COPY INTO`, Auto Loader, Lakeflow Connect, client extraction, and local upload.
- [ ] I can explain where ingestion/checkpoint/schema state lives and how it is recovered.
- [ ] I can handle schema inference, enforcement, evolution, rescue, and malformed records deliberately.
- [ ] I can design for out-of-order, duplicate, late, missing, and replayed input.
- [ ] I can parse nested JSON and define output grain before exploding arrays.
- [ ] I can explain bronze, silver, and gold responsibilities as contracts.
- [ ] I can implement casts, null handling, filters, columns, aggregations, and summaries in PySpark/SQL.
- [ ] I can predict inner, left, cross, broadcast, and union consequences.
- [ ] I can write a deterministic business deduplication rule.
- [ ] I can validate counts, keys, types, ranges, references, freshness, and rejected rows.
- [ ] I can choose table, view, materialized view, or streaming table from lifecycle and latency.
- [ ] I can explain lazy evaluation and locate the action that starts execution.
- [ ] I can interpret shuffle partitions, parallelism, broadcast threshold, and memory settings as hypotheses.
- [ ] I can distinguish liquid clustering/predictive optimization from query-plan correction.
- [ ] I can model a Lakeflow Job as jobs, tasks, dependencies, and triggers.
- [ ] I can choose schedule, file-arrival, table-update, continuous, or external triggering.
- [ ] I can design retry, conditional branch, loop, cleanup, timeout, and notification behavior.
- [ ] I can distinguish a successful run from complete and correct published data.
- [ ] I can use Git folders for interactive source-control collaboration.
- [ ] I can describe bundle source, variables, targets, resources, artifacts, permissions, and state.
- [ ] I can validate, deploy, and run a bundle with a non-human CI identity.
- [ ] I can prove the deployed revision rather than infer it from a merged branch.
- [ ] I can use job history to locate the first failed or delayed task.
- [ ] I can classify startup, dependency, identity, data, application, resource, and downstream failure.
- [ ] I can use Spark UI to identify skew, shuffle, spill, executor loss, and driver pressure.
- [ ] I can measure an optimization without sacrificing correctness.
- [ ] I can distinguish managed and external data lifecycle.
- [ ] I can apply catalog/schema/object traversal and action privileges through groups.
- [ ] I can distinguish workspace/resource permission from data permission.
- [ ] I can choose a dynamic view, table filter/mask, or ABAC policy.
- [ ] I can state why fine-grained-control runtime and operation limitations must be rechecked.
- [ ] I can run positive and negative authorization tests as the real principal.
- [ ] I can solve the three integrated scenarios without relying on product-name recognition alone.
- [ ] I will recheck the live page and linked official PDF shortly before the exam.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Pick one primary explanation route, use the official objectives as the gap list, build the labs, and add a practice source only for diagnosis. Times below are provider-listed where the page exposes them; otherwise they are clearly labeled planning estimates. Commercial content can lag the May 2026 blueprint, especially where it still says Repos, Delta Live Tables, or Asset Bundles without the current Git folders, Lakeflow Spark Declarative Pipelines, or Declarative Automation Bundles names.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page](https://www.databricks.com/learn/certification/data-engineer-associate) and [May 4, 2026 exam guide](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf) | Public | 1–2 hr to map objectives and recheck details |
| Six self-paced courses named in the official PDF through [Databricks Academy](https://customer-academy.databricks.com/) | Free account or customer/partner Academy entitlement; catalog visibility varies | 18–30 hr planning estimate including labs; vendor does not expose a stable public total |
| [Get Started with Databricks for Data Engineering](https://customer-academy.databricks.com/learn/courses/2469/get-started-with-databricks-for-data-engineering/lessons) | Free account; current hands-on onboarding | 4–8 hr planning estimate for demos/labs; no reliable public duration displayed |
| [Databricks Free Edition](https://www.databricks.com/learn/free-edition) plus the eight labs in this guide | Free account; product limits apply | 12–24 hr |
| [Databricks documentation](https://docs.databricks.com/aws/en/introduction/) | Public; select only objective gaps | 8–20 hr selected reading and implementation |
| [Databricks Certified Data Engineer Associate Study Guide](https://www.oreilly.com/library/view/databricks-certified-data/9781098166823/) by Derar Alhussein | O’Reilly subscription or purchase; February 2025 baseline | 9 hr 49 min provider estimate; allow 15–25 hr with labs and May 2026 gap check |
| [O’Reilly Databricks Data Engineer Associate Certification Prep in 2 Weeks](https://www.oreilly.com/live-events/databricks-data-engineer-associate-certification-prep-in-2-weeks/0636920093415/) | O’Reilly subscription/live-event availability | 16 hr provider duration across four sessions; verify current dates and start/end times |
| [Pluralsight certification path](https://www.pluralsight.com/paths/databricks-certified-data-engineer-associate) | Subscription; path actively being produced | 43 min published now plus practice exam; seven-domain path incomplete on September 1, 2026 |
| [Udemy preparation course by Derar Alhussein](https://www.udemy.com/course/databricks-certified-data-engineer-associate/) | Paid; updated August 2026 for May 2026 version | 6 hr 4 min video; allow 12–20 hr with exercises |
| [LinkedIn Learning cert prep](https://www.linkedin.com/learning/databricks-certified-data-engineer-associate-cert-prep) | Subscription; released March 2025 | 2 hr 18 min; use as review and gap-check renamed/new May 2026 topics |
| [Whizlabs certification training and practice](https://www.whizlabs.com/databricks-certified-data-engineer-associate/) | Paid; verify current blueprint, question count, labs, and displayed durations after sign-in | 6–15 hr planning estimate; provider page did not expose stable public totals |
| Official sample questions inside the exam-guide PDF | Public; original vendor examples | 30–60 min plus remediation; do not memorize or redistribute |
| [Databricks YouTube channel](https://www.youtube.com/@Databricks) | Public; select current product sessions | 2–6 hr selected viewing, then reproduce the demonstrations |

No exact current MeasureUp product was independently verified. Avoid products claiming real, leaked, recalled, or guaranteed exam questions. Practice should test reasoning against documentation and hands-on behavior, not reproduce protected exam content.

## Final review routine

1. Reopen the official page and its linked PDF; compare title, weights, effective date, question/language/delivery details, and any change notice with this page.
2. Mark every detailed PDF bullet `explain`, `implement`, `diagnose`, or `recheck`; close only the marked gaps.
3. Complete at least one ingestion-to-gold build, one bundle deployment, one Spark diagnosis, and one negative-permission test from a fresh environment.
4. Take one ethical assessment, classify misses by objective and decision error, and return to documentation/labs.
5. Stop collecting resources when you can explain the mechanism, choose among alternatives, implement safely, and prove the result.
