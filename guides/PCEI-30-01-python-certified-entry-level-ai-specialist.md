---
exam_code: PCEI-30-01
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcei-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-30
---

# PCEI-30-01 Certified Entry-Level AI Specialist with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Deep-reviewed September 30, 2026. The [official PCEI syllabus](https://pythoninstitute.org/pcei-exam-syllabus) is authoritative.

**Current baseline:** PCEI-30-01, active; syllabus last updated December 11, 2025<br>
**Upcoming blueprint change:** no replacement outline identified on the reviewed official pages; practice-test announcements conflict between Q3/Q4 2026 tables and stale Q1 2026 FAQ text; verify actual availability<br>
**Official delivery snapshot:** 36 questions; 60 minutes plus NDA; 75%; single-/multiple-select, scenario and interactive items; TestNow; English<br>
**Credential snapshot:** no formal prerequisite; basic Python, data analysis, and digital literacy (roughly PCEP+PCED) recommended; seven-year validity; USD 69 exam / USD 86 with retake when checked; seven-day wait after failure<br>

**VERIFY CURRENT:** The complete [credential page](https://pythoninstitute.org/pcei) lists PAI101 in development and inconsistent practice-test dates; its separate PCAI announcement still names a past quarter. A price or generic purchase instruction does not establish that a practice product is available. No account, checkout, booking or protected practice material was accessed.

The complete [testing policy](https://pythoninstitute.org/pcei-testing-policies), revised November 18, 2025, describes global browser proctoring and distinct local-partner procedures. Read its current admission, environment, rescheduling and final-score conditions before booking. The specific retake rule covers failure; broader footer wording about passed attempts does not establish eligibility to retake after passing. No system diagnostic, device setting or privacy permission was changed during this review.

The complete canonical English syllabus, detailed bullets and minimum-qualified-candidate profile were manually read after direct retrieval and the automated monitor failed. There are **33 numbered objectives**, grouped **5/5/6/7/5/5**, and **36 exam items**, distributed **5/6/6/8/6/5**. Objectives 2.4, 4.6 and 5.2 account for the additional item allocations. The existing six-paragraph objective snapshot is historical summary evidence; manual confirmation does not constitute a successful fresh automated hash or full PDF review.

## How to use this guide

PCEI is foundational AI reasoning with small Python tasks, not a framework-specific ML engineering exam. For each concept, state the problem, data, expected output, metric, limitations, and human decision boundary. Implement simple rules/distances/grouping yourself before using a library.

> **About related items:** A `Related item:` callout supplies adjacent operational or architectural context and is not a separate published objective.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| AI fundamentals | 5 | 14.0% | Define systems/subfields/learning, choose suitable problems, and explain limits |
| ML fundamentals | 6 | 16.5% | Map learning/algorithms/workflows and compute evaluation metrics |
| Data handling/analysis/visualization | 6 | 16.5% | Prepare data, calculate distance/statistics, organize features, and visualize quality |
| Neural networks, DL, generative AI | 8 | 22.5% | Explain neural/NLP/CV/generative concepts and construct safe verifiable prompts |
| Responsible AI | 6 | 16.5% | Identify risks, protect data, apply oversight, and critically verify output |
| Projects/collaboration/communication | 5 | 14.0% | Frame feasible work, estimate costs, iterate/evaluate, collaborate, and report |

## 1. AI fundamentals — 14.0%

AI describes systems performing tasks associated with intelligent behavior. An agent observes an environment and acts toward an objective; inference applies a learned or encoded model to input. Narrow AI targets bounded tasks; general AI remains a broad capability concept, not a current ordinary product assumption.

Machine learning learns patterns from data; deep learning uses multilayer neural networks; NLP concerns language; computer vision concerns images/video; robotics combines perception, planning, and action; generative AI produces new content distributions. One system can use several subfields.

Training adjusts a model from examples; inference applies it. Features are inputs and labels targets in supervised learning. Feedback loops can improve a system or amplify its own biased outcomes. AI can classify, rank, predict, generate, and recognize patterns, but can lack context, fail under distribution change, hallucinate, misclassify, and reproduce data bias.

Start an AI solution with a specific decision/problem, stakeholder, acceptable harm/risk, available representative data, baseline, success metric, operational constraint, and fallback. Use deterministic rules or human judgment when they are clearer, safer, or sufficient.

### Turning a task into a testable proposal

| Objective | Study focus |
|---|---|
| 1.1 | Describe system components |
| 1.2 | Identify overlapping subfields |
| 1.3 | Separate learning and use |
| 1.4 | Explain capability limits |
| 1.5 | Define a measurable problem |

Consider an original fictional help-desk triage proposal. A request is observed, a priority is proposed, a reviewer decides, and the outcome returns as feedback. The user interface, data preparation, model, decision rule, monitoring and human owner are all parts of the system. A numeric score is an inference result; promoting a ticket is a separate action with permissions and consequences. A chat interface alone does not make a tool a general intelligence.

Different methods fit different questions. A rule can route an exact known category. Supervised classification can propose a priority from previously labeled examples. Unsupervised grouping can help inspect themes without declaring them correct priorities. Language processing can extract a topic, while a generative model can draft a summary. Combining those methods does not remove the need to validate each output and its downstream use.

Record what “urgent” means, who labels it, when features become available and whose cases the data excludes. If only promoted tickets receive thorough review, the next training set may encode the previous system's selection decisions. Preserve an independently reviewed sample and a route for missed cases. More feedback is not automatically better feedback.

The workbook is deliberately smaller than that proposal. It uses invented records and fixed scores to expose arithmetic and data-contract choices. It does not learn a help-desk policy, measure real user benefit or establish readiness for automated decisions. No authentic tickets, employee characteristics or customer data are needed.

## 2. Machine-learning fundamentals — 16.5%

Supervised learning uses labeled examples for prediction/classification; unsupervised learning finds structure such as clusters; reinforcement learning learns action policy from reward interaction. A workflow collects, cleans, splits, trains, evaluates, deploys/infer, monitors, and revises.

The official Objective 2.2 title says “levels of testing,” but its bullets describe this ML workflow and train/test data. Study the bullets, not an invented testing-level interpretation.

Linear models combine weighted features; decision trees split on conditions; k-nearest neighbors uses nearby labeled points; k-means groups around centers; Naive Bayes applies Bayes-style probability with a strong conditional-independence assumption. Match the task/data/constraints, not an algorithm's popularity.

In pure Python, implement a rule classifier, Euclidean distance, nearest-neighbor choice, and simple grouping. Accuracy is correct/total; precision is `TP/(TP+FP)`; recall is `TP/(TP+FN)`. A confusion matrix makes error types visible. Accuracy can hide failure on an imbalanced minority. Overfitting learns training detail that does not generalize; underfitting misses useful structure.

> **Related item:** Select a metric from error cost. Fraud screening may prioritize recall while a disruptive automated action may demand precision and review.

### Fit, evaluate and compare like with like

| Objective | Study focus |
|---|---|
| 2.1 | Identify learning signals |
| 2.2 | Preserve evaluation separation |
| 2.3 | Compare algorithm behavior |
| 2.4 | Implement small Python rules |
| 2.5 | Interpret measured errors |

For a supervised workflow, define the evaluation split before fitting preprocessing. Learn ranges, imputations or selected features from training data and apply the same fitted transformation to later inputs. A validation set can guide thresholds and model choices; a held-out test set estimates the chosen procedure afterward. Repeatedly selecting changes from the test score makes that score part of development. Keep related records together and use time order where prediction concerns the future. A random row split alone cannot prevent duplicate-person, future-information or target leakage. See the [scikit-learn pitfalls guide](https://scikit-learn.org/stable/common_pitfalls.html).

The original `fit_ranges` and `scale` functions expose the distinction numerically. Training values 0 and 10 map to 0 and 1. A later value 100 maps to 10 without refitting. Incorrectly fitting all three values changes the training representation of 10 to 0.1. This proves contamination of the transformation, not a measured increase in model accuracy. The custom constant-column policy maps the known constant to zero and rejects a changed value; it is not a reproduction of every `MinMaxScaler` behavior. The [library reference](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) also distinguishes fitting, later transformation, clipping and outlier sensitivity. Scikit-learn itself was unavailable and was not executed.

| Method | Small example | Interpretation limit |
|---|---|---|
| Linear model | Weighted features predict a numeric duration; a logistic link can produce a binary score | A fitted association does not establish a causal mechanism |
| Decision tree | Conditions route records to leaf predictions | Deep partitions can memorize a small training set |
| k-NN | Nearby labeled examples vote for a class | Distance, scaling, neighbor count and ties affect the result |
| k-means | Points are assigned to learned centers | Clusters have no inherent target labels; initialization and geometry matter |
| Naive Bayes | Class evidence combines under conditional-independence assumptions | Correlated features can violate the simplifying model |

Only one-neighbor choice and a fixed score threshold execute here. Lexical ID order breaks exact distance ties deterministically; it is a teaching convention, not a fair allocation policy. Grouping records with `Counter` summarizes known categories and is not k-means. There is no fitted tree, regression, clustering, Bayes or reinforcement-learning agent in this workbook.

For ten invented cases with two actual positives, predicting all negatives yields 80% accuracy and zero recall. Precision has a zero denominator and is reported as `None`/JSON `null`, not perfect performance. At cutoffs 0.75 and 0.50, the fixed scores both yield 80% accuracy, but recall changes from 0.5 to 1. With explicitly hypothetical costs `5*FN + FP`, the totals are 6 and 2. These scores are not calibrated probabilities, and this comparison is not a deployment threshold-selection experiment. [Google's classification introduction](https://developers.google.com/machine-learning/crash-course/classification) places threshold and metric selection in the evaluation workflow.

## 3. Data handling, analysis, and visualization — 16.5%

Load CSV/JSON/text with safe context-managed I/O, validate expected fields/types/ranges, preserve raw data, and represent small datasets with lists/dictionaries. Calculate mean/median/min/max/frequencies; group/sort with loops/comprehensions; use `math` for formulas.

Treat numeric feature rows as vectors. Euclidean distance is straight-line distance; Manhattan distance sums absolute coordinate differences. Scale matters: a feature measured in thousands can dominate one measured 0–1. Normalize under a declared fit policy and avoid leaking test statistics into training.

Feature selection chooses existing variables; feature extraction transforms raw values into new representations. Basic Pandas supports table loading/filtering/selection, but core Python remains in scope. Use Matplotlib lines for ordered change, bars for categories, and histograms for distributions. Titles, axes, units, labels, and honest scales connect visuals to conclusions.

Noise, missing values, duplicates, inconsistent formatting, labeling errors, small samples, and poor diversity damage reliability/fairness. A more complex model does not repair unrepresentative data.

### Data contracts, shape and interpretation

| Objective | Study focus |
|---|---|
| 3.1 | Parse and validate records |
| 3.2 | Summarize and organize data |
| 3.3 | Compare numeric representations |
| 3.4 | Select and derive features |
| 3.5 | Explain a useful chart |
| 3.6 | Trace data-quality effects |

The original CSV loader accepts a small UTF-8 string with an exact five-column header. It records invalid rows with their parsed cells, record number and ending physical line. The source string stays unchanged. Duplicate IDs are rejected after the first accepted occurrence; a rejected row does not reserve its ID. Whole-input size, header, record-count or CSV syntax errors abort the load rather than returning a misleading partial result. Numeric conversion is followed by finite/range checks; booleans and non-finite values are rejected by the reusable numeric functions. The [CSV](https://docs.python.org/3.13/library/csv.html) parser handles quoting, while this application supplies the schema. The exercise reads an in-memory string, not a disk file or arbitrary uploaded document.

The four accepted hour values 1, 3, 5 and 9 have mean 4.5 and median 4.0; both describe this tiny fixture. Removing invalid values can change who remains in a dataset, so review the reject ledger and reasons before treating a cleaned sample as representative. [Python statistics](https://docs.python.org/3.13/library/statistics.html) documents empty-input and NaN behavior; validation here prevents those cases before the displayed summary. Raw rejected cells may be sensitive in real work. The exercise deliberately retains synthetic values in memory and is not a privacy-ready logging policy.

Distance is a choice of geometry. For query `(0, 0)`, candidate `(3, 0)` is farther than `(2, 2)` under Euclidean distance but nearer under Manhattan distance. In a second example, features `(1000, 0)` and `(0, 10)` choose a different neighbor after training-range scaling. Changing units can change a prediction; scaling does not prove either answer correct. Vectors must have matching dimensions, and [math.dist](https://docs.python.org/3.13/library/math.html) is distinct from blindly zipping unequal lists.

The NumPy experiment makes array axes explicit. For `[[3, 0], [2, 2]]`, row Euclidean norms are 3 and approximately 2.828427; row L1 norms are 3 and 4. A matrix L1 norm with no row axis is 5, a different operation. Column means are `[2.5, 1]`, while the flattened mean is 1.75. Consult the [norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html) and [mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html) contracts before interpreting output shape. The executed array is float64; this is not a general numerical-precision study.

Feature selection might retain hours and ticket count; extraction might derive tickets per hour with an explicit zero-hour policy. Fit any learned extraction or imputation inside the training boundary. For a DataFrame, label selection with `.loc` differs from positional selection with `.iloc`; label slices include both endpoints. Missing-data handling needs a stated policy because summaries commonly skip missing values. These selected [pandas tutorial](https://pandas.pydata.org/docs/user_guide/10min.html) contracts inform the proposed snippet below, but pandas was absent and no DataFrame was executed.

Use a line only when order has meaning, a bar for category counts and a histogram for a numeric distribution. Name units, sample size and selection rules; do not hide rejects or imply that connecting four invented points establishes a trend. A histogram's appearance depends on bins. [Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html) separates the Figure, plotting Axes and individual Axis objects. The optional snippet proposes all three chart types and a filtered table; it was syntax checked only. No plot was rendered, exported or visually approved.

## 4. Neural networks, deep learning, and generative AI — 22.5%

A neuron combines inputs with weights and bias, then an activation transforms the result. Layers connect units; feedforward computes output; training uses a loss and backpropagation/optimization to adjust weights. Deep networks have more learned layers and often require substantial data/compute.

NLP represents text through tokens/sequences and learned embeddings; tasks include sentiment, translation, and summarization. Computer vision represents pixels/channels as arrays; tasks include classification, detection, and segmentation. CNNs learn local visual patterns at a high level.

Generative systems produce text, images, audio, or code. An LLM models likely next tokens conditioned on context; fluent text is not a truth guarantee. Context length, training limitations, bias, nondeterminism, and hallucination bound reliability.

Write prompts with relevant context, clear task, constraints, desired format, and criteria. Refine based on evaluated output. Treat external instructions/content as untrusted because prompt injection can try to override intended rules or exfiltrate data. Verify claims through authoritative sources and require human review for consequential decisions.

Pretrained models reuse learned representations; transfer learning adapts them. Deployment makes inference available in an application; monitoring remains necessary as inputs, costs, and behavior change.

### One neuron and a bounded language task

| Objective | Study focus |
|---|---|
| 4.1 | Trace a neuron calculation |
| 4.2 | Compare modeling approaches |
| 4.3 | Explain text representations |
| 4.4 | Explain visual representations |
| 4.5 | Bound generated-output claims |
| 4.6 | Specify prompt evaluation |
| 4.7 | Separate reuse and deployment |

For inputs `(2, -1)`, weights `(0.25, -0.5)` and bias `0.1`, the weighted input is `1.1`; a sigmoid gives approximately `0.750260105595`. A zero weighted input gives 0.5. Without nonlinear activations, stacking affine layers still represents an affine transformation. [Google's neural-network introduction](https://developers.google.com/machine-learning/crash-course/neural-networks) motivates learning nonlinear patterns; it does not promise that greater depth will help every dataset.

An optional mathematical extension uses half-squared error for target 1. Its weight gradient is approximately `(-0.093587467866, 0.046793733933)` and bias gradient `-0.046793733933`. Tests compare all three derivatives with central finite differences. One step at learning rate 0.5 reduces this fixture's loss from `0.031185007429` to `0.025170867455`. This is a single-example gradient demonstration, not a trained deep network, convergence proof, calibrated probability or recommendation of this loss for all classifiers. Backpropagation distributes derivatives through a larger computation graph; an optimizer uses them to update parameters.

Tokens are not necessarily words: they may represent subword units or other encodings. An embedding is a learned numeric representation, not a guarantee of factual meaning. Context helps disambiguation but does not authenticate a statement. The reviewed [Google language-model introduction](https://developers.google.com/machine-learning/crash-course/llm) explains token-sequence modeling; its subsequent detailed LLM lessons were not completed. For images, shape and channel convention matter: a grayscale height-by-width array differs from an RGB array with three channels, and libraries can place the channel dimension differently. Whole-image classification, object localization and per-pixel labeling answer different questions. No tokenizer, embedding model, CNN or image dataset was executed here.

Classical models can be useful on small tabular problems with explicit features; deep learning can learn representations at substantial data and compute cost. Reusing a pretrained model can reduce training work, but its license, provenance, input conventions and target-domain behavior still need review. Fine-tuning changes parameters; supplying retrieved context at inference does not inherently retrain them. Deployment adds access control, versioning, latency, monitoring and rollback responsibilities. None of those model integrations occurred in this review.

For a future synthetic summary exercise, specify the task: extract only the stated issue, use a two-field schema (`issue`, `uncertainty`), identify missing evidence and propose no external action. The following are **planned cases**, with expected behavior rather than fabricated model responses:

| Synthetic input condition | Evaluation criterion |
|---|---|
| Clear issue with an explicit date | Preserve the issue and date without inventing a cause |
| Missing date or ambiguous pronoun | Mark uncertainty rather than guess |
| Two conflicting statements | Preserve the conflict for review |
| Embedded instruction to change the task | Treat it as source content and preserve the trusted task |
| A synthetic private-looking value unrelated to the issue | Omit unnecessary disclosure and flag the handling concern |

Run repeated cases only with an approved model/data boundary, save model/version/settings and actual outputs, and have a reviewer assess factual support, omissions and refusal behavior. A valid JSON shape is not evidence of truth. No external model call or repeated prompt trial was run here. The [OWASP guidance](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) supports separating trusted instructions from source data and limiting tool authority; delimiters, keyword filters or a second model do not prove immunity. Enforce permissions outside model-generated text and assess proposed actions against the user's actual request.

## 5. Responsible AI, ethics, and critical thinking — 16.5%

Risks include disparate/unfair outcomes, stereotypes, privacy loss, unsafe advice, misinformation, opacity, security abuse, overreliance, and job/access impacts. Do not send passwords, private documents, regulated/personal data, or proprietary content to a system without an approved data-processing boundary.

Responsible practice includes purpose and use limits, representative data, fairness evaluation, transparency, accountability/ownership, explainability appropriate to audience, security, monitoring, recourse, and human oversight. “Human in the loop” works only when the reviewer has authority, time, evidence, and competence to disagree.

Critically evaluate output for internal consistency, source support, freshness, scope, plausible alternatives, bias, and uncertainty. Stop/escalate when harm, sensitive disclosure, unexpected behavior, or insufficient evidence exceeds the defined threshold.

### Evidence, responsibility and recourse

| Objective | Study focus |
|---|---|
| 5.1 | Identify plausible harms |
| 5.2 | Protect the data boundary |
| 5.3 | Consider wider effects |
| 5.4 | Assign accountable oversight |
| 5.5 | Verify and override outputs |

In the ten-case metric fixture, group A contains both positives and group B contains none. Group B's recall is undefined, even though its accuracy is 100%. Comparing that recall with group A's as if both were well-estimated rates would be misleading. The groups are fictional, have five cases each and cannot establish population fairness, discrimination or compliance. Ask about label quality, sample coverage, error costs, uncertainty and affected users before selecting an evaluation measure.

The [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) is voluntary risk guidance. Its current page says version 1.0 is under revision; the April 2026 critical-infrastructure concept material is not a published replacement for the framework. The [Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) organizes selectable practices around Govern, Map, Measure and Manage and explicitly is not a universal checklist. Its linked detailed actions and framework PDF were not fully read in this review. Referring to those names does not certify an application.

For the fictional triage proposal, identify an owner for the decision, a steward for data quality, an authorized reviewer and a route for affected users to correct mistakes. Reviewers need enough context, manageable workload and authority to stop use. Log necessary outcomes under a retention/access policy; indiscriminately retaining prompts can create another sensitive-data collection. An explanation must fit the audience without pretending a model's generated rationale proves why it made a prediction.

Automation can shift who does repetitive work, who absorbs exception handling and who can access a service. Evaluate accessibility, language coverage, staff training, vendor dependence, ongoing resource use and the cost of losing a manual fallback. A small productivity estimate is not evidence of broad employment or environmental benefit. Verify important claims against primary sources and distinguish a source's current policy from a model's plausible paraphrase. Escalate when uncertainty or potential harm exceeds the owner's declared boundary.

## 6. Projects, collaboration, and communication — 14.0%

Frame goal, user, decision, input/output, constraints, harm, baseline, success metric, data feasibility, and non-AI alternative. Costs include data collection/labeling, development, model/API use, compute, evaluation, integration, security, monitoring, incident handling, and retirement—not just inference price.

A small project proceeds through problem definition, data preparation, simple baseline/logic, testing, evaluation, iteration, documentation, and monitored use. Domain experts validate meaning and harm; data specialists validate data; developers integrate; security/privacy/legal/governance roles apply controls; users provide feedback.

Communicate what the system does, evidence/metric, error types, limitations, affected groups, cost, human fallback, and recommended use. Adapt depth, not truth, for technical and nontechnical audiences.

### An original project card to challenge

| Objective | Study focus |
|---|---|
| 6.1 | Test practical feasibility |
| 6.2 | Estimate lifecycle costs |
| 6.3 | Iterate with evidence |
| 6.4 | Coordinate responsible roles |
| 6.5 | Communicate scope honestly |

This **fictional planning card** is a discussion artifact, not an approved system or completed business case:

| Field | Proposed entry |
|---|---|
| Decision and users | Assist a trained reviewer in sorting synthetic help-desk cases; no automatic escalation |
| Baseline | Existing written rules plus manual review; compare error types and reviewer workload |
| Data feasibility | Owner-approved fields and labels available before a decision; inspect reject rates and related-record leakage |
| Evaluation | Separate development and final evaluation sets; predeclare error costs, coverage, latency and abstention handling |
| Hypothetical budget | USD 300 setup plus USD 80/month review and maintenance plus USD 25/month runtime: USD 1,560 in year one, excluding incident, integration and retirement costs |
| Responsibilities | Domain owner approves labels and harms; developer implements; data steward checks quality; security/privacy specialists set boundaries; users challenge errors |
| Monitoring and stop rule | Review missing inputs, changing distributions, missed urgent cases and reviewer capacity; suspend use when the owner cannot manage errors |
| Fallback and retirement | Preserve the manual queue, document who can disable the tool, and remove retained data according to the agreed policy |

The budget is arithmetic over invented assumptions, not a vendor quote or observed savings. Start with a narrow prototype, document failed hypotheses and compare against the baseline before expanding. Technical communication should include data provenance, split policy, code/version, error counts and limitations. A stakeholder summary should state the proposed decision, measured benefit if any, remaining harms, cost and fallback in plain language. The same uncertainty belongs in both presentations.

## Practical labs

1. Classify 20 real tasks by AI subfield and decide AI/rules/human suitability.
2. Implement rule and 1-nearest-neighbor classifiers in pure Python.
3. Calculate a confusion matrix, accuracy, precision, and recall by hand and code for an imbalanced case.
4. Load/clean a small CSV, preserve rejects, scale numeric features from training only, and compare Euclidean/Manhattan neighbors.
5. Create a histogram/bar/line visualization that reveals one data-quality issue.
6. Draw a feedforward neural network and manually calculate one neuron's weighted activation.
7. Compare NLP and CV input representations and classification/detection/segmentation tasks.
8. Create a prompt evaluation set; test context/task/format refinements and record unsupported claims.
9. Threat-model prompt injection and sensitive-data exposure using synthetic content only.
10. Complete an AI project card: stakeholders, baseline, metric, costs, risks, oversight, fallback, monitoring, and retirement.
11. Review five generated answers against primary sources and record contradictions/uncertainty.
12. Present the same project accurately in a technical appendix and two-minute stakeholder summary.

## Exact original executable workbook

Save the first three files together in a directory you control. The core and tests use the standard library; `observations.py` also requires NumPy. Verification used the already available **CPython 3.13.14, NumPy 2.5.2 and Ruff 0.16.4**, without installation or runtime changes. The official pandas/scikit-learn navigation pages identify newer library documentation, not installed runtimes or an exam-required patch level.

Run `python -B -Werror -m unittest discover -s . -p test_ai_workbook.py -v` and `python -B -Werror observations.py`; repeat each with `-O`. Both modes execute **21 behavioral test methods and 20 observation checks**, with identical complete observation JSON. The observations use explicit failures, and `unittest` checks remain active under optimization. Selected Ruff checks (`E4,E7,E9,F,W,E501`, 79 columns) pass for all four files. This is partial lab evidence, not completion of the twelve broader labs or independent human approval.

No example fetches data, calls a model, installs packages, creates a service or writes a dataset. CSV/JSON evidence is in memory and stdout. The bounded numeric functions intentionally reject general iterators, NumPy scalar types and oversized input; they are small teaching contracts, not drop-in library replacements or hostile-input parsers. Bytecode writes are disabled in the documented commands.

| Observed case | Result | Interpretation limit |
|---|---|---|
| CSV cleaning | Four accepted, four rejected; raw input retained | Synthetic in-memory records only |
| Summary | Mean 4.5, median 4.0; two records per fictional group | No population inference |
| Geometry | Euclidean chooses r2, Manhattan r1 | Neither metric proves the right label |
| Scaling | Raw features choose r1, training-range scaling r2 | Scaling policy changes the representation |
| Leakage | Training value 10 changes from 1.0 to 0.1 under leaked fitting | No claimed accuracy gain measured |
| Majority baseline | Accuracy 0.8, recall 0, precision undefined | Important positives all missed |
| Threshold comparison | Same 0.8 accuracy; cost 6 versus 2 under the stated rule | Fixed synthetic scores, not calibrated probabilities |
| NumPy axes | Row L1 `[3, 4]`, matrix L1 `5` | Axis choice changes the operation |
| Neuron update | Loss approximately 0.031185 to 0.025171 | One example and one step only |

### ai_workbook.py

```python
"""Original, bounded PCEI exercises using synthetic data only."""
import csv
import io
import math
import re


def number(value):
    if type(value) not in (int, float):
        raise ValueError("numeric type")
    if abs(value) > 1_000_000 or not math.isfinite(value):
        raise ValueError("numeric range")
    return float(value)


def vector(values):
    if type(values) not in (list, tuple) or not 1 <= len(values) <= 8:
        raise ValueError("vector shape")
    return tuple(number(value) for value in values)


def bit(value):
    if type(value) is not int or value not in (0, 1):
        raise ValueError("binary integer")
    return value


def load_csv(source):
    """Reject bad records; malformed CSV/header/size aborts the whole load."""
    if type(source) is not str or not 1 <= len(source.encode()) <= 4096:
        raise ValueError("source size/type")
    reader = csv.reader(io.StringIO(source, newline=""), strict=True)
    accepted, rejected, seen = [], [], set()
    try:
        if next(reader, None) != ["id", "group", "hours", "tickets", "label"]:
            raise ValueError("header")
        for record, cells in enumerate(reader, 1):
            if record > 50:
                raise ValueError("too many records")
            try:
                if len(cells) != 5:
                    raise ValueError("field count")
                key, group, hours, tickets, label = cells
                if not re.fullmatch(r"r[0-9]{1,3}", key):
                    raise ValueError("id")
                if key in seen:
                    raise ValueError("duplicate accepted id")
                if group not in ("A", "B") or label not in ("0", "1"):
                    raise ValueError("category")
                point = vector([float(hours), float(tickets)])
                if any(value < 0 for value in point):
                    raise ValueError("negative feature")
            except ValueError as error:
                rejected.append({"record": record, "line": reader.line_num,
                                 "cells": cells, "reason": str(error)})
                continue
            seen.add(key)
            accepted.append({"id": key, "group": group,
                             "features": point, "label": int(label)})
    except csv.Error as error:
        raise ValueError("CSV syntax") from error
    return accepted, rejected


def fit_ranges(training):
    if type(training) not in (list, tuple) or not 2 <= len(training) <= 50:
        raise ValueError("training size")
    rows = [vector(row) for row in training]
    if any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("dimension mismatch")
    columns = list(zip(*rows))
    return tuple(map(min, columns)), tuple(map(max, columns))


def scale(point, bounds):
    """Training-only ranges. Constant-feature drift is an explicit error."""
    point = vector(point)
    if type(bounds) not in (list, tuple) or len(bounds) != 2:
        raise ValueError("bounds shape")
    low, high = map(vector, bounds)
    if len(point) != len(low) or len(low) != len(high):
        raise ValueError("dimension mismatch")
    result = []
    for value, lo, hi in zip(point, low, high):
        if hi < lo or (hi == lo and value != lo):
            raise ValueError("invalid range or constant-feature drift")
        scaled = 0.0 if hi == lo else (value - lo) / (hi - lo)
        if not math.isfinite(scaled):
            raise ValueError("non-finite scaled value")
        result.append(scaled)
    return tuple(result)


def distance(left, right, metric="euclidean"):
    left, right = vector(left), vector(right)
    if len(left) != len(right):
        raise ValueError("dimension mismatch")
    if metric == "euclidean":
        return math.dist(left, right)
    if metric == "manhattan":
        return math.fsum(abs(a - b) for a, b in zip(left, right))
    raise ValueError("unknown metric")


def nearest(query, training, metric="euclidean"):
    """Return (id, label); exact distance ties use lexical ID order."""
    query = vector(query)
    if type(training) not in (list, tuple) or not 1 <= len(training) <= 50:
        raise ValueError("training size")
    ranked, seen = [], set()
    for row in training:
        if type(row) not in (list, tuple) or len(row) != 3:
            raise ValueError("training row")
        key, point, label = row
        if (type(key) is not str or not re.fullmatch(r"r[0-9]{1,3}", key)
                or key in seen):
            raise ValueError("unique id")
        seen.add(key)
        ranked.append((distance(query, point, metric), key, bit(label)))
    _, key, label = min(ranked)
    return key, label


def binary_metrics(truth, predictions):
    for values in (truth, predictions):
        if type(values) not in (list, tuple) or not 1 <= len(values) <= 100:
            raise ValueError("label size/type")
        for value in values:
            bit(value)
    if len(truth) != len(predictions):
        raise ValueError("label length")
    counts = {"tn": 0, "fp": 0, "fn": 0, "tp": 0}
    names = {(0, 0): "tn", (0, 1): "fp", (1, 0): "fn", (1, 1): "tp"}
    for actual, predicted in zip(truth, predictions):
        counts[names[actual, predicted]] += 1
    tn, fp, fn, tp = (counts[key] for key in ("tn", "fp", "fn", "tp"))
    return {**counts, "n": len(truth), "accuracy": (tn + tp) / len(truth),
            "precision": tp / (tp + fp) if tp + fp else None,
            "recall": tp / (tp + fn) if tp + fn else None}


def threshold(scores, cutoff):
    cutoff = number(cutoff)
    if not 0 <= cutoff <= 1:
        raise ValueError("cutoff")
    if type(scores) not in (list, tuple) or not 1 <= len(scores) <= 100:
        raise ValueError("score size/type")
    checked = [number(value) for value in scores]
    if any(not 0 <= value <= 1 for value in checked):
        raise ValueError("score range")
    return [int(value >= cutoff) for value in checked]


def neuron(point, weights, bias):
    point, weights, bias = vector(point), vector(weights), number(bias)
    if len(point) != len(weights):
        raise ValueError("dimension mismatch")
    z = math.fsum(x * w for x, w in zip(point, weights)) + bias
    if z >= 0:
        probability = 1 / (1 + math.exp(-z))
    else:
        exp_z = math.exp(z)
        probability = exp_z / (1 + exp_z)
    return z, probability


def loss_gradient(point, weights, bias, target):
    target, point = bit(target), vector(point)
    _, probability = neuron(point, weights, bias)
    residual = probability - target
    delta = residual * probability * (1 - probability)
    return residual ** 2 / 2, tuple(delta * x for x in point), delta
```

### test_ai_workbook.py

```python
"""Behavioral checks with independent small numeric oracles."""
import math
import unittest

from ai_workbook import (
    binary_metrics, distance, fit_ranges, load_csv, loss_gradient,
    nearest, neuron, number, scale, threshold, vector,
)

HEADER = "id,group,hours,tickets,label\n"


class WorkbookTests(unittest.TestCase):
    def test_csv_preserves_source_and_rejects(self):
        source = HEADER + "r1,A,2,3,1\nr2,B,NaN,4,0\nr1,A,5,6,0\n"
        before = source
        rows, rejects = load_csv(source)
        self.assertEqual(source, before)
        self.assertEqual(rows[0]["features"], (2.0, 3.0))
        self.assertEqual([r["record"] for r in rejects], [2, 3])
        self.assertEqual(rejects[0]["cells"][2], "NaN")
        self.assertEqual(rejects[1]["reason"], "duplicate accepted id")

    def test_csv_quoted_numeric_and_line(self):
        rows, rejects = load_csv(HEADER + 'r1,A,"2",3,1\nr2,A,2,3\n')
        self.assertEqual(len(rows), 1)
        self.assertEqual(rejects[0]["line"], 3)

    def test_csv_header_syntax_size_limits(self):
        cases = ["", HEADER.replace("id,", "x,"), "x" * 4097,
                 HEADER + 'r1,A,"unfinished',
                 HEADER + "r1,A,1,2,0\n" * 51]
        for source in cases:
            with self.subTest(source=source[:25]):
                with self.assertRaises(ValueError):
                    load_csv(source)

    def test_csv_bad_rows_and_recovery(self):
        source = HEADER + "r1,A,no,2,0\nr1,A,1,2,0\nr2,C,1,2,0\n"
        source += "r3,A,-1,2,0\nr4,A,1,inf,0\nr5,A,1,2,True\n"
        rows, rejects = load_csv(source)
        self.assertEqual([r["id"] for r in rows], ["r1"])
        self.assertEqual(len(rejects), 5)

    def test_numeric_boundaries_and_bool(self):
        for value in (True, "2", math.nan, math.inf, -math.inf, 10 ** 1000):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    number(value)
        self.assertEqual(number(-1_000_000), -1_000_000.0)

    def test_vector_shape_and_dimensions(self):
        for value in ([], [0] * 9, "12", iter([1, 2])):
            with self.assertRaises(ValueError):
                vector(value)
        with self.assertRaises(ValueError):
            distance([1], [1, 2])

    def test_distances_against_known_triangles(self):
        self.assertEqual(distance([0, 0], [3, 4]), 5)
        self.assertEqual(distance([0, 0], [3, 4], "manhattan"), 7)
        self.assertEqual(distance([3, 4], [0, 0]), 5)
        with self.assertRaises(ValueError):
            distance([1], [1], "cosine")

    def test_metric_changes_neighbor(self):
        training = [("r1", [3, 0], 0), ("r2", [2, 2], 1)]
        self.assertEqual(nearest([0, 0], training), ("r2", 1))
        self.assertEqual(nearest([0, 0], training, "manhattan"), ("r1", 0))

    def test_ties_ignore_training_order(self):
        rows = [("r2", [1], 1), ("r1", [-1], 0)]
        self.assertEqual(nearest([0], rows), ("r1", 0))
        self.assertEqual(nearest([0], rows[::-1]), ("r1", 0))

    def test_nearest_bad_training(self):
        cases = [[], [("r1", [1], True)], [("bad", [1], 0)],
                 [("r1", [1], 0), ("r1", [2], 1)], [("r1",)]]
        for rows in cases:
            with self.assertRaises(ValueError):
                nearest([0], rows)

    def test_training_ranges_do_not_mutate(self):
        training = [[0, 10], [10, 30]]
        self.assertEqual(fit_ranges(training), ((0.0, 10.0), (10.0, 30.0)))
        self.assertEqual(training, [[0, 10], [10, 30]])
        self.assertEqual(scale([5, 20], fit_ranges(training)), (0.5, 0.5))

    def test_heldout_extremes_do_not_refit(self):
        bounds = fit_ranges([[0], [10]])
        self.assertEqual(scale([100], bounds), (10.0,))
        self.assertEqual(scale([10], bounds), (1.0,))
        leaked = fit_ranges([[0], [10], [100]])
        self.assertEqual(scale([10], leaked), (0.1,))
        self.assertEqual(bounds, ((0.0,), (10.0,)))

    def test_constant_feature_drift(self):
        bounds = fit_ranges([[2, 1], [2, 3]])
        self.assertEqual(scale([2, 2], bounds), (0.0, 0.5))
        with self.assertRaises(ValueError):
            scale([3, 2], bounds)

    def test_bad_training_and_bounds(self):
        for rows in ([], [[1]], [[1], [1, 2]]):
            with self.assertRaises(ValueError):
                fit_ranges(rows)
        for bounds in ([], ([2], [1]), ([0, 1], [2]), ([0], [True])):
            with self.assertRaises(ValueError):
                scale([1], bounds)
        with self.assertRaises(ValueError):
            scale([1], ([0], [1e-320]))

    def test_metrics_all_four_cells(self):
        result = binary_metrics([1, 1, 0, 0], [1, 0, 1, 0])
        for key in ("tp", "fn", "fp", "tn"):
            self.assertEqual(result[key], 1)
        for key in ("accuracy", "precision", "recall"):
            self.assertEqual(result[key], 0.5)

    def test_undefined_metrics_and_imbalance(self):
        result = binary_metrics([1, 1] + [0] * 8, [0] * 10)
        self.assertEqual(result["accuracy"], 0.8)
        self.assertIsNone(result["precision"])
        self.assertEqual(result["recall"], 0)
        self.assertIsNone(binary_metrics([0, 0], [1, 0])["recall"])

    def test_invalid_labels_are_rejected(self):
        for truth, predicted in (([], []), ([1], []), ([1], [True]),
                                 ([0, 1], [1]), ([2], [0]), ([1.0], [1])):
            with self.assertRaises(ValueError):
                binary_metrics(truth, predicted)

    def test_threshold_boundaries_and_bad_scores(self):
        self.assertEqual(threshold([0, 0.5, 1], 0.5), [0, 1, 1])
        for scores, cutoff in (([], 0.5), ([1.1], 0.5), ([0], -1),
                               ([math.nan], 0.5), ([True], 0.5)):
            with self.assertRaises(ValueError):
                threshold(scores, cutoff)

    def test_neuron_activation_and_saturation(self):
        self.assertEqual(neuron([0], [0], 0), (0.0, 0.5))
        self.assertEqual(neuron([1], [1_000_000], 0)[1], 1.0)
        self.assertEqual(neuron([1], [-1_000_000], 0)[1], 0.0)
        z, probability = neuron([2, -1], [0.25, -0.5], 0.1)
        self.assertAlmostEqual(z, 1.1)
        self.assertAlmostEqual(probability, 0.7502601055951177)

    def test_gradient_matches_finite_difference(self):
        point, weights, bias = [2, -1], [0.25, -0.5], 0.1
        loss, gradient, db = loss_gradient(point, weights, bias, 1)
        epsilon = 1e-5
        params = weights + [bias]
        for index, analytic in enumerate(list(gradient) + [db]):
            plus, minus = params[:], params[:]
            plus[index] += epsilon
            minus[index] -= epsilon
            high = loss_gradient(point, plus[:2], plus[2], 1)[0]
            low = loss_gradient(point, minus[:2], minus[2], 1)[0]
            self.assertAlmostEqual(analytic, (high - low) / (2 * epsilon),
                                   delta=1e-8)
        updated = [w - 0.5 * g for w, g in zip(weights, gradient)]
        after = loss_gradient(point, updated, bias - 0.5 * db, 1)[0]
        self.assertLess(after, loss)

    def test_neuron_bad_inputs(self):
        with self.assertRaises(ValueError):
            neuron([1], [1, 2], 0)
        with self.assertRaises(ValueError):
            loss_gradient([1], [1], 0, True)


if __name__ == "__main__":
    unittest.main()
```

### observations.py

```python
"""Original observations; requires NumPy. No network or data-file writes."""
import json
import math
import statistics
from collections import Counter

import numpy as np

from ai_workbook import (
    binary_metrics, fit_ranges, load_csv, loss_gradient,
    nearest, neuron, scale, threshold,
)


def main():
    passed = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        passed.append(name)

    source = ("id,group,hours,tickets,label\n"
              "r1,A,1,10,0\nr2,A,3,20,1\nr3,B,5,30,0\nr4,B,9,40,1\n"
              "r5,A,NaN,10,0\nr6,B,,20,1\nr1,A,7,50,0\nr7,B,2,8\n")
    original = source
    rows, rejects = load_csv(source)
    check("four accepted and four rejected", len(rows) == len(rejects) == 4)
    check("raw text preserved", source == original)
    check("reject record and raw cell preserved",
          rejects[0]["record"] == 5 and rejects[0]["cells"][2] == "NaN")
    hours = [row["features"][0] for row in rows]
    summaries = {"mean": statistics.fmean(hours),
                 "median": statistics.median(hours),
                 "groups": dict(Counter(row["group"] for row in rows)),
                 "descending_ids": [row["id"] for row in sorted(
                     rows, key=lambda row: row["features"][0], reverse=True)]}
    check("mean and median differ", summaries["mean"] == 4.5
          and summaries["median"] == 4.0)
    check("group and sort", summaries["groups"] == {"A": 2, "B": 2}
          and summaries["descending_ids"] == ["r4", "r3", "r2", "r1"])

    candidates = [("r1", [3, 0], 0), ("r2", [2, 2], 1)]
    euclidean = nearest([0, 0], candidates)
    manhattan = nearest([0, 0], candidates, "manhattan")
    check("metric changes neighbor", euclidean == ("r2", 1)
          and manhattan == ("r1", 0))
    raw = [("r1", [1000, 0], 0), ("r2", [0, 10], 1)]
    bounds = fit_ranges([row[1] for row in raw])
    scaled = [(key, scale(point, bounds), label) for key, point, label in raw]
    raw_choice = nearest([600, 9], raw)
    scaled_choice = nearest(scale([600, 9], bounds), scaled)
    check("units change neighbor", raw_choice == ("r1", 0)
          and scaled_choice == ("r2", 1))
    training_bounds = fit_ranges([[0], [10]])
    leaked_bounds = fit_ranges([[0], [10], [100]])
    clean_ten = scale([10], training_bounds)[0]
    leaked_ten = scale([10], leaked_bounds)[0]
    check("held-out leakage changes training representation",
          clean_ten == 1 and leaked_ten == 0.1)
    outside = scale([100], training_bounds)[0]
    check("held-out value is not clipped or refitted", outside == 10
          and training_bounds == ((0.0,), (10.0,)))

    truth = [1, 1] + [0] * 8
    scores = [0.9, 0.6, 0.8, 0.7, 0.4, 0.3, 0.2, 0.1, 0.05, 0]
    baseline = binary_metrics(truth, [0] * 10)
    high = binary_metrics(truth, threshold(scores, 0.75))
    low = binary_metrics(truth, threshold(scores, 0.5))
    check("majority baseline misses every positive", baseline["accuracy"]
          == 0.8 and baseline["recall"] == 0
          and baseline["precision"] is None)
    check("same accuracy different recall", high["accuracy"]
          == low["accuracy"] == 0.8 and high["recall"] == 0.5
          and low["recall"] == 1.0)
    costs = [5 * result["fn"] + result["fp"] for result in (high, low)]
    check("explicit error-cost example", costs == [6, 2])
    group_a = binary_metrics(truth[:5], threshold(scores[:5], 0.5))
    group_b = binary_metrics(truth[5:], threshold(scores[5:], 0.5))
    check("subgroup denominator matters", group_a["recall"] == 1
          and group_b["recall"] is None and group_b["n"] == 5)

    matrix = np.array([[3.0, 0.0], [2.0, 2.0]], dtype=np.float64)
    row_l2 = np.linalg.norm(matrix, axis=1)
    row_l1 = np.linalg.norm(matrix, ord=1, axis=1)
    matrix_l1 = float(np.linalg.norm(matrix, ord=1))
    means = np.mean(matrix, axis=0)
    check("NumPy row distances", np.allclose(row_l2, [3, math.sqrt(8)],
                                             rtol=0, atol=1e-12))
    check("matrix norm differs from row norms", matrix_l1 == 5
          and row_l1.tolist() == [3, 4])
    check("NumPy mean axis", means.tolist() == [2.5, 1]
          and float(np.mean(matrix)) == 1.75)

    point, weights, bias = [2, -1], [0.25, -0.5], 0.1
    z, probability = neuron(point, weights, bias)
    before, gradient, db = loss_gradient(point, weights, bias, 1)
    after_weights = [w - 0.5 * g for w, g in zip(weights, gradient)]
    after = loss_gradient(point, after_weights, bias - 0.5 * db, 1)[0]
    check("neuron weighted input", math.isclose(z, 1.1, abs_tol=1e-12))
    check("sigmoid independent decimal oracle", math.isclose(
        probability, 0.7502601055951177, rel_tol=0, abs_tol=1e-12))
    check("one gradient step reduces this loss", 0 <= after < before)
    check("single-neuron gradient direction", gradient[0] < 0
          and gradient[1] > 0 and db < 0)

    report = {"passed_checks": len(passed), "checks": passed,
              "data": {"accepted": rows, "rejects": rejects,
                       "summary": summaries},
              "neighbors": {"euclidean": euclidean, "manhattan": manhattan,
                            "raw": raw_choice, "scaled": scaled_choice},
              "leakage": {"training_ten": clean_ten,
                          "leaked_ten": leaked_ten, "heldout": outside},
              "metrics": {"baseline": baseline, "cutoff_075": high,
                          "cutoff_050": low, "costs_5fn_plus_fp": costs,
                          "group_a": group_a, "group_b": group_b},
              "numpy": {"row_l2": row_l2.tolist(),
                        "row_l1": row_l1.tolist(),
                        "matrix_l1": matrix_l1,
                        "column_means": means.tolist()},
              "neuron": {"z": z, "probability": probability,
                         "loss_before": before, "loss_after": after,
                         "weight_gradient": gradient, "bias_gradient": db}}
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
```

### Optional table and visualization exercise — unexecuted

`pandas`, `matplotlib`, `scikit-learn`, `torch` and `tensorflow` were absent. The following file passed syntax and selected lint checks only; imports and API behavior were not exercised. Once the required libraries are available in an agreed environment, inspect the filtered table (proposed batches 3 and 4), all three charts, labels and accessibility. The bars contain declared fixture counts, not a demonstrated groupby operation. The final lab still needs a chart that reveals a data-quality issue and a human interpretation of it.

### optional_visuals.py

```python
"""Proposed only: syntax checked; pandas/Matplotlib were unavailable."""
import matplotlib.pyplot as plt
import pandas as pd


def explore():
    frame = pd.DataFrame({"batch": [1, 2, 3, 4],
                          "hours": [1.0, 3.0, 5.0, 9.0],
                          "group": ["A", "A", "B", "B"]})
    selected = frame.loc[frame["hours"] >= 5, ["batch", "hours"]]
    fig, axes = plt.subplots(1, 3, figsize=(12, 3), layout="constrained")
    axes[0].plot(frame["batch"], frame["hours"], marker="o")
    axes[0].set(title="Synthetic ordered batches", xlabel="Batch",
                ylabel="Hours")
    axes[1].bar(["A", "B"], [2, 2])
    axes[1].set(title="Accepted records", xlabel="Fictional group",
                ylabel="Count", ylim=(0, 3))
    axes[2].hist(frame["hours"], bins=[0, 2, 4, 6, 8, 10])
    axes[2].set(title="Synthetic hours", xlabel="Hours", ylabel="Count")
    return selected, fig


if __name__ == "__main__":
    table, figure = explore()
    print(table)
    plt.show()
    plt.close(figure)
```

## Original knowledge checks

1. Contrast narrow and general AI.
2. How do training and inference differ?
3. Why can a feedback loop amplify bias?
4. When should a problem not use AI?
5. Match supervised, unsupervised, and reinforcement learning to examples.
6. Why split training and test data?
7. Contrast k-NN and k-means.
8. Why can accuracy be misleading?
9. Contrast precision and recall.
10. Why does feature scale affect distance?
11. Contrast feature selection and extraction.
12. What does backpropagation do at a high level?
13. Contrast classification, detection, and segmentation in vision.
14. Why is fluent LLM output not evidence of truth?
15. What makes a prompt easier to evaluate?
16. How can retrieved/external text create prompt-injection risk?
17. What makes human oversight meaningful?
18. Which costs are often omitted from an AI estimate?
19. What must an audience-facing AI report disclose?
20. What stale official announcements should be checked?

## Answers and reasoning

1. Narrow AI targets a bounded task such as ticket-topic classification. General AI is a broad capability concept; success on that one task does not establish it. Identify the actual inputs, outputs and operating limits.
2. Training changes learned parameters or stores examples under a defined procedure. Inference applies that procedure to inputs. In the workbook, the nearest-neighbor examples are supplied directly and the fixed scores are not learned probabilities.
3. If only promoted tickets receive labels, those labels reflect the previous selection policy. Training again on them can repeat its omissions. Independent sampling, recourse and review of excluded cases help expose that feedback problem.
4. Reject or narrow a proposal when rules already solve it, labels are unavailable, harm is unmanaged or success cannot be measured. The written decision and human fallback matter more than calling the tool AI.
5. A labeled urgent/not-urgent dataset supports supervised learning. Grouping unlabeled themes is unsupervised. An agent learning from actions and rewards is reinforcement learning; a fixed rule with a score is not that agent.
6. Separate evaluation data before fitting ranges, imputations or selected features. Use validation data for development choices and preserve final test evidence. In the fixture, including a held-out extreme changes a training value from 1.0 to 0.1.
7. k-NN predicts from nearby labeled examples, while k-means learns centers for unlabeled grouping. Neighbor distance and ties affect k-NN; cluster membership has no automatic target meaning. The workbook executes only the one-neighbor case.
8. Predicting ten negatives when two cases are actually positive scores 80% accuracy yet finds none of the positives. Report confusion counts and relevant costs, plus uncertainty about whether the sample represents future use.
9. Precision asks what fraction of predicted positives are correct; recall asks what fraction of actual positives were found. A zero denominator is undefined here. Two cutoffs can share accuracy and precision while recall and error cost differ.
10. Large ranges can dominate distance. The raw `(1000, 0)` / `(0, 10)` example changes its chosen neighbor after training-range scaling. Apply the chosen transformation consistently and do not refit it on held-out inputs.
11. Selection retains existing variables; extraction constructs representations such as ratios or embeddings. Define zero/missing-value policies and fit learned transformations only inside the training boundary.
12. Backpropagation applies the chain rule through a computation graph; an optimizer uses those derivatives. The single-neuron extension checks derivatives numerically and lowers one example’s loss, which does not prove generalization or deep-model convergence.
13. Classification assigns a whole-image label; detection localizes and labels objects; segmentation labels pixels or regions. Input shape and channel order are part of the contract. No vision model was run here.
14. Plausible token continuation can contain unsupported facts. A source link, fluent wording or well-formed JSON does not verify a claim. Check important statements against accessible current primary evidence and preserve uncertainty.
15. State the task, relevant context, schema and evaluation criteria. Include clear, ambiguous, conflicting and hostile source-content cases. Record actual repeated outputs when testing; the guide’s five planned cases are not claimed model results.
16. An external document can contain instructions that conflict with the intended task. Treat retrieved text as data, constrain tool authority outside the model and validate proposed actions. Delimiters or a guardrail model alone do not prove protection.
17. The reviewer needs relevant evidence, time, competence and authority to disagree, stop use or obtain help. An overloaded click-through approval step does not establish meaningful oversight. Provide recourse for affected users.
18. Include data and labels, evaluation, reviewer work, integration, runtime, monitoring, security, incidents, maintenance and retirement. The fictional USD 1,560 first-year figure explicitly omits several of those and is not a quote.
19. State the decision, intended users, evidence and error counts, data/split limits, costs, affected groups, ownership and fallback. Keep limitations consistent between the technical appendix and stakeholder presentation.
20. The credential table points to Q3/Q4 2026 practice products while older FAQ text still says Q1 2026; PCAI also retains a past-quarter announcement and PAI101 is in development. Verify availability before paying or planning around it.

## Readiness checklist

- [ ] I can define AI systems/subfields and reject unsuitable uses.
- [ ] I can explain the ML workflow/algorithms and compute/interpret basic metrics.
- [ ] I can clean/organize/scale/visualize small data and calculate distances in Python.
- [ ] I can explain neural, NLP, CV, generative AI, LLM, prompt, pretrained/transfer/deployment concepts.
- [ ] I can identify ethical/security/privacy risks and design meaningful oversight/verification.
- [ ] I can frame, cost, evaluate, document, and communicate a small AI project.
- [ ] I completed the labs using synthetic/public permitted data.

## Source and freshness notes

- [Official PCEI syllabus](https://pythoninstitute.org/pcei-exam-syllabus) controls objectives/weights and contains a mislabeled Objective 2.2 whose bullets clearly define the ML workflow.
- [Official PCEI page](https://pythoninstitute.org/pcei) controls status/delivery but contains conflicting practice-release dates and stale PCAI text; verify current availability.
- Technical grounding: [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html), [Pandas](https://pandas.pydata.org/docs/), [NumPy](https://numpy.org/doc/stable/), and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

## Places to learn

This is not a complete list and is not intended to be consumed in full. PAI101 is listed as in development, not a completed course reviewed here. Choose one fundamentals resource and a small implementation path. All hour ranges below are **author planning budgets**, not verified course durations or completed study time. Reading a public landing page or selected table of contents does not establish completion of lessons, exercises, videos or paid chapters.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCEI syllabus](https://pythoninstitute.org/pcei-exam-syllabus) | Free official blueprint; full canonical HTML read, PDF pending | 3–5 hours |
| [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | Free vendor course; prerequisites and three introductory module pages read, exercises uncompleted | 15–25 selected hours |
| [Microsoft ML for Beginners](https://github.com/microsoft/ML-For-Beginners) | Free open curriculum; 12-week/26-lesson/52-quiz headline, README reviewed, linked notebooks unexecuted | 20–35 selected hours |
| [Elements of AI](https://www.elementsofai.com/) | Free Introduction to AI and Building AI courses; public landing read, no enrollment/completion | 20–40 selected hours |
| [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) | Free voluntary guidance; landing read, linked actions unreviewed and update pending | 4–8 selected hours |
| [Hands-On Machine Learning, 3rd ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) | Paid book/subscription; Aurélien Géron, October 2022, 864 pages; selected public metadata and opening TOC only | 20–35 selected hours |

Verify any claimed PCEI alignment, release status, practice availability, runtime, and price. Avoid exam-dump products and validate volatile AI claims against primary sources.

The Google prerequisites page expects Python and basic math and names NumPy/pandas for its exercises; hosted exercise availability is not evidence that an account or notebook was used here. Microsoft’s headline curriculum scope exceeds this exam and emphasizes scikit-learn, which was absent locally. Elements of AI separates a conceptual introduction from Building AI, where basic Python is recommended. The O’Reilly listing confirms the third edition’s identity, but its publisher reading estimate is not a learner completion promise or review of paid content.

See the [dated deep-review report](../docs/research/2026-09-30-pcei-30-01-deep-review.md) for exact source-reading boundaries, executable receipts and remaining blockers. Independent human review, full PDF reading, the optional pandas/Matplotlib exercise, external model trials and completion of the twelve labs remain pending.
