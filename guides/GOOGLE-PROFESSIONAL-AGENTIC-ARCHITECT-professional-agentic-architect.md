---
exam_code: GOOGLE-PROFESSIONAL-AGENTIC-ARCHITECT
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/agentic-architect/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-29
---

# Google Cloud Professional Agentic Architect Beta Study Guide

> **Independent AI-assisted resource — BETA; SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 29, 2026. Registration and the multiple-choice testing window are open through September 30, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#google-professional-agentic-architect-coverage-record). The [official beta page](https://cloud.google.com/learn/certification/agentic-architect/), [exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf), and [beta FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en) are authoritative.

**Current baseline:** Published beta guide with five domains weighted approximately 13%, 17%, 33%, 22%, and 15%; registration open September 3–30, 2026<br>
**Scheduled change:** Multiple-choice testing runs September 8–30; results are expected in late October; qualifying candidates complete labs from late October through December. Google projects mid-November GA, but that is not a guaranteed launch contract.<br>
**Official source:** [Professional Agentic Architect beta](https://cloud.google.com/learn/certification/agentic-architect/) · [official exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf)

## How to use this guide

Agentic systems connect probabilistic models to data, memory and actions. Study every design as: user/business goal → agent responsibility → authorized context → model/retrieval/memory → tool identity and action contract → orchestration → evaluation → deployment/trace → policy/human control → incident/rollback. Prefer the least autonomy that achieves the outcome.

As of September 29, the beta page says the certification has two parts: a Pearson-delivered proctored multiple-choice assessment for concepts/design/standards and hands-on Google Skills labs for execution/coding. The beta listing says three hours, about 80 multiple-choice questions, USD 120 before tax (40% off a stated USD 200 retail price), English, online or onsite, one-year validity, no prerequisite, and recommended three-plus years building cloud solutions including one-plus year building agents on Google Cloud. The [official beta FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en) says registration closes September 30, multiple-choice testing runs September 8–30, results arrive in late October, and only candidates who pass that part receive the late-October-to-December lab invitation. It estimates less than five hours for the labs and projects mid-November GA. **VERIFY CURRENT:** every date, result message, eligibility step, lab deadline, and GA projection before scheduling.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the published objectives.

## Objective map

| Domain | Weight | End-to-end proof |
|---|---:|---|
| Building agents using low-code tools | ~13% | A stateful low-code flow uses authorized enterprise/multimodal data and bounded behavior |
| Using coding agents for application development | ~17% | Coding agents operate in sandboxed repos/tools with reviewable enterprise customization |
| Developing custom agents | ~33% | Model, ADK, memory, retrieval, identity, tools/protocols and multi-agent coordination fit |
| Evaluating and deploying agentic workflows | ~22% | Test sets, tool/retrieval/response evals, runtime, traces, scale, reliability and cost work |
| Securing and governing agentic workflows | ~15% | Authentication, PAB, gateway/registry/policy, guardrails, HITL and identity propagation constrain action |

The September 29 review read all four pages of the actual PDF: **31 considerations under 11 numbered objectives**, plus a separate **28-item tool list**. Counts by weighted domain are 4/5/9/7/6. No printed PDF publication date was inferred. The monitored capability text changed only by adding a sentence directing readers to the FAQ; the dated comparison is preserved in the review.

This is a fast-moving beta. The official guide's product list includes Agent Gateway, Identity, Registry, Retrieval, Runtime, Search, Agents CLI, Antigravity, Auth Manager, Skill Registry, Gemini Enterprise, ADK, data stores, Model Garden, and Google Cloud Observability. Items may be prerelease, renamed, limited by region/entitlement, or documented under older Vertex/Agent Engine paths. Verify the live exam PDF and current docs before each study session.

### Distinguish preparation from assessment

Both assessment components must be passed. The public Google Skills preparation path is optional and its activities are not the separate qualifying assessment labs. The FAQ gives late October for multiple-choice results and two months to complete the labs once available. The canonical page’s general result estimate—four to six weeks after both windows close—has a different scope; do not substitute it for the component-specific timeline. The projected mid-November GA format is two hours with multiple-choice results in 7–10 business days, followed by the required labs. All windows and projections require a current check. [Certification FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en).

The exam explicitly names the following tool families. This table accounts for all 28 list entries; product names define scope, not universal availability or a requirement to use every service in one design.

| Blueprint tool family | Study and evidence boundary |
|---|---|
| ADK; agent evaluation; Agents CLI; Antigravity (CLI, SDK, App); Skill Registry | Pin runtime and SDK versions; test code, tool contracts, reusable procedures, evaluation and controlled deployment. |
| Agent Identity; Auth Manager (OAuth 2.0); Agent Gateway; Agent Registry | Separate identity, delegated credentials, network mediation and inventory; verify actual policy enforcement. |
| Agent Retrieval and Vector Search 1.0; Agent Search; RAG Engine; MCP servers; agentic protocols (A2A, MCP) | Preserve the blueprint’s version/name; test authorized retrieval, peer/tool trust, lifecycle and current protocol compatibility. |
| Agent Runtime; Cloud Run; GKE | Compare state, identity, network, scale, recovery and cost; Runtime is formerly Agent Engine. |
| Cloud Storage; BigQuery; Cloud SQL; Firestore; Memorystore for Redis | Assign storage, analytics, transactions, document state and cache roles deliberately; prove permission, freshness and recovery behavior. |
| Gemini Enterprise; Gemini LLMs; Model Garden | Choose low-code workflow, model and deployment path from measured requirements and current entitlement/region support. |
| Google Cloud Observability (Logging and Trace); Model Armor; Sensitive Data Protection | Correlate redacted action evidence, enforce supported inspection and protect sensitive data; telemetry and classification do not grant authorization. |

---

## 1. Low-code agents — about 13%

The beta blueprint asks for state-based workflows with pages, transition routes and event handlers, naming Agent Designer and Customer Experience Agent Studio as examples. Current Gemini Enterprise calls Agent Designer **Workflow Builder**. Map each lifecycle control to the selected product’s current capabilities; do not assume identical interfaces or semantics. Google recorded the name change in the [Gemini Enterprise release notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes) on September 3, 2026. Design explicit entry/exit criteria, parameter/schema validation, retry/timeout, no-match/no-input, escalation, cancellation, recovery and audit. Low-code reduces implementation effort; it does not remove identity, data, evaluation or operations.

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

### Pin the protocol and SDK, then prove the boundary

**VERIFY CURRENT:** The current MCP specification resolved to **2026-07-28** during this review. Its overview describes stateless self-contained requests and per-request capability negotiation; older examples can assume a different lifecycle. Pin the protocol, SDK, transport and optional extensions together and test the selected combination. This guide does not claim that a small JSON-RPC example establishes protocol compliance. [MCP specification](https://modelcontextprotocol.io/specification/latest).

For protected HTTP MCP, separate the authorization server, resource server and client. The resource server must validate that a token is intended for it; a token for an upstream service must not simply pass through. Use the authorization header, not a query parameter. The HTTP authorization specification does not prescribe the same flow for stdio. Insufficient scope and invalid credentials need distinct handling, with bounded retries. [MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization).

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

### State persistence is an explicit contract

ADK state scopes differ: unprefixed keys belong to a session, `user:` keys span that user’s sessions within one app, `app:` keys span the app’s users, and `temp:` keys last for an invocation. In-memory services lose state on restart. Update state through managed context/event paths; mutating a separately retrieved Session object can bypass tracking and persistence. [ADK state](https://adk.dev/sessions/state/).

**PRACTICAL DEPTH:** Scope is not authorization. Do not place user secrets in app-wide state or trust a model-written `is_authenticated` flag. Preserve provenance, deletion and tenant ownership for memory. Keep security policy and current principal information in a host-controlled authority boundary that model tools cannot rewrite.

Parallel work needs independent inputs, distinct result keys, a merge rule and conflict handling. Do not assume that conversation history, updates or ordering are automatically synchronized. The current ADK parallel-template page notes that Python/Go ADK 2.0 supersedes templates with graph/dynamic workflows; pin the implementation you actually run. [Parallel workflow guidance](https://adk.dev/agents/workflow-agents/parallel-agents/).

A2A can return an immediate Message or create a tracked Task. A context groups related interactions; a task identifies one unit of work. A terminal task cannot restart: refinements create a new task with context/reference linkage. Track accepted artifact versions explicitly rather than assuming the protocol chooses the right “latest” result for the client. [A2A task lifecycle](https://a2a-protocol.org/latest/topics/life-of-a-task/).

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

### A passing trajectory metric can miss an unsafe extra action

ADK’s `tool_trajectory_avg_score` defaults to EXACT matching. IN_ORDER permits extra calls between required calls; ANY_ORDER also relaxes order. Therefore a workflow can contain the expected calls and still perform an unauthorized additional action. Add a separate forbidden-action/permission gate and inspect actual side effects. `response_match_score` uses ROUGE-1 word overlap, while `final_response_match_v2` uses an LLM judge; neither proves tool authorization or business correctness. [ADK evaluation criteria](https://adk.dev/evaluate/criteria/).

**PRACTICAL DEPTH:** Bind evaluation to the artifact released, preserve failed and interrupted cases, and report denominators for every required slice. Trace an external write by operation identity and durable outcome. A timed-out caller cannot infer that the write failed; reconcile the known operation before retrying a consequential action. Cancellation stops future authorized work where supported and does not automatically reverse completed effects.

---

## 5. Secure and govern — about 15%

Authenticate users, agents, peer agents and tools; authorize each data read and action. OAuth 2.0 grants scoped access, not identity by itself; validate issuer/audience/scope/expiry and use OIDC or platform identity where identification is needed. Avoid token forwarding beyond intended audience and prevent confused-deputy behavior.

Principal access boundary (PAB) policies can restrict which resources a principal may access, complementing grants; verify current Agent Identity integration and limitations. Agent Gateway can mediate/observe traffic and agent/tool access according to its current contract. Registry records identity, version, owner, capability and policy. Neither gateway nor registry makes behavior safe automatically.

Model Armor and safety filters add input/output inspection; Sensitive Data Protection helps discover/transform sensitive content. Layer them with permission-aware retrieval, secret isolation, deterministic validation/policy, sandboxing, network egress control, tool allowlists/limits, HITL, monitoring and stop/reversal. Test bypass and false positives. Human review belongs before consequential irreversible/ambiguous action and needs evidence, authority and an explicit approve/edit/reject path.

Govern inventory, business owner, risk tier, model/data/tool/license lineage, purpose, permissions, evaluation, deployment approval, change, incidents, cost, retention, audit and retirement. Propagate end-user identity only when the downstream service can validate and enforce it; otherwise use constrained delegation or a workload identity with independent authorization.

### Re-check authority when a paused action resumes

ADK tool confirmation is **Experimental**. The current documentation lists `DatabaseSessionService` and `VertexAiSessionService` as unsupported for that feature. Boolean approval, richer confirmation data and remote response handling require a compatible runtime and resume design. A sample dialog alone does not establish durable production approval. [ADK confirmation support](https://adk.dev/tools-custom/confirmation/).

**PRACTICAL DEPTH:** Treat a model tool call as a proposal. A trusted host authenticates the actor and binds approval to the exact destination/resource, parameters, resource version, expiry and logical operation. At execution, validate current access, resource state and limits again. Consume approval and record a local effect atomically when they share a transaction. For external effects, use provider idempotency, a durable dispatch/reconciliation design and explicit compensation; a database commit cannot make an unrelated API call atomic. The local workbook below demonstrates only the single-database case. [ADK in-tool authority guidance](https://adk.dev/safety/).

Principal access boundaries constrain eligibility for supported permissions in their enforcement version; they do not grant access. Multiple applicable PAB policies combine eligible resources by **union**, so another policy can retain broader eligibility. Removing every PAB returns a principal to unrestricted resource eligibility, still subject to actual allow/deny evaluation. Review all bindings and permission support before claiming a resource is excluded. Public cached-resource access has additional documented limits. [PAB evaluation](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies).

Agent Identity distinguishes the agent’s own authority from delegated user authority and works with credential management, registry and gateway controls. Deleting an agent leaves IAM bindings referencing its old principal. A replacement with the same display name receives a different resource-derived principal, so prior grants do not automatically follow it. Include binding cleanup and least-privilege re-granting in deployment/retirement evidence. [Agent Identity lifecycle](https://docs.cloud.google.com/iam/docs/agent-identity-overview).

---

## Integrated scenarios

### 1. Customer service with refund tools

Use a state workflow for identity/intent, permission-aware policy retrieval and a custom ADK agent. A refund tool validates customer/order, policy, amount/currency and idempotency under scoped OAuth identity; thresholds require human approval. Eval routing, retrieval, explanation, tool arguments, duplicate retries, denial/escalation and rollback. Trace with redaction and alert on loops, latency, override, refund anomaly and cost.

### 2. Enterprise coding agent

Run in a disposable Cloud Workstation/worktree with read-only discovery, trusted MCP servers, package/network restrictions, no production secrets, tests/scans and code-owner review. Skills define repository commands; subagents receive independent file scopes. Measure task success, regressions, vulnerable dependency introduction, runtime and token/tool cost; destroy environment and revoke credentials.

### 3. Multi-agent research workflow

Coordinator delegates parallel source retrieval and structured analysis, then a verifier checks evidence before synthesis. A2A messages carry identity, task, deadline and artifact provenance. RAG filters end-user permissions. No agent can publish or mutate systems; human approves export. Step/token/time budgets stop loops. Evaluate source coverage, entailment, permission denial, conflict, malicious documents and peer failure.

## Executed local action-control workbook

**PRACTICAL DEPTH — executed September 29, 2026:** The original standard-library Python program below passed **31 local checks**. It uses actual SQLite transactions to allocate synthetic capacity under a trusted approval record and a current access table. It rejects changed arguments, actor/tenant mismatch, expired approval, stale resource versions, unsupported argument types and excess capacity. An injected interruption after resource/approval updates but before ledger insertion rolls back all three effects; the subsequent retry succeeds once.

The first valid operation changes tenant A’s capacity from 100 to 80. Replaying its logical request after approval expiry returns its stored result without another allocation, but only after checking current access. Revocation blocks that replay. A fresh approved operation consumes the remaining 80; tenant B remains at 200, with two committed ledger entries and two consumed approvals. A separate trace fixture shows that required calls in order can coexist with a forbidden extra export.

The 31 checks comprise **26 transaction/validation assertions and five trace comparisons**. This is an in-memory, single-connection experiment, not an agent framework or production authorization service. The actor/tenant tuple and administrative `approve` method are trusted harness inputs; the program does not authenticate a human or protect an exposed approval API. No real approval, payment, cloud resource, tool server, OAuth exchange, LLM, ADK runtime or A2A/MCP endpoint was used. No concurrency, process-crash durability, distributed transaction or external exactly-once effect is claimed. All state is discarded when the connection closes.

Save as `action_workbook.py` and run with Python 3; no third-party packages or credentials are needed.

```python
"""Original in-memory approval/action experiment, not an ADK or payment service."""
import hashlib
import json
import secrets
import sqlite3


def binding(context, request):
    value = dict(actor=context[0], tenant=context[1], request=request)
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    allow_nan=False).encode()).hexdigest()


def validate(request):
    if set(request) != {'request_id', 'resource_id', 'units', 'version'}:
        raise ValueError('unexpected or missing arguments')
    for name in ('request_id', 'resource_id'):
        if not isinstance(request[name], str) or not 1 <= len(request[name]) <= 40:
            raise ValueError('invalid identifier')
    for name in ('units', 'version'):
        if type(request[name]) is not int or request[name] <= 0:
            raise ValueError('expected positive integer')


class Store:
    def __init__(self):
        self.db = sqlite3.connect(':memory:', isolation_level=None)
        self.db.executescript('''
        CREATE TABLE resources(tenant TEXT, id TEXT, remaining INTEGER CHECK(remaining>=0),
                               version INTEGER, PRIMARY KEY(tenant,id));
        CREATE TABLE grants(actor TEXT, tenant TEXT, resource TEXT,
                            PRIMARY KEY(actor,tenant,resource));
        CREATE TABLE approvals(id TEXT PRIMARY KEY, binding TEXT, expires INTEGER,
                               used INTEGER CHECK(used IN (0,1)));
        CREATE TABLE ledger(tenant TEXT, actor TEXT, request TEXT, binding TEXT,
                            result TEXT, PRIMARY KEY(tenant,actor,request));
        INSERT INTO resources VALUES('A','pool',100,1),('B','pool',200,1);
        INSERT INTO grants VALUES('alice','A','pool'),('bob','B','pool');
        ''')

    def approve(self, context, request, expires):
        # Trusted administrative surface in this exercise, never a model tool.
        validate(request)
        key = secrets.token_hex(16)
        self.db.execute('INSERT INTO approvals VALUES(?,?,?,0)',
                        (key, binding(context, request), expires))
        return key

    def snapshot(self):
        return {table: self.db.execute(f'SELECT * FROM {table} ORDER BY 1,2').fetchall()
                for table in ('resources', 'grants', 'approvals', 'ledger')}

    def run(self, context, request, approval, now, inject_failure=False):
        validate(request)
        actor, tenant = context  # Supplied by a trusted host, not model arguments.
        fingerprint = binding(context, request)
        self.db.execute('BEGIN IMMEDIATE')
        try:
            if not self.db.execute('SELECT 1 FROM grants WHERE actor=? AND tenant=? '
                                   'AND resource=?',
                                   (actor, tenant, request['resource_id'])).fetchone():
                raise PermissionError('current access denied')
            resource = self.db.execute('SELECT remaining,version FROM resources '
                                       'WHERE tenant=? AND id=?',
                                       (tenant, request['resource_id'])).fetchone()
            if resource is None:
                raise PermissionError('resource unavailable')
            prior = self.db.execute('SELECT binding,result FROM ledger WHERE tenant=? '
                                    'AND actor=? AND request=?',
                                    (tenant, actor, request['request_id'])).fetchone()
            if prior:
                if prior[0] != fingerprint:
                    raise ValueError('idempotency key reused for a different request')
                result = json.loads(prior[1])
                replay = True
            else:
                grant = self.db.execute('SELECT binding,expires,used FROM approvals '
                                       'WHERE id=?', (approval,)).fetchone()
                if not grant or grant[0] != fingerprint or grant[2] or now >= grant[1]:
                    raise PermissionError('missing, mismatched, used or expired approval')
                if request['version'] != resource[1]:
                    raise ValueError('resource changed; obtain fresh approval')
                if request['units'] > resource[0]:
                    raise ValueError('insufficient capacity')
                result = dict(remaining=resource[0]-request['units'],
                              version=resource[1]+1)
                self.db.execute('UPDATE resources SET remaining=?,version=? '
                                'WHERE tenant=? AND id=?',
                                (result['remaining'], result['version'], tenant,
                                 request['resource_id']))
                self.db.execute('UPDATE approvals SET used=1 WHERE id=?', (approval,))
                if inject_failure:
                    raise RuntimeError('injected interruption before ledger insert')
                self.db.execute('INSERT INTO ledger VALUES(?,?,?,?,?)',
                                (tenant, actor, request['request_id'], fingerprint,
                                 json.dumps(result, sort_keys=True)))
                replay = False
            self.db.execute('COMMIT')
            return dict(**result, replay=replay)
        except BaseException:
            self.db.execute('ROLLBACK')
            raise


checks = 0


def check(value):
    global checks
    if not value:
        raise AssertionError('workbook check failed')
    checks += 1


def rejected_unchanged(store, error, call):
    before = store.snapshot()
    try:
        call()
    except error:
        check(store.snapshot() == before)
    else:
        check(False)


s = Store()
try:
    alice = ('alice', 'A')
    request = dict(request_id='r1', resource_id='pool', units=20, version=1)
    rejected_unchanged(s, PermissionError, lambda: s.run(alice, request, '', 10))
    for bad in (0, -1, True, 2.5):
        rejected_unchanged(s, ValueError,
                          lambda bad=bad: s.run(alice, {**request, 'units': bad}, '', 10))
    rejected_unchanged(s, ValueError,
                      lambda: s.run(alice, {**request, 'approved': True}, '', 10))
    token = s.approve(alice, request, expires=20)
    for field, value in (('units', 21), ('request_id', 'r2'),
                         ('version', 2), ('resource_id', 'unknown')):
        rejected_unchanged(s, PermissionError,
                          lambda field=field, value=value: s.run(
                              alice, {**request, field: value}, token, 10))
    rejected_unchanged(s, PermissionError,
                      lambda: s.run(('mallory', 'A'), request, token, 10))
    rejected_unchanged(s, PermissionError,
                      lambda: s.run(('bob', 'B'), request, token, 10))
    rejected_unchanged(s, PermissionError, lambda: s.run(alice, request, token, 20))
    rejected_unchanged(s, RuntimeError,
                      lambda: s.run(alice, request, token, 10, inject_failure=True))
    first = s.run(alice, request, token, 10)
    check(first == dict(remaining=80, version=2, replay=False))
    after_commit = s.snapshot()
    check(s.run(alice, request, token, 100) == dict(remaining=80, version=2, replay=True))
    check(s.snapshot() == after_commit)
    rejected_unchanged(s, ValueError,
                      lambda: s.run(alice, {**request, 'units': 21}, token, 10))
    rejected_unchanged(s, PermissionError,
                      lambda: s.run(alice, {**request, 'request_id': 'r2'}, token, 10))
    s.db.execute('DELETE FROM grants WHERE actor=?', ('alice',))
    rejected_unchanged(s, PermissionError, lambda: s.run(alice, request, token, 10))
    s.db.execute('INSERT INTO grants VALUES(?,?,?)', ('alice', 'A', 'pool'))
    stale = {**request, 'request_id': 'stale'}
    stale_token = s.approve(alice, stale, 20)
    rejected_unchanged(s, ValueError, lambda: s.run(alice, stale, stale_token, 10))
    too_large = {**request, 'request_id': 'large', 'version': 2, 'units': 81}
    large_token = s.approve(alice, too_large, 20)
    rejected_unchanged(s, ValueError, lambda: s.run(alice, too_large, large_token, 10))
    next_request = {**request, 'request_id': 'r2', 'version': 2, 'units': 80}
    next_token = s.approve(alice, next_request, 20)
    check(s.run(alice, next_request, next_token, 10)['remaining'] == 0)
    check(s.db.execute('SELECT remaining FROM resources WHERE tenant=?', ('B',)).fetchone()[0] == 200)
    check(s.db.execute('SELECT COUNT(*) FROM ledger').fetchone()[0] == 2)
    check(s.db.execute('SELECT SUM(used) FROM approvals').fetchone()[0] == 2)

    # Separate evaluation fixture: a required subsequence can hide an unsafe extra.
    required = ['read', 'approve', 'allocate']
    good = ['read', 'approve', 'allocate']
    unsafe = ['read', 'export_all', 'approve', 'allocate']

    def in_order(actual):
        iterator = iter(actual)
        return all(any(item == expected for item in iterator) for expected in required)

    check(in_order(good))
    check(in_order(unsafe))
    check(unsafe != required)
    check(not set(unsafe).issubset({'read', 'approve', 'allocate'}))
    check(not in_order(['allocate', 'read', 'approve']))
    print(f'{checks} local checks passed')
finally:
    s.db.close()
```

## Proposed cloud and framework labs

These eight labs remain **unexecuted**. Use a disposable authorized environment, synthetic data, a fixed cost/time budget and named cleanup owner. The existing same-session observation that `gcloud` was absent from PATH is retained; no runtime installation or authentication was attempted for this review.

| Lab | Build and failure case | Evidence and cleanup |
|---|---|---|
| 1. Low-code state workflow | Build a selected tool’s state/transition/error/escalation flow with synthetic enterprise data. Test invalid input, absent answer and revoked retrieval access. | Current product/version, expected/actual transitions and authorization failures; delete trial workflow and data source. |
| 2. Sandboxed coding workflow | Give a coding tool an isolated repository, scoped instructions and one reviewed tool connection. Attempt an out-of-scope file/network action and validate a patch. | Diff, tests, deny evidence, dependency changes and resource limits; destroy the disposable environment and remove temporary access. |
| 3. Custom agent and approval | Pin ADK/SDK/session backend, implement a bounded deterministic tool and pause/resume at a supported confirmation boundary. Change access and resource version while paused. | Denied stale/mismatched/expired action, safe retry and restart behavior; remove agent/session data and trial identities. |
| 4. Permission-aware retrieval/memory | Select source-of-truth, cache and vector/search roles; inject stale, revoked, conflicting and malicious synthetic records. | Retrieval membership, source/availability timestamps, memory provenance, deletion/eviction behavior; delete trial stores and cache. |
| 5. Orchestration and protocol interoperability | Test version-pinned sequential/parallel/graph variants and a compatible controlled peer/tool server. Inject duplicate delivery, failed branch and terminal-task follow-up. | Version/transport contract, state ownership, bounded loops, result merge and artifact linkage; stop servers and remove temporary credentials. |
| 6. Layered evaluation | Build original golden data, required and forbidden tool traces, groundedness/response rubrics and representative slices. Include an unsafe extra call that preserves the required subsequence. | Independent side-effect gate, judge/human comparison, denominators and held-out outcomes; remove synthetic evaluation artifacts and schedules. |
| 7. Deploy/observe/recover | Choose Runtime, Cloud Run or GKE from requirements; canary a compatible version and test model/tool latency, timeout and rollback. | Immutable artifact, redacted correlated traces, user-outcome metrics, capacity/cost and reconciliation evidence; undeploy trial resources. |
| 8. Identity and governance | Test agent-own versus delegated access, supported PAB permissions and all applicable bindings; retire/recreate a disposable agent. | Positive/negative access, broader-policy counterexample, new-principal grants, old-binding cleanup, enforced inspection and incident stop; remove policies/identities and trial data. |

## Original readiness checks with answers

These are original study explanations, not recalled or predicted assessment items.

1. **Why use state routes with an LLM?** Deterministic lifecycle/error/control around probabilistic interpretation.

2. **Why not request hidden reasoning?** It is not a reliable control; request verifiable artifacts/rationale.

3. **What makes enterprise search permission-safe?** Enforce source identity/permissions at ingestion and query and handle revocation.

4. **What must multimodal ingestion preserve?** Authorization, modality/segment metadata, provenance, quality, freshness and deletion.

5. **What does sandbox not solve?** Credential/egress/mount/artifact and logical authorization risk.

6. **Why distrust an MCP server by default?** Tools can expose data or create side effects.

7. **How verify an agent patch?** Inspect diff, run tests/scans/performance and review dependency/license/security.

8. **Skill versus authority?** Reusable procedure versus permission to act.

9. **LLM versus SLM decision?** Evaluated task quality, latency/cost, context, safety and operations.

10. **Self-hosted tradeoff?** More control plus infrastructure/security/serving burden.

11. **Session versus memory?** Active workflow state versus governed cross-session facts.

12. **What belongs in memory governance?** Scope, source, consent, sensitivity, TTL, correction/deletion and conflict.

13. **Retrieval versus reranking?** Candidate retrieval versus reordering by relevance.

14. **Why is embedding not permission?** Similarity is not authorization.

15. **Agent versus end-user identity?** Workload capability versus delegated user authority; choose deliberately.

16. **Name five tool controls.** Scope, schema validation, allowlist, limit, approval, audit/reversal/idempotency.

17. **MCP versus A2A?** Tool/context protocol versus agent-to-agent communication.

18. **Sequential versus parallel?** Dependency order versus independent concurrent work with merge.

19. **How stop loops?** Step/time/token/tool budgets, dedupe and terminal states.

20. **Why can multiple agents reduce quality?** Coordination, latency, cost, trust and failure increase.

21. **What belongs in golden test set?** Typical/edge/adversarial/permission/failure/recovery and representative slices.

22. **Why evaluate retrieval separately?** Bad context and bad generation need different fixes.

23. **How evaluate tool execution?** Tool/argument/identity/side effect/error/idempotency.

24. **Risk of model judges?** Bias, leakage, instability and self-preference.

25. **What makes continuous eval useful?** Representative privacy-safe samples, threshold, owner and action.

26. **Runtime choice factors?** State/streaming/scale/network/identity/region/operations/cost.

27. **How diagnose agent latency?** Trace model, retrieval, tool, handoff, queue and dependency spans.

28. **What is agent outcome SLO?** Correct safe task result within latency/cost, not just uptime.

29. **OAuth does what?** Delegated scoped authorization.

30. **What can PAB add?** Constrain resource universe despite grants.

31. **Gateway limitation?** Mediation/telemetry cannot guarantee correct behavior.

32. **Why layer Model Armor?** No single filter covers identity, permissions, tool actions and all semantic attacks.

33. **When require HITL?** Consequential, irreversible or ambiguous action requiring accountable judgment.

34. **What does registry govern?** Identity/version/owner/capability/policy/lifecycle metadata.

35. **Why is beta status material?** Contract, scoring, windows, names and tools can change; results delayed.

36. **What makes an agent production-ready?** Bounded purpose/authority, governed data/memory, tested tools/orchestration, layered security, representative eval, observable scalable release, owner and rollback.

37. **BigQuery versus Cloud SQL?** Large governed analytics versus relational transactions; select by workload and evidence.

38. **Firestore versus Memorystore?** Durable document/application state versus low-latency cache or disposable state; Redis loss/eviction must be designed.

39. **What must Model Garden selection prove?** Task quality, safety, license/provenance, region, runtime, quota, latency and cost—not catalog visibility alone.

40. **Logging versus Monitoring versus Trace?** Structured events, health/outcome metrics and cross-hop request spans; correlate them.

41. **What are the current beta windows?** Registration and multiple-choice testing close September 30, 2026. The FAQ expects multiple-choice results in late October and gives passing candidates two months for distinct assessment labs once available. Both parts are required; mid-November GA remains a projection.

42. **Agent Designer's current name?** Gemini Enterprise Workflow Builder; retain Agent Designer when mapping the beta blueprint.

43. **Why bind approval to the exact request and resource version?** A broad or stale approval can authorize different effects from those reviewed. Recheck current access and state when executing or resuming; changed terms need a new decision.

44. **Does ADK’s confirmation dialog establish durable approval?** No. The feature is Experimental and currently lists DatabaseSessionService and VertexAiSessionService as unsupported; test the selected runtime/backend and resume contract.

45. **What can go wrong with app-wide state?** It spans users within the app. Storing user-specific sensitive information or model-writable policy there can leak data or corrupt authority; use appropriate scope and trusted host controls.

46. **Does a parallel workflow make shared updates safe?** No. Define independent branch outputs, explicit synchronization/merge and error handling; pin SDK behavior rather than assuming deterministic result order or transactional state.

47. **Why pin MCP version and transport?** Current protocol lifecycle and optional extensions differ from older examples, and protected HTTP authorization differs from stdio credential handling. Test the actual selected combination.

48. **Can a terminal A2A task resume for refinement?** The documented lifecycle requires a new task, linked through context and references. Track the accepted artifact version separately.

49. **Do multiple PAB policies form the narrowest intersection?** No. Eligible resources combine by union for supported permissions. Eligibility still needs an allow grant and remains subject to deny evaluation.

50. **Does recreating an agent preserve its principal?** A new resource ID creates a new principal even with the same display name. Remove inactive old bindings and grant the new identity only the required access.

51. **Why can IN_ORDER evaluation pass an unsafe run?** It permits extra calls between required calls. A separate forbidden-action and authorization gate must inspect the actual trace and effects.

52. **What did the 31 local checks establish?** Behavior of a synthetic single-database approval/allocation transaction and trace fixtures, under trusted identity/admin inputs. They do not validate real cloud/framework/authentication, concurrency or external effects.

## Source and freshness notes

**CURRENT BLUEPRINT:** Four actual PDF pages were read, with 31 considerations mapped across five weighted domains and the 28-item tool list checked separately. The capability snapshot gained only a FAQ-pointer sentence; that editorial difference was reviewed before accepting the new digest. A missing lifecycle baseline was explicitly initialized and a subsequent monitor check was unchanged. The monitor’s empty announcement extraction does not replace checking the dated beta FAQ for lab and projected-GA milestones.

The [deep review](../docs/research/2026-09-29-google-professional-agentic-architect-deep-review.md) records source-reading boundaries, public catalog evidence, objective comparison, exact local execution and remaining cloud/framework work. **VERIFY CURRENT:** beta dates, assessment availability, SDK/protocol versions, Preview/Experimental support, product names, principal support, quotas, regions, entitlement and pricing. Human review remains pending.

The September 3 first-party release entry confirms Workflow Builder’s rename and GA status; it does not make every blueprint tool GA. Product references were read selectively, with prior same-session primary security/retention/blog context reused where stated. No paid training interiors, proprietary assessment labs, recalled beta questions or real customer data were accessed.

## Places to learn

This is **not a complete list**. Map selected resources to the current PDF and fill gaps through primary documentation and executed original labs. September 29 catalog observations below do not establish paid-content quality or certification readiness.

| Resource | Access | Estimated time |
|---|---|---|
| [Official exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf) and [FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en) | Public authoritative scope and assessment lifecycle. | Suggested 1–2h initial mapping, then recheck dates before each milestone; this is an editorial budget. |
| [Google Skills Agentic Architect path](https://www.skills.google/paths/4525) | Public outline; activities may require account/credits. Current page lists 13 activities, a relative 27-day update and expressly incomplete blueprint coverage; it retains stale early-September availability language. | Current activity durations are not exposed; the earlier 44h total is unverified. Preparation activities are distinct from qualifying assessment labs. |
| [ADK documentation](https://google.github.io/adk-docs/) | Public first-party documentation, currently redirected to adk.dev. Focus on versioned tools, state, confirmation support, evaluation and deployment. | Suggested 8–16h targeted reading and local builds, plus cloud verification; not a provider duration. |
| [A2A protocol](https://a2a-protocol.org/latest/) and [MCP specification](https://modelcontextprotocol.io/specification/latest) | Public primary protocols. Pin versions/transport and test compatible implementations. | Suggested 3–6h targeted concepts followed by original protocol labs; not measured completion time. |
| [Google Cloud generative AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs) | Public primary product reference; paths may retain older Vertex names. | Suggested 8–16h targeted to runtime, retrieval, identity and monitoring gaps; verify exact current capabilities. |
| [Whizlabs Professional Agentic Architect listing](https://www.whizlabs.com/google-cloud-professional-agentic-architect/) | A public exam-specific listing now exists. Direct retrieval exposed only its title; paid content, labs, questions and update depth were not reviewed. | Duration and detailed current-blueprint coverage unverified. Its existence supersedes the earlier blanket “no verified listing” statement. |
| This guide and proposed labs | Public original explanation and 31-check local workbook; live labs require a suitable authorized environment. | Suggested 16–24h for framework/cloud experiments, fault diagnosis and evidence after prerequisites; not an exam-pass promise. |

No exam-specific Pluralsight, O’Reilly, Coursera or MeasureUp listing was verified in this review’s targeted discovery. This is a research limit, not proof of absence. Use current public outlines to judge relevance, and keep provider estimates separate from your own lab budget.
