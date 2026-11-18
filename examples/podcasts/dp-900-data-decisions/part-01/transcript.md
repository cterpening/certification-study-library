# DP-900 study conversation — Part 1

> Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING.

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) is authoritative.

Scope: Four selected data-decision topics spanning core concepts, relational services, non-relational storage, and analytics. This companion is not complete DP-900 exam coverage. Scoped technical evidence was checked on November 10, 2026; human review and live Azure, Fabric, and Power BI execution remain pending.

Baseline: Skills measured as of July 21, 2026. Recorded blueprint check: 2026-10-28.

This is a production script, not an assertion that audio has been generated or listened to.

[Companion study guide, practice questions and visual aids](<../../../study-packs/dp-900-data-decisions/study-guide.md>)

[Full source study guide](<../../../../guides/DP-900-microsoft-azure-data-fundamentals.md>)

## Introduction

**Host:** Welcome to our DP-900 study conversation, part 1 of 1. This is an independent, AI-assisted study resource with synthetic voices. Human review is pending. The official exam blueprint is authoritative. Our source package uses this baseline: Skills measured as of July 21, 2026. Its recorded blueprint check was 2026-10-28; preparing this episode does not renew that review. Today's scope: Four selected data-decision topics spanning core concepts, relational services, non-relational storage, and analytics. This companion is not complete DP-900 exam coverage. Scoped technical evidence was checked on November 10, 2026; human review and live Azure, Fabric, and Power BI execution remain pending.

**Learner:** We will work through the ideas, compare common choices, and pause for recall. The linked guide and show notes contain the sources and visual aids.

## Choose from the workload, not just the file format

**Host:** Our example is an online bookshop. It accepts orders, stores book-cover images, remembers customer preferences, and reports monthly sales. We will use those needs to make data decisions. These are original study scenarios, not recalled exam questions.

**Learner:** I am tempted to start by choosing a familiar database. But that bundles several different questions together. What does the data look like, what do people do with it, how quickly do they need results, and who will operate the system?

**Host:** Exactly. Start with representation. Rows with predictable columns are structured data. A document with named fields and a flexible arrangement can be semi-structured. Images and audio are common examples of unstructured content. That last label does not mean the content is useless, unsearchable, or exempt from access control.

**Learner:** Suppose our order arrives as JavaScript Object Notation, usually called JSON. The message format tells me how information is represented. It does not tell me whether the application needs relational constraints, document retrieval, or a file archive. I still need the access and transaction requirements.

**Host:** Now separate the workloads. Checkout repeatedly creates or changes a small set of operational records. Online transaction processing, often shortened to O-L-T-P, describes that kind of work. An analyst comparing several years of sales is asking an analytical question across many records. The same business can need both.

**Learner:** Our visual aid uses three independent arrows. JSON points to representation. Checkout points to transaction and point-access needs. Historical comparison points to aggregation and analytical serving. The arrows are questions to investigate, not instructions to deploy three particular products.

**Host:** Here is a recall check. Orders arrive as JSON, checkout needs reliable order changes, and analysts need historical comparisons. Does the file format prove that both workloads should use one document database? Pause and explain what evidence you would ask for.

**Learner:** No. I would ask which changes belong together, which queries are frequent, what latency is acceptable, and how much history must be scanned. Then I would compare candidate stores and processing engines. Separating operational and analytical serving can help, but it also introduces integration and freshness work. The requirement earns the extra component; the fashionable product name does not.

## Match relational design and the Azure SQL management boundary

**Host:** Return to the bookshop's orders. A relational model can separate customers, products, orders, and order lines. A primary key identifies a row. A foreign key helps enforce the intended relationship, such as which customer an order belongs to.

**Learner:** Why not repeat the customer's current address on every order line? It makes one spreadsheet easy to read, but a later address change would require many rows to agree. Separating repeated current facts reduces that update problem. That is part of the reason for normalization.

**Host:** There is an important meaning check. The address used to deliver an old order is a historical fact. It may need to remain exactly as it was, even after the customer's current address changes. Normalization is not an instruction to delete history or create the largest possible number of tables.

**Learner:** Once the model makes sense, we still have to choose how to run the SQL Server-family database. A managed service can reduce platform administration, but its compatibility and control boundary must fit the application. The name SQL by itself does not settle that.

**Host:** Read the diagram as three starting points. A compatible cloud application needing a managed database leads us to evaluate Azure SQL Database. Broader instance-level dependencies lead us to evaluate Azure SQL Managed Instance. A requirement for guest operating-system and SQL installation control leads us to SQL Server on Azure Virtual Machines.

**Learner:** Those are conditional choices, not a ranking from worst to best. Managed Instance does not guarantee that every existing application will migrate unchanged. A virtual machine gives more control and also brings more administration. We must verify exact feature requirements, supported versions, and the operational design.

**Host:** Our vendor says its application requires an agent installed inside the guest operating system and control over the SQL Server installation. Which starting point matches that requirement? Pause and include the responsibility tradeoff in your answer.

**Learner:** Evaluate SQL Server on Azure Virtual Machines. The requirement explicitly calls for operating-system and installation control, which the platform-managed alternatives do not expose in the same way. The team must accept the corresponding administration work and verify the vendor's support conditions. A shorter management checklist would not compensate for an incompatible application.

## Distinguish objects, shared files, and database documents

**Host:** Now consider three things that are not the bookshop's normalized order tables: cover images, shared application files, and customer preference documents. Calling all three non-relational does not tell us how they should be stored or accessed.

**Learner:** For a cover image fetched by its object name, Blob Storage is a natural candidate. The application asks for an object. That is a different requirement from an older application that expects to open and coordinate files through a shared file system.

**Host:** Azure Files is a candidate for managed file shares using supported protocols such as Server Message Block, or S-M-B, and Network File System, or N-F-S. Check which protocol and features the application needs. Do not turn this distinction into the false rule that Blob Storage can never expose another protocol; supported capabilities and constraints need their own check.

**Learner:** The customer profile is another case. If document access and regional distribution are central requirements, Azure Cosmos DB for NoSQL may fit. But JSON is only the representation. We still need to know which fields identify a request, how data is partitioned, and what consistency the application requires.

**Host:** In that service's resource model, items live in containers. A partition key helps organize and distribute the data and requests. A design that sends most traffic to one key value can create a hot spot. The item's ID and its partition key have different roles, even when the application sometimes uses both together.

**Learner:** Our visual has three independent requirement arrows: image objects to Blob Storage, shared-file access to Azure Files, and distributed document lookup to Cosmos DB for NoSQL with partition design. It does not mean that every shop must deploy three stores. Each extra service also needs integration and operational attention.

**Host:** Try this aloud. We need named image objects, an application with shared-file requirements, and profiles accessed by key across regions. Name a reasonable candidate for each, then name one reason the initial choice might change.

**Learner:** Blob Storage, Azure Files, and Cosmos DB for NoSQL are the initial candidates. Required protocols or compatibility may change the first two choices. Query patterns, partition distribution, consistency, and cost may change the database choice. A useful answer explains the requirement and the remaining validation, instead of merely listing product names.

## Trace data from ingestion to a trustworthy visual

**Host:** The bookshop manager asks two questions. Is the current order rate unusually high, and how did monthly revenue change over the last year? Those questions do not necessarily need the same response time or the same processing path.

**Learner:** A current order-rate alert may justify streaming events and evaluating windows of activity. A monthly revenue comparison can often use a bounded batch. Streaming processes an ongoing flow, but it is not a promise that every downstream result appears instantly. We should choose the pattern from when someone needs to act.

**Host:** Follow the analytics responsibilities. Ingestion receives the records. Transformation validates, combines, and reshapes them. Orchestration coordinates the steps and dependencies. The analytical store serves the result. A semantic model defines tables, relationships, and business measures so people can interpret the same number consistently.

**Learner:** Then we choose a visual. For revenue across months, a line chart is a useful starting point. For category comparisons, bars are useful. For investigating exact records, use a table. Decorating a chart cannot repair a wrong revenue definition or a join that counted an order twice.

**Host:** Our final diagram shows invented timestamps for one Import-model workflow. A sale commits at ten o'clock, is ingested at three minutes past, and is transformed at five minutes past. The scheduled semantic-model refresh finishes at quarter past. At ten minutes past, the report still omits the sale. What should the team inspect first? Pause and trace the path.

**Learner:** Inspect the model's refresh state and the timestamps. In this scenario, transformation has finished but the Import model has not yet completed its refresh. Replacing the chart would not shorten that path. The total delay is fifteen minutes, with ten minutes between transformation and completed model refresh. Those numbers are our example, not a Microsoft service commitment.

**Host:** That reasoning depends on the stated access mode. Other modes have different freshness paths, so verify the configuration instead of applying the example mechanically. Also distinguish freshness from correctness. A current result can still be wrong if its data quality, relationships, or business measure is wrong.

**Learner:** To finish, explain the bookshop's data flow without reciting a product list. Name the operational transaction, object and file access needs, document lookup, processing latency, model meaning, and final business question. These selected distinctions give you a framework for further DP-900 study. They do not replace the complete guide, hands-on practice, or the current official objectives.

## Next steps

**Learner:** Before moving on, explain the distinctions from this episode without looking at your notes. Use the original practice questions in the study pack to find gaps.

**Host:** Then check the current official sources and complete the relevant hands-on work. This conversation covers selected objectives; listening alone is not evidence of readiness or complete exam coverage.

## Show notes

These registered sources are pinned through the study package's input fingerprints.

- **Choose from the workload, not just the file format** — [Explore core data concepts](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/). Guide sections: Data representation; Operational and analytical workloads; A repeatable data-choice method.
- **Match relational design and the Azure SQL management boundary** — [Explore fundamental relational data concepts](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/), [What is Azure SQL?](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview). Guide sections: Tables, keys, and relationships; Relational reasoning in one worked model; Azure relational services; Choose the management boundary before the SKU.
- **Distinguish objects, shared files, and database documents** — [Blob types](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction), [Azure Files overview](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction), [Azure Cosmos DB: Resource model](https://learn.microsoft.com/en-us/azure/cosmos-db/resource-model), [Partitioning and horizontal scaling in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview). Guide sections: Azure Storage options; Azure Cosmos DB; Cosmos DB decisions that explain the service.
- **Trace data from ingestion to a trustworthy visual** — [Explore data ingestion pipelines](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines), [Explore fundamentals of real-time analytics](https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/), [Power BI semantic models](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand), [Understand star schema and the importance for Power BI](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema), [Power BI training](https://learn.microsoft.com/en-us/training/powerplatform/power-bi). Guide sections: The analytics pipeline; Follow the evidence through the pipeline; Batch and streaming; Power BI concepts; Model before decorating; 6. Trace a freshness problem.
