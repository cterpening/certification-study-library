---
exam_code: 1Z0-1124-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-networking-professional-2026/163340
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# 1Z0-1124-26 Oracle Cloud Infrastructure Networking Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked October 28, 2026. It is unofficial and may contain errors. The [official OCI Networking Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-networking-professional-2026/163340) is authoritative.

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

## Current product context — separate from exam objectives

> **Related item:** Oracle’s 2026 OCI refresh removed calendar years from certification names while keeping exam codes; Oracle states OCI credentials are valid for 24 months and professional-level courses require paid access. Recent OCI Networking changes include IPv4 NAT for Dynamic Routing Gateway (October 1, 2026) and FastConnect traffic draining for private virtual circuits (September 16, 2026). Treat these as dated product context; verify topology, region, and current service limits before using them in a design.

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

## Key terms and phrases

**VCN design and addressing**

| Term or phrase | Meaning |
|---|---|
| [Classless Inter-Domain Routing (CIDR) block](#1-vcn-design-and-addressing) | An address range specified by a network prefix. An IPv4 /26 fixes 26 of 32 bits, leaving 2⁶ = 64 addresses before any platform reservations. |
| [Control plane](#1-vcn-design-and-addressing) | The management interfaces and services that configure resources and policies, as distinct from using the configured workload. |
| [Data plane](#1-vcn-design-and-addressing) | The path where workload data is actually processed or forwarded under the configuration established through the control plane. |
| [Availability](#1-vcn-design-and-addressing) | The ability of a service to remain usable for the intended requests over a specified measurement period. |
| [Availability domain](#1-vcn-design-and-addressing) | An infrastructure location isolated from other availability domains in the region, used when planning workload placement. |
| [Virtual cloud network (VCN)](#1-vcn-design-and-addressing) | A configurable regional network containing subnets, routes and security controls for OCI resources. |
| [Subnet](#1-vcn-design-and-addressing) | An address range inside a VCN used to place network interfaces and associate applicable route and security settings. |
| [Peering](#1-vcn-design-and-addressing) | Connecting separate networks to exchange traffic privately under the applicable routing, address-space and security rules. |
| [Regional subnet](#1-vcn-design-and-addressing) | A subnet that can host eligible resources in more than one availability domain within an OCI region. |
| [DNS time to live (TTL)](#1-vcn-design-and-addressing) | The period for which a resolver may cache an answer, relevant to how quickly clients can observe a DNS cutover. |

**Routing, gateways, and service delivery**

| Term or phrase | Meaning |
|---|---|
| [Next hop](#2-routing-gateways-and-service-delivery) | The gateway or other target a routing rule selects to forward traffic toward a destination. |
| [Health check](#2-routing-gateways-and-service-delivery) | A targeted test of a component’s ability to perform a particular task. Its scope determines what a successful result proves. |
| [Load balancer](#2-routing-gateways-and-service-delivery) | A component distributing incoming work among eligible backends under its routing and health policy. |
| [Tenancy](#2-routing-gateways-and-service-delivery) | The organization’s root OCI account and administrative boundary in which compartments and resource policies are managed. |
| [Region](#2-routing-gateways-and-service-delivery) | A geographic area containing OCI infrastructure. Region choice affects service locality, latency, residency and recovery options. |
| [Internet gateway](#2-routing-gateways-and-service-delivery) | A VCN gateway providing a route for public internet traffic when addressing, routes and security rules allow it. |
| [NAT gateway](#2-routing-gateways-and-service-delivery) | A gateway enabling eligible private resources to initiate internet connections without assigning them public IP addresses. |
| [Service gateway](#2-routing-gateways-and-service-delivery) | An OCI gateway providing a private route from a VCN to supported services in the Oracle Services Network. |
| [Backend set](#2-routing-gateways-and-service-delivery) | A load balancer’s pool of servers together with the policy and checks used to choose eligible backends. |
| [Listener](#2-routing-gateways-and-service-delivery) | The load balancer configuration accepting a particular protocol and port and directing matching traffic toward a backend. |

**Hybrid and multicloud architectures**

| Term or phrase | Meaning |
|---|---|
| [Dynamic routing gateway (DRG)](#3-hybrid-and-multicloud-architectures) | OCI’s virtual router that connects VCNs and other attachments, including VPN and FastConnect connections. |
| [FastConnect](#3-hybrid-and-multicloud-architectures) | A dedicated connection option linking an external network to OCI, distinct from an IPsec tunnel over the internet. |
| [Backup network path](#3-hybrid-and-multicloud-architectures) | An alternate route for connectivity when the primary path fails. Test whether routes switch to the VPN and whether the backup can carry the required traffic. |
| [Network segmentation](#3-hybrid-and-multicloud-architectures) | Dividing a network into controlled communication boundaries to limit reachability and the impact of a failure or compromise. |
| [Route table](#3-hybrid-and-multicloud-architectures) | Rules selecting a next hop based on destination. A matching route supplies a path, while security controls separately determine permitted traffic. |
| [Site-to-Site VPN](#3-hybrid-and-multicloud-architectures) | An encrypted network-to-network connection using IPsec tunnels. Both tunnel routing and encryption state affect reachability. |
| [Route import](#3-hybrid-and-multicloud-architectures) | The policy deciding which routes enter a DRG route table from attached networks. |
| [Route export](#3-hybrid-and-multicloud-architectures) | A policy controlling which available routes are advertised to a DRG attachment or peer. |
| [BGP](#3-hybrid-and-multicloud-architectures) | Border Gateway Protocol, used to exchange reachability information and select routes between routing systems. |
| [Customer premises equipment (CPE)](#3-hybrid-and-multicloud-architectures) | The on-premises edge device terminating or participating in hybrid connectivity to the cloud. |

**Secure network implementation and operations**

| Term or phrase | Meaning |
|---|---|
| [Stateful traffic rule](#4-secure-network-implementation-and-operations) | A rule that tracks an allowed connection and permits its corresponding return traffic. |
| [Stateless traffic rule](#4-secure-network-implementation-and-operations) | A rule that evaluates traffic independently in each direction, requiring appropriate rules for the return path. |
| [Audit log](#4-secure-network-implementation-and-operations) | Records of administrative actions that help identify who performed an operation, on what resource and when. |
| [DNS](#4-secure-network-implementation-and-operations) | The naming system resolving service names to addresses or other records. Correct resolution alone does not establish reachability. |
| [Security list](#4-secure-network-implementation-and-operations) | A set of traffic rules associated with a subnet and applied to its VNICs under OCI networking rules. |
| [Network security group (NSG)](#4-secure-network-implementation-and-operations) | Traffic rules applied to chosen VNICs or other supported resource endpoints rather than every VNIC in a subnet. |
| [Bastion](#4-secure-network-implementation-and-operations) | A service for controlled, time-bounded administrative sessions to eligible private resources. |
| [Network Firewall](#4-secure-network-implementation-and-operations) | A network security service enforcing inspection and traffic policy on routed flows that pass through it. |

**Workload migration**

| Term or phrase | Meaning |
|---|---|
| [Cutover](#5-workload-migration) | The planned switch of production traffic or processing to a migrated environment after prerequisites are verified. |
| [Latency](#5-workload-migration) | The time for a request or operation to complete, measured at a specified boundary from the selected start to finish. |
| [Throughput](#5-workload-migration) | The amount of useful work completed per unit time, such as bytes transferred or requests served per second. |

**Evidence-led troubleshooting**

| Term or phrase | Meaning |
|---|---|
| [Flow log](#6-evidence-led-troubleshooting) | A record describing observed network traffic and its disposition, useful for matching source, destination and time during diagnosis. |
| [Metric](#6-evidence-led-troubleshooting) | A numeric measurement recorded over time, such as failed requests or queue depth, with defined units and dimensions. |
| [Encryption in transit](#6-evidence-led-troubleshooting) | Protecting data while it travels between endpoints, commonly through authenticated TLS connections. |
| [Monitoring alarm](#6-evidence-led-troubleshooting) | A rule that evaluates a metric query over time and signals a state change when the configured condition is met. |
| [Path analysis](#6-evidence-led-troubleshooting) | Examining the modeled network path and configuration for an expected flow, alongside logs and endpoint evidence of actual traffic. |

**Original readiness checks**

| Term or phrase | Meaning |
|---|---|
| [Authorization](#answer-guide) | Evaluating whether the requesting identity may take a particular action on a particular resource within the applicable scope. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Runbook](#hands-on-labs) | A documented response procedure identifying evidence to gather, safe actions, decision owners and verification steps. |

## Places to learn

This is a selective learning path, not a complete list of OCI networking resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Networking Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-networking-professional-2026/163340) | Paid Professional course; Oracle account sign-in | **19+ hours** as published by Oracle University |
| [OCI Networking documentation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm) | Public | **12–18 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy or paper design | **28–40 hours** plus two timed troubleshooting drills |
