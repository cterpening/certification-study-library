---
exam_code: ANS-C01
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: retirement-announced
upcoming_change_checked: 2026-09-01
---

# ANS-C01 AWS Certified Advanced Networking - Specialty Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ans-c01-coverage-record). The [official ANS-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01.html) is authoritative.

**Current baseline:** Current four-domain ANS-C01 guide; 50 scored plus 15 unscored questions<br>
**Upcoming blueprint change:** **RETIREMENT ANNOUNCED.** The live English certification page says December 31, 2026 is the last testing date. AWS says credentials earned before retirement retain their normal three-year validity and points future networking learners to Skill Builder; it does not name a replacement certification.<br>
**Important lifecycle conflict:** AWS had announced August 25, 2026, and several localized pages still display that superseded date. The English page now shows December 31. Verify the [live certification page](https://aws.amazon.com/certification/certified-advanced-networking-specialty/) and actual scheduling availability before paying or beginning an exam-specific plan.<br>
**Official source:** [AWS Certified Advanced Networking - Specialty exam guide](https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01.html)

## How to use this guide

ANS-C01 validates design, implementation, operation, automation, and security of AWS and hybrid networks at scale. AWS targets candidates with five or more years of networking experience and two or more years of cloud/hybrid networking. This is a packet-path exam: learn to follow source → name resolution → route selection → security/encryption → middlebox/load balancer → target → return path, then identify the control and evidence at each hop.

The live page lists 170 minutes, 65 questions, USD 300, and English, Japanese, Korean, and Simplified Chinese. The detailed guide identifies 50 scored and 15 unidentified unscored items, multiple-response and matching interactions, compensatory scoring, and a 700 minimum scaled score. The retirement window makes the live page and scheduler authoritative for delivery.

For every design or incident, record:

1. endpoints, direction, address family, protocol/ports, name, expected path, throughput/latency and availability;
2. routing/control-plane source, propagation and preference at every hop;
3. stateful/stateless filtering, identity/resource/endpoint policy, inspection, and encryption;
4. return-path symmetry, MTU/MSS, NAT/translation, DNS cache/TTL, connection state and failure domain;
5. logs, metrics, route/reachability analysis, packet capture or active test that can prove each hypothesis;
6. automation, ownership, rollout/rollback, quota, cost, compliance, and lifecycle.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| 1. Network Design | 30% | Which edge, DNS, load-balancing, visibility, hybrid, and multi-account topology satisfies the requirements? |
| 2. Network Implementation | 26% | How are hybrid, multi-account/Region/VPC, DNS, and automated network constructs configured and validated? |
| 3. Network Management and Operation | 20% | How do you maintain routes, diagnose packets, and optimize performance, reliability, and cost? |
| 4. Network Security, Compliance, and Governance | 24% | How do you enforce, audit, and encrypt network paths against a threat/compliance model? |

Use the detailed [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01-domain1.html), [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01-domain2.html), [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01-domain3.html), and [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01-domain4.html) pages as the task contract. The [in-scope services page](https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/ans-01-in-scope-services.html) is non-exhaustive and mutable.

## 1. Network Design — 30%

### 1.1 Design global ingress and edge behavior

Match the product to protocol, origin, caching, client addressing, health, routing, and security requirements.

- **CloudFront** is an HTTP(S) content-delivery and edge-compute layer. Design cache keys, TTL/invalidation, origin access, signed access, WAF, TLS, origin failover, logging, and dynamic-versus-cacheable behavior.
- **Global Accelerator** supplies static anycast IPs and routes TCP/UDP flows over the AWS network to healthy regional endpoints. It does not provide an HTTP object cache.
- **Route 53** makes DNS answers using policies and health information; TTL and resolver caching affect failover. It does not proxy the subsequent connection.
- **API Gateway** provides managed HTTP/REST/WebSocket API front doors with authentication, throttling, stages and integrations; private/regional/edge patterns differ.
- **ALB** handles Layer-7 HTTP(S) host/path/header and related routing; **NLB** handles high-performance Layer-4 TCP/UDP/TLS use cases and static addressing; **GWLB** inserts fleets of virtual appliances using GENEVE. Verify current feature matrices.

For inbound design, capture source IP requirements, TLS termination/passthrough, mutual TLS, WAF/DDoS, client affinity, cross-zone behavior, health semantics, zonal failure, connection duration, protocol preservation, target type, scale ramp and logging. “Use a load balancer” is not a complete network design.

**Related item:** Health checks must represent the user transaction and dependencies closely enough to route safely. A process-level check can keep an incapable Region or target in service.

### 1.2 Design public, private, and hybrid DNS

Understand authoritative zones, recursive resolution, delegation, record types, negative caching, TTL, split-horizon namespaces, DNSSEC, and query logging.

- Public hosted zones answer internet-visible authoritative names; private hosted zones answer associated VPCs through the VPC resolver.
- Alias records integrate with supported AWS targets and differ from CNAME behavior, especially at the zone apex.
- Route 53 Resolver **inbound endpoints** let on-premises resolvers query VPC/private namespaces. **Outbound endpoints plus forwarding rules** let VPC clients resolve domains through on-premises resolvers.
- Share resolver rules through RAM where a centralized DNS operating model fits. Associate private zones carefully; overlapping names and resolver rule priority can produce surprising answers.
- Use delegation to assign a child zone to another authority/account. Validate parent NS/DS relationships and key rollover if DNSSEC is required.
- Traffic policies—simple, weighted, latency, failover, geolocation, geoproximity, multivalue, and IP-based where supported—solve different routing requirements. DNS answers are not real-time per-packet steering.

Document query source, suffix, resolver path, forwarding direction, network/security requirements for endpoints, expected authority, TTL/cache, failure response, logs, and ownership. Avoid forwarding loops.

### 1.3 Design load balancing and service insertion

Choose OSI layer and behavior before product. ALB understands HTTP requests and can integrate WAF and application routing. NLB preserves Layer-4 semantics and supports TCP/UDP/TLS patterns, static IPs/EIPs and PrivateLink provider endpoints. GWLB distributes IP flows across appliances and requires correct GENEVE, route, appliance, health, symmetry, and fail-open/closed reasoning.

Target groups may use instances, IPs, Lambda, ALBs, or other supported targets depending on load balancer type. Consider target-registration scope, cross-zone distribution, zonal shift/current features, client IP, Proxy Protocol, TLS policy/certificates, idle timeout, deregistration delay, slow start, stickiness, health intervals and draining. For Kubernetes, understand how the AWS Load Balancer Controller translates Ingress/Service intent into AWS constructs and security/target behavior.

### 1.4 Design visibility before incidents

Build an evidence matrix:

| Question | Useful evidence |
|---|---|
| Was a flow accepted/rejected at an interface? | VPC Flow Logs with relevant base/extended fields |
| Is the modeled AWS path reachable? | Reachability Analyzer; Network Access Analyzer for broader access findings |
| Which TGW routes/topology are present? | Transit Gateway route tables, Route Analyzer/Network Manager and TGW Flow Logs where applicable |
| What did the packet/application exchange contain? | Traffic Mirroring or endpoint/application capture where supported and authorized |
| What did edge/LB/DNS do? | CloudFront/LB/WAF/Route 53 Resolver query logs, health and metrics |
| Did control-plane configuration change? | CloudTrail, Config, IaC/deployment history |

Baseline throughput, latency, loss, jitter, DNS response, active paths, BGP state/routes, tunnel/connection state, NAT/port use, load-balancer health/capacity, and quotas during healthy periods. Define retention, central delivery, clock/correlation, access and cost.

### 1.5 Design hybrid connectivity and BGP behavior

Collect sites, carriers, ports, bandwidth, latency/jitter, encryption, routing domains, ASN/prefixes, address overlap, IPv4/IPv6, multicast, MTU, availability, failover time, ownership and cost.

- **Site-to-Site VPN:** redundant IPsec tunnels; static or BGP routing depending on gateway/device. Accelerated VPN uses Global Accelerator for supported paths. Test both tunnels and customer-gateway behavior.
- **Direct Connect:** physical/logical private connectivity. A private VIF reaches VPC resources through a virtual private gateway/DX gateway pattern; a transit VIF connects through a Direct Connect gateway to Transit Gateway; a public VIF reaches supported AWS public prefixes. Validate current association, Region and encryption options.
- **Direct Connect resilience:** separate devices, connections and often locations according to criticality. LAG increases aggregate/circuit management but links at one location/device class do not create location diversity.
- **VPN over Direct Connect** can supply IPsec encryption over private connectivity; MACsec is available only for supported dedicated connections/configurations. Direct Connect is not inherently encrypted.
- **Transit Gateway Connect** uses GRE/BGP overlays for supported SD-WAN/appliance integration.

For BGP, reason about advertisements, accepted prefixes, summarization, ASN, longest-prefix match, local device policy, AS path, MED/communities where supported, equal-cost paths, quotas, convergence, asymmetric routing, and failure. Do not memorize a single “priority list” without identifying which router and route table is selecting.

### 1.6 Design multi-VPC, account, and Region topology

- **VPC peering:** direct, non-transitive routed relationship; good for limited/simple connectivity, but route/policy count grows with meshes.
- **Transit Gateway:** hub-and-spoke routing with separate TGW route tables, propagation/association, appliance mode and cross-account RAM sharing. Segmentation is explicit routing design.
- **PrivateLink:** service-oriented, unidirectional consumer-to-provider connectivity without full route exchange; useful with overlapping address spaces and tenant/service isolation.
- **VPC sharing:** central owner provides subnets to participant accounts. It centralizes network lifecycle but requires clear responsibility for subnet, route, security and workload resources.
- **Cloud WAN:** policy-driven global core networking for an operating model that needs it; compare complexity, features and cost with TGW inter-Region designs.

Plan non-overlapping IP centrally with IPAM and IPv6 where appropriate. For existing overlaps, isolate with PrivateLink/proxies, translate with NAT patterns, or renumber; Transit Gateway does not magically route ambiguous identical prefixes.

## 2. Network Implementation — 26%

### 2.1 Implement and validate hybrid paths

For Direct Connect, verify LOA-CFA/cross-connect responsibility, port speed, VLAN, BGP peering addresses, ASN, MD5 if used, VIF type, gateway association, allowed prefixes, BFD/current support, jumbo frames and resilient connections. For VPN, verify customer-gateway public address/ASN, inside tunnel CIDRs, IKE/IPsec parameters, two tunnels, route propagation/static entries, firewall/NAT traversal and monitoring.

Implement a controlled test plan: expected prefixes on both sides, forward and reverse traceroute/captures where meaningful, TCP/UDP application test, MTU/fragmentation/PMTUD, fail one tunnel/connection/device/location at a time, measure convergence/session effect, and verify the intended backup does not form an unintended transit path.

Route tables exist at VPC subnets, TGW attachments, virtual gateways/devices, on-premises routers, and sometimes appliances. Draw each independently. Propagation reduces manual entries but can leak reachability if route-table associations and advertisements are not bounded.

### 2.2 Implement multi-account and multi-Region paths

For a TGW hub, create attachment ownership/sharing, route-table association, controlled propagation/static routes, inspection and egress attachments, blackhole/isolation behavior, DNS support and cross-Region peering. A TGW attachment associates with one TGW route table but can propagate to multiple tables. VPC subnet route tables still must point to the TGW.

For centralized inspection, use routes and appliance mode/current capabilities to preserve symmetry across AZs and flows. With GWLB, build endpoint/service, appliance targets, health, GENEVE reachability, route chains and failure posture. Validate both return directions and bypass prevention.

PrivateLink implementation requires provider NLB/service acceptance/permissions and consumer interface endpoints/DNS. Endpoint policies, service identity/application authorization, security groups and provider controls remain distinct.

### 2.3 Implement DNS without loops or hidden coupling

Build public/private zones, associations, resolver endpoints, rules, RAM shares, delegation, DNSSEC and logging from a written query-flow diagram. Resolver endpoints need suitable subnets/IP capacity/security-group rules and resilient placement. Forward only intended suffixes; broad reciprocal forwarding can loop.

Test from each client class and network: record type, expected authoritative answer, resolver used, query logs, TTL/negative cache, failover answer and behavior when an endpoint/resolver is lost. Flush or wait for caches deliberately during tests. For multi-account private zones, document association authorization and lifecycle.

### 2.4 Automate network infrastructure safely

Use CloudFormation/CDK/Terraform or supported APIs/SDKs/CLI to version VPCs, IPAM pools, subnets, routes, TGWs, endpoints, resolver rules, security, logs and alarms. Parameterize environment-specific prefixes, ASNs, IDs and Regions; avoid copied hard-coded identifiers and overlapping CIDRs.

Add linting, policy checks, route/reachability intent tests, change sets/plans, sandbox deployment, canary account/Region, approval for blast-radius changes, drift detection, rollback and post-change active tests. Event-driven automation should be idempotent, rate-limited, evidence-preserving and bounded. Do not auto-remediate a route or firewall change without accounting for intended exceptions and active incidents.

**Related item:** A syntactically valid route-table change can still partition an organization. Network CI needs semantic tests: required paths remain, forbidden paths stay blocked, return paths and inspection remain symmetric, and advertisements do not exceed boundaries.

## 3. Network Management and Operation — 20%

### 3.1 Maintain route intent and convergence

Maintain an authoritative IP/prefix/ASN inventory, topology, route ownership, advertisement policy, TGW association/propagation, VIF/tunnel state, quotas, certificates/keys, firmware/vendor support and change history. Summarize routes only where the aggregate does not advertise unreachable space or defeat segmentation.

When paths change, compare expected with actual at every decision point. Longest-prefix match usually dominates, but selection between static/propagated routes and BGP paths is context-specific. Confirm source/destination, table, candidate routes, chosen next hop, advertisement and return path rather than guessing from a high-level diagram.

For active/passive or load sharing, test normal and partial failures. A BGP session can remain up while the application path is unusable. Use health-aware routing/automation where requirements demand it and avoid flapping through hysteresis/dampening designs.

### 3.2 Troubleshoot in layers with evidence

Use a consistent sequence:

1. Reproduce a precise five-tuple/name/time/client symptom and compare a working path.
2. Resolve DNS and confirm address/TTL/authority.
3. Check source host/interface/subnet route, then every gateway/TGW/appliance/on-prem route and the return path.
4. Check SG stateful rules, NACL stateless rules both ways, endpoint/resource policies, firewall/WAF rules and appliance health.
5. Inspect flow logs and service access/error logs; correlate timestamps, ENIs, NAT translations and connection IDs.
6. Check MTU/MSS/PMTUD, fragmentation, packet-per-second/bandwidth/connection tracking, ephemeral ports, NAT ports, quotas and load-balancer target health.
7. Use Reachability Analyzer for modeled AWS configuration and Traffic Mirroring/capture for permitted packet-level questions; neither replaces application logs.
8. Make the smallest reversible change, validate intended and forbidden paths, then record cause and prevention.

Flow Logs are metadata, not payload capture; `ACCEPT` means the logged interface policy accepted the flow, not that the application replied. Traffic Mirroring has source/target/filter/support and cost constraints. Reachability Analyzer analyzes configuration, not live packet success or external device state.

### 3.3 Optimize throughput, reliability, and cost

Performance depends on the narrowest effective constraint: instance/network interface, per-flow behavior, packets per second, placement, load balancer, NAT/firewall, VPN/DX, TGW, destination, MTU or application window. ENA provides enhanced networking for supported instances; EFA adds OS-bypass capabilities for tightly coupled HPC/ML traffic; an ENI is the virtual network interface construct. Select by workload and instance support.

Jumbo frames help only when the entire relevant path supports the MTU; otherwise fragmentation or black holes can result. Validate PMTUD and use MSS adjustment where appropriate. More bandwidth does not fix latency-bound chatty protocols.

Improve availability with diverse connections/devices/locations, multi-AZ endpoints/appliances, tested DNS/route failover, sufficient subnet IPs, quota headroom and failure-domain-aware routing. Add secondary CIDRs or redesign subnet allocation before auto-scaling exhausts addresses.

Optimize cost by modeling hourly attachment/gateway/endpoint/appliance charges plus per-GB processing, inter-AZ, cross-Region, internet egress, NAT, TGW, PrivateLink, CloudFront/GA, DX port/outbound and logs. Place traffic deliberately, use endpoints/caching/aggregation where justified, and avoid hairpin inspection or NAT paths without a policy reason.

## 4. Network Security, Compliance, and Governance — 24%

### 4.1 Build controls from flows and threats

Inventory ingress, egress, east-west, hybrid, administration, service endpoints, DNS and control-plane flows. For each, define source/destination identity/prefix, protocol, business purpose, data class, trust transition, authentication/authorization, encryption, inspection, logging, owner and exception.

- **Security groups** are stateful, attach to supported resources/ENIs and allow traffic. Referencing another SG expresses membership for supported paths; it does not create routing.
- **Network ACLs** are stateless subnet-bound allow/deny lists evaluated by numbered order; include return/ephemeral traffic.
- **WAF** filters supported Layer-7 web requests. **Shield** supplies DDoS protections/service levels. Neither is a generic east-west firewall.
- **Network Firewall** provides managed stateful/stateless network inspection. **GWLB** integrates third-party virtual appliances. Design routing symmetry, scaling, updates, logging, bypass prevention and failure posture.
- **Firewall Manager** applies supported policies across accounts/resources. Config, Security Hub, Network Access Analyzer, Reachability Analyzer and Trusted Advisor provide different evidence/finding roles.
- Endpoint policies, resource policies, IAM and service controls restrict service operations; network reachability alone is not authorization.

Use segmentation/zero-trust principles to minimize implicit reachability. Separate workload environments, tenants, regulated zones, shared services, management and inspection. Test both positive and negative intent continuously.

### 4.2 Audit configuration and traffic centrally

Collect organization-wide CloudTrail, Config, Flow Logs, TGW/network firewall/WAF/LB/CloudFront/DNS logs and security findings to protected destinations with retention and access aligned to policy. Include sufficient flow-log fields for interface, addresses, ports, action, traffic path and service context where supported.

Correlate control-plane change → route/security configuration → flow decision → appliance/edge decision → application result. Alert on disabled logging, permissive exposure, unexpected routes/prefixes, tunnel/BGP changes, firewall bypass, rejected spikes, anomalous egress, DNS anomalies, certificate expiry and log-delivery failure.

Govern changes with IaC, peer review, separation of duties, policy-as-code, exception expiry, change windows, rollback, active validation and tamper-resistant evidence. Sampling and log exclusions must be justified; “centralized” without query ownership and response is merely storage.

### 4.3 Protect confidentiality in transit

Match encryption to threat and hop:

- TLS protects application sessions; decide termination/passthrough/re-encryption, certificate authority, name validation, mTLS, rotation and cipher policy.
- IPsec protects IP traffic across VPNs; verify algorithms, lifetime/rekey, PFS, tunnel endpoints and monitoring.
- VPN over Direct Connect adds IPsec to private connectivity; MACsec can protect supported physical DX links but does not replace end-to-end/application encryption.
- CloudFront, ALB/NLB, API services, managed databases/S3 endpoints and custom instances each have distinct TLS capabilities. Validate every hop, not just client-to-edge.
- DNSSEC authenticates signed DNS data; DNS over HTTPS/TLS support and resolver architecture are separate concerns. DNSSEC does not encrypt ordinary DNS content.

Use ACM for supported public certificates and ACM Private CA for managed private PKI use cases. Define issuance authority, templates, revocation/status, distribution, renewal, private-key protection and audit. A certificate deployment is incomplete without expiry/failure testing.

**Related item:** Encryption can obscure inspection. Choose termination and inspection points deliberately, minimize decrypted exposure, restrict operator access, and preserve metadata/evidence required by compliance.

## Integrated scenarios

### Scenario 1: Global multi-account application

Design global HTTP and TCP ingress for three Regions, private application accounts, centralized egress/inspection, shared services and strict tenant separation. Compare CloudFront, Global Accelerator, Route 53, ALB/NLB, TGW, PrivateLink and GWLB. Show DNS, forward/return routes, failure behavior, source IP, TLS, WAF/firewall, logs, active tests and all data-processing/inter-AZ costs.

### Scenario 2: Resilient hybrid enterprise

Two data centers use MPLS/SD-WAN, overlapping acquired prefixes and a compliance mandate for encryption. Design diverse Direct Connect/VPN/TGW Connect paths, VIF/gateway associations, BGP advertisements and influence, hybrid DNS, overlap isolation/translation, MTU, monitoring, failover tests and ownership. Explain why link-up/BGP-up is insufficient health.

### Scenario 3: Intermittent production failure

Clients see sporadic resets and large transfers fail after a firewall insertion. Small requests work; one AZ is worse. Build a timeline and inspect DNS, LB health/cross-zone behavior, TGW routes/appliance mode, GWLB target health, symmetry, security rules, flow logs, NAT/connection tracking, MTU/PMTUD and packet captures. Propose the smallest safe remediation and regression tests.

## Practice labs

Use disposable accounts/resources, synthetic data, budgets and teardown evidence. Direct Connect can be modeled when physical access is impractical; label what was simulated.

### Lab 1: Packet-path workbook — 120–180 minutes

For internet-to-ALB, VPC-to-S3 endpoint, spoke-to-spoke through TGW, and hybrid DNS flows, enumerate every name, route table, policy, translation, stateful/stateless rule, encryption hop, log and return path. Predict outcomes before testing.

### Lab 2: Multi-account Transit Gateway segmentation — 180–300 minutes

Create or model prod, nonprod, shared-service and inspection attachments with distinct route tables, associations/propagations and RAM ownership. Prove required paths and blocked paths, introduce a route leak, detect it, roll back and calculate hourly/per-GB costs.

### Lab 3: Hybrid BGP and failure simulation — 180–300 minutes

Use a safe virtual router/VPN lab or detailed route simulator. Advertise controlled prefixes, influence active/passive or ECMP behavior, fail a tunnel/session, measure convergence, test return symmetry and document how a physical DX design would differ.

### Lab 4: Centralized hybrid DNS — 180–300 minutes

Build private zones, inbound/outbound Resolver endpoints/rules and query logging across at least two namespaces. Test delegation/forwarding, TTL and negative caching, endpoint failure, split-horizon behavior and a deliberately prevented forwarding loop.

### Lab 5: Load balancer and service insertion comparison — 180–300 minutes

Implement small ALB and NLB paths and model or deploy a safe GWLB flow. Compare client IP, protocol/TLS termination, target health, cross-zone behavior, logs, source/return routing, failure, scaling and cost. Explain where WAF fits.

### Lab 6: Evidence-driven troubleshooting — 180–300 minutes

Enable Flow Logs and appropriate service logs, establish healthy baselines, then inject route, NACL, SG, DNS, target-health and MTU symptoms. Use Reachability Analyzer plus log/capture evidence to localize each fault without random changes.

### Lab 7: Network security and encryption audit — 180–300 minutes

Create a flow/control matrix, audit routes, SGs, NACLs, endpoints, firewalls and certificates, test forbidden paths, and trace a TLS session across termination/re-encryption. Add an exception with owner/expiry and prove the monitoring/response path.

### Lab 8: Network delivery pipeline — 180–300 minutes

Version a reusable VPC/TGW/DNS or firewall module. Add lint/policy tests, CIDR collision checks, required/forbidden reachability assertions, change preview, canary deployment, drift detection, rollback and post-change active probes.

## Knowledge checks

1. When does CloudFront fit better than Global Accelerator?
2. Why can Route 53 health failover take longer than a health-check interval?
3. Which direction does a Route 53 Resolver inbound endpoint serve?
4. How can reciprocal broad DNS forwarding fail?
5. Why is NLB commonly paired with PrivateLink providers?
6. What must be true for stateful appliance insertion to work reliably?
7. What does a Flow Log `ACCEPT` record not prove?
8. What can Reachability Analyzer prove, and what can it not?
9. Why does a Direct Connect connection not by itself satisfy encrypted high availability?
10. Which VIF/gateway pattern reaches a Transit Gateway through Direct Connect?
11. Why can a LAG still share a failure domain?
12. What inputs determine BGP path selection and influence?
13. Why is summarization potentially dangerous across security zones?
14. When does PrivateLink fit better than TGW?
15. Why can overlapping CIDRs not simply attach and route through TGW?
16. What is the ownership tradeoff in VPC sharing?
17. Which route tables must be considered for a TGW VPC path?
18. What does TGW route-table association differ from propagation?
19. Why test both Direct Connect/VPN failure directions?
20. What must an automated route change test beyond syntax?
21. How can DNS caches mislead a failover test?
22. Why should resolver endpoints have multiple AZ placements?
23. What evidence distinguishes a route problem from an SG problem?
24. Why might large packets fail while small packets work?
25. What is the difference between ENI, ENA, and EFA?
26. Why can more link bandwidth fail to improve a chatty application?
27. Which subnet resource can stop otherwise healthy scale-out?
28. What costs should be included in a centralized inspection design?
29. How do security groups and NACLs differ in state and evaluation?
30. Why does referencing a security group not create connectivity?
31. Which controls protect Layer-7 web requests versus arbitrary IP flows?
32. What must a firewall fail-open/fail-closed decision consider?
33. Why centralize network logs across accounts?
34. What does CloudTrail add that packet/flow evidence does not?
35. Why is network reachability not service authorization?
36. How does VPN over Direct Connect differ from Direct Connect alone?
37. What does DNSSEC protect, and what does it not protect?
38. What certificate lifecycle elements follow issuance?
39. Why can TLS termination conflict with inspection requirements?
40. What lifecycle warning must an ANS-C01 learner see in September 2026?
41. Is an AWS replacement certification announced for ANS-C01?
42. What makes a network incident conclusion evidence-based?

### Answer guide

1. For HTTP(S) CDN caching, origin protection and edge request processing; GA fits TCP/UDP anycast path optimization without object caching.
2. Authoritative health decisions interact with record TTL, recursive/client caches and connection reuse.
3. It accepts DNS queries originating from connected external/on-premises networks into the VPC resolver path.
4. Queries can bounce between resolvers until timeout, creating intermittent delay/failure.
5. NLB is a supported scalable Layer-4 provider front end with the addressing/endpoint-service integration PrivateLink requires.
6. Forward and return flows must traverse a healthy corresponding appliance path with correct routes, appliance mode/state and GENEVE/security behavior.
7. That an application replied, return routing worked, an external device allowed it, or the payload was correct.
8. It evaluates modeled AWS configuration reachability; it does not send live packets or know application/external-device runtime state.
9. DX requires deliberate connection/device/location diversity and encryption such as supported MACsec or IPsec where the threat model requires it.
10. A transit VIF through a Direct Connect gateway associated with the Transit Gateway.
11. Member links can terminate at the same DX location/device and therefore lack physical/location diversity.
12. Advertised/accepted prefixes, longest prefix, each router's policy, local preference/weight, AS path, MED/communities and ECMP/current AWS behavior.
13. An aggregate may claim unreachable space or cross a segmentation boundary, causing black holes or leaks.
14. When consumers need access to a specific private service without full routed reachability, including overlap/isolation cases.
15. Identical destinations are ambiguous; isolate behind services/proxies, translate, or renumber.
16. Central network ownership/consistency improves, but subnet/routes versus participant workload/security responsibilities must be explicit.
17. Source subnet route, source/target attachment behavior, associated TGW route table/propagation/static route, target subnet route and any inspection/appliance routes.
18. Association selects the table used to route traffic arriving from an attachment; propagation publishes attachment routes into selected tables.
19. Convergence, symmetry, sessions and on-prem/AWS policy may differ by failure and recovery direction.
20. Required paths, forbidden paths, advertisement boundaries, return symmetry, inspection and active application behavior.
21. Old positive or negative answers can persist until TTL/cache expiry even after authoritative state changes.
22. To avoid one endpoint/AZ becoming a name-resolution failure domain and to support expected availability.
23. Route/reachability analysis establishes candidate path; Flow Log action, SG/NACL evaluation and targeted tests localize filtering.
24. MTU mismatch, blocked ICMP/PMTUD, missing MSS adjustment or fragmentation behavior can create a black hole.
25. ENI is the virtual interface; ENA is enhanced networking; EFA adds specialized OS-bypass capabilities for supported HPC/ML workloads.
26. Round-trip latency and serial protocol exchanges, not capacity, can dominate completion time.
27. Available IP addresses (and related ENI/target quotas) in the scaling subnets.
28. Gateway/endpoint/appliance hours, licenses, per-GB processing, inter-AZ/cross-Region, NAT/TGW/GWLB, compute, logs and operations.
29. SGs are stateful allow rules on supported interfaces/resources; NACLs are stateless ordered allow/deny rules at subnets with return traffic explicit.
30. The reference authorizes matching traffic for supported paths; routing, target state and other policies still must work.
31. WAF handles supported HTTP(S) request filtering; Network Firewall or GWLB appliances handle appropriate IP flows, with Shield for DDoS protection.
32. Safety, availability, compliance, bypass risk, application behavior, detection, manual recovery and the failure scope.
33. To preserve evidence outside workload control, correlate cross-boundary paths and support consistent detection/audit/retention.
34. Who/what changed control-plane configuration and when, rather than data-plane flow/payload behavior.
35. IAM, resource and endpoint policies plus application authentication/authorization govern operations after a route exists.
36. It runs IPsec over the private DX path; plain DX does not inherently encrypt traffic.
37. It authenticates signed DNS data/integrity and denial; it does not encrypt ordinary DNS queries or guarantee endpoint/application trust.
38. Validation, secure key handling, deployment, renewal/rotation, revocation/status, expiry monitoring, audit and failure recovery.
39. Decryption is needed for some content inspection but expands plaintext exposure; termination, re-encryption, access and evidence must be designed.
40. The exam is scheduled to retire December 31, 2026; older/localized sources may still show August 25, so verify live scheduling.
41. No; AWS points to continued Skill Builder networking education but names no replacement certification as of September 1.
42. A precise symptom, timestamped multi-hop evidence, tested hypotheses, smallest reversible fix, validation of allowed/denied paths and documented prevention.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Because ANS-C01 retires December 31, only start an exam-specific plan if the remaining schedule is realistic. The technical content remains valuable after certification retirement.

| Resource | Access | Estimated time |
|---|---|---:|
| AWS exam guide and retiring Skill Builder plan | Public/free-account/subscription mix | 35–60 hours selected plus labs |
| Pluralsight ANS-C01 path | Paid/trial | 53+ hours including legacy path; select current modules |
| O'Reilly 2025 Packt certification guide | Paid/trial | 16 hours 52 minutes listed plus labs |
| Udemy/Maarek-Agrawal current course | Paid | 35 hours 28 minutes plus labs |
| Whizlabs course/practice/labs | Paid | 45–80 hours estimated |

- **Official route:** current guide, live [retiring certification page](https://aws.amazon.com/certification/certified-advanced-networking-specialty/), [AWS networking study areas](https://aws.amazon.com/blogs/training-and-certification/10-study-areas-for-the-aws-certified-advanced-networking-specialty-exam/), and the [Skill Builder networking/ANS plan](https://explore.skillbuilder.aws/learn/public/learning_plan/view/89/networking-learning-plan) (**about 35–60 selected hours plus deep labs**). Skill Builder labels the English plan as retiring December 31.
- **Structured path:** [Pluralsight ANS-C01](https://www.pluralsight.com/paths/aws-certified-advanced-networking-specialty-ans-c01) (**about 13 hours current modular courses plus listed labs, or 40 hours 4 minutes for the legacy course**). Prefer the 2025–2026 domain modules; add substantial labs.
- **Current book:** [O'Reilly / Packt ANS-C01 Certification Guide](https://www.oreilly.com/library/view/aws-certified-advanced/9781835080832/) (**650 pages / 16 hours 52 minutes listed**, February 2025) or [Sybex 2nd Edition](https://www.oreilly.com/library/view/aws-certified-advanced/9781394171859/) (**592 pages / 17 hours 34 minutes**, October 2023; gap-check current features).
- **Compact video supplement:** [O'Reilly / Chad Smith ANS-C01](https://www.oreilly.com/library/view/aws-certified-advanced/9780138319311/) (**4 hours 19 minutes**, November 2023); use for scenario review, not as the sole route.
- **Current long-form course:** [Udemy/Stéphane Maarek and Chetan Agrawal ANS-C01](https://www.udemy.com/course/aws-certified-advanced-networking-specialty-ans/) (**35 hours 28 minutes**, 267 lectures, hands-on content; shown updated August 2026).
- **Compact alternative:** [Udemy/Neal Davis ANS-C01](https://www.udemy.com/course/aws-advanced-networking-specialty-ans/) (**12 hours 7 minutes**, practical exercises and practice exam; shown updated August 2026).
- **Lab/practice route:** [Whizlabs ANS-C01](https://www.whizlabs.com/aws-advanced-networking-speciality/) (**45–80 selected hours estimated**; page lists 103 videos, 54 labs, nine practice quizzes and sandbox access).

No exact current Tutorials Dojo or MeasureUp ANS-C01 product was independently verified September 1. Avoid recalled-question products. Suggested preparation is **140–220 hours** for an experienced network engineer and **250–400 hours** when core routing/BGP, DNS, security and hybrid prerequisites are still developing—subject to the retirement deadline.

---

## Source map and freshness notes

The root and four domain pages define the current technical assessment contract; the English certification page defines the retirement and live delivery contract. Several localized pages still show the earlier August 25 date, so the English page and scheduler take precedence for a candidate booking now. No replacement certification is announced.

- **VERIFY CURRENT:** December 31 availability, service/features, route preference, supported Regions, quotas, bandwidth/packet/connection limits, MTU, encryption, logging fields, pricing and training availability.
- **Stable troubleshooting pattern:** exact flow/name → control-plane route/DNS → state/security/translation → forward and return data plane → measured evidence → smallest reversible correction → regression/intent automation.
- **After retirement:** retain this page as a high-value AWS networking reference while clearly removing it from active-certification recommendations.

This guide uses no recalled exam questions or restricted content. The knowledge checks are original and test published concepts rather than reproducing vendor items.
