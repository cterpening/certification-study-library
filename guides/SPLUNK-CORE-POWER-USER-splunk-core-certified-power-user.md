---
exam_code: SPLUNK-CORE-POWER-USER
vendor_id: splunk
official_blueprint: https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-power-user.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Splunk Core Certified Power User Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, three-page public blueprint, current Splunk search/knowledge/CIM documentation, public training catalog, and selected learning resources were checked September 2, 2026. The checks here are original learning prompts, not representations of exam items. Recheck the [official certification page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-power-user.html) and [test blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-power-user.pdf) before scheduling.

**Current baseline:** Transforming Commands for Visualizations (5%); Filtering and Formatting Results (10%); Correlating Events (15%); Creating and Managing Fields (10%); Field Aliases and Calculated Fields (10%); Tags and Event Types (10%); Macros (10%); Workflow Actions (10%); Data Models (10%); Common Information Model Add-On (10%). Related topics may appear and the blueprint may change without notice.<br>
**Exam contract:** entry level; 65 multiple-choice questions; 60 total minutes including three minutes for the exam agreement; USD 130 per attempt; Pearson VUE delivery<br>
**Prerequisite contract:** no prerequisite exam. Core User is a useful foundation, but it is not required by the published contract.<br>
**Upcoming change:** no retirement or replacement was announced when checked. The blueprint tests the established SPL and knowledge-object workflow. SPL2 is adjacent current-platform context, not a reason to replace the named commands or objects in this blueprint.<br>

## How to use this guide

Work in a Splunk-provided lab, a trial, or an approved nonproduction environment. Use representative synthetic data with at least two sourcetypes so normalization has real meaning. Build each object privately first, test its search-time dependencies, then share it only after reviewing app context and permissions.

For every objective, preserve four artifacts:

1. the input events and expected fields;
2. the SPL or knowledge-object definition;
3. matched, unmatched, null, duplicate, and boundary evidence;
4. a short explanation of search-time order, scope, permissions, and downstream effect.

> **About related items:** A `Related item:` callout adds architecture, governance, performance, security, or adjacent product context. It makes the objective more useful in practice but does not imply that the extra phrase appears verbatim in the public blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Transforming Commands for Visualizations | 5% | Correct chart and timechart result shapes |
| Filtering and Formatting Results | 10% | Typed eval fields and equivalent/different search/where filters with null handling |
| Correlating Events | 15% | Transaction definition and a justified stats alternative |
| Creating and Managing Fields | 10% | Tested regex- and delimiter-based Field Extractor definitions |
| Field Aliases and Calculated Fields | 10% | Non-destructive normalization plus calculated search-time fields |
| Tags and Event Types | 10% | Reusable categorization whose searches and dependencies are valid |
| Macros | 10% | Basic and argumented macros with validated expansion and safe permissions |
| Workflow Actions | 10% | Lab-only GET, POST, and Search actions with field substitution controls |
| Data Models | 10% | Dataset hierarchy and Pivot evidence with correct constraints/fields |
| Common Information Model Add-On | 10% | Two-source normalization to published CIM tags/fields plus validation |

## 1. Transforming commands for visualizations — 5%

`chart` aggregates values over categorical dimensions. One split-by field commonly becomes series/columns and another the x-axis categories; verify the produced table before selecting a visual. `timechart` aggregates into `_time` buckets and expects time-aware events. Use `span` deliberately and understand that time range and bucket width change both readability and aggregation.

```spl
index=web earliest=-24h
| chart count over status by host

index=web earliest=-24h
| timechart span=30m count by status
```

High-cardinality split fields can create many series and an “OTHER” grouping depending on command options. Missing/null split values may disappear or group unexpectedly. Do not infer absence of activity from a chart until inspecting the underlying table, time zone, series limits, and search completeness.

> **Related item:** Visualization is downstream of aggregation. Labels, units, axes, truncation, time zones, and category limits can mislead even when the SPL is syntactically correct.

## 2. Filtering and formatting results — 10%

`eval` creates or changes fields using expressions and functions. Know arithmetic, string concatenation, conditional `if`/`case`, conversion, comparison, and null-aware functions at a practical level. Splunk values can be strings, numbers, Booleans within evaluation, and multivalue fields; verify type assumptions rather than trusting appearance.

`search` uses search syntax and is convenient for matching field values and Boolean terms. `where` evaluates an expression and supports field-to-field comparisons and functions. Both filter pipeline results, but quoting, nulls, and expression semantics differ.

```spl
... | eval latency_s=duration_ms/1000
    | where latency_s > threshold_s
    | fillnull value="unknown" owner
```

`fillnull` replaces null/missing values for fields that exist in the result schema. If a field is null/missing in every event, Splunk may not recognize it as a field; create it explicitly with `eval` when needed. Do not replace unknown with zero unless zero is semantically correct.

## 3. Correlating events — 15%

A transaction groups related events into one result, usually by shared field values and optionally time/start/end constraints. Understand `maxspan`, `maxpause`, `startswith`, `endswith`, ordering, `eventcount`, `duration`, and multivalue output conceptually. Test overlapping identifiers, missing boundaries, reuse of IDs, out-of-order/late events, and incomplete sessions.

```spl
index=auth earliest=-4h
| transaction session_id startswith="login_start" endswith="logout" maxspan=2h
| table session_id eventcount duration closed_txn
```

`transaction` can be memory-intensive and retains raw event relationships. `stats` is usually preferable when grouping and aggregate fields answer the question:

```spl
index=auth earliest=-4h
| stats earliest(_time) AS first latest(_time) AS last count AS eventcount values(action) AS actions by session_id
| eval duration=last-first
```

Choose transaction when event ordering/boundaries and combined raw-event context are essential; choose stats for scalable grouping/aggregation. A similar row does not prove identical semantics—document handling of incomplete groups, multivalue order, and boundaries.

## 4. Creating and managing fields — 10%

The Field Extractor (FX) creates search-time extractions from returned events. Regex mode suits irregular/unstructured text: select representative samples, highlight values, inspect the generated named-capture expression, and test positive/negative cases. Delimiter mode suits consistent structured rows with headers and a common delimiter.

Define the source type/host/source/app scope carefully. Use meaningful field names and avoid collision with established fields. Representative testing must include missing columns, quoted delimiters, alternate messages, malformed rows, and values at beginning/end. Permissions determine who receives the extraction.

The generated extraction is a starting point, not proof. Greedy expressions can capture too much; a delimiter extraction can fail when quoting/escaping changes. [Build field extractions with the Field Extractor](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4/use-the-field-extractor-in-splunk-web/build-field-extractions-with-the-field-extractor) is the current UI reference.

> **Related item:** Prefer a supported technology add-on and correct sourcetype before building local duplicate extractions. Parallel field definitions create schema drift and search-time cost.

## 5. Field aliases and calculated fields — 10%

A field alias gives an existing extracted field an additional name. It does not rename or remove the original. This supports normalization when different sources use `src_ip`, `client_ip`, or another vendor name for the same concept. It cannot depend on a field created later in search-time processing.

A calculated field uses an `eval` expression automatically at search time for a selected source/host/sourcetype. Use it for a stable derived value such as normalized units or a category. Handle nulls/types and avoid expensive/opaque expressions applied to broad datasets.

Search-time order matters: automatic key-value extraction precedes field aliases; aliases precede calculated fields; lookups, event types, and tags have later dependencies. The current [tags and aliases documentation](https://help.splunk.com/en/splunk-cloud-platform/manage-knowledge-objects/knowledge-management-manual/10.4.2604/tags/about-tags-and-aliases) documents these boundaries.

## 6. Tags and event types — 10%

A tag labels a field-value pair (including an event type) so searches can group equivalent meanings. Search with `tag=name` or tag-qualified forms as appropriate. Tags are search-time knowledge and depend on the field/value existing first. Use governed names and avoid massive tagging where lookups are a better scale mechanism.

An event type is a named search that classifies matching events, supporting tags, reports, dashboards, and other reuse. Give it a selective, valid base search; event-type definitions have search restrictions and cannot depend on tags that are applied later. Assign priority and permissions deliberately. Test both matching and near-miss events.

> **Related item:** Tags categorize values; event types categorize events through a search; aliases normalize field names. Choosing the wrong object can make dependencies circular or maintenance unnecessarily broad.

## 7. Macros — 10%

A search macro is reusable SPL text invoked with backticks. A basic macro can standardize a source constraint or expression. Argumented macros substitute named variables such as `$field$`; the macro name includes its argument count in management context.

```spl
`recent_errors(web,24h)`
```

Inspect the expanded search to debug. Validate arguments when possible, quote according to intended type, and never assume a macro argument is safe merely because it came from another dashboard/search. Recursive/circular expansion and hidden broad searches are operational risks. App context and permissions affect resolution.

Use macros for stable reusable fragments, not to hide incomprehensible searches. Document arguments, expected fields, output, owner, and compatibility.

## 8. Workflow actions — 10%

Workflow actions turn a field/event into a contextual next step:

- GET opens or requests a URL with values in a query string.
- POST sends values in a request body.
- Search launches another Splunk search populated with selected field values.

Define label, scope, required fields/event types, destination/search, app context, and visibility. Field-token substitution requires encoding and validation. GET leaks values into URLs/history/logs; POST is not automatically secure; both require HTTPS, destination trust, authorization, anti-forgery behavior, and data-minimization review. Use a lab endpoint—never trigger a real ticket, containment, or business action while practicing.

A Search workflow action should preserve quoting, time context, index access, and least privilege. Test missing fields and hostile/special characters.

## 9. Data models — 10%

A data model organizes one or more datasets (historically called objects in some interfaces/material) into a hierarchy with constraints and fields/attributes. Root datasets can be based on events, searches, or transactions; child datasets inherit and narrow parent constraints. Fields can be auto-extracted, inherited, calculated, or lookup-derived depending on model design.

Pivot uses data models so users can create tables/charts without writing all SPL directly. A model only exposes what its constraints and fields define. Create a small model, set app/permissions, add a child, test counts against equivalent SPL, and build a Pivot. Data model acceleration is important later-track context; do not enable it casually without retention/capacity/governance decisions.

See [Design data models](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4/build-a-data-model/design-data-models).

## 10. Common Information Model Add-On — 10%

Splunk CIM is a shared semantic model delivered as an add-on with preconfigured data models, documentation, validation tooling, and common field/tag expectations. It normalizes equivalent events from different vendors at search time while leaving raw data unchanged. Apps such as Enterprise Security depend on correctly normalized fields and tags.

Normalization usually combines technology-add-on extractions, field aliases, calculated fields, lookups, event types, and tags. Do not map based only on similar names: confirm the data model/dataset constraint, required/recommended fields, data type, allowed meaning, tag requirements, units, and null behavior. Validate two different sources through the same CIM-based search/Pivot.

The live [CIM overview](https://help.splunk.com/en/splunk-cloud-platform/common-information-model/5.3/introduction/overview-of-the-splunk-common-information-model) describes the shared-model purpose; version-specific release notes should be checked before implementation. CIM is unrelated to the DMTF CIM.

> **Related item:** The OCSF CIM add-on is a newer compatibility layer for OCSF-formatted security events. It does not erase the blueprint requirement to understand the established Splunk CIM and its data-model contract.

## Integrated scenarios

### Scenario 1: Cross-source authentication model

Extract fields from delimited and unstructured authentication sources, alias vendor fields to common names, calculate outcome/duration, create success/failure event types and tags, then map both sources to the appropriate CIM dataset. Validate raw, normalized, model, and Pivot counts.

### Scenario 2: Session correlation decision

Build transaction and stats versions of a session search. Add incomplete, overlapping, reused-ID, and delayed events; compare output semantics and resource evidence. Produce chart/timechart visualizations and justify the selected implementation.

### Scenario 3: Governed analyst workflow

Create an argumented macro for a bounded base search, a Search workflow action to pivot on a user, and lab-only GET/POST actions to an echo endpoint. Test expansion, escaping, missing values, app permissions, data disclosure, and auditability.

## Hands-on labs

1. **Chart/timechart matrix:** vary split fields, nulls, category limits, span, time range, and time zone; validate every graph against its table.
2. **Eval/filter/null workbook:** build typed derived fields and compare search versus where across strings, numbers, nulls, multivalue fields, and field-to-field comparisons.
3. **Correlation comparison:** implement transaction and stats against complete/incomplete/overlapping sessions; record correctness, schema, ordering, and resource behavior.
4. **Field Extractor validation:** create regex and delimiter extractions from representative samples; test malformed/near-miss cases and inspect generated definitions/scope.
5. **Search-time object chain:** create aliases, calculated fields, event types, and tags with a documented dependency order; prove each object on two sources.
6. **Macro safety:** create no-argument and argumented macros, inspect expansion, test quotes/special characters, and verify app/permission resolution.
7. **Workflow action lab:** create GET, POST, and Search actions against nonproduction targets; test token encoding, missing fields, sensitive values, and authorization assumptions.
8. **Data model/CIM project:** build a dataset hierarchy and Pivot, then normalize two vendor-shaped sources to one CIM dataset and validate equivalent counts/fields.

## Original readiness checks

1. When should chart be preferred to timechart?
2. What must timechart have to create time buckets?
3. Why inspect the result table before choosing a visualization?
4. What does eval produce?
5. When is where more natural than search?
6. Why might fillnull fail to expose an all-null field?
7. What does transaction produce?
8. Name two transaction time/boundary controls.
9. When is stats normally preferable to transaction?
10. Why can stats and transaction rows that look alike still differ semantically?
11. When should the FX regex method be used?
12. When should delimiter extraction be used?
13. What must an extraction test set contain?
14. Does a field alias delete the original field?
15. What creates a calculated field?
16. Why does search-time operation order matter?
17. What does a tag label?
18. What does an event type classify?
19. Why cannot an event type safely depend on a later-applied tag?
20. When is a lookup better than thousands of tags?
21. How is a macro invoked?
22. What should an argumented macro document?
23. Why inspect macro expansion?
24. Which workflow action puts values in a URL?
25. Why is POST not inherently safe?
26. What should a Search workflow action preserve?
27. What does app context affect for knowledge objects?
28. What is a data model?
29. What does a child dataset inherit?
30. How does Pivot use a data model?
31. Why compare Pivot counts with SPL?
32. What does CIM normalize?
33. Does CIM rewrite raw indexed data?
34. Which knowledge-object types can contribute to normalization?
35. Why is matching a field name insufficient for CIM compliance?
36. What is the largest weighted domain?
37. How many questions and minutes are published?
38. Is Core User a prerequisite exam?
39. What newer language is related but not a substitute for this blueprint's SPL?
40. What must be rechecked before purchase?

## Answer key

1. For category-based rather than time-bucketed aggregation.
2. `_time`-aware results and a chosen time range/bucketing policy.
3. The graph inherits omissions, limits, null handling, and shape from the table.
4. Derived or modified fields on result rows.
5. For evaluated expressions, functions, and field-to-field comparisons.
6. A field absent/null in every event may not exist in the result schema.
7. One grouped result with combined event context and metadata such as duration/event count.
8. Any two of maxspan, maxpause, startswith, and endswith.
9. When scalable grouping/aggregates answer the question without raw-event transaction semantics.
10. Incomplete groups, ordering, multivalue representation, and boundaries can differ.
11. For unstructured text with a stable pattern.
12. For consistently delimited structured records.
13. Representative positives plus missing, malformed, alternate, and near-miss negatives.
14. No; it adds another searchable name.
15. An automatically applied eval expression for the selected source scope.
16. An object cannot reliably depend on a field/tag produced later.
17. A field-value pair or event type.
18. Events matching a named search definition.
19. Tags are processed after event types, creating an invalid dependency direction.
20. For large or frequently governed/reference-driven classifications.
21. With its name/arguments inside backticks.
22. Argument types/quoting, required fields, expansion, result schema, owner, scope, and errors.
23. To debug and detect unsafe, broad, or incorrect substituted SPL.
24. GET.
25. It still requires TLS, trusted destination, authorization, request-integrity, and data review.
26. Correct quoting, time context, index constraints, app, and permissions.
27. Visibility, resolution, ownership, and sharing.
28. A hierarchy of constrained datasets and fields representing a domain.
29. Parent constraints and fields, then narrows/adds its own definition.
30. It supplies curated datasets/fields for table/chart construction.
31. To validate that model constraints and fields represent the intended events.
32. Equivalent semantic fields/tags across different source formats/vendors.
33. No; it is principally search-time schema.
34. Extractions, aliases, calculated fields, lookups, event types, tags, and data models.
35. Dataset constraints, tags, meaning, type, units, and required fields must also match.
36. Correlating Events at 15%.
37. 65 questions and 60 total minutes including the agreement.
38. No; there are no prerequisite exams.
39. SPL2.
40. Current page/blueprint, price, duration, delivery, identity, retake, and renewal policies.

## Final readiness checklist

- [ ] I can produce honest chart/timechart visualizations from validated tables.
- [ ] I use eval, search, where, and fillnull with deliberate type/null semantics.
- [ ] I can build transaction and stats correlations and justify the choice with boundaries and resource evidence.
- [ ] I can create, scope, test, and share regex/delimiter field extractions.
- [ ] I understand dependencies among aliases, calculated fields, tags, and event types.
- [ ] I can create and safely invoke basic/argumented macros and all three workflow-action types.
- [ ] I can create a data model, dataset hierarchy, fields, and Pivot and validate it against SPL.
- [ ] I can normalize two sources to an actual published CIM dataset and validate fields/tags.
- [ ] I completed all eight labs with approved data and no production side effects.
- [ ] I rechecked the current certification page, blueprint, handbook, and policies.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, use product/CIM documentation to resolve exact behavior, and spend at least as much time creating and testing knowledge objects as watching. Commercial resources are supplementary; reconcile them with the current blueprint and product/CIM versions.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official Power User blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-power-user.pdf) | Free canonical scope | 1–2 hr mapping/final review | Weights and objective contract |
| [Official Power User page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-power-user.html) | Free | 20–40 min before booking | Current status, price, delivery, policies |
| [Official platform curated-learning map](https://www.splunk.com/en_us/pdfs/training/platform-curated-learning.pdf) | Mixed free/paid; 2024 duration sheet, verify live catalog | About 25–35 hr across named blueprint courses, depending on paid Correlation/Knowledge modules | Working with Time, Statistical Processing, Comparing Values, Result Modification, Correlation, Knowledge Objects, Extractions, Data Models |
| [Splunk Knowledge Management Manual 10.4](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4) | Free current product docs | 12–20 hr selected topics plus lab work | Authoritative object behavior and search-time order |
| [Splunk CIM documentation](https://help.splunk.com/en/splunk-cloud-platform/common-information-model/5.3/introduction/overview-of-the-splunk-common-information-model) | Free; choose version compatible with your deployment | 6–12 hr for overview, one data model, normalization, validation | Actual schema rather than memorized field lists |
| [Splunk Search Manual 10.4](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.4/search-overview/get-started-with-search) | Free | 8–12 hr correlation/transforming/optimization topics | SPL foundations and command choice |
| [Splunk How-To YouTube channel](https://www.youtube.com/@SplunkHowTo) | Free official videos; UI/catalog varies | 4–8 hr selected videos plus recreation | Visual object-creation walkthroughs |
| [Splunk Lantern](https://lantern.splunk.com/) | Free official/community-reviewed use cases | 6–10 hr selected search/CIM patterns | Applied examples after fundamentals |
| [Pluralsight Splunk learning search](https://www.pluralsight.com/search?q=Splunk) | Subscription; catalog changes and may not align by exam | Select 8–15 hr after matching each course to blueprint | Alternate explanations, not blueprint authority |
| [O'Reilly Splunk search](https://www.oreilly.com/search/?q=Splunk) | Subscription; many books/courses use older UI/product releases | Select 8–15 hr, then verify every object in current docs | Deeper SPL/knowledge-management context |
| [Udemy Power User search](https://www.udemy.com/courses/search/?q=Splunk%20Core%20Certified%20Power%20User) | Paid marketplace; offerings change | Select 8–15 hr only after verifying update date, blueprint, labs, and provenance | Optional alternate path |

No exact current MeasureUp or Whizlabs Power User practice product was verified. Reject live/recalled/guaranteed-pass questions; use the public blueprint, official docs, and hands-on behavior as truth.
