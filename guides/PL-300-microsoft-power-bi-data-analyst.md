---
exam_code: PL-300
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# PL-300 Microsoft Power BI Data Analyst Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the April 20, 2026 objectives and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#pl-300-coverage-record). The [official PL-300 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300) is authoritative.

**Current baseline:** Skills measured as of April 20, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Official source:** [PL-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300)

## How to use this guide

PL-300 is an end-to-end analyst exam. It tests whether a report is correct, understandable, supportable, and appropriately secured—not whether its canvas merely looks polished. For each requirement, trace:

1. audience, business question, grain, freshness, latency, ownership, and security;
2. source, credential/privacy boundary, connector, gateway, and storage mode;
3. Power Query profiling, quality rule, transformation, key, and load behavior;
4. star schema, relationship/filter path, calculation location, and DAX context;
5. visual choice, interaction, accessibility, mobile, and narrative intent;
6. workspace, app/share route, semantic-model permission, RLS, label, and refresh;
7. reconciliation, restricted-user test, performance trace, and business acceptance evidence.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Prepare the data | 25–30% | Is the source connected, profiled, cleaned, shaped, keyed, and loaded at the intended grain? |
| Model the data | 25–30% | Do relationships and calculations return correct results under every filter and total? |
| Visualize and analyze the data | 25–30% | Does the report communicate the right insight accessibly and support defensible analysis? |
| Manage and secure Power BI | 15–20% | Can people receive fresh content through the correct distribution and security boundary? |

---

## 1. Prepare the data

### Requirements, sources, and storage mode

Start with the decision the report must support. Record business definitions, row grain, history, refresh/freshness target, expected volume, concurrency, data residency, source owner, and who may see which rows. A technically valid connection can still be the wrong analytical contract.

[Prepare data for analysis with Power BI](https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/) covers connectors, connectivity/storage choice, profiling, Power Query, and load. Use a shared semantic model when another team already owns trusted dimensions, measures, refresh, and security; confirm whether you need a live connection or are permitted to extend it with a local model.

| Mode | Where queries run | Strong fit | Primary tradeoff to prove |
|---|---|---|---|
| Import | Against an in-memory compressed copy | Fast interaction and supported modeling with acceptable refresh lag/size | Refresh window, capacity/model size, and copied-data governance |
| DirectQuery | Translated to the source during interaction | Source-controlled freshness/volume where the source can sustain queries | Source latency/concurrency, folding, limitations, and gateway/network path |
| Direct Lake | Semantic engine over supported data in OneLake | Fabric-resident Delta data with low-copy, high-performance goals | Supported source/model/security behavior, framing, and fallback/guardrail behavior |

The April 2026 blueprint explicitly adds Direct Lake to this decision. Do not reduce the choice to “fast versus current.” Test model features, source load, user concurrency, security, licensing/capacity, refresh or framing behavior, and failure response. **VERIFY CURRENT:** Direct Lake prerequisites, guardrails, fallback behavior, and Copilot/capacity requirements change quickly.

Data-source settings include location, authentication method, credentials, encryption, privacy levels, and sometimes gateway mapping. Privacy levels help prevent unintended combination across isolation boundaries; they are not a replacement for source authorization. Parameters make server/database/path/date/environment choices reusable. Do not put secrets in ordinary parameters.

> **Related item:** Query folding pushes supported Power Query steps to the source. A folded filter before a large import or DirectQuery operation can radically change performance; one non-folding step can move work to the mashup engine. Inspect the native query/folding indicator and source telemetry rather than assuming.

### Profile and clean before transforming

Power Query column quality, distribution, and profile reveal valid/error/empty values, distinctness, frequency, min/max, and patterns. Profiling may initially use the top 1,000 rows; switch to the entire data set when the decision requires it. A sample that misses the one malformed month is not quality evidence.

For every important column, define:

- meaning, type, nullability, allowed range/domain, uniqueness, and business key;
- locale/time-zone/currency behavior and whether leading zeros are significant;
- missing-value, invalid-value, duplicate, and late-arriving-data treatment;
- reconciliation control such as source row count, total amount, or exception count.

Set types deliberately and, where necessary, use locale-aware conversion. Text-to-number/date conversion, schema drift, unavailable files, credential failures, privacy/firewall conflicts, and source values that cannot be represented are different import-error classes. Preserve the original evidence before replacing errors or nulls. “Replace with zero” is a business decision, not generic cleaning.

### Transform and load at an explicit grain

Power Query (M) shapes data before model evaluation. Filter rows/columns early when safe, standardize names/types, split/combine columns, group and aggregate at a declared grain, and turn lists/records/JSON/XML into tables before expanding only required fields.

| Operation | What it changes | Common failure |
|---|---|---|
| Pivot | Distinct row values become columns | Unexpected new values create schema drift or aggregation ambiguity |
| Unpivot | Columns become attribute/value rows | Identifier columns are accidentally unpivoted or mixed types are introduced |
| Transpose | Rows and columns exchange orientation | Headers/types require repair; rarely a durable large-data design |
| Merge | Joins columns using keys and join kind | Nonunique keys multiply rows; unmatched rows disappear under the wrong join |
| Append | Stacks rows from compatible tables | Mismatched names/types create sparse or erroneous columns |
| Group | Aggregates rows to a higher grain | Detail is destroyed before reconciliation or later analysis needs it |

A fact table records an event, transaction, or snapshot at one declared grain. A dimension supplies descriptive filtering/grouping. Choose stable relationship keys; use a surrogate key when a business key changes, is composite, or must support history. Prove key uniqueness on the dimension side and reconcile row counts/totals before and after each merge.

Reference creates a new query whose steps begin from another query's result/definition, supporting shared staging logic. Duplicate copies the steps as an independent starting point. Neither should be chosen from the label alone: understand dependency, evaluation, maintenance, folding, and load behavior. Disable load for staging/helper queries that should not become model tables, but keep refresh dependencies valid.

> **Related item:** A reusable staging query does not guarantee one cached source read. Power Query evaluation and folding determine actual source work. Diagnose with folding indicators, query diagnostics, refresh history, and source logs.

---

## 2. Model the data

### Build a semantic model that explains itself

[Model data with Power BI](https://learn.microsoft.com/en-us/training/paths/model-power-bi/) starts from prepared data and develops relationships and DAX. Prefer a star schema: dimensions on the one side filter facts on the many side. Hide technical keys, assign useful formats/data categories/default summarization, and give tables, columns, and measures business-readable names and descriptions.

Relationship decisions require cardinality, active/inactive state, cross-filter direction, and referential integrity. Favor single-direction dimension-to-fact filters. Many-to-many relationships and bidirectional filters can be legitimate, but they make ambiguity, totals, performance, and RLS harder to reason about. Use a bridge table at an explicit grain for genuine many-to-many business relationships.

A role-playing dimension supplies multiple roles such as Order Date, Ship Date, and Due Date. Common patterns are one shared date table with one active relationship plus inactive relationships invoked by `USERELATIONSHIP`, or duplicated role-specific date dimensions when independent simultaneous filtering/usability warrants it. Create or import a contiguous common date table, mark it when required, and include the attributes needed for the organization's calendar.

### Put each calculation in the right layer

[Power BI calculation options](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculations-options) differ in timing, storage, context, and reuse:

| Calculation | Language/timing | Best question to ask |
|---|---|---|
| Power Query custom column | M at refresh | Can this row-level transformation fold or be computed once before modeling? |
| Calculated column | DAX at model refresh and stored | Must the result act as a slicer, grouping, relationship key, or row attribute? |
| Calculated table | DAX at model refresh and stored | Must this derived table participate in model relationships/metadata? |
| Measure | DAX at query time | Must the answer respond to report filter context and be reusable? |
| Visual calculation | DAX over the visual result | Is the calculation local to this visual's axes/aggregated result? |

Row context identifies a current row. Filter context is the set of filters applied by visuals, slicers, relationships, and DAX. `CALCULATE` evaluates an expression in modified filter context and can trigger context transition. Learn single aggregations, variables, iterators, basic statistics, and filter modifiers by predicting detail rows, subtotals, and grand totals before running them.

Time intelligence depends on a trustworthy date table, appropriate relationships, and calendar semantics. A semi-additive measure aggregates normally across some dimensions but differently across time—for example, month-end inventory is often last-observation logic rather than a sum of daily balances. Quick measures can teach patterns and accelerate authoring, but read and test the generated DAX.

Calculation groups centralize transformations such as current/prior/variance across many measures. Define precedence and formatting when groups interact. They reduce repetition but can hide complexity if names and scope are unclear. [Visual calculations](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-visual-calculations-overview) operate on the visual matrix and are not reusable semantic-model measures; use them for visual-local running totals, moving averages, or comparisons, then test sort/axis/filter changes.

> **Related item:** A measure belongs to the reusable business semantic layer; a visual calculation belongs to one presentation. If another report, Excel, API, or Copilot consumer needs the same definition, prefer a governed measure.

### Optimize from evidence

Remove unnecessary rows/columns before loading, use efficient data types, reduce high-cardinality columns and grain when business requirements allow, preserve star-schema filter paths, and avoid broad bidirectional relationships. Do not remove needed detail or preaggregate away valid questions merely to shrink a model.

[Performance Analyzer](https://learn.microsoft.com/en-us/power-bi/create-reports/performance-analyzer) separates DAX query, DirectQuery/source, visual display, and other time. Copy or run a visual's DAX in [DAX query view](https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view), then inspect whether the issue is a visual, measure, relationship, source query, model cardinality, or concurrency problem. Establish a reproducible baseline, change one hypothesis, and compare the same filters and user/security context.

---

## 3. Visualize and analyze the data

### Select and configure reports for a decision

[Design effective reports in Power BI](https://learn.microsoft.com/en-us/training/paths/power-bi-effective/) begins with audience, task, device, accessibility, and story. Choose visuals by analytical relationship:

- cards/KPIs for a small number of status values with context and target;
- bars for category comparison, lines for ordered time trends, and scatterplots for relationship/distribution;
- tables/matrices for precise detail and hierarchies, with restrained conditional formatting;
- maps only when location is analytically relevant and geocoding/granularity is reliable;
- decomposition tree, key influencers, anomaly detection, or other AI visuals when their assumptions and output can be explained.

Use consistent themes, formats, titles, units, sort order, colors, and whitespace. Apply conditional formatting to convey a defined threshold—not decoration. Separate report/page/visual filters from slicers users can see. Configure page size, background, wallpaper, display mode, and supported automatic page refresh for the intended consumption environment. Choose paginated reports for printable, pixel-controlled, multi-page operational output rather than forcing an interactive canvas to behave like a document.

Copilot can create narrative visuals, suggest or create report-page content, and summarize a semantic model/report. Its quality depends on clear model names/descriptions, curated measures, relationships, data quality, and verified business definitions. Treat generated DAX, visuals, and prose as drafts; validate totals, filters, claims, and sensitive-data exposure. **VERIFY CURRENT:** availability, capacity/licensing, UI, grounding, AI instructions, and supported Copilot experiences.

### Usability, storytelling, and accessibility

Bookmarks capture a configured report state and can power navigation/story views; decide whether data, display, current page, and selected visuals belong in the bookmark. Tooltips add context without crowding. Edit interactions so cross-filter/highlight/none behavior matches the question. Use buttons, page navigation, bookmark navigators, and drillthrough deliberately, and provide a visible return route.

Sync slicers only where a shared selection improves comprehension; hidden synced slicers can confuse users. Use the Selection pane to name, group, show/hide, and layer objects. Configure exports from the organization's data-loss requirements, not user convenience alone. Personalize visuals allows consumers to change supported fields/visuals but does not grant access to hidden or secured data.

Design mobile layouts instead of assuming desktop shrinking. For accessibility, provide logical tab order, descriptive titles/alt text, sufficient contrast, keyboard operation, meaningful labels, and alternatives to color-only meaning; test with a screen reader and keyboard. Accessibility is part of correctness because an insight unavailable to its audience is not effectively delivered.

### Analyze patterns without overclaiming

Use Analyze/Explain features, grouping, bins, clusters, reference/constant lines, error bars, forecasts, anomaly detection, and AI visuals to explore. Distinguish categorical from continuous axes, association from causation, forecast interval from certainty, and statistical anomaly from business incident.

Check grain, filter context, missing periods, seasonality, sample size, outliers, and measure definition before telling a story. Preserve the question, selected data, method, result, limitations, and business interpretation so another analyst can reproduce it.

> **Related item:** A visually compelling trend can be a modeling defect. Validate source totals, date continuity, relationships, DAX totals, filters, and refresh time before explaining the business.

---

## 4. Manage and secure Power BI

### Workspaces, assets, apps, and distribution

[Manage and secure Power BI](https://learn.microsoft.com/en-us/training/paths/manage-secure-power-bi/) covers workspaces, semantic models, distribution, dashboards, and security. A workspace is the collaborative container; a report is multi-page interactive content over one semantic model; a dashboard is a service artifact whose tiles may be pinned from multiple reports/models; an app packages curated workspace content for audiences.

| Distribution | Strong fit | Control to verify |
|---|---|---|
| Workspace access | Authors/operators collaborating on content | Role is no broader than necessary |
| App/audience | Managed, discoverable consumption for a group | Audience content, update process, Build/reshare options, and lifecycle |
| Direct share/item permission | Small or exceptional targeted access | Permission sprawl, reshare, and semantic-model dependency |
| Subscription/data alert | Scheduled delivery or threshold notification | Recipient access, supported visual/tile, data sensitivity, and refresh timing |
| Export/embed/publish route | Specific offline/application/public requirement | Tenant policy, identity, licensing, data leakage, and revocation |

Publish/import/update the correct report and semantic-model items, then verify connections, credentials, refresh, permissions, and dependent reports. Promote content when owners recommend it for reuse; certify only through the organization's governed certification process. Endorsement signals trust but does not grant permission or prove a result.

### Gateways and refresh

A gateway is required when the Power BI service cannot directly reach a source—for example, many on-premises or private-network sources. Configure the appropriate gateway/data-source mapping, authentication/credentials, privacy boundary, cluster availability, ownership, and monitoring. Personal and standard/enterprise gateway choices have different collaboration and administration implications.

Scheduled refresh updates imported semantic-model data; it does not make DirectQuery or Direct Lake identical to Import. Validate source availability, credential expiration, gateway status, timeout/resource limits, refresh history, and the report's displayed freshness. Coordinate schedule with source load and dependent transformations.

> **Related item:** Incremental refresh partitions a date-filtered table so recent periods refresh while history is retained under policy. It can reduce refresh cost, but it requires suitable date filtering/folding and an initial-load/partition strategy; it is adjacent operational depth rather than a named April 2026 subobjective.

### Roles, item permissions, semantic-model access, and RLS

Workspace Admin, Member, Contributor, and Viewer roles grant progressively different management/edit/consumption capabilities. Use groups, least privilege, and separation of duties. Item-level access can expose one artifact without broad workspace membership. Semantic-model permissions such as Read, Build, Reshare, and Write govern distinct actions; Build enables new content/analysis against the model and deserves explicit approval.

Define static RLS roles with fixed filters or dynamic RLS using identity-to-security-table mappings, then assign users or supported groups in the service. Test in Desktop and as a real restricted identity after publishing. Workspace users with edit capability are not ordinary RLS consumers; use Viewer/app consumption paths when RLS must apply and recheck current behavior. RLS filters rows, not columns or objects, and does not secure an independently accessible source.

Sensitivity labels classify and can protect supported Power BI content under Purview policy and downstream behavior. They do not replace permissions, RLS, tenant settings, or export controls. Test label inheritance/persistence and supported export routes with representative data. **VERIFY CURRENT:** licensing, label propagation, app/Org app behavior, tenant settings, and permission names can change.

---

## Integrated scenarios

### Scenario 1: Regional sales app

Acquire transaction and dimension data, define order-line grain, profile keys/nulls, and build a star model. Create reusable sales/margin measures and a role-playing date design; test details and totals. Publish an accessible desktop/mobile report through an app, assign regional dynamic RLS, schedule refresh through the gateway, label the content, and prove allowed/denied identities plus source reconciliation.

### Scenario 2: Near-real-time operations report

Compare DirectQuery and Direct Lake from source location, latency, modeling, security, capacity, and failure requirements. Build an anomaly/trend page with explicit intervals and freshness. Use Performance Analyzer/DAX query view and source telemetry under concurrency, then document which layer owns each bottleneck and how the report behaves during source or capacity degradation.

### Scenario 3: Executive report returns a wrong total

Trace the visual filter context through relationship cardinality/direction and measure logic. Check whether a merge multiplied facts, a bidirectional/many-to-many path is ambiguous, or a semi-additive balance was summed across dates. Repair at the correct layer, reconcile source/detail/subtotal/grand total, retest RLS, and only then update the narrative.

---

## Hands-on labs

### Lab 1 — Connect and profile

Connect to one file and one database source, configure parameters/privacy, profile all rows, and inject type/null/import errors. **Evidence:** source contract, profile, error taxonomy, and corrected refresh.

### Lab 2 — Power Query and folding

Build a staging/reference pattern, filter/transform data, compare merge and append, and inspect folding before/after a nonfolding step. **Evidence:** query plan/indicator, row-count reconciliation, and load settings.

### Lab 3 — Dimensional model

Create fact/dimensions, stable keys, one-to-many relationships, a bridge where justified, and role-playing dates. **Evidence:** model diagram plus unmatched/duplicate-key tests.

### Lab 4 — DAX calculation layers

Create aggregation, `CALCULATE`, time-intelligence, statistical, and semi-additive measures; compare a calculated column/table, calculation group, quick measure, and visual calculation. **Evidence:** detail/subtotal/total/filter test table.

### Lab 5 — Report story and accessibility

Build desktop/mobile pages with theme, conditional formatting, bookmarks, tooltip, drillthrough, sync slicer, Selection pane, and accessible navigation. **Evidence:** audience task test, keyboard/screen-reader notes, and export setting.

### Lab 6 — Analysis and Copilot

Use grouping/binning, reference/error/forecast features and an AI visual; generate one Copilot page/narrative where available. **Evidence:** assumptions, expected result, model improvements, validation, and corrected output.

### Lab 7 — Publish, distribute, and refresh

Publish to a workspace, configure app audience/item/model access, dashboard, subscription or alert, gateway, and scheduled refresh. **Evidence:** permission matrix, refresh history, freshness indicator, and failure drill.

### Lab 8 — RLS and performance

Implement static and dynamic RLS, test real identities, record Performance Analyzer output, inspect a visual in DAX query view, and tune one proven bottleneck. **Evidence:** denial proof and before/after timings with unchanged results.

---

## Knowledge checks

1. **Why define grain first?** It controls keys, joins, aggregation, relationships, and what one row means.
2. **Shared semantic model advantage?** Reuse governed measures, security, refresh, and business meaning.
3. **Import tradeoff?** Fast compressed queries in exchange for copied data, refresh lag, and model-capacity management.
4. **DirectQuery tradeoff?** Source-time freshness/control in exchange for source latency, concurrency, folding, and feature constraints.
5. **Direct Lake fit?** Supported OneLake data where low-copy analytical performance and its guardrails/security fit.
6. **Privacy level purpose?** Control data combination isolation; it does not authorize source access.
7. **Why not store a secret in a parameter?** Ordinary parameters are configuration, not a secret store.
8. **Why profile all rows?** A top-1,000 sample can miss quality failures elsewhere.
9. **Merge versus append?** Join columns by keys versus stack compatible rows.
10. **Why reconcile a merge?** Duplicate keys can multiply rows and silently inflate totals.
11. **Reference versus duplicate?** Dependent reusable query logic versus an independently copied starting definition.
12. **Disable load when?** For helper/staging queries that should not become model tables.
13. **Fact versus dimension?** Measurable event/snapshot at a grain versus descriptive filtering context.
14. **Why star schema?** Clear one-to-many filter paths improve correctness, usability, and performance.
15. **Bridge-table purpose?** Represent a genuine many-to-many relationship at a controlled grain.
16. **Why avoid broad bidirectional filtering?** It increases ambiguity, performance cost, and RLS reasoning risk.
17. **Role-playing dimension?** One business entity such as Date used in multiple semantic roles.
18. **Row versus filter context?** Current-row evaluation versus filters shaping the calculation's data set.
19. **What does `CALCULATE` do?** Evaluates an expression under modified filter context and can perform context transition.
20. **Semi-additive example?** Inventory summed across products but evaluated as last balance across time.
21. **Measure versus calculated column?** Reusable query-time result versus stored row-level refresh result.
22. **Visual calculation versus measure?** Visual-local calculation over displayed aggregates versus reusable semantic logic.
23. **Calculation group value?** Centralize repeated measure transformations with defined precedence.
24. **First performance step?** Reproduce and measure the slow interaction with Performance Analyzer.
25. **Why DAX query view?** Inspect/run a visual's semantic query and test measure/query behavior.
26. **Paginated report fit?** Pixel-controlled printable or multi-page operational output.
27. **Bookmark risk?** Capturing unintended data/display/page state can reset or confuse user selections.
28. **Why design mobile separately?** A desktop canvas rarely becomes usable merely by shrinking.
29. **Accessible color rule?** Never make color the only carrier of meaning; also use labels/symbols/text and contrast.
30. **Forecast proves causation?** No; it models a pattern with assumptions and uncertainty.
31. **Workspace versus app?** Author collaboration container versus curated audience distribution package.
32. **Dashboard versus report?** Single-page service tiles possibly from multiple models versus multi-page interaction over one model.
33. **When is a gateway needed?** When the service cannot directly reach/authenticate to the source network path.
34. **Build permission impact?** Lets a user create analysis/content against the semantic model; grant deliberately.
35. **RLS security boundary?** Rows through the governed model for applicable consumers, not columns or separately accessible sources.
36. **What proves release readiness?** Reconciled results, correct filters/totals, accessibility, performance, refresh, distribution, and allowed/denied identity tests.

---

## Places to learn

This is a curated starting point, **not a complete list**, and it is not meant to be consumed in full. Choose one primary course or path, build an end-to-end report, and add only resources that close measured gaps. Reconcile every resource with the April 20, 2026 blueprint, especially Direct Lake, calculation groups, DAX query view, Copilot, visual calculations, current usability controls, and workspace/asset changes.

The five official paths are [data-analytics foundations](https://learn.microsoft.com/en-us/training/paths/data-analytics-microsoft/) (1h28), [prepare data](https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/) (4h33), [model data](https://learn.microsoft.com/en-us/training/paths/model-power-bi/) (5h50), [effective reports](https://learn.microsoft.com/en-us/training/paths/power-bi-effective/) (5h07), and [manage and secure](https://learn.microsoft.com/en-us/training/paths/manage-secure-power-bi/) (2h54), totaling **19 hours 52 minutes**.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official PL-300 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/) | Public | 1–2 hours initially; 15 minutes per recheck |
| Five official paths from [PL-300T00](https://learn.microsoft.com/en-us/training/courses/pl-300t00) | Public | 19h52 listed; allow 35–60 hours with exercises and notes |
| PL-300T00 instructor-led course | Paid/partner delivery | 3 days listed |
| [Official MicrosoftLearning PL-300 labs](https://github.com/MicrosoftLearning/PL-300-Microsoft-Power-BI-Data-Analyst) (MIT) | Public | 15–25 hours estimated; repeat without step-by-step help |
| [Microsoft PL-300 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/practice/assessment?assessment-type=practice&assessmentId=48&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Microsoft Reactor PL-300 orientation](https://www.youtube.com/watch?v=tDwNtxAB49k) | Public | 1 hour listed; June 2026 overview, not a complete course |
| [Pluralsight PL-300 path](https://www.pluralsight.com/paths/microsoft-certified-microsoft-power-bi-data-analyst-pl-300) | Paid | 12 hours, 4 courses, 4 labs, and practice exam listed; courses Sep 2025–Jan 2026, labs Jul 2026 |
| [O'Reilly PL-300 Study Guide](https://www.oreilly.com/library/view/microsoft-power-bi/9781098175276/) by Paul Turley | Paid | 12h07 / 478 pages; March 2026 and based on 2025 revisions, supplement April additions |
| [Udemy PL-300 exam-prep course](https://www.udemy.com/course/pl-300-da-100-microsoft-power-bi-data-analyst-exam-prep/) by Nikolai Schuler | Paid | 8h57 / 120 lectures plus full practice exam; updated August 2026 |
| [Coursera Microsoft PL-300 Exam Preparation and Practice](https://www.coursera.org/learn/microsoft-pl-300-exam-preparation-and-practice/) | Paid/subscription; audit terms vary | About 38 hours listed including guided activities and mock exam |
| [Whizlabs PL-300 bundle](https://www.whizlabs.com/microsoft-power-bi-certification-pl-300/) | Paid | Vendor total not publicly extractable; plan 8–20 hours selectively and verify April 2026 coverage before purchase |
| [MeasureUp PL-300 practice test](https://www.measureup.com/microsoft-practice-test-pl-300-microsoft-power-bi-data-analyst.html) | Paid | 158 questions; last updated February 2026; explicitly omits Direct Lake in its published objective list, so supplement April changes |
| [Udemy 2026 PL-300 practice tests](https://www.udemy.com/course/pl300-tests/) by HawkEye Data | Paid | 330 original questions / 6 tests; updated August 2026 and lists visual calculations |
| [Microsoft Power BI](https://www.youtube.com/@MicrosoftPowerBI) and [Guy in a Cube](https://www.youtube.com/@GuyInACube) | Public | 3–12 hours selectively for current features and weak areas; not exam checklists |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) / ESI PL-300 delivery | Partner-restricted | 3-day course pattern; verify the signed-in event's published start/end time |

Use practice assessments to locate weak objectives, then return to documentation and your own `.pbix`/service lab. Reject any source offering recalled live questions, “actual exam” files, or guaranteed pass material.

## Final readiness checklist

- I can select and configure a source, credential/privacy boundary, parameter, gateway, and Import/DirectQuery/Direct Lake mode from requirements.
- I can profile all relevant data, repair types/errors/nulls deliberately, preserve grain, reconcile merges, and configure staging/load behavior.
- I can build a star schema with correct keys, date roles, cardinality, filter direction, and an auditable bridge where necessary.
- I can predict DAX context and choose among Power Query, calculated columns/tables, measures, calculation groups, and visual calculations.
- I can diagnose model/measure/relationship/visual/source performance with measured evidence.
- I can design a meaningful, interactive, mobile-ready, accessible report and explain the limits of its analysis or AI-generated content.
- I can publish and distribute through workspaces/apps/items with correct gateway, refresh, endorsement, permissions, labels, and RLS.
- I can prove source reconciliation, totals, refresh, performance, and allowed/denied user behavior before release.
