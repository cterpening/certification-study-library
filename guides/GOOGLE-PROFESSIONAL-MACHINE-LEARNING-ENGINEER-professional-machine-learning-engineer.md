---
exam_code: GOOGLE-PROFESSIONAL-MACHINE-LEARNING-ENGINEER
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/machine-learning-engineer
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Google Cloud Professional Machine Learning Engineer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#google-professional-machine-learning-engineer-coverage-record). The [official page](https://cloud.google.com/learn/certification/machine-learning-engineer) and its linked [June 1, 2026 guide](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf) are authoritative.

**Current baseline:** June 1, 2026; six domains weighted approximately 13%, 16%, 21%, 20%, 18%, and 13% (published approximations total 101%)<br>
**Published transition:** Google says the exam was updated for branding changes and the transition from Vertex AI to Gemini Enterprise Agent Platform. No future effective date is announced.<br>
**Official source:** [Professional Machine Learning Engineer](https://cloud.google.com/learn/certification/machine-learning-engineer) · [current detailed PDF](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf)

## How to use this guide

Study the production AI lifecycle: measurable task and harm → governed data → baseline/model/technique → repeatable experiment → training/evaluation → registry/release → serving → continuous quality/safety/cost monitoring → retraining or rollback. Compare conventional predictive ML, generative AI and deterministic systems; do not choose an LLM by default.

The exam is two hours, USD 200 before applicable tax or regional differences, 50–60 multiple-choice and multiple-select questions, English/Japanese, online or onsite. There is no formal prerequisite; Google recommends three or more years of industry experience including at least one year designing and managing Google Cloud solutions. Coding is not directly assessed, but the guide expects enough Python and SQL to interpret snippets. Verify the live page before scheduling.

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

Older resources say Vertex AI, Vertex AI AutoML/Workbench/Experiments/Pipelines/Feature Store/Model Registry/Prediction/Model Monitoring. The current exam guide uses Gemini Enterprise Agent Platform and shorter Agent Platform names. Learn the capability continuity but verify each current interface, availability and migration path.

---

## 1. Architecting low-code AI solutions — about 13%

Start from the decision/output, acceptable error, consequence, latency/volume, interpretability, data/modality, privacy, change rate, integration and budget. Create a simple baseline before a complex model.

BigQuery ML fits SQL-centered teams and data already governed in BigQuery. It supports classification, regression, forecasting, clustering and other model families, feature transformations, evaluation and prediction; choose algorithm and metric from the task. Agent Platform AutoML fits managed training where labeled data and supported modality/task align. Low-code reduces implementation burden, not data leakage, bias, evaluation or lifecycle responsibility.

Use specialized APIs such as Document AI, Vision or Translate when their managed task contract fits. Use Model Garden to compare Google, third-party and open models; evaluate license/provenance, modality/context, quality/safety, latency/throughput, cost, data terms, customization, region/stage and operations. Gemini handles multimodal language/reasoning use cases, Imagen image generation and Veo video generation. “Model as a service” reduces infrastructure work but not application/data governance.

Improve a Gemini application in order: clarify task/prompt/output schema → add authorized context/grounding → select model/settings → evaluate → optimize caching/batching/context/output tokens and serving → consider tuning only for a demonstrated stable behavior gap. Fine-tuning through BigQuery or Agent Platform needs representative governed examples, holdout evaluation, versioning and rollback. Optimize cost, latency and availability together; a smaller model may win for a bounded task.

> **Related item:** Retrieval supplies current or private facts at inference; fine-tuning changes learned behavior. Tuning is a poor substitute for frequently changing knowledge or permission-aware retrieval.

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

---

## 5. Automating and orchestrating pipelines — about 18%

An end-to-end pipeline ingests/version data → validates → transforms/features → trains/tunes → evaluates/slices → registers → approves → deploys/canaries → verifies → monitors. Components need typed contracts, idempotency, cache semantics, retry/timeout, isolated identity and lineage.

Agent Platform Pipelines/Kubeflow Pipelines provide managed pipeline patterns; Managed Service for Apache Airflow orchestrates DAGs/services; Ray on Agent Platform fits distributed Python/AI workloads. Choose by task semantics, integrations, state, team and operating burden—not because all three can schedule code.

Validate schema, ranges, missingness, distribution, leakage and privacy before training; validate model quality, robustness, safety, bias, explainability, latency/resource and packaging before promotion. Training-serving skew arises when feature logic, data availability or timing differs. Share versioned transformation code or contract and test offline versus online outputs.

CI tests code/config/infrastructure/components; CD promotes approved pipeline/model/application artifacts; CT retrains based on schedule/event/evidence. Retrain only when new representative labels/data, drift with impact, performance degradation, requirement change or planned cadence justifies it. Automatic retraining must still compare to incumbent, pass gates and permit rollback. Cloud Build or another controlled pipeline uses short-lived identity, signed/scanned artifacts, approvals and audit.

---

## 6. Monitoring AI solutions — about 13%

Monitor service health (availability, latency, throughput, errors, saturation), input/data (schema, missingness, ranges, drift, quality), model (task metric, calibration, slice fairness, attribution/explainability), gen AI (retrieval relevance, groundedness/faithfulness, task success, safety, citation/tool behavior), security/abuse and cost. Link alerts to owner, runbook and action.

Data drift changes input distribution; concept drift changes the relationship between input and target; training-serving skew is pipeline mismatch; feature-attribution drift changes how features influence predictions. None alone proves degradation. Join drift signals to delayed labels, slice metrics, business outcomes and causal investigation.

Agent Platform Model Monitoring can establish continuous evidence for supported models; define baseline, thresholds, slices, sampling, alert and response. Explainability/attribution helps understand influence, not causality or correctness.

Gen-AI monitoring needs versioned prompts/context/retrieval/model/settings/tools, traces, sampled privacy-safe review and continuous evaluation. Test prompt injection, data/model exfiltration, malicious inputs, sensitive disclosure, unsafe output and excessive tool action. Regex and safety filters cover bounded patterns; Model Armor may add supported inspection/protection. Enforce identity, authorization, data filters, schema/argument validation, allowlists/limits, human approval, sandboxing, audit and stop/reversal outside the prompt.

Responsible AI includes fairness, privacy, safety, transparency, accountability and human oversight. Define affected people and foreseeable misuse, evaluate representative slices and accessibility, document limitations, enable appeal/escalation and monitor real use. A better average metric can conceal increased harm.

---

## Integrated scenarios

### 1. Fraud model with delayed labels

Create time/entity-safe splits, BigQuery/Dataflow features with point-in-time correctness, a simple baseline and tuned model, slice/calibration/cost evaluation, registry approval and canary endpoint. Monitor latency/errors, feature freshness, drift and later-arriving fraud labels. Retrain only when evidence passes incumbent comparison; preserve rollback and decision thresholds owned by risk teams.

### 2. Multimodal product assistant

Compare specialized APIs and Gemini/Model Garden candidates. Build permission-aware product retrieval, version prompts/model/index, validate citations and tool calls, apply safety/PII controls, evaluate task/safety/latency/cost across languages, deploy canary and trace end-to-end. Keep pricing/eligibility and write actions in deterministic authorized services with limits/approval.

### 3. Prototype-to-accelerated training

Refactor a notebook into package/container/pipeline, version data and dependencies, establish CPU/GPU/TPU benchmarks, detect input bottleneck, tune with a fixed budget, checkpoint/recover distributed training, register with lineage, batch/online test, and monitor utilization/quality/cost. Scale only where measured time-to-quality or price-performance improves.

## Hands-on evidence path

1. Train/evaluate comparable BigQuery ML or low-code baselines for classification/forecasting and document metric/cost/interpretability choice.
2. Build a point-in-time feature dataset, simulate leakage/skew, and reconcile offline versus online features.
3. Convert a notebook into versioned package/container with pinned environment, tests, lineage and clean rerun.
4. Run custom training/tuning at small scale, inject data/dependency/quota failure and diagnose from evidence.
5. Benchmark CPU/GPU/TPU or simulated profiles; record utilization, throughput, convergence, cost and checkpoint strategy.
6. Register and serve batch/online versions; canary/A-B with rollback, private/public identity and load test.
7. Build an end-to-end pipeline with validation, approval, CI/CD/CT and incumbent comparison.
8. Monitor predictive and synthetic gen-AI workloads for quality/slices/drift/skew/security/safety/cost; trigger and execute a rollback.

## Original readiness checks

1. Why start with baseline? 2. BigQuery ML versus AutoML? 3. API versus foundation model? 4. Retrieval versus tuning? 5. What drives model selection? 6. How can feature store still leak? 7. What makes notebook reproducible? 8. What belongs in experiment lineage? 9. Why calibrate an LLM judge? 10. Aggregate metric risk? 11. ARIMA versus LLM task? 12. When custom training? 13. How diagnose training? 14. Why not tune test set? 15. CPU/GPU/TPU choice? 16. Data versus model parallelism? 17. Why can more accelerators be slower? 18. Batch versus online inference? 19. When custom container? 20. What does registry not prove? 21. Canary versus A/B? 22. Private endpoint limitation? 23. How prevent train/serve skew? 24. CI/CD/CT difference? 25. When retrain? 26. Why compare to incumbent? 27. Data drift versus concept drift? 28. Attribution versus causality? 29. What monitors gen AI? 30. Why is regex insufficient? 31. What controls agent tools? 32. What makes fairness evaluation useful? 33. Why monitor cost with quality? 34. What does current “Agent Platform” replace? 35. Why use the `_new.pdf`? 36. What makes an AI solution production-ready?

## Answer key

1. Establish minimum evidence and complexity justification. 2. SQL/data-local models versus managed supported-task training. 3. Narrow managed task contract versus flexible generative capability. 4. Current/private facts versus learned stable behavior. 5. Task/data/modality/quality/safety/latency/cost/license/operations. 6. Wrong timestamps or online/offline definitions. 7. Versioned code/data/config/dependencies/seed/environment and clean rerun. 8. All inputs, artifacts, versions, metrics/slices, cost and approvals. 9. Judges have bias/error and change. 10. It hides slices/failure types. 11. Structured time series versus language/generation. 12. Need framework/control/algorithm beyond low-code. 13. Data, code/container, identity/network, quota/hardware, numerical, outputs. 14. Evaluation leakage/overfitting. 15. Framework/model, memory/topology, availability, utilization and price-performance. 16. Replicated model with data shards versus model partition. 17. Communication/input overhead. 18. Throughput/delay-tolerant versus interactive latency. 19. Unsupported framework/runtime/server needs. 20. Approval/quality/safety/readiness. 21. Limit exposure versus measure alternative outcome. 22. It does not create application authorization. 23. Shared/versioned transformation contract and comparison tests. 24. Integrate/test, promote/deploy, retrain. 25. Evidence/labels/drift-impact/requirement or justified cadence. 26. New is not automatically better. 27. Input distribution versus input-target relationship. 28. Influence explanation versus causal proof. 29. Retrieval/grounding/task/safety/tool/version plus service and cost. 30. It covers known patterns, not semantic attacks/authorization. 31. Identity, permission filter, allowlist/schema, limits/approval, audit/reversal. 32. Representative affected slices, meaningful metric/threshold and action. 33. Optimization can degrade quality and uncontrolled use can explode cost. 34. Former Vertex AI capabilities under current branding. 35. It is the linked June 1, 2026 baseline; the older URL resolves to a different file. 36. Governed data/lineage, reproducible pipeline, evaluated release, secure scalable service, monitoring, owner and rollback/retraining.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Pick one route and use the June 2026 guide as the gap checklist. Times checked September 2, 2026; add coding, experiment, troubleshooting and review time.

| Resource | Access | Estimated time | Best use / currency note |
|---|---|---:|---|
| [June 1, 2026 official exam guide](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf) | Public | 1–2h then weekly | Authoritative current objectives and names |
| [Google Skills PMLE path](https://www.skills.google/paths/17) | Account; labs may require credits | 17 activities totaling about 57h45m | Modular first-party predictive ML, MLOps, gen AI and responsible-AI route |
| [Official sample questions](https://docs.google.com/forms/d/e/1FAIpQLSeYmkCANE81qSBqLW0g2X7RoskBX9yGYQu-m1TtsjMvHabGqg/viewform) | Public | 30–60m plus review | Official style; not a score predictor |
| [Preparing for Google Cloud ML Engineer](https://www.coursera.org/professional-certificates/preparing-for-google-cloud-machine-learning-engineer-professional-certificate) | Paid/subscription; audit varies | Six-course program; page estimate varies by pace, budget 40–80h | Coherent Google route; verify June branding and gen-AI scope |
| [Official Google Cloud Certified Professional Machine Learning Engineer Study Guide](https://www.oreilly.com/library/view/official-google-cloud/9781119944683/) | Paid O’Reilly | About 15–22h reading plus labs (2023, 480 pages) | Strong structured base; predates current Agent Platform/gen-AI depth |
| [Whizlabs Professional Machine Learning Engineer](https://www.whizlabs.com/google-cloud-certified-professional-machine-learning-engineer/) | Paid; free items may vary | Budget 25–45h across selected course/labs/practice and review | Commercial supplement; verify every explanation against current Google sources |
| [Google Cloud AI/ML documentation](https://cloud.google.com/docs/ai-ml) | Public | 15–40h targeted | Current capability, API, MLOps and responsible-AI details |

No current PMLE-specific MeasureUp or verified current Pluralsight path was located; neither is invented. Older courses require a gap check for Gemini Enterprise Agent Platform names, Model Garden and Gemini/Imagen/Veo, BigQuery Gemini tuning, LLM-as-judge, gen-AI evaluation/monitoring/security, Model Armor, Ray on Agent Platform, current Feature Store/Registry/Inference/Monitoring, responsible AI and accelerator/distributed-training scope.

## Source and freshness notes

- The official page’s linked `_new.pdf`, dated June 1, 2026, is the baseline. A different older PDF still resolves at the non-`_new` URL; this guide does not treat it as current.
- The live page’s two transition notices, high-level objectives and delivery facts were checked September 2, 2026.
- Models, names, APIs, regions, release stages, quotas, accelerators, prices, evaluation and safety practices change rapidly. Verify first-party documentation during practice.
- This is original public-source synthesis with no recalled item, dump, proprietary bank or copied course content.

> **Related items remain contextual:** The official June guide defines scope; related explanations connect it to sound production AI engineering.
