---
exam_code: GES-C02
vendor_id: snowflake
official_blueprint: https://learn.snowflake.com/en/certifications/snowpro-GenAI-C02/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# SnowPro Specialty: Gen AI (GES-C02) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public scope, citations, links, lifecycle evidence and exam-integrity compliance were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#ges-c02-coverage-record).

**Current baseline:** GES-C02 is the active SnowPro Specialty: Gen AI exam. Snowflake publishes four abilities and recommends one or more years of enterprise Gen AI experience with Snowflake. Python proficiency plus prior data-engineering and SQL knowledge are assumed.<br>
**Upcoming change:** No future revision or retirement announcement was present on the checked official page September 2, 2026.<br>
**Public scope boundary:** Snowflake distributes the detailed study guide through a web form. This guide maps the four live public abilities to current first-party documentation; it does not reconstruct inaccessible subobjectives or weights. Reconcile it with the official guide you receive before scheduling.<br>
**Credential contract:** The public certification catalog lists Specialty attempts at USD 225. Current policy says SnowPro certifications expire after two years, uses a 0–1000 scale with 750 passing, and defines renewal and retake rules. Confirm price, format, question count, delivery, language, policy and accommodations at registration.

## How to use this guide

Treat every Gen AI design as an evaluated data application, not a prompt demo. Begin with the business decision and permitted action, then define data authority, model/retrieval/tool boundaries, identity, failure behavior, quality and safety thresholds, cost/latency targets, telemetry, human escalation and rollback. Build the smallest authorized version with synthetic or approved data and preserve an evidence pack.

For every feature choice, be able to answer: why this surface rather than another; which role and object grants apply; where data, prompts, model artifacts and outputs live; which region/model limitations apply; how retrieval or tool access is constrained; what is measured; how unsafe or low-confidence output is contained; and how the version is reproduced or reversed.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural or adjacent context. It helps explain the topic but does not claim Snowflake published that wording in GES-C02's four public abilities.

## Public ability map

| Published ability | Evidence to produce |
|---|---|
| Define and implement Snowflake Gen AI principles, capabilities and best practices | Use-case contract, responsible-risk record, architecture decision, identity/data boundary, evaluation plan and cost/operations plan |
| Use Cortex AI features/functions, including LLMs, for customer use cases | Feature-selection matrix, governed prompt/context/retrieval/tool implementation, positive/adversarial evaluation and observable run evidence |
| Build and fine-tune open-source models with Snowpark Container Services and Model Registry | Reproducible artifact/image, lineage/signature/metrics, least-privilege service, capacity/endpoint evidence, rollout and rollback |
| Use document-processing functions to build, manage and optimize parsing pipelines | Document contract, parse/extract/chunk/index lineage, quality set, idempotent orchestration, security/cost metrics and replay proof |

---

## 1. Define and implement Snowflake Gen AI principles and best practices

### Frame the use case before selecting a model

Write the user, decision or action, permitted data, acceptable output, quality threshold, latency, volume, budget, regulatory obligation and failure consequence. Separate deterministic analytics, predictive ML, generative transformation, retrieval-grounded answering and agentic action. SQL or rules remain better when an exact, auditable result exists; an LLM helps when language understanding or generation is central and probabilistic output can be evaluated and contained.

Classify the task: summarize, classify, extract, translate, generate, answer over approved knowledge, query governed metrics, understand media, write code, or plan/use tools. Match it to the narrowest adequate Snowflake surface. A managed AI SQL function can be simpler than a custom application; Cortex Search supports unstructured retrieval; Cortex Analyst works over a governed semantic view; Cortex Agents orchestrates models and tools; Snowflake Intelligence/CoWork supplies a business-facing agent experience; Snowpark Container Services fits custom runtimes and open models. Current names and availability are volatile, so verify documentation in the target account and region.

Create explicit acceptance and abstention behavior. A support assistant may cite approved articles and route uncertain answers to a person. A document extractor may reject a field below confidence or schema validation. An agent proposing a refund must not execute it without authorized policy, identity, limit and approval controls. “Sounds good” is not a measurable success criterion.

### Design context, grounding and evaluation

A model response is conditioned by system/developer/user instructions, retrieved context, tool results, conversation state and model behavior. Define precedence and a context budget. Do not stuff arbitrary documents into a prompt. Select authoritative sources, preserve document identity/version/access metadata, chunk along meaning and structure, retrieve by an evaluated method, and require traceable citations where users need evidence.

Evaluate components as well as the final answer. Retrieval measures can include relevance, coverage, ranking and citation support. Generation measures can include correctness, groundedness, completeness, instruction following, format validity, tone and refusal. Tool evaluation checks selection, arguments, authorization, outcome and recovery. System evaluation adds latency, availability, token/credit consumption, concurrency and user/business outcomes.

Build a versioned representative set with normal, ambiguous, missing-context, multilingual, long-context, malicious and edge cases. Keep train/tune examples separate from evaluation. Slice results by document type, user group, language and risk. Combine deterministic checks, model judges with calibrated rubrics and human subject-matter review; none is universally sufficient alone.

### Govern the complete data and action path

Inventory prompts, staged files, tables/views, semantic views, search services, models, registry artifacts, agents, tools, network integrations, logs and outputs as securable data/application assets. Apply least privilege, role hierarchy, object ownership, masking/row policies and network/external-access controls as appropriate. Understand caller versus owner execution and which user/default role an interactive agent actually evaluates.

Threat-model prompt injection, indirect instructions in documents, unauthorized retrieval, sensitive-data disclosure, insecure output use, tool argument manipulation, excessive agency, model/artifact supply chain, denial/cost abuse and logging leakage. Treat model output as untrusted until validated for the destination. Parameterize downstream SQL/API calls; allowlist tools/actions/resources; use bounds, approvals and idempotency for material changes; redact or minimize sensitive logs.

Define incident controls: disable an agent/tool/endpoint, revoke grants or credentials, roll back prompt/model/index/image versions, preserve traces, identify affected users/data/actions and correct durable side effects. Responsible AI is an operating practice across data, model, user experience and response—not a one-time disclaimer.

**Related item:** Retrieval augmentation changes what context reaches a model; fine-tuning changes model behavior. Neither automatically supplies authorization, factuality, privacy or fresh data.

---

## 2. Use Cortex AI features and functions for customer use cases

### Choose the narrowest managed surface

Cortex AI Functions expose AI operations through SQL/Python-friendly interfaces. Current functions cover general completion plus tasks such as classification, embedding, similarity, sentiment, translation, transcription, redaction, filtering, summarization and document work. Prefer a purpose-built function when its input/output contract fits; use `AI_COMPLETE` when controlled general or multimodal generation is required. Confirm current function name, model, data type, limit, region and privilege because legacy `SNOWFLAKE.CORTEX.*` names are being replaced by canonical `AI_*` surfaces.

For each invocation, constrain input rows/files, validate null/size/type, select a suitable model, define prompt and structured output/schema, capture version/configuration, parse defensively and record failures/cost. Batch work should be restartable and attributable. Do not call an expensive function repeatedly over unchanged rows; persist input hashes and versioned results where policy allows. Test cross-region inference and data-governance implications rather than assuming availability.

Embeddings convert content into vectors for similarity workflows, but embedding model, dimensionality, normalization and indexing must remain compatible. Re-embedding is a migration. Cortex Search combines search capabilities over a defined source/query with refresh behavior and access controls. Measure retrieval before tuning generation: poor chunks, metadata, filters or corpus permissions cannot be repaired reliably by a better prose prompt.

### Build governed natural-language and agent experiences

Cortex Analyst translates natural-language questions through a semantic view. The semantic layer should encode verified dimensions, facts, metrics, relationships, synonyms and sample/verified queries as appropriate. Test generated SQL, access behavior, ambiguity and business definitions. Do not expose raw schemas and hope a model infers finance or operational semantics correctly.

Cortex Agents can orchestrate Cortex Analyst for structured data, Cortex Search for unstructured data and other supported tools. Define agent instructions, model selection, tool descriptions/schemas, resource bounds and conversation/thread handling. A tool description is part of the control plane: vague names or overlapping capabilities cause incorrect selection. Validate tool arguments and results, propagate identity correctly, and require confirmation or human approval before sensitive actions.

Remote Model Context Protocol connectors can expose external tools. Treat an MCP server as an integration and software-supply-chain boundary: authenticate the user/workload, allowlist endpoints and tools, minimize scopes, validate schemas, time out calls, prevent secret/context leakage, log decisions and define unavailable/partial-effect recovery. MCP standardizes context/tool exchange; it does not make a tool trusted.

Snowflake Intelligence/CoWork and Cortex Code provide user-facing agent and coding experiences. Review generated SQL, Python, objects and changes before execution. Generated code needs the same lint, test, security, performance and change-control gates as human code. Never grant a broad role to compensate for a confusing agent authorization failure.

### Engineer prompts, structured outputs and RAG

Use a stable instruction template: role/purpose, authorized sources, task, constraints, decision/refusal rules, output schema and examples chosen for coverage. Delimit untrusted text and say it is data, not instruction. Put volatile business knowledge in governed retrieval or tools instead of a hard-coded prompt. Version prompts, semantic definitions, corpus/index, model and tool configuration together so an evaluation can be reproduced.

A production RAG path is ingest → parse → normalize → classify/protect → chunk → embed/index → retrieve/filter/rerank → construct context → generate → cite/validate → observe/feedback. Every arrow needs an owner, identity, contract and failure path. Enforce source authorization before or during retrieval, not after a model has already seen restricted content.

Measure retrieval recall/precision/ranking on labeled questions; then measure grounded answer and citation support. Include “answer absent” cases. An abstention can be correct. Cache only when identity, corpus/version, freshness and data classification permit it. Monitor query patterns, retrieval results, model/tool traces, latency, errors and consumption without logging secrets or unrestricted sensitive content.

**Related item:** A semantic view and a vector/search index solve different grounding problems. Structured business metrics need modeled relationships and definitions; unstructured knowledge needs document retrieval and provenance. Agents can use both.

---

## 3. Build and fine-tune open-source models with container services and Model Registry

### Decide managed versus custom model operation

Use managed Cortex models/functions when their capability, governance, region, latency and cost meet the use case. Use an open-source model in Snowpark Container Services when you need a specific architecture/weight/license, custom dependencies, tuning method, serving behavior or portability that the managed surface does not provide. Custom control also transfers more responsibility: license and provenance, vulnerabilities, image/dependency integrity, capacity, scaling, endpoint protection, monitoring, upgrades and incident response.

Select a model using task quality, language/modality, context, license/acceptable-use terms, size, precision/quantization, hardware memory/throughput, latency and supportability. Establish a zero/few-shot or RAG baseline before tuning. Fine-tune only when repeatable behavior/task adaptation justifies data preparation and lifecycle cost; do not use tuning merely to inject frequently changing facts.

Prepare approved training/tuning data with provenance, consent/license, classification, deduplication, quality checks, train/validation/test separation and leakage/poisoning review. Record base model and revision, tokenizer, template, code/dependencies, random seeds, hyperparameters, hardware, checkpoints and evaluation. Compare the tuned candidate to baseline by slices and safety cases, not only aggregate loss.

### Package and run the workload reproducibly

Snowpark Container Services uses image repositories, compute pools and services or job services. Package a pinned OCI image, generate dependency and vulnerability evidence, avoid embedded credentials, run as a constrained identity and define ingress/egress through supported controls. A long-running service is restarted when its container exits; a job service is finite and is not the same operational contract. Training/tuning commonly fits an authorized GPU job service; inference may use a persistent service or registry-supported serving path.

Choose compute-pool instance type, minimum/maximum nodes and autoscaling from measured model memory, request size, batch/concurrency and SLO. Separate build/training and production-serving identities and pools when risk or contention requires it. Bound queue, timeout, payload, replicas and spend; test cold start, node loss, out-of-memory, malformed input, burst, downstream outage and scale down. Capture service/job status, events, metrics and logs with correlation IDs and safe redaction.

Use private, reviewed artifacts and trusted base images. Sign or record digest/provenance where available. Scan the OS, Python/native dependencies and model artifact; an ML file can contain executable serialization or malicious configuration. Restrict external egress and image/model pull paths. Patch and rebuild reproducibly instead of mutating a running container.

### Govern models through the registry and delivery lifecycle

Snowflake Model Registry provides a governed model/version record with signatures, metrics, metadata and lineage, and supports inference through Snowflake compute choices. Log the model with an explicit input/output signature and representative sample where appropriate. Attach evaluation metrics, dataset/code/run references, owner, approval, intended/forbidden use and lifecycle state. Treat aliases/tags as deployment pointers, not substitutes for immutable versions.

Promote development → validation → staged/canary → production through gates. Compare output quality/safety, endpoint health, latency percentiles, throughput, error/timeout/OOM, GPU utilization and cost per accepted outcome. Shadow or canary when consequences justify it. Rollback means restoring the complete compatible bundle: model, tokenizer, prompt/template, image/dependencies, endpoint configuration and callers.

For batch inference, design deterministic versioned inputs and outputs with idempotent replay. For online endpoints, authenticate and authorize callers, limit request size/rate/concurrency, validate schemas, protect against adversarial inputs and avoid returning internal errors. Monitor drift in input, use case and quality; a healthy endpoint can serve bad answers perfectly.

**Related item:** Model Registry records and governs model versions; an image repository stores container images; a compute pool supplies nodes; a service exposes a running workload. Be able to trace how they connect without treating them as interchangeable.

---

## 4. Build, manage and optimize document parsing pipelines

### Start with a document contract

Inventory source/owner, document type/version/language, digital versus scanned origin, expected layout/tables/images/handwriting, size/pages, classification, residency, retention, update/delete behavior and downstream use. Define accepted formats and limits from current documentation. Stage documents with least-privilege access and an immutable content hash/version so retries and corrections are distinguishable.

Current `AI_PARSE_DOCUMENT` extracts text, layout structure and optionally images from staged documents. Layout mode is appropriate when reading order, headings, tables and visual structure matter; OCR/text extraction may fit simpler cases. The older `SNOWFLAKE.CORTEX.PARSE_DOCUMENT` exists for compatibility but is documented for deprecation by the end of 2026, so new designs should use the canonical `AI_PARSE_DOCUMENT` surface.

`AI_EXTRACT` produces structured fields, lists or tables from documents according to questions or schema. `AI_COMPLETE` can reason over supported files or parsed content for broader tasks. Other current functions can classify/filter, transcribe media or redact sensitive text. Select functions by required output and evaluation; do not chain every AI feature by default. Confirm region, type, size/page, privilege and consumption limits.

### Build a restartable, governed pipeline

Use a state model such as discovered → validated → protected/quarantined → parsed → extracted/chunked → indexed → evaluated → published. Persist content hash, source version, parser/function/model/prompt/schema version, processing timestamp, result location, error and approval. Make each transition idempotent. A retry must not duplicate chunks, overwrite a newer version or leave half-published search content.

Validate file signatures/types and malware policy before processing. Quarantine unsupported, corrupt, encrypted or policy-prohibited inputs. Apply access controls to the original, intermediate images/text, extracted structured fields, chunks/index and generated output. Redaction after indexing is too late if restricted content has already entered retrieval. Propagate document and row-level authority into search filters or separate services where required.

Preserve page, section, table, image and source-version provenance in chunks. Chunk at semantic/layout boundaries with deliberate overlap; avoid separating a table from its header or a policy condition from its exception. Select embedding and index configuration as a versioned contract. On change/delete, identify and remove every derived object. Rebuild or dual-run indexes when embedding/chunk/schema versions change.

Orchestrate bounded batches with streams/tasks/dynamic tables or application code as supported by the chosen functions. Track discovered/processed/failed documents and pages, queue age, parse/extract latency, warehouse/function consumption and retries. Use documented warehouse guidance: document functions may be service-driven, and simply increasing warehouse size does not necessarily accelerate them.

### Evaluate and optimize the right layer

Create a gold set across document types, scans, languages, layouts, tables, checkboxes, handwriting, missing fields and adversarial embedded instructions. For parsing, compare reading order, text/layout/table/image retention and character errors. For extraction, measure field/table precision/recall or exact/schema validity, plus missing/ambiguous handling. For RAG, measure chunk/retrieval relevance and citation support before answer style.

Diagnose errors by layer: acquisition/file → parse/OCR/layout → normalization/protection → extraction/chunk → embedding/index/retrieval → prompt/model → output validation/publication. Changing the LLM cannot restore a table lost during parsing. A larger overlap can improve retrieval but increase duplication, context and cost. A more detailed extraction schema can improve consistency but raise latency and failure rate. Use controlled comparisons.

Test duplicate arrival, corrected version, document deletion, parser/model update, partial failure, timeout, malformed file, poison instruction, unauthorized user and full replay. Define human review for sensitive or low-confidence fields. Preserve evidence for the exact source and pipeline versions that produced an answer or action.

**Related item:** Document processing prepares governed evidence; Cortex Search retrieves it; a model synthesizes it; an agent may act on it. Each layer needs its own quality, security and recovery controls.

---

## Integrated scenarios

### Scenario 1: Governed support knowledge assistant

Build an assistant over synthetic public and restricted support articles. Define identity and source access, parse/chunk/index with document/version provenance, retrieve with authorization filters, require citations and abstention, and evaluate answer/retrieval quality. Attempt indirect prompt injection and restricted-document queries; prove denial, traceability and index rollback.

### Scenario 2: Contract extraction and review

Process varied synthetic contracts through validation, `AI_PARSE_DOCUMENT` and `AI_EXTRACT` into a versioned schema. Preserve page evidence, redact restricted values before broader use, route ambiguous/missing/high-risk fields to a reviewer, and publish only validated rows. Measure field/table quality, latency/pages/cost and idempotent corrected-document replay.

### Scenario 3: Open-model governed inference service

Choose an appropriately licensed small model, establish a managed-model/RAG baseline, tune only on approved synthetic examples, record it in Model Registry, package a pinned image and serve from an isolated compute pool. Enforce endpoint identity/schema/rate limits, canary the version, observe quality/latency/GPU/cost and execute full-bundle rollback.

## Hands-on evidence labs

1. **Use-case contract:** Compare rules, AI Function, RAG, Analyst, agent and custom-model choices for three cases; document risk, success/abstention, identity, data and cost boundaries.
2. **AI SQL functions:** On synthetic text, use selected canonical `AI_*` functions with versioned prompts/schema, validate outputs and record failure, latency and consumption evidence.
3. **Search/RAG:** Parse approved documents, chunk/index with provenance, measure retrieval and grounded citations, then test absent answers, restricted access and indirect injection.
4. **Semantic/agent tool path:** Create or paper-design a semantic view and constrained agent/tools; validate generated query/tool arguments, authorization, approval and partial-failure recovery.
5. **Document pipeline:** Process clean, scanned, tabular, corrupt, duplicate and corrected synthetic documents; prove quarantine, quality comparison, lineage, idempotent replay and deletion.
6. **Registry lifecycle:** Log a harmless small model/version with signature, metrics, lineage, owner and intended use; compare a candidate to baseline and demonstrate alias/version rollback.
7. **Container service:** Build or paper-design a pinned image, repository, GPU/CPU compute pool and job/service contract; document grants/network, capacity, logs/metrics, vulnerability evidence and cleanup.
8. **Production evidence pack:** Assemble architecture/threat model, eval set/results by slice, grants/data flow, model/prompt/corpus/tool versions, dashboard/runbook, incident stop and rollback proof.

## Readiness checks

1. Can you distinguish deterministic, predictive, generative, RAG and agentic cases?
2. What is the permitted decision/action and failure consequence?
3. When is an AI SQL function narrower and safer than an agent?
4. When do Search and Analyst solve different grounding problems?
5. When does a custom open model justify its operational burden?
6. Which data, prompt, output and artifact assets need classification and grants?
7. How will you test prompt injection, disclosure and excessive agency?
8. What acceptance, abstention and human-review rules apply?
9. How are evaluation examples separated from tuning data?
10. Which retrieval, generation, tool and system measures matter?
11. How do canonical `AI_*` functions differ from legacy Cortex names?
12. What model/function/region/privilege/limit must be checked?
13. How will repeated AI SQL calls be versioned and bounded?
14. What makes an embedding/index migration compatible?
15. What belongs in a governed semantic view?
16. How are agent tools described, authorized, validated and recovered?
17. Why does MCP not make a remote tool trustworthy?
18. How do you prevent untrusted retrieved text from becoming instruction?
19. How do you reproduce a prompt/model/corpus/tool evaluation?
20. What makes an open model/license appropriate for the use case?
21. When should you use tuning instead of RAG or prompting?
22. What provenance and leakage checks apply to tuning data?
23. How do service and job-service lifecycles differ?
24. How do image repository, compute pool, service and registry relate?
25. What image/model supply-chain evidence is required?
26. How do you size and bound GPU capacity, concurrency and spend?
27. What belongs in a model registry version and promotion gate?
28. How do online and batch inference contracts differ?
29. Can you roll back the complete model/tokenizer/prompt/image/config bundle?
30. What belongs in a document source and version contract?
31. When do layout, OCR, extraction and multimodal completion differ?
32. Why should new pipelines avoid legacy `PARSE_DOCUMENT`?
33. What state makes a document pipeline idempotent and replayable?
34. How do you propagate access and deletion into chunks and indexes?
35. How do page/section/table/image provenance improve evidence?
36. Can you diagnose an error at the parse, extract, retrieve or generation layer?
37. Which quality measures fit parsing, extraction and RAG?
38. What should trigger human review or quarantine?
39. Can you map all four public abilities to production evidence?
40. Have you reconciled this guide with the form-delivered official guide?

### Check key

- **Ready:** You can build, evaluate, secure, observe, fail and recover the design with versioned evidence.
- **Review:** You know the product name but cannot defend identity, data, evaluation, failure or cost behavior.
- **Gap:** You guessed or memorized an item. Return to current documentation and an authorized lab.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Use the official guide plus one practical route, then select current documentation, labs or a course for gaps. Durations, access and revision details were checked September 2, 2026 and can change.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [GES-C02 certification page and guide request](https://learn.snowflake.com/en/certifications/snowpro-GenAI-C02/) | Public; guide form | 20–40m | Canonical active identity, four abilities, candidate profile and detailed-guide request. Reconcile the received guide. |
| [SnowPro program policies](https://learn.snowflake.com/en/pages/snowpro-policies/) | Public | 30–60m | Current validity, scoring, renewal, retake and accommodation policy; verify at registration. |
| [Official SnowPro Practice Exams](https://learn.snowflake.com/en/certifications/snowpro-practice-exams/) | Paid, portal | One timed attempt + 3–5h review | Gen AI practice is listed in English and follows the live specification/weighting. Checked policy allows one attempt within 24 hours. |
| [Snowflake GenAI Training](https://learn.snowflake.com/en/courses/ILT-GENAI) | Paid instructor-led | 16h + 20–35h labs | First-party two-day lectures, demos, labs and discussion across governed AI capabilities. Confirm GES-C02 alignment and schedule. |
| [Cortex AI Functions documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions) | Public | 8–15h selective + 15–25h labs | Canonical function, model, privilege, availability, cost and limitation reference; highly volatile. |
| [Cortex Agents documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents) | Public | 8–15h + 15–25h labs | Current Analyst/Search/tool/MCP orchestration, identity, governance and monitoring path. Follow linked getting-started material. |
| [Snowpark Container Services documentation](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview) | Public | 12–20h + 20–40h labs | Current image, compute-pool, service/job, networking, observability and cost foundation for custom models. |
| [Model Registry and inference documentation](https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview) | Public | 8–15h + 15–30h labs | Model/version/signature/metrics/lineage and deployment foundation. Verify current supported frameworks/serving behavior. |
| [Cortex AI document functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-documents) | Public | 6–12h + 12–25h labs | Current parse, extract and completion choices plus linked limits, regions, privileges and consumption. |
| [Udemy — Training for Snowflake Cortex Masterclass Hands-On](https://www.udemy.com/course/snowflake-cortex/) | Paid | 20h34m + 20–35h labs | Broad intermediate Cortex/Snowpark/ML foundation, updated May 2026. Close Agents, current AI function and document-pipeline deltas officially. |
| [Udemy — Snowflake Cortex AI: Cortex Code, Search & Agents](https://www.udemy.com/course/snowflake-cortex-ai-cortex-code-coco-course/) | Paid | 5h21m + 12–20h labs | August 2026 practical route across current AI Functions, RAG, semantic views and agents; still verify every fast-moving interface. |

Avoid products that promise real/current questions, exact live-exam simulation or guaranteed passing. Ethical practice uses original scenarios and teaches why a design works; verify every technical rationale against current documentation.
