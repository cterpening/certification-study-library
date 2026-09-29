---
exam_code: DATABRICKS-MACHINE-LEARNING-PROFESSIONAL
vendor_id: databricks
official_blueprint: https://www.databricks.com/learn/certification/machine-learning-professional
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# Databricks Certified Machine Learning Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#databricks-machine-learning-professional-coverage-record). The [official certification page](https://www.databricks.com/learn/certification/machine-learning-professional) and its linked exam guide are authoritative.

**Library identifier:** `DATABRICKS-MACHINE-LEARNING-PROFESSIONAL`; Databricks does not publish a short exam code on the official page checked.<br>
**Current baseline:** Detailed official guide for the live version as of September 30, 2025; live three-domain weighted page checked September 28, 2026.<br>
**Upcoming blueprint change:** None announced as of September 28, 2026. The PDF uses older “Databricks Asset Bundles” and “Lakehouse Monitoring” wording; current documentation uses Declarative Automation Bundles and expanded data-quality/monitoring terminology. Preserve the published objectives and verify current interfaces.<br>
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

**VERIFY CURRENT:** the [Ray integration](https://docs.databricks.com/aws/en/machine-learning/ray/) distinguishes Ray on Spark from Ray on AI Runtime. Ray-on-Spark cannot start on serverless-based runtimes; its documented access modes are dedicated, no-isolation shared and job clusters. Install dependencies before initializing Ray: `%pip` on a running Ray cluster can shut it down. Do not apply this restriction to the separate serverless GPU integration without checking its own support matrix.

### Tune with Optuna or Ray without losing reproducibility

Optuna chooses trials through a sampler/pruner and can use [nested MLflow tracking](https://mlflow.org/docs/latest/ml/getting-started/hyperparameter-tuning/) to record studies/trials. Ray Tune distributes supported search workloads. Define search space, objective direction, seed, budget, pruning rule, storage/concurrency, per-trial resources and failure policy. Limit nested parallelism so trials and each model do not both seize all CPUs/GPUs.

Log each trial as a child run under a parent search run. Aggregate cross-validation metrics and retain the final refit/evaluation as a clearly associated run. Nested runs keep experiment comparison coherent; they do not validate that folds are leakage-safe. For distributed workers, carry the parent run identifier explicitly and verify each child's parent tag; do not assume the driver's active-run context is inherited by another process. Record failed and pruned trials as well as successful candidates. A local sequential Optuna example verifies tracking mechanics only, not distributed execution.

### Use advanced MLflow records as lineage, not decoration

Log code/data/environment, parameters, custom metrics and slices, plots, feature definitions, model signature/input example and custom artifacts. A parent run can describe a tuning/retraining execution; child runs describe candidates/folds. Select a candidate with a declared gate across primary metric, constraints, robustness, latency/cost and protected slices.

A custom [MLflow PyFunc](https://mlflow.org/docs/latest/ml/model/python_model/) wraps arbitrary Python prediction logic with artifacts/dependencies and a standard `predict` interface. It is useful when preprocessing/postprocessing or a non-native framework must travel with the model. Avoid hidden network calls, secrets or mutable global state inside prediction.

### Make features point-in-time correct and production-consistent

For every training row, feature values must come only from information available at its prediction timestamp. Use entity/time keys and point-in-time joins. A latest-value join leaks future state. Validate duplicate keys, late corrections, timezone and feature availability lag.

Automate offline feature computation through governed pipelines and a Feature Engineering client. Publish selected values to online tables for low-latency lookups, with synchronization, TTL/freshness and missing-key behavior. [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store) are derivatives, not historical training truth. The earlier plural-URL reference now describes [third-party online stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-stores); those are a different configuration route. Current native-store creation uses `FeatureEngineeringClient.create_online_store`, backed by Lakebase Autoscaling, and features must then be published. Do not mechanically substitute this call for every older SDK online-table example. Check client version, source keys, publication state, credentials, capacity and deletion of temporary stores before the lab; no online store was provisioned in this review.

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

Current [data-quality monitoring](https://docs.databricks.com/aws/en/data-quality-monitoring/) includes two capabilities. Anomaly detection checks freshness/completeness across selected tables; **data profiling** is the former Lakehouse Monitoring capability used for detailed statistics, drift and inference quality. A healthy freshness result does not prove model quality. Choose the [profile type](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/) from data semantics:

| Profile | Use | Required thinking |
|---|---|---|
| Snapshot | periodically compare entire current dataset | baseline and refresh cadence; changes may be diluted |
| Time series | compare timestamped windows | timestamp, window/granularity and seasonality |
| Inference | predictions/features with model and optional labels | model/version, prediction, label delay and performance metrics |

Drift compares current versus baseline or consecutive windows. Numerical tests/distances and categorical distribution tests require sample size and multiple-comparison context; statistical significance is not automatically operational importance. Define thresholds from risk and historical variation.

The [metric table reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output) distinguishes numeric `ks_test`/Wasserstein distance from categorical chi-square/Jensen–Shannon distance. A p-value is evidence against a distributional null; a distance measures magnitude. Require a useful effect size and sufficient observations, account for multiple tests, and compare equivalent seasonal windows. Model-quality metrics require prediction and label columns; missing outcomes leave quality unknown.

For new code, consult the [current profile API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api): it uses `WorkspaceClient.data_quality` and SDK 0.68.0 or later, while `quality_monitors` is deprecated. Resolve table/output-schema identifiers and required privileges, then verify refresh status and metric-table results; a create request is not proof that monitoring completed.

**Unconfirmed — validation needed (September 28):** the [overview limits](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/) describe a last-30-days window, while the [API guide](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api) describes an initial 30-day backfill followed by new data. The metric reference also qualifies the initial window. Do not assume automatic coverage of late labels or historical corrections outside that interval. In an authorized disposable table, test an old event, a newly appended old-timestamp event and a delayed label update; inspect refresh and metric windows. Keep an independent evaluation path until the required case is proven. Follow-up is scheduled for October 5.

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

### Make a custom model's input contract explicit

This original local example wraps a small decision rule, not a trained business model. Log/save it with an explicit signature, input example and pinned dependencies. The [PyFunc reference](https://mlflow.org/docs/latest/ml/model/python_model/) explains model packaging and loading; a signature alone does not encode every business invariant.

```python
import numpy as np
import pandas as pd
import mlflow

class MarginRule(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input, params=None):
        required = ["units", "unit_price", "unit_cost"]
        missing = set(required) - set(model_input.columns)
        if missing:
            raise ValueError(f"Missing columns: {sorted(missing)}")
        values = model_input[required].to_numpy(dtype=float)
        if not np.isfinite(values).all() or (values < 0).any():
            raise ValueError("Inputs must be finite and nonnegative")
        margin = values[:, 0] * (values[:, 1] - values[:, 2])
        return pd.DataFrame({"margin": margin}, index=model_input.index)
```

Use rows `(2, 10, 6)` and `(3, 5, 7)` to expect margins `8` and `-6`. Negative margin is valid even though negative input quantities/prices are rejected. Test missing columns, null, infinity, wrong types and empty input. Save and reload the model, then compare predictions; test in a fresh interpreter to catch hidden global dependencies. This does not test serving authentication, network behavior or concurrency.

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

## Worked operational decisions and answers

| Original scenario | Expected decision |
|---|---|
| Eight independent trials each request four CPUs; the cluster exposes sixteen usable CPUs | At most four fit concurrently under this simplified CPU-only budget. Reserve overhead and check memory/GPU constraints before expecting that concurrency. |
| A canary has 4 errors in 400 requests; champion has 6 in 2,000 | Error rates are 1% and 0.3%. The canary has fewer raw errors but a higher rate; use the predeclared gate and uncertainty/sample requirements. |
| Prediction inputs drift, but only 120 of 1,000 requests have labels | Investigate drift and label coverage (12%). Do not claim population-wide quality from an unrepresentative labeled subset. |
| A profile create call succeeds but the latest refresh fails | Monitoring is incomplete. Inspect refresh error and metric freshness; do not present stale output as a current pass. |

1. **Does adding workers make a single-node estimator distributed?** No; choose an algorithm or trial strategy that uses them.
2. **Can unlimited parallel trials compensate for insufficient trial memory?** No; enforce per-trial resource and concurrency limits.
3. **Does the driver's active MLflow run automatically exist in every worker?** No; pass and verify explicit run linkage.
4. **Is a failed trial equivalent to a low-scoring completed trial?** No; record state and failure evidence separately.
5. **Does schema freshness monitoring replace inference profiling?** No; they assess different properties.
6. **Does a small drift p-value prove operational harm?** No; inspect effect size, sample, seasonality and outcomes.
7. **Can missing labels establish acceptable model accuracy?** No; record coverage and delay.
8. **Does creating a profile prove its metrics refreshed?** No; validate refresh status and output windows.
9. **Should a model reject every negative output?** No; the margin example permits losses but constrains its inputs.
10. **Does local model reload prove a serving rollout?** No; endpoint identity, readiness, traffic and recovery require separate workspace tests.

**Review execution boundary — September 28, 2026:** local PyFunc save/load and fresh-process prediction, serial Optuna trials with nested local MLflow tracking, and numerical decision checks were executed. No Spark, Ray cluster, distributed worker, Unity Catalog, online store, monitoring service or endpoint was run. All eight service labs remain proposed.

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

This is **not a complete list**, and it is not meant to be consumed in full. Select the material that closes measured gaps and spend most effort building an observable, tested release system. Public resource availability was checked September 28, 2026. Durations are editorial planning estimates; signed-in Academy and paid lessons were not inspected. O'Reilly access was blocked, and Whizlabs returned an empty body.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official certification page and September 30, 2025 guide](https://www.databricks.com/learn/certification/machine-learning-professional) | Free | 2–3 hours to map objectives and inspect vendor sample format; do not redistribute questions |
| [Databricks Academy](https://customer-academy.databricks.com/) — *Machine Learning at Scale* and *Advanced Machine Learning Operations* | Free account/customer or partner entitlement varies | 25–45 hours with labs; verify current catalog/runtime after sign-in |
| [Databricks ML documentation](https://docs.databricks.com/aws/en/machine-learning/) | Free | 12–20 hours selected implementation across Spark/Ray/features/MLflow/monitoring/serving |
| Authorized workspace plus the guide's eight labs | Organizational; some labs can start in Free Edition | 30–50 hours including failure, scale, monitoring and rollout experiments |
| [MLflow documentation](https://mlflow.org/docs/latest/ml/) | Free | 6–12 hours selected nested-run, PyFunc and deployment practice |
| [Databricks: Data Quality Monitoring at scale (February 4, 2026)](https://www.databricks.com/blog/data-quality-monitoring-scale-agentic-ai) | Free product article | About 30–50 minutes to read and draw separate freshness, drift, performance and alert paths; estimate includes the worksheet. Product context, checked against current profile/API documentation, not added exam scope. |
| [Databricks YouTube](https://www.youtube.com/@Databricks) | Free | 4–8 hours selected recent MLOps, Ray, MLflow, feature and serving sessions |
| [Whizlabs: Databricks Machine Learning Professional](https://www.whizlabs.com/databricks-certified-machine-learning-professional/) | Paid; training/practice product | Stable public totals were not exposed; budget 8–18 hours and verify September 2025 alignment |
| [O'Reilly search: Databricks MLOps](https://www.oreilly.com/search/?q=Databricks%20MLOps) | Paid/trial | 8–20 hours selected current material; map chapters/events to the blueprint rather than assuming completeness |

The blueprint is current but fast-moving interfaces require explicit checks for bundle names, monitoring terminology, Ray/Optuna integrations, online/on-demand features and serving traffic. No exact current Pluralsight, Udemy, LinkedIn Learning or MeasureUp product was independently verified.
