---
exam_code: AZ-104
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AZ-104 Microsoft Azure Administrator Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official AZ-104 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) is authoritative.

**Current baseline:** Skills measured as of April 17, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)

## How to use this guide

AZ-104 is an implementation and operations exam. Learn each control in three forms: what problem it solves, where it is scoped, and how you would verify or troubleshoot it. Use the portal to discover relationships, then repeat important tasks with Azure CLI, PowerShell, or Bicep so that you understand the resource model rather than memorizing screens.

The objective percentages overlap a real administrator workflow: identity grants authority, governance constrains deployment, networking creates reachability, platform configuration creates behavior, and monitoring plus recovery provide evidence. A scenario may cross several domains.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Operational question |
|---|---:|---|
| Manage Azure identities and governance | 20–25% | Who can do what, at which scope, under which guardrails and cost boundary? |
| Implement and manage storage | 15–20% | How should data be authorized, protected, placed, transferred, and recovered? |
| Deploy and manage Azure compute resources | 20–25% | Which deployment model fits, and how is it configured, scaled, and maintained? |
| Implement and manage virtual networking | 15–20% | Can traffic resolve, route, pass policy, reach the correct endpoint, and return? |
| Monitor and maintain Azure resources | 10–15% | What telemetry proves health, and how will data or service be restored? |

---

# 1. Administrator mental model

## Scope, inheritance, and the resource provider

Keep these boundaries separate:

```text
Microsoft Entra tenant (identity directory)
└── management groups
    └── subscriptions (billing, quota, and management boundary)
        └── resource groups (lifecycle and deployment grouping)
            └── resources and child resources
```

Azure Resource Manager is the management plane. A resource provider exposes resource types such as `Microsoft.Compute/virtualMachines`. A deployment sends desired configuration to a scope; the relevant providers create or update resources. Data-plane operations—reading a blob, querying a database, connecting to a VM—may use separate endpoints and permissions.

This distinction explains common failures: Contributor can create a storage account through the management plane but does not automatically receive permission to read blobs through the data plane. Likewise, a valid data role cannot overcome a storage firewall that blocks the network path.

## A reusable troubleshooting sequence

When an operation fails, do not randomly toggle controls. Work through the dependency chain:

1. **Identity:** Which user, group, service principal, or managed identity is actually making the request?
2. **Token and tenant:** Was the token issued by the expected tenant, for the correct resource, and after the assignment became effective?
3. **Authorization:** Which role, deny assignment, policy, key, or SAS applies at the effective scope?
4. **Name resolution:** Does the name resolve to the intended public or private address?
5. **Route:** Which route is selected in each direction?
6. **Filtering:** Do NSGs, service firewalls, platform access rules, or appliances permit the flow?
7. **Resource state:** Is the target running, healthy, listening, and configured for the requested protocol?
8. **Evidence:** Which activity log, resource log, metric, flow/connectivity result, or guest log confirms the failing layer?

That sequence is more useful than memorizing isolated troubleshooting blades.

---

# 2. Manage Azure identities and governance (20–25%)

## Microsoft Entra identities

Users represent people or synchronized identities; groups make access and licensing manageable; service principals represent application identities in a tenant; managed identities give an Azure resource an identity without the operator storing an application secret.

| Task | Key decision | Verification |
|---|---|---|
| Create or invite a user | Member versus external guest; cloud-only versus synchronized lifecycle | User type, source, sign-in identity, group memberships |
| Manage a group | Security versus Microsoft 365 behavior; assigned versus dynamic membership | Membership processing and effective assignments |
| Assign licenses | Direct versus group-based assignment; service-plan dependencies | License state and assignment errors |
| Configure SSPR | Target group, methods, registration, writeback if hybrid | Test with a scoped non-admin account |

Deleting and restoring a user does not mean every downstream application relationship returns automatically. Know what object is soft-deleted, the recovery window, and which linked credentials, licenses, and application data require separate verification. **VERIFY CURRENT:** licensing, recovery windows, authentication-method availability, and portal names.

## Azure RBAC

An Azure role assignment is:

```text
security principal + role definition + scope
```

- A **role definition** lists allowed and excluded management/data actions.
- A **scope** is normally management group, subscription, resource group, or resource.
- Assignments inherit downward; use the narrowest practical scope.
- A **deny assignment** can block an action even when a role allows it.
- Microsoft Entra directory roles and Azure resource roles govern different planes.

Use the [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) to trace effective access. If a user can view a storage account but cannot list blobs, check for a storage data-plane role. If a recent assignment appears ineffective, renew the token and allow for propagation before changing the design.

> **Related item:** Privileged Identity Management adds eligible, time-bound activation and approval around privileged roles. It is adjacent identity-governance context; AZ-104 still expects you to reason first about the underlying role, scope, and principal.

## Policy, locks, tags, and hierarchy

These controls are complementary:

| Control | What it does | What it does not do |
|---|---|---|
| Azure Policy | Audits, denies, modifies, deploys related configuration, or otherwise evaluates resource compliance | Grant a caller permission |
| Azure RBAC | Authorizes principals to perform actions at scope | Enforce every property value inside an allowed deployment |
| Resource lock | Protects a scope against deletion or modification at the management plane | Protect data-plane operations or replace backup |
| Tag | Adds queryable metadata for ownership, automation, or cost analysis | Inherit automatically in every case without policy/automation |

A policy definition contains a condition and an effect. An initiative groups definitions. An assignment applies a definition or initiative at a scope, optionally with exclusions. `deny` prevents a noncompliant change; `audit` records noncompliance; `modify` and `deployIfNotExists` require a managed identity and remediation to change existing resources. Review current effects in the [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview).

Locks inherit from a parent scope. `CanNotDelete` permits updates but blocks deletion; `ReadOnly` blocks management-plane writes and can have broader consequences than expected. Always test the operation the workload needs.

## Subscriptions, costs, and management groups

Management groups organize subscriptions for inherited policy and RBAC. Subscriptions separate billing, quota, access, and deployment concerns; resource groups usually align resources with a shared lifecycle rather than acting as identity or network boundaries.

Budgets and cost alerts notify; they do not normally stop consumption. Azure Advisor recommendations identify potential cost, reliability, security, operational-excellence, or performance improvements, but an administrator must evaluate workload context. **VERIFY CURRENT:** Advisor categories, supported scopes, cost-management features, and alert delivery behavior.

### Domain failure modes

- Assigning a broad Owner role to solve an access issue instead of locating the missing action.
- Confusing Microsoft Entra roles with Azure RBAC roles.
- Assuming group, role, policy, license, or DNS changes are instantaneous.
- Treating a policy compliance result as proof that a workload is secure.
- Using resource groups as if they were hard security boundaries.
- Applying a ReadOnly lock before checking automation, backup, and monitoring writes.

---

# 3. Implement and manage storage (15–20%)

## Authorization and network access are separate gates

A storage request generally needs all of these:

```text
valid endpoint and DNS
AND permitted network path
AND valid authentication material
AND sufficient data-plane authorization
AND an existing object in an accessible state/tier
```

Storage access options include Microsoft Entra authorization with Azure RBAC, account keys, and shared access signatures (SAS). Prefer identity-based, least-privilege access where supported. Account keys are broad shared secrets. A SAS delegates constrained access by service/resource, permission, time, and optionally network/protocol. A stored access policy can provide a revocation/change point for a service SAS; a user-delegation SAS is authorized through Microsoft Entra credentials.

Regenerate keys deliberately: identify every consumer, move consumers to the alternate key, rotate the old key, and verify. Rotating a key invalidates SAS tokens signed with that key.

## Firewalls, service endpoints, and private endpoints

- A storage firewall controls which networks or addresses may reach the public endpoint.
- A virtual-network service endpoint keeps the service's public endpoint but extends subnet identity to the service.
- A private endpoint creates a private IP in a subnet for the storage subresource.

Private endpoint success depends on DNS. The normal service name must resolve to the private address from the client environment, and each required storage subresource may need its own endpoint/DNS arrangement. Public network access settings remain a separate decision.

## Accounts, redundancy, encryption, and replication

Choose the account type and region first, then redundancy and access characteristics. The [Azure Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction) and [redundancy guide](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) are the current references.

| Redundancy | Failure boundary addressed | Important limitation |
|---|---|---|
| LRS | Copies within one primary-region datacenter | Does not survive a regional or zone-level loss |
| ZRS | Synchronous copies across availability zones in the primary region | No secondary region by itself |
| GRS | Adds asynchronous secondary-region replication | Secondary may not be readable until failover |
| GZRS | ZRS in primary plus geo-replication | Still needs a tested application recovery plan |
| RA-GRS / RA-GZRS | Adds read access to secondary endpoint | Reads may be stale because geo replication is asynchronous |

Storage service encryption protects data at rest. Microsoft-managed keys are the default for many services; customer-managed keys change Key Vault/Managed HSM, identity, availability, and rotation dependencies. Infrastructure encryption is a separate additional layer where supported. **VERIFY CURRENT:** account-type support, region availability, encryption scopes, key-store requirements, and failover behavior.

Object replication asynchronously copies block blobs between accounts. It is not the same as account redundancy, backup, or synchronous application replication.

## Blob and file data protection

| Feature | Protects against / enables | Trap |
|---|---|---|
| Blob versioning | Preserve previous versions after writes | Adds capacity/cost and needs lifecycle policy |
| Soft delete | Recover deleted or overwritten blobs/containers for a retention period | Not immutable and not indefinite |
| Lifecycle management | Move or delete blobs based on rules | Rule effects and timing must be tested |
| Blob access tiers | Trade storage cost for access/retrieval characteristics | Archive rehydration is not immediate |
| File share snapshot | Point-in-time read-only share state | Snapshot capacity and restore workflow matter |
| Azure Files soft delete | Recover deleted shares | Does not replace file-level backup strategy |

Use Storage Explorer for interactive administration and [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) for scripted high-performance transfers. Test authentication, filters, overwrite behavior, checksums, and restart/resume handling before a migration.

### Domain failure modes

- Granting Contributor instead of a blob/file data role.
- Creating a private endpoint without private DNS and client-side resolution tests.
- Treating geo-redundancy as backup against accidental deletion or corruption.
- Issuing a long-lived account SAS with more services and permissions than required.
- Enabling versioning or soft delete without modeling retention cost.
- Moving data to archive without designing rehydration time into the recovery objective.

---

# 4. Deploy and manage compute resources (20–25%)

## ARM templates and Bicep

Declarative deployment describes the desired resource graph; Azure Resource Manager determines ordering from dependencies. Bicep provides a concise language that compiles to ARM JSON. Understand parameters, variables, resource symbolic names, modules, outputs, conditions, loops, existing resources, and scope.

Before deployment, run syntax/build checks and a what-if operation; after deployment, inspect deployment operations rather than only the final error. Exported templates are a discovery aid, not automatically clean reusable infrastructure as code. Remove runtime state, parameterize environment values, review dependencies, and bring the result under source control. See the [Bicep overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview).

## Virtual machines

A VM depends on compute, disks, NICs, networks, identity, extensions, and sometimes load-balancing or availability resources. The [VM overview](https://learn.microsoft.com/en-us/azure/virtual-machines/overview) is the starting reference.

| Requirement | Relevant choice |
|---|---|
| Survive host/rack maintenance domains | Availability set for supported non-zonal designs |
| Survive datacenter-level failure in one region | Multiple availability zones |
| Operate an autoscaled identical fleet | Virtual Machine Scale Sets |
| Protect guest disks from host access | Encryption at host where supported |
| Preserve OS/data independently | Managed disk design, snapshots/backup, and recovery procedure |

Resizing can require a restart and is constrained by regional/cluster capacity. Moving a VM may involve multiple dependent resources and has different procedures for resource-group, subscription, and region moves. A resource move is not a zero-downtime disaster-recovery plan.

Extensions run post-deployment configuration or agents inside the guest. Failure can be caused by guest connectivity, package repositories, identity, handler state, or stale extension configuration. Check instance view and guest logs before repeatedly redeploying.

## Containers and application platforms

| Platform | Use when | Administrator still owns |
|---|---|---|
| Azure Container Registry | Store and govern private container images/artifacts | Identity, networking, image lifecycle, scanning/integration decisions |
| Azure Container Instances | Run isolated containers without an orchestrator | Image, command, ports, environment, secrets, storage, restart behavior |
| Azure Container Apps | Run revisioned microservices/jobs with managed environment and scaling | App configuration, ingress, revisions, scaling rules, identity, observability |
| Azure App Service | Host web apps/APIs on a managed plan | Plan sizing, app configuration, identity, TLS/domains, networking, slots, backup |

Container images are immutable artifacts; environment configuration and secrets should be supplied at deployment. Registry authentication is not the same as application identity. In Container Apps, distinguish an environment from an app, an app from a revision, and traffic splitting from replica scaling. **VERIFY CURRENT:** supported registries, revision modes, KEDA scalers, networking models, quotas, and region availability in the [Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview).

For App Service, the plan supplies regional compute; the app supplies configuration and content. Scale up changes the plan tier/size; scale out changes instance count. Deployment slots are live apps with their own hostnames and configurable slot-specific settings. Warm and validate a slot before swap, and understand which settings move. Custom domains require DNS ownership and certificates; private access, inbound restrictions, and outbound VNet integration solve different network directions. Review the [App Service overview](https://learn.microsoft.com/en-us/azure/app-service/overview).

### Domain failure modes

- Editing a generated ARM template without understanding its resource dependencies.
- Assuming a Bicep deployment deletes resources absent from the file under incremental mode.
- Confusing VM availability, backup, and scale—three different concerns.
- Storing registry passwords or application secrets directly in a template.
- Scaling an App Service app without realizing the plan is the compute boundary.
- Swapping a slot before validating slot-sticky settings, migrations, and health.

---

# 5. Implement and manage virtual networking (15–20%)

## Addressing, subnets, peering, and routes

Plan non-overlapping address spaces with growth and connectivity in mind. Azure reserves addresses in each subnet; do not size only for today's hosts. Some platform services require dedicated or delegated subnets.

VNet peering connects two virtual networks over the Azure backbone, but it is non-transitive: if A peers with B and B peers with C, A does not automatically reach C. Options such as forwarded traffic and gateway transit must match both sides and the routing design. **VERIFY CURRENT:** peering constraints and cross-region support in the [Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview).

Azure selects the most specific route, then applies route-source precedence rules. User-defined routes can send traffic to a virtual appliance, internet, virtual network gateway, or none. Always verify effective routes on the NIC; a correct outbound path is insufficient if return traffic is asymmetric.

## NSGs and application security groups

NSGs are stateful packet filters with prioritized inbound and outbound rules. They can apply to subnets and NICs; traffic must be allowed by every applicable evaluation. Default rules remain unless overridden by a higher-priority custom rule. Application security groups let rules refer to logical application groupings of NICs rather than fixed IP lists.

Use effective security rules to combine inherited/effective NSG evaluation. A rule hit does not prove an application is listening or that the return route works. See the [NSG overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

## Bastion, service endpoints, and private endpoints

Azure Bastion provides managed RDP/SSH connectivity through the portal or supported clients without requiring a public IP on each VM. Its subnet, SKU, routes, NSGs, and target connectivity still matter.

Service endpoints identify a subnet to a supported PaaS service while the service keeps a public endpoint. Private Link/private endpoints map a service subresource to a private IP in the VNet and depend heavily on DNS. Review the [private endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview).

## DNS and load balancing

Azure DNS hosts public zones; Azure Private DNS hosts zones resolvable through linked VNets and hybrid resolver designs. Delegating a public zone requires the registrar/parent nameserver records to match Azure's assigned nameservers. Private DNS auto-registration and VNet links have specific behavior; design hybrid forwarding explicitly.

Azure Load Balancer is a layer-4 service for TCP/UDP flows. Public and internal front ends address different exposure requirements. A rule ties front end, protocol/port, backend pool, and health probe together; outbound behavior is a separate consideration. See [Azure Load Balancer overview](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview).

Troubleshoot load balancing in this order: DNS/front-end address, rule, health probe, backend membership, NSG, guest firewall, listener, route symmetry, then application logs. A failed probe intentionally removes a backend even if the VM itself is running.

### Domain failure modes

- Deploying overlapping address spaces and discovering the conflict during peering or VPN work.
- Assuming peering is transitive.
- Checking an NSG rule but not effective rules, guest firewall, or return route.
- Creating a private endpoint while clients still resolve the public address.
- Blocking a load-balancer health probe or pointing it to a path that requires authentication.
- Confusing inbound private access with outbound VNet integration.

---

# 6. Monitor and maintain Azure resources (10–15%)

## Metrics, logs, alerts, and Insights

Metrics are numeric time-series signals suited to fast aggregation and alerting. Resource logs describe events emitted by a service and often require diagnostic settings to route them to a Log Analytics workspace, storage account, or event destination. The activity log records subscription-level management events. Application and guest telemetry are separate sources.

A robust alert has:

```text
signal + scope + condition + evaluation settings
        + action group + ownership/runbook + suppression/processing policy
```

Action groups define notifications or automation. Alert processing rules modify notification behavior at scale; they do not change the underlying resource condition. Tune dimensions, aggregation, window, frequency, and thresholds to avoid both noise and missed incidents. Use [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/) for current signal support.

Log Analytics uses Kusto Query Language. Start with a bounded time range and relevant table, filter early, then project/summarize. Confirm that diagnostic settings and agents are sending the expected category before debugging the query.

Insights provide curated workbooks and data collection for services such as VMs, storage, and networks. They do not eliminate the need to understand the underlying metrics, logs, and collection rules.

Network Watcher tools answer different questions: topology/effective configuration show state; IP flow verification checks whether NSG evaluation permits a flow; next hop shows route choice; Connection Monitor repeatedly tests reachability and latency across endpoints. **VERIFY CURRENT:** tool names, regional support, agent requirements, pricing, and retirement notices.

## Backup and recovery

Do not collapse these concepts:

| Concept | Purpose |
|---|---|
| Snapshot/version | Point-in-time resource or data state; may share failure/identity boundaries |
| Azure Backup | Policy-driven protected recovery points and restore workflows |
| Azure Site Recovery | Replication, orchestration, failover, and failback for supported workloads |
| Availability | Keep service running through component failure |

Recovery Services vaults and Backup vaults support different workload matrices. A backup policy defines schedule, retention, tiering, and related settings. Soft delete, immutability, multi-user authorization, resource guard, and private access may add defense against destructive operations, but support differs by workload and vault. **VERIFY CURRENT:** use the [Azure Backup overview](https://learn.microsoft.com/en-us/azure/backup/backup-overview) and workload-specific support matrices.

Recovery point objective is acceptable data loss measured in time; recovery time objective is acceptable restoration time. A successful backup job does not prove either. Perform restore tests, validate the application and identity/network dependencies, record timings, and retain evidence.

Site Recovery needs a recovery plan beyond replication: dependency order, network mapping, DNS/routing changes, test-failover isolation, validation, failover criteria, and failback. A test failover should not disrupt production or create duplicate writers.

### Domain failure modes

- Creating an alert without an action group owner or response procedure.
- Querying a table before enabling the required diagnostic setting or agent.
- Treating the activity log as application or guest telemetry.
- Treating a successful backup job as a tested restore.
- Confusing availability-zone placement with regional disaster recovery.
- Running a Site Recovery test failover on a network that can affect production.

---

# 7. Integrated administrator scenarios

## Scenario: private web application

Requirement: deploy a web application that reaches storage privately, is managed by a team, scales safely, and produces actionable evidence.

1. Put the workload in a dedicated resource group with ownership and cost tags.
2. Assign the team the least-privilege Azure role at resource-group scope; give the app a managed identity and only the required storage data role.
3. Use Bicep modules and a what-if review to deploy the plan/app, storage, private endpoint, DNS link, diagnostic settings, and alerts.
4. Disable or restrict public storage access only after the app resolves and reaches the private endpoint.
5. Use an App Service deployment slot for change validation; preserve slot-specific secrets and endpoints.
6. Route metrics and logs to the chosen workspace; alert on health, latency/error signals, and capacity symptoms with owned action groups.
7. Configure workload-appropriate data protection and prove restore steps.

The key is dependency order: locking down the public endpoint before private DNS works creates an outage; assigning Contributor to the application does not grant blob access; deploying an alert without ingestion creates false confidence.

## Scenario: VM connectivity failure

Symptoms: a VM is running, but a client cannot reach TCP 443.

1. Resolve the service name from the client and confirm the expected front-end/private address.
2. If load balanced, confirm backend membership and probe health.
3. Check Connection Monitor or an equivalent test from a meaningful source.
4. Inspect effective routes and effective NSG rules on the NIC/subnet.
5. Confirm the guest firewall and that the application listens on the correct address/port.
6. Check asymmetric paths through appliances, peering, or gateways.
7. Correlate platform metrics and guest/application logs at the failure time.

Do not stop at “the NSG allows 443.” That proves only one layer.

---

# 8. Hands-on labs

Use a disposable subscription or sandbox, apply a budget, and remove billable resources when finished. Record commands, observed IDs, effective settings, failure evidence, and cleanup—not only screenshots of success.

## Lab 1 — Scope and governance

1. Create a resource group with owner, environment, and cost-center tags.
2. Assign a test group Reader, then a narrow operational role; compare effective access.
3. Assign an audit policy, inspect compliance, and create a remediation task if the effect supports it.
4. Add a delete lock and prove which update/delete operations fail.
5. Remove the lock and clean up.

## Lab 2 — Storage authorization and recovery

1. Create a general-purpose storage account and private blob container.
2. Access it using your Entra identity; compare management and data-plane roles.
3. Create a short-lived, least-privilege SAS and verify expiry/permission behavior.
4. Enable versioning and soft delete, overwrite/delete a blob, and recover it.
5. Transfer a test directory with AzCopy and validate the result.

## Lab 3 — Bicep deployment lifecycle

1. Author a Bicep file with parameters, a storage resource, tags, and outputs.
2. Build/lint it, run what-if, and deploy at resource-group scope.
3. Change one property and inspect the deployment operation.
4. Export the deployment template and compare it with the authored Bicep.
5. Deliberately introduce a dependency or validation error and diagnose it from evidence.

## Lab 4 — VM availability and operations

1. Deploy a VM without a public IP and connect through an approved path such as Bastion.
2. Add and initialize a managed data disk.
3. Inspect VM size, availability choice, NIC effective routes, and NSG rules.
4. Configure a managed identity and use it for a supported Azure operation.
5. Capture monitoring evidence, stop/deallocate, and remove resources.

## Lab 5 — App Service safe deployment

1. Create a plan and web app with a staging slot.
2. Configure app settings and mark an environment-specific setting as slot-specific.
3. Configure logging, deploy distinct versions, warm staging, and swap.
4. Verify TLS/custom-domain concepts even if you do not buy a domain.
5. Test scale settings and document which scope they affect.

## Lab 6 — VNet, private endpoint, and DNS

1. Create non-overlapping application and management VNets/subnets and peer them.
2. Add an NSG using an application security group where appropriate.
3. Create a storage private endpoint and the matching private DNS integration.
4. From a test VM, prove the name resolves privately and the service is reachable.
5. Break the DNS link, capture the failure, then restore it.

## Lab 7 — Load balancing and network troubleshooting

1. Deploy two simple backend instances behind an internal or public load balancer.
2. Configure a probe and rule, then verify distribution.
3. Break the probe path or guest listener and observe backend health.
4. Use effective rules/routes and Network Watcher evidence to locate the failure.
5. Repair and document why the first failing layer caused the symptom.

## Lab 8 — Monitoring, alerting, and restore proof

1. Send resource logs to a Log Analytics workspace.
2. Query a bounded interval and summarize a useful operational signal.
3. Create a metric or log alert with an action group and a clear owner.
4. Back up a supported disposable workload, delete/change test data, and restore it.
5. Compare actual recovery time and recovery point with your stated objectives.

---

# 9. Original knowledge checks

1. A user can create a storage account but cannot list blobs. What boundary should you check first? **Answer:** Storage data-plane authorization; management-plane Contributor does not imply a blob data role.
2. A policy assignment uses `deployIfNotExists`, but existing resources remain unchanged. Why? **Answer:** Existing noncompliant resources need remediation, and the assignment identity needs required permissions.
3. Why can a ReadOnly lock break unexpected operations? **Answer:** It blocks management-plane writes at and below scope, including writes performed by some services.
4. A budget reaches 100%. Does Azure automatically stop all resources? **Answer:** No; budgets primarily alert unless separate automation is deliberately implemented.
5. What happens to a SAS signed by an account key after that key rotates? **Answer:** It becomes invalid.
6. What extra dependency commonly breaks a private endpoint deployment? **Answer:** DNS still resolves the normal service name to its public rather than private address.
7. Does GRS protect against an authorized user deleting data that then replicates? **Answer:** Not by itself; use data-protection/backup controls appropriate to the workload.
8. What is the value of a what-if operation? **Answer:** It previews expected resource changes before deployment, subject to documented limitations.
9. Availability zone or Azure Backup: which protects against accidental guest-data deletion? **Answer:** Backup; zones address infrastructure failure, not logical deletion.
10. Does A-to-B and B-to-C peering provide A-to-C reachability? **Answer:** No; VNet peering is not transitive.
11. An NSG allows 443, but traffic fails. Name three other layers. **Answer:** DNS, route/return route, guest firewall/listener; load-balancer health may also apply.
12. What is the difference between an App Service plan and app? **Answer:** The plan supplies regional compute/scale; apps supply hosted application configuration/content on that plan.
13. Scale up versus scale out? **Answer:** Change capacity/tier of instances versus change the number of instances.
14. A load-balancer backend VM is healthy but receives no traffic. First load-balancer-specific check? **Answer:** Health-probe status and probe path/port.
15. Activity log versus resource log? **Answer:** Subscription management-plane events versus service-specific operational/data events.
16. Why can a correct KQL query return nothing? **Answer:** The required data source/category may not be enabled, routed, or within the queried time range.
17. Action group versus alert rule? **Answer:** The rule detects a condition; the action group defines notification/automation targets.
18. Successful backup job versus recovery proof? **Answer:** The job creates a recovery point; only a validated restore demonstrates recoverability and timing.
19. RPO versus RTO? **Answer:** Maximum acceptable data loss in time versus maximum acceptable restoration time.
20. What should every troubleshooting change preserve? **Answer:** The original evidence, a hypothesis, the exact change, observed result, and rollback path.

---

# 10. Readiness checklist

You are approaching readiness when you can:

- trace effective RBAC across principal, role, scope, inheritance, and data-plane differences;
- explain Policy, locks, tags, management groups, budgets, and Advisor without conflating them;
- configure identity-based storage access, SAS, network restrictions, redundancy, and data protection;
- read and modify ARM/Bicep, deploy safely, and diagnose deployment operations;
- choose and operate VMs, scale sets, ACR/ACI/Container Apps, and App Service;
- calculate and troubleshoot VNet/subnet, peering, route, NSG, endpoint, DNS, and load-balancer behavior;
- distinguish metrics, activity/resource/guest logs, diagnostic settings, alerts, and Insights;
- design and prove backup/restore and Site Recovery procedures against RPO/RTO;
- perform the labs without a click-by-click script and explain every security/cost tradeoff;
- score consistently on original scenario questions and explain why every distractor is wrong.

## Primary references

- [Official AZ-104 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- [Azure Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)
- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
- [Azure Virtual Machines overview](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)
- [Azure Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Network security groups overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
- [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/)
- [Azure Backup overview](https://learn.microsoft.com/en-us/azure/backup/backup-overview)

---

# Places to learn

This is a curated starting set, not a complete list. Do **not** consume every resource. Pick one structured spine, use documentation for weak objectives, do the labs, and add one assessment source. Time estimates are planning ranges, not guarantees; playback speed, prior experience, exercises, lab cleanup, and vendor changes matter. Verify the current blueprint before buying or starting a course.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Microsoft Learn AZ-104 course](https://learn.microsoft.com/en-us/training/courses/az-104t00) | Free self-paced; instructor delivery varies | Published: 4 instructor-led days; plan 20–30 hours reading or 30–45 with exercises | Best official objective-aligned spine |
| [Microsoft free Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/?practice-assessment-type=certification) | Free account | Plan 45–90 minutes including review | Baseline and gap finding; not a substitute for labs |
| [John Savill AZ-104 Study Cram v2](https://www.youtube.com/watch?v=0Knf9nub4-k) | Free | Published: about 3.5 hours; plan 4–6 hours with pauses and notes | High-density review after hands-on study; verify changed objectives |
| [Pluralsight AZ-104 certification path](https://www.pluralsight.com/paths/az-104-microsoft-azure-administrator-certification-prep) | Paid/trial or organization access | Published: 36 hours; plan 40–55 hours with eight labs and review | Structured video path with current 2026 domain updates |
| [O'Reilly Exam Ref AZ-104, 2nd Edition](https://www.oreilly.com/library/view/exam-ref-az-104/9780138345990/) | Paid subscription/book | Published: 391 pages / platform estimate 10h 34m; plan 14–22 hours | Objective-organized reference; pair with current docs |
| [O'Reilly/ACI Learning AZ-104 course](https://www.oreilly.com/library/view/microsoft-azure-administrator/9781836206132/video1_1.html) | Paid subscription | Published: 27h 23m; plan 32–45 hours with labs and notes | Detailed video alternative; select weak domains rather than duplicating a full path |
| [Udemy AZ-104 course by Scott Duffy](https://www.udemy.com/course/70533-azure/) | Paid; frequent discounts | Published: 18h 2m; plan 24–35 hours with practice | Current compact video spine; verify outline against blueprint |
| [Whizlabs AZ-104 course, labs, and practice tests](https://www.whizlabs.com/microsoft-azure-certification-az-104/) | Paid; limited samples may be free | Plan 12–25 hours if selecting from 107 videos, 164 labs, and 22 quizzes | Targeted labs and assessment after primary study |
| [MeasureUp AZ-104 assessment](https://www.measureup.com/assessment-az-104-microsoft-azure-administrator.html) | Paid | Plan 1–2 hours for 30 questions and review | Independent readiness check; associated full practice product may differ |

Practice products should contain independently authored questions and explanations, not recalled live-exam content. Use results by objective domain, revisit documentation and labs, then retest with unseen questions.
