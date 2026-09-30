---
exam_code: SPLUNK-CORE-USER
vendor_id: splunk
official_blueprint: https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/splunk-test-blueprint-user.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-30
---

# Splunk Core Certified User Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 30, 2026 best-effort review read the complete indexed credential page and three-page blueprint, mapped all 40 objectives, and checked selected public documentation. Direct retrieval and the objective monitor encountered DNS errors; the historical objective snapshot is retained. The [official certification page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-user.html) and [test blueprint](https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/splunk-test-blueprint-user.pdf) are authoritative. Source-reading limits and unexecuted labs are explicit below; these original explanations and checks are not exam items.

**Current baseline:** Splunk Basics (5%); Basic Searching (22%); Using Fields in Searches (20%); Search Language Fundamentals (15%); Using Basic Transforming Commands (15%); Creating Reports and Dashboards (12%); Creating and Using Lookups (6%); Creating Scheduled Reports and Alerts (5%). The blueprint says related topics may appear and may change without notice.<br>
**Exam contract:** entry-level; 60 multiple-choice questions; 60 total minutes including three minutes for the exam agreement; USD 130 per attempt; Pearson VUE delivery<br>
**Prerequisite contract:** none. This is an optional entry point intended for candidates with little or no Splunk experience.<br>
**Credential lifecycle — VERIFY CURRENT:** The [candidate handbook](https://www.splunk.com/en_us/pdfs/training/splunk-certification-candidate-handbook.pdf), selected retake and renewal sections, describes a three-year cycle and requires a qualifying renewal retake in the final year. A previously passed exam cannot simply be retaken outside approved recertification. Confirm your own expiration and eligible path before booking; this review did not inspect an account or all handbook sections.<br>
**Upcoming change:** No retirement, replacement or new Core User blueprint was found in the credential page and blueprint read on September 30. This is a bounded source check, not proof that no announcement exists elsewhere. Practice classic SPL: the blueprint's objective 4.4 literally says “tables,” while the command is `table`; preserve that source wording when comparing snapshots. SPL2 is a separate syntax contract.<br>

## How to use this guide

Use a Splunk-provided lab, a trial, or an employer-approved nonproduction environment with synthetic or approved data. Do not upload production secrets or personal data to an unmanaged system. Complete a single data story end to end: find the right events, constrain time/index, use fields, transform results, enrich them, save a report, display it, schedule it, and create a carefully scoped alert.

For every search:

1. state the question and relevant time window;
2. name the smallest likely index/source/sourcetype and selective terms;
3. predict whether the next command filters events, changes fields, or transforms rows;
4. run it and compare Events, Statistics, Visualizations, fields, timeline, and job evidence;
5. save/share only after checking permissions, time semantics, and sensitive data.

The user exam evaluates using an existing Splunk environment. Installation, distributed architecture, parsing configuration, and index administration are useful context but belong primarily to administrator/architect tracks.

> **About related items:** A `Related item:` callout adds architecture, governance, performance, security, or adjacent product context. It makes the objective more useful in practice but does not imply that the extra phrase appears verbatim in the public blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Splunk Basics | 5% | Component/use/app map, correct app navigation, and deliberate personal settings |
| Basic Searching | 22% | Time-bounded retrieval, event/timeline interpretation, iterative refinement, and controlled job/result handling |
| Using Fields in Searches | 20% | Field-aware filtering and sidebar evidence with missing/multivalue boundaries |
| Search Language Fundamentals | 15% | Explainable command pipeline using index, table, rename, fields, dedup, and sort |
| Using Basic Transforming Commands | 15% | Correct top/rare/stats tables and aggregation interpretation |
| Creating Reports and Dashboards | 12% | Reusable report plus a purposeful dashboard panel/visualization |
| Creating and Using Lookups | 6% | Governed CSV definition, explicit and automatic enrichment, and unmatched-row validation |
| Creating Scheduled Reports and Alerts | 5% | Time-correct schedule/alert with permissions, trigger, action, and fired-instance evidence |

## 1. Splunk basics — 5%

### Components and common uses

At user level, understand the flow without administering it. Forwarders and other inputs collect/send machine data. Indexers process and store searchable data and participate in retrieval. Search heads coordinate searches and present results; in a small single-instance deployment these roles can coexist. Splunk Web provides the browser interface, while Splunk Cloud Platform manages more infrastructure for the customer than self-managed Splunk Enterprise.

Splunk commonly supports IT operations, security, observability, application troubleshooting, business/service analysis, audit investigation, and capacity insight. The value comes from searchable time-stamped evidence and reusable knowledge—not from assuming every source is complete or correct.

### Apps, user settings, and navigation

A Splunk app packages a user experience and related knowledge/configuration: searches, reports, dashboards, lookups, field extractions, workflows, and navigation. An app is also a namespace/context for knowledge objects and permissions; changing the current app can change what is visible and how an object is resolved.

Know Splunk Home, app selection, Search & Reporting, Settings access allowed by your role, and the Search view: search bar, time picker, mode, job controls/status, results counts, fields sidebar, timeline, and Events/Patterns/Statistics/Visualizations tabs. The exact UI varies by product version and permission.

Personal preferences can include time zone and display/search behavior. Time zone changes how timestamps are presented and interpreted; it does not rewrite the stored event. Do not “fix” confusing time evidence by changing preferences without recording the context.

The current [About the Search app](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.4/use-the-search-app/about-the-search-app) page is the live UI reference.

> **Related item:** Role capabilities and knowledge-object permissions control what a user can see, edit, schedule, and share. A missing menu is often a permission, product, or app-context difference—not proof that the platform lacks the feature.

## 2. Basic searching — 22%

### Retrieve and refine events

A basic SPL search begins with retrieval terms and can continue through pipe-delimited commands. Use explicit index, sourcetype, source, host, field-value constraints, quoted phrases, Boolean operators, and wildcards deliberately. Boolean keywords are conventionally uppercase. Parentheses make logic clear. Avoid leading broad wildcards and all-time searches unless the learning task specifically requires them.

```spl
index=web sourcetype=access_combined status>=500
| table _time host clientip method uri_path status
| sort - _time
```

The time picker is a primary constraint. Relative windows such as last 15 minutes move with execution time; absolute windows identify fixed instants. `_time` is the event timestamp Splunk uses for time-based retrieval, while `_indextime` describes indexing time and answers a different question. Check time zone and boundary inclusivity when reproducing evidence.

Refine from selective indexed terms toward later commands. Add or remove one condition and observe event count. Use field/value clicks or the search bar, but always understand the generated SPL. A search that returns zero can mean no matching activity, the wrong time/index/permissions, field extraction differences, or missing/delayed data.

### Interpret results, timeline, and events

Raw events include `_time`, source metadata, extracted fields, and raw text (`_raw`). The Events tab shows event-oriented output; transforming commands usually move primary results to Statistics. Visualizations require an appropriate table shape.

The timeline groups event counts over time. Zooming/selecting a region changes the time constraint and can reveal bursts, gaps, or seasonality, but a bucket represents a range and visual shape depends on scale. Expand an event to inspect fields; selected/interesting fields reflect extraction and UI heuristics, not a schema guarantee.

### Control jobs and preserve results

A running search is a job with lifecycle, time range, progress, result count, and artifacts. Depending on product/version/permissions, controls can pause, stop/finalize, inspect, share, or rerun it. Pausing temporarily stops execution; finalizing ends it while preserving available results. A completed result can still be partial if the search hit limits or source data was incomplete.

Saving search results (for example export) preserves a point-in-time result; saving the search as a report preserves reusable search logic and presentation settings. Exports can contain sensitive raw fields and are detached from later source corrections. Apply minimum necessary fields, access controls, approved location, and retention.

Splunk's current [Search Tutorial](https://help.splunk.com/en/splunk-enterprise/search/search-tutorial/10.0/introduction/about-the-search-tutorial) provides a safe, connected workflow across these objectives.

## 3. Using fields in searches — 20%

A field is a named value associated with an event. Default metadata fields and search-time extractions may be present; not every event has every field, and a field can be multivalued. `field=value` requires an event with a matching extracted value. Quoting is needed for values with spaces/special meaning.

Use fields early enough to make searches precise, but distinguish retrieval/filtering from display. The `fields` command retains or removes fields; it does not rename them. `table` creates a tabular result with selected columns and is generally placed late because it is transforming and drops other fields from the result.

The fields sidebar summarizes fields found in current results. Selecting a field shows common values/counts and can add terms. Those counts describe the current result set/sample and time window, not universal data quality. Validate missing values, case/format differences, multivalue content, and whether an automatic extraction/lookup produced the field.

```spl
index=web sourcetype=access_combined earliest=-24h
| fields _time host status uri_path
```

> **Related item:** `host`, `source`, and `sourcetype` are core metadata with different meanings: event origin, input source, and data-format classification. Misclassified sourcetypes often lead to missing or incorrect field extractions.

## 4. Search language fundamentals — 15%

### Pipeline model and index scope

Pipes pass the result of the command on the left to the command on the right. Retrieval finds events; streaming/filtering commands operate on events; transforming commands create result tables. Once a transforming command aggregates raw events, later commands see the transformed rows, not the original event set.

Specify the permitted, relevant index rather than relying on role defaults. Narrow time and selective indexed metadata before expensive processing. Put display-only commands late. Use readable indentation for long searches and document intent outside fragile inline tricks.

### Required commands

- `table field1 field2` emits a table with fields in the requested order and drops other fields.
- `rename old AS new` changes a result field's display/name for downstream commands; quote names with spaces as required.
- `fields field1 field2` keeps fields; `fields - field3` removes fields.
- `dedup key` retains representative events by field value according to current result order/options. It is not a universal data-cleaning operation.
- `sort field` sorts ascending and `sort - field` descending. Default result limits/options and numeric/string interpretation matter; check the command reference for production searches.

```spl
index=web status>=400 earliest=-1h
| sort 0 - _time
| dedup clientip
| rename clientip AS client
| table _time client status uri_path
```

Search order changes meaning: sorting before `dedup` deliberately chooses which representative survives. The [SPL Search Reference](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/introduction/welcome-to-the-search-reference) is authoritative for command syntax and limitations.

Here the intended representative is the latest error event per populated client IP. A final sort alone cannot repair an earlier selection. Tied timestamps need an agreed secondary key if reproducibility matters. This is a source-checked example, not an executed Splunk search.

The [SPL sort reference, version 10.2](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sort) documents a default cap of 10,000 results. `sort 0` removes that cap but can increase resource use; use it only on a deliberately bounded lab search. The [SPL dedup reference, Cloud 10.4.2604](https://help.splunk.com/en/splunk-cloud-platform/spl-search-reference/10.4.2604/search-commands/dedup) documents that missing key fields are dropped by default. `keepempty=true` retains every event with a missing key; it does not collapse all missing clients into one representative. These are the specific document versions checked, not a requirement to upgrade your lab.

### Predict the result before running it

This original worksheet uses three events with distinct timestamps. The middle row has no `clientip` field, represented by an em dash here. Assume all three are within the same permitted search window and all have an error status.

| Event | `_time` order | `clientip` | `status` |
|---|---:|---|---:|
| A | 1 (oldest) | 192.0.2.10 | 500 |
| B | 2 | — | 503 |
| C | 3 (newest) | 192.0.2.10 | 404 |

For descending time followed by `dedup clientip`, the predicted survivor is C. Adding `keepempty=true` predicts C and B. Sorting ascending before dedup predicts A; sorting that output descending afterwards still cannot restore C. Deduplicating by client answers a representative-event question, not “how many errors occurred?” The original event count remains three. These are paper predictions from the documented contracts; no SPL engine result is claimed.

## 5. Basic transforming commands — 15%

`top field` reports the most common values with count and percentage by default. `rare field` reports least common values. Both can group with `by`, limit output, and control whether count/percent fields appear. Rare values are not automatically errors, and common values are not automatically normal; interpret them against source completeness and the question.

`stats` calculates aggregations across results. Without `by`, it produces one aggregate row; with `by`, it groups by distinct field combinations. Common functions include `count`, `dc`, `sum`, `avg`, `min`, `max`, `earliest`, `latest`, `values`, and `list`. `count` and `count(field)` answer different questions when the field is missing.

```spl
index=web earliest=-24h
| stats count AS requests dc(clientip) AS clients avg(bytes) AS avg_bytes by status
| sort - requests
```

An aggregate destroys event-level detail from the pipeline. Preserve/drill back to a raw-event search when investigation requires evidence. Give calculated columns clear names and verify units. In the worksheet above, a count of events is three, while a count of populated client values is two. A single client representative cannot answer either count without returning to the original events. This arithmetic is a prediction, not a recorded Splunk execution.

> **Related item:** A percentage is only as representative as its denominator. Time window, source coverage, late data, permissions, and deduplication can all change the apparent top/rare distribution.

## 6. Reports and dashboards — 12%

A report is a saved search (or pivot) that can be rerun, shared, scheduled, accelerated where appropriate, visualized, or used by dashboards. Save a stable title, description, app context, time behavior, display/table format, and the minimum permissions needed. Edit by reopening its search/report definition, testing the change, and considering downstream dashboards/alerts.

A statistical table needs meaningful columns and units. A chart needs an appropriate result shape and should match the question: time chart for trends, bars for category comparison, single value for one carefully contextualized KPI. Avoid misleading truncated axes, excessive categories, and decoration that obscures values.

A dashboard groups panels for a particular audience/decision. A report can power a panel; inline searches can also power panels. Know how to create, add, and edit panels in your available dashboard framework. Dashboard Studio and Classic dashboards differ, and migrating layout formats can be destructive—verify framework/version before editing.

Current references: [Create and edit reports](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/reporting-manual/10.4/report-management/create-and-edit-reports) and [Create a Dashboard Studio dashboard](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/dashboard-studio/10.4/create-a-dashboard-in-dashboard-studio).

## 7. Lookups — 6%

A lookup enriches events by matching one or more input fields to reference data and returning fields. A CSV lookup workflow has two distinct objects: uploaded lookup table file and lookup definition. Permissions/app context govern use.

```spl
index=web earliest=-1h
| lookup asset_reference ip AS clientip OUTPUTNEW owner criticality
| table _time clientip owner criticality status
```

`OUTPUTNEW` avoids overwriting an existing output field; `OUTPUT` can overwrite it. Field names on each side can be mapped with `AS`. Test matched, unmatched, duplicate, blank, case, and stale entries. Treat lookup content as governed data; enrichment is not proof that the reference is current.

An automatic lookup applies at search time to matching host/source/sourcetype data without an explicit `lookup` command. It improves consistency but can add hidden fields/cost and create collision/reference-cycle problems. Know how to define it in Splunk Web for the credential; file-based `props.conf`/`transforms.conf` implementation is deeper admin context. See [Define a CSV lookup in Splunk Web](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4/use-lookups-in-splunk-web/define-a-csv-lookup-in-splunk-web).

## 8. Scheduled reports and alerts — 5%

A scheduled report runs a saved search on a cadence and can retain or deliver results. Define schedule, time window, owner/app, permissions, and actions so the search covers intended data without gaps or accidental overlap. “Run every hour” and “search the previous hour” are related but separate decisions; ingestion delay may require a deliberate lag/window.

An alert evaluates scheduled or real-time search results against a trigger condition and performs configured actions. Use scheduled alerts unless a real-time requirement and capacity justify otherwise. Define trigger threshold, per-result versus number-of-results behavior, throttling/suppression, severity, recipients/action, and recovery/ownership. Test with safe data.

A fired alert is an instance/history record, not merely the alert definition. Inspect its scheduled time, searched interval, result count, trigger reason, actions, and failures. A notification proves an action ran, not that a human resolved the condition.

> **Related item:** Alerts are operational commitments. Every alert needs an owner, useful message/context, response path, review cadence, and retirement rule; otherwise technically correct searches become noise.

## Integrated scenarios

### Scenario 1: Web-service reliability view

Search one web index for the last 24 hours, inspect the timeline, filter status/host fields, find top and rare codes, and use `stats` by host. Save a report with a chart and add it to a dashboard. Verify that clicking/drilling to raw events preserves the same time/field constraints.

### Scenario 2: Asset enrichment

Create a small approved CSV mapping client IP to owner and criticality. Upload it, define it, invoke it with `lookup`, configure an automatic form in a lab, and test matched/unmatched/duplicate rows. Limit the final table to necessary fields and record ownership/update cadence.

### Scenario 3: Scheduled error alert

Turn an error report into a schedule and a test alert. Deliberately model schedule time, search window, ingestion delay, threshold, throttle, recipient, and safe action. Trigger it with synthetic data and inspect the fired-alert record.

## Hands-on labs

1. **Interface and component tour:** label component roles, app context, settings, navigation, search controls, result tabs, fields, timeline, and permission-dependent differences.
2. **Search refinement workbook:** start broad in a bounded lab window, then add index, sourcetype, host, phrases, Boolean logic, wildcards, and fields one change at a time; explain every count change.
3. **Time and event lab:** compare relative/absolute windows, timeline zoom, `_time`, `_indextime`, time zone display, missing periods, late events, and expanded event fields.
4. **Job/result controls:** run a long safe search, inspect/pause/finalize it, distinguish partial/completed results, then export minimum fields and save the logic as a report.
5. **Pipeline command matrix:** use table, rename, fields, dedup, and sort in different orders; record schema, row count, representative selection, and performance consequences.
6. **Transforming workbook:** use top, rare, and at least eight stats functions with and without `by`; cover missing fields, empty results, units, and misleading denominators.
7. **Report/dashboard build:** create/edit statistical and chart reports, add one to a purposeful dashboard, set minimal permissions, and verify time behavior and underlying events.
8. **Lookup/schedule/alert build:** create the CSV definition and automatic/explicit enrichments, schedule a report, create a throttled alert, trigger it synthetically, and inspect history/action evidence.

## Lab evidence and next-pass fixes

**September 30 execution status: none of the eight proposed Splunk labs was executed in this review.** No Splunk executable or approved endpoint was available. Source review and the worksheet predictions do not validate indexing, SPL parsing, extraction, time-zone behavior, dashboard permissions, scheduling or alert delivery.

| Work to reproduce | Evidence still needed | Useful contribution |
|---|---|---|
| Labs 1–4: navigation, searching, time and jobs | Product/build, app/role, safe fixture, exact time range, result/job observations | Record missing menus, errors and any version-specific correction |
| Labs 5–6: command pipelines and transformations | Exact SPL, input rows, observed output, missing/multivalue and sort-limit cases | Compare actual output with a written prediction; include failures |
| Lab 7: reports and dashboards | Framework, saved report/panel, time behavior and tested access | Describe the smallest working reproduction and permissions |
| Lab 8: lookup, schedule and alert | Definition/file, matched/unmatched rows, schedule window, fired-instance and action evidence | Distinguish a configured object from a successful run or delivery |

**More research needed — next pass:** refresh the unavailable 10.4 UI/reporting/lookup pages, confirm current training access and the unverified commercial book listing, rerun the objective monitor, and execute the eight labs in an approved environment. The [Search Tutorial introduction](https://help.splunk.com/en/splunk-enterprise/search/search-tutorial/10.0/introduction/about-the-search-tutorial) explains its separate tutorial dataset and sequential parts; linked lessons were not completed here. Keep error text, expected versus observed results and product version with community fixes. Independent human content review remains pending.

## Original readiness checks

1. What roles do forwarder, indexer, and search head perform?
2. What does a Splunk app commonly package?
3. Why can app context change object visibility?
4. Which user setting commonly changes timestamp presentation?
5. What are the principal elements of the Search view?
6. Why should a search begin with a deliberate time range?
7. What is the difference between `_time` and `_indextime`?
8. Name four reasons a valid search might return zero events.
9. What does the timeline summarize?
10. When do Statistics results normally appear?
11. How do pausing and finalizing a job differ?
12. How does exporting results differ from saving a report?
13. What can a raw event contain besides `_raw`?
14. Why can a field be absent from some matching events?
15. What does the fields sidebar summarize?
16. How do `fields` and `table` differ?
17. What does a pipe do in SPL?
18. Why should an index be named explicitly where possible?
19. What happens to raw-event detail after aggregation?
20. What does `rename` affect for downstream commands?
21. Why does command order matter for `sort` and `dedup`?
22. What is the risk of using `dedup` as generic data cleaning?
23. What do top and rare return by default conceptually?
24. Why is a rare value not automatically suspicious?
25. How do `stats count` and `stats count(field)` differ?
26. What does a `by` clause do in stats?
27. What should a report definition preserve?
28. How should a visualization be selected?
29. What is the purpose of a dashboard?
30. How can a report relate to a dashboard panel?
31. What are the two required UI objects in a basic CSV lookup setup?
32. How do OUTPUT and OUTPUTNEW differ?
33. What does an automatic lookup do?
34. Which lookup boundary rows should be tested?
35. How do schedule cadence and report search window differ?
36. Why might a scheduled search deliberately lag behind wall-clock time?
37. What does an alert trigger condition evaluate?
38. What evidence appears in a fired-alert instance?
39. What is the published prerequisite requirement?
40. What should be rechecked before purchase?

## Answer key

1. Collection/forwarding, processing/storage/retrieval, and search coordination/presentation.
2. Navigation plus knowledge/configuration such as searches, reports, dashboards, lookups, and fields.
3. Knowledge objects and permissions are scoped/resolved by app and sharing context.
4. Time zone.
5. Search bar, time picker/mode, controls/status, counts, fields, timeline, and result tabs.
6. Time is a core retrieval constraint and controls relevance, cost, and reproducibility.
7. Event time used for time search versus the time Splunk indexed the event.
8. Wrong time/index/permission, missing/delayed data, wrong value, or extraction mismatch; any four.
9. Event counts in time buckets for the current search.
10. After a transforming/table-producing search.
11. Pause can resume; finalize ends the job and preserves available results.
12. Export captures current rows; a report saves reusable search logic and presentation/time configuration.
13. Time/source metadata and extracted fields.
14. Sources/formats/extractions vary and some events do not carry the value.
15. Fields/values found in the current result set or sample.
16. Fields retains/removes fields; table produces an ordered table and discards others.
17. Passes the left command's results into the next command.
18. It narrows work and avoids relying on role defaults.
19. Later commands see aggregate rows rather than original events.
20. The field name visible to later commands/output, not source data at rest.
21. Dedup retains representatives from its input order. For the worksheet, descending time first keeps C; ascending first keeps A. Sorting afterwards only reorders surviving rows.
22. It can silently discard distinct evidence sharing a selected key. Missing keys are dropped by default; retaining them needs a deliberate option. A representative is not an event count.
23. Most and least frequent values with counts/percentages.
24. Legitimate categories can be uncommon; context and source completeness determine meaning.
25. The first counts rows; the second counts rows where that field has a value. The worksheet predicts three events versus two populated client values, before deduplication.
26. Creates one aggregate group per distinct listed field combination.
27. Search, time behavior, title/description, app/owner/permissions, and display settings as needed.
28. From the question and result shape, with honest scales/labels.
29. Group panels for a defined audience and decision/workflow.
30. The saved report can power the panel.
31. Lookup table file and lookup definition.
32. OUTPUT may overwrite; OUTPUTNEW adds only where the destination is absent.
33. Enriches matching events at search time without an explicit lookup command.
34. Matched, unmatched, duplicate, blank, case/format, and stale-reference rows.
35. One controls execution frequency; the other controls which event interval each execution searches. An hourly run with a 15-minute window leaves a 45-minute gap between windows; a two-hour window overlaps the preceding run by one hour. Neither choice guarantees complete data arrival.
36. To allow expected ingestion delay while keeping intentional coverage.
37. The alert search result/result count against configured criteria.
38. Scheduled/run time, searched interval, results, trigger reason, and action outcome. A saved alert definition, a fired instance and a delivered action are different pieces of evidence; this review observed none of them in a Splunk runtime.
39. None; it is an optional entry point.
40. Active blueprint, version, duration/agreement, price, delivery, retake/renewal, identity, and regional rules.

## Final readiness checklist

- [ ] I can navigate the platform and explain user-facing component/app context.
- [ ] I constrain searches by time, index, source metadata, terms, and fields before refining.
- [ ] I can interpret raw events, fields, timeline, tabs, search job state, and saved/exported results.
- [ ] I predict schemas and results for table, rename, fields, dedup, sort, top, rare, and stats.
- [ ] I can create/edit reports and statistical/chart panels in the dashboard framework available to me.
- [ ] I can create a CSV lookup file/definition, invoke it, configure automatic enrichment, and test failures.
- [ ] I can schedule a report and create, trigger, throttle, inspect, and operationalize a safe alert.
- [ ] I completed all eight labs with approved data and retained evidence.
- [ ] I can answer the original checks without looking at the answer key.
- [ ] I rechecked the official Core User page, blueprint, handbook, and policies.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, use documentation to resolve specific behavior, and spend at least as much time searching and building objects in a lab as watching. Commercial resources are supplementary; reconcile them with the current official blueprint and product version.

All hour ranges below are author planning budgets, not measured completion times. The course-sheet durations are publisher figures from **2024**, not a fresh price/access guarantee. The indexed seven-page sheet was read; no course was enrolled in or completed. Lantern's landing/index was read but its linked articles were not. The YouTube response exposed only a short page shell; no video or current playlist was reviewed. Udemy and the O'Reilly listing could not be verified in this pass.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official Core User blueprint](https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/splunk-test-blueprint-user.pdf) | Free canonical scope | 1–2 hr initial mapping and final review | Objective checklist, weights, contract |
| [Official Core User page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-user.html) | Free | 20–40 min before booking | Current status, delivery, price, links |
| [Splunk Search Tutorial 10.0](https://help.splunk.com/en/splunk-enterprise/search/search-tutorial/10.0/introduction/about-the-search-tutorial) | Free docs; trial/account may be needed for labs | 8–12 hr with all seven parts and variation testing | Connected search, lookup, report, chart, and dashboard lab |
| [Official Search Expert course set](https://www.splunk.com/en_us/pdfs/training/platform-curated-learning.pdf) | Mixed free/paid; 2024 duration sheet, so verify live catalog | About 13h45 for free Intro, Fields, Scheduling, Visualizations, Time, and Statistical Processing; add 3 hr paid lookup class if useful | Blueprint-aligned modules and time planning |
| [Splunk Search Manual 10.4](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.4/search-overview/get-started-with-search) | Free current product docs | 8–15 hr selected topics | Search UI, retrieval, time, fields, jobs, optimization |
| [Splunk SPL Search Reference](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/introduction/welcome-to-the-search-reference) | Free reference | 3–6 hr focused study plus ongoing lookup | Exact command syntax/options |
| [Splunk How-To YouTube channel](https://www.youtube.com/@SplunkHowTo) | Free official videos; catalog changes | 3–6 hr selected current search/report/dashboard videos plus lab recreation | Visual walkthroughs; verify UI against your version |
| [Splunk Lantern](https://lantern.splunk.com/) | Free official/community-reviewed use cases | 4–8 hr selected search/dashboard articles | Applied patterns after fundamentals |
| [Previously recorded O'Reilly Exploring Splunk listing](https://www.oreilly.com/library/view/exploring-splunk/9781977339805/) | Access and exact edition/format unverified this pass | No current duration verified | Historical lead only; confirm the title, format and contents before choosing it |
| [Udemy Splunk Core Certified User practice/course search](https://www.udemy.com/courses/search/?q=Splunk%20Core%20Certified%20User) | Paid marketplace; offerings change | Select 6–12 hr only after checking update date, active blueprint, instructor, and hands-on content | Optional alternate instruction, never recalled questions |

No exact current MeasureUp, Whizlabs, or Pluralsight Core User practice product was verified. Splunk's blueprint recommends official documentation, the Splunk How-To channel, and hands-on experience. Reject any source claiming live, recalled, exact-match, or guaranteed-pass questions.
