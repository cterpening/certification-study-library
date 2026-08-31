---
exam_code: DP-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# DP-900 Microsoft Azure Data Fundamentals Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official DP-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) is authoritative.

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

# 1. Core data concepts

## Data representation

| Shape | Characteristics | Examples |
|---|---|---|
| Structured | Fixed schema, predictable fields and types | Relational rows, transaction records |
| Semi-structured | Self-describing records with flexible fields | JSON, XML, event messages |
| Unstructured | No tabular schema inherent in the content | Images, audio, video, documents |

The representation does not dictate one store. JSON can be placed in a file, document database, or relational column; the right choice depends on access, transaction, scale, querying, governance, and integration requirements.

Common file formats include delimited text such as CSV, JSON, XML, Parquet, Avro, images, audio, and video. CSV is simple and widely interoperable but carries limited type/schema metadata. Parquet is a compressed columnar format well suited to analytical scans because an engine can read selected columns rather than entire records.

> **Related item:** A schema is a contract between producers and consumers. Schema-on-write validates structure before data is stored; schema-on-read interprets structure when data is consumed. Neither eliminates the need for data-quality tests and versioning.

## Operational and analytical workloads

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

## Data roles

| Role | Primary focus |
|---|---|
| Database administrator | Availability, security, backup/recovery, performance, and database operations |
| Data engineer | Ingestion, transformation, storage, quality, orchestration, and dependable data products |
| Data analyst | Modeling, visualization, interpretation, and decision support |

Data scientists and application developers are related consumers/builders, but the current blueprint emphasizes the three roles above. In small organizations one person may perform several roles; responsibilities still exist even when titles differ.

## Data quality and governance

Accuracy, completeness, consistency, timeliness, uniqueness, and validity are useful quality dimensions. A technically successful pipeline can still deliver wrong business outcomes if definitions differ or late/missing data is silently accepted.

Governance establishes ownership, discovery, classification, access, retention, lineage, and acceptable use. Microsoft Purview provides data-governance and compliance capabilities across data estates. It does not replace source-system controls or responsible owners.

> **Related item:** Data lineage records where data came from and how it changed. It reduces diagnosis time when a dashboard value is questioned, but lineage alone does not prove that the transformation was correct.

---

# 2. Relational data

## Tables, keys, and relationships

A relational model stores data in tables. Each row represents an instance; columns represent attributes with types and constraints. A primary key uniquely identifies a row. A foreign key references a key in another table and supports referential integrity.

| Relationship | Example | Modeling note |
|---|---|---|
| One-to-one | Person to one profile | May be separated for optional/security/lifecycle reasons |
| One-to-many | Customer to orders | Foreign key commonly appears on the many side |
| Many-to-many | Students to courses | Junction table holds the two foreign keys and relationship attributes |

Normalization separates repeated facts to reduce anomalies. For example, storing a customer address on every order line creates inconsistent updates. Denormalization duplicates selected data to improve read performance or simplify analytics, accepting additional synchronization responsibility.

## SQL and database objects

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

## Azure relational services

| Requirement | Likely service |
|---|---|
| Managed SQL Server database for cloud applications | Azure SQL Database |
| Managed instance with broad SQL Server instance compatibility | Azure SQL Managed Instance |
| Full SQL Server and OS control or lift-and-shift dependency | SQL Server on Azure Virtual Machines |
| Managed community PostgreSQL workload | Azure Database for PostgreSQL |
| Managed community MySQL workload | Azure Database for MySQL |

Azure SQL Database is database-oriented PaaS. Managed Instance supplies an instance-oriented compatibility surface. SQL Server on Azure VMs is IaaS: Microsoft manages the host, while the customer manages the guest OS and SQL Server configuration to the applicable service-management boundary.

Selection considerations include engine compatibility, instance-level features, migration effort, administration responsibility, availability, scale, networking, identity, backup/restore needs, region, and cost. Use the current [Azure SQL service comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview) rather than assuming PaaS is always drop-in compatible.

> **Related item:** Recovery point and recovery time objectives should drive backup, replication, and failover choices. “The service is managed” does not define how much data loss or downtime the business accepts.

---

# 3. Non-relational data

NoSQL is an umbrella for models optimized beyond a traditional normalized relational design. Choose from the access pattern rather than from a belief that one model is more modern.

| Model | Natural fit | Key design question |
|---|---|---|
| Key-value | Cache, session, profile by known key | Can every important request start with the key? |
| Document | Aggregate stored/retrieved as flexible JSON-like documents | What belongs in one aggregate and partition? |
| Column-family/wide-column | High-scale sparse records and known query paths | Which partition and clustering keys serve queries? |
| Graph | Traversal across rich relationships | Are relationship hops central to the workload? |

## Azure Storage options

- Azure Blob Storage holds object data and supports block, append, and page blob patterns.
- Azure Files provides managed file shares over supported SMB/NFS scenarios.
- Azure Table Storage supplies a simple key/attribute NoSQL store using partition and row keys.

Blob containers are not directories in the same sense as a file system, even though names can create a folder-like hierarchy. Azure Data Lake Storage capabilities add a hierarchical namespace and analytics-oriented features to Blob Storage.

## Azure Cosmos DB

Azure Cosmos DB is a globally distributed NoSQL database family. The current service offers APIs/data models for different workloads; **VERIFY CURRENT** names, availability, and compatibility before the exam. The blueprint expects recognition of suitable use cases and supported APIs rather than deep implementation of every one.

Partition-key selection is fundamental. A good key spreads storage and request load, supports common queries, and avoids a single hot logical partition. Cross-partition queries may cost more and add latency. Consistency choices trade how quickly replicas converge against latency and availability characteristics.

| Requirement | Design concern |
|---|---|
| Global low-latency reads/writes | Region distribution and conflict/consistency design |
| Flexible document schema | Document/API choice and application validation |
| Predictable scale | Partition key and request-unit behavior |
| Relationship traversal | Graph-capable model/API if traversal is primary |

Use the current [Azure Cosmos DB documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/) for supported APIs and consistency semantics.

> **Related item:** CAP-style tradeoffs are about behavior during a network partition, not a label that one database is simply “consistent” or “available.” Product consistency levels and application conflict handling deserve precise review in later certifications.

---

# 4. Analytics workloads

## The analytics pipeline

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

## Batch and streaming

Batch processing operates on bounded collections at intervals. Stream processing handles a continuing sequence of events with low-latency windows, state, and event-time concerns.

| Concern | Batch | Streaming |
|---|---|---|
| Input | Finite dataset | Unbounded event flow |
| Latency | Minutes to hours often acceptable | Seconds or sub-seconds may matter |
| Failure handling | Re-run a partition/job | Checkpoints, replay, idempotency, late events |
| Example | Nightly sales aggregation | Live fraud or telemetry detection |

Real-time does not mean every system must be streaming. If a business acts daily, a dependable daily batch may be simpler and cheaper.

## Analytical stores and Microsoft services

| Concept/service | Role |
|---|---|
| Data lake | Low-cost storage for data in original and processed forms |
| Data warehouse | Curated relational analytical store optimized for reporting/SQL |
| Lakehouse | Combines lake openness with warehouse-style tables/management |
| Microsoft Fabric | SaaS analytics platform spanning data integration, engineering, warehousing, real-time, data science, and Power BI experiences |
| Azure Databricks | Managed Apache Spark-based data and AI platform for engineering, analytics, and ML workloads |
| Power BI | Semantic modeling, reports, dashboards, and business analytics |

The official July 2026 blueprint explicitly includes Fabric and Databricks. Know their broad roles; **VERIFY CURRENT** workloads, branding, licensing, and integration details.

## Power BI concepts

Power BI Desktop is an authoring tool. The Power BI service supports publishing, sharing, refresh, governance, dashboards, and collaboration under applicable licensing. A semantic model contains tables, relationships, measures, and security. A report is a multi-page interactive collection of visuals; a dashboard is a service artifact composed of pinned tiles.

Choose visuals by question: bar/column for category comparison, line for time trend, card/KPI for a headline measure, table/matrix for detail, scatter for relationships, and maps only when location matters. More visuals do not create more insight.

> **Related item:** Star schemas separate fact tables containing measurable events from dimension tables describing who, what, where, and when. This simplifies analytical queries and usually improves semantic-model usability.

---

# 5. Hands-on labs

## Lab 1: Classify a data estate

Classify a CSV export, JSON events, invoices, product images, and application transactions by structure and workload. Choose storage and record the access, schema, consistency, latency, and governance reasons.

## Lab 2: Relational model and SQL

Create Customer, Order, Product, and OrderLine tables in a local or Azure sandbox. Define keys and constraints. Write joins and aggregations, inspect an execution plan if available, and explain when an index helps.

## Lab 3: Document and partition design

Model a shopping cart as a document. Choose a partition key, then test likely reads/writes. Identify one query that becomes cross-partition and decide whether to change the model or accept the cost.

## Lab 4: Batch and stream architecture

Draw a nightly sales pipeline and a live device-alert pipeline. For each, define source, ingestion, storage, transformation, failure/replay, quality, serving, and consumer. Explain why their operating models differ.

## Lab 5: Power BI semantic model

Load a small public dataset into Power BI Desktop. Create a date/product dimension, fact table, relationship, explicit measure, time trend, category comparison, and detail table. Explain report versus dashboard and publish only if a suitable tenant is available.

---

# 6. Knowledge checks and distinctions

1. A system must update an account and ledger atomically. Which workload characteristic matters before brand selection?
2. A dashboard query scans years of sales and slows the order system. Which architecture boundary is missing?
3. A JSON field varies between documents. Why does that not automatically make the data invalid?
4. A Cosmos DB container has one hot partition. Which key characteristics should be revisited?
5. A nightly file arrives twice. Which ingestion control prevents duplicate business records?
6. A report uses a different revenue definition from finance. Is this a visualization, semantic, quality, or governance failure?

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

## Readiness checklist

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

## Primary references

- [Official DP-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
- [Azure data fundamentals learning collection](https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-core-data-concepts/)
- [Azure SQL documentation](https://learn.microsoft.com/en-us/azure/azure-sql/)
- [Azure Storage documentation](https://learn.microsoft.com/en-us/azure/storage/)
- [Azure Cosmos DB documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/)
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [Azure Databricks documentation](https://learn.microsoft.com/en-us/azure/databricks/)
- [Power BI documentation](https://learn.microsoft.com/en-us/power-bi/)

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — DP-900 course](https://learn.microsoft.com/en-us/training/courses/dp-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation across all four domains |
| [Microsoft Partner Skilling Hub — LevelUp DP-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058340) | Partner login required | 10 hours | No additional cost for eligible Microsoft partners; use a work account associated with the partner organization |
| [Microsoft Learn DP-900 learning paths](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/) | Free | About 8–12 hours | Official modules plus knowledge checks; add hands-on SQL and Power BI practice |
| [Pluralsight — Microsoft Azure Data Fundamentals (DP-900)](https://www.pluralsight.com/paths/microsoft-azure-data-fundamentals-dp-900) | Subscription | 5 hours plus 3 labs | Compact structured path updated through April 2026; check July blueprint additions |
| [O'Reilly — Azure Data Fundamentals (DP-900)](https://www.oreilly.com/videos/azure-data-fundamentals/0642572019011/) | Subscription | 3 hours 19 minutes | Reza Salehi video course published November 2025; use current Learn for July 2026 deltas |
| [Udemy — DP-900 Azure Data Fundamentals](https://www.udemy.com/course/dp-900-azure-data-fundamentals-certification/) | Purchase or subscription | About 7 hours 47 minutes | in28Minutes course shown as updated May 2026; inspect curriculum and previews before choosing |
| [LinkedIn Learning — DP-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-azure-data-fundamentals-dp-900-cert-prep-by-microsoft-press) | Subscription | 3 hours 11 minutes | Chris Sorensen course released August 2024; fill Fabric and July 2026 changes from current Learn |
| [Coursera — Microsoft DP-900 Exam Prep specialization](https://www.coursera.org/specializations/microsoft-azure-dp-900-data-fundamentals) | Subscription; audit options vary | About 4 weeks at 10 hours/week (provider pace) | Microsoft-created five-course sequence with sandbox exercises; older Synapse/HDInsight emphasis needs a July 2026 Fabric cross-check |
| [MeasureUp — DP-900 practice test](https://www.measureup.com/microsoft-practice-test-dp-900-microsoft-azure-data-fundamentals.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 118 questions; public last update is March 2024, so perform a current Fabric delta check |
| [Whizlabs — DP-900 training and practice](https://www.whizlabs.com/microsoft-azure-certification-dp-900/) | Paid course or subscription | About 4–8 hours for assessment and review; course total not verified | Use the practice component for gap detection; current instructional runtime and July 2026 delta coverage were not independently verified |
| [Microsoft Fabric Career Hub](https://learn.microsoft.com/en-us/fabric/fundamentals/career-hub) | Free | Select 2–4 hours by gap | Current Fabric explanations and role paths; broader than the fundamentals objective |
| [Power BI guided learning](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) | Free | Select 3–6 hours by gap | Hands-on semantic-model and reporting reinforcement |

The assessment products above supplement—not replace—explanatory learning and hands-on data work. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
