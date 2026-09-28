---
exam_code: AZ-400
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AZ-400 Designing and Implementing Microsoft DevOps Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-400-coverage-record). The [official AZ-400 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) is authoritative.

**Current baseline:** Skills measured as of July 27, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Certification lifecycle:** Active; no retirement or replacement is announced on the [official DevOps Engineer Expert credential page](https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/) as of September 28, 2026.<br>
**Credential prerequisite:** The official credential page requires Azure Administrator Associate or Azure Developer Associate. The AZ-204 exam used to earn the latter retired July 31, 2026, so a new candidate should verify the currently accepted path before scheduling; AZ-104 remains an active route as of this review.<br>
**Official source:** [AZ-400 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400)

The [September 28 deep review](../docs/research/2026-09-28-az-400-deep-review.md) maps all 86 detailed objectives. Seven worked examples, ten labs and 48 explained checks develop the reasoning behind pipeline choices. Local arithmetic and one release-gate example were executed; cloud pipelines, identity changes, deployment and paid content were not. Independent human review remains pending.

The credential profile lists ten exam languages and renewal. The standalone Microsoft Learn course lists four instructor days and eight languages even though the credential page has an empty training placeholder. Exact exam duration was not verified in this review.

## How to use this guide

Study AZ-400 as a value-delivery and evidence system, not as a list of product screens. For any design, trace one change through:

```text
idea or incident
-> owned work item and acceptance criteria
-> small reviewed source change
-> reproducible build and immutable version
-> layered tests and security evidence
-> approved environment deployment
-> progressive exposure and rollback decision
-> production telemetry and user feedback
-> learning recorded in the backlog
```

At every arrow ask: who or what is the identity, what artifact crosses the boundary, which policy decides, what evidence is retained, and how does the system recover? A green build is not proof of a healthy release, and a fast release is not proof that users received value.

Use disposable Azure, GitHub, and Azure DevOps projects or an authorized sandbox. Hosted minutes, self-hosted compute, artifacts, Log Analytics, Application Insights, Deployment Environments, Key Vault, App Configuration, Defender plans, and test infrastructure can create cost. Restrict permissions and remove resources after labs.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | DevOps engineer question |
|---|---:|---|
| Design and implement processes and communications | 10–15% | Can every change, decision, signal, and outcome flow to the right owner with useful traceability? |
| Design and implement a source control strategy | 10–15% | Can teams change code quickly without losing review, policy, recoverability, or repository performance? |
| Design and implement build and release pipelines | 50–55% | Can one trusted version be built, tested, promoted, deployed, observed, and recovered predictably? |
| Develop a security and compliance plan | 10–15% | Are identities, secrets, code, dependencies, artifacts, infrastructure, and evidence protected end to end? |
| Implement an instrumentation strategy | 5–10% | Can teams detect impact, correlate it to a change, act, and improve the delivery system? |

---

## 1. End-to-end delivery model

### Separate delivery objects

| Object | Purpose | Failure if confused |
|---|---|---|
| Work item or issue | Intent, owner, acceptance criteria, risk and priority | Commits exist without a reason or responsible owner |
| Source commit | Immutable code/configuration history point | A branch name is treated as deployable evidence |
| Build | Execution that compiles, tests and packages a commit | Rebuilding later produces a different result |
| Package/artifact/image | Versioned output promoted between stages | Environments receive different bits for the same release |
| Environment | Governed target plus approvals/checks and operational context | “Production” is just a variable value with no protection |
| Deployment | Recorded attempt to apply a version to an environment | Build success is mistaken for release success |
| Release | Business exposure of capability, possibly controlled by flags | Deployment and user exposure cannot be separated |
| Telemetry/feedback | Evidence about delivery and runtime outcomes | Teams optimize activity rather than value/reliability |

Prefer **build once, promote the same immutable artifact**. Environment-specific values should arrive through controlled configuration, secret stores and deployment inputs—not by recompiling source for each environment.

### Map the three control planes

1. **Work and source:** GitHub Issues/Projects or Azure Boards plus GitHub/Azure Repos.
2. **Automation:** GitHub Actions or Azure Pipelines, hosted/self-hosted execution, packages and deployment environments.
3. **Runtime and evidence:** Azure resources, Azure Monitor/Application Insights, security findings, alerts, user feedback and post-incident work.

Hybrid designs are valid. Azure Boards can track work whose code is in GitHub; Azure Pipelines can build GitHub repositories. Define the system of record, integration identity, linking syntax, retry/failure behavior and ownership of each boundary.

> **Related item:** Platform engineering packages these controls as paved roads: reusable workflows/templates, approved images, environment definitions and observability defaults. Self-service is safe only when the platform preserves policy and evidence.

---

## 2. Processes and communications (10–15%)

### Design traceability and flow of work

Choose a flow from product risk and release needs:

| Flow | Strength | Cost/risk |
|---|---|---|
| GitHub Flow / short-lived branches | Frequent integration, small reviews, continuous deployment friendly | Requires strong automated checks and incomplete-feature control |
| Trunk-based development | Minimizes divergence and integration delay | Demands very small changes, fast CI and disciplined feature flags |
| Feature branches | Isolates work and supports PR review | Long-lived branches create merge debt and delayed feedback |
| Release branches | Supports maintained versions or controlled release trains | Requires explicit backport, ownership, security-fix and retirement rules |

A useful work item contains outcome, acceptance criteria, owner, dependencies, security/operational needs and links to code, build, test, deployment and incident evidence. Configure Azure Boards–GitHub integration so commits and pull requests link to work rather than depending on manual status copying. The [official integration documentation](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops) also identifies connection and authentication constraints.

Use feedback loops at different speeds:

- seconds/minutes: compiler, lint, unit, secret and policy feedback;
- hours: pull-request review, integration/security tests and preview environment;
- days: progressive exposure, user behavior and operational objectives;
- weeks: flow metrics, retrospectives and architectural/dependency improvement.

Notifications must be actionable. Route a failure to the current owner, include correlation identifiers and a runbook, deduplicate noise, define escalation and close the loop in the work tracker. A Teams message is a communication surface, not a durable system of record.

### Measure outcomes, flow and reliability

Use a balanced set rather than one target:

| Concern | Example measure | Misuse to avoid |
|---|---|---|
| Planning | aging work, WIP, blocked time, forecast accuracy | Treating story points as cross-team productivity |
| Development | review latency, change size, rework, build wait | Rewarding commit or line counts |
| Testing | escaped defects, flaky rate, time to signal, meaningful coverage | Optimizing coverage percentage without risk context |
| Security | exposure time, fix time, recurrence, exception age | Counting findings without severity/reachability |
| Delivery | lead time, deployment frequency, failure/recovery | Increasing frequency while hiding failed changes |
| Operations | SLO/error budget, MTTD, MTTR, saturation | Alert count as a proxy for reliability |

Lead time starts when demand enters the system; cycle time commonly starts when active work begins. Define start/end states before comparing results. Azure DevOps [Analytics widgets](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/analytics-widgets?view=azure-devops) can expose cycle time, lead time, velocity and cumulative flow, but poor state hygiene produces misleading charts.

Dashboards should connect measures to decisions: owner, target, time window, population, threshold and next action. Separate product outcome, flow, quality/security and runtime health. Show distributions and trends where averages hide outliers.

> **Related item:** DORA-style delivery metrics are system-level signals. They are most useful for learning and constraint removal, not ranking individual developers.

### Configure documentation and integrations

Keep durable documentation near its change source:

- repository README for build/use entry points;
- versioned architecture decisions and diagrams;
- wiki for cross-repository operating knowledge;
- generated API documentation from source contracts;
- release notes from intentionally labeled changes, not raw commit noise;
- runbooks linked from alerts and deployment records.

Use [GitHub-flavored Markdown](https://docs.github.com/en/get-started/writing-on-github) and [Mermaid diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) when text-source review and version history matter. Validate links and generated output in CI.

Webhooks push signed event payloads to endpoints; polling queries on a schedule. With webhooks, validate signatures, restrict secrets, make handlers idempotent, tolerate retries/out-of-order delivery and monitor dead letters or failures. For Teams integrations, decide which events require an interactive card/action and which belong only in dashboards or work items.

#### Keep integration lifecycle separate from its destination

For Teams notifications, identify the actual integration: a native Azure DevOps/GitHub app, a legacy Office 365 connector or a Power Automate workflow. The [connector retirement notice](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) now identifies May 18–22, 2026 as the final disablement rollout. It directs connector-based webhooks to Workflows and notes that MessageCard action buttons do not work there; interactive scenarios need Adaptive Cards and response handling. This is not a retirement notice for every Teams integration. Test payload, identity, delivery failure, ownership and escalation for the mechanism you actually use.

#### Failure patterns

| Symptom | Likely design problem | Better evidence/action |
|---|---|---|
| Work is “done” but not deployed | Completion state ignores deployment/acceptance | Link work, PR, build, environment and exposure events |
| Dashboard improves while users complain | Proxy metric optimized | Add outcome/SLO and qualitative feedback |
| Teams channel is noisy | No severity, ownership or deduplication | Route actionable exceptions with runbook and owner |
| Release notes omit changes | Commit text is inconsistent | Labels/conventional metadata plus reviewed generation |
| GitHub/Azure Boards links fail | App/PAT scope or multi-org mapping issue | Audit integration identity, installation and AB# behavior |

#### Primary references

- [Connect Azure Boards to GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops)
- [Azure DevOps Analytics widgets](https://learn.microsoft.com/en-us/azure/devops/report/dashboards/analytics-widgets?view=azure-devops)
- [GitHub writing and formatting documentation](https://docs.github.com/en/get-started/writing-on-github)

---

## 3. Source control strategy (10–15%)

### Choose a branch and pull-request contract

The branch model and protection policy must agree. A trunk-based team may require PRs, fast checks, small changes, linear history and a merge queue. A supported-product team may add version branches, signed release tags and controlled backports.

For every protected branch define:

- who can push, review, dismiss, merge and bypass;
- required independent/code-owner reviews;
- required build, test, security, coverage and deployment checks;
- whether conversations must resolve and history must be linear;
- merge method and stale-approval behavior;
- force-push/deletion policy and emergency audit path.

GitHub [branch protection and rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and Azure Repos branch policies are preventive controls. They do not make an irrelevant test useful or a rubber-stamp review independent. Ensure check names are unique and trusted branches cannot change their own required control without review.

> **Related item:** A merge queue tests a proposed merge against current branch state, reducing the “each PR was green independently, but the combined branch is broken” race.

For a [GitHub merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue), required GitHub Actions checks need the `merge_group` trigger as well as ordinary PR validation. External CI must handle the queue's temporary branch convention and report on its commit. A green check on the PR commit does not satisfy a different merge-group commit. Verify plan/organization eligibility before proposing this control.

### Configure repositories, permissions and tags

Grant repository access through teams/groups and roles, keep administrators few, protect automation identities separately, and review dormant/outside access. Distinguish Git tags from product labels: a signed/annotated tag can identify a source version; a repository label categorizes work.

Use tags/releases to make source-to-artifact provenance queryable. Do not move an existing release tag silently. Decide how tags are created, protected, signed, mapped to package versions and retained.

Repository topology trades autonomy against coordination:

| Choice | Prefer when | Watch for |
|---|---|---|
| Monorepo | Atomic cross-component change and shared tooling dominate | Checkout/build scope, permissions and ownership boundaries |
| Multiple repositories | Independent ownership, lifecycle and access dominate | Version coordination, duplicated pipelines and cross-repo change |
| Shared templates/modules repo | Central paved road with governed consumers | Breaking changes and unpinned references |

[Azure DevOps public projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/public-projects-retirement?view=azure-devops) no longer accept new public-project creation; existing public projects convert to private in 2027, with exact dates communicated in product banners. Inventory anonymous source/wiki links, badges, package consumers and pipeline capacity before conversion. Public feed consumers will need authentication or a supported public distribution destination. Do not infer that Azure DevOps private enterprise projects are retiring.

### Manage large repositories and files

Git retains reachable history, so deleting a file in a later commit does not shrink earlier history. Keep generated binaries, dependency caches, database exports and secrets out of normal Git.

- [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) stores pointer files in Git and large objects elsewhere; clients, quotas, billing, retention and archive behavior still matter.
- `git-fat` is an external approach named in the blueprint; verify maintenance, hosting, client and recovery requirements before choosing it.
- Scalar helps operate very large Git repositories through optimized configuration and partial/background behaviors; test client/host compatibility.
- Sparse checkout and partial clone reduce working data but do not repair poor repository boundaries.
- Cross-repository sharing should use versioned packages, modules, APIs or submodules/subtrees only with explicit ownership/update rules—not copy/paste.

**VERIFY CURRENT:** GitHub/Azure Repos file, repository, LFS, pack, API and billing limits; Scalar/Git client support; and any external `git-fat` implementation before committing a design.

### Recover or remove data safely

Choose the least disruptive command:

| Intent | Typical mechanism | History effect |
|---|---|---|
| Restore a deleted file | restore/checkout from a known commit, then commit | Adds history; shared history unchanged |
| Undo a shared bad commit | `git revert` | Adds an inverse commit; safest default for shared branches |
| Move an unpublished local branch | `git reset` | Rewrites local branch position/index/worktree depending on mode |
| Find a lost local reference | `git reflog` then restore/branch | Uses local reference history; not a server backup |
| Remove sensitive/large history | approved history-rewrite tool and force update | Changes commit IDs; every clone/fork/cache and credential remains a concern |

If a secret enters Git, revoke/rotate it first. History rewrite reduces exposure but cannot prove that clones, logs, caches, forks or artifacts forgot it. Coordinate freeze, backup, rewrite, protected-branch exception, force push, collaborator reclone and post-scan. Preserve audit evidence.

#### Primary references

- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub large-file guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

---

## 4. Build and release pipelines (50–55%)

### 4.1 Package and dependency strategy

Use a package manager/feed that supports the ecosystem and required provenance, access, upstream, retention and promotion controls. GitHub Packages integrates with repository/organization permissions and Actions; Azure Artifacts supports multiple ecosystems, scoped feeds, views and upstream sources.

An [Azure Artifacts feed](https://learn.microsoft.com/en-us/azure/devops/artifacts/artifacts-key-concepts?view=azure-devops) is the package collection and permission boundary. A **view** exposes a selected quality level such as prerelease/release; it does not create a new package. An **upstream** proxies/caches an external registry so resolution can be controlled and repeatable. Package versions are immutable—promote metadata/view membership rather than overwrite a released version.

Version intentionally:

- SemVer `major.minor.patch` communicates compatibility intent; pre-release/build metadata need consistent rules.
- CalVer communicates time/release train, not compatibility by itself.
- Pipeline artifacts can use source commit, run ID and human release version together.
- Lock files pin the resolved graph; a version range alone does not guarantee repeatability.

Protect against dependency confusion and supply-chain drift: control source order, namespaces, upstreams, checksums/signatures/attestations, license policy, vulnerability scans and retention. Generate an SBOM where required. Never promote by rebuilding the same version from a different commit.

> **Related item:** Package promotion is an authorization decision about an immutable object. Copying/rebuilding a package for each stage breaks the strongest source-to-production chain of custody.

#### Promotion, access and provenance are separate controls

[Azure Artifacts promotion](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/views?view=azure-devops) adds a package version to a view; publishing still goes to the base feed. Promotion cannot be undone by demoting a package. A deployment rollback selects a retained earlier version rather than assuming view demotion is available.

[View permissions](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/feed-permissions?view=azure-devops) can allow downloading a package even without direct feed access. Restrict both surfaces. A view set to “Specific people” with no people selected falls back to parent-feed permissions; an empty selection is not a deny-all rule. Distinguish reading packages, saving upstream packages and publishing/promoting packages when assigning the pipeline identity.

[Artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) establish provenance. Verify the actual binary or image digest against the expected repository and applicable signer policy before consuming it; merely producing an attestation is insufficient. An SBOM predicate and build-provenance predicate answer different questions. Neither proves that tests are meaningful or the artifact has no vulnerabilities. Record the verified artifact, source, build identity, scan result and deployment together.

### 4.2 Testing and quality gates

Design tests by failure boundary:

| Layer | Fast question | Pipeline placement |
|---|---|---|
| Static/lint/type | Is source structurally acceptable? | Local and first CI job |
| Unit | Does isolated logic behave? | Every change; parallel where safe |
| Component/contract | Does one deployable component honor interfaces? | PR/build; version external contracts |
| Integration | Do real dependencies and identity/network paths work? | Disposable or controlled environment |
| End-to-end | Does the critical user journey work? | Small, high-value suite after deployment |
| Performance/load | Does it meet latency/throughput/saturation targets? | Scheduled/pre-release representative environment |
| Resilience/security | Does it fail safely and resist known risks? | Targeted gates and scheduled deeper tests |

Publish results even on failure so the failed test—not only the task exit code—is visible. Use [Test Analytics](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-analytics?view=azure-devops) to find recurring/flaky failures. Quarantine only with owner, deadline and tracked risk; blind retry makes an unreliable system look green.

[Code coverage](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/review-code-coverage-results?view=azure-devops) identifies unexecuted code, not assertion quality. Gate high-risk changed code or unacceptable regression, then inspect missing paths. A universal percentage can reward low-value tests.

Quality/release gates may evaluate test, scan, change-management, policy, approval, business hours, runtime health or external checks. Make the result deterministic, time-bounded, auditable and fail closed where the risk requires it. Approval is not a substitute for automated evidence.

### 4.3 Select and design pipeline automation

| Decision | GitHub Actions | Azure Pipelines |
|---|---|---|
| Source-native experience | Strong for GitHub repositories, checks and environments | Strong for Azure Repos; first-class GitHub integration also supported |
| Reuse | Reusable workflows, composite/JavaScript/container actions | YAML templates, task groups for classic, variable groups |
| Execution | GitHub-hosted/larger/self-hosted/ARC | Microsoft-hosted/self-hosted agents and pools |
| Governance | Org/enterprise policies, environments, runner groups | Organizations/projects, environments, service connections, approvals/checks |
| Packages | GitHub Packages and external registries | Azure Artifacts and external registries |

Select from source location, platform skill, governance boundary, required integrations, networking, OS/tooling, licensing, concurrency, cost and maintainability—not “the other tool can’t deploy Azure.” Hybrid is valid but adds identities, integration failures and evidence surfaces.

#### Hosted versus self-hosted execution

Hosted execution offers clean managed images and low maintenance; self-hosted execution adds private reach, custom hardware/software and caching control but makes you responsible for patching, isolation, scale, cleanup and compromise response. GitHub explicitly warns that [self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners) do not necessarily provide a clean instance per job.

Never let untrusted pull-request code run on a persistent privileged runner with production network/credentials. Prefer ephemeral isolated workers, separate runner/agent pools by trust zone, restrict which repositories/pipelines can use them, and scope egress and identities.

**VERIFY CURRENT:** hosted image contents, runner/agent SKUs, concurrency/minutes, licensing, private networking, autoscaling and deprecation notices.

#### September 2026 runner and workflow changes

[GitHub removed the Node 20 JavaScript-action runtime on September 23, 2026](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/). Actions now run on Node 24 and the temporary insecure-runtime opt-out is gone on github.com and GitHub with Data Residency. This is the runtime used by JavaScript actions, not automatically the Node version of the application you build. Update action releases and self-hosted runner OS/architecture compatibility; test application runtimes separately.

[Workflow execution protections](https://docs.github.com/en/actions/how-tos/administer/control-workflow-execution) allow actor/event policies with workflow-file targeting. Availability depends on repository visibility and plan; Evaluate mode requires Enterprise Cloud. The [GA announcement](https://github.blog/changelog/2026-09-17-workflow-execution-protections-in-github-actions-generally-available/) schedules November 2, 2026 enforcement of the default `pull_request_target` block for affected public repositories using the default policy. Inspect the actual policy and insights; private/internal repositories are outside that default rollout.

These policies complement the [secure-use guidance](https://docs.github.com/en/actions/reference/security/secure-use): do not check out or execute untrusted PR code in privileged `pull_request_target` or `workflow_run` jobs. Treat downloaded artifacts from another run as untrusted inputs until verified. Pin reviewed actions to full commit SHAs; pinning does not itself establish that the pinned code is safe. Pass untrusted text as data through a safely quoted argument/environment boundary instead of embedding expressions into shell source.

### 4.4 Author reliable YAML pipelines

Build the dependency graph deliberately:

```text
validate
├─ unit + coverage
├─ security scans
└─ build/package
   -> integration environment
   -> integration tests
   -> production approval/checks
   -> progressive deployment
   -> health decision
```

Triggers define when a workflow/run starts; conditions decide whether a stage/job/step executes. Account for branch/path filters, pull-request versus push security context, schedules, manual dispatch and pipeline completion. Prevent duplicate CI and recursive triggers.

Use stages for major lifecycle boundaries, jobs for independently scheduled units and steps for ordered work on one worker. Parallelize independent work after considering test isolation, service quotas, license/concurrency cost and diminishing returns. Express dependencies explicitly; filesystem state does not cross agents unless published/downloaded.

Reusable elements should have versioned contracts:

- input type/default/validation and safe secret handling;
- clear outputs and artifact names;
- pinned actions/tasks/templates where possible;
- compatibility/deprecation policy;
- centralized security checks that consumers cannot silently bypass.

Variables are configuration strings, not automatically secrets. Variable groups centralize values, while secure secret systems and federation are preferred for credentials. Templates are expanded/compiled differently from runtime conditions; understand evaluation timing before debugging an “empty” value.

Use GitHub environments or Azure Pipelines environments for deployment history and scoped protection. In Azure Pipelines, resource owners configure [approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) outside the consuming YAML, which helps prevent a pipeline author from weakening the gate in the same change.

#### Conditions, evaluation time and resource checks

Setting an Azure Pipelines [custom condition](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions?view=azure-devops) replaces the default success condition. A branch-only condition can permit work after an earlier failure; combine required success and branch checks, for example `and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))`. Reserve `always()` for appropriate cleanup/evidence work and account for parent-stage cancellation/skips.

[Template expressions, macros and runtime expressions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops) are evaluated at different times. A value set during a job cannot decide whether that same job starts. Typed template parameters differ from string variables; expose cross-job values through declared outputs and dependencies.

Resource checks remain outside consuming YAML. In the current [approval/lock documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops), approvers are fixed when checks begin; a changed group/list is not dynamically substituted into that pending approval. An exclusive lock with `runLatest` differs from `sequential`: superseded waiting deployments versus every queued deployment in order. Choose deliberately for stateful migrations, and retain the identity/reason for any authorized check bypass.

### 4.5 Design deployments and exposure

Separate deployment from release/exposure:

| Pattern | Mechanism | Good for | Rollback concern |
|---|---|---|---|
| Rolling | Replace instances in bounded batches | Capacity-efficient service update | Old/new compatibility during rollout |
| Blue-green | Prepare parallel environment, switch traffic | Fast environment rollback | Data/schema and double-capacity cost |
| Canary/ring | Send increasing population/traffic to new version | Evidence-based risk reduction | Cohort/telemetry correctness and stop criteria |
| Progressive exposure | Combine rings, health gates and feature controls | Controlled blast radius | Requires automated decision-quality telemetry |
| Feature flag | Runtime capability control independent of deploy | Dark launch, kill switch, cohort rollout | Flag debt, permissions and code-path testing |
| A/B test | Randomized/controlled variants measured against hypothesis | Product experiment | Statistical validity and guardrail metrics |

Azure App Configuration [feature management](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management) distinguishes switch, rollout and experiment scenarios. A flag is not a substitute for version rollback when the deployed binary or infrastructure is unhealthy.

Order dependencies through explicit contracts and readiness, not sleeps. Deploy infrastructure before dependent application where necessary; migrate database with an **expand–migrate–contract** approach so old and new application versions overlap safely. Make scripts idempotent, transactional where possible, retry-aware and resumable.

For minimal downtime, combine health probes, load-balancer draining, surge capacity, rolling limits or deployment slots. Slot swap moves configuration according to sticky/non-sticky rules and does not solve unsafe database changes.

Define a hotfix path before the incident: eligible branch/source, expedited reviewers, non-bypassable checks, artifact version, deployment route, rollback, forward merge/backport and retrospective. “Direct production edit” destroys provenance and reproducibility.

Resilient deployment handles partial failure: deployment timeout, retry policy, health threshold, automatic stop/rollback, idempotency, regional ordering and last-known-good artifact/configuration. Test rollback—including schema and configuration—not merely the forward path.

### 4.6 Infrastructure as code and configuration management

Use source-controlled IaC with review, static/security analysis, preflight/what-if, environment parameters, deployment identity, state/history and post-deployment tests. [Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) previews intended resource changes but cannot prove runtime correctness or every downstream effect.

| Tool/approach | Primary job | Key boundary |
|---|---|---|
| ARM/Bicep | Declarative Azure resource deployment | Azure resource/control-plane configuration |
| Azure Machine Configuration | Audit/apply guest OS configuration at scale | In-guest desired state and compliance |
| Configuration scripts/tools | Application/OS configuration and orchestration | Must be repeatable, idempotent and securely supplied |
| Azure Deployment Environments | Curated self-service environment catalog | Platform team governs definitions, identity, subscriptions and policies |

The blueprint still names Azure Automation State Configuration. Microsoft states it [retires September 30, 2027 and should transition to Azure Machine Configuration](https://learn.microsoft.com/en-us/azure/governance/machine-configuration/whats-new/migrating-from-azure-automation). Know the legacy concept and the current destination; do not design a new long-lived implementation around the retiring service.

[Azure Deployment Environments](https://learn.microsoft.com/en-us/azure/deployment-environments/concept-environments-key-concepts) uses dev centers, projects, environment types, catalogs, definitions and managed identities to offer governed on-demand environments. Catalog approval and template versioning determine what self-service can create. Add ownership, cost tags, quota and expiration/deletion policy.

> **Related item:** Desired state does not mean “rerun until green.” A safe controller understands ownership, drift, destructive change, secret handling and whether reconciliation can interrupt service.

For [Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if), record the validation level and diagnostics. `Provider` includes deployment permission checks; `ProviderNoRbac` uses read permission checks for resources; `Template` performs static validation without provider preflight checks. Unresolved external state can exclude a resource or module from analysis. A short or empty diff is not proof of complete coverage, successful deployment or working data-plane permissions.

### 4.7 Maintain and optimize pipelines

Measure queue time, execution time, pass rate, retry/flaky rate, top failing tasks, runner utilization, cache effectiveness, artifact transfer and cost. Azure Pipelines [pipeline reports](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport?view=azure-devops) expose pass-rate and duration trends; GitHub [Actions metrics](https://docs.github.com/en/actions/concepts/metrics) include job duration, queue time and failure rate.

Optimize in this order:

1. Remove redundant or low-value work.
2. Fail fast on cheap deterministic checks.
3. Cache only keyed, validated and safely scoped dependencies.
4. Parallelize independent critical-path work.
5. Right-size workers and use autoscaling/ephemeral capacity.
6. Split scheduled deep tests from the fast PR signal without dropping coverage.

More concurrency can increase cost, downstream throttling and test collision. An overly broad cache can poison builds or conceal missing dependency declarations. Retain artifacts, packages, logs, test/security evidence and deployments according to rollback, audit, legal and cost needs; do not apply one retention period to all objects.

Migrate classic pipelines to YAML by inventorying triggers, variables/secrets, service connections, agents, tasks/extensions, artifacts, approvals, schedules and retention. Reproduce behavior in versioned YAML, run parallel comparison, preserve environment checks outside YAML, document the cutover/rollback and retire the classic definition only after evidence agrees.

#### Cache access and evidence retention

[GitHub `cache-mode`](https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode/) now controls restores/saves at workflow or job scope: `read`, `write`, `write-only` or `none`. A called reusable workflow cannot gain cache access beyond its caller. Explicit write access on a low-trust event can override the read-only default, so assess that trust boundary. Cache data remains a performance input, not an immutable release artifact.

From [October 1, 2026](https://github.blog/changelog/2026-08-27-actions-retention-will-cover-checks-workflow-runs-and-statuses/), GitHub Actions retention also governs checks, workflow runs and statuses, including relevant third-party checks/statuses. Public repositories have a 90-day maximum; organization/enterprise caps still apply. Archive required release evidence before expiry. Raising a setting cannot recover data already deleted.

[Azure Pipelines retention](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention?view=azure-devops) is configured at project scope for YAML/classic build pipelines; classic releases and test data have additional policies. Inventory the artifact, logs, tests, scans, approvals and deployment evidence needed for rollback and audit. Keeping a tag alone does not preserve the tested package.

For reusable GitHub workflows, the [September job-context additions](https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates/) distinguish `job.workflow_sha`/`job.workflow_ref` for the file defining the job from the caller's workflow identity. Record both when auditing a central build workflow. These new job properties are not available on GitHub Enterprise Server.

#### Pipeline failure patterns

| Symptom | First distinction | Evidence |
|---|---|---|
| Same commit produces different package | Unpinned input or mutable build image/cache? | lock file, image/tool version, hashes, build provenance |
| PR pipeline passes, main fails | Trigger/context/merge-base or concurrent change? | event payload, evaluated YAML, merge queue/check history |
| Deployment hangs | Approval/check, worker connectivity or target operation? | environment timeline, agent log, Azure activity/deployment log |
| Canary is “healthy” but users fail | Wrong cohort/metric/window? | version/cohort dimensions, traces, business and guardrail metrics |
| Rollback fails after DB migration | Backward-incompatible schema? | migration journal, old/new contract tests, restore point |
| Pipeline slows over weeks | Queue, task, cache, test or artifact growth? | duration percentile by stage/job and run history |

#### Primary references

- [Azure Artifacts key concepts](https://learn.microsoft.com/en-us/azure/devops/artifacts/artifacts-key-concepts?view=azure-devops)
- [Azure Pipelines test analytics](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-analytics?view=azure-devops)
- [GitHub Actions concepts](https://docs.github.com/en/actions/concepts)
- [Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)
- [Azure App Configuration feature management](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management)
- [Azure Deployment Environments key concepts](https://learn.microsoft.com/en-us/azure/deployment-environments/concept-environments-key-concepts)

---

## 5. Security and compliance plan (10–15%)

### 5.1 Authentication, authorization and organizational boundaries

Distinguish identity types:

| Identity | Best fit | Risk/control |
|---|---|---|
| Human user | Interactive administration/review | MFA, least privilege, conditional access, no shared accounts |
| GitHub App | Scoped GitHub integration/automation | Installation/repository permissions and short-lived tokens |
| `GITHUB_TOKEN` | Current GitHub Actions workflow/repository operations | Explicit minimal `permissions`; fork/event context matters |
| Fine-grained PAT | Legacy/user-delegated gaps | Owner departure, scope, expiration and rotation; avoid when app/federation works |
| Entra service principal | Nonhuman Azure/API identity | Prefer federation/certificate over client secret; scoped RBAC |
| Managed identity | Azure-hosted workload accessing Azure resources | No managed credential; system/user-assigned lifecycle differs |
| Azure DevOps service connection | Governed pipeline connection to external service | Per-pipeline authorization, owner, federation and audit |

System-assigned managed identity shares the Azure resource lifecycle; user-assigned identity has an independent lifecycle and can be shared. Sharing reduces identity count but broadens blast radius and complicates attribution.

Prefer short-lived workload identity federation. GitHub Actions can use [OIDC with Azure](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure) so the workflow exchanges a constrained identity assertion instead of storing a client secret. Constrain issuer, audience and subject to intended organization/repository/branch/environment.

Azure Pipelines recommends [workload identity federation for Azure Resource Manager service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/connect-to-azure?view=azure-devops). The [Azure DevOps issuer retirement](https://devblogs.microsoft.com/devops/retirement-of-azure-devops-issuer-in-workload-identity-federation-service-connections/) on July 1, 2027 applies to public-cloud connections using single-tenant applications or managed identities. Non-public clouds and multi-tenant applications are explicitly excluded from this announcement. Convert affected existing connections using the documented workflow and preserve pipeline references; verify the replacement federated credential before removing the old trust. Secretless authentication still has an issuer and trust lifecycle.

The new [Azure DevOps workload-identity service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-devops-entra-service-connection?view=azure-devops) authenticates to Azure DevOps resources, rather than being an ARM connection to deploy Azure resources. Create/add the identity to each target organization and grant the required access level, resource permissions and per-pipeline connection authorization. Cross-organization use requires the supported tenant relationship; the launch UI calls the connection preview, so verify rollout/support in your organization.

[Application identities in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops) use Azure DevOps permissions, not Entra application permissions, for authorization. Azure Repos needs Basic or an appropriate higher functional access level; paid access consumes a license in each organization. Deleting the Entra identity does not automatically remove its Azure DevOps membership. Include both in deprovisioning.

In GitHub, model enterprise/organization/repository roles, teams, outside collaborators and base permissions. In Azure DevOps, model organization/project/team, access level, security groups and object permissions. Access level (such as Stakeholder) controls licensed capabilities; a security permission controls an operation. Test effective permissions, deny inheritance and service identities.

### 5.2 Protect secrets, files and logs

Store keys, secrets and certificates in Azure Key Vault or the platform’s protected secret facility; use references/federation so pipelines do not print or persist values. Separate vaults and deployment identities by environment/risk. Apply RBAC, network controls, rotation, expiration, recovery protection and audit.

Azure Pipelines secure files protect files such as signing certificates during authorized jobs; download only for the step that needs them and delete workspace copies. They are not a general artifact store.

Prevent leakage:

- reject secrets before commit and enable repository secret scanning;
- avoid passing secrets on command lines, environment dumps or untrusted scripts;
- mask values but assume masking cannot catch transformed/fragmented secrets;
- restrict pull-request contexts, logs, artifacts, caches and test reports;
- pin/review third-party actions, tasks, containers and extensions;
- revoke exposed credentials immediately and investigate use.

### 5.3 Automate security and compliance scanning

Design a layered plan:

| Scan | Finds | Placement/action |
|---|---|---|
| Secret scanning | Credentials/tokens in history or push | Pre-commit/push protection plus continuous repository scan; revoke on exposure |
| SAST/code scanning | Source/data-flow weaknesses | PR plus default/scheduled full scan; triage reachable/high severity |
| Dependency/SCA | Vulnerable/open-source components and licenses | Restore/build and continuous advisory monitoring; lock and update |
| IaC/configuration | Misconfiguration/policy violations | PR and deployment preflight; enforce high-risk policy |
| Container image | OS/application packages and malware/signature issues | After build, before registry promotion and continuously after publish |
| DAST/runtime | Behavior of running service | Controlled deployed environment with safe test data |

[GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features) cover secret protection, code scanning/CodeQL, dependency review and Dependabot capabilities with plan/repository differences. Dependabot alerts identify vulnerable dependencies; security updates can propose fixes. Neither proves that an update is compatible—run tests and assess reachability.

Container scanning should inspect the final image by digest, minimize base packages, rebuild when bases change, sign/attest the artifact and enforce registry/deployment policy. To run CodeQL inside a container, preserve the required source/build database and upload results even though analysis executes in the container.

[Defender for Cloud DevOps security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction) connects GitHub, Azure DevOps or GitLab visibility with code-to-cloud posture and findings. GitHub Advanced Security and GitHub Advanced Security for Azure DevOps remain distinct products/surfaces; integration does not mean every finding, license or feature is identical.

**VERIFY CURRENT:** GitHub security product names, licensing, default setup language support, Defender connector/scanner capabilities, Azure DevOps availability, container/IaC scanners and pull-request annotation support.

> **Related item:** Compliance evidence should be produced by the delivery system—approved change, immutable artifact, scan result, authorized identity and deployment record—not reconstructed manually after release.

[CodeQL default setup for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-code-scanning?view=azure-devops) is now GA according to the [sprint 276 release](https://learn.microsoft.com/en-us/azure/devops/release-notes/2026/sprint-276-update). It scans the default branch with automatic setup and no custom build steps. Go and Swift require advanced setup in the current matrix. Choose advanced setup for custom builds, additional branches or specialized queries; do not equate default setup with PR validation for every language. Current default-setup scheduling/agent options and concurrency consumption also require capacity planning.

#### Primary references

- [GitHub Actions OIDC with Azure](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure)
- [Azure Pipelines Resource Manager service connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/connect-to-azure?view=azure-devops)
- [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features)
- [Defender for Cloud DevOps security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction)

---

## 6. Instrumentation strategy (5–10%)

### Configure monitoring from code to delivery

Collect four correlated evidence sets:

1. **Delivery telemetry:** source version, workflow/pipeline, artifact digest, environment, deployment status and duration.
2. **Application telemetry:** requests, dependencies, exceptions, traces, logs and business events.
3. **Infrastructure telemetry:** CPU, memory, disk, network, platform metrics, resource/diagnostic logs and health.
4. **User/feedback telemetry:** availability, latency, feature exposure, user behavior, support/incidents and satisfaction.

Standardize service name, environment, region, version, instance, operation/trace ID and deployment ID. Never place secrets or unnecessary personal data in telemetry. Define sampling, retention, access and cost before turning on everything.

For new supported application scenarios, Microsoft recommends the Azure Monitor OpenTelemetry distribution; [Application Insights OpenTelemetry guidance](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable) covers traces, metrics, logs and exceptions. Distributed tracing follows a transaction across services; missing context propagation makes each component look locally healthy while the user request fails end to end.

Configure Azure Monitor/Application Insights plus VM, Container, Storage and Network insights according to workload. Resource metrics are not application outcomes: low CPU can coexist with authentication failure. Alerts should be symptom/user-impact oriented where possible, use dynamic/static thresholds deliberately, include ownership/runbook/context and avoid duplicate notification storms.

GitHub/Azure pipeline alerts should distinguish infrastructure/transient failure, deterministic code/test failure, approval wait, security rejection and deployment/runtime health failure. A notification should link to the exact run/job/commit/environment.

### Analyze evidence

Start KQL with a known table, bounded time and filters, then project and summarize only needed data. The [Azure Monitor query tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries) documents `where`, `project`, `summarize`, `bin`, `top` and time ranges.

Example reasoning query (replace table/fields with your schema):

```kusto
requests
| where timestamp > ago(2h)
| summarize estimatedRequests=sum(itemCount),
            estimatedFailures=sumif(itemCount, success == false),
            sampledP95=percentile(duration, 95)
  by bin(timestamp, 5m), cloud_RoleName, application_Version
| order by timestamp asc
```

For the classic `requests` schema above, [sampling guidance](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling-classic-api) requires `itemCount` weights for estimated totals. The displayed percentile is still calculated from retained rows; do not treat it as a corrected population percentile. Confirm the schema and sampler before adapting the query. [OpenTelemetry sampling](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-sampling) varies by language/version, and preaggregated metrics are not sampled. Prefer appropriate unsampled metrics for release guardrails, while sampled traces support diagnosis. These KQL statements were reviewed, not run against a workspace.

Correlate a metric spike with deployment annotation/version, trace to the slow/failing dependency, inspect logs for cause and create owned remediation. CPU/memory/disk/network show saturation symptoms; application traces show request path; business metrics show impact.

Define SLI, SLO and error budget for important journeys. Use burn-rate or sustained-impact alerts rather than a raw metric threshold alone. After an incident, run a blameless retrospective that records contributing system conditions, detection/recovery quality and concrete owners—not just “be more careful.”

#### Failure patterns

| Symptom | Likely gap | Next evidence |
|---|---|---|
| App is slow, infrastructure looks normal | Dependency/code/client latency | Distributed trace and version/cohort dimensions |
| Alert fires for every deployment | No warm-up/suppression or wrong threshold | Deploy event, health window, baseline and SLO impact |
| Cannot link incident to code | Version/deployment metadata absent | Artifact digest, commit and environment deployment record |
| KQL is expensive/slow | Unbounded time/search and excessive columns | Start table/time, `where`, `project`, aggregation |
| Pipeline duration average looks stable | Tail queue/task regression hidden | p50/p95 by stage, agent pool and event type |

#### Primary references

- [Enable Azure Monitor OpenTelemetry](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)
- [Get started with Azure Monitor log queries](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries)
- [Azure Pipelines pipeline reports](https://learn.microsoft.com/en-us/azure/devops/pipelines/reports/pipelinereport?view=azure-devops)
- [GitHub Actions metrics](https://docs.github.com/en/actions/concepts/metrics)

---

## 7. Integrated scenarios

### Scenario A: GitHub source with Azure Boards and Azure Pipelines

A regulated team tracks work in Azure Boards, stores code in GitHub and deploys to Azure with Azure Pipelines.

1. Install/configure the Azure Boards GitHub integration with the smallest repository scope; link commits/PRs to acceptance criteria.
2. Protect the default branch with independent review, unique required checks, code owners and controlled bypass.
3. Trigger YAML pipelines from GitHub PR/merge events while preventing untrusted fork code from receiving privileged credentials.
4. Build once, publish a hashed/versioned package and SBOM, then promote the same object.
5. Use ephemeral or isolated agents and a workload-federated service connection scoped per environment.
6. Apply tests, code/dependency/secret/IaC scans and policy checks before the production environment.
7. Deploy canary, evaluate version/cohort SLO and business signals, then continue or roll back automatically.
8. Link deployment and incident evidence back to the work item and dashboard.

The main failure is treating each product integration as configuration only. Every integration has identity, authorization, event delivery, retry and audit behavior.

### Scenario B: Safe application and database release

A service change needs a non-null database column and a new UI available to 10% of customers.

1. Expand schema with a nullable/default-compatible column while old application versions continue working.
2. Deploy code that writes both forms and can read both; run contract/integration tests.
3. Migrate/backfill with resumable, observable batches and explicit throttling.
4. Deploy the feature disabled, then expose it to an internal ring and 10% cohort through App Configuration.
5. Compare version/cohort error, latency and business guardrails for a predeclared window.
6. Stop exposure or disable the flag if application behavior fails; roll back binary if the deployed version is unhealthy.
7. Contract/remove old schema only after all consumers and rollback windows have moved forward.

The main failure is assuming blue-green application switching can roll back a destructive schema migration.

### Scenario C: Compromised self-hosted runner

A persistent production runner executed a workflow changed by an untrusted pull request.

1. Isolate/destroy the runner and stop queued workloads; preserve authorized forensic evidence.
2. Revoke runner registration, tokens, PATs, service-connection credentials and any reachable secrets.
3. Audit workflow changes, logs, package/registry pushes, Azure activity, Key Vault access and deployments.
4. Identify artifacts built on the worker and rebuild from trusted source on a clean worker; compare provenance/digests.
5. Restore with ephemeral isolated runner pools separated by trust zone and repository allowlists.
6. Replace stored Azure credential with tightly constrained federation; minimize `GITHUB_TOKEN`/service connection permissions.
7. Add fork/event restrictions, pinned dependencies and a tested incident runbook.

---

### Worked examples — verify the release decision

These are fictional inputs and original exercises, not service limits, real measurements or production validation.

#### Example 1 — critical path versus worker consumption

Assume independent build, unit and security jobs take 6, 8 and 12 minutes. Integration then takes 5 minutes, deployment 2, and an approval wait adds 15. Elapsed time is `max(6, 8, 12) + 5 + 2 + 15 = 34 minutes`; running all three initial jobs sequentially takes **48 minutes**. Worker execution totals **33 minutes** either way under this model; reducing elapsed time does not automatically reduce compute usage. Approval waiting remains a separate process bottleneck.

#### Example 2 — runner capacity at steady state

Thirty runs/hour averaging 12 worker-minutes each require `30 × 12 / 60 = 6` continuously occupied slots. Six slots imply 100% utilization with no room for arrival or duration variability. Eight slots average **75% utilization** under those assumptions. This is a capacity estimate, not a queue-latency guarantee; include concurrency licensing, security scans, peak arrivals and private dependency limits.

#### Example 3 — an aggregate can hide a failed canary

The control serves 100,000 requests with 200 failures (**0.2%**). The candidate serves 1,000 with 20 failures (**2%**). Combined failure rate is only `220 / 101000 × 100 ≈ 0.2178%`, hiding a tenfold candidate regression. Use the correct version/cohort and a declared observation window.

This local Python function illustrates a health decision that rejects missing, malformed, stale, sampled or wrong-version observations. Its thresholds are exercise policy: at least 500 requests over 15 minutes, data no older than two minutes, failures at most 0.5% and p95 at most 300 ms. It assumes trusted, correctly aggregated telemetry; it does not authenticate evidence, verify artifacts, prove statistical significance or deploy anything.

```python
import math

def may_promote(observed, expected_version):
    if observed.get("version") != expected_version or observed.get("sampled") is not False:
        return False
    requests, failures = observed.get("requests"), observed.get("failures")
    if type(requests) is not int or type(failures) is not int:
        return False
    if requests < 500 or not 0 <= failures <= requests:
        return False
    window, age, p95 = (observed.get(k) for k in ("window_seconds", "age_seconds", "p95_ms"))
    if any(type(x) not in (int, float) or not math.isfinite(x) for x in (window, age, p95)):
        return False
    return window >= 900 and 0 <= age <= 120 and 0 < p95 <= 300 and failures / requests <= .005

healthy = dict(version="release-42", sampled=False, requests=1000, failures=2,
               window_seconds=900, age_seconds=30, p95_ms=180)
assert may_promote(healthy, "release-42")
assert not may_promote({**healthy, "failures": 20}, "release-42")
assert not may_promote(healthy, "release-41")
assert not may_promote({**healthy, "requests": 0}, "release-42")
assert not may_promote({**healthy, "requests": True}, "release-42")
assert not may_promote({**healthy, "failures": -1}, "release-42")
assert not may_promote({**healthy, "failures": 1001}, "release-42")
assert not may_promote({**healthy, "sampled": True}, "release-42")
assert not may_promote({**healthy, "age_seconds": 121}, "release-42")
assert not may_promote({**healthy, "window_seconds": 899}, "release-42")
assert not may_promote({**healthy, "p95_ms": float("nan")}, "release-42")
assert not may_promote({k: v for k, v in healthy.items() if k != "p95_ms"}, "release-42")
```

In a real gate, bind the observation to the deployed digest, environment, cohort and query interval, verify telemetry completeness and source, and define rollback ownership. A low-volume or missing signal should not silently be treated as healthy.

#### Example 4 — retries can hide flaky tests

For 100 independent tests each with a 0.5% false-failure probability, the chance of an entirely green first run is `0.995 ** 100 ≈ 60.58%`. Retrying each failed test once, assuming independent failures, raises the chance of an eventually green suite to `(1 − 0.005 ** 2) ** 100 ≈ 99.75%`. That change improves the displayed pass rate without repairing the tests. Report first-attempt results, retries and quarantine scope separately; correlated failures invalidate this simple model.

#### Example 5 — complete evidence is an intersection

For release IDs 1–20, suppose artifact identity is verified for 1–18, security results exist for 4–19, and deployment records exist for 6–20. Individual coverage is **90%, 80% and 75%**. Complete linked evidence exists only for IDs 6–18: **13/20 = 65%**. Neither the average nor the smallest individual coverage equals the intersection. Investigate the missing links before claiming release traceability.

#### Example 6 — retained rows are not request counts

Suppose nine retained successful rows each represent ten requests, while one retained failed row represents one. Raw counts report **1/10 = 10%** failure. Weighted estimates give **1/(9×10+1) ≈ 1.10%**, over 91 estimated requests. This illustrates why `itemCount` matters; it does not make a biased or broken sample trustworthy. Use the actual schema and sampler, and keep appropriate unsampled metrics for decisions that need them.

#### Example 7 — remaining error budget

A fictional monthly request SLO is 99.9% over 30 million requests: **30,000 failed requests** are allowed. If 18,000 have already failed, 12,000 remain. At 10,000 requests/minute and a 1% error rate, failures consume **100/minute**, exhausting that remaining budget in **120 minutes** if conditions stay constant. The observed error rate is **10 times** the allowed 0.1% rate. This estimate supports a release decision; it is not a promise that future traffic or impact will stay constant.

---

## 8. Hands-on labs

### Lab 1 — Work-to-production traceability

Create an issue/work item with acceptance criteria, link a branch, PR, commit, build, artifact and deployment, and generate release notes. Break one link and identify what a stakeholder can no longer prove.

**Evidence:** traceability map, integration identity/scope, generated notes and broken-link finding.

### Lab 2 — Branch flow and recovery

Implement short-lived PR flow with required review/checks and a controlled emergency path. Revert a shared defect, restore a deleted file via a new commit and recover an unpublished commit with reflog. Explain why reset differs.

**Evidence:** policy export/screenshots, commit graph, recovery commands/results and bypass audit.

### Lab 3 — Immutable package pipeline

Build a small application once, run unit tests, publish coverage, generate a version from tag/commit/run, publish a package/artifact and record its digest. Promote it to a release view or second stage without rebuilding.

**Evidence:** YAML, test/coverage result, version contract, digest and promotion record.

### Lab 4 — Reusable multi-stage pipeline

Create reusable YAML with validate, build, integration and deployment stages. Use explicit dependencies, parallel safe tests, a protected environment, approval/check and retention. Trigger from PR and main without duplicate runs.

**Evidence:** evaluated graph, reusable input/output contract, run timelines and environment history.

### Lab 5 — Progressive deployment and database compatibility

Deploy two versions to slots or a small lab service, warm/health-check the candidate and shift/swap exposure. Add a flag and tabletop an expand–migrate–contract database change. Force a health failure and restore service.

**Evidence:** version/cohort telemetry, flag state, migration sequence, stop/rollback timeline and last-known-good proof.

### Lab 6 — IaC self-service and drift

Deploy a Bicep environment through a pipeline using lint/preflight/what-if, policy/security scan and federated identity. Change a resource manually, detect drift and decide whether reconciliation is safe. Diagram an Azure Deployment Environments catalog equivalent.

**Evidence:** source, what-if, deployment record, drift decision and catalog/environment-type design.

### Lab 7 — Secretless pipeline and security chain

Configure GitHub OIDC or Azure Pipelines WIF to a least-privilege Azure scope. Add secret, dependency, code/IaC and container scans to a sample pipeline. Deliberately introduce safe synthetic findings, remediate them and verify no secret appears in logs/artifacts.

**Evidence:** trust subject/issuer/audience, RBAC, scan results, blocked gate, clean rerun and audit log.

### Lab 8 — Instrumentation and delivery incident

Instrument a small service with Application Insights/OpenTelemetry, include application version and deployment ID, and create a dashboard/query for throughput, failures and p95 latency. Deploy a controlled fault, alert, trace it to the version, roll back and create retrospective work.

**Evidence:** KQL, trace, alert payload/runbook, deployment correlation, recovery time and owned actions.

---

### Lab 9 — trust and evidence across pipeline boundaries

Inventory workflow events, actors, runner pools, cache modes, token permissions, reusable workflow SHAs and cloud trust subjects. Tabletop an untrusted PR artifact arriving at a privileged follow-up job. Require expected run/source/digest/provenance checks before consuming it. Trace package feed and view permissions separately, then verify retained release evidence covers the rollback window.

**Evidence:** trust diagram, expected versus observed identities, artifact verification policy, policy insights and a retention gap register. No actual compromise or privileged job execution is needed for the tabletop.

### Lab 10 — replace a placeholder promotion gate

Use the promotion blog below as a design exercise. Replace its simulated validation with explicit test/security/health evidence, protected deployment resources and failure/cancellation behavior. Run example 3 locally, vary one condition at a time and explain each rejection. Add database compatibility, missing telemetry, public package access migration and issuer conversion to the tabletop.

**Evidence:** reviewed decision policy, local gate results, rollback ownership, compatibility assumptions and migration acceptance criteria. A passing local predicate is not proof that a cloud release succeeded.

---

## 9. Knowledge checks

1. Why is a green build not proof of a successful release?
2. What evidence connects a business request to a production change?
3. How do lead time and cycle time differ?
4. Why should story points not rank individual productivity?
5. When is trunk-based development preferable to release branches?
6. What do protection rules not guarantee?
7. Why is `git revert` usually safer than `git reset` on a shared branch?
8. What must happen first after a committed secret is discovered?
9. What does Git LFS store in normal Git history?
10. Why promote one package instead of rebuilding per environment?
11. How does an Azure Artifacts feed view differ from a feed?
12. Why is code coverage not equivalent to test quality?
13. What makes a flaky-test quarantine responsible?
14. What security risk is special to persistent self-hosted runners?
15. How do triggers differ from conditions?
16. Why do filesystem outputs not automatically cross jobs?
17. What is the key difference between a feature flag rollout and an A/B test?
18. Why use expand–migrate–contract for database changes?
19. What should a hotfix path preserve?
20. What current replacement should new designs prefer over Azure Automation State Configuration?
21. Why is workload identity federation preferable to a stored client secret?
22. What is the difference between Azure DevOps access level and permission?
23. How do Defender for Cloud DevOps security and repository scanners relate?
24. What dimensions let telemetry connect a production symptom to a deployment?

25. Why can a PR check pass while a merge queue stalls?
26. Does the Azure DevOps public-project retirement retire private enterprise projects?
27. Can a package consumer bypass a restricted feed through a permitted view?
28. Can Azure Artifacts promotion be rolled back by demoting the package?
29. Does generating an attestation prove the deployed bytes are approved?
30. Does the Node 24 action-runtime migration upgrade application code automatically?
31. Do workflow execution policies replace safe event and runner design?
32. Can a called reusable workflow receive more cache access than its caller?
33. Which workflow identity do the new job.workflow_* properties describe?
34. Why is a branch-only Azure Pipelines condition insufficient for deployment?
35. Can a variable computed during a job decide whether that job starts?
36. Does changing an approver group rewrite a pending Azure Pipelines approval?
37. runLatest versus sequential for an exclusive lock?
38. Does Template-level what-if prove provider readiness and deployment permissions?
39. Will retaining a Git tag preserve expiring Actions checks and artifacts?
40. Does the July 2027 Azure DevOps issuer announcement apply to every cloud and application type?
41. Does adding an Entra identity automatically authorize Azure DevOps repository access?
42. Is Azure DevOps CodeQL default setup equivalent to scanning all PR branches and languages?
43. How much elapsed time does example 1 save by parallelizing the first three jobs?
44. Does six average occupied runner slots justify a six-slot pool with no queue risk?
45. Why reject the candidate in example 3 despite a low global error rate?
46. Does a 99.75% pass rate after retries prove the flaky suite is repaired?
47. Why is complete evidence coverage 65% when individual coverage is 90%, 80% and 75%?
48. Can count() replace weighted request totals under sampling?

### Answers

1. It proves configured build steps passed; deployment, configuration, exposure, runtime health and user outcome can still fail.
2. Linked work/acceptance criteria, reviewed commit/PR, build and immutable artifact provenance, test/security results, authorized environment deployment and runtime outcome.
3. Lead time covers request-to-delivery; cycle time typically covers active-work-to-completion, with exact states defined by the team.
4. Estimation units vary by team/work and are easy to game; optimize system flow and outcomes instead.
5. When small changes can integrate frequently under fast automation and incomplete features can remain safely hidden.
6. That checks are relevant, reviews are independent/thoughtful, bypass is appropriate or the protected configuration itself is correct.
7. Revert adds an auditable inverse commit without rewriting history other collaborators use; reset moves history and can require force update.
8. Revoke/rotate it, then investigate exposure; history rewrite alone cannot invalidate a copied credential.
9. A small pointer containing object identity/size metadata; the large object is stored in the LFS service.
10. It preserves artifact identity, provenance and test evidence so each stage receives the same bits.
11. The feed stores/manages packages; a read-only view exposes a promoted subset/quality state of versions in that feed.
12. Coverage measures executed code, not assertion correctness, missing requirements or realistic failure behavior.
13. An owner, tracked risk, deadline, visible exclusion and repair—not indefinite blind retry.
14. Untrusted code can persist changes or steal credentials/network access that affect later privileged jobs.
15. A trigger starts a run from an event/schedule; a condition controls whether an element runs within that run.
16. Jobs can execute on different clean workers; outputs must be declared or published/downloaded as artifacts/caches appropriately.
17. Rollout controls exposure; A/B testing also requires a hypothesis, controlled cohorts and statistically valid outcome/guardrail analysis.
18. It keeps old and new application versions compatible throughout progressive rollout and rollback windows.
19. Source provenance, required security/quality evidence, authorized deployment, rollback, forward merge/backport and auditability.
20. Azure Machine Configuration; Azure Automation State Configuration is announced to retire September 30, 2027.
21. It exchanges short-lived, context-constrained tokens and removes stored credential rotation/exposure risk.
22. Access level licenses/enables broad features; permissions authorize specific actions on scoped objects.
23. Repository scanners produce findings near code; Defender can aggregate/prioritize DevOps posture and correlate code to cloud, subject to configured products/connectors.
24. At least service, environment, region, application/artifact version, instance, trace/operation ID and deployment ID/cohort.

---

25. Required checks must also run for the merge-group commit; GitHub Actions needs merge_group and external CI needs the queue branch/event handling.
26. No. It changes public creation/access; inventory anonymous consumers and the 2027 conversion notice.
27. Yes. Restrict both feed and view access; an empty Specific people list inherits feed permissions.
28. No. Promotion cannot be demoted; deploy a retained earlier immutable version when rollback is appropriate.
29. No. Verify the actual artifact against trusted provenance and policy, and separately inspect test/security evidence.
30. No. JavaScript action execution and the application runtime/toolchain are separate.
31. No. Actor/event allowlists do not make privileged execution of untrusted code safe.
32. No. The cache service enforces that boundary; explicitly granting writes to low-trust events still creates risk.
33. The workflow file defining that job; it can differ from the caller in a reusable workflow.
34. A custom condition replaces the default success condition; require dependency success as well as the branch.
35. No. Evaluation time differs; use prior-job outputs and declared dependencies for that decision.
36. No. The approver list is fixed when checks begin.
37. runLatest allows the latest competing run; sequential processes all queued runs in order. Choose for the stateful operation, not merely speed.
38. No. It is static validation; inspect the chosen level and any resources/modules excluded from analysis.
39. No. Audit and rollback evidence need their own retention/export; October 2026 expands Actions retention to checks, runs and statuses.
40. No. Its scope is public-cloud connections with single-tenant applications or managed identities; specified sovereign/multi-tenant cases are excluded.
41. No. Add it to the target organization and assign the required access level, Azure DevOps permissions and connection authorization.
42. No. It scans the default branch with documented language/build limits; advanced setup handles other requirements.
43. 14 minutes, from 48 to 34; modeled worker consumption remains 33 minutes.
44. No. That is 100% average utilization and leaves no capacity for variation or added scans.
45. Its own cohort fails at 2%, ten times the control rate; aggregation hides the regression.
46. No. First-attempt failures and retry counts expose the underlying instability.
47. Only 13 of the 20 releases have all three linked evidence sets; completeness is their intersection.
48. No. It counts retained rows; use documented weights for estimates and appropriate unsampled metrics for release decisions.

---

## 10. Final review checklist

- [ ] I can trace one change from owned work through code, artifact, deployment, telemetry and feedback.
- [ ] I can choose flow metrics and dashboards without turning proxies into individual targets.
- [ ] I can implement GitHub/Azure Boards traceability, documentation and actionable notifications.
- [ ] I can compare trunk, feature and release branches and enforce an appropriate PR policy.
- [ ] I can handle LFS/large-repository choices and recover or remove Git data safely.
- [ ] I can design immutable package/version/upstream/view and retention strategies.
- [ ] I can layer tests, meaningful coverage, quality gates and flaky-test controls.
- [ ] I can compare GitHub Actions/Azure Pipelines and hosted/self-hosted execution.
- [ ] I can author reusable multi-stage YAML with explicit triggers, conditions, dependencies and environments.
- [ ] I can select rolling, blue-green, canary/ring, flag and A/B strategies and design a hotfix/rollback path.
- [ ] I can implement IaC, desired state and governed self-service while accounting for retiring Automation State Configuration.
- [ ] I can optimize pipeline time, reliability, concurrency, cost and retention from evidence.
- [ ] I can choose human/app/token/service-principal/managed-identity/service-connection boundaries.
- [ ] I can implement federation, Key Vault/secure-file handling and leak prevention.
- [ ] I can combine secret, code, dependency/license, IaC and container scanning.
- [ ] I can correlate delivery, application, infrastructure and user evidence using Application Insights and KQL.
- [ ] I completed at least one end-to-end pipeline and one failure-injection lab.

---

## Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick the resources and formats that fit you, and use the official July 27, 2026 objectives as the coverage checklist. Estimated times include reasonable note-taking or practice where stated and should be rechecked before purchase. Older material can still teach durable concepts, but reconcile every product screen, feature, identity method and objective against current documentation.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official AZ-400 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) | Free; authoritative scope and change log | 60–90 min initially; 10–15 min before exam |
| [Microsoft Learn AZ-400 course](https://learn.microsoft.com/en-us/training/courses/az-400t00) | Free self-paced collection; instructor-led delivery may be paid; official instructor-led duration 4 days | Plan 30–45 hr self-paced with notes/labs, or 4 instructor-led days plus review |
| [Microsoft free AZ-400 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/?practice-assessment-type=certification) | Free with Microsoft Learn account | 45–90 min per attempt; plan 3–5 hr with remediation |
| [Microsoft AZ-400 Exam Readiness Zone](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/?terms=AZ-400) | Free short objective-review videos; verify age against July 2026 scope | Selected-video runtime unverified from the series shell; plan 2–4 hr for a focused selection and blueprint reconciliation |
| [Azure DevOps Labs](https://azuredevopslabs.com/) | Free Microsoft-authored/maintained hands-on labs; choose by gap | 1–2 hr per selected lab; plan 8–16 hr for a focused set |
| [Pluralsight AZ-400 certification path](https://www.pluralsight.com/paths/az-400-designing-and-implementing-microsoft-devops-solutions) | Paid path: legacy 2023 full course, five 2024–2025 domain courses and three April 2026 labs; includes John Savill security content | 36 hr heading; components total 35h 36m, including a 15h 22m legacy course. Five domain courses plus labs total 20h 14m; avoid duplicate coverage |
| [O'Reilly: Exam AZ-400 Microsoft Azure DevOps Solutions Crash Course](https://www.oreilly.com/live-events/exam-az-400-microsoft-azure-devops-solutions-crash-course/0636920382614/) | Paid/subscription Tim Warner event; public agenda accessible but contains AZ-500/Security Engineer and obsolete exam-name errors; current booking date unverified | Two 3-hour agenda days, including breaks; older catalog option, not a verified current booking or complete 2026 course |
| [Udemy: AZ-400 Designing and Implementing DevOps Certification](https://www.udemy.com/course/azure100/) | Paid; Alan Rodrigues; browser provider page confirms September 2025, 10 sections and 258 lectures; direct fetch blocked | 20 hr 46 min video; plan 30–40 hr with labs and July 2026 reconciliation |
| [Whizlabs AZ-400 training and practice](https://www.whizlabs.com/microsoft-azure-certification-az-400/) | Paid; public fetch returned a JavaScript shell, so current bundle contents were not verified | Verify current duration; plan 15–30 hr plus targeted remediation |
| [MeasureUp AZ-400 practice test](https://www.measureup.com/microsoft-practice-test-az-400-designing-and-implementing-microsoft-devops-solutions.html) | Paid; 139 questions displayed, last updated August 2024; reconcile with July 2026 objectives | Plan 4–7 hr across baseline, review and retest |
| [John Savill DevOps Master Class playlist](https://www.youtube.com/playlist?list=PLlVtbbG169nFr8RzQ4GIxUEznpNR53ERq) and [public whiteboards/materials](https://github.com/johnthebrit/DevOpsMC) | Free; broad durable concepts and Azure DevOps/GitHub demonstrations; 2021 content needs current-product reconciliation | Historical 12h 39m estimate not reverified from the playlist shell; plan 16–22 hr with notes/current docs |
| [Microsoft Reactor Agentic DevOps Live series](https://developer.microsoft.com/en-us/reactor/series/s-1625/) | Free/on-demand Microsoft sessions; current supplement, not full AZ-400 coverage | Twelve distinct one-hour scheduled sessions, January 27–April 21, 2026; select 1–6 hr by gap; recordings not watched |

#### Experienced delivery/platform engineer route

1. Diff the July 2026 blueprint and complete Microsoft Learn modules only for weak domains.
2. Implement Labs 3–8 using the pipeline platform you know least.
3. Study current federation, GitHub/Azure hybrid, Deployment Environments, Machine Configuration and Defender changes directly from docs.
4. Use practice assessments to choose remediation; reproduce each weak design in YAML or a tabletop.

**Planning range:** 55–85 focused hours after Azure administration/development prerequisites.

#### Newer to DevOps route

1. Learn Git, pull requests, testing, Azure identity/RBAC, networking and basic application deployment first.
2. Complete the Microsoft Learn course and all ten labs in this guide.
3. Use one structured video path, John Savill’s concepts and targeted Azure DevOps Labs—do not consume every course.
4. Practice one complete system repeatedly: work item to progressive production exposure to trace/rollback.

**Planning range:** 110–170 hours after foundational Git, Azure and software-delivery study.

---

### Currency and integrity note

This guide is an independent synthesis of public sources. It does not reproduce exam questions and is not an exam dump. Microsoft and GitHub can change objectives, credential prerequisites, product names, security/licensing plans, hosted images, runner/agent behavior, limits, identity issuers, pipeline tasks, Azure service capabilities and retirement dates. Verify the official blueprint, credential page, retirement notices and linked product documentation before an exam or production decision.

### Blog reading with a pipeline review exercise

| Reading | Learning value | Deliverable and boundary |
|---|---|---|
| [PAT-free Azure DevOps service connection](https://devblogs.microsoft.com/devops/you-can-now-use-the-azure-devops-service-connection-instead-of-a-pat-or-build-session-token/) — Eric van Wijk, August 6, 2026 | Connects secretless authentication to cross-organization repositories, feeds and APIs | Map identity membership, licensed access, permissions, federation and pipeline authorization. The launch uses a preview-labeled connection; current task versions and service availability control implementation. |
| [Azure DevOps issuer retirement](https://devblogs.microsoft.com/devops/retirement-of-azure-devops-issuer-in-workload-identity-federation-service-connections/) — Eric van Wijk, June 22, 2026 | Shows that a secretless pipeline still needs trust maintenance | Inventory issuer, cloud and application type. Plan conversion validation before deleting old trust, with special attention to excluded clouds/multi-tenant identities. |
| [Dev-to-prod with Azure DevOps and Azure Developer CLI](https://devblogs.microsoft.com/devops/azure-developer-cli-from-dev-to-prod-with-azure-devops-pipelines/) — PuiChee and Kristen, August 13, 2025 | Demonstrates immutable package promotion across stages | Trace the same package into both targets, then replace the article's TODO/sleep validation with actual checks. Add protected deployment resources, provenance verification, pinned tooling and failure handling. The demonstration is not a completed production gate. |

Only the noted public sections were reviewed; linked sample repositories and cloud commands were not executed. Treat examples and launch posts as starting points to evaluate against the current primary documentation.
