---
exam_code: C3000-006
vendor_id: ibm
official_blueprint: https://www.ibm.com/training/credentials/getExam/C3000-006
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# C3000-006 IBM Bob v2 Developer Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Original study material checked against IBM's public objectives on October 28, 2026. This is unofficial and may contain errors. The [official exam record](https://www.ibm.com/training/credentials/getExam/C3000-006) is authoritative. Product labs below are proposed exercises; they have not been executed in Bob.

**VERIFY CURRENT — assessment contract:** IBM Certified Bob v2 Developer – Associate, credential **C9010800**, requires exam **C3000-006**. IBM lists Live status, 42 questions, 29 correct to pass, 90 minutes, English, and US$200. No prerequisite exam, replacement, or withdrawal was listed in the public exam record when checked. Software development, Git, basic AI/LLM knowledge, and CI/CD familiarity are recommended preparation. See the [certification page](https://www.ibm.com/training/certification/ibm-certified-bob-v2-developer-associate-C9010800) for current booking and preparation resources.

**Preparation resources:** That certification page provides IBM's official **24-page study guide**, a sample test, and an assessment-exam route. Open PDF downloads through the page: its generated download URLs expire. The sample test is linked for independent use; none of its questions or answers is reproduced here.

**VERIFY CURRENT — product version:** The [Bob IDE documentation](https://bob.ibm.com/docs/ide) says support for IDE 2.0.1 ends **October 31, 2026**, and instructs users to upgrade to **2.0.2 or later**. Use the [installation instructions](https://bob.ibm.com/docs/ide/getting-started/install) for your platform. This is a client support notice, not an announced exam revision or retirement.

## How to use this guide

For exam essentials, learn the objective map, the decision table in section 3, and the answered scenarios. For deeper understanding, trace a request from context through tools and approvals to verified changes. For practical work, use a disposable repository and save the evidence requested by each lab.

> **About related items:** A `Related item:` callout supplies supporting professional context; it does not predict undisclosed exam content.

## Objective map

The [official exam objectives](https://www.ibm.com/training/credentials/getExam/C3000-006) contain 52 public items in six domains. Weights sum to 100%; they are not a guarantee of an exact question count per section.

| Official domain | Weight | Coverage in this guide |
|---|---:|---|
| Concepts | 17% | Section 1: prompts, project initialization, MCP, skill structure; labs 1–2 |
| Bob Core Features | 23% | Section 2: files, packages, modes, models, Shell, architecture, deployment, analytics, context, rules; labs 1–5 |
| Bob Use Cases | 19% | Section 3: planning, literate coding, customization choices, delegation, modernization, agents, debugging and review; labs 3–6 |
| Bob Configuration | 17% | Section 4: tools, limits, mentions, extensions, MCP, custom modes/skills/rules and PRs; labs 2–5 and 8 |
| Bob Accounts | 8% | Section 5: Bobalytics, API authentication, Enterprise, Bobcoins and tokens; labs 5 and 7 |
| Bob Security | 16% | Section 6: permissions, context poisoning, project restrictions, ignore files, approvals and recovery; labs 1, 6 and 8 |

The [dated research record](../docs/research/2026-10-28-ibm-bob-certification-intake.md) maps each individual objective and records evidence limits.

## 1. Concepts

### Effective prompts and project initialization

A useful prompt names the outcome, relevant code, constraints, and evidence of success. Give a role only when it changes the work; add an example when an edge case or output format is ambiguous. IBM's [prompting tutorial](https://bob.ibm.com/docs/ide/tutorials/write-effective-prompts) explains how to supply specific, bounded requests.

**Original example:** “Review `src/discount.py` and its tests. Explain why a zero-price order fails. Propose a change that preserves the public function signature. Add cases for zero and negative input, run the existing tests, and report their results. Ask before changing dependencies.” This defines a small, reviewable task and leaves a measurable result.

Use project initialization to establish the repository's purpose, setup, test commands, style, and constraints. IBM documents `/init` and a root `AGENTS.md` in [Start a project](https://bob.ibm.com/docs/ide/tutorials/start-a-project). Inspect generated instructions before trusting them: an inferred test command may be wrong. Keep standing instructions short; put transient logs and incident details in the current task.

### MCP and skill structure

MCP connects Bob to tools and services beyond its built-in capabilities. Bob hosts a client that communicates with a server exposing tools; a documentation search server and a ticket-writing server confer different capabilities. Connection does not establish authorization for every action. See [Using MCP in Bob](https://bob.ibm.com/docs/ide/configuration/mcp/mcp-in-bob).

A skill packages a repeatable procedure. **VERIFY CURRENT — file layout:** project skills live under `.bob/skills/<skill-name>/SKILL.md`; global skills live under `~/.bob/skills/`. A project skill with the same name takes precedence. YAML front matter supplies `name` and a useful `description`; the body supplies instructions. Supporting templates or scripts can sit beside it. Bob selects relevant skills from descriptions and loads the instructions on demand. See [Skills](https://bob.ibm.com/docs/ide/features/skills).

An original, minimal skill body might ask Bob to inspect changed API endpoints, compare request/response contracts, identify compatibility risks, and report file locations. Test its description against both a relevant request and an unrelated request. A skill that activates constantly adds noise; a missing or vague description may prevent useful activation.

## 2. Bob core features

### Files, tools, and default modes

Bob can inspect a repository, create or edit files, execute commands, and use external tools. Read access supplies evidence; edit access changes artifacts; execution runs programs. Ask which capability a task needs before granting it. The [tool reference](https://bob.ibm.com/docs/ide/core-concepts/tools) describes the available actions.

**VERIFY CURRENT — default mode behavior:** [Modes](https://bob.ibm.com/docs/ide/features/modes) describes Agent for implementation, Plan for analysis and design, and Ask for explanations. Plan currently includes an edit capability; Ask includes MCP and permitted exploration subagents. Custom definitions can override built-in modes. Therefore, a mode name describes a workflow and is insufficient evidence that every side effect is impossible. Inspect configured tool groups and approvals.

| Need | Starting mode | Evidence to request |
|---|---|---|
| Understand existing behavior | Ask | Relevant files, explanation and uncertainty |
| Compare design options | Plan | Assumptions, dependencies, risks and implementation steps |
| Implement an approved change | Agent | Diff, test results and remaining limitations |

### Architecture, model routing, and deployment

IBM's [Bob v2 announcement](https://bob.ibm.com/blog/bob-v2-release-announcement/) separates the **agent**, which performs reasoning and code generation; the **harness**, which supplies shared authentication, logging, feature flags and telemetry; and **clients**, such as IDE and Shell, through which users interact. Improving a prompt does not repair a missing permission or disconnected server.

IBM's official preparation PDF, available through the [certification page](https://www.ibm.com/training/certification/ibm-certified-bob-v2-developer-associate-C9010800), describes SaaS model selection as automatic routing according to task complexity, capabilities, context and cost. **VERIFY CURRENT:** do not memorize a fixed model roster or assume every deployment permits manual model selection. Efficient routing chooses suitable resources; it does not establish the correctness of the output.

**VERIFY CURRENT — hybrid deployment:** [Self-hosted Bob](https://bob.ibm.com/docs/ide/enterprise/on-premises/overview) runs its backend on customer-managed Red Hat OpenShift while retaining IDE/Shell clients. IBM-managed SaaS and self-hosted operation place infrastructure ownership in different hands. For hybrid designs, identify client location, backend location, inference endpoints, network routes, identity and data boundaries. Installing a local IDE alone does not establish local inference or an air-gapped deployment. Do not assume identical SaaS and self-hosted feature availability.

### Premium packages and SDLC work

Bob supports understanding code, planning, generation, modification, testing, documentation and workflow automation. Match the task to evidence: a generated test file is weaker evidence than a recorded passing run; generated architecture needs comparison with actual dependencies.

[Premium Packages](https://bob.ibm.com/docs/ide/premium-packages/pkg-index) add specialized domain workflows. **VERIFY CURRENT:** the current overview lists Java modernization, IBM i, IBM Z and DevSecOps offerings. Select one for relevant platform expertise, not simply because the project uses code. Package entitlement and prerequisites need separate confirmation. A migration should preserve behavior with characterization tests before attempting framework or runtime upgrades.

### Bob Shell and code functions

[Bob Shell](https://bob.ibm.com/docs/shell) brings agentic development to terminal workflows. Prefer the IDE when visual diffs, selected code and interactive navigation help; prefer Shell when terminal context or repeatable automation is central. Interactive sessions allow iterative diagnosis; non-interactive runs need explicit scope, authentication, limits and inspectable results. **VERIFY CURRENT — syntax:** consult [interactive sessions](https://bob.ibm.com/docs/shell/getting-started/start-bobshell-interactive) and [non-interactive sessions](https://bob.ibm.com/docs/shell/getting-started/start-bobshell-non-interactive) before copying commands into automation.

The exam's “Code Functions” objective concerns editor assistance, not serverless functions. [Code actions](https://bob.ibm.com/docs/ide/features/code-actions) can send selected code with its location to Bob for explanation or improvement through the lightbulb, context menu or command palette. [Literate coding](https://bob.ibm.com/docs/ide/features/literate-coding) starts with instructions near the intended implementation. In either case, inspect the resulting diff and run checks; editor convenience does not validate semantics.

### Context, rules, and usage

The context window is the model's active working material. It includes system instructions, tool definitions, MCP descriptions, rules, loaded skills and messages. File reads, mentions and command results contribute to the transcript; the last typed prompt is only part of the input. IBM's [context management guide](https://bob.ibm.com/docs/ide/core-concepts/context-window-management) describes the breakdown and lossy compaction. **VERIFY CURRENT:** inspect the actual usage indicator rather than relying on a remembered numeric limit.

Use targeted searches, narrow mentions, concise rules and fresh tasks for new goals. More connected tools can increase overhead before useful work begins. A long history can preserve abandoned assumptions and make each later request more expensive. Check the resulting code against tests after compaction.

[Custom rules](https://bob.ibm.com/docs/ide/configuration/rules) standardize recurring expectations. **VERIFY CURRENT — scope:** global rules use `~/.bob/rules/`; workspace rules use `.bob/rules/`; mode-specific directories use `.bob/rules-<slug>/`. Project `AGENTS.md` is normally loaded as well. Workspace rules can override global rules. These are model instructions; use tool restrictions and operating-system permissions to enforce access boundaries.

[Bobalytics](https://bob.ibm.com/docs/ide/features/bobalytics) helps relate adoption, code contribution and spend. Section 5 explains interpretation; neither a high contribution percentage nor low consumption establishes code quality.

## 3. Bob use cases

### Choose the right customization

| Mechanism | Use when | Common mistake |
|---|---|---|
| `AGENTS.md` | A newcomer needs stable repository setup and working conventions | Filling it with temporary debugging output |
| Rules | An expectation should apply repeatedly at global, project or mode scope | Treating prose as an access-control system |
| Mode | A role or tool capability set should change | Inferring safety from its display name |
| Skill | A repeatable procedure is relevant only to certain requests | Using a vague activation description |
| Hook | A lifecycle event should run a configured command | Forgetting the hook itself executes code |

See [rules](https://bob.ibm.com/docs/ide/configuration/rules), [custom modes](https://bob.ibm.com/docs/ide/configuration/custom-modes), [skills](https://bob.ibm.com/docs/ide/features/skills) and [lifecycle hooks](https://bob.ibm.com/docs/ide/configuration/lifecycle-hooks). **VERIFY CURRENT:** review hook event names and configuration before use. A hook can log, add context or block work according to its implementation; an untested hook is not evidence that a policy is enforced.

### Plan, implement, debug, and modernize

For a larger change, first ask Bob to identify the entry point, data flow and dependencies. Compare alternatives against requirements, failure behavior, deployment and testability. Refine the plan before applying changes. The [project tutorial](https://bob.ibm.com/docs/ide/tutorials/start-a-project) supports this progression from repository context to an implementation task.

**Original worked example:** a service duplicates discount calculations in two endpoints. Ask for call sites and existing tests, then a plan for extracting one function. Add boundary tests before refactoring, update each caller, and run the tests. If an endpoint changes behavior unexpectedly, compare inputs and requirements before accepting the generated patch. Documentation should explain the final behavior, not an abandoned plan.

For literate coding, specify behavior in comments where code belongs, including edge cases and exceptions. Review the generated implementation against the comments and independent checks. For modernization, first capture existing behavior; change one compatibility boundary at a time and retain an executable rollback strategy. [Literate coding](https://bob.ibm.com/docs/ide/features/literate-coding) and [Premium Packages](https://bob.ibm.com/docs/ide/premium-packages/pkg-index) provide the relevant product context.

### Specialized tools, agents, and delegated work

Bob can build an agent application, but Bob and that application's runtime are different systems. IBM's [agent and MCP tutorial](https://developer.ibm.com/tutorials/build-agents-mcp-tools-watsonx-orchestrate-using-bob/) shows generating tools, testing an MCP workflow and importing an agent into watsonx Orchestrate. Use this as optional implementation practice. Verify tool schemas, failure handling, credentials and deployment separately; a plausible generated YAML file does not prove the agent works.

Use a specialized tool when it supplies necessary evidence or capability, such as documentation search or a controlled test runner. Avoid adding an integration for a task that a bounded file read can complete. Every connection adds permissions, dependencies and context overhead.

[Subagents](https://bob.ibm.com/docs/ide/features/subagents) handle focused work in separate contexts and return summaries. Subtasks have a visible, interactive conversation for work needing dedicated tracking. **VERIFY CURRENT:** allowed subagent types depend on mode, and history must be supplied deliberately when needed. Give each delegated task a clear input, scope and expected result. Independent research can run concurrently; overlapping edits require coordination and validation. A summary can omit assumptions, so request the evidence needed to assess it.

### Code review and Bob Findings

**VERIFY CURRENT — review workflow:** [Code reviews](https://bob.ibm.com/docs/ide/features/code-reviews) documents `/review`, comparison branches, optional uncommitted changes and the Bob Findings panel. Select the correct base before interpreting findings. A review against an old or incorrect branch answers the wrong question. GitHub issue validation is a separate capability from branch comparison.

Inspect findings in code, fix useful ones, justify dismissals, and rerun relevant checks. IBM describes review analysis as using auto-approval; do not assume every analysis step will request confirmation. Review output is an additional signal alongside tests and human review.

## 4. Bob configuration

### Tool groups, task limits, mentions, and extensions

Differentiate Read, Execute, Subtask and MCP tools by their effects: inspection, process execution, delegated conversation and external capability. Inspect the actual tool call when a permission prompt appears. A harmless-looking description can conceal an overbroad command or external write. See [Tools](https://bob.ibm.com/docs/ide/core-concepts/tools).

The exam blueprint includes configuring task limits for Bobcoins. **VERIFY CURRENT:** inspect the current task's spending control, record its value, and verify what happens at the threshold in your installed version. The [Shell automation documentation](https://bob.ibm.com/docs/shell/getting-started/start-bobshell-non-interactive) provides `--max-cost` and `--max-turns` controls; check their units and behavior before use. Task budget, context-window capacity, and subscription overage are separate controls. The official preparation PDF's configuration discussion emphasizes context management and does not establish a universal task-budget UI or enforcement rule; confirm these in the installed client.

[Context mentions](https://bob.ibm.com/docs/ide/features/context-mentions) attach files, locations or diagnostic information to a request. Prefer the relevant file or selection over a whole repository. Confirm the file exists and that the mentioned evidence addresses the current bug.

**More research needed — next pass: marketplace installation.** The blueprint explicitly includes downloading extensions from a marketplace. However, IBM's official preparation PDF says the existence of a general-purpose VS Code Marketplace/Open VSX browser inside Bob IDE needs confirmation with the product team. It describes Premium Packages and the Shell Companion as related mechanisms; those do not establish a general extension marketplace. Do not invent a menu path or equate these mechanisms. Inspect the installed version and current documentation, review publisher and permissions, and record what is actually supported. This objective's general marketplace workflow remains unverified.

### MCP deployment and tool development

| Transport | Operating model | What to check |
|---|---|---|
| STDIO | Bob launches a local server process | Executable, arguments, environment, filesystem rights and protocol output |
| Streamable HTTP | Bob connects to a service endpoint | URL, TLS, authentication, per-user authorization and service health |

**VERIFY CURRENT — transport discrepancy:** the [MCP transport page](https://bob.ibm.com/docs/ide/configuration/mcp/server-transports) initially lists three transports, but its detailed **SSE transport (removed)** section says Bob no longer supports standalone HTTP+SSE. Use STDIO or Streamable HTTP for current configurations. SSE streaming inside Streamable HTTP remains distinct from the removed two-endpoint transport. Old examples need migration; do not assume an automatic fallback.

For a custom tool, define its name, input schema, bounded behavior, output and failure response. Validate inputs on the server and authorize the action there. Register it through the appropriate MCP configuration, confirm discovery, test a valid request and a rejected request, and inspect logs. Use project scope for project-specific integrations. The [MCP setup guide](https://bob.ibm.com/docs/ide/configuration/mcp/mcp-in-bob) explains server management; the [IBM agent tutorial](https://developer.ibm.com/tutorials/build-agents-mcp-tools-watsonx-orchestrate-using-bob/) offers a larger example.

### Custom modes, skills, and rules

**VERIFY CURRENT — original configuration example:** [Custom modes](https://bob.ibm.com/docs/ide/configuration/custom-modes) documents project `.bob/custom_modes.yaml` and global `~/.bob/settings/custom_modes.yaml`. A mode below grants read access and limits the edit tool to Markdown paths:

```yaml
customModes:
  - slug: study-docs
    name: Study Documentation
    roleDefinition: Write documentation supported by the current project.
    groups:
      - read
      - - edit
        - fileRegex: '.*\.md$'
          description: Markdown files
```

No execute, MCP or mode-switch group is included. Check the installed parser and effective permissions before use; file restrictions on the edit tool do not create an operating-system sandbox. Invalid group names or regular expressions can prevent intended configuration from loading. Use unique slugs and test allowed and denied paths.

Create skills with explicit activation descriptions and small instructions, then verify that the project skill is discovered. Put shared stable requirements in project rules and personal preferences in global rules. If behavior conflicts, inspect loaded scopes and mode-specific instructions instead of repeatedly expanding the prompt. See [Skills](https://bob.ibm.com/docs/ide/features/skills) and [Custom rules](https://bob.ibm.com/docs/ide/configuration/rules).

### Pull requests

[PR generation](https://bob.ibm.com/docs/ide/features/pull-requests) uses branch changes, commit history and repository templates to draft a title and description. **VERIFY CURRENT:** IBM documents committed branch changes and remote push access as prerequisites. Inspect the selected remote/base, generated text and actual diff before submitting. Include tests actually run and unresolved limitations. Drafting a PR description and creating a remote PR are separate actions; lab 8 ends before publishing.

## 5. Bob accounts

### Bobalytics and Enterprise administration

**VERIFY CURRENT — entitlement and visibility:** [Bobalytics](https://bob.ibm.com/docs/ide/features/bobalytics) is currently documented as Enterprise-only. Its main measures include adoption, Bob's contribution to committed code, and Bobcoin spend. Use comparable time ranges and team filters. IBM describes anonymized team views and users seeing their own individual data; an admin role does not imply unrestricted access to another user's personal analytics.

**Original example:** average daily active users of 12 across 20 seats gives 60% adoption. If Bob-authored committed lines are 300 of 1,000 in an eligible comparison, the simple contribution ratio is 30%. These synthetic calculations illustrate measures; actual analytics include documented exclusions. Neither ratio says whether the changes were correct. High spend with little committed code might reflect valuable investigation or inefficient work: inspect the task mix before deciding.

The [Enterprise overview](https://bob.ibm.com/docs/ide/enterprise/enterprise-index) describes shared Bobcoin pools, user/seat management, spending controls, usage visibility, scaling and support. **VERIFY CURRENT:** SSO, deployment options and feature availability must be checked for the purchased plan. [Group policies](https://bob.ibm.com/docs/ide/security/group-policies) provide organizational controls; local configuration does not establish the final effective policy.

### API authentication

**VERIFY CURRENT — API key types:** [API keys](https://bob.ibm.com/docs/ide/account/api-keys) distinguishes General keys, scoped to a subscription instance, from Inference keys, scoped to an instance and team for inference. General inference requests additionally require team context; Inference keys already bind that context. Verify the current endpoint and headers rather than guessing them.

Users manage their own keys; instance admins can list and revoke keys across the instance. Store secrets in the approved secret store for automation, keep them out of prompts and committed configuration, and revoke unused or exposed credentials. For Shell automation, follow the [non-interactive session instructions](https://bob.ibm.com/docs/shell/getting-started/start-bobshell-non-interactive). An inference-only key should not be assumed to authorize every platform-management operation.

### Bobcoins, tokens, and spending controls

[Bobcoins](https://bob.ibm.com/docs/ide/account/bobcoins) are IBM's consumption/billing units; tokens are model input/output units. They are not interchangeable counts. Different operations and models can consume resources differently. Long context, excessive tool descriptions and repeated failed attempts can increase consumption even when the last prompt is short.

**VERIFY CURRENT:** allocations, pack prices, expiry, overage rates and plan terms change. Verify the current subscription before enabling overage. Separate a task spending limit from account-level capacity and shared organization budgets. Use the task usage display for current work and eligible analytics for trends.

## 6. Bob security

### Permissions and approval scope

**VERIFY CURRENT — approval controls:** [Auto-approve](https://bob.ibm.com/docs/ide/features/auto-approving-actions) distinguishes task tool-group settings, global command prefixes, task/global MCP tool allowances, and a one-time approval. New tasks inherit global defaults; changing the active task does not automatically change those defaults. Turning on MCP does not grant blanket approval for all MCP tools. Inspect each tool's allowance separately.

For command auto-approval, prefer narrow prefixes such as `git status` over a broad `git` rule. The documentation describes matching each segment of pipelines/chained commands and blocking denied commands. Mode tool availability, approval settings, command policy and organizational policy answer different questions. Review effective restrictions for the project, including [group policies](https://bob.ibm.com/docs/ide/security/group-policies).

### Ignore files and project boundaries

**VERIFY CURRENT — original example:** [Ignoring files](https://bob.ibm.com/docs/ide/configuration/bobignore) documents `.bobignore` at the workspace root with Git-style patterns:

```text
.env
.env.*
private-fixtures/
*.pem
```

Use synthetic files to verify the patterns before bringing sensitive material into a workspace. Ignore rules limit Bob's file-tool access in the workspace; they do not constitute an OS sandbox or automatically constrain every command or external server. Use filesystem permissions, scoped credentials and isolated workspaces where appropriate. Ignore configuration also does not remove information already pasted into a conversation.

### Context poisoning and secure development

[Context poisoning](https://bob.ibm.com/docs/ide/core-concepts/context-poisoning) includes stale, wrong or irrelevant information continuing to shape later work. Symptoms include drift, repeated bad edits, looping and forgetting the original goal. Reset the task with a concise statement of the verified facts and open questions, then inspect code and tests. Keep standing rules small and avoid indiscriminate log or repository ingestion.

> **Related item:** Untrusted repository text or tool output may also contain instructions intended to redirect an agent. Treat such content as evidence to inspect, not authority to expand permissions or reveal secrets. Context cleanup helps quality; permission boundaries and tool authorization still need enforcement.

Secure development means reviewing diffs and generated commands, validating inputs, retaining required checks, protecting secrets and minimizing tool capabilities. A green test run supports the tested behaviors; it does not prove the whole application is secure. An unexpected external action requires checking its remote effect, not merely reverting local files.

### Rollback and recovery

**VERIFY CURRENT:** [Rollback](https://bob.ibm.com/docs/ide/features/rollback) captures task-related file snapshots separately from main version control. Inspect the changed files and restore the appropriate snapshot when a proposed edit fails. Restoration can overwrite unsaved work; preserve needed work first. Do not assume it captures manual edits made outside tasks or reverses database writes, messages or deployments. Retain Git history and service-specific recovery procedures.

## Hands-on labs

These are **proposed, unexecuted product exercises**. Use a disposable repository containing synthetic data. Bob access, an eligible plan or additional services may be required. Record client version, mode, effective permissions, expected result, observed result and limitations. Do not report an expected result as a successful run.

| Lab | Exercise | Evidence and success condition |
|---|---|---|
| 1. Project and scope | Initialize a toy repo; review `AGENTS.md`; add ignore patterns for harmless secret-like fixtures; ask for a code explanation | Correct setup/test commands, scoped prompt, and observed file-tool access restrictions; no real secrets |
| 2. Skill, rule and mode | Add a project review skill, a concise rule and the Markdown-only mode above; test relevant/unrelated skill prompts and allowed/denied edits | Discovered skill, recorded activation behavior and effective tool restrictions; any unexpected access documented |
| 3. Plan to implementation | Define a discount function with zero/negative cases; request a plan, implement in a separate step, then use literate coding for a small helper | Original tests, reviewed diff, actual test output and updated explanation |
| 4. MCP contract | Implement one read-only tool over synthetic fixtures, register a local server, test discovery and malformed input; compare the remote deployment requirements | Tool schema, successful call, rejected invalid input and logs; no deployment to production |
| 5. Context and costs | Compare a targeted file mention with a broad context request on the same synthetic problem; inspect the usage breakdown and current task limit | Actual observations of context and consumption; no assumed fixed token-to-Bobcoin conversion |
| 6. Review and recovery | Introduce a reversible bug; select the correct base in Code Review; inspect Findings; fix and retest; practice snapshot restore after preserving work | Correct comparison, justified finding disposition, test result and observed restoration limits |
| 7. Account tabletop | With an eligible account inspect analytics, budget and key-management controls; otherwise draw the workflow using synthetic values | Distinguish individual/team visibility, key types and spending scopes; no real key copied into notes |
| 8. Delivery controls | Compare task/default approvals, test narrow harmless command prefixes, inspect a hook definition, and draft a PR description locally | Recorded approval scopes and accurate PR text; stop before publishing or changing shared settings |

For broader agent development, optionally follow the [IBM Developer tutorial](https://developer.ibm.com/tutorials/build-agents-mcp-tools-watsonx-orchestrate-using-bob/). Its services, model choices and deployment steps need a separate environment check.

## Original scenario checks with answers

These independently written checks are not IBM assessment items.

1. **A one-line prompt is expensive. Why?** Existing rules, schemas, history, file reads and tool results can dominate input. Inspect the context breakdown before shortening the final sentence.
2. **You need an explanation without code edits. Which mode starts the work?** Ask. Still inspect MCP tools, overrides and approvals to understand effective capability.
3. **A Plan session can edit. Is that automatically a defect?** No. Current Plan includes editing capability. Inspect what it may edit and whether implementation was authorized.
4. **The same review procedure applies only to API work. Rule or skill?** A focused skill with a clear activation description; stable repository-wide requirements belong in rules or `AGENTS.md`.
5. **A tool connects over HTTP but uses old separate SSE endpoints. What next?** Check transport compatibility and migrate to Streamable HTTP or local STDIO. An SSE response inside Streamable HTTP is different.
6. **MCP is enabled, yet an action asks for approval. Why?** Group availability and individual tool auto-approval are separate controls.
7. **Does approving one command permanently permit its executable?** No. One-time, task-level and global command allowances have different scopes.
8. **An ignored file appears in command output. What was misunderstood?** File-tool ignore rules are not an OS sandbox and do not erase data already present in context.
9. **An admin wants another user's personal analytics. Is Enterprise enough?** No. Current docs distinguish anonymized team insights from the individual user view.
10. **Are 1,000 tokens equal to 1,000 Bobcoins?** No. Tokens measure model text processing; Bobcoins aggregate billable resource consumption.
11. **An automation only needs inference. Which key deserves consideration?** An Inference key scoped to the instance/team. Verify endpoint support and avoid broader credentials without need.
12. **A subagent needs a decision from earlier in the chat. Will it know automatically?** Do not assume so. Supply required context and request evidence with its summary.
13. **Bob Findings is empty. Is the release safe?** That conclusion is unsupported. Verify comparison scope, exclusions, tests, requirements and human review.
14. **Rollback restored code after a remote write. Is recovery complete?** No. Check and recover the external system separately.
15. **A modernization patch compiles but changes rounding behavior. Accept it?** Compare the required behavior and characterization tests; compilation does not establish semantic compatibility.
16. **IDE support changes on October 31. Does the exam retire then?** No such conclusion follows. Client support and exam lifecycle are separate evidence streams.

## Readiness checklist

- I can turn a request into a bounded prompt with measurable acceptance evidence.
- I can distinguish `AGENTS.md`, rules, modes, skills, hooks, subtasks and subagents.
- I can explain agent/harness/client roles, model routing and deployment ownership.
- I can choose IDE or Shell and identify the controls automation needs.
- I can configure a scoped MCP integration and distinguish current transport support.
- I can inspect context overhead, task limits, Bobcoins and Enterprise analytics without confusing their meanings.
- I can explain approval scopes, ignore-file limitations, context poisoning and recovery boundaries.
- I can review a diff, interpret a finding, test a change and describe evidence limits honestly.
- I have compared all six domains with the current official objectives and identified where more hands-on practice is needed.

## Places to learn

This is a curated starting point, not a complete list or a requirement to consume every resource. Times are **author estimates** based on reading scope and proposed practice unless explicitly stated otherwise; they are not IBM-published runtimes. **VERIFY CURRENT:** access, versions, downloads and plan entitlements can change.

| Resource | Access | Estimated time |
|---|---|---|
| [Official certification page, study PDF and sample test](https://www.ibm.com/training/certification/ibm-certified-bob-v2-developer-associate-C9010800) | Public preparation links; exam/assessment booking separate | About **1–2 hours** for the 24-page study guide and objective mapping; sample-test time not measured |
| [Official machine-readable exam objectives](https://www.ibm.com/training/credentials/getExam/C3000-006) | Public | About **20–30 minutes** to check the six domains and 52 objectives |
| [Bob IDE docs](https://bob.ibm.com/docs/ide) and [Bob Shell docs](https://bob.ibm.com/docs/shell) | Public docs; execution needs Bob access | About **3–5 hours** of selected reading across features, configuration, account and security topics |
| [Prompting tutorial](https://bob.ibm.com/docs/ide/tutorials/write-effective-prompts) and [project initialization tutorial](https://bob.ibm.com/docs/ide/tutorials/start-a-project) | Public docs; Bob access for practice | About **1–2 hours** to read, apply and compare prompts in a toy project |
| [Build AI agents with Bob and watsonx Orchestrate](https://developer.ibm.com/tutorials/build-agents-mcp-tools-watsonx-orchestrate-using-bob/) | Public tutorial; Bob and Orchestrate environment required, terms may involve cost | About **2–4 hours** for setup, MCP-tool tests and deployment practice; optional and not runtime-validated here |
| [Meet Bob: external-audience workshop](https://ibm.github.io/intro-bob-workshop/lab-6/) | Public materials; Bob access for exercises | **60 minutes**, published guided agenda; separate **30-minute** presentation; prompts, skill setup and role-based practice |
| [IBM Bob Level 3 labs](https://ibm.github.io/bob-l3/) | Public courseware; Bob access; some linked setup routes are employee/partner-specific | About **4–6 hours**, estimated for four modules: assistance, delegation, customization and context/Shell/MCP; verify older setup and trial claims |
| [Galaxium Travels application](https://github.com/IBM/galaxium-travels) | Public repository; local runtimes needed | About **1–2 hours** for setup and code/test inspection; reuse it for several labs rather than adding this time repeatedly; choose the tutorial's branch |
| [IBM Bob demo collection](https://github.com/IBM/bob-demo) | Public Apache-2.0 examples; Bob and demo-specific tooling | About **30–90 minutes per selected demo**, editorial estimate; older five-mode terminology and sample defects require repair, and maintenance is disclaimed |
| [Create and use skills](https://bob.ibm.com/docs/ide/tutorials/use-skills) | Public tutorial; Bob and demo code | About **45–60 minutes** to build a changelog skill and compare explicit/automatic activation; supports Concepts and Configuration |
| [Generate architecture diagrams](https://bob.ibm.com/docs/ide/tutorials/generate-architecture-diagrams) | Public tutorial; Bob, Git and demo code | About **45–90 minutes** to inspect a repository, generate a diagram and compare it with the code; supports planning and code understanding |
| [Build MCP servers with Bob](https://bob.ibm.com/docs/ide/tutorials/mcp-server-integration) | Public tutorial; Bob and Node.js | About **1–2 hours before repairs**, estimated for planning and a local tool; example helper code is incomplete and prose/code contracts differ; see caveats below |
| [Actor-critic secure-code workflow](https://bob.ibm.com/docs/ide/tutorials/generate-secure-code) | Public tutorial; Bob and specified demo branch | About **1–2 hours** to inspect paired skills and compare generated/reviewed changes; supports security practice, not compliance certification |
| [Getting the Most Out of Bob](https://bob.ibm.com/blog/getting-the-most-out-of-bob/) | Public first-party article | About **20–30 minutes** of reading plus optional **30–60 minutes** of applying its planning/context/verification cycle |
| [Monolith modernization with reusable skills](https://developer.ibm.com/tutorials/ai-assisted-app-mod-workflow/) | Public tutorial; Bob, Neo4j, MinIO and additional tools | About **4–8 hours**, estimated setup and practice; advanced optional depth across skills, MCP and modernization, not a required exam stack |
| Eight original labs in this guide | Disposable repository; account/plan requirements vary | About **8–12 hours** to produce and review the requested evidence; product execution remains pending |

### Additional-source review — October 28, 2026

The ten additional resources above extend the initial documentation set with courses and examples. **VERIFY CURRENT:** these are reading/practice options, and none was executed in this review. The Level 3 setup contains older trial/registration details; use current account terms and installation docs. Galaxium Travels `main` may already contain features an older exercise asks you to add. The demo collection retains older five-mode names; its introductory skill example also has front-matter and script-path defects. Prefer the current skills tutorial when learning the actual file format.

The MCP tutorial's prose asks for `search_papers` with default 5/max 20 results; its code instead names `search_arxiv` and uses default 10/max 50, with XML/formatting helpers omitted. Reconcile and test a contract before treating it as runnable code. The security tutorial is a workflow exercise: instructions and a reviewing model cannot guarantee compliance, and a user-supplied identity header alone does not authenticate a caller. Keep independent tests, scanners and human review.

These supplemental materials do not resolve the general marketplace-browser gap. A PR-review video linked by IBM was inaccessible through the reader and remains in the source-candidate inbox pending content and runtime review.

Avoid sources selling recalled or “actual” exam questions and guaranteed passes. Use public objectives, official preparation and independently written practice to identify understanding gaps.
