---
exam_code: GH-600
vendor_id: github
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-600
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-07
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-07
---

# GH-600 Developing in Agentic AI Systems Study Guide

> **Independent AI-assisted resource — BETA BLUEPRINT; SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The certification and exam are in beta as of September 7, 2026. Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked against public sources; this is not a guarantee that the beta outline, product behavior, or eventual scored exam will remain unchanged. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#gh-600-coverage-record). The [official GH-600 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-600) is authoritative.

**Current baseline:** Initial public beta skills outline, checked September 7, 2026  
**Upcoming blueprint change:** None separately announced; beta content is inherently volatile.  
**Credential status:** [GitHub Certified: Agentic AI Developer (beta)](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-developer/)

## How to use this guide

Study each domain as an operating decision, not a product vocabulary list. For every scenario, identify:

1. the desired outcome and its acceptance evidence;
2. the agent's authority, tools, data, and execution boundary;
3. deterministic gates before and after probabilistic work;
4. the durable state and handoff artifacts;
5. failure detection, retry, rollback, escalation, and ownership;
6. the audit evidence that explains what happened.

Use the official [GH-600 course](https://learn.microsoft.com/en-us/training/courses/gh-600t00), [Part 1 learning path](https://learn.microsoft.com/en-us/training/paths/gh-developing-agentic-systems-1), and [Part 2 learning path](https://learn.microsoft.com/en-us/training/paths/github-agentic-systems-part-two/github-agentic-systems-part-two) for the current Microsoft-authored sequence. This guide adds decision tables, failure reasoning, labs, and review prompts; it does not reproduce exam questions.

> **About related items:** A `Related item:` callout adds implementation or operational context that makes the current objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published beta objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| Prepare agent architecture and SDLC processes | 15–20% | What should the agent do, under what boundary, and what proves success? |
| Implement tool use and environment interaction | 20–25% | Which tools and permissions are necessary, and how does execution fail safely? |
| Manage memory, state, and execution | 10–15% | What must persist, expire, synchronize, or be corrected? |
| Perform evaluation, error analysis, and tuning | 15–20% | How do we measure outcomes, classify failures, and improve behavior? |
| Orchestrate multi-agent coordination | 15–20% | How do agents divide work without conflicts, ambiguity, or lost accountability? |
| Implement guardrails and accountability | 10–15% | Which actions are allowed, gated, denied, observed, and owned by humans? |

The official outline gives ranges, so do not convert them into an invented point count. Product configuration is moving quickly; the architecture and evidence questions are more durable than any screen or preview label.

---

## 1. Prepare agent architecture and SDLC processes

### Start with a bounded work contract

An agent task needs more than a prompt. Define a contract:

| Contract field | Useful question | Evidence |
|---|---|---|
| Outcome | What user or engineering result is required? | Acceptance criteria tied to an issue or change request |
| Inputs | Which repository state, issue, logs, policies, and context are authoritative? | Versioned references and input hashes where useful |
| Output | Code, plan, report, PR, comment, or deployment? | Schema, template, or explicit deliverable list |
| Authority | Read, edit, execute, create PR, merge, deploy, or communicate externally? | Tool allowlist, token scope, rules, environment protection |
| Constraints | What must never happen? | Deny rules, protected paths, data boundaries, time/cost limits |
| Success | What proves the result works? | Tests, scans, review, runtime signals, user acceptance |
| Failure | How does the agent stop and hand off? | Error class, retained state, retry count, escalation owner |

Good candidates are bounded, observable, reversible, and objectively verifiable. Weak candidates have ambiguous intent, broad authority, hidden dependencies, or success that can only be judged after irreversible impact.

### Integrate agents into the SDLC

Map responsibilities before selecting a tool:

```text
issue / request
      |
      v
clarify -> plan artifact -> plan validation -> isolated execution
                                            |
                                            v
                                  tests + scans + review
                                            |
                                  approve / revise / reject
                                            |
                                    merge or deployment
                                            |
                                  observe + learn + audit
```

Useful agent work includes investigation, change design, bounded implementation, test generation, documentation synchronization, triage, and evidence assembly. Keep product ownership, risk acceptance, exception approval, and other judgment-heavy accountabilities assigned to people.

### Recognize common anti-patterns

| Anti-pattern | Why it fails | Better control |
|---|---|---|
| “Fix everything” prompt | No stable scope or completion test | Enumerated targets and stop conditions |
| One powerful token | Blast radius exceeds the task | Task-specific least privilege and short-lived identity |
| Plan and execute in one opaque step | Bad assumptions become mutations | Inspectable plan with pre-action validation |
| Agent-generated test is the only test | Same blind spot may affect code and test | Independent assertions, existing regression tests, review |
| Retry every failure | Permanent or policy failures become loops | Classify transient, deterministic, conflict, and authorization failures |
| Chat transcript as state | Hard to resume or audit reliably | Durable issue, branch, commit, manifest, report, or checkpoint |
| More agents for every task | Coordination cost and conflicts grow | Use the smallest topology that creates real separation of concerns |
| Approval theater | Human sees volume without decision context | Concise risk/evidence packet and explicit approval question |

### Separate planning, reasoning, and action

A structured plan should expose assumptions, targets, dependencies, risks, verification, rollback, and open decisions. Validation asks whether the plan is complete, authorized, internally consistent, and grounded in current repository state. Action begins only after the applicable gate passes.

This separation is especially important when the agent can push, merge, deploy, delete, spend money, access sensitive data, or communicate outside the repository. A textual “be careful” instruction is weaker than an enforced inability to perform an unapproved action.

### Choose an autonomy level

| Level | Example | Suitable control |
|---|---|---|
| Observe | Summarize test failures | Read-only credentials; output reviewed |
| Recommend | Propose a remediation plan | No mutation tools; structured plan |
| Prepare | Create a branch and PR | Isolated branch, scoped token, required checks |
| Execute reversible action | Update a nonproduction environment | Environment gate, rollback, monitoring |
| Execute high-impact action | Production or irreversible change | Explicit human authorization and protected path |

Autonomy is an action-by-action risk decision, not a single label for the whole agent.

### Make work observable

Capture correlation ID, initiating actor, agent/profile/version, repository/ref/SHA, inputs, plan, tool calls, policy decisions, outputs, test results, approvals, elapsed time, cost signals, and final disposition. Redact secrets and minimize personal or regulated data. Logs without identity and correlation are activity, not useful accountability.

---

## 2. Implement tool use and environment interaction

### Select tools from the task contract

Grant only capabilities needed for the next bounded outcome.

| Need | Tool category | Principal risk | Evidence/control |
|---|---|---|---|
| Understand repository | Read/search | Sensitive-data exposure | Scope and redaction |
| Change files | Edit | Unauthorized or overlapping change | Branch isolation and diff |
| Validate | Shell/test/scan | Command or dependency execution | Allow rules, sandbox, pinned dependencies |
| Query GitHub | GitHub API/tool | Data or mutation overreach | Fine-grained permissions and audit log |
| Reach external service | MCP/API | Data exfiltration and prompt injection | Approved server, endpoint allowlist, schema validation |
| Deploy | Workflow/environment | Production impact | Protected environment, approval, rollback |

The current [GitHub agent concepts](https://docs.github.com/en/copilot/concepts/agents) distinguish cloud, CLI, IDE, workflow, custom, and partner-agent surfaces. Do not assume they share configuration discovery, tool behavior, network access, memory, or enterprise policy.

### Configure custom agents deliberately

The [custom-agent configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration) describes profiles with instructions and selectable tools, including MCP-provided tools. A secure profile should name its specialty, expected inputs/outputs, prohibited behavior, evidence expectations, escalation path, and a minimal tool set.

Important reasoning rule: omitting a tool restriction may grant more capability than listing only the necessary tools. Unknown tool names can be ignored, so validate actual effective capability rather than assuming a configuration typo fails closed.

### Treat MCP as a trust boundary

For each MCP server, document:

- owner and business purpose;
- transport and authentication;
- exposed tools and data classifications;
- input/output schemas and size limits;
- read versus mutation behavior;
- tenant/repository scope;
- secrets handling and log redaction;
- timeout, retry, rate-limit, and outage behavior;
- approval, versioning, review, and retirement process.

An MCP registry improves discovery and governance; an allowlist constrains approved choices. Neither proves that every tool invocation is safe. Validate arguments, returned content, and downstream use. Treat tool output as untrusted data that may be stale, malicious, or shaped to influence the model.

### Bound the execution environment

Evaluate operating system, installed tools, filesystem persistence, network egress, secrets, identity, working directory, compute/time limits, and repository/ref visibility. A local IDE session, ephemeral cloud sandbox, and CI runner may execute the same instruction differently.

The [hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference) documents important environment-specific behavior, including ephemeral cloud-agent storage, restricted outbound networking, and hook differences across cloud and CLI. **VERIFY CURRENT:** hooks, custom agents, agentic workflows, memory, and third-party-agent support remain fast-moving features.

### Use GitHub-native isolation

- One task should have an explicit issue or work item.
- Give each independent change its own branch.
- Limit workflow permissions and repository scope.
- Use path ownership and required checks for sensitive areas.
- Use environments for deployments and protected secrets.
- Use concurrency to prevent overlapping work where “latest wins” is safe, or serialize where every run matters.

GitHub documents [workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) and [deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments). A concurrency key prevents certain overlap; it does not replace application-level idempotency, locking, or transaction design.

### Design robust error handling

| Failure class | Example | Response |
|---|---|---|
| Transient | Rate limit, network timeout | Bounded exponential backoff with jitter |
| Deterministic | Test failure from code defect | Stop, retain evidence, revise |
| Authorization | Tool or endpoint denied | Do not retry unchanged; escalate scope decision |
| Conflict | Branch changed or file overlaps | Refresh state, replan, arbitrate ownership |
| Policy | Protected action denied | Preserve denial and request authorized path |
| Ambiguous | Acceptance criteria conflict | Stop before mutation and ask for judgment |
| Partial side effect | External write succeeded before timeout | Reconcile using idempotency key or read-after-write |

Rollback must be designed for the actual side effect. Reverting a commit does not automatically retract a message, undo a database migration, rotate a disclosed secret, or restore deleted external data.

### Related preview: GitHub Agentic Workflows

The current [agentic-workflow authoring guide](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows) describes natural-language workflow source compiled into a lock workflow, explicit permissions, safe outputs, and selectable engines. It is useful hands-on context for repository-scoped CI invocation, but it is public preview and must not be treated as a permanent syntax contract or the only way to satisfy the objective.

---

## 3. Manage memory, state, and execution

### Distinguish memory from state

| Concept | Purpose | Example | Main risk |
|---|---|---|---|
| Working context | Immediate reasoning material | Current issue, diff, logs | Context-window loss or distraction |
| Short-term memory | Reuse during a session/task | Decisions and intermediate observations | Stale assumption |
| Long-term memory | Reuse across tasks | Repository conventions or preferences | Cross-task leakage and outdated facts |
| External memory | Retrieval from governed system | Documentation, vector store, issue history | Poisoned retrieval and access leakage |
| Execution state | Resume/control work | Step status, attempt, branch, output hashes | Duplicate or skipped side effects |

Memory helps choose what to do. State records what has happened and what must happen next. A durable checkpoint needs enough information to resume without repeating an unsafe action.

### Define memory lifecycle

For each memory class, specify source, owner, scope, access control, freshness, expiration, correction, deletion, and provenance. Repository-specific facts should not silently influence unrelated repositories. User preferences should not become organization policy. Sensitive prompts or tool output should not be retained simply because they may be useful later.

### Persist resumable state

A practical checkpoint can include:

```yaml
task: ISSUE-123
repository: owner/repo
base_sha: abc123
branch: agent/issue-123
plan_version: 3
completed_steps: [inspect, patch]
next_step: validate
artifacts:
  diff_sha256: "..."
  test_report: reports/test.json
side_effects: []
open_risks: ["upstream API contract not independently verified"]
```

Store only fields the workflow actually needs. Validate the checkpoint schema and current repository state before resuming.

### Detect context drift

Drift occurs when the task, base branch, policy, dependency, objective, or external system changes while work continues. Detect it with SHA comparison, timestamps, version identifiers, changed acceptance criteria, new comments, failed preconditions, or mismatched artifact hashes.

When drift matters:

1. stop mutations;
2. preserve current artifacts;
3. refresh authoritative inputs;
4. classify what remains valid;
5. replan the affected portion;
6. rerun appropriate gates.

### Prevent conflicting context across tools

Use one authoritative task ID and base SHA, explicit artifact ownership, idempotency keys for external writes, versioned schemas, and a handoff manifest. Never merge two agent conclusions merely because both sound plausible; reconcile them against source evidence and current state.

---

## 4. Perform evaluation, error analysis, and tuning

### Define success at multiple layers

| Layer | Signal |
|---|---|
| Contract | Required files/fields exist; prohibited actions absent |
| Functional | Tests and acceptance scenarios pass |
| Quality | Review, lint, security, maintainability, accessibility |
| Operational | Latency, failure rate, retries, cost, saturation |
| Agent behavior | Tool correctness, plan adherence, groundedness, escalation quality |
| Business/user | Task usefulness, adoption, rework, incident or cycle-time effect |

Do not optimize a proxy until it undermines the real outcome. More commits, tool calls, or completed tickets can represent inefficiency rather than value.

### Build an evaluation set

Include normal work, edge cases, ambiguous requests, malicious or conflicting instructions, missing dependencies, stale context, permission denial, tool outage, concurrent edits, and partial failure. Record expected outcome and forbidden behavior. Separate the evaluation set from examples used to tune instructions when possible.

Automated scans create signals; they do not decide every risk. A passing scan can miss semantic errors, and a finding may be a false positive. Retain tool version, configuration, input SHA, raw result, triage decision, and remediation evidence.

### Classify failures before tuning

| Root cause | Diagnostic evidence | Likely correction |
|---|---|---|
| Reasoning error | Correct facts, wrong conclusion | Better decomposition or decision rule |
| Missing/stale context | Absent or outdated source | Retrieval, freshness gate, explicit assumption |
| Instruction ambiguity | Multiple defensible outcomes | Clarify contract and priority |
| Tool misuse | Wrong tool/arguments/order | Narrow tool instructions and validate calls |
| Permission/configuration | Denied or excessive access | Correct least-privilege configuration |
| Environment mismatch | Local works, CI fails | Reproduce target environment and pin assumptions |
| Coordination failure | Duplicate/conflicting work | Ownership, isolation, handoff, arbitration |
| Evaluation defect | Metric rewards wrong result | Improve rubric and add counterexamples |

### Tune one layer at a time

Change instructions, context selection, memory, tools, permissions, workflow gates, or model settings according to evidence. Version the change, rerun the same evaluation set, inspect regressions, and compare cost/latency as well as correctness. Avoid changing everything at once because the improvement cannot be attributed.

---

## 5. Orchestrate multi-agent coordination

### Choose the smallest useful topology

| Pattern | Best for | Main risk |
|---|---|---|
| Sequential handoff | Ordered specialties | Lost assumptions between stages |
| Manager/worker | Decomposable bounded tasks | Manager becomes bottleneck or trusts weak summaries |
| Parallel independent review | Diverse analysis of same artifact | Cost and false consensus |
| Parallel partition | Disjoint files/components | Hidden shared dependency |
| Debate/arbitration | High-uncertainty decision | Performative disagreement without evidence |
| Event-driven specialists | Operational triage | Duplicate response and unclear incident command |

An orchestrator should define task IDs, ownership, inputs, allowed paths, outputs, dependencies, deadlines, stop conditions, and merge authority.

### Isolate parallel execution

Branches isolate Git history, not every resource. Agents can still collide on issue comments, environments, package registries, databases, cloud resources, caches, or generated artifacts. Use distinct namespaces and credentials, path ownership, concurrency groups, idempotency keys, and explicit shared-resource rules.

### Make handoffs reviewable

A handoff should state:

- objective and completion status;
- base/current SHA and owned paths;
- evidence consulted;
- artifacts created or changed;
- tests/scans run and results;
- assumptions and unresolved risks;
- side effects already performed;
- exact next action and responsible actor.

Summaries are navigation aids. Keep links to primary artifacts so the next agent or human can verify claims.

### Resolve conflicts by evidence and ownership

Detect overlapping diffs, contradictory plans, incompatible dependencies, stale bases, duplicate external actions, or disagreement about source facts. Stop affected work, identify the authoritative contract and current state, assign an arbiter, choose/reconcile/replan, then rerun gates. “Last writer wins” is rarely safe for semantics.

### Recover degraded workflows

Define how to detect failed, partial, slow, looping, silent, or low-quality agents. Recovery may retry a transient read, replace an unhealthy worker, replay from a safe checkpoint, rebase/replan after drift, roll back a reversible change, compensate an external side effect, or escalate to a person.

Agent retirement should revoke credentials, disable triggers, archive configuration and evaluation evidence, transfer ownership, handle durable memory according to policy, and preserve enough history for audit and incident analysis.

---

## 6. Implement guardrails and accountability

### Classify actions by impact

Assess confidentiality, integrity, availability, financial cost, legal/compliance effect, external visibility, reversibility, and blast radius.

| Risk | Example | Control |
|---|---|---|
| Low | Read public docs | Logging and bounded scope |
| Moderate | Edit branch files | Diff, tests, path rules, PR review |
| High | Merge, publish, change security policy | Required review and protected rule |
| Critical | Delete production data, rotate shared identity, legal communication | Explicit authorized human decision and recovery plan |

### Build layered guardrails

```text
instruction boundary
  -> identity and tool permissions
    -> network/data scope
      -> pre-action policy check
        -> isolated execution
          -> deterministic tests/scans
            -> protected review/environment gate
              -> monitoring, audit, and recovery
```

No single layer is sufficient. Instructions influence behavior; permissions enforce capability; rules and environments gate changes; monitoring detects failures; recovery limits damage.

The [enterprise agent-management reference](https://docs.github.com/en/copilot/concepts/enterprise/agent-management) describes policy and visibility surfaces for agent types and MCP. **VERIFY CURRENT:** local IDE agents, cloud agents, partner agents, and other clients can have distinct control planes; enabling or disabling one does not necessarily govern the others.

### Design meaningful human intervention

Intervention should occur where human judgment materially reduces risk: ambiguous intent, policy exception, novel security impact, irreversible action, production deployment, or unresolved evidence conflict. Present scope, change, tests, residual risk, rollback, and the exact decision requested. Require a fresh check when the approved plan or underlying state changes materially.

### Preserve accountability

The human remains accountable for delegated decisions, but accountability requires usable evidence and real authority. Record who requested, configured, approved, executed, reviewed, and accepted the result. Do not credit an agent approval as independent human judgment, and do not hide agent-originated work behind a generic automation identity.

---

## Integrated scenarios

### Scenario A — Dependency-remediation agent

The agent may open PRs for vulnerable dependencies but cannot merge. It reads the advisory and lockfile, updates one dependency family, runs the project gate, records transitive changes, and opens a PR. A required workflow and code owner protect merge. Permanent test failure stops the task; a transient registry failure receives bounded retry. Success is not “PR opened,” but a reviewed, passing, non-regressive update linked to the advisory.

### Scenario B — Production incident assistant

The agent correlates read-only logs and recent deployments, proposes hypotheses, and prepares rollback instructions. It cannot execute production changes. Evidence is timestamped and redacted; uncertainty is explicit. Incident command chooses action. This preserves speed while keeping authority with the accountable operator.

### Scenario C — Parallel documentation refresh

An orchestrator assigns disjoint guide files to workers and reserves shared indexes for one integrator. Every worker uses the same source-date boundary and produces a handoff with source URLs, changed claims, validations, and concerns. The integrator detects duplicate URLs and cross-guide contradictions before merging. If a vendor source is unavailable, the worker records the gap and uses adjacent evidence only as labeled support.

---

## Hands-on labs

Use a disposable personal repository with no real secrets or production integration. If a feature or plan is unavailable, complete a tabletop design and capture expected configuration, evidence, and failure behavior.

### Lab 1 — Write and validate an agent work contract

Create an issue for a small documentation defect. Specify inputs, outputs, allowed paths/tools, forbidden actions, success evidence, retry policy, rollback, and escalation. Have another person or a separate review pass identify ambiguity before any edit.

**Evidence:** issue, plan artifact, review comments, final acceptance checklist.

### Lab 2 — Least-privilege custom-agent design

Design two profiles: a read-only investigator and a branch-editing implementer. Use the custom-agent reference to select only necessary tools. Explain how MCP tools would be approved and how effective capabilities would be verified.

**Evidence:** versioned profiles or tabletop YAML, permission matrix, misuse test cases.

### Lab 3 — Failure-aware CI invocation

Design a repository-scoped CI task with explicit timeout, concurrency behavior, read/write permissions, retry classification, artifacts, and a protected merge gate. Inject a deterministic test failure, an authorization denial, and a simulated transient fetch failure; verify different responses.

**Evidence:** workflow or pseudocode, run logs, failure classification, retained artifacts.

### Lab 4 — Durable checkpoint and drift recovery

Create a checkpoint after planning, then change the base branch before resume. Detect the SHA mismatch, identify invalidated assumptions, update the plan, and rerun applicable validation without repeating an external side effect.

**Evidence:** before/after checkpoint, drift decision, revised plan, idempotency design.

### Lab 5 — Evaluation and root-cause analysis

Build ten task cases: normal, ambiguous, stale context, prompt injection in tool output, permission denied, tool timeout, concurrent edit, malformed output, hidden test failure, and irreversible request. Define expected outcomes and prohibited behavior, run the agent, classify failures, change one control, and rerun.

**Evidence:** versioned evaluation set, results, root-cause table, regression comparison.

### Lab 6 — Multi-agent coordination tabletop

Decompose a three-file change among two workers and an integrator. Then introduce one shared-file collision and one contradictory source. Practice ownership enforcement, conflict detection, arbitration, handoff, and recovery.

**Evidence:** task graph, ownership map, handoff manifests, conflict-resolution record.

### Lab 7 — Guardrail bypass tests

Attempt to induce an agent to edit a protected path, expose a fake secret, call an unapproved endpoint, skip tests, and perform a high-impact action without approval. Confirm capability controls block the action and logs explain the decision without leaking sensitive values.

**Evidence:** test cases, policy decisions, redacted logs, corrective actions.

---

## Quick review checks

1. Why is a branch boundary necessary but insufficient isolation?
2. What makes a plan inspectable and enforceable rather than decorative?
3. When should a retry become an escalation?
4. How do memory and execution state differ?
5. What evidence detects context drift before resume?
6. Why can an allowlisted MCP server still return unsafe content?
7. Which evaluation signals reveal a technically correct but operationally poor result?
8. How do you distinguish reasoning, context, tool, permission, and coordination failures?
9. When is parallel review worth its cost?
10. What must a handoff include to avoid blind trust in a summary?
11. Which actions require human judgment even if an agent can technically execute them?
12. Why are instructions, permissions, gates, monitoring, and recovery separate guardrail layers?

## Readiness checklist

- [ ] I can map every published objective group to a section and lab.
- [ ] I can turn an ambiguous prompt into a bounded task contract.
- [ ] I can separate plan creation, plan validation, and action authorization.
- [ ] I can select tools and MCP capabilities using least privilege.
- [ ] I can compare local, cloud-agent, and CI execution constraints.
- [ ] I can classify transient, deterministic, authorization, conflict, policy, and partial-side-effect failures.
- [ ] I can define memory scope, expiration, provenance, correction, and deletion.
- [ ] I can create a durable checkpoint and respond to context drift.
- [ ] I can define functional, quality, operational, behavioral, and user-value evaluation signals.
- [ ] I can tune one layer and demonstrate whether it improved the evaluation set.
- [ ] I can choose and govern a multi-agent topology with isolation, handoffs, arbitration, and recovery.
- [ ] I can design layered guardrails and meaningful human intervention.
- [ ] I can explain residual uncertainty and current product limitations without presenting them as confirmed exam scope.

## Source map and volatility watch

| Need | Primary source |
|---|---|
| Exam authority and current domains | [Official GH-600 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-600) |
| Beta credential status | [Agentic AI Developer certification](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-developer/) |
| Official training sequence | [GH-600 course](https://learn.microsoft.com/en-us/training/courses/gh-600t00), [Part 1](https://learn.microsoft.com/en-us/training/paths/gh-developing-agentic-systems-1), and [Part 2](https://learn.microsoft.com/en-us/training/paths/github-agentic-systems-part-two/github-agentic-systems-part-two) |
| Current agent surfaces | [GitHub agent concepts](https://docs.github.com/en/copilot/concepts/agents) |
| Custom profile and tools contract | [Custom agents configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration) |
| Hooks and environment-specific behavior | [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference) |
| Enterprise agent policy/control plane | [Agent management for enterprises](https://docs.github.com/en/copilot/concepts/enterprise/agent-management) |
| Preview repository automation | [Creating GitHub Agentic Workflows](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows) |
| Workflow isolation controls | [Workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) and [deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) |

**VERIFY CURRENT before the exam:** beta status and scoring timeline; objective revision date and weights; available exam languages and booking terms; product/plan availability; preview versus GA status; agent, hook, memory, MCP, workflow, and enterprise-policy behavior; supported tools and configuration syntax. When sources conflict, preserve the discrepancy, prefer the narrowest authoritative source for the decision, and record what still needs validation.

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Start with the current official paths, then use documentation and this guide's labs to close specific gaps. Times are approximate reading or module time; note-taking, setup, repetition, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — Developing in Agentic AI Systems Part 1](https://learn.microsoft.com/en-us/training/paths/gh-developing-agentic-systems-1) | Free; account optional for reading | About 2 hours 45 minutes | Official architecture, SDLC, tool, MCP, and execution-environment sequence |
| [Microsoft Learn — Developing in Agentic AI Systems Part 2](https://learn.microsoft.com/en-us/training/paths/github-agentic-systems-part-two/github-agentic-systems-part-two) | Free; account optional for reading | About 3 hours 5 minutes | Official multi-agent, memory/state/evaluation, guardrail, and operations sequence |
| [GH-600 course hub](https://learn.microsoft.com/en-us/training/courses/gh-600t00) | Free syllabus; instructor-led delivery varies | About 30 minutes to map the syllabus; course delivery varies | Use to confirm the current role, prerequisites, and official learning sequence |
| [GitHub agent concepts](https://docs.github.com/en/copilot/concepts/agents), [custom-agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration), and [hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference) | Free | Select about 3–6 hours by gap | Current product depth; client, plan, preview, syntax, and policy behavior can change |
| [Creating GitHub Agentic Workflows](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows) | Free; hands-on use requires supported tools/accounts | About 1–2 hours for reading and a disposable-repository exercise | Useful CI integration practice, but public preview and adjacent to the durable objective rather than permanent syntax authority |
| This guide's seven labs | Free; some product features need an eligible account | About 7–14 hours | Evidence-first practice; use tabletop substitutes where a licensed or enterprise feature is unavailable |

No exact third-party GH-600 course or practice product was promoted in the September 7 review. That is a current catalog gap, not a claim that none exists. Avoid products centered on “real,” recalled, or leaked questions, and recheck all beta-alignment claims against the official study guide.
