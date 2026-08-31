---
exam_code: TERRAFORM-AUTHORING-OPERATIONS-PROFESSIONAL
vendor_id: hashicorp
official_blueprint: https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-review
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: scheduled
upcoming_change_checked: 2026-08-31
---

# HashiCorp Certified: Terraform Authoring and Operations Professional Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official HashiCorp professional exam content list](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-review) is authoritative.

**Current baseline:** Terraform Authoring and Operations Professional, AWS-provider exam version; verified August 31, 2026<br>
**Upcoming blueprint change:** HashiCorp says an Azure-provider exam version is in active development with expected launch in late 2026. Both versions award one Terraform Professional credential; verify availability before scheduling.<br>
**Official source:** [Terraform Authoring and Operations Professional content list](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-review)

HashiCorp does not display a short exam code for this credential. This library uses `TERRAFORM-AUTHORING-OPERATIONS-PROFESSIONAL` as a stable internal identifier.

## How to use this guide

This is a performance-oriented professional credential, not an associate exam with harder vocabulary. HashiCorp expects extensive production experience, Linux terminal fluency, cloud-provider and credential knowledge, and deep Terraform authoring and operations skill. The [official orientation](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-orientation) describes lab scenarios whose grading inspects configuration, state, and provisioned infrastructure, plus a multiple-choice HCP Terraform portion.

Choose a route:

- **Gap analysis:** Read the objective map and high-value distinctions, then use the official content list to identify weak operations.
- **Authoring practice:** Concentrate on dynamic expressions, types, validation, modules, provider configuration, and refactoring without address churn.
- **Operations practice:** Repeatedly initialize, plan, import, move, apply, diagnose, and recover disposable environments under time pressure.
- **Exam-environment practice:** Work from a Linux terminal with unfamiliar editor defaults, limited documentation, and no general web search. Accuracy and verification matter more than typing speed.
- **HCP Terraform review:** Study runs, workspaces, access, credentials, and policy as architecture decisions. HashiCorp labels this domain multiple-choice only.

The [Terraform Associate (004) guide](TERRAFORM-ASSOCIATE-004-hashicorp-terraform-associate.md) is a prerequisite refresher, not a substitute for production experience.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

HashiCorp publishes six domains and detailed subobjectives without percentage weights. Do not infer scoring from this guide's length or the number of bullets.

| Published domain | Weight | Guide coverage |
|---|---:|---|
| 1. Manage resource lifecycle | Not published | CLI workflow, plans, apply/destroy, import, state, drift, and safe refactoring |
| 2. Develop and troubleshoot dynamic configuration | Not published | Validation, data sources, functions, expressions, meta-arguments, types, outputs, and sensitive data |
| 3. Develop collaborative Terraform workflows | Not published | Version management, remote state, automation, locking, and cross-configuration data |
| 4. Create, maintain, and use Terraform modules | Not published | Interface design, composition, sourcing, versioning, refactoring, and migration |
| 5. Configure and use Terraform providers | Not published | Plugin architecture, aliases, sourcing, upgrades, authentication, and troubleshooting |
| 6. Collaborate on infrastructure as code using HCP Terraform | Not published | Runs, workspaces, access, dynamic credentials, policy, and governance; multiple-choice only |

## Exam operating model

The current exam uses AWS resources. HashiCorp's content list names the provider resources and documentation available for that version. The announced Azure version changes provider syntax and cloud-resource behavior, not the durable Terraform domains. **VERIFY CURRENT:** provider-version availability, the resources exposed in the environment, permitted documentation, keyboard constraints, and exam delivery details immediately before scheduling.

Treat each lab as a small production change:

```text
requirements
    ↓
inspect configuration, state, provider, and environment
    ↓
predict the smallest safe change
    ↓
format + validate + plan
    ↓
read addresses, dependencies, and replacement reasons
    ↓
apply only when the plan matches intent
    ↓
verify configuration + state + remote result
```

Do not optimize for “a successful command.” A configuration can validate while targeting the wrong account, an apply can succeed while creating the wrong topology, and a manual cloud change can satisfy a visual check while leaving Terraform state inconsistent.

> **Related item:** Performance exams reward a repeatable verification loop. Shell history, targeted state inspection, saved plan output, and provider/API observations are evidence; success-colored terminal output alone is not.

## 1. Manage resource lifecycle

### Initialize with intent

`terraform init` installs providers and modules, prepares the backend, and creates or updates local initialization metadata. It is safe to rerun, but backend and dependency changes still require judgment. Know when to use normal initialization, `-upgrade`, backend migration, or reconfiguration. The [initialization command reference](https://developer.hashicorp.com/terraform/cli/commands/init) is the precise source for current options.

Before initializing, identify:

- the root module and working directory;
- the required Terraform and provider versions;
- the backend and target state location;
- module sources and credentials;
- whether a backend change should migrate existing state or deliberately start elsewhere.

A common professional failure is initializing successfully against the wrong backend or workspace. Check the backend configuration and current workspace before planning.

### Plan as a diagnostic artifact

The [plan command](https://developer.hashicorp.com/terraform/cli/commands/plan) combines configuration, prior state, provider observations, input values, and dependency analysis. Read the full plan rather than only the summary.

For each action, ask:

1. Is the resource address the intended instance?
2. Is a change in-place, create, destroy, replace, import, move, or forget?
3. What forces replacement?
4. Which values remain unknown until apply, and why?
5. Did refresh expose drift?
6. Are provider aliases, regions, accounts, and credentials correct?
7. Does targeting hide related changes?

Resource targeting is a recovery and exceptional-scoping tool, not a normal decomposition strategy. A targeted plan can omit other changes required to reconcile the complete configuration. Follow it with an untargeted plan.

### Apply and destroy safely

Applying a saved plan binds execution to the reviewed proposal; applying without a plan file creates a fresh plan. Both can become unsafe if credentials, remote objects, or external dependencies change. Terraform is not a transaction coordinator across independent provider APIs: a failure can leave partial changes. Inspect the resulting state and create a new plan before retrying.

Destroy is a planned lifecycle operation. Review dependencies, retention requirements, provider protections, lifecycle rules, and data backups. `prevent_destroy` can block a Terraform destroy or replacement, but it is not a backup, cloud deletion lock, or authorization boundary.

### State, import, drift, and refactoring

Terraform [state](https://developer.hashicorp.com/terraform/language/state) maps configuration addresses to remote identities and retains attributes needed for planning. Professional operations require distinguishing four things:

| Operation | Configuration | State binding | Remote object |
|---|---|---|---|
| Normal apply | Desired declaration changes | Updated | Created/changed/deleted to converge |
| Import | Must describe the intended object | Existing identity becomes bound | Not created by import |
| `moved` block | New address declared | Binding moves to new address | Normally preserved |
| Remove from management | Declaration records or implies removal | Binding removed | May be destroyed or retained depending on method |

Use configuration-driven [import blocks](https://developer.hashicorp.com/terraform/language/import) when a reviewed, repeatable import belongs in the change. Import creates a binding; it does not prove that the configuration fully matches the remote object. Always plan afterward.

When drift appears, determine whether the remote change was authorized and whether configuration or the object should become authoritative. A refresh-only plan updates state to remote reality without proposing configuration convergence. It is useful only when accepting the remote change is the intended decision.

> **Related item:** State surgery can repair a binding, but it bypasses normal configuration review. Back up state, record the reason, use the narrowest command, and immediately verify with a full plan.

### Failure patterns

- wrong backend or workspace;
- importing to the wrong address or provider alias;
- renaming a resource without a `moved` block;
- using `-target` until the plan looks quiet;
- treating refresh-only as remediation rather than acceptance of observed reality;
- retrying a partial apply without inspecting state and the remote system;
- applying a plan generated with different input, credentials, or provider assumptions.

## 2. Develop and troubleshoot dynamic configuration

### Model data before writing expressions

Strong HCL starts with stable identities and precise types. Choose structures based on meaning:

| Need | Prefer | Reason |
|---|---|---|
| Named objects whose identity must survive reordering | `map(object(...))` with `for_each` | Stable keys become instance addresses |
| Ordered repeated values | `list(T)` | Position is meaningful |
| Unique unordered values | `set(T)` | Membership matters, not position |
| A fixed heterogeneous interface | `object({...})` or `tuple([...])` | Shape is explicit |
| Derived reusable expression | `locals` | Names a transformation without expanding the module interface |

Use input validation to reject invalid caller data, preconditions to assert assumptions before an operation, postconditions to assert guarantees after evaluation, and check blocks for ongoing assertions that should report rather than necessarily block infrastructure changes. Review current semantics in [custom conditions and validation](https://developer.hashicorp.com/terraform/language/validate).

### Data sources and unknown values

A data source queries a provider without owning the remote object's lifecycle. A reference creates an implicit dependency when data flows between objects. Use `depends_on` only for a real behavioral dependency that expressions cannot represent.

Unknown values are not errors. Terraform preserves them when an input can be known only after an upstream apply. Trouble begins when an unknown value is needed to determine instance count, `for_each` keys, provider selection, or another graph-shaping decision during planning. Move stable identity into configuration-known keys and keep apply-time values in attributes.

### Expressions, functions, and meta-arguments

Be fluent with conditionals, `for` expressions, splats, collection functions, string/path functions, `try`, `can`, `coalesce`, `flatten`, `merge`, `setproduct`, and type conversion. The goal is not memorizing every [function](https://developer.hashicorp.com/terraform/language/functions); it is recognizing input types, output shape, unknown/null behavior, and stable keys.

Meta-arguments solve different problems:

| Meta-argument | Decision |
|---|---|
| `count` | Create indexed instances when position is stable and meaningful |
| `for_each` | Create keyed instances when identity should follow a key |
| `depends_on` | Add a hidden dependency not represented by value flow |
| `provider` | Select a nondefault provider configuration |
| `lifecycle` | Change replacement, ignore, or safety behavior |

Avoid `ignore_changes` as a blanket drift suppressor. It deliberately assigns ownership of selected attributes elsewhere; document that control plane and ensure ignored changes cannot undermine security or availability.

### Sensitive data

Marking a value sensitive redacts normal display but does not remove it from state or plan artifacts. Prefer short-lived provider credentials, external secret stores, and supported ephemeral or write-only paths where appropriate. Protect state, saved plans, crash logs, debug output, CI artifacts, and shell history. HashiCorp's [sensitive-data guidance](https://developer.hashicorp.com/terraform/language/manage-sensitive-data) distinguishes display protection from persistence protection.

> **Related item:** Vault can issue dynamic secrets, but Terraform may still persist values it receives if the provider/resource schema stores them. Secret issuance and state persistence are separate boundaries.

### Troubleshooting sequence

1. Run `terraform fmt -check` and `terraform validate`.
2. Inspect exact type errors rather than adding conversions at random.
3. Use `terraform console` with representative values to test expressions.
4. Inspect instance keys and addresses.
5. Separate configuration-known, state-known, data-source, and apply-time values.
6. Reduce the expression to a small local value or output in a disposable branch.
7. Enable targeted logging only when necessary; protect and delete the logs afterward.

## 3. Develop collaborative Terraform workflows

### Pin, lock, and upgrade deliberately

Manage four version layers separately:

- Terraform CLI constraint and installation;
- provider source constraints and `.terraform.lock.hcl` selections;
- module sources and versions;
- cloud/API behavior outside Terraform's version system.

Constraints define acceptable versions; the lock file records selected provider versions and checksums. Test upgrades in a branch, review lock changes, read upgrade notes, plan representative environments, and roll forward in controlled stages.

### Remote state and locking

Remote state centralizes the address-to-object record for collaboration. It requires access control, encryption, recovery/versioning, and locking appropriate to the backend. Locking reduces concurrent writers; it does not resolve competing design ownership or guarantee that every backend supports locking identically. Review [remote state](https://developer.hashicorp.com/terraform/language/state/remote) and the selected backend's current behavior.

Split state by lifecycle, ownership, blast radius, and access—not merely by directory aesthetics. Avoid a single state that forces unrelated teams to share credentials and change windows; also avoid fragments connected by fragile chains of remote outputs.

### Share data across configurations

`terraform_remote_state` exposes root outputs from another state but requires access to the backing state system, which may be broader than the output implies. HCP Terraform's `tfe_outputs` can provide a narrower output-sharing path. Alternatives include publishing identifiers through a configuration registry, DNS, parameter store, or provider data source.

Choose based on ownership, freshness, access boundary, failure behavior, and whether the consumer needs a Terraform-specific coupling.

### Automation workflow

A dependable pipeline separates:

```text
format/validate → test/static checks → speculative plan → review/policy
                → approved apply → post-apply verification → evidence
```

Use noninteractive flags intentionally, inject credentials through the platform, serialize applies per state, preserve a reviewable plan where appropriate, and ensure the apply uses the reviewed revision and inputs. Do not expose state or plan files as broadly readable build artifacts.

> **Related item:** A pipeline is part of the Terraform control plane. Protect workflow changes, runner identity, plugin/module provenance, variables, approval rules, and logs with the same care as infrastructure credentials.

## 4. Create, maintain, and use modules

### Design an interface, not a folder

A useful module encapsulates one coherent capability with:

- typed, validated inputs;
- minimal outputs needed by callers;
- stable resource identities;
- documented provider and version requirements;
- explicit security and lifecycle assumptions;
- examples and automated tests;
- an upgrade path for breaking changes.

Avoid mirroring every provider argument as a module variable. That creates an expensive wrapper without a meaningful abstraction. Encode a supported operating model while leaving deliberate extension points.

The [module documentation](https://developer.hashicorp.com/terraform/language/modules) explains calling, sourcing, composition, and scope. Child modules receive values through inputs and expose values through outputs; they do not inherit arbitrary caller variables. Provider configurations should normally be supplied by the root module, while reusable child modules declare provider requirements.

### Version and refactor safely

Registry modules can use semantic version constraints. Git sources should reference deliberate tags or immutable commits rather than floating branches for production. Test a new module version against representative callers.

Refactoring can change code without changing remote infrastructure when address migrations are declared. Use `moved` blocks for resource or module address changes and preserve them long enough for all supported upgrade paths. When splitting a configuration into modules or separate states, plan the address and state migration before editing files.

### Module review questions

- Does each input represent a supported decision rather than provider passthrough?
- Are types and defaults safe?
- Can callers accidentally create unstable `for_each` keys?
- Which resources force replacement when an input changes?
- Are outputs sufficient but not secret-heavy?
- Are providers injected correctly for aliases and multiple regions/accounts?
- Can an older caller traverse the proposed migration without destroy/recreate?

## 5. Configure and use providers

Terraform Core loads provider plugins that define schemas, translate planned operations, call remote APIs, and return state. Provider source addresses and version constraints belong in `required_providers`; endpoint, region, alias, and authentication behavior belong in provider configurations. Review [provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements).

### Aliases and module boundaries

Use aliases for multiple configurations of one provider, such as regions or accounts. Pass aliased configurations explicitly to modules and declare `configuration_aliases` where a child module expects them. A resource that silently uses the default provider can target the wrong environment even when every other value looks correct.

### Authentication

Prefer the provider's supported ambient or workload-identity chain over static credentials in configuration. Understand precedence among environment variables, shared credential files, instance/workload identity, assumed roles, and explicit arguments. The exact chain is provider-specific and **VERIFY CURRENT**.

### Troubleshooting providers

Classify the failure before changing configuration:

| Failure phase | Likely boundary |
|---|---|
| `init` cannot install | Source address, network/registry access, constraint, lock checksum, platform build |
| Schema/configuration error | Provider version, renamed/deprecated argument, wrong alias, missing required block |
| Authentication error | Credential source, expiration, trust, tenant/account, environment precedence |
| Authorization error | Identity is known but lacks action/resource permission |
| API validation error | Provider request conflicts with remote service rules |
| Inconsistent result/state error | Provider bug, eventual consistency, concurrent change, schema mismatch |

Do not delete the lock file or state as a first troubleshooting step. Preserve evidence, reproduce narrowly, and compare provider release notes and debug logs without leaking secrets.

## 6. Collaborate using HCP Terraform

This domain is multiple-choice only in the current official content list, but it still tests architectural reasoning.

### Runs and workspaces

An HCP Terraform workspace owns state, variables, run history, execution settings, and access around one configuration boundary. A run moves through planning, policy and task checks, approval, apply, and completion states depending on configuration. Review current [run behavior](https://developer.hashicorp.com/terraform/cloud-docs/run) and [workspace concepts](https://developer.hashicorp.com/terraform/cloud-docs/workspaces).

Do not confuse an HCP Terraform workspace with a CLI workspace. A CLI workspace is an alternate state instance for one working directory; an HCP workspace is a managed collaboration and execution boundary.

### Credentials and access

Workspace variables can hold configuration and sensitive values, but long-lived cloud keys create rotation and exposure burden. [Dynamic provider credentials](https://developer.hashicorp.com/terraform/cloud-docs/dynamic-provider-credentials) use workload identity to obtain short-lived credentials for runs. This reduces stored-secret risk while introducing an issuer, audience, claim, trust-policy, and role-permission boundary that must be governed.

Scope teams and permissions to projects/workspaces based on duties. Separate permission to queue a plan, approve an apply, administer variables, read state, and change workspace settings where the service supports it.

### Policy and extensibility

Policy sets evaluate organization rules against runs. Run tasks integrate external checks; run triggers connect workspace execution dependencies. A control should have a clear enforcement point, failure behavior, ownership, and exception process. See [HCP Terraform policy enforcement](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement).

**VERIFY CURRENT:** HCP Terraform editions, entitlements, run modes, agent behavior, project/workspace permissions, policy engines, run-task stages, health features, and Terraform Enterprise parity change independently.

## Integrated professional playbook

For any scenario, write this compact decision record before changing files:

| Question | Evidence |
|---|---|
| What must be true when finished? | Requirement and observable acceptance check |
| Which root module, backend, workspace, and provider identity apply? | Configuration plus CLI/provider inspection |
| Which addresses and remote objects are involved? | Plan and state inspection |
| Is this create/change, import, refactor, drift acceptance, or management removal? | Lifecycle classification |
| What can be replaced or destroyed? | Plan replacement paths and lifecycle rules |
| How will the change be verified? | Terraform output/state plus provider observation |
| How will partial failure be recovered? | State backup, new plan, remote repair, escalation boundary |

This record prevents the most common category error: using a correct command for the wrong lifecycle intention.

## Hands-on labs

Use disposable personal sandboxes only. Review cost and destroy resources when complete. Never use employer, customer, shared, or production credentials without explicit authorization.

### Lab 1: Import and normalize an existing object

Create a small resource manually in an approved sandbox. Write matching Terraform configuration and an `import` block. Predict the target address, run a plan, apply the import, then iterate configuration until the full plan is intentionally quiet. Record which remote defaults had to be represented and which arguments would force replacement.

### Lab 2: Refactor indexed resources into modules

Start with two `count`-based resources in a root module. Refactor them to `for_each` with stable keys and move them into a child module. First capture the destructive plan without applying. Add precise `moved` blocks, plan again, and prove that remote objects are preserved. Test an upgrade from the original state rather than only a fresh deployment.

### Lab 3: Build and test a dynamic module

Create a module accepting a `map(object(...))`. Use a filtered `for` expression, `for_each`, typed validation, a precondition, and a useful output. Add `terraform test` cases for valid input, invalid input, and a boundary condition. Use `terraform console` to explain each intermediate collection shape.

### Lab 4: Operate remote state through automation

Configure a disposable remote backend that supports locking and recovery. Build a pipeline that formats, validates, plans, preserves review evidence, and applies only an approved revision. Attempt two concurrent operations safely to observe locking. Document credential injection, state access, artifact retention, and recovery.

### Lab 5: Diagnose provider identity and aliases

Configure two provider aliases targeting distinct disposable regions or accounts. Pass them explicitly to a child module. Introduce one error at a time: missing alias mapping, wrong region, expired credential, insufficient permission, and incompatible provider constraint. For each, identify the failure phase and the smallest correction.

### Lab 6: Design an HCP Terraform operating model

Design projects and workspaces for a shared network and three applications across test and production. Specify state boundaries, VCS/run workflow, team permissions, dynamic credentials, variable sets, policy sets, run tasks, output sharing, failure handling, and audit evidence. Explain why each boundary exists.

### Lab 7: Timed unfamiliar-repository drill

Clone a disposable Terraform repository you did not author. Give yourself 45 minutes to inspect it, initialize it, identify backend/provider/module assumptions, correct one validation error, correct one lifecycle error, produce a safe plan, and write verification steps. Repeat with a different repository until the process—not the file layout—is familiar.

## Knowledge checks

1. Why can `terraform init` succeed against the wrong operational target?
2. What evidence distinguishes an in-place update from replacement in a plan?
3. Why should a targeted plan be followed by a complete plan?
4. What does import change, and what must configuration still prove afterward?
5. When is refresh-only mode an acceptance decision rather than a repair?
6. How does a `moved` block differ from directly changing state?
7. Why must `for_each` keys normally be known during planning?
8. When is `depends_on` justified, and what does overuse cost?
9. Contrast sensitive, ephemeral, and write-only data handling.
10. What should determine a remote-state boundary?
11. What security concern exists when consuming another configuration's remote state?
12. Which revision, inputs, credentials, and plan should an automated apply bind together?
13. Why is a module that exposes every provider argument often a weak abstraction?
14. How can module refactoring preserve remote objects?
15. Contrast provider requirements, provider configurations, and provider aliases.
16. How do authentication and authorization failures differ?
17. Why is deleting `.terraform.lock.hcl` a poor first response to provider trouble?
18. How does an HCP Terraform workspace differ from a CLI workspace?
19. What trust relationship makes dynamic provider credentials work?
20. Which HCP control should own a rule: Terraform condition, policy, run task, or approval—and why?

## High-value distinctions

| Contrast | Remember |
|---|---|
| Valid configuration vs correct change | Syntax/type consistency vs right target and lifecycle intent |
| Speculative plan vs saved plan | Proposed review output vs executable reviewed artifact |
| Import vs create | Bind existing identity vs ask provider to create |
| Refresh-only vs normal plan | Accept observations into state vs converge remote system to configuration |
| `moved` block vs state command | Declarative repeatable migration vs immediate administrative surgery |
| `count` vs `for_each` | Positional identity vs keyed identity |
| Sensitive vs nonpersisted | Display redaction vs exclusion from state/plan through supported paths |
| Locking vs ownership | Serialize writers vs decide which configuration/team controls an object |
| Module interface vs provider wrapper | Supported capability abstraction vs argument passthrough |
| Provider requirement vs configuration | Plugin source/version contract vs one target/auth instance |
| Authentication vs authorization | Prove identity vs permit requested action |
| HCP workspace vs CLI workspace | Managed run/state/access boundary vs alternate local state instance |
| Policy vs run task | IaC governance evaluation vs external integration/check |

## Readiness checklist

- [ ] I can inspect an unfamiliar root module, backend, workspace, provider, and state before changing it.
- [ ] I can initialize, plan, apply, destroy, and recover from partial failure deliberately.
- [ ] I can import objects and reconcile configuration without accidental replacement.
- [ ] I can diagnose drift and choose convergence, acceptance, import, movement, or removal correctly.
- [ ] I can build stable dynamic configuration with precise types and keys.
- [ ] I can use validations, conditions, functions, expressions, and meta-arguments intentionally.
- [ ] I can protect credentials, state, plans, logs, and automation artifacts.
- [ ] I can design, version, test, consume, and refactor modules safely.
- [ ] I can configure aliases, pass providers to modules, manage upgrades, and troubleshoot each failure phase.
- [ ] I can design remote-state and automated workflows with locking, recovery, approval, and evidence.
- [ ] I can explain HCP Terraform runs, workspaces, access, dynamic credentials, policy, and run tasks.
- [ ] I have repeatedly completed timed, hands-on scenarios from a Linux terminal.
- [ ] I checked the current cloud-provider exam version and every **VERIFY CURRENT** item.

## Primary references

- [Official professional exam content list](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-review)
- [Official professional learning path](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-study)
- [Official exam orientation](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-orientation)
- [Terraform state](https://developer.hashicorp.com/terraform/language/state)
- [Terraform modules](https://developer.hashicorp.com/terraform/language/modules)
- [Provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements)
- [HCP Terraform runs](https://developer.hashicorp.com/terraform/cloud-docs/run)

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the official material, labs, instructor, and review format that fit your gaps. Times are approximate consumption time at normal speed; hands-on repetition, troubleshooting, notes, and prerequisite repair add substantial time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [HashiCorp professional learning path](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-study) | Free; cloud exercises require an authorized sandbox | About 20–35 hours for linked reading and implementation (library estimate; the landing page's four-minute read time excludes linked work) | Authoritative ordered review of all six domains; production repetition remains necessary |
| [Professional exam content list](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-review) | Free | About 3–6 hours for an active documentation pass; longer when practicing gaps | Best objective-to-documentation checklist and current provider-version notice |
| [Professional exam orientation](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-orientation) | Free | About 20–40 minutes including notes and environment planning | First-party explanation of prerequisites, lab grading, environment, provider version, and permitted references |
| [HashiCorp professional practice labs](https://developer.hashicorp.com/terraform/tutorials/pro-cert/pro-practice-landing) | Free; interactive labs and cloud-provider access vary | About 4–10 hours across repeated labs (library estimate because HashiCorp publishes only landing-page read time) | Closest first-party preparation for task execution; repeat from clean environments and verify state plus remote results |
| [Terraform Associate (004) guide](TERRAFORM-ASSOCIATE-004-hashicorp-terraform-associate.md) | Free | About 8–14 hours for targeted prerequisite review and selected labs | Repair core workflow, state, module, provider, and HCP gaps before professional practice; not professional-level preparation by itself |
| [HashiCorp Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) | Free; some exercises require HCP or cloud accounts | About 2–6 hours per selected operational gap | Use narrowly for import, refactoring, testing, automation, state, providers, modules, and HCP Terraform rather than consuming the entire catalog |

No current third-party course was included as an exact end-to-end Terraform Authoring and Operations Professional resource during this review. That is a catalog gap, not a claim that none exists. Evaluate any course against the current AWS/Azure exam-version notice and the official content list before investing substantial time.
