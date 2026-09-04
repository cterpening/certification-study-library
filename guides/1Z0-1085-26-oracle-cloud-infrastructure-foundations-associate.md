---
exam_code: 1Z0-1085-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/-become-an-oci-foundations-associate-2026/163541
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1085-26 Oracle Cloud Infrastructure Foundations Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Foundations Associate learning path](https://mylearn.oracle.com/ou/learning-path/-become-an-oci-foundations-associate-2026/163541) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Foundations Associate, exam 1Z0-1085-26, 60 minutes, online and unproctored.<br>
**Published scope:** fundamentals and distributed-cloud architecture; identity and access; networking and load balancing; compute, containers, and functions; object, block, and file storage; security services; pricing, cost management, tagging, and support rewards.<br>
**Source boundary:** Oracle does not publish a question count, passing score, or domain weights on this public path. Do not invent them. **VERIFY CURRENT** in MyLearn before scheduling.

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

## Places to learn

This is a selective learning path, not a complete list of OCI resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Foundations Associate learning path](https://mylearn.oracle.com/ou/learning-path/-become-an-oci-foundations-associate-2026/163541) | Oracle account; exam listed as free | **7+ hours** as published by Oracle University |
| [OCI overview and concepts](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/baremetalintro.htm) | Public | **4–6 hours** targeted reading |
| Eight labs in this guide | Authorized OCI tenancy or paper design | **10–16 hours** plus review |
