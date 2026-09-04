---
exam_code: 1Z0-1072-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-associate-2026/162234
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1072-26 Oracle Cloud Infrastructure Architect Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Architect Associate learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-associate-2026/162234) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Architect Associate, exam 1Z0-1072-26, 90 minutes.<br>
**Published scope:** hands-on design and implementation with OCI IAM, networking, compute, and storage; secure, scalable, high-performance environments; cost and operational efficiency.<br>
**Source boundary:** the public path exposes high-level capabilities rather than weights, question count, or passing score. This guide preserves that boundary. **VERIFY CURRENT** in MyLearn before scheduling.

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

## Places to learn

This is a selective learning path, not a complete list of OCI architecture resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Architect Associate learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-associate-2026/162234) | Oracle account/subscription may be required | **27+ hours** as published by Oracle University |
| [OCI best practices and reference architectures](https://docs.oracle.com/en/solutions/oci-best-practices/) | Public | **8–12 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy | **24–36 hours** plus two timed design reviews |
