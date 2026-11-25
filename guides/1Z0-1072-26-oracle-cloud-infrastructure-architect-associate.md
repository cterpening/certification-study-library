---
exam_code: 1Z0-1072-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-associate-2026/162234
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# 1Z0-1072-26 Oracle Cloud Infrastructure Architect Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked October 28, 2026. It is unofficial and may contain errors. The [official OCI Architect Associate learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-associate-2026/162234) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Architect Associate, exam 1Z0-1072-26, 90 minutes.<br>
**Published scope:** hands-on design and implementation with OCI IAM, networking, compute, and storage; secure, scalable, high-performance environments; cost and operational efficiency.<br>
**Source boundary:** the public path exposes high-level capabilities rather than weights, question count, or passing score. This guide preserves that boundary. **VERIFY CURRENT** in MyLearn before scheduling.

**Japanese-language option (Japan only; checked October 28, 2026):** Oracle's September 4 launch notice added 1Z0-1072-26-JPN. The current Japanese exam list shows 90 minutes, 50 questions, and a 68% pass score for that distinct code. This route does not replace the English exam or its contract. [Japan launch notice](https://www.oracle.com/jp/education/news/) · [Japanese exam list](https://www.oracle.com/jp/education/certification/certification-exam-list/).
## How to use this guide

Solve each design as constraints → candidate architecture → failure domains and data paths → IAM and encryption → observability and recovery → cost test. Build only in an authorized tenancy and destroy resources after capturing evidence.

> **About related items:** A `Related item:` callout adds practical architecture context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Published capability | Architecture proof |
|---|---|
| IAM | Every human and workload has the minimum scoped access |
| Networking | Every intended path and prohibited path is explainable |
| Compute | Placement, shape, scaling, and image choices match demand and failure goals |
| Storage | Data access, performance, lifecycle, durability, and recovery are explicit |
| Secure and scalable solutions | Controls and capacity behavior remain correct under growth and failure |
| Performance, cost, and operations | Metrics, budgets, runbooks, and tradeoffs support the design |

## 1. Requirements and OCI topology

Turn vague goals into measurable availability, recovery, latency, throughput, residency, security, and budget constraints. Map regions, availability domains, fault domains, and compartments to those constraints. Avoid assuming that multi-AD is always available or that cross-region replication is synchronous.

A compartment design should support delegation, resource discovery, quotas, and cost reporting. Separate environment and sensitivity boundaries where they produce clearer policy—not merely because a hierarchy looks tidy.

## 2. Identity architecture

Design identity domains, federation, users, groups, workload principals, policies, and conditions as one access system. Prefer dynamic groups, instance principals, or resource principals to embedded API keys. Keep emergency administration deliberate, logged, and tested.

Trace each policy from principal to verb, resource type, compartment/tenancy scope, and condition. Account for inherited access and for permissions needed by managed services to call other services.

## 3. Network architecture

Define CIDRs and subnets with growth and connectivity in mind. Route tables choose next hops; NSGs/security lists permit traffic. Combine internet, NAT, service, local/remote peering, DRG, VPN, FastConnect, DNS, load balancers, and private endpoints according to the required path.

Troubleshoot directionally: name resolution, source route, gateway/DRG propagation, security rules, return route, backend listener, health check, and application. Document overlapping address space and asymmetric routing before connecting networks.

## 4. Compute and application platform

Match flexible or fixed shapes to CPU, memory, acceleration, network, and licensing requirements. Use images, boot volumes, instance configurations, pools, autoscaling, and placement controls for repeatable deployment and failure isolation. Statelessness helps scaling but does not remove data consistency needs.

Choose compute instances, OKE, Container Instances, or Functions based on control, orchestration, runtime, event, and operational requirements. Keep application health separate from instance power state.

## 5. Storage, databases, and data protection

Choose block, file, object, or archive access patterns deliberately. Set performance, encryption, lifecycle, retention, replication, and backup policies. Design databases around consistency, availability, operations, connectivity, recovery, and workload shape.

Recovery design starts with RPO and RTO, then defines copies, replication, failover, restore, and validation. A copied backup in the same administrative failure boundary may not satisfy the requirement.

## 6. Reliability, observability, and cost

Remove single points of failure across placement, load balancing, data, DNS, and administration. Test degraded states and capacity limits. Logs, metrics, alarms, events, tracing, and health checks should answer whether users are affected and which dependency failed.

Estimate cost using shape runtime, storage capacity/performance, requests, backups, data transfer, managed-service consumption, and support. Use tagging, budgets, quotas, autoscaling boundaries, and scheduled cleanup.

> **Related item:** High availability reduces interruption from selected failures; disaster recovery restores service after a larger declared event. Treat their tests and decision authority separately.

**Related item: workload network design.** Oracle's Architecture Center compares redundant FastConnect/VPN patterns, non-overlapping CIDRs, service gateways and hub/spoke choices. Use the design playbook to explain failure domains and connectivity tradeoffs; validate region and service limits before implementation. [Network architecture guidance](https://docs.oracle.com/en/solutions/oci-best-practices/define-your-network-and-connectivity-architecture1.html).

## Integrated practice scenarios

1. **Regional commerce service:** Design public delivery, private application/database tiers, least privilege, scaling, backups, and observable failover.
2. **Hybrid analytics intake:** Connect a data center privately, land data in object storage, process it safely, and quantify transfer/recovery tradeoffs.
3. **Multi-team platform:** Build compartments, delegated policies, network hubs, shared services, quotas, and chargeback without creating an unrestricted shared administrator role.

## Hands-on labs

1. Convert a narrative into availability, RPO/RTO, latency, security, and cost acceptance criteria.
2. Design and test a least-privilege human and workload identity path.
3. Draw forward and return paths for internet, NAT, service gateway, and DRG traffic.
4. Deploy a repeatable compute pool with health checks and bounded autoscaling in an authorized tenancy.
5. Compare OKE, Container Instances, Functions, and VMs for three workloads.
6. Build a storage lifecycle and recovery matrix; execute one restore.
7. Create metrics, logs, alarms, and an incident query for a deliberately failed dependency.
8. Produce a cost estimate, tag plan, quota boundary, cleanup list, and architecture decision record.

## Original readiness checks

1. Requirement before service? 2. AD versus fault domain? 3. Compartment design purpose? 4. Workload principal benefit? 5. Policy reasoning parts? 6. Route versus security rule? 7. NAT versus service gateway? 8. DRG role? 9. Asymmetric-routing symptom? 10. Load-balancer health check? 11. Image versus instance configuration? 12. Autoscaling boundary? 13. VM versus OKE decision? 14. Block versus object storage? 15. RPO versus RTO? 16. Backup versus replication? 17. HA versus DR? 18. Which telemetry proves user impact? 19. What creates data-transfer cost? 20. Quota versus budget? 21. Why test restore? 22. Why document a rejected design? 23. What remains unpublished? 24. What proves readiness?

### Answer guide

1. Establish constraints before choosing products. 2. Data-center-scale versus within-AD hardware isolation. 3. Delegation, policy scope, quotas, ownership, and cost. 4. Removes stored human/API credentials. 5. Principal, action/verb, resource, scope, condition. 6. Next-hop selection versus permission. 7. Private outbound internet versus private supported-service access. 8. Dynamic-routing hub for external/peered connectivity. 9. Requests arrive but replies use another path. 10. Remove unhealthy backends from service. 11. Boot content versus repeatable launch definition. 12. Safe minimum/maximum and meaningful signals. 13. Required control and orchestration versus operating burden. 14. Attached random-access volume versus API object store. 15. Acceptable data loss versus restoration time. 16. Recoverable copy versus continuously maintained secondary state. 17. Local resilience versus declared recovery from wider failure. 18. Service-level symptoms correlated with dependencies. 19. Direction, source/destination, service, and volume. 20. Consumption allowance versus financial signal. 21. To prove recoverability and timing. 22. Preserve constraints and tradeoffs. 23. Weights, count, and passing score. 24. Defensible designs plus tested access, paths, failure, recovery, telemetry, and cost.

## Readiness checklist

- I derive architecture from measurable constraints and state every important tradeoff.
- I can trace identity, packet, data, failure, and recovery paths end to end.
- I test denied access, dependency failure, restore, and cleanup—not just happy-path deployment.
- I can explain why the design is secure, scalable, observable, recoverable, and cost-aware.

## Key terms and phrases

**Requirements and OCI topology**

| Term or phrase | Meaning |
|---|---|
| [Availability domain](#1-requirements-and-oci-topology) | An isolated location within an OCI region used to design placement and reduce common infrastructure failures. |
| [Fault domain](#1-requirements-and-oci-topology) | A grouping inside an availability domain that helps distribute instances across separate hardware and maintenance boundaries. |
| [Resource quota](#1-requirements-and-oci-topology) | An administrative limit on a resource category within a defined scope, which can prevent creation even when infrastructure is healthy. |
| [Availability](#1-requirements-and-oci-topology) | The ability of a service to remain usable for the intended requests over a specified measurement period. |
| [Latency](#1-requirements-and-oci-topology) | The time for a request or operation to complete, measured at a specified boundary from the selected start to finish. |
| [Throughput](#1-requirements-and-oci-topology) | The amount of useful work completed per unit time, such as bytes transferred or requests served per second. |
| [Compartment](#1-requirements-and-oci-topology) | A logical OCI grouping for resources, policy scope, ownership and cost reporting, which can span regions. |
| [Region](#1-requirements-and-oci-topology) | A geographic area containing OCI infrastructure. Region choice affects service locality, latency, residency and recovery options. |

**Identity architecture**

| Term or phrase | Meaning |
|---|---|
| [Dynamic group](#2-identity-architecture) | An OCI grouping whose membership rules identify resources that can receive permissions through policy. |
| [Instance principal](#2-identity-architecture) | An identity that lets a compute instance call OCI services under assigned permissions without storing a user’s API key. |
| [Federation](#2-identity-architecture) | Trusting an external identity provider’s assertions so people can authenticate through their established organization identity. |
| [Tenancy](#2-identity-architecture) | The organization’s root OCI account and administrative boundary in which compartments and resource policies are managed. |
| [Identity domain](#2-identity-architecture) | An OCI identity boundary managing users, groups, applications and authentication rules. |
| [Group](#2-identity-architecture) | A collection of identities to which access can be granted through a policy, reducing the need to manage permissions user by user. |
| [IAM policy](#2-identity-architecture) | An authorization statement identifying who may perform which class of operations on which resources within a specified scope and conditions. |
| [Resource principal](#2-identity-architecture) | An identity allowing a supported OCI resource to call other services under the permissions assigned to that resource. |
| [Policy inheritance](#2-identity-architecture) | The application of permissions granted at a wider scope to eligible resources below it in the compartment hierarchy. |

**Network architecture**

| Term or phrase | Meaning |
|---|---|
| [Service gateway](#3-network-architecture) | A gateway providing a private route from a VCN to supported Oracle services. |
| [Health check](#3-network-architecture) | A targeted test of a component’s ability to perform a particular task. Its scope determines what a successful result proves. |
| [DNS](#3-network-architecture) | The naming system resolving service names to addresses or other records. Correct resolution alone does not establish reachability. |
| [Load balancer](#3-network-architecture) | A component distributing incoming work among eligible backends under its routing and health policy. |
| [Subnet](#3-network-architecture) | An address range inside a VCN used to place network interfaces and associate applicable route and security settings. |
| [CIDR block](#3-network-architecture) | An IP address prefix defining a network range. The prefix length determines the range size and possible overlap with other networks. |
| [Route table](#3-network-architecture) | Rules selecting a next hop based on destination. A matching route supplies a path, while security controls separately determine permitted traffic. |
| [Security list](#3-network-architecture) | A set of traffic rules associated with a subnet and applied to its VNICs under OCI networking rules. |
| [Network security group (NSG)](#3-network-architecture) | Traffic rules applied to chosen VNICs or other supported resource endpoints rather than every VNIC in a subnet. |
| [Internet gateway](#3-network-architecture) | A VCN gateway providing a route for public internet traffic when addressing, routes and security rules allow it. |
| [NAT gateway](#3-network-architecture) | A gateway enabling eligible private resources to initiate internet connections without assigning them public IP addresses. |
| [Dynamic routing gateway (DRG)](#3-network-architecture) | A virtual router joining attached networks or connectivity resources, with route policies determining which paths are available. |
| [Peering](#3-network-architecture) | Connecting separate networks to exchange traffic privately under the applicable routing, address-space and security rules. |
| [FastConnect](#3-network-architecture) | A dedicated connectivity option between an external network and OCI that supports private or public peering configurations. |
| [Listener](#3-network-architecture) | The load balancer configuration accepting a particular protocol and port and directing matching traffic toward a backend. |

**Compute and application platform**

| Term or phrase | Meaning |
|---|---|
| [Instance pool](#4-compute-and-application-platform) | A managed collection of compute instances based on a shared configuration that can be scaled together. |
| [Shape](#4-compute-and-application-platform) | An OCI compute configuration defining available processing, memory and other hardware characteristics. |
| [Instance configuration](#4-compute-and-application-platform) | A reusable specification of the settings needed to launch instances consistently, often used by an instance pool. |
| [Autoscaling](#4-compute-and-application-platform) | Adjusting capacity when a defined condition or schedule warrants it, subject to limits, capacity and application readiness. |
| [Boot volume](#4-compute-and-application-platform) | Persistent block storage containing the operating system and startup files used to boot an instance. |
| [Oracle Kubernetes Engine (OKE)](#4-compute-and-application-platform) | OCI’s managed Kubernetes service for running orchestrated container workloads on configured cluster capacity. |
| [Function](#4-compute-and-application-platform) | Code invoked through OCI Functions for a bounded task, with runtime capacity and execution managed by the service. |

**Storage, databases, and data protection**

| Term or phrase | Meaning |
|---|---|
| [Recovery point objective (RPO)](#5-storage-databases-and-data-protection) | The maximum acceptable amount of lost recent data, expressed as a time interval. |
| [Recovery time objective (RTO)](#5-storage-databases-and-data-protection) | The maximum acceptable time to return a service to usable operation after a failure. |
| [Failover](#5-storage-databases-and-data-protection) | Transferring service to an alternate component or location when the primary cannot serve the workload. |
| [Backup](#5-storage-databases-and-data-protection) | A retained copy created to support recovery. Validate it by restoring the relevant data and exercising the service that depends on it. |
| [Restore](#5-storage-databases-and-data-protection) | Recreating data or a resource from a retained recovery copy, followed by checks that it meets the intended recovery point. |

**Reliability, observability, and cost**

| Term or phrase | Meaning |
|---|---|
| [Metric](#6-reliability-observability-and-cost) | A numeric measurement recorded over time, such as failed requests or queue depth, with defined units and dimensions. |
| [Service limit](#6-reliability-observability-and-cost) | A tenancy’s allowed service resource capacity under provider rules, distinct from a compartment quota an administrator sets. |
| [Cost allocation tag](#6-reliability-observability-and-cost) | A metadata label used to attribute resources or consumption to an owner, environment or cost center. |
| [Budget](#6-reliability-observability-and-cost) | A target for planned spending with alerts that support investigation when spending approaches an agreed threshold. |
| [Monitoring alarm](#6-reliability-observability-and-cost) | A rule that evaluates a metric query over time and signals a state change when the configured condition is met. |
| [Distributed trace](#6-reliability-observability-and-cost) | A record linking the timed work of multiple instrumented components for a single request or transaction. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Least privilege](#integrated-practice-scenarios) | Granting only the access a specific identity needs for its assigned work, then checking both allowed and denied actions. |
| [Object Storage](#integrated-practice-scenarios) | A service that stores independently addressed objects in buckets and serves them through an API. |

## Places to learn

This is a selective learning path, not a complete list of OCI architecture resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Architect Associate learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-associate-2026/162234) | Oracle account/subscription may be required | **27+ hours** as published by Oracle University |
| [OCI network and connectivity architecture](https://docs.oracle.com/en/solutions/oci-best-practices/define-your-network-and-connectivity-architecture1.html) and [workload-networking design playbook](https://docs.oracle.com/en/solutions/oci-best-practices-networking/index.html) | Public architecture guidance | No publisher duration; 1–2 hours for selected decisions is an estimate | Compare redundant FastConnect/VPN, CIDR, service gateway and hub/spoke choices; apply to a design scenario, not as a complete course |
| [OCI best practices and reference architectures](https://docs.oracle.com/en/solutions/oci-best-practices/) | Public | **8–12 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy | **24–36 hours** plus two timed design reviews |
