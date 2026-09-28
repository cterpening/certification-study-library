# DP-900 deep review — September 28, 2026

The entire guide and all 30 detailed objectives were reviewed against the unchanged July 21, 2026 blueprint. The update adds six worked exercises, eight labs and 30 answered checks, including answers to the eleven existing questions. Two blog tasks provide useful supplemental reading. Independent human review and live platform labs remain pending.

## Scope and evidence

The eleven objective groups contain 3/3/2/3/4/2/3/2/3/2/3 bullets. Each has a section mapping in `ADLC_Docs/operations/2026-09-28-dp-900-deep-review.json`, together with prior records, fetch evidence, reading boundaries and validation results. The objective hash remains `7cef780d1a9e8e88b587fba89acb994985c4aedbd491710e814686ce5dc6559f`; the status hash remains `ef35a98bc74c2cf998b4c131ec8c9936b80c4b42997b9bd708c48ad0bb9e38e5`.

The [credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/) is active, with a 45-minute assessment and 13 languages. Fundamentals certifications do not expire under the [expiration policy](https://learn.microsoft.com/en-us/credentials/support/certification-expiration-policy). The official one-day, 13-language course is now titled Introduction to Microsoft Azure Data. Completing a training course is distinct from earning the certification.

## Changes that help learners

The original SQL query grouped customers only by display name. It now includes customer identity so two customers named Alex remain separate. An original in-memory SQLite exercise demonstrates correct totals, a left join retaining zero-revenue customers, inflated totals after joining order headers to lines, rollback, and rejected references. Additional checks show why `SUM(DISTINCT ...)` cannot generally repair aggregation at the wrong grain. SQL syntax and constraints were checked against [GROUP BY](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver17) and [key-constraint documentation](https://learn.microsoft.com/en-us/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver17). SQLite execution does not establish Azure SQL feature parity or concurrency behavior.

Normalization guidance now distinguishes current customer/product facts from historical delivery addresses and sale prices. Storage guidance separates object, managed-share and key/attribute access. The hierarchical namespace discussion explains why slashes in blob names are not equivalent to directory semantics.

Cosmos guidance separates dedicated container throughput from database-shared throughput, RU work from RU/s capacity, and an SDK point read from a SQL query with equivalent predicates. The [resource model](https://learn.microsoft.com/en-us/azure/cosmos-db/resource-model) supplies the native API boundary. The [DocumentDB release notice](https://learn.microsoft.com/en-us/azure/documentdb/release-notes) identifies the renamed MongoDB vCore offering. The distinct [Cosmos DB for PostgreSQL notice](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/product-updates) describes a retirement path without a final date; none was invented. These distinctions prevent broad landing-page inventories from becoming misleading service-selection advice.

Fabric coverage maps Eventstream, Eventhouse, Activator and Spark Structured Streaming to ingestion, storage/query, reaction and processing roles. It distinguishes mirroring from shortcuts and acknowledges caching and access identities. The [lakehouse SQL endpoint](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-sql-analytics-endpoint) supports SQL objects while remaining read-only for Delta-table data; its SQL permissions do not secure every alternate access path.

Current [semantic-model documentation](https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models) controls the explicit creation and existing-model lifecycle guidance. Older tutorial assumptions and earlier announcement schedules are not treated as current instructions. Power BI examples cover model/report/dashboard roles, an 11% weighted margin rather than a misleading 15% average, and a 15-minute Import-workflow freshness trace. Additional exercises cover invented RU rates and duplicate/late events.

## Blog decisions

| Article | Decision and task | Boundary |
|---|---|---|
| [Point reads versus queries](https://devblogs.microsoft.com/cosmosdb/point-reads-versus-queries/), Tim Sander, October 22, 2020 | Accept: classify requests by whether ID and partition key are already known. | Current product documentation controls names and RU assumptions. No sample code copied. |
| [Introducing the Azure DocumentDB Blog](https://devblogs.microsoft.com/documentdb/introducing-azure-documentdb/), Marko Hotti, May 27, 2026 | Accept: draw the separate native Cosmos, RU MongoDB and DocumentDB offerings. | Portfolio orientation only; no compatibility, savings or migration guarantee. |
| [Sunsetting default semantic models](https://blog.fabric.microsoft.com/en-us/blog/sunsetting-default-semantic-models-microsoft-fabric/) | Defer blog inclusion after blocked/inconsistent redirect access. | Complete article was not verified. Use current primary model documentation instead. |

Both accepted main articles were read. Linked media, comments and migration procedures were not audited or executed.

## Catalog comparison

Pluralsight lists four courses totaling 3h40 and three 30-minute labs: 5h10, rounded to five hours in the header. The prior row incorrectly added the labs again. Component dates run through April 21, 2026; this does not prove full July-baseline alignment.

O’Reilly public browser metadata confirms Reza Salehi, November 2025, 3h19, with Fabric and Databricks in the outline. Udemy now lists August 2026, 15 sections, 131 lectures and 7h45. Direct retrieval remains blocked for both. LinkedIn remains 3h11, August 30, 2024. Coursera’s five estimates total 35 hours, distinct from its four-week/10-hour-week pace; its older Synapse/HDInsight emphasis needs a Fabric supplement. MeasureUp lists 118 questions and a March 2024 update.

Partner, Whizlabs, direct assessment and generic O’Reilly practice pages returned shells or no substantive text. Current entitlement, sandbox/voucher access and complete lesson accuracy remain unverified. No paid lessons or assessment questions were accessed.

## Validation and follow-up

One original Python/SQLite block and 31 local assertions passed. They check relational behavior, invented RU/event/margin/freshness arithmetic and catalog sums. Repository tests, metadata/learning-resource checks, strict site build, generated-site validation and whitespace checks are recorded in the receipt after success.

October 26 follow-ups cover product lifecycle and learning catalogs, including access-limited resources. Weekly automation detects changes and queues review work; it does not perform this semantic review itself. The [Microsoft tracker](../MICROSOFT-REVIEW-STATUS.md) keeps the remaining backlog visible.

No cloud resource, migration, Power BI publication, notification or paid assessment was executed. Selected long-page sections were read; full API, compatibility, region and security matrices were not exhaustively audited. There is no unresolved blocker for the bounded claims applied to this fundamentals guide.
