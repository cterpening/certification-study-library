---
exam_code: AZ-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AZ-900 Microsoft Azure Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-900-coverage-record). The [official AZ-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) is authoritative.

**Current baseline:** Skills measured as of July 20, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Official source:** [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)

**September 28 deep review:** All 57 detailed objectives remain on the July 20 baseline. The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/?practice-assessment-type=certification) lists a 45-minute assessment in 13 languages. Earned fundamentals certifications [do not expire](https://learn.microsoft.com/en-us/credentials/support/certification-expiration-policy); that does not make every older course current. The official AZ-900T00 course is now titled **Introduction to Cloud Infrastructure**, with one instructor day and 13 languages. Course completion, exam booking and earning the certification are separate steps.

This review adds six worked examples, seven labs, 30 answered checks and three blog exercises. The [review report](../docs/research/2026-09-28-az-900-deep-review.md) records sources and limitations. Only local calculations were executed; live Azure labs and independent human review remain pending.

## How to use this guide

AZ-900 tests whether you can explain cloud decisions and recognize the Azure service or governance control that fits a basic scenario. Study the contrasts, then prove each one in the portal or a sandbox. Do not memorize a catalog of product names without learning the problem each product solves.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe cloud concepts | 25–30% | Why use cloud, which service model fits, and who is responsible? |
| Describe Azure architecture and services | 35–40% | Where do resources live, and which compute, network, storage, or identity service fits? |
| Describe Azure management and governance | 30–35% | How are cost, policy, deployment, and health controlled? |

---

## 1. Cloud concepts

### Cloud computing and the consumption model

Cloud computing makes compute, storage, networking, platforms, and software available on demand. Capacity can be provisioned quickly and charged according to the applicable consumption or subscription model. That shifts part of the planning problem from buying enough hardware for a future peak to governing services that can expand or shrink.

Do not reduce cloud value to “someone else's computer.” A cloud provider supplies standardized services, regions, automation interfaces, metering, and economies of scale. The customer still owns workload design, data protection, access decisions, cost control, and every responsibility not transferred by the selected service.

| Term | Practical meaning | Common trap |
|---|---|---|
| Capital expenditure | Up-front purchase of an asset | Assuming ownership automatically lowers total cost |
| Operational expenditure | Ongoing payment for consumed service | Assuming consumption cannot be wasteful |
| Elasticity | Resources can respond to changing demand | Treating it as the same thing as adding capacity manually |
| Scalability | Ability to increase or decrease capacity | Ignoring whether scale is vertical or horizontal |
| High availability | Design to remain accessible despite component failure | Assuming one VM receives a platform-wide SLA |
| Reliability | Ability to recover and perform consistently | Ignoring application and data design |
| Predictability | Better forecasting of performance or cost | Confusing an estimate with a guarantee |

Vertical scaling changes the capacity of an instance; horizontal scaling changes the number of instances. Elasticity adds the idea that capacity adjusts with demand, often automatically. Azure capabilities enable these patterns, but the workload must be designed to use them.

> **Related item:** FinOps joins finance, engineering, and business ownership around cloud value. Tags, budgets, recommendations, and unit costs become useful when they drive an accountable decision, not merely a monthly report. See the [Microsoft FinOps guidance](https://learn.microsoft.com/en-us/cloud-computing/finops/).

### Public, private, and hybrid cloud

| Model | Boundary | Useful when | Tradeoff |
|---|---|---|---|
| Public cloud | Provider-operated infrastructure shared through logical isolation | Rapid access, global services, elastic capacity | Requires deliberate identity, network, data, and cost governance |
| Private cloud | Cloud operating model dedicated to one organization | Specialized control, locality, or legacy constraints | Organization carries more platform cost and operations |
| Hybrid cloud | Coordinated public and private/on-premises environments | Gradual migration, locality, latency, or regulatory needs | Identity, networking, monitoring, and governance are more complex |

Hybrid is an architecture choice, not simply “we have both.” It needs a designed relationship such as identity federation, private connectivity, consistent policy, or coordinated operations.

### Shared responsibility

Microsoft is always responsible for physical datacenters, physical networking, and physical hosts in Azure. Customer responsibility grows as the customer takes more control:

| Layer | SaaS | PaaS | IaaS | On-premises |
|---|---|---|---|---|
| Physical facility/host | Provider | Provider | Provider | Customer |
| Operating system | Provider | Provider | Customer | Customer |
| Application | Shared | Shared | Customer | Customer |
| Data, identities, configuration | Customer | Customer | Customer | Customer |
| Client devices | Shared | Customer | Customer | Customer |

Shared application responsibility does not transfer the customer’s code, access decisions or tenant configuration to Microsoft. SaaS still requires the customer to govern its data, identities and settings. The exact division depends on the service. “Microsoft secures Azure” does not mean Microsoft approves a customer's role assignments, classifies its data, or prevents insecure application logic. Review the official [shared responsibility model](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility).

### IaaS, PaaS, SaaS, and serverless

| Model | Customer mainly manages | Example decision |
|---|---|---|
| IaaS | OS, runtime, application, data, much of network configuration | Choose a VM when the application needs OS-level control |
| PaaS | Application, data, identity, configuration | Choose App Service or a managed database to reduce platform operations |
| SaaS | Users, data, access, tenant configuration | Use a completed business application such as Microsoft 365 |
| Serverless | Code or workflow plus triggers/configuration; infrastructure is abstracted | Use Azure Functions for event-driven work with variable demand |

Serverless does not mean no servers, no cost, or no operations. It means the provider manages the underlying server allocation while the customer designs triggers, permissions, state, retries, monitoring, and cost limits.

#### Scenario method

Ask these questions in order:

1. Is a finished application enough? Consider SaaS.
2. Does the team need to control the application but not the OS? Consider PaaS.
3. Does a legacy dependency or OS requirement demand machine control? Consider IaaS.
4. Is the work event-driven and naturally short-lived? Consider a serverless option.
5. What responsibility, portability, scaling, and cost tradeoff follows?

---

## 2. Core Azure architecture

### Regions, availability zones, and datacenters

An Azure geography is a market/data-residency boundary containing one or more regions. A region contains one or more datacenters connected by a low-latency network. An availability zone is a physically separate grouping of datacenters within a region with independent power, cooling, and networking. Region pairs and sovereign regions address different resiliency or jurisdictional needs. Current regional capabilities must be checked in the [Azure geographies documentation](https://learn.microsoft.com/en-us/azure/reliability/regions-list).

| Requirement | Likely design concern |
|---|---|
| Survive a datacenter-level failure in one region | Zone-redundant or zonal deployment across zones |
| Survive a regional outage | Multi-region replication and failover |
| Meet jurisdiction or sovereign-cloud rules | Eligible geography/sovereign environment and validated service availability |
| Reduce user latency | Region placement and edge/network design |

A zone is not a backup, and a second region is not automatically a working disaster-recovery solution. Data replication, application routing, identity dependencies, recovery sequencing, and testing remain design work.

> **Related item:** Recovery objectives turn “be resilient” into a testable requirement. Recovery time objective describes acceptable restoration time; recovery point objective describes acceptable data loss measured in time.

Not every Azure region has a pair. The [paired/nonpaired region guidance](https://learn.microsoft.com/en-us/azure/reliability/regions-paired) permits resilient designs with either: some services use a predefined pair, while others support a chosen secondary region. Geography and pairing labels are starting points for service-specific residency/recovery checks, not automatic guarantees that all workload data stays in one jurisdiction or fails over successfully.

### Resource hierarchy and scope

```text
Microsoft Entra tenant
└── management groups
    └── subscriptions
        └── resource groups
            └── resources
```

- A **resource** is a manageable Azure item such as a VM, storage account, or virtual network.
- A **resource group** is a lifecycle and management container. A resource belongs to one resource group, while resources in a group may reside in different regions.
- A **subscription** is a billing and management boundary with its own quotas and access scope.
- A **management group** organizes subscriptions so policy and access can be assigned above them.
- A **Microsoft Entra tenant** is an identity and directory boundary. A subscription trusts a tenant for authentication.

Assignments at a parent scope can flow to children. Place a policy or role at the narrowest scope that achieves the intended control without creating unnecessary exceptions.

### Compute choices

| Need | Azure option | Key distinction |
|---|---|---|
| OS control and lift-and-shift | Virtual Machines | Customer patches and secures the guest OS |
| Identical VM fleet with autoscale | Virtual Machine Scale Sets | Manages a group of load-balanced VM instances |
| Managed web/API hosting | App Service | PaaS web hosting without guest-OS administration |
| Event-driven code | Azure Functions | Trigger-based serverless execution |
| Container without managing a cluster | Azure Container Instances | Simple, isolated container execution |
| Orchestrated container platform | Azure Kubernetes Service | Managed Kubernetes control plane; workloads still require Kubernetes operations |
| User desktops/apps from Azure | Azure Virtual Desktop | Virtualized desktop/application delivery |

Availability sets distribute VMs across fault and update domains; availability zones separate deployments across physical zones. Scale sets address fleet management and scale. These concepts solve different failure and operating concerns.

#### VM power state is a billing decision

[VM billing states](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) distinguish **Stopped (allocated)** from **Stopped (deallocated)**. Shutting down inside the guest OS can leave the VM allocated and its compute bill running. Deallocation releases the host allocation and stops VM instance usage charges, but retained disks and some network resources can still cost money. Inspect the power state and dependent resources; a successful provisioning state is not the same as a running or deallocated VM. Worked example 1 separates those charges.

### Networking

A virtual network provides a private IP boundary in Azure. Subnets partition that address space. Network security groups filter traffic using rules. VNet peering connects virtual networks privately. Azure DNS hosts and resolves DNS zones; private DNS supports name resolution for private resources.

| Connection | Purpose |
|---|---|
| Site-to-site VPN | Encrypted connection between networks over the internet |
| Point-to-site VPN | Individual client connection to an Azure VNet |
| ExpressRoute | Private connection from an organization's network through a connectivity provider |
| Public endpoint | Service reached using a public IP/DNS path, possibly protected by firewall rules |
| Private endpoint | Private IP in a VNet representing a supported service through Private Link |

A private endpoint changes the data path, but DNS must resolve the service name to the private address and access still needs valid identity/authorization. Network reachability and authorization are independent layers. See [Azure networking fundamentals](https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview).

### Storage services and redundancy

| Data shape/access | Service |
|---|---|
| Object data, backups, media, data-lake files | Azure Blob Storage |
| Managed SMB/NFS file share | Azure Files |
| Simple NoSQL key/attribute store | Azure Table Storage |
| VM block storage | Azure managed disks |
| Durable messaging between components | Azure Queue Storage |

Storage tiers trade access cost, storage cost, and retrieval characteristics. Hot is designed for frequent access; cool/cold/archive choices reduce storage cost for less-active data while adding retrieval constraints or costs. **VERIFY CURRENT:** tier names, minimum retention, availability, and pricing.

Redundancy controls how copies are distributed:

- locally redundant storage keeps copies in one primary-region datacenter;
- zone-redundant storage distributes copies across zones in the primary region;
- geo-redundant storage adds asynchronous replication to a secondary region;
- geo-zone-redundant storage combines zone redundancy in the primary region with geo-replication.

Read-access geo variants permit reads from the secondary endpoint. More copies do not replace application-consistent backup, protection from logical deletion, or a tested recovery procedure. Use the [Azure Storage redundancy guide](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) for current support.

AzCopy is a command-line data transfer utility; Storage Explorer is a graphical management client; Azure File Sync caches Azure file shares on Windows Servers. Azure Migrate helps assess and move servers, databases, and applications, while Azure Data Box handles large offline data transfers.

---

#### Account type, access tier and redundancy are separate choices

| Choice | What it controls | Example |
|---|---|---|
| Storage service/data shape | API, protocol and object model | Blob versus Files versus Queue versus Table; VM managed disks are a different resource choice. |
| Account type/performance | Supported services and capabilities | Standard general-purpose v2 is the usual multipurpose account; premium block-blob, file-share and page-blob accounts serve specialized needs. |
| Blob access tier | Storage/access economics and retrieval behavior | Hot, cool and cold are online; archive is offline. |
| Redundancy | Location of copies and failure coverage | LRS, ZRS, GRS/GZRS and applicable read-access variants. |

Use the [account-type matrix](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) before assuming that every performance, protocol, redundancy and tier combination works. Premium does not simply mean “every standard feature, faster.”

For ordinary explicitly tiered block blobs in GPv2, [cool/cold/archive](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview) have 30/90/180-day minimum-duration charging rules. Earlier deletion, overwrite or retiering can incur a prorated charge; this is not a retention lock that prevents deletion. Archive requires rehydration before reading and can take hours, so it cannot meet an immediate-read requirement. Its redundancy support also differs from online tiers; do not assume archive works with ZRS/GZRS. Blob access tiering does not apply to page or append blobs, and premium block-blob accounts cannot simply retier their data into standard hot/cool/cold/archive tiers.

**Related current feature:** [Smart tier](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-smart) automates hot/cool/cold placement for eligible GPv2 block blobs with zonal redundancy. It remains online and does not use archive. The feature is generally available in public-cloud zonal regions; Government and 21Vianet remain preview. Inherited-tier objects can be managed automatically; explicitly tiered objects are not automatically enrolled. Its monitoring/access/capacity charges differ from ordinary manual tiering, so compare the full workload cost. This is supporting context for storage-tier decisions, not a new exam objective.

## 3. Identity, access, and security

### Authentication and authorization

Authentication establishes who or what an identity is. Authorization determines what that identity may do. Microsoft Entra ID supplies cloud identity, authentication, application access, and directory capabilities. Microsoft Entra Domain Services supplies managed domain services such as domain join, LDAP, and Kerberos/NTLM for workloads that require them.

| Control | Job |
|---|---|
| Multifactor authentication | Requires additional evidence beyond one factor |
| Passwordless authentication | Uses methods such as passkeys/FIDO2, Windows Hello, or Authenticator instead of a password |
| Single sign-on | Reuses an authenticated identity across applications |
| Conditional Access | Evaluates signals and applies access decisions such as require MFA or block |
| Azure RBAC | Grants management/data actions to principals at Azure scopes |
| External identities | Supports partner, guest, and customer identity scenarios |

An RBAC assignment combines a security principal, role definition, and scope. Effective access includes inherited assignments and deny controls; removing one visible assignment may not remove all access. Prefer groups and least privilege over many direct user assignments.

#### External users: collaboration versus customer apps

[Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview) covers two different designs. B2B collaboration lets partners/guests access permitted resources in a **workforce tenant**. Customer identity and access management uses an **external tenant** for consumer or business-customer applications, separate from the employee directory. Inviting a guest does not grant all Azure roles, and customer-app sign-in is not a replacement for employee Microsoft 365 access. Choose the user population, application and tenant model before configuring authentication.

### Zero Trust and defense in depth

Zero Trust uses three principles: verify explicitly, use least privilege, and assume breach. Defense in depth layers controls across physical security, identity, perimeter, network, compute, application, and data. They are related but not identical: Zero Trust guides access decisions; defense in depth reduces dependence on one control.

Microsoft Defender for Cloud provides cloud security posture management and workload-protection capabilities. Recommendations identify posture improvements; regulatory-compliance views organize assessments against standards. **VERIFY CURRENT:** plans, protected resource types, included features, and pricing.

> **Related item:** A secure score is prioritization evidence, not proof that a system is secure or compliant. Risk acceptance and compensating controls still need an owner and record.

---

## 4. Cost, governance, and resource management

### Cost management

Major cost drivers include resource type and size, running time, storage tier/capacity/transactions, data transfer, region, licensing, and support. The pricing calculator estimates planned Azure workloads; Cost Management analyzes actual/forecast usage, supports budgets, and helps allocate costs. Tags attach metadata such as application, environment, owner, or cost center.

A tag is not a security boundary and not every resource automatically inherits tags. A budget notifies; it does not normally stop resources. Reservations and savings plans exchange commitments for eligible discounts, while Azure Hybrid Benefit applies eligible existing licenses. Their scopes and billing units differ; they are not all compute-only offers. **VERIFY CURRENT:** prices, eligible services, terms, and benefits.

#### Budgets, limits, commitments and tags

[Cost Management budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) can alert on actual or forecast cost. They do not stop consumption by themselves. Cost data commonly arrives 8–24 hours later, budgets evaluate every 24 hours, and notification follows evaluation. Treat the result as delayed financial evidence, not a real-time cutoff. An action group can invoke separately designed automation; a shutdown still requires the right scope, permissions and failure handling.

An Azure [spending limit](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit) is different: eligible credit-based subscriptions can be disabled when credit is exhausted. It is not a custom cap available on every pay-as-you-go subscription, and some separately billed services can still incur charges. For labs, inspect the actual offer, estimate all resources, configure alerts and delete retained resources deliberately.

[Reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations) discount matching usage for specified products/attributes; some cover storage or database capacity, not just VMs. [Savings plans](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-compute-overview) use a fixed hourly spend commitment over one or three years, with distinct compute and database offerings. Unused hourly commitment does not roll forward. Neither offer starts, resizes or shuts down resources, and a billing discount is not a capacity reservation. Compare actual eligible steady usage before choosing a commitment.

[Resource tags](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources) do not automatically inherit from a resource group or subscription. Azure Policy can apply supported tagging rules. Separately, [Cost Management tag inheritance](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance) can copy parent tags into **usage records** for supported billing scopes without modifying the resources. Seeing a cost-center tag in a cost report therefore does not prove that a resource satisfies a tag policy.

### Governance controls

| Tool | Purpose | Does not do |
|---|---|---|
| Azure Policy | Audit, deny, modify, or deploy required resource configuration through definitions/initiatives | Grant a user permission |
| Azure RBAC | Authorize identities at a scope | Declare resource compliance |
| Resource lock | Protect a scope from deletion or modification | Replace backup or block data-plane actions universally |
| Tags | Classify resources for ownership/cost/automation | Enforce access by themselves |
| Microsoft Purview | Data governance, catalog, protection, risk, and compliance capabilities | Automatically make every resource compliant |

Policy evaluates resource state. An initiative groups policy definitions. Remediation can bring supported existing resources toward the desired state, often using a managed identity. A `CanNotDelete` lock permits updates but blocks deletion; `ReadOnly` is more restrictive and can affect operations that require control-plane writes.

A `deny` policy can stop a disallowed deployment without repairing existing resources. For supported `modify` and `deployIfNotExists` policies, [remediation tasks](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) use the assignment's managed identity with sufficient permissions. A compliance scan alone is not proof that remediation ran or succeeded.

[Locks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources) restrict management-plane operations even when RBAC permits them. `ReadOnly` can block starting/restarting a VM because these operations write through the management API. A storage-account delete lock does not universally protect blob contents from data-plane deletion. Combine access, policy, locks and actual data-protection features according to the operation being protected.

### Deployment and management tools

The Azure portal is graphical; Cloud Shell provides a browser-based shell; Azure CLI and Azure PowerShell support repeatable command-line automation. Azure Resource Manager is the management plane and deployment service. ARM JSON templates and Bicep declare desired infrastructure. Terraform is a widely used third-party declarative option.

Declarative infrastructure describes the desired result; imperative scripts list actions. Declarative deployments improve repeatability, review, and drift control, but templates still need testing, state awareness, safe parameter handling, and controlled identities.

Azure Arc projects Azure management and governance to supported resources outside Azure, including servers and Kubernetes. It does not move those machines into an Azure datacenter.

[Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) supplies an authenticated, temporary browser terminal with Bash or PowerShell; its host is free and inactive sessions time out. Persistent storage and resources created through shell commands can incur charges. It operates under your identity and selected subscription, so a browser terminal is not a free isolated Azure lab or permission bypass.

### Monitoring and service health

| Service | Question answered |
|---|---|
| Azure Advisor | What personalized reliability, security, performance, cost, or operational improvements are recommended? |
| Azure status | Is there a widely affecting Azure incident on the public status page? |
| Azure Service Health | Is an Azure incident, planned maintenance, or advisory affecting my subscriptions/services? |
| Resource Health | What is the health of this individual resource? |
| Azure Monitor | What telemetry exists across applications and infrastructure? |
| Log Analytics | How can collected log data be queried and analyzed? |
| Application Insights | How is an application behaving from requests through dependencies and failures? |
| Alerts | When should metric, log, activity, or health evidence notify or trigger action? |

Metrics are numerical time-series signals; logs are richer event/record data. An alert rule evaluates a condition and routes through an action group. Monitoring is not complete until the signal has an owner, severity, response, and test.

> **Related item:** Observability asks whether operators can explain a system's internal state from its outputs. Collecting logs without correlation, useful queries, retention decisions, and response ownership is storage—not observability.

---

## 5. Objective-by-objective decision guide

### Turn a cloud requirement into a responsibility decision

A service choice changes both technology and ownership. Work through a scenario in this order:

1. Identify the business outcome and acceptable failure or delay.
2. Identify the control the customer truly needs: tenant configuration, application/runtime, operating system, or physical platform.
3. Choose SaaS, PaaS, IaaS, or serverless based on that control boundary.
4. List the responsibilities retained for identity, data, application logic, configuration, monitoring, recovery, and cost.
5. Select a scaling and availability model.
6. Estimate and monitor the consumption unit that drives cost.

| Requirement | Likely direction | Responsibility returned or removed |
|---|---|---|
| Completed collaboration application | SaaS | Customer governs users, data, tenant settings, and use; provider operates the application stack |
| Web API with no OS dependency | PaaS | Customer owns code, data, access, configuration, and monitoring; provider operates runtime/OS |
| Legacy component requiring a kernel driver | IaaS VM | Customer regains guest OS, patching, runtime, and VM-level availability responsibilities |
| Bursty event handler | Serverless function | Customer owns code, trigger, permissions, state, retries, observability, and consumption guardrails |

Consumption pricing aligns expense with measured use, but it also permits rapid waste. A stopped service may continue charging for retained storage or reserved resources; a serverless workload may scale into unexpected invocation or downstream-service cost. Use the [Cost Management and Billing overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) to separate price estimation, actual-cost analysis, budgets, allocation, and optimization.

#### Separate the cloud benefits

| Benefit | Question to ask | Design implication |
|---|---|---|
| High availability | Can the service remain usable when a component fails? | Redundant instances, zones, health probes, routing, and application behavior |
| Scalability | Can capacity be increased or decreased? | Vertical/horizontal limits and application partitioning |
| Elasticity | Can capacity follow demand with little manual delay? | Autoscale signals, safe minimum/maximum limits, and statelessness where appropriate |
| Reliability | Can the system consistently meet its intended outcome and recover? | Failure analysis, backup, replication, recovery, and testing |
| Predictability | Can cost and performance be forecast within useful bounds? | Baselines, reservations/commitments where suitable, quotas, budgets, and load tests |
| Security | Can confidentiality, integrity, and availability risks be controlled? | Identity, network, application, data, posture, and response controls |
| Governance | Can the organization require and prove intended use? | Policy, scope, ownership, classifications, exceptions, and audit evidence |
| Manageability | Can people and automation deploy, observe, and change the system safely? | APIs, IaC, monitoring, standard configurations, and operational ownership |

> **Related item:** An SLA is a provider commitment under stated conditions; an SLO is an operational reliability target for a workload. Neither substitutes for an architecture that meets the application's end-to-end requirement.

### Design from geography to resource

Azure placement decisions form a chain:

```text
jurisdiction and users
        ↓
geography / sovereign environment
        ↓
region and current service availability
        ↓
zonal, zone-redundant, or nonzonal deployment
        ↓
multi-region recovery where required
        ↓
management group → subscription → resource group → resource
```

The [Azure reliability documentation](https://learn.microsoft.com/en-us/azure/reliability/) distinguishes reliability concepts, while the [current region list](https://learn.microsoft.com/en-us/azure/reliability/regions-list) is the source for regions, paired-region information where published, zones, and services. Region pairs can influence platform update and recovery behavior, but a paired region does not automatically replicate or fail over every customer workload.

Use management scopes for different purposes:

- A tenant supplies the identity directory trusted by subscriptions.
- A management group organizes subscriptions for inherited governance.
- A subscription supplies a billing, quota, access, and management boundary.
- A resource group groups resources for lifecycle and scoped management; it is not a network or region boundary.
- A resource is the manageable service instance.

The Cloud Adoption Framework [resource-organization guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources) helps connect this hierarchy to ownership. Group resources with a shared lifecycle, and use subscriptions or management groups when isolation, quota, delegated administration, or governance requires a stronger boundary.

### Select compute by control, orchestration, and workload shape

The [Azure compute decision guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) is a decision aid rather than a product-ranking table. Ask:

- Does the workload need guest-OS control?
- Is it a web/API workload, an event handler, a batch process, a desktop, or a containerized service?
- Must the platform orchestrate multiple containers and their networking/state?
- What startup time, scaling unit, runtime duration, and availability model are acceptable?
- What skills and operational burden can the team sustain?

A [virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/overview) normally participates in a wider resource design: image, size, OS disk, optional data disks, NIC, VNet/subnet, addressing, filtering, identity, availability placement, boot diagnostics, backup, and monitoring. A VM Scale Set manages a fleet of similar VMs and can integrate autoscale. An availability set distributes VMs across fault and update domains; zones use physically separate zone locations. Azure Virtual Desktop delivers desktops/applications and introduces host pools, identity, profiles, and user-access concerns beyond one VM.

Choose App Service when managed web hosting is the primary requirement, Functions for event-driven execution, Container Instances for relatively simple container execution without cluster management, and AKS when Kubernetes orchestration is itself required. PaaS removes guest-OS administration, not application security, identity, data, configuration, resilience, or monitoring.

> **Related item:** Portability is not binary. A container image may move between platforms, while identity, ingress, storage, secrets, scaling, and observability remain platform-specific.

### Trace a network request through independent control layers

An Azure request can fail at several separate layers:

```text
DNS name
  → public or private endpoint address
  → route / peering / VPN / ExpressRoute path
  → NSG, firewall, or service network rule
  → service listener and TLS
  → authentication
  → authorization
  → application/data decision
```

The [virtual network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) explains address spaces, subnets, routing, filtering, service connectivity, peering, and hybrid connectivity. Peering connects VNets through the Azure backbone but does not merge their address spaces or make every control transitive. VPN Gateway carries encrypted traffic over the internet; ExpressRoute uses a private connectivity-provider path and still requires resilient circuit/routing design.

A [private endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview) places a private IP for a supported service in a VNet. It does not automatically disable the public endpoint, fix DNS, grant application permission, or configure every client network. Diagnose the name resolution, route, filtering, and identity layers separately.

### Select storage from data shape through recovery

Choose storage by walking through six decisions:

1. **Data shape and protocol:** object/blob, hierarchical files, SMB/NFS share, key/attribute table, VM block device, or queue message.
2. **Access pattern:** frequent, infrequent, cold, or archival.
3. **Performance and transaction pattern:** latency, throughput, object size, concurrency, and request volume.
4. **Durability and availability scope:** local, zone, and optional asynchronous secondary-region copies.
5. **Data protection:** soft delete, versioning/snapshots where supported, backup, retention, and recovery testing.
6. **Movement:** online CLI/GUI transfer, hybrid caching/synchronization, migration orchestration, or offline appliance.

The [Azure Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction) describes storage services and account choices. Redundancy protects against specified infrastructure failures; it can faithfully replicate an accidental deletion or corruption. Recovery controls protect historical data and must be tested separately.

Use [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) for scripted high-performance Storage transfers, [Storage Explorer](https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer) for graphical management, and [Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction) when Windows Servers should cache an Azure file share. [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) coordinates assessment and migration scenarios; [Azure Data Box](https://learn.microsoft.com/en-us/azure/databox/data-box-overview) addresses supported offline/large-scale transfer needs. These tools solve different movement problems and do not replace target-architecture design.

### Separate directory, authentication, access policy, and Azure authorization

[Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/whatis) is the cloud identity and access directory for users, groups, applications, service principals, and managed identities. [Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview) supplies managed traditional domain capabilities for workloads that require domain join, LDAP, Kerberos, or NTLM without operating domain controllers.

Keep the decision chain clear:

| Layer | Example | Question |
|---|---|---|
| Directory identity | User, group, service principal, managed identity | What security principal exists? |
| Authentication | Passwordless, MFA, SSO | How is the identity proven? |
| Conditional Access | Require MFA, compliant device, location/risk decision | Under which conditions may sign-in/token access continue? |
| Azure RBAC | Role assignment at management group, subscription, resource group, or resource | Which Azure actions may the principal perform at this scope? |
| Resource data-plane authorization | Storage/database/key access model | Which application data operations are allowed? |

[Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) is a policy engine using identity and other signals; it is not the same as the [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) role assignment that authorizes Azure resource actions. An identity can satisfy MFA and Conditional Access yet still lack the RBAC or data permission needed for the requested operation.

Zero Trust says to verify explicitly, use least privilege, and assume breach. Defense in depth places independent safeguards across layers. Defender for Cloud adds posture and workload-protection capabilities, but recommendations and scores require prioritization, ownership, remediation, and verification.

### Apply governance controls at the correct scope

Use this sequence for an Azure governance scenario:

1. Place the workload in the correct management group, subscription, and resource groups.
2. Assign access through Azure RBAC to identities or groups.
3. Express allowed/required resource configuration with [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview).
4. Use locks for exceptional protection against control-plane modification or deletion.
5. Apply tags for classification, ownership, cost allocation, and automation metadata.
6. Use Microsoft Purview capabilities where the requirement concerns [data governance, catalog, protection, risk, or compliance](https://learn.microsoft.com/en-us/purview/purview).
7. Collect evidence and govern exceptions.

Policy, RBAC, and locks can all affect one deployment without duplicating one another. RBAC may permit a user to submit a deployment, Policy may deny the resource configuration, and a [resource lock](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources) may block a later control-plane change. Trace scope inheritance and the failed operation instead of calling the controls contradictory.

For cost, use the pricing calculator to model a planned design, Cost Management for actual/forecast evidence, budgets for notifications, tags/scopes for allocation, and Advisor for recommendations. None automatically understands business value; assign an owner who can resize, stop, commit, redesign, or accept the cost.

### Choose a management and deployment interface

[Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) is the management plane behind portal, command-line, SDK, and template operations. The interfaces suit different jobs:

| Interface | Best fit | Limitation to remember |
|---|---|---|
| Azure portal | Discovery, one-off inspection, visual operations | Manual actions are hard to reproduce consistently |
| Cloud Shell | Browser-accessible authenticated CLI or PowerShell session | Still executes commands with the signed-in identity and selected context |
| Azure CLI | Cross-platform command automation | Imperative scripts need idempotency/error handling |
| Azure PowerShell | Object-oriented PowerShell administration | Module/context/version behavior must be controlled |
| ARM template or Bicep | Declarative Azure-native deployment | Safe parameters, identities, sequencing, and change review still matter |
| Terraform | Declarative multi-provider workflow | External state/provider/version governance is required |

[Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/overview) projects supported non-Azure and multicloud resources into Azure management patterns. It does not relocate the resource or remove its local platform, network, identity, patching, and recovery responsibilities.

### Build an evidence chain from platform incident to application behavior

When a service is unhealthy, ask in this order:

1. Does [Azure Service Health](https://learn.microsoft.com/en-us/azure/service-health/overview) report an Azure incident, maintenance event, or advisory relevant to the subscription?
2. Does Resource Health report a problem with the individual resource?
3. Do Azure Monitor metrics and activity/resource logs show platform or configuration evidence?
4. Does Log Analytics query correlated logs across resources?
5. Does Application Insights show request, dependency, exception, or performance behavior inside the application?
6. Did an alert rule evaluate the intended condition and notify the correct action group?
7. Does [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview) identify a longer-term reliability, security, performance, cost, or operational improvement?

The broad [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/) is the reference for current data sources and capabilities. A provider incident can explain symptoms without proving that the application handled them correctly; an application exception can occur while every Azure resource reports healthy.

---

### Worked example 1 — VM hours and costs that remain

Use invented rates, not Azure price quotes: compute costs $0.20/hour and retained disks/network resources cost $12 for the month. A 30-day always-allocated month costs `720 × $0.20 + $12 = $156`. Deallocating outside a 10-hour schedule on 20 workdays reduces compute to 200 hours: `200 × $0.20 + $12 = $52`. Savings are $104, about 66.7%, rather than 100%. Shutting down only inside the guest can leave the original allocation charge. Real commitments, licenses and service-specific charges need separate treatment.

### Worked example 2 — actual cost versus forecast alert

Suppose a $3,000 calendar-month budget shows $1,200 spent after ten days, with no known usage changes. A simple classroom projection for a 30-day month is `$1,200 / 10 × 30 = $3,600`: actual usage is 40% of budget, while projected usage is 120%. An 80% actual-cost threshold has not been reached, but a 100% forecast threshold could warn of a projected $600 overrun. This straight-line calculation is not Azure's forecast algorithm; delayed data and changing usage limit both projections. Neither alert automatically turns resources off.

### Worked example 3 — allocate shared cost without changing access

Team A directly spends $700 and team B $300; a shared service costs $200. An agreed 70/30 allocation adds $140 and $60, yielding $840 and $360, with the $1,200 total preserved. This is an allocation policy chosen by the organization, not an automatic consequence of tags. Distinguish a resource tag, a cost-record inherited tag and a finance allocation. None grants either team access to the shared service.

### Worked example 4 — storage duration and access clocks

For 600 GB explicitly placed in the ordinary cold tier and permanently deleted after 40 days, the 90-day charging minimum leaves 50 days of early-deletion charges: `600 × 50 = 30,000 GB-days` of capacity pricing. No price or soft-delete retention is assumed here. The charge does not stop the deletion.

Now consider a different, eligible 1 MiB object managed by smart tier from day 0. With no access it moves to cool at day 30, then cold at day 90. A metadata-only read on day 40 does not reset that clock. A `Get Blob` on day 100 moves it to hot and resets the cycle; with no further access it reaches cool on day 130 and cold on day 190. Smart tier does not impose the ordinary early-deletion/retrieval fees in the first scenario; monitoring and other applicable charges still matter. Archive rehydration is a separate process.

### Worked example 5 — translate an availability target

**Related reliability exercise:** A 30-day month contains 43,200 minutes. A 99.9% availability target leaves `43,200 × 0.001 = 43.2` minutes unavailable. Twenty unavailable minutes would yield about 99.9537% availability for that defined observation window. State the measured user operation, exclusions and measurement method; this arithmetic is not an Azure SLA entitlement or evidence that a single VM meets the target.

### Worked example 6 — permission, policy, lock and data protection

| Request | Evidence to evaluate | Result under the stated assumptions |
|---|---|---|
| Contributor creates a resource in a location denied by policy | Role scope plus applicable policy/exception | RBAC permission does not override the policy denial. |
| Authorized user starts a VM under a resource-group `ReadOnly` lock | Inherited lock and management operation | The lock can block the start despite the role. |
| Authorized data user deletes a blob in a delete-locked storage account | Data-plane permission and actual blob protection | The account lock alone does not stop that data-plane operation. |
| Existing resource lacks a required tag | Compliance finding plus remediation task/identity/result | A finding is not evidence of a repaired tag. |

### Blog exercises that reinforce fundamentals

| Article | Learning exercise | Boundary |
|---|---|---|
| [Forecasted cost alerts](https://azure.microsoft.com/en-us/blog/prevent-exceeding-azure-budget-with-forecasted-cost-alerts/), Adam Wise, March 15, 2021 | Apply worked example 2 and define an owner/action for each threshold. | Useful older explanation; current budget documentation controls UI, scope and evaluation delays. The title does not mean alerts prevent every overrun. |
| [Smart tier general availability](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/), Aung Oo, April 14, 2026 | Trace the object in example 4 and compare automatic online tiering with archive. | Verify account/redundancy/blob eligibility and complete costs; customer savings stories are not a promised percentage for your workload. |
| [Observability Agent billing](https://techcommunity.microsoft.com/blog/azureobservabilityblog/understanding-billing-for-the-azure-copilot-observability-agent/4537780), Noa Kuperberg, July 16, 2026 | Identify the consumption unit, billing scope and separate telemetry costs in a monitoring design. | Optional current example, not an added exam objective. Agent work has separate Azure Agent Credit charges; it does not replace ingestion/retention/alert charges. Use [current billing documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-billing), not a future-feature promise, for operational planning. |

The main article text was reviewed; no linked cloud commands, paid activities or agent investigations were run. A more advanced landing-zone automation article was considered but not added: its abbreviated scripts and expired budget dates do not provide a suitable beginner exercise.

## 6. Hands-on labs

### Lab 1: Resource hierarchy and effective governance

In a sandbox, inspect tenant, subscription, resource-group, and resource scopes. Assign a tag, view an Azure Policy definition, and inspect an RBAC role assignment. Explain which settings inherit and why Policy and RBAC answer different questions.

### Lab 2: Compute decision record

For a legacy Windows application, event-driven image processor, web API, and containerized microservice set, choose among VMs, Functions, App Service, Container Instances, and AKS. Record control required, scaling, patch responsibility, availability, and cost driver.

### Lab 3: Network path

Draw a VNet with two subnets, an NSG, a VPN or ExpressRoute connection, public DNS, and a private endpoint. Trace DNS resolution, routing, filtering, authentication, and authorization for one request. Identify a failure at each layer.

### Lab 4: Storage and recovery

Upload public test data to Blob Storage with a suitable tier. Compare LRS, ZRS, GRS, and GZRS against requirements. Enable a reversible data-protection feature available in the sandbox, simulate a safe deletion, and document recovery.

### Lab 5: Cost and monitoring

Use the pricing calculator for a simple workload, then find Cost Management, budgets, Advisor, Service Health, Resource Health, Monitor, and alerts in a sandbox. Write one sentence explaining what each can and cannot tell you.

---

### Lab 6: Offline cost and control worksheet

Recalculate examples 1–5 with different hours, budget, shared allocation and data retention. Label every invented rate and assumption. For example 6, identify the management or data-plane request, role, policy and lock before predicting a result. Keep the worksheet usable without a paid subscription.

### Lab 7: Evidence and learning-resource review

Use the three blog exercises to create a claim/source/date table. Compare the chosen course's chapters with all 57 blueprint objectives, then identify one gap to fill from primary documentation. Record whether each activity is a paper design, local calculation, portal inspection or actual deployment. For any later Azure lab, record dependent billable resources and cleanup evidence; this guide's review did not execute those deployments.

## 7. Knowledge checks and distinctions

1. A team wants OS access for a legacy driver. Why is a VM a better fit than App Service, and which customer responsibilities return? **Answer:** The driver needs guest-OS control. With IaaS the customer handles OS patching, runtime, application/data protection and VM-level configuration/recovery.
2. A web application must survive a single datacenter failure. What does a zone-aware design add, and what does it not solve? **Answer:** It separates supported deployments across physical zone failure domains. It does not by itself replicate application data, supply backups or recover a whole region.
3. A user passes MFA but cannot start a VM. Which authentication and authorization evidence should you inspect? **Answer:** Check the successful sign-in/token context, tenant/subscription, role definition, assignment scope and inherited restrictions; MFA proves identity, not permission to start the VM.
4. A policy reports noncompliance while RBAC allows deployment. Why is that not contradictory? **Answer:** RBAC authorizes an action; Policy evaluates configuration. Audit can report noncompliance without denying, while an applicable deny effect can block an otherwise authorized deployment.
5. A budget reaches 100 percent. Why might resources keep running? **Answer:** Budgets notify based on evaluated costs; they do not stop consumption by themselves. Separate automation or an eligible credit-based spending limit has different behavior.
6. A private endpoint exists, but clients still use a public address. Which network dependency is likely incomplete? **Answer:** The client’s DNS resolver, private zone/record/link or hybrid forwarding path may still return the public address. Verify the answer from that client before changing roles.
7. Geo-redundant storage is enabled. Why are backup and restore testing still required? **Answer:** Replication can copy deletion or corruption, and asynchronous geo-replication can lag. Historical recovery controls and a tested restore protect different failure cases.
8. Does a Microsoft fundamentals certification require annual renewal? **Answer:** No. Earned fundamentals certifications do not expire, while exam content and course material can change.
9. Does PaaS transfer all application security to Microsoft? **Answer:** No. Application responsibilities are shared, and customer code, data, identities and settings remain customer responsibilities.
10. Does every Azure region have a pair? **Answer:** No. Nonpaired regions can also support resilient designs; service-specific replication and recovery choices matter.
11. Does a resource group require every resource to be in its own region? **Answer:** No. It is a lifecycle/management container, not a regional or network boundary.
12. What is the billing difference between stopped and deallocated? **Answer:** Stopped but allocated still incurs VM instance charges; deallocation stops those instance charges while retained resources may still bill.
13. Are Blob, GPv2, cold and GZRS four names for one choice? **Answer:** No. They identify service/data shape, account type, access tier and redundancy respectively.
14. Can ordinary archive blobs satisfy an immediate-read requirement? **Answer:** No. Their content must first be rehydrated to an online tier, which can take hours.
15. Does the cold tier’s 90-day minimum prevent earlier deletion? **Answer:** No. It is a charging rule, not an immutable retention policy.
16. Does smart tier automatically use archive? **Answer:** No. It manages eligible objects across online hot/cool/cold tiers.
17. Does a metadata-only read reset smart tier’s access clock? **Answer:** No. Get Blob Properties/Metadata/Tags do not count like a Get Blob or Put Blob access.
18. Is a customer-app external tenant the same design as partner B2B access? **Answer:** No. Customer apps use an external tenant; B2B collaboration grants permitted access in the workforce tenant.
19. Does a 100% budget alert guarantee no excess spending? **Answer:** No. Data/evaluation delays and continued consumption can cause an overrun; an alert is not a hard cap.
20. Can every pay-as-you-go subscriber set a custom Azure spending limit? **Answer:** No. The credit-based spending-limit feature is offer-specific and not an arbitrary pay-as-you-go cap.
21. Can unused savings-plan hourly commitment be saved for tomorrow? **Answer:** No. Unused commitment expires each hour.
22. Do billing reservations automatically deploy or guarantee compute capacity? **Answer:** No. A billing discount and a capacity reservation are different mechanisms.
23. Why can a cost report show an inherited tag that the resource lacks? **Answer:** Cost Management tag inheritance applies to usage records; it does not write the tag onto resources.
24. Does a deny policy repair all existing noncompliant resources? **Answer:** No. Use the appropriate effect and, where supported, a remediation task with an authorized managed identity.
25. Can a ReadOnly lock affect VM start even for a permitted user? **Answer:** Yes. Start is a management operation that the lock can block.
26. Does a storage-account delete lock replace blob backup or soft delete? **Answer:** No. It does not universally block data-plane deletion or provide historical recovery.
27. Does Cloud Shell make commands free and isolated? **Answer:** No. The shell host is free, but created resources and applicable storage can bill; commands use the signed-in identity/context.
28. Which view is personalized: Azure status or Service Health? **Answer:** Service Health is personalized to relevant services/subscriptions; the public status page emphasizes widespread incidents.
29. Can an application fail while Resource Health is healthy? **Answer:** Yes. Application code, dependencies, identity or configuration can fail independently; inspect application telemetry.
30. Does a course completion certificate prove the Microsoft certification was earned? **Answer:** No. Complete the actual Microsoft credential requirements; provider completion, practice results and exam registration are separate.

| Contrast | Remember |
|---|---|
| Scalability vs elasticity | Ability to change capacity versus demand-responsive change |
| Availability vs disaster recovery | Resist local failures versus restore after larger disruption |
| Region vs availability zone | Geographic service area versus isolated location inside a region |
| Resource group vs subscription | Lifecycle container versus billing/quota/management boundary |
| Authentication vs authorization | Prove identity versus permit action |
| Azure Policy vs Azure RBAC | Evaluate resource configuration versus grant permissions |
| Public endpoint vs private endpoint | Public network path versus private VNet address to a service |
| Pricing calculator vs Cost Management | Estimate planned cost versus analyze actual/forecast usage |
| Service Health vs Resource Health | Azure events relevant to you versus an individual resource's state |
| Metrics vs logs | Numerical time series versus detailed records/events |

### Readiness checklist

- [ ] I can explain the shared-responsibility shift across SaaS, PaaS, and IaaS.
- [ ] I can distinguish public, private, hybrid, consumption, scalability, elasticity, and availability.
- [ ] I can map regions, zones, management groups, subscriptions, resource groups, and resources.
- [ ] I can choose basic compute, networking, storage, identity, and security services by requirement.
- [ ] I can compare storage tiers and redundancy without calling replication a backup.
- [ ] I can distinguish identity, authentication, authorization, Conditional Access, and RBAC.
- [ ] I can distinguish Policy, locks, tags, Purview, and access control.
- [ ] I can choose portal, Cloud Shell, CLI, PowerShell, ARM/Bicep, and Arc appropriately.
- [ ] I can distinguish Advisor, Service Health, Resource Health, Monitor, Log Analytics, alerts, and Application Insights.
- [ ] I rechecked every **VERIFY CURRENT** item and the current official blueprint.

### Primary references

- [Official AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
- [Azure architecture fundamentals](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources)
- [Shared responsibility in the cloud](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)
- [Azure reliability documentation](https://learn.microsoft.com/en-us/azure/reliability/)
- [Azure networking documentation](https://learn.microsoft.com/en-us/azure/networking/)
- [Azure Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)
- [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)
- [Azure governance documentation](https://learn.microsoft.com/en-us/azure/governance/)
- [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — Introduction to Cloud Infrastructure (AZ-900T00)](https://learn.microsoft.com/en-us/training/courses/az-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation and best scope anchor |
| [Microsoft — AZ-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/practice/assessment?assessment-type=practice&assessmentId=23&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; start here before buying another assessment |
| [Microsoft Partner Skilling Hub — LevelUp AZ-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058307) | Partner login required | Earlier 10-hour estimate; current content requires sign-in | No additional cost for eligible Microsoft partners; use a work account associated with the partner organization |
| [Microsoft Learn AZ-900 learning paths](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/?practice-assessment-type=certification) | Free | About 8–12 hours | Read modules and use the free sandbox exercises where available |
| [John Savill — AZ-900 Study Cram](https://www.youtube.com/watch?v=tQp1YkB2Tgs) and [course handout repository](https://github.com/johnthebrit/AZ900CertCourse) | Free | Earlier estimate: about 4 hours, not reverified in this pass; add handout review | Clear visual review with a public companion handout; published for the 2022 scope, so fill July 2026 changes from Learn. The repository has no detected license, so link rather than republish the PDF. |
| [Pluralsight — Microsoft Azure Fundamentals (AZ-900) and practice exam](https://www.pluralsight.com/paths/microsoft-certified-azure-fundamentals-az-900) | Subscription; practice access depends on plan/library | Header: 21 hours including four labs; component sum 18h 56m courses + 2h labs = 20h 56m. Add assessment/review time | Broad structured path updated through 2026; its public page explicitly includes a practice exam, and you should choose only modules that close gaps |
| [O'Reilly — AZ-900 Microsoft Azure Fundamentals](https://www.oreilly.com/videos/az-900-microsoft/9781806387694/) | Subscription | 6 hours 27 minutes | Rithin Skaria/KodeKloud video course published August 2025; cross-check July 2026 blueprint |
| [Udemy — AZ-900 Azure Fundamentals](https://www.udemy.com/course/az-900-azure-certification-exam-prep/) | Purchase or subscription | About 8 hours 17 minutes | Nikolai Schuler course shown as updated September 2026; inspect curriculum and previews before choosing |
| [Whizlabs — AZ-900 training](https://www.whizlabs.com/microsoft-azure-certification-az-900/) | Paid course or subscription | Earlier 7+ video-hour estimate; current bundle/runtime unverified | Use the explanatory videos and labs; disregard any marketing implication that questions reproduce the exam |
| [MeasureUp — AZ-900 practice test](https://www.measureup.com/microsoft-practice-test-az-900-microsoft-azure-fundamentals.html) | Paid test or subscription; free demo available | About 5–9 hours for simulation and review | Assessment supplement with 159 questions and a June 2026 update; map misses back to the current blueprint |
| [O'Reilly — AZ-900 interactive practice test](https://www.oreilly.com/products/certification-prep.html) | Subscription | About 2–4 hours for an attempt and review | O'Reilly's public certification-prep catalog lists an AZ-900 Pearson practice test; exact launch details appear after sign-in |
| [LinkedIn Learning — AZ-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-azure-fundamentals-az-900-cert-prep-by-microsoft-press) | Subscription | 4 hours 11 minutes | Jim Cheshire course released September 2024; useful compact review, then fill July 2026 changes from Learn |
| [Coursera — Microsoft Azure Fundamentals AZ-900 specialization](https://www.coursera.org/specializations/microsoft-azure-fundamentals-az900-exam-prep) | Subscription; audit options vary | Provider pace: 3 months at 10 hours/week; four course estimates total 63 hours (18 + 21 + 20 + 4) | Microsoft-created four-course sequence with projects; far broader than a compact exam review, and the final course is practice-focused |
| [Microsoft Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) | Free | Reference as needed | Goes beyond fundamentals with patterns and decision guides; use for related-item depth |

See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md) for selection criteria and provider notes.

**Catalog boundary, September 28:** Public metadata and contents were compared with the blueprint; no paid lessons, video playback, partner account or assessment questions were accessed. O’Reilly and Udemy blocked direct retrieval, but their public browser pages confirmed the listed metadata; Udemy lists 15 sections/148 lectures. Pluralsight’s path total already includes its four 30-minute labs. LinkedIn’s 4h 11m/September 5, 2024 metadata is unchanged. Coursera’s advertised pace and summed course estimates measure different things. The partner page, direct practice-assessment page, Whizlabs and O’Reilly’s generic practice catalog returned shells or no substantive content, so current entitlement, launch details and bundle contents remain unverified.
