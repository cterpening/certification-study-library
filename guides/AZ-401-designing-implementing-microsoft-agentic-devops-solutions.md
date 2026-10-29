---
exam_code: AZ-401
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-29
---

# AZ-401 Designing and Implementing Microsoft Agentic DevOps Solutions Study Guide

> **Independent AI-assisted resource — BETA; sources and objectives checked; human review pending.** Microsoft labels the credential and AZ-401 exam beta. The current [dedicated exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-401/) and [official AZ-401 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401) agree on five DevOps domains. The [credential landing page](https://learn.microsoft.com/en-us/credentials/certifications/agentic-devops-engineer-expert/) currently displays unrelated AB-100 objectives in an “Assessed on this exam” block; use AZ-401-specific sources for scope. The vendor source is authoritative. **VERIFY CURRENT** before scheduling or using Preview/AI features.

**Current baseline, checked October 29, 2026:** Credential and exam are beta; the study-guide page says it was updated October 13, 2026. The exam page lists English, a passing score of 700, delayed beta results, and no retirement date. It does not state an exam duration or item count; Microsoft says exam prices vary by country or region, so check the current local amount when scheduling. No formal prerequisite credential was identified. These are observations, not guarantees; see the [coverage record](../docs/SOURCE-VALIDATION.md#az-401-coverage-record).

## How to use this guide

AZ-401 combines established DevOps engineering with AI-assisted and agentic workflows. Learn the control system first, then decide where an assistant or agent can safely help:

> **About related items:** A **Related item:** callout marks supporting context beyond exact published objective wording; it is useful preparation, not a claim that the item is separately tested.

1. Define owned work and acceptance criteria.
2. Make a reviewed, traceable source change.
3. Build and test reproducibly; retain artifact identity and evidence.
4. Promote the same artifact through protected environments.
5. Expose the change gradually and observe its behavior.
6. Record operational feedback and follow-up work.

At each step identify the human or workload principal, exact permissions, data crossing a boundary, policy that allows the action, evidence retained, and rollback path. An agent suggestion, green pipeline, passing scanner, or healthy dashboard is one signal—not proof that the release is safe.

The official study guide says its bullets illustrate assessment and related topics may appear; English is updated first, and commonly used Preview features may be tested. Do not infer scope from another credential’s prerequisites or a broad agentic-AI course. The credential page’s unrelated AB-100 objective block is documented in the [research report](../docs/research/2026-10-29-az401-refresh.md) and excluded from this exam map.

Use disposable repositories, organizations, projects, and subscriptions for exercises. Agentic MCP tools, GitHub workflows, runners, Azure Monitor, Key Vault, and cloud labs can read or mutate resources and may incur cost. No tenant, Azure resource, MCP server, production pipeline, or beta exam was accessed or executed for this guide.

## Objective map

| Official domain | Weight | Study question |
|---|---:|---|
| Design and implement processes and communications | 15–20% | Can work, decisions, quality and feedback be traced with safe AI assistance? |
| Design and implement a source control strategy | 10–15% | Can the team balance integration speed with policy, permissions, traceability and recovery? |
| Design and implement build and release pipelines | 35–40% | Can the team build, test, protect, promote and operate releases across Azure DevOps and GitHub? |
| Design and implement a security and compliance plan | 15–20% | Are identities, secrets, permissions, scanning and exceptions scoped and evidenced? |
| Implement an instrumentation strategy | 15–20% | Can teams connect delivery signals to workload telemetry and validate AI investigations? |

The full objective snapshot is [stored in the repository](../data/objective-snapshots/az-401-official-objectives.txt). Microsoft’s [AZ-401 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401) and [exam-specific page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-401/) are authoritative. The credential page’s mismatched block is not used as scope evidence.

## 1. Design and implement processes and communications — 15–20%

### Trace work and feedback end to end

A useful work item records an outcome, owner, acceptance criteria, dependencies, risk and operational needs. Link it to repository change, review, tests, package/artifact, release, deployment and incident. Azure Boards can track work while GitHub hosts source; decide which system owns each record and verify integration identity, linking, retries and failure behavior. The [Azure Boards–GitHub integration guidance](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops) describes setup and link constraints.

Design the plan/build/deploy/operate flow around short feedback loops: local checks before commit, CI before merge, environment checks before release, and workload telemetry after deployment. Notifications should identify the affected change, owner, evidence and next action. Do not make a chat post the only incident or approval record.

Translate business KPIs into measures teams can act on. Define population, time window and calculation. Lead time, cycle time, deployment frequency, change failure, recovery time, test reliability and security-fix age can reveal bottlenecks; none should rank individual developers or be optimized alone. An AI-assisted query can draft a report, but validate filters, denominators, missing records and the decision the chart supports.

### Document and integrate with bounded agent authority

AI assistance can draft a README, change log, release note, license inventory, code-owner proposal or process diagram from repository evidence. Require links to source records and review for omissions and invented claims. For each agent, skill or loop, define allowed projects, tools, read/write scope, stop conditions, approvals, logs and rollback. Issue text, pull requests, code comments and tool responses are untrusted input that may contain prompt injection. Start read-only; add a narrow write operation only when an owner can explain and verify its exact side effect.

The [Azure DevOps MCP overview](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops) and [remote server setup](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server?view=azure-devops) distinguish connectivity, OAuth/client support and signed-in user permissions. A configured [GitHub MCP integration](https://docs.github.com/en/copilot/concepts/customizations/mcp) is a tool path, not an authorization grant. **VERIFY CURRENT:** client support, transports, scopes, feature stage and tool names.

**Check yourself:** Given a bug, PR, failed test and release record, trace which work is blocked and whether the release is verified. Propose read-only MCP tools; name the policy and human approval needed before enabling writes.

## 2. Design and implement a source control strategy — 10–15%

| Strategy | Useful when | Main trade-off |
|---|---|---|
| Trunk-based / short-lived feature branches | Frequent integration and small changes | Needs fast checks and incomplete-feature controls |
| Release branches | Several maintained release lines | Adds backport, ownership and security-fix coordination |
| GitHub Flow | Small reviewed changes with continuous delivery | Depends on reliable PR checks and safe deployment |
| Gitflow | Explicit develop/release/hotfix lanes fit the team | Long-lived branches increase merge and patch overhead |
| Git Worktree | Parallel local worktrees help a contributor | Changes local directories, not server authorization or merge policy |

Use review rules and protected branches to enforce approvals, status checks, ownership and merge restrictions. Azure Repos policies and [GitHub protected branches/rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) are server-side controls. Local hooks provide quick feedback but can be bypassed; enforce authoritative checks at the server or in CI. **VERIFY CURRENT:** policy names, plan entitlements and Copilot-specific settings.

Copilot-specific branch controls can request automated code review through user settings or repository/organization rulesets, where available. Treat that review as advisory: GitHub documents that Copilot review does not approve a pull request or request changes. Keep required human approvals and passing status checks as separate merge rules, and verify which rulesets apply to the target branch. A configured review request is not itself a release gate. See [configure Copilot code review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review).

Configure least-privilege repository/project permissions, meaningful tags, code owners and direct links from code/tests to a work item or issue. Preserve code-quality and coverage evidence. A link to an unrelated or mutable work item does not prove acceptance criteria were met.

### Migrate and recover deliberately

Before moving Azure Repos to GitHub, inventory branches, tags, LFS objects, history requirements, permissions, teams, work items/issues, policies, pipelines, webhooks, packages and service connections. Map identities and controls, rehearse, compare refs and artifacts, then cut over with an owner and rollback plan.

Choose recovery by the mistake. For a bad shared commit, `git revert <commit>` adds an inverse change without rewriting shared ancestry. For accidental local edits, inspect `git status` and use `git restore <path>` only when discarding those edits is intended. For a commit no longer on a branch, inspect `git reflog`, then preserve the selected commit with `git branch recovered <commit>` before garbage collection; do not assume reflog is permanent backup. Reset and history rewriting change references or ancestry. Removing a secret from all history requires coordination, backup, cache/artifact review and credential rotation; rewriting commits does not revoke a leaked credential. Practice in a disposable repository with a known-good reference.

**Check yourself:** A local hook is bypassed and a sensitive PR lacks a required check. Which server controls should stop merge? For “undo a shared commit,” “remove a credential from history,” and “recover a deleted local commit,” choose distinct recovery paths and name backup/coordination steps.

## 3. Design and implement build and release pipelines — 35–40%

This is the largest domain. Design one controlled path from source to an immutable artifact, then promote the same artifact through gated environments. Rebuilding per environment makes it harder to prove tested bits are released.

### Packages, tests and quality gates

Choose Azure Artifacts or GitHub Packages based on ecosystem, repository location, feed/view needs, upstream sources, permissions, retention and consumers. Define package and artifact versioning: SemVer communicates compatibility intent; CalVer communicates release date; neither establishes provenance. Link source, dependencies, build identity, test result and artifact digest. Limit feed publishing to stages that need it.

Order tests by cost and signal: local/static checks, unit, integration, then load or environment tests. Decide which failures block promotion, who may grant an exception, and how evidence is retained. Configure test tasks and agents/runners; publish results and coverage, track flaky tests and make failures actionable. A coverage percentage does not prove high-risk behavior was tested.

For a package feed, draw the producer, consumer, upstreams and release boundary. In Azure Artifacts, feeds are storage and permission boundaries; an upstream source lets consumers resolve packages from another feed or public registry, while feed views expose a selected subset such as validated releases. A collaborator-or-higher install can save an upstream package into the feed. Check who may add an upstream, who can save packages, whether upstream ordering is intentional, and whether package lock files pin the dependency graph. Do not confuse a view with a separate feed or assume every reader can import a new upstream package. See [Azure Artifacts key concepts](https://learn.microsoft.com/en-us/azure/devops/artifacts/artifacts-key-concepts?view=azure-devops) and [feed views](https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/views?view=azure-devops).

Keep package identity separate from pipeline-run identity. For each run, record source commit, run/build ID, version, producing pipeline, test results and artifact digest. Promote an artifact with that identity; do not rebuild the package under the same version for each environment. A useful review question is: can the deployment record identify the exact package bytes and the build that produced them? If retention expires the artifact or its provenance, rollback and audit evidence may be lost.

When configuring tests, check the task’s runtime requirements against the selected agent image or self-hosted agent capabilities, then confirm the job actually publishes machine-readable test results and coverage output. In Azure Pipelines, `PublishTestResults` consumes supported result formats; coverage requires a report in a supported format and a publish step. A task that ran tests but published no results leaves the quality gate without inspectable evidence. For a failing sample run, inspect the run’s test tab and coverage report, then identify whether the failure came from test execution, result discovery, format, or publication. See [test result publishing](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-test-results-v2?view=azure-pipelines) and [coverage results](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/codecoverage-for-pullrequests).

Copilot or an MCP-connected agent can draft tests, YAML or queries, but cannot independently make output a trusted release gate. Review generated code/workflow diffs, run checks in the intended isolation boundary, and preserve the pipeline status as decision evidence.

### Azure Pipelines, GitHub Actions and agentic workflows

Select [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops) or [GitHub Actions](https://docs.github.com/en/actions) by repository integration, permissions, runners, connectivity, required tools, licensing, cost and maintenance. Hybrid designs can be useful; explicitly map identities and traceability across systems.

Choose hosted, managed or self-hosted agents/runners by workload and trust boundary. Consider OS, toolchain, network reach, licensing, isolation, persistence, cache, concurrency, cost and host patching. Untrusted PR code must not inherit privileged deployment credentials. Use ephemeral or resettable execution where risk warrants it.

In YAML, make triggers, path filters, job dependencies, parallelism, stages, conditions, templates, parameters and variable scopes explicit. Reuse templates only from trusted, versioned sources. Separate build and deployment permissions. Azure resource approvals/checks are owned by the protected resource; a YAML author cannot remove a resource-owner check by changing YAML. See [Azure approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?tabs=check-pass&view=azure-devops), [protected-resource permissions](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/resources) and [variable/parameter guidance](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?tabs=yaml&view=azure-devops).

For reusable elements, distinguish YAML templates (reusable stages/jobs/steps or variables, parameterized and expanded into a run) from variable groups (shared values governed by Library permissions) and Classic task groups (not supported in YAML). Review template source/version and parameters as code; authorize variable groups per pipeline because an open group can expose secrets to anyone able to change YAML. For a pipeline that builds a GitHub repository, inspect the GitHub service connection/app, CI and PR triggers, status reporting, fork-PR trust boundary, and how the run maps back to the GitHub commit. A PR can change its own YAML, so validate untrusted contributions without exposing deployment credentials. See [variables and variable groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?tabs=yaml&view=azure-devops), [GitHub integration](https://learn.microsoft.com/en-us/azure/devops/cross-service/github-integration?view=azure-devops), and [build GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops).

**Pipeline inspection sequence:** open a representative failed and successful run; compare trigger/commit, agent image or capabilities, resolved template and variables, job dependency graph, test result and coverage publication, artifact name/version/digest, approval/check history, and deployment artifact identity. If a stage waits, distinguish unavailable parallel capacity from an agent whose capabilities do not match the job’s demands. Fresh hosted agents reduce cross-run residue; persistent self-hosted agents require workspace cleanup and patching. See [agent demand and capability matching](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/demands?tabs=yaml&view=azure-devops).

The blueprint includes **GitHub Agentic Workflows**. GitHub’s current [tutorial](https://docs.github.com/en/actions/tutorials/develop-agentic-workflows-in-github-actions) describes Markdown-authored instructions compiled by gh aw into a GitHub Actions workflow. Treat generated YAML as code: inspect token permissions, trigger trust, safe-output restrictions, branch/PR boundaries, generated files and handling of issue/PR text. A model response is not a trusted check or approval. **VERIFY CURRENT:** product stage, commands, events and security model.

### Deployment, IaC and pipeline operations

Choose blue/green, canary, ring, progressive exposure, feature flags or A/B tests by blast radius, traffic control, health signals and rollback speed. Order dependent service/database deployments. Use load balancing, slots/swaps or rolling updates where the application supports them. A database migration may not be safely reversible; prefer expand/contract changes and a tested forward-fix path. Document the hotfix route, resiliency and rollback owner.

Deploy containers, binaries, scripts or database tasks with appropriate integrity checks and permissions. Use IaC such as Bicep for repeatable infrastructure; separate desired configuration from secrets and review the plan/diff before application. Test drift and recovery, not just template syntax.

Monitor failure rate, duration, queue time, flaky tests and deployment outcomes. Optimize cost, elapsed time, performance and reliability together; dropping a security check is not an improvement. Set retention for artifacts and dependencies based on audit, rollback, privacy and storage needs. **VERIFY CURRENT:** retention defaults, runner limits, billing and plan-specific features.

**Check yourself:** Design a multistage pipeline that builds once, publishes an artifact with provenance, runs tests, waits for environment-owner approval, and promotes to a canary. Add a database gate, rollback signal and hotfix route. Inspect a generated agentic workflow for an untrusted-event prompt path or unnecessary write token.

## 4. Design and implement a security and compliance plan — 15–20%

### Identity, authorization and secretless access

Choose an identity for each actor and target. A managed identity is useful for an Azure-hosted workload that can use it. An external GitHub runner generally needs a configured federation path such as OpenID Connect/workload identity federation, not an assumed local managed identity. A service principal is an application identity whose credential lifecycle and permissions must be managed. Scope roles to the repository, environment, service connection and resource that need them.

For GitHub automation, compare GitHub Apps, workflow tokens and personal access tokens by actor, scope, lifetime, permission set and revocation. Prefer short-lived, narrow credentials. Avoid broad PATs for unattended workflows. In Azure DevOps, understand service connections and PATs separately; restrict project/service-connection access and maintain ownership/rotation. Review current [workload identity federation setup](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/configure-workload-identity?view=azure-devops) and Microsoft’s [secretless-authentication overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/secretless-authentication). Federation issuers/configurations evolve: **VERIFY CURRENT** before creating or migrating a connection.

Use this identity decision check before granting access: **GitHub App** = installed application acting for repositories granted to the installation; **`GITHUB_TOKEN`** = per-workflow-job token scoped to the repository and permissions configured for that workflow; **PAT** = a user’s delegated credential whose scope and lifetime depend on token type and policy; **Azure DevOps service connection** = project resource that stores/configures an external connection and can carry approvals/checks; **Azure DevOps PAT** = a user-associated token with selected scopes and expiry. Ask who owns the principal, how it is scoped, how it is revoked/rotated, whether a short-lived federation option fits, and what audit record shows its use. Do not treat the tokens as interchangeable. **VERIFY CURRENT** for token type limits, plan controls and UI. See [GitHub App authentication](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app), [GITHUB_TOKEN permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication), and [Azure DevOps service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops).

Configure project/team access in Azure DevOps and GitHub to match responsibility. Separate read, build, package-publish and deployment privileges. A service connection should not have broad subscription ownership merely because a release needs one resource. Verify effective identity and permissions at the target.

### Protect sensitive information and scan

Fetch secrets only in the job and stage that need them. Use [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) for governed keys, secrets and certificates where appropriate; scope access and rotation. Use secure files or GitHub secrets only when needed. Do not print secrets, pass them in shell arguments, write them into logs/artifacts, or assume masking catches every transformation. Debug output and model prompts are data paths too.

Threat-model untrusted PRs, prompts/issue text, MCP results, dependencies, package feeds, artifacts, caches, runner persistence and AI-suggested commands. Design dependency, code and secret-scanning coverage across repositories/branches; triage findings with owner, severity and exception expiry. [GitHub Advanced Security](https://docs.github.com/en/code-security) and the [Azure DevOps security overview](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/overview?view=azure-devops) describe product controls. Connect [Defender for Cloud DevOps Security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) to supported environments and verify which repositories/findings are included. A configured scanner does not prove complete coverage or remediation.

Do not treat GitHub Advanced Security and GitHub Advanced Security for Azure DevOps as one toggle. Inventory the platform and repository first. On GitHub, verify that code scanning, secret scanning and dependency alerts are enabled for the intended repository/branch and that alerts have an owner. For Azure DevOps, verify the organization/project setup, repository connection/permissions, enabled feature, repository coverage and surfaced findings for GHAS for ADO; separately check Defender for Cloud DevOps Security onboarding and its supported environments. Record excluded repositories and licensing/entitlement constraints. A green scan run is evidence only for the configured tools and scanned commit. **VERIFY CURRENT:** product availability, license and coverage scope. See [GHAS for Azure DevOps setup](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) and [GitHub code security](https://docs.github.com/en/code-security).

GitHub documents security features for AI coding agents, including secret scanning; review exact workflow and result visibility before relying on them: [GHAS with AI coding agents](https://docs.github.com/en/code-security/how-tos/use-ghas-with-ai-coding-agents). **VERIFY CURRENT:** licensing, eligibility, scanner coverage, issuers and feature stages.

**Check yourself:** For a GitHub workflow deploying to Azure, draw the trust path from repository/event to OIDC token, Azure identity and minimum resource role. Identify an incorrect subject claim, a fork PR that must receive no deployment credential, a secret written to an artifact, and evidence that a scan was reviewed.

## 5. Implement an instrumentation strategy — 15–20%

### Connect delivery and workload signals

Build dashboards for flow, cycle time, recovery time and lead time with explicit definitions and source data. Integrate Azure Monitor/Log Analytics with Azure DevOps and GitHub where supported; use GitHub repository graphs/Insights for available activity views and configure alerts on pipeline or Actions failures. GitHub Insights is a set of repository views, not a general-purpose arbitrary chart builder: identify the exact graph, permissions and plan/data limits (for example, traffic history is bounded). For a custom flow/cycle-time chart, export or query an appropriate data source and define the metric yourself rather than implying it is a native Insights chart. Connect commit, workflow run, artifact version, deployment, service version and incident with stable identifiers. An alert without owner, threshold, context and response path creates noise. See [repository graphs](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/about-repository-graphs) and [repository traffic](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository).

For an investigation, align time windows and inspect workflow logs, resource metrics, application telemetry and distributed traces in [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview). For each query record time range, aggregation, dimensions, missing-data limits and what would disprove the hypothesis. Natural-language log queries can speed exploration; validate the query and result, then use basic KQL for explicit filters and joins. Restrict and redact telemetry that can contain prompts, secrets or personal data.

### Use the named AI observability agents carefully

The blueprint names **Azure Copilot Observability Agent** and **Azure SRE Agent**; these are distinct capabilities. Current [Observability Agent documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview) describes natural-language investigation over telemetry. Its background autonomous alert-correlation/issue-creation mode has a separate Preview boundary; do not infer that it restarts resources or changes configuration autonomously. Read the [governance FAQ](https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-governance-faq) and [telemetry best practices](https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-best-practices) before enabling access. Regions, languages, data handling, retention and modes change: **VERIFY CURRENT**.

Azure SRE Agent run modes distinguish review/approval from autonomous execution. Permissions and tool policies still determine what an action can do. Inspect the proposed action/target, validate its explanation against correlated logs/metrics/traces, require approval for consequential changes, and verify afterward. See [SRE Agent run modes](https://learn.microsoft.com/en-us/azure/sre-agent/run-modes). An AI-generated cause is a hypothesis, not a confirmed incident finding.

The objective also asks about GitHub Copilot agent logs and natural-language/basic KQL queries. First identify the agent surface: cloud coding-agent session logs, local editor extension logs, and the Copilot CLI/IDE Agent Debug Panel are different sources with different availability and contents. For an investigation, capture the relevant session/run identifier, timestamps, prompt/response or tool event needed to diagnose the issue, and associated code/workflow change; redact secrets and personal data before sharing or ingesting. Define collection scope, retention, access, redaction and correlation. The current [Copilot agent session guide](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents) describes session logs, while [Copilot troubleshooting logs](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/view-logs) covers client diagnostics. These are not interchangeable with Azure Monitor workload telemetry or a universal organization-wide agent-log export. Exact interfaces, policies and preview features may change: **VERIFY CURRENT** before configuring ingestion.

**Check yourself:** A rollout fails while CPU rises and an application trace shows dependency latency. Correlate pipeline run, deployed version, time range and trace before accepting an agent’s suggested cause. Decide whether its remediation is read-only, approval-gated or disallowed, then state the recovery evidence.

## Integrated scenarios

### Cross-platform feature delivery

A team tracks work in Azure Boards, hosts source in GitHub and deploys to Azure. Design identifiers and links across work item, PR, test, package, deployment and incident. Choose Azure Pipelines or GitHub Actions based on integration and trust needs. Explain how to handle a failed MCP request without duplicating a work item or falsely advancing state.

### Agent-assisted pull request

An agent drafts code and tests from an issue containing untrusted text. Restrict it to a disposable branch, inspect tool calls and generated workflow changes, deny privileged credentials to fork code, and require human review plus server-side checks. Show where scanning runs, what evidence is retained, and how to revoke access after a suspicious result.

### Progressive deployment and SRE investigation

Promote one tested artifact through a protected environment to a canary. A telemetry alert arrives and an SRE agent proposes a change. Check version, health baseline, query window, permissions and blast radius; approve or deny, verify recovery and record follow-up work. Preserve rollback or a forward fix for database changes.

## Proposed evidence labs

These are study plans, not executed product tests. Use authorized disposable resources and follow current vendor steps.

1. **Traceability tabletop:** map a synthetic feature from Azure Boards through a GitHub PR, tests, artifact, deployment and feedback; identify missing links.
2. **MCP trust boundary:** in a dummy project compare read-only and write-enabled Azure DevOps MCP tools; inspect sign-in scope, permissions, prompt-injection input and action logs.
3. **Branch/recovery drill:** set a protected branch, required check and owner rule; demonstrate why a local hook is not authoritative. Practice revert/recovery in a disposable clone.
4. **Pipeline design review:** compare Azure Pipelines with GitHub Actions for one synthetic app; specify runner isolation, cost, triggers, stages, artifacts and owners.
5. **Testing/package gate:** in a disposable project, create a feed with an upstream and test/release views, publish a versioned sample package, pin a dependency, run tests on a compatible agent, and inspect published test/coverage results plus artifact identity. Simulate a flaky test and untrusted dependency; record who may promote a package and who can consume it.
6. **Deployment tabletop:** plan a canary/slot/rolling release with dependency order, schema expand/contract, health threshold, hotfix and rollback owner. Do not deploy to production.
7. **Identity/scanning matrix:** compare GitHub App, `GITHUB_TOKEN`, GitHub PAT, Azure DevOps service connection and Azure DevOps PAT across principal, scope, lifetime, revocation and audit evidence. Then map GitHub GHAS and GHAS for Azure DevOps/Defender coverage to repositories and branches; identify gaps without creating credentials or enabling paid features.
8. **Telemetry incident exercise:** use synthetic logs/metrics/traces to correlate an unhealthy release; compare a human query with an AI summary and mark unsupported claims. In a demo repository, identify available GitHub Insights graphs, permissions and data limits, then distinguish them from a custom flow-time chart.
9. **Pipeline and agent-log evidence:** inspect a representative Azure Pipelines run and a GitHub Actions run. Record source commit, trigger, agent image/capabilities, templates/variables, test and coverage publication, artifact digest, approval history and deployed artifact identity. From a disposable Copilot session, locate the relevant agent/session or client log and make a redacted incident record; do not ingest raw prompts into a shared log system.

For cloud labs that provision resources, estimate cost, set a budget/alert, capture before-state, use minimum access and clean up. If access is unavailable, submit the design and expected evidence as a tabletop and label it unexecuted.

## Original readiness checks with answers

1. **What proves end-to-end traceability?** A linked work item/issue, reviewed commit/PR, test evidence, immutable artifact, deployment record and operational outcome—not merely a branch.
2. **Why define metric denominators?** Different populations/windows make identical labels incomparable or misleading.
3. **Does MCP connectivity grant access?** No. OAuth scopes, signed-in identity and resource permissions also constrain actions.
4. **Why start an agent read-only?** It limits side effects while validating prompts, tools, logs and usefulness.
5. **Can a local hook enforce merge policy?** No. Use server-side policy and CI for authoritative checks.
6. **When is trunk-based work a poor fit?** When teams cannot keep changes small or maintain fast checks and incomplete-feature controls.
7. **What must migration reconcile?** Refs/tags/LFS, history, identities, permissions, work tracking, policies, pipelines, packages, webhooks and cutover/rollback.
8. **Revert or rewrite shared history?** Prefer auditable revert; rewrite only with coordination, backup and downstream recovery.
9. **Why build once and promote?** It preserves tested artifact identity across environments.
10. **What makes a quality gate useful?** Named risk, reproducible criterion, retained evidence, owner and exception path.
11. **What does coverage percentage prove?** Only its calculation under current instrumentation, not test quality or risk coverage.
12. **How select a runner?** Isolation, trust, tools, OS, network, persistence, licensing, patching and cost.
13. **Who controls Azure resource checks?** The protected-resource owner; pipeline YAML should not bypass them.
14. **What must an agentic workflow reviewer inspect?** Instructions, generated YAML, triggers, tokens, safe outputs and untrusted event text.
15. **When choose a canary?** When gradual exposure and measurable stop criteria reduce blast radius and rollback is workable.
16. **Why are database deployments special?** Schema/data changes may not reverse with application code; use compatibility phases and recovery/forward-fix plans.
17. **Why use workload federation?** It can replace long-lived secrets with short-lived tokens tied to configured trust; subject claims still matter.
18. **Is managed identity available to every GitHub runner?** No. Configure supported federation for external runners.
19. **Scan alert versus compliance?** Findings need coverage, triage, remediation, exceptions and retained evidence.
20. **How use an AI incident explanation?** As a hypothesis to validate against raw correlated evidence and agent permissions.
21. **What should a dashboard show?** Definition, population, window, source, threshold, owner and decision supported.
22. **What can Copilot agent logs reveal?** Sensitive prompts, outputs, code context and tool activity; define access, redaction and retention.
23. **What follows an SRE agent action?** Verify target/permission, review or approve, observe, validate recovery and record the outcome.
24. **How distinguish missing telemetry from health?** Check collection, time range, sampling and expected data volume.
25. **What is safe beta preparation?** Recheck official scope/assessment availability; do not infer item counts, prerequisites or current Preview steps.
26. **When is an upstream package available to ordinary feed readers?** After a collaborator or higher has installed/saved it into the feed; distinguish feed views and reader permissions.
27. **A test task passed, but the pipeline shows no test results or coverage. What do you inspect?** Agent/task compatibility, result and coverage file creation/format/path, publish-task inputs and run evidence; execution alone does not publish a gate signal.
28. **Which reusable pipeline elements work in YAML?** Templates and variable templates/groups; Classic task groups are not supported in YAML. Check template provenance/parameters and explicitly authorize protected variable groups.
29. **Can a Copilot review request satisfy the required PR approval rule?** No. It is advisory and does not approve the PR; retain configured human approval/status requirements.
30. **Does GitHub Insights natively provide any arbitrary DevOps chart?** No. It exposes specific repository graphs subject to permissions/plan/data limits; derive custom flow metrics from an identified source and define the calculation.
31. **Which Copilot logs should an incident responder collect?** Identify the client or cloud-agent surface, session/run ID and relevant timestamps/events, redact sensitive content, and avoid treating session logs, IDE diagnostic logs and Azure Monitor telemetry as interchangeable.

## Places to learn

This is a curated starting point, not a complete list or a requirement to consume every resource. The official study guide is the scope authority; supporting resources teach parts of the role and do not claim complete AZ-401 coverage.

- **Official AZ-401 study guide** — [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401). Public browser reference; no vendor time estimate. **About 30–45 minutes estimated** for one read from the concise objective/resource page; linked documentation is additional. Start here.
- **Introduction to agentic DevOps using Microsoft tools on Azure** — [Microsoft Learn module](https://learn.microsoft.com/en-us/training/modules/introduction-agentic-devops-microsoft-tools-azure/). Seven self-paced units; sign-in for assessment/badge. Duration not displayed; **about 30–45 minutes estimated** from seven units. Advanced orientation, not full AZ-401 coverage; assumes CI/CD, IaC, Azure operations and Copilot familiarity.
- **DevOps and Platform Engineering exercises** — [MicrosoftLearning collection](https://microsoftlearning.github.io/mslearn-devops/) and its [public repository](https://github.com/MicrosoftLearning/mslearn-devops). Individual labs publish durations: [Azure Boards/Copilot](https://microsoftlearning.github.io/mslearn-devops/Instructions/agentic/01-ai-assisted-azure-boards.html) **about 45 minutes**; [Azure DevOps MCP](https://microsoftlearning.github.io/mslearn-devops/Instructions/agentic/02-manage-ado-using-mcp-server.html) **about 30 minutes**; [Azure SRE](https://microsoftlearning.github.io/mslearn-devops/Instructions/agentic/03-optimize-azure-reliability-using-sre-agent.html) **about 45 minutes**; [multi-agent IaC](https://microsoftlearning.github.io/mslearn-devops/Instructions/agentic/06-transition-traditional-ops-using-agent-automation.html) **about 45 minutes**. Access/cost differ; some require paid Copilot, Contributor roles or a billable Azure subscription. Use selected exercises in disposable environments; these are supplements, not an AZ-401 course.
- **Azure Pipelines documentation** — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops). Public technical reference without an end-to-end duration. **45–90 minutes estimated** for selected objective-aligned topics; broader pipelines and lab execution take longer.
- **Azure agentic AI governance path (related item)** — [Microsoft Learn](https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/). Four advanced modules; **2–4 hours estimated** for selected reading. Prerequisites include AI-103/AI-300-equivalent experience and Foundry/identity/GitHub Actions knowledge. It focuses on agentic application lifecycle, not AZ-401 breadth.

## Source and freshness notes

- Scope is bound to the Microsoft AZ-401 study-guide page checked October 29, 2026; it displayed a last-updated date of October 13. The objective snapshot is at ../data/objective-snapshots/az-401-official-objectives.txt.
- The certification page’s AB-100 objective block and unrelated exam-page related-certification copy are an issuer-page content conflict. AZ-401-specific exam and study-guide pages agree; see the [research note](../docs/research/2026-10-29-az401-refresh.md).
- Beta scoring, assessment availability, languages, product stages, GitHub Agentic Workflows, MCP clients, identity federation and Azure agent capabilities are volatile. **VERIFY CURRENT** against linked official pages.
- One Microsoft Learn view displayed an authorization-required notice while objectives remained readable in the web reader. Source health records automated access state; it does not imply the page is missing.
- Labs are proposed. No product behavior, cloud resource, external tenant, exam question or paid course was executed/accessed. No recalled or live exam material is used.
