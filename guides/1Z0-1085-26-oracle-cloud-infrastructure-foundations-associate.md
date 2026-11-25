---
exam_code: 1Z0-1085-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/-become-an-oci-foundations-associate-2026/163541
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# 1Z0-1085-26 Oracle Cloud Infrastructure Foundations Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked October 28, 2026. It is unofficial and may contain errors. The [official OCI Foundations Associate learning path](https://mylearn.oracle.com/ou/learning-path/-become-an-oci-foundations-associate-2026/163541) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Foundations Associate, exam 1Z0-1085-26, 60 minutes, online. The public path does not state the proctoring model; **VERIFY CURRENT** in MyLearn before scheduling.<br>
**Published scope:** fundamentals and distributed-cloud architecture; identity and access; networking and load balancing; compute, containers, and functions; object, block, and file storage; security services; pricing, cost management, tagging, and support rewards.<br>
**Source boundary:** Oracle does not publish a question count, passing score, or domain weights on this public path. Do not invent them. **VERIFY CURRENT** in MyLearn before scheduling.

**Japanese-language option (Japan only; checked October 28, 2026):** Oracle's September 4 launch notice added 1Z0-1085-26-JPN. The current Japanese exam list shows 60 minutes, 40 questions, and a 65% pass score for that distinct code; it does not specify the proctoring mode. This route does not replace the English exam or its contract. [Japan launch notice](https://www.oracle.com/jp/education/news/) · [Japanese exam list](https://www.oracle.com/jp/education/certification/certification-exam-list/).
## How to use this guide

For each requirement, name the OCI resource, its scope, the identity that changes it, its network/data path, the observable evidence, and the cost or security consequence. Use a free or explicitly authorized tenancy for labs and remove billable resources afterward.

> **About related items:** A `Related item:` callout adds practical cloud-engineering context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Oracle-published capability group | Central question |
|---|---|
| Fundamentals | How do regions, availability domains, fault domains, tenancies, and compartments structure OCI? |
| Networking | How does traffic move through a VCN, routes, gateways, security controls, and load balancers? |
| Compute services | Which instance, scaling, container, Kubernetes, or serverless option fits the workload? |
| Storage solutions | When should data use object, block, or file storage, and how is it protected? |
| Security | How do IAM, Cloud Guard, Security Zones, encryption, and Vault reduce risk? |
| Cost management | How do pricing, budgets, tags, quotas, and support programs shape consumption? |

## 1. OCI structure and responsibility

A tenancy is the top-level account boundary. Compartments organize and isolate resources for policy, operations, and cost reporting; they are logical and can span regions. Regions contain availability domains, which contain fault domains. Choose placement according to failure independence, latency, residency, and service availability.

Oracle secures the cloud infrastructure; customers configure identities, networks, workloads, data, and service-specific controls. The exact boundary changes by service model. A managed service reduces infrastructure work without transferring responsibility for data classification or authorized access.

## 2. Identity and access

Identity domains contain users, groups, applications, and authentication settings. OCI IAM policies grant a subject permission to a resource type in a location, optionally under conditions. Read a policy as subject, verb, resource, scope, and condition. Prefer group or workload identity over direct user-specific grants and test least privilege.

Compartments are not folders on a local disk: moving a resource can change which policies, quotas, and cost reports apply. MFA, federation, short-lived credentials, and rotation reduce credential risk.

## 3. Networking and delivery

A VCN contains subnets, route tables, security lists, and network security groups. Route tables select next hops; security rules permit traffic. Internet, NAT, service, local peering, and dynamic routing gateways solve different reachability problems. Public IP assignment alone does not create a working path.

Load balancers distribute requests across healthy backends. Design listeners, backend sets, health checks, TLS, and subnet placement together. DNS resolves names; it does not repair a missing route or blocked port.

## 4. Compute, containers, and serverless

Choose shapes from CPU, memory, acceleration, network, and price requirements. Images provide boot content; instance configurations and pools support repeatable scaling. Autoscaling needs a meaningful signal and safe minimum/maximum boundaries.

OKE manages Kubernetes control-plane concerns while customers still govern cluster access, node or virtual-node choices, workloads, networking, and secrets. Container Instances suit simpler container workloads. Functions suit event-driven, short-lived execution with explicit triggers, permissions, limits, and observability.

## 5. Storage and databases

Block volumes attach disk-like storage to compute; file storage provides shared hierarchical access; object storage holds objects in buckets through APIs. Compare access pattern, consistency, lifecycle, durability, performance, sharing, and cost. Backups and replicas are useful only when restore tests prove the required recovery objective.

OCI also offers managed database choices. At foundation level, distinguish operational ownership, workload fit, scaling, availability, and connectivity instead of memorizing every edition.

## 6. Security and cost

Encryption protects data at rest and in transit; Vault centralizes keys and secrets where customer control is required. Cloud Guard detects risky activity and configuration; Security Zones enforce preventive recipes. Neither replaces sound IAM, network segmentation, patching, logging, or incident response.

Use tags for ownership and allocation, budgets and alerts for visibility, quotas for service limits, and compartment boundaries for delegated control. Price estimates are hypotheses—validate actual usage, data transfer, storage tiers, and idle resources.

> **Related item:** A budget alert reports spend; it does not automatically stop a workload unless you design a separate governed response.

## Integrated practice scenarios

1. **Public web service:** Place load-balanced compute in appropriate subnets, define the minimum inbound/outbound paths, store static assets, and estimate cost.
2. **Private batch processor:** Use object events and functions or containers with workload identity, Vault-held secrets, logging, and failure handling.
3. **Department tenancy:** Design compartments, groups, policies, tags, budgets, and Cloud Guard oversight without granting broad administrator access.

## Hands-on labs

1. Draw a tenancy-to-region-to-availability/fault-domain map and attach five sample resources.
2. Create a compartment, group, and read-only policy; test one allowed and one denied action.
3. Build a VCN path table covering public, NAT, service, and dynamic routing gateways.
4. Launch a small authorized compute instance, inspect its route and security path, then terminate it.
5. Compare object, block, and file storage for four workloads and test one object lifecycle rule.
6. Trace an HTTPS request through DNS, load balancer, network controls, and backend health.
7. Configure a budget and defined tags; identify an idle-resource cleanup candidate.
8. Review Cloud Guard, Security Zones, and Vault in the console and record preventive versus detective roles.

## Original readiness checks

1. Tenancy versus compartment? 2. Availability versus fault domain? 3. What does a route table decide? 4. Security list versus NSG? 5. Internet versus NAT gateway? 6. Service gateway purpose? 7. Why can a public IP still be unreachable? 8. Instance configuration versus image? 9. Autoscaling needs what guardrails? 10. OKE responsibility boundary? 11. Function suitability? 12. Block versus file storage? 13. Object lifecycle benefit? 14. Policy's five reasoning parts? 15. Why prefer groups? 16. Cloud Guard versus Security Zones? 17. Vault purpose? 18. What proves recovery? 19. Tag versus budget? 20. Quota versus limit? 21. Load-balancer health-check role? 22. What changes when moving compartments? 23. What must be verified before scheduling? 24. What proves readiness?

### Answer guide

1. Account boundary versus policy/organization boundary. 2. Data-center-scale isolation versus hardware/rack-scale isolation within an AD. 3. The next hop for matching traffic. 4. Subnet-wide versus VNIC-selective rules. 5. Public inbound/outbound path versus outbound-only internet access for private resources. 6. Private access to supported Oracle services. 7. Routes or security controls may still block it. 8. Repeatable launch settings versus boot content. 9. Useful metrics plus safe capacity boundaries. 10. Oracle manages the service control plane while you govern access, nodes/workloads, networking, and data. 11. Event-driven bounded work. 12. Attached disk-like storage versus shared filesystem. 13. Automated tiering or deletion by age. 14. Subject, verb, resource, scope, condition. 15. Scalable least-privilege administration. 16. Detection/response versus preventive enforcement. 17. Controlled keys and secrets. 18. A successful restore test meeting objectives. 19. Allocation metadata versus spend visibility/alerting. 20. Governed allowance versus service capacity ceiling. 21. Keep unhealthy backends out of rotation. 22. Applicable policies, quotas, and reports may change. 23. Current MyLearn contract. 24. Correct service/control choices plus tested paths, evidence, and cleanup.

## Readiness checklist

- I can translate a small workload into tenancy, identity, network, compute, storage, security, and cost decisions.
- I can explain both the intended path and the most likely failure point.
- I distinguish preventive controls, detective signals, and recovery evidence.
- I can complete the labs without retaining broad credentials or unexpected billable resources.

## Key terms and phrases

**OCI structure and responsibility**

| Term or phrase | Meaning |
|---|---|
| [Tenancy](#1-oci-structure-and-responsibility) | The top-level OCI account boundary that contains an organization’s cloud resources and identity configuration. |
| [Compartment](#1-oci-structure-and-responsibility) | A logical grouping of resources used to delegate access, apply policies and track ownership or cost across regions. |
| [Availability](#1-oci-structure-and-responsibility) | The ability of a service to remain usable for the intended requests over a specified measurement period. |
| [Latency](#1-oci-structure-and-responsibility) | The time for a request or operation to complete, measured at a specified boundary from the selected start to finish. |
| [Region](#1-oci-structure-and-responsibility) | A geographic area containing OCI infrastructure. Region choice affects service locality, latency, residency and recovery options. |
| [Availability domain](#1-oci-structure-and-responsibility) | An infrastructure location isolated from other availability domains in the region, used when planning workload placement. |
| [Fault domain](#1-oci-structure-and-responsibility) | A grouping within an availability domain that separates workloads across hardware and maintenance boundaries. |

**Identity and access**

| Term or phrase | Meaning |
|---|---|
| [Identity domain](#2-identity-and-access) | A boundary for managing identities, applications and authentication settings. |
| [Authentication](#2-identity-and-access) | Establishing the identity used for a request, for example by validating a credential or identity assertion. |
| [Least privilege](#2-identity-and-access) | Granting only the access a specific identity needs for its assigned work, then checking both allowed and denied actions. |
| [Federation](#2-identity-and-access) | Trusting an external identity provider’s assertions so people can authenticate through their established organization identity. |
| [Resource quota](#2-identity-and-access) | An administrative limit on a resource category within a defined scope, which can prevent creation even when infrastructure is healthy. |
| [Group](#2-identity-and-access) | A collection of identities to which access can be granted through a policy, reducing the need to manage permissions user by user. |
| [IAM policy](#2-identity-and-access) | An authorization statement identifying who may perform which class of operations on which resources within a specified scope and conditions. |

**Networking and delivery**

| Term or phrase | Meaning |
|---|---|
| [Virtual cloud network (VCN)](#3-networking-and-delivery) | A software-defined regional network in which subnets, addresses and routing connect OCI resources. |
| [Health check](#3-networking-and-delivery) | A targeted test of a component’s ability to perform a particular task. Its scope determines what a successful result proves. |
| [Encryption in transit](#3-networking-and-delivery) | Protecting data while it travels between endpoints, commonly through authenticated TLS connections. |
| [DNS](#3-networking-and-delivery) | The naming system resolving service names to addresses or other records. Correct resolution alone does not establish reachability. |
| [Load balancer](#3-networking-and-delivery) | A component distributing incoming work among eligible backends under its routing and health policy. |
| [Subnet](#3-networking-and-delivery) | An address range inside a VCN used to place network interfaces and associate applicable route and security settings. |
| [Route table](#3-networking-and-delivery) | Rules selecting a next hop based on destination. A matching route supplies a path, while security controls separately determine permitted traffic. |
| [Security list](#3-networking-and-delivery) | A set of traffic rules associated with a subnet and applied to its VNICs under OCI networking rules. |
| [Network security group (NSG)](#3-networking-and-delivery) | Traffic rules applied to chosen VNICs or other supported resource endpoints rather than every VNIC in a subnet. |
| [Internet gateway](#3-networking-and-delivery) | A VCN gateway providing a route for public internet traffic when addressing, routes and security rules allow it. |
| [NAT gateway](#3-networking-and-delivery) | A gateway enabling eligible private resources to initiate internet connections without assigning them public IP addresses. |
| [Dynamic routing gateway (DRG)](#3-networking-and-delivery) | A virtual router joining attached networks or connectivity resources, with route policies determining which paths are available. |
| [Peering](#3-networking-and-delivery) | Connecting separate networks to exchange traffic privately under the applicable routing, address-space and security rules. |
| [Backend set](#3-networking-and-delivery) | A load balancer’s pool of servers together with the policy and checks used to choose eligible backends. |
| [Listener](#3-networking-and-delivery) | The load balancer configuration accepting a particular protocol and port and directing matching traffic toward a backend. |

**Compute, containers, and serverless**

| Term or phrase | Meaning |
|---|---|
| [Compute shape](#4-compute-containers-and-serverless) | The configuration of processing, memory and related capabilities available to a compute instance. |
| [Control plane](#4-compute-containers-and-serverless) | The management interfaces and services that configure resources and policies, as distinct from using the configured workload. |
| [Instance configuration](#4-compute-containers-and-serverless) | A reusable specification of the settings needed to launch instances consistently, often used by an instance pool. |
| [Instance pool](#4-compute-containers-and-serverless) | A group of instances managed together from a reusable configuration for scaling and availability. |
| [Autoscaling](#4-compute-containers-and-serverless) | Adjusting capacity when a defined condition or schedule warrants it, subject to limits, capacity and application readiness. |
| [Oracle Kubernetes Engine (OKE)](#4-compute-containers-and-serverless) | OCI’s managed Kubernetes service for running orchestrated container workloads on configured cluster capacity. |
| [Function](#4-compute-containers-and-serverless) | Code invoked through OCI Functions for a bounded task, with runtime capacity and execution managed by the service. |

**Storage and databases**

| Term or phrase | Meaning |
|---|---|
| [Object storage](#5-storage-and-databases) | Storage that organizes data as individually addressed objects in buckets, accessed through a service interface. |
| [Block volume](#5-storage-and-databases) | Disk-like storage presented to a compute instance for workloads that read and write blocks. |
| [Backup](#5-storage-and-databases) | A retained copy created to support recovery. Validate it by restoring the relevant data and exercising the service that depends on it. |
| [Restore](#5-storage-and-databases) | Recreating data or a resource from a retained recovery copy, followed by checks that it meets the intended recovery point. |
| [File storage](#5-storage-and-databases) | Shared hierarchical storage enabling multiple eligible clients to work with files and directories through a filesystem protocol. |

**Security and cost**

| Term or phrase | Meaning |
|---|---|
| [Budget alert](#6-security-and-cost) | A notification tied to a spending threshold that helps an owner investigate usage and costs. |
| [Alert](#6-security-and-cost) | A notification that a configured condition was met, requiring interpretation with its time window, source and affected scope. |
| [Encryption at rest](#6-security-and-cost) | Protecting persisted data through encryption, with access to keys and backups forming part of the protection boundary. |
| [Network segmentation](#6-security-and-cost) | Dividing a network into controlled communication boundaries to limit reachability and the impact of a failure or compromise. |
| [Service limit](#6-security-and-cost) | A tenancy’s allowed service resource capacity under provider rules, distinct from a compartment quota an administrator sets. |
| [Cost allocation tag](#6-security-and-cost) | A metadata label used to attribute resources or consumption to an owner, environment or cost center. |
| [Vault](#6-security-and-cost) | OCI’s service for centrally managing cryptographic keys and secrets under access policy and lifecycle controls. |
| [Security Zone](#6-security-and-cost) | An OCI scope in which preventive security policy restricts resource configurations that violate its requirements. |
| [Cloud Guard](#6-security-and-cost) | OCI’s service for identifying risky activity or configuration and helping operators investigate or respond to detected problems. |

**Original readiness checks**

| Term or phrase | Meaning |
|---|---|
| [Service gateway](#original-readiness-checks) | An OCI gateway providing a private route from a VCN to supported services in the Oracle Services Network. |
| [Metric](#answer-guide) | A numeric measurement recorded over time, such as failed requests or queue depth, with defined units and dimensions. |

## Places to learn

This is a selective learning path, not a complete list of OCI resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Foundations Associate learning path](https://mylearn.oracle.com/ou/learning-path/-become-an-oci-foundations-associate-2026/163541) | Oracle account; exam listed as free | **7+ hours** as published by Oracle University |
| [Get started with OCI basics](https://docs.oracle.com/en/learn/oci-basics-tutorial/) | Oracle-provided free lab; personal-tenancy resources may incur charges | No publisher duration; 1–2 hours is an estimate for this tutorial | Guided VCN, compute, block-volume and web-service practice; stay in the assigned compartment and terminate billable resources |
| [OCI release notes](https://docs.oracle.com/en-us/iaas/releasenotes/index.htm) | Public | Variable | Current service and region announcements; use as a discovery index, not an exam blueprint |
| [OCI overview and concepts](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/baremetalintro.htm) | Public | **4–6 hours** targeted reading |
| Eight labs in this guide | Authorized OCI tenancy or paper design | **10–16 hours** plus review |
