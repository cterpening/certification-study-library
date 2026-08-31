---
exam_code: GH-100
vendor_id: github
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# GH-100 GitHub Enterprise Administrator Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official GH-100 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100) is authoritative.

**Current baseline:** Skills measured as of July 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [GH-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100)

## How to use this guide

Use the objective map to choose a domain, study its decision tables and examples, then complete the labs and explain the exam distinctions without notes. Focus on control planes, identity boundaries, policy inheritance, evidence, and operational ownership rather than memorizing screens.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight |
|---|---:|
| Manage GitHub identities and access | 15–20% |
| Administer GitHub Enterprise environment | 10–15% |
| Implement secure development and compliance | 25–30% |
| Manage GitHub Actions | 20–25% |
| Monitor and optimize GitHub usage | 10–15% |

GH-100 asks you to select the correct control plane and operating model. For every scenario, identify the deployment, identity source, ownership boundary, effective policy, responsible administrator, and evidence needed to verify the result.

---

# 1. Enterprise topology and deployment choices

```text
enterprise account
├── enterprise teams and policy
├── organization A
│   ├── teams
│   └── repositories
└── organization B
    ├── teams
    └── repositories
```

| Deployment | Main characteristics |
|---|---|
| GHEC with personal accounts | Users retain personal GitHub identities; enterprise governs organizations and enterprise resources |
| GHEC with Enterprise Managed Users | Identity provider provisions and controls enterprise-only managed identities |
| GHEC with data residency and EMU | Hosted enterprise environment with regional data-residency capabilities and managed identities |
| GitHub Enterprise Server | Customer-hosted appliance with separate upgrade, backup, networking, and support responsibilities |

Start architecture decisions with GitHub's current [enterprise-type comparison](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/choose-an-enterprise-type). Identity lifecycle, outside collaboration, recovery, data location, endpoint behavior, service operations, and migration options follow from this choice; it is not merely a billing selection.

**VERIFY CURRENT:** Feature availability, migration paths, licensing, residency regions, and release support differ. Do not assume a GitHub.com feature exists in the deployed GHES version.

Enterprise policy can enforce a setting or delegate it to organizations. Organization settings govern their repositories within enterprise boundaries. Repository administrators cannot override a higher-scope prohibition.

---

# 2. Identity, authentication, and provisioning

## Personal accounts versus managed users

| Personal account model | Enterprise Managed Users model |
|---|---|
| User creates and controls general GitHub identity | Enterprise IdP provisions and controls identity |
| Identity may participate outside enterprise | Managed identity is constrained to enterprise use |
| Enterprise links access through org membership/SSO | Lifecycle follows enterprise identity provisioning |

EMU improves centralized lifecycle control but changes external collaboration and identity behavior. The [Enterprise Managed Users documentation](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users) is authoritative for current account restrictions and identity-provider requirements. Do not infer EMU behavior from a personal-account enterprise.

## SAML SSO, SCIM, and team synchronization

- [**SAML SSO**](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-saml-for-enterprise-iam) authenticates users and connects GitHub access to the identity provider.
- [**SCIM**](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim) provisions, updates, and deprovisions user identity/membership data.
- [**Team synchronization**](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/managing-team-synchronization-for-organizations-in-your-enterprise) maps IdP groups to GitHub teams without becoming the entire account-lifecycle mechanism.
- **2FA** strengthens personal-account authentication and can be required by organizations/enterprises.

Authentication answers who the user is. Provisioning manages lifecycle. Authorization determines what authenticated users can do.

### Lifecycle example

When an employee leaves:

1. Disable the identity in the authoritative IdP.
2. SCIM or managed-user lifecycle removes access according to configuration.
3. Review sessions, tokens, SSH keys, app grants, outside-collaborator access, and ownership assignments.
4. Reassign issues, reviews, code ownership, and operational responsibilities.
5. Verify the change through access reports and audit logs.

Do not depend on a manual GitHub removal as the only offboarding control when the enterprise has automated identity lifecycle.

---

# 3. Authorization, roles, and teams

## Repository roles

| Role | Intended use |
|---|---|
| Read | View and participate at a basic level |
| Triage | Manage issues and PRs without writing code |
| Write | Contribute code and normal repository changes |
| Maintain | Manage project settings without full sensitive administration |
| Admin | Full repository administration |

Custom roles can refine capabilities on supported plans. Use the lowest role that supports the responsibility.

## Organization and enterprise responsibility

- Enterprise owners govern enterprise policy and enterprise-level resources.
- Organization owners administer membership, teams, policy, and repositories within the organization.
- Security managers receive security-management capabilities without full organization ownership.
- Outside collaborators receive selected repository access without organization membership.
- Enterprise teams can support enterprise-wide assignment in supported models.

## Effective access

Access can come from base permissions, organization teams, enterprise teams, direct grants, outside-collaborator assignment, repository ownership, or custom roles. Audit effective access, not just the most visible team.

Use the current [organization-role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization) and [enterprise-role](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles) references when delegating administration. Similar role names at different scopes do not grant interchangeable authority.

Teams should represent durable responsibilities such as `terraform-maintainers`, not temporary projects or individuals. Nested teams inherit membership for some access/mention purposes, but **VERIFY CURRENT** the exact behavior for synchronization and review requests.

---

# 4. Policies, rulesets, and standards

| Mechanism | Purpose |
|---|---|
| Enterprise/organization policy | Controls feature availability or allowed behavior |
| Repository instruction/template | Communicates or seeds standards |
| Actions workflow | Performs deterministic checking or automation |
| CODEOWNERS | Routes path-based review responsibility |
| Ruleset/branch protection | Blocks reference updates until conditions pass |
| Environment protection | Governs deployments to an environment |
| Audit log | Records relevant administrative/security activity |

An organization standard is mature when it includes guidance, reusable implementation, automated evidence, accountable ownership, enforced conditions, and exception/audit processes.

### Example Terraform control stack

- Template repository supplies README, CODEOWNERS, workflows, and instructions.
- Reusable workflow runs `terraform fmt`, `validate`, linting, scanning, and plan.
- CODEOWNERS requests platform/security review.
- Organization ruleset requires PR, owner approval, and the central workflow.
- Production environment requires authorized deployment review.
- Actions uses Azure OIDC, not a stored client secret.
- Audit logs and deployment history provide evidence.

## Rulesets

[Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) can target repositories and refs and may require PRs, approvals, code owners, status checks, signed commits, linear history, successful deployments, or restricted updates. Bypass should be limited, justified, and audited.

CODEOWNERS alone does not enforce approval. A running workflow alone does not block merge. Connect each with a rule.

---

# 5. Secure software development and compliance

Administrators enable and govern capabilities; developers and security teams triage and remediate findings.

| Capability | Administrative concern |
|---|---|
| Dependabot alerts/updates | Enablement, permissions, update configuration, alert workflow |
| Secret Protection | Push protection, alert access, patterns, bypass, response |
| Code Security/CodeQL | Default setup, advanced workflows, languages, alert permissions |
| Security advisories | Private coordination and disclosure process |
| Security Overview | Enterprise/organization posture and coverage |

Define a response plan covering ownership, severity, SLAs, triage, remediation, exception approval, disclosure, and evidence. Enabling alerts without assigning responders creates unmanaged risk.

## Audit and compliance

Use the [enterprise audit log](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise) to investigate policy, access, membership, repository, app, security, and administrative events. Enterprise plans may support streaming/export to external systems.

Know:

- Who can view which logs
- Search/query syntax and APIs
- Retention and export architecture
- Time synchronization and identity attribution
- Alerting on high-risk events
- Difference between GitHub audit evidence and application/workload telemetry

**VERIFY CURRENT:** Event names, fields, retention, and streaming destinations.

---

# 6. APIs and integrations

## PATs, GitHub Apps, and OAuth Apps

| Credential/integration | Best-fit model |
|---|---|
| Fine-grained PAT | User automation restricted to selected resources/permissions |
| Classic PAT | Legacy or unsupported fine-grained scenario; broader scopes |
| [GitHub App](https://docs.github.com/en/apps/overview) | Installation-scoped service integration with granular permissions and short-lived tokens |
| OAuth App | Acts on behalf of a user using authorized scopes |

Prefer GitHub Apps for durable organizational integrations when supported. Review requested permissions, webhook access, publisher, ownership, incident response, and token lifecycle.

Rate limits vary by authentication type and endpoint. Build integrations that inspect response headers, paginate, cache, retry with backoff, and avoid wasteful polling.

Enterprise/organization policy may restrict PATs and require approval for GitHub or OAuth Apps. A useful integration is not automatically an approved integration.

---

# 7. GitHub Actions administration

## Governance

The [enterprise Actions administration documentation](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-github-actions-for-your-enterprise) covers the policy, reuse, runner, and networking control planes. Administrators decide:

- Whether Actions is enabled
- Which actions/reusable workflows may run
- Default `GITHUB_TOKEN` permissions
- Fork PR behavior
- Workflow and artifact retention
- Runner access and isolation
- Secret and variable scope
- Required reusable workflows or status checks

Central reusable workflows reduce drift but must be versioned, reviewed, available, and protected. Template workflows are copied and then drift independently.

## Runners

| Concern | GitHub-hosted | Self-hosted |
|---|---|---|
| Maintenance | GitHub | Customer |
| Lifecycle | Usually ephemeral | Must be designed/operated |
| Internal network access | Product-dependent networking | Customer-controlled |
| Custom software | Install at runtime/custom options | Fully customizable |
| Untrusted-code risk | Isolated hosted lifecycle | High if persistent/privileged |

Runner groups restrict which repositories/organizations can use runners. Labels select capabilities. Monitor online/offline state, queue time, job duration, capacity, image/tool versions, patching, and cleanup.

For Azure private networking, choose a supported hosted-networking option or isolated self-hosted design. Avoid placing broadly trusted runners on networks with unrestricted production access.

## Secrets

Secrets can be scoped to enterprise-supported constructs, organizations, repositories, and environments. Environment approval can delay access until deployment is approved. Integrate external vaults with short-lived identity—prefer OIDC to a stored cloud secret.

---

# 8. Support and diagnostics

Administrators should separate:

- Configuration or access problems they can resolve
- Product incidents visible on GitHub Status
- GHES appliance issues requiring diagnostics/support bundles
- Security incidents requiring internal response and possibly GitHub Support
- Billing/licensing issues requiring the appropriate account/support path

[GHES support bundles](https://docs.github.com/en/enterprise-server@latest/admin/monitoring-and-managing-your-instance/monitoring-your-instance/about-support-bundles) can contain sensitive diagnostic data. Limit access and transfer them only through approved support procedures. For GHES, know the roles of appliance health checks, logs, backups, upgrades, replication, and support tooling at a conceptual level.

---

# 9. Licensing, usage, and optimization

Use the current [product and license usage](https://docs.github.com/en/billing/how-tos/products/view-productlicense-use) views as evidence, then interpret them in business context. Monitor:

- Enterprise and product license assignment/consumption
- Copilot and metered-product usage
- Actions minutes, storage, runners, and artifacts
- Security-feature enablement and adoption
- Active versus dormant organizations/repositories/users
- API consumption and integrations

Optimization is not simply reclaiming every unused seat. Consider seasonal work, critical responders, new teams, compliance, and adoption barriers. Pair usage data with business context.

**VERIFY CURRENT:** SKU names, included allowances, metering, billing, and license-assignment methods.

---

# 10. Objective-by-objective administration deep dive

## Use a six-question administrator method

Enterprise scenarios often mention several products and roles at once. Reduce each scenario to six questions before choosing a control:

1. **Where does the requirement apply?** Enterprise, organization, repository, environment, runner group, or application installation?
2. **Who or what is the subject?** Managed user, personal account, outside collaborator, team, GitHub App, workflow identity, or support engineer?
3. **Which system is authoritative?** Identity provider, enterprise policy, organization setting, repository configuration, or external vault?
4. **Is the need guidance, automation, or enforcement?** Documentation teaches; workflows produce evidence; rules and policies enforce.
5. **What exception is allowed?** Identify bypass actors, duration, approval, and compensating control.
6. **What evidence proves the result?** Effective access, audit event, workflow result, deployment record, usage report, or support diagnostic?

This method prevents a common category error: choosing a repository control for an enterprise requirement or choosing an identity-provider control for a GitHub authorization decision.

> **Related item:** Treat each administrative change as a control with an owner, desired state, evidence source, and rollback plan. That is the same control-design discipline used in infrastructure as code and compliance engineering, even when the GitHub setting is changed manually.

## Identity architecture and recovery paths

### Separate four identity functions

| Function | Question answered | Typical mechanism |
|---|---|---|
| Authentication | Who is signing in? | GitHub authentication, SAML SSO, 2FA |
| Provisioning | Should the identity exist and remain active? | SCIM or the EMU provisioning integration |
| Group mapping | Which responsibility groups should the user join? | Team synchronization |
| Authorization | What can the authenticated subject do? | Enterprise, organization, team, repository, and app permissions |

A successful SAML assertion does not itself prove that the user should have a particular repository role. A SCIM-created account does not itself determine every team or direct repository grant. Diagnose the failed layer instead of reconfiguring all four.

### Joiner, mover, and leaver design

For a **joiner**, validate the immutable identity mapping, provision the account, map durable IdP groups to teams, assign only necessary roles, and verify access from the user's perspective. For a **mover**, remove access associated with the former role before or alongside new access; additive-only automation creates privilege accumulation. For a **leaver**, disable the authoritative identity, revoke active access, review credentials and app grants, transfer business ownership, and retain appropriate audit evidence.

Build reconciliation into the lifecycle. Compare expected IdP membership with GitHub membership and effective repository access. A healthy provisioning job can still preserve an inappropriate direct grant that it does not own.

### Break-glass administration

Design emergency access before the identity provider fails. Define which accounts can recover the enterprise, how credentials are protected, when their use is allowed, how actions are monitored, and how access is rotated afterward. Do not make the normal SSO path and the recovery path depend on the same failed component.

> **Related item:** Break-glass access is a resilience control, not a convenience account. Practice the recovery procedure in a controlled exercise and alert on every use. The current GitHub identity documentation should determine which recovery mechanisms are supported for the chosen deployment.

### Authentication troubleshooting sequence

When a user cannot reach a repository, check in this order:

1. Is the correct GitHub identity being used?
2. Is the account active in the authoritative identity system?
3. Did SAML authentication and authorization succeed for the correct enterprise or organization?
4. Did SCIM provisioning and group synchronization complete?
5. Is the user a member, outside collaborator, or managed user as intended?
6. Which team, direct grant, base permission, or custom role produces effective access?
7. Does a higher-scope policy or IP restriction block the operation?
8. What do audit and IdP logs show at the same timestamp?

This sequence moves from identity to lifecycle to authorization to policy. It avoids treating every access problem as an SSO problem.

## Access and permission review

### Build an effective-access inventory

Inventory more than organization members. Include enterprise owners, organization owners, billing managers, security managers, outside collaborators, repository administrators, custom roles, enterprise and organization teams, direct grants, deploy keys, machine users where still present, GitHub App installations, OAuth grants, PAT policies, Actions credentials, and bypass actors.

For each privileged path, record:

- business owner and technical owner;
- source of the grant;
- scope and expiration if temporary;
- last use or review evidence;
- removal mechanism;
- whether the grant can bypass another control.

### Review permission intent, not only membership

Ask why a team has access, whether the role matches its job, and whether the repository still belongs in that access boundary. A correctly synchronized group can be overprivileged. A repository that changes sensitivity can invalidate a previously reasonable team grant.

Prefer team-based grants for durable responsibilities because they are easier to review and automate. Reserve direct grants for justified exceptions and make them visible in review reports. Use outside collaborators deliberately: their narrower membership model does not eliminate the need to govern repository access and credentials.

> **Related item:** Periodic access reviews and just-in-time access solve different problems. Reviews find accumulated or stale privilege; time-bound elevation limits how long a privileged grant exists. Mature enterprises often need both.

## Policy inheritance, rulesets, and exceptions

### Determine effective configuration

Think from the highest scope downward:

```text
enterprise policy
        ↓ enforce or delegate
organization policy / ruleset
        ↓ narrow or inherit
repository rule / environment protection
        ↓ evaluate actor, ref, and operation
allow, block, or allow through approved bypass
```

An enterprise owner should enforce controls that must be consistent across organizations and delegate choices that genuinely belong to product teams. Excessive centralization creates bottlenecks; excessive delegation creates inconsistent risk.

### Choose the right enforcement mechanism

| Requirement | Better control |
|---|---|
| Only approved actions may execute | Actions use policy at organization or enterprise scope |
| Changes to protected branches need reviews and checks | Ruleset or branch protection |
| A specific team must review changes to owned paths | CODEOWNERS plus required code-owner review |
| Production deployment needs approval | Environment protection and deployment policy |
| Every repository starts with recommended files | Repository template or automation |
| Every repository must continuously meet a condition | Policy, ruleset, required workflow/check, or monitoring automation depending on the condition |

Rulesets define conditions on targeted refs or repositories. Workflows perform tests. Status-check requirements connect workflow evidence to merge enforcement. Keep names and ownership stable so repositories do not silently require obsolete checks.

### Govern bypass

Bypass is part of the control design. Limit bypass to roles or apps that require it, document acceptable reasons, log its use, review the resulting change, and remove temporary access. An emergency bypass that nobody can exercise is not resilient; a standing bypass granted broadly is not meaningful enforcement.

> **Related item:** Policy as code can test administrative configuration for drift, but the automation identity becomes a privileged subject. Protect its source, deployment workflow, token permissions, and change approvals as carefully as the settings it manages.

## Secure-development administration as a service

### Roll out in observable stages

Use a staged rollout for Dependabot, Secret Protection, Code Security, and related policies:

1. Inventory repositories, languages, dependency ecosystems, current enablement, and ownership.
2. Define eligibility, exceptions, data-handling constraints, and minimum configuration.
3. Pilot with representative teams and measure noise, runtime, and remediation capacity.
4. Establish triage ownership, severity rules, service levels, and escalation.
5. Enable defaults or policies in waves.
6. Monitor coverage, backlog age, bypass, dismissal, and failed analysis.
7. Tune configuration without hiding genuine risk.
8. Report residual risk and overdue exceptions to accountable owners.

Feature enablement is an input, not the outcome. The outcome is reduced exposure with a response process that developers can actually use.

### Incident response for an exposed secret

Use this order:

1. Treat the credential as compromised.
2. Revoke or rotate it at the issuing system.
3. Determine scope, privilege, use, and exposure window.
4. Contain affected systems and investigate access logs.
5. Remove the secret from active code and configuration.
6. Decide whether history rewriting is required for the risk and distribution model.
7. Add preventive controls such as push protection, a custom pattern, or safer secret delivery.
8. Document the incident and verify recovery.

Deleting the line from the latest commit does not revoke a credential and does not remove prior Git history or clones.

### Dismissal and exception evidence

A dismissal should capture reason, reviewer, scope, expiration or review date, and compensating control where appropriate. Distinguish false positive, test data, accepted risk, and unavailable remediation; they imply different follow-up. Report stale dismissals and repeated bypass patterns.

> **Related item:** Security managers and organization owners need different privilege sets. Delegating security work through a purpose-built role reduces the number of full organization owners and improves separation of duties.

## API and application governance

### Select an integration identity

Use a GitHub App when an automation needs an installation identity, selected repositories, granular permissions, webhook delivery, and short-lived tokens. Use user-delegated OAuth when the application genuinely acts for a consenting user. Use a fine-grained PAT for constrained user automation where a GitHub App is disproportionate or unsupported. Treat classic PAT use as a legacy exception when broader scopes are unavoidable.

Ask these questions before approval:

- Who owns and supports the application?
- Which repositories and permissions does it request?
- Does it receive repository content or webhook payloads?
- Where are keys and tokens stored and rotated?
- What happens when the owner leaves or the vendor is compromised?
- Can installation be limited and reviewed?
- What audit evidence and incident contacts exist?

### Engineer for API limits

An integration should paginate, request only needed fields, cache stable data, prefer webhooks to polling where appropriate, respect primary and secondary limits, use conditional requests when supported, back off on throttling, and expose its own request/error metrics. Retrying aggressively can deepen an outage and extend rate limiting.

> **Related item:** Webhooks reduce polling but introduce delivery authenticity, replay, ordering, duplication, and retry concerns. Design consumers to verify signatures and process deliveries idempotently.

## Actions governance and runner threat modeling

### Evaluate the complete trust chain

For each workflow, identify:

- who can modify the workflow and referenced scripts;
- which event supplies the input;
- whether untrusted fork code executes;
- which token permissions and secrets are available;
- which action versions and registries are trusted;
- which runner and network receive the job;
- which artifacts cross jobs or trust zones;
- which environment approval gates deployment credentials.

A workflow can be syntactically correct and still unsafe because its event, permissions, runner, or data flow crosses a trust boundary.

### Segment runner pools

Do not use one broadly connected persistent pool for every workload. Separate at least:

| Workload | Trust posture | Design direction |
|---|---|---|
| Public or fork pull-request checks | Untrusted code | Ephemeral, no production secrets, no privileged internal network |
| Internal build and test | Organization-controlled code | Scoped repository access and limited internal services |
| Release signing | Highly privileged | Isolated, tightly approved workflow, protected keys, auditable output |
| Production deployment | Privileged target access | Environment approval, short-lived identity, restricted runner group/network |

Prefer ephemeral self-hosted runners for untrusted or variable workloads when self-hosting is required. If runners persist, assume a job can alter state for the next job unless cleanup and isolation are proven.

### Troubleshoot runner capacity

Separate **queue delay** from **execution duration**. Queue delay points toward labels, group access, offline runners, concurrency, autoscaling, or capacity. Slow execution points toward tools, network, cache, dependency service, hardware, or the job itself. Capture both distributions rather than only average workflow duration.

> **Related item:** Runner groups are authorization boundaries; labels are scheduling selectors. A sensitive label does not prevent an unauthorized repository from targeting a runner if group access is too broad.

## Monitoring, support, and optimization

### Use three evidence planes

| Plane | Examples | Answers |
|---|---|---|
| Audit | Administrative and security events | Who changed what, where, and when? |
| Operational | Status, runner health, queues, API errors, GHES diagnostics | Is the platform or integration healthy? |
| Adoption and cost | Active users, feature use, Actions consumption, licenses | Is the service delivering value efficiently? |

Do not use aggregate usage data to prove a specific administrative action, and do not use an audit event to infer that a feature is broadly adopted.

### Escalate with a useful diagnostic package

Before opening support, establish impact, start time, affected users and repositories, deployment/version, recent changes, reproduction steps, correlation identifiers, sanitized logs, and checks already performed. For GHES, follow the supported bundle-generation and secure-transfer process. Remove secrets from ad hoc attachments but do not arbitrarily alter an official diagnostic bundle in a way that makes it unusable.

### Optimize without creating hidden risk

For licenses and metered services, classify apparent underuse:

- truly unused and reclaimable;
- seasonal or standby responsibility;
- blocked by missing training or configuration;
- intentionally retained for resilience or compliance;
- incorrectly measured because the signal is incomplete.

Then choose reclaim, reassign, train, repair, or retain. Cost optimization is a decision process, not an automatic deletion job.

> **Related item:** Adoption metrics can become perverse incentives. Pair volume measures with outcomes such as lead time, reliability, remediation age, or developer satisfaction so teams are not rewarded merely for generating more activity.

## Knowledge checks

1. A user can authenticate through SAML but cannot access a repository expected from an IdP group. Which layers should you inspect, and in what order?
2. An organization wants every production deployment approved, but not every pull request. Why is an environment protection rule a better fit than another branch-review requirement?
3. A repository administrator can merge after a CodeQL workflow succeeds even though no security reviewer approved the change. Which controls are missing if owner approval is required?
4. A vendor requests an OAuth App with broad user scopes for a background organization integration. What alternative identity should you evaluate, and what approval evidence do you need?
5. Fork pull requests wait for a runner labeled `production`. Explain why changing the label alone does not fix the security design.
6. License reports show no recent activity for incident responders. What business context should be checked before reclaiming their seats?

For each answer, state the scope, subject, authoritative system, enforcement point, exception path, and evidence source.

---

# 11. Deployment and operations playbooks

## Choose a deployment from operational requirements

Use the deployment name only after mapping the requirement:

| Requirement | GHEC personal accounts | GHEC with EMU | GHEC data residency with EMU | GHES |
|---|---|---|---|---|
| Users need one identity for enterprise and public open source | Strong fit | Managed users have restricted external behavior | Managed users have restricted external behavior | Separate server identity/environment |
| IdP controls account creation and username lifecycle | Limited to membership/access lifecycle | Core design | Core design | Depends on GHES authentication/provisioning design |
| GitHub operates the application platform | Yes | Yes | Yes | No—customer operates appliance and dependencies |
| Customer selects a supported hosted data region | GitHub.com service terms | GitHub.com service terms | Core design goal in supported regions | Customer selects hosting location |
| Customer controls upgrade window and server version | No | No | No | Yes, within supported releases |
| Private/disconnected network requirements | Limited by cloud connectivity model | Limited by cloud connectivity model | Limited by hosted environment model | Strongest platform/network control, with greater operations burden |

Document collaboration with outsiders, account recovery, IdP outage behavior, legal/residency interpretation, integration endpoints, Actions networking, service availability, support, backup, and disaster recovery. Data residency is not the same as data sovereignty: the latter includes legal control, access, processing, and organizational obligations beyond storage location.

> **Related item:** Deployment choice creates a responsibility model. GitHub operates GHEC availability and upgrades; a GHES customer must operate capacity, networking, backups, recovery, patching, upgrades, high availability, and monitoring. The feature list alone is an incomplete comparison.

## Operate GitHub Enterprise Server

GHES is an appliance, not a set of packages to customize freely. Build a supported runbook around the current [GHES administration documentation](https://docs.github.com/en/enterprise-server@latest/admin).

### Availability, backup, and recovery

GitHub documents GHES high availability as active/passive, with asynchronous one-way replication from a primary to a replica. The customer must manage traffic redirection and promotion. An HA replica is not a backup: logical corruption or deletion can replicate, so separate historical backups and restore testing remain necessary. See [high-availability configuration](https://docs.github.com/en/enterprise-server@latest/admin/monitoring-and-managing-your-instance/configuring-high-availability/about-high-availability-configuration).

| Control | Protects against | Does not replace |
|---|---|---|
| Backup snapshots | Need to restore historical appliance data | Tested restore, secure/off-site storage, HA |
| HA replica | Selected primary appliance/infrastructure failures | Backup or capacity scaling |
| Geo-replication/repository cache | Supported geographic performance/availability needs | Primary write capacity or backup |
| Monitoring | Early detection of health, capacity, replication, or backup failures | Recovery procedure |

Define recovery time and recovery point objectives, backup frequency/retention, encryption and access, restore host capacity, external storage dependencies, DNS/load-balancer changes, and validation. A completed backup job is not sufficient evidence; periodically restore into an isolated supported target and verify repositories, metadata, identity configuration, Actions dependencies, packages, and critical integrations.

GitHub's current backup method and prerequisites can change across GHES releases. **VERIFY CURRENT:** whether the deployment uses the appliance backup service or GitHub Enterprise Server Backup Utilities, supported versions, storage sizing, and restore compatibility.

### Upgrade runbook

Before an upgrade:

1. confirm the current version, supported upgrade path, release notes, known issues, and package signature guidance;
2. validate platform capacity and hypervisor/cloud prerequisites;
3. confirm current successful backup and tested recovery evidence;
4. validate replication health for HA and external storage/services;
5. inventory Actions runners, GitHub Connect, SMTP, object storage, proxies, TLS, IdP, monitoring, and integrations;
6. define maintenance communication, validation, rollback/recovery decision, and support contacts;
7. test the upgrade in a representative nonproduction environment when risk warrants it.

Afterward, validate web/Git/API access, authentication and provisioning, representative repositories and searches, Actions, packages, pages, hooks/apps, mail, audit, backup, replication, and monitoring. Treat a version upgrade as a service change with business validation, not merely a successful installer exit.

> **Related item:** A rollback may be a restore or appliance replacement rather than an in-place downgrade. Determine the supported recovery method before the change and make the go/no-go point explicit.

## Plan enterprise migrations without confusing tool coverage

Migration is adjacent operational knowledge rather than a named GH-100 objective. It matters because deployment and identity choices often occur during adoption.

GitHub Enterprise Importer supports selected source-to-GHEC paths and can run repository migrations or, for supported GitHub.com sources, organization migrations. The migrated data differs by source and migration type. Trial runs, error-log review, identity attribution, and follow-up configuration are required; the importer is not a promise that every setting and integration moves. See the official [GitHub Enterprise Importer overview](https://docs.github.com/en/migrations/using-github-enterprise-importer/understanding-github-enterprise-importer/about-github-enterprise-importer).

Create these inventories before the first trial:

- organizations, repositories, size, LFS, visibility, forks, and archives;
- users, teams, outside collaborators, bots, mannequins/attribution, and ownership;
- branch protection/rulesets, webhooks, apps, deploy keys, secrets, environments, and Pages;
- Actions workflows, reusable dependencies, runners, artifacts, packages, and external storage;
- security settings, alerts, custom patterns, audit requirements, and exceptions;
- names, redirects, DNS, network paths, freeze/delta plan, and user communications.

For each item mark migrate automatically, recreate, transform, archive, or retire. GitHub notes that the importer does not provide delta migration for applicable repository migration paths; if work continues after the migration source snapshot, the change must be handled explicitly. Validate Git objects and platform metadata separately.

> **Related item:** A migration is complete when the destination is usable and governed—not when bytes arrive. Identity reclamation, team access, secrets, apps, runners, rules, and owner acceptance are post-migration work.

## Implement IP allow lists safely

An enterprise IP allow list restricts access to protected enterprise resources for covered interactive and non-interactive authentication. GitHub documents important exceptions and product interactions, so do not summarize it as “only office IPs can reach GitHub.” Review the current [IP allow-list scope](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-network-traffic-to-your-enterprise-with-an-ip-allow-list).

Rollout sequence:

1. inventory users, VPN/egress, IPv4/IPv6, IdP, CI runners, GitHub Apps, webhooks, Dependabot, Pages, and emergency administration;
2. decide GitHub-managed versus applicable IdP allow-list control;
3. add and describe explicit CIDR entries, including the administrator's path;
4. use the built-in address check and test UI, Git, API, SSH, apps, and Actions;
5. enable in a controlled window with a recovery owner;
6. monitor denials and audit changes;
7. review ranges and GitHub App inherited entries regularly.

With an IP allow list, Actions needs network egress that appears from allowed addresses. GitHub's documentation calls for self-hosted runners or eligible larger hosted runners with static ranges, with Azure subnet considerations when using private networking. **VERIFY CURRENT:** exact runner types and addressing because hosted networking changes.

## Design Azure private networking for hosted runners

Azure private networking connects eligible GitHub-hosted runners to an Azure virtual network. A network configuration is associated with a runner group; repository/organization access to that group remains the authorization boundary. The VNet controls private reachability and outbound policy, while GitHub manages the ephemeral runner infrastructure under the supported design. See [private networking for GitHub-hosted runners](https://docs.github.com/en/enterprise-cloud@latest/actions/concepts/runners/private-networking).

Trace four separate layers when a job cannot reach a private service:

1. Can the repository target the runner group?
2. Did the job land on a runner associated with the expected network configuration?
3. Do subnet, route, DNS, firewall/NSG, proxy, and private-endpoint rules permit the path?
4. Does the workflow identity have application/resource authorization?

Do not solve a denied Azure role assignment by broadening the network. Do not solve missing DNS by granting a more powerful GitHub token.

## Engineer the audit pipeline

Audit-search, API, and streaming serve different operating patterns. Search supports investigation; APIs support bounded retrieval/automation; streaming forwards new enterprise events to an external system for longer retention and correlation. GitHub documents audit streaming as at-least-once delivery, so consumers must tolerate duplicates. See [enterprise audit-log streaming](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).

For the external pipeline, preserve source event identifiers, timestamp, actor, action, scope, transport receipt time, and raw evidence under appropriate controls. Normalize into a schema but retain the original event for investigation. Monitor delivery health and gaps; an enabled stream is not proof that events arrive in the SIEM.

Create detections for high-risk administrative changes such as owner/role changes, authentication-policy changes, app installation/permission changes, ruleset bypass, secret or runner policy changes, and audit-stream changes. Tune to the exact current event names and fields.

> **Related item:** At-least-once delivery favors completeness over uniqueness. Deduplicate by stable event identity rather than discarding two similar-looking actions that may both be legitimate events.

---

# 12. Failure-mode drills and administrative decision records

## Diagnose identity as a chain of control planes

An identity problem is rarely solved by changing every setting that mentions the user. Locate the failed plane first:

| Plane | Authoritative evidence | Typical symptom | Administrator question |
|---|---|---|---|
| Account creation | IdP provisioning job and SCIM result | No managed account or organization invitation exists | Was the subject assigned to the correct enterprise application and provisioning scope? |
| Authentication | IdP sign-in log and GitHub linked-identity/session evidence | Account exists, but interactive sign-in fails | Did SAML/OIDC complete, and do issuer, subject, certificate, clock, and policy match? |
| Enterprise/organization membership | GitHub People views, IdP group assignment, SCIM audit | Authentication succeeds, but the expected organization is unavailable | Was access provisioned at the correct enterprise or organization boundary? |
| Team membership | IdP group membership and synchronized-team state | User reaches the organization but not team repositories | Is the correct IdP group mapped, synchronized, and nested in a supported way? |
| Repository authorization | Team/direct/base/custom role and effective access | User sees the repository but cannot perform one action | Which grant supplies the role, and is a rule or policy blocking the operation? |
| Credential authorization | SSO authorization, token/app permissions, expiry, IP/network policy | Browser access works while Git/API/automation fails | Is this credential current, authorized, scoped, and allowed by enterprise policy? |

For a personal-account enterprise with SAML, the GitHub account and external identity are linked; provisioning access and authenticating the account remain separate operations. With Enterprise Managed Users, the IdP controls managed-account lifecycle. GitHub's [enterprise-type comparison](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/choose-an-enterprise-type) should be the starting point because the recovery and collaboration model follows that initial choice.

### SAML/SCIM incident drill

Suppose an existing employee can authenticate but loses access after moving departments:

1. Establish whether the incident affects one identity, one mapped group, one organization, or the enterprise application.
2. Check the IdP assignment and group-change event before manually adding GitHub access.
3. Confirm the SCIM operation and resulting enterprise/organization membership.
4. Confirm synchronized team membership and repository grants.
5. Inspect SAML-linked identity, sessions, credentials, and relevant audit events.
6. Correct the authoritative IdP mapping, then allow reconciliation to restore the intended state.
7. Remove temporary direct access and record why it existed.

Directly adding the user to a team may hide a broken group rule and create access that survives the next move. A safe temporary grant needs an owner, reason, expiration, and follow-up test of the authoritative path.

For a broad provisioning failure, preserve one failed request/response and correlation time, then examine credentials, endpoint/tenant selection, attribute mapping, uniqueness, rate limits, and IdP job status. Avoid repeated bulk retries until the failure class is understood; retries can create load and make the evidence harder to read.

> **Related item:** Identity reconciliation is a desired-state problem. The IdP says who should exist and which source groups they belong to; GitHub reports the realized access. A useful control continuously compares the two and has an owned exception process.

## Delegate administration without losing accountability

GitHub provides enterprise owners, billing managers, app managers, security managers, organization roles, repository roles, and supported custom roles. Current capabilities and preview status must be checked in [Abilities of roles in an enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles).

Use a task-to-role record:

| Administrative task | Preferred delegation question | Evidence to retain |
|---|---|---|
| Manage invoices or payment details | Can a billing-specific role replace enterprise ownership? | Role assignment and periodic review |
| Approve an enterprise-owned GitHub App | Can app management be separated from organization ownership? | Requested permissions, reviewer, decision, expiry/review date |
| Review security coverage and alerts | Can a security role/team perform this without general settings control? | Assignment scope and response ownership |
| Maintain one repository | Is `Maintain` or a custom repository role sufficient? | Effective-access result and task test |
| Change enterprise policy | Is the change truly enterprise-wide, and is dual review warranted? | Change record, before/after policy, audit event |
| Emergency recovery | Who holds break-glass authority and how is use detected? | Credential custody, test, alert, post-use rotation |

GitHub recommends at least two owners for an account so administration does not depend on one reachable person. That does not justify granting owner everywhere. Keep daily roles narrow, protect emergency ownership separately, and test both removal and recovery.

An enterprise role, organization role, repository role, Actions environment reviewer, and IdP administrator are different authorities. A segregation-of-duties review should identify dangerous combinations—for example, a person who can change a deployment workflow, bypass its merge rule, approve the production environment, and alter the cloud role used by the job.

## Troubleshoot Actions from queue to target

Treat an Actions failure as a staged path:

```text
event -> workflow eligibility -> policy/reuse -> queue -> runner match
      -> checkout/action download -> identity -> network -> target authorization
      -> artifacts/logs/retention
```

| Symptom | First evidence | Avoid this shortcut |
|---|---|---|
| Workflow never appears | Event, path/branch filters, workflow file location, Actions policy | Increasing runner capacity |
| Job remains queued | Runner-group access, labels, online/busy capacity, concurrency | Adding a broadly accessible persistent runner |
| Reusable workflow is denied | Allowed-actions/reuse policy and caller/called-workflow scope | Copying the central workflow into every repository |
| OIDC token exchange fails | Job permissions, subject/audience claims, cloud federation rule | Storing a long-lived cloud secret |
| Private service is unreachable | Runner network association, DNS, route, firewall/NSG, endpoint | Granting broader GitHub repository permission |
| Target returns authorization denied | Workload identity and target role assignment | Opening the network to the internet |
| Artifact is unavailable | Upload step, name, retention, permissions, run conclusion | Raising retention without confirming creation |

Record queue time separately from execution time. Long queue time suggests capacity, runner selection, concurrency, or service availability; long execution time suggests workflow, dependency, cache, target-service, or runner-performance issues. Averages can hide a small pool with severe tail latency, so compare percentiles and segment by runner group, repository, job, and event source.

When self-hosted runners process pull requests, assume workflow-controlled code may attempt to read the runner filesystem, environment, network, credentials, or prior-job residue. Prefer ephemeral clean instances, segment trust levels, minimize network and token privilege, and do not place untrusted contributions on a runner that can deploy production.

## Write an evidence-producing control

For each enterprise standard, create a short decision record:

1. **Objective:** the risk or operating outcome, stated without naming a feature.
2. **Scope:** enterprise, organizations, repositories, identities, runners, or integrations covered.
3. **Mechanism:** policy, ruleset, role, workflow, application, operational procedure, or layered set.
4. **Owner:** who maintains the control and who responds to violations.
5. **Exception:** eligibility, approver, compensating control, expiration, and review.
6. **Evidence:** configuration export, audit event, workflow result, access report, ticket, or test.
7. **Failure response:** alert, containment, restoration, communication, and learning review.

Example: “Require pull requests” is only a mechanism. The objective may be independent review of protected code. Evidence then includes the targeted ruleset, bypass actors, approval state, merge/audit record, and periodic test—not a screenshot showing that one repository has a checkbox enabled.

> **Related item:** Compliance evidence should be reproducible. A reviewer should be able to start from the stated scope, retrieve the current configuration and events, and reach the same conclusion without relying on the control owner's memory.

---

# 13. Hands-on labs

## Lab 1: Enterprise design comparison

Design identity, collaboration, support, and migration for GHEC personal accounts, GHEC EMU, data-residency deployment, and GHES. State why each is or is not suitable.

## Lab 2: Organization standards stack

Create teams, base permissions, a template repository, CODEOWNERS, a reusable Terraform workflow, ruleset, and protected production environment. Demonstrate guidance versus enforcement.

## Lab 3: Identity lifecycle tabletop

Walk through joiner, mover, and leaver cases using SAML, SCIM, team sync, direct grants, PATs, SSH keys, GitHub Apps, and audit verification.

## Lab 4: Actions runner architecture

Design runner groups for untrusted PR validation, internal integration tests, and production deployment through Azure private networking. Include isolation, scaling, patching, logging, and failure recovery.

## Lab 5: Security rollout

Plan phased enablement of dependency alerts, Secret Protection, push protection, CodeQL, security managers, response SLAs, exception handling, and reporting.

## Lab 6: Audit investigation

Create a hypothetical unauthorized ruleset bypass. Identify the audit searches, identities, timestamps, linked workflow/deployment evidence, containment, and follow-up controls.

---

# 14. Exam distinctions

| Contrast | Remember |
|---|---|
| SAML vs SCIM | Authentication/SSO versus provisioning lifecycle |
| SCIM vs team sync | Account/membership lifecycle versus IdP group-to-team mapping |
| Personal account vs managed user | User-controlled general identity versus enterprise-provisioned identity |
| Team vs role | Group of people versus capability set |
| Base permission vs team grant | Default member access versus responsibility-based added access |
| Policy vs ruleset | Feature/behavior governance versus ref-update conditions |
| CODEOWNERS vs required review | Review routing versus enforced approval |
| GitHub App vs OAuth App | Installation/service identity versus user-delegated access |
| Runner label vs group | Capability selection versus access boundary |
| Template vs reusable workflow | Copied starting point versus centrally invoked automation |
| Audit log vs usage metrics | Event evidence versus aggregate adoption/consumption |
| GHEC vs GHES | GitHub-hosted service versus customer-operated appliance |
| HA replica vs backup | Current replicated standby versus historical recovery copy |
| IP allow list vs authorization | Permitted network origin versus permission to the resource |
| Runner group vs network configuration | Which repositories may use compute versus which VNet the compute joins |
| Migration transfer vs migration completion | Data movement versus usable, governed destination and acceptance |

---

# 15. Readiness checklist

- [ ] I can select among GHEC personal accounts, EMU, data residency, and GHES.
- [ ] I distinguish authentication, provisioning, authorization, SAML, SCIM, and team sync.
- [ ] I can determine effective repository access and apply least privilege.
- [ ] I can design policy inheritance, teams, CODEOWNERS, workflows, rulesets, and environments.
- [ ] I can govern Dependabot, Secret Protection, CodeQL, advisories, and security response.
- [ ] I distinguish fine-grained/classic PATs, GitHub Apps, and OAuth Apps.
- [ ] I can manage Actions policies, reusable workflows, runners, groups, networking, secrets, and OIDC.
- [ ] I can distinguish administrator, internal security/operations, and GitHub Support responsibilities.
- [ ] I can use audit evidence and usage data for investigation, compliance, adoption, and optimization.
- [ ] I can explain GHES backup, HA, restore testing, upgrade, and validation responsibilities.
- [ ] I can plan an enterprise migration inventory and post-migration validation without assuming every object transfers.
- [ ] I can design and troubleshoot IP allow lists, Azure private networking, and audit streaming by layer.
- [ ] I can diagnose identity and Actions failures from the authoritative control plane instead of masking them with direct access or broader privilege.
- [ ] I can delegate administrative duties and define reproducible control evidence, exceptions, and recovery ownership.
- [ ] I know which product, licensing, event, and UI details require current documentation.

## Primary references

- [GitHub Enterprise Cloud documentation](https://docs.github.com/en/enterprise-cloud@latest/admin)
- [About Enterprise Managed Users](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)
- [Choosing a GitHub Enterprise Cloud enterprise type](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/choose-an-enterprise-type)
- [SAML SSO](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-saml-for-enterprise-iam)
- [SCIM](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim)
- [Abilities of enterprise roles](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles)
- [Organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)
- [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [Audit log](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise)
- [Actions enterprise administration](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-github-actions-for-your-enterprise)
- [GitHub Apps](https://docs.github.com/en/apps/overview)
- [GitHub Enterprise Server administration](https://docs.github.com/en/enterprise-server@latest/admin)
- [GHES high availability](https://docs.github.com/en/enterprise-server@latest/admin/monitoring-and-managing-your-instance/configuring-high-availability/about-high-availability-configuration)
- [GitHub Enterprise Importer](https://docs.github.com/en/migrations/using-github-enterprise-importer/understanding-github-enterprise-importer/about-github-enterprise-importer)
- [Enterprise IP allow lists](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-network-traffic-to-your-enterprise-with-an-ip-allow-list)
- [Private networking for hosted runners](https://docs.github.com/en/enterprise-cloud@latest/actions/concepts/runners/private-networking)
- [Audit-log streaming](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)

Recheck licensing, deployment availability, identity restrictions, GHES version support, runner networking, and audit-event references before the exam.

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Start with the official paths, then pick the explanations, formats, and practice that work for you and close specific blueprint gaps. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — GitHub Administration Part 1](https://learn.microsoft.com/en-us/training/paths/github-administration-products/) and [Part 2](https://learn.microsoft.com/en-us/training/paths/github-admin-2/github-admin-2/) | Free | About 12–16 hours | Official starting point and closest match to the published objectives |
| [Microsoft — GH-100 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/github-administration/practice/assessment?assessment-type=practice&assessmentId=1841205577&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; start here before buying another assessment |
| [GitHub Skills](https://github.com/skills) | Free account | Select 2–5 hours | Repository, Actions, and security practice; enterprise identity and governance still need a suitable lab or sandbox |
| [Pluralsight — GitHub Administration](https://www.pluralsight.com/paths/github-administration) | Subscription | About 12–18 hours | Structured administration path; compare its module dates and coverage with the July 2026 blueprint |
| [LinkedIn Learning — GitHub Administration Cert Prep](https://www.linkedin.com/learning/github-administration-cert-prep) | Subscription | 3 hours 3 minutes | Noah Gift course released September 2025; useful compact survey, but it includes older-scope material and needs a July 2026 objective delta |
| [MeasureUp — GH-100 practice test](https://www.measureup.com/microsoft-gh-100-github-administration-practice-test.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 105 questions; its detailed domains are administration-oriented, but some public marketing copy incorrectly describes Copilot, so validate explanations against the current blueprint and GitHub Docs |
| [GitHub YouTube](https://www.youtube.com/@GitHub) | Free | Select 2–6 hours by gap | Product demonstrations and enterprise sessions; select videos by objective rather than treating the channel as an exam course |
| [GitHub Enterprise Server documentation](https://docs.github.com/en/enterprise-server@latest/admin) | Free | Select 4–8 hours by GHES gap | Primary source for backup, HA, upgrades, support, and appliance operations |
| [GitHub Enterprise Importer documentation](https://docs.github.com/en/migrations/using-github-enterprise-importer) | Free | About 2–4 hours | Related migration planning and validation; adjacent rather than named exam scope |

No current individual Whizlabs, O'Reilly, or instruction-first Udemy GH-100 course was verified during the August 31, 2026 review. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md) and its selection criteria.
