---
exam_code: DATABRICKS-MACHINE-LEARNING-PROFESSIONAL
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/machine-learning-professional
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# Databricks Certified Machine Learning Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-machine-learning-professional-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/machine-learning-professional) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-MACHINE-LEARNING-PROFESSIONAL`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official guide for the live version as of September 30, 2025; live three-domain weighted page checked September 1, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026. The PDF uses older “Databricks Asset Bundles” and “Lakehouse Monitoring” wording; current documentation uses Declarative Automation Bundles and expanded data-quality/monitoring terminology. Preserve the published objectives and verify current interfaces.<br>
**Lifecycle status:** Active; valid for two years, with the currently live exam required for recertification.<br>
**Assessment:** 59 scored multiple-choice questions, 120 minutes, USD 200, no test aids, English, online or test-center delivery. The September PDF lists online proctoring only; the live page controls current delivery metadata.<br>
**Prerequisite:** None required. The official guide highly recommends course attendance and one year of hands-on Databricks experience. This guide assumes associate-level ML/statistics plus production Spark, MLflow, Unity Catalog, testing, CI/CD, monitoring and serving experience.

## How to use this guide

Build a production system with two execution scales and a controlled release. Retain feature/event-time contracts, split logic, code/data/runtime/library versions, parent/child run IDs, compute/topology, trial resources, model signature/artifacts, registry version/alias, bundle target, test evidence, monitor/baseline/slices, alert/retrain decision and endpoint rollout/rollback.

```text
workload shape -> Spark/single-node/Ray and vertical/horizontal choice
-> point-in-time features -> distributed train/tune -> nested MLflow evidence
-> unit + end-to-end integration gates -> environment bundle deployment
-> monitor + alert -> retrain candidate gate -> canary/blue-green serving
-> health/outcome evidence -> promote or rollback
```

Model Development and ML Ops are each 44%. Treat them as one system: a sophisticated distributed trial with no reproducible environment or release gate is not professional MLOps.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes an objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Databricks' published exam objectives.

## Objective map

| Published domain | Weight | Professional evidence |
|---|---:|---|
| Model Development | 44% | Scalable Spark/single-node/Ray training and inference, distributed tuning, nested MLflow and point-in-time/on-demand features. |
| ML Ops | 44% | Deploy-code lifecycle, multi-environment resources, unit/integration tests, automated retraining and sliced drift/performance/health monitoring. |
| Model Deployment | 12% | Blue-green/canary rollout and custom PyFunc endpoint through UI, REST or MLflow Deployments SDK. |

---

## 1. Model Development (44%)

### Choose Spark ML only when distribution helps

Use [Spark ML](https://spark.apache.org/docs/latest/ml-guide.html) when the dataset/feature transformation exceeds practical single-node memory, the supported estimator scales across partitions, or batch/stream scoring is already distributed. Use scikit-learn or another single-node library when data fits memory and its algorithms/ecosystem are stronger. Moving a small model to Spark adds serialization, scheduling and tuning overhead without creating useful scale.

A Spark ML pipeline orders estimators and transformers: index/encode categories, assemble/scale features where required, fit the estimator and retain the fitted `PipelineModel`. Select classification versus regression from target type; choose metric, thresholds and interpretability/latency constraints before tuning.

For batch or streaming inference, load the Spark `PipelineModel` once and transform a DataFrame. For single-node models over distributed data, use a vectorized Pandas function/UDF or partition-level pattern where supported. Real-time calls belong to serving when latency and request semantics require them; do not send millions of row-wise endpoint requests from Spark.

### Scale from the limiting resource

| Choice | Strong fit | Failure boundary |
|---|---|---|
| Vertical scaling | one model/task needs more CPU, memory or GPU on one process | hardware ceiling, cost and single-node failure |
| Horizontal/data parallelism | training algorithm partitions data/gradients across workers | communication overhead, stragglers and scaling efficiency |
| Model parallelism | model cannot fit one device/process | communication/partition complexity |
| Trial parallelism | many independent hyperparameter candidates | each trial still needs sufficient resources; oversubscription |
| Grouped model parallelism | separate model per customer/site/device via Pandas function APIs | group skew, many tiny models and registry/serving sprawl |

Spark excels at data preparation, Spark ML algorithms and grouped operations. [Ray on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/) supports distributed Python ML ecosystems and training/tuning patterns. Compare library compatibility, fault tolerance, scheduler/topology, GPU support, data movement, observability and operational ownership—not “which is faster” in the abstract.

### Tune with Optuna or Ray without losing reproducibility

Optuna chooses trials through a sampler/pruner and can use [MLflow integration](https://mlflow.org/docs/latest/ml/traditional-ml/hyperparameter-tuning/with-optuna/) to record studies/trials. Ray Tune distributes supported search workloads. Define search space, objective direction, seed, budget, pruning rule, storage/concurrency, per-trial resources and failure policy. Limit nested parallelism so trials and each model do not both seize all CPUs/GPUs.

Log each trial as a child run under a parent search run. Aggregate cross-validation metrics and retain the final refit/evaluation as a clearly associated run. Nested runs keep experiment comparison coherent; they do not validate that folds are leakage-safe.

### Use advanced MLflow records as lineage, not decoration

Log code/data/environment, parameters, custom metrics and slices, plots, feature definitions, model signature/input example and custom artifacts. A parent run can describe a tuning/retraining execution; child runs describe candidates/folds. Select a candidate with a declared gate across primary metric, constraints, robustness, latency/cost and protected slices.

A custom [MLflow PyFunc](https://mlflow.org/docs/latest/ml/model/python_model/) wraps arbitrary Python prediction logic with artifacts/dependencies and a standard `predict` interface. It is useful when preprocessing/postprocessing or a non-native framework must travel with the model. Avoid hidden network calls, secrets or mutable global state inside prediction.

### Make features point-in-time correct and production-consistent

For every training row, feature values must come only from information available at its prediction timestamp. Use entity/time keys and point-in-time joins. A latest-value join leaks future state. Validate duplicate keys, late corrections, timezone and feature availability lag.

Automate offline feature computation through governed pipelines and a Feature Engineering client. Publish selected values to online tables for low-latency lookups, with synchronization, TTL/freshness and missing-key behavior. [Online feature stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-stores) are derivatives, not historical training truth.

On-demand features compute from request data at inference. Package their function and dependencies with the model so training and serving use identical logic. Combine with retrieved features through a documented schema/signature; test nulls, unknown keys and version changes.

> **Related item:** “Real-time feature engineering” has three clocks: event production, offline/online publication and request-time computation. Model latency and correctness depend on all three.

---

## 2. ML Ops (44%)

### Prefer deploy-code when environments own data and controls

A deploy-code strategy promotes versioned code/configuration while each environment creates its experiment, feature/training workflow, registered model and endpoint under local identities and data access. This reduces artifact copying and respects environment governance. A deploy-model strategy references/moves the exact validated artifact where business assurance requires it. Explicitly define which objects cross boundaries.

Map lifecycle stages:

- Git and code review: source, tests, bundle definitions.
- Declarative Automation Bundles: experiments, jobs/pipelines, registered-model/serving resources and environment targets where supported.
- Unity Catalog: training data/features/models, permissions, lineage, tags and aliases.
- MLflow: runs, candidates, metrics/artifacts and model packaging.
- Jobs/pipelines: feature, train, evaluate, register/retrain orchestration.
- Model Serving: staged traffic, inference evidence and endpoint health.

Current [Declarative Automation Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) replace the DAB name in the PDF. Use variables/targets for dev/test/prod catalog, schema, experiment, model, endpoint, identity and permissions. CI should validate syntax, run unit/security checks and deploy/test in isolation before approval.

### Test components and contracts at the right stage

Unit-test pure feature/metric/prediction functions with small boundary fixtures. Store reusable code in modules rather than making every function notebook-local. Notebook tests can validate widgets and entry-point behavior, but packaging improves local/CI execution and dependency control.

Integration tests should exercise:

1. Source and point-in-time feature computation/write/lookup.
2. Training-set schema and leakage guards.
3. Training and MLflow logging/registry contract.
4. Evaluation gates, signature/artifacts and candidate selection.
5. Deployment configuration, identity and endpoint readiness.
6. Inference payload/output/error, feature parity and cleanup.

A hyperparameter change leaves feature code unchanged but can change model signature/size/latency and every downstream behavior. Re-run training, evaluation and deployment/inference integration; preserve a smaller stable feature test as a dependency gate.

### Automate retraining without automating approval away

A drift/performance alert can create a retraining candidate, not automatically crown it. Capture trigger, data cutoff, baseline, code/config, candidate set and selection gate. Compare candidate against the current production alias on untouched recent and reference data. Require minimum performance, slices, calibration, latency/cost, robustness and compliance; apply cooldown/minimum sample rules. If labels are delayed, drift may trigger investigation while performance remains unknown.

Use aliases to resolve the current champion and an immutable version to reproduce it. A top-performing candidate is the one satisfying the declared decision loss and constraints, not necessarily highest AUROC. For a probability-based downstream policy, log loss/calibration may be more important than a threshold summary.

### Monitor data, predictions, outcomes and infrastructure

Current [data-quality monitoring](https://docs.databricks.com/aws/en/data-quality-monitoring/) supports profiles/metrics over snapshot, time-series and inference-style data; names and APIs have evolved from Lakehouse Monitoring. Choose table type from semantics:

| Profile | Use | Required thinking |
|---|---|---|
| Snapshot | periodically compare entire current dataset | baseline and refresh cadence; changes may be diluted |
| Time series | compare timestamped windows | timestamp, window/granularity and seasonality |
| Inference | predictions/features with model and optional labels | model/version, prediction, label delay and performance metrics |

Drift compares current versus baseline or consecutive windows. Numerical tests/distances and categorical distribution tests require sample size and multiple-comparison context; statistical significance is not automatically operational importance. Define thresholds from risk and historical variation.

Slice by region, device, customer segment, label and model version where justified. Avoid exploding combinations or exposing sensitive small groups. Custom metrics should have stable SQL/definition, owner, unit, expected range and alert meaning.

Monitor model performance trends when labels arrive and separately monitor data freshness/schema/nulls, feature drift, prediction distribution and endpoint health: latency percentiles, request rate, error rate, CPU/memory, scale/cold start and saturation. Use the current [serving monitoring guidance](https://docs.databricks.com/aws/en/machine-learning/model-serving/monitor-diagnose-endpoints).

### Alert with an owner and response path

Write metric tables to governed storage, query a stable window and alert only after sample-size/freshness checks. The message needs model/version, slice/window, current/baseline value, threshold, dashboard/run link, owner and response. Test notification failure and deduplicate persistent breaches.

> **Related item:** Data drift is a change in inputs; concept drift changes the relationship between inputs and target; model-performance degradation requires outcomes/labels. One is not proof of another.

---

## 3. Model Deployment (12%)

### Compare blue-green and canary releases

**Blue-green** prepares a complete new serving environment/version and switches traffic after validation; rollback is a fast switch but duplicate capacity costs more. **Canary** routes a small proportion to a challenger and increases it based on health/outcome gates; it limits blast radius but requires attributable traffic and statistically sound comparison. A high-traffic critical endpoint commonly combines adequate horizontal scaling, route optimization where supported and a gradual canary.

Define pre-deployment load/contract/security tests, traffic steps, minimum observations, latency/error/performance limits, approver, pause and rollback. Do not send 100% to a “canary.” Shadow traffic can compare predictions without influencing users, but protect request data and account for duplicated compute.

### Package and serve custom models

Implement a PyFunc `PythonModel` with deterministic `load_context` and `predict`; log dependencies, signature, input example and required artifacts; register the resulting version in Unity Catalog. Test clean-environment loading, missing/extra columns, batch sizes, invalid inputs, concurrency and artifact permissions.

Deploy a version/alias to Model Serving through supported UI, REST API, Databricks SDK/MLflow Deployments client or bundle resource. Query with the exact payload contract and workspace authentication. The [MLflow Deployments API](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.deployments.html) offers `predict` against an endpoint; REST integration must use headers/body safely, not tokens in query strings.

**VERIFY CURRENT:** route optimization, endpoint resource fields, traffic configuration, scale-to-zero, inference tables, AI Gateway, online features and monitoring vary by cloud/region and release. Recheck [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) before implementation.

> **Related item:** A registry alias chooses a logical model version; endpoint served entities and traffic rules choose runtime deployment. Coordinate them, but do not assume changing one automatically changes the other.

---

## Integrated decision scenarios

### Scenario A — 400-million-row credit model

Use Spark ML for distributed indexing/encoding/assembly/training and a leakage-safe pipeline. Tune supported models with bounded distributed trials, log parent/child MLflow runs and evaluate probability/error slices. Compare horizontal Spark efficiency against sampled/single-node alternatives. Batch-score through the fitted pipeline and retain data/code/model/runtime evidence.

### Scenario B — multi-tenant real-time forecasting

Train grouped models through Pandas function APIs only after measuring group size/skew and model-count operations. Use point-in-time offline features plus online/on-demand features for requests. Package custom PyFunc behavior, deploy with canary traffic, monitor per-model/tenant slices and endpoint health, and rollback on a predeclared gate without exposing small-group data.

### Scenario C — drift-triggered fraud retraining

An inference table records request features, model version, probability, decision, latency and delayed label. Configure time-series/inference monitoring with baseline and slices, alert after sample/freshness checks, then trigger retraining. A bundle deploys code/resources to test; integration tests exercise feature-to-inference; the candidate must beat champion on log loss/calibration, action costs, slices, latency and errors before canary promotion.

## Hands-on lab sequence

1. **Spark ML scale:** Build and tune a Spark pipeline; capture partitioning, stages, resources, trial count and evaluation evidence against a single-node baseline.
2. **Distributed tuning:** Run a bounded Optuna or Ray experiment with explicit per-trial resources and nested MLflow runs; inject and recover one failed trial.
3. **Grouped models:** Train/infer one model per group using a Pandas function API; test skew, empty/small groups and model-artifact organization.
4. **Point-in-time features:** Build offline/time-keyed features, publish/test online values and implement one on-demand feature; prove no future leakage and training-serving parity.
5. **Test pyramid:** Package unit tests and a feature→train→evaluate→register→deploy→inference integration test in an isolated catalog/schema.
6. **Environment bundle:** Define dev/test/prod targets for experiment, job, model and endpoint resources; validate/deploy with workload identity and evidence.
7. **Monitor and retrain:** Create a snapshot/time-series/inference monitor, custom slice metric and tested alert; produce a candidate but require a multi-metric champion gate.
8. **Custom rollout:** Register a PyFunc with artifacts/signature, deploy/query it, execute canary or blue-green steps under synthetic load, then rollback and clean up.

## Readiness checks

### Development

- [ ] I can choose Spark ML versus single-node from data/model/inference requirements.
- [ ] I can construct, tune, evaluate and batch/stream score a Spark pipeline.
- [ ] I can choose vertical, data/model, trial or grouped-model parallelism.
- [ ] I can compare Ray and Spark ownership, data movement and fault behavior.
- [ ] I can distribute Optuna/Ray trials without nested oversubscription.
- [ ] I can structure parent/child MLflow runs for tuning and final evaluation.
- [ ] I can log custom metrics/artifacts and package a clean-load PyFunc.
- [ ] I can build point-in-time feature lookups without future leakage.
- [ ] I can distinguish offline, online and on-demand feature clocks/contracts.
- [ ] I can preserve training-serving feature parity and missing-key behavior.

### ML Ops

- [ ] I can explain deploy-code versus deploy-model environment transitions.
- [ ] I can map Git, bundles, Unity Catalog, MLflow, Jobs and Serving to lifecycle activities.
- [ ] I can define ML resources with environment-specific bundle targets.
- [ ] I can separate function unit tests from end-to-end ML integration tests.
- [ ] I can state which integration gates a model/code/feature/config change invalidates.
- [ ] I can automate retraining while preserving candidate approval and rollback.
- [ ] I can select a candidate across decision loss, slices, robustness, latency and cost.
- [ ] I can select snapshot, time-series or inference monitoring.
- [ ] I can interpret numerical/categorical drift with sample and practical significance.
- [ ] I can compare current-to-baseline and consecutive-window drift.
- [ ] I can monitor delayed-label performance by model/version and slice.
- [ ] I can define governed custom metrics and avoid unsafe small slices.
- [ ] I can separate data, prediction, outcome and endpoint-health monitoring.
- [ ] I can create an actionable alert with sample/freshness check, owner and runbook.

### Deployment

- [ ] I can compare blue-green, canary and shadow strategies.
- [ ] I can define traffic steps, health/outcome gates, pause and rollback.
- [ ] I can register custom PyFunc artifacts/dependencies/signature in Unity Catalog.
- [ ] I can deploy and query a custom model through UI, REST or MLflow Deployments SDK.
- [ ] I can authenticate without putting secrets/tokens in payloads or query strings.
- [ ] I can distinguish registry alias from endpoint served entity and traffic config.
- [ ] I can load-test latency/error/throughput and attribute canary outcomes.
- [ ] I can remove endpoints/online tables/test data and retain audit evidence.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Select the material that closes measured gaps and spend most effort building an observable, tested release system. Durations are planning estimates checked September 1, 2026 and may change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page and September 30, 2025 guide](https://www.databricks.com/learn/certification/machine-learning-professional) | Free | 2–3 hours to map objectives and inspect vendor sample format; do not redistribute questions |
| [Databricks Academy](https://customer-academy.databricks.com/) — *Machine Learning at Scale* and *Advanced Machine Learning Operations* | Free account/customer or partner entitlement varies | 25–45 hours with labs; verify current catalog/runtime after sign-in |
| [Databricks ML documentation](https://docs.databricks.com/aws/en/machine-learning/) | Free | 12–20 hours selected implementation across Spark/Ray/features/MLflow/monitoring/serving |
| Authorized workspace plus the guide's eight labs | Organizational; some labs can start in Free Edition | 30–50 hours including failure, scale, monitoring and rollout experiments |
| [MLflow documentation](https://mlflow.org/docs/latest/ml/) | Free | 6–12 hours selected nested-run, PyFunc and deployment practice |
| [Databricks YouTube](https://www.youtube.com/@Databricks) | Free | 4–8 hours selected recent MLOps, Ray, MLflow, feature and serving sessions |
| [Whizlabs: Databricks Machine Learning Professional](https://www.whizlabs.com/databricks-certified-machine-learning-professional/) | Paid; training/practice product | Stable public totals were not exposed; budget 8–18 hours and verify September 2025 alignment |
| [O'Reilly search: Databricks MLOps](https://www.oreilly.com/search/?q=Databricks%20MLOps) | Paid/trial | 8–20 hours selected current material; map chapters/events to the blueprint rather than assuming completeness |

The blueprint is current but fast-moving interfaces require explicit checks for bundle names, monitoring terminology, Ray/Optuna integrations, online/on-demand features and serving traffic. No exact current Pluralsight, Udemy, LinkedIn Learning or MeasureUp product was independently verified.
