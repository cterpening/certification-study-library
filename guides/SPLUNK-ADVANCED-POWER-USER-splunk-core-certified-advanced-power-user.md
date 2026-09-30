---
exam_code: SPLUNK-ADVANCED-POWER-USER
vendor_id: splunk
official_blueprint: https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-advanced-power-user.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-30
---

# Splunk Core Certified Advanced Power User Study Guide

> **Independent AI-assisted resource — BEST-EFFORT PUBLIC-SOURCE REVIEW; HUMAN REVIEW PENDING.** On September 30, 2026, the complete indexed credential page and parsed six-page blueprint, all 104 mapped objectives, the full guide and 40 answers were reviewed. Selected official command and token references support the corrections below. Direct official retrieval failed DNS; the September 2 objective snapshot is retained with manual confirmation recorded separately. All ten Splunk labs remain unexecuted. See the [review and follow-ups](../docs/research/2026-09-30-splunk-advanced-power-user-deep-review.md). This is original learning material, not exam content.

**Current baseline:** 22 published domains spanning advanced SPL/knowledge objects (67%) and Simple XML forms/dashboards (33%). The highest individual domains are Multivalued Fields and Drilldowns at 7% each; all domains are required.<br>
**Exam contract:** intermediate; 70 multiple-choice questions; 60 total minutes including three minutes for the exam agreement; USD 130 per attempt; Pearson VUE delivery<br>
**Prerequisite contract:** Splunk Core Certified Power User is the named prerequisite on the credential page and blueprint. Confirm current eligibility and credential validity before booking.<br>
**Upcoming/lifecycle boundary:** no retirement or replacement was found in the credential page and blueprint checked September 30. This is a bounded observation, not a check of every release channel. Simple XML remains explicit blueprint scope. Framework availability and deprecations in your deployment need current verification; the existing dashboard overview and event-handler bodies could not be freshly retrieved.<br>

## How to use this guide

Build a version-controlled lab app in an approved nonproduction deployment. Use a varied data set large enough to expose nulls, multivalue fields, late events, cardinality, subsearch limits, summary overlap, and dashboard concurrency. For every optimization, record semantic equivalence before recording speed.

Use three passes:

1. **SPL correctness:** predict schema, row count, order, null/multivalue behavior, and time bounds.
2. **Search efficiency:** inspect distributed/search execution and Job Inspector; change one constraint or command at a time.
3. **Dashboard behavior:** trace each input, token, filter, search, event handler, drilldown, refresh, permission, and failure state.

> **About related items:** A `Related item:` callout adds architecture, governance, performance, security, or adjacent product context. It makes the objective more useful in practice but does not imply that the extra phrase appears verbatim in the public blueprint.

## Blueprint map

| Domains | Weight | Evidence to produce |
|---|---:|---|
| 1–7: statistics, eval, lookup, alert, fields, structured data, macros | 26% | Tested search/knowledge-object workbook with type, null, scope, and side-effect evidence |
| 8–11: acceleration and search efficiency/tuning | 15% | Baseline/equivalent optimized searches plus Job Inspector and summary-completeness evidence |
| 12–16: manipulation, multivalue, transaction, time, subsearch | 26% | Boundary-heavy SPL pipelines with cardinality and limit analysis |
| 17–18: Simple XML prototypes and forms | 9% | Valid prototype and token/cascading-input trace |
| 19–22: dashboard performance, customization, drilldowns, advanced behavior | 24% | Responsive, bounded dashboard with measured concurrency, token security, and contextual navigation |

## 1–2. Statistical commands and eval functions — 8%

`stats` transforms events into aggregates. Know count/list/values, distinct count, sum/average/min/max, earliest/latest, percentiles, and grouping behavior. `fieldsummary` profiles field presence/types/value characteristics to guide exploration, not to certify data quality. `appendpipe` runs a subpipeline against current results and appends its output—useful for totals/summary rows without restarting retrieval.

`eventstats` calculates aggregates and adds them back to each applicable event; `streamstats` calculates running/windowed results in current event order. Sort intentionally before order-dependent processing and understand memory/window/reset boundaries. `list` preserves ordered values but has limits; `values` deduplicates and orders rather than preserving event order.

`eval` function families include conversions, text, comparison/conditional, informational/type/null, statistical/math, and time formatting. Use [`makeresults`](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/search-commands/makeresults) to generate temporary rows without indexed input. Its default `_time` is execution time; assign fixed values when testing repeatability. The following SPL is a proposed, unexecuted type/null exercise:

```spl
| makeresults count=4
| streamstats count AS n
| eval value=case(n=1,"7",n=2,"",n=3,null(),true(),"12")
| eval numeric=tonumber(value), state=case(isnull(value),"missing",value="","blank",true(),"present")
| eventstats avg(numeric) AS average
```

> **Related item:** A command can be mathematically correct and still answer the wrong population. Preserve time, source coverage, grouping keys, units, and missing-value assumptions with every statistic.

## 3–4. Advanced lookups and alert actions — 8%

Advanced lookup work includes field mappings, `OUTPUT`/`OUTPUTNEW`, local behavior where relevant, match rules, time-bounded lookups, inclusion/exclusion patterns, and handling duplicates/nulls. Use `lookup` plus `where isnotnull(...)` for an inclusion filter, or a safe marker to distinguish unmatched rows. KV Store suits mutable application data and supports richer scale/update patterns; CSV remains simpler for static reference data. External lookups execute approved scripts/programs; geospatial lookups map location shapes and require suitable coordinates/features.

Govern lookup owner, app, permissions, update path, key uniqueness, case, freshness, and failure behavior. Never let a stale enrichment silently authorize a destructive action.

Alert actions can reference lookups, output results to a lookup, send a webhook, or create a searchable log event. `outputlookup` changes reference state; concurrency can overwrite/race unless designed. Webhooks send data outside Splunk and require TLS, authentication/secrets handling, allowlisting, schema/retry/idempotency, and data-minimization controls. Logging an alert event supports correlation/audit but can create feedback loops if the alert matches its own output.

## 5–7. Advanced fields, structured data, and macros — 10%

Choose extraction by data: built-in structured parsing/technology add-on where possible; delimiter for stable tabular text; `spath` for JSON/XML structures; `multikv` for table-like multi-line events; regex for stable unstructured patterns. In searches, `rex` extracts with named groups; `erex` generates candidate regex from examples and must be reviewed. Anchor/select literal prefixes, avoid catastrophic backtracking, constrain character classes/repetition, extract only needed fields, and test nonmatches/long adversarial input.

`spath` can auto-extract structured paths or target a path/output. The `spath()` eval function returns a selected value inside expressions. Self-describing data carries field structure, but it can still be malformed, nested, inconsistent, duplicated, or too large. `multikv` converts a table-shaped event into events/fields; headers and row boundaries need validation.

Nested macros expand reusable SPL and can call other knowledge objects. Preview expansion before execution, especially when arguments can broaden retrieval or carry quotes/wildcards. Track scope, ownership, dependency cycles, required fields, output schema, and permissions.

## 8–9. Acceleration and summaries — 8%

Report acceleration builds summaries for eligible transforming reports and transparently uses them for compatible time ranges/searches. Eligibility, schedule priority, changing definitions, data-model dependencies, permissions, and insufficient workload can prevent summary creation. Use the summary management/detail pages to inspect status, range, size, and errors.

Summary indexing explicitly writes scheduled transforming results to a summary index, commonly with `collect` or `sistats`/`sitimechart`/related commands, then searches those summarized fields. Design the summary schema, `_time`, source marker, schedule, window, lateness/backfill, retention, and deduplication. Gaps undercount and overlaps double count.

Data model acceleration builds `.tsidx` summaries for selected model datasets over a configured range. `datamodel` explores models. [`tstats`](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/search-commands/tstats) can query indexed fields without a data model, and can run over accelerated or unaccelerated models. For a model, select its root dataset and use the required field qualification. The default `summariesonly=false` can include unsummarized data outside summary coverage, at additional cost; `true` excludes that data and does not run over an unaccelerated model. Compare coverage and results before speed.

**Paper example, not a Splunk result:** if an intended population contains 120 matching events and only 90 are summarized, an otherwise equivalent summary-only count can cover just those 90. Faster execution does not establish a complete answer. Verify source population, time bounds, model constraints and lag in the actual deployment.

Choose among raw search, report acceleration, summary indexing, and data-model acceleration from reuse pattern, schema control, compatible searches, latency, retention, storage/compute, backfill, and governance—not merely fastest demo.

## 10–11. Efficient search and tuning — 7%

Search heads parse/plan/co-ordinate; indexers retrieve/process distributable work; forwarders collect/send. Command type affects where and how work runs. Streaming commands can process incrementally; centralized streaming may move work to the search head; transforming commands create aggregate datasets. Put selective time/index/indexed terms before broad processing and delay centralizing/transforming/display commands.

Job Inspector shows execution costs, event/result counts, remote/local phases, command timings, and warnings. Compare identical time/data/result semantics; cache/warmth and concurrency can distort one-off timing.

Lispy is the normalized Boolean form used for base-search optimization. Parentheses and uppercase Boolean operators matter; wildcard placement can block efficient term matching. `TERM(value)` asks Splunk to treat punctuation-containing text as a single indexed term where indexing/tokenization supports it. Test correctness—TERM is not magic substring search.

> **Related item:** Optimization has a correctness budget of zero. A faster search that changes time bounds, drops late data, changes nulls, or narrows events incorrectly is a different search.

## 12–13. Manipulating data and multivalue fields — 13%

`bin` discretizes numeric or time values into bins. `xyseries` pivots row-form x/y/value data into a wide matrix; duplicate x/y pairs require prior aggregation. `untable` reverses a wide table into row form. `foreach` applies a template across matching fields and needs predictable field selection. `strftime(epoch,"format")` formats epoch seconds using the search user's time zone unless otherwise controlled; retain numeric time for calculation.

Multivalue fields contain multiple values in one field. Know functions such as `mvcount`, `mvindex`, `mvfind`, `mvfilter`, `mvmap`, `mvappend`, `mvdedup`, `mvsort`, `mvjoin`, `split`, and `mvzip` according to current reference. `makemv` splits one value into several; `mvexpand` creates one result per value and can multiply rows/memory dramatically. Preserve relationships between paired arrays with explicit design rather than independent expansion.

```spl
... | eval pairs=mvzip(user,action,"::")
    | mvexpand pairs
    | eval user=mvindex(split(pairs,"::"),0), action=mvindex(split(pairs,"::"),1)
```

The pairing example assumes equal-length arrays in corresponding order and a delimiter absent from both values. For example, `user=[A,B]` and `action=[read,write]` represent two intended pairs; independent expansions would instead create four combinations. This is paper reasoning, not measured SPL output. Add unequal-length, missing-value and embedded-delimiter cases before trusting the implementation.

## 14–16. Transactions, time, and subsearches — 13%

Advanced transactions may need equivalent identifiers under different field names. Normalize before grouping with conditional assignment or rename; `coalesce(a,b,c)` selects the first non-null value but can incorrectly merge concepts that are not semantically equivalent. An alternative is separate transaction field lists/unified aliases or evaluated normalization with explicit source conditions.

The [`transaction` reference](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.4/search-commands/transaction) requires descending chronological input. Use explicit boundaries and inspect `eventcount`, `duration` and eviction behavior. `closed_txn` reports command closure, which can result from configured limits; it is not proof that the business process observed every expected boundary or succeeded. Define business completeness separately. Constrain time and fields first. Use stats only when grouping and ordering assumptions preserve the intended population and session boundaries.

Default time fields include `_time` and `_indextime`; date/time fields may be derived. Search earliest/latest, bin/span, time zone, snapping, DST, and timestamp extraction answer different concerns. Keep epoch values for arithmetic.

A subsearch runs first and formats its results into the outer search. It has time/result/runtime limits, so truncation can silently change logic. Use it for small bounded dynamic filters; prefer lookup, join-free stats patterns, eventstats, OR searches, or data models where scalable. Run the subsearch alone, inspect `format`, time range, count, truncation messages, and Job Inspector. `append` adds subsearch rows vertically and still carries subsearch caveats.

## 17–18. Simple XML prototypes and forms — 9%

Simple XML dashboards use elements such as `<form>`/`<dashboard>`, `<label>`, `<fieldset>`, `<input>`, `<row>`, `<panel>`, visualization elements, and `<search><query>`. Start with valid minimal source, comments, stable IDs/tokens, bounded searches, and accessible labels. Validate XML nesting/escaping and use browser/search-job evidence to troubleshoot blank panels.

Tokens are variables populated by form inputs, search results/states, page initialization, or drilldowns. Form inputs can have defaults, initial values, choices, search-populated choices, and submitted/change behavior. Cascading inputs derive later choices from earlier tokens; define safe defaults, unset behavior, and bounded search dependencies.

The [Simple XML token reference](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/simple-xml-dashboards/10.4/drilldown-and-dashboard-interactivity/token-usage-in-dashboards) distinguishes `|s` (quote a value and escape embedded quotes), `|h` (HTML) and `|u` (URL). **`|n` disables default escaping; it is not another protective encoder.** Select the filter for the consuming context and validate allowed values. No filter grants authorization. A quoted search value is not automatically a valid field name or an allowed URL destination.

Token-based `depends`/`rejects` visibility does not by itself stop background searches. Hiding a panel therefore proves neither lower search load nor restricted data access; inspect search jobs and permissions separately.

For deployment-specific verification, Classic/Simple XML behavior is documented in [Dashboard overview](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/simple-xml-dashboards/10.4/get-started-with-dashboards/dashboard-overview).

## 19–22. Performance, customization, drilldowns, and behavior — 24%

Improve dashboard performance by limiting time/data, using efficient commands/tstats where semantically valid, reducing high-cardinality panels, limiting concurrent searches, sharing a base search with post-process searches, delaying panels until inputs are ready, and choosing refresh intervals from data freshness/decision need. A post-process search sees only fields/results retained by the base search and has row/result limits; do not use it when panels require incompatible raw events or time ranges.

Customize chart/panel properties for honest titles, axes, units, legends, nulls, colors, and interaction. Refresh and delay settings can prevent stale data or search storms. Search-access controls can hide open/export/inspect affordances from users, but are not data security; roles/search constraints still enforce access. Event annotations add time-aligned contextual markers to charts and need reliable time/category/search definitions.

Drilldowns can link to searches, dashboards/forms, or external URLs, or manage tokens in the current dashboard. Predefined click tokens vary by visualization, such as clicked values/rows. Dynamic drilldowns must encode values, carry earliest/latest deliberately, restrict destinations, and handle null/multivalue input. Never create injection-prone SPL/URLs from raw token text.

Event handlers respond to input change, search progress/done/error, page load, selection, and drilldown contexts, using actions such as set, unset, eval, and link. Contextual behavior uses conditions and tokens to choose actions. Simple XML extensions can add JavaScript/CSS behavior in supported environments, but expand security, compatibility, accessibility, and upgrade risk; prefer native supported capabilities when adequate.

The versioned [Event Handler Reference](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/simple-xml-dashboards/10.2/simple-xml-reference/event-handler-reference) and [token management guidance](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/simple-xml-dashboards/10.4/drilldown-and-dashboard-interactivity/manage-token-values-in-the-current-dashboard) are official references; their full bodies remain next-pass reading.

> **Related item:** Dashboard Studio also supports tokens and event handlers through a different JSON model. Learn it for current work where appropriate, but keep framework syntax separate from the blueprint's explicit Simple XML contract.

## Integrated scenarios

### Scenario 1: Efficient service-health model

Parse structured and multiline data, normalize multivalue fields, create raw/stats/accelerated model versions, then prove equivalent results across time boundaries and summary lag. Record Job Inspector, tsidx/tstats, subsearch replacement, and gap/overlap evidence.

### Scenario 2: Safe enrichment-to-alert workflow

Use KV/geospatial/reference lookups to enrich events, filter matched/unmatched cases, write a bounded alert state lookup, log a searchable alert event, and post a redacted/idempotent webhook to a lab endpoint. Prevent self-trigger loops.

### Scenario 3: Classic interactive dashboard

Create a valid Simple XML form with cascading inputs, token filters, base/post-process searches, annotations, refresh/delay, conditional event handlers, internal/external drilldowns, and access controls. Test blank/default/special/multivalue tokens, no data, search error, permissions, concurrency, keyboard use, and version portability.

## Hands-on labs

1. Statistical/eval/makeresults boundary workbook.
2. Advanced CSV/KV/external/geospatial lookup comparison with safe alert actions.
3. Regex/rex/erex/spath/multikv extraction correctness and performance test.
4. Nested macro dependency, expansion, argument, permission, and failure audit.
5. Report/summary/model acceleration comparison with backfill gap/overlap exercise.
6. Raw-to-efficient SPL rewrite using command types, Lispy/TERM, and Job Inspector.
7. Bin/xyseries/untable/foreach/time and multivalue cardinality pipeline.
8. Transaction versus stats and bounded subsearch versus non-subsearch alternatives.
9. Simple XML prototype/form with input, cascading token, filter, and error-state trace.
10. Full dashboard performance/customization/drilldown/event-handler/extension review.

For each lab, retain input, expected/actual results, SPL/source, version, timings, warnings, permission context, and regression case.

## Lab evidence and next-pass fixes

All ten labs are **not executed**: no Splunk runtime or approved endpoint was available. The numeric and pairing examples are predictions only. No lookup write, alert, webhook, service, dashboard deployment or configuration change was performed.

| Lab | Evidence still needed |
|---|---|
| 1. Statistics/eval | Fixed-time fixtures; null/type/order results and warnings |
| 2. Lookups/alerts | Approved isolated data; duplicate/missing keys; write races; redacted webhook/log-loop evidence |
| 3. Extraction | Valid/malformed structured input; regex nonmatches and measured costs |
| 4. Macros | Expanded nested syntax; dependencies, scope and permission failures |
| 5. Acceleration | Raw versus summary populations, lag, backfill gaps/overlaps and summary-only omission |
| 6. Search tuning | Equivalent result sets and Job Inspector evidence under comparable conditions |
| 7. Multivalue/time | Pair alignment, unequal/missing values, delimiter collisions, row counts and time-zone edges |
| 8. Transactions/subsearches | Descending input, reused identifiers, boundary closure, eviction and truncated-filter cases |
| 9. Forms/tokens | Blank/special inputs; context-specific filters; `|n` risks and actual submitted searches |
| 10. Dashboard | Background jobs for hidden panels, concurrency, drilldowns, permissions, accessibility and extension compatibility |

Contributors can add fixes with the product version/framework, minimal public or synthetic input, exact SPL/XML, expected and observed results, warnings and reproduction steps. If sources conflict, record both dated sources and mark the point as needing more research on the next pass. An unavailable source or unexecuted lab is not a successful verification.

## Original readiness checks

1. How do stats, eventstats, and streamstats change results differently?
2. What does appendpipe consume?
3. Why can list and values differ?
4. What makes makeresults useful?
5. How do OUTPUT and OUTPUTNEW differ?
6. When is KV Store preferable to CSV?
7. What is the primary risk of outputlookup in an alert?
8. How can a log-event alert loop?
9. When should rex, spath, and multikv be selected?
10. Why must erex output be reviewed?
11. Name two regex performance improvements.
12. What must a nested macro dependency map include?
13. What makes a report eligible/useful for acceleration?
14. How do summary gaps and overlaps affect results?
15. What does data model acceleration build?
16. When can tstats use an accelerated data model?
17. Why compare optimized and raw results at boundaries?
18. How does command type affect distributed execution?
19. What evidence does Job Inspector add?
20. What does TERM attempt to match?
21. What prefiltering belongs earliest?
22. Why must xyseries inputs be aggregated for duplicate x/y pairs?
23. What does mvexpand do to row cardinality?
24. How can paired multivalue relationships be preserved?
25. Why can coalesce create incorrect transactions?
26. How do complete and incomplete transactions differ?
27. Which default time fields answer event versus ingest time?
28. What is the main subsearch danger?
29. How should a subsearch be troubleshot?
30. What does append do?
31. What root elements distinguish a Simple XML form and dashboard?
32. What creates a cascading input?
33. Why are token filters not authorization?
34. When is base/post-process unsuitable?
35. Why do refresh settings affect capacity?
36. Does hiding search/export controls secure the underlying data?
37. Which destinations can drilldowns target?
38. What should dynamic drilldowns preserve and encode?
39. What is the explicit certification prerequisite?
40. What lifecycle/framework fact must be rechecked?

## Answer key

1. Aggregate rows; aggregates copied to events; running/windowed aggregates by current order.
2. The current pipeline's results, then appends its subpipeline output.
3. List preserves values/order with limits; values deduplicates/sorts.
4. It creates temporary synthetic rows without indexed input. Set fixed values, including `_time` where relevant, for repeatability; the default timestamp is execution time.
5. OUTPUT may overwrite; OUTPUTNEW only fills absent destinations.
6. For frequently updated/application-managed keyed data; CSV for simpler static reference.
7. Concurrent/stateful writes can overwrite, race, grow, or corrupt intended state.
8. If its own logged event satisfies the same trigger search.
9. Regex text, structured JSON/XML, and table-like multiline events respectively.
10. Generated patterns may over/under-match or perform poorly.
11. Anchor/literal prefixes, narrow classes/quantifiers, avoid backtracking, constrain scope; any two.
12. Macro/knowledge objects, arguments, fields/schema, app/permissions, version, and cycle risk.
13. A repeatedly run eligible transforming report whose compatible ranges benefit from summaries.
14. Gaps undercount; overlaps double count.
15. `.tsidx` summaries for configured model datasets/range.
16. Reference the model/root dataset correctly and inspect summary coverage. `tstats` also supports indexed data and unaccelerated models. Default `summariesonly=false` may include unsummarized data; `true` restricts results to summaries, potentially omitting part of the intended range.
17. Acceleration/range/null/late-data behavior can change results.
18. It determines streaming/centralizing/transforming placement and data movement.
19. Per-command phase/timing/count/warning evidence.
20. A punctuation-containing indexed term as a single token, where supported by tokenization.
21. Time, index, indexed metadata, and selective terms that preserve intended events.
22. Otherwise duplicate coordinates can overwrite or produce ambiguous matrix cells.
23. Creates one row per value and can multiply memory/results.
24. Preserve an explicit relationship key, or zip aligned equal-length arrays before expansion with a collision-free delimiter. Test missing, unequal and delimiter-containing inputs.
25. It can collapse identifiers that look interchangeable but represent different semantics.
26. Business completeness requires explicit expected-boundary evidence. `closed_txn` alone describes command closure, including configured-limit closure, and does not prove business success.
27. `_time` and `_indextime`.
28. Runtime/result limits can truncate filters silently.
29. Run alone, inspect formatted output/count/time/warnings, then inspect outer search and Job Inspector.
30. Adds subsearch rows vertically to main results.
31. `<form>` and `<dashboard>`.
32. A later input's choice search depends on an earlier input token.
33. Encoding changes representation; permissions enforce authority. `|n` disables escaping. Hiding panels also does not stop their background searches.
34. When panels need incompatible raw fields, time ranges, or result cardinality beyond base/post-process behavior.
35. They determine repeated search concurrency/load and freshness.
36. No; role and search permissions remain the security boundary.
37. Search, dashboard/form, external URL, or current-dashboard token behavior.
38. Correct encoding, allowlisted destination, time range, fields, null/multivalue semantics, and permissions.
39. Splunk Core Certified Power User.
40. Simple XML remains explicit blueprint scope, while framework/features vary and deprecations must be checked.

## Final readiness checklist

- [ ] I can explain and prove every command/knowledge-object result across null, type, order, and cardinality boundaries.
- [ ] I can compare raw, report summary, summary index, and accelerated-model implementations for equivalent results.
- [ ] I can use Job Inspector and command distribution evidence without trading away correctness.
- [ ] I can safely handle lookups, alert side effects, regex, structured data, and nested macro dependencies.
- [ ] I can reason about time, transactions, multivalue fields, and subsearch limits under realistic edge cases.
- [ ] I can author/troubleshoot valid Simple XML forms and token/cascading-input behavior.
- [ ] I can measure and control dashboard searches, refresh, base/post-process, tstats, and panel behavior.
- [ ] I can build encoded contextual drilldowns and event handlers without confusing UI controls with authorization.
- [ ] I completed all ten labs with approved data and regression evidence.
- [ ] My required Power User credential is current, and I rechecked the exam/framework contract.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick official training or a documentation-led lab as the primary path, then add targeted alternatives. Spend more time producing and measuring searches/dashboards than watching. Reconcile all resources with the current blueprint and your product/framework version.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official Advanced Power User blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-advanced-power-user.pdf) | Free canonical scope | 2–3 hr mapping/final review | All 22 domains and prerequisite |
| [Official certification page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-advanced-power-user.html) | Free | 20–40 min before booking | Status, price, delivery, prerequisite |
| [Official Advanced Power User named-course set](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-advanced-power-user.pdf) | Mixed free/paid; follow links/search current catalog | 35–55 hr author planning budget for the 14 suggested course topics plus labs; actual course durations unverified | Blueprint sequence |
| [Search Manual 10.4](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.4/search-overview/get-started-with-search) and [SPL reference](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/introduction/welcome-to-the-search-reference) | Free versioned docs | 18–30 hr selected advanced commands with experiments | Exact SPL semantics/performance |
| [Knowledge Management Manual 10.4](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4) | Free | 15–25 hr selected extraction/lookup/macro/model/acceleration topics | Search-time objects and acceleration |
| [Classic/Simple XML dashboards 10.4](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/simple-xml-dashboards/10.4/get-started-with-dashboards/dashboard-overview) | Free; framework availability varies | 15–25 hr with one complete form/dashboard | Explicit 33% dashboard scope |
| [Splunk How-To YouTube](https://www.youtube.com/@SplunkHowTo) | Free official videos | 5–10 hr selected videos plus recreation | Visual walkthroughs; verify UI/version |
| [Splunk Lantern](https://lantern.splunk.com/) | Free use cases | 8–15 hr selected optimization/dashboard examples | Applied second path |
| [Pluralsight Splunk search](https://www.pluralsight.com/search?q=Splunk) | Subscription; catalog may not align to exam/framework | Select 10–20 hr after objective mapping | Alternate explanations |
| [O'Reilly Splunk search](https://www.oreilly.com/search/?q=Splunk) | Subscription; much content uses older versions | Select 10–20 hr, verifying syntax/deprecations in current docs | Deep dives/reference |
| [Udemy Advanced Power User search](https://www.udemy.com/courses/search/?q=Splunk%20Advanced%20Power%20User) | Paid marketplace; quality/version vary | Select 10–20 hr only after blueprint/provenance/lab review | Optional structured course |

**September 30 evidence boundary:** the blueprint names 14 suggested courses, but current enrollment, access and individual course durations were not verified. All time ranges in this table are author planning budgets. Direct receipts include three reachable links, twelve DNS errors and two blocked searches. Lantern passed its initial health check but its subsequent body retrieval failed; no fresh article reading is claimed. YouTube returned a 176-character shell, and the complete 3,919-character Pluralsight response contained navigation and an unrendered template, not course results. O'Reilly and Udemy searches were blocked. No paid interior or video was reviewed.

No exact current MeasureUp or Whizlabs Advanced Power User practice product was verified. Reject recalled/live/guaranteed-pass questions. The volume and age of marketplace Simple XML material make version verification especially important.
