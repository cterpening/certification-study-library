---
title: Anthropic Claude Certified Architect, Foundations reference
description: A partner-oriented public learning map for Anthropic's partner-gated solution-architect certification.
---

# Anthropic Claude Certified Architect, Foundations reference

> **Status:** Provisional public-source reference, checked September 1, 2026.
> This is **not** a reconstruction of the partner exam. Anthropic publicly names
> the credential and candidate role, while its detailed training, objectives,
> exam, and enrollment experience remain in Anthropic Partner Academy.

Anthropic describes **Claude Certified Architect, Foundations** as its first
technical certification for solution architects building production
applications with Claude. It launched for members of the Claude Partner Network
in March 2026. A later public update says certification exams are earned through
Anthropic Partner Academy, certifications belong to individuals, and a current
certification contributes to a partner firm's Services Track standing.

That is enough to establish a real credential and audience, but not enough to
publish a conventional objective-mapped study guide. This page therefore gives
partner learners a public technical foundation and a clean place for an
authorized work mirror to map the private objectives.

## Public certification contract

| Contract element | Public status on September 1, 2026 | How to use it |
|---|---|---|
| Credential name | Claude Certified Architect, Foundations | Use the exact public name; confirm the current display name in Partner Academy. |
| Candidate role | Solution architects building production applications with Claude | Use this as the public learning audience, not a detailed domain list. |
| Access | Claude Partner Network / Anthropic Partner Academy | Partner login and organizational eligibility are required. |
| Program relevance | Individual certification contributes to partner-tier certified-practitioner counts | Firms should verify current-use and tier rules in Partner Hub. |
| Public weighted objectives | Not found | Do not infer weights or claim that the headings below are official. |
| Delivery, duration, score, price, languages | Not found in a stable public page | Verify in Partner Academy before scheduling. |
| Public sample questions or practice assessment | Not found | The checks below are original formative questions, not replicas. |
| Expiration and renewal | Public program language refers to a “current” or “active” certification, but detailed individual lifecycle terms were not found | Verify renewal and recency requirements in the authorized portal. |

**Integrity boundary:** never paste partner course text, objective wording,
screenshots, assessment questions, answer rationales, or portal-only metadata
into this public repository. An authorized downstream mirror may record an
objective-to-section crosswalk in a private overlay. It should link back to the
gated source, identify the access date, and avoid storing real exam questions.

> **About related items:** A **Related item** adds architectural context or a
> useful production connection but has not been verified as partner-exam scope.
> Related items deepen understanding; they are not predictions about questions.

## Independent solution-architect learning map

### 1. Requirements, risk, and architecture boundaries

Begin with the business outcome and operating constraint, not a model name.
Identify users, decisions, source data, output consumers, actions, expected
volume, latency, quality threshold, cost envelope, failure impact, and owner.
Separate an assistance workflow from an autonomous action. A production design
needs explicit authority, evidence, fallback, and escalation paths.

Choose the simplest reliable pattern. A single model call with strong context
may be enough; retrieval adds current or private knowledge; tools connect
controlled actions; a deterministic workflow chains known steps; an agent lets
the model choose steps dynamically. Anthropic's public agent guidance recommends
adding complexity only when measurement shows that simpler approaches fall
short, because agentic systems trade latency and cost for flexibility.

Threat-model the complete data and action path: identities, instructions,
untrusted content, retrieval, tools, tool results, generated outputs, logs, and
human decisions. Important risks include hallucination, prompt injection,
sensitive-data exposure, excessive agency, unauthorized tool calls, model or
dependency change, and overreliance. Define prevention, detection, response, and
recovery rather than treating a safety prompt as the entire control plane.

**Related item — build versus integrate:** custom development offers control,
while Claude products, managed features, cloud services, and partner frameworks
may reduce undifferentiated work. Compare feature maturity, identity, data,
networking, compliance, observability, portability, and operational ownership.

### 2. Access surface and deployment selection

Claude can be accessed through Anthropic's direct API and through supported
cloud platforms. The current public API overview distinguishes the direct
service from AWS, Google Cloud, and Microsoft Azure options and warns that
feature availability and timing vary. Select a surface through verified
requirements: organization standards, region, identity/IAM, billing, network,
compliance, support, model and feature availability, quotas, and team skills.

Do not assume API parity. Authentication, model identifiers, request envelopes,
streaming, tooling, quotas, logging, and new-feature timing can differ. Create a
capability matrix for the required features and validate a thin slice on the
selected platform. Isolate development, test, and production; use workspaces,
projects, accounts, or subscriptions appropriate to the platform.

For direct API access, understand API keys versus short-lived federated access,
required version headers, official SDK responsibilities, request IDs, errors,
rate limits, spend controls, and regions. Store credentials outside source code,
grant least privilege, rotate them, and make workload ownership visible.

**Related item — portability:** an abstraction can make basic message calls
portable, but the least-common denominator can hide valuable platform features.
Portability is an architectural decision with a tested cost, not an automatic
benefit of using a wrapper.

### 3. Messages, context, prompting, and outputs

Understand the Messages API as a sequence of typed content and conversational
roles with a system instruction outside the message list. Responses can contain
text, thinking-related blocks where supported, or tool-use blocks; stop reasons
help determine the next application action. Streaming changes delivery, not the
need to validate and safely assemble output.

Good prompting starts after success criteria exist. Give Claude a clear task,
relevant context, constraints, output needs, and representative examples where
they improve measured behavior. Anthropic recommends clear and direct
instructions and documents XML tags as one way to separate structured prompt
components. Keep trusted instructions distinct from untrusted retrieved data.

Manage context as a finite design resource. Place stable reusable material in a
cache-friendly order, count tokens before oversized requests, retrieve only
relevant evidence, summarize or compact with quality checks, and retain the
state required by the workflow. Prompt caching improves latency and economics
for repeated prefixes; it is not memory, authorization, or semantic caching.

Use structured outputs or strict tool schemas when downstream code needs a
contract. Schema conformance does not prove factual correctness, permission, or
business validity. Validate all three separately. Use citations when supported
and appropriate, then verify that the cited source entails the claim.

**Related item — model choice:** compare quality on the customer's evaluation
set, modality, context, tools, latency, throughput, cost, availability, and
change tolerance. Product-family labels and model versions are volatile; the
selection method is more durable than a memorized recommendation.

### 4. Knowledge, retrieval, tools, and MCP

Grounding retrieves or supplies evidence at run time; it does not retrain the
model. Design chunking, metadata, access filters, freshness, ranking, citations,
and no-answer behavior from the use case. Evaluate retrieval recall/precision
separately from final answer correctness so a plausible answer does not hide a
failed retriever.

Tool use is an application loop: define an understandable tool and input schema,
send it with the request, inspect Claude's tool-use block and stop reason,
authorize and validate inputs, execute trusted code, return a matching tool
result, and continue. The application owns the side effect. Use strict tool use
where it helps, clear descriptions, least-capability tools, bounded results,
timeouts, idempotency, and explicit approval for consequential actions.

MCP standardizes how compatible clients connect to tools and context, but does
not make an unknown server trustworthy. Review server provenance, authentication,
requested capabilities, data flow, result content, versioning, and operational
ownership. Treat remote content and tool output as untrusted even when delivered
through a standard protocol.

**Related item — agent-computer interface:** a model performs better when tools
make valid choices obvious and invalid choices difficult. Prefer explicit names,
purpose-built parameters, absolute identifiers, narrow actions, useful errors,
and examples over a broad shell-like interface.

### 5. Workflows, agents, and human control

Distinguish predefined workflows from agents that dynamically direct their own
process. Common composable workflows include prompt chaining, routing,
parallelization, orchestrator-workers, and evaluator-optimizer. Each pattern has
a reason to exist and an observable cost. Do not add multiple models or agents
merely because the architecture diagram looks advanced.

An agent needs a clear goal, tools, state, environmental feedback, stopping
conditions, and checkpoints. Bound total steps, time, tokens, cost, retries,
concurrency, and tool calls. Sandbox risky capabilities and expose only the
minimum tools and data needed for the current task. Capture traces that connect
instructions, messages, tool calls/results, handoffs, approvals, and outputs.

Human-in-the-loop control must be executable. Define when the run pauses, what
evidence is shown, who may approve, which exact action is authorized, how long
approval remains valid, and what rejection or timeout does. A generic system
instruction to “ask before dangerous actions” is helpful behavior guidance but
not the authorization boundary.

**Related item — multi-agent systems:** specialized agents can isolate context
and tools or parallelize independent work. They also introduce coordination,
duplicate-action, context-loss, inconsistent-policy, cost, and debugging risks.
Use evaluation evidence to justify the extra system.

### 6. Evaluation and lifecycle engineering

Define measurable success criteria before prompt tuning. Build representative
normal, edge, failure, and adversarial cases from the intended population.
Choose evaluation methods by property: deterministic assertions for schemas and
business invariants, reference comparisons where one answer is expected, rubric
or model graders for nuanced qualities, and human review for high-impact or
subjective decisions.

Evaluate the whole system. For a tool-using grounded workflow, measure source
selection, retrieval quality, citation support, tool choice, arguments,
authorization, side effects, final result, latency, token use, cost, and
escalation. Agent evaluation should inspect trajectories and end states because
two runs can reach similar text through very different—and differently risky—
paths.

Version prompts, tool schemas, knowledge, policies, model configuration, and
evaluation sets. Run regression gates before changing any of them. Canary or
stage releases, monitor segmented outcomes, retain rollback options, and turn
reviewed production failures into tests. User feedback is useful evidence but
is neither objective ground truth nor a substitute for incident review.

**Related item — evaluation economics:** a tiny clean dataset produces fast but
misleading confidence. Invest first in high-value boundary and failure cases,
then expand based on production risk and observed error categories.

### 7. Security, governance, reliability, and operations

Apply least privilege to users, service identities, workspaces, cloud roles,
data stores, MCP servers, and tools. Minimize data, classify it, define approved
uses, and verify the current commercial terms, privacy, retention, residency,
training-use, and logging behavior for the exact product and platform. Do not
transfer an assumption from Claude consumer products to an API or cloud-hosted
deployment.

Defend against direct and indirect prompt injection with layered controls:
instruction/data separation, authorized source selection, least-capability
tools, input/output validation, approval, isolation, monitoring, and adversarial
testing. Content filters and constitutional behavior are parts of a system, not
guarantees that arbitrary external content is safe to execute.

Engineer normal distributed-system behavior: timeouts, bounded retries with
backoff, circuit breaking, concurrency limits, graceful degradation, capacity
planning, request correlation, and idempotent writes. Track availability,
quality, safety, latency, tokens, cost, rate-limit pressure, tool failures, and
business outcomes. Define support ownership, incident severity, audit evidence,
customer communication, recovery, and post-incident improvement.

**Related item — partner responsibility:** Anthropic and a selected cloud
provider operate their respective service layers. The implementation partner
and customer still own requirement accuracy, identity and access, selected data,
tool code, application controls, integration, validation, monitoring, adoption,
and lawful use.

## Integrated partner scenarios

### Scenario A: regulated-policy assistant

The assistant answers from approved, versioned policy documents. Preserve
source identity and effective date, enforce document-level access, return
citations, abstain or escalate on missing/conflicting evidence, and create tests
for outdated content and injection inside documents. Measure retrieval,
entailment, refusal quality, latency, and reviewer overrides. It drafts guidance;
the authorized professional owns the regulated decision.

### Scenario B: service-request agent

Separate retrieval, proposal, and write tools. Authenticate the user, authorize
each resource and action, validate arguments and business rules, show the exact
change, require approval, use idempotency, and record tool evidence. Test an
expired approval, retry after timeout, partial external failure, malicious tool
result, and a user asking for another customer's record.

### Scenario C: cross-platform architecture decision

Compare direct Claude API, AWS, Google Cloud, and Microsoft Azure access only
for the features the customer requires. Record identity, region, network,
model/tool availability, quotas, observability, commercial ownership, support,
cost, portability, and team skills. Prove the uncertain items with a thin slice.
Keep the decision record dated because parity and platform names change.

## Hands-on evidence plan

1. **Requirements and threat model (60–120 minutes):** turn a proposed assistant
   into users, outcome, sources, actions, risks, controls, measures, and owners.
2. **Messages API thin slice (45–90 minutes):** make a request, handle content
   blocks and stop reasons, capture request IDs, and classify errors.
3. **Prompt evaluation (60–120 minutes):** compare a baseline and revised prompt
   over at least 20 representative cases; report failures by category.
4. **Grounded response (90–180 minutes):** implement citations and access-aware
   retrieval; test relevant, missing, conflicting, stale, and malicious sources.
5. **Controlled tool loop (90–180 minutes):** implement strict validation,
   authorization, approval, idempotency, timeout, and error handling.
6. **Workflow versus agent (90–150 minutes):** implement one task both ways and
   compare quality, steps, latency, cost, traceability, and failure recovery.
7. **Platform decision record (60–120 minutes):** compare the candidate access
   surfaces using verified requirements and mark volatile facts with dates.
8. **Production review (90–180 minutes):** create evaluation, release, capacity,
   cost, monitoring, incident, rollback, privacy, and shared-responsibility evidence.

## Readiness checks

1. What public facts establish the credential and its target role?
2. Which exam-contract details remain partner-only or unverified?
3. Why should an architect start with outcome and consequence rather than model?
4. When is one model call preferable to retrieval, a workflow, or an agent?
5. How do direct API and cloud-platform requirements affect selection?
6. Why must feature parity be verified rather than assumed?
7. What do API version headers, request IDs, rate limits, and spend limits do?
8. How are system instructions, message roles, content blocks, and stop reasons related?
9. What makes prompt caching different from memory and authorization?
10. What does schema conformance fail to prove?
11. How is retrieval different from model training?
12. How do you measure retrieval separately from answer quality?
13. What is the complete Claude tool-use loop?
14. Where are tool inputs authorized, validated, and executed?
15. Which MCP security questions remain the application's responsibility?
16. How do chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer differ?
17. What bounds make an agent operationally controllable?
18. What makes a human approval enforceable and auditable?
19. When does multi-agent complexity earn its cost?
20. What belongs in a representative evaluation set?
21. Why do agent trajectories matter as well as final outputs?
22. Which changes should trigger regression evaluation?
23. How do injection controls follow the full data and action path?
24. Which data-handling facts must be verified for the exact access surface?
25. How do idempotency, backoff, circuit breaking, and degradation differ?
26. Which service, partner, and customer responsibilities must be explicit?
27. What private partner material must stay out of this repository?
28. What new public evidence would justify a blueprint-mapped guide?

## Places to learn

This is **not a complete list**, and it is not meant to be consumed end to end.
Begin with Partner Academy if authorized, select public material for your gaps,
and spend more time producing evidence than collecting links. Times are planning
estimates, not vendor promises.

| Resource | Access | Estimated time |
|---|---|---:|
| Anthropic Partner Academy certification path and exam | Partner-restricted | Verify the current course and assessment schedule after sign-in |
| [Claude Partner Network launch and credential announcement](https://www.anthropic.com/news/claude-partner-network) | Public | 10–20 min |
| [Services Track and Partner Hub](https://www.anthropic.com/news/services-track-partner-hub) | Public | 15–30 min |
| [Anthropic learning resources and Academy](https://www.anthropic.com/learn) | Public catalog; some experiences require sign-in | 1–4 hr selected learning |
| [Claude API overview](https://platform.claude.com/docs/en/api/overview) | Public; account/usage may be required for labs | 45–90 min |
| [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-templates-and-variables) | Public | 60–120 min plus evaluation |
| [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | Public | 90–180 min plus lab |
| [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | Public | 45–90 min plus measurement |
| [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | Public | 60–120 min plus dataset work |
| [Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Public | 60–90 min plus architecture comparison |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Public | 60–90 min plus trace review |
| [Anthropic security and compliance](https://trust.anthropic.com/) | Public overview; some evidence may require request/sign-in | 30–90 min selected review |

## Maintenance triggers

Check weekly for a public credential page or exam guide; published objectives;
delivery, scoring, price, language, renewal, or practice details; additional
architect/developer/seller certifications; Partner Academy metadata changes;
platform availability changes; and material API, agent, evaluation, security, or
data-control changes.

Keep the page outside `config/exams.json` and `CERTIFICATIONS.txt` while the
blueprint remains gated. If public objectives appear, create a dated official
snapshot and adapter before promoting it. A private work mirror can add its
authorized objective crosswalk now without changing that public catalog rule.

