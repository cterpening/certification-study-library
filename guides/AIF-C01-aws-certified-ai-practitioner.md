---
exam_code: AIF-C01
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# AIF-C01 AWS Certified AI Practitioner Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#aif-c01-coverage-record). The [official AIF-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html) is authoritative.

**Current baseline:** AIF-C01 revision 1.0 dated March 26, 2026; five domains; 50 scored plus 15 unscored questions<br>
**Upcoming blueprint change:** None announced in the official exam-guide index or AIF-C01 pages as of September 1, 2026.<br>
**Important freshness boundary:** The current guide includes agentic AI, MCP, multi-agent patterns, memory, tool use, workflow orchestration, Amazon Quick, Kiro, Strands Agents, and Amazon Bedrock AgentCore. Older courses may cover the original AIF-C01 outline without these additions.<br>
**Official source:** [AWS Certified AI Practitioner exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html)

## How to use this guide

AIF-C01 is a foundational decision exam, not a model-development exam. The target candidate has up to six months of exposure to AWS AI/ML, uses but does not necessarily build solutions, and can connect a business need to a technique, managed service, risk, evaluation method, and governance control. Coding models, feature engineering, hyperparameter tuning, building pipelines, mathematical analysis, and implementing full security or governance programs are explicitly outside the target role.

The certification page lists a 90-minute, 65-question, USD 100 exam delivered online or at Pearson VUE. The detailed guide identifies 50 scored and 15 unidentified unscored questions, multiple-choice, multiple-response, ordering, and matching formats, a 700 minimum scaled score, and compensatory scoring. Recheck the [live exam page](https://aws.amazon.com/certification/certified-ai-practitioner/) before scheduling.

For every topic, practice a five-part answer:

1. What business outcome is required?
2. Is a deterministic rule, traditional ML, a foundation model, or an agent appropriate?
3. What data, model, service, and operating boundary fit?
4. How will quality, safety, security, cost, and business value be measured?
5. What evidence would cause a human owner to approve, correct, pause, or retire it?

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Fundamentals of AI and ML | 20% | Which AI/ML approach fits the problem, data, lifecycle, and success measure? |
| Fundamentals of GenAI | 24% | How do foundation and agentic systems work, where do they help, and what do they cost? |
| Applications of Foundation Models | 28% | How should a model, grounding/customization method, prompt, and evaluation approach be selected? |
| Guidelines for Responsible AI | 14% | How are fairness, safety, transparency, explainability, and human-centered controls made observable? |
| Security, Compliance, and Governance for AI Solutions | 14% | How are identity, data, interactions, evidence, lifecycle, and regulatory obligations controlled? |

The largest domain is application of foundation models, but Domains 4 and 5 change whether a seemingly capable solution is acceptable. Do not study security and responsible AI as end-of-project checklists.

---

## 1. Fundamentals of AI and ML — 20%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html) covers terminology, practical use cases, and the AI/ML lifecycle.

### Choose rules, traditional ML, GenAI, or agents deliberately

| Approach | Best fit | Output contract | Common failure |
|---|---|---|---|
| Deterministic rules | Stable policy with a specific reproducible answer | Same valid input produces the defined result | Rule growth, missed exceptions, and brittle maintenance |
| Supervised ML | Labeled history supports classification or regression | Probability or numeric prediction | Leakage, unrepresentative labels, drift, or wrong threshold |
| Unsupervised ML | Structure must be discovered without labels | Cluster, anomaly, or latent pattern | Clusters interpreted as truth without validation |
| Reinforcement learning | Sequential actions can learn from reward and safe exploration | Policy selecting actions | Unsafe exploration, poorly specified reward, delayed effects |
| Foundation model | Flexible language, image, audio, code, or multimodal task | Nondeterministic generated content | Hallucination, prompt sensitivity, cost, latency, or unsafe output |
| Agentic system | A goal requires reasoning, tools, state, and orchestrated steps | Actions plus evidence and final response | Excess authority, looping, tool misuse, hidden state, or weak approval gates |

AI is the broad field. ML learns patterns from data. Deep learning uses multilayer neural networks. Generative AI creates new content from learned distributions. A foundation model is pretrained broadly and adapted or prompted for many tasks. An agent combines a model with instructions, tools, memory/state, and an execution loop. These categories overlap; they are not maturity levels where the newest option is automatically best.

**Related item:** A workflow can use deterministic validation around probabilistic models. For example, an FM drafts a refund explanation, but policy code enforces eligibility and a human approves unusual amounts. This separation is often safer than asking the model to infer and enforce policy by itself.

### Match problem, data, and evaluation

- **Classification:** select a category, such as fraudulent/not fraudulent. Precision asks how many positive predictions were correct; recall asks how many actual positives were found; F1 balances them.
- **Regression:** predict a numeric quantity, such as demand. Use error measures tied to business tolerance, not accuracy.
- **Clustering:** group similar records without labels. A cluster still needs a defensible business interpretation.
- **Forecasting:** predict time-dependent values while respecting order, seasonality, and changing conditions.
- **Computer vision:** analyze images/video; **NLP** analyzes language; speech services can transcribe or synthesize; recommendation systems rank likely-relevant items.

Accuracy can conceal minority-class failure. A fraud model that predicts “not fraud” for almost every transaction can look accurate in an imbalanced dataset. Set the metric and decision threshold from the cost of false positives and false negatives.

### Lifecycle means evidence from idea through retirement

1. Frame the outcome, affected users, non-AI alternative, risk, and acceptance criteria.
2. Establish data origin, permission, quality, representativeness, retention, and train/evaluate separation.
3. Select a technique/model and baseline; experiment reproducibly.
4. Evaluate technical, subgroup, safety, security, cost, latency, and business measures.
5. Deploy through a controlled interface with identity, logging, version, fallback, and approval boundaries.
6. Monitor inputs, outputs, drift, incidents, cost, adoption, and business outcomes.
7. Retrain, replace, roll back, suspend, or retire from evidence.

Batch inference handles accumulated work; real-time inference serves an interactive request; asynchronous inference decouples longer jobs; serverless inference reduces infrastructure management for suitable traffic. Choose from latency, payload, scale, availability, cost, and control—not from the service label alone.

[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) supports the broader model lifecycle and custom ML work. Managed task services such as Transcribe, Translate, Comprehend, Lex, Polly, Rekognition, Textract, and Personalize provide higher-level capabilities. [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) provides managed access to foundation models and generative-AI capabilities. The current in-scope list also names Amazon Quick, Kiro, Strands Agents, Amazon Q, and AgentCore; verify their current interfaces and boundaries rather than inferring them from older product names.

**Related item:** MLOps makes experiments, data, code, configurations, approvals, deployments, monitoring, and retraining reproducible. It is not merely a CI/CD pipeline; model behavior also depends on data and statistical conditions.

---

## 2. Fundamentals of GenAI — 24%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html) adds foundation-model, token, context-engineering, and current agentic concepts.

### Tokens, embeddings, context, and generation

- A **token** is a model input/output unit, not reliably a word. Context windows and usage prices are commonly token based.
- An **embedding** represents content as a numeric vector so semantically related items can be compared.
- **Chunking** divides source content into retrievable units. Too large wastes context and blurs relevance; too small removes meaning and relationships.
- A **transformer** uses attention-based processing central to many modern language models.
- **Multimodal** models accept or produce more than one modality. **Diffusion** models iteratively generate content such as images.
- **Context engineering** designs the complete information environment: system instructions, conversation, retrieved facts, tool results, memory, examples, permissions, and output contract.

Token optimization is not simply shortening everything. A smaller prompt can omit evidence, while an oversized prompt increases cost, latency, and distraction. Measure task success per interaction, total tokens, latency, retries, cached content, and human correction.

### Foundation-model lifecycle and adaptation ladder

Start with the least invasive method that meets the requirement:

| Method | Changes model weights? | Best fit | Main tradeoff |
|---|---:|---|---|
| Prompting / in-context examples | No | Behavior can be elicited from instructions/examples | Sensitive to phrasing and context budget |
| Retrieval-augmented generation (RAG) | No | Answers need current, private, attributable knowledge | Retrieval quality, permissions, freshness, and citations become critical |
| Fine-tuning | Yes | Repeated domain behavior/style needs examples | Curated training data, evaluation, cost, and lifecycle ownership |
| Continued pretraining | Yes | Deep domain-language adaptation at significant scale | High data/compute/governance burden |
| Distillation | Produces a smaller learned model | A smaller model should emulate selected behavior | Capability loss and new evaluation obligations |
| Training from scratch | Yes, entirely | Exceptional differentiated need and sufficient expertise/data/compute | Highest cost, time, risk, and operational burden |

Pretraining, fine-tuning, evaluation, deployment, feedback, monitoring, and replacement are a lifecycle. Model selection also considers modality, quality, supported languages, context/input-output limits, latency, regional availability, compliance, licensing, customization, safety controls, and price.

### Agentic AI adds an action boundary

An agentic system uses a model to plan or select actions, invoke tools, observe results, maintain relevant state, and continue toward a goal. A multi-agent design assigns roles or capabilities to several agents. MCP is a protocol for connecting AI clients to tools and context; it does not itself make a tool trustworthy or authorize an action.

| Component | Design question |
|---|---|
| Instructions | Is the goal, constraint, stop condition, and escalation path explicit? |
| Tools | Is each input/output schema validated and authority least privileged? |
| Identity | Does the tool act as the user, workload, service, or delegated role? |
| Memory/state | What is stored, scoped, expired, corrected, and disclosed? |
| Orchestration | Is a single agent, supervisor, graph, or deterministic workflow justified? |
| Observability | Can operators reconstruct prompt, retrieval, tool, policy, approval, cost, and outcome? |
| Human control | Which action needs preview, confirmation, separation of duties, or prohibition? |

The [Amazon Bedrock AgentCore documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) describes current infrastructure services for agents. Treat feature names, release stages, regions, identity behavior, and pricing as **VERIFY CURRENT**. The exam asks foundational recognition, not implementation mastery.

**Related item:** A deterministic workflow is often preferable when steps and approvals are known. Agentic autonomy is valuable when the path genuinely needs adaptive reasoning, but each added choice expands test, security, and failure-state complexity.

---

## 3. Applications of Foundation Models — 28%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html) covers model/application design, prompting, training/customization, and evaluation.

### Select the system, not only the model

Begin with a simple baseline and evaluate the end-to-end application. A strong model with weak retrieval, unsafe tools, or ambiguous instructions can be worse than a smaller model in a controlled system.

| Requirement | Likely decision emphasis |
|---|---|
| Current internal answers with citations | RAG, permission-aware retrieval, source metadata, abstention, citation validation |
| Stable voice or output structure | Prompt/template first; fine-tune only if measured gaps remain |
| Low interactive latency | Smaller suitable model, streaming/caching, short justified context, measured regional path |
| High-risk decision support | Explainability, source evidence, calibrated uncertainty, subgroup tests, human decision owner |
| Multi-step action | Tool contract, least privilege, state, approval, audit, idempotency, recovery |
| Predictable high throughput | Compare on-demand with provisioned capacity from utilization and service availability |

Inference parameters influence behavior. Higher temperature generally increases variety and nondeterminism; lower temperature does not guarantee truth. Input/output length affects cost and latency. Prompt caching can reduce repeated processing where supported, but cached content needs privacy and freshness controls.

### RAG is a retrieval contract

RAG normally ingests authorized sources, parses and chunks them, creates embeddings, stores vectors plus metadata, retrieves candidates for a query, may filter/rerank them, and supplies evidence to the model. [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) can support managed RAG. The blueprint names OpenSearch Service, Aurora, Neptune, and RDS for PostgreSQL as possible embedding/vector storage contexts.

Evaluate retrieval separately from generation:

- coverage/recall: did retrieval find the needed source?
- precision/relevance: how much retrieved content was useful?
- permission correctness: could the caller retrieve only authorized material?
- freshness and provenance: was the current governed source used?
- groundedness/faithfulness: does the response follow the evidence?
- citation correctness: does each citation support its claim?
- abstention: does the system decline when evidence is inadequate?

**Related item:** Adding more documents or a larger context window does not repair poor retrieval. It can raise cost and expose irrelevant or unauthorized text.

### Prompt engineering is a controlled artifact

A useful prompt separates role, task, context, constraints, allowed sources/tools, output schema, examples, uncertainty behavior, and refusal/escalation. Zero-shot uses instructions alone; single/few-shot adds examples; prompt templates parameterize repeatable use. “Chain-of-thought” is an objective term, but production systems should ask for concise evidence or structured justification rather than expose hidden reasoning as if it were guaranteed truth.

Version prompts, retrieval configuration, model, parameters, guardrails, tool schemas, evaluation set, and release decision together. [Amazon Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) is one current AWS feature in this space.

Prompt injection attempts to alter instructions through untrusted input. Jailbreaking attempts to bypass controls. Poisoning corrupts data or context. Defenses are layered: isolate instructions and data, restrict tools, validate schemas, filter inputs/outputs, apply guardrails, use permissions at retrieval/action time, require approvals, and monitor. A clever system prompt alone is not a security boundary.

### Evaluation must connect quality to consequence

Use representative, versioned datasets including normal, edge, adversarial, subgroup, refusal, and regression cases. Human evaluation captures usefulness and domain judgment. Automatic metrics can help but each measures a proxy: BLEU and ROUGE compare text overlap, BERTScore uses semantic representations, and LLM-as-a-judge uses another model with its own bias and calibration risks. [Amazon Bedrock model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) supports current evaluation workflows.

Application measures include task completion, retrieval quality, groundedness, tool success, policy violations, human correction/escalation, latency, tokens/cost per successful task, user satisfaction, and business outcome. “The answer looked good” is not a release gate.

---

## 4. Guidelines for Responsible AI — 14%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html) focuses on responsible development, transparency, and explainability.

### Responsible AI becomes concrete through tests and ownership

| Concern | Evidence and control examples |
|---|---|
| Fairness and inclusivity | Representative data, subgroup metrics, accessibility review, affected-user participation, appeal route |
| Safety and robustness | Misuse/edge/adversarial tests, guardrails, restricted actions, graceful failure, incident procedure |
| Veracity | Grounded sources, citations, output validation, uncertainty/abstention, human verification |
| Privacy | Purpose limitation, minimization, redaction, access control, retention/deletion, privacy-enhancing methods |
| Transparency | AI disclosure, data/model/system documentation, intended-use limits, traceable versions and decisions |
| Explainability | Explanations appropriate to user, operator, risk owner, and regulator; evidence linked to the decision |
| Sustainability | Right-sized model and infrastructure, utilization and energy/resource tradeoffs, avoided unnecessary retraining |

Bias can enter through problem framing, sampling, labels, proxies, model choice, evaluation, thresholds, deployment context, and feedback. Variance is sensitivity to data; high variance can overfit. High bias can underfit. “Bias” in statistical fit and “bias” as harmful disparate behavior are related but not interchangeable.

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) can apply configurable safeguards, but responsible operation also needs requirements, tests, identity, human controls, monitoring, incident response, and policy. Amazon A2I supports human review patterns. SageMaker Model Cards document intended use, risk, evaluation, and lifecycle evidence.

Transparent does not mean publishing sensitive prompts, weights, or personal data. Explainability must be useful to its audience. A customer may need the reason and appeal route; an operator needs trace/version/retrieval/tool evidence; a regulator may need documented controls and validation.

Legal risks include intellectual-property and licensing issues, personal/confidential data misuse, discrimination, misleading output, contractual limits, and loss of trust. Identify the applicable jurisdiction and organizational counsel; a certification guide is not legal advice.

**Related item:** The [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) organizes voluntary AI-risk work around Govern, Map, Measure, and Manage. It is useful cross-vendor context, not a substitute for applicable law or AWS-specific objectives.

---

## 5. Security, Compliance, and Governance for AI Solutions — 14%

The official [Domain 5 page](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html) connects AI-specific threats to established cloud controls and governance evidence.

### Secure the complete data and action path

Threat-model user input, system prompts, retrieved documents, embeddings/vector stores, model endpoints, plugins/tools, agent memory, output, logs, feedback, training/fine-tuning data, and the deployment pipeline.

- Use IAM roles, temporary credentials, least privilege, separation of duties, and explicit resource boundaries.
- Encrypt at rest and in transit using appropriate key control; avoid logging secrets or sensitive prompts by default.
- Use VPC/private connectivity where required; verify actual service and regional support.
- Classify/minimize data, control retrieval at query time, and preserve lineage and approved use.
- Treat retrieved content and tool output as untrusted data, not higher-priority instructions.
- Validate tool arguments and outputs; constrain destinations, amounts, methods, and side effects.
- Filter and validate model output before an application executes or publishes it.
- Record model/prompt/retrieval/tool/policy versions, approvals, action results, and relevant identities.
- Monitor prompt injection, leakage, toxicity, anomalous access/action, quality regression, and spend.

AWS remains responsible for security of the cloud; the customer remains responsible for identities, data, configuration, application behavior, and every controlled layer in the AI system. Managed services change the division of operational tasks, not accountability for the use case.

Macie helps discover sensitive data in S3; KMS protects keys; Secrets Manager manages supported secrets; Inspector assesses supported workload vulnerabilities; CloudTrail records supported API activity; Config evaluates resource configuration; Artifact provides compliance reports/agreements; Audit Manager helps collect assessment evidence; CloudWatch supplies telemetry; Trusted Advisor provides checks and guidance. Select each from the evidence/control need, not because “it is a security service.”

### Governance is a decision system

A defensible governance record connects:

1. approved outcome, owner, affected users, risk tier, and prohibited uses;
2. data/model/source licensing, lineage, residency, retention, deletion, and access;
3. evaluation thresholds across quality, subgroup, safety, security, cost, and business value;
4. release approvals, exceptions, training, and supplier/change management;
5. versioned inventory and monitoring evidence;
6. incident, appeal, correction, rollback, suspension, and retirement paths;
7. review cadence triggered by time and material change.

The AWS Generative AI Security Scoping Matrix is named in the objectives as a governance framework example. The [Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) provides current AWS architectural context. Framework adoption is not compliance by itself; map actual obligations and produce evidence.

**Related item:** Data lineage says where data came from and how it changed. A catalog makes assets discoverable with ownership and metadata. A model card documents intended use and evaluation. An audit trail records events. They support different questions and are strongest together.

---

## 6. Integrated decision scenarios

### Scenario A: Internal policy assistant

Employees need answers grounded in current approved policy documents with citations. Start with RAG rather than fine-tuning facts into model weights. Ingest only approved sources, preserve version/owner/effective dates, enforce employee permissions during retrieval, evaluate retrieval and citations separately from prose quality, require abstention when evidence is absent, and give policy owners a correction path. Monitor unsupported claims, stale-source use, latency, cost, adoption, and resolved-task rate.

### Scenario B: Marketing-content copilot

A marketing team wants draft copy across regions. Define supported tasks and prohibited claims; select a model for language/modality/latency/cost; use templates and examples before fine-tuning; provide approved brand/product context; block personal/confidential data; test regional language, subgroup representation, IP/licensing, hallucinated claims, and safety; require human approval before publishing. Measure accepted-with-minor-edit rate, correction reasons, policy violations, cycle time, and cost per approved asset.

### Scenario C: Customer-service action agent

An agent may retrieve an order, explain policy, and initiate a return. Give each tool a narrow schema and delegated identity, keep policy enforcement deterministic, treat retrieved/customer text as untrusted, require confirmation for side effects, use idempotency to prevent duplicate returns, cap steps/cost/time, and log model/tool/policy/approval versions. Escalate ambiguous, high-value, or policy-exception cases. Evaluate correct task completion and safe refusal—not conversational fluency alone.

---

## 7. Hands-on labs

Use a controlled sandbox, set a small budget, avoid personal/confidential data, check service/region pricing first, delete resources afterward, and prefer free documentation or no-deployment design work when possible.

### Lab 1: Technique decision matrix

Write six business problems. For each, choose deterministic rules, classification, regression, clustering, a foundation model, or an agent. Record data need, output, metric, human owner, and why two alternatives are weaker.

### Lab 2: Metric and threshold experiment

Use a small synthetic imbalanced dataset. Calculate accuracy, precision, recall, and F1 for two thresholds. Write which failure is more costly and select a threshold from the business consequence.

### Lab 3: Model and cost scorecard

From current Bedrock documentation, compare two models for modality, context, region, latency approach, price unit, customization, and safeguards. Estimate tokens and cost for a small scenario; label every volatile value with retrieval date.

### Lab 4: RAG evaluation design

Create ten public sample documents and ten questions with expected source passages. Design chunking/metadata and score retrieval coverage, relevance, permission filtering, groundedness, citation correctness, and abstention. Deployment is optional.

### Lab 5: Prompt and regression pack

Create a versioned prompt with task, sources, constraints, output schema, uncertainty behavior, and three examples. Build 15 cases spanning normal, edge, injection, refusal, and regression behavior. Change one element at a time and record results.

### Lab 6: Responsible-AI evidence card

For one scenario, document users, affected groups, intended/prohibited uses, data origin, subgroup/safety tests, human control, transparency, appeal, monitoring, incident owner, and retirement trigger. Identify what remains unknown.

### Lab 7: Agent threat and authority map

Draw user, agent, memory, retrieval, model, three tools, and downstream systems. Mark identity, trust boundary, data class, allowed action, validation, approval, log, timeout, retry/idempotency, and recovery for every edge.

### Lab 8: Governance review

Run a mock review of a model/prompt or source change. Require updated evaluation, cost, security/privacy, supplier, licensing, rollback, and owner approvals. Produce an approve/conditional/reject decision with evidence and an expiry date.

---

## 8. Knowledge checks and distinctions

Explain why each answer is true and why the nearest alternative is weaker.

1. Why is deterministic policy code often better than an FM for a mandatory eligibility rule?
2. How do classification, regression, and clustering differ?
3. Why can accuracy mislead on imbalanced data?
4. When would recall matter more than precision, and what cost follows?
5. What changes between batch, real-time, asynchronous, and serverless inference?
6. Why is “managed service” not the same as “customer has no responsibility”?
7. When does a task-specific AWS AI service fit better than Bedrock or SageMaker AI?
8. What makes an agent different from a chat response?
9. Why does MCP connectivity not grant trustworthy authorization?
10. When is a deterministic workflow safer than multi-agent orchestration?
11. How do tokens affect context, latency, and cost?
12. What is an embedding, and why does vector similarity not prove factual correctness?
13. Why does chunk size affect both retrieval precision and meaning?
14. What does context engineering include beyond a user prompt?
15. When does RAG fit better than fine-tuning?
16. Why must RAG permissions be enforced during retrieval?
17. How do prompting, fine-tuning, continued pretraining, distillation, and training from scratch differ?
18. What do temperature and output length influence, and what do they not guarantee?
19. Why should prompt, model, retrieval, guardrail, and evaluation versions be released together?
20. How are prompt injection, jailbreaking, and poisoning different?
21. Why can a system with strong model scores still fail the business objective?
22. What do BLEU, ROUGE, BERTScore, human review, and LLM-as-a-judge each approximate?
23. Which measures evaluate retrieval separately from generation?
24. What is a safe abstention, and when is it preferable to a fluent answer?
25. Where can harmful bias enter the lifecycle?
26. How do statistical underfit/overfit relate to, but differ from, fairness harms?
27. Why is a guardrail one layer rather than a responsible-AI program?
28. How should transparency differ for a customer, operator, and regulator?
29. Why can publishing more system detail reduce security or privacy?
30. What legal and licensing questions exist for input data, model terms, and generated output?
31. Which controls protect prompts, retrieved data, embeddings, tools, memory, output, and logs?
32. How do IAM, KMS, Macie, CloudTrail, Config, Artifact, Audit Manager, Inspector, and CloudWatch differ?
33. Why should an action tool use least privilege, schema validation, confirmation, and idempotency?
34. How do lineage, catalog, model card, and audit trail answer different evidence questions?
35. What evidence should trigger rollback, suspension, retraining, replacement, or retirement?

### Readiness checklist

- [ ] I can map each current domain and task statement to a business and technical decision.
- [ ] I can distinguish rules, traditional ML, GenAI, RAG, workflow, and agent use cases.
- [ ] I can explain the March 2026 agentic/MCP/Kiro/Strands/AgentCore/Quick additions without relying on an older course.
- [ ] I can select metrics from failure consequence and identify misleading aggregates.
- [ ] I can compare prompting, RAG, fine-tuning, continued pretraining, distillation, and training from scratch.
- [ ] I can evaluate retrieval, generation, agent actions, safety, cost, and business value separately.
- [ ] I can map AI risks to identity, data, application, model, tool, monitoring, and governance controls.
- [ ] I completed several labs and can explain evidence, failure, recovery, and human ownership.
- [ ] I checked the official page for changes before booking.

### Primary references

- [Official AIF-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html)
- [Domain 1: Fundamentals of AI and ML](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html)
- [Domain 2: Fundamentals of GenAI](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html)
- [Domain 3: Applications of Foundation Models](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html)
- [Domain 4: Guidelines for Responsible AI](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html)
- [Domain 5: Security, Compliance, and Governance](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html)
- [AIF-C01 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-in-scope-services.html)
- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [AWS Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you and use the official March 26, 2026 blueprint to close only your gaps. Times are approximate consumption time at normal speed; labs, notes, assessment review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [AWS AIF-C01 exam page and four-step prep plan](https://aws.amazon.com/certification/certified-ai-practitioner/) | Public page; Skill Builder account for learning | About 15–25 hours selected official preparation plus labs | Start with the current guide, pretest/question set, gap learning, labs, and official practice exam; some components require a subscription |
| [AWS Standard Exam Prep Plan for AIF-C01](https://explore.skillbuilder.aws/learn/learning-plans/2193/standard-exam-prep-plan-aws-certified-ai-practitioner-aif-c01) | Skill Builder account; free and subscription elements vary | About 12–20 hours estimated plus practice | Official structured route; confirm it visibly reflects the March 2026 agentic additions |
| [Pluralsight — AIF-C01 Fundamentals of AI and ML](https://www.pluralsight.com/courses/aws-certified-ai-practitioner-ai-ml-fundamentals) | Subscription/trial | 2 hours 4 minutes | Strong Domain 1 supplement last updated November 2024; not complete current coverage and predates the March 2026 agentic revision |
| [O'Reilly — AIF-C01 Certification Course](https://www.oreilly.com/videos/aws-certified-ai/0642572022568/) | Subscription/trial | 2 hours 36 minutes plus gap work | Tom Taulli course dated March 2026; compare its outline carefully with revision 1.0 because visible introductory lessons contain reused Cloud Practitioner labels |
| [Udemy — Ultimate AWS Certified AI Practitioner AIF-C01](https://www.udemy.com/course/aws-ai-practitioner-certified/) | Purchase or subscription | 10 hours 17 minutes plus labs and practice review | Stéphane Maarek course shown updated August 2026 with a practice exam; verify explicit coverage of every March 2026 addition |
| [Whizlabs — AWS Certified AI Practitioner AIF-C01](https://www.whizlabs.com/aws-certified-ai-practitioner/) | Paid modules/subscription; trial items vary | About 10–18 hours estimated plus 59 listed labs and practice review | Page shown updated April 2026 with 92 videos, quizzes, labs and practice; public counts are inconsistent in places, so inspect the live outline |
| [Tutorials Dojo — AIF-C01 practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-ai-practitioner-aif-c01-practice-exams/) | Paid; free sampler may be available | About 8–14 hours for diagnostic, timed, review, section, and randomized modes | Current page lists 16 quizzes and multiple modes; use each rationale with the March 2026 AWS guide, never recalled-question claims |
| [MeasureUp — AIF-C01 practice test](https://www.measureup.com/aif-c01-aws-certified-ai-practitioner-practice-test.html) | Paid; separate lower-cost 30-question assessment | About 6–12 hours across certification/practice modes and review | Current exact product with explanations/references; inspect blueprint revision and translation caveats before purchase |
| [freeCodeCamp/ExamPro — AWS AI Practitioner full course](https://www.youtube.com/watch?v=WZeZZ8_W-M4) | Free | About 15 hours plus labs | Andrew Brown long-form course is a useful foundation; it predates revision 1.0, so add the March 2026 agentic, MCP, Quick, Kiro, Strands, and AgentCore objectives |

See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md) for provider-selection criteria. Avoid any source claiming real or recalled exam questions; use original practice to test reasoning, then verify explanations against current first-party documentation.
