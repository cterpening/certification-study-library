---
exam_code: PCAD-31-02
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcad-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# PCAD-31-02 Certified Associate Data Analyst with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Checked September 2, 2026. The [official PCAD syllabus](https://pythoninstitute.org/pcad-exam-syllabus) is authoritative.

**Current baseline:** PCAD-31-02, active since July 15, 2025; PCAD-31-01 retired July 14, 2025<br>
**Upcoming blueprint change:** none announced on the official pages<br>
**Official delivery snapshot:** 48 questions; 60 minutes plus NDA; 75%; single-/multiple-select and scenario items; TestNow; English<br>
**Credential snapshot:** no formal prerequisite; PCAP/PCED-equivalent and domain skills recommended; six-year validity; exam from USD 195 when checked; 15-day retake wait<br>

## How to use this guide

PCAD spans data governance, Python, SQL, statistics, Pandas/NumPy, introductory modeling, and communication. Build an auditable notebook/script repository around one dataset: raw/clean separation, data dictionary, validation report, parameterized SQL, reproducible transformations, tests, figures, and an executive summary.

> **About related items:** A `Related item:` callout supplies adjacent context that improves understanding. It is not extra blueprint scope.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| Acquisition and preprocessing | 14 | 29.2% | Defend source, storage, validation, cleaning, scaling, encoding, extraction, and split choices |
| Programming and database skills | 16 | 33.3% | Implement maintainable Python/OOP and secure SQL/database workflows |
| Statistical analysis | 4 | 8.3% | Interpret distributions, relationships, bootstrap results, and regression assumptions |
| Analysis and modeling | 9 | 18.8% | Manipulate Pandas/NumPy data and evaluate supervised models without leakage |
| Communication and visualization | 5 | 10.4% | Create clear Matplotlib/Seaborn evidence for technical and business audiences |

## 1. Data acquisition and preprocessing — 29.2%

Match surveys, interviews, observation, databases, APIs, files, and web extraction to the question and population. Sampling must represent the target, while collection must respect consent, privacy, license/terms, rate limits, and data minimization. PII anonymization is a risk-control process, not deletion of one obvious name field.

Integration requires common keys, units, granularity, time zones, schemas, and definitions. Assess warehouses, lakes, cloud stores, databases, and files by structure, scale, access, governance, cost, and workload—not popularity.

Profile missing values, duplicates, impossible ranges, category drift, type/format errors, and outliers before changing data. MCAR means missingness is independent of observed/unobserved values; MAR depends on observed data; MNAR depends on the missing value or unobserved cause. These mechanisms affect whether deletion or imputation is defensible.

Min-max scaling maps a range; z-score standardization centers by mean and scales by standard deviation. One-hot encoding avoids imposing order on nominal categories; label encoding can introduce artificial numeric order. Bucketization loses resolution. Fit transformations on training data and apply the learned parameters to validation/test data.

Validation checks type, range, allowed values, uniqueness, referential consistency, and cross-field rules. Keep failed records and reasons in a quarantine/report rather than silently discarding them.

Know CSV, JSON, XML, TXT, spreadsheet structure, and wide versus long layout. Extract through documented APIs where available; ethical scraping respects authorization, `robots.txt`, terms, rate limits, and source load. `requests` retrieves content and BeautifulSoup parses HTML, but neither grants permission.

> **Related item:** A schema contract and lineage record turn ad hoc cleaning into a repeatable data product. They are professional extensions of validation and integrity objectives.

## 2. Programming and database skills — 33.3%

Use functions with explicit inputs/outputs, exceptions that preserve context, and data structures chosen by access pattern. PEP 8 covers style; PEP 257 covers docstrings. Manage dependencies in an isolated environment with `pip`; pin/review versions for repeatability.

Model a record with a class only when behavior/invariants justify it. `__init__` establishes instance state; composition embeds collaborators; inheritance specializes a substitutable base; overriding supports polymorphism. `is` tests identity and `==` equality; implement `__eq__` consistently for value objects. Double-underscore name mangling is not security.

SQL logical intent matters more than clause memorization. `SELECT` chooses expressions, `FROM` sources rows, `JOIN` combines them, `WHERE` filters rows, `GROUP BY` forms groups, `HAVING` filters groups, `ORDER BY` sorts, and `LIMIT` restricts output. Inner joins retain matches; left/right/full outer joins retain unmatched rows from designated sides. Aggregation grain must match the analytical question.

CRUD maps to `INSERT`, `SELECT`, `UPDATE`, and `DELETE`. Connect through `sqlite3` or an appropriate driver; use transactions and close/rollback safely. Always parameterize values through the driver's placeholder mechanism. Parameterization prevents values from becoming SQL syntax; it does not make dynamically chosen table/column identifiers safe.

Map SQL/Python types deliberately, especially null/`None`, decimals, booleans, dates, and time zones. Do not assume an engine or driver preserves every representation automatically.

## 3. Statistical analysis — 8.3%

Mean, median, and mode describe center; range, variance, standard deviation, and quantiles describe spread/position. Gaussian and uniform distributions make different shape assumptions. Univariate, bivariate, and multivariate views answer different questions.

Pearson's `r` summarizes linear association from -1 through +1. It is sensitive to outliers and does not establish causation. Use histograms for distributions, boxplots for robust distribution summaries/candidate outliers, scatterplots for paired numeric relationships, lines for ordered change, and heatmaps for many pairwise correlations.

Bootstrapping repeatedly samples with replacement from observed data to approximate a statistic's sampling distribution. The resampling unit must preserve the study structure; it does not cure biased/nonrepresentative source data.

Linear regression models a continuous response under assumptions including functional form and error behavior; logistic regression models class probability/log-odds for a categorical target. Interpret coefficients in the model's scale, validate on held-out data, examine assumptions and uncertainty, and avoid causal claims from predictive fit alone.

## 4. Data analysis and modeling — 18.8%

A Pandas `Series` is a labeled one-dimensional array; a `DataFrame` is a two-dimensional labeled table built from aligned columns/Series. `.loc` selects by labels and `.iloc` by integer positions. Boolean masks filter; assignment should be explicit enough to avoid ambiguous chained operations.

Use `merge`/`join` with known key uniqueness and validate row counts to detect accidental many-to-many expansion. Pivot changes shape around unique index/column pairs; pivot tables aggregate duplicates; melt converts wide to long. `groupby()` uses split-apply-combine; crosstabs summarize category combinations.

NumPy arrays support vectorized arithmetic, aggregation, and broadcasting. Broadcasting aligns compatible trailing dimensions; verify shape before trusting an output. Distinguish Python lists, NumPy ndarrays, Series, and DataFrames by typing, labels, dimensionality, missing-value behavior, and operation semantics.

Split train/test data before fitting preprocessors. Underfitting reflects excessive bias/insufficient capacity; overfitting reflects excessive sensitivity/variance. Report an appropriate held-out metric and baseline, not training accuracy alone. Linear/logistic regression have different target/assumption boundaries.

> **Related item:** Cross-validation gives a more stable development estimate, but a final untouched test set still protects the last evaluation from iterative tuning.

## 5. Communication and visualization — 10.4%

Use Matplotlib for explicit figure/axes control and Seaborn for statistical plots with data-aware defaults. Select plots from variable types and question. Label title, axes, units, categories, time range, source, and uncertainty; annotate sparingly. Accessible color and direct labels should not make meaning depend on hue alone.

Tailor depth and vocabulary, never the underlying evidence. Summaries should state question, result, magnitude/context, limitation, and recommendation. Distinguish observation, interpretation, and action.

## Integrated labs

1. Acquire a permitted API/file dataset and document population, sampling, fields, license, and ethical constraints.
2. Profile and classify missingness, errors, duplicates, category drift, outliers, and integrity failures.
3. Implement a fit/transform cleaner with train-only scaling/encoding parameters.
4. Store normalized records in SQLite and answer five questions with parameterized joins, grouping, HAVING, ordering, and limits.
5. Model an exporter family using composition/inheritance and test equality/identity behavior.
6. Bootstrap a median or difference, visualize the sampling distribution, and state what the interval cannot prove.
7. Fit one linear and one logistic example; compare baseline/train/test behavior and diagnose bias/variance risks.
8. Recreate each Pandas reshape/group result with a small hand-worked table.
9. Publish a technical appendix and one-page stakeholder brief whose claims trace to calculations.

## Original knowledge checks

1. Why can joining two nonunique keys multiply rows?
2. How do MCAR, MAR, and MNAR differ?
3. When is one-hot encoding preferable to labels?
4. Why fit scaling after the train/test split?
5. Contrast type, range, and cross-field validation.
6. Why does public HTML not imply permission to scrape?
7. Contrast object identity and equality.
8. Why do parameterized values not solve dynamic-identifier injection?
9. What does HAVING filter that WHERE does not?
10. How should SQL null map into Python reasoning?
11. What does Pearson correlation measure and not measure?
12. Why can bootstrap precision be misleading?
13. When choose logistic rather than linear regression?
14. Contrast `.loc` and `.iloc`.
15. How do pivot and pivot table differ with duplicate pairs?
16. What is a broadcasting compatibility question?
17. Contrast overfitting and underfitting.
18. What five components make a defensible executive finding?

## Answers and reasoning

1. Every matching row on one side combines with every match on the other.
2. Independent missingness; dependence on observed values; dependence on missing/unobserved values.
3. For nominal categories where numeric order would be false.
4. Fitting on all data leaks test-distribution information into training.
5. Representation/class, permitted interval/set, and relationship among fields.
6. Authorization, terms, copyright, privacy, and load constraints remain.
7. Same object versus equivalent value.
8. Placeholders represent data values; identifiers require allow-listing/controlled query construction.
9. Groups after aggregation rather than source rows before grouping.
10. As missing/unknown, normally `None`, with explicit downstream policy rather than a numeric zero or empty text.
11. Direction/strength of linear association, not causation.
12. It quantifies resampling variability from the observed sample but does not fix selection bias.
13. For a categorical/binary target where class probability is modeled.
14. Label-based versus integer-position indexing.
15. Pivot requires unique index/column pairs; pivot table can aggregate duplicates.
16. Whether trailing dimensions are equal or one so vectorized alignment is defined.
17. Excess variance/sensitivity to training data versus excess bias/insufficient pattern capture.
18. Question, result, magnitude/context, limitation, and proportionate recommendation.

## Readiness checklist

- [ ] I can defend collection, integration, storage, cleaning, encoding, validation, and split decisions.
- [ ] I can implement clear Python/OOP modules and secure parameterized transactional SQL.
- [ ] I can explain distributions, correlation, bootstrap, and both regression families with limitations.
- [ ] I can merge, reshape, index, group, vectorize, and validate Pandas/NumPy results.
- [ ] I can identify leakage, overfitting, underfitting, and inappropriate metrics.
- [ ] I can create accessible evidence-backed visual/report outputs for two audiences.
- [ ] I completed the labs with a permitted dataset and reproducible code.

## Source and freshness notes

- [Official PCAD syllabus](https://pythoninstitute.org/pcad-exam-syllabus) controls objectives and weights.
- [Official PCAD page](https://pythoninstitute.org/pcad) controls current delivery/status and official learning/practice references.
- Use [Python](https://docs.python.org/3/), [Pandas](https://pandas.pydata.org/docs/), [NumPy](https://numpy.org/doc/stable/), [Matplotlib](https://matplotlib.org/stable/), [Seaborn](https://seaborn.pydata.org/), and your SQL driver's current primary documentation for behavior.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose a coherent data-analysis path, then spend most study time on a reproducible end-to-end project.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCAD-31-02 syllabus](https://pythoninstitute.org/pcad-exam-syllabus) | Free official blueprint | 3–5 hours |
| [Cisco recommended sequence](https://pythoninstitute.org/pcad) | Official page links Intro to Data Science, Data Science Essentials with Python, and selected Data Analytics Essentials modules | Roughly 45–70 hours; verify catalog |
| [Official PCAD practice tests](https://ums.edube.org/) | Paid official practice | 5–8 hours with remediation |
| [Python for Data Analysis, 3rd ed.](https://wesmckinney.com/book/) | Free author-hosted web edition | 25–40 selected hours |
| [Pandas getting started](https://pandas.pydata.org/docs/getting_started/) | Free primary docs | 8–15 hours with exercises |
| [Introduction to Statistical Learning, Python edition](https://www.statlearning.com/) | Free official book PDF/site; broader modeling | Select 20–35 hours |
| [Kaggle Learn](https://www.kaggle.com/learn) | Free/account; Python, Pandas, visualization, SQL, intro ML | 20–35 hours plus project |

Course availability, prices, and runtimes are volatile. Avoid any product marketing recalled exam questions; use explanation-led assessments and original datasets.
