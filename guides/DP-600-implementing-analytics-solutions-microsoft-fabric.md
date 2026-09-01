---
exam_code: DP-600
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# DP-600 Implementing Analytics Solutions Using Microsoft Fabric Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 21, 2026 objectives and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dp-600-coverage-record). The [official DP-600 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600) is authoritative.

**Current baseline:** Skills measured as of July 21, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Official source:** [DP-600 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600)

## How to use this guide

DP-600 tests the contract between an analytical source, a governed Fabric item and a semantic model consumed by people or AI. For every design, trace:

1. business grain, freshness, history, security and latency requirements;
2. lakehouse, warehouse, eventhouse, shortcut/OneLake integration and semantic-model choices;
3. ingestion/access, transformation, dimensional model and quality rules;
4. workspace/item/data-layer access and governance metadata;
5. storage mode, relationships, DAX, refresh/fallback and performance;
6. version control, deployment, lineage/impact analysis and rollback;
7. SQL, KQL, DAX or visual-query evidence that proves correctness.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Maintain a data analytics solution | 25–30% | Is the solution securely governed, reusable and deployable without breaking downstream consumers? |
| Prepare data | 45–50% | Is data in the right store, grain, shape and quality for repeatable analysis? |
| Implement and manage semantic models | 25–30% | Does the model express trusted business meaning with correct security, scale and performance? |

---

## 1. Maintain a data analytics solution

### Security and governance layers

Fabric authorization is layered. Workspace roles grant broad collaborative capability; item permissions can share a specific artifact; data-plane controls restrict rows, columns, objects or files. Always grant at the lowest layer that satisfies the task and test through the same endpoint the consumer uses.

| Layer | Typical control | Question to prove |
|---|---|---|
| Workspace | Admin, Member, Contributor, Viewer | Can this person create/manage all workspace content or only consume it? |
| Item | Read, share/build or item-specific permission | Can the person discover/use this exact lakehouse, warehouse, eventhouse or semantic model? |
| SQL/data store | SQL granular permissions, RLS, CLS/OLS, masking | Which schemas, objects, rows and columns can this identity query? |
| OneLake/file | OneLake security roles or file/folder access under current capabilities | Can a non-SQL/Spark/OneLake path bypass the intended restriction? |
| Semantic model | Build, RLS, OLS | Can the consumer create reports and see only allowed business data? |

[Secure and govern analytics data](https://learn.microsoft.com/en-us/training/paths/secure-govern-analytics-data/) emphasizes that workspace/item access and data-store security complement one another. A Viewer plus semantic-model RLS is common for report consumers; a workspace Contributor can have broader data access than RLS testing suggests. Validate `View as` and a real restricted test identity, Direct Lake/DirectQuery behavior and downstream export/build routes.

Row-level security filters rows. Column-level or object-level security hides columns/tables/metadata. Dynamic data masking changes displayed values but is not equivalent to denying access. File-level controls govern direct OneLake/file access. Choose the control at the actual exposure path, not from its name.

Apply sensitivity labels to supported items to communicate and enforce information-protection behavior under configured policies. Endorsement signals trust: promoted is owner/community recommendation; certified requires the organization's certification process; master-data endorsement identifies authoritative reusable data under current Fabric behavior. Endorsement does not grant permission or prove technical quality. Document owner, definition, lineage, freshness and support SLA.

> **Related item:** A semantic model can correctly enforce RLS while a user with direct lakehouse or warehouse access reads the underlying rows. Secure every path, including SQL, OneLake, Spark, XMLA, Analyze in Excel and export where applicable.

### Analytics development lifecycle

Configure supported Git integration at the workspace and map the correct branch/directory. Treat the workspace as a deployable environment, not the only copy. Define branch strategy, ownership, secrets/connections/parameters, conflict handling and synchronization direction. Review unsupported-item and serialization limitations before assuming a complete workspace round trip.

A Power BI Desktop project (`.pbip`) decomposes report and semantic-model definitions into source-control-friendly files. Store text definitions, not credentials or local caches. Use deterministic formatting, small changes and validation. A `.pbit` template packages report/model structure without data for reuse; `.pbids` describes a data-source connection experience; a shared semantic model centralizes measures/security/business meaning for thin reports. They solve different reuse problems.

Deployment pipelines move supported Fabric/Power BI items across stages. Configure stage workspaces, deployment rules/bindings/parameters and approval/testing. A successful deployment proves artifact movement, not data correctness. Validate connections, credentials, refresh, permissions, semantic-model queries and downstream reports after promotion.

Use lineage view and impact analysis before changing or deleting lakehouses, warehouses, dataflows, semantic models or shared fields/measures. Automated lineage can be incomplete for external or dynamically referenced consumers, so combine it with ownership/usage records. Classify changes as additive, compatible or breaking and keep rollback artifacts.

The XMLA endpoint allows supported external tools and APIs to inspect/deploy/manage semantic models under workspace capacity and permission requirements. Use read-only versus read/write modes appropriately, service principals/managed identities where supported, transactions and backups/versioned metadata. Test processing and queries after deployment.

> **Related item:** Git synchronization, deployment pipelines and XMLA deployment are three lifecycle mechanisms. Decide which owns each artifact so two automation paths do not overwrite the same production model.

---

## 2. Prepare data

### Choose and connect to the data store

[Explore Fabric analytics data stores](https://learn.microsoft.com/en-us/training/paths/explore-analytics-data-stores/) frames OneLake as the tenant-wide logical data lake. Choose the item from workload rather than team title:

| Store | Strong fit | Query/processing strengths |
|---|---|---|
| Lakehouse | Delta/Parquet data, Spark engineering plus SQL analytics | Open-file lake patterns, notebooks, shortcuts and SQL read access |
| Warehouse | Governed relational analytics and dimensional models | Full transactional T-SQL capabilities supported by Fabric Warehouse |
| Eventhouse | High-volume time/event/telemetry and Real-Time Intelligence | KQL ingestion, exploration and near-real-time analysis |
| Semantic model | Curated business metrics/relationships/security for BI and AI | DAX and report/agent consumption; Import, DirectQuery, Direct Lake or composite choices |

Create connections with the correct authentication, gateway and privacy/credential boundary. Prefer managed organizational connections and least privilege. Record owner, source, credential rotation, network/gateway, refresh, data classification and support responsibility.

OneLake catalog supports discovery across governed Fabric data. Real-Time hub focuses streaming/event sources. A OneLake shortcut references data without making another managed copy; validate source availability, security propagation, supported format/location and lifecycle. OneLake integration can expose applicable Eventhouse data or semantic-model storage paths without indiscriminate duplication. **VERIFY CURRENT:** shortcut, mirroring, OneLake integration and catalog names/capabilities evolve rapidly.

Choose ingest/copy when you need an owned snapshot, transformation boundary, independent retention/performance or source isolation. Choose access/shortcut when freshness, minimized duplication and shared ownership outweigh source dependency. Record data movement, egress, residency, deletion and schema-change behavior.

### Transform to an analytical contract

[Design and transform analytics data](https://learn.microsoft.com/en-us/training/paths/design-transform-analytics-data/) covers Dataflows Gen2/Power Query, Spark notebooks and T-SQL. Select by source, scale, team skill, required libraries, transaction semantics and operations:

- Dataflows Gen2 provide low-code Power Query transformations and destinations; preserve query folding when it pushes work efficiently to the source.
- notebooks use Spark SQL/PySpark for distributed transformation and Delta-table operations; partition/file sizing and idempotency matter.
- T-SQL provides views, functions, stored procedures and set-based warehouse transformations.
- visual query tools support interactive selection/filter/aggregation and can expose generated logic for review.

Define the target grain before joining. A fact row describes a business event/snapshot at one grain; dimensions describe analysis context. Use surrogate keys when source/business keys are unstable or history requires them. Conformed dimensions enable comparable measures across facts. Handle late-arriving facts/dimensions and slowly changing attributes deliberately.

Star schemas favor understandable one-to-many filter paths. Denormalization reduces runtime joins but duplicates data and creates update responsibility. Aggregations precompute a higher grain for speed; retain detail or drill-through strategy. Views encapsulate reusable query logic; stored procedures coordinate multi-step parameterized transformations; functions return reusable computations under engine limitations.

Data-quality order matters:

1. profile distribution, uniqueness, nulls, type and referential integrity;
2. normalize types/time zones/codes and retain raw evidence;
3. define duplicate business key and survivorship rule;
4. join with known cardinality and inspect unmatched/exploding rows;
5. impute, reject or flag missing values with business approval;
6. aggregate only after detail grain is correct;
7. reconcile counts, totals and exceptions to source controls.

An accidental many-to-many join can produce valid-looking but inflated totals. Prove row counts and key uniqueness before and after every merge. Make transformation reruns idempotent and partition-aware; avoid many tiny Delta files and unbounded full-table rewrites.

### Query and analyze with the right language

SQL is natural for relational/set-based warehouse and SQL-endpoint analysis. KQL is natural for event/time-series exploration in Eventhouse. DAX evaluates semantic-model measures in filter/row context. The visual query editor builds supported transformations/queries interactively. Know how equivalent select/filter/group operations differ, but do not treat the languages as interchangeable.

For SQL, practice joins, CTEs, window functions, grouping, null semantics, views and stored procedures. For KQL, practice `where`, `project`, `extend`, `summarize`, time windows and joins. For DAX, practice measures with variables, `CALCULATE`, iterators, table filters, time/context transitions, window and information functions. Validate totals and filter context, not just a sample row.

> **Related item:** Power Query/M shapes data before model evaluation; DAX calculates over the semantic model at query/refresh time depending on object type. A transformation and a measure can return the same sample result but have different refresh, storage and security behavior.

---

## 3. Implement and manage semantic models

### Model design and storage mode

Start with a star schema and measures, not report visuals. Define fact grain, additive/semi-additive/nonadditive measures, conformed dimensions, date role-playing, unknown members and business definitions. Hide technical keys and default summarize behavior where appropriate.

Relationships need correct cardinality, active direction and filter propagation. Favor single-direction dimension-to-fact. Use an inactive relationship plus `USERELATIONSHIP` for alternate roles where appropriate. A bridge table resolves many-to-many business relationships at an explicit grain; bidirectional filtering can solve a specific requirement but increases ambiguity and performance/security risk.

| Storage mode | Data behavior | Use when |
|---|---|---|
| Import | Compressed model copy refreshed on schedule/on demand | Fast interactive queries and manageable freshness/model size |
| DirectQuery | Queries source at interaction time | Source-controlled freshness/size with acceptable source latency/concurrency |
| Direct Lake | Reads OneLake Delta data through the Fabric semantic engine | Fabric-resident data with low-copy, high-performance goals and supported design |
| Composite | Combines storage modes/sources | Requirements genuinely need mixed behavior and relationship constraints are understood |

Large semantic model storage format supports models beyond ordinary limits and XMLA/write scenarios under capacity configuration. Incremental refresh partitions historical versus refresh-window data and can add real-time behavior where supported; define date parameters, policy, detect-data-change logic and initial-load strategy.

Direct Lake has refresh/framing and fallback behavior. Configure and observe default fallback: a model intended for Direct Lake may use DirectQuery or fail depending on current mode/configuration and unsupported condition. The July 2026 blueprint explicitly distinguishes Direct Lake on OneLake from Direct Lake on a SQL analytics endpoint. Choose from supported source/security/model requirements and verify current limitations. **VERIFY CURRENT:** Direct Lake modes, fallback, refresh/framing and security support.

### DAX and reusable calculation design

Prefer explicit measures. Use variables to make logic readable and avoid repeated expression evaluation. Understand row context, filter context and context transition. Iterators evaluate an expression per table row; table-filter functions shape the filter set; window functions operate over ordered partitions; information functions expose state/type/context.

Test measures at detail, subtotal, grand total, no-data, multi-select and restricted-user contexts. Avoid calculated columns for logic that should respond to report filters. Reduce high-cardinality text and unnecessary calculated objects.

Calculation groups centralize repeated calculation transformations such as time intelligence; precedence matters when groups interact. Dynamic format strings change presentation without converting numeric results to text. Field parameters let report consumers switch dimensions/measures through a generated model construct; secure underlying objects because hiding a field parameter option is not object security.

### Security and performance at enterprise scale

Semantic-model RLS filters rows by role; dynamic RLS maps the signed-in user/group to security data. OLS hides model objects. Test role membership, effective identity, workspace permissions, Direct Lake/DirectQuery behavior and build/export paths. Keep security tables and relationships simple enough to audit.

[Design and manage semantic models](https://learn.microsoft.com/en-us/training/paths/design-manage-semantic-models-fabric/) combines Performance Analyzer, DAX/model tuning and lifecycle. Diagnose by layer:

1. Performance Analyzer separates visual rendering, DAX query and other delay;
2. DAX Studio/server timings/current tools expose storage-engine versus formula-engine work;
3. query plans and source telemetry show DirectQuery/SQL/KQL bottlenecks;
4. capacity metrics show throttling/concurrency/refresh contention;
5. model metadata shows cardinality, relationships, partitions and unused objects.

Improve report visuals by reducing unnecessary visuals/interactions and high-cardinality results. Improve the model through star schema, fewer columns/rows, correct data types, reduced cardinality, efficient relationships and aggregations. Improve DAX by filtering columns rather than whole tables when appropriate, reusing variables, avoiding expensive iterators at broad grains and preserving storage-engine execution. Tune the proven bottleneck; moving to a larger capacity can mask a bad model.

### AI-ready analytics data

The current official course adds [AI-ready analytics data](https://learn.microsoft.com/en-us/training/paths/prepare-ai-ready-analytics-data/). AI consumers need a governed gold layer, unambiguous names/descriptions, curated measures, synonyms/linguistic context, stable relationships, provenance, freshness and security. Test natural-language questions against expected queries/results and adversarial ambiguity.

Fabric IQ ontology items express business concepts/relationships across governed sources and can support data agents/Graph experiences under current availability. An ontology is not a replacement for accurate source grain, semantic-model measures or permissions. Bind only approved data, assign owners and evaluate generated answers. **VERIFY CURRENT:** Fabric IQ, Graph, ontology and data-agent availability/licensing.

---

## Integrated scenarios

### Scenario 1: Governed sales model for regional managers

Land/source sales and dimension data, build a star at order-line grain, reconcile totals, and publish a shared semantic model. Grant consumers minimal workspace/item access, implement region RLS and test a real manager plus an unauthorized user. Add labels/endorsement, lineage and owner. Deploy through dev/test/prod and prove report totals and denial after promotion.

### Scenario 2: Near-real-time operations analytics

Ingest telemetry to Eventhouse and discover it in Real-Time hub; use KQL for time-window anomaly analysis and OneLake integration where supported. Combine governed reference data only at a defined grain. Choose Direct Lake/DirectQuery/import behavior based on freshness and supported source. Validate latency, late events, security and capacity under concurrent dashboard load.

### Scenario 3: Slow executive semantic model

Use Performance Analyzer to identify the slow visual/DAX query, then inspect model cardinality, relationships and engine timings. Replace a broad bidirectional relationship or expensive iterator only when evidence supports it; add aggregation or tune Direct Lake/source behavior. Retest same filters, concurrency and RLS user, then deploy with rollback and impact analysis.

---

## Hands-on labs

### Lab 1 — Security-path matrix

Create a workspace, lakehouse/warehouse and semantic model. Assign workspace/item/data/RLS controls to test identities and query through multiple endpoints. **Evidence:** allowed/denied matrix and effective permissions.

### Lab 2 — Git and deployment lifecycle

Create a PBIP, connect a workspace to version control, deploy stages and make a controlled breaking change. **Evidence:** diff, impact analysis, validation and rollback.

### Lab 3 — Store and access decision

Model one batch, one relational and one streaming requirement across lakehouse, warehouse and eventhouse; implement a shortcut or OneLake integration. **Evidence:** decision record and freshness/security test.

### Lab 4 — Dimensional transformation

Build fact/dimensions with Dataflow Gen2, notebook or T-SQL. Handle duplicate/null/late data and a slowly changing dimension. **Evidence:** reconciliation and rerun/idempotency result.

### Lab 5 — SQL, KQL and DAX comparison

Answer the same filter/aggregate business question in each applicable language. **Evidence:** query, result and explanation of evaluation context.

### Lab 6 — Semantic model and DAX

Create relationships/bridge, measures with variables/iterators, calculation group, dynamic format and field parameter. **Evidence:** detail/total/filter tests.

### Lab 7 — Direct Lake and refresh

Configure Direct Lake and observe refresh/framing/fallback behavior; compare with Import/DirectQuery and configure incremental refresh in a lab model. **Evidence:** storage/freshness/performance table.

### Lab 8 — Performance and AI readiness

Diagnose a slow visual/model, tune it, then add metadata/curated measures and evaluate representative natural-language questions. **Evidence:** before/after timings and answer-quality rubric.

---

## Knowledge checks

1. **Workspace role versus item permission?** Broad workspace collaboration versus access to a specific Fabric item.
2. **RLS versus OLS/CLS?** Restrict rows versus hide model/database objects or columns.
3. **Masking versus denial?** Masking changes presentation; permission prevents access.
4. **Why secure every endpoint?** Semantic-model RLS does not automatically govern direct SQL/OneLake/Spark access.
5. **Sensitivity label purpose?** Classify/protect supported content under policy; it does not grant access.
6. **Endorsement purpose?** Signal promoted/certified/master trust, not authorize or guarantee correctness.
7. **PBIP value?** Source-control-friendly project representation of report/model artifacts.
8. **PBIT versus PBIDS?** Reusable report/model template versus data-source connection description.
9. **Deployment success proves correctness?** No; validate bindings, refresh, permissions, queries and consumers.
10. **Why impact analysis?** Identify downstream assets/owners before a breaking source/model change.
11. **XMLA endpoint purpose?** External semantic-model inspection, deployment and management under supported mode/permissions.
12. **Lakehouse fit?** Delta/open-file and Spark plus SQL analytics patterns.
13. **Warehouse fit?** Relational dimensional analytics and T-SQL transformation/query.
14. **Eventhouse fit?** High-volume event/time-series ingestion and KQL analysis.
15. **Shortcut versus copy?** Reference source data versus own another stored snapshot.
16. **OneLake catalog versus Real-Time hub?** Governed data discovery versus streaming/event discovery/operations.
17. **Transformation grain first?** Joins/keys/aggregates are unsafe until each target row's meaning is explicit.
18. **Why reconcile every join?** Many-to-many expansion can silently inflate valid-looking totals.
19. **Query folding value?** Push supported transformation work to a capable source.
20. **Idempotent pipeline?** Rerun produces the intended state without duplicate/corrupt results.
21. **SQL versus KQL versus DAX?** Relational sets, event/time-series pipelines and semantic-model evaluation.
22. **Import tradeoff?** Fast compressed queries but refresh copy/freshness/capacity management.
23. **DirectQuery tradeoff?** Source freshness/control but source latency/concurrency and query limitations.
24. **Direct Lake promise and risk?** Low-copy Fabric performance with mode/fallback/framing/security constraints.
25. **Composite model risk?** Mixed storage/source relationships create semantic and performance complexity.
26. **Why star schema?** Clear grain and one-to-many filter propagation improve correctness/usability/performance.
27. **Bridge-table purpose?** Express a genuine many-to-many business relationship at a controlled grain.
28. **Why avoid broad bidirectional filters?** Ambiguous paths, slower queries and harder security reasoning.
29. **Measure versus calculated column?** Query-context calculation versus stored row-by-row refresh calculation.
30. **Calculation group purpose?** Reuse calculation transformations across measures with controlled precedence.
31. **Dynamic format string advantage?** Retains numeric data type while changing display.
32. **Incremental refresh purpose?** Refresh a policy-defined recent partition window while retaining history.
33. **Performance Analyzer first value?** Separates visual, DAX/query and other delay.
34. **Capacity upgrade first fix?** No; identify model/query/source/visual bottleneck first.
35. **What makes data AI-ready?** Governed grain, curated measures, meaning/metadata, provenance, freshness, security and evaluated questions.
36. **What proves a release?** Versioned artifact plus deployment, data/refresh/security/query/downstream tests and rollback.

---

## Places to learn

This is a curated starting point, **not a complete list**, and it is not meant to be consumed in full. Choose one primary route, build a Fabric solution, and add only resources that close measured gaps. Reconcile every older source with the July 21, 2026 blueprint, especially Direct Lake on OneLake versus SQL analytics endpoint, OneLake security, Real-Time hub, AI-ready data, Fabric IQ and current endorsement/lifecycle behavior.

The five official paths are [analytics data stores](https://learn.microsoft.com/en-us/training/paths/explore-analytics-data-stores/) (4h34), [transform analytics data](https://learn.microsoft.com/en-us/training/paths/design-transform-analytics-data/) (5h14), [semantic models](https://learn.microsoft.com/en-us/training/paths/design-manage-semantic-models-fabric/) (6h21), [AI-ready analytics data](https://learn.microsoft.com/en-us/training/paths/prepare-ai-ready-analytics-data/) (3h50), and [security/governance](https://learn.microsoft.com/en-us/training/paths/secure-govern-analytics-data/) (3h21), totaling **23 hours 20 minutes**.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official DP-600 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-analytics-engineer-associate/) | Public | 1–2 hours initially; 15 minutes per recheck |
| Five official paths from [DP-600T00](https://learn.microsoft.com/en-us/training/courses/dp-600t00) | Public | 23 hours 20 minutes listed; allow 45–75 hours with exercises/notes |
| DP-600T00 instructor-led course | Paid/partner delivery | 4 days listed |
| [Microsoft DP-600 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/fabric-analytics-engineer-associate/practice/assessment?assessment-type=practice&assessmentId=90&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Pluralsight DP-600 path](https://www.pluralsight.com/paths/implementing-analytics-solutions-using-microsoft-fabric-dp-600) | Paid | 7 hours / 5 courses plus practice exam; 2024 content, supplement July 2026 |
| [O'Reilly DP-600 Study Guide](https://www.oreilly.com/library/view/microsoft-fabric-analytics/9798341634800/) by Brian Bønk and Valerie Junk | Paid | 10 hours 23 minutes / 390 pages; February 2026, reconcile July changes |
| [Microsoft Press Exam Ref DP-600 on O'Reilly](https://www.oreilly.com/library/view/exam-ref-dp-600/9780135336014/) | Paid | 9 hours 22 minutes / 337 pages; August 2024, use update chapter and supplement July 2026 |
| [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor), [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics), and [Microsoft Fabric](https://www.youtube.com/@MicrosoftFabric) | Public | 3–12 hours selectively by current objective gap |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use published start/end times after sign-in |

No exact current Whizlabs or MeasureUp DP-600 product was independently verified in this review. Start with Microsoft's free assessment and source-explained questions; reject any provider claiming recalled live exam content.

## Final readiness checklist

- I can select lakehouse, warehouse, eventhouse, shortcut/OneLake integration and semantic-model modes from requirements.
- I can transform at an explicit grain, reconcile quality and query correctly with SQL, KQL and DAX.
- I can layer workspace, item, row/column/object/file and semantic-model controls and prove every access path.
- I can model star schemas, relationships, bridges, DAX and reusable calculations without ambiguous filters.
- I can configure and explain Import, DirectQuery, Direct Lake, composite, large-model and incremental-refresh behavior.
- I can diagnose visual, DAX, engine, source and capacity performance with evidence.
- I can version, deploy, inspect impact, validate, govern and roll back analytics assets.
- I can prepare governed semantics for AI without treating an ontology or generated answer as proof of correctness.

