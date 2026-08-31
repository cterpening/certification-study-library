---
exam_code: AZ-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AZ-900 Microsoft Azure Fundamentals Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official AZ-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) is authoritative.

**Current baseline:** Skills measured as of July 20, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)

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

# 1. Cloud concepts

## Cloud computing and the consumption model

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

> **Related item:** FinOps joins finance, engineering, and business ownership around cloud value. Tags, budgets, recommendations, and unit costs become useful when they drive an accountable decision, not merely a monthly report. See the [Microsoft Cloud Adoption Framework FinOps guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/finops/).

## Public, private, and hybrid cloud

| Model | Boundary | Useful when | Tradeoff |
|---|---|---|---|
| Public cloud | Provider-operated infrastructure shared through logical isolation | Rapid access, global services, elastic capacity | Requires deliberate identity, network, data, and cost governance |
| Private cloud | Cloud operating model dedicated to one organization | Specialized control, locality, or legacy constraints | Organization carries more platform cost and operations |
| Hybrid cloud | Coordinated public and private/on-premises environments | Gradual migration, locality, latency, or regulatory needs | Identity, networking, monitoring, and governance are more complex |

Hybrid is an architecture choice, not simply “we have both.” It needs a designed relationship such as identity federation, private connectivity, consistent policy, or coordinated operations.

## Shared responsibility

Microsoft is always responsible for physical datacenters, physical networking, and physical hosts in Azure. Customer responsibility grows as the customer takes more control:

| Layer | SaaS | PaaS | IaaS | On-premises |
|---|---|---|---|---|
| Physical facility/host | Provider | Provider | Provider | Customer |
| Operating system | Provider | Provider | Customer | Customer |
| Application | Mostly provider | Customer | Customer | Customer |
| Identities, access, devices, data | Shared/customer decisions | Shared/customer decisions | Shared/customer decisions | Customer |

The exact division depends on the service. “Microsoft secures Azure” does not mean Microsoft approves a customer's role assignments, classifies its data, or prevents insecure application logic. Review the official [shared responsibility model](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility).

## IaaS, PaaS, SaaS, and serverless

| Model | Customer mainly manages | Example decision |
|---|---|---|
| IaaS | OS, runtime, application, data, much of network configuration | Choose a VM when the application needs OS-level control |
| PaaS | Application, data, identity, configuration | Choose App Service or a managed database to reduce platform operations |
| SaaS | Users, data, access, tenant configuration | Use a completed business application such as Microsoft 365 |
| Serverless | Code or workflow plus triggers/configuration; infrastructure is abstracted | Use Azure Functions for event-driven work with variable demand |

Serverless does not mean no servers, no cost, or no operations. It means the provider manages the underlying server allocation while the customer designs triggers, permissions, state, retries, monitoring, and cost limits.

### Scenario method

Ask these questions in order:

1. Is a finished application enough? Consider SaaS.
2. Does the team need to control the application but not the OS? Consider PaaS.
3. Does a legacy dependency or OS requirement demand machine control? Consider IaaS.
4. Is the work event-driven and naturally short-lived? Consider a serverless option.
5. What responsibility, portability, scaling, and cost tradeoff follows?

---

# 2. Core Azure architecture

## Regions, availability zones, and datacenters

An Azure geography is a market/data-residency boundary containing one or more regions. A region contains one or more datacenters connected by a low-latency network. An availability zone is a physically separate grouping of datacenters within a region with independent power, cooling, and networking. Region pairs and sovereign regions address different resiliency or jurisdictional needs. Current regional capabilities must be checked in the [Azure geographies documentation](https://learn.microsoft.com/en-us/azure/reliability/regions-list).

| Requirement | Likely design concern |
|---|---|
| Survive a datacenter-level failure in one region | Zone-redundant or zonal deployment across zones |
| Survive a regional outage | Multi-region replication and failover |
| Meet jurisdiction or sovereign-cloud rules | Eligible geography/sovereign environment and validated service availability |
| Reduce user latency | Region placement and edge/network design |

A zone is not a backup, and a second region is not automatically a working disaster-recovery solution. Data replication, application routing, identity dependencies, recovery sequencing, and testing remain design work.

> **Related item:** Recovery objectives turn “be resilient” into a testable requirement. Recovery time objective describes acceptable restoration time; recovery point objective describes acceptable data loss measured in time.

## Resource hierarchy and scope

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

## Compute choices

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

## Networking

A virtual network provides a private IP boundary in Azure. Subnets partition that address space. Network security groups filter traffic using rules. VNet peering connects virtual networks privately. Azure DNS hosts and resolves DNS zones; private DNS supports name resolution for private resources.

| Connection | Purpose |
|---|---|
| Site-to-site VPN | Encrypted connection between networks over the internet |
| Point-to-site VPN | Individual client connection to an Azure VNet |
| ExpressRoute | Private connection from an organization's network through a connectivity provider |
| Public endpoint | Service reached using a public IP/DNS path, possibly protected by firewall rules |
| Private endpoint | Private IP in a VNet representing a supported service through Private Link |

A private endpoint changes the data path, but DNS must resolve the service name to the private address and access still needs valid identity/authorization. Network reachability and authorization are independent layers. See [Azure networking fundamentals](https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview).

## Storage services and redundancy

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

# 3. Identity, access, and security

## Authentication and authorization

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

## Zero Trust and defense in depth

Zero Trust uses three principles: verify explicitly, use least privilege, and assume breach. Defense in depth layers controls across physical security, identity, perimeter, network, compute, application, and data. They are related but not identical: Zero Trust guides access decisions; defense in depth reduces dependence on one control.

Microsoft Defender for Cloud provides cloud security posture management and workload-protection capabilities. Recommendations identify posture improvements; regulatory-compliance views organize assessments against standards. **VERIFY CURRENT:** plans, protected resource types, included features, and pricing.

> **Related item:** A secure score is prioritization evidence, not proof that a system is secure or compliant. Risk acceptance and compensating controls still need an owner and record.

---

# 4. Cost, governance, and resource management

## Cost management

Major cost drivers include resource type and size, running time, storage tier/capacity/transactions, data transfer, region, licensing, and support. The pricing calculator estimates planned Azure workloads; Cost Management analyzes actual/forecast usage, supports budgets, and helps allocate costs. Tags attach metadata such as application, environment, owner, or cost center.

A tag is not a security boundary and not every resource automatically inherits tags. A budget notifies; it does not normally stop resources. Reservations and savings plans exchange commitment for lower eligible compute cost, while Azure Hybrid Benefit applies eligible existing licenses. **VERIFY CURRENT:** prices, eligible services, terms, and benefits.

## Governance controls

| Tool | Purpose | Does not do |
|---|---|---|
| Azure Policy | Audit, deny, modify, or deploy required resource configuration through definitions/initiatives | Grant a user permission |
| Azure RBAC | Authorize identities at a scope | Declare resource compliance |
| Resource lock | Protect a scope from deletion or modification | Replace backup or block data-plane actions universally |
| Tags | Classify resources for ownership/cost/automation | Enforce access by themselves |
| Microsoft Purview | Data governance, catalog, protection, risk, and compliance capabilities | Automatically make every resource compliant |

Policy evaluates resource state. An initiative groups policy definitions. Remediation can bring supported existing resources toward the desired state, often using a managed identity. A `CanNotDelete` lock permits updates but blocks deletion; `ReadOnly` is more restrictive and can affect operations that require control-plane writes.

## Deployment and management tools

The Azure portal is graphical; Cloud Shell provides a browser-based shell; Azure CLI and Azure PowerShell support repeatable command-line automation. Azure Resource Manager is the management plane and deployment service. ARM JSON templates and Bicep declare desired infrastructure. Terraform is a widely used third-party declarative option.

Declarative infrastructure describes the desired result; imperative scripts list actions. Declarative deployments improve repeatability, review, and drift control, but templates still need testing, state awareness, safe parameter handling, and controlled identities.

Azure Arc projects Azure management and governance to supported resources outside Azure, including servers and Kubernetes. It does not move those machines into an Azure datacenter.

## Monitoring and service health

| Service | Question answered |
|---|---|
| Azure Advisor | What personalized reliability, security, performance, cost, or operational improvements are recommended? |
| Azure Service Health | Is an Azure incident, planned maintenance, or advisory affecting my subscriptions/services? |
| Resource Health | What is the health of this individual resource? |
| Azure Monitor | What telemetry exists across applications and infrastructure? |
| Log Analytics | How can collected log data be queried and analyzed? |
| Application Insights | How is an application behaving from requests through dependencies and failures? |
| Alerts | When should metric, log, activity, or health evidence notify or trigger action? |

Metrics are numerical time-series signals; logs are richer event/record data. An alert rule evaluates a condition and routes through an action group. Monitoring is not complete until the signal has an owner, severity, response, and test.

> **Related item:** Observability asks whether operators can explain a system's internal state from its outputs. Collecting logs without correlation, useful queries, retention decisions, and response ownership is storage—not observability.

---

# 5. Hands-on labs

## Lab 1: Resource hierarchy and effective governance

In a sandbox, inspect tenant, subscription, resource-group, and resource scopes. Assign a tag, view an Azure Policy definition, and inspect an RBAC role assignment. Explain which settings inherit and why Policy and RBAC answer different questions.

## Lab 2: Compute decision record

For a legacy Windows application, event-driven image processor, web API, and containerized microservice set, choose among VMs, Functions, App Service, Container Instances, and AKS. Record control required, scaling, patch responsibility, availability, and cost driver.

## Lab 3: Network path

Draw a VNet with two subnets, an NSG, a VPN or ExpressRoute connection, public DNS, and a private endpoint. Trace DNS resolution, routing, filtering, authentication, and authorization for one request. Identify a failure at each layer.

## Lab 4: Storage and recovery

Upload public test data to Blob Storage with a suitable tier. Compare LRS, ZRS, GRS, and GZRS against requirements. Enable a reversible data-protection feature available in the sandbox, simulate a safe deletion, and document recovery.

## Lab 5: Cost and monitoring

Use the pricing calculator for a simple workload, then find Cost Management, budgets, Advisor, Service Health, Resource Health, Monitor, and alerts in a sandbox. Write one sentence explaining what each can and cannot tell you.

---

# 6. Knowledge checks and distinctions

1. A team wants OS access for a legacy driver. Why is a VM a better fit than App Service, and which customer responsibilities return?
2. A web application must survive a single datacenter failure. What does a zone-aware design add, and what does it not solve?
3. A user passes MFA but cannot start a VM. Which authentication and authorization evidence should you inspect?
4. A policy reports noncompliance while RBAC allows deployment. Why is that not contradictory?
5. A budget reaches 100 percent. Why might resources keep running?
6. A private endpoint exists, but clients still use a public address. Which network dependency is likely incomplete?
7. Geo-redundant storage is enabled. Why are backup and restore testing still required?

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

## Readiness checklist

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

## Primary references

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

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AZ-900 course](https://learn.microsoft.com/en-us/training/courses/az-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation and best scope anchor |
| [Microsoft Partner Skilling Hub — LevelUp AZ-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058307) | Partner login required | 10 hours | No additional cost for eligible Microsoft partners; use a work account associated with the partner organization |
| [Microsoft Learn AZ-900 learning paths](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/?practice-assessment-type=certification) | Free | About 8–12 hours | Read modules and use the free sandbox exercises where available |
| [John Savill — AZ-900 Study Cram](https://www.youtube.com/watch?v=tQp1YkB2Tgs) and [course handout repository](https://github.com/johnthebrit/AZ900CertCourse) | Free | About 4 hours plus handout review | Clear visual review with a public companion handout; published for the 2022 scope, so fill July 2026 changes from Learn. The repository has no detected license, so link rather than republish the PDF. |
| [Pluralsight — Microsoft Azure Fundamentals (AZ-900)](https://www.pluralsight.com/paths/microsoft-certified-azure-fundamentals-az-900) | Subscription | 21 hours plus labs | Broad structured path updated through 2026; choose only modules that close gaps |
| [O'Reilly — AZ-900 Microsoft Azure Fundamentals](https://www.oreilly.com/videos/az-900-microsoft/9781806387694/) | Subscription | 6 hours 27 minutes | Rithin Skaria/KodeKloud video course published August 2025; cross-check July 2026 blueprint |
| [Udemy — AZ-900 Azure Fundamentals](https://www.udemy.com/course/az-900-azure-certification-exam-prep/) | Purchase or subscription | About 8 hours 17 minutes | Nikolai Schuler course shown as updated August 2026; inspect curriculum and previews before choosing |
| [Whizlabs — AZ-900 training](https://ask.whizlabs.com/microsoft-azure-certification-az-900/) | Paid course or subscription | 7+ video hours plus labs | Use the explanatory videos and labs; disregard any marketing implication that questions reproduce the exam |
| [LinkedIn Learning — AZ-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-azure-fundamentals-az-900-cert-prep-by-microsoft-press) | Subscription | 4 hours 11 minutes | Jim Cheshire course released September 2024; useful compact review, then fill July 2026 changes from Learn |
| [Coursera — Microsoft Azure Fundamentals AZ-900 specialization](https://www.coursera.org/specializations/microsoft-azure-fundamentals-az900-exam-prep) | Subscription; audit options vary | About 3 months at 10 hours/week (provider pace) | Microsoft-created four-course sequence with projects; far broader than a compact exam review, and the final course is practice-focused |
| [Microsoft Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) | Free | Reference as needed | Goes beyond fundamentals with patterns and decision guides; use for related-item depth |

See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md) for selection criteria and provider notes.
