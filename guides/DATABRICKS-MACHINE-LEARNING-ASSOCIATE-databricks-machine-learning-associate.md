---
exam_code: DATABRICKS-MACHINE-LEARNING-ASSOCIATE
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/machine-learning-associate
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# Databricks Certified Machine Learning Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-machine-learning-associate-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/machine-learning-associate) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-MACHINE-LEARNING-ASSOCIATE`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official guide for the live version as of March 1, 2025; live four-domain page checked September 1, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026. The detailed PDF is 18 months old and uses earlier names such as Delta Live Tables and workspace model registry comparisons. Translate those terms through current documentation, but do not silently replace the published objective.<br>
**Lifecycle status:** Active; valid for two years, with the currently live exam required for recertification.<br>
**Assessment:** Live page: 48 scored multiple-choice questions, 90 minutes, USD 200, no test aids, online or test-center delivery; English, Japanese, Brazilian Portuguese and Korean listed. The older PDF says multiple-choice or multiple-selection and online proctoring only; use the live page for current delivery metadata.<br>
**Prerequisite:** None required. The official guide highly recommends course attendance and six months of hands-on experience; working Python, scikit-learn, Spark ML, Unity Catalog and basic statistics are practical prerequisites.

## How to use this guide

Use one reproducible classification or regression project end to end. Preserve business objective, entity/time grain, feature definitions, split strategy, experiment/run IDs, code/data/environment versions, parameters, metrics and slices, registered model/version/alias, deployment contract, inference evidence and cleanup.

```text
decision and metric -> governed labels/features -> leakage-safe split
-> preprocessing pipeline -> baseline -> tuning/CV -> slice evaluation
-> MLflow run -> registered model and alias -> batch/stream/realtime inference
-> monitored outcome and rollback evidence
```

The live page labels the second domain “ML Workflows,” while the detailed PDF calls its corresponding section “Data Processing.” This guide preserves the live label and maps the detailed data exploration/feature engineering objectives into it.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes an objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Databricks' published exam objectives.

## Objective map

| Published domain | Weight | Evidence you should produce |
|---|---:|---|
| Databricks Machine Learning | 38% | MLOps lifecycle, runtime/AutoML decision, governed feature table, MLflow run and Unity Catalog model lifecycle. |
| ML Workflows | 19% | Profile/visualization, outlier and missing-data decision, encoding and transformation without leakage. |
| Model Development | 31% | Algorithm/metric choice, pipeline, imbalance treatment, tuning/CV calculation and bias/variance diagnosis. |
| Model Deployment | 12% | Batch, streaming or real-time serving design with tested schema, scale and release behavior. |

---

## 1. Databricks Machine Learning (38%)

### Treat MLOps as a controlled lifecycle

An MLOps strategy connects data and feature contracts, reproducible training, experiment tracking, validation, registry governance, deployment, monitoring and retraining/rollback. Separate responsibilities: a notebook can explore; a job reproduces training; MLflow records runs and model artifacts; Unity Catalog governs data/features/models; serving or pipelines execute inference.

Best practices include version-controlled code, immutable or traceable data snapshots, isolated environments, deterministic seeds where possible, automated data/model tests, approval evidence, least-privilege workload identities, observability and an explicit champion rollback. Accuracy alone is not operational readiness.

### Choose compute/runtime from dependencies

[Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml) includes tested ML libraries and integrations, reducing setup and compatibility work. A standard or serverless environment may be better where it supports the workload with lower operational overhead. Verify runtime version, CPU/GPU, Python/library compatibility, access mode, Unity Catalog requirements and serving/training differences.

> **Related item:** Preinstalled libraries improve repeatability only when the runtime itself is pinned and recorded. Adding unpinned notebook packages can reintroduce drift.

### Use AutoML as transparent acceleration

[AutoML](https://docs.databricks.com/aws/en/machine-learning/automl/) can inspect data, train/tune candidate models and create reviewable notebooks/results. It accelerates baseline, algorithm and feature exploration; it does not define the business target, prevent leakage, decide the cost of errors, guarantee fairness or approve deployment. Inspect preprocessing, split, trials, primary metric, feature importance/interpretability and generated code.

Use AutoML when its supported problem types and automation fit. Use custom development when the objective, data structure, constraints, algorithm, evaluation or deployment requires control it does not supply.

### Create governed feature tables

Unity Catalog feature engineering uses governed Delta tables with primary keys (and timestamp keys for time series) plus feature metadata. Create/write features through supported DataFrame/SQL/Feature Engineering APIs, then use feature lookups during training so lineage and definitions travel with the model. The current [feature engineering documentation](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc) controls APIs and prerequisites.

| Offline feature table | Online feature table |
|---|---|
| Historical governed features for training and batch scoring | Low-latency published feature values for real-time serving |
| Supports point-in-time historical joins where configured | Optimized for key lookup and freshness, not training history |
| Source of record usually remains Delta/Unity Catalog | Synchronized derivative with publication/TTL/freshness concerns |

Feature keys must represent an entity at a defined time. Split training/validation by time or entity before fitting imputers/encoders when leakage is possible. For online serving, require training-serving feature parity, key availability, default/missing behavior and freshness SLO.

### Track experiments with MLflow

An [MLflow tracking](https://docs.databricks.com/aws/en/mlflow/tracking) run records parameters, metrics, tags, artifacts, source/environment and a model. Manual logging is appropriate when autologging misses a business metric or custom artifact. Use the MLflow client/search API to compare runs by a declared primary metric and constraints; “best” is contextual, not simply the largest number.

The UI exposes runs, parameters, metrics over steps, artifacts, models, tags and comparison. Log data version/table, split seed/period, code revision, dependency/environment, signature/input example and slice metrics. Avoid logging secrets or unrestricted sensitive samples.

### Govern models in Unity Catalog

The [Unity Catalog model registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) uses three-level model names, governed privileges, lineage, tags, versions and aliases. Register a model through a supported MLflow API; then test and assign an alias such as `Champion` to a validated version. An alias is a mutable pointer, not a copy or immutable approval record.

Promote **code** across environments when retraining should occur from environment-owned data/configuration. Promote a **model artifact/version** when the exact validated artifact must move or be referenced consistently. In many current Unity Catalog designs, share governed data/model access and deploy the same tested code rather than copying opaque artifacts between isolated registries.

The older PDF contrasts Unity Catalog with the legacy workspace model registry. Current new designs should use Unity Catalog unless a documented compatibility constraint applies. Tags carry metadata; aliases support deployment references; neither grants data access.

---

## 2. ML workflows: data processing and feature engineering (19%)

### Profile distributions before choosing a repair

Use Spark DataFrame `summary()`/`describe()`, null/distinct counts, quantiles and Databricks data-profile summaries to inspect count, center, spread, extrema and missingness. Stratify by label, time and important groups; an overall average can hide drift or harm.

Choose visualizations by variable types:

| Comparison | Useful methods | What to check |
|---|---|---|
| Continuous distribution | histogram, box plot, density/quantiles | skew, tails, outliers, clipping |
| Categorical distribution | bar/count proportions | rare levels, cardinality, missing/unknown |
| Continuous vs continuous | scatter/correlation, colored by split/label | nonlinearity, clusters, leakage, scale |
| Categorical vs categorical | contingency table/stacked proportions | association, sparse cells, imbalance |
| Continuous by category | box/violin/summary table | group spread, sample size and instability |

Correlation is not causation, and a high correlation with the label may indicate leakage.

### Handle outliers from domain and model behavior

Standard-deviation rules assume a roughly symmetric distribution and are sensitive to extreme values. IQR fences are more robust for skewed data. A value can be rare but valid; removing it changes the target population. Compare cap/winsorize, transform, robust model/scale, domain validation and quarantine. Fit any threshold on training data and apply it unchanged to validation/test.

### Impute with a pipeline

- Mean is sensitive to skew/outliers and suits roughly symmetric numeric features.
- Median is robust for skewed numeric features.
- Mode fits categorical or discrete features but can amplify the majority category.
- Constant/unknown categories preserve missingness semantics where missing has meaning.
- Add a missing-indicator when absence itself may be informative, while checking leakage.

Never compute imputation from the full dataset before splitting. Put the imputer in a scikit-learn or Spark ML pipeline so each cross-validation fold fits preprocessing only on its training portion.

### Encode and transform deliberately

One-hot encoding suits unordered categories with manageable cardinality for models that need numeric features. It is usually unnecessary for tree implementations with native categorical handling and unsuitable for unbounded identifiers. Handle unknown categories at inference and avoid dummy-variable redundancy where the estimator requires it.

A log transform can reduce positive right skew, stabilize multiplicative relationships and make some models/residuals better behaved. Zero/negative values require a defined alternative such as `log1p` where appropriate. If the target is log-transformed, convert predictions back before interpreting them, and calculate business-scale metrics carefully because exponentiation introduces bias and changes error meaning.

> **Related item:** Feature engineering must be fitted inside the training fold. Leakage can produce excellent validation scores and a useless deployed model.

---

## 3. Model development (31%)

### Start from target, data and error costs

Classification predicts categories/probabilities; regression predicts a continuous target; clustering discovers groups without labels. Select an algorithm from sample size, linearity/nonlinearity, sparsity, interpretability, latency, missing/categorical behavior and distributed versus single-node scale—not brand popularity.

Linear/logistic models offer interpretable baselines; trees and ensembles capture nonlinearities/interactions; Spark ML pipelines scale distributed feature transforms/training for supported algorithms; scikit-learn is often productive for single-node data that fits memory. Always establish a simple baseline.

### Understand estimators, transformers and pipelines

An estimator learns from data and produces a model/transformer. A transformer applies `transform()` to produce new columns/predictions. A pipeline orders stages so preprocessing and training are fitted consistently. In Spark ML, `StringIndexer`, `OneHotEncoder` and assembled features are transformers or estimators according to whether they learn state; the classifier/regressor is an estimator.

### Mitigate class imbalance

Accuracy can hide minority failure. Use stratified splits, class/sample weights, cost-sensitive learning, threshold tuning, suitable metrics, or carefully applied under/oversampling. Fit resampling within the training fold only. Synthetic examples can distort sparse or categorical spaces; evaluate precision/recall and calibration on the untouched natural distribution.

### Tune without multiplying work blindly

Grid search evaluates every parameter combination; random search samples combinations and often explores more values efficiently; Bayesian approaches such as Hyperopt use prior trial results to choose promising configurations. The 2025 objective explicitly names Hyperopt `fmin`; use the [Hyperopt documentation](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/) for current support/deprecation context before practice.

If a grid has `a` choices, `b` choices and `k` cross-validation folds, it fits `a × b × k` fold models, commonly plus a final refit depending on framework settings. Parallelizing single-node models can reduce wall time but multiplies CPU/memory and experiment runs. Avoid nested Spark oversubscription: distribute trials or each model deliberately.

Cross-validation estimates performance across multiple folds and uses data efficiently, but costs more and can still leak if folds ignore time/group structure. A train/validation/test split is cheaper and clearer for large data. For time series, use chronological validation; for repeated entities, group them to prevent identity leakage.

### Choose metrics from the decision

| Task/metric | Meaning and boundary |
|---|---|
| Precision | Of predicted positives, fraction correct; important when false positives cost more. |
| Recall | Of actual positives, fraction found; important when misses cost more. |
| F1 | Harmonic mean of precision/recall at a threshold; hides probability calibration and true-negative value. |
| ROC AUC | Ranking over thresholds; can look optimistic with severe imbalance. |
| Log loss | Penalizes wrong confident probabilities; needs calibrated probability reasoning. |
| RMSE | Square-root mean squared error; emphasizes large errors. |
| MAE | Mean absolute error; robust and directly interpretable in target units. |
| R² | Variance explained relative to a mean baseline; not an absolute error unit and can be negative. |

Evaluate the primary metric plus operational constraints and group/time slices. Choose a threshold using validation data, then report once on an untouched test set.

### Diagnose bias and variance

High bias/underfitting: training and validation performance both poor—add signal, improve representation or model capacity. High variance/overfitting: training strong, validation materially worse—simplify, regularize, add representative data, reduce leakage or tune. Learning curves and fold variance strengthen the diagnosis. More complexity is not automatically better.

> **Related item:** Statistical performance, fairness, explainability, robustness and serving cost are separate acceptance dimensions. A champion requires an explicit multi-dimensional gate.

---

## 4. Model deployment (12%)

### Select an inference mode from the service contract

| Mode | Strong fit | Key design evidence |
|---|---|---|
| Batch inference | periodic scoring of many records | input snapshot, model alias/version, output idempotency, schedule and reconciliation |
| Streaming inference | continuous events through a stateful pipeline | checkpoint, watermark/state, model loading, throughput/backpressure and replay |
| Real-time serving | request/response low-latency decisions | endpoint schema, authentication, concurrency, scale-to-zero/cold start, timeout and fallback |

For batch scoring, load the model once per partition/batch where possible; a Pandas UDF can vectorize scoring. Do not call a real-time endpoint row by row from a high-volume Spark transformation when local/distributed artifact scoring fits.

Current [model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) deploys supported Unity Catalog/MLflow models to endpoints. Define signature and input example, workload size/scaling, identity, network, secrets, traffic configuration and inference table/monitoring needs. Query with the expected records/DataFrame/tensor format and handle errors/timeouts.

Traffic splitting routes proportions between served model versions for canary/A/B behavior. It is not randomization proof by itself: record assignment, exposure, outcome, sample size, rollback threshold and version. Pin a version for reproducibility; use aliases for controlled release references.

For streaming inference, the PDF says Delta Live Tables; the current name is Lakeflow Spark Declarative Pipelines. Apply a locally loaded model/UDF in the stream where supported, manage checkpoints and autoscaling, and avoid high-latency external calls per event. Review [batch and streaming inference](https://docs.databricks.com/aws/en/machine-learning/model-inference/) for current patterns.

**VERIFY CURRENT:** serving endpoint types, scale behavior, traffic configuration, online feature stores, inference tables, AI Gateway and monitoring capabilities change quickly. Recheck them in the target cloud/region.

---

## Integrated decision scenarios

### Scenario A — churn model with governed features

Define churn horizon, prediction time and cost of misses/false outreach. Create Unity Catalog feature tables with point-in-time keys, split by time/customer, fit imputation/encoding inside folds and mitigate imbalance with weights/threshold rather than contaminating validation. Log run/data/code/slice metrics, register in Unity Catalog and assign `Champion` only after approval. Batch score customers and reconcile entity/version/output counts.

### Scenario B — real-time fraud canary

Use online features only where latency/freshness justify them and prove training-serving parity. Train a probability model with log loss, precision/recall at an operating threshold and segment slices. Deploy a signed/versioned model endpoint, split limited traffic to a challenger, authenticate clients, monitor latency/error/drift/outcomes and rollback the alias/traffic based on a predetermined threshold.

### Scenario C — streaming engagement anomaly detection

Use a Lakeflow/Structured Streaming pipeline with a ten-minute event-time window, watermark/checkpoint and a locally distributed model artifact. Test late/duplicate events and throughput/backpressure. Avoid per-row endpoint calls. Track the model/run/version used for each prediction, quarantine invalid features and make replay idempotent.

## Hands-on lab sequence

1. **Profile and split:** Build label/time/entity-aware train/validation/test data; profile missingness, skew, outliers and imbalance by split/group and document leakage risks.
2. **Preprocessing pipeline:** Implement median/mode imputation, unknown-category handling, one-hot/log transforms and a reproducible scikit-learn or Spark ML pipeline; prove validation data did not fit preprocessing.
3. **Feature table:** Create a governed feature table with primary/time keys, write features and train through feature lookup; demonstrate point-in-time behavior and lineage.
4. **MLflow experiment:** Train baseline plus candidates, log parameters/metrics/slices/artifacts/signature/environment, search for candidates and explain why the selected run is “best.”
5. **Tuning and evaluation:** Compare grid/random/Bayesian search, calculate expected fits, run leakage-safe CV and tune a decision threshold against business error costs.
6. **Registry lifecycle:** Register the validated model in Unity Catalog; apply tags and a `Champion` alias with a written approval/rollback record; test privileges.
7. **Batch and stream:** Score a batch through a vectorized pattern and a bounded stream through a pipeline/UDF; record versions, checkpoint and reconciliation.
8. **Real-time canary:** Deploy/query a test endpoint, validate schema/auth/error behavior, split test traffic between versions and execute rollback/cleanup.

## Readiness checks

### Databricks ML and workflows

- [ ] I can explain an MLOps lifecycle beyond experiment tracking.
- [ ] I can select an ML runtime from dependencies/compute and record its version.
- [ ] I can use AutoML as a reviewable baseline rather than outsourced judgment.
- [ ] I can define feature entity, key, time and freshness semantics.
- [ ] I can distinguish offline and online feature tables.
- [ ] I can train/score through governed feature lookups and identify training-serving skew.
- [ ] I can log parameters, metrics, artifacts, model, signature, environment, code and data references.
- [ ] I can search runs and define “best” using metric plus constraints/slices.
- [ ] I can register and govern models in Unity Catalog.
- [ ] I can distinguish model versions, aliases and tags.
- [ ] I can choose promoting code versus an exact model artifact.
- [ ] I can translate workspace-registry and Delta Live Tables terminology to current guidance without changing the published objective.
- [ ] I can profile continuous/categorical features with appropriate comparisons.
- [ ] I can choose outlier handling from distribution/domain/model impact.
- [ ] I can select mean/median/mode/constant imputation and fit it without leakage.
- [ ] I can decide when one-hot and log transforms are appropriate.

### Development and deployment

- [ ] I can select classification/regression/clustering and an algorithm from the problem/data constraints.
- [ ] I can distinguish estimator, transformer, fitted model and pipeline.
- [ ] I can mitigate imbalance without contaminating validation.
- [ ] I can compare grid, random and Bayesian tuning.
- [ ] I can calculate parameter combinations × cross-validation folds and account for refit.
- [ ] I can choose CV versus a holdout and use group/time-aware folds.
- [ ] I can interpret precision, recall, F1, ROC AUC and log loss.
- [ ] I can interpret RMSE, MAE and R² in the business context.
- [ ] I can return log-target predictions to the business scale safely.
- [ ] I can diagnose bias versus variance with training/validation evidence.
- [ ] I can select batch, streaming or real-time inference from latency/volume/cost/replay needs.
- [ ] I can perform batch scoring without per-row driver or endpoint bottlenecks.
- [ ] I can design checkpointed streaming inference with a pinned model version.
- [ ] I can deploy/query a serving endpoint with signature, identity, scaling and failure behavior.
- [ ] I can split traffic with measurable canary assignment/outcomes and rollback.
- [ ] I can record prediction-to-model/run/data lineage and remove temporary endpoints/artifacts.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Choose a primary path, then spend at least equal time producing and testing feature, experiment, registry and deployment evidence. Durations are planning estimates checked September 1, 2026 and may change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page and March 1, 2025 exam guide](https://www.databricks.com/learn/certification/machine-learning-associate) | Free | 1–2 hours; map every objective and inspect vendor sample format without redistributing questions |
| [Databricks Academy](https://customer-academy.databricks.com/) — *Machine Learning with Databricks* and four named self-paced courses | Free account/customer or partner entitlement varies | 20–35 hours with labs; verify catalog and current terminology after sign-in |
| [Databricks Free Edition](https://www.databricks.com/learn/free-edition) or authorized workspace | Free/organizational | 18–30 hours for eight labs; serving/online-feature capabilities may require another environment |
| [Databricks machine learning documentation](https://docs.databricks.com/aws/en/machine-learning/) | Free | 8–14 hours selected reading and reproduction |
| [MLflow documentation](https://mlflow.org/docs/latest/ml/) | Free | 4–8 hours selected tracking, model and deployment practice; reconcile OSS and managed Databricks behavior |
| [Databricks YouTube](https://www.youtube.com/@Databricks) | Free | 3–6 hours selected current MLflow, feature engineering, MLOps and serving sessions |
| [Whizlabs: Databricks Machine Learning Associate](https://www.whizlabs.com/databricks-certified-machine-learning-associate/) | Paid; training/practice product | Stable public totals were not exposed; budget 6–14 hours and verify March 2025 coverage after sign-in |
| [Udemy search: Databricks Machine Learning Associate](https://www.udemy.com/courses/search/?q=databricks%20machine%20learning%20associate) | Paid marketplace | 8–20 hours only after selecting a current, lab-based course; reject dump-focused listings |

The 2025 blueprint is still live but aged: explicitly gap-check current Unity Catalog model/feature APIs, Lakeflow naming, Hyperopt support and serving behavior. No exact current Pluralsight, O'Reilly, LinkedIn Learning or MeasureUp product was independently verified.
