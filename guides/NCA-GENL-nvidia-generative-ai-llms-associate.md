---
exam_code: NCA-GENL
vendor_id: nvidia
official_blueprint: https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# NVIDIA-Certified Associate: Generative AI LLMs (NCA-GENL) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live weighted blueprint, delivery contract, links and exam-integrity boundary were checked September 29, 2026. This review maps 33 detailed public topic bullets and executes 23 local NumPy checks; independent human review and GPU/LLM infrastructure activities remain pending. See the [coverage record](../docs/SOURCE-VALIDATION.md#nca-genl-coverage-record).

**Current baseline — CURRENT BLUEPRINT:** NCA-GENL remains an active associate-level exam. The current detail panel lists English, 50–60 multiple-choice questions, one hour and USD 125. The page now exposes 33 detailed topic bullets across five weighted areas; the earlier introductory “50 questions” inconsistency is no longer present. No separate effective date is supplied for the page redesign.<br>
**Upcoming change:** No revision or retirement announcement was present on the checked page September 29, 2026.<br>
**Prerequisite:** NVIDIA lists basic generative-AI and LLM understanding, not a required prior credential.<br>
**Validity:** NVIDIA says the credential is valid for two years and can be renewed by retaking the exam. Recheck policy and price before purchase.

**VERIFY CURRENT:** The [program FAQ and policies](https://www.nvidia.com/en-us/learn/certification/) describe pass/fail results without a reported score, a 14-day retake wait and at most five attempts in a 12-month period starting with the first purchase. Remote exams do not allow breaks. Cancellation/rescheduling generally requires at least 24 hours, and a rescheduled exam must fall within two months of payment. Check your actual booking and accommodations before paying; no booking, account creation or secure-browser installation occurred in this review.

The current preparation page recommends the public [Fundamentals of Deep Learning materials](https://github.com/NVDLI/fundamentals-of-deep-learning) and Rapid Application Development with LLMs. Earlier course prices and runtimes are not reproduced as current facts when their public endpoints return only a blank template or maintenance message.

## How to use this guide

Learn one connected lifecycle: define an authorized use case and success criteria → inspect/prepare governed data → choose model/adaptation/retrieval and prompt → implement a small application → evaluate against a versioned baseline → deploy with resource/latency/security controls → monitor quality, safety, drift and cost. Use synthetic or licensed data. Never upload confidential content to an unapproved model, copy a private question bank or treat fluent output as evidence of truth.

> **About related items:** A `Related item:` callout adds prerequisite, architectural or operational context. It supports the topic but does not assert that NVIDIA used the wording in the public blueprint.

## Blueprint map

| Topic area | Weight | Evidence to produce |
|---|---:|---|
| Core Machine Learning and AI Knowledge | 30% | Problem/model/data map; training-versus-inference and transformer/token/embedding reasoning; adaptation/RAG choice |
| Software Development | 24% | Small tested Python LLM application, explicit API/data contracts, safe integration, versioned deployment and telemetry |
| Experimentation | 22% | Hypothesis, baseline, controlled variants, split/metrics, reproducible run record and error-based decision |
| Data Analysis | 14% | Data-quality/profile evidence, appropriate transformation/features, honest plots/slices and communicated limitations |
| Trustworthy AI | 10% | Risk/impact record, privacy/security/safety/bias/transparency controls, evaluations, ownership and response |

---

## 1. Core Machine Learning and AI Knowledge — 30%

AI is the broad field; machine learning learns patterns from data; deep learning uses multilayer neural networks. Supervised learning uses labeled targets, unsupervised learning seeks structure without labels and reinforcement learning learns from reward through interaction. A model maps input to output using learned parameters. Training computes predictions, loss and gradients, then an optimizer updates parameters; validation guides model/hyperparameter choices; a held-out test estimates final generalization. Inference applies the frozen/deployed model to new input.

Neural networks combine weighted transformations and nonlinear activation. Depth and representation learning support complex features but create data, compute, optimization and interpretability challenges. Know parameter versus hyperparameter, epoch versus batch/step, underfitting versus overfitting, and regularization/augmentation/early stopping. GPU parallelism accelerates matrix/tensor-heavy training and inference; acceleration only helps when the workload, data movement, batching and memory use fit the hardware.

Language models estimate token sequences. Tokenization maps text to token IDs; embeddings represent tokens or other items as vectors. Transformers use attention to relate positions, plus feed-forward layers, normalization, residual connections and positional information. Encoder-style models emphasize representations/understanding; decoder-style autoregressive models generate next tokens; encoder–decoder models transform sequences. Context window, vocabulary, parameter count, precision and decoding settings affect capability, latency, memory, consistency and cost.

A foundation/pretrained model learns broad patterns from large data. Prompting conditions behavior without changing weights. Zero-shot supplies instruction; one/few-shot adds demonstrations; structured prompts state role, task, data boundaries, output schema and constraints. Temperature/top-p and other decoding settings trade deterministic concentration against diversity. Do not expose hidden chain-of-thought or rely on unsupported reasoning claims; evaluate the answer and relevant evidence.

Choose among prompt/context engineering, retrieval-augmented generation and fine-tuning. RAG retrieves governed external evidence and supplies it at inference, improving freshness/provenance when retrieval works. Fine-tuning changes model behavior/weights using curated examples; parameter-efficient methods change a smaller adapter set. Pretraining/domain adaptation is much more resource intensive. Alignment methods and human/preference feedback aim to make behavior helpful and safer, but do not guarantee factuality or harmlessness.

Map NVIDIA’s ecosystem by responsibility, not name memorization: GPUs and CUDA accelerate compute; RAPIDS accelerates data science; NeMo supplies generative-AI development/customization/guardrail capabilities; NIM packages supported inference microservices; TensorRT/TensorRT-LLM optimizes inference; Triton serves models; NGC distributes curated containers/models/resources. Product APIs and packaging change, so validate current documentation and distinguish development, training, optimization, serving and governance layers.

**Related item:** Embeddings enable similarity search but are lossy model outputs, not semantic truth. A vector database indexes vectors/metadata; RAG still needs governed ingestion, chunking, filtering, reranking, citations, generation and end-to-end evaluation.

---

### Learning a model, adapting a model and retrieving evidence

**PRACTICAL DEPTH:** A fitted parameter comes from data; a hyperparameter controls the fitting procedure or model family. A least-squares model can learn coefficients without neural-network backpropagation. The CPU workbook below demonstrates an actual fit, held-out prediction and metric calculation, but it does not train an LLM.

NVIDIA's [prompting and P-tuning introduction](https://developer.nvidia.com/blog/an-introduction-to-large-language-models-prompt-engineering-and-p-tuning/) distinguishes ordinary prompt examples from learned virtual prompt tokens. Few-shot examples condition a request without updating model weights. Parameter-efficient tuning trains an adaptation component; full fine-tuning changes a broader parameter set. The article is dated April 2023: its early-access service and timing examples are historical, not current purchase or performance promises. Evaluate the answer and supporting evidence rather than assuming a written explanation reveals faithful internal reasoning.

The [NVIDIA RAG explainer](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/) describes retrieval as a source of external context. An embedding model, an index, a reranker and a generator have separate roles. New documents do not become retrievable until ingestion/index updates succeed, and fresh retrieval does not itself establish permission, correctness or citation support. Treat a vendor demonstration's speedup as workload-specific evidence, not a prediction for your hardware.

The current topic list explicitly includes reading research. When comparing a paper or model card, record the task, data/split, baseline, metric, compute, failure cases and reproducibility limits. Do not transfer an improvement measured on one benchmark to an unrelated service without testing that service.

## 2. Software Development — 24%

Start with a written contract: user and decision, allowed data, model/provider, latency/cost targets, safety boundaries, output schema, evidence/citations, failure behavior and owner. Build the smallest pipeline: validate input → retrieve or construct context → call model → validate output → apply human/tool policy → log safe metadata/result. Separate configuration from code and pin compatible model, prompt, library, container and API versions.

Python is common because NumPy/pandas or GPU equivalents handle data, PyTorch and related frameworks handle tensors/models, and Transformers-style libraries expose tokenizers/models/pipelines. Understand arrays/tensors, shapes/dtypes/devices, batching, dataset/dataloader, model evaluation mode and no-gradient inference. Framework convenience does not remove memory, serialization, dependency or untrusted-model-code risks.

Prompts are versioned application assets. Use clear delimiters, trusted system/developer instructions, typed inputs and constrained/structured outputs. Treat model output as untrusted: schema-validate, authorize each downstream action, escape/parameterize for its sink, cap time/size/retries and require human approval for material effects. Prompt injection is a trust-boundary problem; telling the model to “ignore attacks” is not a sufficient control.

For RAG, parse and normalize approved documents, preserve source/owner/version/ACL metadata, chunk by meaning and retrieval needs, embed/index, filter by authorization, retrieve/rerank and compose citations. Evaluate retrieval recall/precision/relevance separately from grounded generation. Propagate deletion and permission changes through source, index, cache, context and logs.

Deployment may be local, managed API, NIM/container, Triton or another serving system. Package reproducibly; choose GPU/precision/quantization/batch/concurrency according to quality and SLOs; expose health/readiness; secure identity/network/secrets; rate-limit and budget; log trace/request/model/prompt versions without sensitive content. Use canary/shadow/A-B patterns when appropriate and retain rollback.

Testing includes deterministic unit tests for preprocessing/schema/policy, mocked API failures, retrieval tests, model evaluation sets, adversarial/safety checks, load/latency/resource tests and end-to-end user outcomes. CI should not leak data or secrets. Monitor input/output distributions, refusal/grounding/task quality, latency/errors, token/GPU use and safety incidents.

**Related item:** Orchestration frameworks can simplify chains and agents, but every abstraction still has data, identity, retry, state, tool, observability and version contracts. Know what the framework hides before production use.

---

### Current serving documentation changes the version assumptions

**VERIFY CURRENT / PRACTICAL DEPTH:** The current [NIM LLM and VLM overview](https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/overview.html) describes the 2.x architecture using one backend per container and vLLM as its inference engine. Do not assume every NIM is the older multi-backend architecture or that NIM and Triton are interchangeable names. [Triton's quickstart](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/quickstart.html) instead walks through a model repository, server/model readiness and an inference request. Triton has a CPU path, but a model configuration requiring a GPU will not load merely because the server starts without GPU access.

[NIM offerings](https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/nim-offerings.html) distinguish rapid model access from NIM Certified branch validation and support. A no-charge container is not automatically an enterprise support entitlement. Verify offering, image tag, model/profile, GPU, driver, API behavior, licensing and operational support as a set.

The checked [2.0.13 release notes](https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/release-notes.html) provide a concrete regression example: one documented model now rejects more than four stop strings, where the previous release accepted them. That example motivates versioned request-contract tests; it is not a universal limit for every server or model. The notes also distinguish container package updates from host-driver remediation. No NIM/Triton image, model or API was run during this review.

## 3. Experimentation — 22%

Write a falsifiable hypothesis and primary success metric before changing the system. Keep a simple baseline—rule, smaller model, current prompt or no-retrieval case. Define dataset population, sampling, labels/rubric, train/validation/test split, slices and unacceptable regressions. Avoid train-test contamination and data leakage from duplicates, time/future knowledge, preprocessing fitted on all data or benchmark answers in prompts/training.

Data preprocessing includes validation, deduplication, missing/outlier handling, normalization/standardization where relevant, tokenization/truncation/padding, class balancing and privacy/licensing review. Feature engineering encodes useful signal without leaking the target. For language applications, examples, chunking, metadata, embedding model and prompt context are experimental variables too.

Change one controlled factor when causal understanding matters. Track code/data/model/prompt/configuration versions, seeds, hardware/software environment, parameters/hyperparameters, run ID, time, metric definitions, results and artifacts. Random seeds improve repeatability but GPU kernels, distributed execution and external APIs may remain nondeterministic; record uncertainty across repeated runs.

Choose metrics that match the task. Classification uses precision, recall, F1, ROC/PR and confusion matrices with class/base-rate context. Regression uses MAE/RMSE and error distribution. Generation may use exact/semantic/task-specific metrics plus groundedness, factuality, relevance, completeness, style, refusal and human rubric. Perplexity or lexical overlap alone does not prove user value. RAG needs retrieval and generation measures; production adds latency, throughput, errors and cost.

Use error analysis to cluster failures by input, user, language, source, length, risk or stage. Compare variants with confidence intervals/significance or practical effect size when appropriate; do not promote on a tiny cherry-picked average. A/B tests need ethical approval, allocation and guardrails. Document negative results and stop conditions. Select the simplest variant that meets quality, safety, operational and cost constraints.

**Related item:** An offline benchmark estimates behavior on a fixed sample; an online experiment measures actual interaction; production monitoring detects change after release. They answer different questions and should form one evidence chain.

---

### Evaluation must keep the data and decision boundaries intact

The selected [scikit-learn pitfalls guidance](https://scikit-learn.org/stable/common_pitfalls.html) separates fitting a transform from applying it. Estimate preprocessing parameters from training data, then apply the same transform to held-out data. Fit data-dependent preprocessing inside each cross-validation training fold. Split by entity or time where repeated people/documents or future information would otherwise leak into the estimate. Scikit-learn was used as a reference, not installed or executed here.

Choose a metric and denominator before evaluating. The [metrics reference](https://scikit-learn.org/stable/modules/model_evaluation.html) distinguishes mean absolute error from mean squared error; squaring gives large errors more influence and changes units. For retrieval, precision asks how much returned material is relevant and recall asks how much relevant material was returned. Define relevance for the authorized, current source versions. Neither metric measures whether a generated answer correctly uses the evidence.

In the original workbook, a model fits four training rows exactly, yet one of two held-out rows has error 12. A mean error is useful but does not explain that failure. The two-row sample is deliberately too small for a generalization claim, fairness assessment or deployment decision. Keep a separate validation process for tuning and an untouched final test for evaluation; the example fixes its model rather than selecting a new one from test results.

## 4. Data Analysis — 14%

Begin with provenance, license/consent, owner, intended use, population and sensitivity. Profile schema/types, counts, missingness, duplicates, label consistency, ranges/distributions, imbalance, language/length, temporal coverage and leakage. Separate structured tables, semi-structured events/documents and unstructured text/images/audio; each needs different validation and preprocessing.

Use dataframe operations to filter, join, aggregate and transform reproducibly. CPU pandas may fit moderate data; cuDF/RAPIDS and distributed tools can accelerate compatible larger operations, but conversion/data transfer and unsupported operations can erase benefit. Measure end-to-end, not a single kernel. Preserve stable IDs and lineage so errors can be traced to sources without exposing personal data.

Visualization should answer a question. Use histograms/density for distribution, box/violin for spread/outliers, bar for categorical comparison, line for time, scatter for relationships and confusion/calibration/error plots for model behavior. Start axes honestly, show units/sample size/uncertainty, avoid misleading dual axes/3-D decoration and inspect slices rather than only aggregate means. Dimensionality-reduction plots of embeddings are exploratory and sensitive to method/parameters; proximity in a 2-D plot is not proof of semantic grouping.

Communicate what data excludes, which transformation was applied and what decision the chart supports. Dashboard freshness and query definitions are part of evidence. Never send sensitive row-level examples into screenshots or public experiment trackers.

**Related item:** Data quality is fitness for a specific use, not universal cleanliness. A representative dataset for one region, language or time may be dangerously unrepresentative elsewhere.

---

### Shapes and data lineage affect the result

The [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) introduces axes, shape, dtype and array operations. Make feature order and units explicit. A matrix with rows as documents and columns as features must use the same column meaning for a query. A compatible shape can still encode the wrong meaning. Normalizing a zero vector needs an explicit outcome; the workbook returns no match rather than dividing by zero.

For a chart, name the population, sample size, units, exclusions and uncertainty. A line plot suits ordered time; a histogram describes a distribution; a confusion matrix describes class errors. Showing only a favorable mean or changing the y-axis scale between variants can hide an operational regression. Use a table when the few available observations are clearer than a graph.

## 5. Trustworthy AI — 10%

NVIDIA’s public principles emphasize privacy, safety/security, transparency/accountability and nondiscrimination. Translate principles into requirements, named owners, risk tiers, evaluations, release gates, monitoring and response. Record intended use, prohibited/out-of-scope use, training/evaluation data, model/version, limitations and human oversight in a model/system card.

Privacy controls include purpose limitation, minimization, consent/legal basis, retention/deletion, access, encryption and protection against memorization/inference. Security threat-models data poisoning, supply chain/model code, model theft, prompt injection, sensitive disclosure, insecure output handling, denial/wallet exhaustion and excessive tool agency. Apply least privilege, provenance, sandboxing, output validation, action approval, rate/budget limits and logging.

Safety evaluates harmful content and domain-specific physical/financial/legal consequences. Guardrails can filter or guide inputs/outputs and tools, but can fail or over-refuse; test bypasses and operational impact. Grounding/citations reduce some hallucination risks but cited text can be wrong or misused. Use calibrated uncertainty, abstention/escalation and qualified human review for high-impact decisions.

Fairness analysis defines affected groups and an appropriate outcome/opportunity/error metric with domain stakeholders. Dataset balance alone does not ensure fairness; compare performance and harms across slices and intersectional groups, investigate proxies and document tradeoffs. Transparency should explain system purpose, AI involvement, relevant evidence and limits without exposing secrets or enabling abuse. Provide feedback/appeal where impact warrants.

Monitor drift, quality, abuse, security events, complaints and unequal outcomes. Establish halt/rollback, notification, incident investigation and remediation. Compliance depends on use and jurisdiction; consult qualified governance/legal/privacy teams.

**Related item:** A model can be technically accurate yet unsafe, unfair, insecure or unsuitable for the business decision. Trustworthiness is an end-to-end system property, not a single model score.

---

### Framework guidance and product claims need separate evidence

The [NIST AI RMF portal](https://www.nist.gov/itl/ai-risk-management-framework) describes a voluntary framework and its generative-AI profile. It also says AI RMF 1.0 is being revised and identifies an April 2026 critical-infrastructure concept note. A concept note or revision effort is not a newly finalized replacement baseline. Choose applicable obligations with qualified stakeholders rather than treating a framework or product label as a compliance certificate.

Translate NVIDIA's [trustworthy-AI principles](https://www.nvidia.com/en-us/ai-trust-center/trustworthy-ai/) into evidence: data permission and deletion tests for privacy; unauthorized-action and misuse tests for safety/security; understandable purpose and limitations for transparency; and task-specific outcome/error analysis for nondiscrimination. An empty result may be the correct authorized response. Do not expose a forbidden document to a model and expect an instruction to repair the disclosure.

## Integrated scenarios

These original reasoning cases are not examination questions.

1. **Governed support assistant.** Define roles, source owners and current versions before retrieval. Filter eligibility before choosing the top results, cite the selected version and provide an abstention path. Evaluate retrieval and generation separately, then test permission changes, source deletion and rollback. An unauthorized top hit is not a reason to disclose it.
2. **Classifier with repeated customers.** Split by the intended deployment boundary, fit preprocessing only on training folds and compare with a simple baseline. Inspect minority slices and costly errors rather than promoting on accuracy alone. Record intended use, uncertain results and human review responsibilities.
3. **Summarizer upgrade.** Freeze task/rubric and compare quality, privacy, latency and cost across a justified evaluation set. Recheck request contracts and supported profiles for the candidate serving version. A vendor throughput claim does not replace your measurement; retain a rollback and a clear rejection criterion.

## Executed local NumPy workbook

**PRACTICAL DEPTH — actual CPU computation with synthetic data.** The code ran with Python 3.13.14 and the already installed NumPy 2.5.2: **23 checks passed**. It uses actual [least-squares fitting](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) and [vector norms](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html), then lexical cosine retrieval with trusted permission/version fixtures. It performs no file writes, network calls, installations, account operations, GPU inference or model downloads.

The regression data are dimensionless teaching numbers, not observed latency, cost or customer measurements. Its exact training fit does not predict held-out quality. The fixed-vocabulary count vectors are not learned semantic embeddings, and no text generator or LLM is present. The retrieval portion is a component demonstration, not a complete RAG implementation or an authenticated authorization service. The actor/role/tenant/manifest fixtures must be trusted; document IDs are globally distinct except for explicit versions in this tiny example. A real system needs authoritative identity, scoped IDs, ingestion/deletion propagation, cache invalidation and concurrency controls.

Copy the code into an environment with the stated NumPy dependency. Explain both the successful results and the deliberately demonstrated failure before extending the example.

```python
# Original synthetic CPU computation. Requires NumPy 2.5.2; no model download.
import json
import numpy as np

checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


# Fit preprocessing and two linear coefficients on training data only.
train_x = np.array([1., 2., 3., 4.])
train_y = np.array([4., 6., 8., 10.])
test_x = np.array([7., 8.])
test_y = np.array([16., 30.])
center, scale = train_x.mean(), train_x.std()


def design(x):
    return np.column_stack((np.ones(len(x)), (x - center) / scale))


coefficients, residuals, rank, singular_values = np.linalg.lstsq(
    design(train_x), train_y, rcond=None)
predictions = design(test_x) @ coefficients
errors = predictions - test_y
baseline = np.full_like(test_y, train_y.mean())
check("training-only center", center == 2.5)
check("test-inclusive center would differ", np.concatenate((train_x, test_x)).mean() != center)
check("full-rank two-parameter fit", rank == 2)
check("training fit", np.allclose(design(train_x) @ coefficients, train_y))
check("held-out predictions", np.allclose(predictions, [16, 18]))
check("held-out MAE six", np.isclose(np.abs(errors).mean(), 6))
check("held-out MSE seventy-two", np.isclose(np.square(errors).mean(), 72))
check("better than fixed training-mean baseline",
      np.square(errors).mean() < np.square(baseline - test_y).mean())
check("one held-out slice still has large error", np.isclose(abs(errors[1]), 12))
# An empty solver residual array can reflect matrix dimensions, not perfect fit.
_, under_residuals, _, _ = np.linalg.lstsq(np.array([[1., 2.]]), np.array([3.]), rcond=None)
check("underdetermined residual output is empty", under_residuals.size == 0)

# A fixed vocabulary is a lexical representation, not a learned embedding model.
vocabulary = ("refund", "policy", "days", "delivery", "invoice")
documents = [
    dict(id="private", version=1, tenant="A", roles={"finance"}, text="refund policy days"),
    dict(id="policy", version=1, tenant="A", roles={"support"}, text="refund policy days"),
    dict(id="policy", version=2, tenant="A", roles={"support"}, text="refund policy days invoice"),
    dict(id="other-tenant", version=1, tenant="B", roles={"support"}, text="refund policy days"),
    dict(id="shipping", version=1, tenant="A", roles={"support"}, text="delivery days"),
]
current = {"private": 1, "policy": 2, "other-tenant": 1, "shipping": 1}


def vector(text):
    tokens = text.casefold().split()
    return np.array([tokens.count(term) for term in vocabulary], dtype=float)


def cosine(query, document):
    denominator = np.linalg.norm(query) * np.linalg.norm(document)
    return float(query @ document / denominator) if denominator else 0.0


def retrieve(query, *, tenant, role, manifest, k=1):
    # tenant/role/manifest are trusted fixtures, not values authenticated here.
    if type(k) is not int or k < 1:
        raise ValueError("k must be a positive integer")
    eligible = [d for d in documents
                if d["tenant"] == tenant and role in d["roles"]
                and manifest.get(d["id"]) == d["version"]]
    q = vector(query)
    ranked = [(cosine(q, vector(d["text"])), d) for d in eligible]
    ranked.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
    return [(d["id"], d["version"]) for score, d in ranked[:k] if score > 0]


context = dict(tenant="A", role="support", manifest=current)
result = retrieve("refund policy days", **context)
check("authorized current version retrieved", result == [("policy", 2)])
check("unknown vocabulary yields abstention", retrieve("unicorn", **context) == [])
check("unknown tenant denied", retrieve("refund", **(context | {"tenant": "C"})) == [])
check("unknown role denied", retrieve("refund", **(context | {"role": "visitor"})) == [])
check("current-manifest removal takes effect",
      retrieve("refund", **(context | {"manifest": {"shipping": 1}})) == [])
check("query magnitude does not change cosine ranking",
      retrieve("refund policy days refund policy days", **context) == result)
check("zero vector is explicitly handled", cosine(vector("?"), vector("refund")) == 0)
unsafe = max(documents, key=lambda d: cosine(vector("refund policy days"), vector(d["text"])))
check("unfiltered top result exposes a forbidden record", unsafe["id"] == "private")
check("post-filtering only the top hit loses an eligible result",
      "support" not in unsafe["roles"] and bool(result))
try:
    retrieve("refund", **context, k=True)
except ValueError:
    check("boolean k rejected", True)
else:
    raise AssertionError("boolean k accepted")

# Retrieval evaluation uses relevant authorized current (id, version) pairs.
relevant = {("policy", 2)}
returned = set(retrieve("refund days", **context, k=2))
precision = len(returned & relevant) / len(returned)
recall = len(returned & relevant) / len(relevant)
check("retrieval precision one-half", precision == 0.5)
check("retrieval recall one", recall == 1.0)
check("stale citation is not current evidence", ("policy", 1) not in relevant)
metrics = dict(numpy=np.__version__, test_mae=float(np.abs(errors).mean()),
               test_mse=float(np.square(errors).mean()),
               held_out_predictions=predictions.round(6).tolist(),
               retrieval_precision=precision, retrieval_recall=recall)
print(json.dumps(dict(metrics=metrics, checks=checks)))
print(f"{len(checks)} local NumPy checks passed")
```

Expected final line: `23 local NumPy checks passed`.

| Observation | Actual result | Meaning and limit |
|---|---|---|
| Held-out prediction | 16 and 18 against targets 16 and 30 | One test row fails despite exact training fit. Two rows do not establish generalization. |
| MAE / MSE | 6 / 72 | Different loss functions and units; neither replaces error analysis. |
| Unfiltered top document | A forbidden finance record | Similarity does not confer permission. |
| Eligibility before ranking | Current support policy version 2 | Trusted fixture rules reject old versions, other tenants and disallowed roles. |
| Precision / recall at two returned results | 0.5 / 1.0 | All one relevant document was found, along with an irrelevant eligible document. No answer-grounding score was computed. |

An empty residual array from `lstsq` can follow from rank or matrix dimensions; it is not by itself proof of zero prediction error. Likewise, successful retrieval of a source does not prove a generated claim is supported by that source.

## Hands-on evidence labs

These eight activities remain proposed. Use an authorized disposable environment and synthetic or appropriately licensed data. Preserve versions, expected/observed results, failures, cleanup and limitations.

| Activity | Evidence to produce | Failure case to investigate |
|---|---|---|
| 1. Traditional ML baseline | Fit a small model with a training-only transform; compare validation/test losses and a simple baseline. | Introduce repeated entities or future information and show why the split no longer answers the deployment question. |
| 2. Transformer inspection | Record tokenizer/model versions, token IDs, lengths, truncation, tensor shapes and task fit. | Test long, empty and multilingual input; explain truncation and model limitations without inferring hidden reasoning. |
| 3. Prompt contract | Version instructions, examples, input/output schema, allowed tools and evaluation rubric. | Test ambiguous requests, injection, refusal and invalid output; verify enforcement outside the model. |
| 4. Governed retrieval | Map licensed sources, IDs/versions, permissions, chunks, embeddings and citations. | Revoke access or delete a source, then check the index, retrieval, context and caches. Measure retrieval separately from answers. |
| 5. Controlled experiment | State hypothesis, baseline, sampling, metrics, seeds/configuration and acceptance criteria. | Include a negative result, a harmful slice and a resource regression; do not tune on the final test set. |
| 6. Data analysis | Profile provenance, missingness, duplicates, imbalance and temporal coverage; produce a justified chart or table. | Change aggregation or axis scale and explain why the apparent conclusion changes. |
| 7. Serving and upgrade | Verify exact image/model/profile/hardware/API compatibility, health, load and rollback. | Exercise an invalid request, failed model load or OOM in an approved environment; distinguish server readiness from useful inference. |
| 8. Trust evidence | Write a system card, risk record, data/permission map and operational escalation plan. | Evaluate privacy/security/bias/safety failure cases with appropriate stakeholders; document uncertainty and stop criteria. |

## Readiness checks

These original answered prompts support study; they do not reproduce an exam or guarantee a pass.

### Core machine learning and AI

1. **How do AI, ML, deep learning and generative AI relate?** AI is the broad field; ML learns from data; deep learning uses multilayer models; generative systems produce content. Their scopes overlap without making every AI system an LLM.
2. **Training versus inference?** Training changes learned parameters using data and an objective. Inference applies a chosen model to new input; deployment still needs validated data and operational controls.
3. **Parameter versus hyperparameter?** Coefficients or weights are learned parameters. Model family, regularization and learning rate are chosen settings; tune them using an appropriate validation process.
4. **Why do GPU benefits vary?** Parallel compute, memory, batching and data movement must fit the workload. Compare complete task time and quality on the actual configuration.
5. **Tokens, embeddings and attention?** Tokens encode the input into discrete units; embeddings represent units/items as vectors; attention combines context-dependent information. Similar vectors are not proof of truth.
6. **Prompt, retrieve or tune?** Prompt for task conditioning, retrieve for external evidence and tune for a justified behavior/domain adaptation need. Evaluate data rights, cost, quality and operational burden for each.
7. **Does a few-shot prompt train weights?** Ordinary in-context examples do not update weights. Learned virtual prompts/adapters use a training process and require their own version and evaluation evidence.
8. **How should a research claim be assessed?** Inspect the task, dataset/split, baseline, metric, compute and uncertainty; reproduce the relevant result where practical and state what does not transfer to your use case.

### Software development

9. **What belongs in an application contract?** Input/output schema, user/task, allowed data/actions, model and prompt versions, latency/cost limits, failure behavior and accountable owner.
10. **Why do dtype, shape and feature order matter?** They determine numerical representation and interpretation. Correct dimensions cannot compensate for swapped columns or incompatible embedding spaces.
11. **Is valid JSON safe model output?** No. Validate semantics and authorization, then parameterize or encode for the destination. Apply limits and approval requirements outside the model.
12. **Where should retrieval permissions apply?** Determine eligibility before ranking and context construction using trusted identity and source rules. Post-filtering a small top-k result can lose useful eligible evidence.
13. **How do NIM and Triton differ?** They are serving products with distinct packaging and deployment contracts. Current NIM LLM/VLM 2.x architecture and Triton repository/backend behavior must be checked by exact version.
14. **What proves a serving system is ready?** Server and model readiness, a valid representative inference, protected access and required performance/quality. A running container alone is insufficient.
15. **What should an upgrade verify?** Image/model/profile/hardware and driver compatibility, API behavior, quality/safety, observability and rollback. Version-specific release notes identify cases to test.
16. **Does no-charge availability include enterprise support?** Not automatically. Verify offering, branch, license and subscription requirements; current NIM and NIM Certified have different support conditions.

### Experimentation

17. **What makes a useful hypothesis?** A falsifiable expectation tied to task, population, baseline, metric and acceptable regression limits. Decide the evaluation method before looking at results.
18. **Where is preprocessing fitted?** Only on the training partition, including within each cross-validation fold. Apply its learned transform to validation/test data without refitting there.
19. **When is a random row split misleading?** Repeated people/documents, temporal dependencies or future features can leak information. Match the split to the intended deployment population and time boundary.
20. **Does a perfect training score prove generalization?** No. The local model fits training exactly but misses one held-out target by 12. Evaluate representative unseen data and failure slices.
21. **MAE versus MSE?** MAE averages absolute errors in target units; MSE averages squared errors and emphasizes larger deviations. Select by consequences, not whichever looks better.
22. **Retrieval precision versus recall?** Precision is relevant returned material divided by returned material; recall is relevant returned material divided by all relevant material under a declared eligibility/version scope.
23. **Does a seed make every run identical?** It helps repeatability, but hardware kernels, distributed execution and remote services can still vary. Record versions/configuration and measure repeat-run variation when relevant.
24. **What does human feedback require?** Consent and appropriate data handling, qualified instructions/rubrics, representative raters and disagreement analysis. Human labels are evidence with limitations, not infallible truth.

### Data analysis

25. **What should profiling begin with?** Provenance, rights/consent, purpose, population and sensitivity, followed by types, missingness, duplicates, ranges, labels, imbalance and temporal coverage.
26. **Can clean data be unsuitable?** Yes. It may exclude the users or conditions of deployment, encode biased labels or lack required permission.
27. **What does a feature transform need to preserve?** Meaning, units, column order, identifiers and lineage, with a reproducible fit/apply boundary. Keep held-out information out of learned preprocessing.
28. **When does GPU data processing help?** When supported operations and problem size offset transfer and conversion costs. Measure the whole pipeline, including unsupported fallbacks.
29. **Which chart should be chosen?** Use the question: distributions, time trends, category comparisons or relationships. Show sample size, units, exclusions and uncertainty.
30. **Can an average hide a harmful slice?** Yes. Break errors down by relevant groups/conditions and inspect absolute impacts; a good aggregate may coexist with a serious failure.
31. **Does a 2-D embedding plot establish semantic groups?** No. Projection method and parameters change the display. Treat it as exploration and validate the intended relationship separately.
32. **What should an analyst communicate?** What was measured, transformations, population limits, uncertainty and the decision supported. Avoid exposing sensitive rows in reports or trackers.

### Trustworthy AI

33. **Privacy versus security?** Privacy concerns appropriate data use and individual interests; security concerns protection against unauthorized access or disruption. A secure system can still process data inappropriately.
34. **Safety versus factuality?** A factually accurate answer can enable harm or exceed permitted use. Evaluate consequences, context and human oversight as well as correctness.
35. **Does a citation prove grounding?** Only if the cited authorized source actually supports the claim and is current for the task. Retrieval success and answer support need separate evaluation.
36. **Can a guardrail guarantee protection?** No. Test bypasses, over-refusal and integration failures; enforce data/action permissions independently and maintain incident response.
37. **How should bias be assessed?** Define affected groups, task-specific harms and suitable metrics with stakeholders; inspect slices and proxies and document tradeoffs. Balanced counts alone are insufficient.
38. **What belongs in a system card?** Purpose, users, data/model versions, evaluation scope, known limitations, responsible owners, prohibited uses and operational monitoring/escalation.
39. **Does framework adoption establish compliance?** No. NIST AI RMF is voluntary guidance; applicable legal/contractual duties and actual control evidence require separate assessment.
40. **When should a system abstain or stop?** When evidence, permission, quality or safety requirements are unmet. Define thresholds, human escalation, rollback and review triggers before production.

Readiness means being able to explain a decision, implement the relevant component, evaluate its failures and state what the evidence does not establish.

## Places to learn

This is not a complete list. Start with the current topic list and one teaching route, then select targeted practice. Public availability was checked September 29, 2026. Planning estimates are original suggestions; a reachable URL does not prove that its course metadata or paid content was accessible.

| Resource | Access | Estimated time |
|---|---|---|
| [NCA-GENL certification and preparation topics](https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/): canonical five weights and 33 detailed bullets. | Public | 3–5h mapping/review estimate. |
| [Fundamentals of Deep Learning public materials](https://github.com/NVDLI/fundamentals-of-deep-learning): six listed modules covering neural networks, CNNs, augmentation, transfer and advanced architecture/NLP. | Public repository; compute/dependencies separate | No fixed runtime stated in the checked README; budget by module. README reviewed, notebooks not executed. |
| [Rapid Application Development with LLMs](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-26+V1): still named on the current preparation page. | Course endpoint returns an empty metadata template; course access unverified | Earlier 8h/runtime/price not reverified; confirm through the current catalog. |
| [Getting Started with Deep Learning](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-01+V1): earlier recommendation. | Empty public course template | Earlier 8h not reverified; current blueprint instead links open materials. |
| [Accelerating End-to-End Data Science](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-DS-01+V2): earlier supplemental route. | Empty public course template | Earlier 8h not reverified. |
| [Introduction to Transformer-Based NLP](https://courses.nvidia.com/courses/course-v1:DLI+S-FX-08+V1/): older endpoint. | Maintenance/moved notice | Earlier 6h not reverified; no current course interior reviewed. |
| [Building LLM Applications with Prompt Engineering](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-12+V2): earlier supplemental route. | Empty public course template | Earlier 8h not reverified. |
| [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) and the local workbook: arrays, fitting and retrieval components. | Public; NumPy dependency for execution | 2–4h selected reading and workbook estimate; not LLM/GPU execution. |
| [scikit-learn pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) and [metrics](https://scikit-learn.org/stable/modules/model_evaluation.html): evaluation references. | Public documentation | 2–4h selected reading estimate; library not run in this review. |
| [NVIDIA Trustworthy AI](https://www.nvidia.com/en-us/ai-trust-center/trustworthy-ai/) and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework): principles and risk context. | Public | 2–4h selected reading/scenario estimate; not a complete compliance assessment. |
| [Udemy NCA-GENL specialization](https://www.udemy.com/course/nca-genl-nvidia-certified-generative-ai-llms-specialization/): HTTP 403. | Paid catalog access blocked | Earlier March 2026/1h48m metadata unverified; no current contents or quality assessment. |

Use original practice that explains decisions and failure cases. Avoid recalled questions, dumps and guaranteed-pass banks; completing a course or a tiny local example does not establish examination or production readiness.
