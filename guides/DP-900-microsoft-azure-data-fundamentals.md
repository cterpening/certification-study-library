---
exam_code: DP-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# DP-900 Microsoft Azure Data Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dp-900-coverage-record). The [official DP-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) is authoritative.

**Current baseline:** Skills measured as of July 21, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [DP-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)

## How to use this guide

Learn the shape and use of data before memorizing an Azure service. For every scenario, identify the workload pattern, structure, access and consistency needs, scale, latency, governance, and consumer. Then choose a data store or analytics service and explain why a nearby option is less suitable.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe core data concepts | 25–30% | What kind of data and workload is this? |
| Identify considerations for relational data on Azure | 20–25% | When do tables, keys, constraints, and SQL fit? |
| Describe considerations for working with non-relational data on Azure | 15–20% | Which flexible or specialized data model fits the access pattern? |
| Describe an analytics workload on Azure | 25–30% | How does data move from source to insight? |

---

## 1. Core data concepts

### Data representation

| Shape | Characteristics | Examples |
|---|---|---|
| Structured | Fixed schema, predictable fields and types | Relational rows, transaction records |
| Semi-structured | Self-describing records with flexible fields | JSON, XML, event messages |
| Unstructured | No tabular schema inherent in the content | Images, audio, video, documents |

The representation does not dictate one store. JSON can be placed in a file, document database, or relational column; the right choice depends on access, transaction, scale, querying, governance, and integration requirements.

Common file formats include delimited text such as CSV, JSON, XML, Parquet, Avro, images, audio, and video. CSV is simple and widely interoperable but carries limited type/schema metadata. Parquet is a compressed columnar format well suited to analytical scans because an engine can read selected columns rather than entire records.

> **Related item:** A schema is a contract between producers and consumers. Schema-on-write validates structure before data is stored; schema-on-read interprets structure when data is consumed. Neither eliminates the need for data-quality tests and versioning.

### Operational and analytical workloads

Online transaction processing (OLTP) systems support frequent, small, concurrent operations such as placing an order or changing an address. They favor current state, predictable transactions, fast point lookups, and normalized structures that avoid inconsistent duplication.

Analytical systems support scans, aggregations, historical comparison, and exploration across large datasets. They often use denormalized star schemas, columnar storage, distributed processing, and data copied from operational systems so analysis does not disrupt transactions.

| Characteristic | Transactional | Analytical |
|---|---|---|
| Typical operation | Insert/update/read a few records | Scan, join, group, aggregate many records |
| Time focus | Current operational state | Historical and cross-domain trends |
| Modeling tendency | Normalized entities | Facts, dimensions, denormalized views |
| Users | Applications and operations | Analysts, data scientists, decision makers |
| Optimization | Concurrency and transaction latency | Throughput and query performance |

ACID describes atomicity, consistency, isolation, and durability for transaction behavior. It is not synonymous with a relational database, and “NoSQL” does not automatically mean transactions are absent. Capabilities and scope vary by engine.

### Data roles

| Role | Primary focus |
|---|---|
| Database administrator | Availability, security, backup/recovery, performance, and database operations |
| Data engineer | Ingestion, transformation, storage, quality, orchestration, and dependable data products |
| Data analyst | Modeling, visualization, interpretation, and decision support |

Data scientists and application developers are related consumers/builders, but the current blueprint emphasizes the three roles above. In small organizations one person may perform several roles; responsibilities still exist even when titles differ.

### A repeatable data-choice method

When a question describes a dataset, do not jump from a file extension to a product. Work through these questions in order:

1. **What is the business operation?** Recording an order and calculating a five-year sales trend are different workloads even if both use sales data.
2. **How is the data shaped?** Identify fixed rows, self-describing records, binary objects, relationships, or a continuous event stream.
3. **How will it be accessed?** Point lookup, transaction, file sharing, object retrieval, relationship traversal, broad scan, and aggregation favor different designs.
4. **What guarantees matter?** Consider transaction scope, consistency, durability, recovery, and acceptable staleness.
5. **What scale and latency are required?** Include both total data and whether requests are evenly distributed.
6. **Who operates and consumes it?** Administration responsibility, SQL/Spark skills, reporting tools, governance, and cost are part of the choice.

| Scenario clue | First interpretation | Do not assume |
|---|---|---|
| “Update an order and payment together” | Transaction boundary and atomicity matter | Every relational service has identical compatibility |
| “Keep product images and PDFs” | Object/blob storage is a natural starting point | Unstructured means unsearchable or ungoverned |
| “Retrieve a customer profile by ID at global scale” | Key/document access and partitioning matter | NoSQL removes schema and consistency decisions |
| “Analysts scan several years of history” | Separate analytical serving from the operational path | A data lake alone supplies a business-ready model |
| “React to sensor readings within seconds” | Streaming ingestion and event processing matter | Every downstream consumer must also be real time |

The official [core data concepts module](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/) uses formats, file and database storage, and transactional versus analytical processing as separate concepts. Keep those dimensions separate in your reasoning.

> **Related item:** A format describes how bytes are encoded; a data model describes how information is organized; a store persists it; and an engine processes it. One product may cover several layers, but the layers are not synonyms.

### Data quality and governance

Accuracy, completeness, consistency, timeliness, uniqueness, and validity are useful quality dimensions. A technically successful pipeline can still deliver wrong business outcomes if definitions differ or late/missing data is silently accepted.

Governance establishes ownership, discovery, classification, access, retention, lineage, and acceptable use. Microsoft Purview provides data-governance and compliance capabilities across data estates. It does not replace source-system controls or responsible owners.

> **Related item:** Data lineage records where data came from and how it changed. It reduces diagnosis time when a dashboard value is questioned, but lineage alone does not prove that the transformation was correct.

---

## 2. Relational data

### Tables, keys, and relationships

A relational model stores data in tables. Each row represents an instance; columns represent attributes with types and constraints. A primary key uniquely identifies a row. A foreign key references a key in another table and supports referential integrity.

| Relationship | Example | Modeling note |
|---|---|---|
| One-to-one | Person to one profile | May be separated for optional/security/lifecycle reasons |
| One-to-many | Customer to orders | Foreign key commonly appears on the many side |
| Many-to-many | Students to courses | Junction table holds the two foreign keys and relationship attributes |

Normalization separates repeated facts to reduce anomalies. For example, storing a customer address on every order line creates inconsistent updates. Denormalization duplicates selected data to improve read performance or simplify analytics, accepting additional synchronization responsibility.

### SQL and database objects

SQL is a declarative language: state the result or change, and the database optimizer chooses an execution plan. Core operations include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`; clauses such as `WHERE`, `JOIN`, `GROUP BY`, and `ORDER BY` shape results.

```sql
SELECT c.CustomerName, SUM(o.TotalAmount) AS Revenue
FROM Customers AS c
JOIN Orders AS o ON o.CustomerId = c.CustomerId
WHERE o.OrderDate >= '2026-01-01'
GROUP BY c.CustomerName
ORDER BY Revenue DESC;
```

The query joins entities, filters rows, aggregates measures, groups results, and sorts the output. It does not change source data.

| Object | Purpose |
|---|---|
| Table | Stores rows under a defined schema |
| View | Saved query presented as a virtual table |
| Index | Additional structure that accelerates access at storage/write cost |
| Stored procedure | Named executable database program with parameters and control logic |

An index helps selected query patterns; too many indexes slow writes and consume storage. A view does not necessarily store results. **VERIFY CURRENT:** product-specific materialized/indexed-view behavior.

### Relational reasoning in one worked model

Suppose an order application begins with one spreadsheet-like table containing customer name, customer address, product name, unit price, quantity, and order date. Repeating customer and product facts on every line creates update anomalies: changing a product name or customer address requires many rows to agree.

A normalized design could separate `Customer`, `Product`, `Order`, and `OrderLine`:

- `Customer.CustomerId`, `Product.ProductId`, and `Order.OrderId` are primary keys.
- `Order.CustomerId` is a foreign key to `Customer`.
- `OrderLine` resolves the many-to-many relationship between orders and products and can store relationship-specific facts such as quantity and sale price.
- `NOT NULL`, uniqueness, referential, and check constraints reject invalid states at the database boundary.

Normalization reduces redundant facts and update anomalies; it does not mean “create as many tables as possible.” Analytical systems may deliberately denormalize data into facts and dimensions to make scans and business queries simpler. The official [relational concepts module](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/) covers normalization, SQL statement types, and common database objects.

SQL statements are often grouped by intent:

| Intent | Common examples | Reasoning cue |
|---|---|---|
| Define structure | `CREATE`, `ALTER`, `DROP` | Changes schema objects, not ordinary business rows |
| Query or change rows | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Reads or modifies data |
| Control access | `GRANT`, `REVOKE` | Changes permissions |
| Control transactions | `COMMIT`, `ROLLBACK` | Accepts or reverses a transaction where supported |

Syntax and grouping can vary by database engine. At fundamentals level, distinguish what the statement is trying to do.

### Azure relational services

| Requirement | Likely service |
|---|---|
| Managed SQL Server database for cloud applications | Azure SQL Database |
| Managed instance with broad SQL Server instance compatibility | Azure SQL Managed Instance |
| Full SQL Server and OS control or lift-and-shift dependency | SQL Server on Azure Virtual Machines |
| Managed community PostgreSQL workload | Azure Database for PostgreSQL |
| Managed community MySQL workload | Azure Database for MySQL |

Azure SQL Database is database-oriented PaaS. Managed Instance supplies an instance-oriented compatibility surface. SQL Server on Azure VMs is IaaS: Microsoft manages the host, while the customer manages the guest OS and SQL Server configuration to the applicable service-management boundary.

Selection considerations include engine compatibility, instance-level features, migration effort, administration responsibility, availability, scale, networking, identity, backup/restore needs, region, and cost. Use the current [Azure SQL service comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview) rather than assuming PaaS is always drop-in compatible.

#### Choose the management boundary before the SKU

Use this progression for SQL Server-family scenarios:

1. If the application is cloud-designed and needs a managed database, begin with **Azure SQL Database**.
2. If migration requires broader instance-scoped SQL Server compatibility while retaining PaaS management, evaluate **Azure SQL Managed Instance**.
3. If the workload requires operating-system access or full control over the SQL Server installation, evaluate **SQL Server on Azure VMs** and accept the additional administration.

The control boundary is the durable distinction. PaaS removes responsibility for the guest operating system and database software maintenance; IaaS preserves more control and more customer work. The current Microsoft comparison says SQL Database and Managed Instance include service-managed upgrades, high availability, and backups, while SQL Server on an Azure VM allows full database-engine and OS control.

Engine compatibility is a separate decision. A PostgreSQL or MySQL application normally starts with the corresponding managed Azure service rather than being rewritten merely to use an Azure SQL product. Use the [Azure relational database services module](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/) to compare the SQL and open-source choices at the expected depth.

| Scenario | Better starting point | Why the neighbor is weaker |
|---|---|---|
| New multitenant app with isolated SQL Server databases | Azure SQL Database | Managed Instance adds instance scope the app may not need |
| Existing SQL Server estate with instance-level dependencies | Azure SQL Managed Instance | SQL Database can require more compatibility remediation |
| Vendor appliance requires OS agents and custom SQL installation control | SQL Server on Azure VMs | PaaS intentionally withholds OS control |
| Existing PostgreSQL application | Azure Database for PostgreSQL | Azure SQL is a different engine and compatibility surface |

**VERIFY CURRENT:** exact engine versions, feature compatibility, service tiers, availability, scaling limits, and regional support.

> **Related item:** Recovery point and recovery time objectives should drive backup, replication, and failover choices. “The service is managed” does not define how much data loss or downtime the business accepts.

---

## 3. Non-relational data

NoSQL is an umbrella for models optimized beyond a traditional normalized relational design. Choose from the access pattern rather than from a belief that one model is more modern.

| Model | Natural fit | Key design question |
|---|---|---|
| Key-value | Cache, session, profile by known key | Can every important request start with the key? |
| Document | Aggregate stored/retrieved as flexible JSON-like documents | What belongs in one aggregate and partition? |
| Column-family/wide-column | High-scale sparse records and known query paths | Which partition and clustering keys serve queries? |
| Graph | Traversal across rich relationships | Are relationship hops central to the workload? |

### Azure Storage options

- Azure Blob Storage holds object data and supports block, append, and page blob patterns.
- Azure Files provides managed file shares over supported SMB/NFS scenarios.
- Azure Table Storage supplies a simple key/attribute NoSQL store using partition and row keys.

Blob containers are not directories in the same sense as a file system, even though names can create a folder-like hierarchy. Azure Data Lake Storage capabilities add a hierarchical namespace and analytics-oriented features to Blob Storage.

Choose by protocol and access pattern:

| Need | Start with | Boundary to remember |
|---|---|---|
| Store and retrieve images, backups, media, or large objects | Blob Storage | Object access is not the same as mounting a shared drive |
| Preserve application/user access through a managed file share | Azure Files | SMB/NFS-style file semantics differ from blob APIs |
| Store simple entities addressed by partition and row key | Table Storage | This is not a relational table with joins and foreign keys |
| Build an analytics lake over Azure object storage | Data Lake Storage capabilities | Hierarchical namespace and analytics access do not create a curated warehouse by themselves |

The current [DP-900 non-relational learning path](https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-non-relational-data/) explicitly covers Blob Storage, Data Lake Storage Gen2, OneLake, Azure Files, Azure Tables, and Cosmos DB. Product limits, supported protocols, redundancy, tiers, and region availability are **VERIFY CURRENT**.

### Azure Cosmos DB

Azure Cosmos DB is a globally distributed NoSQL database family. The current service offers APIs/data models for different workloads; **VERIFY CURRENT** names, availability, and compatibility before the exam. The blueprint expects recognition of suitable use cases and supported APIs rather than deep implementation of every one.

Partition-key selection is fundamental. A good key spreads storage and request load, supports common queries, and avoids a single hot logical partition. Cross-partition queries may cost more and add latency. Consistency choices trade how quickly replicas converge against latency and availability characteristics.

| Requirement | Design concern |
|---|---|
| Global low-latency reads/writes | Region distribution and conflict/consistency design |
| Flexible document schema | Document/API choice and application validation |
| Predictable scale | Partition key and request-unit behavior |
| Relationship traversal | Graph-capable model/API if traversal is primary |

Use the current [Azure Cosmos DB documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/) for supported APIs and consistency semantics.

#### Cosmos DB decisions that explain the service

Cosmos DB exposes database-account, database, container, and item concepts. A container is the principal scale boundary for provisioned throughput and storage, and its items are distributed by partition-key value. The [partitioning documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview) distinguishes logical partitions, which group items with the same key value, from physical partitions managed by the service.

A useful partition key has:

- high enough cardinality to distribute data and requests;
- values that do not concentrate most traffic in one logical partition;
- alignment with frequent query filters and transaction boundaries; and
- stable values, because changing a key generally means moving or recreating data.

An item ID identifies an item; the partition key helps place and scale it. Neither is automatically the same as a relational primary key. Operations confined to one logical partition are easier for the service to route, and some transaction capabilities are partition-scoped. **VERIFY CURRENT:** partition-size limits, hierarchical partition-key support, transaction scope, and migration tooling.

Request units (RUs) normalize the CPU, memory, and I/O work of database operations. A point read with an ID and partition key is generally more efficient than a broad cross-partition query, but the exact charge depends on operation and data. Use the live [request-unit documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/understand-request-unit-consumption) for current behavior.

Azure Cosmos DB offers five consistency levels from strongest to weakest: strong, bounded staleness, session, consistent prefix, and eventual. Stronger is not universally better: the [consistency documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) explains the latency, availability, and throughput tradeoffs. Session consistency is especially important to recognize because it supplies read-your-writes behavior within a client session. **VERIFY CURRENT:** API-specific mappings and multi-region restrictions.

The APIs support different programming models. At fundamentals level, recognize API for NoSQL as the native document experience and MongoDB, Cassandra, Gremlin, and Table compatibility models for corresponding workload shapes. Confirm the current list in [Choose an API in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/choose-api).

> **Related item:** CAP-style tradeoffs are about behavior during a network partition, not a label that one database is simply “consistent” or “available.” Product consistency levels and application conflict handling deserve precise review in later certifications.

---

## 4. Analytics workloads

### The analytics pipeline

```text
operational sources / files / events
            ↓ ingest
raw or landing storage
            ↓ validate and transform
curated lake / warehouse / lakehouse
            ↓ semantic model
reports, dashboards, notebooks, ML, applications
```

Ingestion moves data from sources. Transformation cleans, combines, and reshapes it. Orchestration schedules and coordinates activities and dependencies. A semantic model exposes business measures, dimensions, relationships, and security in a consistent form.

ETL transforms before loading the final analytical store. ELT loads data first and uses the target engine to transform it. Both patterns can coexist. Selection depends on engine capabilities, governance, latency, volume, and reuse.

### Follow the evidence through the pipeline

For an analytical scenario, name every boundary and its failure mode:

| Stage | Purpose | Question that exposes a weak design |
|---|---|---|
| Source | Produces operational records, files, or events | Who owns the definition and schema? |
| Ingestion | Copies or receives data | Can it retry without creating duplicates? |
| Raw/landing | Preserves replayable input | Can the original be audited and reprocessed? |
| Transformation | Cleans, joins, validates, and reshapes | What happens to bad, late, or missing data? |
| Curated serving | Organizes trustworthy data for queries | Is the store optimized for its consumers? |
| Semantic model | Defines measures, relationships, labels, and security | Is “revenue” defined once and governed? |
| Visualization/consumer | Communicates or acts on the result | Does the display answer the business question? |

Orchestration coordinates activities, dependencies, schedules, parameters, retries, and monitoring; it is not the same as transformation. A pipeline can orchestrate a notebook or SQL job that performs transformations. The [large-scale analytics module](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/) connects warehouse architecture, ingestion pipelines, analytical stores, and a Fabric exercise.

> **Related item:** Idempotent processing means a safe retry produces the intended state without duplicating business effects. It matters in both batch and streaming designs because delivery and compute can be retried.

### Batch and streaming

Batch processing operates on bounded collections at intervals. Stream processing handles a continuing sequence of events with low-latency windows, state, and event-time concerns.

| Concern | Batch | Streaming |
|---|---|---|
| Input | Finite dataset | Unbounded event flow |
| Latency | Minutes to hours often acceptable | Seconds or sub-seconds may matter |
| Failure handling | Re-run a partition/job | Checkpoints, replay, idempotency, late events |
| Example | Nightly sales aggregation | Live fraud or telemetry detection |

Real-time does not mean every system must be streaming. If a business acts daily, a dependable daily batch may be simpler and cheaper.

Streaming adds time semantics. Event time records when the event occurred; processing time records when the engine handled it. Windows group an unbounded flow into finite intervals for aggregation. Late or out-of-order events, checkpoints, replay, and duplicate handling determine whether a low-latency result is also trustworthy. The official [real-time analytics module](https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/) is the right current source for blueprint-level Azure and Fabric service mappings.

| Scenario | Likely pattern | Reason |
|---|---|---|
| Monthly financial close | Batch | Complete bounded period and control totals matter more than seconds |
| Alert when machine temperature remains high | Stream | The organization must act while events are arriving |
| Rebuild two years of aggregates | Batch/backfill | Historical bounded input can be partitioned and rerun |
| Live telemetry dashboard plus nightly reconciliation | Both | Streaming serves immediacy; batch verifies completeness |

### Analytical stores and Microsoft services

| Concept/service | Role |
|---|---|
| Data lake | Low-cost storage for data in original and processed forms |
| Data warehouse | Curated relational analytical store optimized for reporting/SQL |
| Lakehouse | Combines lake openness with warehouse-style tables/management |
| Microsoft Fabric | SaaS analytics platform spanning data integration, engineering, warehousing, real-time, data science, and Power BI experiences |
| Azure Databricks | Managed Apache Spark-based data and AI platform for engineering, analytics, and ML workloads |
| Power BI | Semantic modeling, reports, dashboards, and business analytics |

The official July 2026 blueprint explicitly includes Fabric and Databricks. Know their broad roles; **VERIFY CURRENT** workloads, branding, licensing, and integration details.

#### Store and platform selection

| Requirement | Better conceptual fit | Key distinction |
|---|---|---|
| Retain varied raw and curated files at scale | Data lake | Flexible storage; consumers still need processing and governance |
| Govern structured enterprise reporting with SQL and dimensional models | Data warehouse | Curated relational analytics surface |
| Use lake files/tables with Spark engineering and SQL access | Lakehouse | Lake flexibility plus table-management and query capabilities |
| Unify ingestion, engineering, warehousing, real-time analysis, and Power BI in SaaS | Microsoft Fabric | Integrated experiences over OneLake and shared platform services |
| Build Spark-centered data engineering, analytics, and ML on Azure | Azure Databricks | Managed data/AI platform centered on Spark and lakehouse patterns |

Fabric and Azure Databricks overlap; the exam does not require pretending they are mutually exclusive. Microsoft describes [Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview) as an end-to-end analytics SaaS platform with workloads operating over OneLake, while [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/introduction/) is an Azure-optimized data and AI platform built around lakehouse and Apache Spark capabilities. Choose by required platform experience, existing estate, skills, governance, integration, and operating model.

Within Fabric, a warehouse is the SQL-first fit for structured, governed BI workloads; a lakehouse supports structured and unstructured data with Spark-oriented engineering and a SQL analytics endpoint. The current [Fabric storage decision guide](https://learn.microsoft.com/en-us/fabric/fundamentals/store-data) is authoritative because workload names and capabilities can change.

### Power BI concepts

Power BI Desktop is an authoring tool. The Power BI service supports publishing, sharing, refresh, governance, dashboards, and collaboration under applicable licensing. A semantic model contains tables, relationships, measures, and security. A report is a multi-page interactive collection of visuals; a dashboard is a service artifact composed of pinned tiles.

Choose visuals by question: bar/column for category comparison, line for time trend, card/KPI for a headline measure, table/matrix for detail, scatter for relationships, and maps only when location matters. More visuals do not create more insight.

#### Model before decorating

A Power BI result has layers:

1. **Power Query/data preparation** connects to sources and shapes data.
2. **Semantic model** defines tables, relationships, calculated measures, hierarchies, formats, and row-level security.
3. **Report** provides interactive, usually multi-page visual analysis.
4. **Dashboard** is a Power BI service canvas of pinned tiles that can summarize content from reports and semantic models.

Measures are calculated in filter context and should encode reusable business logic; calculated columns are evaluated for rows and stored in the model. At fundamentals level, the key point is that a visual should reuse governed measures rather than redefine revenue in every chart. A star schema places numerical events in a fact table and descriptive attributes in dimensions, usually with one-to-many relationships from dimension to fact. See Microsoft’s [star-schema guidance for Power BI](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema) and [semantic model documentation](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand).

| Business question | Suitable first visual | Common mistake |
|---|---|---|
| How did revenue change by month? | Line chart | Sorting month names alphabetically |
| Which five categories are largest? | Sorted bar chart | Using many similar pie slices |
| Are sales and discount related? | Scatter chart | Claiming correlation proves causation |
| What is the current total? | Card/KPI | Omitting time period, target, or unit |
| Which records need investigation? | Table or matrix | Hiding required detail behind decoration |

Power BI Desktop authors models and reports. The service hosts and shares artifacts, refreshes data, and supports dashboards and governance subject to licensing and tenant configuration. **VERIFY CURRENT:** Fabric/Power BI licensing, sharing rules, refresh limits, and feature names.

> **Related item:** Star schemas separate fact tables containing measurable events from dimension tables describing who, what, where, and when. This simplifies analytical queries and usually improves semantic-model usability.

---

## 5. Objective-to-scenario drill

Use this sequence before looking at product names:

1. **Classify the workload.** Is the user completing an operational transaction, retrieving an object, traversing relationships, or analyzing history?
2. **Identify the natural data shape.** Relational rows, document aggregate, key/attribute entity, file/object, or event stream?
3. **State the critical access path.** Include keys, query filters, transaction scope, latency, and expected scale.
4. **Choose the management boundary.** SaaS, PaaS, or IaaS changes responsibility even when the database engine is familiar.
5. **Trace the consumer path.** For analytics, name ingestion, storage, transformation, serving, semantic, and visualization layers.
6. **Reject the nearest alternative.** Explain which stated requirement it fits less well.

#### Worked scenario: orders and sales insight

An online store must place orders atomically, keep product images, retrieve a globally used customer profile, show a live order-rate alert, and publish a governed monthly sales report.

| Need | Reasoned starting point |
|---|---|
| Order transaction | Relational OLTP store with explicit transaction and key constraints; choose the Azure SQL boundary from compatibility and control requirements |
| Product images | Blob Storage because the access pattern is object retrieval, not relational joins |
| Global customer profile | Cosmos DB may fit if global distribution and key/document access are central; validate partition key and consistency rather than selecting it only because the record is JSON |
| Live order-rate alert | Streaming ingestion and windowed processing, with replay and duplicate handling |
| Monthly sales report | Ingest operational data into a curated analytical store, define facts/dimensions and governed measures, then visualize through Power BI |

This is deliberately a multi-store design. A single product is not automatically simpler if it makes every workload a poor fit. Equally, every extra store adds integration, security, governance, monitoring, and cost, so use only the boundaries the requirements justify.

---

## 6. Hands-on labs

### Lab 1: Classify a data estate

Classify a CSV export, JSON events, invoices, product images, and application transactions by structure and workload. Choose storage and record the access, schema, consistency, latency, and governance reasons.

### Lab 2: Relational model and SQL

Create Customer, Order, Product, and OrderLine tables in a local or Azure sandbox. Define keys and constraints. Write joins and aggregations, inspect an execution plan if available, and explain when an index helps.

### Lab 3: Document and partition design

Model a shopping cart as a document. Choose a partition key, then test likely reads/writes. Identify one query that becomes cross-partition and decide whether to change the model or accept the cost.

### Lab 4: Batch and stream architecture

Draw a nightly sales pipeline and a live device-alert pipeline. For each, define source, ingestion, storage, transformation, failure/replay, quality, serving, and consumer. Explain why their operating models differ.

### Lab 5: Power BI semantic model

Load a small public dataset into Power BI Desktop. Create a date/product dimension, fact table, relationship, explicit measure, time trend, category comparison, and detail table. Explain report versus dashboard and publish only if a suitable tenant is available.

---

## 7. Knowledge checks and distinctions

1. A system must update an account and ledger atomically. Which workload characteristic matters before brand selection?
2. A dashboard query scans years of sales and slows the order system. Which architecture boundary is missing?
3. A JSON field varies between documents. Why does that not automatically make the data invalid?
4. A Cosmos DB container has one hot partition. Which key characteristics should be revisited?
5. A nightly file arrives twice. Which ingestion control prevents duplicate business records?
6. A report uses a different revenue definition from finance. Is this a visualization, semantic, quality, or governance failure?
7. An application must keep SQL Server instance-scoped behavior but should not manage the guest OS. Which Azure SQL boundary is the first candidate?
8. A large Cosmos DB container is evenly sized, but nearly every request targets one customer. Why can the design still have a hot partition?
9. A pipeline copied files successfully, but a retry doubled sales totals. Which ingestion property was missing?
10. A team wants Spark engineering over varied raw files and SQL reporting from managed tables. Which analytical store pattern should it evaluate?
11. A chart is accurate but every department calculates margin differently. Which layer should standardize the definition?

| Contrast | Remember |
|---|---|
| Structured vs semi-structured | Fixed schema versus self-describing flexible records |
| OLTP vs analytics | Operational transactions versus broad historical analysis |
| Normalization vs denormalization | Reduce update anomalies versus optimize selected reads |
| Primary key vs foreign key | Identify a row versus reference another relation |
| View vs table | Stored query abstraction versus stored rows |
| SQL Database vs Managed Instance vs SQL VM | Database PaaS versus instance PaaS versus IaaS control |
| Blob vs Files | Object storage versus managed file shares |
| Partition key vs primary key | Scale/data-placement boundary versus record identity |
| ETL vs ELT | Transform before load versus load before transform |
| Batch vs streaming | Bounded scheduled data versus continuing event flow |
| Data lake vs warehouse | Broad file/object repository versus curated analytical database |
| Semantic model vs report | Reusable business logic versus visual analysis artifact |

### Readiness checklist

- [ ] I can classify structured, semi-structured, and unstructured data and common formats.
- [ ] I can distinguish transactional and analytical workloads and their roles.
- [ ] I can explain tables, keys, normalization, SQL operations, and database objects.
- [ ] I can choose among Azure SQL Database, Managed Instance, SQL VM, PostgreSQL, and MySQL at a fundamental level.
- [ ] I can distinguish Blob, Files, Table Storage, and Cosmos DB use cases.
- [ ] I understand partitioning and consistency as design decisions rather than slogans.
- [ ] I can describe ingestion, transformation, orchestration, ETL/ELT, batch, and streaming.
- [ ] I can describe Fabric, Databricks, data lakes, warehouses, lakehouses, and Power BI at the blueprint level.
- [ ] I can distinguish a semantic model, report, dashboard, and appropriate visualization.
- [ ] I checked every **VERIFY CURRENT** item and the current official blueprint.

### Primary references

- [Official DP-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
- [Azure data fundamentals learning collection](https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-core-data-concepts/)
- [Azure SQL documentation](https://learn.microsoft.com/en-us/azure/azure-sql/)
- [Azure Storage documentation](https://learn.microsoft.com/en-us/azure/storage/)
- [Azure Cosmos DB documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/)
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [Azure Databricks documentation](https://learn.microsoft.com/en-us/azure/databricks/)
- [Power BI documentation](https://learn.microsoft.com/en-us/power-bi/)
- [Relational data learning path](https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-relational-data/)
- [Non-relational data learning path](https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-non-relational-data/)
- [Analytics learning path](https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-data-warehouse-analytics/)
- [Azure SQL service comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview)
- [Cosmos DB partitioning](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview)
- [What is Microsoft Fabric?](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — DP-900 course](https://learn.microsoft.com/en-us/training/courses/dp-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation across all four domains |
| [Microsoft — DP-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/practice/assessment?assessment-type=practice&assessmentId=24&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; start here before buying another assessment |
| [Microsoft Partner Skilling Hub — LevelUp DP-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058340) | Partner login required | 10 hours | No additional cost for eligible Microsoft partners; use a work account associated with the partner organization |
| [Microsoft Learn DP-900 learning paths](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/) | Free | About 8–12 hours | Official modules plus knowledge checks; add hands-on SQL and Power BI practice |
| [Pluralsight — Microsoft Azure Data Fundamentals (DP-900) and practice exam](https://www.pluralsight.com/paths/microsoft-azure-data-fundamentals-dp-900) | Subscription; practice access depends on plan/library | 5 hours plus 3 labs and about 2–4 hours for assessment/review | Compact structured path updated through April 2026; public page explicitly includes a practice exam, and July blueprint additions still need checking |
| [O'Reilly — Azure Data Fundamentals (DP-900)](https://www.oreilly.com/videos/azure-data-fundamentals/0642572019011/) | Subscription | 3 hours 19 minutes | Reza Salehi video course published November 2025; use current Learn for July 2026 deltas |
| [Udemy — DP-900 Azure Data Fundamentals](https://www.udemy.com/course/dp-900-azure-data-fundamentals-certification/) | Purchase or subscription | About 7 hours 47 minutes | in28Minutes course shown as updated May 2026; inspect curriculum and previews before choosing |
| [LinkedIn Learning — DP-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-azure-data-fundamentals-dp-900-cert-prep-by-microsoft-press) | Subscription | 3 hours 11 minutes | Chris Sorensen course released August 2024; fill Fabric and July 2026 changes from current Learn |
| [Coursera — Microsoft DP-900 Exam Prep specialization](https://www.coursera.org/specializations/microsoft-azure-dp-900-data-fundamentals) | Subscription; audit options vary | About 4 weeks at 10 hours/week (provider pace) | Microsoft-created five-course sequence with sandbox exercises; older Synapse/HDInsight emphasis needs a July 2026 Fabric cross-check |
| [MeasureUp — DP-900 practice test](https://www.measureup.com/microsoft-practice-test-dp-900-microsoft-azure-data-fundamentals.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 118 questions; public last update is March 2024, so perform a current Fabric delta check |
| [Whizlabs — DP-900 training and practice](https://www.whizlabs.com/microsoft-azure-certification-dp-900/) | Paid course or subscription | About 4–8 hours for assessment and review; course total not verified | Use the practice component for gap detection; current instructional runtime and July 2026 delta coverage were not independently verified |
| [O'Reilly — DP-900 interactive practice test](https://www.oreilly.com/products/certification-prep.html) | Subscription | About 2–4 hours for an attempt and review | O'Reilly's public certification-prep catalog lists a DP-900 Pearson practice test; exact launch details appear after sign-in |
| [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/) | Free | Select 2–4 hours by gap | Current Fabric explanations and links to role-based learning; broader than the fundamentals objective |
| [Power BI guided learning](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) | Free | Select 3–6 hours by gap | Hands-on semantic-model and reporting reinforcement |

The assessment products above supplement—not replace—explanatory learning and hands-on data work. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
