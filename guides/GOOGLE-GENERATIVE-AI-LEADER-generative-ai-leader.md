---
exam_code: GOOGLE-GENERATIVE-AI-LEADER
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/generative-ai-leader
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Google Cloud Generative AI Leader Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 29, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#google-generative-ai-leader-coverage-record). The [official certification page](https://cloud.google.com/learn/certification/generative-ai-leader) and its linked [exam guide](https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf) are authoritative.

**CURRENT BLUEPRINT — current baseline:** Four domains weighted 30%, 35%, 20%, and 15%; current PDF and study workbook checked September 29, 2026<br>
**Upcoming blueprint change:** None announced as of September 29, 2026.<br>
**Official source:** [Generative AI Leader certification page](https://cloud.google.com/learn/certification/generative-ai-leader) · [official detailed exam guide](https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf)

## How to use this guide

This certification is about strategic leadership and influence, not technical implementation. Learn enough system structure to ask good questions and make defensible choices. For every use case, state the business decision or workflow, user and affected parties, permitted data and actions, success and safety measures, best-fit Google offering, human-control boundary, operational owner, and stop/rollback condition.

The current exam is 90 minutes, USD 99 before applicable tax or regional differences, 50–60 multiple-choice questions, online- or onsite-proctored, available in English, Japanese, Spanish, and Portuguese, valid for three years, and has no prerequisite. Renewal is available during the eligibility period. Verify the [live page](https://cloud.google.com/learn/certification/generative-ai-leader) before scheduling.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central decision |
|---|---:|---|
| Fundamentals of gen AI | ~30% | What can the technology do, what data/model/layer fits, and where are its limits? |
| Google Cloud's gen AI offerings | ~35% | Which ready-made application, enterprise agent/search/CX offering, platform, model, API, or tool fits? |
| Techniques to improve gen AI model output | ~20% | Should prompting, grounding/RAG, customization, settings, evaluation, or human review improve the result? |
| Business strategies for a successful gen AI solution | ~15% | How should value, adoption, security, responsibility, and measurable change be governed? |

The current exam PDF contains 61 enumerated considerations under 15 numbered objectives, distributed 21/18/10/12 across the domains. Three data considerations repeat under 1.1 and 1.2; the count preserves the published occurrences. The certification page says the exam was recently rebranded, without giving a revision date.

The current guide uses 2026 product names such as Gemini Enterprise Agent Platform, Agent Platform, Agent Studio, Agent Search, and Agent Platform AutoML. Older training commonly says Vertex AI, Vertex AI Agent Builder/Search, Agentspace, or Generative AI Studio. Treat those as historical/product-transition terms and **VERIFY CURRENT** against the exam PDF and first-party documentation. The exam PDF remains the scope authority: it still names **Cloud Functions** and **Customer Engagement Suite**, while the study workbook uses Cloud Run functions and Gemini Enterprise for Customer Experience terminology. Learn the capability and map the labels; do not silently replace the exam wording with every newer product name.

---

## 1. Fundamentals of generative AI — about 30%

### A connected mental model

Artificial intelligence is the broad field of systems performing capabilities associated with intelligence. Machine learning learns patterns from data rather than encoding every rule. Deep learning uses multilayer neural networks. Natural-language processing concerns human language. Generative AI produces new content—text, code, images, audio, video, or structured output—from learned patterns. A large language model is a foundation model specialized in language and related representations; multimodal models accept or generate more than one modality. Diffusion models iteratively transform noise toward a learned image/video/audio distribution.

Foundation models are pretrained broadly and can be adapted to many tasks. **Prompt engineering** changes the human-readable instructions or examples supplied at inference. **Prompt tuning**, in the learned soft-prompt sense described by [Google Research](https://research.google/blog/guiding-frozen-language-models-with-learned-soft-prompts/), trains a small set of input vectors while the base model remains frozen. It differs from manually rewriting a prompt and from changing model weights or adapters through fine-tuning. Few-shot examples in a request do not by themselves update weights. The 2022 research explains the concept; it does not establish that every current Google model offers that tuning method. They are probabilistic: a fluent response is not proof of truth, authorization, fairness, or safe action. The useful business unit is therefore not “the model”; it is the whole system of data, model, prompt/context, retrieval, tools, identity, application, evaluation, humans, and operations.

| Learning approach | Signal | Typical business fit | Misconception |
|---|---|---|---|
| Supervised | Labeled input-output examples | Classification, prediction, extraction | Labels are automatically unbiased or correct |
| Unsupervised | Patterns in unlabeled data | Segmentation, representation, anomaly discovery | Every discovered cluster has business meaning |
| Reinforcement | Reward from actions/interactions | Sequential decisions and policy optimization | A reward fully expresses safe human intent |
| Foundation-model prompting | Instructions and context at inference | General creation, summarization, discovery, automation | A better prompt removes the need for evaluation |

### Create, summarize, discover, and automate

Creation generates drafts, images, code, video, or personalized material. Summarization compresses information. Discovery finds and synthesizes relevant knowledge. Automation connects understanding or generation to a workflow; an agent may observe, reason/plan, call tools, and act repeatedly toward a goal.

Start with the existing workflow rather than an AI feature. High-value candidates have meaningful volume or delay, adequate authorized data, a measurable output, tolerable error paths, and an accountable owner. Avoid automating a broken process or an inherently high-consequence judgment without suitable human authority.

Examples:

- Drafting marketing variations can tolerate review before publication.
- Summarizing a case can accelerate an employee but must preserve source links and access boundaries.
- Enterprise search needs permission-aware retrieval, freshness, citations, and “not found” behavior.
- A service agent that issues refunds requires identity, transaction limits, policy checks, human escalation, audit, and reversal.

### Data determines what is possible and permissible

Structured data follows a defined model, while unstructured data includes prose, images, recordings, and video. Labeled data carries target annotations; unlabeled data does not. Quality includes completeness, consistency, relevance, availability, cost, and usable format; in practice also examine accuracy, timeliness, uniqueness, provenance, permission, representativeness, and leakage.

Accessibility never means broad uncontrolled access. It means the authorized system can obtain fit-for-purpose data with governed identity, purpose, lineage, residency, retention, and deletion. First-party enterprise data can create differentiation, but customer content, employee records, licensed works, regulated data, and secrets require purpose-specific legal and security review.

The ML lifecycle is ingestion → preparation → training or model selection/customization → deployment → management. Unlabeled data can be curated, structured and useful; lack of target labels does not mean meaningless or unprocessed data. Generative systems add prompt/context, retrieval index, tool, policy, eval-set, and model-version lifecycles. A leader should ask who owns each artifact, what evidence permits promotion, and what triggers rollback.

| Lifecycle responsibility | Tool category or Google example | Evidence to request |
|---|---|---|
| Ingest and prepare | Governed stores, databases and repeatable data pipelines | Permission, lineage, quality, schema and train/evaluation separation |
| Train or customize | Managed training, supported AutoML/tuning, experiment tracking | Dataset and model version, baseline, cost and independent evaluation |
| Register and deploy | Model Registry and a supported serving endpoint/API | Artifact identity, approval, serving configuration and rollback route |
| Manage and improve | Pipelines, Feature Store, Model Monitoring and application telemetry | Reproducibility, relevant features, drift signal and measured task quality |

[Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction) manages your models and versions; **Model Garden** helps discover model choices. The workbook's broad storage wording should not make these interchangeable. [Deployment documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/overview) distinguishes managed APIs from models needing a deployed endpoint: finding a model card does not mean capacity is already running. A Model Garden update does not automatically update your imported model. [MLOps guidance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/introduction-mlops) also separates drift/skew alerts from evaluation: changed inputs may warrant investigation, but do not alone prove lower task accuracy.

### Choose model and layer deliberately

| Gen-AI layer | Supplies | Leadership question |
|---|---|---|
| Infrastructure | Accelerators, compute, storage, networking, systems software | Does scale/performance/control justify operating at this layer? |
| Model | Learned generation/reasoning capability | Which modality, context, quality, safety, latency, cost, geography and customization fit? |
| Platform | Model access, data, building, evaluation, deployment and operations tools | Can governed teams build consistently without assembling every component? |
| Agent | Goal loop plus tools, state and policy | What may act, under whose identity, with what limits and approval? |
| Application | User workflow and experience | Does it solve the measured task safely and inclusively? |

Gemini is Google’s flagship multimodal family. Gemma provides model options suited to customization and local/controlled deployments. Check the exact version's [license and terms](https://ai.google.dev/gemma/terms): the current terms page directs Gemma 4 to a separate license. A family name or access to weights does not establish identical use, distribution or support rights across versions. Imagen generates images. Veo generates video. Model versions and capabilities change; select by evaluated workload evidence, not newest-name bias.

Model choice considers modality, context window, input/output and data restrictions, security/privacy, regional availability, reliability, quality, latency, throughput, price, fine-tuning/customization support, openness, and operational skill. A larger context window may enable more input but can raise cost/latency and does not make all included information equally usable.

> **Related item:** An embedding maps content to a numeric representation useful for semantic similarity. It supports retrieval, clustering, and recommendations; it is not a citation, truth score, or permission check.

---

## 2. Google Cloud's generative AI offerings — about 35%

### Select the consumption surface first

| Need | Candidate surface | Why | Boundary to verify |
|---|---|---|---|
| Individual general assistance | Gemini app / Gemini Advanced and Gems | Fast personal creation, analysis, and reusable custom instructions | Account tier, data handling, connectors, sharing and current naming |
| Assistance inside work tools | Gemini for Google Workspace | Meets users in Gmail, Docs, Sheets, Slides, Meet and related workflows | Licensing, admin controls, source permissions and review |
| Grounded document research | Gemini Notebook / NotebookLM and the distinct Gemini Notebook Enterprise surface | Synthesizes and explores supplied sources | Consumer versus enterprise account, API availability, licenses, source permissions and sharing |
| Permission-aware enterprise search/agents | Gemini Enterprise and Agent Search | Connects governed enterprise knowledge and custom agents | Connector permissions, freshness, authorization trimming and product availability |
| Customer engagement | Customer Engagement Suite | Conversational agents, Agent Assist, conversation insights and cloud contact-center capabilities | Channel integration, identity, consent, escalation, latency and human operation |
| Rapid prototype | Google AI Studio | Quickly explore Gemini models/prompts | Prototype controls and quotas are not production architecture |
| Governed custom production solution | Agent Studio / Agent Platform | Model Garden, search/RAG, AutoML/customization, agents, evaluation and operations | Exact service naming, region, release stage and responsibility |

The [Gemini Enterprise app](https://docs.cloud.google.com/gemini/enterprise/docs) is the employee search/assistant/agent surface; [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) supplies developer and operational capabilities. The [April 22, 2026 announcement](https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development) explains this relationship and the evolution from Vertex AI. Neither a product name nor a low-code designer proves all governance requirements are configured.

The workbook's notebook exercise points to `notebooklm.google.com`; the exam also names **Gemini Notebook API**. The [current enterprise notebook API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) is documented as **preview**, requires enterprise setup/licenses, and manages notebooks within a cloud project. Do not infer that a personal notebook account grants enterprise API access or identical sharing/data controls. **VERIFY CURRENT** for the specific edition and interface.

Prebuilt applications reduce time and engineering, but the organization still governs identity, data, acceptable use, output review, records, integration, adoption, and value. Custom platforms enable differentiation and control while adding design, security, evaluation, deployment and operating work.

### Google’s platform value proposition

Google presents an AI-first ecosystem with integrated applications, an enterprise-ready platform, open and first-party model choices, AI-optimized infrastructure, low/no-code paths, APIs, data control, agents, and security/responsible-AI practices. AI Hypercomputer combines TPUs/GPUs, network/storage/system design and software rather than representing one accelerator. Evaluate workload performance, utilization, availability, capacity plan, flexibility and total cost.

**PRACTICAL DEPTH — VERIFY CURRENT:** data handling follows the actual service, account and terms. Under the [Gemini Developer API terms](https://ai.google.dev/gemini-api/terms), unpaid services generally permit product-improvement use and human review, with specified regional exceptions. Paid-service treatment differs, and the definition for AI Studio depends on account/project access or an enterprise Workspace account, not simply whether the UI charges a fee. The API has its own billed-project condition. Confirm the route before supplying organizational data; a personal upgrade name is not proof of enterprise protection.

“Not used for training” and “not retained” are separate claims. [Developer API retention guidance](https://ai.google.dev/gemini-api/docs/zdr) lists abuse monitoring, grounding, uploaded files, caches and conversation state. [Agent Platform guidance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention) has its own feature-specific controls and exceptions. A no-training commitment does not turn off logging, stored interactions or grounding retention. State the platform, enabled features, data path and retention requirement explicitly rather than applying one retention number everywhere.

“Enterprise-ready” is a claim to test: identity integration, tenant/data behavior, encryption/key options, residency, availability, support, logging, policy, compliance evidence, model-change policy, portability, recovery, and contractual commitments must match the organization’s requirement.

Model Garden provides model choice across Google, third-party, and open options. Managed model building/customization reduces infrastructure work. Low/no-code tools democratize access but do not remove the need for governed data, competent reviewers, change control, evaluation, or an escalation path.

### Search, grounding, RAG, and customer experience

External consumer search, enterprise search, and retrieval for generation are related but distinct. Search returns or ranks information; grounding connects generated output to supplied sources or world data; retrieval-augmented generation retrieves context and gives it to a model for a response. Permission-aware enterprise retrieval must enforce the source system’s authorization at query time and during indexing, not only hide links after generation. [Custom Cloud Storage/BigQuery sources](https://docs.cloud.google.com/gemini/enterprise/docs/identity) require appropriate identity, document ACL metadata and an access-controlled store. The [identity configuration guide](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider) says access control is selected when creating the store; it cannot simply be enabled later on an existing store. Changing the identity provider does not automatically migrate existing stores. Design identity mapping, ingestion/federation behavior, group changes and revocation tests before importing data. These are configuration obligations, not guarantees that every connector has identical synchronization behavior.

A RAG system includes ingestion, parsing, chunking, metadata, embeddings/index, query transformation, retrieval, filters, reranking, prompt/context construction, generation, citation rendering, evaluation, freshness, deletion and access control. A weak response can originate at any layer. Adding RAG does not guarantee correct retrieval or faithful generation.

Customer Engagement Suite capabilities span conversational self-service, real-time assistance for human agents, insight from interactions, and contact-center platform functions. Choose based on desired customer journey and human role. A bot that cannot authenticate, resolve, or escalate may reduce staffing cost while making the customer outcome worse.

### Agents and tools

An agent combines a model, reasoning/decision loop, instructions, memory/state as appropriate, and tools. Tools may be API extensions, function calls, data stores, plugins, or Google/prebuilt APIs. Cloud Storage and databases supply governed data; Cloud Run and Cloud Run functions host actions; speech, translation, document, vision, video, and language APIs supply specialized perception/transformation.

Tool selection asks:

1. Is read-only retrieval sufficient, or may the agent change state?
2. Which end-user or workload identity authorizes the action?
3. Are tool schemas and arguments validated independently of generated text?
4. What data may cross the boundary?
5. What limit, confirmation, approval, timeout, retry, idempotency, audit and reversal exist?
6. How does the system behave when the model, tool, dependency, or network fails?

[Function calling](https://ai.google.dev/gemini-api/docs/function-calling) supplies a proposed function name and arguments; the application is responsible for execution. [Structured output](https://ai.google.dev/gemini-api/docs/structured-output) helps satisfy a supported schema, but valid JSON can still contain the wrong customer, amount or claim. Validate semantics, authenticated identity, current permission, operation limits and approval independently; SDK automation belongs inside that same boundary.

For a refund proposal, distinguish four tests: the payload parses; the amount and order are valid; the caller can act on that order; and a trusted approval covers this exact action. A retry must not create a second refund, while the same retry identifier with changed amount must not silently reuse an earlier approval. These are proposed control tests, not an executed financial integration.

Use the simplest deterministic control for deterministic requirements. Let a model interpret language or select among bounded options; keep pricing, eligibility, safety, financial, legal, and permission rules in testable policy/code where possible.

### Specialized APIs versus general models

Speech-to-Text transcribes; Text-to-Speech synthesizes speech; Translation and Document Translation translate while the latter preserves document structure; Document AI extracts from documents; Vision and Video Intelligence analyze media; Natural Language analyzes text. A general multimodal model may overlap, but a specialized API can provide a narrower contract, predictable schema, domain capability, or operating model. Compare actual accuracy, format, latency, cost, languages, safety, compliance and integration.

> **Related item:** Function calling lets a model propose a structured tool invocation; the application must validate and authorize it. It does not give the model direct implicit permission to act.

---

## 3. Techniques to improve model output — about 20%

### Diagnose before choosing a technique

| Symptom | Likely intervention | Why another intervention may be weaker |
|---|---|---|
| Vague or inconsistent task | Clear instruction, constraints, examples, schema | Fine-tuning a poorly specified requirement preserves confusion |
| Missing current/private facts | Grounding/RAG with authorized sources | Prompt wording cannot supply unknown facts reliably |
| Stable domain style/behavior gap | Prompt tuning or fine-tuning after baseline evidence | Retrieval supplies facts but may not change durable behavior |
| Unsupported high-consequence decision | Human-in-the-loop and narrower automation | Temperature reduction does not create authority or correctness |
| Wrong source retrieved | Improve ingestion/chunking/metadata/query/retrieval/rerank | Changing the generator cannot repair absent evidence |
| Correct evidence but unfaithful answer | Better context/instruction/model, citation/faithfulness eval | Adding more documents can increase noise |
| Unsafe tool action | Identity, allowlist, validation, policy, approval, sandbox, limit | A “be safe” prompt is not an enforcement boundary |

Foundation models can hallucinate, reflect bias, miss edge cases, depend on training and cutoff knowledge, and vary across versions. Use multiple layers: task design, quality/authorized data, model selection, prompting, grounding, customization, safety settings, deterministic validation, human review, continuous evaluation, monitoring and rollback.

### Prompting is interface design

A good prompt establishes task, relevant role/context, input delimiters, constraints, allowed sources, output format, examples, uncertainty/abstention behavior, and acceptance criteria. Zero-shot provides instruction only; one-shot and few-shot add examples. Role prompting sets perspective, not authority. Prompt chaining decomposes a workflow with intermediate checks.

ReAct-style patterns interleave reasoning and action/tool observations. Do not depend on exposing hidden chain-of-thought. Ask for concise rationale, cited evidence, structured intermediate artifacts, or verifiable calculations instead. Sensitive internal reasoning is neither a control nor a substitute for external validation.

Version prompts and their evaluation results. Untrusted content can contain prompt injection; isolate system policy from data, label content, constrain tools, validate output/actions, and test adversarial cases.

### Grounding and RAG boundaries

First-party grounding uses authorized organizational data; third-party grounding uses licensed/contracted external data; world grounding may use Google Search or broad public information. Each has different freshness, provenance, permission, privacy, attribution, and reliability. The presence of a citation does not prove the claim is entailed by the cited text.

Evaluate retrieval separately with relevance/coverage and permission tests, then generation with faithfulness, completeness, citation correctness, safety and usefulness. Test “answer absent,” conflicting sources, stale documents, revoked access, deleted records and malicious documents.

### Sampling and limits

Temperature changes randomness; top-p limits sampling to a cumulative probability mass. Lower values tend toward consistency, not truth. Tokens are model-specific units, not a fixed count of words or characters. Token/output limits cap generated length and influence truncation, latency and cost; a truncated schema response still needs failure handling. Safety settings influence filtered behavior and need domain testing. Set values from eval results; changing several at once prevents clear attribution.

### Continuous evaluation and change control

Maintain representative, edge, adversarial and slice-based eval sets. Track business KPI and task success along with quality, groundedness, safety, fairness, latency, throughput, availability, token/tool use and cost. Monitor drift in inputs, retrieval corpus, behavior and user outcomes. Treat automatic model upgrades, security patches, model retirement, prompts, index updates and feature-store changes as versioned changes with compatibility tests, staged rollout and rollback.

> **Related item:** An offline evaluation is repeatable and safe for comparison; an online experiment measures real behavior but exposes users and systems. Production changes often need both, plus guardrails and an incident path.

---

## 4. Business strategies for successful gen AI — about 15%

### Move from possibility to portfolio

Create an opportunity inventory across employee productivity, customer experience, product innovation, operations and research. Prioritize with a transparent rubric:

| Dimension | Question |
|---|---|
| Value | Which revenue, cost, risk, quality, speed, access or experience metric changes? |
| Feasibility | Are data, integration, model capability, skills and operating capacity available? |
| Risk | What harm follows wrong, biased, leaked, unsafe or unauthorized behavior? |
| Adoption | Does it fit the workflow, and will users understand and challenge it? |
| Evidence | Can a baseline, counterfactual and pilot measure the change? |
| Reversibility | Can scope be bounded, human control preserved, and rollback performed? |

Begin with a bounded workflow and explicit non-goals. Establish baseline, sponsor, product owner, domain reviewers, security/privacy/legal/data roles, operators, training, feedback and incident processes. Prototype to learn, pilot with representative users and controlled data, evaluate against gates, then scale incrementally. A pilot is successful when it answers a decision—not when it produces an impressive demo.

### Measure impact honestly

Leading measures include adoption, completion, override, escalation, error, safety event, latency and cost. Lagging measures include cycle time, resolution, revenue, loss, satisfaction, quality, employee experience or risk reduction. Measure displaced work and newly created review/rework. An hour of potential capacity is not automatically an hour of eliminated payroll or realized revenue; state how the capacity will be used and measured. Separate correlation from causation with comparison groups or staged rollout where practical. Monitor distributional effects: an average gain can hide harm to a language, disability, region or customer group.

Total cost includes licenses/API tokens, retrieval/indexing, tools, data preparation, evaluation, integration, security, operations, support, human review, change management, incidents and exit. Unit economics should connect cost to a valuable completed outcome rather than requests alone.

### Secure AI with SAIF and defense in depth

Google’s [Secure AI Framework](https://saif.google/) treats AI security as an ecosystem/lifecycle problem. Its [original six-part framework](https://blog.google/innovation-and-ai/technology/safety-security/introducing-googles-secure-ai-framework/) connects established security foundations, AI-aware detection/response, automated defenses, consistent platform controls, adaptive feedback and the surrounding business process. Turn each into an owner and evidence requirement: for example, control coverage, incident exercises, bounded response automation, common policies, adversarial regression cases and an end-to-end risk review. The 2023 article provides the framework's origin, not current product availability or a claim that one filter secures an entire system. Threat-model data, supply chain, infrastructure, model, prompt/context, retrieval, agent/tools, application, user and operations. Apply secure-by-design infrastructure, IAM, Security Command Center, monitoring, data controls, isolation, provenance, evaluation, detection, response and recovery.

Protect against prompt injection, poisoned sources, sensitive-data disclosure, model/supply-chain compromise, insecure tool calls, excessive agency, denial of service/resource exhaustion, evasion, theft and misuse. Least privilege applies to people, pipelines, deployed models and agents. **PRACTICAL DEPTH:** [Model Armor](https://docs.cloud.google.com/model-armor/overview) detection, model refusal and application enforcement are distinct. Inspect-only observations do not prove a tool action was blocked; a blocking verdict must be honored by the integration. [Coverage varies by integration and modality](https://docs.cloud.google.com/model-armor/integrations), so test the actual path. These controls supplement identity and business rules. High-impact actions require independent authorization and often human approval. Log what is needed for accountability while redacting secrets and respecting privacy.

### Responsible AI is operating governance

Responsible AI covers purpose, benefit, fairness, safety, privacy, security, transparency, explainability, accountability, inclusivity and human control. Anonymization aims to prevent reidentification; pseudonymization replaces direct identifiers but can usually be reversed with separately protected information. Neither permits arbitrary reuse or eliminates linkage risk.

Document intended and prohibited use, data provenance/consent, performance and limitations by relevant group, human role, monitoring, user notice and recourse. Model cards or system documentation support transparency, but accountability requires named decision owners and enforcement. When capability, law, product terms or observed harm changes, reassess.

> **Related item:** Governance establishes decision rights, policy, evidence and accountability. Guardrails implement some constraints. A guardrail without an owner, monitoring, exceptions process and incident response is not complete governance.

---

### Local evidence worksheet: access, evaluation and value

**PRACTICAL DEPTH — executed locally:** this original Python worksheet uses a tiny exact-user ACL model, twenty invented rubric observations and fictional cost assumptions. It makes no model, embedding, retrieval-service or cloud call. The ACL model assumes trusted identity and up-to-date metadata; it does not implement provider IAM, groups, inheritance, connector synchronization or concurrent updates. The required slices and pass thresholds are teaching choices, not Google certification requirements or evidence of statistical reliability.

Save as `evidence_workbook.py` and run `python evidence_workbook.py`.

```python
"""Original local models: no model call, cloud ACL, or real user identity."""
from fractions import Fraction as F
from decimal import Decimal as D


def authorized_context(candidates, documents, readers, principal):
    """Candidates can be stale; current trusted records are checked again.

    This tiny model has exact per-user ACLs only, not groups, inheritance,
    service IAM, connector synchronization, identity proof, or concurrency.
    """
    if not principal:
        return []
    result = []
    for document_id in dict.fromkeys(candidates):
        if document_id in documents and principal in readers.get(document_id, set()):
            result.append((document_id, documents[document_id]))
    return result


def evaluate_pilot(rows, overall_floor, slice_floor):
    if not rows:
        raise ValueError('An empty evaluation cannot pass')
    if {name for name, _, _ in rows} != {'majority', 'small_slice'}:
        raise ValueError('This worksheet requires evidence for both named slices')
    # Each row is an independently recorded rubric result, not a model judge.
    if any(type(good) is not bool or type(unsafe) is not bool
           for _, good, unsafe in rows):
        raise ValueError('Rubric outcomes must be explicit booleans')
    scores = {}
    for name in sorted({name for name, _, _ in rows}):
        group = [good for label, good, _ in rows if label == name]
        scores[name] = F(sum(group), len(group))
    overall = F(sum(good for _, good, _ in rows), len(rows))
    violations = sum(unsafe for _, _, unsafe in rows)
    passed = (overall >= overall_floor and
              all(score >= slice_floor for score in scores.values()) and
              violations == 0)
    return overall, scores, violations, passed


def run():
    count = 0

    def check(condition):
        nonlocal count
        if not condition:
            raise AssertionError('Evidence worksheet mismatch')
        count += 1

    documents = {'public': 'Approved public instructions.',
                 'finance': 'Fictional finance figure: 731.',
                 'other': 'Fictional other-team figure: 842.'}
    readers = {'public': {'lee', 'sam'}, 'finance': {'lee'}, 'other': {'sam'}}
    candidates = ['finance', 'public', 'other', 'missing', 'finance']
    check([key for key, _ in authorized_context(candidates, documents, readers, 'lee')]
          == ['finance', 'public'])
    check([key for key, _ in authorized_context(candidates, documents, readers, 'sam')]
          == ['public', 'other'])
    check(authorized_context(candidates, documents, readers, '') == [])
    check(authorized_context(candidates, documents, readers, 'unknown') == [])
    # Hiding a citation after building context has already exposed its content.
    unsafe_context = '\n'.join(documents[k] for k in candidates if k in documents)
    check('842' in unsafe_context)
    safe_context = '\n'.join(text for _, text in authorized_context(
        candidates, documents, readers, 'lee'))
    check('731' in safe_context and '842' not in safe_context)
    readers['finance'].remove('lee')
    check(authorized_context(candidates, documents, readers, 'lee')
          == [('public', documents['public'])])
    del documents['public']
    check(authorized_context(candidates, documents, readers, 'lee') == [])
    # Missing ACL metadata fails closed even when a candidate contains the ID.
    documents['orphan'] = 'Fictional text without an ACL.'
    check(authorized_context(['orphan'], documents, readers, 'lee') == [])
    readers['orphan'] = {'lee'}
    check(len(authorized_context(['orphan', 'orphan'], documents, readers, 'lee')) == 1)
    check(authorized_context([], documents, readers, 'lee') == [])

    # Twenty synthetic rubric observations, not twenty actual LLM executions.
    baseline = [('majority', True, False)] * 18 + [('small_slice', False, False)] * 2
    overall, slices, violations, passed = evaluate_pilot(baseline, F(9, 10), F(4, 5))
    check(overall == F(9, 10))
    check(slices == {'majority': F(1), 'small_slice': F(0)})
    check(violations == 0 and not passed)
    repaired = baseline[:18] + [('small_slice', True, False)] * 2
    check(evaluate_pilot(repaired, F(9, 10), F(4, 5))[3])
    unsafe = repaired[:-1] + [('small_slice', True, True)]
    result = evaluate_pilot(unsafe, F(9, 10), F(4, 5))
    check(result[0] == 1 and result[2] == 1 and not result[3])
    check(not evaluate_pilot(baseline, F(19, 20), F(4, 5))[3])
    for invalid in [[], [('majority', True, False)],
                    [('majority', None, False), ('small_slice', True, False)]]:
        try:
            evaluate_pilot(invalid, F(9, 10), F(4, 5))
        except ValueError:
            check(True)
        else:
            raise AssertionError('Invalid evaluation was accepted')

    # Potential capacity, with no assumption that time becomes cash savings.
    tasks, adoption, saved_minutes = D('1000'), D('0.60'), D('4')
    gross_hours = tasks * adoption * saved_minutes / 60
    review_hours, rework_hours, hourly_value, monthly_cost = D('12'), D('8'), D('40'), D('1000')
    net_hours = gross_hours - review_hours - rework_hours
    capacity_value = net_hours * hourly_value
    check(gross_hours == D('40'))
    check(net_hours == D('20'))
    check(capacity_value == D('800'))
    check(capacity_value - monthly_cost == D('-200'))
    break_even_adoption = ((monthly_cost / hourly_value + review_hours + rework_hours)
                          * 60 / (tasks * saved_minutes))
    check(break_even_adoption == D('0.675'))
    check(break_even_adoption > adoption)
    check((tasks * break_even_adoption * saved_minutes / 60
           - review_hours - rework_hours) * hourly_value == monthly_cost)
    print(f'{count} local checks passed; no cloud or model execution')
    print('90% overall can fail a slice gate; 100% task success can fail a safety gate')
    print('40 gross hours, 20 net hours, 800 capacity value, -200 versus assumed cost')
    return count


if __name__ == '__main__':
    run()
```

Expected: **27 local checks pass**. Revoked or deleted content is excluded even if its ID remains in an old candidate list. Hiding a citation after constructing context would be too late. A 90% overall score fails the required small-slice gate, and perfect task success still fails a safety gate. Missing evidence does not pass. This checks arithmetic and explicit local rules, not a model's safety, factuality or cloud access enforcement.

The value case yields 40 gross hours and 20 net hours after review/rework. At an assumed 40 per hour, 800 of potential capacity value falls 200 short of a 1,000 monthly cost. The 67.5% break-even adoption assumes review/rework remain fixed; changing workload mix, quality or those costs changes the result. Measure realized benefit separately. Two observations in a small slice demonstrate a blind spot but cannot establish a production failure rate.

## Integrated scenarios

### Scenario 1: Permission-aware knowledge assistant

The outcome is reduced employee search time without cross-team data leakage. Baseline search success and time. Select Gemini Enterprise/Agent Search or a governed Agent Platform RAG design based on connector and customization needs. Preserve source permissions at ingestion and query, add citations and abstention, test revoked access and malicious documents, measure retrieval relevance separately from answer faithfulness, monitor latency/cost and user overrides, and create a feedback/deletion/reindex/incident process.

### Scenario 2: Customer-service agent with transactional tools

Separate conversational triage from account actions. Customer Engagement Suite capabilities may support conversation, human Agent Assist and insights; a custom agent may call order/refund tools. Authenticate the customer, scope the agent identity and tool schema, keep eligibility/limit rules deterministic, require confirmation or human approval for consequential changes, make calls idempotent and auditable, redact sensitive logs, and provide escalation and reversal. Measure containment only alongside resolution, correctness, satisfaction, safety and total cost.

### Scenario 3: Marketing content portfolio

Use Gemini for drafts, Imagen for images and Veo for video only where brand, rights, consent and regional policies permit. Ground factual claims in approved sources, use templates/examples for style, review accessibility and representation, retain human publication authority, version model/prompt/assets, and measure cycle time plus correction, rejection, conversion, complaint and cost. A productivity gain that increases legal review or harms a customer group is not a net win.

## Hands-on labs

These eight activities are **proposed labs**. Only the exact local worksheet above was executed. No Gemini call, managed retrieval, cloud policy, paid lesson, provider lab, notebook, model deployment or external tool action was performed. Use public or synthetic data and an authorized account when extending them into live practice; record the actual model, account/data terms, configurations and cleanup.

1. **Use-case scorecard:** rank ten candidate workflows by value, feasibility, risk, adoption, evidence and reversibility; reject at least three and defend the decision.
2. **Model-selection memo:** compare Gemini, Gemma, Imagen and Veo plus build/buy choices for one portfolio; include modality, context, quality, security, availability, latency, price and customization.
3. **Prompt experiment:** create a task/constraint/schema prompt and zero/one/few-shot variants; hold model/settings constant, use a 20-case eval, record errors and select from evidence.
4. **Grounding experiment:** build a small authorized source set; test retrieval relevance, answer faithfulness, citations, absent/conflicting/stale facts, deletion and revoked permission.
5. **Agent threat model:** diagram user → application → model → retrieval → tools → systems; assign identities, limits, approvals, logs, kill switch and recovery; test an injection without performing an external action.
6. **Offering map:** place 12 scenarios among Gemini app/Gems, Workspace, Notebook, Gemini Enterprise/search, Customer Engagement, AI Studio, Agent Studio/Platform and specialized APIs; explain rejected neighbors.
7. **Responsible-AI review:** create intended/prohibited uses, affected groups, data permissions, slice metrics, human role, notice/recourse, monitoring and incident triggers for one scenario.
8. **Executive capstone:** propose a 90-day bounded pilot with baseline, success/safety gates, RACI, architecture boundary, total cost, adoption plan, evaluation, security, rollback and scale/stop decision.

| Lab | Evidence required | Negative case |
|---|---|---|
| 1 | Ten scored use cases, three rejected candidates, explicit owners and assumptions | High headline value with unauthorized data or no measurable baseline |
| 2 | Version-specific capability, license, service/account and total-cost comparison | Treating every family version or endpoint as having identical rights and retention |
| 3 | Fixed twenty-case evaluation, prompt/model/settings versions, failures and repeatability limits | A few successful demos mistaken for a measured improvement |
| 4 | Authorized context, retrieval/answer scores, citations, deletion and revocation evidence | Restricted text enters context before its citation is hidden |
| 5 | Identity and tool-policy diagram, exact approval scope, retries, denial and recovery evidence | Valid JSON requests the wrong order or replay performs an action twice |
| 6 | Twelve scenarios with consumer/enterprise/API distinctions and rejected alternatives | Model Garden mistaken for your version registry or a personal notebook for enterprise API access |
| 7 | Required slices, task/safety gates, affected groups, human review capacity and recourse | High aggregate quality hides a failing group or unsafe action |
| 8 | Adoption, net time, realized benefit, full costs, accountable scale/stop decision | Potential capacity value recorded as guaranteed cash savings |

Keep proposed evidence separate from observed results. A written policy or local model does not establish deployed enforcement.

## Original knowledge checks

1. Distinguish AI, ML, deep learning, NLP, generative AI, foundation model, and LLM.
2. How do supervised, unsupervised, and reinforcement learning differ?
3. Why is fluent output not evidence of truth or authority?
4. Give one create, summarize, discover, and automate use case.
5. Which properties make a candidate use case worth piloting?
6. How do structured/unstructured and labeled/unlabeled describe different things?
7. What data qualities and governance properties matter to AI?
8. Which artifacts extend the classic ML lifecycle for a generative system?
9. What are the five layers of the gen-AI landscape?
10. When would Gemini, Gemma, Imagen, or Veo fit?
11. What factors belong in foundation-model selection?
12. Why does a large context window not solve knowledge quality automatically?
13. Contrast personal Gemini, Workspace assistance, enterprise search/agents, customer engagement, and a custom platform.
14. When should Google AI Studio give way to a governed production platform?
15. What does AI Hypercomputer combine?
16. Why must an “enterprise-ready” claim still be evaluated?
17. Distinguish search, grounding, and RAG.
18. Which layers can make a RAG answer fail?
19. How does permission-aware retrieval differ from hiding a link after generation?
20. What components and controls make an agent?
21. Why must a tool call be independently authorized?
22. When can a specialized AI API be better than a general model?
23. Which current blueprint names require a terminology freshness check?
24. When should prompting, RAG, fine-tuning, or human review be used?
25. Contrast zero-shot, few-shot, role, chaining, and ReAct-style prompting.
26. Why should hidden chain-of-thought not be a business control?
27. How do first-party, third-party, and world grounding differ?
28. What must be evaluated separately in RAG?
29. What do temperature, top-p, token limit, and safety settings control?
30. Why do lower randomness settings not guarantee truth?
31. What should continuous evaluation cover?
32. How should automatic model upgrades be governed?
33. Which dimensions belong in a use-case portfolio score?
34. What decision should a pilot answer?
35. How do leading and lagging AI value measures differ?
36. What costs are missing from API-token price alone?
37. Which layers need threat modeling under SAIF-style defense in depth?
38. Contrast anonymization and pseudonymization.
39. What makes responsible AI an operating practice rather than a principle list?
40. What is the difference between a guardrail and governance?
41. How do prompt engineering, learned prompt tuning and few-shot inference differ?
42. Why are Model Garden and Model Registry not interchangeable?
43. Why does a paid or no-training service claim not establish zero retention?
44. What makes a personal notebook different from the enterprise notebook API?
45. Why can schema-valid tool output still require rejection?
46. What must be configured before importing a custom access-controlled search source?
47. How can a strong overall evaluation still fail a launch gate?
48. Why can apparent time savings fail the business case?

## Answers and reasoning

1. Broad intelligent capability; learning from data; multilayer neural learning; language processing; content generation; broadly pretrained adaptable model; language-oriented foundation model.
2. Labeled examples, unlabeled pattern discovery, and action/reward learning.
3. Generation is probabilistic pattern completion; truth, permissions, policy and consequence require external evidence and controls.
4. Draft copy; condense a case; find authorized policy; route and execute a bounded approved workflow.
5. Measurable value, adequate permitted data/capability, bounded tolerable failure, adoption fit, evidence and an accountable owner.
6. Organization/schema versus target annotations; structured data can be labeled or unlabeled.
7. Completeness, consistency, relevance, availability, format, cost, accuracy, timeliness, provenance, permission, representation and leakage controls.
8. Prompts/context, retrieval corpus/index, tools, policies, eval sets and model/config versions.
9. Infrastructure, model, platform, agent and application.
10. General multimodal work; open/custom/local model needs; image generation; video generation, subject to evaluated version capability.
11. Modality, context, quality, security/privacy, geography, availability/reliability, latency/throughput, cost, customization, openness and skill.
12. More content can add noise, stale or unauthorized facts and cost; retrieval/attention and faithfulness still need evaluation.
13. Individual surface; embedded productivity; permission-aware organizational knowledge/actions; contact-center journey; differentiated governed application building.
14. When production needs identity, deployment, policy, evaluation, observability, reliability, scale and accountable change management.
15. Accelerators, compute, storage/networking, orchestration/systems software and consumption/operations choices.
16. Requirements for identity, data, region, reliability, support, logging, policy, compliance, upgrades and contracts are organization-specific.
17. Rank/return information; tie output to evidence; retrieve context and generate from it.
18. Ingestion, parsing/chunking, metadata, embedding/index, query, retrieval/filter/rerank, context, generation, citations, freshness and permission.
19. It prevents unauthorized content from being retrieved or entering context, not merely from being visibly linked.
20. Model, instructions/loop, state, tools and policies plus narrow identity, validation, approval, limits, audit, monitoring, kill switch and recovery.
21. Generated arguments are untrusted; application policy and user/workload identity decide permission.
22. When the narrower contract, schema, domain accuracy, language, latency, safety, compliance or operations fit better.
23. Gemini Enterprise Agent Platform, Agent Platform/Studio/Search/AutoML and older Vertex AI/Agentspace/Studio names; also Cloud Functions versus Cloud Run functions.
24. Clarify task; supply current/private evidence; alter durable behavior after evidence; retain judgment/authority for uncertain or consequential work.
25. No example; several examples; perspective/context; decomposed steps; interleaved decision/tool observation.
26. It is not reliably inspectable, may expose sensitive reasoning and does not enforce policy; use evidence, structured artifacts and external checks.
27. Authorized internal data, contracted external data, and broad public/search data have different permission, provenance and freshness.
28. Retrieval relevance/permission and generation faithfulness/completeness/citation/safety, then end-to-end task outcome.
29. Randomness, probability-mass sampling, length/cost/truncation, and filtering behavior.
30. Consistency is not correctness; missing or false evidence can be repeated deterministically.
31. Representative/edge/adversarial slices, task/business outcome, quality/grounding, safety/fairness, latency/reliability and cost.
32. Version, compatibility-evaluate, stage, monitor and preserve rollback like any dependency change.
33. Value, feasibility, risk, adoption, evidence and reversibility.
34. Whether evidence supports stopping, changing, scaling or further testing against predefined gates.
35. Adoption, completion, override/escalation and errors appear early; business outcome, risk, satisfaction or quality mature later.
36. Data, retrieval, tools, evaluation, integration, people, review, security, operations, support, adoption, incidents and exit.
37. Data, supply chain, infrastructure, model, prompt/context, retrieval, agent/tools, application, user and operations.
38. Prevent reidentification versus replace identifiers with a reversible mapping; both retain governance and linkage risk.
39. Named owners, enforced use/data boundaries, evidence, human control, monitoring, user recourse, incidents and reassessment.
40. A guardrail enforces a constraint; governance supplies decision rights, policy, evidence, accountability, exceptions and lifecycle oversight.
41. Engineering edits textual instructions/examples; learned prompt tuning optimizes soft input vectors against data while freezing the base model; few-shot inference supplies examples without itself updating weights. Supported methods vary by model.
42. Garden supports discovering model options; Registry manages your models and versions. Deployment and serving capacity are additional concerns, and an upstream model-card update does not automatically update your imported artifact.
43. Product-improvement/training use differs from storage for abuse monitoring, grounding, files, caches, logs or conversation state. Check the actual platform, account, features and terms.
44. They have different account, license, project/API and sharing boundaries. The currently documented enterprise management API is preview; a personal account does not establish API entitlement.
45. Schema conformity does not prove factual correctness, ownership, permission, approval or safe replay. Validate those before execution.
46. The appropriate identity provider/mapping, document ACL metadata and access-control selection at store creation, plus tests for group changes and revocation. Existing stores do not automatically migrate when the identity provider changes.
47. Required slice, safety or coverage gates can fail even when the overall average passes. Missing or tiny samples also limit the conclusion.
48. Adoption may be limited, review/rework can consume the benefit, and capacity may not turn into cash savings. Under the worksheet's assumptions, 800 in capacity value does not cover 1,000 in monthly cost.

## Terminology and freshness checklist

Map older **Vertex AI**, **Vertex AI Agent Builder/Search**, **Vertex AI Studio**, **Agentspace**, **NotebookLM**, and **Cloud Functions** content to the exact current exam wording—**Gemini Enterprise Agent Platform**, **Agent Platform**, **Agent Studio**, **Agent Search**, **Gemini Notebook/API**, and **Cloud Run functions**—without assuming a one-to-one commercial or technical replacement. Verify Gemini/Gemma/Imagen/Veo versions, Gemini application tiers, Workspace features, Gems, Customer Engagement Suite components, Model Garden, RAG APIs, AutoML, Google AI Studio, API availability, region, pricing, data terms and release stage. Preserve durable concepts even when the product label changes.

## Source and freshness notes
- Google Cloud controls the domain weights, named examples, delivery, renewal, product names and certification lifecycle.
- The detailed PDF is current as checked, but it does not print a launch/revision date. The source-health and objective snapshots therefore watch the live certification page; any objective or delivery change returns the guide to review.
- Generative AI products, model versions, limits, price, availability, data terms, policies and threat guidance change rapidly. **VERIFY CURRENT** before implementation.
- This guide’s explanations, comparisons, scenarios, labs, checks and answers are original synthesis from public sources. It does not reproduce Google course content, proprietary practice questions or recalled exam items.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one current primary path, add the official guide/workbook and sample questions, and spend additional time on use-case, evaluation, agent-control and responsible-AI exercises. Provider estimates, catalogs, names and access terms change.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official exam guide](https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf), [study guide](https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf), and [sample questions](https://forms.gle/soztS7Q74AXBncATA) | Public, first-party | 3–5 hours with objective mapping and answer review |
| [Google Skills Generative AI Leader path](https://www.skills.google/paths/1951) | Google account; public path confirms five activities and an update about two months earlier | Current durations/access details were not fully exposed; allow 10–14 hours as a study-planning estimate |
| [Google Cloud Generative AI Leader Professional Certificate on Coursera](https://www.coursera.org/professional-certificates/generative-ai-for-leaders) | Coursera audit/subscription terms vary; first-party Google Cloud courses | Landing page says 8 hours, while five course cards total 20 hours (3/4/4/4/5). Treat these as different estimates; choose time based on activities completed |
| [Pluralsight Generative AI Leader path](https://www.pluralsight.com/paths/google-cloud-generative-ai-leader-by-pluralsight) | Paid subscription; four courses, one lab and practice exam | Four course durations sum 5h44m plus a 30-minute lab (rounded path total: 6h). Public dates range December 2025–May 2026, with the lab dated August 11, 2026; add 5–10 hours of planned review |
| [O'Reilly — GenAI on Google Cloud](https://www.oreilly.com/library/view/genai-on-google/9798341623842/) | Paid subscription/book; broader and more technical than the exam | Earlier 9h58m estimate **not reverified** because public access was blocked; allow 5–10 hours for selected practice and terminology mapping |
| [Udemy / in28Minutes Generative AI Leader](https://www.udemy.com/course/google-cloud-certified-generative-ai-leader-certification/) | Paid marketplace course | Earlier 3h51m and August 2026 update **not reverified** because public access was blocked; allow 5–10 hours for exercises/review |

No exact current MeasureUp product was found during this review. The Google-authored Coursera outline lists five courses and practical Gemini, NotebookLM and AI Studio activities; that is public metadata, not evidence of completed provider exercises. Pluralsight's four course titles follow the exam domains, but dates and a lab title alone do not establish full current-product alignment. The sample-form content was not exposed by the fetch, and no paid lessons or assessment questions were read.

For focused technical gaps, use the linked documentation on data handling, access controls, model lifecycle and tool validation. Allow 2–3 additional hours for selected reading and the original worksheet; this is a planning estimate. Google's official sample resource and independently authored exercises can help locate learning gaps. Reject “actual questions,” copied exam material, or guaranteed replicas; use explanation-led assessment to locate a concept or decision gap.
