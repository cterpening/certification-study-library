---
exam_code: PL-300
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-27
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-27
---

# PL-300 Microsoft Power BI Data Analyst Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The whole guide and all 78 April 20, 2026 objectives were reviewed against current public sources on September 27, 2026. Four worked examples, ten labs and 44 answered checks support practice. No Power BI engine or tenant lab was executed. See the [deep-review report](../docs/research/2026-09-27-pl-300-deep-review.md). It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#pl-300-coverage-record). The [official PL-300 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300) is authoritative.

**Current baseline:** Skills measured as of April 20, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 27, 2026. The fetched text reformats the audience profile and line wrapping; the objective content and weights are unchanged.<br>
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

### Living-guide watch — September 27, 2026

Microsoft's [AI at Work roadmap transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) changes where future business-application and AI capabilities are discovered. The [roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) contains estimated, mutable release information and is not a Power BI exam blueprint. Use it to notice changes that may affect labs, then confirm implemented Power BI behavior in Microsoft Learn and the tenant.

Independent Power BI books, courses, blogs, and videos in Places to learn remain useful for DAX and modeling explanations. Validate screenshots, licensing, Copilot features, and service limits; durable star-schema, filter-context, reconciliation, accessibility, and least-privilege reasoning should survive those changes.

The [latest published Power BI feature summary](https://learn.microsoft.com/en-us/power-bi/fundamentals/whats-new) observed in this review is August 2026. It includes Fluent 2 visual defaults/Theme pane GA and new refresh controls. It also announces that, starting in October, Desktop versions from March 2026 or earlier lose the old OneDrive/SharePoint save/share experience. Update and test that route; this notice is not retirement of local PBIX authoring.

**Q&A timeline correction:** Microsoft's [September retirement update](https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/power-bi-qa-retirement-reminder-february-2027-timeline-update/5365841) moves retirement to **February 2027**. The [current Q&A limitations](https://learn.microsoft.com/en-us/power-bi/natural-language/q-and-a-limitations) agree; the older [Q&A visual page](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-q-and-a) still says December 2026. Inventory old labs and reports, and test alternatives. Copilot requires supported paid capacity and has no announced direct replacement for embedded Q&A PaaS or sovereign-cloud availability. The April blueprint does not name Q&A configuration as a subobjective.

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

The April 2026 blueprint explicitly adds Direct Lake to this decision. Do not reduce the choice to “fast versus current.” Test model features, source load, user concurrency, security, licensing/capacity, refresh or framing behavior, and failure response. The [Direct Lake variants](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works) differ: Direct Lake on OneLake does not fall back to SQL DirectQuery. SQL-based Direct Lake can fall back under Automatic behavior; DirectLakeOnly instead returns an error when fallback is required. Framing establishes the source version visible to the model; separate source writes, model framing and report queries when checking freshness.

Data-source settings include location, authentication method, credentials, encryption, privacy levels, and sometimes gateway mapping. Privacy levels help prevent unintended combination across isolation boundaries; they are not a replacement for source authorization. Parameters make server/database/path/date/environment choices reusable. Do not put secrets in ordinary parameters.

For connectors affected by the [ODBC-to-ADBC transition](https://learn.microsoft.com/en-us/power-query/transition-to-adbc), compare effective implementation, data types, credentials, row totals and timings in Desktop and the service. Cloud tenant/workspace settings do not establish the driver used by a gateway. October default enablement and later embedded ODBC removals are planned transitions with separate rechecks, not evidence that every connection has already changed.

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

Define a deterministic survivor before removing duplicates: business key, latest change time and a tie-breaker such as source sequence. [Table.Distinct](https://learn.microsoft.com/en-us/powerquery-m/table-distinct) does not generally guarantee which duplicate survives when folding/optimization changes evaluation. A sorted, buffered input can make a deliberate pattern predictable, but [Table.Buffer](https://learn.microsoft.com/en-us/powerquery-m/table-buffer) consumes memory, is shallow, prevents downstream folding and can slow refresh. Compare a source-side deterministic solution with the local pattern; buffering is not a general speed fix.

> **Related item:** A reusable staging query does not guarantee one cached source read. Power Query evaluation and folding determine actual source work. Diagnose with folding indicators, query diagnostics, refresh history, and source logs.

---

## 2. Model the data

### Build a semantic model that explains itself

[Model data with Power BI](https://learn.microsoft.com/en-us/training/paths/model-power-bi/) starts from prepared data and develops relationships and DAX. Prefer a star schema: dimensions on the one side filter facts on the many side. Hide technical keys, assign useful formats/data categories/default summarization, and give tables, columns, and measures business-readable names and descriptions.

Relationship decisions require cardinality, active/inactive state, cross-filter direction, and referential integrity. Favor single-direction dimension-to-fact filters. Many-to-many relationships and bidirectional filters can be legitimate, but they make ambiguity, totals, performance, and RLS harder to reason about. Use a bridge table at an explicit grain for genuine many-to-many business relationships.

A role-playing dimension supplies multiple roles such as Order Date, Ship Date, and Due Date. Common patterns are one shared date table with one active relationship plus inactive relationships invoked by `USERELATIONSHIP`, or duplicated role-specific date dimensions when independent simultaneous filtering/usability warrants it. Create or import a contiguous common date table, mark it when required, and include the attributes needed for the organization's calendar.

[RLS propagates only through active relationships](https://learn.microsoft.com/en-us/power-bi/guidance/relationships-active-inactive); invoking an inactive relationship in a calculation does not turn on an RLS path through it. When both date roles need secured filtering, evaluate separate active role-playing dimensions. A correct Ship Date total alone is not a security test.

### Put each calculation in the right layer

[Power BI calculation options](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculations-options) differ in timing, storage, context, and reuse:

| Calculation | Language/timing | Best question to ask |
|---|---|---|
| Power Query custom column | M at refresh | Can this row-level transformation fold or be computed once before modeling? |
| Standard Import calculated column | DAX at model refresh and stored | Must the result act as a slicer, grouping, relationship key, or row attribute? |
| Calculated table | DAX at model refresh and stored | Must this derived table participate in model relationships/metadata? |
| Measure | DAX at query time | Must the answer respond to report filter context and be reusable? |
| Visual calculation | DAX over the visual result | Is the calculation local to this visual's axes/aggregated result? |

That column row describes the ordinary Import case. [Expression Context and storage mode](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculated-columns) also support user-context-aware columns evaluated at query time. Direct Lake on OneLake calculated columns are **preview**, use User Context, do not materialize and cannot be relationship keys. Direct Lake on SQL does not support that column feature. Treat the older blanket “all calculated columns are stored at refresh” explanation as incomplete; record mode and expression context before predicting performance or behavior.

Row context identifies a current row. Filter context is the set of filters applied by visuals, slicers, relationships, and DAX. `CALCULATE` evaluates an expression in modified filter context and can trigger context transition. Learn single aggregations, variables, iterators, basic statistics, and filter modifiers by predicting detail rows, subtotals, and grand totals before running them.

**Worked example — Replacing versus keeping a filter.** Assume a simple star model, an existing filter on `Product[Category] = "Hardware"`, Hardware sales of 100 and Software sales of 150, with no other filters. These illustrative measures have different contracts:

```dax
Software Sales = CALCULATE([Sales], Product[Category] = "Software")
Software Within Selection =
    CALCULATE([Sales], KEEPFILTERS(Product[Category] = "Software"))
```

With `[Sales]` defined as a sum, the first returns 150 because [CALCULATE](https://learn.microsoft.com/en-us/dax/calculate-function-dax) replaces the ordinary filter on that column. The second intersects Hardware and Software, yielding no rows and BLANK. Other-column filters remain; neither formula bypasses RLS. Define whether the business wants a fixed category or a category constrained by the user's selection before choosing the expression.

**Worked example — A total can be correct without adding the rows.** East serves customers `{A, B}` and West serves `{B, C}`. [DISTINCTCOUNT](https://learn.microsoft.com/en-us/dax/distinctcount-function-dax) gives two in each region and three overall, because B appears in both. Summing the region results gives four regional customer occurrences, a different question. Do not replace a correct distinct total with a visual sum just to make the numbers add. Also decide how BLANK customer keys should be treated; DISTINCTCOUNT includes BLANK.

Time intelligence depends on a trustworthy date table, appropriate relationships, and calendar semantics. A semi-additive measure aggregates normally across some dimensions but differently across time—for example, month-end inventory is often last-observation logic rather than a sum of daily balances. Quick measures can teach patterns and accelerate authoring, but read and test the generated DAX.

Calculation groups centralize transformations such as current/prior/variance across many measures. Define precedence and formatting when groups interact. They reduce repetition but can hide complexity if names and scope are unclear. [Visual calculations](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-visual-calculations-overview) operate on the visual matrix and are not reusable semantic-model measures; use them for visual-local running totals, moving averages, or comparisons, then test sort/axis/filter changes.

**Worked example — Previous visible year is not necessarily prior calendar year.** A visual shows 2024 sales of 80 and 2026 sales of 120 because 2025 is filtered out. Comparing 2026 with `PREVIOUS` on that visual axis gives 50% growth over the previous displayed value. It does not establish year-over-year growth from 2025. Choose calendar-aware model logic when that is the requirement, and test missing periods, hierarchy resets and visual ordering.

Visual calculations cannot use relationship-dependent functions such as `USERELATIONSHIP` or `RELATED`. Current limitations also exclude exporting their results, dashboard pinning and Publish to web; a configured alert is not triggered by changes in a visual-calculation value. Hidden fields still participate in the visual calculation and can appear in underlying-data exports. Check the delivery route before using a visual-local formula for a business obligation.

> **Related item:** A measure belongs to the reusable business semantic layer; a visual calculation belongs to one presentation. If another report, Excel, API, or Copilot consumer needs the same definition, prefer a governed measure.

### Optimize from evidence

Remove unnecessary rows/columns before loading, use efficient data types, reduce high-cardinality columns and grain when business requirements allow, preserve star-schema filter paths, and avoid broad bidirectional relationships. Do not remove needed detail or preaggregate away valid questions merely to shrink a model.

[Performance Analyzer](https://learn.microsoft.com/en-us/power-bi/create-reports/performance-analyzer) separates DAX query, DirectQuery/source, visual display, and other time. Copy or run a visual's DAX in [DAX query view](https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view), then inspect whether the issue is a visual, measure, relationship, source query, model cardinality, or concurrency problem. Establish a reproducible baseline, change one hypothesis, and compare the same filters and user/security context.

“Other” includes waiting/queued UI work, so a large value does not by itself identify slow DAX. Export the trace before clearing it. DAX query view's query-scoped `DEFINE MEASURE` lets you test a definition without automatically replacing the model measure; updating the model is a separate action. In the web, current guidance requires model Write permission and says query tabs are discarded on close. A Viewer with Build can instead use Desktop's live connection; Build does not grant model-edit permission.

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

[Automatic page refresh](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-automatic-page-refresh) re-queries supported sources; it does not reload an Import model. A short interval that works in Desktop can be overridden after publishing: shared capacity has a 30-minute minimum and no change detection, while dedicated-capacity settings govern allowed intervals. The documentation's mode matrix has broader entries than its DirectQuery-focused setup text; verify the actual mode, live connection and service configuration before promising a cadence.

Copilot can create narrative visuals, suggest or create report-page content, and summarize a semantic model/report. Its quality depends on clear model names/descriptions, curated measures, relationships, data quality, and verified business definitions. Treat generated DAX, visuals, and prose as drafts; validate totals, filters, claims, and sensitive-data exposure. The [current requirements](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction) include supported paid Fabric F2+ or Power BI Premium P1+ capacity, region and admin settings; a Pro/PPU license alone and trial capacity are insufficient. The report pane is GA, while standalone and app agents remain preview. Verify the selected surface's permissions and capacity route.

In [Copilot report summaries](https://learn.microsoft.com/en-us/power-bi/explore-reports/copilot-pane-summarize-content), eligible display-only bookmarks can expose hidden visuals to summarization while RLS/OLS remains enforced. The bookmark must have Data cleared and be reachable by a report button or navigator; personal bookmarks are excluded. Hiding a visual is not access control. Follow citations and verify filter scope instead of assuming that a summary uses only the visible canvas.

### Usability, storytelling, and accessibility

Bookmarks capture a configured report state and can power navigation/story views; decide whether data, display, current page, and selected visuals belong in the bookmark. Tooltips add context without crowding. Edit interactions so cross-filter/highlight/none behavior matches the question. Use buttons, page navigation, bookmark navigators, and drillthrough deliberately, and provide a visible return route.

Sync slicers only where a shared selection improves comprehension; hidden synced slicers can confuse users. Use the Selection pane to name, group, show/hide, and layer objects. Configure exports from the organization's data-loss requirements, not user convenience alone. Personalize visuals allows consumers to change supported fields/visuals within their permissions. Hiding a field or visual is a presentation choice, not a security boundary; enforce sensitive columns/rows through the model and source controls.

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

Traditional [dashboard data alerts](https://learn.microsoft.com/en-us/power-bi/create-reports/service-set-data-alerts) apply to supported numeric card, KPI and gauge tiles, evaluate refreshed data and are personal to the creator. Sharing a dashboard does not share its alert rules. Report/Activator alerts are a separate path with different prerequisites. Test the exact threshold, refresh event and recipient route.

### Gateways and refresh

A gateway is required when the Power BI service cannot directly reach a source—for example, many on-premises or private-network sources. Configure the appropriate gateway/data-source mapping, authentication/credentials, privacy boundary, cluster availability, ownership, and monitoring. Personal and standard/enterprise gateway choices have different collaboration and administration implications.

Scheduled refresh updates imported semantic-model data; it does not make DirectQuery or Direct Lake identical to Import. Validate source availability, credential expiration, gateway status, timeout/resource limits, refresh history, and the report's displayed freshness. Coordinate schedule with source load and dependent transformations.

[Scheduled refresh](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh) currently allows up to eight scheduled runs/day for Pro and 48 for PPU or supported capacity. The selected time is a target, not an exact completion promise. Four consecutive failures disable the schedule; an unrecoverable credential/configuration error can disable it sooner. Two months without report/dashboard use can pause it. Repair the cause, check history and re-enable the schedule where required.

[Refresh types and controls](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data) distinguish source-data refresh from OneDrive/SharePoint file synchronization and visual refresh. OneDrive sync alone does not query the original database. Current schema-only, data-only and combined refresh options, including table-level actions, have different effects: syncing a new column is not proof of fresh rows, and data-only refresh intentionally preserves the model schema. Recheck privacy settings and credentials in service/gateway connections after publishing.

> **Related item:** Incremental refresh partitions a date-filtered table so recent periods refresh while history is retained under policy. It can reduce refresh cost, but it requires suitable date filtering/folding and an initial-load/partition strategy; it is adjacent operational depth rather than a named April 2026 subobjective.

### Roles, item permissions, semantic-model access, and RLS

Workspace Admin, Member, Contributor, and Viewer roles grant progressively different management/edit/consumption capabilities. Use groups, least privilege, and separation of duties. Item-level access can expose one artifact without broad workspace membership. Semantic-model permissions such as Read, Build, Reshare, and Write govern distinct actions; Build enables new content/analysis against the model and deserves explicit approval.

Define static RLS roles with fixed filters or dynamic RLS using identity-to-security-table mappings, then assign users or supported groups in the service. Test in Desktop and as a real restricted identity after publishing. Workspace users with edit capability are not ordinary RLS consumers; use Viewer/app consumption paths when RLS must apply and recheck current behavior. RLS filters rows, not columns or objects, and does not secure an independently accessible source.

**Worked example — Two RLS roles broaden access.** An East role permits East and a West role permits West. A user in both sees their union, not an intersection or whichever role was assigned last. Adding a restrictive role does not subtract an existing grant. A Viewer with Build still receives RLS filtering; granting Contributor instead bypasses ordinary consumer RLS. Validate effective workspace and model permissions together.

The [RLS guidance](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls) permits supported security/distribution groups but excludes Microsoft 365 groups. Test as role does not fully simulate B2B/embedded identity, Copilot, or DirectQuery with SSO. Test actual restricted consumers and the real identity path, especially guest UPN mappings. Importing data also requires model-side controls; source filters at extraction are not automatically per-viewer RLS.

[Sensitivity labels](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-sensitivity-label-overview) classify content and can protect supported exported Excel, PDF and PowerPoint files according to policy. CSV and other unsupported export routes do not receive that label/protection. A label does not replace workspace/model permissions or RLS. Validate both the exported file and the actual recipient's ability to open it; test each enabled route separately.

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

### Lab 9 — Predict calculations before running them

Build a tiny synthetic model for the four worked examples. Compare replacement/intersection filters, distinct totals, missing-year visual comparisons and multiple-role membership. Test detail, subtotal and grand total; change sorting and filtering; compare a model measure with a visual calculation. **Evidence:** prediction table, actual results, expression/mode/axis context and explanation of every difference. The DAX examples above are illustrative and were not run against a Power BI engine during this review.

### Lab 10 — Prove the delivery and refresh contract

Use an appropriate test workspace to compare a visual, export, dashboard alert and app consumer. Check label behavior on supported files versus CSV, a real restricted identity, the scheduled-refresh failure route and schema-only versus data-only actions. Where available, test Copilot's hidden-bookmark scope and compare the SQLBI article's measure/visual performance pattern on your own data. **Evidence:** access/export matrix, source/model/visual freshness times, traces and limits. Mark unavailable licensed features as unexecuted rather than assuming their behavior.

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
21. **Measure versus ordinary Import calculated column?** Reusable query-time result versus stored row-level refresh result; other storage modes and user-context columns can evaluate at query time.
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

37. **Why can CALCULATE ignore the selected category?** An ordinary same-column filter replaces the selection; KEEPFILTERS intersects it. Neither removes RLS.
38. **Why can region distinct counts total differently?** A customer may belong to both regions; the overall context counts that customer once.
39. **Does PREVIOUS mean previous calendar year?** It refers to the visual axis; missing/filtered years can change the comparison.
40. **Are all calculated columns stored at refresh?** No; storage mode and Expression Context matter. Direct Lake on OneLake columns are query-time preview and cannot be relationship keys.
41. **Can a new narrow RLS role cancel a broad role?** No; roles are additive. Check groups and edit permissions as well.
42. **Does a hidden visual protect its data from Copilot?** No; supported display-only bookmarks can be read while model security remains enforced.
43. **Do CSV exports inherit sensitivity-label protection?** No; use a supported route and test the resulting file and recipient permissions.
44. **Can you replace Q&A simply by owning Pro?** No; retirement is now announced for February 2027, and Copilot requires supported capacity, settings and an available experience.

---

## Places to learn

This is a curated starting point, **not a complete list**, and it is not meant to be consumed in full. Choose one primary course or path, build an end-to-end report, and add only resources that close measured gaps. Reconcile every resource with the April 20, 2026 blueprint, especially Direct Lake, calculation groups, DAX query view, Copilot, visual calculations, current usability controls, and workspace/asset changes.

The five official paths retain their **September 1 duration estimates**; September 27 module listings did not independently reverify the total. They are [data-analytics foundations](https://learn.microsoft.com/en-us/training/paths/data-analytics-microsoft/) (1h28), [prepare data](https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/) (4h33), [model data](https://learn.microsoft.com/en-us/training/paths/model-power-bi/) (5h50), [effective reports](https://learn.microsoft.com/en-us/training/paths/power-bi-effective/) (5h07), and [manage and secure](https://learn.microsoft.com/en-us/training/paths/manage-secure-power-bi/) (2h54), totaling **19 hours 52 minutes**.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official PL-300 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/) | Public | 1–2 hours initially; 15 minutes per recheck |
| Five official paths from [PL-300T00](https://learn.microsoft.com/en-us/training/courses/pl-300t00) | Public | 19h52 historical estimate; allow 35–60 hours with exercises and notes |
| PL-300T00 instructor-led course | Paid/partner delivery | 3 days listed |
| [Official MicrosoftLearning PL-300 labs](https://github.com/MicrosoftLearning/PL-300-Microsoft-Power-BI-Data-Analyst) (MIT) | Public | 15–25 hours estimated; repeat without step-by-step help |
| [Microsoft PL-300 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/practice/assessment?assessment-type=practice&assessmentId=48&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Microsoft Reactor PL-300 orientation](https://www.youtube.com/watch?v=tDwNtxAB49k) | Public | 1 hour listed; June 2026 overview, not a complete course |
| [Pluralsight PL-300 path](https://www.pluralsight.com/paths/microsoft-certified-microsoft-power-bi-data-analyst-pl-300) | Paid | 12 hours, 4 courses, 4 labs, and practice exam listed; courses Sep 2025–Jan 2026, labs Jul 2026 |
| [O'Reilly PL-300 Study Guide](https://www.oreilly.com/library/view/microsoft-power-bi/9781098175276/) by Paul Turley | Paid | Earlier listing: 12h07 / 478 pages, March 2026, based on 2025 revisions; access blocked on recheck |
| [Udemy PL-300 exam-prep course](https://www.udemy.com/course/pl-300-da-100-microsoft-power-bi-data-analyst-exam-prep/) by Nikolai Schuler | Paid | Earlier listing: 8h57 / 120 lectures and August 2026 update; access blocked on recheck |
| [Coursera Microsoft PL-300 Exam Preparation and Practice](https://www.coursera.org/learn/microsoft-pl-300-exam-preparation-and-practice/) | Paid/subscription; audit terms vary | About 40 hours in the current overview; five module estimates total 37 hours |
| [Whizlabs PL-300 bundle](https://www.whizlabs.com/microsoft-power-bi-certification-pl-300/) | Paid | Vendor total not publicly extractable; plan 8–20 hours selectively and verify April 2026 coverage before purchase |
| [MeasureUp PL-300 practice test](https://www.measureup.com/microsoft-practice-test-pl-300-microsoft-power-bi-data-analyst.html) | Paid | 158 questions; last updated February 2026; explicitly omits Direct Lake in its published objective list, so supplement April changes |
| [Udemy 2026 PL-300 practice tests](https://www.udemy.com/course/pl300-tests/) by HawkEye Data | Paid | Earlier vendor listing: 330 questions / 6 tests, August 2026 update; access blocked on recheck |
| [Microsoft Power BI](https://www.youtube.com/@MicrosoftPowerBI) and [Guy in a Cube](https://www.youtube.com/@GuyInACube) | Public | 3–12 hours selectively for current features and weak areas; not exam checklists |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) / ESI PL-300 delivery | Partner-restricted | 3-day course pattern; verify the signed-in event's published start/end time |

Use practice assessments to locate weak objectives, then return to documentation and your own `.pbix`/service lab. Reject any source offering recalled live questions, “actual exam” files, or guaranteed pass material.

### Blog reading with a purpose

[Marco Russo and Alberto Ferrari — Analyzing the performance impact of visual calculations](https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/), SQLBI, July 27, 2026. Allow 20–30 minutes plus Lab 10. The authors show why smaller visual result sets can benefit while large combinations of categories can create expensive intermediate rows. Compare equivalent measures and visual calculations at two visual grains, retaining filters, totals and traces. Their timings are experiments on their models, not promised gains for yours. The public article was reviewed; its downloads, paid material, screenshots and benchmarks were not independently executed.

The attributed Microsoft Q&A timeline update above is operational reading for migration planning. Both readings supplement the blueprint; neither is an exam question source.

## Final readiness checklist

- I can select and configure a source, credential/privacy boundary, parameter, gateway, and Import/DirectQuery/Direct Lake mode from requirements.
- I can profile all relevant data, repair types/errors/nulls deliberately, preserve grain, reconcile merges, and configure staging/load behavior.
- I can build a star schema with correct keys, date roles, cardinality, filter direction, and an auditable bridge where necessary.
- I can predict DAX context and choose among Power Query, calculated columns/tables, measures, calculation groups, and visual calculations.
- I can diagnose model/measure/relationship/visual/source performance with measured evidence.
- I can design a meaningful, interactive, mobile-ready, accessible report and explain the limits of its analysis or AI-generated content.
- I can publish and distribute through workspaces/apps/items with correct gateway, refresh, endorsement, permissions, labels, and RLS.
- I can prove source reconciliation, totals, refresh, performance, and allowed/denied user behavior before release.
