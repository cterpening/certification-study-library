---
exam_code: SALESFORCE-AGENTFORCE-SPECIALIST
vendor_id: salesforce
official_blueprint: https://help.salesforce.com/s/articleView?id=005298924&language=en_US&type=1
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Salesforce Certified Agentforce Specialist Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The official Spring ’26 guide, credential page, current Trailhead learning and maintenance material, product-change context, learning resources, links, and integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#salesforce-agentforce-specialist-coverage-record).

**Current baseline:** Prompt Engineering 20%, Data 360 Fundamentals 20%, AI Agents 35%, Testing, Deployment, and Maintenance 10%, Governance and Observability 10%, and Multi-Agent Orchestration 5%. Older material organized around five domains or using the retired AI Specialist outline is not a current blueprint.<br>
**Exam contract:** The official Spring ’26 guide lists 60 scored multiple-choice questions, up to five unscored questions, 105 minutes, 72% passing, USD 200 registration, USD 100 retake, and no formal prerequisite. Verify taxes, delivery, accommodations, languages, version, and checkout details for your region.<br>
**Experience target:** Salesforce describes a candidate with about one year configuring Salesforce and standard objects, including Data 360, plus hands-on experience with Agent Builder, Prompt Builder, Testing Center, and sandbox-to-production deployment. Platform Administrator and Platform App Builder are related credentials, not published prerequisites.<br>
**Upcoming change:** No retirement or dated blueprint replacement was found September 2, 2026. Agentforce itself changes as often as weekly, so a product release can postdate the Spring ’26 exam baseline without changing the tested objectives.<br>
**Maintenance:** If you earned the certification on or before August 24, 2026, Salesforce requires the free Agentforce Specialist Maintenance (Summer ’26) badge by August 20, 2027. Later earners should verify their own credential account and the current maintenance schedule.<br>
**Terminology watch:** Salesforce announced that beginning in April 2026, agent topics are called **subagents** in newer product experiences. Current exam and learning pages can contain both terms. Recognize the mapping; do not assume every older screenshot matches the current builder.

## How to use this guide

Build one bounded agent use case through the entire lifecycle: intended user and outcome → trusted data and retrieval → prompt and agent behavior → least-privilege actions → repeatable tests → controlled deployment → trace, quality, safety, cost, and business monitoring. For each decision, explain what the agent may know, decide, and change; how uncertainty or denial is handled; and which evidence proves acceptable behavior.

Use an authorized Agentforce-enabled Developer Edition, Trailhead-provisioned playground, or sandbox with synthetic data. Product availability depends on licenses and org configuration. Never put customer secrets, personal data, or production credentials into a practice environment. The scenarios and checks here are original; do not use dumps, recalled live questions, copied superbadge solutions, or products marketed as “actual questions.”

> **About related items:** A `Related item:` callout adds prerequisite, architectural, security, release, or operational context. It helps connect the blueprint to responsible implementation but does not assert that Salesforce uses that wording in the public exam guide.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Prompt Engineering | 20% | Versioned prompt templates, grounding/access decision, adversarial tests, and activation evidence |
| Data 360 Fundamentals | 20% | Governed data-library, chunking, index, retriever, citation, and access evaluation |
| AI Agents | 35% | Agent/subagent and action contract, deterministic controls, channel/security tests, and API boundary |
| Testing, Deployment, and Maintenance | 10% | Evaluation suite, dependency-aware promotion, smoke tests, monitoring, rollback, and ownership |
| Governance and Observability | 10% | Policy, trace/metric dashboard, thresholds, incident path, optimization decision, and audit evidence |
| Multi-Agent Orchestration | 5% | SOMA boundary and secured MCP/A2A interaction contract |

## 1. Prompt Engineering — 20%

Use Prompt Builder when a repeatable business task needs controlled instructions, Salesforce context, reusable inputs, versioning, activation, permissions, and operational use. A casual one-off user request does not automatically need a template. Start with an explicit task, audience, allowed facts, response format, refusal/handoff rule, quality criteria, and examples only where they improve consistency.

Select the template type from the invocation contract. Field generation writes or proposes content for a supported record field; flex templates support more adaptable input/output use cases. Other available types and model choices are release- and license-sensitive. Confirm where the output appears, who invokes it, what data resolves, whether a human reviews it, and whether any later automation treats it as trusted.

Grounding supplies relevant business context rather than relying only on model knowledge. Possible techniques include merge fields, related records, Flow or Apex-supplied context, and trusted retrieved content. Grounding does not guarantee correctness: stale, conflicting, overshared, poisoned, or weakly retrieved context can produce a confidently wrong answer. Preserve provenance and test missing, denied, conflicting, multilingual, and malicious content.

Create a template as a lifecycle artifact: define inputs and least-privilege access, write bounded instructions, preview with representative records, inspect the resolved prompt and response where authorized, refine, version, activate, place it in the intended surface, and verify as both allowed and denied users. Separate Prompt Template Manager-style configuration rights from user execution rights. A template that works for an administrator may reveal a permission or data-path defect for the real persona.

The Einstein Trust Layer provides Salesforce controls around model interaction, including supported secure data handling and governance features. Describe the exact configured control and verify current documentation; do not turn “trust layer” into a blanket claim that every data, prompt-injection, model, retention, output, or downstream-action risk disappears. Model access and selection must be intentionally governed. Avoid secrets in prompts, minimize sensitive context, validate output, and keep authorization on the server-side action boundary.

`Related item:` Prompt injection can arrive through a user message or grounded document. Treat retrieved text as data, not authority. Instructions from an untrusted source must not expand permissions, reveal hidden context, select a more powerful tool, or bypass confirmation.

## 2. Data 360 Fundamentals — 20%

An Agentforce Data Library connects an agent to governed knowledge. Before selecting a source, define the question set, owners, system of record, audience, freshness, deletion, classification, language, citation, and failure behavior. Ingesting more documents can reduce quality if authoritative and obsolete content compete or if access metadata is lost.

Chunking divides source content into retrievable units. Chunks that are too small lose surrounding meaning; chunks that are too large dilute relevance and consume context. Headers, sections, tables, metadata, overlap, and document boundaries influence whether a returned unit answers the question. Choose a strategy using real content structure, then evaluate rather than memorizing one universal size.

Indexing turns supported content into a searchable representation. A retriever uses the index and query/context to select useful passages for grounding. Keep the pipeline distinct: source → parsing/chunking → index → retriever/query → ranked results → grounded prompt → answer/citation. When an answer is wrong, inspect each stage instead of immediately rewriting the prompt.

Evaluate retrieval with an approved test set containing answerable, unanswerable, ambiguous, stale, access-denied, paraphrased, multilingual, and adversarial questions. Measure whether authoritative passages appear near the top, whether forbidden content stays absent, whether citations support the claim, and whether the agent refuses or hands off when evidence is insufficient. Record index/retriever versions so results can be reproduced.

Data access must remain consistent across the source, index, retrieval, prompt, agent identity, channel, and action. A correct answer returned to an unauthorized user is a serious failure. Test record/object/field and knowledge visibility with real representative personas, not only an administrator.

`Related item:` Data lineage connects an answer to source, version, transformation, index, retrieval event, prompt, model response, and action. It makes quality, privacy, deletion, incident response, and audit questions answerable.

## 3. AI Agents — 35%

An agent combines an identity and purpose with allowed subagents/topics, instructions, actions, variables, reasoning behavior, data, channels, and guardrails. The reasoning system interprets the request, selects an eligible area of work, plans or follows configured logic, invokes permitted actions, evaluates results, and responds or hands off. Do not confuse fluent reasoning text with authorization or proof.

Use standard subagents/topics and actions when their supported contract matches; create custom ones when the business boundary or capability differs. Write narrow classification descriptions, explicit scope and instructions, typed action inputs/outputs, safe errors, and stop/handoff behavior. An action can read, calculate, update, invoke Flow or Apex, or call an approved integration depending on configuration. Each side effect needs server-side authorization, input validation, duplicate/replay handling, timeouts, failure semantics, audit evidence, and sometimes human confirmation.

The new builder supports Agent Script in Canvas and Script View and hybrid reasoning. Use deterministic controls—filters, variables, template expressions, programmatic instructions, and explicit transitions—when policy or sequence must not be left to probabilistic selection. Use reasoning where language and context require flexibility. A good hybrid design reserves hard eligibility, money movement, identity, compliance, and irreversible changes for enforceable controls.

Employee agents assist authenticated workers; service agents serve customer-service interactions and may operate through externally facing channels. The correct type follows the user, identity, channel, data, action, escalation, session, and licensing requirement—not the most familiar template. Channels such as a digital experience, email, voice, or Slack add distinct identity, latency, formatting, disclosure, consent, session, and handoff concerns. Test the deployed channel, not only Builder preview.

Execution context determines what the agent and its actions can access. Map the human user, agent user, integration principal, Flow/Apex context, permission sets, sharing, and external credentials. Enforce least privilege at every capability boundary. Never assume that hiding an action from instructions prevents invocation or that client-side channel controls provide authorization.

The Agent API supports programmatic interaction with supported agents. Define authentication, authorization, session/conversation correlation, input/output schema, rate and timeout behavior, retries, idempotency, content handling, logging/redaction, error translation, and version compatibility. Keep an API consumer from expanding what the configured agent may do.

`Related item:` A high-impact action should use a two-phase pattern: prepare a clear proposal, re-check identity/authorization/current state, obtain required human approval, then commit once with an idempotency key and audit record.

## 4. Testing, Deployment, and Maintenance — 10%

Testing Center supports scaled agent evaluations using test cases and expected behavior. A useful suite covers subagent/topic selection, action choice and parameters, grounded-answer quality, refusal, escalation, safety, access denial, channel behavior, latency, and side effects. Test generation can broaden coverage but is not an oracle; review synthetic cases for realistic inputs, protected data, expected outputs, and accidental production changes.

Separate evaluation layers. Unit-style checks validate prompts, instructions, actions, retrievers, and deterministic expressions. Conversation tests validate multi-turn state and ambiguity. Integration tests validate identities, data, Flow/Apex, APIs, and channels. Adversarial tests probe prompt injection, data exfiltration, tool misuse, unauthorized actions, toxicity, and malformed inputs. User acceptance tests prove the business journey and handoff. Regression suites compare a candidate version with an accepted baseline.

Promote agents from sandbox to production with their complete dependencies: agent metadata, versions, subagents/topics, actions, prompt templates, Flow/Apex and tests, permissions, data/index/retriever configuration, channel settings, external credentials, and operational dashboards. Validate target-org licenses and configuration. Use a deployment manifest, owner/approver, preflight, test evidence, post-deploy smoke journeys, monitoring window, and rollback/deactivation decision.

Maintenance is both credential and system work. Complete the assigned Trailhead maintenance badge by its deadline. Separately, review product releases, model changes, data/index freshness, prompt/agent versions, permissions, action dependencies, tests, metrics, cost, incidents, and user feedback on a defined schedule. A badge does not maintain a production agent for you.

`Related item:` Rollback may mean restoring metadata, activating a prior prompt/agent version, disabling a channel/action, reverting a data/index change, rotating a credential, or routing to humans. Rehearse the appropriate controls before launch.

## 5. Governance and Observability — 10%

Governance starts with an approved use case, accountable business and technical owners, affected people, risk classification, data and action boundaries, success/failure criteria, human oversight, legal/policy review, and an exit plan. Inventory every deployed agent, version, channel, data source, model/configuration, action, integration, owner, and approval. Require stronger evidence as consequence and autonomy increase.

Observe the full path: request/channel/session → identity and access → selected subagent/topic → reasoning/plan and deterministic branch → retrieval sources → action inputs/results → response/handoff → user and business outcome. Redact or minimize sensitive logs while retaining enough correlation for diagnosis and audit. Define retention and access for prompts, traces, feedback, and derived analytics.

Monitor adoption, containment or completion, escalation, groundedness/quality, incorrect or unsupported response rate, action success/error/duplicate rate, safety/access violations, latency, token or credit consumption, user feedback, and business outcomes. A rising containment rate is not automatically success if customers abandon, repeat requests, or receive unsafe resolutions. Set thresholds, owners, alert paths, sampling/review cadence, and controlled optimization experiments.

Optimization should follow evidence: segment failures, reproduce them, locate the failing layer, change one bounded artifact, run regression/adversarial tests, compare quality/safety/cost, approve, deploy, and watch. Prompt wording cannot repair missing permissions, bad content, a weak retriever, an unsafe action, or a broken process.

`Related item:` An agent incident runbook should support containment, evidence preservation, affected-session and data/action scoping, credential or action disablement, human routing, correction, replay/compensation where safe, stakeholder notification, and lessons learned.

## 6. Multi-Agent Orchestration — 5%

Use a single bounded agent when one identity, context, policy boundary, and action set can satisfy the task. Consider Salesforce Orchestration and Multi-Agent architecture (SOMA) when specialized agents need coordinated delegation, independent ownership or scaling, and explicit control over how work moves among them. Additional agents add routing, state, identity, failure, latency, cost, observability, and governance complexity; decomposition must earn that cost.

Define the orchestrator’s authority, each specialist’s purpose and allowed capabilities, delegation criteria, shared versus isolated context, data minimization, maximum hops/time/cost, loop prevention, partial-failure behavior, human escalation, and end-to-end correlation. Preserve the initiating user’s intent and authorization; a handoff must never amplify privilege.

Model Context Protocol (MCP) standardizes how an AI application can discover and use exposed context, resources, or tools. Agent2Agent (A2A) supports interaction and task collaboration between agents. Know their purposes without treating interoperability as trust. Authenticate peers/servers, authorize every tool and resource, validate schemas and content, constrain egress, protect secrets, pin or govern versions, handle timeouts/replay, and log delegation and results.

`Related item:` Apply zero trust to agent networks: verify explicitly, grant least privilege, assume messages and tool output may be compromised, and make policy enforcement independent of natural-language instructions.

## Integrated scenarios

### Scenario 1: Grounded employee policy agent

An authenticated employee asks HR-policy questions in Slack. Define authoritative documents, classification and access metadata, chunk/index/retriever evaluation, prompt format and citations, employee-agent identity, denied and ambiguous behavior, injection-resistant grounding, Slack session/disclosure needs, Testing Center suite, trace/quality dashboard, content-owner refresh, and human escalation.

### Scenario 2: Service agent with a controlled refund action

A customer uses a digital channel to ask about an order and request a refund. Define service-agent scope, identity verification, grounded policy, standard/custom subagent and action choices, deterministic eligibility filters, typed action contract, current-state recheck, confirmation, idempotency, partial failure/compensation, least privilege, sandbox evaluation, channel smoke test, fraud/human handoff, audit evidence, and rollback kill switch.

### Scenario 3: Multi-agent case resolution

An orchestrator delegates product troubleshooting and account-entitlement work to specialized agents, then prepares a resolution. Justify SOMA over one agent; define ownership, MCP/A2A trust, shared context minimization, hop/loop limits, conflicting-result handling, correlated traces, action approval, latency/cost budget, safe partial degradation, adversarial tests, deployment order, and incident containment.

## Hands-on evidence labs

1. **Prompt-template lifecycle (75–120 min):** Build and version a field-generation or flex template; test grounding, access, missing context, adversarial text, format, activation, and denied persona.
2. **Data Library and retrieval (120–180 min):** Load synthetic governed documents, compare two chunk/retrieval choices, and score relevant, stale, forbidden, unanswerable, and injection-bearing cases with citations.
3. **Bounded agent/subagent (120–180 min):** Configure purpose, instructions, variables, one read-only action, refusal, and handoff; record selection and parameter evidence across paraphrases.
4. **Deterministic high-impact action (120–180 min):** Add filters or Agent Script controls, reauthorization, confirmation, idempotency, safe failure, and audit output to a synthetic state-changing action.
5. **Channel and API contract (90–150 min):** Exercise one authorized channel or mock Agent API client with identity, session, schema, timeout, retry, redaction, error, and version tests.
6. **Testing Center evaluation (90–150 min):** Create reviewed cases across happy, denied, ambiguous, multi-turn, injection, tool-failure, unsafe, and escalation paths; preserve baseline and candidate results.
7. **Deployment and observability (120–180 min):** Produce a dependency manifest, promote safely, run smoke journeys, inspect correlated traces/metrics, trigger one threshold, and rehearse deactivation/rollback.
8. **Multi-agent tabletop (75–120 min):** Model an orchestrator plus two specialists, MCP/A2A boundaries, privilege propagation, loop and partial failure; test whether a simpler single-agent design is safer.

## Readiness checks

1. When is Prompt Builder more appropriate than a one-off prompt?
2. How do field-generation and flex template contracts differ?
3. Which access controls separate prompt management from execution?
4. What evidence belongs in create, preview, version, activate, and invoke stages?
5. Which grounding technique fits each data source and invocation path?
6. Why can grounded output still be wrong or unsafe?
7. Which prompt practices improve bounded, testable responses?
8. What does the Trust Layer address, and what remains your responsibility?
9. How do you govern specific model access and change?
10. How do direct and indirect prompt injection differ?
11. What belongs in an Agentforce Data Library source contract?
12. How do chunk size and document structure affect retrieval?
13. How are indexing and retrieval different stages?
14. Which tests show that a retriever is useful rather than merely returning text?
15. How do provenance, freshness, deletion, and access flow into grounded answers?
16. Which building blocks define an agent’s authority and behavior?
17. How do standard and custom subagents/topics and actions differ?
18. When should deterministic filters, variables, expressions, or Agent Script override flexible reasoning?
19. Which controls make a state-changing action safe and repeatable?
20. How do Employee and Service agents differ in identity and use?
21. What changes when an agent moves to email, voice, Slack, or a digital experience?
22. Which human, agent, Flow/Apex, and integration contexts participate in execution?
23. What must an Agent API client do about auth, sessions, retries, and output?
24. Why is Builder preview insufficient release evidence?
25. Which cases belong in a Testing Center evaluation set?
26. How do generated tests differ from reviewed expected behavior?
27. Which dependencies must move with an agent and prompt template?
28. How do smoke testing, monitoring, and rollback connect after promotion?
29. How does certification maintenance differ from production-system maintenance?
30. Which inventory facts establish accountable agent governance?
31. Which trace stages let you distinguish prompt, retrieval, action, and channel failure?
32. Which quality, safety, operational, cost, and business metrics belong together?
33. Why can high adoption or containment hide a poor outcome?
34. What triggers containment and which evidence must an incident preserve?
35. When does SOMA solve a real boundary or scaling problem?
36. Which costs and failure modes argue for one agent instead?
37. What purposes do MCP and A2A serve?
38. Why does protocol interoperability not establish trust or authorization?
39. How do the April 2026 subagent terminology and weekly release cadence affect study?
40. Which official pages will you recheck before scheduling and deployment?

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick resources that match your gaps and learning style. Favor current hands-on material; reconcile every course against the six-domain Spring ’26 outline and current product UI before investing substantial time.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official exam guide](https://help.salesforce.com/s/articleView?id=005298924&language=en_US&type=1) and [credential page](https://trailhead.salesforce.com/credentials/agentforcespecialist) | Public | 25–40 min | Authoritative six-domain scope, candidate boundary, contract, and official learning entry point |
| [Become an Agentblazer Legend 2026](https://trailhead.salesforce.com/content/learn/trails/become-an-agentblazer-legend-2026) | Free Trailhead; prior trail required | ~15 hr 28 min after prerequisites | Current advanced customization, Data 360, retrieval, testing, monitoring, Slack, DX, and API practice |
| [Agentforce Specialist Maintenance (Summer ’26)](https://trailhead.salesforce.com/content/learn/modules/agentforce-specialist-certification-maintenance-summer-26) | Free Trailhead | ~5 min | Current Agent Script/new Builder, Agentforce Grid, and Observability maintenance delta |
| [Agentforce for Service Specialist (AFS401)](https://trailheadacademy.salesforce.com/classes/afs401-agentforce-for-service-specialist---afs401) | Paid instructor-led | 3 days | Official guided build/test/deploy practice; service-focused, so supplement Data 360 and multi-agent breadth |
| [Agentforce Partner Pocket Guide](https://cloud.mail.salesforce.com/agentforcepartnerpocketguide) | Public landing page; some linked assets require Partner Community login | 2–4 hr selected; monthly additions | Partner-oriented release readiness, demos, implementation guidance, and current-change discovery—not an exam blueprint |
| [Practical Salesforce Agentforce Playbook](https://www.oreilly.com/library/view/practical-salesforce-agentforce/9781806389230/) | O’Reilly subscription/book | 7 hr 11 min listed / 298 pages | April 2026 end-to-end architecture, build, retrieval, security, testing, deployment, analytics, and operations |
| [Salesforce Certified Agentforce Specialist and Practice Test](https://www.udemy.com/course/agentforce/) by Mike Wheeler and team | Paid | 6 hr 11 min plus practice | July 2026 guided route including current MCP/multi-agent additions; identify retained retired-AI-Specialist lessons |
| [Focus on Force Agentforce resources](https://focusonforce.com/) | Paid | 12–20 hr selected plus original practice | Explanations and practice; verify that the purchased revision shows six domains rather than the older five-domain page copy |
| [Your COMPLETE Guide to the Salesforce Agentforce Specialist Certification Exam](https://www.youtube.com/watch?v=jbqQPedm_lk) by Salesforce Ben | Public | ~7 min | March 2026 credential orientation and study priorities; use official sources for exact objectives |
| [Agentforce release notes](https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein_platform.htm&language=en_US&release=262&type=5) | Public | 30–90 min selected | Distinguish current product changes from the Spring ’26 exam baseline and maintain implementation awareness |

Reject guaranteed-pass products, “actual question” files, VCE collections, unexplained answer banks, and courses advertising dumps. Quality practice explains why alternatives fail, identifies its blueprint version, and sends you back to first-party documentation and hands-on evidence.
