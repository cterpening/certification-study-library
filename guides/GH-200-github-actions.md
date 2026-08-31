---
exam_code: GH-200
vendor_id: github
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# GH-200 GitHub Actions Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official GH-200 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200) is authoritative.

**Current baseline:** Skills measured as of January 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)

## How to use this guide

Trace each workflow from event to run, job, runner, identity, data, and result. Reproduce the examples in a disposable repository, deliberately break them, and use logs and contexts to explain the failure before checking the answer.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight |
|---|---:|
| Author and manage workflows | 20–25% |
| Consume and troubleshoot workflows | 15–20% |
| Author and maintain actions | 15–20% |
| Manage GitHub Actions for the enterprise | 20–25% |
| Secure and optimize automation | 10–15% |

GH-200 tests both YAML authorship and enterprise operation. Learn what executes, when it executes, which identity it uses, what data crosses boundaries, and how reusable automation is governed.

---

# 1. Workflow execution model

A workflow is a YAML file under `.github/workflows`. An event triggers a workflow run. A workflow contains jobs; a job runs on one runner and contains steps. Jobs run in parallel unless connected with `needs`. Use the [workflow-syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) to distinguish structural rules from values that are available only at runtime.

| Object | Meaning |
|---|---|
| Event | Activity that can trigger a workflow |
| Workflow | Automated process defined in YAML |
| Job | Steps executed on one runner or container |
| Step | Shell command or action invocation |
| Action | Reusable step-level component |
| Runner | Machine executing a job |

## Triggers

```yaml
name: Terraform CI

on:
  pull_request:
    paths: ["**/*.tf", ".github/workflows/terraform.yml"]
  push:
    branches: [main]
  schedule:
    - cron: "23 7 * * 1"
  workflow_dispatch:
    inputs:
      environment:
        description: Target environment
        required: true
        type: choice
        options: [dev, qa, prod]
```

Know scheduled, manual, webhook, and repository events. Filters can narrow branches, tags, paths, and activity types. A workflow must exist on the appropriate ref for its trigger semantics. The [events reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) documents which commit and ref each event uses and whether the workflow must exist on the default branch.

**Security warning:** `pull_request_target` runs in the base-repository context and can receive powerful credentials. Never check out and execute untrusted fork code in that privileged context.

## Manual and reusable inputs

- `workflow_dispatch` exposes typed manual inputs.
- `workflow_call` makes a workflow reusable and defines inputs, secrets, and outputs.
- Inputs are not automatically secrets. Sensitive values belong in secret mappings.
- Validate values even when the UI offers a choice; API callers and later changes can violate assumptions.

```yaml
on:
  workflow_call:
    inputs:
      terraform_version:
        required: true
        type: string
    secrets:
      private_registry_token:
        required: false
```

---

# 2. Jobs, steps, expressions, and contexts

```yaml
jobs:
  validate:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v7
      - name: Validate
        id: validate
        env:
          TF_IN_AUTOMATION: "true"
        run: terraform validate

  report:
    needs: validate
    if: ${{ always() }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Result was ${{ needs.validate.result }}"
```

## Conditions and status functions

- `success()` is the normal default.
- `failure()` tests earlier failure.
- `cancelled()` detects cancellation.
- `always()` runs even after failure/cancellation, but use it carefully for steps that may hang or access missing data.
- `needs.<job>.result` exposes a dependency’s result.

## Contexts

Know these: `github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `strategy`, `job`, `steps`, and event-specific fields such as `github.event` and `github.ref`.

Contexts are not equally trusted. Branch names, issue titles, PR bodies, commit messages, and other event properties can contain attacker-controlled text. The [contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts) and [expressions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions) references are the authority for availability and evaluation behavior.

### Script-injection risk

Unsafe:

```yaml
- run: echo "${{ github.event.pull_request.title }}"
```

Safer:

```yaml
- shell: bash
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
  run: printf '%s\n' "$PR_TITLE"
```

Passing untrusted data through an environment variable prevents the expression engine from inserting it directly into generated shell source. Shell quoting and validation still matter.

## Static and runtime evaluation

Some workflow structure must be known when GitHub parses the workflow, while other values exist only on the runner. If a context is unavailable at a YAML key, it cannot be used there. Learn to read the documentation’s context-availability table rather than assuming every `${{ }}` works everywhere.

## Workflow commands and environment files

- Write environment variables for later steps to `$GITHUB_ENV`.
- Write step outputs to `$GITHUB_OUTPUT`.
- Write Markdown job summaries to `$GITHUB_STEP_SUMMARY`.
- Mask sensitive values with the appropriate workflow command, but do not rely on masking as permission control.

```bash
echo "plan_file=tfplan" >> "$GITHUB_OUTPUT"
echo "## Terraform validation passed" >> "$GITHUB_STEP_SUMMARY"
```

The environment files are interpreted by the runner after the step writes them. They do not retroactively change the writing step's environment. Follow the [workflow-command reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands) for multiline values, delimiters, and restricted variables.

## Authoring and validation tooling

The official [GitHub Actions extension for VS Code](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions) provides workflow syntax highlighting, schema validation, completion for actions and expressions, and navigation or monitoring features. Editor validation catches misspelled keys, invalid shapes, and some context mistakes before a push; it cannot prove repository permissions, secret availability, runner capacity, network reachability, or the safety of a referenced action.

Treat an editor warning and a successful YAML parse as early gates rather than execution proof. Review the expanded matrix, effective permissions, event trust boundary, and external action references separately.

---

# 3. Matrices, services, containers, and YAML reuse

## Matrix strategy

```yaml
strategy:
  fail-fast: false
  max-parallel: 3
  matrix:
    os: [ubuntu-latest, windows-latest]
    terraform: ["1.13", "1.14"]
    exclude:
      - os: windows-latest
        terraform: "1.13"
    include:
      - os: ubuntu-latest
        terraform: "1.15"
        experimental: true
```

- Matrix axes create job combinations.
- `include` adds or augments combinations.
- `exclude` removes combinations.
- `fail-fast` controls cancellation after one variant fails.
- `max-parallel` limits simultaneous matrix jobs.

Large matrices increase cost and queue pressure. Test combinations that represent real risk.

**VERIFY CURRENT:** Hosted runner labels and images change. Check runner-image release notes, especially for `*-latest` migrations and preinstalled tool versions.

## Service containers

`services:` starts supporting containers such as PostgreSQL or Redis for a job. Configure image, environment, ports, health checks, and options. On a containerized job, networking differs from a job running directly on the runner; learn how host ports and service names are addressed. Matrix and service-container keys are defined in the [workflow-syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax); runner and container behavior still has to be tested with the selected images.

## YAML anchors and aliases

Anchors (`&`), aliases (`*`), and merge keys (`<<`) can reduce repetition inside one YAML document. They do not create a centrally versioned reusable workflow and can make expanded configuration harder to troubleshoot. Expand the YAML mentally or with editor tooling when diagnosing the effective mapping.

---

# 4. Data between steps and jobs

| Mechanism | Scope and use |
|---|---|
| Environment variable | Current process/step, job, or declared workflow scope |
| Step output | Small named value consumed by later steps/jobs |
| Job output | Exposes a mapped step output to dependent jobs |
| Artifact | Files retained or transferred between jobs/runs |
| Cache | Restores reusable dependencies to improve speed |

Artifacts are outputs you want to retain, inspect, or transfer. Caches are an optimization and may be evicted. Never use a cache as authoritative deployment input without validation.

Retention is configurable at repository/organization level and for artifacts. The [organization retention setting](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization) establishes the allowed storage window, while individual upload steps may request a shorter artifact lifetime. REST endpoints can enumerate or delete [artifacts](https://docs.github.com/en/rest/actions/artifacts) and [workflow runs and logs](https://docs.github.com/en/rest/actions/workflow-runs); deleting history is an administrative action, not a performance shortcut.

## Environments

An environment such as `production` can provide:

- Environment-scoped secrets and variables
- Required reviewers
- Deployment branch/tag restrictions
- Protection rules and deployment history

A job must reference the environment for its controls and secrets to apply.

## Workflow visibility and status badges

A [workflow status badge](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge) reports the state of a selected workflow and can be narrowed by branch or event. It is a communication signal, not a branch-protection rule: a green badge does not prove that the displayed run is required for the current commit. Private-repository badges are not available to unauthenticated external viewers.

> **Related item:** Operational evidence has an audience and a retention requirement. Decide which logs, summaries, artifacts, attestations, deployments, and audit records must survive a run rather than retaining everything indefinitely.

---

# 5. Reuse models

| Mechanism | Behavior |
|---|---|
| Starter/workflow template | Copies a scaffold into a repository; copies drift independently |
| Reusable workflow | Calls a centrally versioned workflow containing jobs |
| Composite action | Reuses a sequence of steps within a job |
| JavaScript/Docker action | Packages executable action logic |

GitHub's [workflow templates](https://docs.github.com/en/actions/how-tos/write-workflows/use-workflow-templates) are selected and copied into the consuming repository. An organization can provide private templates through its designated `.github` repository, but the resulting workflow still belongs to each consumer and can drift. A reusable workflow remains referenced centrally at a ref and is evaluated as a called workflow.

## Reusable workflow

```yaml
jobs:
  terraform:
    uses: contoso/platform-workflows/.github/workflows/terraform-ci.yml@v2
    with:
      working_directory: environments/qa
    secrets: inherit
```

Use `secrets: inherit` only when the called workflow genuinely needs the caller’s available secrets. Explicit mappings better communicate least privilege.

## Disabling versus deleting

- Disabling stops new runs while retaining workflow history and the file.
- Deleting the file removes the definition from that branch but does not erase historical runs.

## Workflow troubleshooting

1. Confirm the expected event actually occurred.
2. Verify branch/path/activity filters.
3. Inspect YAML parsing and expression evaluation.
4. Expand matrix combinations and identify the failing axis.
5. Inspect job and step logs.
6. Check permissions, secret availability, environment approvals, and runner labels.
7. Inspect artifacts and job outputs.
8. Re-run only the failed job when appropriate.
9. Enable step/runner debug logging only when needed and protect sensitive output.

---

# 6. Authoring custom actions

Every custom action has metadata, normally `action.yml` or `action.yaml`, defining its name, inputs, outputs, and execution method. The [creating-actions documentation](https://docs.github.com/en/actions/sharing-automations/creating-actions) covers metadata, JavaScript, Docker, and composite implementations.

## Action types

| Type | Strength | Tradeoff |
|---|---|---|
| JavaScript | Fast startup; cross-platform when runtime supported | Requires bundled dependencies and runtime maintenance |
| Docker container | Controlled Linux environment | Slower startup; Linux/Docker constraints |
| Composite | Simple reuse of shell/action steps | Less flexible than a full JavaScript action |

Composite example:

```yaml
name: Terraform checks
description: Run formatting and validation
inputs:
  directory:
    required: true
    description: Terraform root directory
runs:
  using: composite
  steps:
    - shell: bash
      working-directory: ${{ inputs.directory }}
      run: terraform fmt -check -recursive
    - shell: bash
      working-directory: ${{ inputs.directory }}
      run: terraform init -backend=false && terraform validate
```

Version actions through releases and stable tags, document breaking changes, and test supported runners. Marketplace publishing requires appropriate metadata and repository visibility. Private actions can be shared according to enterprise/organization settings.

**Security:** Consumers should prefer immutable releases or full commit SHAs. Maintainers must protect release creation and tags.

## Immutable releases and consumer references

When a repository enables GitHub immutable releases, a release-specific tag and its assets become an unchangeable release boundary. GitHub's [immutable action release guidance](https://docs.github.com/en/actions/how-tos/create-and-publish-actions/using-immutable-releases-and-tags-to-manage-your-actions-releases) deliberately distinguishes that release tag from movable compatibility tags such as `v1`. A consumer pinned to a full commit SHA selects one Git object; a consumer using a movable tag accepts the maintainer's future tag updates.

**VERIFY CURRENT:** Immutable-release availability, enforcement behavior on hosted runners, and enterprise policy controls can change. Check both the current product documentation and the consuming organization's action policy rather than assuming every tag has become immutable.

---

# 7. Enterprise Actions administration

## Policy and distribution

The [enterprise Actions policy](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise) can control:

- Whether Actions is enabled
- Whether all, GitHub-authored, verified, or selected actions may run
- Which reusable workflows/actions are accessible
- Default workflow token permissions
- Fork-pull-request workflow behavior
- Artifact/log retention and usage

Policy inheritance matters: a lower scope cannot normally weaken a higher-scope enforced restriction.

## Runners and runner groups

| Runner | Advantages | Responsibilities/risks |
|---|---|---|
| GitHub-hosted | Ephemeral, maintained images, easy scaling | Product/network limits; image changes; metered usage |
| Larger hosted runner | More resources and enterprise networking options | Cost and policy management |
| Self-hosted | Custom hardware/software and internal access | Patching, isolation, capacity, credentials, cleanup, monitoring |

Runner groups control which organizations or repositories may target groups of runners. Labels describe capabilities; groups govern access. The [self-hosted runner access documentation](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access) shows how group visibility is scoped to repositories or organizations.

Do not run untrusted code on a persistent privileged self-hosted runner. Prefer ephemeral runners, network segmentation, minimal credentials, and workload isolation.

For Azure access, consider GitHub-hosted runner networking options, larger runners with private networking where available, or carefully isolated self-hosted runners. If an organization or enterprise uses a GitHub IP allow list, ordinary dynamically addressed hosted runners are not automatically suitable: current [IP allow-list guidance](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization) calls for self-hosted runners, larger runners with static ranges, or the documented private-networking pattern, with the relevant runner addresses allowed. **VERIFY CURRENT:** available Azure private-networking designs and plan requirements.

GitHub-hosted images are maintained dependencies. The [hosted-runner documentation](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners) explains that included software is updated regularly and that the exact image/tool list is linked from the run's **Set up job** log. Use `setup-*` actions, package managers, containers, or a controlled image to select critical tool versions rather than relying accidentally on `*-latest` contents.

## Secrets and variables

- Secrets and variables can exist at organization, repository, and environment scopes.
- Environment secrets become available only to jobs using that environment after protections are satisfied.
- Organization values can be limited to selected repositories.
- Repository secrets do not automatically cross into reusable workflows or forked PRs.
- APIs and CLI can manage values, but secret values cannot be read back after storage. The [Actions secrets REST API](https://docs.github.com/en/rest/actions/secrets) exposes public keys and encrypted-value update operations rather than returning stored plaintext.

Integrate a third-party vault by retrieving short-lived data at runtime with a securely authenticated action. Prefer identity federation over a stored vault credential.

---

# 8. Authentication and security

## `GITHUB_TOKEN`

GitHub creates an ephemeral token for each job. Its permissions derive from enterprise, organization, repository, workflow, and job configuration. The [secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use) treats token scope, untrusted input, action pinning, and runner trust as parts of one boundary. Declare minimal permissions:

```yaml
permissions:
  contents: read
  id-token: write
```

A PAT represents a user and may have broader/longer-lived access. A GitHub App token is installation-scoped and often better for service automation. Do not use a PAT when `GITHUB_TOKEN` or a GitHub App satisfies the requirement.

## OIDC for Azure

[OIDC federation for Azure](https://docs.github.com/en/actions/how-tos/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure) lets a job request a short-lived identity token and exchange it for Azure credentials through a federated identity credential. It removes the need to store an Azure client secret.

Required design elements:

- `id-token: write`
- A trust relationship restricted by repository, branch/tag, pull-request, or environment subject
- Minimal Azure RBAC on the target scope
- Protected production environment and reviewed workflow

OIDC is authentication, not authorization. Azure RBAC still determines what the identity can do.

## Third-party actions

- Review publisher, repository, release practices, and permissions.
- Pin to a full commit SHA for strong immutability.
- Use Dependabot/Renovate to propose controlled pin updates.
- Restrict allowed actions through policy.
- Treat an action as code executing inside the job with its credentials.

## Artifact attestations

[Artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations) bind provenance claims to an artifact, helping consumers verify how and where it was built. Understand the connection to SLSA/build provenance and verification before deployment. An attestation does not prove the application is vulnerability-free.

---

# 9. Performance and cost

- Cache immutable package dependencies with precise keys and safe restore keys.
- Avoid caching secrets, credentials, or untrusted executable output.
- Use path filters and concurrency groups to avoid obsolete runs.
- Limit matrix size and parallelism deliberately.
- Choose an appropriate runner size.
- Set artifact retention to business need.
- Reuse workflows instead of maintaining divergent copies.
- Inspect queue time, execution time, cache hit rate, and repeated setup work.
- Cancel superseded branch/PR runs when safe.

Optimization must preserve correctness and security. A faster pipeline that skips required checks is not an improvement.

---

# 10. Objective-by-objective workflow deep dive

## Read a workflow as a program and a security boundary

Use this sequence whenever you author or troubleshoot YAML:

```text
event payload
    ↓ filters and concurrency
workflow permissions and inputs
    ↓ job if / needs / matrix / environment
runner selection and job permissions
    ↓ ordered steps, actions, and shell code
outputs, artifacts, attestations, logs, and deployments
```

At each arrow ask what is already known, what remains untrusted, and which identity is active. Many difficult failures are boundary mistakes: a runtime value used where workflow structure is parsed, an output assumed to cross jobs automatically, a secret expected in a fork run, or a deployment credential exposed before approval.

> **Related item:** Workflow YAML is declarative orchestration wrapped around imperative programs. GitHub decides the graph and scheduling; actions and `run` steps execute code. Debug the orchestration layer separately from the program being invoked.

## Trigger and event design

### Choose the event from the desired guarantee

| Desired behavior | Candidate trigger | Design question |
|---|---|---|
| Validate a proposed change | `pull_request` | Is code from a fork untrusted, and which base-branch workflow definition applies? |
| Act after trusted code reaches a branch | `push` | Which branch/tag filters and path filters express the release boundary? |
| Provide an operator-run procedure | `workflow_dispatch` | Which typed inputs, permissions, and environment approvals constrain the operator? |
| Expose central automation to callers | `workflow_call` | Which inputs, secrets, outputs, and caller permissions form the contract? |
| Run periodic maintenance | `schedule` | Is the default-branch definition present, and is exact wall-clock execution required? |
| Continue after another workflow | `workflow_run` | Does crossing into a more privileged workflow introduce untrusted artifacts or code? |
| Integrate an external system | `repository_dispatch` or webhook-driven API | How is the sender authenticated and the payload validated? |

Path filters should reduce irrelevant work, not become the only security control. If a required workflow is skipped because its path filter does not match, make sure branch policy and expected-check behavior still produce the intended merge decision.

### Understand ref and definition questions

Before debugging a missing run, identify:

- the event name and activity type;
- the base and head refs involved;
- the branch on which GitHub searches for the workflow definition;
- whether branch, tag, or path filters all match;
- whether the workflow file is disabled or invalid;
- whether organization policy allows it;
- whether concurrency cancelled or replaced the run.

Do not begin with the job steps when no workflow run was created. The error is upstream of the runner.

### Concurrency is state management

A concurrency group can prevent overlapping work and optionally cancel an in-progress run. Choose a key that represents the protected resource, such as a pull request, branch, or target environment. Cancellation is safe for idempotent validation but can be dangerous during non-transactional deployment or teardown.

> **Related item:** Idempotency means rerunning an operation leads to the same desired state without harmful duplication. It makes manual reruns, retries, and concurrency cancellation much safer, especially for deployments and external API calls.

## Jobs, permissions, and evaluation timing

### Design the dependency graph explicitly

Jobs without `needs` can run in parallel. Add `needs` only for a real data or sequencing dependency. A fan-out/fan-in graph is common:

```text
              ┌─ lint ───────┐
prepare ──────┼─ unit-test ──┼─ package ─ deploy
              └─ scan ───────┘
```

If `package` needs all three checks, declare all three. If it only needs an artifact from `unit-test`, adding unrelated dependencies slows the critical path and changes failure behavior.

### Compute effective token permission

Think of permission as a narrowing process:

1. Enterprise or organization policy constrains the maximum.
2. Repository defaults establish a baseline.
3. Workflow-level `permissions` sets the workflow grant.
4. Job-level `permissions` can specialize the job.
5. Event and fork rules may further reduce what is available.

Declare permissions rather than relying on a broad default. A reporting job may need `checks: write`; the build job often needs only `contents: read`; an OIDC deployment job needs `id-token: write` plus only the repository permissions it uses.

### Know value precedence and availability

Variables can come from workflow YAML, configuration variables, environment declarations, matrix values, inputs, and the runner process. Do not treat similarly named values as interchangeable. Inspect the documented precedence and context availability for the exact key.

Expressions are evaluated by GitHub before a shell sees the generated command. Shell variables are expanded by the shell later. This distinction explains why quoting inside an expression is not the same defense as passing a value through `env` and quoting it in shell code.

> **Related item:** A workflow has two interpreters: GitHub's expression/template engine and the selected shell or action runtime. Injection can occur at either boundary, so validate data before it becomes source code, command arguments, paths, or action inputs.

## Matrices and services in production-quality tests

### Calculate the matrix before running it

For independent axes, begin with the Cartesian product. Two operating systems × three runtimes × two dependency versions creates 12 jobs before `include` and `exclude`. Then:

1. remove each excluded combination;
2. apply include entries that augment compatible combinations;
3. add include entries that cannot merge into an existing combination;
4. account for dynamically generated matrix JSON if used;
5. apply `max-parallel` to capacity, not to the total number of variants.

Use matrices for meaningful compatibility risk. Do not test every conceivable combination when representative boundaries or a smaller supported set provide the necessary confidence.

### Interpret matrix failures

The displayed job name should expose useful axes. A single operating-system failure suggests shell, path, line-ending, image, or tool differences. A single runtime failure suggests compatibility. Broad intermittent failure suggests shared service, rate limiting, resource pressure, or test instability. Rerun an individual matrix job only after deciding whether shared state could make that misleading.

### Service-container network model

When the job runs directly on a runner, published service ports are reached through the runner host. When the job itself runs in a container, service containers share a Docker network and can be addressed by service label; host port publishing is not used in the same way. Add a health check so test steps do not race service startup.

> **Related item:** A health check proves the dependency is ready to accept the intended operation, while a process merely being started proves much less. The same readiness-versus-liveness distinction appears in container platforms such as Kubernetes.

## Moving data safely

### Select the narrowest data mechanism

| Need | Mechanism | Important constraint |
|---|---|---|
| Value for later steps in one job | `$GITHUB_ENV` or step output | Environment files affect subsequent steps, not the step writing them |
| Small value for another job | Step output mapped to job output | Dependent job must use `needs`; avoid secrets in outputs |
| Files for another job or later inspection | Artifact | Validate provenance and retention; uploading does not make content trustworthy |
| Reusable dependencies | Cache | Cache hit is optional and content can be influenced by key/design |
| Human-readable run report | `$GITHUB_STEP_SUMMARY` | Treat inserted event data as untrusted Markdown/text |

Outputs should be small control values, not encoded file-transfer channels. Artifacts should have intentional names and retention. Caches should be rebuildable.

### Protect artifact handoffs

An artifact from an untrusted workflow remains untrusted when a later privileged workflow downloads it. Before execution or deployment, verify the producer, run conclusion, commit, expected files, digest, signature or attestation where appropriate, and the trust level of the triggering event. Never use a workflow boundary to launder untrusted code into a privileged context.

### Design cache keys

A robust dependency-cache key usually includes operating system, dependency manager, relevant runtime, and a hash of the lockfile. Restore keys can accept older related entries, but overly broad restore keys increase the chance of stale or inappropriate content. Do not cache generated credentials or privileged build output.

> **Related item:** Artifact integrity and artifact confidentiality are separate. A digest or attestation helps detect replacement and prove provenance; encryption and access control protect sensitive contents.

## Reuse contracts and versioning

### Decide where reuse belongs

Use a reusable workflow when the reusable unit owns jobs, permissions, runners, environments, or a multi-job process. Use a composite action when the caller should own the job but wants the same steps. Use JavaScript or Docker when the component needs richer logic, a stable runtime, or packaging beyond composite steps. Use a starter workflow when teams need a customizable starting point and central updates are not required.

### Treat reusable workflows like APIs

Define:

- typed, documented inputs with safe defaults;
- required and optional secret mappings;
- outputs with stable meaning;
- minimum caller permissions;
- supported runners and prerequisites;
- failure behavior and observability;
- a versioning and deprecation policy.

Callers cannot grant a called workflow more repository token permission than the caller has. Nesting makes permission and secret flow harder to see, so keep contracts explicit. Avoid `secrets: inherit` when a small named set is sufficient.

### Version for stability and patchability

A full commit SHA is immutable and strongest for consumers. A protected release tag is easier to read and can represent a compatibility line, but tags can be moved unless governance prevents it. A branch such as `main` receives fixes quickly but can break consumers without notice. Choose intentionally, publish changelogs, and automate reviewed updates.

> **Related item:** Central reuse reduces configuration drift but creates platform dependency. Define service ownership, availability expectations, rollback, and a way to test changes against representative callers before release.

## Custom-action engineering

### Metadata is the action's public interface

An action metadata file defines inputs, outputs, branding where applicable, and the `runs` implementation. Give inputs descriptions, avoid ambiguous defaults, and validate them in the implementation. Do not assume a required metadata field prevents malicious or semantically invalid values.

For JavaScript actions, commit the distributable bundle expected by the runtime so consumers do not need to install dependencies during each invocation. Keep source, generated distribution, and release process synchronized. For Docker actions, minimize the image, pin base dependencies appropriately, run with the least privilege practical, and understand Linux-only constraints. For composite actions, specify a shell for every `run` step and account for platform differences.

### Produce and consume outputs correctly

Write outputs through `$GITHUB_OUTPUT` and declare/document their meaning. Multiline values require the supported environment-file syntax and careful delimiter handling. Never print a secret merely to capture it as an output; outputs can flow into logs, expressions, and downstream jobs.

### Release an action safely

1. Test supported runners and representative failure cases.
2. Review dependencies and generated distribution.
3. Create an immutable release commit and version tag under protected release controls.
4. Publish documentation, permissions, inputs, outputs, and upgrade notes.
5. Update a major compatibility tag only through the approved release process if you choose to maintain one.
6. Monitor issues and security reports and provide a supported update path.

> **Related item:** An action is a software supply-chain dependency executing inside the consumer's trust boundary. Secure maintenance and release provenance matter as much as the YAML used to call it.

## Enterprise governance and runner operations

### Build an allowed-action policy

Start from business need and trust, not convenience. Decide whether to allow GitHub-authored actions, verified creators, selected actions, and internal actions. For exceptions, record owner, exact reference, requested permissions, review evidence, version/pin, expiration, and replacement plan.

An allow policy does not eliminate the need to pin and update dependencies. An allowed action can later have a vulnerability; an immutable pin can remain vulnerable until deliberately updated.

### Separate runner authorization from scheduling

Runner groups decide which repositories or organizations may use a runner pool. Labels describe the pool's capabilities and let jobs select it. Network reach and cloud identity decide what the running job can affect. All three boundaries must align.

For self-hosted runners, operate:

- image creation and patch cadence;
- ephemeral registration or workspace cleanup;
- autoscaling and capacity limits;
- egress and internal network policy;
- credential injection and removal;
- job, runner, and platform logs;
- quarantine and rebuild after suspicious execution;
- upgrades of the runner application itself.

### Diagnose queue and image failures

For a queued job, check group access, matching labels, runner status, concurrency, plan limits, and autoscaler health. For a job that suddenly fails on `*-latest`, compare runner image release notes and the actual image/tool versions in the log. Install critical tool versions explicitly rather than depending accidentally on a changing preinstalled version.

> **Related item:** Hosted images are versioned infrastructure dependencies. Recording tool versions in logs and using setup actions turns an implicit environmental dependency into an explicit, reviewable one.

## Security hardening and cloud federation

### Threat-model event data

Treat data from pull requests, issues, commits, branch names, workflow inputs, repository dispatch, artifacts, and external APIs according to its source. Keep untrusted strings out of generated shell source; pass them as data, quote them for the actual shell, validate expected format, and avoid using them to construct executable paths or commands.

Review `pull_request_target`, `workflow_run`, and other patterns that can cross from untrusted contribution to privileged context. The secure design often separates unprivileged build/test from a later privileged action that consumes only verified, non-executable evidence.

### Design an OIDC subject narrowly

Cloud federation should bind trust to the expected GitHub organization/repository and an appropriate subject such as a protected environment, branch, tag, or pull-request context. The workflow requests an OIDC token; the cloud validates issuer, audience, and subject/claims; cloud RBAC then authorizes resource actions.

For production:

1. make the deployment job reference a protected environment;
2. restrict who can modify the workflow and deployment configuration;
3. grant `id-token: write` only to the job that needs it;
4. limit cloud RBAC to the target scope and required operations;
5. record deployment and cloud audit evidence;
6. test that an untrusted ref cannot satisfy the federated credential.

### Understand attestations precisely

An artifact attestation records a signed provenance claim such as which workflow and repository produced an artifact. Verification can enforce that deployment input came from an approved build identity and source. It does not prove the source was correct, the dependencies were safe, or the artifact has no vulnerability. Combine provenance with review, scanning, policy, and environment protection.

> **Related item:** SLSA describes increasing supply-chain integrity guarantees. GitHub artifact attestations can support provenance requirements, while hermetic/reproducible builds, dependency controls, and protected builders address additional parts of the supply chain.

## Troubleshooting by failure phase

| Phase | Symptom | First checks |
|---|---|---|
| Trigger | No run exists | Event, workflow location, filters, disabled state, policy |
| Parse/plan | Workflow rejected or job omitted | YAML, expression availability, `if`, matrix expansion |
| Queue | Job never starts | Runner labels/groups, capacity, concurrency, approvals |
| Setup | Checkout/action/tool failure | Token permission, action pin, network, runner image |
| Execute | Command or test fails | Shell, working directory, environment, service health, logs |
| Handoff | Downstream job lacks data | `needs`, output mapping, artifact name/retention/download |
| Deploy | Credential or target denied | Environment approval, OIDC claims, RBAC, network |
| Post-run | Cleanup/upload fails | Cancellation behavior, missing paths, retention, permissions |

Avoid enabling verbose debug output before considering secret exposure. Reproduce with the smallest safe input, preserve the original failure evidence, and change one hypothesis at a time.

## Performance engineering with evidence

Break total lead time into queue, setup, dependency restore, build/test, artifact transfer, approval wait, and deployment. Optimize the largest relevant component:

- queue: capacity, runner groups, concurrency, matrix size;
- setup: prebuilt image or explicit setup with caching;
- dependencies: lockfile-keyed caches and nearby registries;
- test: safe parallelism, changed-scope selection, remove flaky retry masking;
- artifact: smaller outputs, appropriate compression and retention;
- approval: clear ownership and notification without bypassing governance.

Track cache hit rate, p50/p95 duration, queue time, failure/retry rate, cancellation rate, runner utilization, and cost per useful run. Averages alone hide slow tails.

> **Related item:** The critical path, not the sum of every parallel job duration, determines wall-clock workflow time. Speeding up a non-critical parallel job may save billed compute without improving developer feedback time.

## Knowledge checks

1. A scheduled workflow works on manual dispatch but never runs on schedule. Which workflow-location and default-branch conditions should you verify before debugging its steps?
2. A matrix defines three operating systems and four runtimes, excludes two combinations, and adds one new experimental combination. How many jobs are expected, and what could `max-parallel: 3` change?
3. A reusable workflow needs one deployment secret, but the caller uses `secrets: inherit`. How would you reduce the contract and why?
4. A privileged `workflow_run` downloads and executes a binary built from a fork PR. Why is the second workflow still exposed to the fork's input?
5. An OIDC token is issued successfully, but Azure denies a resource operation. Which layer succeeded, and which authorization layer should you inspect?
6. A job targets the correct runner label but remains queued. Which access and capacity controls are independent of the label?
7. A deployment artifact has a valid attestation. What security questions remain unanswered?
8. After changing the `ubuntu-latest` image, one tool disappears. What should be made explicit in the workflow?

---

# 11. Hands-on labs

## Lab 1: Terraform PR validation

Create a workflow that checks formatting, initializes without a backend, validates, uploads a short report, and writes a job summary. Make the check required through a ruleset.

## Lab 2: Reusable Terraform workflow

Move validation into a separate repository or reusable workflow. Define typed inputs, explicit secret mappings, and a workflow output. Call it from two sample repositories.

## Lab 3: Matrix and service container

Test two supported Terraform versions and OS images. Then create a small application test job using a database service with a health check. Explain every expanded job.

## Lab 4: Azure OIDC

In a disposable subscription, create a federated identity tied to a protected GitHub environment. Run an Azure read-only command, inspect token/RBAC boundaries, and remove the lab identity afterward.

## Lab 5: Injection and permissions

Create a harmless demonstration showing why direct expression interpolation into `run:` is unsafe. Refactor through an environment variable, reduce token permissions, and pin third-party actions.

## Lab 6: Runner governance design

Design runner groups for trusted platform workflows, application CI, and isolated production deployment. Specify allowed repositories, network access, cleanup, patching, and incident response.

---

# 12. Distinctions to know cold

| Contrast | Correct distinction |
|---|---|
| Workflow vs action | Workflow orchestrates jobs; action is reusable step logic |
| Reusable workflow vs composite action | Reuses jobs versus steps inside a job |
| Starter workflow vs reusable workflow | Copied scaffold versus centrally invoked definition |
| Artifact vs cache | Retained/transferred output versus performance optimization |
| Secret vs variable | Protected sensitive value versus ordinary configuration |
| Runner label vs runner group | Capability selection versus access governance |
| `GITHUB_TOKEN` vs PAT | Ephemeral job token versus user token |
| OIDC vs cloud RBAC | Authentication/federation versus authorization |
| `workflow_dispatch` vs `workflow_call` | Manual run versus reusable invocation |
| Disable vs delete | Stop runs while retaining file versus remove definition from branch |
| Environment approval vs PR approval | Deployment gate versus source-change review |
| Tag pin vs SHA pin | Convenient movable reference versus immutable object identity |

---

# 13. Readiness checklist

- [ ] I can choose and configure triggers, filters, inputs, and reusable calls.
- [ ] I can explain jobs, steps, `needs`, conditions, contexts, and expressions.
- [ ] I can expand a matrix with include/exclude, fail-fast, and max-parallel.
- [ ] I can use service containers, outputs, environment files, summaries, artifacts, and caches.
- [ ] I distinguish starter workflows, reusable workflows, composite actions, and custom actions.
- [ ] I can troubleshoot events, filters, matrices, permissions, runners, outputs, and artifacts.
- [ ] I can describe JavaScript, Docker, and composite action structure and distribution.
- [ ] I can govern allowed actions, token permissions, runners, runner groups, secrets, and variables.
- [ ] I can defend against script injection and dangerous fork workflows.
- [ ] I can explain `GITHUB_TOKEN`, GitHub App tokens, PATs, and Azure OIDC.
- [ ] I understand action pinning, attestations, environment protection, and least privilege.
- [ ] I can optimize matrix size, caching, concurrency, runners, and retention without weakening controls.

## Primary references

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts)
- [Expressions reference](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions)
- [Workflow commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands)
- [Reusable workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [Creating actions](https://docs.github.com/en/actions/sharing-automations/creating-actions)
- [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners)
- [Secure use](https://docs.github.com/en/actions/reference/security/secure-use)
- [OIDC in Azure](https://docs.github.com/en/actions/how-tos/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure)
- [Artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations)

Recheck hosted images, action versions, immutable-action behavior, networking options, pricing, and preview features immediately before the exam.

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Start with the official paths, then pick the explanations, formats, and practice that work for you and close specific blueprint gaps. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — GitHub Actions Part 1](https://learn.microsoft.com/en-us/training/paths/github-actions/) and [Part 2](https://learn.microsoft.com/en-us/training/paths/github-actions-2/) | Free | About 12–16 hours | Official starting point, with modules and exercises mapped to the credential |
| [Microsoft — GH-200 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/github-actions/practice/assessment?assessment-type=practice&assessmentId=1001&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; start here before buying another assessment |
| [Microsoft Learn GH-200 video course](https://www.youtube.com/playlist?list=PLahhVEj9XNTd5N_seZDoRXVIn6N1qAp-_) | Free | About 6–8 hours | Official instructor-led reinforcement for visual learners |
| GitHub Skills: [Test with Actions](https://github.com/skills/test-with-actions), [Reusable workflows](https://github.com/skills/reusable-workflows), and [Workflow artifacts](https://github.com/skills/workflow-artifacts) | Free account | About 2–4 hours | Real-repository practice with automated feedback |
| [Pluralsight — GitHub Actions](https://www.pluralsight.com/paths/github-actions) | Subscription | 7 hours | Five-course structured path; verify 2024 course behavior against the January 2026 baseline |
| [O'Reilly — Learning GitHub Actions](https://www.oreilly.com/library/view/learning-github-actions/9781098131067/) | Subscription | About 8–12 hours reading/practice | Durable workflow and automation depth; published in 2023, so it is not a current exam map by itself |
| [MeasureUp — GH-200 practice test](https://www.measureup.com/microsoft-gh-200-github-actions-practice-test.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 126 questions and explanations; the public page contains copied Copilot-oriented introduction text, so use the official Actions blueprint as the scope check |
| [O'Reilly — GitHub Actions interactive practice test](https://www.oreilly.com/products/certification-prep.html) | Subscription | About 2–4 hours for an attempt and review | O'Reilly's public certification-prep catalog lists a GitHub Actions practice test; exact launch details appear after sign-in |
| [John Savill — DevOps Master Class](https://www.youtube.com/playlist?list=PLlVtbbG169nFr8RzQ4GIxUEznpNR53ERq) and [companion repository](https://github.com/johnthebrit/DevOpsMC) | Free | About 2 hours for CI/CD plus artifact review | Strong supporting explanations and workflow examples; [Part 4: CI/CD](https://www.youtube.com/watch?v=nLRHV2sRTe8) demonstrates triggers, runners, actions, environments, approvals, and matrices. It is not an end-to-end GH-200 course, and the repository has no detected license, so link rather than republish its files. |

No instruction-first Whizlabs or Udemy course is listed yet. The MeasureUp assessment above is a gap-detection supplement, not explanatory instruction. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
