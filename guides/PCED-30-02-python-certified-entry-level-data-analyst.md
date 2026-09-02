---
exam_code: PCED-30-02
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pced-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# PCED-30-02 Certified Entry-Level Data Analyst with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Validate this guide against the [official PCED syllabus](https://pythoninstitute.org/pced-exam-syllabus), checked September 2, 2026.

**Current baseline:** PCED-30-02, active since July 15, 2025; syllabus last updated July 14, 2025; PCED-30-01 retired July 14, 2025<br>
**Upcoming blueprint change:** none announced on the live credential or syllabus pages<br>
**Official delivery snapshot:** 40 questions; 60 minutes plus NDA; 75%; single-/multiple-select and scenarios; TestNow; English and Spanish<br>
**Credential snapshot:** no formal prerequisite; PCEP-equivalent Python plus basic mathematics/statistics recommended; seven-year validity; exam from USD 69 when checked; seven-day retake wait<br>

## How to use this guide

Use one small, auditable dataset from collection through reporting. Keep the raw input immutable, record each transformation, validate assumptions, and reproduce every reported number from code. At this level, sound reasoning and clean Python matter more than tool breadth.

> **About related items:** A `Related item:` callout adds useful adjacent context, not an additional published objective.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| Data and analysis concepts | 9 | 22.5% | Classify data/source/storage/lifecycle choices and identify ethical risks |
| Python basics for analysis | 13 | 32.5% | Manipulate core collections, functions, flow, exceptions, modules, and NumPy |
| Working with and analyzing data | 13 | 32.5% | Read, clean, validate, summarize, filter, correlate, and inspect outliers |
| Communicating insights | 5 | 12.5% | Select/interpret visuals and produce an audience-aware evidence narrative |

## 1. Data and data-analysis concepts — 22.5%

Data are recorded observations; information is data organized with context; knowledge is interpretation usable for action. Quantitative data represent amounts or counts; qualitative data represent categories or qualities. Structured data follows an explicit schema, semi-structured data carries flexible structure such as JSON, and unstructured data lacks a simple tabular model.

Sources include surveys, interviews, observations, applications/logs, APIs, databases, web pages, and devices. Evaluate each for relevance, coverage, timeliness, accuracy, collection bias, consent, and permitted use. A large sample can still be systematically unrepresentative. Web accessibility does not imply permission to scrape or republish.

CSV is portable tabular text but has weak type/schema semantics; JSON represents nested structures; spreadsheets mix data, formulas, and presentation; relational databases enforce tables/relationships and support queries. Warehouses integrate governed analytical data; lakes retain varied data at scale. Metadata describes meaning, origin, schema, units, lineage, and quality.

The lifecycle runs through collection, storage, processing, analysis, reporting, archiving, and deletion. A mistake early in the chain can invalidate every later calculation. Lifecycle management supports quality, security, retention, reproducibility, and compliance.

Analysis examines data for a question; analytics describes the broader systematic decision practice; data science often adds engineering and predictive modeling. Descriptive asks what happened, diagnostic why, predictive what may happen, and prescriptive what action to take.

Ethical handling requires purpose limitation, transparency, appropriate consent/lawful basis, minimization, privacy, fairness, security, and accountability. GDPR, HIPAA, and CCPA apply under different jurisdictions and contexts; knowing a name is not enough to determine applicability. Anonymization aims to prevent re-identification; encryption protects data under a key but does not anonymize it.

> **Related item:** A data-protection impact assessment and organizational counsel translate general principles into a specific legal/compliance decision. This guide is not legal advice.

## 2. Python basics for analysis — 32.5%

Track both value and type. `type()` reports the current type; `isinstance()` supports ancestry-aware checks. Lists are ordered/mutable, tuples ordered/immutable, sets unique/unordered collections, dictionaries key/value mappings, and strings immutable text sequences. Use comprehensions for readable transformations, sets for membership/uniqueness, and dictionaries for grouping/counting/lookup.

Functions create reusable analysis steps. Distinguish positional, keyword, and default arguments; return a result instead of relying on printing. Local names normally hide global names. Avoid mutable global analysis state because it damages reproducibility.

Use comparison and Boolean expressions for explicit validation/filtering. `if` selects paths; `for` traverses observations; `while` repeats until state changes. `break`, `continue`, and loop `else` alter trace flow. Catch specific, expected exceptions such as conversion or file errors and record enough context to diagnose rejected rows.

Standard modules in scope include `math`, `random`, `statistics`, `collections`, `os`, `datetime`, and `csv`. NumPy is third-party: install it into a controlled environment, import conventionally, and understand arrays as homogeneous, vectorized numerical structures. Do not silently mix missing sentinels, strings, and numeric values.

## 3. Working with data and simple analyses — 32.5%

Use `with open(..., encoding="utf-8")` for text. The `csv` module handles quoting/newlines that manual splitting does not. Preserve raw data; write cleaned output separately. Check path existence only when it improves the workflow—existence can change between check and open, so still handle open failures.

Cleaning is a declared policy, not “make the errors disappear.” Identify missingness, invalid types/ranges, duplicates, inconsistent case/whitespace, and date/number formats. Record how many rows each rule changes or removes. Min-max normalization maps values relative to observed min/max and needs a policy when the range is zero.

Use `len`, `sum`, `min`, `max`, and `round`; `statistics.mean`, `median`, and `stdev`; `Counter` for frequencies; and NumPy arrays with `mean`, `median`, `std`, `sum`, `arange`, and `linspace`. Be explicit about population versus sample standard-deviation conventions: similarly named functions can use different default denominators.

EDA uses sorting, filtering, unique/frequency counts, correlation, and outlier review to discover questions and data problems. Correlation from `numpy.corrcoef()` measures linear association, not causation. A standard-deviation rule can flag candidates, but domain context determines whether a value is error, rare reality, or important signal.

> **Related item:** Fit transformations and thresholds on training data when building predictive systems; otherwise test information can leak into preparation. Formal ML workflows are beyond PCED but the habit prevents optimistic results.

## 4. Communicating insights — 12.5%

Use a line chart for ordered/time change, a bar chart for category comparison, and a pie chart only for a small part-to-whole view where angle comparison remains clear. Titles state the question or conclusion; axes, units, scales, labels, color, and source make the evidence interpretable. Truncated axes, inconsistent intervals, excessive categories, and decorative effects can mislead.

A concise narrative leads with the question and answer, shows the strongest evidence, acknowledges limitation/uncertainty, and closes with a proportionate recommendation. Adapt vocabulary and depth to the audience without changing facts. When challenged, trace a claim to the visual, metric, transformation, and source.

## Integrated lab

Analyze a public, non-sensitive CSV of service requests:

1. write a one-paragraph question and data dictionary;
2. preserve raw input and log source/date/license;
3. validate required fields, parse dates/numbers, and count rejected rows;
4. normalize categories, handle missing values under a stated rule, and de-duplicate by a defensible key;
5. compute grouped counts, mean/median/spread, conditional metrics, unique values, candidate outliers, and one correlation;
6. reproduce a selected metric with both built-ins and NumPy;
7. create a bar or line chart and a five-sentence evidence narrative;
8. document limitations, ethical risks, and what would change your conclusion.

## Original knowledge checks

1. Distinguish data, information, and knowledge.
2. Why can a large sample remain biased?
3. Compare CSV, JSON, database, warehouse, and lake.
4. How can a collection error affect the lifecycle?
5. Match descriptive, diagnostic, predictive, and prescriptive questions.
6. Why is encryption not anonymization?
7. When is a set preferable to a list?
8. Why should an analysis function return rather than only print?
9. Why catch specific exceptions while ingesting rows?
10. Why is manual comma splitting unsafe for CSV?
11. What policy is needed for a constant column under min-max scaling?
12. Why can standard-deviation results differ across libraries?
13. What does correlation not establish?
14. Why should an outlier not be deleted automatically?
15. What makes a chart misleading?
16. What chain should support every reported claim?

## Answers and reasoning

1. Recorded observations; organized/contextualized observations; interpreted understanding for action.
2. Size reduces random error but does not repair systematic under/overrepresentation.
3. Portable table text; nested semi-structured text; governed queryable tables; integrated analytical store; varied scalable raw/curated store.
4. It changes or biases the observations every downstream transformation summarizes.
5. What happened; why; what may happen; what action is suitable.
6. Decryption restores identifiable data to authorized key holders.
7. For uniqueness, set operations, or efficient membership where order/duplicates are not required.
8. A returned value can be composed, tested, and reused independently of presentation.
9. Recovery/rejection policy differs by failure, and broad catches can hide defects.
10. Quoted delimiters and embedded newlines are valid CSV.
11. Avoid division by zero and decide whether output should be zero, unchanged, missing, or excluded.
12. Sample versus population denominator and missing-data behavior may differ.
13. Causality or freedom from confounding/nonlinear effects.
14. It may be valid and important; use domain and provenance evidence.
15. Missing units/source, distorted scale, unsuitable form, clutter, or visual emphasis disproportionate to evidence.
16. Source → validation/cleaning → calculation → visual/table → statement.

## Readiness checklist

- [ ] I can classify sources, formats, lifecycle stages, analytics types, and ethical risks from a scenario.
- [ ] I can use every listed Python collection, flow construct, function/error concept, standard module, and NumPy operation.
- [ ] I preserve raw data and make cleaning/validation decisions explicit and countable.
- [ ] I can calculate and interpret aggregates, descriptive statistics, conditional metrics, frequencies, correlation, and candidate outliers.
- [ ] I can select and critique a visual and produce an evidence-backed audience-aware report.
- [ ] I completed the integrated lab with original code and data.

## Source and freshness notes

- [Official PCED syllabus](https://pythoninstitute.org/pced-exam-syllabus) controls all objectives and weights.
- [Official PCED page](https://pythoninstitute.org/pced) controls status, delivery, price, language, validity, retake, aligned learning, and practice availability.
- Technical references: [Python documentation](https://docs.python.org/3/), [NumPy user guide](https://numpy.org/doc/stable/user/), and applicable official regulator guidance for legal questions.

## Places to learn

This is not a complete list and is not intended to be consumed in full. Choose one foundation path, do the integrated lab, then use targeted documentation and practice to close gaps.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCED-30-02 syllabus](https://pythoninstitute.org/pced-exam-syllabus) | Free official blueprint | 2–3 hours |
| [Python for Data Analytics 101](https://pythoninstitute.org/pced) | Official aligned learning link | Verify availability; roughly 30–45 hours with labs |
| [Official PCED practice tests](https://ums.edube.org/) | Paid official practice | 4–7 hours with remediation |
| [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) | Free primary documentation | 4–8 hours |
| [Cisco Data Analytics Essentials](https://www.netacad.com/courses/data-analytics-essentials) | Free/account; broader than PCED | About 30 hours; verify current listing |
| [Python for Data Analysis, 3rd ed.](https://wesmckinney.com/book/) | Free web edition; broader and Pandas-heavy | Select 15–25 hours |
| [Kaggle: Python and Pandas micro-courses](https://www.kaggle.com/learn) | Free/account; practical | 8–12 hours plus project |

Vendor runtimes, prices, and access can change. Third-party analytics courses frequently emphasize Pandas while PCED emphasizes core Python and basic NumPy, so map selections back to this blueprint.
