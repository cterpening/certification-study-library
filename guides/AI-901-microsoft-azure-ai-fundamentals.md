---
exam_code: AI-901
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AI-901 Microsoft Azure AI Fundamentals Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official AI-901 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) is authoritative.

**Current baseline:** Skills measured as of April 15, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)

> **Replacement note:** AI-900 retired on June 30, 2026. AI-901 is the active Azure AI Fundamentals exam and has a substantially more implementation-oriented Foundry scope. Older AI-900 resources can refresh concepts but are not an AI-901 study plan.

## How to use this guide

AI-901 asks you to recognize AI workload patterns and perform foundational implementation with Microsoft Foundry and Foundry Tools. Study each capability as an input → processing → output → evaluation pipeline. Build small examples rather than memorizing service names, and verify all model, SDK, region, quota, pricing, and preview details before the exam.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe AI concepts and use cases | 40–45% | Which workload, technique, model, and responsible-AI concern apply? |
| Implement AI workloads with Microsoft Foundry | 55–60% | How do prompts, models, agents, language, speech, vision, and extraction become a small working solution? |

---

# 1. AI workloads and techniques

## What AI systems do

| Workload | Input | Typical output |
|---|---|---|
| Generative AI | Prompt plus optional context/media | New text, code, image, audio, or other content |
| Agentic AI | Goal, state, knowledge, and tools | Multi-step decision/action with observations |
| Natural language processing | Text | Entities, sentiment, summary, translation, classification |
| Speech AI | Audio/text | Transcript, synthesized voice, translation |
| Computer vision | Image/video | Classification, objects, description, generated/edited media |
| Information extraction | Documents, forms, images, audio, or video | Structured fields, layout, Markdown, segments |

AI is suitable when the task needs pattern recognition, flexible language/media understanding, prediction, or generation and can tolerate/mitigate uncertainty. Deterministic rules remain better for exact policy, arithmetic, validation, and invariant business constraints. Hybrid systems often use a model for interpretation and code/rules for enforcement.

Machine learning learns a mapping from examples rather than expressing every rule manually. Supervised learning uses labeled examples; unsupervised learning finds structure without target labels; reinforcement learning optimizes behavior from feedback/reward. AI-901 emphasizes contemporary generative and Foundry use cases, but these foundations help explain evaluation.

> **Related item:** A probabilistic system can be reliable only when the surrounding product constrains, evaluates, observes, and safely handles uncertainty. Reliability is a system property, not a promise that a model always returns identical text.

## Generative models

Large language models tokenize input, represent patterns learned during training, and predict output tokens. They do not query an authoritative truth database merely because their response is fluent. Context supplied at inference—system instructions, user prompt, retrieved evidence, history, and tool results—changes the response without retraining the base model.

| Adaptation method | Changes model weights? | Good for |
|---|---:|---|
| Prompting | No | Task instruction, examples, output format, current context |
| Retrieval-augmented generation | No | Supplying current/private evidence with citations |
| Fine-tuning | Yes | Teaching stable task behavior/style from curated examples |
| Tool use | No | Querying systems or performing authorized actions |

Choose a model using task quality, modalities, context window, latency, throughput, cost, safety, region, deployment availability, and contractual/data requirements. A larger model is not automatically the best production choice.

## Agents

An agent combines a model with instructions, state, knowledge, tools, and an orchestration loop. It observes the request/state, selects a step, invokes a capability, interprets the result, and continues or stops. Agents are useful when the path cannot be completely predetermined; a workflow is safer when steps and rules are known.

Agent controls include narrow goals, precise tool schemas, least privilege, argument validation, human approval, time/turn/tool budgets, idempotency, timeouts, audit, and a clear stop/escalation path.

> **Related item:** A tool schema describes how to call a function. Authorization must still be enforced by the application or target API; a model must never be the security boundary.

---

# 2. Responsible AI

Microsoft identifies six responsible-AI principles:

| Principle | Implementation question |
|---|---|
| Fairness | Do outcomes differ unjustifiably across relevant groups or contexts? |
| Reliability and safety | Does the system behave within tested limits and fail safely? |
| Privacy and security | Is data collected, used, retained, and accessed appropriately? |
| Inclusiveness | Does the design work for diverse users and accessibility needs? |
| Transparency | Do people understand that AI is involved, its evidence, and its limits? |
| Accountability | Which human/organization owns decisions, monitoring, and remediation? |

Apply the principles through the lifecycle:

1. define intended use, affected people, and prohibited use;
2. identify data, model, security, safety, accessibility, and business risks;
3. choose model/service and design mitigations;
4. build representative evaluation cases;
5. deploy with access, filters, approvals, monitoring, and incident controls;
6. review feedback, drift, changes, and retirement.

Content filters classify categories of harmful content and can block input/output under configured thresholds. Prompt Shields detect some direct and indirect prompt attacks. Groundedness evaluation asks whether output is supported by evidence. These controls address different failures and none is perfect.

Human oversight may be human-in-the-loop before an action, human-on-the-loop supervising automation, or human-in-command controlling the system and policy. Use stronger intervention for consequential, ambiguous, irreversible, or novel decisions.

> **Related item:** A model card or system card communicates capabilities, limitations, evaluation, and intended use. It is evidence for a decision—not permission to ignore the application's own context and risks.

---

# 3. Microsoft Foundry foundations

Microsoft Foundry supplies a platform for discovering models, creating projects, deploying models, building applications and agents, connecting tools/data, evaluating behavior, and operating AI workloads. Product naming and SDKs are evolving; use the current [Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/) immediately before the exam.

## Model catalog, deployment, and endpoints

A model is a capability/version. A deployment is a configured serving instance with a name, region/project relationship, capacity/deployment type, and endpoint behavior. Application code targets a deployment, not an abstract marketing name.

Selection workflow:

1. define representative requests, constraints, and unacceptable outcomes;
2. shortlist eligible models by modality, region, data terms, and deployment availability;
3. deploy/configure candidates;
4. test quality, safety, latency, and cost on the same cases;
5. choose the smallest/least expensive option that meets the requirement;
6. version the model/deployment/prompt configuration and monitor it.

Use keyless Microsoft Entra authentication where supported for production and grant the workload only the needed role. API keys are secrets and require secure storage and rotation. Never embed them in code or a public repository.

## Prompting and model interaction

A prompt can include system/developer instructions, user content, examples, retrieved evidence, and an output schema. High-quality prompts state task, context, constraints, format, and how to handle missing evidence. Few-shot examples demonstrate intended behavior.

| Setting | Effect |
|---|---|
| Temperature/sampling | Changes variability, subject to model/API support |
| Maximum output tokens | Bounds response length/cost but may truncate |
| Stop/response format | Constrains termination or structure when supported |
| Tool choice | Allows, requires, or restricts callable tools |

Structured output must still be parsed and validated. Retry transient failures with bounded exponential backoff and jitter; do not blindly retry unsafe or invalid work.

### Minimal interaction pattern

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
# Create the current documented Foundry/project or model client here.
# Supply a deployment name, bounded request, timeout, and correlation ID.
# Validate the response before using it.
```

The exact client package and method names are **VERIFY CURRENT** because Foundry SDKs are changing. The durable pattern is credential → client → deployment → structured request → validated response → telemetry.

---

# 4. Generative and agentic implementation

## Build a chat application

A basic application needs configuration, authentication, request validation, message history, model invocation, output validation, error handling, logging, and a user experience. Limit context growth and avoid logging secrets or sensitive prompt bodies by default.

Separate the instruction trusted by the application from untrusted user or retrieved content. Treat text inside documents and web pages as data, not as higher-priority instructions.

## Build a single agent

Define role, goal, knowledge, tools, state, allowed actions, budgets, termination, and evaluation. Start with a read-only tool. A tool implementation should authenticate, authorize, validate arguments, execute with timeout, return structured results, and record safe telemetry.

For side effects:

1. show a preview or request approval when needed;
2. use an idempotency key;
3. constrain resource and amount;
4. distinguish retryable from permanent errors;
5. retain an accountable audit record;
6. supply compensation or escalation for partial failure.

The Foundry Agent Service manages supported agent resources, threads/conversations, tools, and execution. **VERIFY CURRENT:** agent types, tool support, SDK surface, connected-agent features, and pricing.

## Evaluation

Create normal, edge, unsafe, adversarial, and unauthorized cases. Evaluate task completion, relevance, groundedness, safety, tool selection, argument accuracy, latency, and cost. An average can hide a critical failure slice; define release thresholds for high-risk cases separately.

> **Related item:** Tracing shows the execution path—model calls, retrieval, tool calls, latency, and errors. Evaluation judges quality. Monitoring detects production behavior. You need all three to diagnose and improve an AI application.

---

# 5. Text, speech, and translation

## Text workloads

Generative models can summarize, classify, extract, rewrite, answer questions, and produce structured data. Specialized Azure language capabilities may be preferable for defined tasks such as named-entity recognition, key phrases, sentiment, conversational language understanding, or custom classification when predictability and supported semantics fit.

Define allowed labels or a JSON schema. Test negation, ambiguity, long input, multiple languages, names/numbers, and unsupported content. Preserve evidence spans when a reviewer needs to verify extraction.

## Speech workloads

Speech to text transcribes audio. Text to speech synthesizes audio. Speech translation combines recognition and translation. Voice applications also need microphone/audio format, language, latency, partial results, turn detection, interruption, error recovery, consent, and transcript protection.

Custom speech or voices add data, consent, approval, evaluation, and lifecycle responsibilities. **VERIFY CURRENT:** supported languages, regions, features, and access requirements in [Azure Speech documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/).

## Translation

Translation evaluation must cover terminology, names, numbers, tone, negation, layout, and target-language fluency. Document translation and conversational text translation have different preservation and latency needs. A natural-sounding result can still invert meaning.

---

# 6. Vision and multimodal workloads

Computer vision can classify an image, detect objects, extract text, describe content, answer questions about visual evidence, or generate/edit media. Match the output contract to the capability.

| Need | Approach |
|---|---|
| Read text from an image | OCR/document or image text extraction |
| Locate known object categories | Object detection |
| Assign one/more image categories | Classification |
| Flexible description or visual Q&A | Multimodal generative model |
| Produce/edit an image | Image generation/editing model |

Generation workflows require prompt/reference rights, safety filtering, output provenance, review, and storage. Vision input can contain private content, harmful material, or indirect prompt injection embedded as text.

Accessible alt text describes the information needed for the page's purpose. Decorative images may require empty alt text; complex diagrams may need a concise label and a long description. Generated descriptions require contextual human review.

> **Related item:** Multimodal does not mean universally capable. A model can accept an image while performing poorly on tiny text, precise counting, spatial measurement, or domain-specific diagnosis. Evaluate the exact task and input quality.

---

# 7. Content Understanding and information extraction

Azure Content Understanding processes documents, images, audio, and video into structured fields or Markdown using supported analyzers. It can combine recognition, layout/segmentation, and model-based interpretation. Prebuilt analyzers offer common starting schemas; custom analyzers define task-specific outputs under current product capabilities.

```text
source → validate → analyze/OCR/transcribe → fields/Markdown
                                             ↓
                                 confidence + source regions
                                             ↓
                           review, index, automate, or agent
```

Implementation decisions include source format/size, analyzer/schema, field descriptions and types, page/time regions, confidence, asynchronous status, error/retry, throughput, privacy, retention, and human review. Preserve source references so a reviewer can trace an extracted value back to the page, region, or timestamp.

OCR recognizes text; layout captures structural relationships; field extraction maps evidence into a schema; multimodal reasoning interprets content. A correct OCR transcript can still feed an incorrect field mapping.

## Light application pattern

1. upload or reference a permitted public sample;
2. invoke a prebuilt or custom analyzer;
3. poll the asynchronous operation using bounded intervals/timeouts;
4. validate returned fields and confidence/evidence;
5. show the source region to a reviewer;
6. handle unsupported/corrupt input and partial results;
7. record safe telemetry without copying sensitive content unnecessarily.

> **Related item:** Human review should be risk-based. Low confidence is one trigger, but high-confidence extraction of a high-impact value may still require verification.

---

# 8. Hands-on labs

## Lab 1: Model comparison

Using public, non-sensitive prompts, compare two eligible Foundry models on classification, structured extraction, and explanation. Record model/deployment, prompt, quality, safety, latency, and approximate consumption. Choose based on evidence.

## Lab 2: Small chat app

Build a local Python app using current Foundry documentation and keyless authentication where supported. Add bounded history, structured output, timeout, retry, and a correlation ID. Prove invalid output is rejected.

## Lab 3: Tool-using agent

Create an agent with a read-only public-data tool and a simulated side-effecting tool behind confirmation. Validate arguments, enforce authorization outside the model, cap turns, and test prompt injection, timeout, denial, and repetition.

## Lab 4: Speech and text pipeline

Transcribe a short public-domain audio sample, summarize it, translate a passage, and synthesize a response. Compare names, numbers, negation, latency, and transcript privacy needs.

## Lab 5: Visual accessibility

Use public images to create short alt text and detailed descriptions. Include an infographic, decorative image, and image containing misleading embedded instructions. Review against page purpose.

## Lab 6: Content extraction

Analyze public forms/documents/media with Content Understanding. Validate structured fields, inspect page/region evidence, introduce a low-quality scan, and route uncertain/high-impact values to review.

---

# 9. Knowledge checks and distinctions

1. A generated answer is fluent but unsupported. Which evaluation property failed?
2. A model selects a refund tool correctly but exceeds the user's limit. Which control cannot be delegated to the model?
3. A smaller model meets the task threshold with lower cost and latency. What reason remains to choose the larger model?
4. OCR text is accurate but an invoice total field is wrong. Which later stage should be inspected?
5. An image contains instructions telling the agent to reveal data. Why should those words remain untrusted?
6. A voice agent produces good text but feels unusable. Which real-time interaction requirements might be missing?

| Contrast | Remember |
|---|---|
| Model vs deployment | Capability/version versus configured serving endpoint |
| Prompting vs fine-tuning | Inference context versus weight adaptation |
| RAG vs fine-tuning | Supply current evidence versus teach stable learned behavior |
| Workflow vs agent | Predetermined path versus model-mediated next-step selection |
| Tool schema vs authorization | Describes invocation versus permits operation |
| Content filter vs groundedness | Harm classification versus evidentiary support |
| Tracing vs evaluation vs monitoring | Execution path versus quality judgment versus production observation |
| Speech recognition vs synthesis | Audio to text versus text to audio |
| Classification vs object detection | Label image versus locate labeled objects |
| OCR vs layout vs extraction | Recognize text versus structure versus schema mapping |
| Confidence vs correctness | Model signal versus verified outcome |

## Readiness checklist

- [ ] I can describe generative, agentic, language, speech, vision, and extraction workloads.
- [ ] I can explain responsible-AI principles and lifecycle controls.
- [ ] I can distinguish prompting, RAG, fine-tuning, and tool use.
- [ ] I can choose and deploy a model based on task, quality, modality, safety, latency, cost, and region.
- [ ] I can describe keyless authentication, model interaction, structured output, retry, and telemetry.
- [ ] I can build a basic chat app and a bounded single agent using current Foundry guidance.
- [ ] I can distinguish text analysis, speech recognition/synthesis, and translation patterns.
- [ ] I can distinguish vision classification, detection, OCR, multimodal understanding, and generation.
- [ ] I can use Content Understanding conceptually for documents, images, audio, and video.
- [ ] I can explain tracing, evaluation, monitoring, approval, and human review.
- [ ] I checked every **VERIFY CURRENT** item and the current blueprint.

## Primary references

- [Official AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
- [AI-900 retirement notice](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900)
- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Foundry models](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/foundry-models-overview)
- [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)
- [Responsible AI principles](https://www.microsoft.com/en-us/ai/principles-and-approach)
- [Azure AI Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
- [Azure Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)
- [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview)
- [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AI-901 course](https://learn.microsoft.com/en-us/training/courses/ai-901t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation and implementation sequence |
| [Microsoft — AI-901 Practice Assessment on AI Skills Navigator](https://aiskillsnavigator.microsoft.com/credentials/cert-83587e0a0754cfee561ade3e27d9fa1cdaf15ae03be52d2413b2b858d1b4eda4) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check; AI Skills Navigator sign-in is required, and the blueprint and product documentation remain authoritative |
| [Microsoft Learn AI-901 certification material](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/) | Free | About 10–14 hours | Official scope anchor; complete current Foundry exercises rather than relying on AI-900 modules |
| [O'Reilly — Azure AI Fundamentals AI-901](https://www.oreilly.com/videos/azure-ai-fundamentals/9781807782979/) | Subscription | 4 hours 4 minutes | Anand Rao Nednur course published April 2026 and aligned to the replacement exam |
| [Udemy — AI-901 by Christopher Nett](https://www.udemy.com/course/ai-901-azure-ai-fundamentals/) | Purchase or subscription | About 6 hours 20 minutes | Course shown as updated June 2026; inspect demos and current SDK usage |
| [Udemy — AI-901 exam prep by Kuljot Singh Bakshi](https://www.udemy.com/course/azure-ai-fundamentals-exam-prep/) | Purchase or subscription | About 6 hours 54 minutes | Alternative shown as updated July 2026; inspect previews and hands-on depth |
| [Whizlabs — AI-901 instruction and practice](https://www.whizlabs.com/ai-901-microsoft-azure-ai-fundamentals/) | Paid course or subscription | About 3–6 hours for 3 quizzes and review; video total not published | Public listing shows 63 videos and three quizzes; use the assessment after learning and verify explanations against the current blueprint |
| [Microsoft AI Show](https://learn.microsoft.com/en-us/shows/ai-show/) | Free | Select 2–5 hours by gap | Official product demonstrations; choose current Foundry, agents, speech, vision, and extraction episodes |
| [John Savill — AI-900 Study Cram v2](https://www.youtube.com/watch?v=bTkUTkXrqOQ) | Free | About 3 hours | Optional legacy concept refresher only; AI-900 retired and this does not cover AI-901 implementation scope |

No exact Pluralsight path or standalone MeasureUp AI-901 practice test was verified on August 31, 2026. The free Microsoft assessment above and the Whizlabs mixed bundle provide two different readiness checks. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
