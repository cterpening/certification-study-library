---
exam_code: DP-750
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-750
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-27
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-27
---

# DP-750 Implementing Data Engineering Solutions Using Azure Databricks Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 27, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dp-750-coverage-record). The [official DP-750 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-750) is authoritative.

**Current baseline:** Skills measured as of March 11, 2026; the accepted snapshot records the July 13 page update. The newly fetched October revision is preparation material until its effective date.<br>
**Upcoming blueprint change (checked September 27, 2026):** The English blueprint changes October 19, 2026. The revision uses Declarative Automation Bundles and Databricks CLI terminology, and removes deletion vectors from the clustering-strategy bullet. Domain weights are unchanged; deletion vectors remain useful technical context, not a clustering strategy. The current baseline below remains dated separately. See the [official revision](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-750).<br>
**Lifecycle status:** Active; no retirement or replacement was announced on the official pages checked.<br>
**Exam page:** [Azure Databricks Data Engineer Associate](https://learn.microsoft.com/en-us/credentials/certifications/implementing-data-engineering-solutions-using-azure-databricks/) · 120-minute assessment · ten listed languages: English, Japanese, Simplified and Traditional Chinese, Korean, German, French, Italian, Brazilian Portuguese and Spanish. Recheck language-specific revision timing when booking.<br>
**Official course:** [DP-750T00 Implement data engineering solutions using Azure Databricks](https://learn.microsoft.com/en-us/training/courses/dp-750t00) · four instructor-led days.<br>
**Practice:** Microsoft’s Practice Assessment is on [AI Skills Navigator](https://aiskillsnavigator.microsoft.com/en-us/certifications/microsoft-certified-associate/azure-databricks-data-engineer); sign-in is required to launch it.

## How to use this guide

DP-750 is an implementation exam. Trace every pipeline through this chain:

```text
source contract -> ingestion semantics -> checkpoint/idempotency -> governed target
principal -> compute identity -> storage credential/connection -> securable -> audit evidence
data contract -> validation -> quarantine/failure -> published table -> lineage
code commit -> test -> bundle target -> deployment identity -> job/pipeline run -> alert/repair
slow stage -> DAG/operator metrics -> skew/shuffle/spill/cache -> correction -> cost proof
```

Practice both SQL and Python/PySpark. For each lab retain source/target schemas, table properties, query/job/run IDs, compute/runtime/access mode, permissions, expectation metrics, checkpoint/high-water mark, Spark UI or query-profile evidence, cost/usage evidence, and cleanup. Product capabilities, names, runtime requirements, preview states, and serverless availability change quickly; recheck the linked documentation before implementing or booking.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes the objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Microsoft's published exam objectives.

## Objective map

| Published domain | Weight | Data-engineering question |
|---|---:|---|
| Set up and configure an Azure Databricks environment | 15–20% | Can you select governed compute and organize Unity Catalog objects for isolation, discovery, and lifecycle? |
| Secure and govern Unity Catalog objects | 15–20% | Can the correct workload or person reach only the permitted rows, columns, files, and shares, with lineage and audit evidence? |
| Prepare and process data | 30–35% | Can you choose and implement batch/stream ingestion, model/layout, transformation, CDC, and quality behavior? |
| Deploy and maintain data pipelines and workloads | 30–35% | Can you orchestrate, test, deploy, observe, repair, and optimize production workloads repeatably? |

---

## 1. Build the operating model

### Separate platform, workspace, governance, compute, and storage

- **Azure resource plane:** subscription/resource group, Azure Databricks workspace, networking, managed identity/access connector, Key Vault, storage, diagnostic settings and Azure RBAC.
- **Databricks account/workspace plane:** identities, workspace assignment, entitlements, compute policies, jobs, pipelines, Git folders, SQL warehouses and workspace permissions.
- **Unity Catalog governance plane:** metastore, catalog, schema, table/view/materialized view, volume, function, connection, foreign catalog, share/recipient/provider, storage credential and external location.
- **Data plane:** files, Delta/Iceberg/Parquet/CSV/JSON data, transaction logs, checkpoints, tables and streaming state in cloud storage.
- **Execution plane:** serverless or classic compute executes SQL/Python/Spark; its access mode, runtime, identity, libraries, capacity and topology control what the code can do.

Unity Catalog is the integrated governance layer for data and AI: it applies access control, discovery, lineage, auditing, and sharing across governed objects. Start with [What is Unity Catalog?](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/) and the [Azure Databricks documentation](https://learn.microsoft.com/en-us/azure/databricks/).

### Use an evidence-first delivery loop

1. Define consumer grain, freshness, completeness, correctness, retention, security, RPO/RTO and cost SLOs.
2. Inventory source extraction/CDC capabilities, schema, volume/rate, ordering, duplicates, late data, delete semantics and authentication.
3. Choose ingestion mechanism and batch/stream processing semantics.
4. Design bronze/silver/gold or another explicit responsibility model; choose format, managed/external lifecycle, partition/clustering and SCD/temporal behavior.
5. Define principals, workspace/catalog isolation, grants/ABAC/masks, storage access, secrets, audit and share boundary.
6. Implement deterministic transformations, validation/quarantine and idempotent writes.
7. Package source, job/pipeline resources and permissions as a bundle; deploy with a non-personal identity.
8. Test unit, integration, end-to-end, UAT, replay, schema drift, scale, recovery and negative authorization paths.
9. Monitor data quality/freshness, run state, compute, Spark/operator behavior, storage layout, cost and audit.
10. Repair from evidence, reconcile outputs, record recovery, and feed findings into design.

> **Related item:** A lakehouse layer name is not a quality guarantee. “Silver” data is trustworthy only if its contract, validation, failed-record path, lineage, ownership, freshness and reconciliation are defined and observed.

### Know the current terminology

Current documentation uses **Lakeflow Spark Declarative Pipelines** (often shortened to Lakeflow pipelines) for the product historically known as Delta Live Tables. Current deployments and older courses may still contain `dlt` APIs or “DLT” names. Preserve the distinction between product evolution and Delta Lake itself. Use current [Lakeflow pipeline concepts](https://learn.microsoft.com/en-us/azure/databricks/ldp/concepts/) and mark old UI/API instructions for verification.

Declarative Automation Bundles are the current name in documentation for the capability often known as Databricks Asset Bundles. The March baseline says “Databricks Asset Bundles”; the October 19 revision adopts “Declarative Automation Bundles”. Understand `databricks.yml`, resources, targets, variables, artifacts, permissions and `databricks bundle ...` operations while following current naming in the [bundle documentation](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/).

---

## 2. Set up and configure an Azure Databricks environment (15–20%)

### Select compute from workload and governance requirements

| Compute | Strong fit | Key decision points |
|---|---|---|
| Serverless jobs/notebooks/pipelines | supported workloads needing rapid startup, managed infrastructure and elastic operation | region/workspace eligibility, feature/library/network/data-source support, budget policies, run-as identity |
| Job compute | scheduled production jobs requiring classic configuration | ephemeral per run/job, task reuse, startup cost, policy, access mode, node/runtime/Photon |
| Classic all-purpose compute | interactive exploration and collaborative development | idle cost, termination, user isolation, permissions; avoid for routine production jobs |
| SQL warehouse | SQL queries, dashboards, BI, SQL tasks and serverless SQL | serverless/pro/classic capabilities, size/autoscaling/auto-stop, concurrency, channel and permissions |
| Classic Lakeflow pipeline compute | pipeline features unsupported on serverless or requiring classic configuration | pipeline mode, runtime/channel, workers, Photon, policy, libraries |
| Compute pool | reduce classic cluster startup by retaining ready instances | pool idle capacity/cost, node compatibility, min idle/max capacity, not a running Spark cluster |
| Shared/standard access | multiple users with workload isolation and Unity Catalog | language/runtime/library limitations and least privilege |
| Dedicated access | one user/group/workload needing features unavailable on standard | lower sharing efficiency; assigned principal and isolation |

Current guidance recommends serverless for most supported job workloads; when classic is required, use job compute for jobs and standard access where supported. Review [compute selection](https://learn.microsoft.com/en-us/azure/databricks/compute/) and [classic jobs compute guidance](https://learn.microsoft.com/en-us/azure/databricks/jobs/run-classic-jobs).

#### Configure performance and cost settings

- Choose driver and worker CPU/memory/local disk/GPU from serialized task size, shuffle, cache, library and workload needs—not raw input size alone.
- Fixed workers simplify known demand; autoscaling adapts worker count but cannot fix a single skewed partition or driver bottleneck.
- Auto-termination controls idle classic compute, not job correctness. A warehouse has its own auto-stop behavior.
- Pool-backed classic compute reduces startup but pays for idle pool instances; size from measured concurrency.
- Choose a supported Databricks Runtime/Spark version. Prefer an LTS runtime for stability unless a required feature/fix needs a newer version.
- Enable Photon for eligible SQL/DataFrame/ETL work; it is enabled by default or mandatory on several compute types, but unsupported operators can fall back. See [Photon](https://learn.microsoft.com/en-us/azure/databricks/compute/photon).
- Use compute policies to constrain node families, runtime, autoscaling bounds, tags, access mode and cost rather than relying on user memory.
- Use current ML runtime only when ML libraries/GPU stack are actually required; it is not a generic performance upgrade.

Measure startup, DBUs and cloud VM cost, utilization, throughput, shuffle/spill, p95 duration, failure/retry and downstream SLO before resizing.

#### Install libraries safely

Prefer environment/dependency specifications committed with the workload. Pin compatible versions and test against the selected runtime. Libraries can come from PyPI, Maven, CRAN, workspace files, volumes or approved repositories according to compute/access-mode rules.

Distinguish:

- notebook-scoped install for interactive isolation;
- compute-scoped library for classic shared execution;
- job/pipeline dependency declared with deployable resource;
- runtime-bundled library already supported by Databricks.

Avoid mutable “latest,” hidden `%pip` state, ungoverned JARs, secrets in coordinates and incompatible binary/Spark versions. Restart semantics differ; prove the package is present in a fresh run, not only an already-mutated notebook. Check [libraries documentation](https://learn.microsoft.com/en-us/azure/databricks/libraries/).

#### Configure compute permissions

Compute permissions such as `CAN ATTACH TO`, `CAN RESTART` and `CAN MANAGE` control use/administration of compute; they do not grant Unity Catalog data privileges. A job’s run-as principal and each task’s compute determine data access. Separate:

- permission to create compute under a policy;
- permission to attach/restart/manage an existing resource;
- job/pipeline ownership and `CAN MANAGE RUN`/view permissions;
- Unity Catalog object and storage access;
- Azure resource permissions.

A user who can attach code to privileged compute may be able to act through that compute identity, so combine access mode, run-as identity, policy and data grants.

### Organize Unity Catalog objects

The three-level namespace is `catalog.schema.object`. A practical design might use catalogs for environment or domain isolation, schemas for bounded products/layers, and objects for governed tables/views/volumes/functions.

#### Naming and isolation

Choose conventions that encode stable ownership and boundary, not every transient implementation detail. Decide:

- separate catalogs/workspaces for production versus nonproduction where blast radius or policy requires it;
- domain/product versus bronze/silver/gold catalog/schema split;
- external-sharing catalog boundary;
- regional/residency separation;
- names for service principals, storage credentials, connections and bundle targets;
- owner group, description, tags and lifecycle for every published object.

Avoid per-user production catalogs and grants directly to individuals. Use account groups and automation identities.

#### Create catalogs, schemas and volumes

A catalog contains schemas; schemas contain tables, views, volumes, functions, models and related objects. Creation requires the parent `CREATE` privilege plus `USE` through the hierarchy. The [catalog creation guide](https://learn.microsoft.com/en-us/azure/databricks/catalogs/create-catalog) documents managed-storage and foreign-catalog prerequisites.

Use a **volume** for governed non-tabular files such as landing files, checkpoints, libraries or artifacts that workloads address as files. A managed volume delegates storage lifecycle; an external volume governs an existing cloud path while you retain file lifecycle. Do not register overlapping external locations/volumes casually.

#### Managed versus external tables

| Asset | Storage/lifecycle | Drop behavior | Prefer when |
|---|---|---|---|
| Managed table/volume | Unity Catalog selects managed location and manages file lifecycle/optimization | metadata and underlying data are removed after governed retention behavior | Databricks is primary owner; default for new governed data |
| External table/volume | explicit external-location path; external system/customer owns files | metadata is removed, underlying files remain | existing/shared paths or lifecycle managed outside Databricks |

Both are governed; “external” does not mean ungoverned. See [managed versus external assets](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/managed-versus-external).

#### Tables, views and materialized views

- A table persists data. Managed Delta is the normal default; managed Iceberg or external formats apply when interoperability/requirements justify them.
- A standard view stores a query and evaluates it at read time; it can present a stable/fine-grained interface but depends on underlying objects and owner/security semantics.
- A materialized view persists query results and is refreshed by managed pipeline logic; use for repeated expensive transformations with acceptable refresh latency.
- A streaming table incrementally processes a streaming source and preserves checkpointed state.

Use DDL such as `CREATE TABLE`, `CREATE OR REPLACE TABLE`, `ALTER TABLE`, `COMMENT ON`, `CREATE VIEW`, and `CREATE MATERIALIZED VIEW` through a governed deployment. `CREATE OR REPLACE` can preserve table identity/history better than drop/recreate for supported operations, but confirm schema/property behavior.

#### Foreign catalogs and connections

Lakehouse Federation uses a Unity Catalog **connection** containing endpoint/authentication configuration and a **foreign catalog** that mirrors external database metadata. It enables pushdown/federated queries; it does not ingest data into Delta automatically.

Choose federation for current/low-copy access and migration discovery; ingest when performance, independence, history, quality, joins, governance or source load requires a local table. Protect the connection credential, restrict `USE CONNECTION`/foreign catalog creation, test pushdown/query plans and account for source concurrency. Start with [Lakehouse Federation](https://learn.microsoft.com/en-us/azure/databricks/query-federation/).

#### AI/BI Genie instructions

Genie spaces use governed semantic context and instructions to help users query data conversationally. Instructions should define business terms, synonyms, joins, filters, time logic and example SQL without granting new access. Good metadata and verified queries matter more than a long prompt. Test ambiguous phrasing and permission differences, and never treat generated results as authoritative without validation. See [curate an AI/BI Genie space](https://learn.microsoft.com/en-us/azure/databricks/genie/).

> **Related item:** Catalog/schema design and workspace binding are security architecture, not just naming. A perfectly written `GRANT` cannot compensate for a production catalog exposed to the wrong workspace or a storage path reachable outside governed access.

---

## 3. Secure and govern Unity Catalog objects (15–20%)

### Apply least privilege through the hierarchy

Unity Catalog securables inherit privileges downward under the current model. To query a table, a principal commonly needs `USE CATALOG`, `USE SCHEMA`, and `SELECT`; modifying requires `MODIFY` plus traversal. Creating objects needs the relevant `CREATE` privilege on the parent. Check the current [privileges reference](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/access-control/privileges-reference).

```sql
GRANT USE CATALOG ON CATALOG prod_sales TO `grp_sales_analysts`;
GRANT USE SCHEMA ON SCHEMA prod_sales.curated TO `grp_sales_analysts`;
GRANT SELECT ON TABLE prod_sales.curated.daily_revenue TO `grp_sales_analysts`;
```

Grant Unity Catalog privileges to account groups and registered service principals for routine access. The access connector’s Azure managed identity is a separate storage-authentication layer; it does not substitute for the querying principal’s Unity Catalog grants. Ownership includes powerful management ability; assign stable owner groups. `ALL PRIVILEGES` is evaluated dynamically and is rarely the minimum. Validate with `SHOW GRANTS`, `INFORMATION_SCHEMA` and negative tests from the actual run-as principal.

### Choose fine-grained controls

The [Unity Catalog access-control overview](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/access-control/) distinguishes:

| Control | Scope | Best fit |
|---|---|---|
| object privileges/ownership | securable hierarchy | baseline access and delegation |
| workspace bindings | catalogs, credentials, external locations | restrict governed objects to selected workspaces |
| dynamic view | reusable query interface | complex joins/derived security or broad compatibility |
| table row filter / column mask | one table | table-specific predicate/masking UDF |
| ABAC policy | tagged objects at catalog/schema scale | centralized tag-driven row filtering/masking |

Databricks recommends ABAC for consistent policy across many tables; table-specific [row filters and column masks](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/filters-and-masks/) remain useful but have runtime, write, sharing, time-travel and optimizer constraints. Test `is_account_group_member`, policy-function ownership, fail-closed behavior, predicate performance, type-preserving masks and excluded principals.

#### Governed tags and ABAC

Governed tags constrain allowed keys/values and who can assign them. An ABAC policy uses tags plus a SQL UDF to apply filtering/masking automatically. Design:

1. taxonomy and data-owner approval;
2. governed tag definition and assignment rights;
3. deterministic, simple policy UDF;
4. catalog/schema policy scope and exemptions;
5. current compute/runtime support;
6. conflict behavior if several policies match;
7. performance and negative authorization tests;
8. audit/reporting and change rollout.

ABAC row filters and masks require serverless or supported Runtime 16.4+ compute; dedicated compute also needs fine-grained filtering. Tag changes can take minutes to take effect. Multiple distinct filters on one table/user or masks on one column/user cause an error; identical UDFs with identical arguments can coexist. Exemptions expose unmasked, unfiltered data. Check the [current ABAC requirements](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/abac/requirements).

When a view reads a protected base table, ABAC uses the **session user** for its filters/masks, while base-object privilege checks use the view owner. Pipeline refreshes use the pipeline owner/run-as identity and can persist that identity’s filtered or masked result. Design any trusted ETL exemption explicitly and secure its output. OpenSharing requires an exempt share owner; provider ABAC does not govern recipient access. Apply recipient-side controls or publish an appropriately restricted dataset.

The [policy evaluation rules](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/abac/policy-evaluation) explain why deleting a referenced governed tag or UDF can deny queries throughout the policy scope. Removing a tag definition is not a safe way to disable a policy. Test missing attributes, policy conflicts, owner/exempt identities and actual reader routes.

**September additions, not blanket GA claims:** [Metastore policies](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/abac/metastore-policies) are Beta; SQL management requires Runtime 19+ and metastore administration. [DENY policies](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/abac/deny-policies) are separately Beta and currently deny only `MANAGE ACCESS CONTROL`. They can prevent an owner from changing access, but do not remove that owner’s other data privileges; metastore admins are exempt. This is not a general `DENY SELECT` facility. The metastore page mentions view targets in Beta while the requirements page still excludes direct view policies: use the documented base-table/view evaluation path above and verify direct-view support before designing around it.

#### Worked example: identity changes a persisted result

A synthetic sales table contains East = 120 and West = 80. A base-table ABAC filter allows analyst Ana only East. Ana’s query through a view returns 120 even if the view owner can read both regions. If a materialization runs under an East-filtered pipeline identity, its persisted total can also be 120; giving a later consumer broader privileges cannot reconstruct the missing 80. An explicitly approved, exempt ETL identity can read 200, but the resulting table needs its own consumer protections. Separately, denying access-management to an owner does not itself turn their readable total into zero.

### Authenticate workloads and resources

Distinguish identities:

- **User:** interactive development; not a stable production run-as owner.
- **Service principal:** application/automation identity for jobs, bundles, REST/CLI and supported storage/data sources; use OAuth/federation where possible.
- **Managed identity:** Azure-managed identity, commonly through an Azure Databricks access connector for storage credentials or Azure resource access; no client secret lifecycle.
- **Compute identity:** effective identity under access mode and resource configuration; must align with Unity Catalog and source permissions.

For ADLS governed access, create an access connector/managed identity, grant minimum Azure storage role, create Unity Catalog storage credential, then external location/volume/table. An Azure role alone does not grant Unity Catalog object access; a Unity Catalog grant alone cannot overcome missing Azure storage access. Follow the [managed-identity storage setup](https://learn.microsoft.com/en-us/azure/databricks/connect/unity-catalog/cloud-storage/azure-managed-identities): Azure storage roles go to the connector identity; Unity Catalog grants go to the Databricks principal.

Use service-principal OAuth for unattended CLI/REST and source connections when managed identity is unsupported. Rotate any remaining secret and scope it to the environment.

#### Key Vault secrets

Azure Key Vault-backed secret scopes let notebooks/jobs reference a secret without embedding it, but permission to read the scope is powerful and returned values can leak through logs, exceptions or transformations. Prefer managed identity/OAuth and Unity Catalog connections/storage credentials. Use secrets only when the target lacks passwordless support; restrict scope ACLs, rotate, redact logs and test expiration. See [secret management](https://learn.microsoft.com/en-us/azure/databricks/security/secrets/).

> **Related item:** A secret scope centralizes storage; it does not make a shared secret least-privileged. Passwordless identity removes the copied bearer secret and usually improves attribution and rotation.

### Preserve definitions, descriptions, retention and lineage

#### Discovery metadata

Every published table/column should have stable name, owner, business and technical description, grain, units, allowed values, sensitivity/classification, freshness and support contact. Apply comments through DDL so definitions travel with deployment. Use governed tags for policy/classification; do not put sensitive values in comments/tags.

Catalog Explorer exposes owners, history, dependencies, popularity and lineage. AI-generated descriptions are drafts that a data owner validates. Genie instructions build on this semantic layer.

#### Retention

Separate:

- business record retention;
- Delta history/log and deleted-file retention;
- `VACUUM` eligibility;
- streaming checkpoint/source retention;
- job/run/log retention;
- external-source/share retention;
- managed versus external drop lifecycle.

Do not reduce Delta retention merely to reclaim space. Active readers/streams, time travel, rollback, legal hold and recovery can depend on old files. Apply policy via table properties/automation and prove deletion plus exception handling.

#### Lineage

Unity Catalog captures runtime lineage for supported queries/jobs/pipelines down to columns in many cases. Use it for impact analysis and discovery, but validate coverage: path-based access, external tools, unsupported workloads or incomplete runtime history can create gaps. Record owner, history, upstream/downstream and job/notebook relationships in Catalog Explorer/system tables. See [Unity Catalog lineage](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/data-lineage).

### Audit activity

Prefer the `system.access.audit` system table for account audit analysis where available. Query who, service, action, object, workspace, request/run identifiers, result and source details; restrict access because audit rows can expose sensitive metadata. Azure diagnostic settings can stream workspace logs to Log Analytics, Storage or Event Hubs for central Azure operations, but exporting increases exposure and cost. See [audit log system table](https://learn.microsoft.com/en-us/azure/databricks/admin/system-tables/audit-logs) and [Azure diagnostic log delivery](https://learn.microsoft.com/en-us/azure/databricks/admin/account-settings/audit-log-delivery).

Build detections for privilege/owner changes, credential/connection changes, share/recipient activity, token/secret operations, repeated denials, production job changes and destructive DDL. Correlate with source control and deployment identity.

### Design secure Delta Sharing

Delta Sharing/OpenSharing provides live governed data access without copying files manually. Define provider, share, recipient, assets, authentication/profile/token lifecycle, network boundary, recipient use, row/column policy compatibility, revocation, audit and version/change contract.

Prefer recipient-specific objects and minimum share content. For open recipients, protect bearer credentials, set expiry/rotation, monitor downloads and revoke promptly. A share grants access to current underlying data according to sharing semantics; it is not a one-time export. Validate views, history/CDC options and ABAC/mask support in [Delta Sharing documentation](https://learn.microsoft.com/en-us/azure/databricks/data-sharing/).

---

## 4. Prepare and process data (30–35%)

### Design the model before choosing syntax

For each dataset define:

```text
business grain + key + event/effective/ingest time
source extraction + ordering + duplicate/delete/late semantics
target contract + SCD/history + retention + quality thresholds
batch/stream freshness + replay boundary + reconciliation
format + managed/external lifecycle + partition/clustering layout
```

#### Choose format

| Format | Strong fit | Limitations/decision |
|---|---|---|
| Delta | governed mutable lakehouse tables, batch/stream unification, ACID, MERGE, schema enforcement/history | transaction log and retention/maintenance semantics |
| Managed Iceberg | open interoperability requirement under supported Unity Catalog/runtime behavior | feature/runtime/client compatibility and preview/GA details |
| Parquet | portable immutable columnar exchange | no Delta transaction/constraint/evolution semantics by itself |
| CSV | simple text interchange | weak types, quoting/delimiter/header/encoding ambiguity |
| JSON | nested/semi-structured interchange | parse cost, schema drift, mixed types, many small files |

Landing raw files and governed operational tables can use different formats. Preserve source evidence in bronze while publishing typed Delta/Iceberg tables downstream.

#### Model grain, SCD and temporal history

- **Fact grain:** one row per event/transaction/snapshot at an explicitly stated level. Measures must be additive only across valid dimensions.
- **Dimension key:** stable business/natural key plus optional surrogate key for warehouse relationships.
- **SCD Type 1:** overwrite corrected/current attributes; no historical dimension versions.
- **SCD Type 2:** expire old row and insert a new version with effective start/end/current flag; preserves point-in-time relationship.
- **Temporal event/history table:** append state changes with business event and ingestion/process times, ordering key and source version.

Late/out-of-order CDC requires sequence logic. A later-arriving record is not necessarily a later business state. Define tie-breaking, delete/tombstone behavior, replay and interval non-overlap.

#### Partitioning, liquid clustering, Z-order and deletion vectors

Traditional Hive partitioning creates directory partitions and works best for large, predictable, low-cardinality filter columns; over-partitioning creates small files and metadata overhead. Z-order co-locates multiple columns during `OPTIMIZE` for data skipping on non-liquid tables.

Current Databricks recommends [liquid clustering](https://learn.microsoft.com/en-us/azure/databricks/delta/clustering) for new tables. It replaces partitioning and Z-order for that table, supports evolving clustering keys, and requires compatible runtime/table features. `CLUSTER BY AUTO`/predictive optimization support depends on managed-table/runtime features.

Deletion vectors record row-level changes without immediately rewriting all Parquet files, enabling faster deletes/updates/merges and row-level concurrency in supported configurations. Readers must support the table feature. `OPTIMIZE` materializes layout; `REORG`/`VACUUM` may be needed for physical removal under current behavior. Verify format/runtime/external-client compatibility.

Choose layout from table size, file arrival, query predicates, cardinality, skew, DML concurrency and maintenance—not a rule such as “partition by date.” Capture scan bytes/files and runtime before/after.

### Choose an ingestion tool

| Tool | Choose when | Key operational state |
|---|---|---|
| Lakeflow Connect | managed connectors for supported SaaS/database/object sources | connection, gateway where needed, source cursor, destination pipeline/table, connector limits |
| Auto Loader in Lakeflow pipelines/notebook | scalable incremental cloud-file discovery and schema handling | checkpoint, schema location, notification/listing mode, rescued data |
| `COPY INTO` | SQL-driven idempotent incremental file load at moderate file scale | file tracking, format/options, validation, target table |
| Notebook/PySpark | custom extraction/transformation/protocol or unsupported connector | code, secret/identity, checkpoint/high-water mark, retry and tests |
| Azure Data Factory | Azure-wide orchestration/copy, hybrid integration runtime and many connectors | linked service/identity, integration runtime, trigger, activity retries/monitoring |
| Structured Streaming | custom stateful streaming and event-time logic | checkpoint, offsets, watermark/state/output mode, sink semantics |

[Cloud-object ingestion guidance](https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/) recommends Auto Loader at very high file counts and explains when `COPY INTO` is simpler. [Lakeflow Connect](https://learn.microsoft.com/en-us/azure/databricks/ingestion/lakeflow-connect/) is source-specific and rapidly evolving; verify connector availability, gateway, auth, CDC/delete/schema and destination constraints.

#### Full, incremental and CDC extraction

- **Full snapshot:** simple source truth but expensive; requires replacement or diff logic and consistent extraction point.
- **High-water mark:** query values after last successful `(timestamp,key)`; overlapping window plus dedup handles ties/late commits.
- **Log-based CDC:** preserves inserts/updates/deletes/order metadata where connector supports it; retain source logs long enough to recover.
- **File arrival:** file path/metadata and checkpoint prevent reprocessing; upstream must not mutate silently or reuse names.
- **Streaming offset:** checkpoint owns progress; never share one checkpoint between distinct queries.

Persist progress only after durable target commit, or use a framework that atomically coordinates it. Replaying should converge to the same target.

#### Batch versus streaming

Use batch/triggered incremental processing when minute/hour/day freshness meets SLO; it is simpler and often cheaper. Use continuous streaming for genuine low-latency need with state/checkpoint operations understood. “Streaming” describes execution, not automatically exactly-once business results.

Structured Streaming tracks source offsets and state in a checkpoint. Watermarks bound how long event-time state waits for late data; they do not repair arbitrary late records. Choose output mode and sink idempotency. For Event Hubs, use its Kafka-compatible endpoint with the Structured Streaming Kafka connector, and configure consumer group, offsets, authentication, Event Hub partitions versus Spark partitions, max rates and checkpoint. Lakeflow pipelines do not support the third-party JVM Event Hubs connector. See [Structured Streaming](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/) and the current [Event Hubs pipeline-source guidance](https://learn.microsoft.com/en-us/azure/databricks/ldp/event-hubs).

### Ingest with SQL and Spark

#### SQL patterns

These illustrative statements assume a disposable `lab` catalog, `raw`/`curated` schemas, a `lab.raw.landing` volume, an existing typed `lab.raw.events` Delta target, and appropriate privileges. A [volume path](https://learn.microsoft.com/en-us/azure/databricks/volumes/) needs catalog, schema and volume before its relative file path. Validate source columns and unique, non-null ordering keys before running.

```sql
CREATE TABLE lab.raw.orders
USING DELTA
AS SELECT * FROM read_files('/Volumes/lab/raw/landing/orders', format => 'json');

CREATE OR REPLACE TABLE lab.curated.customer_snapshot AS
SELECT customer_id, name, status
FROM (
  SELECT customer_id, name, status,
         row_number() OVER (
           PARTITION BY customer_id
           ORDER BY updated_at DESC, change_id DESC
         ) AS rn
  FROM lab.raw.customer_changes
) ranked
WHERE rn = 1;

COPY INTO lab.raw.events
FROM '/Volumes/lab/raw/landing/events'
FILEFORMAT = JSON
FORMAT_OPTIONS ('rescuedDataColumn' = '_rescued_data')
COPY_OPTIONS ('mergeSchema' = 'false');
```

CTAS creates a table from a query; replacement publishes a complete snapshot; `COPY INTO` tracks files. The snapshot query chooses current attributes, not SCD Type 2 history. [`row_number`](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/functions/row_number) is deterministic only with a unique ordering; reject unresolved ties instead of treating arbitrary output as a business decision.

#### Worked example: a file is not a business key

File `part-a.json` contains two synthetic events and is loaded once. Repeating [`COPY INTO`](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/delta-copy-into) against that already loaded file leaves two target rows, even if the file was modified. With `force=true`, idempotency is disabled: replaying the unchanged two-row file into an append target produces four rows. Two identical business events arriving in a different new file can also duplicate business keys. Keep immutable source files and design key-level reconciliation separately. `VALIDATE ALL` checks prospective data without writing; it does not prove end-to-end freshness.

#### Auto Loader

```python
raw = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", schema_path)
    .option("rescuedDataColumn", "_rescued_data")
    .load(source_path)
)

(raw.writeStream
    .option("checkpointLocation", checkpoint_path)
    .trigger(availableNow=True)
    .toTable("lab.raw.events_auto"))
```

Define `source_path` under the lab volume and use stable schema/checkpoint paths dedicated to this ingestion workload. In Lakeflow pipelines, the framework manages those locations. [Auto Loader](https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/) does not promise file arrival order; deleting a checkpoint removes progress, and a checkpoint is not a retained copy of source files.

[Schema evolution](https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/schema) has operational consequences: inferred JSON/CSV/XML fields default to strings. Without an explicit schema, `addNewColumns` updates schema metadata and then fails so a restart can use it. With an explicit schema, the default is `none`; `rescue` records unexpected fields without evolving the schema. A type mismatch rescued into `_rescued_data` does not necessarily trigger parser `FAILFAST`. Monitor rescue counts and separately validate types and business meaning.

#### Lakeflow pipeline ingestion and AUTO CDC

Lakeflow pipelines define streaming tables, materialized views and flows declaratively, infer dependency order and capture an event log. Auto Loader handles files; `AUTO CDC ... INTO` handles ordered CDC and SCD Type 1/2 under declared keys/sequence/delete rules. It is preferable to hand-coded merge state when semantics fit.

Choose a notebook/job when bespoke side effects/control flow dominate. Choose a declarative pipeline when the result is a graph of incrementally maintained tables with expectations and managed recovery. Do not put arbitrary API side effects inside a declarative transformation expected to be re-evaluated.

[AUTO CDC](https://learn.microsoft.com/en-us/azure/databricks/ldp/cdc) requires serverless pipelines or Pro/Advanced editions. It consumes a change feed; `AUTO CDC FROM SNAPSHOT` compares ordered snapshots and is Python-only. These Databricks APIs are not part of Apache Spark Declarative Pipelines. For tied timestamps, use a stable sequence such as `STRUCT(event_time, change_id)`; keep tombstones longer than the expected arrival/processing delay.

#### Worked example: last arrival is not the latest change

Customer C has `(08:00, 1, bronze)`, `(08:00, 2, silver)`, then a late-arriving `(07:59, 9, starter)`. Ordering lexicographically by `(event_time, change_id)` gives current state **silver**, not starter or bronze. A Type 1 target retains one state; a Type 2 design needs separate effective intervals. Deduplicating a micro-batch alone does not prevent an older later batch from overwriting a newer target: compare source and target sequence, and retain delete/tombstone state for replay.

**Related item — automatic versus legacy CDF:** [Automatic CDF](https://learn.microsoft.com/en-us/azure/databricks/delta/delta-change-data-feed) computes changes at read time on eligible Unity Catalog tables with Runtime 19+: Delta needs row tracking; managed Iceberg needs v3. Azure Databricks readers are required. It uses the familiar `table_changes`/`readChangeFeed` APIs, but has limitations for row filters/masks and non-additive schema changes. Legacy Delta CDF still needs explicit enablement; do not run both modes together. Neither feed is a permanent audit archive. Verify regional rollout and retained versions before migration; September GA and the planned end-of-October regional rollout are separately stated in the [upcoming changes](https://learn.microsoft.com/en-us/azure/databricks/release-notes/whats-coming).

### Cleanse, transform and load

#### Profile and type data

Profile counts, distinct/cardinality, null/missing, min/max/quantiles, distributions, pattern/length, freshness, duplicates and referential coverage by meaningful segment. Samples can miss rare failures; profile at scalable aggregation and preserve baseline/trend.

Choose types from semantics and range:

- decimal precision/scale for money rather than floating point;
- `DATE` versus `TIMESTAMP`/`TIMESTAMP_NTZ` with explicit time-zone contract;
- integral width large enough for future values;
- structs/arrays/maps for genuine nested semantics, not to avoid modeling;
- cast quarantine for invalid strings instead of silently producing null.

#### Handle duplicates, missing and null

Define duplicate by business key plus ordering/version, not whole-row equality. Use a deterministic window or `dropDuplicatesWithinWatermark` for appropriate streaming cases. Distinguish missing field, null, empty string, default and “unknown.” Imputation must be a documented analytical rule; operational pipelines often quarantine instead.

#### Transform correctly

- Filter early only when it preserves required evidence.
- Aggregate at the declared grain; check double counting after joins.
- Inner/left/right/full/semi/anti joins encode different existence behavior.
- `UNION` removes duplicates while `UNION ALL` retains them; DataFrame `union` is position-based unless using a name-aware form.
- `INTERSECT` and `EXCEPT` have set semantics and are useful for reconciliation.
- Pivot creates data-dependent columns and can explode schema; unpivot normalizes measures.
- Denormalization improves consumption but requires a refresh/source-of-truth rule.

#### Load with append, insert and MERGE

- append immutable new events when duplicates are controlled;
- insert into explicit columns when target contract is stable;
- `MERGE` for upsert/delete CDC with a unique source match per target row;
- replace only when snapshot scope, atomicity, readers and history are understood.

Deduplicate the merge source by key and sequence first; multiple source matches can be ambiguous/fail. [MERGE duplicate detection](https://learn.microsoft.com/en-us/azure/databricks/delta/merge) considers `ON` and `WHEN MATCHED` conditions in Runtime 16.0+, while 15.4 LTS and earlier consider only `ON`. Pin the runtime when comparing behavior. Use predicates to limit scanned target data where safe. Reconcile insert/update/delete counts and rerun the same input to prove idempotency.

### Enforce schema and data quality

Delta [schema enforcement](https://learn.microsoft.com/en-us/azure/databricks/tables/schema-enforcement) validates writes. Schema evolution explicitly accepts compatible additions/changes; it is not a reason to allow every source drift. Maintain a contract:

| Change | Default response |
|---|---|
| new nullable field | rescue/quarantine, review, then explicit evolution |
| missing required field | fail or quarantine |
| safe widening | approve/test consumer compatibility |
| incompatible type/meaning | new column/version and migration |
| renamed field | treat as add + deprecate unless mapped explicitly |
| unexpected nested shape | rescued data plus source-owner alert |

#### Validation mechanisms

- Delta `NOT NULL` and `CHECK` constraints protect supported row conditions.
- pipeline expectations can warn, drop or fail per record/flow and emit metrics;
- SQL/Python validation tables cover uniqueness, referential, aggregate/batch and cross-table checks;
- schema enforcement prevents incompatible Delta writes;
- reconciliation compares source/target counts, sums, hashes, keys and CDC offsets.

Expectations are data-quality actions, not arbitrary orchestration gates. A failed expectation’s scope differs between triggered and continuous pipeline behavior. [Expectation semantics](https://learn.microsoft.com/en-us/azure/databricks/ldp/expectations) distinguish retaining invalid rows, dropping them, and failing the affected update. Fail does not produce normal expectation metrics. In a triggered pipeline, independent parallel flows can still succeed; continuous failures also stop dependent flows. Expectations are not supported with `AUTO CDC FROM SNAPSHOT`.

#### Worked example: quality counts and commit scope

Of 100 synthetic inputs, six have invalid prices. A warn expectation writes 100; drop writes 94 and records six dropped; fail rejects that update instead of publishing its 94 valid rows. A separately successful parallel flow is not rolled back merely because this flow fails. A drop action does not automatically save the six rejected rows: add an explicit quarantine branch and reconcile accepted plus quarantined records to the input. Use a publication gate when consumers require several outputs to be mutually consistent.

Read [expectation patterns](https://learn.microsoft.com/en-us/azure/databricks/ldp/expectation-patterns), retain invalid records in a quarantine with reason/source/run, and alert on trends rather than hiding dropped data.

> **Related item:** “Exactly once” in an engine does not guarantee an external business side effect occurred once. Bound the claim to source offsets and transactional Delta writes, then add idempotency for APIs, messages and nontransactional sinks.

---

## 5. Deploy and maintain pipelines and workloads (30–35%)

### Design the pipeline graph

Make tasks small enough to retry/own/observe but not so fragmented that orchestration dominates. Define for each node: inputs, outputs, run-as identity, compute, parameters, timeout, retries, quality gate, success evidence and idempotency.

Typical order:

```text
source readiness -> ingest bronze -> validate/quarantine -> transform silver
-> reconcile -> publish gold/materialized view -> quality/freshness gate
-> notify consumers -> maintenance
```

Dependencies are not necessarily sequential. Parallelize independent branches; converge only at a real data dependency. Avoid using sleeps as readiness. Use task values/parameters or persisted control tables, not notebook-local state.

#### Notebook versus Lakeflow pipeline

| Notebook/task graph | Lakeflow pipeline |
|---|---|
| explicit control flow, mixed task types, external side effects, bespoke Spark | declarative table graph, managed incremental processing, expectations, Auto Loader/AUTO CDC |
| developer owns checkpoints/retries/table writes | framework owns more orchestration/event-log/maintenance behavior |
| unit-test pure functions and integration-test notebook entry point | test transformations plus pipeline-specific APIs in supported framework |

A Lakeflow Job can orchestrate notebooks and a Lakeflow pipeline together. Choose the smallest abstraction that preserves correctness and operations.

### Implement Lakeflow Jobs

A job contains tasks, dependency conditions, parameters, compute, run-as identity, trigger, concurrency, timeout/retry and notifications. Task types include notebook, Python, JAR, SQL, pipeline, dbt and control-flow types under current product support. See [configure jobs](https://learn.microsoft.com/en-us/azure/databricks/jobs/configure-job) and [tasks](https://learn.microsoft.com/en-us/azure/databricks/jobs/configure-task).

#### Triggers and schedules

[Job triggers](https://learn.microsoft.com/en-us/azure/databricks/jobs/triggers) include schedule, file arrival, table update, model update, continuous and manual/external invocation. Choose:

- schedule for predictable windows;
- file arrival for event-driven files without constant polling;
- table update for governed upstream dependency;
- continuous for always-on restart behavior and true latency needs;
- external orchestration when a broader system owns dependencies.

Account for timezone/DST and overlapping runs. Default maximum active run is limited; configure concurrency only when outputs/checkpoints can safely overlap.

#### Alerts, retries and restart

Configure job/task notifications for failure, duration, success only where useful, streaming backlog and other supported events. Route to owned email/system/webhook destinations and include runbook/run URL. [Job notifications](https://learn.microsoft.com/en-us/azure/databricks/jobs/notifications) have destination/rate behavior that can change.

For [continuous pipeline maintenance](https://learn.microsoft.com/en-us/azure/databricks/ldp/maintenance-windows), configure day, local hour and time zone. Maintenance normally starts within a one-hour window, but a serverless cluster lifetime limit can force a restart outside it. A pending-free window does not force a restart. Maintenance notifications use system destinations, not email; test checkpoint recovery, backlog and freshness after the pause.

Retry only transient/idempotent work. A code/schema/permission/quality failure needs correction, not repeated cost. Configure timeout per attempt, exponential backoff where applicable, and continuous-job restart behavior. Use repair run to rerun failed/skipped tasks while preserving successful upstream outputs, only if those outputs and parameters remain valid.

### Implement development lifecycle processes

#### Git workflow

Use a Git repository as source of truth. Databricks Git folders provide a workspace client, but production deployments should come from a reviewed commit/tag through automation. Keep notebooks as source format where practical, separate pure transformation functions from orchestration entry points, and exclude generated data, secrets, checkpoints and environment-specific IDs.

Branch briefly, resolve conflicts in source-aware tools, run tests before merge, protect the production branch and map deployed commit to bundle/job/run. Even if this repository itself does not require PRs, the exam objective expects understanding branches, pull requests and conflict resolution as SDLC controls.

#### Testing strategy

| Level | Proves | Example |
|---|---|---|
| Unit | pure transformation for bounded inputs | null/duplicate/SCD function with local/small Spark data |
| Contract/schema | source/target compatibility | required columns/types and drift classification |
| Integration | real catalog/storage/runtime/identity behavior | write/read temp Delta table, expectation and permission denial |
| End-to-end | source through published output and monitoring | replay batch, reconcile and observe job event |
| UAT | business meaning and consumer acceptance | finance totals/grain/security/freshness signed by owner |
| Performance/recovery | SLO at representative scale and failure | skewed join, checkpoint loss rehearsal, repair run |

Tests must be deterministic, isolated by catalog/schema, use representative skew and clean up. Pipeline-specific expectations/AUTO CDC need supported Azure Databricks tests; [pipeline unit testing](https://learn.microsoft.com/en-us/azure/databricks/ldp/unit-testing) documents current boundaries.

The pipeline unit-test framework is **Beta**, uses Python tests in the web editor, and requires pipeline ownership plus catalog `USE CATALOG`/`CREATE SCHEMA`. Triggered mode is required. Named-table operations through the supplied test session redirect to a temporary schema; path writes, Kafka/Auto Loader connectors, external APIs and governance mutations can reach real systems. Keep them outside test code and selected pipeline dependencies. Mocks do not inherit production masks or row filters. Do not run tests concurrently with a pipeline update. Query the returned test event-log table when available; `event_log()` can refer to production history. Prove security and integration separately in an isolated environment.

#### Package and deploy bundles

A bundle includes `databricks.yml`, resources (jobs/pipelines), code/artifacts, variables, targets and permissions. A safe workflow:

```text
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle run -t dev <resource>
# test/review evidence
databricks bundle validate -t prod
databricks bundle deploy -t prod
```

Use target-specific workspace/root paths, catalogs, identities, compute policies and schedules without copying source definitions. Give CI a service principal/OAuth identity with only deploy/run permissions. Validate/deploy through the [bundle CLI](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/cli/bundle-commands); use REST APIs for supported resource lifecycle/invocation when another automation system owns deployment.

Review the [direct deployment engine](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/direct) before updating a bundle. Current CLI behavior includes direct defaults for new bundles and version-dependent migration of existing Terraform state. Migrate in a test target, inspect `bundle plan` and retain required settings explicitly: removing a configured field under the direct engine restores the resource default, whereas the old Terraform engine could leave the deployed value. A clean syntax validation is not approval of a deployment diff. Treat the announced September Terraform-engine disablement as a version/rollout check, not proof every installed CLI has changed.

Deployment success does not prove run success. Record resource version/commit, effective configuration, run-as identity, dry run/test run, data reconciliation and rollback. Avoid an interactive user owning production jobs.

### Monitor and troubleshoot workloads

#### Start with the failure boundary

1. Is source data present, complete and authorized?
2. Did the trigger create the expected run with parameters?
3. Which job task/pipeline flow/Spark stage failed or slowed?
4. Is the error code/configuration deterministic or transient?
5. Did target commit, partially commit or not start?
6. Are checkpoint/high-water mark and retry safe?
7. Are downstream tables/freshness/quality affected?
8. Can repair safely reuse successful upstream outputs?

Do not restart the cluster first and erase useful state/log context. Save run output, event log, driver/executor logs, Spark UI/query profile, cluster event log and recent changes.

#### Diagnose Spark with DAG and UI

| Symptom | Evidence | Likely direction |
|---|---|---|
| one task much slower | stage task duration/input/shuffle distribution | data skew; salt/repartition, join strategy or AQE |
| high shuffle read/write | exchanges in DAG/query profile | filter/project earlier, partition/join strategy, avoid unnecessary repartition |
| memory/disk spill | task metrics, executor logs | reduce partition size/state, fix skew, more memory/appropriate workers |
| driver OOM | collect/toPandas/large broadcast/metadata | keep distributed, bound results, avoid oversized broadcast, fix small files |
| many tiny tasks/files | scan/file/task metrics | compact/OPTIMIZE, tune ingestion batch and layout |
| low CPU with long I/O | storage/network/scan metrics | data skipping/layout, source throughput, node/storage choice |
| repeated recomputation | DAG and cache lifecycle | persist reused expensive dataset only; materialize/checkpoint when justified |

The [query profile](https://learn.microsoft.com/en-us/azure/databricks/sql/user/queries/query-profile) shows scan, join, shuffle, hash/sort operators and metrics. Spark UI exposes jobs, stages, tasks, executors, storage and SQL plans. Adaptive Query Execution can coalesce partitions, change joins and mitigate skew, but it cannot repair bad data model or unbounded state.

#### Cache deliberately

Spark cache/persist helps when the same expensive DataFrame is reused within a computation and fits memory/disk. It can evict useful data, become stale in a long session and waste serialization/memory for one-use data. SQL/Delta/remote/disk caching has different scope and invalidation. Measure wall time and resource/cost with a cold and warm run; `unpersist` when done.

#### Optimize Delta tables

- `OPTIMIZE` compacts small files and applies Z-order or clustering behavior according to table layout.
- `ZORDER BY` applies to non-liquid tables and uses data-skipping statistics.
- liquid clustering uses `CLUSTER BY`; it cannot be combined with partitioning/Z-order on the same table.
- predictive optimization can automate maintenance for supported Unity Catalog managed tables.
- `VACUUM` permanently removes files older than retention that are no longer referenced; it can break old readers/time travel/streams if retention is unsafe.
- deletion vectors speed DML but require compatible clients and later physical cleanup under applicable behavior.

Before maintenance, inspect table detail/history, file count/size, query predicates, data-skipping stats, concurrency, retention and downstream reader versions. Afterward compare bytes/files scanned, runtime and cost—not just file count. See [OPTIMIZE](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/delta-optimize) and [VACUUM](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/delta-vacuum).

### Monitor cost and Azure signals

Use job/pipeline run history, event logs, system tables, query history/profile, compute metrics and billing system tables. Attribute usage with tags/resource identifiers and compare DBUs/cloud cost to data volume and SLO. Serverless, classic, SQL warehouse, pool, Photon and pipeline modes have different cost levers.

The blueprint explicitly includes log streaming to Log Analytics and Azure Monitor alerts. Configure workspace diagnostic settings for required categories/destination, secure the Log Analytics workspace, account for ingestion/retention cost and query delay, then create Azure Monitor alert rules/action groups for actionable control/platform conditions. Databricks job/pipeline alerts remain closer to workload state; Azure Monitor provides Azure-wide correlation. Test alert firing, ownership, deduplication and recovery notification.

[Pipeline update choices](https://learn.microsoft.com/en-us/azure/databricks/ldp/updates) also affect recovery: full refresh can rebuild only from source data still available. Resetting selected flow checkpoints can replay without clearing target rows; the API requires fully qualified flow names. Do not substitute checkpoint reset for a reconciled rebuild.

> **Related item:** A healthy Spark job can still publish bad data, and a green data-quality run can still miss its freshness SLO. Monitor infrastructure, execution, data quality, reconciliation, freshness and business consumption separately.

---

## 6. Integrated design scenarios

### Scenario A: governed sales lakehouse

**Requirements:** nightly SQL Server snapshot plus CDC, hourly SaaS extract, PII masking, analyst self-service, 90-day source retention, Type 2 customers and production deployment controls.

1. Use Lakeflow Connect where the current database/SaaS connectors meet CDC/extraction needs; otherwise ADF or a notebook with persisted high-water mark.
2. Land immutable bronze Delta with source operation, sequence, event and ingestion time; quarantine contract failures.
3. Apply `AUTO CDC`/deterministic MERGE for customer Type 2 with business key, sequence, delete and late-event rules.
4. Create managed silver/gold Delta tables with liquid clustering chosen from measured consumer filters.
5. Put production objects in bound catalogs/schemas, grant groups through hierarchy and apply governed sensitivity tags plus ABAC masks/filters.
6. Add verified comments and Genie instructions for approved gold tables only.
7. Deploy pipeline/job/permissions with bundle targets and a service principal; test schema/replay/security/UAT.
8. Monitor expectation rate, source-to-target reconciliation, freshness, job state, usage and audit.

**Failure trap:** Type 2 based on ingestion time rewrites history incorrectly when CDC arrives out of order. Use source sequence/effective semantics and test ties/deletes.

### Scenario B: Event Hubs telemetry

**Requirements:** near-real-time events, occasional late arrival and duplicates, per-device aggregates, seven-year curated retention and cost control.

1. Consume Event Hubs with a unique consumer group/checkpoint and managed identity/OAuth where supported.
2. Parse into typed bronze streaming table; rescue unexpected fields and retain original metadata.
3. Deduplicate with device/event ID and bounded watermark only if business late-arrival tolerance supports the state bound.
4. Use a Lakeflow pipeline streaming table for incremental silver and a materialized view/gold aggregate if refresh semantics fit.
5. Apply warn/drop/fail expectations deliberately and retain quarantine.
6. Use triggered available-now processing if minute-level freshness meets SLO; continuous only if measured need justifies always-on cost.
7. Monitor streaming backlog, input/processed rates, state size, checkpoint health, expectation metrics, small files and cost.

**Failure trap:** deleting/reusing the checkpoint to “fix” a stream can replay or skip data. Preserve it, identify corruption/source retention, and use a documented recovery/reconciliation plan.

### Scenario C: federated source and external sharing

**Requirements:** query operational PostgreSQL without initial copy, then publish a governed daily product dataset to an external partner.

1. Create a least-privileged connection and foreign catalog; test query pushdown and source load.
2. Materialize daily Delta snapshot when repeated analytics/source isolation justifies ingestion.
3. Reconcile keys/counts/totals and record snapshot point.
4. Publish a recipient-specific table/view in a sharing catalog, excluding internal fields.
5. Configure share/recipient credential expiry, network/usage contract and audit; test revocation.
6. If row/column policies apply, verify current OpenSharing support and recipient semantics rather than assuming provider policy travels.

**Failure trap:** federation gives a governed name for remote data, but the remote system still owns availability, transaction consistency and query performance.

---

## 7. Hands-on labs

Use an isolated workspace/catalog and a budget. Retain code, SQL, bundle files, schemas, metrics, screenshots/query output, run IDs, permission denials, reconciliation and cleanup evidence.

### Lab 1: compute decision and runtime experiment

1. Run the same representative SQL/DataFrame ETL on eligible serverless, classic job and SQL warehouse paths.
2. On classic compute vary worker type/count/autoscaling and Photon while keeping data/query constant.
3. Capture startup, duration, CPU, shuffle/spill, DBUs/cloud cost and output equality.
4. Install a pinned job dependency and prove a clean new run resolves it.
5. enforce a compute policy and prove an unauthorized configuration is denied.
6. Defend the selected compute and record a fallback for unsupported serverless features.

### Lab 2: Unity Catalog object and lifecycle design

1. Create dev catalog/schema, managed table, external table, managed/external volume, view and materialized view.
2. apply names, owners, comments and governed tags.
3. prove drop behavior in a disposable path for managed versus external assets.
4. Create a test connection/foreign catalog if an approved source is available; inspect pushdown and source query impact.
5. Bind/restrict a catalog to the correct workspace where supported and test denial elsewhere.

### Lab 3: identity and fine-grained governance

1. Grant a group only `USE CATALOG`, `USE SCHEMA` and `SELECT` on one table; prove neighboring access is denied.
2. Run a job as a service principal and access storage through managed identity/storage credential.
3. Implement a table row filter and column mask, then an equivalent tag-driven ABAC policy in a supported lab.
4. Test authorized, unauthorized, owner/exempt and older/unsupported compute behavior.
5. Query lineage and audit system tables for the actions.
6. Remove direct individual grants and transfer ownership to a stable group.

### Lab 4: batch and incremental file ingestion

1. Generate CSV/JSON/Parquet files with duplicates, nulls, corrupt records, new columns and late files.
2. Compare `COPY INTO` and Auto Loader using separate targets/checkpoints.
3. Run each twice and prove file/idempotency behavior.
4. Configure explicit schema, rescued-data column and controlled evolution.
5. reconcile source files/rows and quarantine by reason.
6. Compare file-discovery behavior and choose from measured scale/operations.

### Lab 5: CDC, SCD and quality pipeline

1. Create out-of-order insert/update/delete CDC with stable key/sequence.
2. Implement SCD Type 1 and Type 2 with Lakeflow `AUTO CDC` or a deterministic MERGE.
3. Add null, range, type and uniqueness validation with warn/drop/fail/quarantine behavior.
4. Replay the same input and prove target convergence and nonoverlapping SCD intervals.
5. inspect pipeline graph, expectation metrics and event log.
6. compare triggered with continuous implications without leaving expensive resources running.

### Lab 6: Structured Streaming from Event Hubs

1. Configure approved authentication, consumer group and unique checkpoint.
2. ingest events with event time, duplicates and controlled late arrival.
3. apply watermark, deduplication and window aggregate; record output/update semantics.
4. stop/restart and prove offset recovery.
5. introduce a downstream failure and reconcile retry behavior.
6. capture input/processed rate, backlog, state, shuffle, files and end-to-end freshness.

### Lab 7: job, tests and bundle deployment

1. Refactor a transformation into pure tested Python plus notebook entry point.
2. add unit, contract and integration tests with isolated catalog/schema.
3. define a multi-task job and pipeline in a bundle with dev/prod targets, permissions and variables.
4. validate/deploy/run dev with CLI; deploy through a service principal or document the permission model without claiming a successful deployment.
5. call a safe run/status operation through REST.
6. create a failure, use a repair run only after proving upstream output remains valid, and map run to Git commit.

### Lab 8: performance, maintenance and monitoring incident

1. Generate a skewed join and many small Delta files.
2. diagnose DAG, stages/tasks, query profile, skew, shuffle, spill, cache and driver/executor signals.
3. apply one code/join/layout correction and compare results/runtime/cost.
4. enable liquid clustering on a suitable test table or compare with partition/Z-order on separate tables.
5. run `OPTIMIZE`; inspect history/files/data skipping. Demonstrate a safe `VACUUM` retention decision without destroying needed history.
6. send required diagnostics to Log Analytics and configure an Azure Monitor alert/action group.
7. trigger a job failure/backlog condition, verify notification/runbook, repair, and record recovery.

### Lab 9: replay, schema and quality boundaries

1. Use synthetic files in a disposable volume and verify all path/target privileges.
2. Repeat a `COPY INTO` load, then test a modified already loaded file and a new file with duplicate business keys. Compare file progress with key reconciliation.
3. Exercise inferred-schema evolution and explicit `rescue`/`none` modes; inspect rescued values and restart behavior.
4. Feed the ordered/tied/late customer example into Type 1 and Type 2 targets; verify convergence and interval history after replay.
5. Compare warn/drop/fail and quarantine counts; prove an independent successful flow is a separate commit boundary.
6. Document recoverable source retention before trying a checkpoint reset or full refresh in the disposable target.

### Lab 10: governance identities and deployment migration

1. Compare a base table, a view over it, and a materialized output for a restricted analyst and separately approved ETL principal.
2. Test tag propagation, conflicting masks and exemption scope without broad production grants. Keep newer DENY/metastore policies explicitly Beta.
3. Inventory every path/connector/API operation before using the pipeline test framework; prove named-table isolation separately from access-control integration tests.
4. Pin the CLI, inspect a test bundle migration and plan, then compare an explicitly retained setting with an omitted setting. Record the expected default before deploying.
5. Verify actual automatic-CDF availability, runtime and table features, or record why the lab uses legacy CDF. Do not relabel unavailable features as tested.
6. Configure a test continuous maintenance window/system notification only if needed; retain restart, backlog, reconciliation and cleanup evidence.

---

## 8. Original knowledge checks

These are original prompts, not recalled exam questions. Answer with decision, dependencies, evidence, failure mode and corrective action.

1. Why is serverless a strong default for supported jobs, and what compatibility evidence can require classic job compute?
2. Compare job, all-purpose, SQL warehouse, pipeline and pool responsibilities.
3. Why can more workers fail to improve a job dominated by one skewed partition?
4. What do compute permissions grant, and what Unity Catalog permissions remain separate?
5. Choose catalog/schema boundaries for dev/test/prod and two business domains.
6. Compare managed and external tables/volumes, including drop behavior.
7. When is a foreign catalog better than ingestion, and when is it worse?
8. How do descriptions, tags and Genie instructions improve discovery without granting access?
9. Which traversal and object privileges does a read-only analyst need?
10. Compare dynamic views, table row filters/masks and ABAC.
11. Why does managed identity improve storage authentication, and which Unity Catalog object still mediates governed path access?
12. What risks remain when a password is stored in a Key Vault-backed secret scope?
13. Why can Unity Catalog lineage be incomplete, and how do you validate coverage?
14. Compare system audit tables with Azure diagnostic export to Log Analytics.
15. Design a Delta Share so one partner sees only approved data and revocation is testable.
16. Choose Delta, managed Iceberg, Parquet, JSON and CSV for five distinct responsibilities.
17. Explain when SCD Type 1, SCD Type 2 and an event-history table are appropriate.
18. Why is liquid clustering preferred for many new tables, and why can it not simply be combined with Z-order/partitioning?
19. Compare Lakeflow Connect, ADF, Auto Loader, `COPY INTO`, notebook and Structured Streaming ingestion.
20. What checkpoint/high-water state proves an incremental load can resume without gap or duplicate?
21. Why does a watermark bound state rather than guarantee every late record is processed?
22. How do CTAS, `CREATE OR REPLACE TABLE`, append, insert and MERGE differ?
23. Why must a MERGE source be deterministic and unique per target key?
24. Design schema-drift actions for new nullable column, missing required column and incompatible type.
25. Compare Delta constraints, pipeline expectations, validation tables and reconciliation.
26. When should an expectation warn, drop or fail, and where do rejected records go?
27. Compare notebook orchestration with Lakeflow Spark Declarative Pipelines.
28. Choose schedule, file-arrival, table-update and continuous job triggers.
29. When is a job repair safe, and when must the entire pipeline be replayed?
30. What belongs in a bundle target versus shared resource definition?
31. Map unit, contract, integration, end-to-end, UAT and recovery tests to a pipeline risk.
32. A stage spills and has one long task. Which Spark UI/query-profile evidence distinguishes skew from general memory shortage?
33. When does caching help, and how can it increase cost or return stale development results?
34. What does `OPTIMIZE` do, and why can aggressive `VACUUM` break readers/recovery?
35. Why do Databricks workload alerts and Azure Monitor alerts complement rather than replace one another?
36. A run is green but the published table is stale. Which separate signals should have detected this?
37. Why can a view and a materialized output expose different results under ABAC?
38. Does a Beta DENY policy remove SELECT access from a table owner?
39. Why might a corrected file be skipped by COPY INTO, and why is force not a deduplication strategy?
40. What happens when inferred Auto Loader input adds a column, and how does an explicit schema change the default?
41. Compare automatic CDF, legacy CDF and AUTO CDC FROM SNAPSHOT.
42. Does a failing expectation roll back every parallel flow or automatically preserve rejected rows?
43. Which operations escape pipeline unit-test redirection?
44. What can happen when a field disappears from a direct-engine bundle configuration?

### Answer checkpoints

1. Serverless reduces infrastructure work, but library, network, source, regional or runtime constraints can require classic compute.
2. Job compute executes production tasks; all-purpose supports exploration; warehouses run SQL; pipelines manage their graph; pools retain ready VMs.
3. One oversized partition can bottleneck one task; prove skew before adding workers.
4. Compute ACLs control compute use; the effective principal still needs catalog/schema traversal and object permissions.
5. Choose boundaries from isolation, ownership, residency and deployment needs, then test cross-environment denial.
6. Managed assets delegate data lifecycle; dropping external metadata leaves customer-managed files. Verify asset-specific retention.
7. Federation favors live, low-copy queries; ingestion favors source isolation, history, predictable repeated performance and independent availability.
8. Metadata supplies meaning; only authorization controls grant access. Test Genie with different principals.
9. `USE CATALOG`, `USE SCHEMA` and `SELECT` on the intended object; avoid unrelated inherited grants.
10. Views expose a query interface, table rules target one object, and ABAC uses governed attributes across a scope; compatibility and identity still matter.
11. Azure maintains credentials, but the storage credential/external location and the requesting principal’s Unity Catalog privileges remain necessary.
12. Scope readers can misuse or leak a secret; storage location alone does not constrain its downstream authority.
13. Capture covers supported runtime operations; compare known test dependencies with the observed graph and inspect unsupported paths.
14. System tables support Databricks audit analysis; Azure export supports broader monitoring with separate ingestion, retention and access controls.
15. Publish minimum recipient-specific content, verify the exact sharing mode and policy boundary, protect credentials and test revocation.
16. Use Delta for mutable transactional tables, supported Iceberg for interoperability, Parquet for columnar exchange, JSON for nested records and CSV for simple text exchange.
17. Type 1 keeps current state, Type 2 keeps effective versions, and event history preserves transitions; define ordering and deletion semantics.
18. Liquid clustering changes layout without fixed partitions; it replaces partitioning/Z-order on that table and needs compatible readers.
19. Match connector coverage, scale, latency, custom logic and operational state to the source contract; no tool removes reconciliation.
20. Durable offsets/checkpoints must align with successful commits, source retention and a convergent replay rule.
21. A watermark bounds event-time state; data outside the bound is not guaranteed to be incorporated.
22. CTAS creates, replacement republishes a snapshot, append/insert adds rows, and MERGE applies conditional matched/unmatched changes.
23. Unique ordering avoids ambiguous matches; compare against target sequence so a later batch cannot overwrite newer state.
24. Quarantine or review new fields, reject missing required values, and version incompatible types with consumer tests.
25. Constraints cover supported row conditions; expectations control record handling; validation tables and reconciliation cover wider contracts.
26. Warn retains invalid rows, drop removes them, and fail rejects the affected update; quarantine requires an explicit design.
27. Notebooks own explicit control flow and side effects; declarative pipelines own dataset dependencies and managed incremental processing.
28. Choose the trigger from arrival/dependency/freshness needs and test timezone, concurrency and run-as behavior.
29. Repair is safe only if retained successful outputs, source versions and parameters still satisfy the contract; otherwise reconcile and rebuild a defined scope.
30. Put environment bindings, identity, catalog, compute and schedules in targets; share reusable source/resource intent.
31. Unit checks logic, contracts check schemas, integration checks real boundaries, end-to-end checks the delivery chain, and UAT checks business meaning; recovery proves replay.
32. Compare per-task distributions, shuffle bytes, spill and executor memory. A single outlier suggests skew; widespread pressure suggests broader sizing/partition issues.
33. Reuse can save repeated computation, but cache overhead, eviction and lifecycle can erase that gain; compare cold/warm results and cost.
34. OPTIMIZE changes file layout; VACUUM removes eligible obsolete files that old readers or recovery may still need.
35. Workload alerts report job/pipeline behavior; Azure Monitor correlates platform and Azure-wide signals. Test both delivery paths.
36. Source watermark, published version, row/key reconciliation and consumer freshness can detect a stale output despite a successful run.
37. View filters use the session user; materialization persists what its pipeline identity read. Later grants cannot restore rows omitted earlier.
38. No. Current DENY scope is access management, with metastore-admin exemption; it does not revoke unrelated SELECT privileges.
39. COPY INTO remembers loaded files even after modification; force reloads them and can duplicate append results.
40. Default inferred evolution updates metadata then fails for restart; an explicit schema defaults to none. Rescue handles drift without evolving columns.
41. Automatic CDF derives changes from supported row metadata; legacy CDF records enabled Delta changes; FROM SNAPSHOT compares ordered snapshots in Python. All need a retention/recovery plan.
42. No. Independent triggered flows can succeed, and rejected rows need a quarantine branch. Fail also lacks normal expectation metrics.
43. Paths, external connectors/APIs and governance mutations are not safely redirected; mocks also omit production row/mask policies.
44. The direct engine can reset it to the resource default. Inspect the plan and declare every value that must persist.

---

## 9. Final readiness checklist

- [ ] I can map every March 11, 2026 objective to a section, lab and evidence artifact.
- [ ] I can select serverless, job, classic, SQL warehouse, pipeline, shared/dedicated compute and pooling from requirements.
- [ ] I can configure runtime/Spark, Photon, workers/autoscaling, termination, node type, libraries, policies and permissions.
- [ ] I can design and create catalogs, schemas, volumes, tables, views, materialized views, connections and foreign catalogs.
- [ ] I can explain and test Genie instructions as semantic guidance, not authorization.
- [ ] I can grant least privilege to Databricks groups/service principals and separately configure Azure managed-identity storage access.
- [ ] I can implement ABAC, tags, row filters and column masks with current limitations.
- [ ] I can use Key Vault-backed secrets only where passwordless identity is unavailable.
- [ ] I can manage comments, retention, Catalog Explorer lineage/history/dependencies and audit evidence.
- [ ] I can design/revoke/audit secure Delta Sharing.
- [ ] I can choose source extraction, ingestion tool, batch/stream, format, grain, SCD, temporal and layout strategy.
- [ ] I can implement Lakeflow Connect/notebook/SQL/Auto Loader/Structured Streaming/Event Hubs/Lakeflow pipeline ingestion.
- [ ] I can profile, type, deduplicate, transform, merge and reconcile data with SQL and Python.
- [ ] I can enforce schema and manage drift with constraints, expectations and quarantine.
- [ ] I can design notebook/pipeline task order, triggers, schedules, alerts, retries, restarts and repair.
- [ ] I can use Git, testing layers, bundle targets, CLI and REST under a non-personal deployment identity.
- [ ] I can diagnose DAG/stage/task/operator behavior, caching, skew, spill, shuffle and resource bottlenecks.
- [ ] I can maintain Delta tables with the correct clustering, `OPTIMIZE`, deletion-vector and `VACUUM` reasoning.
- [ ] I can stream diagnostics to Log Analytics and configure owned Azure Monitor alerts.
- [ ] I have rechecked the blueprint, lifecycle, AI Skills Navigator assessment, product terminology, runtime/preview support and vendor freshness.

---

## Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick a current primary path, build the labs, and use targeted references/practice for gaps. Times are page-published when available; otherwise they are clearly labeled estimates. Catalogs, access, duration, price and alignment change. DP-750 is new enough that several vendors had no dedicated current course on the pages found; broad Databricks material must be mapped to the March baseline and separately checked against the October revision. Avoid dumps or anything claiming real exam questions.

### Start with Microsoft and Databricks

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official DP-750 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-750) | Public | 30–60 min | Authoritative scope, weights and lifecycle |
| [DP-750T00 Microsoft Learn course](https://learn.microsoft.com/en-us/training/courses/dp-750t00) | Public self-study; paid instructor option | 4 instructor-led days; roughly 25–40 hours self-study/labs (estimate) | Primary structured path across all four domains |
| [Azure Databricks documentation](https://learn.microsoft.com/en-us/azure/databricks/) | Public | 20–40 hours selectively (estimate) | Current Azure-specific product truth and troubleshooting |
| [AI Skills Navigator DP-750 Practice Assessment](https://aiskillsnavigator.microsoft.com/en-us/certifications/microsoft-certified-associate/azure-databricks-data-engineer) | Free account; sign-in required | 45–90 min attempt plus review (estimate) | Official readiness baseline; use explanations to find gaps |
| [Databricks free training](https://www.databricks.com/learn/training/home) | Public/account depending offering | 8–30 hours selectively (estimate) | Platform, Spark, Delta, Unity Catalog and Lakeflow skill building; map to Microsoft objectives |
| [Microsoft exam sandbox](https://aka.ms/examdemo) | Public | 20–30 min | Interface familiarity, not technical preparation |

### Courses, books and video

| Resource | Access | Estimated time | Best use and freshness note |
|---|---|---:|---|
| [O'Reilly Data Engineering with Azure Databricks](https://www.oreilly.com/library/view/data-engineering-with/9781806106370/) | Paid subscription/book | 412 pages / 10h17m previously recorded; current retrieval blocked | April 2026 Azure-specific book spanning setup, ingestion and production; gap-check exact blueprint items such as Genie/ABAC/alerts. |
| [O'Reilly Data Engineering Fundamentals on Databricks](https://www.oreilly.com/videos/data-engineering-fundamentals/10001ACADFORD/) | Paid subscription | 4h31m previously recorded; current retrieval blocked | July 2025 course includes Lakeflow Connect/pipelines/jobs, bundles and Unity Catalog; supplement Azure identity/monitoring specifics. |
| [O'Reilly Data Governance with Unity Catalog on Databricks](https://www.oreilly.com/library/view/data-governance-with/9781098179625/) | Paid subscription/book | 384 pages / 11h34m previously recorded; current retrieval blocked | September 2025 governance depth, including Azure-specific identity and observability. |
| [Pluralsight Manage Data with Azure Databricks and Azure Data Lake](https://www.pluralsight.com/courses/azure-databricks-data-lake-manage-data) | Paid/trial depending plan | 1h39m published; updated July 23, 2025 | Focused ADLS, managed identity, Key Vault, Auto Loader, Delta, Unity Catalog and sharing supplement; not full DP-750 coverage. Its catalog includes credential-passthrough/mount demonstrations; use current Unity Catalog storage guidance for new governed access. Paid lessons were not reviewed. |
| [Databricks YouTube channel](https://www.youtube.com/@Databricks) | Public | 4–15 hours selectively (estimate) | Current product sessions; search by Lakeflow, Unity Catalog, Spark performance and Asset Bundles. |
| [Microsoft Reactor Databricks search](https://www.youtube.com/@MicrosoftReactor/search?query=Azure%20Databricks) | Public | 2–8 hours selectively (estimate) | Azure workshops and architecture; check date/current terminology. |
| [John Savill Databricks search](https://www.youtube.com/@NTFAQGuy/search?query=Databricks) | Public | 1–3 hours selectively (estimate) | Supplemental Azure architecture only, not a complete DP-750 path. |

### Practice and labs

| Resource | Access | Estimated time | Best use and caution |
|---|---|---:|---|
| [Microsoft DP-750 Practice Assessment on AI Skills Navigator](https://aiskillsnavigator.microsoft.com/en-us/certifications/microsoft-certified-associate/azure-databricks-data-engineer) | Free account | 45–90 min per attempt plus remediation (estimate) | Use first as an official diagnostic; sign-in required. |
| [Udemy DP-750 topic search](https://www.udemy.com/courses/search/?q=DP-750) | Paid catalog; price varies | Varies | Search access was blocked during this review; earlier product observations are not a current recommendation. Compare update date, blueprint weights and explanation quality. Reject real-question claims. |
| [Databricks sample datasets and notebooks](https://learn.microsoft.com/en-us/azure/databricks/discover/databricks-datasets) | Public/platform access | 4–12 hours selectively (estimate) | Build reproducible SQL/Python, streaming, quality and performance labs. |
| This guide’s ten labs | Azure/Databricks access; costs vary | 24–48 hours (estimate) | Implementation, failure, security, replay, deployment and recovery evidence rather than passive recall. |

### Useful blog reading with an exercise

- [ABAC, governed tags and classification GA](https://www.databricks.com/blog/abac-row-filtering-and-column-masking-policies-governed-tags-and-data-classification-are-now) — Adriana Ispas, Kristen Wilder, Jacqueline Li, Corey Sunwold, Menglei Sun and Viswesh Periyasamy; May 13, 2026. Use the taxonomy → classification → enforcement explanation to design a tag/owner/test matrix. Check current Azure requirements for propagation delays, exemptions and view identity; the announcement’s immediate-protection language is not a zero-delay guarantee.
- [Lakeflow on Azure Databricks](https://www.databricks.com/blog/modernize-your-data-engineering-platform-lakeflow-azure-databricks) — Joanna Zouhour and Katie Cummiskey; February 10, 2026. Map one ingestion → transformation → orchestration path and assign each component its identity, replay state and alert. Treat customer speed/cost claims as examples, not expected lab results. Newer naming and support rules come from current documentation.

Both public articles were read as supplementary explanations. No linked customer benchmarks, videos, downloads or paid lessons were executed. Relevant [September release notes](https://learn.microsoft.com/en-us/azure/databricks/release-notes/product/2026/september) were cross-checked against feature documentation; staged rollout is not universal availability.

### A practical study sequence

1. Map the official blueprint to current hands-on evidence in 30–60 minutes.
2. Complete the Microsoft Learn path or one current structured path; do not stack passive courses.
3. Build Labs 1–5 while reading exact Unity Catalog, Lakeflow and Delta references for failures.
4. Build Labs 6–10 and retain streaming, bundle, Spark UI/query profile, cost and recovery artifacts.
5. Take the AI Skills Navigator Practice Assessment once; remediate by objective, not answer memory.
6. Use one ethical third-party practice product only if it supplies current, sourced explanations.
7. Recheck the official guide, credential page, runtime/product notices and lifecycle immediately before the exam.

---

*This guide is an independent public-source synthesis. It is not affiliated with or endorsed by Microsoft, Databricks, GitHub, HashiCorp, or any training provider.*
