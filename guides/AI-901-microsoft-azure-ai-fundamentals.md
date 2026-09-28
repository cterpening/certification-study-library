---
exam_code: AI-901
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AI-901 Microsoft Azure AI Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ai-901-coverage-record). The [official AI-901 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) is authoritative.

**Current baseline:** Skills measured as of April 15, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Official source:** [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)

> **Replacement note:** AI-900 retired on June 30, 2026. AI-901 is the active Azure AI Fundamentals exam and has a substantially more implementation-oriented Foundry scope. Older AI-900 resources can refresh concepts but are not an AI-901 study plan.

The September 28 [deep-review report](../docs/research/2026-09-28-ai-901-deep-review.md) maps all **29 detailed objectives** across seven groups. This guide adds six worked examples, eight labs and 36 explained checks. Cloud examples were syntax-checked only; the invoice validator and synthetic arithmetic were checked locally. No Azure lab or paid lesson was executed or watched.

The [certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/) lists 13 exam languages and links the sign-in Practice Assessment. Its empty training widgets do not invalidate the directly available course and learning paths below. The retrieved page did not establish a current exam duration; confirm appointment details when scheduling.

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

### Worked example 1: Fit evidence into a context budget

A fictional text model allows 8,192 tokens in total. Reserve 1,024 for output, 500 for instructions, 1,800 for the user/history and 400 for tool definitions. That leaves **4,468 tokens** for evidence. Four 1,200-token chunks need 4,800 tokens and exceed the budget by 332; three need 3,600 and leave 868 spare. Select relevant evidence and preserve citations before trimming trusted instructions. Count actual serialized requests with the selected model's rules; image/audio and reasoning-token accounting can differ. These numbers are an exercise, not a model specification.

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

### Worked example 2: An average can hide a failing group

Suppose a text classifier is correct on 90 of 100 examples for group A and 5 of 10 for group B. The overall score is **95/110 = 86.36%**, while B is at **50%**. Reporting only the average hides a useful investigation target. Check labeling, language/input coverage and error consequences; collect more representative B examples before interpreting a small sample as a precise population estimate or proof of a cause. Assign an owner and a follow-up evaluation. Fairness, reliability, transparency and accountability all contribute here.

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

#### A lightweight chat client

The [Python Projects SDK reference](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python) documents the project-client pattern below. Use a compatible 2.x `azure-ai-projects` package and `azure-identity`, an existing Foundry project/deployment, and an authorized Entra identity. Record the exact resolved package versions in your lab. The reference currently describes 2.7.0 and requires at least 2.3.0 for its main examples; stable packages can still expose preview features. Do not mix classic 1.x samples with this interface.

Set `FOUNDRY_PROJECT_ENDPOINT` to the project's `https://<resource>.services.ai.azure.com/api/projects/<project>` URL and `FOUNDRY_MODEL_NAME` to the **deployment name**. A local CLI sign-in can supply a development identity; production should use an appropriate workload identity and role. `DefaultAzureCredential` obtains a token; it does not grant access.

```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

with DefaultAzureCredential() as credential:
    with AIProjectClient(
        endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"], credential=credential
    ) as project:
        with project.get_openai_client() as client:
            response = client.responses.create(
                model=os.environ["FOUNDRY_MODEL_NAME"],
                input="Explain the difference between a transcript and a summary.",
            )
            if not response.output_text.strip():
                raise ValueError("No text answer; inspect the response outcome")
            print(response.output_text)
```

This is a minimal single-turn public-prompt example, not a production error handler. Add configured request/output budgets, timeouts, supported response-status checks, bounded retries and safe correlation telemetry for your model/client version. Nonempty output is not evidence of correctness. [Foundry Responses guidance](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/responses-api) recommends Agent Framework for orchestration; the SDK example here isolates the exam's lightweight client objective. Project and resource endpoints have different capability scopes.

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

#### Invoke an agent created in the portal

Create and test a **prompt agent** in the portal, using an eligible model deployment and a narrow instruction. Start without tools, then add a read-only tool and test its authorization and failure paths. Record its name, version and configuration. In a separate client script, reuse that resource instead of creating a new version on every request. This follows the [prompt-agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent).

```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

with DefaultAzureCredential() as credential:
    with AIProjectClient(
        endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"], credential=credential
    ) as project:
        with project.get_openai_client(
            agent_name=os.environ["FOUNDRY_AGENT_NAME"]
        ) as client:
            conversation = client.conversations.create()
            response = client.responses.create(
                conversation=conversation.id,
                input="Explain when this assistant should ask for human review.",
            )
            print(response.output_text)
```

This selects an agent by name; it does not demonstrate version pinning or tool execution. Inspect the actual configuration/version served, validate the response, and manage conversation retention/cleanup. A conversation ID is sensitive state, not authorization. A persisted prompt agent, a hosted runtime and an application-owned Responses loop have different deployment/state responsibilities.

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

#### Keep per-document failures visible

The [Language SDK quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/quickstart) calls `TextAnalyticsClient.analyze_sentiment`. Its Python example uses `azure-ai-textanalytics`; a Foundry chat client does not replace that client's endpoint/authentication contract. With an already configured Language client:

```python
def sentiment_rows(client, documents):
    rows = []
    for result in client.analyze_sentiment(documents):
        if result.is_error:
            rows.append({"id": result.id, "status": "error", "code": result.error.code})
        else:
            rows.append({"id": result.id, "status": "ok", "sentiment": result.sentiment})
    return rows
```

Also handle request-level exceptions at the caller. Test mixed sentiment, negation, unsupported inputs and a failed item in an otherwise successful batch. Silently dropping errors can inflate apparent success. Sentiment labels describe expressed attitude; they do not establish factual accuracy or authorize an action.

### Speech workloads

Speech to text transcribes audio. Text to speech synthesizes audio. Speech translation combines recognition and translation. Voice applications also need microphone/audio format, language, latency, partial results, turn detection, interruption, error recovery, consent, and transcript protection.

Custom speech or voices add data, consent, approval, evaluation, and lifecycle responsibilities. **VERIFY CURRENT:** supported languages, regions, features, and access requirements in [Azure Speech documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/).

For a spoken assistant, reason across the full path:

```text
microphone/audio → endpoint/turn detection → speech recognition
                 → model or agent → text validation → speech synthesis
```

Good transcript accuracy does not guarantee a responsive voice experience. Budget latency per stage, handle silence and interruptions, and do not speak an unconfirmed side effect as completed.

#### Recognition results and direct spoken prompts

The [Speech quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text) uses the separate `azure-cognitiveservices-speech` package. With a configured recognizer and permitted short audio, distinguish recognized speech, no match and cancellation:

```python
import azure.cognitiveservices.speech as speechsdk

def transcribe_short(recognizer):
    result = recognizer.recognize_once_async().get()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return {"status": "ok", "text": result.text}
    if result.reason == speechsdk.ResultReason.NoMatch:
        return {"status": "no-match", "text": None}
    return {"status": "error", "text": None}
```

Record a sanitized cancellation diagnostic separately; do not treat no-match/error as an empty successful transcript. The quickstart's one-shot operation ends on silence or after up to 30 seconds. Choose continuous or another supported transcription path for longer input. This fragment does not configure audio, credentials, cancellation or synthesis.

A deployed multimodal voice model can accept spoken prompts without your application chaining separate STT and TTS services. Confirm its input/output audio formats and model support, test silence/interruptions and protect transcripts. The [voice prompt-agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-voice-agent) is **preview**, requires project/region access and uses a different voice SDK surface; its current examples require Projects 2.7.0 or later. A hosted Voice Live integration's GA announcement is not proof that this separate feature is GA.

### Worked example 3: Measure speech errors and meaning

A 20-word reference transcript has two substitutions, one deletion and one insertion. Word error rate is **(2 + 1 + 1) / 20 = 20%**. Also score critical names, amounts and negation: deleting “not” can reverse the request even when most words are correct. Compare equivalent audio conditions and languages; a low overall WER does not prove intent preservation.

### Worked example 4: Budget voice response time

For a fictional sequential pipeline, turn detection takes 300 ms, recognition 400 ms, model generation 700 ms, synthesis 200 ms and transport 100 ms: **1,700 ms** in total. A streaming pipeline can overlap stages, so measure the actual trace and time to first audible response. Do not add independent p95 measurements and label their sum the end-to-end p95. When a user interrupts, stop queued playback and reconcile any already-started action; interrupted speech is not a canceled backend operation.

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

For a lightweight vision app, validate the permitted image and attach it using the selected SDK/API's image-input structure alongside a focused question. Compare the result with a known answer and preserve the input identifier. A generation model needs a separate supported generation/edit operation: receiving images does not imply producing them. Decode/store the documented output type and review it before display. Lab 5 requires both paths and a deliberately unsupported input.

**Lifecycle check:** the [Image Analysis migration notice](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/migration-options) retires the Image Analysis API on **September 25, 2028**, including supported cloud and container deployments. This is not a retirement of all vision capabilities. Choose OCR/document extraction, multimodal reasoning or structured image analysis by requirement and retest output contracts; alternatives are not automatic drop-in replacements.

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
3. follow the chosen API contract: poll an asynchronous operation with a deadline, or consume a supported synchronous response;
4. validate returned fields and confidence/evidence;
5. show the source region to a reviewer;
6. handle unsupported/corrupt input and partial results;
7. record safe telemetry without copying sensitive content unnecessarily.

### Choose the version, analyzer and model configuration

| Contract | Learner decision |
|---|---|
| GA `2025-11-01` | Start with the documented asynchronous analysis flow; accepted work is not a completed result |
| Preview `2026-06-01-preview` | Synchronous **Read/Layout** returns eligible small-document/image results directly; it does not make every analyzer synchronous |
| Preview agentic document analysis | Multistep reasoning with one input file per request in the initial preview; continue validating calculations and evidence |

Check the [release history](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/whats-new) for feature-specific support. Read/Layout does not require an LLM deployment. For model-dependent analyzers, inspect `supportedModels` and map supported names/aliases to actual deployments. [Model configuration guidance](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/models-deployments) supports resource defaults or per-request `modelDeployments`; request mappings override defaults. Prebuilt aliases such as `prebuilt-analyzer-completion` are not deployment names. Account for both model token charges and Content Understanding usage.

For document fields, [confidence and grounding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/overview) are opt-in via analyzer `estimateFieldSourceAndConfidence` or field `estimateSourceAndConfidence`. They apply to supported extract, classify and generate fields. Supported typed values are normalized automatically; the API does not provide a configurable raw-versus-normalized pair. Preserve source evidence and verify critical values independently. Signature detection locates a signature region; it does not establish signer identity or authenticity.

### Worked example 5: Valid JSON can still contain the wrong total

An invoice has subtotal 100.00 and tax 8.00. An extracted total of 100.00 is incorrect even if its confidence is 0.99 and the JSON schema is valid. The following **original local validator** checks a deliberately narrow, single-currency invoice contract: exactly three nonnegative money strings, at most two decimal places, total = subtotal + tax. An application adapter must first map service fields into this contract. Discounts, currencies, credits and rounding policies need explicit additional rules.

```python
import re
from decimal import Decimal

def invoice_is_consistent(fields):
    keys = {"subtotal", "tax", "total"}
    if not isinstance(fields, dict) or set(fields) != keys:
        return False
    if any(not isinstance(v, str) or
           re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", v) is None or len(v) > 12
           for v in fields.values()):
        return False
    values = {k: Decimal(v) for k, v in fields.items()}
    return values["subtotal"] + values["tax"] == values["total"]
```

Route a false result to review; never repair it by inventing a value. A true result proves only this arithmetic contract, not that the figures came from the right invoice or that payment is authorized. Bounding string length keeps this example inside Decimal's default precision.

### Worked example 6: Completion, accuracy and coverage differ

Of 1,000 accepted analyses, 950 finish successfully, 30 fail and 20 remain in progress at the deadline. Completion coverage is **95%**, not 100%. Reviewers verify 940 of the 950 completed outputs as correct: that is **98.95% among completed outputs**, but only **94% of all planned requests** have a verified correct output. Keep failures and unfinished work visible. Neither HTTP acceptance nor a successful operation status certifies field correctness.

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

### Two useful Microsoft blog exercises

- [Content Understanding August updates](https://devblogs.microsoft.com/foundry/azure-content-understanding-updates-august-2026/) — Peyton Fraser, Krishnakumar Muthukrishnan and Joe Filcik, August 12, 2026. Build a one-page choice record for GA asynchronous extraction versus preview synchronous Read/Layout. Add a sample invoice's source, validation rule, review decision and latency measurement. Confirm the feature contract in current documentation. Published performance percentages are not guarantees for your documents.
- [Foundry July/August roundup](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/) — Nick Brady, September 9, 2026. Use its hosted-agent and Voice Live sections to draw the audio-event sequence. Mark where interrupted playback stops, where tool approval occurs and how the app distinguishes requested, started and completed work. Check preview status for each actual feature; the article is broader than this exam.

These are original exercises informed by selected announcement sections. They are adjacent implementation practice, not new exam objectives or evidence that linked samples have been executed.

## 9. Hands-on labs

Use only permitted non-sensitive fixtures. For every lab, keep configuration/version, input ID, expected outcome, observed result, failure diagnosis and cleanup evidence. A written plan or syntax check is not cloud execution. Record failed and skipped cases. Cloud resources and model calls can incur charges.

### Lab 1: Model comparison

Using public, non-sensitive prompts, compare two eligible Foundry models on classification, structured extraction, and explanation. Record model/deployment, prompt, quality, safety, latency, and approximate consumption. Choose based on evidence.

### Lab 2: Small chat app

Build a local Python app using current Foundry documentation and keyless authentication where supported. Add bounded history, structured output, timeout, retry, and a correlation ID. Prove invalid output is rejected.

### Lab 3: Tool-using agent

Create an agent with a read-only public-data tool and a simulated side-effecting tool behind confirmation. Validate arguments, enforce authorization outside the model, cap turns, and test prompt injection, timeout, denial, and repetition.

### Lab 4: Speech and text pipeline

Transcribe a short public-domain audio sample, summarize it, translate a passage, and synthesize a response. Compare names, numbers, negation, latency, and transcript privacy needs.

### Lab 5: Visual accessibility

Use public images to create short alt text and detailed descriptions. Include an infographic, decorative image, and image containing misleading embedded instructions. Review against page purpose. Build a lightweight image-input client and a separate image-generation call for a new illustration; record supported format, model, output type, safety result and an unsupported-input failure. Do not infer accuracy from a plausible caption.

### Lab 6: Content extraction

Analyze public forms/documents/media with Content Understanding. Validate structured fields, inspect page/region evidence, introduce a low-quality scan, and route uncertain/high-impact values to review.

### Lab 7: Validate a batch offline

Run the invoice validator with correct, mismatched, missing, malformed, negative and boolean inputs. Reproduce examples 1–6 with your own numbers. Build a batch ledger that retains failed/incomplete outcomes and displays both completion coverage and verified correctness. Explain why passing arithmetic is insufficient for invoice approval.

### Lab 8: Trace a voice interruption

Start with a paper event log: speech begins, turn ends, model responds, playback starts, user interrupts, a tool completes. Mark what must stop and what still needs reconciliation. Then, if your environment supports the chosen voice feature, reproduce with a harmless read-only tool; record first-audio/end-to-end latency and no-match/canceled cases. Compare the direct multimodal path with a separate Speech pipeline and label any preview dependencies.

---

## 10. Knowledge checks and distinctions

These original practice scenarios are not recalled exam questions. Explain your answer before reading the rationale.

1. **A generated answer is fluent but unsupported. What failed?**
   Groundedness: its claims lack evidence. Fluency and harm filtering do not verify facts.

2. **A correctly selected refund tool receives an amount above policy. Where must it be stopped?**
   The application or target API must enforce the authorized amount independently of model intent.

3. **A smaller model meets quality, safety, latency and cost requirements. Must you use the larger model?**
   No. Change only for a demonstrated unmet requirement; a larger model is not inherently a better fit.

4. **OCR is accurate but an invoice total maps to the subtotal. What should you inspect?**
   Field interpretation and source association, then application validation. Correct characters do not establish correct field meaning.

5. **An image asks the agent to reveal private data. How should the app treat that text?**
   As untrusted image content. It cannot override trusted instructions or source/tool permissions.

6. **Good voice response text still feels unusable. What might be wrong?**
   Turn detection, first-audio latency, audio format, interruptions or playback handling. Text quality alone is insufficient.

7. **A model-card benchmark winner loses on representative product cases. Which evidence guides selection?**
   The product evaluation and constraints, after checking its quality and coverage. Generic benchmarks are screening evidence.

8. **What distinguishes extraction from OCR?**
   OCR recognizes text; extraction maps source content into defined fields or other structured outputs.

9. **An endpoint is reachable but access is denied. What does that show?**
   Network reachability is separate from successful identity authentication and authorization at the needed scope.

10. **A refund confirmation screen exists. Can the backend omit policy checks?**
   No. The backend must authorize and validate every operation; a UI can be bypassed or stale.

11. **Does adding retrieved evidence retrain the model?**
   No. RAG supplies request context; fine-tuning changes learned weights.

12. **What goes in FOUNDRY_MODEL_NAME in the example?**
   The deployed model target name in the project, not an arbitrary catalog marketing name.

13. **Does DefaultAzureCredential assign an Azure role?**
   No. It discovers credentials and obtains tokens; permissions must already be assigned.

14. **Why should a client avoid creating an agent version every turn?**
   Creation is configuration work. Invoking an existing agent avoids unintended version changes and separates deployment from conversation.

15. **Does a conversation ID grant access or guarantee a pinned agent version?**
   Neither. Enforce identity and verify the actual agent/version configuration separately.

16. **What fits in example 1: three or four 1,200-token chunks?**
   Three fit within 4,468 remaining tokens; four exceed the budget by 332.

17. **Does the overall 86.36% score in example 2 describe both groups well?**
   No. Group B scores 50% on only ten examples. Investigate errors and improve representative sample coverage.

18. **Which principle calls for screen-reader and alternative-input testing?**
   Inclusiveness. Also preserve reliability and privacy across these interaction modes.

19. **Which principle requires identifying a responsible incident owner?**
   Accountability. A disclosure alone does not assign responsibility.

20. **Can positive sentiment prove that a claim is true or safe?**
   No. Sentiment measures expressed attitude, not truth, intent or policy compliance.

21. **Why retain text-analysis errors in a batch report?**
   Dropping failed documents changes the denominator and hides coverage gaps.

22. **What is WER for two substitutions, one deletion and one insertion over 20 reference words?**
   20%. Also evaluate critical meaning, because different word errors have different consequences.

23. **Can the one-shot Speech example transcribe an hour-long meeting as written?**
   No. It stops at silence or up to 30 seconds; choose a documented longer-audio path.

24. **Is a no-match result an empty successful transcript?**
   No. Preserve its distinct outcome so the app can retry appropriately or ask for another input.

25. **Why is 1,700 ms in example 4 not a guaranteed streaming latency?**
   It sums a fictional sequential path. Streaming overlaps work; measure actual end-to-end traces.

26. **Does stopping spoken playback undo a completed tool call?**
   No. Reconcile backend state and use approval/idempotency controls appropriate to the action.

27. **Are all voice prompt agents GA because a related Voice Live integration is GA?**
   No. Feature-specific documentation still marks voice prompt agents preview.

28. **Can every image-input model generate images?**
   No. Check separate input/output modalities and the supported generation operation.

29. **Does the Image Analysis retirement end all Azure vision services in 2026?**
   No. Its specific API retirement date is September 25, 2028; scope alternatives separately.

30. **Does synchronous Content Understanding eliminate polling for all analyzers?**
   No. Preview synchronous support applies to eligible Read/Layout operations; other flows retain their documented operation contract.

31. **Must every Content Understanding analyzer have a model deployment?**
   No. Read/Layout is an exception. Model-dependent analyzers need supported deployment mappings.

32. **Are a prebuilt completion alias and an actual deployment name interchangeable?**
   No. Map the supported alias to a real deployment; a per-request mapping can override resource defaults.

33. **Does confidence 0.99 override an invoice arithmetic failure?**
   No. Review source evidence and the failed rule; confidence is not proof of correctness.

34. **Can an extracted signature prove who signed?**
   No. Locating a signature region does not authenticate identity or legal validity.

35. **How do you enable supported document field confidence/grounding?**
   Use the documented analyzer-wide or per-field opt-in settings, then calibrate review policy on representative examples.

36. **Why report both 98.95% and 94% in example 6?**
   The first is correctness among completed outputs; the second counts verified correct outputs over all planned requests. Missing work remains visible.

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
| [Microsoft Learn — AI concepts](https://learn.microsoft.com/en-us/training/paths/ai-concepts/) | Free | Budget 4–6 hours including notes (editorial estimate) | Seven modules; current total runtime not exposed. Concepts path across the workloads in the first domain |
| [Microsoft Learn — AI applications and agents](https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/) | Free | Budget 6–10 hours including labs (editorial estimate) | Seven modules; current total runtime not exposed. Implementation path across Foundry, apps/agents, text, speech, vision, extraction, and retrieval |
| [O'Reilly — Azure AI Fundamentals AI-901](https://www.oreilly.com/videos/azure-ai-fundamentals/9781807782979/) | Subscription | 4 hours 4 minutes | Anand Rao Nednur, April 2026; indexed public outline only, direct access blocked. Verify current SDK demos before purchase |
| [Udemy — AI-901 by Christopher Nett](https://www.udemy.com/course/ai-901-azure-ai-fundamentals/) | Purchase or subscription | About 6 hours 20 minutes | Christopher Nett; indexed outline: June 2026, 12 sections/49 lectures. Direct access blocked; lessons not watched |
| [Udemy — AI-901 exam prep by Kuljot Singh Bakshi](https://www.udemy.com/course/azure-ai-fundamentals-exam-prep/) | Purchase or subscription | About 6 hours 54 minutes | Kuljot Singh Bakshi; indexed outline: July 2026, 11 sections/47 lectures. Direct access blocked; lessons not watched |
| [Whizlabs — AI-901 instruction and practice](https://www.whizlabs.com/ai-901-microsoft-azure-ai-fundamentals/) | Paid course or subscription | Duration and current counts unverified | Direct and indexed pages expose only a title shell; earlier 63-video/three-quiz counts were not reproduced. Verify the current bundle before purchase |
| [Pluralsight — Implement AI Solutions by Using Microsoft Foundry](https://www.pluralsight.com/courses/implement-ai-solutions-by-using-microsoft-foundry--ai-901) | Subscription | 1 hour 59 minutes | Clint Bonnett, September 16, 2026. Public outline targets the implementation domain; pair with concepts study. Paid lessons not watched |
| [Microsoft AI Show](https://learn.microsoft.com/en-us/shows/ai-show/) | Free | Select 2–5 hours by gap | Official product demonstrations; choose current Foundry, agents, speech, vision, and extraction episodes |
| [John Savill — AI-900 Study Cram v2](https://www.youtube.com/watch?v=bTkUTkXrqOQ) | Free | About 3 hours | Optional legacy concept refresher only; AI-900 retired and this does not cover AI-901 implementation scope |

A matching Pluralsight implementation course is now verified; no exact standalone MeasureUp AI-901 listing was found in the bounded September 28 search. This is not proof that none exists. The Microsoft assessment remains sign-in gated, so its questions and coverage were not inspected. Paid resources were evaluated only from public metadata, not lesson quality or question originality. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
