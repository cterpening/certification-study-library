---
title: OpenAI AI Foundations certification reference and learning map
description: A provisional, partner-oriented OpenAI learning map based on public first-party documentation, not an inferred exam blueprint.
---

# OpenAI AI Foundations certification reference and learning map

> **Status:** Provisional public-source reference, checked September 1, 2026.
> This is **not** a blueprint-mapped exam guide. OpenAI has announced certificate
> courses, but this review did not find a stable public AI Foundations objective
> list, weighting, exam-delivery page, practice assessment, or renewal contract.

This page gives partner learners something useful now without presenting an
independent curriculum as official exam scope. Its learning map uses current
first-party OpenAI documentation. If your employer or partner organization gives
you authorized course objectives, use those objectives as the source of truth
and treat this page as preparation and technical context.

## Public certification contract

| Contract element | Public status on September 1, 2026 | How to use it |
|---|---|---|
| Program announcement | Announced publicly | Confirms program direction, not detailed assessment scope. |
| Stable exam or assessment code | Not found | Do not invent a code for catalogs, scripts, or résumés. |
| Published objective list and weights | Not found | The learning areas below are editorial, not official domains. |
| Candidate profile or prerequisites | Not found in a stable public contract | Partner instructions override this page. |
| Delivery, duration, score, price, languages | Not found in a stable public contract | Verify in the authorized enrollment experience. |
| Public practice assessment | Not found | Use the evidence checks below as formative practice only. |
| Expiration or renewal rules | Not found | Do not claim that the certificate expires or remains permanent. |

**Promotion rule:** convert this reference into a regular certification guide
only after OpenAI publishes a durable assessment page with a named credential,
scope or objectives, and enough delivery/lifecycle information to monitor. Keep
the old dated reference in history so readers can see what changed.

## Who this learning map is for

The map supports a partner audience that needs to explain, demonstrate, govern,
or implement OpenAI capabilities. It intentionally spans three viewpoints:

- a business practitioner who uses ChatGPT and must judge outputs responsibly;
- a solution practitioner who maps a customer outcome to models, data, tools,
  evaluation, and controls; and
- a developer who can implement a small, testable Responses API workflow.

An introductory certificate may assess less technical depth. The extra depth is
useful partner context, not a claim about exam difficulty. Start with the first
four areas and add the developer and production areas when they match your role.

> **About related items:** A **Related item** is useful context that clarifies a
> decision or connects the topic to real delivery, but has not been verified as
> certification scope. Related items are included to deepen understanding, not
> to predict questions.

## Independent learning map

### 1. Generative AI and responsible use

Be able to explain that a language model generates outputs from patterns in its
inputs and learned representation; it is not a database of guaranteed facts or
an accountable decision maker. Distinguish useful fluency from factuality. A
good workflow gives the model relevant context, asks for an inspectable result,
and lets a person or deterministic system own consequential decisions.

Know the practical risk categories: inaccurate or unsupported content, harmful
content, bias, privacy leakage, prompt injection, excessive agency, insecure
tool use, and overreliance. Controls should follow the data and action path:
minimize inputs, authorize access, constrain tools, validate structured results,
moderate when appropriate, require approval for consequential actions, log
evidence, and test misuse cases. OpenAI's public safety guidance recommends
moderation, adversarial testing, human review in high-stakes uses, constrained
inputs/outputs, and mechanisms for users to report problems.

**Related item — risk versus capability:** blocking every open-ended response
can destroy the value of an assistant, while unrestricted tools can create
unacceptable impact. Design controls from the task's consequence, data
sensitivity, reversibility, and user population rather than from a generic
"AI-safe" label.

### 2. Effective ChatGPT use and prompting

A useful prompt communicates the outcome, context, relevant source material,
constraints, audience, and success criteria. Treat prompting as iterative work:
inspect the answer, identify the failure, improve the instruction or evidence,
and rerun a representative task. Examples help when they encode a real pattern,
but many examples can also make a prompt brittle or expensive.

Separate instructions from untrusted content. A document, webpage, or retrieved
passage can contain text that looks like an instruction; it must not silently
override the application's rules. Ask for citations or evidence when claims
need grounding, then check whether the cited material actually supports the
claim. A confident answer is not verification.

In ChatGPT, understand the difference between a conversation instruction,
uploaded or connected source material, and the model's generated response.
Product features and names change frequently, so learn the purpose of the
capability rather than memorizing a transient menu location.

**Related item — prompt versus product control:** a prompt expresses desired
behavior. Authentication, authorization, retention, allowed tools, schemas,
approvals, and monitoring are application or platform controls. Do not ask a
prompt to enforce a security boundary that the surrounding system can enforce.

### 3. Models, inputs, outputs, and the Responses API

Choose a model through measured requirements: supported modalities and tools,
quality on representative cases, latency, throughput, context needs, cost, and
deployment constraints. A newer or larger model is not automatically the best
production choice. Pin or record versions when reproducibility matters and
rerun evaluations before migrations.

For new API applications, understand the Responses API request-and-result
shape. Instructions influence the response; input can contain text, images, or
files when supported; output is a sequence of typed items, not necessarily one
plain assistant string. Use the SDK's output helper only when a text-only result
is truly expected. Understand conversation state versus explicitly resending
context, and decide whether response storage is acceptable for the workload.

Use Structured Outputs when downstream software needs a schema. A valid JSON
string is weaker than a schema-conforming business result, and schema validity
still does not prove that field values are factually correct. Validate values,
permissions, and business invariants in application code.

**Related item — reliability layers:** transport success, schema validity,
semantic correctness, authorization, and business acceptance are separate
checks. A `200` response with valid JSON can still be wrong or unsafe.

### 4. Grounding, retrieval, and tool use

Grounding supplies relevant evidence at run time. File search can retrieve from
managed vector stores; web search can obtain current public information; custom
function tools connect the model to an application's controlled capabilities.
Retrieval should respect identity and source permissions, return enough
provenance for verification, and be evaluated for both retrieval quality and
answer quality.

Function calling is a loop, not magic execution: define a tool and schema, let
the model request it, validate and authorize the arguments, execute trusted
application code, return the result, and let the model produce or request the
next output. Use strict schemas where supported. Keep tool descriptions clear,
limit the tools available for each step, treat tool output as untrusted input,
and make side effects idempotent or explicitly approved.

Know when not to use a tool. If the answer is already in supplied context, a
network call adds cost and failure modes. If an action is irreversible or
high-impact, require policy checks and human confirmation outside the model.

**Related item — retrieval is not training:** adding files to retrieval changes
the context available to a request; it does not retrain the base model. Model
customization, retrieval, prompt changes, and deterministic application logic
solve different problems.

### 5. Agents and workflow design

An agent combines a model with instructions, tools, state, and a run loop to
pursue an outcome. Start with the smallest workflow that works. A deterministic
sequence is easier to reason about than open-ended autonomy; add model-directed
routing only when the task genuinely requires it.

Define the agent's authority: what it may read, what it may propose, what it may
change, and what needs approval. Bound iterations, time, cost, and tool calls.
Preserve traceable inputs, tool requests, results, handoffs, and final outputs.
Guardrails can check inputs or outputs, but they do not replace authorization or
secure tool implementation.

Multi-agent designs are justified when roles need different context, tools, or
independent work. They add handoff ambiguity, duplicated work, latency, and
observability needs. Prefer a single agent or deterministic orchestration until
evaluation evidence shows a benefit.

**Related item — human in the loop:** human approval is a designed state in the
workflow, not a vague instruction to "be careful." Specify what evidence the
reviewer sees, what choices they can make, what expires, and how rejection or
timeout is handled.

### 6. Evaluation and improvement

Define success before optimizing. Build a dataset of representative normal,
edge, and adversarial cases; retain expected qualities or reference outputs;
and use graders appropriate to the task. Exact match can test a fixed code,
schema checks can test structure, rubric or model graders can help with nuanced
quality, and human review remains important for consequential or subjective
outcomes.

Evaluate the complete workflow, not only the final prose. For a grounded agent,
inspect retrieval relevance, citations, tool selection, tool arguments,
handoffs, approvals, latency, token usage, and final correctness. Track false
acceptance as well as false rejection. Re-run the same regression set after
model, prompt, tool, policy, or knowledge changes.

The public agent-evaluation guidance distinguishes reproducible evaluation from
manual inspection and supports trace-based grading. Partners should be able to
explain not just that a demo worked, but what evidence shows it will keep
working across representative customer cases.

**Related item — production feedback:** user ratings are signals, not ground
truth. Segment feedback, investigate failures, protect privacy, and turn useful
cases into reviewed regression tests.

### 7. Security, data, and production operations

Protect API keys and service credentials on the server; never embed them in
client code or public repositories. Separate projects and service identities by
environment or workload, grant least privilege, rotate credentials, and monitor
usage. Apply rate, spend, timeout, retry, and concurrency controls. Retries need
backoff and must not repeat unsafe side effects.

Read the current data-control documentation for the exact endpoint, feature,
account type, region, and retention requirement. Do not generalize one feature's
data behavior to all OpenAI products. Minimize sensitive data, define legal and
organizational approval, and document subprocessors or residency requirements
where they matter.

Production readiness includes observable request identifiers and traces,
versioned prompts/configuration, tested fallbacks, error classification,
capacity and cost monitoring, incident ownership, and a rollback plan. Current
model aliases, quotas, pricing, limits, and feature maturity are volatile facts;
verify them at implementation time rather than memorizing this page.

**Related item — shared responsibility:** OpenAI secures and operates its
services; the customer and partner remain responsible for application identity,
data selection, tool authorization, business logic, user experience, monitoring,
and appropriate use.

## Integrated partner scenarios

### Scenario A: grounded support assistant

A customer wants an assistant over approved product manuals. Define authorized
sources and document owners, ingest only current material, preserve citations,
and create evaluation cases for correct answers, missing answers, conflicting
versions, and prompt injection inside documents. The assistant may draft an
answer but must not change an entitlement or issue a refund. Measure retrieval,
support accuracy, abstention, citation support, latency, and escalations.

### Scenario B: controlled order-change agent

The agent can retrieve an order and propose a change. Use separate read and
write tools, authorize both against the signed-in user, validate schemas and
business limits, show the proposed side effect, require confirmation, attach an
idempotency key, log the result, and handle partial failure. A natural-language
promise that the agent will ask first is not the approval control.

### Scenario C: partner discovery workshop

Turn "we need an AI chatbot" into an evidence plan. Identify users, outcome,
source data, actions, risk, integration, latency, volume, quality threshold,
operating owner, and economics. Build a thin vertical slice and an evaluation
set before committing to a large architecture. Present measured gaps and a
controlled next stage instead of treating an impressive conversation as proof.

## Hands-on evidence plan

Complete the activities that match your role. A partner learner should retain
the artifact and be able to explain its tradeoffs.

1. **Prompt comparison (45–75 minutes):** run five representative tasks with a
   baseline and improved prompt. Record the success criteria and failure types.
2. **Grounded answer (60–120 minutes):** use an approved small document set,
   require citations, and test relevant, irrelevant, missing, and malicious
   passages.
3. **Structured result (45–90 minutes):** return a schema-conforming business
   object; separately test schema validation and business-rule validation.
4. **Read-only function tool (60–120 minutes):** implement and validate a tool
   call, including malformed and unauthorized arguments.
5. **Approved side effect (90–180 minutes):** add explicit confirmation,
   idempotency, audit evidence, rejection, timeout, and retry behavior.
6. **Agent trace review (60–120 minutes):** inspect a successful and failed run,
   identifying state, tool choices, results, and the earliest bad decision.
7. **Evaluation set (90–180 minutes):** create at least 20 normal, edge, and
   adversarial cases and report pass rate by failure category.
8. **Production review (60–120 minutes):** create a one-page threat, data,
   capacity, cost, monitoring, incident, and rollback checklist.

## Readiness checks

You should be able to answer these without relying on product-menu memory:

1. Why can a fluent answer still be wrong?
2. Which facts should be grounded or independently verified?
3. What makes a prompt clear without turning it into a security control?
4. How do model capability, quality, latency, cost, and data constraints affect selection?
5. Why is a Response made of typed output items rather than guaranteed plain text?
6. When should Structured Outputs be used, and what do they not validate?
7. How is retrieval different from model training or customization?
8. What is the complete function-calling loop?
9. Where are tool arguments authorized and validated?
10. How do you prevent duplicate side effects after a retry?
11. When is deterministic orchestration preferable to an agent?
12. What authority, iteration, time, and cost boundaries should an agent have?
13. What evidence must accompany a human approval?
14. Why can a multi-agent design reduce reliability?
15. What belongs in a representative evaluation set?
16. Which parts of a grounded tool-using workflow need separate evaluation?
17. Why are user ratings insufficient as a quality measure?
18. How should secrets and service identities be isolated?
19. Which data-control facts must be checked for the exact product and endpoint?
20. What observability and rollback evidence is needed before production?
21. Which responsibilities remain with the customer and implementation partner?
22. Which facts on this page are volatile and must be checked again?
23. What public evidence is still missing from the certification contract?
24. What event would justify promoting this page into a normal exam guide?

## Places to learn

This is **not a complete list**, and it is not meant to be consumed end to end.
Pick the format and depth that fit your role, then use hands-on evidence and
evaluation results to close the gaps. Times are planning estimates for selected
reading and practice, not vendor promises.

| Resource | Access | Estimated time |
|---|---|---:|
| [OpenAI certificate-course announcement](https://openai.com/index/openai-certificate-courses/) | Public; program-level context | 10–20 min |
| [ChatGPT prompting](https://learn.chatgpt.com/docs/prompting) | Public | 30–60 min plus practice |
| [OpenAI developer quickstart](https://developers.openai.com/api/docs/quickstart) | Public; API account/usage may be needed for labs | 45–90 min |
| [Text generation and Responses API](https://developers.openai.com/api/docs/guides/text) | Public | 45–90 min |
| [Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Public | 60–120 min plus lab |
| [Function calling](https://developers.openai.com/api/docs/guides/function-calling) | Public | 90–180 min plus lab |
| [File search](https://developers.openai.com/api/docs/guides/tools-file-search) | Public | 60–120 min plus lab |
| [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) | Public | 60–120 min plus dataset work |
| [Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices) | Public | 30–60 min plus threat review |
| [Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data) | Public | 45–90 min; verify current workload details |
| Authorized OpenAI partner or employer learning | Partner/employer restricted when offered | Verify course and assessment schedule in the authorized portal |

## Maintenance triggers

Check this page weekly for the following changes:

- a public AI Foundations credential or assessment page;
- a stable objective list, candidate profile, or assessment guide;
- delivery, duration, scoring, language, price, expiration, or renewal details;
- a public practice assessment or official preparation path;
- renamed or deprecated core APIs and agent/evaluation guidance; and
- data-control, safety, or production guidance that changes the learning map.

Until the first four contract items appear, keep this page outside the generated
exam catalog and `CERTIFICATIONS.txt`. That machine-readable boundary prevents a
downstream script from treating an announced course as a fully specified exam.

