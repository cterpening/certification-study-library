---
exam_code: PCAD-31-02
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcad-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# PCAD-31-02 Certified Associate Data Analyst with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Deep-reviewed September 29, 2026; original numerical/SQL/extraction workbook executed, Pandas/plotting companion prepared only. The [official PCAD syllabus](https://pythoninstitute.org/pcad-exam-syllabus) is authoritative.

**Current baseline:** PCAD-31-02, active since July 15, 2025; PCAD-31-01 retired July 14, 2025<br>
**Upcoming blueprint change:** none found in the reviewed public syllabus/exam sections; direct objective monitoring timed out, so the existing snapshot was compared manually and retained<br>
**Official delivery snapshot:** 48 questions; 60 minutes plus NDA; 75% cumulative passing score; single-/multiple-select and scenario items; TestNow; English<br>
**Credential snapshot:** no formal prerequisite; PCAP/PCED-equivalent and domain skills recommended; six-year validity; USD 195 exam, USD 225 with retake, USD 215 with practice, USD 245 with both when checked; 15-day wait after a failed attempt<br>

**VERIFY CURRENT:** The [exam page](https://pythoninstitute.org/pcad), [testing policies](https://pythoninstitute.org/pcad-testing-policies), [standalone practice kit](https://ums.edube.org/products/1-pi-pcad-3102-pt) and [exam/retake/practice bundle](https://ums.edube.org/products/1-pi-pcad-3102-erpt) describe different products and procedures. The USD 49 standalone kit lists two tests with up to **10 launches each**; the USD 245 bundle lists **five each**. Both list 12-month voucher validity. The store says Test Candidate → Practice while the credential FAQ says Learner; confirm the profile and exact entitlement before redemption. Local testing-partner rescheduling generally requires 24 hours; the global unredeemed-voucher route has different scheduling rules. No account, booking, purchase, system test or private practice questions were accessed.

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

The snapshot contains **48 numbered objectives**, grouped 14/16/4/9/5. The official table assigns at most one point to each of 48 items. Its Block 4 section heading says seven objectives/items, while the table, nine numbered objectives and minimum-qualified-candidate profile say nine/18.8%. This guide preserves all nine and records the publisher's internal wording conflict. Rounded block weights total 100.1%; they are not separate pass thresholds. All numbered objectives were read; part of the Block 2 candidate-profile prose and the full PDF remain unverified.

## 1. Data acquisition and preprocessing — 29.2%

Match surveys, interviews, observation, databases, APIs, files, and web extraction to the question and population. Sampling must represent the target, while collection must respect consent, privacy, license/terms, rate limits, and data minimization. PII anonymization is a risk-control process, not deletion of one obvious name field.

Integration requires common keys, units, granularity, time zones, schemas, and definitions. Assess warehouses, lakes, cloud stores, databases, and files by structure, scale, access, governance, cost, and workload—not popularity.

Profile missing values, duplicates, impossible ranges, category drift, type/format errors, and outliers before changing data. MCAR means missingness is independent of observed/unobserved values; MAR means missingness no longer depends on the missing values after conditioning on observed information; MNAR retains dependence on unobserved information. These mechanisms affect whether deletion or imputation is defensible.

Min-max scaling maps a range; z-score standardization centers by mean and scales by standard deviation. One-hot encoding avoids imposing order on nominal categories; label encoding can introduce artificial numeric order. Bucketization loses resolution. Fit transformations on training data and apply the learned parameters to validation/test data.

Validation checks type, range, allowed values, uniqueness, referential consistency, and cross-field rules. Keep failed records and reasons in a quarantine/report rather than silently discarding them.

Know CSV, JSON, XML, TXT, spreadsheet structure, and wide versus long layout. Extract through documented APIs where available; ethical scraping respects authorization, `robots.txt`, terms, rate limits, and source load. `requests` retrieves content and BeautifulSoup parses HTML, but neither grants permission.

> **Related item:** A schema contract and lineage record turn ad hoc cleaning into a repeatable data product. They are professional extensions of validation and integrity objectives.

### Worked preprocessing and acquisition decisions

State the unit of observation first: one reading, order or person is a different grain from a monthly total. Join only after documenting keys, units, timezone and aggregation rules. Keep immutable raw input and record source, collection time, license/permission, schema version, validation decisions and output hash. A public URL does not establish sampling quality or permission. Anonymization must consider combinations of fields and re-identification, not just names.

For missingness, distinguish a proposed mechanism from a proven finding. An original teaching scenario might lose readings through random equipment failure, through an observed station's reporting process, or because high readings are deliberately withheld. These suggest MCAR, MAR and MNAR assumptions respectively; a table of blanks cannot distinguish MAR from MNAR on its own. The author's [identification discussion](https://stefvanbuuren.name/fimd/sec-idconcepts.html) explains this limit. Simple median filling below is a preprocessing exercise, not evidence that uncertainty or missingness bias has been resolved. Never impute a missing target merely to score a classifier.

The workbook fits on `[0, 2, missing, 6]`: observed median 2, filled training mean 2.5, population SD approximately 2.17945, minimum 0 and range 6. Held-out values `[8, missing]` become `[8, 2]`, then min-max values `[1.33333, 0.33333]`. Values outside the training range legitimately fall outside `[0,1]`. Training-only North/South one-hot columns encode unseen West as all zeros **plus an explicit unknown flag/report**. Constant vectors use divisor one; empty/all-missing/infinite training inputs are rejected. Different production policies require explicit justification.

For spreadsheets, use one header row, one variable per column and one observation per row. Keep identifier text, units and missing-value definitions in a dictionary; avoid merged cells, mixed subtotals and meaning encoded only by color. Separate raw, derived and presentation sheets. Check formulas across the intended rows, use references deliberately, audit hidden/filter-excluded rows, and preserve an export with types and dates verified. A CSV is a text interchange format: it does not preserve formulas, multiple sheets or formatting. No spreadsheet application was executed in this review.

The exact original HTML/JSON exercise uses only a temporary loopback server. Requests checks status independently of JSON decoding and sets timeouts; Beautiful Soup extracts nested text with an explicit separator and handles absent elements. A timeout is not a total-download deadline. Real acquisition additionally needs pagination, rate-limit handling, schema drift, authorization and source-load controls; none is demonstrated by this tiny local server. See [Requests](https://requests.readthedocs.io/en/latest/user/quickstart/) and the selected [Beautiful Soup contract](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## 2. Programming and database skills — 33.3%

Use functions with explicit inputs/outputs, exceptions that preserve context, and data structures chosen by access pattern. PEP 8 covers style; PEP 257 covers docstrings. Manage dependencies in an isolated environment with `pip`; pin/review versions for repeatability.

Model a record with a class only when behavior/invariants justify it. `__init__` establishes instance state; composition embeds collaborators; inheritance specializes a substitutable base; overriding supports polymorphism. `is` tests identity and `==` equality; implement `__eq__` consistently for value objects. Double-underscore name mangling is not security.

SQL logical intent matters more than clause memorization. `SELECT` chooses expressions, `FROM` sources rows, `JOIN` combines them, `WHERE` filters rows, `GROUP BY` forms groups, `HAVING` filters groups, `ORDER BY` sorts, and `LIMIT` restricts output. Inner joins retain matches; left/right/full outer joins retain unmatched rows from designated sides. Aggregation grain must match the analytical question.

CRUD maps to `INSERT`, `SELECT`, `UPDATE`, and `DELETE`. Connect through `sqlite3` or an appropriate driver; use transactions and close/rollback safely. Always parameterize values through the driver's placeholder mechanism. Parameterization prevents values from becoming SQL syntax; it does not make dynamically chosen table/column identifiers safe.

Map SQL/Python types deliberately, especially null/`None`, decimals, booleans, dates, and time zones. Do not assume an engine or driver preserves every representation automatically.

### Worked database and object boundaries

The original CSV has five records: North units 10/missing, South units 30/50, and a missing region with units 20. With a North/South/West dimension, observation-to-dimension inner/left/right/full joins produce **4/5/5/6 rows** on the tested SQLite 3.50.4. Do not assume every SQL engine/version supports identical syntax. Two rows sharing a key joined to three rows sharing that key yield six combinations; unexpected row multiplication is a grain problem, not a reason to delete arbitrary results.

| Region | Records, `COUNT(*)` | Measured values, `COUNT(units)` | Mean units |
|---|---:|---:|---:|
| North | 2 | 1 | 10 |
| South | 2 | 2 | 40 |
| Missing category | 1 | 1 | 20 |

An outer join's `ON` condition chooses matches before unmatched rows are padded. A later `WHERE units > 25` removes those padded rows because the predicate is unknown for NULL. To retain every region, put the qualifying observation condition in `ON` and count `o.id`; `COUNT(*)` still counts the padded West row. SQL `NULL = NULL` is unknown, while `IS NULL` tests missingness. Empty SQL `AVG`/`SUM` are NULL, not evidence of zero activity. See the selected [SELECT](https://www.sqlite.org/lang_select.html) and [aggregate](https://www.sqlite.org/lang_aggfunc.html) documentation.

The Python 3.13 example connects with `autocommit=True`, enables and verifies [foreign keys](https://www.sqlite.org/foreignkeys.html), then selects `autocommit=False`. Changing that PRAGMA inside an open transaction is ineffective. `with con` commits/rolls back but does **not** close the connection; outer `contextlib.closing` owns it. A transaction that first inserts a valid record and then an invalid foreign key must leave neither record committed. The workbook verifies this and parameterized CRUD, a bound hostile-looking string, and an allowlist for identifiers. Placeholders cannot substitute table/column names. See [sqlite3](https://docs.python.org/3.13/library/sqlite3.html) and [closing](https://docs.python.org/3.13/library/contextlib.html).

Ordinary SQLite columns have [type affinity](https://www.sqlite.org/datatype3.html), not universal strict type enforcement: the demonstrated INTEGER column stores `'001'` as integer 1 and `'unparsed'` as text. Validate identifiers before coercion; preserve fixed-width IDs as text where appropriate. NULL maps to `None`, booleans bind as integers, and dates/time zones need an explicit application convention. STRICT tables are an available SQLite feature, not used by this example.

The exporter example composes a caller-owned sink, subclasses an exporter and overrides `export`. Two equal `Record(7)` instances are distinct objects; an alias shares mutations. `__eq__` returns `NotImplemented` for unsupported types, and the mutable value object remains unhashable. `__init__` initializes an already-created instance and must return `None`. Read the selected [data-model contracts](https://docs.python.org/3.13/reference/datamodel.html), [PEP 8](https://peps.python.org/pep-0008/) and [PEP 257](https://peps.python.org/pep-0257/). Selected lint passing is not complete PEP conformance or correctness proof. No dependency installation or environment modification was performed.

## 3. Statistical analysis — 8.3%

Mean, median, and mode describe center; range, variance, standard deviation, and quantiles describe spread/position. Gaussian and uniform distributions make different shape assumptions. Univariate, bivariate, and multivariate views answer different questions.

Pearson's `r` summarizes linear association from -1 through +1. It is sensitive to outliers and does not establish causation. Use histograms for distributions, boxplots for robust distribution summaries/candidate outliers, scatterplots for paired numeric relationships, lines for ordered change, and heatmaps for many pairwise correlations.

Bootstrapping repeatedly samples with replacement from observed data to approximate a statistic's sampling distribution. The resampling unit must preserve the study structure; it does not cure biased/nonrepresentative source data.

Linear regression models a continuous response under assumptions including functional form and error behavior; logistic regression models class probability/log-odds for a categorical target. Interpret coefficients in the model's scale, validate on held-out data, examine assumptions and uncertainty, and avoid causal claims from predictive fit alone.

### Worked inference and model interpretation

The six original values 10/14/18/22/26/30 have mean and median 20. With 2,000 seeded resamples, the **95% percentile bootstrap interval** for their mean is approximately **[14.6667, 25.3333]** on the recorded runtime. Endpoints are the 0.025/0.975 quantiles using NumPy's explicit `linear` method. A seed aids repeatability within a recorded environment; NumPy's Generator does not promise an unchanged stream across versions. This interval describes a resampling procedure under assumptions, not a 95% posterior probability that a fixed population mean is inside this particular interval, nor repair for biased sampling.

Pairs must be resampled together for paired measurements. A deliberately artificial paired example adds exactly three to every baseline value; every paired mean difference and both percentile endpoints are three. This degenerate result describes the constructed sample, not certain generalization. Independent rows, clustered/repeated records and time series need different resampling units or methods. SciPy's default BCa method differs from the explicitly chosen percentile method, and degenerate BCa cases can warn or produce NaNs. See [bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html), [quantiles](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html) and [Generator](https://numpy.org/doc/stable/reference/random/generator.html).

Population variance divides by N; the usual sample variance divides by N−1. Its familiar unbiasedness result depends on sampling assumptions and does not make sample SD unbiased. A Gaussian model is symmetric and unbounded; a continuous uniform model has constant density on a specified finite interval. Neither is established by a small histogram. Pearson correlation measures linear association: the workbook's symmetric x and x² have zero Pearson correlation despite a deterministic relationship. Inspect outliers and nonlinear structure; do not automatically delete a valid extreme observation.

For linear regression, the workbook uses six training and two predeclared held-out records. It checks rank and the residual normal equations, then compares test MAE **0.42857** with a training-mean baseline MAE **7.66667**. Predicted test responses are **12.33333 and 14.19048** versus observed **13 and 14**. Training MAE is **0.57143**. An empty `lstsq` residual array may indicate an underdetermined/rank-deficient design; calculate residuals explicitly and inspect rank. Coefficients here use standardized predictors, so the intercept refers to the training mean predictor and the slope to one training SD. See [least squares](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html).

For binary logistic regression, a separate eight-record fixture uses stable `logaddexp` loss, SciPy's sigmoid and BFGS with an analytic gradient checked against finite differences. The chosen slope penalty is 0.2; the intercept is unpenalized. Four fixed held-out probabilities are approximately **0.30624, 0.43227, 0.56773, 0.69376**. Threshold 0.5 produces TP=2, TN=2, FP=0, FN=0: test accuracy 1.0 versus a fixed training-majority/tie-to-zero baseline 0.5; training accuracy is 0.75. These tiny constructed results do **not** show real-world performance or a justified optimum threshold. A one-unit log-odds coefficient corresponds to multiplicative odds, not a constant probability increase. See [minimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) and [expit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.expit.html).

Check linear functional form and residual structure, dependence between observations, influential points and collinearity. Error-variance/normality assumptions matter especially for classical intervals and tests; prediction fit alone establishes none of them. Logistic models require appropriate binary targets, a defensible log-odds form and attention to separation, calibration and sampling. Compare MAE/RMSE for continuous responses and confusion-matrix metrics for classification; accuracy can conceal class imbalance. No causal interpretation or real population inference is established by these synthetic examples.

## 4. Data analysis and modeling — 18.8%

A Pandas `Series` is a labeled one-dimensional array; a `DataFrame` is a two-dimensional labeled table built from aligned columns/Series. `.loc` selects by labels and `.iloc` by integer positions. Boolean masks filter; use a single `.loc[mask, column] = value` assignment when updating a DataFrame. In Pandas 3, Copy-on-Write is the default and only mode: chained assignment cannot update the parent, and mutating a selected Series does not update it.

Use `merge`/`join` with known key uniqueness and validate row counts to detect accidental many-to-many expansion. Pivot changes shape around unique index/column pairs; pivot tables aggregate duplicates; melt converts wide to long. `groupby()` uses split-apply-combine; crosstabs summarize category combinations.

NumPy arrays support vectorized arithmetic, aggregation, and broadcasting. Broadcasting aligns compatible trailing dimensions; verify shape before trusting an output. Distinguish Python lists, NumPy ndarrays, Series, and DataFrames by typing, labels, dimensionality, missing-value behavior, and operation semantics.

Split train/test data before fitting preprocessors. Underfitting reflects excessive bias/insufficient capacity; overfitting reflects excessive sensitivity/variance. Report an appropriate held-out metric and baseline, not training accuracy alone. Linear/logistic regression have different target/assumption boundaries.

> **Related item:** Cross-validation gives a more stable development estimate, but a final untouched test set still protects the last evaluation from iterative tuning.

### Pandas semantics and leakage checks

The documentation currently identifies **Pandas 3.0.6**, **NumPy 2.5**, **Matplotlib 3.11.2** and **Seaborn 0.13.2**. These are observed documentation versions, not a claim that the exam requires those exact versions. The prepared companion targets Pandas 3 [Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html); it was compiled/linted but **not executed**. Pandas, scikit-learn, Matplotlib, Seaborn and openpyxl were absent from this environment and were not installed.

| Operation | Contract to verify in the companion |
|---|---|
| [CSV ingestion](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) | Explicit nullable types and per-column missing markers; `keep_default_na=False` prevents unrelated default strings from silently becoming missing |
| [Indexing](https://pandas.pydata.org/docs/user_guide/indexing.html) | `.loc[1:3]` includes labels 1/2/3; `.iloc[1:3]` selects positions 1/2; scalar out-of-range errors differ from clipped slices |
| [Missing values](https://pandas.pydata.org/docs/user_guide/missing_data.html) | `isna` identifies missingness; `pd.NA` cannot be treated as a normal Boolean; zero is a measured value, not a generic fill |
| [Merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) | `validate='many_to_one'` rejects duplicate dimension keys; `indicator=True` exposes unmatched rows; Pandas missing keys match each other, unlike SQL `=` joins |
| [Grouping](https://pandas.pydata.org/docs/user_guide/groupby.html) | `dropna=False` keeps the missing-region group; `size` counts rows while `count` counts observed values; set `observed` explicitly for categorical grouping |
| [Reshaping](https://pandas.pydata.org/docs/user_guide/reshaping.html) | `pivot` rejects duplicate coordinates; `pivot_table` requires a chosen aggregation; `melt` expands measured columns into variable/value rows |
| [Crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html) | Frequency versus normalized proportions answers different questions; include and name missing categories deliberately |
| [Standard deviation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html) | Pandas defaults to `ddof=1` and skips missing measures; NumPy defaults to `ddof=0` and requires explicit missing-value handling |

Series align by labels when building tables or operating together; NumPy arrays align by position and compatible shape. [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) compares trailing dimensions: each must be equal or one. A 2×3 matrix plus a length-3 vector works; adding a length-2 vector fails. Adding a 3×1 and a length-2 array yields a 3×2 result, which may be valid but unintended. Check the intended row/column meaning and memory cost of the output.

The [scikit-learn pitfalls chapter](https://scikit-learn.org/stable/common_pitfalls.html) supports splitting before fitting imputation, scaling, feature selection or dimensionality reduction. For cross-validation, fit every learned preprocessing step separately inside each training fold; a pipeline helps enforce that boundary. Repeatedly choosing models using final test results turns that test set into development data. Grouped/time-dependent samples need a split that respects dependence and deployment order. These concepts were reviewed from current primary docs; scikit-learn itself was not executed. A high training score with poor validation performance suggests overfitting, while poor performance on both can suggest underfitting; neither diagnosis follows from one number without context.

## 5. Communication and visualization — 10.4%

Use Matplotlib for explicit figure/axes control and Seaborn for statistical plots with data-aware defaults. Select plots from variable types and question. Label title, axes, units, categories, time range, source, and uncertainty; annotate sparingly. Accessible color and direct labels should not make meaning depend on hue alone.

Tailor depth and vocabulary, never the underlying evidence. Summaries should state question, result, magnitude/context, limitation, and recommendation. Distinguish observation, interpretation, and action.

### A traceable stakeholder finding

For the five-record operational fixture, North has two records but only one measured value, so its mean is 10 units; South has two measured values and mean 40 units. The missing-region observation contributes another 20 units. The observed total is 110 across four measured records, overall observed mean 27.5, with one missing measure. A defensible brief says: **“In five synthetic teaching records, South's observed mean is 40 units versus North's 10; North has one missing measurement. Check the missing record and collection process before interpreting the difference.”** This is a descriptive example, not a station-performance ranking.

For an analyst, provide the raw CSV/hash, dictionary, count-versus-size table, SQL/Pandas missing-key distinction and reproducible script. For an executive, lead with the comparison, amount of missing evidence and proportionate next step. When challenged, trace the claim to its numerator, denominator, exclusions and units; correct errors openly rather than changing the evidence for the audience.

Use histograms for distributions, scatterplots for paired measurements, lines for an ordered quantity such as time, and bars for category comparisons. Record ID is not time. The prepared plot helper uses explicit Figure/Axes, labels, units, source and marker shape as well as hue; its histogram counts four observed values and acknowledges the missing fifth. It has **not** exported or visually validated a figure here. Seaborn can estimate summaries and uncertainty automatically, so inspect the chosen estimator and interval rather than treating every mark as a raw observation. See the selected [Matplotlib quickstart](https://matplotlib.org/stable/users/explain/quick_start.html) and complete [Seaborn introduction](https://seaborn.pydata.org/tutorial/introduction.html). Human and accessibility review remain pending.

## Original executable workbook

These original teaching fixtures cover a bounded part of the objectives. They are not actual exam items, real population data, a complete security test, or completion of the broader integrated labs. Save the two files below together. `analysis.py` uses the already-available Python 3.13.14, NumPy 2.5.2, SciPy 1.18.0, Requests 2.34.2, Beautiful Soup 4.13.3 and SQLite 3.50.4. It writes JSON to stdout, creates an in-memory database and stops its temporary loopback server in `finally`. No external dataset request, installation or persistent service is involved.

The first file passed **86 checks normally and 86 with optimization**, using `python -B -Werror analysis.py` and the additional `-O` flag; checks remain active in both modes. Selected Ruff rules `E4,E7,E9,F,W,E501` also pass for both files at a 79-character limit. Keep the JSON output with the exact source and package versions. Only run `pandas_companion.py NEW_OUTPUT_DIRECTORY` in a separately prepared environment with its required packages; its directory must not already exist. Syntax/lint checking does not verify Pandas results or rendered charts.

### analysis.py

```python
"""Run original PCAD numerical, database and local extraction exercises.

Use Python 3.13+ with NumPy, SciPy, Requests and Beautiful Soup already
available. This script uses synthetic data, an in-memory database and a
temporary loopback HTTP server; it writes one JSON report to stdout.
It does not install packages or contact an external data service.
"""

from contextlib import closing
from hashlib import sha256
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import StringIO
import csv
import json
import math
import platform
import sqlite3
from threading import Thread

import bs4
from bs4 import BeautifulSoup
import numpy as np
import requests
import scipy
from scipy.optimize import minimize
from scipy.special import expit
from scipy.stats import bootstrap


CHECKS = []
RAW = (
    "id,region,units\n1,North,10\n2,North,\n3,South,30\n"
    "4,South,50\n5,,20\n"
)


def check(condition, label):
    """Record a successful condition, including under Python -O."""
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def expect(error, operation, label):
    """Require the named exception; let unrelated failures propagate."""
    try:
        operation()
    except error:
        check(True, label)
    else:
        raise AssertionError(label)


class NumericTransform:
    """Learn median imputation and scaling from a nonempty training vector.

    NaN means missing; infinity is rejected. Constant training vectors use
    divisor one. Transform never fits again and returns new arrays.
    """

    def __init__(self, training):
        values = self._vector(training)
        observed = values[~np.isnan(values)]
        if not observed.size:
            raise ValueError("training needs observed values")
        self.median = float(np.median(observed))
        filled = np.where(np.isnan(values), self.median, values)
        self.mean = float(filled.mean())
        self.std = float(filled.std(ddof=0)) or 1.0
        self.minimum = float(filled.min())
        self.width = float(np.ptp(filled)) or 1.0

    @staticmethod
    def _vector(values):
        result = np.array(values, dtype=float, copy=True)
        if result.ndim != 1 or not result.size or np.isinf(result).any():
            raise ValueError("need nonempty one-dimensional finite/NaN data")
        return result

    def transform(self, values):
        """Return imputed, standardized and min-max transformed vectors."""
        raw = self._vector(values)
        filled = np.where(np.isnan(raw), self.median, raw)
        return (filled, (filled - self.mean) / self.std,
                (filled - self.minimum) / self.width)


def preprocessing():
    """Check training-only parameters, shapes and explicit unknowns."""
    train = np.array([0.0, 2.0, np.nan, 6.0])
    saved = train.copy()
    fitted = NumericTransform(train)
    frozen = vars(fitted).copy()
    imputed, standardized, scaled = fitted.transform(train)
    held = fitted.transform([8.0, np.nan])
    check(np.array_equal(train, saved, equal_nan=True), "raw unchanged")
    check(fitted.median == 2 and fitted.mean == 2.5, "training estimates")
    check(np.array_equal(imputed, [0, 2, 2, 6]), "median fill")
    check(abs(standardized.mean()) < 1e-12, "training centered")
    check(abs(standardized.std() - 1) < 1e-12, "population scaling")
    check(np.allclose(scaled, [0, 1 / 3, 1 / 3, 1]), "training min-max")
    check(np.allclose(held[2], [4 / 3, 1 / 3]), "test outside train range")
    check(vars(fitted) == frozen, "transform did not refit")
    check(held[0][1] == 2, "test missing uses train median")
    check(NumericTransform([4, 4]).transform([4])[1][0] == 0,
          "constant training policy")
    for bad in ([], [np.nan], [np.inf], [[1, 2]]):
        expect(ValueError, lambda bad=bad: NumericTransform(bad),
               "reject invalid fit " + repr(bad))
    expect(ValueError, lambda: fitted.transform([np.inf]),
           "reject infinite test value")
    categories = tuple(sorted(set(["North", "South", "North"])))
    test_categories = ["South", "West"]
    encoded = np.array([[int(v == c) for c in categories]
                        for v in test_categories])
    unknown = [v not in categories for v in test_categories]
    check(encoded.tolist() == [[0, 1], [0, 0]], "fixed one-hot vocabulary")
    check(unknown == [False, True], "unknown explicitly reported")
    matrix = np.arange(6).reshape(2, 3)
    check((matrix + [10, 20, 30]).tolist()
          == [[10, 21, 32], [13, 24, 35]], "trailing broadcast")
    expect(ValueError, lambda: matrix + np.ones(2), "incompatible shapes")
    check((np.arange(3)[:, None] + np.arange(2)).shape == (3, 2),
          "explicit outer broadcast")
    return {"parameters": frozen, "held_minmax": held[2].tolist(),
            "unknown_categories": ["West"]}


def database():
    """Verify join grain, SQL NULL, CRUD, value binding and rollback."""
    rows = []
    for row in csv.DictReader(StringIO(RAW)):
        rows.append((int(row["id"]), row["region"] or None,
                     int(row["units"]) if row["units"] else None))
    check(len(rows) == 5, "five original CSV records")
    check(rows[-1] == (5, None, 20), "missing category remains missing")
    with closing(sqlite3.connect(":memory:", autocommit=True)) as con:
        con.execute("PRAGMA foreign_keys = ON")
        check(con.execute("PRAGMA foreign_keys").fetchone() == (1,),
              "foreign keys enabled before transaction")
        con.autocommit = False
        with con:
            con.execute("CREATE TABLE region(name TEXT PRIMARY KEY)")
            con.execute("CREATE TABLE observation("
                        "id INTEGER PRIMARY KEY, region TEXT "
                        "REFERENCES region(name), units INTEGER "
                        "CHECK(units >= 0))")
            con.executemany("INSERT INTO region VALUES(?)",
                            [(v,) for v in ("North", "South", "West")])
            con.executemany("INSERT INTO observation VALUES(?,?,?)", rows)
        def q(sql, params=()):
            return con.execute(sql, params).fetchall()
        check(q("SELECT count(*) FROM observation") == [(5,)], "insert")
        group = q("SELECT region,count(*),count(units),avg(units) "
                  "FROM observation GROUP BY region ORDER BY region")
        check(group == [(None, 1, 1, 20.0), ("North", 2, 1, 10.0),
                        ("South", 2, 2, 40.0)], "NULL and group grain")
        check(q("SELECT region FROM observation WHERE units >= ? "
                "GROUP BY region HAVING count(*) >= ? "
                "ORDER BY region LIMIT ?", (25, 2, 1)) == [("South",)],
              "WHERE HAVING ORDER LIMIT")
        for join, count in (("INNER", 4), ("LEFT", 5), ("RIGHT", 5),
                            ("FULL", 6)):
            result = q(f"SELECT count(*) FROM observation o {join} JOIN "
                       "region r ON o.region=r.name")
            check(result == [(count,)], join + " join count")
        on = q("SELECT r.name,count(o.id),count(*) FROM region r "
               "LEFT JOIN observation o ON o.region=r.name AND o.units>25 "
               "GROUP BY r.name ORDER BY r.name")
        where = q("SELECT r.name,count(o.id) FROM region r "
                  "LEFT JOIN observation o ON o.region=r.name "
                  "WHERE o.units>25 GROUP BY r.name ORDER BY r.name")
        check(on == [("North", 0, 1), ("South", 2, 2), ("West", 0, 1)],
              "ON preserves unmatched regions; star counts padded row")
        check(where == [("South", 2)], "WHERE removes padded NULL rows")
        check(q("SELECT NULL = NULL, NULL IS NULL") == [(None, 1)],
              "SQL unknown versus IS NULL")
        check(q("SELECT avg(units),sum(units),count(units) "
                "FROM observation WHERE 0") == [(None, None, 0)],
              "empty aggregate is not zero mean")
        check(q("WITH a(k) AS (VALUES(1),(1)), "
                "b(k) AS (VALUES(1),(1),(1)) "
                "SELECT count(*) FROM a JOIN b ON a.k=b.k") == [(6,)],
              "two times three duplicate-key expansion")
        check(q("SELECT id FROM observation WHERE region=?",
                ("North' OR 1=1 --",)) == [], "hostile-looking value bound")
        check(q("SELECT ? FROM observation LIMIT 1", ("units",))
              == [("units",)], "placeholder is value not identifier")
        allowed = {"units": "units", "id": "id"}

        def projection(name):
            if name not in allowed:
                raise ValueError("unsupported column")
            return q(f"SELECT {allowed[name]} FROM observation ORDER BY id")

        check(projection("units")[0] == (10,), "allowlisted column")
        expect(ValueError, lambda: projection("units;DROP TABLE region"),
               "reject arbitrary identifier")
        with con:
            con.execute("UPDATE observation SET units=? WHERE id=?", (12, 1))
        check(q("SELECT units FROM observation WHERE id=1") == [(12,)],
              "update committed")
        with con:
            con.execute("UPDATE observation SET units=10 WHERE id=1")

        def bad_transaction():
            with con:
                con.execute("INSERT INTO observation VALUES(6,'North',1)")
                con.execute("INSERT INTO observation VALUES(7,'Unknown',1)")

        expect(sqlite3.IntegrityError, bad_transaction, "foreign key fails")
        check(q("SELECT count(*) FROM observation") == [(5,)],
              "whole transaction rolled back")
        with con:
            con.execute("INSERT INTO observation VALUES(8,'West',9)")
            con.execute("DELETE FROM observation WHERE id=?", (8,))
        check(q("SELECT count(*) FROM observation") == [(5,)], "delete")
        with con:
            con.execute("CREATE TABLE affinity(value INTEGER)")
            con.executemany("INSERT INTO affinity VALUES(?)",
                            [("001",), ("unparsed",)])
        check(q("SELECT value,typeof(value) FROM affinity ORDER BY rowid")
              == [(1, "integer"), ("unparsed", "text")],
              "ordinary SQLite affinity is not strict validation")
        check(q("SELECT typeof(?),typeof(?),typeof(?),typeof(?)",
                (None, True, 2.5, b"x"))
              == [("null", "integer", "real", "blob")], "bound types")
        check(q("SELECT 1") == [(1,)], "with con does not close")
    expect(sqlite3.ProgrammingError, lambda: con.execute("SELECT 1"),
           "outer closing owns connection")
    return {"raw_sha256": sha256(RAW.encode()).hexdigest(),
            "rows": rows, "groups": group, "outer_join_on": on}


def modeling():
    """Fit original toy regressions and evaluate fixed held-out examples."""
    train_ids, test_ids = set(range(6)), {6, 7}
    check(train_ids.isdisjoint(test_ids), "disjoint regression IDs")
    x = np.arange(6, dtype=float)
    y = np.array([1, 4, 4, 7, 8, 11], dtype=float)
    tx, ty = np.array([6., 7.]), np.array([13., 14.])
    transform = NumericTransform(x)
    design = np.column_stack([np.ones(x.size), transform.transform(x)[1]])
    test = np.column_stack([np.ones(tx.size), transform.transform(tx)[1]])
    beta, _, rank, singular = np.linalg.lstsq(design, y, rcond=None)
    check(rank == 2 and np.all(singular > 0), "linear full rank")
    residual = y - design @ beta
    check(np.allclose(design.T @ residual, 0, atol=1e-10),
          "least-squares normal equations")
    predictions = test @ beta
    mae = float(np.mean(np.abs(ty - predictions)))
    baseline = float(np.mean(np.abs(ty - y.mean())))
    check(mae < baseline, "linear held-out beats train-mean baseline")
    under = np.array([[1., 0., 0.], [0., 1., 0.]])
    _, residues, deficient_rank, _ = np.linalg.lstsq(under, [1, 2], rcond=None)
    check(residues.size == 0 and deficient_rank < under.shape[1],
          "empty residual array can mean underdetermined")
    lx = np.arange(-3, 5, dtype=float)
    ly = np.array([0, 0, 1, 0, 1, 0, 1, 1], dtype=float)
    lt, ltruth = np.array([-2.5, -.5, 1.5, 3.5]), np.array([0, 0, 1, 1])
    ltform = NumericTransform(lx)
    ld = np.column_stack([np.ones(lx.size), ltform.transform(lx)[1]])
    ltd = np.column_stack([np.ones(lt.size), ltform.transform(lt)[1]])
    penalty = .2

    def loss(b):
        z = ld @ b
        return float(np.mean(np.logaddexp(0, z) - ly * z)
                     + penalty * b[1] ** 2 / 2)

    def gradient(b):
        return ld.T @ (expit(ld @ b) - ly) / ly.size + [0, penalty * b[1]]

    probe, step = np.array([.2, -.3]), 1e-6
    numerical = np.array([
        (loss(probe + np.eye(2)[i] * step)
         - loss(probe - np.eye(2)[i] * step)) / (2 * step)
        for i in range(2)
    ])
    check(np.allclose(gradient(probe), numerical, atol=1e-8),
          "analytic logistic gradient versus finite difference")
    result = minimize(loss, np.zeros(2), jac=gradient, method="BFGS",
                      options={"gtol": 1e-8, "maxiter": 200})
    check(result.success, "logistic optimizer succeeded")
    check(np.isfinite(result.x).all() and result.fun < loss(np.zeros(2)),
          "finite optimized logistic objective improves")
    check(np.max(np.abs(result.jac)) < 1e-7, "logistic gradient small")
    probability = expit(ltd @ result.x)
    labels = (probability >= .5).astype(int)
    tp = int(np.sum((labels == 1) & (ltruth == 1)))
    tn = int(np.sum((labels == 0) & (ltruth == 0)))
    fp = int(np.sum((labels == 1) & (ltruth == 0)))
    fn = int(np.sum((labels == 0) & (ltruth == 1)))
    check(tp + tn + fp + fn == 4, "confusion matrix reconciles")
    check(np.all((probability > 0) & (probability < 1)), "probability bounds")
    check(np.all(np.diff(probability) > 0), "positive logistic slope")
    check(expit(-1000) == 0 and expit(1000) == 1, "stable extreme sigmoid")
    check(math.isfinite(loss([1000, 1000])), "stable extreme log loss")
    return {"linear_coefficients_standardized": beta.tolist(),
            "linear_test_predictions": predictions.tolist(),
            "linear_test_mae": mae, "linear_baseline_mae": baseline,
            "linear_train_mae": float(np.mean(np.abs(residual))),
            "logistic_coefficients_standardized": result.x.tolist(),
            "logistic_test_probabilities": probability.tolist(),
            "logistic_threshold": .5, "logistic_slope_penalty": penalty,
            "logistic_confusion": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
            "logistic_test_accuracy": float(np.mean(labels == ltruth)),
            "logistic_train_accuracy": float(np.mean(
                (expit(ld @ result.x) >= .5) == ly)),
            "logistic_baseline_accuracy": float(np.mean(ltruth == 0))}


def resampling():
    """Check a seeded percentile interval and paired resampling units."""
    values = np.array([10., 14., 18., 22., 26., 30.])

    def interval():
        return bootstrap((values,), np.mean, vectorized=True,
                         n_resamples=2000, method="percentile",
                         confidence_level=.95, rng=np.random.default_rng(731))

    first, second = interval(), interval()
    check(np.array_equal(first.bootstrap_distribution,
                         second.bootstrap_distribution), "same-run seed")
    check(first.bootstrap_distribution.shape == (2000,), "resample count")
    expected = np.quantile(first.bootstrap_distribution, [.025, .975],
                           method="linear")
    check(np.allclose(first.confidence_interval, expected),
          "percentile endpoints from explicit quantile method")
    check(np.isfinite(expected).all() and expected[0] <= expected[1],
          "finite ordered interval")
    before, after = values, values + 3

    def difference(a, b, axis=-1):
        return np.mean(b - a, axis=axis)

    paired = bootstrap((before, after), difference, paired=True,
                       vectorized=True, n_resamples=200, method="percentile",
                       rng=np.random.default_rng(49))
    check(np.all(paired.bootstrap_distribution == 3), "resample pairs")
    check(tuple(paired.confidence_interval) == (3, 3),
          "degenerate percentile interval is not universal certainty")
    check(float(values.mean()) == 20 and float(np.median(values)) == 20,
          "mean and median")
    check(np.isclose(values.var(ddof=1), values.var(ddof=0) * 6 / 5),
          "N versus N-1 variance")
    check(np.quantile([0, 10, 20, 30], .25, method="linear") == 7.5,
          "quantile method identified")
    symmetric = np.array([-2., -1., 0., 1., 2.])
    check(abs(np.corrcoef(symmetric, symmetric ** 2)[0, 1]) < 1e-12,
          "zero Pearson does not mean no relationship")
    return {"sample_mean": 20, "percentile_95_interval": expected.tolist(),
            "resamples": 2000, "seed": 731,
            "paired_percentile_interval": list(paired.confidence_interval)}


class Record:
    """Represent a simple mutable value object, intentionally unhashable."""

    def __init__(self, identifier):
        self.identifier = identifier

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.identifier == other.identifier


class Exporter:
    """Compose with a writable sink and export a scalar record."""

    def __init__(self, sink):
        self.sink = sink

    def export(self, record):
        """Write one line to the caller-owned sink."""
        self.sink.write(str(record.identifier) + "\n")


class JSONExporter(Exporter):
    """Override Exporter to write an original JSON line."""

    def export(self, record):
        """Write one JSON object to the caller-owned sink."""
        self.sink.write(json.dumps({"id": record.identifier}) + "\n")


def objects_and_extraction():
    """Use original loopback HTML/JSON with bounded resource ownership."""
    first, equal = Record(7), Record(7)
    alias = first
    check(first == equal and first is not equal, "equality versus identity")
    alias.identifier = 8
    check(first.identifier == 8 and equal.identifier == 7, "alias mutation")
    check(first.__eq__(8) is NotImplemented, "unsupported comparison")
    expect(TypeError, lambda: hash(first), "mutable value object unhashable")
    with StringIO() as sink:
        for exporter in (Exporter(sink), JSONExporter(sink)):
            exporter.export(equal)
        check(sink.getvalue() == '7\n{"id": 7}\n', "polymorphic exporters")
        check(not sink.closed, "caller owns composed sink")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            payloads = {
                "/rows": (200, "application/json", '{"units": [10, 30]}'),
                "/page": (200, "text/html; charset=utf-8",
                          '<p class="label">North <b>station</b></p>'),
                "/bad": (200, "application/json", "not-json"),
            }
            status, kind, body = payloads.get(
                self.path, (404, "application/json", '{"error":"missing"}'))
            data = body.encode()
            self.send_response(status)
            self.send_header("Content-Type", kind)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *_):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    worker = Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        with requests.Session() as session:
            session.trust_env = False
            base = f"http://127.0.0.1:{server.server_port}"

            def get(path):
                return session.get(base + path, timeout=(2, 2),
                                   allow_redirects=False)

            with get("/rows") as response:
                response.raise_for_status()
                payload = response.json()
                check(set(payload) == {"units"}, "JSON schema keys")
                check(all(type(v) is int and v >= 0 for v in payload["units"]),
                      "JSON field validation")
                check(sum(payload["units"]) == 40, "local API calculation")
            with get("/missing") as response:
                check(response.json() == {"error": "missing"},
                      "decodable JSON can be HTTP error")
                expect(requests.HTTPError, response.raise_for_status,
                       "HTTP status checked independently")
            with get("/bad") as response:
                expect(requests.exceptions.JSONDecodeError, response.json,
                       "malformed JSON rejected")
            with get("/page") as response:
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                label = soup.find("p", class_="label")
                check(label.get_text(" ", strip=True) == "North station",
                      "HTML nested text with explicit separator")
                check(soup.find("table") is None, "absent HTML element")
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=3)
    check(not worker.is_alive(), "temporary server stopped")
    return {"external_requests": 0, "persistent_services": 0}


def main():
    """Run every exercise and emit a traceable synthetic report."""
    report = {"synthetic_only": True,
              "versions": {"python": platform.python_version(),
                           "numpy": np.__version__, "scipy": scipy.__version__,
                           "sqlite": sqlite3.sqlite_version,
                           "requests": requests.__version__,
                           "beautifulsoup": bs4.__version__},
              "preprocessing": preprocessing(), "database": database(),
              "models": modeling(), "bootstrap": resampling(),
              "extraction": objects_and_extraction()}
    report["checks"] = CHECKS
    report["passed_checks"] = len(CHECKS)
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
```

### pandas_companion.py

```python
"""Exercise Pandas 3 contracts, then export original Matplotlib/Seaborn plots.

PREPARED ONLY: this companion was syntax/lint checked, not executed during
the review. Pandas, Matplotlib and Seaborn were unavailable. Save alongside
analysis.py. In an environment that already has those packages, run this
file with one NEW output-directory path. Existing paths are rejected.
"""

from io import StringIO
from pathlib import Path
import sys

import matplotlib
import numpy as np
import pandas as pd

from analysis import RAW, check, expect


def tables():
    """Return the table after explicit missingness and reshape checks."""
    if int(pd.__version__.split(".")[0]) < 3:
        raise RuntimeError("this companion targets Pandas 3 Copy-on-Write")
    frame = pd.read_csv(
        StringIO(RAW), dtype={"id": "Int64", "region": "string",
                              "units": "Int64"},
        keep_default_na=False, na_values={"region": [""], "units": [""]},
    ).set_index("id")
    check(frame.shape == (5, 2), "Pandas explicit CSV shape")
    check(frame["units"].isna().sum() == 1, "nullable missing measure")
    check(frame["region"].isna().sum() == 1, "nullable missing category")
    check(frame.loc[1:3].index.tolist() == [1, 2, 3], "loc inclusive labels")
    check(frame.iloc[1:3].index.tolist() == [2, 3], "iloc exclusive stop")
    expect(KeyError, lambda: frame.loc[999], "missing label")
    check(frame.iloc[:999].shape == frame.shape, "slice clips positions")
    expect(IndexError, lambda: frame.iloc[999], "scalar position bounds")
    view = frame["units"]
    view.iloc[0] = 99
    check(frame.loc[1, "units"] == 10, "CoW Series change isolates parent")
    frame.loc[frame["region"] == "North", "units"] = [12, pd.NA]
    check(frame.loc[1, "units"] == 12, "single loc assignment updates")
    frame.loc[1, "units"] = 10
    expect(TypeError, lambda: bool(pd.NA), "NA has ambiguous truth value")
    selected = frame.loc[(frame["units"] >= 20) & frame["region"].notna()]
    check(selected.index.tolist() == [3, 4], "parenthesized nullable mask")
    summary = frame.groupby("region", dropna=False, observed=True).agg(
        records=("units", "size"), observed=("units", "count"),
        mean=("units", "mean"),
    )
    check(summary["records"].sum() == 5, "group includes missing key")
    check(summary.loc["North", "records"] == 2, "group size")
    check(summary.loc["North", "observed"] == 1, "group count")
    check(summary.loc["South", "mean"] == 40, "group mean oracle")
    check(frame.groupby("region")["units"].size().sum() == 4,
          "default groupby omits NA keys")
    observed = frame["units"].dropna().to_numpy(dtype=float)
    check(np.isclose(frame["units"].std(), observed.std(ddof=1)),
          "Pandas sample standard deviation")
    check(not np.isclose(frame["units"].std(), observed.std(ddof=0)),
          "NumPy default divisor differs")
    dimension = pd.DataFrame({"region": ["North", "South", "West"],
                              "owner": ["N", "S", "W"]})
    joined = frame.reset_index().merge(dimension, on="region", how="left",
                                       validate="many_to_one", indicator=True)
    check(len(joined) == 5, "validated merge preserves five rows")
    check((joined["_merge"] == "left_only").sum() == 1,
          "merge indicator exposes missing category")
    duplicate_dimension = pd.concat([dimension, dimension.iloc[[0]]])
    expect(pd.errors.MergeError, lambda: frame.reset_index().merge(
        duplicate_dimension, on="region", validate="many_to_one"),
        "reject duplicate dimension key")
    missing_dimension = pd.DataFrame({"region": pd.Series([pd.NA],
                                                          dtype="string"),
                                      "owner": ["Missing"]})
    missing_match = frame.reset_index().merge(missing_dimension, on="region")
    check(missing_match["id"].tolist() == [5], "Pandas NA merge matches NA")
    shape = frame.assign(period=["p1", "p2", "p1", "p2", "p1"])
    wide = shape.pivot(index="region", columns="period", values="units")
    check(wide.loc["South", "p2"] == 50, "unique pivot oracle")
    duplicate_pair = pd.concat([shape, shape.iloc[[0]]])
    expect(ValueError, lambda: duplicate_pair.pivot(
        index="region", columns="period", values="units"),
        "pivot rejects duplicate coordinate")
    aggregate = duplicate_pair.pivot_table(
        index="region", columns="period", values="units", aggfunc="mean",
        observed=True,
    )
    check(aggregate.loc["North", "p1"] == 10, "pivot table aggregates")
    long = wide.reset_index().melt(id_vars="region", var_name="period",
                                   value_name="units")
    check(long.shape[0] == wide.shape[0] * wide.shape[1], "melt shape")
    cross = pd.crosstab(frame["region"].fillna("Missing"),
                        frame["units"].isna(), dropna=False)
    check(cross.to_numpy().sum() == 5, "crosstab accounts for every record")
    aligned = pd.DataFrame({"left": pd.Series([1, 2], index=["a", "b"]),
                            "right": pd.Series([3, 4], index=["b", "c"])})
    check(aligned.loc["b"].tolist() == [2, 3], "Series align by labels")
    check(aligned.loc["a", "right"] is np.nan
          or pd.isna(aligned.loc["a", "right"]), "alignment creates NA")
    return frame, summary


def plots(frame, output):
    """Export descriptive charts with explicit units and original data."""
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns

    output.mkdir(parents=False, exist_ok=False)
    shown = frame.reset_index().assign(
        region=lambda data: data["region"].fillna("Missing category"))
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    sns.scatterplot(data=shown, x="id", y="units", hue="region",
                    style="region", s=90, ax=ax)
    ax.set(title="Synthetic observations: 4 measured, 1 missing",
           xlabel="Record ID (identifier, not time)", ylabel="Units",
           ylim=(0, 60))
    ax.text(.02, .97, "Source: five original PCAD teaching records",
            transform=ax.transAxes, va="top", fontsize=8)
    fig.savefig(output / "observations.png", dpi=160)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    values = frame["units"].dropna().to_numpy(dtype=float)
    ax.hist(values, bins=[0, 20, 40, 60], edgecolor="black")
    ax.set(title="Synthetic distribution; n=4 observed, 1 missing",
           xlabel="Units; bins [0,20), [20,40), [40,60]",
           ylabel="Count", yticks=[0, 1, 2, 3], ylim=(0, 3))
    fig.savefig(output / "distribution.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: pandas_companion.py NEW_OUTPUT_DIRECTORY")
    target = Path(sys.argv[1])
    if target.exists():
        raise SystemExit("choose a new output directory")
    data, grouped = tables()
    print(grouped.to_string())
    plots(data, target)
```

## Integrated labs

1. Acquire a permitted API/file dataset and document population, sampling, fields, license, and ethical constraints.
2. Profile missingness, errors, duplicates, category drift, outliers and integrity failures; state competing missingness mechanisms and evidence needed rather than claiming to classify MAR/MNAR from blanks alone.
3. Implement a fit/transform cleaner with train-only scaling/encoding parameters.
4. Store normalized records in SQLite and answer five questions with parameterized joins, grouping, HAVING, ordering, and limits.
5. Model an exporter family using composition/inheritance and test equality/identity behavior.
6. Bootstrap a median or difference, visualize the sampling distribution, and state what the interval cannot prove.
7. Fit one linear and one logistic example; compare baseline/train/test behavior and diagnose bias/variance risks.
8. Recreate each Pandas reshape/group result with a small hand-worked table.
9. Publish a technical appendix and one-page stakeholder brief whose claims trace to calculations.

These nine activities remain proposed end-to-end work with a permitted external dataset. The original synthetic workbook supplies component practice; it does not certify completion of the nine labs or enrolled courses.

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

1. A join pairs every matching row: two occurrences on the left and three on the right produce six rows. Confirm keys/grain before joining, then validate cardinality and unmatched rows; arbitrary deduplication can hide real records.
2. MCAR has missingness independent of the data; MAR permits dependence on observed information after which missing values add no further dependence; MNAR retains dependence on unobserved information. These are assumptions about a process, not labels established merely by seeing blanks.
3. Use one-hot columns for nominal categories when numeric order would be false. Learn the vocabulary on training data, specify unknown/missing policies and consider whether a linear model needs a reference category. An all-zero unknown needs explicit interpretation.
4. Imputation/scaling/selection estimates calculated before splitting expose held-out information. Fit on the training partition or each cross-validation training fold, freeze the parameters, then transform the corresponding validation/test data.
5. Type validation checks representation; range/domain validation checks allowed values; cross-field validation checks relationships such as end time after start. A valid numeric value may still violate a domain or referential rule.
6. Public HTML does not settle authorization, terms, privacy or source-load obligations. Requests retrieves a response and Beautiful Soup parses it; neither guarantees permission, a stable schema or representative sampling.
7. `is` tests the same object; `==` uses equality behavior. Two Record(7) objects may compare equal yet be distinct. Mutating an alias changes the shared instance; unsupported `__eq__` operands return `NotImplemented`.
8. A placeholder binds a value, so `SELECT ?` with `units` yields the string rather than choosing the column. Use a fixed mapping of allowed identifiers; never interpolate an arbitrary name from input.
9. WHERE filters individual input rows before grouping; HAVING filters groups after aggregation. With outer joins, moving a condition from ON to WHERE can remove padded NULL rows and change the question answered.
10. SQL NULL represents missing/unknown and usually maps to Python None. `NULL = NULL` is unknown, `IS NULL` tests it, COUNT(column) ignores it, and COUNT(*) counts rows. Pandas missing-key merges differ from SQL equality joins.
11. Pearson r describes linear association and is undefined for a constant variable. Zero does not exclude nonlinear dependence, and a high value does not establish causation or independence of observations.
12. Bootstrap intervals reflect resampling from the observed sample under assumptions. Wrong resampling units, selection bias, tiny samples or ignored preprocessing uncertainty can make precision misleading; a seed cannot repair those issues.
13. Use binary logistic regression for a binary response/probability model and linear regression for an appropriate continuous response. Check optimization, rank or separation, assumptions, calibration and held-out metrics; coefficient scales differ.
14. `.loc` uses labels and normally includes both slice endpoints; `.iloc` uses positions with an excluded stop. Series alignment is by label, and missing-mask/position bounds need explicit handling. A single loc assignment is the Pandas 3 parent-update idiom.
15. Pivot needs unique index/column coordinates; pivot_table aggregates repeated coordinates with a specified function. Check missing categories and row counts before accepting the new shape.
16. Compare trailing dimensions: each pair must be equal or one. A valid broadcast can still produce an unintended outer result or excessive output size; verify semantic axes, not just absence of an exception.
17. Underfitting can reflect insufficient capacity/high bias; overfitting can reflect excessive sensitivity/variance. Compare training and properly held-out performance with a baseline, then investigate leakage, drift and sampling before assigning a cause.
18. State the question, observed result, magnitude/denominator, limitation and proportionate action. For the fixture, disclose North's missing measurement beside its mean; do not turn a synthetic association into an operational recommendation.

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

This is not a complete list and is not meant to be consumed in full. Times labeled author budget are planning suggestions, not provider runtimes or observed course completion. Public outlines do not establish enrolled content quality or complete PCAD alignment.

| Resource | Access | Estimated time |
|---|---|---|
| [PCAD syllabus](https://pythoninstitute.org/pcad-exam-syllabus) and this objective map | Free canonical scope; manual comparison after retrieval failure | Author budget: 2–3 hours to map gaps |
| [Cisco sequence on the exam page](https://pythoninstitute.org/pcad) | Intro to Data Science → Data Science Essentials with Python → Data Analytics Essentials modules 1/2/3/5/6/7/9/10; direct [catalog](https://www.netacad.com/courses/data-analytics-essentials) returned only an application shell | Current course durations/access unverified; earlier 45–70 hour claim removed |
| [PD101 public outline](https://edube.org/study/pd101) | Free Core lessons/module tests, USD 49 Full/Pro interactive work; explicitly PCED-aligned foundation | Provider: five weeks, about one hour/day; not a complete PCAD preparation claim |
| [PCAD standalone practice kit](https://ums.edube.org/products/1-pi-pcad-3102-pt) | USD 49, two tests, up to 10 launches each, 12-month voucher; no exam included; account/profile distinction unresolved | Provider exam simulations; author budget: two sittings plus explanation-led remediation |
| [Python for Data Analysis, third edition](https://wesmckinney.com/book/) | Free author-hosted web edition; landing updated for Pandas 2.0/Python 3.10, so compare newer Pandas 3 behavior | Author budget: 15–25 selected hours; chapters not audited here |
| [Pandas getting started](https://pandas.pydata.org/docs/getting_started/) and linked contracts above | Free primary documentation; companion still needs runtime execution | Author budget: 6–10 hours with original tables |
| [Introduction to Statistical Learning](https://www.statlearning.com/) | Retrieval failed; current download/access and chapters unverified | Current duration unverified; use only after inspecting the resource |
| [Kaggle Learn](https://www.kaggle.com/learn) | Retrieval failed; current catalog/account requirements unverified | Earlier 20–35 hour claim removed |

The PCAD exam page still calls PD101 “in development,” while the public Edube page offers an explicitly PCED-aligned course. Record that discrepancy rather than assuming current full PCAD coverage. No protected lesson or exam content was accessed, and no purchases were made. Avoid providers offering recalled exam questions.

## Review evidence and remaining work

The [deep-review record](../docs/research/2026-09-29-pcad-31-02-deep-review.md) records source-reading boundaries, exact code hashes, observed versions and repository gates. The original workbook's five-record CSV SHA-256 is `3d2fa43225b00e41b1953578478e2402bdfec87778ec675d3cc80d5a66c47b33`. Direct HTTP success does not imply a readable course body. The generic Python index reports 3.14.7 and pinned 3.13 references report 3.13.15; actual local execution used 3.13.14. Selected SciPy 1.18.0 installed docstrings supplement failed direct documentation retrieval; current Beautiful Soup web docs and local 4.13.3 are not identical versions.

Pending: run the Pandas/Matplotlib/Seaborn companion and inspect exported figures in an authorized environment; complete the broader permitted-dataset and spreadsheet activities; resolve practice redemption/launch terms and publisher wording conflicts; inspect inaccessible course interiors if available; obtain human content/accessibility review. These blockers do not count as successful live execution or exam readiness approval.
