---
exam_code: DEA-C01
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# DEA-C01 AWS Certified Data Engineer - Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dea-c01-coverage-record). The [official DEA-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html) is authoritative.

**Current baseline:** DEA-C01 exam guide version 1.1, published December 12, 2025; 50 scored plus 15 unscored questions<br>
**Upcoming blueprint change:** None announced in the current guide, revisions page, or certification page as of September 1, 2026.<br>
**Important freshness boundary:** Version 1.1 added LLM-assisted data processing, Apache Iceberg/open-table formats, HNSW and IVF vector indexes, vectorization and Bedrock knowledge-base context, SageMaker Catalog and Unified Studio governance, and related current services. It removed Cloud9, CodeCommit, and AWS SCT from the in-scope service list. Treat version 1.0 courses as gap-fill resources, not complete coverage.<br>
**Official source:** [AWS Certified Data Engineer - Associate exam guide](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html)

## How to use this guide

DEA-C01 is about making data pipelines reliable, economical, secure, and explainable. The target candidate has roughly two to three years of data-engineering experience and one to two years using AWS. You should be able to reason about volume, variety, velocity, access patterns, schema, quality, cost, failure, recovery, identity, and governance—not merely name services.

The live certification page lists a 130-minute, 65-question, USD 150 exam delivered online or at Pearson VUE in English, Japanese, Korean, and Simplified Chinese. The detailed guide identifies 50 scored and 15 unidentified unscored multiple-choice or multiple-response items and a 720 minimum scaled score. Recheck the [live certification page](https://aws.amazon.com/certification/certified-data-engineer-associate/) before scheduling because delivery details are **VERIFY CURRENT**.

Use one decision loop throughout the guide:

1. Characterize the source, consumers, volume, velocity, variety, quality, latency, retention, and regulatory constraints.
2. Decide batch, streaming, change-data-capture, event-driven, request/response, or a justified combination.
3. Select storage from access pattern, consistency, query shape, durability, recovery, scale, and cost—not familiarity.
4. Design replay, idempotency, schema evolution, checkpoints, quality gates, and failure isolation before choosing orchestration.
5. Apply identity, network, encryption, masking, audit, and governance controls across every hop.
6. Measure freshness, completeness, correctness, performance, failure, and cost; make recovery observable and testable.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, operational, or adjacent context that helps explain an objective. It is supporting knowledge, not a claim that the wording appears verbatim in the official objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Data Ingestion and Transformation | 34% | How should data enter, change, and move through a resilient pipeline? |
| Data Store Management | 26% | Which store, model, catalog, format, and lifecycle fit the workload? |
| Data Operations and Support | 22% | How is the pipeline automated, queried, observed, repaired, and quality-controlled? |
| Data Security and Governance | 18% | Who can use which data, through what path, under which protection and evidence? |

The domains reinforce each other. A fast ingestion design is incomplete if it cannot replay; a well-modeled table is incomplete if it is uncataloged; a successful job is incomplete if its data is late or wrong; encryption is incomplete if unauthorized identities can decrypt.

---

## 1. Data Ingestion and Transformation — 34%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain1.html) covers ingestion, transformation, orchestration, programming concepts, IaC, CI/CD, APIs, scheduling, events, rate limits, fan-in/fan-out, replay, distributed processing, containers, and the new LLM-processing skill.

### Choose the ingestion contract

| Pattern | Good fit | Design questions |
|---|---|---|
| Scheduled batch | Files, snapshots, bounded extracts, predictable windows | How is completion detected? Can partial input be quarantined? What is the watermark? |
| Event-triggered batch | Object arrival or business event starts bounded work | Are notifications duplicate or out of order? What proves all required objects arrived? |
| Streaming | Continuous events with seconds-to-minutes latency | What is the partition key, retention, consumer model, checkpoint, late-data policy, and replay plan? |
| Change data capture | Ordered database changes must reach another system | Where is the replication position stored? How are DDL, deletes, ordering, and target idempotency handled? |
| API ingestion | A producer or external service exposes request-driven data | How are pagination, throttling, retries, authentication, and incremental state handled? |

Amazon S3 is a common durable landing zone for batch data. Kinesis Data Streams is a shard-based stream with multiple consumers and configurable retention; Kinesis Data Firehose is managed delivery with buffering and optional transformation; Amazon MSK provides managed Apache Kafka compatibility. DynamoDB Streams captures item-level changes for a bounded retention window. AWS DMS can perform full load plus ongoing changes. These are not interchangeable: choose from source protocol, ownership, ordering, retention, replay, consumer isolation, scale, and operational burden.

For Kinesis, a partition key controls shard placement and therefore ordering and load distribution. A hot partition key creates a hot shard even when total capacity looks sufficient. Consumers must checkpoint after safely processing data, tolerate retries, and handle records more than once. Enhanced fan-out can isolate consumer throughput; ordinary polling shares read capacity. See the [Kinesis Data Streams developer guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) for current mechanics and limits.

Batch ingestion should distinguish file arrival from dataset completeness. Use manifests, control records, expected-count checks, checksums, or upstream completion events. Store raw immutable input when replay and audit matter. A pipeline that overwrites its only copy of source data cannot safely reproduce a transformation.

**Related item:** Exactly-once business outcomes usually come from idempotent sinks, deduplication keys, conditional writes, transaction boundaries, or commutative operations—not from assuming a delivery system never duplicates a message.

### Transform at the appropriate scale

[AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) provides serverless data integration, a catalog, crawlers, jobs, workflows, and related quality capabilities. Use Glue/Spark for distributed transformation and connectors, Lambda for short event-driven work within its current execution constraints, EMR when framework/runtime control or a broader big-data ecosystem is needed, Redshift SQL for warehouse-local ELT, and ECS/EKS when container control is justified.

Understand these transformation decisions:

- **ETL versus ELT:** ETL shapes data before the destination; ELT loads first and uses destination compute. Security, raw-data retention, engine capability, cost, lineage, and latency determine the choice.
- **Row versus columnar:** CSV and JSON are human-friendly or exchange-oriented; Parquet and ORC support typed, columnar analytical reads and compression. File size, partitioning, compression codec, schema, and query engine all affect results.
- **Full versus incremental:** Full reload is simple but may be slow and costly. Incremental work needs a reliable high-water mark, CDC position, job bookmark, merge/upsert rule, late-arrival policy, and replay boundary.
- **Narrow versus wide transformation:** Filters and projections can reduce data early. Joins, aggregations, sorts, and repartitioning often shuffle data; skewed keys can dominate runtime.
- **Managed versus self-managed compute:** More control increases patching, scaling, security, observability, and recovery ownership.

Glue job bookmarks track previously processed data for supported sources, but they are not a universal deduplication guarantee. Define what the bookmark represents, how resets/backfills work, and whether target writes are idempotent. For Spark, choose partitions from data volume and executor resources; avoid both huge partitions and thousands of tiny output files. Push filters down and select only needed columns when the format/source supports it.

### Orchestrate durable workflows

Step Functions expresses state transitions, retries, catches, timeouts, parallel/map work, and service integrations. Amazon MWAA provides managed Apache Airflow for DAG-driven ecosystems. Glue workflows coordinate Glue components. EventBridge routes events and schedules work. Lambda can connect small steps but should not become an invisible, unbounded orchestrator.

A production workflow should make these states explicit:

- input accepted and uniquely identified;
- prerequisites satisfied;
- transformation started with immutable parameters/code version;
- quality gate passed or quarantined;
- publication committed atomically or by a clear manifest/pointer;
- downstream notification delivered;
- retry, timeout, cancellation, compensation, and human escalation recorded.

Retries require backoff, jitter where appropriate, bounded attempts, and classification of transient versus permanent errors. Retrying a non-idempotent write can corrupt data. Dead-letter queues or failure destinations preserve work for investigation but do not themselves replay safely.

### Apply engineering practices

Keep pipeline code, SQL, schemas, infrastructure, quality rules, and configuration under version control. Separate environment-specific values from logic. Test transformations with small deterministic fixtures, contract/schema cases, boundary values, duplicates, late events, missing values, and failure paths. Deploy resources through CloudFormation, CDK, SAM, or another governed IaC process; the current blueprint explicitly expects IaC and CI/CD concepts.

The version 1.1 objective to integrate LLMs for data processing does not make DEA-C01 a model-training exam. An LLM can classify, extract, summarize, or normalize ambiguous text, but its output is probabilistic. Define schema-constrained output, source grounding, validation, confidence/escalation, sensitive-data handling, prompt/model versioning, evaluation data, cost/latency budgets, and deterministic fallbacks. Never silently treat generated values as authoritative records.

**Related item:** A pipeline has both a control plane and a data plane. Orchestration, deployment, catalog changes, policy, and schedules control work; records and files are the data. Debugging becomes clearer when you identify which plane failed.

---

## 2. Data Store Management — 26%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain2.html) covers store selection, catalogs, lifecycle, schemas, lineage, open-table formats, vector indexes, and optimization.

### Select from the access pattern

| Need | Likely starting point | Key tradeoffs to verify |
|---|---|---|
| Durable object data lake | S3 | Object semantics, format, partitioning, request/query cost, lifecycle, governance |
| Analytical warehouse | Redshift | Workload isolation, distribution, sort/layout, concurrency, materialization, serverless/provisioned economics |
| Serverless SQL over S3/catalog | Athena | Scanned bytes, partition pruning, file format/size, catalog accuracy, workgroups, result controls |
| Relational transactions | RDS or Aurora | Engine compatibility, indexes, connections, replicas, failover, backup, scaling |
| Key-value/document access at scale | DynamoDB | Partition/sort keys, item size, access patterns, capacity mode, indexes, consistency, hot keys |
| Distributed Spark/Hadoop ecosystem | EMR | Runtime/framework control, cluster/serverless choice, storage separation, tuning, operations |
| Real-time stream retention | Kinesis or MSK | Producer protocol, partitioning, ordering, consumer model, replay, operational ownership |
| Search/log/vector use cases | OpenSearch Service | indexing, shard design, refresh, durability, query needs, vector behavior, cost |
| Low-latency in-memory key/value | ElastiCache or MemoryDB | durability, consistency, engine semantics, memory cost, eviction, availability |

[Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) is a managed analytical warehouse; Athena queries supported formats in S3 without managing a cluster. Redshift Spectrum lets Redshift query external S3 data. Federated query reaches supported operational sources. A materialized view stores results for faster reuse but must be refreshed and adds storage/maintenance tradeoffs. Do not infer that “serverless” means cheaper: compare workload shape, idle time, concurrency, data scanned, performance target, and operating effort.

DynamoDB modeling begins with known access patterns. A partition key distributes items; a sort key groups ordered related items. Global secondary indexes enable different partition/sort keys and have their own capacity/storage/write implications. Local secondary indexes share a partition key and have creation and size constraints. Avoid scans when a keyed query fits. Use TTL for asynchronous expiry, not exact-time deletion or a compliance proof by itself.

### Design lake data intentionally

For S3 analytical data, partition by columns frequently used to filter and with practical cardinality. Excessively granular partitions and tiny files increase listing, planning, and request overhead. Columnar formats reduce scanned data when queries need subsets of columns. Compression saves storage and I/O but costs CPU and must be supported by readers. Validate assumptions with real query plans and metrics; see [S3 performance guidance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html).

Apache Iceberg is an open table format that tracks table metadata and snapshots over object files. It can support schema evolution, partition evolution, time travel, and atomic table changes through compatible engines. The table format does not remove the need to manage file sizes, snapshot retention, orphan files, catalog integration, engine/version compatibility, permissions, and concurrency. Use the current [Athena Iceberg documentation](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html) for supported behavior.

**Related item:** A lakehouse is an architectural pattern, not one service. It combines low-cost object storage with table metadata, governance, transaction-like behavior, multiple engines, and warehouse-style management. Interoperability depends on actual feature/version compatibility.

### Catalog technical and business meaning

The Glue Data Catalog stores database, table, schema, location, partition, and related metadata used by Glue, Athena, EMR, Redshift Spectrum, and Lake Formation integrations. Crawlers infer schemas; inference can be wrong or change unexpectedly, so control classifiers, schema-change policy, recrawl scope, and table naming. Partition projection can avoid enumerating predictable partitions; explicit catalog partitions remain appropriate elsewhere.

SageMaker Catalog/Unified Studio adds business discovery, domain/project organization, governed access, and lineage-oriented workflows in the current blueprint. Names, integrations, and release behavior are **VERIFY CURRENT**. Distinguish:

- technical metadata: type, column, location, format, partition, owner, job, run;
- business metadata: definition, steward, classification, approved use, quality expectation;
- operational metadata: freshness, row counts, failures, SLA/SLO, cost;
- lineage: source-to-transformation-to-output relationships and version/run context.

A catalog does not guarantee trustworthy data. Ownership, curation, quality, access workflows, lineage, and lifecycle make metadata useful.

### Evolve schemas and models safely

Classify changes as additive, compatible, breaking, semantic, or storage-layout changes. Adding an optional nullable field may be compatible; changing a type, meaning, unit, time zone, key, or required status may not be. Producers and consumers can deploy at different times, so use contracts, compatibility checks, versioning, dual-read/write transitions, backfills, and deprecation periods.

For analytical modeling, understand facts, dimensions, grain, surrogate/natural keys, slowly changing dimensions, star schemas, and denormalization. For DynamoDB, model items and indexes around requests rather than normal forms. For Redshift, distribution and sort/layout choices influence data movement and pruning, but current automated features can change tuning recommendations—verify behavior and measure.

Vectorization turns content into numeric embeddings. Approximate-nearest-neighbor indexes trade exactness for speed/scale. HNSW uses a navigable graph and often favors strong recall/low query latency at memory/build cost; IVF partitions vector space into lists and searches selected lists, trading training/tuning and recall for efficiency. Treat these as conceptual comparisons and consult the specific engine because parameters and support vary. A Bedrock knowledge base connects ingestion, chunking, embeddings, vector storage/retrieval, and generation; it does not eliminate source permissions, freshness, deletion, quality, or evaluation.

### Manage lifecycle and recovery

S3 Lifecycle can transition or expire eligible current/noncurrent objects. Versioning protects against some overwrites/deletes but retains versions and cost. Object Lock supports retention controls where configured. DynamoDB TTL expires items asynchronously. Redshift `COPY` and `UNLOAD` move data between S3 and tables. Choose backup, replication, retention, archival, and deletion from RPO, RTO, legal hold, sovereignty, recovery testing, and cost.

Deletion is a system-wide process. Find source, replicas, caches, extracts, indexes, streams, backups, catalogs, lineage, and downstream products. Some backups must age out under an approved retention policy rather than be surgically edited. Record the policy and evidence; do not promise instantaneous erasure when the platform does not provide it.

---

## 3. Data Operations and Support — 22%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain3.html) covers automation, analysis, SQL, visualization, monitoring, audit, troubleshooting, and data quality.

### Operate outcomes, not job status

A green job only proves that its process returned success. Monitor the data product:

| Dimension | Example measure |
|---|---|
| Freshness | source watermark to published watermark lag |
| Completeness | expected partitions/files/records received |
| Validity | fields conforming to type, range, pattern, or reference rules |
| Uniqueness | duplicate business keys or event IDs |
| Consistency | reconciliation across source, stages, and target |
| Accuracy | sampled comparison with an authoritative source or reviewed labels |
| Performance | end-to-end latency, job duration, throughput, queue/backlog |
| Reliability | success rate, retries, time to detect/recover, replay success |
| Cost | per run, record, TB processed, consumer, or data product |

Use CloudWatch metrics, logs, alarms, and dashboards; CloudTrail for account/API activity; service job histories; Spark/engine logs; EventBridge/SNS for routing/notification; and data-quality results. Carry a correlation value such as dataset/run/batch ID through orchestration, logs, manifests, and audit records.

Troubleshoot in an evidence chain: symptom → affected dataset/consumer → last good watermark → recent code/schema/config/permission/quota change → source completeness → orchestration state → compute/logs → target commit → quality result → publication/consumer. Preserve failed inputs and run parameters before retrying.

### Understand query and engine behavior

In Athena, reduce scanned bytes with columnar formats, compression, partition pruning, and selecting only required columns. Use workgroups for controls and isolation. In Redshift, examine query plans, data movement, join distribution, skew, spill, workload management, concurrency, table statistics/layout, and materialization. In Spark/Glue/EMR, inspect stages, tasks, shuffles, partition sizes, skew, executor memory/GC, spills, retries, and small files.

SQL readiness includes joins, set operations, filtering, grouping, aggregations, window functions, conditional logic, null semantics, pivots/unpivots where supported, views, and rolling calculations. Know the intended grain before joining; many-to-many joins can multiply rows without an error. A rolling average needs an ordered window and an explicit frame. `NULL` is unknown, so comparisons and aggregates have rules that differ from empty strings or zero.

Amazon Quick is the current name listed in the DEA-C01 service scope, while detailed objective text may still mention QuickSight. Product names and capabilities are **VERIFY CURRENT**. Visualization is useful for profiling and communicating quality, but charts do not replace deterministic checks or reconciliations.

### Build quality into the pipeline

[AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-gs-studio.html) can define and evaluate rules on cataloged or job data. Whether using it, DataBrew, SQL, Spark, or custom code, separate:

- structural checks: schema, types, required fields, parseability;
- semantic checks: valid states, ranges, units, referential integrity;
- statistical checks: distribution drift, anomaly, unexpected volume;
- reconciliation: counts, sums, checksums, control totals across stages;
- timeliness: event time, processing time, watermark, late-arrival threshold.

Decide whether each failure blocks publication, quarantines records, warns, or requires approval. Store rejected data with reason and lineage. Thresholds should reflect business risk and expected variability, not arbitrary perfection. Sampling lowers cost but may miss rare defects; stratify or target high-risk records when appropriate.

Data skew can mean a statistical distribution or an execution imbalance. For distributed compute, a dominant key sends disproportionate records to one partition/task. Diagnose task-duration and partition-size outliers. Remedies include better keys, salting, pre-aggregation, broadcast joins for suitable small data, adaptive query execution where supported, or isolating exceptional keys. Each remedy changes complexity or semantics; measure it.

**Related item:** Data observability links pipeline telemetry to data semantics. Infrastructure can be healthy while a source silently stops sending one category of records; freshness, schema, distribution, lineage, and reconciliation close that gap.

---

## 4. Data Security and Governance — 18%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain4.html) covers authentication, authorization, network paths, credentials, encryption, masking, audit, privacy, sovereignty, Lake Formation, and current SageMaker Catalog governance.

### Separate identity, permission, and path

Authentication establishes identity; authorization decides allowed actions/resources/conditions. IAM roles provide temporary credentials to workloads and people through an assumed-role flow. Resource policies, identity policies, permission boundaries, session policies, service control policies, VPC endpoint policies, Lake Formation permissions, KMS key policies/grants, and service-native database permissions can all affect access.

Evaluate a denial systematically: principal and session → requested action/resource → explicit denies → organization/boundary/session constraints → identity/resource grants → KMS/key access → Lake Formation/data-store grants → network/DNS/endpoint path → application credentials. The [IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) is the authoritative starting point.

Use Secrets Manager for governed secret storage and rotation integrations where appropriate; Parameter Store can hold configuration and secure strings. Do not place static credentials in code, images, notebooks, logs, connection strings, or IaC state. A secret rotation is complete only when the producer, consumers, connection pools, fallback/rollback, and audit trail work.

Lake Formation provides data-lake permissions integrated with cataloged resources and supported engines. Understand database/table/column/row controls, data-location permissions, grants, cross-account sharing, and the interaction with IAM. A broad IAM permission does not automatically substitute for Lake Formation authorization, and vice versa.

### Protect data and keys

Encrypt in transit with supported TLS and private/network controls when required. Encrypt at rest with service-managed or customer-managed KMS keys according to control needs. A caller needs both data-plane authorization and usable key authorization/context. Cross-account encryption requires aligned resource policy, key policy/grant, IAM permission, region, and service support. Rotation changes key material under a logical key for supported KMS rotation; it does not automatically re-encrypt all existing data.

Masking hides values in approved query or presentation paths. Tokenization substitutes a controlled token; hashing is one-way only when designed safely and remains vulnerable to guessing for small domains; encryption is reversible with a key. Anonymization aims to prevent re-identification and requires more than deleting a name. Apply controls at ingestion, storage, processing, sharing, logs, extracts, and non-production copies.

[Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) discovers and reports sensitive data in S3 through managed/custom identifiers and findings. A finding drives investigation and policy; it does not automatically prove classification completeness or remediate every copy.

### Produce audit evidence

CloudTrail answers which supported API activity occurred; CloudWatch Logs stores/query application and service logs; CloudTrail Lake supports event data stores and SQL queries over retained events; AWS Config records supported resource configuration state/change. Preserve time synchronization, region/account coverage, organization trails where applicable, log destination protection, encryption, retention, access separation, validation, and alerting.

Audit logging must avoid leaking secrets or sensitive rows. Record identity, action, target, result, time, source context, run/build/version IDs, and approval where appropriate. Separate operators who administer the pipeline from those who can alter audit evidence when the risk requires it.

### Govern sharing, privacy, and sovereignty

For every data product, identify owner, steward, producer, consumers, lawful/approved purpose, classification, retention, residency, quality SLO, lineage, and access-review process. Prefer governed shares or cross-account access over uncontrolled copies. Redshift data sharing can expose live governed data across consumers without an ETL copy, subject to current support and permissions; copied exports create another lifecycle to manage.

Sovereignty includes where data, metadata, keys, logs, replicas, backups, support access, and processing occur. Blocking a resource deployment in one Region is insufficient if replication, exports, pipelines, or logs can cross the boundary. Use organization policies, region controls, preventive/detective controls, catalog classifications, network architecture, key policies, and evidence appropriate to the requirement.

SageMaker Unified Studio domains, domain units, projects, and Catalog access appear in version 1.1. Treat their exact product behavior as **VERIFY CURRENT**. The durable idea is delegated, project-oriented governance: approved identities receive bounded access to discover, request, create, and share data/analytics assets, with ownership and lineage.

**Related item:** Governance is a lifecycle control system. A one-time access approval without periodic review, purpose limits, lineage, deletion, and monitoring is only a ticket—not durable governance.

---

## Integrated scenarios

### Scenario 1: Replayable retail ingestion

A retailer receives hourly partner files and continuous checkout events. Land immutable batch files in S3 with a manifest and checksum. Stream checkout events through Kinesis with a partition key that preserves required ordering without creating hot shards. Store event IDs and checkpoints; make downstream writes idempotent. Transform into typed columnar tables, quarantine malformed records, and publish only after completeness and reconciliation gates pass. Catalog technical/business metadata and keep run-to-output lineage.

If a transformation defect is found, select affected source/run versions, write corrected output to a new snapshot or partition, validate it, and atomically change the published pointer/table metadata. Do not append a second unmarked copy and hope consumers deduplicate it.

### Scenario 2: Governed lakehouse and warehouse

An enterprise keeps raw and curated data in S3/Iceberg and serves finance aggregates in Redshift. Glue Catalog records schemas/locations; Lake Formation grants project- and column/row-scoped access; KMS protects storage; Macie helps discover unexpected sensitive S3 data. Athena supports ad hoc lake queries while Redshift serves repeated governed analytics. Model facts at an explicit grain, manage schema compatibility, compact small files, expire superseded snapshots under policy, and reconcile warehouse totals to curated source snapshots.

Choose sharing over copies when requirements and service support allow it. If a consumer needs an export, assign ownership, encryption, retention, residency, revocation, and deletion evidence to the new copy.

### Scenario 3: Failed overnight pipeline

The dashboard is green but yesterday’s sales are low. Start at freshness and reconciliation, not instance CPU. Identify the last good source and published watermarks. Check expected partner manifests, stream backlog, orchestration branch states, Glue/Spark skew and failed tasks, schema/crawler changes, permissions/KMS, target transaction/manifest, quality quarantine volume, and dashboard refresh. Correlate CloudTrail configuration changes and deployment version.

Stabilize by pausing publication or marking the data stale, preserve failed input, repair the smallest cause, replay from a known boundary, reconcile results, and communicate consumer impact. Then add a completeness/freshness alarm and a tested runbook so a green job cannot mask missing data again.

---

## Hands-on labs

Use a sandbox account, least privilege, budgets, synthetic data, and cleanup. Service availability and cost are **VERIFY CURRENT**.

### Lab 1: Batch contract and catalog

Create a small synthetic CSV dataset with valid, duplicate, malformed, and late records. Land it in S3 under raw/date/run prefixes with a manifest. Catalog it with Glue, inspect inference, then define a controlled schema. Query counts and nulls with Athena. Deliverable: source contract, manifest, catalog diff, query evidence, and cleanup record.

### Lab 2: Idempotent event pipeline

Send synthetic events to Kinesis or a locally simulated equivalent. Choose partition keys, attach unique event IDs, checkpoint only after successful processing, and write conditionally/deduplicate at the target. Replay the same batch and prove business totals do not change. Deliverable: ordering/replay assumptions and before/after reconciliation.

### Lab 3: Transformation and file-layout experiment

Transform the same dataset into CSV and Parquet with two partition strategies and deliberately create a tiny-file variant. Compare object counts, bytes scanned, query latency, and cost indicators in Athena. Deliverable: evidence-backed layout choice and compaction rule.

### Lab 4: Orchestration failure paths

Model ingest → transform → quality → publish with Step Functions or a local state-machine diagram plus executable scripts. Add timeout, retry, permanent validation failure, quarantine, notification, and a manual approval/rollback branch. Force each failure. Deliverable: state history and proof that incomplete output is not published.

### Lab 5: Schema evolution and Iceberg

Create a small Iceberg table in a supported sandbox or use local Spark/Iceberg. Add a nullable column, rename/evolve a field where supported, append a late partition, query an earlier snapshot, and document engine compatibility. Deliverable: compatibility matrix and snapshot/file-retention plan.

### Lab 6: Data-quality gate

Define completeness, uniqueness, range, reference, freshness, and reconciliation checks using Glue Data Quality, SQL, or code. Assign block/quarantine/warn outcomes. Test both a valid and intentionally bad batch. Deliverable: rule rationale, results, quarantined records, and publication decision.

### Lab 7: Least-privilege governed access

Create producer and consumer roles around a small S3/cataloged dataset. Restrict access with IAM and, if available, Lake Formation; use a customer-managed KMS key. Test allowed and denied actions, then rotate a test secret. Deliverable: access matrix, policy-evaluation explanation, KMS dependency, and audit events.

### Lab 8: Operational game day

Inject one missing file, one skewed key, one incompatible schema, and one permission failure across separate runs. Use run IDs, metrics, logs, CloudTrail, data-quality results, and reconciliations to diagnose each without changing several variables at once. Replay safely and confirm recovery. Deliverable: four evidence chains plus preventive controls.

---

## Original knowledge checks

These are independent prompts, not recalled or reconstructed exam items.

1. Why is an S3 object-created notification insufficient proof that an hourly dataset is complete?
2. Which properties make Kinesis Data Streams a better fit than managed delivery through Firehose for a given workload?
3. How can a poor partition key cause throttling despite acceptable aggregate stream traffic?
4. Where should a consumer checkpoint, and why must its target write still be idempotent?
5. What state is required to replay a CDC pipeline safely after a partial target failure?
6. When would a manifest be safer than discovering all files under a prefix?
7. Why can a Glue job bookmark fail to prevent duplicate business records?
8. Which clues indicate that a Spark job is slowed by skew rather than insufficient total compute?
9. When is Lambda a poor choice for a transformation despite event-driven invocation?
10. What must be tested before an LLM-derived field is published as governed data?
11. How do retries change the design of a non-idempotent workflow step?
12. What is the distinction between EventBridge routing and Step Functions orchestration?
13. Why might Parquet reduce Athena cost relative to CSV?
14. How can over-partitioning a lake harm query planning and operations?
15. When would Redshift be preferable to Athena, and when would the reverse be true?
16. Why does DynamoDB schema design begin with access patterns?
17. What makes a DynamoDB partition key hot, and which remedies preserve request semantics?
18. What operational work remains after adopting an Iceberg table?
19. Which schema changes are syntactically additive but semantically breaking?
20. How do technical catalog metadata and business catalog metadata complement each other?
21. Why is lineage incomplete if it records only source and destination table names?
22. How do HNSW and IVF broadly trade build/storage/query behavior and recall?
23. Why does a vector store not make a Bedrock knowledge base automatically accurate or authorized?
24. What is the difference between S3 expiration, versioning, and Object Lock?
25. Why is DynamoDB TTL not an exact-time compliance deletion mechanism?
26. What does a successful pipeline job fail to prove about its data product?
27. How would you distinguish missing input from a failed transformation using watermarks and manifests?
28. Why can a many-to-many SQL join silently corrupt analytical totals?
29. Which metrics reveal small-file and shuffle problems?
30. How should a quality rule’s block, quarantine, or warning outcome be chosen?
31. When does sampling provide weak assurance for rare but severe defects?
32. What evidence should accompany a safe backfill?
33. Why can an IAM `Allow` still result in denied access to encrypted lake data?
34. What is the authorization relationship among IAM, Lake Formation, and KMS?
35. Why should application secrets never be placed in notebooks or IaC state?
36. What must be coordinated when rotating a database credential?
37. How do masking, tokenization, hashing, and encryption serve different goals?
38. What does a Macie finding establish, and what does it not establish?
39. Which audit controls protect evidence from the same operator who runs the pipeline?
40. Why must a copied data share receive its own retention, residency, and deletion controls?

---

## Readiness checklist

- [ ] I can map every published task in all four domains to an implementation or decision.
- [ ] I can choose batch, streaming, CDC, event-driven, and API ingestion from requirements.
- [ ] I can explain ordering, partitioning, throttling, fan-out, checkpointing, idempotency, and replay.
- [ ] I can compare Glue, EMR, Lambda, Redshift, containers, and SQL-based transformation.
- [ ] I can design explicit workflow retries, timeouts, quarantine, publication, and rollback.
- [ ] I can choose S3/Athena, Redshift, RDS/Aurora, DynamoDB, EMR, Kinesis/MSK, and OpenSearch from access patterns.
- [ ] I can explain file formats, partitioning, compression, small files, Iceberg, catalogs, lineage, lifecycle, and schema evolution.
- [ ] I can write and diagnose the SQL concepts named in this guide.
- [ ] I can measure freshness, completeness, validity, uniqueness, consistency, performance, reliability, and cost.
- [ ] I can diagnose a pipeline from source evidence through publication and consumer refresh.
- [ ] I can distinguish IAM, resource, organization, boundary, session, endpoint, Lake Formation, KMS, and database authorization.
- [ ] I can design encryption, secrets, masking, audit, privacy, sharing, deletion, and sovereignty controls.
- [ ] I have gap-checked any version 1.0 course against the December 2025 version 1.1 revisions.
- [ ] I have completed at least one replay/backfill and one failure-injection exercise.
- [ ] I reject dumps, recalled questions, and “real exam question” claims.

---

## Places to learn

This is **not a complete list** and is not meant to be consumed in full. Pick one structured route, use official documentation for gaps, perform the labs, and add one legitimate practice source. Time estimates combine provider-published runtime where available with clearly labeled library estimates for practice and review. Access, price, duration, and freshness are **VERIFY CURRENT**.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official exam guide, four domain pages, in-scope list, and v1.1 revisions](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html) | Free | 3–5 hours to map and gap-check |
| [AWS Skill Builder DEA-C01 exam-prep plan](https://skillbuilder.aws/category/exam-prep/data-engineer-associate-DEA-C01) | Mix of free and subscription content | About 6 hours for the standard course; 13+ hours for enhanced prep, plus labs/practice; verify current catalog |
| [Pluralsight DEA-C01 path](https://www.pluralsight.com/paths/aws-certified-data-engineer-associate-dea-c01) | Subscription/trial terms vary | 17 listed hours: six courses, one lab, and practice exam; add 10–20 hours hands-on |
| [O'Reilly AWS Certified Data Engineer Associate Study Guide](https://www.oreilly.com/library/view/aws-certified-data/9781098170066/) | Subscription or book purchase | 12 hours 52 minutes listed / 476 pages, plus 12–20 hours labs and review |
| [O'Reilly/Sybex AWS Certified Data Engineer Study Guide](https://www.oreilly.com/library/view/aws-certified-data/9781394286584/) | Subscription or book purchase | 18 hours 22 minutes listed / 656 pages, plus practice; gap-check December 2025 additions |
| [Udemy — Nikolai Schuler](https://www.udemy.com/course/aws-certified-data-engineer-associate-dea-c01/) | Paid; sales/subscription vary | 22 hours 17 minutes video plus 12–25 hours demos and review; updated August 2026 when checked |
| [Coursera — Neal Davis and Wayde Gilchrist](https://www.coursera.org/learn/aws-certified-data-engineer-associate-exam-prep) | Subscription/audit terms vary | 11 modules and 10 assignments; plan 12–24 hours, recently updated April 2026 |
| [LinkedIn Learning DEA-C01 Cert Prep](https://www.linkedin.com/learning/aws-certified-data-engineer-associate-dea-c01-cert-prep/the-dea-c01-exam) | Subscription/trial terms vary | Plan 4–8 hours video/review; verify full runtime and v1.1 coverage after sign-in |
| [Tutorials Dojo DEA-C01 video course](https://portal.tutorialsdojo.com/courses/aws-certified-data-engineer-associate-dea-c01-video-course/) | Paid | 16+ video hours, 10+ labs, and one 65-question simulator; add 8–16 hours practice |
| [Tutorials Dojo DEA-C01 practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-data-engineer-associate-practice-exam-dea-c01/) | Paid | 13 listed quizzes across randomized, timed, review, and domain modes; plan 8–14 hours with explanation review |
| [Whizlabs DEA-C01 course, labs, and practice](https://www.whizlabs.com/aws-certified-data-engineer-certification-exam/) | Paid/free sample | 134 videos and 38 labs listed; plan 25–45 hours selectively because a stable combined runtime was not exposed |
| [Johnny Chivers DEA-C01 full course](https://www.youtube.com/watch?v=6G0bLDIcO7Y) | Free YouTube | 4 hours 45 minutes video plus 8–16 hours reproducing selected demos; older baseline, so close all v1.1 gaps |
| [AWS Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html) | Free | 3–6 hours selected design review; adjacent architecture depth, not an exam course |

Use official practice question sets, pretests, and practice exams through the current AWS Skill Builder plan when available. No exact current MeasureUp DEA-C01 product was independently verified, so none is inferred. Third-party questions should explain why options are right or wrong and cite documentation; reject any resource advertising recalled, leaked, or “actual” exam items.

### A practical 6–8 week route

- **Week 1:** Map the official guide and version 1.1 revision; baseline SQL, IAM, S3, and distributed-data concepts.
- **Weeks 2–3:** Ingestion/transformation and Labs 1–4; emphasize replay, partitions, Glue/Spark, orchestration, and failure.
- **Week 4:** Stores, modeling, catalog, Iceberg, vector concepts, and Lab 5.
- **Week 5:** Monitoring, SQL/query optimization, data quality, and Lab 6.
- **Week 6:** IAM/Lake Formation/KMS, audit, privacy, sovereignty, and Lab 7.
- **Weeks 7–8:** Game day, weak-domain remediation, timed legitimate practice, and teach-back of every service choice.

---

## Source map and maintenance boundary

Primary scope and status evidence:

- [Official DEA-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html)
- [Domain 1: Data Ingestion and Transformation](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain1.html)
- [Domain 2: Data Store Management](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain2.html)
- [Domain 3: Data Operations and Support](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain3.html)
- [Domain 4: Data Security and Governance](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01-domain4.html)
- [In-scope AWS services](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/dea-01-in-scope-services.html)
- [Version 1.1 revisions](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/dea-01-revisions.html)
- [Live certification page](https://aws.amazon.com/certification/certified-data-engineer-associate/)

Implementation references used for deeper explanation:

- [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
- [S3 performance guidance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html)
- [Athena with Iceberg](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
- [Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-gs-studio.html)
- [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [AWS Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html)

The blueprint, detailed domains, revisions, in-scope list, AWS names/features/limits, delivery contract, prices, languages, and every learning-provider listing are volatile. The weekly source monitor should flag changes; a human must interpret them before rewriting the guide. “SOURCES + OBJECTIVES CHECKED” means traceability and automated checks passed—not that AWS or a community reviewer endorsed the content.

## Exam-integrity boundary

This guide is an original synthesis of public objectives and documentation. It does not contain recalled exam questions, leaked items, copied vendor question banks, paid-course reproductions, or claims about what appeared on a live exam. Use practice material to learn decision-making, then verify technical behavior in current first-party documentation.
