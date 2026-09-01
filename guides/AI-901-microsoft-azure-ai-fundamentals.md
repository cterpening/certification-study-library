---
exam_code: AI-901
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AI-901 Microsoft Azure AI Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ai-901-coverage-record). The [official AI-901 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) is authoritative.

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
| Identify AI concepts and capabilities | 40–45% | Which workload, technique, model, and responsible-AI concern apply? |
| Implement AI solutions by using Microsoft Foundry | 55–60% | How do prompts, models, agents, language, speech, vision, and extraction become a small working solution? |

---

## 1. AI workloads and techniques

### What AI systems do

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

### Choose the workload from the required output

Start with what the user or downstream system needs, not with the input file type. One image can be classified, searched for text, described, edited, or analyzed for fields; those are different workloads.

| Requirement | Workload to consider first | Evidence that distinguishes it |
|---|---|---|
| Mark a review as positive, neutral, or negative | Text analysis/classification | Fixed labels and evaluated classification behavior |
| Turn a meeting recording into searchable text | Speech recognition | Audio input and transcript output |
| Read invoice number, total, and table rows | Information extraction | Defined schema plus page/region evidence |
| Answer an open question about a photograph | Multimodal generative model | Flexible visual-language reasoning |
| Create a new marketing illustration | Image generation | New visual output, rights, safety, and provenance controls |
| Decide which approved function to call next | Agentic AI | Model-mediated action selection within a bounded loop |
| Enforce that a refund never exceeds policy | Deterministic application rule | Exact invariant; do not delegate it to a probabilistic model |

The official [AI concepts learning path](https://learn.microsoft.com/en-us/training/paths/ai-concepts/) treats generative AI and agents, computer vision, speech, text analysis, information extraction, and retrieval-augmented generation as related but distinct workloads.

Use a four-question test:

1. What input modalities arrive?
2. Is the desired output a label, transcript, generated content, structured field, or action?
3. Must the result be exact/repeatable, or can uncertainty be reviewed and mitigated?
4. What evidence and evaluation will show success?

> **Related item:** “Multimodal” describes supported input/output modalities. It does not mean that one model is the best choice for every specialized speech, vision, or extraction task.

### Generative models

Large language models tokenize input, turn tokens into numerical representations, use learned attention and network weights to model relationships, and predict likely output tokens. During **training**, the model’s weights are adjusted from examples. During **inference**, the deployed weights process the current context and generate an output. A fluent response is a probability-driven continuation, not a lookup from an authoritative truth database.

The context can contain system instructions, user prompts, examples, retrieved evidence, conversation history, images/audio for an eligible multimodal model, and tool results. Supplying context changes this request without retraining the base model. The context window is finite; exceeding it requires selection, truncation, summarization, or another design rather than assuming the model remembers everything.

| Adaptation method | Changes model weights? | Good for |
|---|---:|---|
| Prompting | No | Task instruction, examples, output format, current context |
| Retrieval-augmented generation | No | Supplying current/private evidence with citations |
| Fine-tuning | Yes | Teaching stable task behavior/style from curated examples |
| Tool use | No | Querying systems or performing authorized actions |

Choose a model using task quality, modalities, context window, latency, throughput, cost, safety, region, deployment availability, and contractual/data requirements. A larger model is not automatically the best production choice.

Sampling parameters such as temperature can alter output variability but cannot make unsupported claims true. Maximum-output settings bound generation and cost but can truncate an answer. Embedding models produce vectors for similarity and retrieval; they are not chat models. Image, video, speech, and multimodal models have distinct inputs, outputs, limits, and safety constraints.

> **Related item:** A model version and its deployment configuration form part of the evaluated system. Changing either can change quality, latency, safety behavior, or cost even when the application code stays the same.

### Agents

An agent combines a model with instructions, state, knowledge, tools, and an orchestration loop. It observes the request/state, selects a step, invokes a capability, interprets the result, and continues or stops. Agents are useful when the path cannot be completely predetermined; a workflow is safer when steps and rules are known.

Agent controls include narrow goals, precise tool schemas, least privilege, argument validation, human approval, time/turn/tool budgets, idempotency, timeouts, audit, and a clear stop/escalation path.

| Use a workflow when… | Use an agent when… |
|---|---|
| the steps and branches are known in advance; | selecting the next step requires interpretation; |
| deterministic execution and audit are primary; | tools or knowledge must be selected from changing context; |
| a rules engine can express the decision safely. | uncertainty is acceptable inside strict action boundaries. |

An agent is not permission to make every step autonomous. It can suggest an action, prepare it for confirmation, act only within a low-risk bound, or escalate. Choose oversight by consequence and reversibility.

> **Related item:** A tool schema describes how to call a function. Authorization must still be enforced by the application or target API; a model must never be the security boundary.

---

## 2. Responsible AI

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

### Apply the principles to one system

Consider an AI assistant that summarizes employee accommodation requests:

| Principle | Concrete design and validation work |
|---|---|
| Fairness | Test summary omissions and tone across relevant language, disability, and request categories; investigate outcome differences |
| Reliability and safety | Restrict intended use, preserve source evidence, abstain on missing content, and route consequential decisions to a person |
| Privacy and security | Minimize collected data, authorize source access, redact telemetry, define retention/deletion, and prevent cross-user retrieval |
| Inclusiveness | Test keyboard/screen-reader interaction, plain-language output, alternative formats, and supported languages with affected users |
| Transparency | Disclose AI involvement, show source passages and limitations, and distinguish a draft summary from an approved decision |
| Accountability | Name the product owner, reviewer, risk approver, incident path, monitoring cadence, and retirement authority |

The principles overlap but are not interchangeable. Encryption supports privacy/security but does not establish fairness. A disclosure supports transparency but does not transfer accountability to the user. Microsoft’s [responsible AI approach](https://www.microsoft.com/en-us/ai/principles-and-approach) is the primary source for the six principles; the controls above are application-level ways to operationalize them.

#### Control by failure type

| Failure | Better first control | Why a neighboring control is insufficient |
|---|---|---|
| Harmful text/image | Content classification/filtering and policy | Grounding does not decide whether supported content is allowed |
| Unsupported factual claim | Grounding, citations, abstention, evaluation | A harm filter does not verify evidence |
| Unauthorized document disclosure | Identity and retrieval-time authorization | Removing the citation after generation is too late |
| Agent attempts prohibited action | Tool authorization, allow-list, validation, approval | Prompt instructions alone are not enforcement |
| Poor results for a user group | Representative evaluation and slice analysis | One average quality score can hide disparity |
| Sensitive data in traces | Redaction, minimization, access, retention | Private networking does not sanitize telemetry |

> **Related item:** A model card or system card communicates capabilities, limitations, evaluation, and intended use. It is evidence for a decision—not permission to ignore the application's own context and risks.

---

## 3. Microsoft Foundry foundations

Microsoft Foundry supplies a platform for discovering models, creating projects, deploying models, building applications and agents, connecting tools/data, evaluating behavior, and operating AI workloads. Product naming and SDKs are evolving; use the current [Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/) immediately before the exam.

| Component | Mental model | Common confusion |
|---|---|---|
| Foundry resource/account boundary | Azure governance, identity, networking, and shared management scope | It is not the same as one model deployment |
| Project | Workspace/scope for an application team and its assets | A project does not erase underlying Azure permissions |
| Model catalog | Discover models by task, modality, provider, and availability | A catalog benchmark is not proof for your application |
| Model deployment | Named, configured serving target for a model/version | Code normally calls the deployment, not a catalog card |
| Project/model endpoint | Network address used by a client under current API patterns | Endpoint reachability does not grant authorization |
| Agent | Versioned instructions/model/tools/behavior under the supported service model | A chat model without tools/state is not automatically an agent |
| Foundry Tool | Specialized capability such as Speech, Language, or Content Understanding | Specialized tools and general models can coexist |

The current [Foundry capability map](https://learn.microsoft.com/en-us/azure/foundry/concepts/capabilities) is useful when choosing the shortest supported build path. **VERIFY CURRENT:** new versus classic project terminology, endpoints, SDKs, roles, agent types, tool names, and preview status.

### Model catalog, deployment, and endpoints

A model is a capability/version. A deployment is a configured serving instance with a name, region/project relationship, capacity/deployment type, and endpoint behavior. Application code targets a deployment, not an abstract marketing name.

Selection workflow:

1. define representative requests, constraints, and unacceptable outcomes;
2. shortlist eligible models by modality, region, data terms, and deployment availability;
3. deploy/configure candidates;
4. test quality, safety, latency, and cost on the same cases;
5. choose the smallest/least expensive option that meets the requirement;
6. version the model/deployment/prompt configuration and monitor it.

Use keyless Microsoft Entra authentication where supported for production and grant the workload only the needed role. API keys are secrets and require secure storage and rotation. Never embed them in code or a public repository.

#### From portal exploration to a small client

The exam explicitly expects both portal and lightweight application work. Use this progression:

1. Create or select the required Foundry resource/project under an Azure subscription.
2. Browse a model card and confirm task, modality, region, provider/terms, and deployment options.
3. Deploy an eligible model and record the deployment name and endpoint.
4. Test a representative system/user prompt in the portal and inspect output plus safety behavior.
5. Configure a local client with the current SDK and an identity credential.
6. Send the same prompt through code, validate the response, and handle authorization, invalid-request, throttling, and transient failures differently.
7. Compare portal and application configuration so an implicit default does not explain a behavioral difference.
8. Delete or scale down paid lab resources when finished.

The [Foundry Models overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) and [deployment guide](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models) support this model-to-deployment distinction. **VERIFY CURRENT:** model names, versions, regions, quotas, deployment types, prices, and retirement dates.

### Prompting and model interaction

A prompt can include system/developer instructions, user content, examples, retrieved evidence, and an output schema. High-quality prompts state task, context, constraints, format, and how to handle missing evidence. Few-shot examples demonstrate intended behavior.

| Setting | Effect |
|---|---|
| Temperature/sampling | Changes variability, subject to model/API support |
| Maximum output tokens | Bounds response length/cost but may truncate |
| Stop/response format | Constrains termination or structure when supported |
| Tool choice | Allows, requires, or restricts callable tools |

Structured output must still be parsed and validated. Retry transient failures with bounded exponential backoff and jitter; do not blindly retry unsafe or invalid work.

Separate prompt roles conceptually:

- **system/developer instruction:** trusted application behavior and constraints;
- **user content:** the request, which is untrusted input;
- **retrieved/tool content:** supporting data, also untrusted unless the application establishes otherwise;
- **output contract:** the schema or format the application validates.

A prompt should say what to do when evidence is missing. “Always answer” encourages fabrication; an abstention or clarification path is often the correct behavior. Few-shot examples can demonstrate the output, but poor or contradictory examples become part of the problem.

#### Minimal interaction pattern

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
# Create the current documented Foundry/project or model client here.
# Supply a deployment name, bounded request, timeout, and correlation ID.
# Validate the response before using it.
```

The exact client package and method names are **VERIFY CURRENT** because Foundry SDKs are changing. The durable pattern is credential → client → deployment → structured request → validated response → telemetry.

---

## 4. Generative and agentic implementation

### Build a chat application

A basic application needs configuration, authentication, request validation, message history, model invocation, output validation, error handling, logging, and a user experience. Limit context growth and avoid logging secrets or sensitive prompt bodies by default.

Separate the instruction trusted by the application from untrusted user or retrieved content. Treat text inside documents and web pages as data, not as higher-priority instructions.

Use a simple request lifecycle:

```text
validate input → acquire identity → build bounded context → call deployment
               → validate output → present result → record safe telemetry
```

Do not let message history grow without policy. Retain only what the interaction needs, protect sensitive content, and distinguish current conversation context from durable user memory.

### Build a single agent

Define role, goal, knowledge, tools, state, allowed actions, budgets, termination, and evaluation. Start with a read-only tool. A tool implementation should authenticate, authorize, validate arguments, execute with timeout, return structured results, and record safe telemetry.

For side effects:

1. show a preview or request approval when needed;
2. use an idempotency key;
3. constrain resource and amount;
4. distinguish retryable from permanent errors;
5. retain an accountable audit record;
6. supply compensation or escalation for partial failure.

The [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) manages supported agent resources, conversations/state, tools, versions, and execution. **VERIFY CURRENT:** agent types, state terminology, tool support, SDK surface, connected/multi-agent features, hosting model, and pricing.

#### Trace a single agent turn

```text
user request
  → instructions + authorized context
  → model selects response or tool
  → application validates and authorizes tool arguments
  → tool returns structured result
  → model uses result
  → application validates response and stops/escalates
```

If a turn fails, identify whether the wrong context arrived, the model selected the wrong tool, arguments were invalid, authorization failed, the tool timed out, the result was misinterpreted, or the loop did not terminate. “The agent failed” is not yet a diagnosis.

### Evaluation

Create normal, edge, unsafe, adversarial, and unauthorized cases. Evaluate task completion, relevance, groundedness, safety, tool selection, argument accuracy, latency, and cost. An average can hide a critical failure slice; define release thresholds for high-risk cases separately.

| Signal | What it tells you |
|---|---|
| Trace | Which model, tool, retrieval, or application step ran and how long it took |
| Evaluation | Whether output or behavior meets a quality/safety rubric on chosen cases |
| Service metric | Request count, error, throttle, latency, token, or capacity behavior |
| Human feedback | Whether the result actually helped and what failure category occurred |

Correlate signals to a configuration version. Otherwise a score or incident cannot identify the model, prompt, agent, or deployment that produced it.

> **Related item:** Tracing shows the execution path—model calls, retrieval, tool calls, latency, and errors. Evaluation judges quality. Monitoring detects production behavior. You need all three to diagnose and improve an AI application.

---

## 5. Text, speech, and translation

### Text workloads

Generative models can summarize, classify, extract, rewrite, answer questions, and produce structured data. Specialized Azure language capabilities may be preferable for defined tasks such as named-entity recognition, key phrases, sentiment, conversational language understanding, or custom classification when predictability and supported semantics fit.

Define allowed labels or a JSON schema. Test negation, ambiguity, long input, multiple languages, names/numbers, and unsupported content. Preserve evidence spans when a reviewer needs to verify extraction.

| Task | Output example | Important distinction |
|---|---|---|
| Key phrase extraction | `shipping delay`, `damaged package` | Salient phrases, not necessarily topics with a fixed taxonomy |
| Named-entity recognition | person, organization, location, date | Identifies entities/types; does not authorize their use |
| Sentiment analysis | positive/neutral/negative plus supported detail | Sentiment is not intent, safety, or truth |
| Summarization | concise representation of source | Must preserve material meaning and evidence |
| Structured generative extraction | JSON matching a schema | Flexible reasoning, but validate schema and source support |

Use the current [Azure Language documentation](https://learn.microsoft.com/en-us/azure/ai-services/language-service/) for specialized capability names and supported behavior. **VERIFY CURRENT:** languages, SDKs, models, limits, regions, and pricing.

### Speech workloads

Speech to text transcribes audio. Text to speech synthesizes audio. Speech translation combines recognition and translation. Voice applications also need microphone/audio format, language, latency, partial results, turn detection, interruption, error recovery, consent, and transcript protection.

Custom speech or voices add data, consent, approval, evaluation, and lifecycle responsibilities. **VERIFY CURRENT:** supported languages, regions, features, and access requirements in [Azure Speech documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/).

For a spoken assistant, reason across the full path:

```text
microphone/audio → endpoint/turn detection → speech recognition
                 → model or agent → text validation → speech synthesis
```

Good transcript accuracy does not guarantee a responsive voice experience. Budget latency per stage, handle silence and interruptions, and do not speak an unconfirmed side effect as completed.

### Translation

Translation evaluation must cover terminology, names, numbers, tone, negation, layout, and target-language fluency. Document translation and conversational text translation have different preservation and latency needs. A natural-sounding result can still invert meaning.

Azure Translator is a purpose-built option for supported text/document translation; a generative model can support contextual translation flows. Choose by language support, terminology/customization, document layout, latency, scale, evaluation evidence, and current availability—not by assuming the largest model is always more accurate.

---

## 6. Vision and multimodal workloads

Computer vision can classify an image, detect objects, extract text, describe content, answer questions about visual evidence, or generate/edit media. Match the output contract to the capability.

| Need | Approach |
|---|---|
| Read text from an image | OCR/document or image text extraction |
| Locate known object categories | Object detection |
| Assign one/more image categories | Classification |
| Flexible description or visual Q&A | Multimodal generative model |
| Produce/edit an image | Image generation/editing model |

Generation workflows require prompt/reference rights, safety filtering, output provenance, review, and storage. Vision input can contain private content, harmful material, or indirect prompt injection embedded as text.

For visual understanding, preserve the image and question used for evaluation. A broad caption, concise alt text, field extraction, and answer to a visual question have different success criteria. For generation, record prompt/reference identifiers, configuration, safety result, and output when provenance or review matters.

Use current product guidance for [vision-enabled models](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/gpt-with-vision) and [image generation/editing](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-mai-image). **VERIFY CURRENT:** eligible models, media limits, supported generation/edit operations, regions, safety controls, and prices.

Accessible alt text describes the information needed for the page's purpose. Decorative images may require empty alt text; complex diagrams may need a concise label and a long description. Generated descriptions require contextual human review.

> **Related item:** Multimodal does not mean universally capable. A model can accept an image while performing poorly on tiny text, precise counting, spatial measurement, or domain-specific diagnosis. Evaluate the exact task and input quality.

---

## 7. Content Understanding and information extraction

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

#### Separate extraction stages and evidence

| Stage | Example output | Failure to test |
|---|---|---|
| Input validation | accepted PDF/image/audio/video reference | Corrupt, unsupported, oversized, inaccessible source |
| Recognition | text, transcript, key frames | Missing/incorrect characters, speakers, timestamps, frames |
| Structure/layout | paragraphs, tables, regions, segments | Wrong reading order or table association |
| Field interpretation | invoice total, vendor, event summary | Value mapped to wrong field despite correct source text |
| Representation | structured JSON or Markdown | Lost evidence, schema mismatch, unsafe content |
| Application decision | review, index, agent context, automation | High-impact value accepted without suitable review |

The current [Content Understanding quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/quickstart/use-rest-api) demonstrates asynchronous analysis across documents, images, audio, and video. Keep analyzer ID/schema, input identifier, operation status, result version, page/region/timestamp evidence, and review outcome connected. **VERIFY CURRENT:** analyzer modes, API versions, model dependencies, supported inputs, limits, regions, and pricing.

### Light application pattern

1. upload or reference a permitted public sample;
2. invoke a prebuilt or custom analyzer;
3. poll the asynchronous operation using bounded intervals/timeouts;
4. validate returned fields and confidence/evidence;
5. show the source region to a reviewer;
6. handle unsupported/corrupt input and partial results;
7. record safe telemetry without copying sensitive content unnecessarily.

> **Related item:** Human review should be risk-based. Low confidence is one trigger, but high-confidence extraction of a high-impact value may still require verification.

---

## 8. Objective-to-scenario drill

An organization wants a public help assistant that accepts typed or spoken questions, answers policy questions, lets users attach a form, and can open a low-severity support case after confirmation.

| Requirement | Reasoned implementation boundary |
|---|---|
| Typed or spoken request | Text input or Speech recognition; protect audio/transcripts and define language/latency behavior |
| Policy answer | Deployed generative model plus authorized grounding, citations, and abstention when evidence is missing |
| Attached form | Content Understanding produces fields/Markdown with page/region evidence; review uncertain or high-impact values |
| Open support case | Single agent may select a narrowly defined tool; API enforces authentication, authorization, validation, confirmation, and idempotency |
| Spoken response | Validate response before Speech synthesis; do not announce an action succeeded until the tool confirms it |
| Operational proof | Correlated trace, evaluation cases, service metrics, safe feedback, and accountable audit for the side effect |

Apply responsible AI across the whole design: test language/accessibility slices, fail safely, minimize data, disclose AI involvement and evidence, and name the human owner. Content filtering does not replace policy grounding; private networking does not replace authorization; a confirmation prompt does not replace API enforcement.

Use this exam-question sequence:

1. Identify the requested workload and input/output modality.
2. Choose a general model, agent, or specialized Foundry Tool from the required behavior.
3. Identify the resource, project, deployment, endpoint, client, and identity boundary involved.
4. Add the responsible-AI and operational control that matches the failure.
5. Explain why the closest alternative does not meet the stated requirement as well.

---

## 9. Hands-on labs

### Lab 1: Model comparison

Using public, non-sensitive prompts, compare two eligible Foundry models on classification, structured extraction, and explanation. Record model/deployment, prompt, quality, safety, latency, and approximate consumption. Choose based on evidence.

### Lab 2: Small chat app

Build a local Python app using current Foundry documentation and keyless authentication where supported. Add bounded history, structured output, timeout, retry, and a correlation ID. Prove invalid output is rejected.

### Lab 3: Tool-using agent

Create an agent with a read-only public-data tool and a simulated side-effecting tool behind confirmation. Validate arguments, enforce authorization outside the model, cap turns, and test prompt injection, timeout, denial, and repetition.

### Lab 4: Speech and text pipeline

Transcribe a short public-domain audio sample, summarize it, translate a passage, and synthesize a response. Compare names, numbers, negation, latency, and transcript privacy needs.

### Lab 5: Visual accessibility

Use public images to create short alt text and detailed descriptions. Include an infographic, decorative image, and image containing misleading embedded instructions. Review against page purpose.

### Lab 6: Content extraction

Analyze public forms/documents/media with Content Understanding. Validate structured fields, inspect page/region evidence, introduce a low-quality scan, and route uncertain/high-impact values to review.

---

## 10. Knowledge checks and distinctions

1. A generated answer is fluent but unsupported. Which evaluation property failed?
2. A model selects a refund tool correctly but exceeds the user's limit. Which control cannot be delegated to the model?
3. A smaller model meets the task threshold with lower cost and latency. What reason remains to choose the larger model?
4. OCR text is accurate but an invoice total field is wrong. Which later stage should be inspected?
5. An image contains instructions telling the agent to reveal data. Why should those words remain untrusted?
6. A voice agent produces good text but feels unusable. Which real-time interaction requirements might be missing?
7. A model card has the best benchmark score, but another model performs better on the product's evaluation set. Which evidence should drive deployment?
8. A form's OCR text is correct, but the `Total` field points to a subtotal. Which extraction layer failed?
9. A user can reach an endpoint but receives an authorization error. Why is that not proof of a networking problem?
10. An agent asks the user to confirm a refund, but its API accepts amounts over policy. Which layer must enforce the invariant?

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

### Readiness checklist

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

### Primary references

- [Official AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
- [AI-900 retirement notice](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900)
- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/)
- [Foundry models](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview)
- [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview)
- [Responsible AI principles](https://www.microsoft.com/en-us/ai/principles-and-approach)
- [Azure AI Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
- [Azure Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)
- [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview)
- [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)
- [AI concepts learning path](https://learn.microsoft.com/en-us/training/paths/ai-concepts/)
- [AI applications and agents learning path](https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/)
- [Foundry capability map](https://learn.microsoft.com/en-us/azure/foundry/concepts/capabilities)
- [Content Understanding quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/quickstart/use-rest-api)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AI-901 course](https://learn.microsoft.com/en-us/training/courses/ai-901t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation and implementation sequence |
| [Microsoft — AI-901 Practice Assessment on AI Skills Navigator](https://aiskillsnavigator.microsoft.com/credentials/cert-83587e0a0754cfee561ade3e27d9fa1cdaf15ae03be52d2413b2b858d1b4eda4) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check; AI Skills Navigator sign-in is required, and the blueprint and product documentation remain authoritative |
| [Microsoft Learn AI-901 certification material](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/) | Free | About 10–14 hours | Official scope anchor; complete current Foundry exercises rather than relying on AI-900 modules |
| [Microsoft Learn — AI concepts](https://learn.microsoft.com/en-us/training/paths/ai-concepts/) | Free | 3 hours 51 minutes | Current seven-module concepts path across the workloads in the first domain |
| [Microsoft Learn — AI applications and agents](https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/) | Free | 5 hours 37 minutes | Current seven-module implementation path across Foundry, apps/agents, text, speech, vision, extraction, and retrieval |
| [O'Reilly — Azure AI Fundamentals AI-901](https://www.oreilly.com/videos/azure-ai-fundamentals/9781807782979/) | Subscription | 4 hours 4 minutes | Anand Rao Nednur course published April 2026 and aligned to the replacement exam |
| [Udemy — AI-901 by Christopher Nett](https://www.udemy.com/course/ai-901-azure-ai-fundamentals/) | Purchase or subscription | About 6 hours 20 minutes | Course shown as updated June 2026; inspect demos and current SDK usage |
| [Udemy — AI-901 exam prep by Kuljot Singh Bakshi](https://www.udemy.com/course/azure-ai-fundamentals-exam-prep/) | Purchase or subscription | About 6 hours 54 minutes | Alternative shown as updated July 2026; inspect previews and hands-on depth |
| [Whizlabs — AI-901 instruction and practice](https://www.whizlabs.com/ai-901-microsoft-azure-ai-fundamentals/) | Paid course or subscription | About 3–6 hours for 3 quizzes and review; video total not published | Public listing shows 63 videos and three quizzes; use the assessment after learning and verify explanations against the current blueprint |
| [Microsoft AI Show](https://learn.microsoft.com/en-us/shows/ai-show/) | Free | Select 2–5 hours by gap | Official product demonstrations; choose current Foundry, agents, speech, vision, and extraction episodes |
| [John Savill — AI-900 Study Cram v2](https://www.youtube.com/watch?v=bTkUTkXrqOQ) | Free | About 3 hours | Optional legacy concept refresher only; AI-900 retired and this does not cover AI-901 implementation scope |

No exact Pluralsight path or standalone MeasureUp AI-901 practice test was verified on August 31, 2026. The free Microsoft assessment above and the Whizlabs mixed bundle provide two different readiness checks. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
