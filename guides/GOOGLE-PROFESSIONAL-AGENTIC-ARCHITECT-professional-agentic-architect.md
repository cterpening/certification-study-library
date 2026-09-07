---
exam_code: GOOGLE-PROFESSIONAL-AGENTIC-ARCHITECT
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/agentic-architect/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-06
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-06
---

# Google Cloud Professional Agentic Architect Beta Study Guide

> **Independent AI-assisted resource — BETA; SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 6, 2026. Registration is open, but the multiple-choice testing window has not started on that date. See the [coverage record](../docs/SOURCE-VALIDATION.md#google-professional-agentic-architect-coverage-record). The [official beta page](https://cloud.google.com/learn/certification/agentic-architect/), [exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf), and [beta FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en) are authoritative.

**Current baseline:** Published beta guide with five domains weighted approximately 13%, 17%, 33%, 22%, and 15%; registration open September 3–30, 2026<br>
**Scheduled change:** Multiple-choice testing runs September 8–30; results are expected in late October; qualifying candidates complete labs from late October through December. Google projects mid-November GA, but that is not a guaranteed launch contract.<br>
**Official source:** [Professional Agentic Architect beta](https://cloud.google.com/learn/certification/agentic-architect/) · [official exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf)

## How to use this guide

Agentic systems connect probabilistic models to data, memory and actions. Study every design as: user/business goal → agent responsibility → authorized context → model/retrieval/memory → tool identity and action contract → orchestration → evaluation → deployment/trace → policy/human control → incident/rollback. Prefer the least autonomy that achieves the outcome.

As of September 6, the beta page says the certification has two parts: a Pearson-delivered proctored multiple-choice assessment for concepts/design/standards and hands-on Google Skills labs for execution/coding. The beta listing says three hours, about 80 multiple-choice questions, USD 120 before tax (40% off a stated USD 200 retail price), English, online or onsite, one-year validity, no prerequisite, and recommended three-plus years building cloud solutions including one-plus year building agents on Google Cloud. The [official beta FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en) says registration closes September 30, multiple-choice testing runs September 8–30, results arrive in late October, and only candidates who pass that part receive the late-October-to-December lab invitation. It estimates less than five hours for the labs and projects mid-November GA. **VERIFY CURRENT:** every date, result message, eligibility step, lab deadline, and GA projection before scheduling.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the published objectives.

## Objective map

| Domain | Weight | End-to-end proof |
|---|---:|---|
| Building agents using low-code tools | ~13% | A stateful low-code flow uses authorized enterprise/multimodal data and bounded behavior |
| Using coding agents for application development | ~17% | Coding agents operate in sandboxed repos/tools with reviewable enterprise customization |
| Developing custom agents | ~33% | Model, ADK, memory, retrieval, identity, tools/protocols and multi-agent coordination fit |
| Evaluating and deploying agentic workflows | ~22% | Test sets, tool/retrieval/response evals, runtime, traces, scale, reliability and cost work |
| Securing and governing agentic workflows | ~15% | Authentication, PAB, gateway/registry/policy, guardrails, HITL and identity propagation constrain action |

This is a fast-moving beta. The official guide's product list includes Agent Gateway, Identity, Registry, Retrieval, Runtime, Search, Agents CLI, Antigravity, Auth Manager, Skill Registry, Gemini Enterprise, ADK, data stores, Model Garden, and Google Cloud Observability. Items may be prerelease, renamed, limited by region/entitlement, or documented under older Vertex/Agent Engine paths. Verify the live exam PDF and current docs before each study session.

---

## 1. Low-code agents — about 13%

Gemini Enterprise **Workflow Builder**—called Agent Designer in the beta blueprint—and Customer Experience Agent Studio model state-based workflows with pages/states, transition routes and event handlers. Google recorded the name change in the [Gemini Enterprise release notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes) on September 3, 2026. Design explicit entry/exit criteria, parameter/schema validation, retry/timeout, no-match/no-input, escalation, cancellation, recovery and audit. Low-code reduces implementation effort; it does not remove identity, data, evaluation or operations.

System instructions define role, allowed sources/actions, constraints, output and escalation. Prompt templates combine task, delimited context, examples and structured output. The official guide names few-shot and chain-of-thought. Do not depend on exposing hidden model reasoning; request concise rationale, cited evidence, plans or structured intermediate artifacts that can be validated. Treat retrieved/user content as untrusted and keep policy outside it.

Enterprise connection requires source authorization, connector identity, permission-aware indexing/retrieval, freshness, deletion, lineage, residency and audit. Gemini Enterprise and Agent Search must not return content merely because the index can see it. For video/audio/image, define ingestion, transcription/OCR/segmentation, metadata, modality-specific quality, access and cost. Evaluate retrieval separately from generated response.

> **Related item:** A conversation state machine makes expected paths explicit; an LLM can interpret language within a state, but deterministic routes and policy remain valuable for high-consequence transitions.

---

## 2. Coding agents — about 17%

Give a coding agent a bounded repository/worktree, written task/acceptance criteria, relevant instructions, read-only discovery first, approved tools/MCP servers/skills, least-privilege short-lived identity, network/package allowlists, secret isolation, resource/time limits and audit. Run generated code/tests in Cloud Workstations, GKE or Antigravity sandboxing suited to the risk. Never expose production credentials or permit unreviewed destructive deployment.

MCP standardizes how a host/client discovers and invokes server-provided tools/resources/prompts; it does not make a server trusted or authorize every call. Review server provenance, schema, transport/auth, data flow, tool side effects, prompt-injection exposure, timeout/retry and output. Pin/version dependencies and isolate untrusted builds.

Use agents to explore, refactor, test, optimize or patch, but establish a behavioral/performance/security baseline and verify diffs, tests, static/security scans, dependency/license changes and runtime evidence. A plausible vulnerability patch can create a bypass or regression. Human/code-owner approval and CI gates remain.

Antigravity customization may include skills, plugins, extension hooks, rules and subagents. Keep instructions scoped, versioned and tested; distinguish reusable procedure from authority. Agents CLI may support build/deploy/govern/optimize workflows—verify exact current commands. Multi-agent coding increases coordination and review surface; use it only when independent scopes or specialization create value.

> **Related item:** A sandbox limits blast radius but is not a trust verdict. Credentials, network egress, mounted files, package installation and produced artifacts can cross its boundary.

---

## 3. Custom agents — about 33%

### Choose model and architecture

Compare LLM versus smaller language model, self-hosted versus SaaS, and open versus proprietary by evaluated task quality, modality/context, safety, latency/throughput, availability, cost, license/provenance, data terms, region, customization and operations. Use deterministic code for stable rules and calculations. A larger model may improve difficult reasoning but add latency/cost; route only justified tasks to it.

ADK provides code-first agent, tool, session, callback, evaluation and orchestration patterns. Keep model/provider and business tools behind explicit interfaces so each can be tested. System design separates user/API layer, agent policy, model, retrieval, memory/session, tools, state, trace/evaluation and operations.

Session is the active interaction/workflow state; memory persists selected facts beyond a session. Define schema, scope (user/tenant/agent), provenance, TTL, consent, sensitivity, correction/deletion, conflict and summarization. Memory Bank/managed sessions add service capability but do not decide what is appropriate to remember. Never treat model-generated memory as verified fact.

Agents CLI skills/plugins and agent-versus-human modes need a capability contract: trigger/input/output, identity, side effects, approval, errors, version and owner. Human mode must give enough evidence and time for meaningful approval, not a rubber-stamp button.

### Retrieval, tools and identity

A RAG pipeline is authorize/ingest → parse/chunk → metadata/permissions → embed/index → retrieve/filter/rerank → construct context → generate/cite → evaluate → refresh/delete. Choose embedding and similarity/reranking by measured recall/relevance, language/modality, latency and cost. Vector Search, Agent Retrieval or RAG Engine are implementation choices; test absent answers, conflicting/stale/malicious documents and revoked permissions.

### Blueprint-named data, model, and observability services

Choose a managed product from workload semantics, not because the agent can connect to it:

| Product | Useful agent role | Boundary and evidence |
|---|---|---|
| [Cloud Storage](https://cloud.google.com/storage/docs/introduction) | Documents, media, batch inputs, exports and model artifacts | Object version, metadata, location, encryption, retention and object-level authorization; prove stale/deleted/oversized object handling |
| [BigQuery](https://cloud.google.com/bigquery/docs/introduction) | Governed analytical history, feature/evaluation data and large set-oriented queries | Dataset/table policy, row/column controls, job identity, bytes/cost, freshness and query result; it is not a low-latency transaction store |
| [Cloud SQL](https://cloud.google.com/sql/docs/introduction) | Relational application state and transactions requiring SQL constraints | Engine/version, connection path, pool, transaction, backup/replica and failover; prove rollback and recovery rather than treating managed as failure-free |
| [Firestore](https://cloud.google.com/firestore/docs/overview) | Document-oriented application, conversation or workflow state | Database mode/location, document schema, index, consistency/transaction need, IAM/rules and hot-path limits; do not confuse stored state with verified memory truth |
| [Memorystore for Redis](https://cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview) | Low-latency cache, rate/coordination data or explicitly disposable session state | TTL, eviction, persistence/HA tier, failover and cache-miss behavior; keep an authoritative source when loss or staleness is unacceptable |
| [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) | Discover and compare Google, partner and open models and deployment paths | Evaluate task quality, safety, license, provenance, region, endpoint/runtime, quota, latency and cost before selection; catalog presence is not approval |
| [Google Cloud Observability](https://cloud.google.com/stackdriver/docs) | Cloud Logging events, Monitoring metrics/alerts and Trace request spans | Correlate user, agent, model, retrieval and tool outcomes with redaction, sampling, retention and tenant controls; telemetry presence is not proof of correctness |

Data classification and access decide which service an agent may use. Define source of truth, schema, identity, locality, latency, consistency, retention, deletion, backup, cost and degraded behavior. Cache and memory are separate decisions; an agent-generated statement does not become authoritative because it was persisted.

Agent Identity represents agent/workload access. Decide whether a tool acts as end user, agent or delegated combination; propagate identity only where intended. Every tool/API/MCP server needs narrow OAuth/IAM scope, schema/argument validation, destination/action allowlist, transaction/rate/cost limit, idempotency, timeout/retry, approval, audit and reversal. Google Cloud MCP Servers or custom integration layers do not remove these controls.

### Orchestration and multi-agent coordination

MCP connects tools/context; A2A supports agent-to-agent communication/interoperability. Validate peer identity, capability declaration, message/artifact schema, confidentiality, authorization, timeouts, provenance and loop prevention. Protocol interoperability does not imply trust.

Sequential orchestration fits ordered dependencies; parallel fits independent tasks and needs merge/conflict policy; graph workflows express conditional branches/cycles with explicit termination. Specialist delegation needs routing evidence, bounded context/authority and accountable coordinator. Agent Registry/Skill Registry discover/version capabilities; Agent Runtime executes; policies constrain; traces correlate. Prevent delegation/action loops with budgets, step/time limits, deduplication and terminal states.

> **Related item:** More agents do not guarantee better quality. They add model calls, latency, cost, failure paths, identity transitions and evaluation combinations.

---

## 4. Evaluate and deploy — about 22%

Build versioned test sets from requirements and production failure categories: typical, edge, adversarial, multilingual/accessibility, permission, absent/conflicting knowledge, tool failure, long conversation and recovery. Keep train/development and final holdout separate. Golden responses can be reference answers, criteria or permitted action traces; avoid overfitting wording.

Evaluate layers independently:

| Layer | Evidence |
|---|---|
| Routing/planning | correct agent/tool/sequence, termination, unnecessary steps |
| Retrieval | relevance/recall, permission correctness, freshness, citation source |
| Response | task success, faithfulness, completeness, format, uncertainty, safety |
| Tool | correct tool/arguments/identity, side effect, idempotency, error/recovery |
| System | end-to-end success, latency, availability, token/tool/infrastructure cost |
| Human outcome | adoption, override, escalation, satisfaction and business KPI without hidden harm |

ADK evalsets, Agent Platform gen-AI evaluation and custom autoraters can automate. Calibrate model judges against humans and version judge/model/prompt. Continuous evaluation uses privacy-safe sampling, representative slices, alert thresholds and an action; it must not leak production sensitive content.

Choose Agent Runtime for managed agent execution/integration, Cloud Run for stateless container control, or GKE for Kubernetes/custom networking/runtime. Check state/session, streaming, scale, concurrency, timeout, tool network, identity, region, release stage, observability and cost. Package immutable versions, canary, run compatibility/data migration checks, observe, promote or roll back.

Trace user request → model/retrieval/tool/agent hops with correlation while redacting secrets/sensitive data. Use [Google Cloud Observability](https://cloud.google.com/stackdriver/docs) to separate structured events, service/user-outcome metrics and cross-hop traces; none substitutes for representative evaluation. Diagnose drift, tool latency, reasoning loops, hallucination and system failure by layer. Apply time/step/token/tool budgets, circuit breakers, retry/backoff, cache/batch where valid, dependency limits and graceful human/degraded paths.

> **Related item:** An SLO should measure a user-valued agent outcome, not only endpoint uptime. A fast 200 response with the wrong action is a failure.

---

## 5. Secure and govern — about 15%

Authenticate users, agents, peer agents and tools; authorize each data read and action. OAuth 2.0 grants scoped access, not identity by itself; validate issuer/audience/scope/expiry and use OIDC or platform identity where identification is needed. Avoid token forwarding beyond intended audience and prevent confused-deputy behavior.

Principal access boundary (PAB) policies can restrict which resources a principal may access, complementing grants; verify current Agent Identity integration and limitations. Agent Gateway can mediate/observe traffic and agent/tool access according to its current contract. Registry records identity, version, owner, capability and policy. Neither gateway nor registry makes behavior safe automatically.

Model Armor and safety filters add input/output inspection; Sensitive Data Protection helps discover/transform sensitive content. Layer them with permission-aware retrieval, secret isolation, deterministic validation/policy, sandboxing, network egress control, tool allowlists/limits, HITL, monitoring and stop/reversal. Test bypass and false positives. Human review belongs before consequential irreversible/ambiguous action and needs evidence, authority and an explicit approve/edit/reject path.

Govern inventory, business owner, risk tier, model/data/tool/license lineage, purpose, permissions, evaluation, deployment approval, change, incidents, cost, retention, audit and retirement. Propagate end-user identity only when the downstream service can validate and enforce it; otherwise use constrained delegation or a workload identity with independent authorization.

---

## Integrated scenarios

### 1. Customer service with refund tools

Use a state workflow for identity/intent, permission-aware policy retrieval and a custom ADK agent. A refund tool validates customer/order, policy, amount/currency and idempotency under scoped OAuth identity; thresholds require human approval. Eval routing, retrieval, explanation, tool arguments, duplicate retries, denial/escalation and rollback. Trace with redaction and alert on loops, latency, override, refund anomaly and cost.

### 2. Enterprise coding agent

Run in a disposable Cloud Workstation/worktree with read-only discovery, trusted MCP servers, package/network restrictions, no production secrets, tests/scans and code-owner review. Skills define repository commands; subagents receive independent file scopes. Measure task success, regressions, vulnerable dependency introduction, runtime and token/tool cost; destroy environment and revoke credentials.

### 3. Multi-agent research workflow

Coordinator delegates parallel source retrieval and structured analysis, then a verifier checks evidence before synthesis. A2A messages carry identity, task, deadline and artifact provenance. RAG filters end-user permissions. No agent can publish or mutate systems; human approves export. Step/token/time budgets stop loops. Evaluate source coverage, entailment, permission denial, conflict, malicious documents and peer failure.

## Hands-on evidence path

1. Build a low-code state flow with transition/error/escalation tests and an authorized synthetic knowledge source.
2. Configure a coding agent in a sandbox with one trusted MCP server/skill; prove denied filesystem/network/credential paths and review a tested patch.
3. Build an ADK agent with deterministic tool schema, session and explicitly governed memory.
4. Create permission-aware RAG with vector retrieval/rerank; deliberately choose Cloud Storage, BigQuery, Cloud SQL, Firestore or Memorystore roles, then test revoked, stale, conflicting, absent, evicted and injected data.
5. Orchestrate sequential, parallel and graph/multi-agent variants; measure accuracy, merge errors, loops, latency and cost.
6. Create evalsets for response/retrieval/tool traces and calibrate an autorater against human labels.
7. Select a model through Model Garden evidence and deploy a version to Agent Runtime/Cloud Run/GKE-style environment with canary, Logging/Monitoring/Trace, load/failure tests and rollback.
8. Threat-model and enforce OAuth/IAM/PAB-style boundaries, gateway/policy, HITL, budgets, sensitive-data controls and incident stop/reversal.

## Original readiness checks

1. Why use state routes with an LLM? 2. Why not request hidden reasoning? 3. What makes enterprise search permission-safe? 4. What must multimodal ingestion preserve? 5. What does sandbox not solve? 6. Why distrust an MCP server by default? 7. How verify an agent patch? 8. Skill versus authority? 9. LLM versus SLM decision? 10. Self-hosted tradeoff? 11. Session versus memory? 12. What belongs in memory governance? 13. Retrieval versus reranking? 14. Why is embedding not permission? 15. Agent versus end-user identity? 16. Name five tool controls. 17. MCP versus A2A? 18. Sequential versus parallel? 19. How stop loops? 20. Why can multiple agents reduce quality? 21. What belongs in golden test set? 22. Why evaluate retrieval separately? 23. How evaluate tool execution? 24. Risk of model judges? 25. What makes continuous eval useful? 26. Runtime choice factors? 27. How diagnose agent latency? 28. What is agent outcome SLO? 29. OAuth does what? 30. What can PAB add? 31. Gateway limitation? 32. Why layer Model Armor? 33. When require HITL? 34. What does registry govern? 35. Why is beta status material? 36. What makes an agent production-ready? 37. BigQuery versus Cloud SQL? 38. Firestore versus Memorystore? 39. What must Model Garden selection prove? 40. Logging versus Monitoring versus Trace? 41. What are the current beta windows? 42. Agent Designer's current name?

## Answer key

1. Deterministic lifecycle/error/control around probabilistic interpretation. 2. It is not a reliable control; request verifiable artifacts/rationale. 3. Enforce source identity/permissions at ingestion and query and handle revocation. 4. Authorization, modality/segment metadata, provenance, quality, freshness and deletion. 5. Credential/egress/mount/artifact and logical authorization risk. 6. Tools can expose data or create side effects. 7. Inspect diff, run tests/scans/performance and review dependency/license/security. 8. Reusable procedure versus permission to act. 9. Evaluated task quality, latency/cost, context, safety and operations. 10. More control plus infrastructure/security/serving burden. 11. Active workflow state versus governed cross-session facts. 12. Scope, source, consent, sensitivity, TTL, correction/deletion and conflict. 13. Candidate retrieval versus reordering by relevance. 14. Similarity is not authorization. 15. Workload capability versus delegated user authority; choose deliberately. 16. Scope, schema validation, allowlist, limit, approval, audit/reversal/idempotency. 17. Tool/context protocol versus agent-to-agent communication. 18. Dependency order versus independent concurrent work with merge. 19. Step/time/token/tool budgets, dedupe and terminal states. 20. Coordination, latency, cost, trust and failure increase. 21. Typical/edge/adversarial/permission/failure/recovery and representative slices. 22. Bad context and bad generation need different fixes. 23. Tool/argument/identity/side effect/error/idempotency. 24. Bias, leakage, instability and self-preference. 25. Representative privacy-safe samples, threshold, owner and action. 26. State/streaming/scale/network/identity/region/operations/cost. 27. Trace model, retrieval, tool, handoff, queue and dependency spans. 28. Correct safe task result within latency/cost, not just uptime. 29. Delegated scoped authorization. 30. Constrain resource universe despite grants. 31. Mediation/telemetry cannot guarantee correct behavior. 32. No single filter covers identity, permissions, tool actions and all semantic attacks. 33. Consequential, irreversible or ambiguous action requiring accountable judgment. 34. Identity/version/owner/capability/policy/lifecycle metadata. 35. Contract, scoring, windows, names and tools can change; results delayed. 36. Bounded purpose/authority, governed data/memory, tested tools/orchestration, layered security, representative eval, observable scalable release, owner and rollback. 37. Large governed analytics versus relational transactions; select by workload and evidence. 38. Durable document/application state versus low-latency cache or disposable state; Redis loss/eviction must be designed. 39. Task quality, safety, license/provenance, region, runtime, quota, latency and cost—not catalog visibility alone. 40. Structured events, health/outcome metrics and cross-hop request spans; correlate them. 41. Registration Sept. 3–30, testing Sept. 8–30, late-October results, and qualifying labs late October–December; verify live. 42. Gemini Enterprise Workflow Builder; retain Agent Designer when mapping the beta blueprint.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. The beta market is immature: prioritize the official guide, select first-party modules for gaps, and build the labs. Times checked September 6, 2026.

| Resource | Access | Estimated time | Best use / currency note |
|---|---|---:|---|
| [Official beta exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf) | Public | 1–2h then every study week | Complete published objectives and in-scope tool list |
| [Official beta FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en) | Public | 15–30 min then before every milestone | Registration, testing, results, qualifying lab and projected-GA windows |
| [Google Skills Agentic Architect path](https://www.skills.google/paths/4525) | Account; labs may require credits | 13 activities totaling about 44h | Current first-party agents, ADK, memory/tools/skills, AgentOps, data and multi-agent route |
| [Agent Development Kit documentation](https://google.github.io/adk-docs/) | Public | 8–20h targeted plus builds | Code-first agent/tools/sessions/evaluation/deployment patterns |
| [Agent2Agent protocol documentation](https://a2a-protocol.org/latest/) | Public | 1–3h plus protocol lab | A2A concepts and trust/interoperability boundaries |
| [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest) | Public | 4–10h targeted | Protocol semantics; pair with threat modeling and one controlled server |
| [Google Cloud generative AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs) | Public | 15–35h targeted | Current Agent Platform, models, RAG, evaluation, runtime and security behavior; URLs may retain Vertex branding during transition |

No credible exam-specific O’Reilly, Pluralsight, Whizlabs, Udemy or MeasureUp product was verified on September 6; none is invented. Add commercial resources only after a live listing demonstrates beta/current-guide alignment. Do not use dumps or recalled beta questions.

## Source and freshness notes

- Page, PDF, beta FAQ, release notes, product references and 13-activity path were checked September 6. Registration is open, testing starts September 8, and later result/lab/GA dates remain provider projections or scheduled windows.
- Product names, CLIs/SDKs, protocols, release stages, regions, quotas, pricing, two-part delivery and GA conversion are highly volatile.
- This guide is original public-source synthesis. It contains no leaked/recalled beta item, proprietary lab, dump or copied course material.

> **Related items remain contextual:** The beta exam guide defines current scope; related explanations connect it to defensible agent architecture and operations.
