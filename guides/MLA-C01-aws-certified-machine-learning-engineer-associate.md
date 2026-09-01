---
exam_code: MLA-C01
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: retirement-announced
upcoming_change_checked: 2026-09-01
---

# MLA-C01 AWS Certified Machine Learning Engineer - Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, transition warnings, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mla-c01-coverage-record). The [official MLA-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html) is authoritative.

**Current baseline:** MLA-C01, four scored domains, 50 scored plus 15 unidentified unscored questions, and a 720 minimum scaled score<br>
**Upcoming blueprint change:** **Retirement announced. September 28, 2026 is the last day to take MLA-C01 in English.** AWS says Korean, Japanese, and Simplified Chinese remain available until MLA-C02 reaches general availability. Registration for MLA-C02 opens September 1; its English-only beta delivery code is **ME1-C02**, with delivery beginning September 29. Verify the live [certification page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) before booking.<br>
**Replacement:** [MLA-C02 study guide](MLA-C02-aws-certified-machine-learning-engineer-associate.md), which links its official blueprint. New learners should normally prepare for MLA-C02. This page exists for candidates already scheduled for C01 and for historical/reference use; passing C01 earns the certification, not an automatic exam-version conversion.<br>
**Important freshness boundary:** MLA-C01 emphasizes traditional ML engineering and MLOps, with limited foundation-model selection/fine-tuning context. MLA-C02 explicitly adds generative AI, Amazon Bedrock, foundation-model development, agentic workflows, and their operations. Do not assume a C01 course covers C02 merely because the credential name is unchanged.<br>
**Official source:** [AWS Certified Machine Learning Engineer - Associate exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html)

## How to use this guide

MLA-C01 validates the ability to build, operationalize, deploy, monitor, maintain, and secure ML solutions and pipelines on AWS. AWS targets someone with at least one year using SageMaker and related AWS services plus experience in a role such as backend development, DevOps, data engineering, MLOps, or data science. The target is an implementer working within an architecture—not the person defining an enterprise-wide ML strategy or deeply specializing in multiple ML fields.

The live page lists a 130-minute, 65-question, USD 150 exam. The detailed guide identifies multiple-choice, multiple-response, ordering, and matching items; 50 are scored and 15 unscored items are not identified. Recheck delivery, price, language, scheduling, and transition details immediately before booking.

Use this page in one of two ways:

- **Already booked for C01:** map each weak area to the objective table, do the labs, then use original practice questions to test decisions rather than definitions.
- **Not yet booked:** read the transition section, move to MLA-C02, and use only the enduring C01 material—data quality, traditional ML, SageMaker lifecycle, deployment, monitoring, security, and cost—as foundation.

For every scenario, identify:

1. the business prediction, latency, scale, explainability, cost, and compliance contract;
2. data source, format, arrival pattern, label quality, leakage, bias, and train/serve consistency;
3. algorithm or managed AI service, training strategy, metric, baseline, and approval evidence;
4. batch, asynchronous, serverless, real-time, multi-model, container, or edge delivery target;
5. orchestration, versioning, tests, deployment safety, monitoring, retraining, rollback, and ownership;
6. identities, network paths, encryption boundaries, logs, quotas, and cost controls.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the objective easier to reason about. It is supporting knowledge, not a claim that the item appears verbatim in the official outline.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Data Preparation for Machine Learning | 28% | How should data be ingested, stored, transformed, validated, protected, and made reproducible for training? |
| ML Model Development | 26% | Which approach, algorithm, training method, tuning process, metric, and evidence fit the problem? |
| Deployment and Orchestration of ML Workflows | 22% | How should a model be packaged, provisioned, released, scaled, automated, tested, and rolled back? |
| ML Solution Monitoring, Maintenance, and Security | 24% | How are drift, service health, cost, access, networking, audit, and retraining controlled in production? |

---

## 1. Data Preparation for Machine Learning — 28%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html) covers ingestion and storage, transformation and feature engineering, and data integrity/readiness.

### Frame the data contract before choosing a service

A useful design begins with grain: what does one row, record, image, sequence, or event represent? Record the prediction timestamp, label definition, entity key, source-of-truth owner, arrival delay, retention, region, classification, and expected volume. Then decide batch versus stream and choose storage/processing from the access pattern.

| Need | Common fit | Decision boundary |
|---|---|---|
| Durable data lake and training artifacts | Amazon S3 | Object storage; design prefixes/partitions, formats, lifecycle, versioning, encryption, and access separately |
| Shared POSIX file access | EFS | Elastic shared file system; useful only when file semantics are required |
| High-performance managed file system | FSx family | Select the exact file system from workload/protocol/performance requirements |
| Relational operational source | RDS/Aurora | Preserve transactional workload; extract deliberately rather than training against production indiscriminately |
| Key-value operational source | DynamoDB | Export/stream from access patterns; do not scan a hot production table casually |
| Batch discovery and transformation | Glue, EMR/Spark, SageMaker Processing/Data Wrangler | Choose visual versus code, serverless versus cluster, scale, libraries, lineage, and operational ownership |
| Ordered, replayable event stream | Kinesis or managed Kafka path | Define partitioning, retention, checkpoint, late/duplicate events, schema, and backpressure |
| Reusable online/offline features | SageMaker Feature Store | Define event time, record identifier, online/offline need, ownership, freshness, and point-in-time behavior |

CSV and JSON are easy to inspect and exchange but can be verbose and weakly typed. Parquet and ORC are columnar, compressed, and efficient when analytics or training reads a subset of columns. Avro is row-oriented with schema-evolution strengths for event/data exchange. RecordIO variants can optimize specific training paths. Compression saves storage and transfer but changes splittability and CPU cost. A format answer is correct only when it matches producer, reader, schema, query, and parallelism requirements.

For batch ingestion, make each run idempotent: immutable landing objects, a run or snapshot identifier, schema validation, checkpoints/manifests, deterministic outputs, and atomic publication where possible. For streams, define event time versus processing time, partition key, duplicate/out-of-order policy, watermark/window, checkpoint, replay, and poison-record destination. Capacity failures are not just a service-sizing problem; small files, skew, hot keys, inefficient serialization, and unbounded consumers can create them.

**Related item:** A data lake is not automatically a governed training dataset. Raw, curated, feature, label, and prediction data need explicit contracts, lineage, access, retention, and reproducibility.

### Transform without creating leakage or skew

Data preparation includes type coercion, deduplication, missing-value treatment, outlier decisions, normalization/standardization, binning, transformations, categorical encoding, tokenization, image/audio processing, and feature creation. Fit stateful transformations on training data only, persist their parameters, and apply the same transformation artifact to validation, test, and inference data.

Data leakage occurs when training uses information unavailable at prediction time or learns from the evaluation set. Common forms include future events in a random time split, target-derived features, normalization fitted on the entire dataset, duplicate entities across train/test, and joins that select a later record. Choose random, stratified, grouped, or time-based splits from the deployment reality. Keep a final test set isolated from iterative tuning.

Feature Store can help maintain training/serving consistency, but it does not repair a bad definition. For every feature, record entity, event time, computation version, source, owner, freshness SLA, default/null semantics, sensitive classification, online/offline availability, and point-in-time retrieval rule. “Latest value” is often wrong for historical training because it leaks future information.

Use Glue Data Quality or equivalent assertions to test schema, completeness, uniqueness, validity, distribution, freshness, and referential expectations. Quarantine failing data instead of silently coercing it. Publish counts and distributions by meaningful slices so a globally healthy average cannot hide a broken source, region, or customer segment.

### Protect integrity, privacy, and fairness

Class imbalance means labels are uneven; selection bias means the sample does not represent the target population; measurement bias means collection/labeling systematically distorts reality. These require different responses. Resampling, class weights, synthetic data, threshold changes, and targeted collection can address imbalance, but none proves fairness. Evaluate impact by relevant subgroups and connect every mitigation to the intended use and error cost.

SageMaker Clarify can calculate pre-training bias metrics and later analyze model bias/explanations. A metric is evidence, not a verdict: confirm label meaning, favorable outcome, facet definition, sample size, and acceptable thresholds with domain owners. Maintain approval and limitation records.

Classify PII, PHI, secrets, confidential business data, licensed data, and residency constraints before moving it. Minimize collection; mask, tokenize, anonymize, or aggregate only with a threat model. Encrypt objects, volumes, databases, file systems, channels, and artifacts as required, and ensure principals can use both the data resource and KMS key. Restrict cross-account and training-role access; retain lineage and audit events without leaking sensitive payloads into logs.

**Related item:** De-identification is contextual. Removing names does not make a high-dimensional dataset anonymous if combinations of remaining fields can re-identify people.

---

## 2. ML Model Development — 26%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html) covers approach selection, training/refinement, and performance analysis.

### Choose the least complex approach that meets the contract

First ask whether ML is warranted. Deterministic rules, search, analytics, optimization, or a managed AI API may meet the need with less data and operational risk. If ML fits, frame the target:

- classification predicts a class or probability;
- regression predicts a continuous value;
- ranking orders alternatives;
- forecasting predicts a time-indexed quantity;
- clustering/embedding/anomaly detection discovers structure without conventional labels;
- computer vision, NLP, speech, translation, recommendations, and foundation-model use cases have specialized services and evaluation needs.

Managed services such as Transcribe, Translate, Rekognition, Comprehend, Personalize, or Bedrock can reduce model ownership when their contract fits. SageMaker built-in algorithms provide managed containers and documented input/hyperparameter behavior. Framework containers support TensorFlow, PyTorch, scikit-learn, XGBoost, and other supported stacks. Script mode supplies training code to a managed framework image; bring-your-own-container is appropriate when runtime, system libraries, or serving behavior require control. JumpStart provides models and solution starting points. Verify licenses, regions, data handling, and current support.

Algorithm choice depends on target, data type and size, linear/nonlinear relationships, sparsity, class balance, missing values, explainability, training/inference cost, latency, update frequency, and team skill. Begin with a meaningful baseline—business rule, naive predictor, simple linear/tree model—so complexity has something to beat.

**Related item:** Interpretability includes global behavior, local explanation, uncertainty, and operational transparency. A technically explainable model can still be unsuitable if stakeholders cannot act on its outputs.

### Train reproducibly and tune deliberately

A reproducible training run pins input snapshot/query, split, transformation artifact, code commit, container digest, dependency versions, random seed where meaningful, algorithm/hyperparameters, instance type/count, distributed strategy, environment, metric definitions, and output locations. Store model artifacts and evaluation evidence together, then register versions with approval status and lineage.

Batch size changes gradient noise, memory, throughput, and sometimes generalization. Learning rate changes update size; epochs/steps determine exposure to data. L1/L2 regularization, dropout, early stopping, feature selection, augmentation, and more data can control overfitting depending on the model. Underfitting calls for suitable features/model capacity/training; overfitting calls for stronger generalization controls—not simply more epochs.

Distributed data parallelism divides batches among workers; model parallelism divides a model that does not fit or perform on one device. Distribution adds communication and convergence costs. Managed Spot Training can reduce interruptible training cost when checkpointing and job tolerance make interruption acceptable. Warm pools can reduce repeated startup overhead. Match CPU/GPU/accelerator, memory, network, storage, and instance count to measured bottlenecks.

Automatic Model Tuning searches a declared hyperparameter space against an objective metric. Random search is a broad baseline; Bayesian approaches use prior results to choose promising trials; Hyperband-style early stopping can allocate less work to weak configurations. Prevent tuning from optimizing on the final test set. Bound jobs, ranges, concurrency, time, and spend, and inspect whether the “best” trial is stable and deployable.

Fine-tuning a pretrained model requires representative data, base-model/license review, adaptation method, catastrophic-forgetting controls, evaluation against the unchanged baseline, cost, artifact ownership, and safety/privacy assessment. C01 mentions foundation models, but this is not a substitute for MLA-C02’s expanded FM/GenAI scope.

### Evaluate the decision, not a vanity metric

For classification:

- precision asks how many predicted positives are correct;
- recall asks how many actual positives were found;
- F1 balances precision and recall through their harmonic mean;
- specificity measures true-negative rate;
- ROC-AUC ranks positives above negatives across thresholds but can look optimistic in highly imbalanced problems;
- precision-recall curves focus on positive-class tradeoffs;
- a confusion matrix exposes actual error types.

For regression, MAE is interpretable and less sensitive to large errors; MSE/RMSE penalize large errors more; percentage metrics can fail around zero. Ranking, forecasting, anomaly, vision, and language tasks need metrics aligned to their output and business decision. Select a threshold from error costs and capacity, not from 0.5 by habit.

Compare train versus validation behavior to diagnose bias/variance. Use cross-validation when suitable, but preserve group/time constraints. Evaluate by region, cohort, device, product, class, and other relevant slices. Check calibration when probabilities drive decisions. Compare performance, latency, throughput, resource use, and cost—not accuracy alone.

SageMaker Debugger can capture tensors/metrics and identify training issues; Clarify can analyze bias and feature attribution; experiments and lineage make comparisons reproducible. A shadow variant receives production-like traffic without driving the response, enabling realistic comparison; an A/B test exposes variants to users and measures outcomes. Both need assignment, duration, safety, rollback, and statistical interpretation.

**Related item:** Model approval is a risk decision. The winning experiment should not enter production without data, metric, fairness, security, latency, cost, and rollback evidence.

---

## 3. Deployment and Orchestration of ML Workflows — 22%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html) covers deployment selection, scripted infrastructure, and CI/CD/orchestration.

### Match inference mode to traffic and latency

| Mode | Best fit | Watch |
|---|---|---|
| Batch Transform | Bounded offline datasets; no persistent endpoint | Input partitioning, job duration, failed records, output reconciliation, per-job provisioning |
| Real-time endpoint | Predictable low-latency interactive traffic | Always-on cost, instance selection, scaling, health, variants, quotas |
| Serverless inference | Intermittent traffic that tolerates supported payload/latency constraints | Cold starts, limits, feature/region support, concurrency |
| Asynchronous inference | Large payloads or longer processing with queued response | S3 input/output, queue age, notification, expiration, failure path |
| Multi-model endpoint | Many compatible models with shared fleet and variable use | Model loading/caching, noisy neighbors, cold latency, container compatibility |
| ECS/EKS/custom target | Platform requirements exceed managed SageMaker hosting fit | Cluster, scaling, networking, patching, observability, deployment ownership |
| Lambda | Small, short, supported inference or orchestration | Package/runtime/memory/time/concurrency limits and model loading |
| Edge optimization | Local/offline/low-latency constraints | Supported hardware/operators, accuracy change, update/security fleet lifecycle |

Evaluate p50/p95/p99 latency, throughput, payload size, request duration, concurrency, burstiness, availability, data locality, hardware, explainability, cost, and operational ownership. CPU may be cheaper for small classical models; GPU/accelerators help only when model and batching use them. Benchmark the actual container and traffic shape.

Provided containers reduce maintenance; custom containers control dependencies and inference logic but add base-image, patch, scan, user, secret, logging, health, and compatibility responsibilities. Record image digest with model artifact, inference code, schema, dependencies, and evaluation report. Never use an unversioned “latest” tag as release identity.

VPC-attached endpoints and jobs require subnet address capacity, security groups, DNS, routing, VPC endpoints or controlled egress, endpoint policies, and least-privilege roles. A private subnet alone does not guarantee private data flow.

### Provision, scale, and release safely

Use CloudFormation or CDK to define repeatable infrastructure, roles, encryption, networking, alarms, repositories, build projects, pipelines, and endpoints. Parameterize genuine environment differences; avoid uncontrolled console drift. Change sets, policy checks, tests, and rollback make IaC a release mechanism rather than a template archive.

Target-tracking scaling follows a metric such as invocations per instance; step scaling reacts in defined increments; scheduled scaling prepares for known demand. Min/max capacity, cooldown, metric delay, instance startup, downstream quotas, and failure response matter. Scaling cannot repair a slow model or a saturated dependency. Provisioned resources serve steady load; on-demand/serverless/Spot choices trade readiness, interruption, and cost.

Deployment patterns include all-at-once, rolling, blue/green, canary, linear, and shadow. Define routing percentage, bake time, success metrics, alarm thresholds, minimum sample, rollback trigger, and artifact/config/database compatibility. Version and approve models in Model Registry; separate registration from production deployment so evidence and authorization remain visible.

### Orchestrate the complete lifecycle

SageMaker Pipelines models processing, training, evaluation, conditional approval/registration, and related ML steps as a DAG. Step Functions is useful for broader service orchestration and explicit branching/retry/catch behavior. Managed Workflows for Apache Airflow fits teams already using Airflow DAGs. EventBridge can trigger workflows from schedules or events. Choose based on scope, state model, integrations, retry semantics, observability, and operator skill—not by diagram preference.

A production path commonly follows:

`source change or schedule → data validation → processing/features → training → evaluation gates → bias/security checks → registration → approval → staging deployment → integration/load tests → canary → monitor → promote or rollback`

CodePipeline coordinates release stages; CodeBuild executes builds/tests; CodeDeploy supports deployment patterns for compatible compute. Git branch/flow conventions should protect mainline and connect commits to artifacts. Unit tests cover transformation and inference logic; integration tests exercise storage, permissions, containers, endpoints, and orchestration; end-to-end tests validate representative requests and rollback. Include malformed input, schema change, missing feature, duplicate event, timeout, throttling, unauthorized access, corrupt artifact, and failed evaluation.

Retraining triggers can be schedule-, data-, drift-, performance-, or event-based. A trigger starts evaluation, not automatic promotion. Reuse the approved pipeline, compare to the production baseline, require gates, and preserve rollback. Keep data, feature, code, container, and model versions distinct so an incident can locate the changed component.

**Related item:** ML CI validates code and infrastructure; ML continuous training validates data and model behavior; CD releases an approved artifact. Treating all three as one opaque pipeline weakens controls.

---

## 4. ML Solution Monitoring, Maintenance, and Security — 24%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html) covers model inference, infrastructure/cost, and security.

### Monitor four different systems

1. **Data:** schema, types, missingness, ranges, categories, freshness, volume, label availability, sensitive-field leakage, and feature distribution.
2. **Model:** prediction distribution, confidence/calibration, bias and feature-attribution drift, ground-truth performance, threshold/business outcome, and model version.
3. **Service:** request count, errors, model latency, overhead latency, concurrency, queue/backlog, CPU/GPU/memory, disk/network, endpoint/variant health, and dependency behavior.
4. **Workflow/business:** pipeline duration/failure, skipped/late inputs, approval state, retraining result, deployment result, cost, user impact, and ownership/SLA.

Data drift is a statistical input change; concept drift changes the relationship between input and outcome; label drift changes outcome distribution; model-quality degradation is measured after ground truth arrives. Model Monitor supports data quality, model quality, bias drift, and feature-attribution drift workflows. Establish a representative baseline, capture inference data safely, schedule monitoring, publish constraints/statistics, alarm on meaningful violations, and connect alarms to investigation—not blind retraining.

An A/B test measures competing variants on assigned live traffic; shadow testing observes a candidate without affecting responses. Define hypotheses and guardrails before traffic begins. Correlation is not causation when marketing campaigns, seasonality, or population shifts coincide with deployment.

CloudWatch metrics, logs, alarms, dashboards, and Logs Insights show service/workflow behavior. CloudTrail records API activity and can support event-driven response. EventBridge routes operational events. X-Ray helps trace supported request paths. Use correlation IDs across data, workflow, model, endpoint, and application logs while excluding sensitive payloads. An alert needs owner, severity, runbook, evidence query, safe mitigation, and closure criteria.

### Optimize from evidence

Investigate latency by separating client/network, queueing, container overhead, model inference, serialization, and dependency time. Test instance family/size, concurrency, model size, precision, batching, compilation, caching, and autoscaling against representative traffic. SageMaker Inference Recommender can assist instance/config comparison; Compute Optimizer applies only to supported resources and is not a substitute for model-specific benchmarking.

Tag resources by application, environment, owner, model, and cost center. Use Cost Explorer for analysis, Budgets for thresholds/forecasts/actions, and current pricing tools for estimates. Common levers include right-sizing, shutting down idle endpoints/notebooks, batch or async delivery, autoscaling, multi-model hosting, managed Spot Training with checkpoints, suitable storage/lifecycle, efficient data format, and avoiding repeated transformations. Optimize dollars per useful outcome, not one resource line in isolation.

Service quotas can present as throttling, failed scale-out, queued jobs, or deployment failure. Monitor quota use and request increases before events. Provisioned concurrency/capacity and reservations trade guaranteed readiness or discount against utilization commitment; verify which purchase options apply to the exact resource.

### Secure every principal, path, and artifact

Separate human, notebook, processing, training, pipeline, build, deployment, and endpoint execution roles. Grant only required actions on scoped resources and constrain `iam:PassRole`. Align identity policies, resource policies, KMS key policies/grants, bucket policies, endpoint policies, SCPs, and permissions boundaries. Do not solve access errors by adding wildcard administrator rights.

Protect data and artifacts with TLS and appropriate at-rest encryption. KMS permissions must permit the actual service principal or execution role along the full path. Store credentials in Secrets Manager or appropriate managed configuration, rotate them, and prevent exposure in notebooks, environment variables, images, logs, model artifacts, and pipeline parameters.

Use private networking where required: approved subnets/security groups, interface/gateway endpoints, controlled egress, DNS, and no-public-internet settings supported by SageMaker. ECR image scanning, signed/provenanced artifacts, dependency review, patched base images, non-root containers, and immutable digests protect the software supply chain. CloudTrail, Config, logs, model lineage, and deployment evidence support audit and incident response.

Threats include poisoned training data, unauthorized artifact replacement, dependency compromise, over-broad notebook access, secrets in code, malicious serialized models, inference abuse, sensitive prediction logging, and cross-tenant access. Controls should prevent, detect, and recover: source validation, checksums/signatures, approval gates, isolation, least privilege, input/output validation, rate limits, monitoring, backup, and rollback.

**Related item:** Shared responsibility applies inside the ML lifecycle. AWS secures underlying managed infrastructure; the customer still owns data, identities, network configuration, code, containers, model behavior, monitoring, and use.

---

## Integrated scenarios

### Scenario 1: Fraud scoring with delayed labels

A payment platform needs sub-100-ms predictions, receives labels weeks later, and has severe class imbalance. Land immutable events in S3 and stream operational features with explicit event time. Use point-in-time-correct offline features and a low-latency online path. Split evaluation by time and customer/entity to avoid leakage. Compare a simple baseline and tree model; tune against a metric tied to review capacity and false-negative cost, not accuracy. Register data/code/model evidence. Deploy to a real-time endpoint with a canary, idempotent callers, and rollback. Monitor service latency immediately; monitor data/prediction distribution continuously; calculate model quality only when labels mature. Investigate drift before retraining and require the candidate to beat the production model on performance, bias, latency, and cost gates.

### Scenario 2: Nightly demand forecast for many products

The output is consumed once daily, so a permanent endpoint is unnecessary. Build time-aware features without future sales/promotions, preserve product groups in evaluation, and compare naive seasonal forecasts before complex models. Orchestrate processing, training/tuning, evaluation, registration, approval, and Batch Transform. Partition work and output by date/product, reconcile record counts, and publish atomically. Use Spot training only with supported checkpoint/retry tolerance. Monitor source freshness, pipeline duration, missing products, forecast error by product group, and total business outcome. Retraining on schedule is justified only when new labels and stable data are available.

### Scenario 3: Regulated document classification

Documents contain sensitive data and require explainability. Classify/minimize data before landing it in an encrypted S3 bucket. Use private paths, scoped roles, KMS controls, and auditable processing. Validate labels and evaluate precision/recall by document/customer group. Compare a managed AI service, pretrained/fine-tuned model, and custom model against accuracy, explainability, residency, cost, and ownership. Store lineage and approval. Deploy asynchronously for large documents; capture only permitted inference metadata. Monitor input schema/distribution, failure queue, latency, model performance after adjudication, and subgroup behavior. Quarantine rather than log malformed sensitive content.

---

## Hands-on lab path

Use a sandbox account and budgets. Destroy billable resources after each lab; do not use production or sensitive data.

1. **Data contract and format:** Create synthetic tabular events with schema versions and event timestamps. Compare CSV and Parquet size/read behavior in S3; document partition and replay rules.
2. **Leakage-safe preprocessing:** Build train/validation/test splits, fit transforms only on training data, persist preprocessing, inject schema/null/range failures, and publish a quality report.
3. **Feature consistency:** Define two time-aware features, create offline historical values and a simulated online lookup, and prove point-in-time retrieval avoids future leakage.
4. **Train, tune, and evaluate:** Train a simple baseline and XGBoost or supported equivalent, run bounded tuning, compare metrics/confusion matrices/slices, and register the winning evidence.
5. **Inference modes:** Run batch inference and a temporary real-time or serverless endpoint. Measure payload, latency, throughput, cold/warm behavior, and estimated cost; delete the endpoint.
6. **Pipeline gate:** Build a SageMaker Pipeline with processing, training, evaluation, conditional threshold, and registration. Make a failed metric prevent registration.
7. **Canary and monitoring:** Route limited synthetic traffic to a candidate variant, capture permitted data, create baseline/monitoring statistics, inject drift, alarm, and execute rollback.
8. **Security and incident drill:** Scope S3/KMS/SageMaker roles, deny an unauthorized path, trace the failure with CloudTrail/CloudWatch, repair least privilege, rotate a test secret, and record cleanup evidence.

For each lab, preserve architecture, assumptions, commands/code, policy, dataset/model versions, expected and actual results, failure injection, cost, cleanup, and what you would change for production.

## Original knowledge checks

These are original blueprint-aligned prompts, not recalled exam questions.

1. Why can a random split leak future information in a forecasting or churn dataset?
2. When is Parquet preferable to JSON, and what producer/consumer constraint could reverse the choice?
3. What makes a batch ingestion job idempotent?
4. Why is a high-cardinality stream partition key operationally important?
5. What is the distinction between event time and processing time?
6. Why can “latest feature value” be wrong for historical training?
7. Which checks distinguish schema validity, completeness, uniqueness, and freshness?
8. How do class imbalance, selection bias, and measurement bias differ?
9. Why does encryption require both resource and KMS authorization reasoning?
10. What evidence is needed before labeling a dataset de-identified?
11. When should a managed AI service be chosen over a custom model?
12. What baseline would make a complex model improvement credible?
13. How do underfitting and overfitting appear in training and validation metrics?
14. Why must hyperparameter tuning not optimize against the final test set?
15. When is data parallelism more appropriate than model parallelism?
16. What makes Spot training safe or unsafe for a job?
17. Why can ROC-AUC be misleading for a rare-positive problem?
18. How should an operating threshold be selected from precision and recall?
19. What additional evidence beyond accuracy belongs in model approval?
20. How does a shadow test differ from an A/B test?
21. Which inference mode fits a nightly complete-file job, and why?
22. When is asynchronous inference a better fit than a real-time endpoint?
23. What risk does a multi-model endpoint introduce even when it saves cost?
24. Why is an image tag such as `latest` insufficient release identity?
25. Which network dependencies can break a VPC-attached training job?
26. How can endpoint autoscaling lag behind a sudden burst?
27. What must be defined before a canary can be called safe?
28. How do SageMaker Pipelines and Step Functions differ in primary scope?
29. Why should model registration be separate from production deployment?
30. What negative tests belong in an ML delivery pipeline?
31. Why should a drift alarm not automatically promote a retrained model?
32. How do data drift, concept drift, label drift, and model degradation differ?
33. Why can a global metric hide a production failure?
34. What is the purpose of an inference-data baseline?
35. Which signals separate model latency from queue or dependency latency?
36. Why might a larger instance be cheaper per prediction?
37. What tags and dimensions make ML cost explainable?
38. Which distinct roles should exist across an ML lifecycle?
39. Why does private-subnet placement not by itself guarantee private traffic?
40. Which controls reduce training-data poisoning and model-artifact replacement risk?

## Final review checklist

- I can explain all four domains and their 28/26/22/24 weighting.
- I can map a scenario from data contract through monitoring, security, cost, and rollback.
- I choose formats, storage, batch/stream paths, transformations, splits, and feature-store behavior from requirements.
- I distinguish leakage, imbalance, bias, drift, and ordinary quality failures.
- I select a model/managed service, training strategy, metric, threshold, tuning plan, and approval evidence.
- I choose batch, real-time, serverless, asynchronous, multi-model, container, or edge deployment deliberately.
- I can construct a versioned pipeline with tests, evaluation gates, registration, canary, monitoring, and rollback.
- I monitor data, model, service, workflow, business, security, and cost signals separately.
- I reason through IAM, KMS, S3, VPC endpoint, container, secret, lineage, and audit boundaries.
- I have checked the live transition page and know whether I am actually sitting C01 or the C02 beta/GA exam.

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed end to end. Pick the explanation style, lab environment, and practice format that close your own gaps. Because C01 retires imminently, do not begin a long paid C01 path unless you already hold a valid C01 appointment; new learners should prefer C02-labeled material. Times are provider-stated when stable and otherwise transparent estimates; access, catalog contents, and runtimes can change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MLA-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html) and detailed domain pages | Public | 2–4 hours for a careful objective map |
| [AWS certification page and transition notice](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) | Public | 10–15 minutes; recheck immediately before booking |
| [AWS Skill Builder MLA-C01 exam-prep plan](https://skillbuilder.aws/category/exam-prep/machine-learning-engineer-associate-MLA-C01) | Mixed public/subscription | 16h 35m comprehensive plan; separate 26h 10m ML learning plan also listed |
| [SageMaker ML lifecycle overview](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html) | Public | 30–60 minutes plus linked implementation topics |
| [SageMaker Pipelines tutorial](https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html) | Public; AWS usage may cost | 3–6 hours hands-on |
| [SageMaker Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) | Public; AWS usage may cost | 2–4 hours selected reading and lab |
| [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) | Public | 4–8 hours selected lifecycle review |
| [Pluralsight MLA-C01 path](https://www.pluralsight.com/paths/aws-certified-machine-learning-engineer-associate-mlac01) | Paid/trial | 20 hours; five courses, eight labs, and practice exam listed |
| [AWS Certified Machine Learning Engineer Study Guide](https://www.oreilly.com/library/view/aws-certified-machine/9781394319954/) by Dario Cabianca | Paid/subscription | 13h 10m provider estimate; 448 pages plus Sybex test bank |
| [LinkedIn Learning MLA-C01 Cert Prep](https://www.linkedin.com/learning/aws-certified-machine-learning-engineer-associate-mla-c01-cert-prep) | Paid/trial | 24h 58m plus exercises |
| [Nikolai Schuler MLA-C01 course](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01-exam-prep/) | Paid | About 25–35 hours including demos and one practice exam; verify displayed runtime |
| [Stéphane Maarek and Abhishek Singh MLA-C01 practice exams](https://www.udemy.com/course/practice-exams-aws-certified-machine-learning-engineer-associate/) | Paid | About 6–10 hours for three 65-question tests plus careful rationale review |
| [MLA-C01 full course by Tech With Lucy](https://www.youtube.com/watch?v=bUHJ8IPakQY) | Public | 3h 25m video plus pause-and-practice time |

Use practice questions as a diagnostic: explain why each alternative fails the stated requirement, return to official product documentation, and implement the weak concept. Avoid recalled-question collections and any source marketed as an exam dump.
