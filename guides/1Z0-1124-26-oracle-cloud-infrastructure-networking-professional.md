---
exam_code: 1Z0-1124-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-networking-professional-2026/163340
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1124-26 Oracle Cloud Infrastructure Networking Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Networking Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-networking-professional-2026/163340) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Networking Professional, exam 1Z0-1124-26, 90 minutes.<br>
**Published scope:** plan and design OCI networking; hybrid and multicloud architectures; secure implementation and operations; workload migration; troubleshooting.<br>
**Source boundary:** the current path and embedded exam identify 2026, but one descriptive sentence still says “2025 Networking Professional.” This guide treats that as stale path copy, does not infer unpublished weights, question count, or passing score, and requires **VERIFY CURRENT** before scheduling.

## How to use this guide

Draw every packet path in both directions. Label source and destination addresses, DNS answer, route-table lookup, gateway or DRG attachment, security decision, translation, load-balancer hop, and application listener. Then test the intended path, prohibited path, and failure path using an authorized environment or a precise paper lab.

> **About related items:** A `Related item:` callout adds practical networking context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Published capability | Network proof |
|---|---|
| Plan and design OCI networking | Addressing, topology, DNS, routing, availability, capacity, and ownership meet explicit requirements |
| Hybrid and multicloud networking | DRG attachments, route policy, encryption, redundancy, and cloud-to-cloud paths are explainable end to end |
| Secure implementation and operations | Reachability is least privilege, changes are controlled, and telemetry detects unintended paths |
| Workload migration | Discovery, address, DNS, dependency, bandwidth, cutover, rollback, and validation risks are managed |
| Troubleshooting | Layered evidence isolates name, route, security, gateway, translation, transport, and application faults |

## 1. VCN design and addressing

Plan IPv4 or IPv6 address space against growth, peering, hybrid networks, acquisitions, and multicloud ranges. Overlap blocks ordinary routing and makes later integration expensive. Define VCN and subnet boundaries from routing, security, availability, delegation, and lifecycle needs—not from a desire to make many subnets.

Regional subnets can span availability domains. Public or private classification concerns public IP assignment behavior, while actual reachability also requires routes, gateways, security rules, and functioning return paths. Separate control-plane resource permissions from data-plane packet permission.

Design DNS zones, views, resolvers, endpoints, forwarding, and naming ownership so clients receive answers appropriate to their network. Record TTL and caching behavior in cutover and rollback plans.

## 2. Routing, gateways, and service delivery

A VCN route table selects the next hop for matching traffic, generally using the most specific destination. Internet, NAT, and service gateways support different destinations and exposure models. Local or remote peering and DRG attachments extend connectivity across VCN, region, tenancy, or external-network boundaries.

Load balancers and network load balancers differ in protocol awareness and features. In either case, trace listener, policy, backend set, health check, source preservation or proxy behavior, security rules, and backend return path. A healthy infrastructure resource can still serve an unhealthy application.

Account for asymmetric routing when traffic enters through one stateful path and returns through another. Route intent must be consistent across subnet, VNIC, gateway, DRG, appliance, and external routes.

## 3. Hybrid and multicloud architectures

A DRG is a virtual router connecting VCN, remote peering, Site-to-Site VPN, FastConnect, and supported attachment types. DRG route tables govern packets entering through attachments; import and export distributions control learned-route propagation. Treat attachments and policy separately so segmentation is intentional.

Site-to-Site VPN uses IPSec tunnels and commonly BGP or static routing. Design both tunnels, fault handling, routing preference, encryption, monitoring, and on-premises CPE behavior. FastConnect provides private connectivity through a provider or colocation model; design redundant circuits, physical diversity, BGP policy, and VPN backup according to the failure target.

For multicloud, document every ownership handoff, interconnect, BGP session, prefix filter, DNS domain, security control, bandwidth limit, metering boundary, and support escalation. “Private” does not mean encrypted, redundant, or trusted by default.

> **Related item:** BFD can accelerate failure detection on supported paths, but aggressive timers do not repair a poorly designed alternate route.

## 4. Secure network implementation and operations

Security lists apply at the subnet association; network security groups group chosen VNICs or resources for policy. Understand stateful and stateless behavior, direction, protocol, port, and source or destination. Apply least reachability and test an explicit deny outcome even where rules are expressed as allows.

Control who can alter VCNs, gateways, DRGs, route tables, DNS, firewalls, and load balancers. Use Bastion or other approved private administration patterns instead of permanent public management exposure. Inspect traffic with Network Firewall or authorized appliances only when routes, symmetric paths, scaling, failure mode, and log handling are designed.

Protect internet-facing applications with the appropriate edge and application controls, certificates, and backend restrictions. Collect VCN flow logs and relevant gateway, load balancer, firewall, DNS, and audit evidence. Validate changes in small stages with rollback criteria.

## 5. Workload migration

Discover application dependencies, addresses, protocols, name resolution, certificates, allowlists, throughput, latency, packet size, state, and timing before moving traffic. Select rehost, replatform, or redesign actions independently for each dependency.

Build connectivity and observability before cutover. Replicate or transfer data, validate delta behavior, lower DNS TTL only when justified, rehearse cutover, freeze conflicting change, and define a rollback point. Measure both technical health and user transactions after traffic moves.

Migration bandwidth estimates must include usable throughput, protocol and encryption overhead, concurrency, retry, change rate, and the available transfer window. A nominal circuit rate is not a completion forecast.

## 6. Evidence-led troubleshooting

Start with scope: who fails, from where, to which resolved address and port, since when, and after what change. Work from DNS and source configuration through routes, gateways or DRG policy, security rules, translation, load-balancer health, transport handshake, TLS, and application behavior. Check the reverse direction explicitly.

Use route inspection, Network Path Analyzer where applicable, VCN flow logs, service logs, metrics, alarms, packet captures at authorized endpoints, and external-device evidence. Timestamps, addresses, protocol, port, action, bytes, and correlation identifiers prevent guesswork.

Change one well-supported hypothesis at a time. Record expected observation, actual result, rollback, and residual risk. Broadly opening traffic is not a valid diagnostic conclusion.

## Integrated practice scenarios

1. **Redundant hybrid hub:** Connect two on-premises sites and three segmented VCNs through a DRG using FastConnect and VPN backup while preventing unintended east-west transit.
2. **Private multicloud data service:** Design cross-cloud routing, DNS, encryption, prefix filters, return paths, monitoring, and support boundaries for an application consuming a private database endpoint.
3. **Zero-downtime migration:** Discover an existing web application, establish OCI connectivity, migrate data and compute, switch DNS, validate transactions, and exercise rollback after a simulated path fault.

## Hands-on labs

1. Create an address plan for six VCNs, two sites, and another cloud; detect and resolve an intentional overlap.
2. Draw and test public, private outbound, and private Oracle-service paths using internet, NAT, and service gateways.
3. Build a DRG paper or authorized lab with multiple attachment route tables and import distributions; prove allowed and isolated paths.
4. Configure or simulate redundant VPN/FastConnect routing and predict convergence under four failures.
5. Apply NSG/security-list rules to a three-tier service; prove required access and at least three prohibited paths.
6. Route authorized test traffic through a firewall or paper appliance design and analyze symmetry, scaling, bypass, and fail-closed/open behavior.
7. Write a migration runbook with dependency inventory, bandwidth estimate, DNS plan, validation, freeze, rollback, and ownership gates.
8. Diagnose five seeded faults across DNS, route, DRG propagation, security, and backend health using an evidence worksheet.

## Original readiness checks

1. Why reserve address space? 2. Public subnet misconception? 3. Control plane versus data plane? 4. DNS TTL effect? 5. Longest-prefix match? 6. NAT versus service gateway? 7. Route versus security rule? 8. DRG attachment versus route table? 9. Import distribution purpose? 10. VPN redundancy requirement? 11. FastConnect failure planning? 12. Why private may not mean encrypted? 13. NSG versus security list? 14. Stateful versus stateless concern? 15. Inspection symmetry? 16. Flow-log use? 17. Migration dependency discovery? 18. Bandwidth-estimate inputs? 19. DNS rollback prerequisite? 20. First troubleshooting question? 21. Why trace return traffic? 22. Healthy backend limitation? 23. Unsafe diagnostic shortcut? 24. Published-year inconsistency? 25. What proves professional readiness?

### Answer guide

1. Growth and future connectivity without overlap. 2. It does not alone create internet reachability. 3. Resource-management authorization versus packet permission. 4. How long old answers can remain cached. 5. Most specific matching destination wins. 6. Private outbound internet versus private supported-service access. 7. Next-hop selection versus permission. 8. Connection to the DRG versus routing policy for entering packets. 9. Control which attachment routes populate a DRG route table. 10. Both tunnel and routing/CPE failure behavior. 11. Diverse circuits and an alternate path matched to requirements. 12. Path privacy does not automatically provide encryption or trust. 13. Selected resource grouping versus subnet-associated policy. 14. Return-flow tracking and explicit reverse rules. 15. Stateful inspection needs predictable forward and return paths. 16. Confirm observed tuple, direction, action, and volume. 17. Avoid moving a service while breaking hidden calls. 18. Usable rate, overhead, change, retry, concurrency, and window. 19. Known old target and a cache-aware reversal plan. 20. Exact scope, source, destination, time, and change. 21. Many failures are asymmetric. 22. Probe success may not prove user transactions. 23. Opening broad access without evidence. 24. The path and exam say 2026 while one sentence says 2025; verify rather than reinterpret it. 25. Defensible designs plus tested reachability, isolation, convergence, cutover, rollback, and diagnosis.

## Readiness checklist

- I can explain forward and return paths through VCN and DRG routing, security, gateways, inspection, and load balancing.
- I can design redundant hybrid and multicloud connectivity without hiding prefix, encryption, DNS, or ownership assumptions.
- I can migrate with discovery, measurable transfer and cutover plans, transaction validation, and rollback.
- I troubleshoot from evidence and preserve Oracle's visible 2026/2025 path inconsistency as a verification warning.

## Places to learn

This is a selective learning path, not a complete list of OCI networking resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Networking Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-networking-professional-2026/163340) | Oracle account/subscription may be required | **19+ hours** as published by Oracle University |
| [OCI Networking documentation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm) | Public | **12–18 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy or paper design | **28–40 hours** plus two timed troubleshooting drills |
