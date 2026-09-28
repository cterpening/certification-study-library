---
exam_code: AZ-104
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AZ-104 Microsoft Azure Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-104-coverage-record). The [official AZ-104 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) is authoritative.

**Current baseline:** Skills measured as of April 17, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Official source:** [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)

The September 28 [deep review](../docs/research/2026-09-28-az-104-deep-review.md) maps all **82 detailed objectives in 15 groups**. This edition has seven worked examples, ten labs and 48 explained original checks. The calculations were verified locally; no tenant, cloud resource, deployment, paid lesson or practice assessment was exercised.

The [current credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/) lists **100 minutes**, ten exam languages and annual renewal. Its Practice Assessment and sandbox links are available, but their questions/session were not entered in this review. Confirm appointment details separately from course or practice-product timing.

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

## 1. Administrator mental model

### Scope, inheritance, and the resource provider

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

### A reusable troubleshooting sequence

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

## 2. Manage Azure identities and governance (20–25%)

### Microsoft Entra identities

Users represent people or synchronized identities; groups make access and licensing manageable; service principals represent application identities in a tenant; managed identities give an Azure resource an identity without the operator storing an application secret.

| Task | Key decision | Verification |
|---|---|---|
| Create or invite a user | Member versus external guest; cloud-only versus synchronized lifecycle | User type, source, sign-in identity, group memberships |
| Manage a group | Security versus Microsoft 365 behavior; assigned versus dynamic membership | Membership processing and effective assignments |
| Assign licenses | Direct versus group-based assignment; service-plan dependencies | License state and assignment errors |
| Configure SSPR | Target group, methods, registration, writeback if hybrid | Test with a scoped non-admin account |

Deleting and restoring a user does not mean every downstream application relationship returns automatically. Know what object is soft-deleted, the recovery window, and which linked credentials, licenses, and application data require separate verification. **VERIFY CURRENT:** licensing, recovery windows, authentication-method availability, and portal names.

#### Identity changes need effective-state checks

For a new user, check source of authority, sign-in name, usage location and membership. For an external user, distinguish invitation/redemption from resource authorization; guest status alone grants no Azure role. Changes to synchronized attributes may need to originate in the source directory.

[Group-based license assignment](https://learn.microsoft.com/en-us/entra/identity/users/licensing-groups-assign) is administered in the Microsoft 365 admin center or supported Graph tooling. It does **not** license users through nested-group membership. Check usage location, available licenses, conflicting plans and processing errors. When moving a user, add the destination assignment and verify it is effective before removing the source; membership change is not instantaneous license activation.

[SSPR's current tutorial](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr) separates eligibility, registered methods and a real reset test. Legacy MFA/SSPR method-management policies stopped being the management path on September 30, 2025; use the Authentication methods policy. SSPR can support nested groups even though group licensing cannot. Test a scoped non-admin account, its supported methods and any hybrid writeback prerequisites. Do not infer eligibility from group membership without the required licensing/configuration.

### Azure RBAC

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

### Worked example 1: Exclusion is not an explicit deny

In a simplified action set, role A grants `{read, write, delete}` but excludes `delete`; role B grants `delete`. Their combined allow set is `{read, write, delete}`. An applicable deny assignment for `delete` then reduces effective access to `{read, write}`. [Role definitions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions) distinguish `NotActions`/`NotDataActions` from deny assignments. Real evaluation also needs scope, conditions, identity, locks and the correct plane.

Contributor's lack of a blob data role does not mean its holder can never obtain data: account-key access can provide another path when available and Shared Key is allowed. Inspect effective permissions and the actual credential used; do not use role names alone as a confidentiality guarantee.

> **Related item:** Privileged Identity Management adds eligible, time-bound activation and approval around privileged roles. It is adjacent identity-governance context; AZ-104 still expects you to reason first about the underlying role, scope, and principal.

### Policy, locks, tags, and hierarchy

These controls are complementary:

| Control | What it does | What it does not do |
|---|---|---|
| Azure Policy | Audits, denies, modifies, deploys related configuration, or otherwise evaluates resource compliance | Grant a caller permission |
| Azure RBAC | Authorizes principals to perform actions at scope | Enforce every property value inside an allowed deployment |
| Resource lock | Protects a scope against deletion or modification at the management plane | Protect data-plane operations or replace backup |
| Tag | Adds queryable metadata for ownership, automation, or cost analysis | Inherit automatically in every case without policy/automation |

A policy definition contains a condition and an effect. An initiative groups definitions. An assignment applies a definition or initiative at a scope, optionally with exclusions. `deny` prevents a noncompliant change; `audit` records noncompliance; `modify` and `deployIfNotExists` require a managed identity and remediation to change existing resources. Review current effects in the [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview).

Locks inherit from a parent scope. `CanNotDelete` permits updates but blocks deletion; `ReadOnly` blocks management-plane writes and can have broader consequences than expected. Always test the operation the workload needs.

### Subscriptions, costs, and management groups

Management groups organize subscriptions for inherited policy and RBAC. Subscriptions separate billing, quota, access, and deployment concerns; resource groups usually align resources with a shared lifecycle rather than acting as identity or network boundaries.

Budgets and cost alerts notify; they do not normally stop consumption. Azure Advisor recommendations identify potential cost, reliability, security, operational-excellence, or performance improvements, but an administrator must evaluate workload context. **VERIFY CURRENT:** Advisor categories, supported scopes, cost-management features, and alert delivery behavior.

#### Domain failure modes

- Assigning a broad Owner role to solve an access issue instead of locating the missing action.
- Confusing Microsoft Entra roles with Azure RBAC roles.
- Assuming group, role, policy, license, or DNS changes are instantaneous.
- Treating a policy compliance result as proof that a workload is secure.
- Using resource groups as if they were hard security boundaries.
- Applying a ReadOnly lock before checking automation, backup, and monitoring writes.

---

## 3. Implement and manage storage (15–20%)

### Authorization and network access are separate gates

A storage request generally needs all of these:

```text
valid endpoint and DNS
AND permitted network path
AND valid authentication material
AND sufficient data-plane authorization
AND an existing object in an accessible state/tier
```

Storage access options include Microsoft Entra authorization with Azure RBAC, account keys, and shared access signatures (SAS). Prefer identity-based, least-privilege access where supported. Account keys are broad shared secrets. A SAS delegates constrained access by service/resource, permission, time, and optionally network/protocol. A stored access policy can provide a revocation/change point for a service SAS; a user-delegation SAS is authorized through Microsoft Entra credentials. The [SAS overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) distinguishes these from account SAS: stored access policies do not apply to account or user-delegation SAS. There are at most five stored access policies per resource container. Treat SAS URLs as secrets and plan revocation before distribution; a signature does not bypass network restrictions.

Regenerate keys deliberately: identify every consumer, move consumers to the alternate key, rotate the old key, and verify. Rotating a key invalidates SAS tokens signed with that key.

#### Identity-based Azure Files access

[Azure Files SMB identity authentication](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview) needs a supported identity source, share-level permissions, file/directory permissions, a prepared client and network/DNS reachability. The user identity sources are AD DS, Microsoft Entra Domain Services and Microsoft Entra Kerberos; select one per storage account. Client/identity support differs, including preview combinations. This SMB design is not NFS identity authorization. A successful mount or a share role alone does not prove access to every file. Diagnose ticket acquisition, share permissions and directory ACLs separately.

### Firewalls, service endpoints, and private endpoints

- A storage firewall controls which networks or addresses may reach the public endpoint.
- A virtual-network service endpoint keeps the service's public endpoint but extends subnet identity to the service.
- A private endpoint creates a private IP in a subnet for the storage subresource.

Private endpoint success depends on DNS. The normal service name must resolve to the private address from the client environment, and each required storage subresource may need its own endpoint/DNS arrangement. Public network access settings remain a separate decision.

### Accounts, redundancy, encryption, and replication

Choose the account type and region first, then redundancy and access characteristics. The [Azure Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction) and [redundancy guide](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) are the current references.

| Redundancy | Failure boundary addressed | Important limitation |
|---|---|---|
| LRS | Copies within one primary-region datacenter | Does not survive a regional or zone-level loss |
| ZRS | Synchronous copies across availability zones in the primary region | No secondary region by itself |
| GRS | Adds asynchronous secondary-region replication | Secondary may not be readable until failover |
| GZRS | ZRS in primary plus geo-replication | Still needs a tested application recovery plan |
| RA-GRS / RA-GZRS | Adds read access to secondary endpoint | Reads may be stale because geo replication is asynchronous |

Storage service encryption protects data at rest. Microsoft-managed keys are the default for many services; customer-managed keys change Key Vault/Managed HSM, identity, availability, and rotation dependencies. Infrastructure encryption is a separate additional layer where supported. **VERIFY CURRENT:** account-type support, region availability, encryption scopes, key-store requirements, and failover behavior.

[Object replication](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview) asynchronously copies supported block blobs between accounts. Enable change feed on the source and versioning on both accounts; hierarchical-namespace accounts are unsupported. Source/destination rules share the same policy ID, and both containers must exist. Existing blobs are excluded by default unless the rule includes them. Destination writes are blocked while the replication rule applies. Snapshots are not replicated; index-tag copying is separately marked preview. Archive tier and destination immutability can stop replication. It is not account redundancy or an independent recovery plan.

### Blob and file data protection

When creating a blob container, choose its storage account, name and access level; keep anonymous access disabled unless the application deliberately requires public data. For a file share, choose the supported protocol, account/provisioning model, redundancy, quota/performance settings and authentication path before mounting. Verify a small upload/read and an intentionally denied operation. Blob access tiers and file-share performance/provisioning settings are different controls. Capture transfer source/destination, authentication, overwrite/delete options and completion evidence in Storage Explorer or AzCopy; do not equate “job started” with a verified copy.

| Feature | Protects against / enables | Trap |
|---|---|---|
| Blob versioning | Preserve previous versions after writes | Adds capacity/cost and needs lifecycle policy |
| Soft delete | Recover deleted or overwritten blobs/containers for a retention period | Not immutable and not indefinite |
| Lifecycle management | Move or delete blobs based on rules | Rule effects and timing must be tested |
| Blob access tiers | Trade storage cost for access/retrieval characteristics | Archive rehydration is not immediate |
| File share snapshot | Point-in-time read-only share state | Snapshot capacity and restore workflow matter |
| Azure Files soft delete | Recover deleted shares | Does not replace file-level backup strategy |

Use Storage Explorer for interactive administration and [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) for scripted high-performance transfers. Test authentication, filters, overwrite behavior, checksums, and restart/resume handling before a migration.

### Worked example 2: Undelete does not recreate the current version

With blob versioning and soft delete enabled, write 10 MiB as v1, overwrite with another 10 MiB as v2, then delete the blob. The versions remain, but there is **no current version**. Undelete restores soft-deleted versions/snapshots; it does not promote a version to current. Copy the chosen previous version to the current blob and verify its content. If a toy full-copy model counts v1, v2 and a new restored version, it holds 30 MiB. That arithmetic is not an Azure billing estimate; actual stored blocks, snapshots and operations matter. See [soft-delete/versioning behavior](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview).

Previous versions do not expire merely because a blob soft-delete period elapsed. Configure appropriate version lifecycle rules. Blob soft delete does not restore a deleted container or storage account; container protection and account recovery/backup boundaries are separate. Versioning is not supported on hierarchical-namespace accounts.

[Lifecycle management](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview) is periodic: changes can take up to 24 hours before a run starts, and a run can take longer to finish. Deleting the policy does not cancel an active run; disable rules first if stopping future actions is the intent. Rules cannot rehydrate archive blobs. Prefix/tag filters combine with AND, and policy writes replace the full policy rather than patching a single rule. Test a narrow disposable prefix before expanding scope.

#### Domain failure modes

- Granting Contributor instead of a blob/file data role.
- Creating a private endpoint without private DNS and client-side resolution tests.
- Treating geo-redundancy as backup against accidental deletion or corruption.
- Issuing a long-lived account SAS with more services and permissions than required.
- Enabling versioning or soft delete without modeling retention cost.
- Moving data to archive without designing rehydration time into the recovery objective.

---

## 4. Deploy and manage compute resources (20–25%)

### ARM templates and Bicep

Declarative deployment describes the desired resource graph; Azure Resource Manager determines ordering from dependencies. Bicep provides a concise language that compiles to ARM JSON. Understand parameters, variables, resource symbolic names, modules, outputs, conditions, loops, existing resources, and scope.

Before deployment, run syntax/build checks and a what-if operation; after deployment, inspect deployment operations rather than only the final error. Exported templates are a discovery aid, not automatically clean reusable infrastructure as code. Remove runtime state, parameterize environment values, review dependencies, and bring the result under source control. See the [Bicep overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview).

#### Incremental deployment is not a property patch

[ARM deployment modes](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-modes) distinguish omitted **resources** from omitted **properties**. Incremental mode preserves other resources, but re-applies the declared resource's full configuration; omitted nondefault properties can reset. Review VNet subnet and web-app child configuration carefully. Complete mode is not recommended; current guidance directs template-driven deletions to deployment stacks. A what-if preview is useful evidence, not a guarantee that later deployment will succeed.

For [JSON-to-Bicep conversion](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile), `az bicep decompile --file main.json` produces `main.bicep`. Review warnings, names, API versions, parameters and dependencies, then build and inspect what-if before deploying. Conversion can require repairs and does not produce text-identical JSON on a round trip. Exporting live resources is not a backup of their data or secrets.

### Virtual machines

A VM depends on compute, disks, NICs, networks, identity, extensions, and sometimes load-balancing or availability resources. The [VM overview](https://learn.microsoft.com/en-us/azure/virtual-machines/overview) is the starting reference.

| Requirement | Relevant choice |
|---|---|
| Survive host/rack maintenance domains | Availability set for supported non-zonal designs |
| Survive datacenter-level failure in one region | Multiple availability zones |
| Operate an autoscaled identical fleet | Virtual Machine Scale Sets |
| Encrypt host-resident disk data and caches at rest | Encryption at host on supported VM sizes |
| Preserve OS/data independently | Managed disk design, snapshots/backup, and recovery procedure |

Resizing can require a restart and is constrained by regional/cluster capacity. Moving a VM may involve multiple dependent resources and has different procedures for resource-group, subscription, and region moves. A resource move is not a zero-downtime disaster-recovery plan.

[Encryption at host](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-enable-host-based-encryption-portal) covers host-resident temporary/ephemeral disk data and OS/data disk caches, with encrypted flow to storage. This does not establish confidential-computing isolation of a running guest from the host. Check subscription feature registration and supported sizes. VMs/scale sets that currently or previously used Azure Disk Encryption cannot simply enable it; existing scale-set instances need deallocation/reallocation after enabling the setting. Disk/customer-managed-key dependencies and recovery remain separate.

For moves, inventory disks, NICs, public IPs, extensions, identities, role assignments, quota and provider registration. Resource-group/subscription relocation and region migration have different support paths; do not assume that moving a resource ID relocates its data to another region. For VM scale sets, record orchestration mode, image, upgrade policy, health signal, minimum/maximum/default capacity and scale-in behavior; fleet creation alone does not configure application health or safe upgrades.

Extensions run post-deployment configuration or agents inside the guest. Failure can be caused by guest connectivity, package repositories, identity, handler state, or stale extension configuration. Check instance view and guest logs before repeatedly redeploying.

### Containers and application platforms

| Platform | Use when | Administrator still owns |
|---|---|---|
| Azure Container Registry | Store and govern private container images/artifacts | Identity, networking, image lifecycle, scanning/integration decisions |
| Azure Container Instances | Run isolated containers without an orchestrator | Image, command, ports, environment, secrets, storage, restart behavior |
| Azure Container Apps | Run revisioned microservices/jobs with managed environment and scaling | App configuration, ingress, revisions, scaling rules, identity, observability |
| Azure App Service | Host web apps/APIs on a managed plan | Plan sizing, app configuration, identity, TLS/domains, networking, slots, backup |

Container images are immutable artifacts; environment configuration and secrets should be supplied at deployment. Registry authentication is not the same as application identity. In Container Apps, distinguish an environment from an app, an app from a revision, and traffic splitting from replica scaling. **VERIFY CURRENT:** supported registries, revision modes, KEDA scalers, networking models, quotas, and region availability in the [Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview).

For ACR, check the registry's permission mode before copying old lab roles. In [RBAC + ABAC repository mode](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-rbac-abac-repository-permissions), legacy `AcrPull`/`AcrPush`/`AcrDelete` are not honored. Use the corresponding Repository Reader/Writer/Contributor roles, optionally scoped with conditions. Registry control-plane access and image access are different. Assign/test replacement roles before changing an existing registry's mode.

For ACI, specify group/container CPU and memory, port/listener, restart policy and persistence; a restarted container does not guarantee durable local data. For Container Apps, independently configure CPU/memory, minimum/maximum replicas and a suitable event/HTTP scaling rule. A revision's traffic percentage is not its replica count. Test idle, burst, failed-start and scale-in behavior against service/region limits.

For App Service, the plan supplies regional compute; the app supplies configuration and content. Scale up changes the plan tier/size; scale out changes instance count. Deployment slots are live apps with their own hostnames and configurable slot-specific settings. Warm and validate a slot before swap, and understand which settings move. Custom domains require DNS ownership and certificates; private access, inbound restrictions, and outbound VNet integration solve different network directions. Review the [App Service overview](https://learn.microsoft.com/en-us/azure/app-service/overview).

#### App Service boundaries worth testing

- **Slots:** Standard/Premium/Isolated plans support slots. [Slot swaps](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) do not swap managed identities, custom domains or VNet integration; several other settings are sticky by default. Private endpoints are not cloned with slot configuration. Validate each slot's identity/network permissions, use production as the target, and account for worker recycling/long-running operations. Swapping back does not undo a database migration.
- **Certificates:** a free [managed certificate](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate) is not exportable and does not support wildcard or private-DNS scenarios. DNS ownership, the certificate and the hostname binding are distinct checks. Current [certificate-change guidance](https://learn.microsoft.com/en-us/azure/app-service/industry-wide-certificate-changes) gives paid ASC certificates a 198-day validity/validation-reuse period from March 2026. App Service manages overlapping issuance for its own bindings; exported copies still need updating, and ASC domain revalidation is not automatic. Inspect issuer/chain/EKU assumptions. Removal of client-authentication EKU from these server certificates does not mean App Service removed all mTLS support.
- **Backups:** [automatic app backups](https://learn.microsoft.com/en-us/azure/app-service/manage-backup) differ from custom backups: current limits are 30 GB versus 10 GB, and automatic backups exclude linked databases. Custom backups use a SAS-capable storage account, not managed-identity authentication. Flexible Server linked databases are unsupported, and linked-database custom backups are scheduled to end March 31, 2028. Use the database's recovery tools and verify both app and data. Restoring over an existing app/slot overwrites its filesystem.

### Worked example 3: Plan capacity includes staging work

For a fictional three-instance plan, each worker has 8 GiB; treat capacity **per worker**, not as one 24-GiB pool. If production uses 5 GiB and a warmed staging slot uses 2 GiB on each worker, 7 GiB is already occupied before other workloads/overhead. A further 2-GiB app would need 9 GiB per worker and exceed this simplified budget. Scale-out adds workers but does not automatically reduce every app's fixed per-worker footprint. Measure real memory, CPU and routing behavior; these numbers are not an App Service SKU specification.

#### Domain failure modes

- Editing a generated ARM template without understanding its resource dependencies.
- Assuming a Bicep deployment deletes resources absent from the file under incremental mode.
- Confusing VM availability, backup, and scale—three different concerns.
- Storing registry passwords or application secrets directly in a template.
- Scaling an App Service app without realizing the plan is the compute boundary.
- Swapping a slot before validating slot-sticky settings, migrations, and health.

---

## 5. Implement and manage virtual networking (15–20%)

### Addressing, subnets, peering, and routes

Plan non-overlapping address spaces with growth and connectivity in mind. Azure reserves addresses in each subnet; do not size only for today's hosts. Some platform services require dedicated or delegated subnets.

VNet peering connects two virtual networks over the Azure backbone, but it is non-transitive: if A peers with B and B peers with C, A does not automatically reach C. Options such as forwarded traffic and gateway transit must match both sides and the routing design. **VERIFY CURRENT:** peering constraints and cross-region support in the [Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview).

Azure selects the most specific route, then applies route-source precedence rules. User-defined routes can send traffic to a virtual appliance, internet, virtual network gateway, or none. Always verify effective routes on the NIC; a correct outbound path is insufficient if return traffic is asymmetric.

### Worked example 4: Subnet headroom and explicit outbound access

A /27 has 32 IPv4 addresses; Azure's five reservations leave **27**. A design requiring 24 addresses now plus four for growth needs 28 and does not fit. A /26 leaves **59**, with 31 spare after that 28-address requirement. Check each service's dedicated/delegated subnet minimum and extra capacity needs; arithmetic alone does not make a subnet valid. The [VNet FAQ](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-faq) documents the reservations.

[Default outbound guidance](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access) now makes new VNet subnets private by default for API versions released after March 31, 2026; the portal already defaults this way. Existing VNets are not automatically changed, and earlier API versions can retain earlier behavior. Verify `defaultOutboundAccess` and the actual deployment API/configuration. Configure NAT Gateway, appropriate Standard Load Balancer outbound rules or a controlled firewall/NVA path when public egress is needed. An NSG allow rule does not create an outbound translation method. A private subnet still needs routes/DNS/permissions for private destinations.

### NSGs and application security groups

A [public IP](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses) is its own resource. Choose a supported SKU, region, zone configuration and IP version compatible with its consumer, then verify its association and DNS separately. Standard public IPs use static allocation and require an allowed inbound path; the address alone does not open a port. Basic public IPs retired September 30, 2025. The public-IP overview's general implicit-egress description must be read alongside the newer private-subnet/default-outbound rules above.

NSGs are stateful packet filters with prioritized inbound and outbound rules. They can apply to subnets and NICs; traffic must be allowed by every applicable evaluation. Default rules remain unless overridden by a higher-priority custom rule. Application security groups let rules refer to logical application groupings of NICs rather than fixed IP lists.

Use effective security rules to combine inherited/effective NSG evaluation. A rule hit does not prove an application is listening or that the return route works. See the [NSG overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

### Bastion, service endpoints, and private endpoints

Azure Bastion provides managed RDP/SSH connectivity through the portal or supported clients without requiring a public IP on each VM. Its subnet, SKU, routes, NSGs, and target connectivity still matter.

Service endpoints identify a subnet to a supported PaaS service while the service keeps a public endpoint. Private Link/private endpoints map a service subresource to a private IP in the VNet and depend heavily on DNS. Review the [private endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview).

### DNS and load balancing

Azure DNS hosts public zones; Azure Private DNS hosts zones resolvable through linked VNets and hybrid resolver designs. Delegating a public zone requires the registrar/parent nameserver records to match Azure's assigned nameservers. Private DNS auto-registration and VNet links have specific behavior; design hybrid forwarding explicitly.

Azure Load Balancer is a layer-4 service for TCP/UDP flows. Public and internal front ends address different exposure requirements. A rule ties front end, protocol/port, backend pool, and health probe together; outbound behavior is a separate consideration. See [Azure Load Balancer overview](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview).

Troubleshoot load balancing in this order: DNS/front-end address, rule, health probe, backend membership, NSG, guest firewall, listener, route symmetry, then application logs. A failed probe normally removes a backend from new-flow selection even if the VM itself is running; inspect any configured administrative-state override. Basic Load Balancer retired on September 30, 2025. Use current supported SKUs and explicitly verify outbound behavior instead of copying a legacy Basic design.

#### Domain failure modes

- Deploying overlapping address spaces and discovering the conflict during peering or VPN work.
- Assuming peering is transitive.
- Checking an NSG rule but not effective rules, guest firewall, or return route.
- Creating a private endpoint while clients still resolve the public address.
- Blocking a load-balancer health probe or pointing it to a path that requires authentication.
- Confusing inbound private access with outbound VNet integration.

---

## 6. Monitor and maintain Azure resources (10–15%)

### Metrics, logs, alerts, and Insights

Metrics are numeric time-series signals suited to fast aggregation and alerting. Resource logs describe events emitted by a service and often require diagnostic settings to route them to a Log Analytics workspace, storage account, or event destination. The activity log records subscription-level management events. Application and guest telemetry are separate sources.

A robust alert has:

```text
signal + scope + condition + evaluation settings
        + action group + ownership/runbook + suppression/processing policy
```

Action groups define notifications or automation. Alert processing rules modify notification behavior at scale; they do not change the underlying resource condition. Tune dimensions, aggregation, window, frequency, and thresholds to avoid both noise and missed incidents. Use [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/) for current signal support.

Log Analytics uses Kusto Query Language. Start with a bounded time range and relevant table, filter early, then project/summarize. Confirm that diagnostic settings and agents are sending the expected category before debugging the query.

Insights provide curated workbooks and data collection for services such as VMs, storage, and networks. They do not eliminate the need to understand the underlying metrics, logs, and collection rules.

For a workspace receiving subscription activity events, this bounded query uses the documented [AzureActivity schema](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/azureactivity):

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
| summarize Events=count() by bin(TimeGenerated, 5m), ActivityStatusValue
```

This counts **events**, not unique operations: one operation can emit started and completed events. Use the operation/correlation identifiers and a defined completion rule for an operation-success report. An empty table can mean missing collection or the wrong time/scope. This query was reviewed as an example and was not executed against a workspace.

Network Watcher tools answer different questions: topology/effective configuration show state; IP flow verification checks whether NSG evaluation permits a flow; next hop shows route choice; Connection Monitor repeatedly tests reachability and latency across endpoints. **VERIFY CURRENT:** tool names, regional support, agent requirements, pricing, and retirement notices.

#### Collection coverage is part of alert meaning

[Azure Monitor Agent](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-overview) needs associated data collection rules specifying sources, processing and destinations. Installing an extension alone does not establish guest-log ingestion. Verify a known fixture in the intended table/time range, permissions and ingestion delay. A service diagnostic setting is a separate collection mechanism.

[NSG flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-overview) no longer permit new creation and retire September 30, 2027. Plan new collection with virtual network flow logs. Retirement of NSG flow-log resources does not itself delete historical storage records; their retention still applies. Flow records, Connection Monitor and guest/application telemetry answer different questions.

### Worked example 5: Missing machines and misleading averages

Five VMs should emit guest telemetry, but only four do: **80% collection coverage**. A healthy average for those four says nothing about the missing VM. Separately, service A fails 10 of 100 requests and B fails 1 of 10: both have 10% failure, so the combined rate is 11/110 = 10%. If B instead fails 1 of 1, averaging 10% and 100% gives 55%, while the request-weighted total is **11/101 = 10.89%**. Use the correct denominator, dimensions and missing-data policy; report coverage alongside health.

### Backup and recovery

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

### Worked example 6: Recovery success can miss both objectives

An incident occurs at 12:00. The selected application-consistent point is 11:42, so observed data loss is **18 minutes**, exceeding a 15-minute RPO. Decision/startup takes 8 minutes, restoration 55 and application validation 12: service recovery takes **75 minutes**, exceeding a 60-minute RTO. A completed restore job alone would hide both failures. Include identity, DNS, dependencies and user acceptance in the timeline.

For an [Azure-to-Azure Site Recovery drill](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill), choose an isolated non-production network and record the selected recovery point. “Latest processed” avoids additional processing delay; “Latest” processes received data before failover; app-consistent recovery points address a different consistency requirement. Validate the recovered application and clean up the test through Site Recovery after recording findings. A test VM that starts is not full recovery proof.

### Worked example 7: Retention and immutability can have different ends

[Immutable-vault guidance](https://learn.microsoft.com/en-us/azure/backup/backup-azure-immutable-vault-concept) distinguishes reversible **Enabled** from irreversible **Enabled and locked**. Recovery Services vaults can also use a fixed immutability duration; Backup vaults use policy-based duration. For a fictional 120-day retention and 45-day fixed immutability setting, a point at age 50 days has 70 days of scheduled retention left but is outside its immutability window. Retention alone is not a deletion prohibition.

Check [vault configuration guidance](https://learn.microsoft.com/en-us/azure/backup/backup-azure-immutable-vault-how-to-manage) before locking: a fixed duration is also locked, and retention cannot be reduced below that configured duration. Immutability does not apply to operational backups of blobs/files/disks. Distinguish service-enforced locked immutability from underlying WORM availability, which varies by vault/workload/region. Test the retention design while reversible; these study labs do not ask you to lock a production vault.

#### Domain failure modes

- Creating an alert without an action group owner or response procedure.
- Querying a table before enabling the required diagnostic setting or agent.
- Treating the activity log as application or guest telemetry.
- Treating a successful backup job as a tested restore.
- Confusing availability-zone placement with regional disaster recovery.
- Running a Site Recovery test failover on a network that can affect production.

---

## 7. Integrated administrator scenarios

### Scenario: private web application

Requirement: deploy a web application that reaches storage privately, is managed by a team, scales safely, and produces actionable evidence.

1. Put the workload in a dedicated resource group with ownership and cost tags.
2. Assign the team the least-privilege Azure role at resource-group scope; give the app a managed identity and only the required storage data role.
3. Use Bicep modules and a what-if review to deploy the plan/app, storage, private endpoint, DNS link, diagnostic settings, and alerts.
4. Disable or restrict public storage access only after the app resolves and reaches the private endpoint.
5. Use an App Service deployment slot for change validation; preserve slot-specific secrets and endpoints.
6. Route metrics and logs to the chosen workspace; alert on health, latency/error signals, and capacity symptoms with owned action groups.
7. Configure workload-appropriate data protection and prove restore steps.

The key is dependency order: locking down the public endpoint before private DNS works creates an outage; assigning Contributor to the application does not grant blob access; deploying an alert without ingestion creates false confidence.

### Scenario: VM connectivity failure

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

### Two blog exercises

- [Routing options for VMs from private subnets](https://techcommunity.microsoft.com/blog/azurenetworkingblog/routing-options-for-vms-from-private-subnets/4271244), Microsoft author `ulkeba`, October 20, 2024: use the introduction and first two scenarios to draw three paths—public internet, ARM management and a service data endpoint. Predict DNS, route, source address and required authorization before testing. **Its September 2025 timeline is outdated**; use current default-outbound documentation above. The full Terraform sample was not audited or run.
- [App Service certificate changes](https://techcommunity.microsoft.com/blog/appsonazureblog/industry-wide-certificate-changes-impacting-azure-app-service-certificates/4477924), Microsoft author `YutangLin`, December 15, 2025, with a February 17, 2026 update: inventory certificate type, binding, export consumer, validation owner, issuer/chain and client-auth dependency. Build a renewal evidence checklist. The linked current Learn article takes precedence, including 198-day ASC validity; do not apply the blog's broad “no action” wording to exported copies or pending domain validation.

These original worksheets apply selected public articles to administrator decisions. They are not additional exam objectives or evidence that the cloud samples were executed.

## 8. Hands-on labs

Use a disposable subscription or sandbox, apply a budget, and remove billable resources when finished. A budget alerts; it does not cap charges. Record skipped/failed cases and permissions as well as success. Record commands, observed IDs, effective settings, failure evidence, and cleanup—not only screenshots of success.

### Lab 1 — Scope and governance

1. Create a resource group with owner, environment, and cost-center tags.
2. Assign a test group Reader, then a narrow operational role; compare effective access.
3. Assign an audit policy and inspect compliance; separately test a modify/deployIfNotExists policy with the required assignment identity and remediation permission.
4. Add a delete lock and prove which update/delete operations fail.
5. Remove the lock and clean up.

### Lab 2 — Storage authorization and recovery

1. Create a general-purpose storage account and private blob container.
2. Access it using your Entra identity; compare management and data-plane roles.
3. Create a short-lived, least-privilege SAS and verify expiry/permission behavior.
4. Enable versioning and soft delete, overwrite/delete a blob, then promote a chosen version to current and verify its content. Explain container/account recovery boundaries.
5. Transfer a test directory with AzCopy and validate the result.

### Lab 3 — Bicep deployment lifecycle

1. Author a Bicep file with parameters, a storage resource, tags, and outputs.
2. Build/lint it, run what-if, and deploy at resource-group scope.
3. Change one property and inspect the deployment operation.
4. Export the deployment template and compare it with the authored Bicep.
5. Deliberately introduce a dependency or validation error and diagnose it from evidence.

### Lab 4 — VM availability and operations

1. Deploy a VM without a public IP and connect through an approved path such as Bastion.
2. Add and initialize a managed data disk.
3. Inspect VM size, availability choice, NIC effective routes, and NSG rules.
4. Configure a managed identity and use it for a supported Azure operation.
5. Capture monitoring evidence, stop/deallocate, and remove resources.

### Lab 5 — App Service safe deployment

1. Create a plan and web app with a staging slot.
2. Configure app settings and mark an environment-specific setting as slot-specific.
3. Configure logging, deploy distinct versions, warm staging, and swap.
4. Verify TLS/custom-domain concepts even if you do not buy a domain.
5. Test scale settings and document which scope they affect.

### Lab 6 — VNet, private endpoint, and DNS

1. Create non-overlapping application and management VNets/subnets and peer them.
2. Add an NSG using an application security group where appropriate.
3. Create a storage private endpoint and the matching private DNS integration.
4. From a test VM, prove the name resolves privately and the service is reachable.
5. Break the DNS link, capture the failure, then restore it.

### Lab 7 — Load balancing and network troubleshooting

1. Deploy two simple backend instances behind an internal or public load balancer.
2. Configure a supported load-balancer SKU, probe and rule, then verify distribution and explicit outbound access separately.
3. Break the probe path or guest listener and observe backend health.
4. Use effective rules/routes and Network Watcher evidence to locate the failure.
5. Repair and document why the first failing layer caused the symptom.

### Lab 8 — Monitoring, alerting, and restore proof

1. Send resource logs to a Log Analytics workspace.
2. Query a bounded interval and summarize a useful operational signal.
3. Create a metric or log alert with an action group and a clear owner.
4. Back up a supported disposable workload, delete/change test data, and restore it.
5. Compare actual recovery time and recovery point with your stated objectives.

### Lab 9 — Identity, licensing and container boundaries

1. In an authorized test tenant, create a member and invite a guest; record source, usage location, group membership and separate resource authorization.
2. Compare direct/nested group licensing and SSPR scope; verify effective license state and a non-admin reset without touching production identities.
3. Create a disposable ACR, select its permissions mode and test a least-privilege image pull; explain why a registry management role can fail to pull.
4. Run a harmless image in ACI and Container Apps; compare sizing, restart behavior, ingress, revisions, scaling and logs.
5. Record expected/observed failure cases, consumed resources and cleanup.

### Lab 10 — Recovery plan and certificate inventory

1. Design a backup policy with explicit workload, vault, retention, immutability mode, recovery point and restore destination. Keep experimental immutability reversible.
2. Run a permitted isolated Site Recovery test failover, validate dependencies, record timing and use test cleanup. A paper plan must be labeled unexecuted.
3. Inventory a disposable web app's certificate, hostname binding, DNS validation and renewal path; distinguish managed, purchased/imported and exported copies.
4. Document database-native recovery beside app recovery. Compare observed RPO/RTO with targets and list the unresolved gaps.

---

## 9. Original knowledge checks

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


21. Does NotActions override another role that permits the same action? **Answer:** No. It subtracts from that role only; an applicable deny assignment is a separate restriction.

22. Does group licensing expand nested membership like SSPR can? **Answer:** No. Check the feature-specific membership rules instead of treating every group consumer identically.

23. What order reduces licensing gaps during a group move? **Answer:** Add the destination, verify the license is effective, then remove the source assignment.

24. Which policy now manages SSPR authentication methods? **Answer:** The Authentication methods policy; legacy MFA/SSPR method management ended September 30, 2025.

25. Does invitation redemption make a guest an Azure resource administrator? **Answer:** No. Directory membership and scoped resource permissions remain separate.

26. Can an account or user-delegation SAS use a stored access policy? **Answer:** No. That revocation mechanism belongs to a service SAS; plan other expiry/revocation controls for the selected type.

27. An SMB share role exists but a file is denied. What else must you inspect? **Answer:** Identity/ticket, file and directory ACLs, client support, network and DNS.

28. What does blob object replication require? **Answer:** Supported block blobs/accounts, source change feed, versioning on both sides and matching rules/policy IDs; it is asynchronous.

29. Does Undelete Blob restore a current version when versioning is enabled? **Answer:** No. Recover soft-deleted versions if necessary, then promote the chosen version by copying it to current.

30. Does soft-delete expiry automatically purge all previous versions? **Answer:** No. Previous versions need explicit deletion or appropriate lifecycle rules.

31. Can a lifecycle rule rehydrate archive data or guarantee deletion at an exact minute? **Answer:** Neither. Rehydration needs a separate supported operation, and lifecycle evaluation is periodic.

32. Does incremental ARM deployment preserve omitted properties on a declared resource? **Answer:** Do not assume so. It reapplies the resource configuration; omitted nondefault properties can reset.

33. Is decompiled Bicep immediately ready for production? **Answer:** No. Inspect conversion warnings, dependencies and parameters, build and review what-if, then validate an actual deployment.

34. Does encryption at host prove confidential isolation of running guest memory? **Answer:** No. It encrypts host-resident disk data/caches and the disk data path; confidential-computing guarantees are separate.

35. Can AcrPull be assumed valid after switching an ACR to ABAC repository mode? **Answer:** No. Use applicable Repository roles and test their conditions before switching.

36. Does an app slot swap carry its managed identity and VNet integration to production? **Answer:** No. Validate the identity/network contract of each slot separately.

37. Can a free App Service managed certificate be exported for another host? **Answer:** No. It is nonexportable; choose a suitable different certificate workflow for that requirement.

38. Does automated ASC issuance update every exported copy or validate every domain automatically? **Answer:** No. Export consumers need updates and ASC ownership revalidation may be required.

39. Does removal of clientAuth EKU from these public server certificates remove App Service mTLS entirely? **Answer:** No. It limits using those certificates for client authentication; examine a supported client-certificate design separately.

40. Does an automatic app backup include its linked database? **Answer:** No. Use and test the database recovery mechanism; also note custom-backup database support and retirement limits.

41. Can a three-worker 8-GiB plan treat a 9-GiB per-worker workload as fitting inside 24 GiB? **Answer:** No. Each worker exceeds its own 8-GiB budget. Measure actual placement and demand.

42. Will 24 addresses plus four for growth fit in an Azure /27 subnet? **Answer:** No. Five reserved addresses leave 27; a /26 leaves 59 before service-specific constraints.

43. Did March 2026 change every existing VNet to private subnets automatically? **Answer:** No. Scope depends on new-VNet API/default behavior and actual subnet settings.

44. Does permitting outbound HTTPS in an NSG provide internet egress for a private subnet? **Answer:** No. It permits a flow; routing and an explicit outbound connectivity method must also exist.

45. Should a new lab create NSG flow logs or use Basic Load Balancer? **Answer:** No. New NSG flow-log creation is unavailable and Basic Load Balancer has retired; choose supported alternatives.

46. Is installing Azure Monitor Agent enough to prove guest telemetry coverage? **Answer:** No. Check DCR associations, configured data sources/destinations and actual ingested fixtures.

47. Does 98% health from reporting machines establish fleet health if some machines are silent? **Answer:** No. Report collection coverage and missing-machine outcomes separately.

48. Does a retained recovery point always remain immutable for its full retention? **Answer:** Not with a shorter supported fixed immutability duration. Check the selected vault mode and age, and distinguish locked configuration from retention.
---

## 10. Readiness checklist

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

### Primary references

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

## Places to learn

This is a curated starting set, not a complete list. Do **not** consume every resource. Pick one structured spine, use documentation for weak objectives, do the labs, and add one assessment source. Time estimates are planning ranges, not guarantees; playback speed, prior experience, exercises, lab cleanup, and vendor changes matter. Verify the current blueprint before buying or starting a course.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Microsoft Learn AZ-104 course](https://learn.microsoft.com/en-us/training/courses/az-104t00) | Free self-paced; instructor delivery varies | Published: 4 instructor-led days; plan 20–30 hours reading or 30–45 with exercises | Best official objective-aligned spine |
| [Microsoft free Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/?practice-assessment-type=certification) | Free account | Plan 45–90 minutes including review | Baseline and gap finding; not a substitute for labs |
| [John Savill AZ-104 Study Cram v2](https://www.youtube.com/watch?v=0Knf9nub4-k) | Free | Historical estimate: about 3.5 hours; current runtime unverified | Video shell only in this pass; useful as a retained review reference after labs, with current objectives checked separately |
| [Pluralsight AZ-104 certification path](https://www.pluralsight.com/paths/az-104-microsoft-azure-administrator-certification-prep) | Paid/trial or organization access | Six courses: 29h47; eight labs: 5h; 34h47 total, rounded to 35h in the header | September 9 identity/storage and September 23 networking updates. An introductory paragraph still has old weights; use the official blueprint. Budget 40–55 hours with review (editorial estimate) |
| [O'Reilly Exam Ref AZ-104, 2nd Edition](https://www.oreilly.com/library/view/exam-ref-az-104/9780138345990/) | Paid subscription/book | Published: 391 pages / platform estimate 10h 34m; plan 14–22 hours | Charles Pluta, July 2024; indexed outline/metadata only, direct access blocked. Pair with current docs; book not read in this review |
| [O'Reilly/ACI Learning AZ-104 course](https://www.oreilly.com/library/view/microsoft-azure-administrator/9781836206132/video1_1.html) | Paid subscription | Published: 27h 23m; plan 32–45 hours with labs and notes | ACI Learning/Adam Gordon, May 2024; indexed public outline only. Older Azure AD/ADE and AKS content needs current-scope filtering; paid lessons not watched |
| [Udemy AZ-104 course by Scott Duffy](https://www.udemy.com/course/70533-azure/) | Paid; frequent discounts | Published: 18h 2m; plan 24–35 hours with practice | Scott Duffy, June 2026; indexed outline lists 26 sections/187 lectures. Direct access blocked; lesson accuracy and practice originality unverified |
| [Whizlabs AZ-104 course, labs, and practice tests](https://www.whizlabs.com/microsoft-azure-certification-az-104/) | Paid; limited samples may be free | Current bundle counts/runtime unverified | Product retrieval exposes only a title shell; earlier 107-video/164-lab/22-quiz counts not reproduced. Confirm current entitlements before purchase |
| [MeasureUp AZ-104 assessment](https://www.measureup.com/assessment-az-104-microsoft-azure-administrator.html) | Paid | Plan 1–2 hours for 30 questions and review | June 2026 listing: 30 questions drawn from its associated practice test, with **no explanations or references**. This assessment-only product is not an explanation-based learning course |

Catalog metadata is not proof of lesson accuracy, exam coverage or question originality. Provider discovery was bounded and paid content was not inspected. Prefer independently authored learning questions with explanations; the listed MeasureUp assessment explicitly omits them. Avoid recalled live-exam material. Use results by objective domain, revisit documentation and labs, then retest with unseen questions.
