---
exam_code: DP-700
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# DP-700 Implementing Data Engineering Solutions Using Microsoft Fabric Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 21, 2026 objectives and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dp-700-coverage-record). The [official DP-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700) is authoritative.

**Current baseline:** Skills measured as of July 21, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Official source:** [DP-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700)

## How to use this guide

DP-700 is an implementation exam. Knowing Fabric item names is not enough. For every design, trace a complete operating contract:

1. source volume, velocity, schema behavior, latency and retention;
2. full, incremental, change-data-capture or streaming load pattern;
3. lakehouse, warehouse, Eventhouse, shortcut or mirrored destination;
4. Dataflow Gen2, pipeline, notebook, Spark, SQL or KQL responsibility;
5. grain, keys, duplicates, missing data, late data and reconciliation;
6. identity, workspace/item/data permissions, governance and audit evidence;
7. schedule/event trigger, parameterization, dependency, retry and idempotency;
8. monitoring signal, likely failure boundary, performance hypothesis and rollback.

Build one end-to-end solution and keep an evidence notebook: configuration screenshots, code, run IDs, row-count checks, security tests and before/after performance measurements. The [official credential page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/) lists a 100-minute exam and expects practical SQL, PySpark and KQL skill.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Implement and manage an analytics solution | 30–35% | Can the platform be configured, secured, versioned, deployed and orchestrated repeatably? |
| Ingest and transform data | 30–35% | Can batch and streaming data reach the correct store at a trustworthy grain and freshness? |
| Monitor and optimize an analytics solution | 30–35% | Can failures and bottlenecks be isolated with evidence and corrected at the right layer? |

---

## 1. Implement and manage an analytics solution

### Configure workspace settings

A workspace is both a collaboration boundary and a configuration/deployment boundary. Before changing a setting, identify whether it belongs at tenant, capacity, domain, workspace, item, Spark environment or data level; similar labels do not make those scopes interchangeable.

#### Spark workspace settings

Set the default Spark pool and environment from workload evidence. Pool size, node family, autoscale bounds, dynamic allocation, executor settings and runtime/library versions affect startup time, concurrency, cost and reproducibility. An environment can centralize libraries and Spark properties; pin dependencies and promote them with code so a notebook does not work only in one developer's session.

Use starter pools for fast interactive work when their shared defaults fit. Use custom pools when isolation, node type, autoscale or library/runtime control justifies the operational cost. Do not make a large pool the first performance fix: inspect partition count, shuffle, skew, file size, cache use and query plan first.

#### Domains and OneLake

Domains organize distributed ownership and discovery. Define domain/subdomain ownership, assign workspaces deliberately and delegate only the necessary administration. A domain is not automatically a security boundary: test the workspace, item and data permissions that enforce access.

OneLake workspace settings affect how the workspace participates in the tenant-wide logical data lake. Establish storage ownership, data residency, shortcut policy, schema/retention conventions and who can expose or consume data. The current [OneLake security overview](https://learn.microsoft.com/en-us/fabric/onelake/security/get-started-security) separates control-plane actions from data-plane access; prove both.

#### Apache Airflow workspace settings

Fabric data workflows provide managed Apache Airflow orchestration under current availability. Configure the workspace/runtime, dependencies, credentials/connections, variables, schedules and access from an explicit DAG contract. Airflow is valuable for Python-defined cross-system dependencies; Fabric pipelines are often simpler for native visual orchestration. Do not place secrets in DAG source, and make tasks retry-safe.

> **Related item:** A workspace connected to Git can still contain runtime-only configuration, connections and credentials. Maintain a deployment manifest that identifies what source control covers and what must be recreated or bound per environment.

### Implement lifecycle management

[Fabric CI/CD](https://learn.microsoft.com/en-us/fabric/cicd/cicd-overview) combines Git integration, deployment pipelines, APIs and environment-specific configuration. Choose one authoritative flow for each item:

| Mechanism | Primary job | Evidence to retain |
|---|---|---|
| Git integration | Version supported workspace item definitions and collaborate through branches | commit, diff, supported-item check and sync result |
| Database project | Develop/build/deploy warehouse schema as code | successful build, schema comparison, migration risk and deployment result |
| Deployment pipeline | Promote supported items across dev/test/prod stages | comparison, rules/bindings, approval, post-deployment tests and rollback |
| Fabric APIs/CLI | Automate item and job operations | versioned request, identity, response/run ID and idempotency behavior |

Connect the intended repository, branch and folder. Before syncing, check whether every item and property is supported; ignored or preview items can make a workspace-to-Git comparison incomplete. Resolve conflicts consciously—switching branches or updating a workspace can overwrite workspace state.

For a warehouse, the database project represents schemas and database objects. Build it locally, detect unsupported objects and review destructive schema changes. A successful project build validates the definition, not the production data or consumer compatibility.

Configure deployment stages, item pairing, deployment rules, variable values, data-source bindings and permissions. After promotion, test connections, credentials, job schedules, security, a representative query and downstream consumers. Retain a versioned rollback path.

> **Related item:** DevOps quality is not the presence of a Git icon. A release is trustworthy only when the definition, environment configuration, data checks, permissions and consumer behavior are all tested.

### Configure security and governance

Security is layered and endpoint-specific:

| Layer | Typical control | What it governs |
|---|---|---|
| Workspace | Admin, Member, Contributor, Viewer | broad ability to create, manage or consume workspace content |
| Item | share/read/build or item-specific permission | use of one lakehouse, warehouse, pipeline, notebook, Eventhouse or other item |
| SQL/data object | SQL grants, RLS, CLS/OLS, masking | schemas, objects, rows, columns and displayed values through that endpoint |
| OneLake/file | OneLake roles and folder/table access | direct data-plane access through OneLake-compatible paths |
| Source/shortcut | source permission plus shortcut behavior | whether referenced data is actually accessible to the consumer |

Grant the least privilege that supports the job and test with a real restricted identity through every consumption path. RLS filters rows; CLS/OLS restrict columns or objects; folder/file controls protect direct lake access. Dynamic data masking changes returned presentation for users without `UNMASK`; it is not encryption and is not a substitute for denying access.

Apply sensitivity labels under the organization's information-protection policy. Use promoted/certified endorsement to signal stewardship and trust; endorsement neither grants permission nor proves that data is correct. Record owner, definition, freshness, quality SLA and lineage.

Microsoft Fabric audit events support investigation and compliance evidence. Define which control requires which event, retention, alert and responder. Correlate audit identity/action with Fabric job logs and source-system evidence instead of treating a single portal view as a complete audit trail.

OneLake security roles can grant granular data access independent of broad workspace collaboration. Test inheritance, default access, shortcut behavior and the exact engine endpoint. **VERIFY CURRENT:** OneLake security coverage and endpoint behavior are evolving quickly.

> **Related item:** A user blocked by warehouse RLS might still have file-level access to the underlying lake data. Access tests must cover SQL, Spark, OneLake and downstream semantic-model/export paths that exist in the architecture.

### Orchestrate processes

The [Fabric ingestion decision guide](https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-pipeline-dataflow-spark) helps separate tool responsibilities:

| Tool | Strong fit | Operational concern |
|---|---|---|
| Dataflow Gen2 | low-code Power Query ingestion, shaping and profiling | folding, staging/destination behavior, schema drift and refresh diagnostics |
| Pipeline | movement plus multi-step visual control flow across activities | dependencies, parameters, retries, timeouts, concurrency and rerun behavior |
| Notebook | code-first Spark/SQL/Python transformation and reusable libraries | environment/runtime, session startup, logging, tests and idempotency |
| Airflow workflow | Python DAGs and broader dependency/orchestration patterns | dependency packages, connections, scheduler behavior and task retry safety |

Choose schedules for time-based commitments and event triggers when an observable event should start work. Account for time zones, daylight saving, overlapping runs, upstream lateness, duplicate events and missed events. An event trigger does not remove the need for reconciliation.

Parameterize workspace/item IDs, paths, dates, watermarks and destinations rather than cloning logic per environment. Dynamic expressions commonly read pipeline parameters, variables, activity output and system values. Validate types and escaping; log resolved nonsecret values so a failed run can be reproduced.

Build explicit dependencies and terminal states: success, expected empty input, retryable failure, quarantined data and unrecoverable failure. Use retries only for transient faults, exponential backoff where supported and a maximum attempt count. Make writes idempotent through merge/upsert, partition replacement, checkpoint or run-control design.

---

## 2. Ingest and transform data

### Design loading patterns

#### Full and incremental loads

A full load is simplest when data is small, refresh windows are generous and replacement is safe. It becomes wasteful or risky as history, volume and source load grow. An incremental design needs a change contract:

- source change signal: modification timestamp, increasing key, CDC log, change version or file arrival;
- durable high-water mark/checkpoint stored only after the destination commit succeeds;
- overlap/lookback window for clock skew and late updates;
- business key plus deterministic insert/update/delete handling;
- recovery plan for expired logs, missed files or a corrupt checkpoint;
- reconciliation of source and destination counts, totals and exceptions.

Never advance the watermark before all intended writes commit. Make rerunning a window safe. If the source can update a row without changing the selected timestamp, the incremental contract is invalid even when every run is green.

#### Prepare a dimensional load

State the fact grain in one sentence before joining. Use stable business keys for matching and surrogate keys where source keys change or historical dimension versions are required. Load dimensions before dependent facts, use an unknown member or quarantine policy, and define slowly changing dimension behavior by attribute.

SCD Type 1 overwrites history; Type 2 creates effective-dated versions and preserves history. Late-arriving dimensions may require an inferred member followed by repair. Late facts must resolve to the dimension version valid at event time, not necessarily the current version.

#### Streaming loads

Define event time versus processing time, acceptable latency, ordering scope, duplicate identity, lateness allowance, window type, state retention, checkpoint and replay boundary. Exactly-once marketing language is not enough: prove end-to-end behavior across source, processor and sink. Prefer idempotent destinations and retained raw events.

> **Related item:** Medallion architecture is useful when Bronze preserves replayable source evidence, Silver applies trustworthy conformance and Gold exposes consumer-ready grain. The names do not guarantee quality; define the contract and owner for each layer.

### Ingest and transform batch data

#### Choose a data store and access pattern

| Option | Strong fit | Important trade-off |
|---|---|---|
| Lakehouse | Delta/Parquet, Spark engineering, open-file interoperability and SQL read access | file/partition maintenance and SQL-endpoint synchronization behavior |
| Warehouse | governed relational analytics, dimensional models and supported transactional T-SQL | relational design, distribution/compute pressure and ingestion concurrency |
| Eventhouse | high-volume event/time-series data and low-latency KQL analytics | ingestion mapping, hot-cache/retention policy and KQL operating skill |
| Shortcut | reference internal/external data without owning another managed copy | source availability/security/performance/schema dependency |
| Mirroring | continuously replicate supported operational data into OneLake with low pipeline management | connector support, latency, source impact, conflict/retention and feature limits |

Use a shortcut when shared ownership and freshness outweigh dependency; copy when you need an owned snapshot, transformation boundary, isolation, independent retention or predictable performance. Use mirroring when a supported source and continuous replication fit better than custom CDC. Document movement, egress, region, deletion and schema-change behavior.

#### Select the transformation engine

Dataflows Gen2 use Power Query for accessible low-code shaping; preserve query folding when it safely moves work to a capable source. Notebooks and Spark scale code-first transformations, libraries and Delta operations. T-SQL fits set-based warehouse transformations. KQL fits event/time-series manipulation. Choose from data location, scale, language, transaction semantics, team ownership and operations—not preference alone.

Practice the same fundamental operations in SQL, PySpark and KQL: filter/project, type conversion, joins, conditional derivation, grouping, windowing and deduplication. Know their null semantics, case behavior and time functions; syntactic resemblance does not imply identical results.

#### Shortcuts, mirroring and pipelines

A OneLake shortcut is metadata that points to data. Validate supported source/format, credential and network model, data residency, caching, source deletion/rename, schema drift and consumer permissions. For an Eventhouse, a standard shortcut reads an external Delta table; [query acceleration](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/query-acceleration-overview) caches a policy-defined window to improve supported query performance at additional capacity/storage cost.

Mirroring owns a replication relationship. Confirm initial snapshot, incremental latency, supported tables/types/DDL, authentication, network access, pause/restart, monitoring and source removal behavior. Do not describe mirroring as universal zero-copy or zero-operations.

In a pipeline, separate extract, stage, validate, transform and publish. Capture source/destination row counts, bytes, duration, watermark and rejected rows. Use parameters and metadata-driven loops carefully; bound concurrency to avoid overwhelming sources or capacity.

#### Shape trustworthy data

Profile before modifying. Establish expected types, uniqueness, null rate, range, referential integrity and volume. Standardize time zones and code values while preserving raw evidence. For duplicates, define the duplicate key and deterministic survivor—latest timestamp alone is unsafe when timestamps tie.

Denormalization can reduce read-time joins but duplicates attributes and creates update responsibility. Grouping and aggregation change grain irreversibly unless detail is retained elsewhere. Reconcile after every join and before every aggregate; accidental many-to-many expansion creates plausible but wrong totals.

Handle missing data by business meaning: unknown, not applicable, not yet received and extraction failure are different states. Quarantine or flag records when imputation would fabricate meaning. Track late data and repair affected dimensions, facts, aggregates and watermarks.

### Ingest and transform streaming data

#### Choose the streaming engine

| Engine | Strong fit | State/evidence to inspect |
|---|---|---|
| Eventstream | visual ingestion, transformation and routing among supported real-time sources/destinations | source/destination activation, event counts, transformation errors and lag |
| Spark Structured Streaming | code-first distributed stream processing with complex state/transformation | checkpoint, batch ID, input rate, processing rate, state and sink commits |
| Eventhouse/KQL | ingestion plus low-latency event/time-series storage and analysis | ingestion failures, extents, cache/retention, query statistics and schema mappings |

Use Eventstream for supported low-code routing/filtering/aggregation, Structured Streaming for code-defined stateful pipelines and Eventhouse/KQL for query-centric real-time analytics. Combining them is normal; document which component owns parsing, deduplication, windowing and persistence.

#### Native Eventhouse table versus OneLake shortcut

Native ingestion creates Eventhouse-managed tables with indexing, retention, caching, update policies and materialized-view capabilities. A standard OneLake shortcut avoids another full managed copy but queries external Delta files and can be slower. Query acceleration caches a chosen window and approaches native-query performance for supported shortcut data but has limitations and cost. Select from latency, feature, freshness, duplication, residency and operational requirements.

#### Windows and late events

Tumbling windows are fixed and nonoverlapping; hopping windows are fixed but overlap at a hop; sliding/session behavior follows activity or evaluation semantics under the chosen engine. Choose event-time windows when the business question follows occurrence time, and define watermark/lateness behavior. A window result can change when late data arrives; decide whether to update, retract, quarantine or ignore it.

Use KQL operators such as `where`, `project`, `extend`, `summarize`, `bin` and joins for event analysis. In Structured Streaming, define schema, watermark, stateful aggregation, checkpoint and an idempotent sink. Retain a replay boundary so bad code can be corrected without losing source truth.

> **Related item:** Streaming dashboards measure current behavior, while durable lake/warehouse layers support reconciled history. An enterprise design often needs both a fast provisional view and a later authoritative result.

---

## 3. Monitor and optimize an analytics solution

### Monitor Fabric items

The [monitoring hub](https://learn.microsoft.com/en-us/fabric/admin/monitoring-hub) provides cross-item run status and history for items the operator can access. [Workspace monitoring](https://learn.microsoft.com/en-us/fabric/data-factory/workspace-monitoring) adds queryable log-level evidence in a monitoring Eventhouse for supported items. Build a layered view:

1. business SLA: freshness, completeness and trusted publishing time;
2. orchestrator: trigger, dependency, retry and terminal state;
3. movement/transformation: rows/bytes, watermark, reject count and duration;
4. engine: Spark stages/shuffle, SQL query/capacity, KQL ingestion/cache/query;
5. platform: capacity pressure, throttling, service health and permissions;
6. consumer: semantic-model refresh and downstream query/report behavior.

Monitor ingestion and transformation separately—a copy can succeed while transformation publishes nothing. For semantic-model refresh, record start/end/status, partition, gateway/source and failure detail. Configure alerts for actionable thresholds with owner, severity, deduplication, route and runbook. Alerting on every failed retry creates noise; alert when the condition requires human action or threatens an SLA.

### Identify and resolve errors

Troubleshoot from the failing boundary outward. Preserve the run ID, time, identity, parameters, source/destination, error detail and last successful evidence before rerunning.

| Item | Common fault classes | First evidence |
|---|---|---|
| Pipeline | connection/authentication, parameter/expression, timeout, throttling, source/sink schema, activity dependency | activity input/output, resolved parameters, copy metrics and inner error |
| Dataflow Gen2 | credentials/privacy, gateway, folding, type conversion, destination/staging, schema drift | refresh history, query step and destination details |
| Notebook/Spark | environment/library, session capacity, driver/executor memory, skew/shuffle, path/permission, code/data | Spark application, cell/driver logs, stage plan and input partition |
| Eventhouse/KQL | ingestion mapping/schema, permission, malformed events, throttling, retention/cache/query | ingestion failures, table/schema, command/query diagnostics and monitoring tables |
| Eventstream | source connectivity, serialization, transform, destination activation/routing, throughput | topology, event preview/metrics, source and destination logs |
| T-SQL | syntax/object, permission, data type/constraint, transaction/concurrency, resource pressure | exact query/error, query plan/insights, blocking and pool pressure |
| OneLake shortcut | credential/token, source rename/delete, permission, unsupported format/Delta feature, region/network | shortcut status, source access with same identity, schema and synchronization state |

Change one hypothesis at a time. A blind rerun can erase evidence, duplicate writes or advance a bad watermark. After remediation, replay the same input, reconcile the output and demonstrate that monitoring now detects the condition.

> **Related item:** A 403 can originate from workspace, item, data, shortcut-source, storage credential or network scope. The error code alone does not identify the control plane that denied access.

### Optimize performance

Optimization starts with a measured bottleneck and a correctness baseline.

#### Lakehouse tables

Reduce many small files, compact with supported table maintenance/`OPTIMIZE`, use V-Order where it benefits Fabric readers, partition by selective and sustainable access patterns and remove obsolete files only after retention/recovery requirements. Overpartitioning creates tiny files and metadata overhead; a very high-cardinality partition key is rarely useful. Verify improvement through bytes/files scanned, runtime and concurrent workload—not file count alone.

#### Pipelines

Push filters/projections to the source when safe, use incremental movement, appropriate copy parallelism and staged bulk loads. Remove unnecessary serial dependencies but cap concurrency to protect source and capacity. Reuse connections and avoid expensive per-row activities. Measure queue time, transfer throughput, source read, sink write and downstream transform independently.

#### Warehouse and query performance

Use [Query Insights](https://learn.microsoft.com/en-us/fabric/data-warehouse/query-insights) and execution evidence to find long-running/frequent/high-resource queries and pool pressure. Select only required columns/rows, use sound star schemas and data types, avoid avoidable data movement and row-by-row logic, update design/queries from the plan, and test with representative volume/concurrency. Scaling capacity can be valid after query/data design is sound; it is not a substitute for diagnosis.

#### Spark

Inspect the physical plan and Spark UI. Address skewed keys, excessive shuffle, wrong partition count, nonselective scans, many small files, repeated computation and driver collection. Prefer built-in expressions over slow user-defined functions when possible, broadcast genuinely small dimensions, cache only reused data that fits, and tune pool/executor resources after code/data-layout issues.

#### Eventstreams and Eventhouses

For Eventstream, minimize unnecessary transforms/routes, match throughput, observe lag and avoid activating ingestion before the complete route is ready. For Eventhouse, align ingestion batching/mapping, retention and hot cache with workload; use materialized views/update policies appropriately for native tables and optimize KQL filters, projections, joins and time bounds. [Eventhouse monitoring](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/monitor-eventhouse) exposes queryable usage and performance evidence.

For shortcut queries, choose standard access, query acceleration or native ingestion from measured latency, freshness, feature and cost needs. Acceleration does not add native-table update policies/materialized views to the external table.

#### Query optimization across languages

In SQL, inspect plans, scans, joins, predicates, spills and concurrency. In Spark, inspect stages, exchange/shuffle, skew and partitions. In KQL, filter early, reduce columns, constrain time, choose join strategy and materialize/preaggregate only when reuse justifies it. Preserve result equivalence and security behavior in every before/after test.

---

## Integrated scenarios

### Scenario 1 — Incremental retail platform

Mirror a supported operational source or ingest CDC to Bronze, maintain a durable watermark and merge conformed dimensions/facts in a lakehouse or warehouse. Orchestrate with parameters, deploy through Git and stages, and secure finance columns/regions through the actual endpoints. Prove rerun safety, delete/late-update behavior, counts/totals and freshness alerts.

### Scenario 2 — Real-time equipment telemetry

Route telemetry with Eventstream, retain replayable raw events, transform with Eventstream/KQL or Structured Streaming, and serve recent analysis from Eventhouse. Join governed reference data through a native table or OneLake shortcut; measure standard versus accelerated query behavior. Prove duplicate, out-of-order, late-window and destination-startup behavior.

### Scenario 3 — Slow and unreliable nightly load

Trace monitoring from trigger through copy, notebook/Spark, warehouse query and semantic refresh. Separate queue time, movement, shuffle/skew, write and query pressure. Fix the measured boundary, replay the same partition, reconcile output and demonstrate that an actionable alert catches a deliberately recreated failure.

---

## Hands-on labs

### Lab 1 — Workspace and security matrix

Configure Spark/environment, domain/OneLake settings and restricted test identities. Query through SQL, Spark and OneLake paths. **Evidence:** configuration manifest and allow/deny matrix.

### Lab 2 — Git, database project and deployment

Version supported Fabric items, build a warehouse database project and promote through dev/test/prod with environment bindings. **Evidence:** diff, build, deployment, post-release checks and rollback.

### Lab 3 — Parameterized orchestration

Build a metadata-driven pipeline that calls a notebook, uses dynamic expressions, handles dependencies/retries and supports schedule plus event execution. **Evidence:** resolved parameter log, run graph and safe rerun.

### Lab 4 — Incremental dimensional load

Implement high-water mark/overlap, SCD behavior, duplicate/missing/late rules and fact-dimension reconciliation. **Evidence:** initial, incremental, replay and late-arrival results.

### Lab 5 — Batch-engine comparison

Transform one representative dataset with two of Dataflow Gen2, PySpark, T-SQL or KQL. **Evidence:** code/steps, result equivalence, runtime and operating trade-off.

### Lab 6 — Streaming and windowing

Ingest events through Eventstream or Structured Streaming, apply a time window and persist/query in Eventhouse. Inject duplicates and late events. **Evidence:** checkpoint/replay contract and expected window corrections.

### Lab 7 — Monitoring and fault injection

Capture pipeline, dataflow/notebook, Eventhouse/Eventstream, T-SQL, shortcut and semantic-refresh signals. Deliberately break credentials, schema or path. **Evidence:** run ID, alert, root cause, remediation and reconciliation.

### Lab 8 — Performance experiment

Measure and tune a lakehouse table, Spark job, warehouse query and Eventhouse/shortcut query without changing results. **Evidence:** hypothesis, plan/metrics, before/after measurements and cost/correctness note.

---

## Knowledge checks

1. **Workspace setting versus tenant setting?** Workspace affects that collaboration/deployment boundary; tenant policy governs broader organizational availability and delegation.
2. **Starter versus custom Spark pool?** Fast shared startup/defaults versus controlled node/autoscale/runtime needs.
3. **Why pin an environment?** Reproducible libraries/runtime/properties across users and stages.
4. **Is a domain a security boundary?** Not by itself; prove workspace, item and data permissions.
5. **Airflow versus pipeline?** Python DAG/cross-system dependency control versus Fabric-native visual orchestration.
6. **Git sync proves deployability?** No; supported definitions, environment bindings, data, jobs and security need tests.
7. **Database-project value?** Versioned, buildable warehouse schema and controlled schema comparison/deployment.
8. **RLS versus masking?** Row denial/filtering versus changed displayed value for users without unmask rights.
9. **Why test every endpoint?** A control at SQL or semantic-model level may not govern direct OneLake/Spark access.
10. **Sensitivity label versus endorsement?** Classification/protection metadata versus trust/stewardship signal; neither grants access.
11. **What makes an audit useful?** Defined event, identity, retention, correlation, alert and responder.
12. **Dataflow versus notebook?** Low-code Power Query shaping versus code-first distributed transformation.
13. **Schedule versus event trigger?** Time commitment versus observable event; both need duplicate/missed-run handling.
14. **Idempotent orchestration?** Replaying the same logical input produces the intended state without duplicate corruption.
15. **When advance a watermark?** Only after all intended destination work commits and validation succeeds.
16. **Why an overlap window?** Capture late updates/clock skew, paired with deterministic deduplication.
17. **Fact grain?** The exact business meaning of one fact row; define before keys, joins or aggregates.
18. **SCD Type 1 versus Type 2?** Overwrite current value versus add effective-dated history.
19. **Event time versus processing time?** When business event occurred versus when engine processed it.
20. **Lakehouse versus warehouse?** Open Delta/Spark engineering plus SQL read patterns versus relational T-SQL analytics/transactions.
21. **Shortcut versus copy?** Reference source data/dependency versus own an independent stored snapshot.
22. **Mirroring versus custom incremental pipeline?** Managed continuous replication for supported sources versus explicit extraction/transformation/control.
23. **Why preserve raw events?** Replay, audit and correction after processing defects.
24. **Query folding value?** Push supported work to a capable source and reduce transferred/local work.
25. **Duplicate rule requirement?** Explicit key and deterministic survivor, including timestamp ties.
26. **Tumbling versus hopping window?** Fixed nonoverlapping periods versus overlapping fixed windows at a hop interval.
27. **Native Eventhouse table versus shortcut?** Managed ingestion/index/cache/retention features versus external Delta access without full managed copy.
28. **Query acceleration purpose?** Cache a policy-defined shortcut window for faster supported Eventhouse queries at cost/limitations.
29. **Monitoring hub versus workspace monitoring?** Cross-item run view versus queryable workspace log evidence for supported items.
30. **Why not blind-rerun?** It can erase evidence, duplicate writes or corrupt a watermark.
31. **Pipeline success proves good data?** No; reconcile grain, counts, totals, rejects, freshness and consumer result.
32. **Small-file problem?** Excessive metadata/open cost and inefficient scans; compact with a measured maintenance policy.
33. **Spark tuning first step?** Inspect plan/UI, data layout, shuffle/skew and partitions before enlarging compute.
34. **Warehouse tuning evidence?** Representative query plan/insights, resource pressure, volume and concurrency.
35. **Alert-quality test?** It is actionable, owned, routed, deduplicated and tied to an SLA/runbook.
36. **What proves optimization?** Same correct/secure result with measured improvement under representative load and an understood cost trade-off.

---

## Places to learn

This is a curated starting point, **not a complete list**, and it is not meant to be consumed in full. Pick one primary route, build a complete Fabric solution, then add documentation, videos or practice questions only for measured gaps. Reconcile older courses with the July 21, 2026 blueprint, especially Airflow workspace settings, OneLake security, query acceleration, current Git/database-project behavior and Fabric monitoring.

The five official paths are [ingest data](https://learn.microsoft.com/en-us/training/paths/ingest-data-with-microsoft-fabric/) (4h49), [lakehouse](https://learn.microsoft.com/en-us/training/paths/implement-lakehouse-microsoft-fabric/) (7h21), [Real-Time Intelligence](https://learn.microsoft.com/en-us/training/paths/explore-real-time-analytics-microsoft-fabric/) (5h31), [data warehouse](https://learn.microsoft.com/en-us/training/paths/work-with-data-warehouses-using-microsoft-fabric/) (6h38), and [manage a Fabric environment](https://learn.microsoft.com/en-us/training/paths/manage-microsoft-fabric-environment/) (3h30), totaling **27 hours 49 minutes**.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official DP-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/) | Public | 1–2 hours initially; 15 minutes per recheck |
| Five official paths from [DP-700T00](https://learn.microsoft.com/en-us/training/courses/dp-700t00) | Public | 27 hours 49 minutes listed; allow 50–90 hours with exercises/notes |
| DP-700T00 instructor-led course | Paid/partner delivery | 4 days listed |
| [Microsoft DP-700 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/practice/assessment?assessment-type=practice&assessmentId=1704375541&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Pluralsight DP-700 path](https://www.pluralsight.com/paths/implementing-data-engineering-solutions-using-microsoft-fabric-dp-700) | Paid | 6h15 across 3 courses plus practice exam; 2025 content, supplement July 2026 |
| [O’Reilly DP-700 bootcamp](https://www.oreilly.com/live-events/microsoft-fabric-data-engineer-associate-bootcamp-dp-700/0642572016304/) with Nikola Ilic | Paid/live | Two sessions; about 8 hours from the public agenda; verify current availability and dates |
| [O’Reilly DP-700 Study Guide early release](https://www.oreilly.com/library/view/microsoft-fabric-data/0642572319250/) by Michael John Pena | Paid/early release | 400 pages / 3h22 currently displayed; December 2027 publication and contents not final |
| [Microsoft Press DP-700 video](https://www.microsoftpressstore.com/store/exam-dp-700-implementing-data-engineering-solutions-9780135497517) by Andy Cutler | Paid | Runtime not exposed on the public page; published February 2026, supplement July changes |
| [Udemy DP-700 prep](https://www.udemy.com/course/dp-700-implementing-data-engineering-solutions-using-fabric/) by Phillip Burton | Paid | 17h23; updated June 2026 and states alignment through July 21, 2026 |
| [Whizlabs DP-700 course and practice test](https://www.whizlabs.com/dp-700-microsoft-certified-fabric-data-engineer-associate/) | Paid | Runtime/question count not reliably exposed publicly; verify after sign-in |
| [MeasureUp DP-700 practice test](https://www.measureup.com/microsoft-dp-700-practice-test.html) | Paid | 102 questions; allow 2–3 hours per timed attempt and review; released August 2026 |
| [Microsoft Reactor DP-700 series starting session](https://developer.microsoft.com/en-us/reactor/events/24581/) and [Microsoft Fabric channel](https://www.youtube.com/@MicrosoftFabric) | Public | Reactor series about 5–8 hours; add 3–12 hours of current product videos selectively |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use listed start/end times after partner sign-in |

Practice tests are diagnostic tools, not a substitute for implementation. Reject any source that promises recalled live questions or guaranteed passes. For each missed question, locate the governing public documentation, reproduce the decision in a lab and record why the distractors fail.

## Final readiness checklist

- I can configure Spark, domain, OneLake and Airflow workspace behavior from requirements.
- I can version, build and deploy supported Fabric items and warehouse schemas with environment-aware validation and rollback.
- I can layer workspace, item, row/column/object/file, masking, label, endorsement, audit and OneLake controls and prove each access path.
- I can choose and implement Dataflow Gen2, pipeline, notebook and event/schedule orchestration with parameters, retries and idempotency.
- I can design full, incremental, dimensional and streaming loads with deterministic late/duplicate/missing-data rules and reconciliation.
- I can select lakehouse, warehouse, Eventhouse, shortcut, acceleration and mirroring from storage, latency, feature, security and operating needs.
- I can transform and reason in PySpark, SQL and KQL at the correct grain.
- I can monitor ingestion, transformation, semantic refresh and alerts, then isolate pipeline, dataflow, notebook, Eventhouse, Eventstream, T-SQL and shortcut failures.
- I can optimize lakehouse files, pipeline movement, warehouse queries, Spark execution and real-time workloads from before/after evidence without changing correctness or security.
