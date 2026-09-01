---
exam_code: TERRAFORM-ASSOCIATE-004
vendor_id: hashicorp
official_blueprint: https://developer.hashicorp.com/certifications/infrastructure-automation
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# HashiCorp Certified: Terraform Associate (004) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#terraform-associate-004-coverage-record). The [official HashiCorp certification page](https://developer.hashicorp.com/certifications/infrastructure-automation) is authoritative.

**Current baseline:** Terraform Associate (004), testing Terraform 1.12; verified August 31, 2026<br>
**Upcoming blueprint change:** No future update or retirement announcement was found on the official certification page as of August 31, 2026.<br>
**Official source:** [HashiCorp infrastructure automation certifications and Terraform Associate objectives](https://developer.hashicorp.com/certifications/infrastructure-automation)

HashiCorp presents the credential as **Terraform Associate (004)** rather than a short exam code. This library uses `TERRAFORM-ASSOCIATE-004` as a stable catalog identifier.

## How to use this guide

Choose the route that matches your current experience:

- **Orientation:** Read the objective map, the 004 changes, the distinction tables, and the readiness checklist.
- **Complete study:** Work through all eight domains and run each safe local lab.
- **Experienced Terraform user:** Use the [official content list](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004) as a checklist, then concentrate on Terraform 1.12 behavior, safe state changes, custom conditions, ephemeral/write-only data, and HCP Terraform.
- **Hands-on learner:** Build one small configuration, turn it into a module, refactor its resource addresses without replacement, and explain the resulting plans before using a course or assessment to find remaining gaps.

The certification targets foundational Terraform Community Edition and HCP Terraform knowledge. HashiCorp recommends production experience but says practice against the objectives in a personal demonstration environment may be sufficient. Provider-specific cloud knowledge is not required, although the official tutorials use AWS, Azure, Google Cloud, Docker, and other platforms for demonstrations.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

HashiCorp publishes eight numbered domains and detailed subobjectives but does **not** publish percentage weights. Do not infer emphasis from the number of bullets, this guide's length, or a training provider's practice-bank distribution.

| Published domain | Weight | Guide coverage |
|---|---:|---|
| 1. Infrastructure as Code (IaC) with Terraform | Not published | IaC model, advantages, multi-cloud and service-agnostic workflows |
| 2. Terraform fundamentals | Not published | Providers, versioning, lock file, multiple configurations, state purpose |
| 3. Core Terraform workflow | Not published | Write, initialize, format, validate, plan, apply, and destroy |
| 4. Terraform configuration | Not published | Resources, data, references, types, expressions, dependencies, validation, sensitive data |
| 5. Terraform modules | Not published | Sources, scope, composition, inputs/outputs, and versions |
| 6. Terraform state management | Not published | Local and remote state, locking, drift, moved and removed resources |
| 7. Maintain infrastructure with Terraform | Not published | Import, state inspection, and verbose logging |
| 8. HCP Terraform | Not published | Workspaces, projects, runs, collaboration, governance, and CLI integration |

## What changed in 004

The official page identifies four notable additions compared with 003 and states that 004 tests Terraform 1.12:

1. explicit dependencies and `create_before_destroy` lifecycle behavior;
2. custom conditions;
3. ephemeral values and write-only arguments; and
4. HCP Terraform workspace/project organization, with HCP Terraform content throughout the exam.

Treat an older 003 course as background rather than complete preparation. The command names may still be useful, but it can miss exactly the safety, secret-handling, and collaboration concepts that distinguish 004.

## 1. Infrastructure as Code with Terraform

### The operating model

Infrastructure as Code expresses intended infrastructure in versionable files rather than relying only on manual console actions. Terraform reads configuration, combines it with prior state and information returned by provider APIs, builds a dependency graph, proposes a plan, and asks the selected providers to perform approved operations. The configuration is the desired declaration; the provider translates Terraform operations into a target API's behavior. [HashiCorp's Terraform introduction](https://developer.hashicorp.com/terraform/intro) is the product-level starting point.

```text
configuration + input values
            + prior state
            + provider observations
                    ↓
             dependency graph
                    ↓
              execution plan
                    ↓
           provider API operations
                    ↓
              updated state
```

This model gives teams several advantages:

- code review and version history for infrastructure intent;
- repeatable creation of similar environments;
- a preview of proposed changes before execution;
- reusable modules and organizational policy;
- less configuration drift caused by undocumented manual steps;
- the same workflow across many providers and services.

Declarative does not mean risk-free or automatically idempotent under every external API. A provider must correctly model the remote system, credentials must permit the operations, and a plan can still include destructive replacement. Read the action symbols and replacement reasons instead of assuming “Terraform will make it safe.”

### Multi-cloud, hybrid, and service-agnostic workflows

Terraform's provider model lets one configuration interact with cloud platforms, SaaS systems, identity platforms, network devices, Kubernetes, and on-premises APIs. A shared language and workflow can reduce tool fragmentation, but provider resources remain platform-specific. A multi-provider configuration is not a universal lowest-common-denominator abstraction and does not make separate APIs one atomic transaction.

> **Related item:** A common workflow and a portable architecture are different claims. Terraform can manage AWS and Azure from one workflow while the resources, failure semantics, identity models, and operating procedures remain provider-specific.

### Practical decision

Use Terraform when the target has a suitable provider or API integration, the infrastructure lifecycle benefits from repeatable plans, and the team can protect state and review changes. A one-time manual action may be simpler for an object that cannot be modeled reliably, but document ownership so Terraform does not later compete with another control plane.

## 2. Terraform fundamentals

### Terraform CLI, providers, and provider configurations

Keep three layers separate:

| Layer | Responsibility | Typical version control |
|---|---|---|
| Terraform CLI | Loads configuration, constructs graphs and plans, coordinates operations, and manages state | Pin with `required_version` and the team's installation process |
| Provider plugin | Implements resource/data-source schemas and calls a target API | Declare source and constraints; commit the dependency lock file |
| Provider configuration | Supplies region, endpoint, aliases, and authentication behavior | Commit nonsensitive settings; inject credentials securely |

The `required_providers` block declares a provider's source address and acceptable versions. A `provider` block configures an installed provider. An alias creates an additional configuration of the same provider; a resource selects it with the `provider` meta-argument.

```hcl
terraform {
  required_version = "~> 1.12.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "secondary"
  region = "us-west-2"
}

data "aws_caller_identity" "secondary" {
  provider = aws.secondary
}
```

The example illustrates syntax; it does not assert that AWS knowledge is required for the certification. Review [provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements) for source addresses, local names, and constraints.

### Version constraints and the dependency lock file

A constraint says which versions are acceptable. `.terraform.lock.hcl` records the provider selection and checksums Terraform chose during initialization. Commit the lock file so collaborators and automation start from the reviewed provider selections. `terraform init -upgrade` deliberately considers newer versions that still satisfy the constraints; a normal `init` generally honors the locked selection.

The dependency lock file tracks provider selections, not Terraform CLI versions and not remote module selections. Pin those through their own mechanisms. HashiCorp documents the exact behavior in the [dependency lock file reference](https://developer.hashicorp.com/terraform/language/files/dependency-lock).

> **Related item:** A loose constraint plus a committed lock file supports deliberate upgrades. A tight exact constraint can prevent accidental change but also makes routine security and compatibility updates harder. The team needs both a selection policy and an upgrade process.

### Why state exists

Terraform state binds resource addresses such as `aws_instance.web["blue"]` to remote object identities, retains metadata, and caches attributes needed for planning. It is neither the configuration nor merely a disposable command cache. Losing state can make Terraform unable to associate code with existing objects; exposing state can disclose sensitive values. The [state documentation](https://developer.hashicorp.com/terraform/language/state) describes this mapping and recommends protected remote storage for collaboration.

## 3. Core Terraform workflow

The [core workflow](https://developer.hashicorp.com/terraform/intro/core-workflow) is often summarized as **write → plan → apply**, with initialization, formatting, validation, review, and cleanup around it.

| Command | Primary job | What it does not prove |
|---|---|---|
| `terraform init` | Initializes the working directory; installs providers/modules and configures the backend | That credentials work for every planned API action |
| `terraform fmt` | Rewrites supported files to canonical style | That configuration is valid or safe |
| `terraform validate` | Checks syntax and internal configuration consistency | That remote objects exist, permissions are sufficient, or a plan has no replacement |
| `terraform plan` | Refreshes relevant observations and proposes actions | That the same plan will exist after the world changes |
| `terraform apply` | Applies an approved saved plan or creates and applies a new plan | That every external API operation is transactional with every other operation |
| `terraform destroy` | Plans and applies removal of managed objects | That deleting those objects is harmless or recoverable |

### Initialization

Run `terraform init` after cloning a configuration, changing provider/module requirements, or changing backend settings. Initialization is designed to be safe to repeat. Backend changes can require migration or reconfiguration choices; read the prompt and protect the original state before moving it.

### Plan review

A useful plan review asks:

- Which objects will be added, changed, replaced, imported, forgotten, or destroyed?
- Is replacement caused by an immutable argument, a resource-address change, or a lifecycle rule?
- Which values are unknown until apply?
- Are provider aliases and module instances the ones intended?
- Is the state/backend the correct environment?
- Did a refresh reveal drift?

Saving a plan and then applying that file connects approval to a particular proposal. Applying without a saved plan creates a new plan at apply time. Saved plan files can contain sensitive data; protect and dispose of them like state artifacts.

### Apply and destroy

Terraform walks the dependency graph and can perform independent operations concurrently. A failure can leave some operations complete and others incomplete; inspect the error and create a new plan rather than assuming an automatic rollback. `destroy` is a normal planning mode whose desired result is removal of all managed objects in that configuration. Lifecycle rules or provider constraints can block deletion.

> **Related item:** A plan is change-control evidence, not a backup. Back up state and critical data using controls appropriate to their systems before risky changes.

## 4. Terraform configuration

### Resources, data sources, and references

A `resource` block declares an object Terraform should manage. A `data` block reads information without taking ownership of that object's lifecycle. Both expose attributes that expressions can reference. [Resource blocks](https://developer.hashicorp.com/terraform/language/resources) and [data sources](https://developer.hashicorp.com/terraform/language/data-sources) can look similar, so ask whether Terraform owns the create/update/delete lifecycle.

```hcl
data "aws_ami" "base" {
  most_recent = true
  owners      = ["self"]
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.base.id
  instance_type = var.instance_type
}

output "instance_id" {
  value = aws_instance.web.id
}
```

The reference from the resource to the data source creates an implicit graph edge. Prefer implicit dependencies derived from actual data flow. Use `depends_on` when a hidden behavioral dependency exists and no expression captures it; overuse makes plans more conservative and can create unnecessary unknown values.

### Inputs, locals, and outputs

- Input variables form a module's configurable interface.
- Local values name reusable expressions inside a module.
- Outputs expose selected root-module results to users or child-module results to callers.

Declare precise types and validation where they make invalid calls fail early. Review [input variables](https://developer.hashicorp.com/terraform/language/values/variables), [output values](https://developer.hashicorp.com/terraform/language/values/outputs), and [type constraints](https://developer.hashicorp.com/terraform/language/expressions/type-constraints).

| Structural type | Main characteristic | Common decision |
|---|---|---|
| `list(T)` | Ordered sequence of one element type | Position/order is meaningful |
| `set(T)` | Unique, unordered collection of one element type | Identity matters more than order |
| `map(T)` | String keys with one value type | Stable named values |
| `tuple([...])` | Fixed positions with independently declared types | Exact heterogeneous structure |
| `object({...})` | Named attributes with declared types | Clear module interface for a structured value |

### Expressions, functions, and repeated resources

Expressions combine references, conditionals, `for` expressions, splats, and [built-in functions](https://developer.hashicorp.com/terraform/language/functions). A `dynamic` block generates repeated nested blocks; it does not generate top-level resources. `count` addresses instances by numeric index, while `for_each` addresses them by stable keys. Inserting an item into a count-based list can shift addresses; a keyed map can preserve identity more naturally.

```hcl
variable "services" {
  type = map(object({
    port    = number
    enabled = bool
  }))
}

locals {
  enabled_services = {
    for name, service in var.services : name => service
    if service.enabled
  }
}

resource "example_service" "this" {
  for_each = local.enabled_services
  name     = each.key
  port     = each.value.port
}
```

### Lifecycle and custom conditions

Lifecycle behavior affects graph construction and replacement decisions. `create_before_destroy` can reduce downtime when the remote system permits two objects to coexist; it cannot override uniqueness, quota, cost, or provider/API constraints. `prevent_destroy` blocks a plan from destroying a protected resource while the rule remains in configuration, but it is not a backup and does not protect an object deleted outside Terraform. See the [lifecycle reference](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle).

Terraform offers several condition locations:

| Condition | Intent | Failure behavior in the usual case |
|---|---|---|
| Variable `validation` | Reject invalid module input | Blocks planning |
| `precondition` | Assert an assumption before acting on an object/output | Blocks the associated operation |
| `postcondition` | Assert a guarantee after evaluating an object | Stops downstream work that depends on the failed result; does not roll back completed operations |
| `check` block | Observe infrastructure health outside normal lifecycle ownership | Reports a warning and continues the operation |

Evaluation can be deferred when values are unknown until apply. Use the [custom-condition guide](https://developer.hashicorp.com/terraform/language/validate) to understand timing instead of memorizing only syntax.

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "environment must be dev, test, or prod."
  }
}
```

### Sensitive, ephemeral, and write-only data

Marking a variable or output `sensitive` redacts it from normal CLI/UI display. It does **not** by itself prevent the value from being stored in state or a saved plan. Protect backend access, encryption, logs, plan artifacts, and state backups.

Ephemeral values are available during an operation without being persisted to state or plan artifacts in the normal way. Write-only resource arguments let a supporting provider receive a value and then discard it rather than returning it to Terraform for storage. They require compatible Terraform/provider/resource support; a conventional argument does not become write-only merely because its value was marked sensitive. Review [write-only argument behavior and requirements](https://developer.hashicorp.com/terraform/language/manage-sensitive-data/write-only).

Vault can issue or broker secrets, but sending a secret into a normal resource argument can still cause the provider to return and persist it in state. Trace the entire data path.

> **Related item:** Secret redaction, secret persistence, secret transport, and credential lifetime are four different controls. A secure design addresses each rather than treating `sensitive = true` as encryption.

## 5. Terraform modules

Every configuration has a root module. A `module` block calls a child module, giving it input values and consuming its outputs. A child module has its own variable and local scope; it does not automatically inherit arbitrary variables from its caller.

Terraform can source modules from local paths, registries, version-control repositories, object storage, and other supported locations. The `version` argument applies to registry modules; pin a VCS module with an appropriate source revision instead. After changing source or version requirements, rerun `terraform init`. The [modules overview](https://developer.hashicorp.com/terraform/language/modules) explains sources and workflow.

```hcl
module "network" {
  source  = "app.terraform.io/example/network/cloud"
  version = "~> 2.3"

  name       = "payments-prod"
  cidr_block = "10.24.0.0/16"
}

output "network_id" {
  value = module.network.id
}
```

Good modules expose meaningful decisions, keep their interfaces typed and documented, and compose with other modules through inputs and outputs. Deeply nesting modules can hide ownership and make changes hard to reason about. A root module commonly composes relatively small child modules and owns environment-specific wiring.

| Source | Version control approach | Important caveat |
|---|---|---|
| Local path | Repository commit | Caller and module change together |
| Public/private registry | `version` constraint | Choose and review an intentional release |
| Git/VCS | `ref` in source URL | Pin a tag or commit rather than an unstable branch for reproducibility |
| HCP private registry | Registry version and organizational access | Availability depends on identity, permissions, and service configuration |

> **Related item:** Module reuse creates a supply-chain boundary. Review the publisher, source, version, license, provider constraints, resource ownership, and upgrade notes before treating a registry module as trusted code.

## 6. Terraform state management

### Local and remote state

The default local backend stores state in `terraform.tfstate` in the working directory. That is convenient for a disposable individual exercise but weak for a team: people can work from different copies, local files can be lost, and state can contain secrets. A remote backend centralizes storage and may provide locking, encryption, access controls, and versioning depending on the backend.

Backend configuration tells Terraform where state lives. Provider configuration tells Terraform how to manage remote infrastructure. They are separate even when both use the same cloud platform.

### Locking and concurrency

When the backend supports it, Terraform automatically locks state for operations that can write it. Not every backend supports locking. A failed lock protects against concurrent writers; disabling locking or force-unlocking without confirming ownership can corrupt coordination. HashiCorp warns that [`force-unlock` should be used only for your own abandoned lock](https://developer.hashicorp.com/terraform/language/state/locking).

### Drift, refresh-only, and address changes

Drift means the observed remote object differs from the most recent state, often because another actor changed or deleted it. A normal plan refreshes relevant observations and then proposes changes to make remote objects match configuration. A refresh-only plan proposes updating state and outputs to match remote objects without changing those objects. Accepting remote drift into state does not update configuration; a later normal plan can still propose restoring the declared configuration.

Distinguish three cases:

| Situation | Typical safe mechanism | Main risk to inspect |
|---|---|---|
| Remote object changed outside Terraform | Normal or refresh-only plan, chosen by desired authority | Accidentally accepting or overwriting legitimate drift |
| Resource renamed/moved in configuration | `moved` block | Replacement if old and new addresses are not associated |
| Terraform should stop managing an object | `removed` block with appropriate lifecycle behavior | Destroying the object instead of forgetting it |

Configuration-driven `moved`, `removed`, and `import` blocks make lifecycle intent reviewable in version control. Direct `terraform state` mutation remains useful for inspection and exceptional repair but has a narrower audit trail and greater operator risk. Review the [state-refactoring guidance](https://developer.hashicorp.com/terraform/language/state/refactor).

> **Related item:** CLI workspaces select separate state instances for one configuration. HCP Terraform workspaces are managed collaboration/run boundaries with configuration, state, variables, permissions, and run history. The shared word “workspace” does not make the two concepts interchangeable.

## 7. Maintain infrastructure with Terraform

### Import existing objects

Import binds an existing remote object to a Terraform resource address. It does not automatically prove that the written configuration represents every important remote setting. After import, inspect state and create a plan; unintended updates or replacement reveal a configuration mismatch.

A configuration-driven import makes the intent reviewable:

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "example-existing-logs"
}

import {
  to = aws_s3_bucket.logs
  id = "example-existing-logs"
}
```

Each remote object should map to one resource instance. Use the provider's resource-specific import identifier and instructions. The [single-resource import workflow](https://developer.hashicorp.com/terraform/language/import/single-resource) emphasizes defining the destination resource, planning, and reviewing post-import changes.

### Inspecting state

Useful read-oriented commands include:

- `terraform state list` to enumerate resource addresses;
- `terraform state show ADDRESS` to inspect one managed instance;
- `terraform show` to inspect a state or plan representation;
- `terraform output` to read declared root outputs.

Commands such as `state mv`, `state rm`, `state push`, and `force-unlock` can change critical mappings or coordination state. Back up, verify the selected backend/workspace, understand dependencies, and prefer configuration-driven mechanisms where supported.

### Verbose logging

`TF_LOG` enables Terraform logging levels such as `TRACE`, while `TF_LOG_PATH` writes logs to a file only when logging is enabled. Provider-specific logging controls can further narrow output. Disable logging after diagnosis and protect the resulting files: debug logs can expose credentials, request/response data, paths, and infrastructure details. See the [Terraform CLI environment-variable reference](https://developer.hashicorp.com/terraform/cli/config/environment-variables).

> **Related item:** Troubleshooting evidence has its own data lifecycle. Collect the minimum useful verbosity, restrict access, redact before sharing, and delete logs according to the incident or support process.

## 8. HCP Terraform

HCP Terraform adds a managed collaboration and execution control plane around Terraform. A workspace contains configuration linkage, state, variables, run history, and settings for a distinct managed collection of infrastructure. A project groups workspaces and can provide a broader boundary for permissions, variable sets, and policy scope. Review [HCP Terraform workspaces](https://developer.hashicorp.com/terraform/cloud-docs/workspaces) and the [projects tutorial](https://developer.hashicorp.com/terraform/tutorials/cloud/projects).

```text
organization
   └── project
       ├── workspace: network-prod
       │      ├── configuration/version-control link
       │      ├── variables and credentials
       │      ├── state
       │      └── runs, plans, applies, and health
       └── workspace: application-prod
```

### Execution and integration workflows

- **CLI-driven:** The user runs Terraform locally while HCP Terraform stores state and can execute operations remotely according to configuration.
- **VCS-driven:** Changes to a connected repository/branch initiate speculative or normal runs under workspace settings.
- **API-driven:** Automation uploads configuration or creates runs through the service API.

`terraform login` obtains a CLI token for a hostname, and a `cloud` block connects configuration to an HCP Terraform organization/workspace. Migrating state changes an important control boundary; confirm the destination, access, lineage, and recovery path before accepting migration prompts.

### Collaboration and governance features

| Feature | Main question it answers |
|---|---|
| Teams and permissions | Who may view, plan, apply, administer, or govern? |
| Projects | How are related workspaces grouped for ownership and policy? |
| Variable sets | Which values should be shared across selected workspaces/projects? |
| Private registry | How are approved modules/providers discovered and versioned internally? |
| Run triggers | Which downstream workspace should queue a run after another completes? |
| Health assessments and drift detection | Does managed infrastructure still satisfy configuration/checks between normal runs? |
| Policy enforcement | Which Sentinel or OPA rules evaluate a proposed change before apply? |
| Explorer and change requests | How can teams view estate-level metadata and coordinate proposed changes? |

Policy sets can apply to an organization, selected projects/workspaces, or tags according to current service capabilities. A policy evaluation is separate from Terraform language validation: it applies organizational rules to run data. Review the current [policy-set documentation](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/policy-enforcement/manage-policy-sets/configure).

[Dynamic provider credentials](https://developer.hashicorp.com/terraform/cloud-docs/dynamic-provider-credentials) use workload identity federation to issue temporary credentials for runs instead of storing long-lived cloud keys. The cloud trust relationship and scoped role remain security-critical; temporary does not mean unrestricted.

**VERIFY CURRENT:** HCP Terraform editions, entitlements, limits, UI labels, policy features, Explorer/change-request availability, and Terraform Enterprise parity change independently. Verify a feature against current documentation and the organization's plan before designing a control around it.

> **Related item:** Remote execution moves trust rather than removing it. The execution agent or managed runner needs controlled network reachability, provider credentials, state access, policy inputs, and protected logs.

## Hands-on labs

Use disposable local files and accounts. Never run a lab against an employer, customer, shared subscription, or production environment without authorization. Review every plan and finish with cleanup.

### Lab 1: Build a provider-free Terraform 1.12 workflow

Create `main.tf`:

```hcl
terraform {
  required_version = "~> 1.12.0"
}

variable "environment" {
  type    = string
  default = "dev"

  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "environment must be dev, test, or prod."
  }
}

resource "terraform_data" "study" {
  input = {
    environment = var.environment
    purpose     = "terraform-associate-004"
  }

  lifecycle {
    precondition {
      condition     = var.environment != "prod"
      error_message = "This disposable lab must not target prod."
    }
  }
}

output "study_record" {
  value = terraform_data.study.output
}
```

Run `terraform init`, `terraform fmt -check`, `terraform validate`, `terraform plan -out=study.tfplan`, `terraform show study.tfplan`, `terraform apply study.tfplan`, `terraform state list`, and `terraform output`. Change the input to `prod` and explain where the precondition fails. Return to `dev`, then run and review `terraform plan -destroy` before cleanup.

### Lab 2: Observe provider selection and locking without a cloud account

Add the `hashicorp/random` provider with a conservative version constraint and a `random_pet` resource. Initialize, inspect `.terraform.lock.hcl`, and record the selected version and checksums. Run `terraform init` again and explain why the selection remains stable. In a disposable branch, use `terraform init -upgrade`, inspect the diff, and explain the difference between the constraint and the lock selection. Do not commit `.terraform/`; do commit the lock file in a normal root-module repository.

### Lab 3: Turn the configuration into a child module

Move the `terraform_data` resource into `modules/study-record`. Give the module typed `environment` and `purpose` variables and one output. Call it from the root module. Draw the value flow from root variable → module input → resource input → child output → root output. Confirm that a child module cannot read an undeclared root variable.

### Lab 4: Refactor an address without replacing the object

Rename a local `terraform_data.study` resource to `terraform_data.record`. First run a plan without a `moved` block and observe the proposed destroy/create behavior; do not apply it. Add:

```hcl
moved {
  from = terraform_data.study
  to   = terraform_data.record
}
```

Plan again and explain how configuration records the address migration. Inspect state before and after apply. Keep the `moved` block long enough for every consumer of a reusable module to traverse the upgrade path.

### Lab 5: Distinguish drift, forgetting, and deletion

Using the disposable resources from earlier labs, write a prediction table for these actions before executing any:

1. change configuration and run a normal plan;
2. change the remote/local artifact outside Terraform and run a refresh-only plan;
3. add a `removed` block with `destroy = false`;
4. remove the resource block without a `removed` block;
5. run `terraform state rm`.

For each, state whether configuration, state, and the real object change. Verify only operations supported safely by the chosen disposable resource. The goal is the control-plane distinction, not command memorization.

### Lab 6: Design an HCP Terraform workspace boundary

On paper or in a permitted free HCP Terraform organization, design projects and workspaces for shared networking plus two applications across test and production. Identify:

- state ownership and naming;
- project/workspace permissions;
- VCS or CLI-driven run workflow;
- variable-set scope;
- dynamic credential trust and least-privilege roles;
- run triggers or published outputs between workspaces;
- policy and health checks;
- break-glass, audit, and recovery evidence.

If you use the live service, **VERIFY CURRENT** plan availability and destroy all disposable infrastructure. Do not place real credentials in Terraform variables merely to complete the exercise.

## Knowledge checks

1. Why can Terraform support one workflow across multiple clouds without making resource definitions portable between them?
2. What is the difference between `required_providers` and a `provider` block?
3. Which component does `.terraform.lock.hcl` lock, and which common dependencies does it not lock?
4. Why can `terraform validate` succeed while `terraform plan` fails?
5. What changes when `terraform apply` receives a saved plan file rather than generating a new plan?
6. Why can an apply failure leave infrastructure partially changed?
7. When is a data source preferable to a resource?
8. What graph edge is created by `subnet_id = aws_subnet.app.id`, and when might `depends_on` still be needed?
9. Why can `for_each` preserve instance identity better than `count` for a named collection?
10. Contrast variable validation, preconditions, postconditions, and check blocks.
11. Why does `sensitive = true` not guarantee that a secret is absent from state?
12. What additional support is required before a value can use a write-only resource argument?
13. How do a module's source and versioning approach differ between a registry and a Git repository?
14. Why is a remote backend not automatically safe for concurrent writers?
15. A server changed outside Terraform. How do normal and refresh-only plans express different intentions?
16. What is the difference between a `moved` block and a `removed` block?
17. Why must import be followed by a plan and configuration review?
18. How do an HCP Terraform workspace and project differ, and how is an HCP workspace different from a CLI workspace?
19. What security problem do dynamic provider credentials reduce, and what trust configuration do they introduce?
20. Why should verbose Terraform logs be handled like sensitive troubleshooting evidence?

## High-value distinctions

| Contrast | Remember |
|---|---|
| Declarative vs imperative | Desired end state and dependency reasoning vs prescribed command sequence |
| Terraform CLI vs provider | Workflow/graph/state coordinator vs target-API plugin |
| Provider requirement vs provider configuration | Source/version contract vs endpoint/alias/authentication settings |
| Constraint vs lock selection | Allowed version range vs chosen provider version and checksums |
| Configuration vs state | Declared intent vs address-to-object bindings and observed attributes |
| Resource vs data source | Manage lifecycle vs read external information |
| Implicit vs explicit dependency | Reference-derived graph edge vs manually declared hidden relationship |
| `count` vs `for_each` | Numeric index identity vs key identity |
| Sensitive vs ephemeral/write-only | Display redaction vs avoiding persistence through supported data paths |
| Variable validation vs check | Invalid input blocks progress vs nonblocking operational assertion |
| Root vs child module | Environment composition/caller vs reusable encapsulated component |
| Local vs remote backend | Local state file vs centralized state service/storage |
| Locking vs versioning | Prevent concurrent writes vs recover previous stored state |
| Drift vs configuration change | Remote differs from recorded state vs desired declaration changed |
| `moved` vs `removed` | Preserve management under a new address vs stop management |
| Import vs create | Bind an existing object vs ask provider to create one |
| HCP workspace vs project | State/run boundary vs group and governance boundary |
| CLI workspace vs HCP workspace | Alternate state instance vs managed collaboration/execution unit |
| Policy vs Terraform condition | Organization-level run governance vs configuration-level assertion |

## Readiness checklist

- [ ] I can explain the Terraform configuration, state, provider, graph, plan, apply loop.
- [ ] I can distinguish Terraform CLI versions, provider constraints, provider locks, and module versions.
- [ ] I can configure and select multiple provider configurations.
- [ ] I can run and explain `init`, `fmt`, `validate`, `plan`, `apply`, and `destroy` safely.
- [ ] I can read plan actions, replacements, unknown values, and saved-plan implications.
- [ ] I can use resources, data sources, references, variables, outputs, complex types, expressions, and functions.
- [ ] I can choose between implicit dependencies and `depends_on` and explain lifecycle tradeoffs.
- [ ] I can distinguish variable validation, preconditions, postconditions, and checks.
- [ ] I can explain sensitive, ephemeral, write-only, Vault, state, plan, and log boundaries.
- [ ] I can source, version, call, and compose modules and explain their scope.
- [ ] I can explain local/remote state, backend locking, drift, refresh-only mode, moved blocks, and removed blocks.
- [ ] I can import an existing object, inspect state, and validate the subsequent plan.
- [ ] I can enable diagnostic logging and protect or remove the resulting evidence.
- [ ] I can explain HCP Terraform organizations, projects, workspaces, runs, variable sets, teams, policies, health, and dynamic credentials.
- [ ] I completed practical work rather than relying only on recognition or memorized command names.
- [ ] I checked every **VERIFY CURRENT** item and the current official blueprint.

## Primary references

- [Official Terraform Associate (004) certification and objectives](https://developer.hashicorp.com/certifications/infrastructure-automation)
- [Official objective-to-documentation content list](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004)
- [Terraform product introduction](https://developer.hashicorp.com/terraform/intro)
- [Terraform core workflow](https://developer.hashicorp.com/terraform/intro/core-workflow)
- [Terraform state](https://developer.hashicorp.com/terraform/language/state)
- [Terraform modules](https://developer.hashicorp.com/terraform/language/modules)
- [HCP Terraform workspaces](https://developer.hashicorp.com/terraform/cloud-docs/workspaces)

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the official material, instructor, format, labs, and assessment that fit your gaps. Times are approximate consumption time at normal speed; labs, pausing, note-taking, troubleshooting, review, and prerequisite work add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [HashiCorp Terraform Associate 004 learning path](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-study-004) | Free; some HCP exercises require a free account and cloud-provider tutorials may require a sandbox | About 18–30 hours (library estimate from the listed reading and tutorials; HashiCorp does not publish one combined runtime) | Authoritative ordered preparation across all eight domains; choose one provider for basic tutorials because provider-specific knowledge is not required |
| [HashiCorp 004 content list](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004) | Free | About 2–4 hours for one active objective/documentation pass | Best scope checklist and targeted remediation map; the page's displayed five-minute read time does not include following its documentation and tutorial links |
| [HashiCorp 004 sample questions](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-questions-004) | Free | About 30–60 minutes including documentation-backed review | Official format orientation for true/false, multiple-choice, and multiple-answer items; too small to be a complete readiness measure |
| [HashiCorp — Introduction to Terraform](https://www.youtube.com/watch?v=ZFLWA1kQ3ls) | Free | About 22 minutes | First-party visual orientation to IaC, Terraform, providers, registry, and HCP Terraform; not an objective-complete certification course |
| [Pluralsight — HashiCorp Terraform Associate (004)](https://www.pluralsight.com/paths/hashicorp-terraform-associate-004) | Subscription; practice-exam access depends on plan/library | 7 hours of video plus about 2–4 hours for the advertised practice exam and review | Current six-course Ned Bellavance path published March–June 2026 and explicitly aligned to Terraform 1.12 |
| [O'Reilly/Pearson — HashiCorp Certified Terraform Associate (004)](https://www.oreilly.com/videos/hashicorp-certified-terraform/9780135909560/) | Subscription | 22 hours 37 minutes plus lab and assessment review | Detailed Dave Prowse path with labs and quizzes; longer than necessary for an experienced practitioner, so select weak domains rather than automatically watching everything |
| [O'Reilly/Packt — Terraform Associate (004) Exam Prep Complete Hands-On Guide](https://www.oreilly.com/videos/terraform-associate-004/9781807781156/) | Subscription | 10 hours 8 minutes plus hands-on repetition | More compact 2026 video alternative; compare demonstrations and HCP terminology with the official content list |
| [KodeKloud — HashiCorp Certified Terraform Associate 004](https://kodekloud.com/courses/hashicorp-certified-terraform-associate-004) | Subscription; some preview/free enrollment controls may vary | 16 hours 40 minutes of video plus labs, quizzes, and practice review | Lab-first Bryan Krausen course with 126 lessons and an advertised practice test; useful when a managed sandbox matters |
| [Udemy — Terraform Associate 004 by Bryan Krausen](https://www.udemy.com/course/hashicorp-certified-terraform-associate-004/) | Purchase or subscription; lab-cloud access has separate plan requirements | About 15–25 hours (library estimate from the eight-domain curriculum, labs, quizzes, and two practice exams; public page does not expose a reliable runtime) | Updated August 2026 and explicitly mapped to 004; confirm what cloud-lab access is included in the selected purchase or subscription |

Use assessments to locate gaps, then verify explanations against HashiCorp documentation. The library did not find a separately verifiable current MeasureUp or exact Whizlabs Terraform Associate 004 product page during this review, so neither is listed as an assessment merely because those providers cover other certifications.
