---
exam_code: GOOGLE-PROFESSIONAL-MACHINE-LEARNING-ENGINEER
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/machine-learning-engineer
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Google Cloud Professional Machine Learning Engineer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 29, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#google-professional-machine-learning-engineer-coverage-record). The [official page](https://cloud.google.com/learn/certification/machine-learning-engineer) and its linked [June 1, 2026 guide](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf) are authoritative.

**Current baseline:** June 1, 2026; six domains weighted approximately 13%, 16%, 21%, 20%, 18%, and 13% (published approximations total 101%)<br>
**Published transition:** Google says the exam was updated for branding changes and the transition from Vertex AI to Gemini Enterprise Agent Platform. No future effective date is announced.<br>
**Official source:** [Professional Machine Learning Engineer](https://cloud.google.com/learn/certification/machine-learning-engineer) · [current detailed PDF](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf)

## How to use this guide

Study the production AI lifecycle: measurable task and harm → governed data → baseline/model/technique → repeatable experiment → training/evaluation → registry/release → serving → continuous quality/safety/cost monitoring → retraining or rollback. Compare conventional predictive ML, generative AI and deterministic systems; do not choose an LLM by default.

The exam is two hours, USD 200 before applicable tax or regional differences, 50–60 multiple-choice and multiple-select questions, English/Japanese, online or onsite. There is no formal prerequisite; Google recommends three or more years of industry experience including at least one year designing and managing Google Cloud solutions. Coding is not directly assessed, but the guide expects enough Python and SQL to interpret snippets. Professional certifications are normally valid for two years according to the separate [official certification help](https://support.google.com/cloud-certification/answer/9750149?hl=en). The monitored PMLE page does not expose a validity field; that omission is not evidence of indefinite validity. Verify PMLE-specific renewal options and the live page before scheduling.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the published objectives.

## Objective map

| Domain | Weight | Production outcome |
|---|---:|---|
| Architecting low-code AI solutions | ~13% | Select BigQuery ML, AutoML, an API or foundation model from task evidence |
| Collaborating to manage data and models | ~16% | Teams share governed data/features, notebooks, experiments, artifacts and lineage |
| Scaling prototypes into ML models | ~21% | Training is reproducible, tuned, diagnosable and matched to hardware |
| Serving and scaling models | ~20% | Versioned models/features serve batch or online with controlled rollout |
| Automating and orchestrating ML pipelines | ~18% | Validation, preprocessing, CI/CD/CT and retraining are repeatable |
| Monitoring AI solutions | ~13% | Quality, drift, bias, security, gen-AI behavior, performance and cost drive action |

The September 29 review read all five pages of the dated PDF and mapped 52 considerations under 14 numbered objectives (9/10/12/10/5/6 by domain). The objective digest was unchanged. A missing lifecycle-monitor baseline was explicitly initialized after reviewing the current page; this is not a new exam announcement.

Older resources say Vertex AI, Vertex AI AutoML/Workbench/Experiments/Pipelines/Feature Store/Model Registry/Prediction/Model Monitoring. The current exam guide uses Gemini Enterprise Agent Platform and shorter Agent Platform names. Learn the capability continuity but verify each current interface, availability and migration path.

---

## 1. Architecting low-code AI solutions — about 13%

Start from the decision/output, acceptable error, consequence, latency/volume, interpretability, data/modality, privacy, change rate, integration and budget. Create a simple baseline before a complex model.

BigQuery ML fits SQL-centered teams and data already governed in BigQuery. It supports classification, regression, forecasting, clustering and other model families, feature transformations, evaluation and prediction; choose algorithm and metric from the task. Agent Platform AutoML fits managed training where labeled data and supported modality/task align. Low-code reduces implementation burden, not data leakage, bias, evaluation or lifecycle responsibility.

Use specialized APIs such as Document AI, Vision or Translate when their managed task contract fits. Use Model Garden to compare Google, third-party and open models; evaluate license/provenance, modality/context, quality/safety, latency/throughput, cost, data terms, customization, region/stage and operations. Gemini handles multimodal language/reasoning use cases, Imagen image generation and Veo video generation. “Model as a service” reduces infrastructure work but not application/data governance.

Improve a Gemini application in order: clarify task/prompt/output schema → add authorized context/grounding → select model/settings → evaluate → optimize caching/batching/context/output tokens and serving → consider tuning only for a demonstrated stable behavior gap. Fine-tuning through BigQuery or Agent Platform needs representative governed examples, holdout evaluation, versioning and rollback. Optimize cost, latency and availability together; a smaller model may win for a bounded task.

> **Related item:** Retrieval supplies current or private facts at inference; fine-tuning changes learned behavior. Tuning is a poor substitute for frequently changing knowledge or permission-aware retrieval.

### Keep transformations inside the model contract

For a SQL baseline, preserve the training query, split rule, feature schema and evaluated model version. A BigQuery ML model created with `TRANSFORM` accepts the required original feature columns at prediction; do not independently recreate transformed columns with different logic. Unused input columns can pass through prediction output without affecting the prediction, so their presence is not proof that the model used them. [ML.PREDICT input and TRANSFORM behavior](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict).

**PRACTICAL DEPTH:** Compare false-positive and false-negative cost before choosing a threshold. A probability of 0.5 is not a universal business decision boundary. Select the threshold on validation data, preserve it with the model, and use final test data for the agreed evaluation. A ranking score, a calibrated probability and an authorized action are three different contracts.

---

## 2. Collaborating to manage data and models — about 16%

### Data and features

Define source/owner, entity/event keys, timestamps, schema/semantics, classification/purpose, quality, lineage, freshness, retention and train/serve access. Split by entity/time where appropriate and prevent label leakage. Use in-memory Python for smaller interactive data, BigQuery SQL for warehouse-scale transformations, Dataflow for managed batch/stream, and Spark for its distributed ecosystem. Match tool to scale, transformations, team skills, reproducibility and serving consistency.

Agent Platform Feature Store consolidates and serves governed features. Define entity keys, feature semantics/owner, event timestamps, point-in-time correctness, offline/online consistency, freshness, skew and deletion. A feature store does not automatically prevent leakage.

Sensitive/PII handling includes minimization, authorized purpose, region, access, masking/tokenization, encryption, logs and deletion. Synthetic data can reduce exposure but may preserve sensitive patterns or distort distributions; validate it.

### Secure reproducible notebooks and experiments

Agent Platform Workbench and Colab Enterprise support managed notebooks. Treat a notebook as exploration, not a production artifact: pin dependencies, parameterize, move reusable code into packages, use source control, isolate identity/network, avoid embedded secrets, control data access, stop idle resources and reproduce from a clean environment.

PyTorch, scikit-learn and JAX suit different model/ecosystem needs; Model Garden prototypes still require license/security/evaluation review. Choose Experiments, Agent Platform Pipelines or Kubeflow Pipelines based on managed integration, framework and portability needs.

Track code/config, data/feature version, split, environment/container, model/base model, prompt/context/retrieval version, hyperparameters, seed, metric slices, artifacts, lineage, cost and approver. Predictive metrics depend on task: precision/recall/F1/ROC/PR, regression error, ranking or calibration. Generative evaluation combines deterministic checks, reference/task metrics, human/SME review and model judges. Calibrate judges against humans, detect bias/leakage and version judge/prompt. One aggregate score can hide harm to a subgroup or failure class.

> **Related item:** Reproducibility means rerunning the same lineage and obtaining meaningfully consistent evidence; determinism may be impossible on distributed/accelerated systems, so record acceptable variance.

### Latest serving values and historical training values

Current Feature Store uses BigQuery tables/views as its offline data source and materializes feature views for serving. Registered feature groups can use historical rows with feature timestamps; direct source-to-feature-view association requires one latest row per entity and does not support a historical time series. Check synchronization before assuming a newly written value is serving. [Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) and [source preparation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/prepare-data-source).

**VERIFY CURRENT:** Null behavior depends on configuration. Feature groups default to the latest non-null value, potentially returning an older value when the newest row is null. `dense=true` includes the newest null with scheduled synchronization; continuous synchronization retains the documented non-null behavior. A null marker therefore cannot be assumed to revoke a feature value. Test deletion and freshness against the selected serving mode. [Feature group null handling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/create-featuregroup).

**PRACTICAL DEPTH:** Reconstruct a training row using information available at the prediction time. A correction with event time Monday but arrival time Thursday was unavailable to a Tuesday prediction. Preserve event time and availability time; select versions satisfying both cutoffs. Separate entities across splits when entity memorization would inflate evaluation. Fit normalization/imputation/vocabulary on training data and reuse those fitted parameters unchanged on validation, test and serving inputs. Google's [dataset split guidance](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets) also warns that repeated decisions against a test set undermine its independence.

### Evaluate support as well as a score

Precision is `TP/(TP+FP)`; recall is `TP/(TP+FN)`. Report the denominator and an undefined result when it is zero. A subgroup with one positive example can show 100% recall while providing very weak evidence. Set minimum support and acceptable uncertainty before promotion; acquire representative evidence when a required slice is missing. Keep threshold-dependent metrics separate from threshold-sweeping ranking measures. [Google classification metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall).

---

## 3. Scaling prototypes into ML models — about 21%

Choose model type from signal and decision: simple linear/tree models for tabular interpretability/baselines, ARIMA-style methods for time-series structure, DNNs for learned complex representations, LLMs for language/generative tasks. Compare quality, data need, explainability, training/serving cost, latency, failure mode and maintenance. Select BigQuery ML, AutoML, custom training or pipelines by task/control/scale and team.

Organize tabular, text, speech, image and video data in Cloud Storage/BigQuery with schemas/metadata, immutable versions, lineage, access and lifecycle. A training job should take versioned inputs/config/code/container and emit model, metrics and metadata. Agent Platform custom training provides managed jobs; Kubeflow on GKE provides Kubernetes control; AutoML manages more of the process; Tabular Workflows supports managed tabular workflows.

Troubleshoot training by layer: data read/schema/quality → code/dependency/container → identity/network/KMS → quota/capacity/accelerator → CPU/GPU/TPU memory/communication → numerical convergence → output/metadata. Preserve logs/config and reproduce at small scale. Hyperparameter tuning needs defined search space, objective, budget, early stopping and untouched final test; repeated tuning against the test set leaks evaluation.

Foundation-model tuning is justified by stable style/format/domain behavior and sufficient representative data. Start with prompting/grounding and evaluate base versus tuned on quality, safety, latency and cost. Retain base/version/data/license lineage.

CPU fits preprocessing/smaller models; GPU fits many parallel neural workloads; TPU fits supported TensorFlow/JAX and large matrix workloads. Distributed data parallelism replicates model across data shards; model/tensor/pipeline parallelism partitions models that do not fit or need scale. Choose topology, interconnect/storage, precision, checkpointing, utilization, quota/capacity, fault recovery and price-performance. More accelerators can lose efficiency to communication or input bottlenecks.

---

## 4. Serving and scaling — about 20%

Batch inference fits high-volume, delay-tolerant processing and must version input/model/output. Online inference fits interactive latency and needs endpoint availability, autoscaling, warm capacity, timeouts/retries and dependency limits. Agent Platform managed serving shifts operations; Cloud Run fits containerized stateless inference; GKE fits Kubernetes/custom serving; edge fits locality/offline/latency/privacy needs but complicates fleet/version monitoring.

Use prebuilt containers when supported frameworks fit; custom containers when runtime/server/dependencies demand control. Minimize/harden/sign/scan images, run unprivileged, load model predictably and expose health/readiness. Preprocessing at serving must match training; postprocessing needs tested schema/business/safety rules.

Agent Platform Model Registry organizes version, lineage, evaluation and deployment status. Registration is not approval. Define promotion gates and model card/decision record. Canary limits traffic exposure; A/B testing compares user/business outcome under experimental design. Monitor guardrail, statistical power, assignment bias, rollback and data/schema compatibility.

Feature Store online serving needs entity correctness, freshness, capacity and offline-online consistency. Private endpoints fit controlled network paths; public endpoints still require authentication/authorization and abuse controls. Scale by throughput, latency, concurrency, payload, model load/memory, accelerator availability and downstream capacity. Benchmark realistic distributions. Quantization/distillation/batching/caching may improve serving but can change quality and safety; reevaluate.

> **Related item:** Model rollout and application rollout are coupled contracts. A model can be valid while an old client cannot parse its output, or vice versa.

### Container readiness and scaling evidence

For custom prediction containers, the server must keep running and listen on `0.0.0.0` at the configured port. Startup TCP liveness establishes connectivity; readiness must establish that the model can actually serve. Default HTTP health checks use status and response timing, ignoring the response body. A body saying “loading” with status 200 can falsely report readiness. Consecutive default health failures stop traffic routing; this mechanism does not itself restart the container. [Container requirements](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/custom-container-requirements).

**VERIFY CURRENT:** Dedicated online deployments default to a 60% CPU target without GPUs, or the higher CPU/GPU utilization with dedicated GPUs. An explicit CPU-only metric can miss a GPU bottleneck. Minimum/maximum replicas still depend on actual quota and capacity. Batch prediction uses its starting replica count and does not adopt online autoscaling. Current Scale To Zero is Preview, excludes shared public endpoints, and a request that triggers scale-up receives a dropped-request 429; design retry and latency behavior deliberately. [Autoscaling and Scale To Zero](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/autoscaling).

**PRACTICAL DEPTH:** Load-test the whole path, including feature fetch, tokenization, model load, inference and postprocessing. Measure tail latency at representative payload lengths, concurrency and warm/cold states. Keep an incumbent artifact, compatible feature transformation and application contract available for rollback. A successful resource operation or average GPU utilization cannot establish a user-facing latency objective.

---

## 5. Automating and orchestrating pipelines — about 18%

An end-to-end pipeline ingests/version data → validates → transforms/features → trains/tunes → evaluates/slices → registers → approves → deploys/canaries → verifies → monitors. Components need typed contracts, idempotency, cache semantics, retry/timeout, isolated identity and lineage.

Agent Platform Pipelines/Kubeflow Pipelines provide managed pipeline patterns; Managed Service for Apache Airflow orchestrates DAGs/services; Ray on Agent Platform fits distributed Python/AI workloads. Choose by task semantics, integrations, state, team and operating burden—not because all three can schedule code.

Validate schema, ranges, missingness, distribution, leakage and privacy before training; validate model quality, robustness, safety, bias, explainability, latency/resource and packaging before promotion. Training-serving skew arises when feature logic, data availability or timing differs. Share versioned transformation code or contract and test offline versus online outputs.

CI tests code/config/infrastructure/components; CD promotes approved pipeline/model/application artifacts; CT retrains based on schedule/event/evidence. Retrain only when new representative labels/data, drift with impact, performance degradation, requirement change or planned cadence justifies it. Automatic retraining must still compare to incumbent, pass gates and permit rollback. Cloud Build or another controlled pipeline uses short-lived identity, signed/scanned artifacts, approvals and audit.

### A cache hit is not a freshness check

Pipeline caching compares an interface built from input parameter values and artifact IDs, output definitions, and component image/command/arguments/environment. Only pipelines with the same name share the cache. The cached result has no TTL while its metadata entry remains. Components should be deterministic; task-level and whole-job caching can be disabled. [Execution caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-caching).

**PRACTICAL DEPTH — inference from that contract:** If an unchanged URI points to new bytes, the declared interface may not express the data change. Use immutable object generations/snapshots, explicit data fingerprints and image digests. Record fitted preprocessing with model artifacts. Disable caching for side-effecting or intentionally fresh steps and make retries idempotent; cache configuration does not make a deployment transaction atomic. Re-evaluate the exact artifact promoted, rather than retraining after approval and silently changing its bytes.

---

## 6. Monitoring AI solutions — about 13%

Monitor service health (availability, latency, throughput, errors, saturation), input/data (schema, missingness, ranges, drift, quality), model (task metric, calibration, slice fairness, attribution/explainability), gen AI (retrieval relevance, groundedness/faithfulness, task success, safety, citation/tool behavior), security/abuse and cost. Link alerts to owner, runbook and action.

Data drift changes input distribution; concept drift changes the relationship between input and target; training-serving skew is pipeline mismatch; feature-attribution drift changes how features influence predictions. None alone proves degradation. Join drift signals to delayed labels, slice metrics, business outcomes and causal investigation.

Agent Platform Model Monitoring can establish continuous evidence for supported models; define baseline, thresholds, slices, sampling, alert and response. Explainability/attribution helps understand influence, not causality or correctness.

Gen-AI monitoring needs versioned prompts/context/retrieval/model/settings/tools, traces, sampled privacy-safe review and continuous evaluation. Test prompt injection, data/model exfiltration, malicious inputs, sensitive disclosure, unsafe output and excessive tool action. Regex and safety filters cover bounded patterns; Model Armor may add supported inspection/protection. Enforce identity, authorization, data filters, schema/argument validation, allowlists/limits, human approval, sandboxing, audit and stop/reversal outside the prompt.

Responsible AI includes fairness, privacy, safety, transparency, accountability and human oversight. Define affected people and foreseeable misuse, evaluate representative slices and accessibility, document limitations, enable appeal/escalation and monitor real use. A better average metric can conceal increased harm.

### Select a monitoring version and a response

**VERIFY CURRENT:** Model Monitoring v1 is GA and configured on Agent Platform endpoints; v2 remains Preview and associates monitoring with a model version. Existing v1 users are not required to migrate, and concurrent operation can avoid gaps. V2 supports tabular models, including models served elsewhere through registry references; reference models do not support feature attribution monitoring. Its on-demand and scheduled jobs each execute a batch comparison. This is not a universal real-time LLM quality monitor. [Version overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview), [setup/support](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/set-up-model-monitoring), and [job execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/run-monitoring-job).

Choose a baseline, observation window, sampling strategy and alert threshold; monitor the monitoring job itself. Pair input/output/attribution distributions with eventual ground truth. An unchanged input histogram can coexist with reversed labels and collapsed accuracy. Drift should initiate diagnosis, label/data checks and candidate evaluation; it should not authorize automatic production replacement.

For generative systems, keep permission-aware retrieval and tool authorization outside the model. Model Armor requires an enforcement integration to block rejected content; inspection alone does not enforce policy. “Not used for training” does not establish zero retention across logging, grounding and stateful features. Verify the selected platform and feature. [Model Armor integration scope](https://docs.cloud.google.com/model-armor/integrations) and [Agent Platform retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention).

---

## Integrated scenarios

### 1. Fraud model with delayed labels

Create time/entity-safe splits, BigQuery/Dataflow features with point-in-time correctness, a simple baseline and tuned model, slice/calibration/cost evaluation, registry approval and canary endpoint. Monitor latency/errors, feature freshness, drift and later-arriving fraud labels. Retrain only when evidence passes incumbent comparison; preserve rollback and decision thresholds owned by risk teams.

### 2. Multimodal product assistant

Compare specialized APIs and Gemini/Model Garden candidates. Build permission-aware product retrieval, version prompts/model/index, validate citations and tool calls, apply safety/PII controls, evaluate task/safety/latency/cost across languages, deploy canary and trace end-to-end. Keep pricing/eligibility and write actions in deterministic authorized services with limits/approval.

### 3. Prototype-to-accelerated training

Refactor a notebook into package/container/pipeline, version data and dependencies, establish CPU/GPU/TPU benchmarks, detect input bottleneck, tune with a fixed budget, checkpoint/recover distributed training, register with lineage, batch/online test, and monitor utilization/quality/cost. Scale only where measured time-to-quality or price-performance improves.

## Executed local training and evaluation workbook

**PRACTICAL DEPTH — executed September 29, 2026:** This original Python program actually fits a one-feature logistic classifier by gradient descent on 120 synthetic rows. It fits normalization on training data, selects one of five thresholds on 30 validation rows with fictional cost `FP + 4*FN`, serializes the fitted model/transform/threshold and fingerprints, and only then reports 30 held-out rows. Separate counterexamples demonstrate a subgroup regression and concept drift with identical input distributions. No packages, credentials, network, cloud jobs or files are needed.

The run completed **36 local checks**. It selected threshold **0.35**, training log loss approximately **0.1934**, validation cost **4**, and held-out cost **2** (13 TP, 15 TN, 2 FP, 0 FN). Held-out accuracy was 28/30. Slice B had only six rows and one positive: its perfect score does not establish adequate support for release. A separate fixture improves aggregate accuracy from 82% to 90% while reducing slice B recall from 100% to zero; the stated slice gate rejects it.

These are synthetic teaching results, not a benchmark, calibration guarantee or production approval. The artificial interleaved split does not implement real temporal/entity splitting. The gate's five-positive minimum and 0.8 recall floor are illustrative, not statistical assurance. The code is intentionally small: it lacks production input validation, regularization, cross-validation, confidence intervals and a real feature pipeline. Exact repeated fitting on this runtime does not promise deterministic distributed accelerator training. Checks include structural assertions as well as experiments; there are not 36 independently validated cloud capabilities.

Save as `pmle_workbook.py` and run with Python 3. Do not use `python -O` as a general testing practice; this workbook's explicit checks remain enabled either way.

```python
"""Original, deterministic synthetic experiment; Python standard library only."""
import hashlib
import json
import math
from collections import Counter


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    allow_nan=False).encode()).hexdigest()


def sigmoid(value):
    if value >= 0:
        return 1 / (1 + math.exp(-value))
    e = math.exp(value)
    return e / (1 + e)


def fit(rows, steps=1200, rate=0.15):
    mean = sum(r['x'] for r in rows) / len(rows)
    scale = math.sqrt(sum((r['x'] - mean)**2 for r in rows) / len(rows))
    if not scale:
        raise ValueError('constant feature')
    weight = bias = 0.0
    for _ in range(steps):
        dw = db = 0.0
        for r in rows:
            z = (r['x'] - mean) / scale
            error = sigmoid(weight*z + bias) - r['y']
            dw += error*z
            db += error
        weight -= rate*dw / len(rows)
        bias -= rate*db / len(rows)
    return dict(mean=mean, scale=scale, weight=weight, bias=bias,
                steps=steps, rate=rate, training_sha256=digest(rows))


def probability(model, x):
    return sigmoid(model['weight']*(x-model['mean'])/model['scale']
                   + model['bias'])


def loss(model, rows):
    total = 0.0
    for r in rows:
        p = min(1-1e-12, max(1e-12, probability(model, r['x'])))
        total -= r['y']*math.log(p) + (1-r['y'])*math.log1p(-p)
    return total / len(rows)


def metrics(labels, predicted):
    if len(labels) != len(predicted) or any(v not in (0, 1)
            for v in labels + predicted):
        raise ValueError('expected aligned binary labels')
    n = len(labels)
    tp = sum(y == p == 1 for y, p in zip(labels, predicted))
    tn = sum(y == p == 0 for y, p in zip(labels, predicted))
    fp = sum(y == 0 and p == 1 for y, p in zip(labels, predicted))
    fn = sum(y == 1 and p == 0 for y, p in zip(labels, predicted))
    return dict(n=n, tp=tp, tn=tn, fp=fp, fn=fn,
                precision=tp/(tp+fp) if tp+fp else None,
                recall=tp/(tp+fn) if tp+fn else None,
                accuracy=(tp+tn)/n if n else None,
                cost=fp+4*fn)


def evaluate(model, rows, threshold):
    return metrics([r['y'] for r in rows],
                   [int(probability(model, r['x']) >= threshold) for r in rows])


checks = 0


def check(condition):
    global checks
    if not condition:
        raise AssertionError('experiment check failed')
    checks += 1


def rejects(function):
    try:
        function()
    except ValueError:
        check(True)
    else:
        check(False)


# Unique rows in an artificial, interleaved split; not a real temporal split.
rows = []
for i in range(180):
    x = (i % 31 - 15)/5 + (i//31)*0.013
    rows.append(dict(id=i, x=x, y=int(x+((i*7) % 9-4)*0.25 > 0.35),
                     slice='B' if i % 5 == 0 else 'A'))
train = [r for r in rows if r['id'] % 3 != 0]
valid = [r for r in rows if r['id'] % 6 == 0]
test = [r for r in rows if r['id'] % 6 == 3]
for left, right in ((train, valid), (train, test), (valid, test)):
    check({r['id'] for r in left}.isdisjoint(r['id'] for r in right))
check(len(train)+len(valid)+len(test) == len(rows))
check(len({r['x'] for r in rows}) == len(rows))
model = fit(train)
check(model['scale'] > 0)
check(loss(model, train) < math.log(2))
check(model['weight'] > 0)
check(fit(train) == model)
rejects(lambda: fit([dict(x=1, y=0), dict(x=1, y=1)]))

# Changing future/held-out values would contaminate a pooled normalizer.
contaminated_mean = (sum(r['x'] for r in train)
                     + sum(r['x']+1000 for r in valid)) / (len(train)+len(valid))
check(abs(contaminated_mean-model['mean']) > 100)
candidates = (0.2, 0.35, 0.5, 0.65, 0.8)
threshold = min(candidates, key=lambda t: (evaluate(model, valid, t)['cost'],
                                          abs(t-0.5), t))
check(evaluate(model, valid, threshold)['cost']
      <= evaluate(model, valid, 0.5)['cost'])
artifact = dict(schema=['x:float'], preprocessing_and_model=model,
                threshold=threshold, false_positive_cost=1,
                false_negative_cost=4, validation_sha256=digest(valid))
encoded = json.dumps(artifact, sort_keys=True, allow_nan=False)
restored = json.loads(encoded)
check(restored == artifact)
check([probability(restored['preprocessing_and_model'], r['x']) for r in test]
      == [probability(model, r['x']) for r in test])
check(digest(artifact) != digest({**artifact, 'threshold': threshold+0.01}))
check(model['training_sha256'] != digest(train[:-1]))

# Only now expose final held-out results; do not use these to retune this run.
test_result = evaluate(model, test, threshold)
slice_results = {s: evaluate(model, [r for r in test if r['slice'] == s], threshold)
                 for s in ('A', 'B')}
check(sum(r['n'] for r in slice_results.values()) == len(test))
check(sum(r['cost'] for r in slice_results.values()) == test_result['cost'])
check(0 <= test_result['accuracy'] <= 1)
known = metrics([0, 0, 1, 1], [0, 1, 0, 1])
check([known[k] for k in ('tn', 'fp', 'fn', 'tp')] == [1, 1, 1, 1])
check(known['precision'] == known['recall'] == known['accuracy'] == 0.5)
check(metrics([0, 1], [0, 0])['precision'] is None)
check(metrics([0, 0], [0, 1])['recall'] is None)
check(metrics([], [])['accuracy'] is None)
rejects(lambda: metrics([1], []))
rejects(lambda: metrics([2], [1]))

# Separate prediction fixtures: more total correct can hide total slice failure.
truth = [1]*100
baseline = [1]*72 + [0]*18 + [1]*10
candidate = [1]*90 + [0]*10
check(metrics(truth, candidate)['accuracy'] > metrics(truth, baseline)['accuracy'])
check(metrics(truth, candidate)['cost'] < metrics(truth, baseline)['cost'])
check(metrics(truth[90:], baseline[90:])['recall'] == 1)
check(metrics(truth[90:], candidate[90:])['recall'] == 0)


def promotion_allowed(labels, predictions):
    # Explicit toy gate: at least 5 positive labels and recall >= .8 per slice.
    for start, stop in ((0, 90), (90, 100)):
        m = metrics(labels[start:stop], predictions[start:stop])
        if m['tp']+m['fn'] < 5 or m['recall'] is None or m['recall'] < 0.8:
            return False
    return True


check(promotion_allowed(truth, baseline))
check(not promotion_allowed(truth, candidate))
check(not promotion_allowed([], []))

# Identical inputs, inverted labels: an input-only drift check cannot see this.
old_x = [-2, -1, 1, 2]
new_x = list(old_x)
predictions = [int(x > 0) for x in old_x]
check(Counter(old_x) == Counter(new_x))
check(metrics([0, 0, 1, 1], predictions)['accuracy'] == 1)
check(metrics([1, 1, 0, 0], predictions)['accuracy'] == 0)
print(json.dumps(dict(threshold=threshold, train_loss=loss(model, train),
                      validation=evaluate(model, valid, threshold),
                      test=test_result, test_slices=slice_results), sort_keys=True))
print(f'{checks} local checks passed')
```

## Proposed cloud labs and evidence

These eight labs are **not executed in this review**. Use a disposable authorized project with a stated budget, synthetic data and named cleanup owner. Existing same-session evidence found no `gcloud` on PATH; no installation, authentication or cloud provisioning was attempted.

| Lab | Build and deliberate failure | Required evidence and cleanup |
|---|---|---|
| 1. SQL/low-code baseline | Compare a BigQuery ML baseline and an eligible AutoML task; preserve training split and transformation. Change a serving input type and test rejection. | Query/model versions, task metrics and FP/FN cost, held-out results, job cost; remove trial models/tables. |
| 2. Historical versus online features | Build synthetic late corrections, historical cutoffs and a current feature view. Introduce duplicate entity rows, stale synchronization and latest-null cases. | Expected/actual feature rows, availability timestamps, sync state and null behavior; remove online resources and trial source tables. |
| 3. Notebook to repeatable training | Move notebook logic into a versioned package/container with explicit dependency and data fingerprints. Attempt a clean rerun and a missing-dependency run. | Environment digest, experiment lineage, logs and reproducibility tolerance; stop/delete notebook resources and trial artifacts. |
| 4. Custom training/tuning | Compare bounded hyperparameter candidates using validation only. Inject malformed input or missing artifact-read permission in a disposable identity. | Failure stage, least-privilege correction, final held-out evaluation and trial budget; terminate jobs and remove temporary access. |
| 5. Hardware/checkpoint experiment | Benchmark a justified CPU/GPU/TPU option at small scale and interrupt an authorized trial after a checkpoint. | Input/compute/communication timings, time-to-quality, restored optimizer/model state and cost; stop jobs and release accelerator resources. |
| 6. Serving and release | Package an eligible custom container, test readiness during model load, serve batch/online, and canary a compatible new version. Exercise rollback and quota/latency limits. | Status/traffic evidence, model and transform digests, tail latency and rollback result; undeploy trial versions and remove endpoints. |
| 7. Pipeline and cache | Build validate/train/evaluate/register/promote components. Change a dataset fingerprint, repeat the run and test failed quality gates and idempotent retry. | Cache-hit/miss lineage, immutable inputs, blocked promotion, artifact-bound approval and recovery evidence; remove schedules and trial artifacts. |
| 8. Monitoring and generative safety | Configure a supported tabular monitor; inject drift and delayed labels. Separately test a synthetic assistant's permission-aware retrieval and enforcement integration. | Job execution/alert evidence, slice/ground-truth evaluation, blocked unauthorized actions and rollback; remove monitors, schedules, endpoints and temporary data. |

## Original readiness checks with answers

The following are original explanations, not recalled or predicted exam questions.

1. **Why start with a baseline?** It gives a measured quality, cost and interpretability reference; added complexity must justify its operational burden.

2. **When does BigQuery ML fit?** When warehouse data, SQL skills and supported model/task capabilities fit; preserve feature transformations and evaluated model version.

3. **Does AutoML remove data responsibilities?** No. Labels, leakage, representative evaluation, privacy and rollout remain your responsibility.

4. **When choose an industry API?** When its supported task contract meets quality, latency and governance needs with less custom model work.

5. **Retrieval or tuning for changing private facts?** Use authorized retrieval for current facts; tuning may improve learned behavior but cannot implement access control.

6. **What should Model Garden selection record?** Exact model/license, provenance, modality, evaluation, cost/latency, deployment support and data-handling terms.

7. **Which data processing tool should you choose?** Match scale, transformations, existing data location and team operation to Python, SQL, Dataflow or Spark; verify the resulting contract.

8. **Why track availability as well as event time?** A backdated correction can be unavailable at prediction time even when its event timestamp precedes the cutoff.

9. **Why fit normalization only on training data?** Held-out distribution information would otherwise influence the fitted pipeline and undermine evaluation independence.

10. **Does the latest online feature reconstruct a past prediction?** No. Historical training needs version selection at the past cutoff and knowledge of data availability.

11. **Does a latest null necessarily erase an online feature?** No. Default non-null serving can use an older value; verify dense configuration and sync mode.

12. **Can a direct feature-view source contain historical duplicates?** The documented direct association requires one latest row per entity; registered time-series feature groups have a different contract.

13. **What makes notebooks reproducible?** Pinned code/environment and immutable inputs, reusable packaged transformations, explicit identity and a successful clean run.

14. **What belongs in experiment lineage?** Data/split/feature and code versions, image, model/prompt/retrieval versions, parameters, seed, metrics/slices, artifacts and cost.

15. **Why calibrate an LLM judge?** Its preferences and errors can distort evaluation; compare with human/SME judgments and version its model and rubric.

16. **Why report slice support?** A perfect result from one positive case gives weak evidence; missing or tiny slices need more representative evaluation.

17. **Why does threshold 0.5 need justification?** Error costs and operating constraints vary; choose on validation and freeze the threshold with the model.

18. **What is precision with no predicted positives?** Its denominator is zero; report undefined with counts rather than substituting a reassuring perfect score.

19. **ARIMA, small tabular model or LLM?** Choose from the data structure and task, comparing baseline quality, interpretation, latency and ongoing cost.

20. **When use custom training?** When model, loss, data flow or runtime requirements need control beyond supported managed low-code options.

21. **How do you diagnose a training failure?** Identify the failing layer: inputs/schema, code/dependency, identity/network, capacity, memory/communication, numerical behavior or artifact output.

22. **Why keep a final test set untouched?** Repeatedly selecting features or hyperparameters from its results implicitly trains to that evidence.

23. **What justifies foundation-model tuning?** A stable measured behavior gap, representative authorized examples, and improved held-out quality/safety/cost compared with simpler interventions.

24. **How choose training hardware?** Benchmark the supported workload and input pipeline for time-to-quality and cost, including memory, communication and availability.

25. **Data parallelism versus model parallelism?** Replicate a model over data shards versus partitioning model computation/state; synchronization and memory tradeoffs differ.

26. **Why can more accelerators be slower?** Input starvation, communication, synchronization or small per-device work can dominate useful computation.

27. **What must a recovery checkpoint preserve?** Enough model, optimizer and progress state to resume the intended training semantics; validate with an actual interrupted trial.

28. **Batch or online serving?** Choose from latency and volume; batch is delay-tolerant processing, while online must sustain the request path and its latency budget.

29. **What does container TCP liveness prove?** Connectivity to the port, not that the model is loaded and ready to predict.

30. **Does default health failure automatically restart a container?** The documented default health mechanism removes it from routing and probes for recovery; startup liveness has separate restart behavior.

31. **What does Model Registry not prove?** Registration alone proves neither business approval nor adequate validation, compatibility or safe deployment.

32. **Canary versus A/B test?** A canary limits rollout exposure; A/B estimates comparative outcomes under an appropriate experiment design.

33. **Why can CPU-only scaling miss overload?** GPU or queue pressure can rise while CPU remains low; select metrics from the actual bottleneck and latency evidence.

34. **Can batch prediction borrow online autoscaling assumptions?** No. Current batch behavior uses starting replicas rather than the online autoscaling contract.

35. **What changes with Scale To Zero?** Current Preview endpoint restrictions and dropped-request 429 during scale-up require explicit retry, latency and support decisions.

36. **Does a private endpoint replace identity controls?** No. Network reachability, caller authorization and application-level data/tool permissions remain distinct.

37. **How prevent training-serving skew?** Reuse fitted, versioned preprocessing and compare actual offline/online features, timing, missing-value and schema behavior.

38. **What makes a pipeline cache hit valid?** The declared interface must capture every meaningful input and deterministic component version; the cache has no automatic TTL.

39. **Why is a stable URI insufficient lineage?** Its bytes may change without changing the declared parameter; use immutable versions and fingerprints.

40. **CI, CD and CT?** CI validates changes, CD promotes controlled artifacts, and CT trains candidates; candidate generation must not bypass promotion gates.

41. **When should retraining trigger deployment?** Only after representative evaluation, incumbent comparison, required gates and compatible rollback preparation.

42. **Data drift versus concept drift?** Input distributions versus the input/target relationship; identical inputs can still accompany changed labels and failing predictions.

43. **Why does attribution not establish causality?** It describes a model-specific contribution to prediction, not the outcome of an intervention in the world.

44. **Which monitoring version should you select?** Check support and deployment needs: v1 GA on endpoints versus v2 Preview tied to model versions with current tabular support.

45. **Are scheduled v2 jobs real-time LLM evaluation?** No. Each is a batch execution for supported tabular monitoring; generative evaluation requires additional evidence.

46. **Why is a regex or inspection result insufficient for tool safety?** Pattern detection cannot establish permission; an enforcement layer must validate the current caller, resource, arguments and allowed effect.

47. **Does no-training mean zero retention?** No. Review the exact API/platform and logging, grounding and stateful feature retention terms.

48. **What proves this review is cloud-ready?** Nothing yet: 36 local checks and source review are completed evidence; the eight cloud labs and independent human review remain pending.

## Source and freshness notes

**CURRENT BLUEPRINT:** The five-page exam PDF prints June 1, 2026 and uses the six domains shown above. Published approximate weights total 101%; do not normalize them into invented exact weights. The canonical page describes an already-completed branding update, not a future transition. The current objective digest is unchanged. Lifecycle monitoring had no prior baseline; initialization and a subsequent unchanged check are recorded separately.

The [deep review](../docs/research/2026-09-29-google-professional-machine-learning-engineer-deep-review.md) records source-reading limits, current public catalog observations, actual PDF receipt, local execution, and blocked live-cloud validation. The [April 22, 2026 announcement](https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development) provides product context; product marketing does not independently change the exam objectives. **VERIFY CURRENT:** models, features, regions, quotas, Preview support, retention, pricing, catalog composition and interfaces.

Only public primary documentation and public provider catalog pages were reviewed. No paid course interiors, proprietary assessments, recalled exam content or real customer data were accessed. Public sample-question access reached a form shell; it did not establish question-content coverage. Human review remains pending.

## Places to learn

This is **not a complete list**. Catalog observations below are from September 29, 2026. Durations are provider metadata unless explicitly described as a suggested practice budget. A certificate/path title does not prove complete June 2026 blueprint coverage.

| Resource | Access | Estimated time |
|---|---|---|
| [Google Skills Machine Learning Engineer path](https://www.skills.google/paths/17) | Public outline; individual activities can require access/credits. Current page exposes 17 activities and a relative two-month update, without activity durations. | Current duration unverified; the earlier 57h45 estimate is not reconfirmed. Add time for repeat labs and evidence. |
| [Google Cloud Training on Coursera](https://www.coursera.org/professional-certificates/preparing-for-google-cloud-machine-learning-engineer-professional-certificate) | Public outline; enrollment/subscription terms vary. Current two cards are Production Machine Learning Systems (15h) and MLOps: Getting Started (4h). | Cards total **19h**. Landing page says two months at 10h/week; FAQ says six months at 5h/week and refers to a starting course absent from the cards. These are inconsistent estimates, not additive requirements. |
| [Pluralsight PMLE path](https://www.pluralsight.com/paths/google-cloud-professional-machine-learning-engineer-by-pluralsight) | Public metadata, paid learning. Six courses by Victor Dantas and Abhishek Kumar, dated February–June 2026; path still marked in production. | Listed durations 60/80/58/120/73/55 minutes total **7h26**, versus rounded 7h header. No paid lesson or practice-exam quality claim. |
| [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets) | Free primary teaching on splits and [classification metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall). Use for foundations alongside the cloud blueprint. | Suggested practice budget: 2–4h on these concepts and the original workbook; not a provider course duration. |
| [Whizlabs PMLE](https://www.whizlabs.com/google-cloud-certified-professional-machine-learning-engineer/) | The current fetch returned an empty readable body. Course, lab and practice-question contents were not reviewed. | Current duration, depth and update status unverified. |
| [O’Reilly reference](https://www.oreilly.com/library/view/official-google-cloud/9781119944683/) | Current access returned HTTP 403; any older title/date/page count needs direct verification. No book interior read. | Current reading time and blueprint fit unverified. |
| This guide, official product documentation and proposed labs | Public explanation and executable synthetic workbook; cloud labs require an authorized budgeted environment. | Suggested 16–24h for lab execution, fault diagnosis and written evidence after prerequisites; not a claim of exam readiness. |

Use an outline-based gap map: learning resource → current objective → explanation → executed evidence. No PMLE-specific MeasureUp catalog was verified in this review; that is a research limit, not proof of absence. Supplement any resource where the public outline does not establish coverage.
