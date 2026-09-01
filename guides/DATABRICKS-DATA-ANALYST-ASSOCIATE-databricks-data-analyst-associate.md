---
exam_code: DATABRICKS-DATA-ANALYST-ASSOCIATE
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/data-analyst-associate
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# Databricks Certified Data Analyst Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-data-analyst-associate-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/data-analyst-associate) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-DATA-ANALYST-ASSOCIATE`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official exam guide current as of October 30, 2025; live nine-domain weighted coverage page checked September 1, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026. The detailed PDF says its self-paced *Data Analysis with Databricks* course was being replaced by *AI/BI for Data Analysts* and *SQL Analytics on Databricks*; that is a learning-catalog transition, not evidence of a scheduled exam change.<br>
**Lifecycle status:** Active; valid for two years, with the currently live exam required for recertification.<br>
**Assessment:** 45 scored multiple-choice questions, 90 minutes, USD 200, no test aids, English, online or test-center delivery.<br>
**Prerequisite:** None required. The official guide recommends related training and six months of hands-on Databricks experience.<br>
**Code convention:** Exam SQL is ANSI SQL. Practice writing and reading SQL without depending on a vendor-specific shortcut when a standard construct is available.

## How to use this guide

Treat the percentages as a study-budget signal, not a prediction of a particular form. Query execution, query analysis, dashboards, and Genie total 63%; nevertheless, those capabilities depend on correct data import, modeling, catalog discovery, and security.

```text
business question -> governed source -> grain and model -> ANSI SQL result
-> profile and validate -> visualization or Genie answer -> permission boundary
-> refresh or alert -> usage and feedback evidence -> measured improvement
```

For each exercise, record the question, intended grain, source objects, warehouse, SQL text, query ID, result checks, visualization choice, refresh state, principal and grants, and one failure/recovery observation. Product names, licensing, sharing modes, serverless behavior, AI/BI features, and UI locations change quickly; recheck the linked documentation in the workspace where you practice.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes an objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Databricks' published exam objectives.

## Objective map

| Published domain | Weight | What you must be able to decide or do |
|---|---:|---|
| Understanding of Databricks Data + AI Platform | 11% | Relate platform components, Catalog Explorer, Marketplace, lineage and certification to an analytics task. |
| Managing Data | 8% | Discover, query, tag, trace and clean governed tables. |
| Importing Data | 5% | Select a supported ingestion or sharing route and use the upload UI for small files. |
| Executing queries using Databricks SQL and Databricks SQL Warehouses | 20% | Choose a warehouse and express joins, sets, aggregates, table creation, history and cross-system analysis in ANSI SQL. |
| Analyzing Queries | 15% | Diagnose correctness and performance using query evidence, Photon, caching, history and clustering. |
| Creating Dashboards and Visualizations in Databricks | 16% | Build, parameterize, share, schedule, embed and alert on an AI/BI dashboard. |
| Developing, Sharing, and Maintaining AI/BI Genie spaces | 12% | Ground a Genie space, govern access, validate answers and improve it from feedback. |
| Data Modeling with Databricks SQL | 5% | Match star, snowflake and Data Vault patterns to grain, change and medallion-layer needs. |
| Securing Data | 8% | Apply the three-level namespace, ownership and least-privilege Unity Catalog access. |

---

## 1. Understanding the Databricks Data + AI Platform (11%)

### Map components to responsibilities

- **Delta Lake** supplies table transactions, schema controls and history over object storage. It is a storage/table contract, not the governance catalog or query engine.
- **Unity Catalog** supplies the `catalog.schema.object` namespace, discovery, permissions, lineage, auditing and governance across supported data and AI objects.
- **Databricks SQL** supplies SQL warehouses, the SQL editor, query history, dashboards, alerts and SQL-facing analytics experiences.
- **Mosaic AI** is the broader AI tooling family. The exam's analyst-specific generative experience is **AI/BI Genie**, not a request to master the full model-development stack.
- **Lakeflow Jobs** orchestrates tasks; **Lakeflow Spark Declarative Pipelines** manages declarative batch/stream pipelines. The 2025 PDF uses the older wording “Delta Live Tables.” Translate old course material to the current product name.
- The **Data Intelligence Engine** uses platform metadata and context to improve experiences such as natural-language analytics. Do not confuse an AI-generated answer with validated business semantics.

Use the [platform introduction](https://docs.databricks.com/aws/en/introduction/) to trace an analyst request through identity, workspace UI, compute, governance, table storage and an output. A sound answer says which component owns each decision.

### Operate Catalog Explorer as a discovery and control surface

[Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/) lets you browse catalogs and schemas; inspect tables, views, volumes, models and functions; review owners, tags, permissions, history and lineage where available; and create or manage supported objects. Know the distinction:

| Concept | Meaning | Decision consequence |
|---|---|---|
| Managed table | Unity Catalog manages governance and the underlying data lifecycle | Dropping the table can delete managed data after the retention behavior applies. |
| External table | Unity Catalog governs access while files remain at an external location | Dropping the table removes metadata, not the underlying files. |
| View | Saved query that resolves its source on use | Useful for abstraction/security, but not precomputed merely because it is saved. |
| Certified asset | A trusted-data marker applied through Unity Catalog | Helps discovery; it does not grant access or prove every query is correct. |
| Tag | Searchable metadata on a securable object | Useful for classification and discovery; privileges still govern access. |
| Lineage | Recorded upstream/downstream relationships for supported workloads | Supports impact analysis and troubleshooting; absence is not proof of no dependency. |

The [Unity Catalog overview](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) and [data-lineage documentation](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage) are the current baselines.

### Understand Marketplace without treating it as anonymous download

[Databricks Marketplace](https://docs.databricks.com/aws/en/marketplace/) is a governed discovery and exchange surface for data products and other assets. A consumer searches listings, evaluates provider and terms, obtains instant-access data or requests access, then queries the shared asset in the recipient environment. Marketplace commonly uses Delta Sharing, so the provider can share without copying a static export into the consumer's workspace.

> **Related item:** Marketplace is a catalog and commercial/distribution experience; Delta Sharing is the open sharing protocol and governed delivery mechanism. A listing can make a product discoverable, while the share, recipient and permissions determine access.

---

## 2. Managing Data (8%)

### Discover and query trusted datasets

Begin with the business definition and required grain, then inspect certification, owner, description, tags, schema, freshness and lineage before querying. A certified table is a useful trust signal, not permission to ignore the source definition. Fully qualify objects when ambiguity matters:

```sql
SELECT order_date, region, SUM(net_amount) AS revenue
FROM analytics.gold.fact_order
WHERE order_date >= DATE '2026-01-01'
GROUP BY order_date, region;
```

Record whether the query reads a managed table, external table, view, materialized view or federated source. That affects freshness, performance, lifecycle and the evidence needed for a result.

### Use tags and lineage as investigation tools

- Search tags to locate domain, sensitivity, quality or ownership metadata, then confirm the tag definition and who may apply it.
- Use upstream lineage to identify source tables and transformations behind a questionable metric.
- Use downstream lineage before changing a column, table or view.
- Compare lineage with query history and job/pipeline evidence. Each answers a different question: dependency, execution and production state.

### Clean data without hiding quality defects

Profile missing, invalid, duplicate and out-of-range values before changing them. Define a business rule and retain rejected counts. Common SQL tools include `CASE`, `COALESCE`, `NULLIF`, `TRY_CAST`, `TRIM`, regular-expression functions, window functions and deduplication with `ROW_NUMBER()`.

```sql
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY updated_at DESC, ingest_id DESC
  ) AS rn
  FROM analytics.silver.customer_candidate
)
SELECT customer_id,
       NULLIF(TRIM(email), '') AS email,
       TRY_CAST(postal_code AS INT) AS postal_code
FROM ranked
WHERE rn = 1;
```

This query makes the survivor rule explicit, but it still needs checks for null conversion, duplicate rate and unintended loss. Do not turn malformed values into nulls without counting and routing them.

> **Related item:** Medallion names are quality contracts, not mandatory database names. Bronze normally preserves reproducible source evidence, silver applies validated conformance, and gold serves a consumer-shaped model. A cleanup query belongs where its ownership, replay and quality evidence are clear.

---

## 3. Importing Data (5%)

### Choose an intake route

| Need | Suitable starting mechanism | Key check |
|---|---|---|
| Tiny local CSV/JSON/Parquet for exploration | Workspace upload/create-table UI | size limits, inferred types, reproducibility and sensitive-data policy |
| Incremental cloud files | Auto Loader or `COPY INTO`, depending scale and flow | discovery/checkpoint state, schema behavior and replay |
| Supported database or SaaS source | Lakeflow Connect or governed connector | release state, CDC semantics, identity and destination |
| Query without copying | Lakehouse Federation | latency, pushdown, source load, credentials and feature support |
| Provider-to-recipient governed exchange | Delta Sharing or Marketplace | provider, recipient, share, refresh and permissions |
| Custom REST/API intake | controlled code/job that lands raw evidence | pagination, rate limits, secrets, watermark and idempotency |

The [data-sharing documentation](https://docs.databricks.com/aws/en/data-sharing/) explains provider and recipient concepts. Upload is valuable for learning and one-off exploration, but it does not create a production ingestion design: capture the original file, type decisions, table ownership and how a repeatable pipeline would replace the manual action.

> **Related item:** Importing and federation solve different problems. Importing establishes a Databricks-side copy and freshness process; federation leaves data in the remote system and introduces remote availability, pushdown and source-capacity dependencies.

---

## 4. Executing queries with Databricks SQL and SQL warehouses (20%)

### Select and reason about a SQL warehouse

A SQL warehouse is the compute resource for Databricks SQL workloads. Choose size, scaling, channel, serverless/classic option, auto-stop and permissions from concurrency, latency, feature, isolation, network and cost requirements. Do not assume a bigger warehouse corrects a poor join or scans less data. Review current [SQL warehouse documentation](https://docs.databricks.com/aws/en/compute/sql-warehouse/).

Separate these permissions:

- Ability to use the warehouse.
- Ability to use the catalog and schema.
- Ability to select source objects.
- Ability to create or modify target objects.
- Ability to view/share the query, dashboard or Genie space.

### Join at a declared grain

Before a join, state the grain and cardinality of both sides. An inner join removes unmatched rows; a left join retains every left row; right and full joins preserve their respective unmatched sides. Multiple conditions normally belong in `ON`, while a post-join `WHERE` filter can unintentionally remove null-extended rows.

```sql
SELECT d.calendar_month,
       p.category,
       SUM(f.quantity * f.net_unit_price) AS revenue
FROM analytics.gold.fact_order_line AS f
JOIN analytics.gold.dim_date AS d
  ON f.order_date_key = d.date_key
LEFT JOIN analytics.gold.dim_product AS p
  ON f.product_key = p.product_key
GROUP BY d.calendar_month, p.category
ORDER BY d.calendar_month, revenue DESC;
```

Validate row count, distinct business keys, unmatched keys and aggregate totals before and after. `UNION` removes duplicate result rows; `UNION ALL` preserves them and usually avoids the deduplication work. Pick from semantics, not speed alone.

### Aggregate and summarize correctly

- `COUNT(*)` counts rows; `COUNT(column)` excludes nulls.
- `COUNT(DISTINCT x)` is exact; `approx_count_distinct(x)` trades exactness for scale. State that tradeoff.
- `AVG` ignores null values. Decide whether null means missing, zero or not applicable before using it.
- Use `GROUP BY` at the requested grain. Window functions calculate over a partition without collapsing all detail rows.
- Apply stable sorting when output order matters. A `LIMIT` without deterministic order is not a top-N definition.

### Create and query durable objects

Know how to create a managed or external table, a view, and a table from a query. Choose CSV, Parquet or Delta from the contract: Delta supplies transactional table behavior; Parquet is a file format; CSV requires explicit delimiter/header/type discipline. Use three-part names and explicit target locations only where the external-lifecycle requirement justifies them.

[Lakehouse Federation](https://docs.databricks.com/aws/en/query-federation/) uses connections and foreign catalogs to query external systems. Cross-system analysis may join a Delta table to a federated table, but the plan can move or push work across a network boundary. Inspect filtering, join location, supported types/functions and source load.

### Distinguish views, materialized views and streaming tables

| Object | Core behavior | Strong fit |
|---|---|---|
| Standard view | Stores a query definition; computes on use | semantic abstraction, reusable logic and some security patterns |
| Materialized view | Stores precomputed results and refreshes them | repeated analytical computation where controlled freshness is acceptable |
| Streaming table | Incrementally processes an append/streaming source | continuously arriving data and incremental pipeline semantics |

Read the current [materialized-view and streaming-table guidance](https://docs.databricks.com/aws/en/ldp/dbsql/materialized). “Dynamic view” in older learning material often refers to a standard view whose results respond to user/context logic; do not confuse that pattern with persisted materialization.

### Use history as evidence

Delta time travel lets you query a version or timestamp within retained history, while `DESCRIBE HISTORY` shows table operations. The [table-history documentation](https://docs.databricks.com/aws/en/tables/history) explains retention interactions. Use history to reproduce a prior result or investigate a change; do not promise indefinite rollback after retention cleanup.

> **Related item:** The SQL editor and Assistant can draft, explain and debug SQL, but the analyst owns the grain, authorization and validation. Preserve the generated query and test its row-level and aggregate behavior before publishing it.

---

## 5. Analyzing Queries (15%)

### Diagnose before tuning

Use a repeatable loop:

1. Confirm the result is semantically correct and identify the query ID, warehouse and data version.
2. Inspect duration, queue time, compilation, execution and bytes/rows read in query history.
3. Use the [query profile](https://docs.databricks.com/aws/en/sql/user/queries/query-profile) to find expensive operators, scans, shuffles, joins and skew.
4. Form one hypothesis: filter earlier, project fewer columns, correct a join, improve data layout, precompute, or right-size compute.
5. Change one factor and compare the same workload and result checks.

Query Insights may surface likely causes and recommendations; the profile supplies evidence. Query history supplies workload context. Neither replaces the business-correctness check.

### Place Photon and caching correctly

[Photon](https://docs.databricks.com/aws/en/compute/photon) is Databricks' vectorized engine for supported SQL and DataFrame workloads. It can accelerate supported operators, joins, aggregations and Delta/Parquet processing. Verify compute and operation support; unsupported parts can fall back. Photon does not repair Cartesian joins, incorrect filters, bad grain or an overloaded remote federated source.

Caching can reduce repeat work but creates freshness and scope questions. A result cache, disk cache and remote-source cache are not interchangeable promises. First determine whether the observed speedup is cache-dependent; then decide whether that dependency is acceptable.

### Use history, clustering and audit evidence deliberately

The [query-history UI](https://docs.databricks.com/aws/en/sql/user/queries/query-history) supports filtering and inspection of executed queries. Table history answers what changed in a Delta table; query history answers what SQL ran; lineage answers dependencies. Combine them to validate or compare historical results.

Liquid clustering reorganizes data by selected clustering keys and can improve skipping as access patterns evolve. Choose keys from repeated selective predicates and join patterns, then measure. Review [liquid clustering](https://docs.databricks.com/aws/en/delta/clustering) because runtime requirements and automatic clustering behavior are volatile.

> **Related item:** Query performance is a system property: model grain, file/layout state, statistics, warehouse capacity/concurrency, cache state, remote-source behavior and SQL shape interact. A single fast run is weak evidence; record a representative comparison.

---

## 6. Creating dashboards and visualizations (16%)

### Build from a question, not a chart palette

An [AI/BI dashboard](https://docs.databricks.com/aws/en/dashboards/) can use multiple datasets and pages with visualization, text and image widgets. Start with audience and decision, then select the visual:

| Analytical need | Useful starting visual | Common failure |
|---|---|---|
| Trend over ordered time | Line | treating irregular categories as continuous time |
| Compare categories | Bar | too many categories or truncated axes |
| Single status against target | KPI/counter | hiding denominator, time window or uncertainty |
| Relationship/distribution | Scatter, histogram or box plot where supported | implying causation from correlation |
| Composition | Stacked bar/area, sparingly | unreadable categories or comparing angles |
| Detailed lookup | Table | substituting raw detail for prioritization |

Notebook and SQL-editor visualizations are useful during exploration; dashboards add governed publication, filters, schedules and sharing. Validate totals and edge cases in SQL before polishing the display.

### Parameterize safely

Dashboard filters constrain datasets or fields. Parameters can substitute controlled values into a dataset query. Use the [dashboard-parameter guidance](https://docs.databricks.com/aws/en/dashboards/manage/filters/parameters) to distinguish field filters from query parameters, define defaults and test all permitted values. Do not concatenate untrusted input into SQL.

### Share, embed, refresh and alert with explicit boundaries

Publishing creates a consumable snapshot of dashboard configuration; sharing determines who may view or edit. Workspace users/groups, account users and external sharing modes have different identity and entitlement requirements. The current [dashboard-sharing documentation](https://docs.databricks.com/aws/en/dashboards/share/share) should control the design.

- Grant the minimum dashboard and underlying-data access required by the chosen credential model.
- Use a shareable link only when its workspace/account and external-sharing behavior matches policy.
- Treat embedding in an external application as an authentication, authorization, content-security and lifecycle integration—not merely an iframe.
- A scheduled refresh changes data freshness; it does not email every consumer by itself.
- An alert evaluates a query/threshold on a schedule and sends configured notifications. Define threshold, evaluation frequency, destination, empty/error behavior and owner.

**VERIFY CURRENT:** AI/BI dashboard publishing, external sharing, embedding, subscriptions and alert capabilities can change independently. Recheck exact entitlement and credential behavior before production use.

> **Related item:** Dashboard access and Unity Catalog data access are separate layers. Document which identity executes the dataset and whether consumers need direct source privileges; otherwise a dashboard may be overexposed or fail after publication.

---

## 7. Developing, sharing and maintaining AI/BI Genie spaces (12%)

### Ground a space before asking it questions

An [AI/BI Genie space](https://docs.databricks.com/aws/en/genie/) provides natural-language exploration over selected Unity Catalog data with a SQL warehouse. A useful space has a narrow domain, curated tables/views, clear column descriptions, representative sample questions, domain instructions and validated SQL examples or Trusted Assets.

```text
domain boundary + governed data + business definitions + instructions
+ trusted examples + usable warehouse + least-privilege sharing
-> generated SQL -> answer validation -> feedback -> maintained space
```

Pick sources at a consistent grain. Hide ambiguous or unsafe columns behind governed views. Explain synonyms, date semantics, fiscal rules, exclusions and approved metrics. A broad catalog dump makes the model guess relationships and business meaning.

### Validate and improve answers

For representative questions:

1. State the expected grain and calculation.
2. Inspect the generated SQL, tables, joins, filters and warehouse execution.
3. Compare with an independently validated query and known edge cases.
4. Capture whether the miss came from metadata, instructions, data, a relationship, ambiguous language or SQL generation.
5. Improve the smallest appropriate artifact: descriptions, instructions, sample question, benchmark, curated source or Trusted Asset.

User thumbs-up/down feedback is a signal, not ground truth. Benchmarks supply a repeatable question/expected-answer evaluation set. Refresh Unity Catalog metadata when schemas or descriptions change, and retire instructions or trusted examples that no longer match the source.

### Share with the same care as a dashboard

Grant space access to intended users/groups and verify the warehouse and data-execution model. External-app embedding needs an explicit supported integration and identity design. Do not paste secrets, personal data or unrestricted source tables into instructions to work around governance.

**VERIFY CURRENT:** Genie Trusted Assets, benchmarks, monitoring, embedding and sharing evolve rapidly. Recheck the product documentation and workspace UI near study and deployment time.

> **Related item:** Genie is a semantic interface over data and SQL, not a replacement for a governed semantic model. Better table grain, definitions, relationships and security improve both human-authored dashboards and AI-generated answers.

---

## 8. Data Modeling with Databricks SQL (5%)

### Select a model from the workload

| Pattern | Core idea | Use when | Cost to remember |
|---|---|---|---|
| Star schema | Fact at a declared grain linked to denormalized dimensions | BI measures, understandable joins and broad query performance | conformed keys, slowly changing dimensions and fact grain must be managed |
| Snowflake | Dimensions normalized into related tables | shared hierarchical structures or stricter normalization matters | more joins and a less direct analyst experience |
| Data Vault | Hubs, links and satellites separate business keys, relationships and descriptive history | auditable integration of changing multi-source data | requires a downstream information-mart/star layer for convenient BI |

Medallion describes progressive data quality; star, snowflake and Data Vault describe logical modeling patterns. They can coexist. For example, bronze retains source evidence, silver integrates a Raw/Business Vault, and gold publishes star-schema marts.

Declare fact grain before keys and measures. Distinguish additive, semi-additive and non-additive measures. Use surrogate keys where dimension history requires versioned members. Ensure an unknown member or explicit unmatched-key process prevents silent fact loss.

> **Related item:** A materialized view can accelerate a consumer-shaped result, but it is not itself a complete dimensional model. Modeling defines meaning and relationships; materialization defines computation and refresh behavior.

---

## 9. Securing Data (8%)

### Traverse the three-level namespace

Unity Catalog uses `catalog.schema.object`. To query a table, a principal normally needs `USE CATALOG`, `USE SCHEMA` and the object privilege such as `SELECT`, subject to ownership, inherited privileges and other controls. Apply grants to groups or workload identities rather than individuals where practical. Review the current [privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/privileges).

Ownership permits management beyond ordinary data access, so separate owner/steward roles from consumers. Catalog and schema organization should reflect domain, lifecycle and isolation requirements; workspace folders are not the data-security hierarchy.

### Secure lifecycle and sensitive data

- Prefer managed tables when Databricks should manage the data lifecycle; use external tables when an external lifecycle is a requirement, not as an automatic default.
- Store files in governed volumes where appropriate rather than unmanaged workspace paths.
- Classify and tag sensitive columns, but enforce protection with privileges and supported fine-grained controls.
- Grant analysts the curated views or tables needed for the question, not blanket catalog access.
- Verify who can use the SQL warehouse and who can share the dashboard or Genie space.
- Record owner, business purpose, retention, recipients and review date for shared assets.

> **Related item:** Object privileges, row filters, column masks, ABAC policies, workspace bindings and dashboard/Genie permissions operate at different layers. Begin with least privilege and a simple governed view; add dynamic controls only when the requirement and supported operations justify them.

---

## Integrated decision scenarios

### Scenario A — governed executive revenue dashboard

A global retailer needs daily revenue, margin and return trends by region. Define the fact grain, validate currency and late-return rules, identify certified gold sources in Catalog Explorer, trace their lineage, and query with ANSI SQL. Check unmatched dimensions and reconcile totals. Publish an AI/BI dashboard with a region filter and controlled date parameter, schedule refresh, share to an executive group and configure an alert with an owner. Prove source, warehouse, dashboard and catalog permissions separately.

### Scenario B — supplier data without uncontrolled copying

A supplier offers governed data through Marketplace/Delta Sharing, while an operational attribute remains in a supported federated database. Compare freshness, latency and access boundaries. Use fully qualified names, filter early, inspect the cross-system plan and materialize only when repeated computation and freshness justify it. Record provider/recipient ownership, query history, data version and recovery when the remote source is unavailable.

### Scenario C — trusted sales Genie space

Business users want natural-language pipeline analysis. Curate a narrow star-shaped model, define opportunity stage, fiscal time and currency rules, select a warehouse, add sample questions and validated Trusted Assets, and restrict sharing. Build benchmark questions for total pipeline, conversion and aging; inspect generated SQL and edge cases. Use feedback to correct metadata or instructions and re-test rather than accepting popular answers as truth.

---

## Hands-on lab sequence

1. **Catalog evidence:** In Catalog Explorer, find a certified dataset; record owner, type, tags, schema, history and upstream/downstream lineage. Explain which signals imply trust and which do not.
2. **Controlled upload:** Upload a small CSV, override at least one inferred type, create a governed table and document how production intake would replace the manual route. Test a malformed and duplicate row.
3. **ANSI SQL correctness:** Join a fact to two dimensions, calculate exact and approximate distinct counts, use a window calculation, and reconcile row counts, unmatched keys and totals.
4. **Objects and history:** Create a managed table, external table, standard view and materialized result where available. Change a Delta table, inspect history and reproduce an earlier result within retention.
5. **Query investigation:** Run a deliberately inefficient but safe query. Capture query history/profile evidence, change one factor and compare correctness, scan/shuffle and runtime under similar cache conditions.
6. **AI/BI dashboard:** Build a multi-page dashboard with two datasets, three justified visual types, a filter, a parameter and clear titles/units. Publish, share to a test group, schedule refresh and test an alert failure.
7. **Genie space:** Curate a narrow dataset, write domain instructions and sample questions, add a trusted query, create five benchmark questions, inspect generated SQL and correct one grounded failure.
8. **Security proof:** Create analyst and steward groups or a written simulation. Build a catalog/schema/object grant matrix, test allowed and denied SQL/dashboard/Genie actions, then remove temporary access and artifacts.

## Readiness checks

### Platform, management and import

- [ ] I can distinguish Delta Lake, Unity Catalog, Databricks SQL, Lakeflow Jobs/pipelines, Mosaic AI and the Data Intelligence Engine.
- [ ] I can explain managed versus external table lifecycle.
- [ ] I can use certification, ownership, tags and lineage without treating any one signal as proof of correctness.
- [ ] I can explain provider, share and recipient roles in Delta Sharing/Marketplace.
- [ ] I can clean null, invalid and duplicate data with an explicit survivor and rejection rule.
- [ ] I can select upload, file ingestion, connector, federation or sharing from ownership and freshness requirements.
- [ ] I can document why a UI upload is not a production pipeline.
- [ ] I can distinguish medallion quality layers from physical or dimensional model patterns.

### SQL and query analysis

- [ ] I can select a SQL warehouse from concurrency, latency, network, feature and cost requirements.
- [ ] I can separate warehouse, catalog, schema, object and presentation-layer permissions.
- [ ] I can predict inner, outer and multi-key join effects at a declared grain.
- [ ] I can explain `UNION` versus `UNION ALL` and exact versus approximate distinct counts.
- [ ] I can handle nulls correctly in counts, averages and cleanup logic.
- [ ] I can create managed/external tables and standard/materialized views deliberately.
- [ ] I can distinguish streaming tables from materialized and standard views.
- [ ] I can reason about a Delta-to-federated-source join and pushdown boundary.
- [ ] I can use table history/time travel without promising indefinite rollback.
- [ ] I can move from query history to profile evidence and one testable tuning hypothesis.
- [ ] I can explain what Photon can accelerate and what it cannot correct.
- [ ] I can control cache state when comparing query performance.
- [ ] I can choose and measure liquid-clustering keys rather than applying them by habit.

### Dashboards, Genie, modeling and security

- [ ] I can choose a visualization from the question and identify a misleading alternative.
- [ ] I can distinguish field filters from query parameters and test permitted/default values.
- [ ] I can explain publish, share, refresh, subscribe, embed and alert as different operations.
- [ ] I can identify the identity used for dashboard data access.
- [ ] I can define a narrow Genie domain with curated sources and business semantics.
- [ ] I can inspect generated SQL and validate Genie answers independently.
- [ ] I can use feedback and benchmarks without treating them as automatic truth.
- [ ] I can maintain instructions, metadata, Trusted Assets and benchmark coverage after a schema change.
- [ ] I can choose star, snowflake or Data Vault from integration and consumption needs.
- [ ] I can define fact grain, keys, conformed dimensions and measure additivity.
- [ ] I can traverse `catalog.schema.object` and state required use/object privileges.
- [ ] I can explain why ownership is more powerful than ordinary access.
- [ ] I can apply least privilege across data, warehouse, dashboard and Genie layers.

## Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick the explanation, lab environment, course, or assessment that closes a demonstrated gap; spend at least as much time producing and testing SQL, dashboards and Genie evidence as watching video. Durations are planning estimates checked September 1, 2026 and may change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page and detailed exam guide](https://www.databricks.com/learn/certification/data-analyst-associate) | Free | 1–2 hours to map objectives and inspect linked sample format; do not reproduce vendor questions |
| [Databricks Academy](https://customer-academy.databricks.com/) — search for *AI/BI for Data Analysts* and *SQL Analytics on Databricks* | Free account or customer/partner entitlement varies | Approximately 8–16 hours selected learning, plus labs; verify current catalog durations after sign-in |
| [Databricks Free Edition](https://www.databricks.com/learn/free-edition) | Free account | 12–24 hours across the eight labs and targeted experiments |
| [Databricks SQL documentation](https://docs.databricks.com/aws/en/sql/) | Free | 4–8 hours selected reading and reproduction |
| [Databricks YouTube](https://www.youtube.com/@Databricks) | Free | 2–5 hours of selected current SQL, dashboards, Genie and Unity Catalog sessions |
| [Pluralsight: Databricks Certified Data Analyst Associate path](https://www.pluralsight.com/paths/databricks-certified-data-analyst-associate) | Paid/trial; includes practice exam | About 7 hours for five courses, plus 1–2 hours for assessment/review; 2025 material needs an October 2025 Genie/objective gap check |
| [Whizlabs: Databricks Certified Data Analyst Associate](https://www.whizlabs.com/databricks-certified-data-analyst-associate/) | Paid; training/practice product | Provider totals were not stably exposed publicly; budget 4–10 hours, verify after sign-in and reject recalled-question claims |
| [Databricks Community certification forum](https://community.databricks.com/t5/certifications/ct-p/databricks-certifications) | Free | 30–90 minutes for current program announcements; community answers are secondary evidence |

Use practice questions to diagnose a domain and explain every option from the official guide and documentation. Do not memorize recalled live-exam content. Recheck the live weighted page, linked PDF, course replacement note and volatile AI/BI behavior near the appointment.
