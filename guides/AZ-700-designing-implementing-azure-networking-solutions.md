---
exam_code: AZ-700
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AZ-700 Designing and Implementing Microsoft Azure Networking Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-700-coverage-record). The [official AZ-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700) is authoritative.

**Current baseline:** Skills measured as of July 27, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)

## How to use this guide

AZ-700 combines design, implementation, and troubleshooting. Learn every service as part of a packet’s complete journey: name resolution, chosen address, route, filter, translation, gateway or proxy, health decision, return path, and observable evidence. A diagram that shows boxes without prefixes, route propagation, DNS zones, security boundaries, and failure paths is not finished.

Practice with a disposable Azure subscription and infrastructure as code where possible. Azure gateways and security services can incur meaningful cost and take time to deploy or remove; estimate cost first and clean up deliberately.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Network-engineering question |
|---|---:|---|
| Design and implement core networking infrastructure | 25–30% | Are addressing, DNS, connectivity, routing, egress and diagnostics correct and scalable? |
| Design, implement, and manage connectivity services | 20–25% | Which resilient VPN, ExpressRoute or Virtual WAN design connects users, sites and networks? |
| Design and implement application delivery services | 15–20% | Which Layer 4, Layer 7 or DNS service should receive, inspect and steer application traffic? |
| Design and implement private access to Azure services | 10–15% | How will PaaS access become private or subnet-restricted without breaking DNS or authorization? |
| Design and implement Azure network security services | 15–20% | Where should segmentation, inspection, WAF and centralized policy be enforced and observed? |

---

## 1. Packet-walk and troubleshooting model

For every flow, write both directions explicitly:

```text
source identity/process
-> DNS query and answer
-> source IP/interface/subnet
-> effective route / next hop
-> NSG and service/firewall policy
-> NAT, gateway, proxy or load-balancer decision
-> destination listener and application
-> return route, filter and translation state
-> logs, metrics and packet/connection evidence
```

Five questions locate most failures:

1. **Did the name resolve to the intended address from this client?**
2. **Which route and next hop were effective in each direction?**
3. **Which control allowed or denied the flow?**
4. **Was the service healthy and listening on the address/port the intermediary tested?**
5. **Which evidence proves the first failing layer?**

Do not treat “the NSG allows it” as a complete diagnosis. The guest firewall, service firewall, route, DNS, health probe, application listener, TLS name, proxy policy, or return path may still fail.

> **Related item:** Azure’s software-defined network can preserve state for an allowed flow, but appliances, asymmetric paths, multiple NICs, load balancers and on-premises devices introduce their own state and routing behavior. Draw the path instead of assuming symmetry.

---

## 2. Design and implement core networking infrastructure (25–30%)

### IP addressing and segmentation

Plan address space before deployment:

- inventory on-premises, branch, partner, other-cloud, VNet and planned prefixes;
- avoid overlap anywhere that may route or peer;
- reserve growth for regions, environments, acquired networks and platform services;
- align subnet size to scale behavior, not current instance count;
- record ownership and allocation in an IP address management system;
- distinguish address segmentation from security segmentation.

Azure reserves addresses in every subnet. Some platform services require a named dedicated subnet, minimum size, delegation, or special route/NSG behavior. Examples include gateways, Azure Firewall, Application Gateway, Bastion, private endpoints, VNet-integrated services and delegated PaaS resources. **VERIFY CURRENT:** exact subnet names, minimum sizes, coexistence rules, delegations and policy support in workload documentation.

| Subnet approach | Benefit | Risk |
|---|---|---|
| Shared application subnet | Fewer prefixes and policy objects | Larger blast radius and mixed lifecycle/service constraints |
| Dedicated tier/service subnet | Clear routing, delegation and security boundary | More address consumption and operational objects |
| Very small subnet | Conserves address space today | Blocks autoscale, upgrades, blue-green capacity or private endpoints later |
| Large flat subnet | Simple initial deployment | Broad policy, noisy dependency discovery and difficult segmentation |

A subnet delegation grants a supported service permissions to manage resources in the subnet; it is not equivalent to a service endpoint or private endpoint. A service association link represents that integration and may constrain subnet changes.

Public IPs are Azure resources with SKU, regional/zonal, allocation, routing-preference and association behavior. A public IP prefix reserves a contiguous Azure-provided block for predictable allocation. Custom IP prefix/BYOIP requires ownership validation and staged commissioning before use. **VERIFY CURRENT:** IPv4/IPv6, prefix sizes, tier/SKU, availability zones, routing preference and association support in the [public IP documentation](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses).

### Name resolution

Design DNS by namespace and query origin:

| Need | Component | Key dependency |
|---|---|---|
| Public authoritative zone | Azure DNS public zone | Registrar/parent-zone delegation to assigned name servers |
| Private records for linked VNets | Azure Private DNS zone | Correct VNet links, optional autoregistration, non-conflicting namespace |
| Hybrid query forwarding without DNS VMs | Azure DNS Private Resolver | Inbound/outbound endpoints, rulesets, VNet links, on-premises forwarders and routes |
| Custom resolver/appliance | DNS server/NVA | VNet DNS settings, forwarding to Azure-provided resolver, availability and patching |

VNet DNS setting changes affect DHCP-provided resolver configuration; clients may need lease renewal or restart. Private DNS zone links determine visibility; autoregistration has separate support and one-zone-per-VNet constraints. Conditional forwarding must avoid loops.

Private endpoint DNS works because the normal service FQDN ultimately resolves to a private IP for clients using the private view. Use the recommended `privatelink` zone for the service, link it to the right resolver path, and test from Azure and on-premises. Hard-coding the private endpoint’s IP bypasses service names and TLS/endpoint lifecycle.

Use `nslookup`, `Resolve-DnsName`, `dig`, resolver logs where available, and queries from the actual client network. A successful lookup from a laptop does not prove resolution from a VM, container, App Service integration subnet, or on-premises server.

See [Azure DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview) for current endpoint and ruleset behavior.

### VNet connectivity, routing and egress

#### Peering and gateway transit

VNet peering supplies private IP connectivity over the Azure backbone. Peering is non-transitive: A-to-B and B-to-C do not automatically provide A-to-C. Each direction is a separate peering object with settings such as virtual-network access, forwarded traffic, and gateway use/transit.

Gateway transit lets a spoke use a compatible gateway in a hub when the hub allows transit and the spoke uses the remote gateway. A VNet cannot use multiple remote gateways in the same way; understand gateway and peering constraints before centralizing.

Azure Virtual Network Manager can group networks and deploy connectivity or security-admin configurations at scale. Mesh and hub-and-spoke topology intent does not eliminate address planning, DNS, route, gateway and application dependencies. Stage deployments and understand regional/scope/feature support.

#### Route selection

Azure creates system routes, learns BGP routes from gateways/Route Server, and applies user-defined routes (UDRs). Longest prefix match is evaluated first; route-source rules decide between equally specific candidates. Inspect **effective routes** rather than only the route-table resource.

| Next hop | Use | Caution |
|---|---|---|
| Virtual network | Within VNet | Address space changes affect system routes |
| Virtual network gateway | VPN/ExpressRoute learned or explicit path | Propagation and gateway coexistence matter |
| Virtual appliance | Firewall/router/NVA | Appliance IP forwarding, health and symmetric return path |
| Internet | Azure internet edge path | Public exposure and platform egress behavior remain separate |
| None | Drop matching traffic | More-specific routes can still win |

Forced tunneling sends selected internet-bound traffic through a central or on-premises inspection path. Account for control-plane/service dependencies, platform service tags, asymmetric routing, SNAT, throughput and outage behavior. Disabling gateway route propagation can prevent unintended learned routes but can also remove required connectivity.

Azure Route Server exchanges BGP routes with supported NVAs so routes can change dynamically. It does not forward data traffic itself. Design ASN, peering IPs, route limits, redundancy, branch-to-branch behavior and interaction with gateways. **VERIFY CURRENT:** coexistence, route exchange and supported NVA behavior.

Azure NAT Gateway provides scalable, explicit outbound SNAT for supported subnet flows. It does not accept unsolicited inbound connections or act as a firewall. Subnet association, public IP/prefix, idle timeout, zone model and port consumption matter. Avoid depending on implicit/default outbound access; design egress explicitly using [NAT Gateway guidance](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview).

> **Related item:** SNAT port exhaustion is a state-capacity problem. Connection reuse, destination tuple distribution, idle timeouts, scale and the number of frontend addresses affect it. Adding compute without fixing outbound translation can worsen pressure.

### Monitor and troubleshoot networks

[Network Watcher](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview) and Azure Monitor network experiences expose different evidence:

| Tool/evidence | Question it answers |
|---|---|
| IP flow verify | Would NSG evaluation allow a specified five-tuple? |
| Effective security rules | Which subnet/NIC NSG rules combine for this interface? |
| Next hop/effective routes | Which route and next hop would Azure choose? |
| Connection troubleshoot / Connection Monitor | Is a path reachable, with what latency and failing layer? |
| Packet capture | What packets reach or leave a supported VM interface? |
| VPN troubleshoot | What gateway/connection configuration or state is failing? |
| Topology | Which resources and relationships exist in scope? |
| Flow logs | What accepted/denied flow metadata was observed? |

The July 2026 blueprint explicitly names **virtual network flow logs**. Treat legacy NSG flow-log material cautiously and check current migration/retirement guidance. Flow logs show network-flow metadata; they are not payload capture or application logs. Plan storage/analytics destination, retention, schema, Traffic Analytics integration, cost and access.

DDoS monitoring and protection require a public endpoint threat model, protected resource scope, telemetry and response plan. Microsoft Defender for Cloud Secure Score, attack path analysis and Cloud Security Explorer identify posture relationships and potential paths; recommendations require workload context and do not replace packet-path verification. **VERIFY CURRENT:** plan names, supported resources, query capabilities and licensing.

#### Domain failure modes

- Allocating overlapping prefixes or leaving no subnet capacity for scale/upgrade.
- Placing a service in a shared subnet despite delegation or dedicated-subnet requirements.
- Linking a private DNS zone to only the endpoint VNet, not the clients’ resolver path.
- Assuming peering is transitive or that gateway-transit settings are one-sided.
- Inspecting a UDR but not the NIC’s effective routes and return path.
- Using NAT Gateway as if it provided inbound load balancing or security inspection.
- Reading a flow log as proof that the application completed a request.

---

## 3. Design, implement, and manage connectivity services (20–25%)

### Site-to-site VPN

A site-to-site connection combines:

```text
Azure VNet + GatewaySubnet + VPN gateway
+ local network gateway (on-prem endpoint and prefixes/BGP)
+ connection (shared key, protocol/IPsec/IKE policy, BGP settings)
+ on-premises VPN device and matching routes/policies
```

Route-based VPNs generally use traffic selectors and routing/BGP suitable for modern multi-prefix designs; policy-based VPNs define static encryption domains and fit specific legacy requirements. Do not infer compatibility—verify the device and Azure configuration.

For high availability, consider active-active gateways, zone-redundant SKUs, multiple on-premises devices and links, BGP, connection redundancy, and shared dependencies. Two tunnels over one ISP or one customer router do not remove that failure domain. Configure and test failover, convergence and expected traffic symmetry.

Custom IPsec/IKE policies must match encryption, integrity, Diffie-Hellman/PFS, SA lifetime and selector expectations. A tunnel can be “connected” while application traffic fails because prefixes, BGP, UDR, NSG, MTU/MSS, NAT or return routes are wrong. Use [VPN Gateway documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/) and device-specific guidance.

Azure Extended Network extends selected on-premises subnets to Azure for migration scenarios. It is not a general replacement for routed connectivity; validate scale, latency, topology, supported workload and lifecycle constraints.

### Point-to-site VPN

P2S connects individual clients to a VNet. Select:

- gateway SKU and capacity;
- tunnel type such as OpenVPN, IKEv2 or SSTP according to client/authentication needs;
- certificate, RADIUS, or Microsoft Entra ID authentication where supported;
- client address pool that does not overlap VNet, on-premises or client-local networks;
- routes advertised to the client and transit expectations;
- client package/profile distribution, versioning and revocation;
- DNS resolution and access controls after tunnel establishment.

Always On VPN and Azure Network Adapter have client/OS/topology requirements beyond “P2S exists.” When troubleshooting, separate tunnel establishment, authentication, assigned address, installed routes, DNS, authorization, filtering and application reachability.

### ExpressRoute

ExpressRoute provides private connectivity through a provider or direct model; it is not encrypted by default merely because it is private. Match the design to bandwidth, provider location, peering location, geography, resiliency, encryption, route and failover requirements.

| Feature | Purpose | Important distinction |
|---|---|---|
| Private peering | Reach private IPs in linked VNets | Requires VNet gateway/connections unless using supported direct patterns |
| Microsoft peering | Reach supported Microsoft public services | Public prefixes, route filters and validation requirements apply |
| Premium | Broader limits/geographic connectivity | Verify exact benefits and cost |
| Global Reach | Connect customer networks through Microsoft backbone | Not the same as connecting VNets to a circuit |
| FastPath | Bypass gateway data path for supported traffic | Gateway remains for control plane; support/limits vary |
| ExpressRoute Direct | Dedicated high-capacity ports into Microsoft edge | Customer/provider operational responsibility is greater |
| MACsec/IPsec options | Encrypt supported portions of the path | Scope, device and peering support differ |
| BFD | Faster supported failure detection | End-to-end convergence still includes routing/device behavior |

Design redundant circuits in different peering locations/providers when the availability requirement demands removal of those shared failures. Each circuit already has redundant physical connections, but an end-to-end design includes customer routers, last mile, provider, Microsoft edge, gateway, VNet and application.

BGP advertisements must be intentional. Avoid accepting or advertising more-specific/default routes that unintentionally hijack traffic. Check AS path, communities, route filters, prefixes, limits and propagation. Use [ExpressRoute documentation](https://learn.microsoft.com/en-us/azure/expressroute/) for current SKU, peering and resiliency behavior.

> **Related item:** VPN over ExpressRoute or other encryption designs add tunnel overhead, MTU, throughput and operational dependencies. “Private circuit” and “encrypted data in transit” are different requirements.

### Azure Virtual WAN

Virtual WAN provides Microsoft-managed virtual hubs for branch, P2S, ExpressRoute, VNet and supported NVA/security integration. Standard versus Basic capabilities differ. Plan:

- regions and hubs;
- VNet, branch and remote-user connections;
- VPN/ExpressRoute/P2S gateway scale units;
- hub route tables, labels, associations and propagations;
- routing intent and security provider/Azure Firewall behavior;
- branch-to-branch and inter-hub requirements;
- NVA integration and BGP;
- inspection symmetry, DNS and egress;
- failure domains, throughput and cost.

An association chooses the hub route table used to route a connection’s traffic; propagation determines which route tables learn its routes. Incorrect association/propagation can create isolation or bypass. Use the [Virtual WAN overview](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about) and inspect effective routes.

#### Domain failure modes

- Calling two tunnels “highly available” when they share one customer device and ISP.
- Matching the VPN shared key but not the IKE/IPsec policy or traffic selectors.
- Overlapping the P2S client pool with a client’s local or connected network.
- Assuming ExpressRoute traffic is inherently encrypted.
- Designing one ExpressRoute circuit/provider/peering location for a regional-DR requirement.
- Advertising an unintended default or more-specific BGP route.
- Configuring Virtual WAN routing labels without tracing associations and propagation end to end.

---

## 4. Design and implement application delivery services (15–20%)

### Choose by scope, layer and proxy behavior

| Service | Scope/layer | Traffic handling | Strong fit |
|---|---|---|---|
| Azure Load Balancer | Regional or cross-region Layer 4 | Flow load balancing/NAT; not an HTTP reverse proxy | TCP/UDP, internal/public frontends, high-performance pass-through-style flows |
| Traffic Manager | Global DNS | Returns endpoint DNS choice; client connects to endpoint | Protocol-agnostic global distribution where DNS behavior is acceptable |
| Application Gateway | Regional Layer 7 | HTTP(S) reverse proxy, TLS, routing and optional WAF | Regional web ingress, path/host routing and private frontend scenarios |
| Front Door | Global edge Layer 7 | Anycast edge proxy, acceleration, routing, caching and optional WAF | Global HTTP(S), multi-region origins, edge protection/acceleration |
| Gateway Load Balancer | Regional service chaining | Transparently inserts compatible virtual appliances | Scalable bump-in-the-wire NVA patterns |

Use the [Azure load-balancing decision guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview) and verify current tiers. A solution may compose Front Door globally with Application Gateway or Load Balancer regionally. Define which layer terminates TLS, evaluates health, preserves client identity and controls origin exposure.

### Azure Load Balancer and Traffic Manager

A load-balancer rule binds frontend IP/port/protocol, backend pool, health probe, session persistence and idle/reset behavior. Backend membership alone is insufficient; an unhealthy probe removes an instance from new flows. A probe should test a meaningful but efficient readiness endpoint that does not require authentication.

Inbound NAT rules target administrative or application ports on individual backends; they are not load-balanced service rules. Explicit outbound rules define SNAT behavior for supported backends, but NAT Gateway may be the preferred explicit scalable egress design. Model port allocation and connection scale.

Traffic Manager routing methods include priority, weighted, performance, geographic, multivalue and subnet patterns. DNS TTL and resolver/client caching affect failover convergence. Monitoring observes endpoints according to configured protocol/port/path; a healthy endpoint may still fail a different user flow.

### Application Gateway

Core relationships:

```text
frontend IP -> listener (host/port/TLS) -> routing rule
            -> backend pool + backend settings -> health probe
```

Plan a dedicated subnet, frontend visibility, autoscale/manual capacity, zones, listener type, certificates, end-to-end TLS, backend hostname/SNI, path/host routing, redirects, rewrites, cookie affinity, connection draining, private backend DNS and diagnostics.

TLS termination decrypts at the gateway. End-to-end TLS re-encrypts to the backend, which requires correct certificate trust and hostname. A backend certificate can be valid yet fail if the configured host name/SNI does not match. Application Gateway WAF is a separate policy decision, discussed in the security domain.

### Azure Front Door

Front Door terminates/proxies HTTP(S) at Microsoft’s global edge and chooses an origin by route, health, priority, weight and latency. Plan:

- profile tier and feature support;
- custom domain and certificate lifecycle;
- routes, patterns, protocols and forwarding behavior;
- origin groups, origins, host headers and health probes;
- caching/query-string/compression behavior;
- rules engine redirects, rewrites and header changes;
- WAF policy and bot/rate controls where supported;
- Private Link to supported origins or origin access restrictions;
- logs, metrics and regional-failure testing.

Caching can serve stale or inappropriate content if cache keys and dynamic/private responses are misunderstood. Private Link origin access is not the same as making the client connection private; clients still reach Front Door’s public edge. **VERIFY CURRENT:** Front Door tiers, Private Link origin support, caching/rules behavior and migration/retirement notices in [Front Door documentation](https://learn.microsoft.com/en-us/azure/frontdoor/).

#### Domain failure modes

- Choosing Traffic Manager when the requirement needs a Layer 7 proxy or immediate failover.
- Using Load Balancer for host/path routing or WAF.
- Blocking a platform health probe or requiring user authentication on its path.
- Configuring Application Gateway backend TLS without correct hostname/SNI and trust.
- Exposing a Front Door origin directly and assuming edge policy cannot be bypassed.
- Caching personalized or mutable responses without a correct cache-key/purge design.
- Ignoring SNAT port capacity for high outbound connection counts.

---

## 5. Design and implement private access to Azure services (10–15%)

### Private endpoint and Private Link service

A private endpoint creates a NIC with a private IP in the consumer VNet for a supported service subresource. Private Link carries supported traffic to the service without requiring its public endpoint in the client path. Success requires four independent gates:

```text
correct service subresource and endpoint approval/state
AND DNS resolves the service name to the endpoint private IP
AND route/filter path allows traffic
AND service/data authorization permits the caller
```

Plan endpoint placement, address capacity, policies, service subresources, multiple regions, endpoint approval, public-network access, DNS zones/records, VNet links, Private Resolver/on-prem forwarding, service firewall, monitoring and lifecycle. Storage may require separate private endpoints for blob, file, queue, table, web or DFS behaviors used by the workload.

A Private Link service publishes a customer-owned service behind a Standard Load Balancer so consumers can create private endpoints to it. Design NAT/source behavior, visibility/auto-approval, alias, frontend/backend, health, quotas and provider/consumer responsibility. It is different from consuming a Microsoft PaaS private endpoint.

See the [Private Link overview](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview).

### Service endpoints and policies

A service endpoint extends a subnet’s identity to a supported service over the Azure backbone while the service retains its public endpoint/IP. Configure the endpoint on the subnet and a virtual-network rule on the target service. Service endpoint policies can restrict supported outbound service destinations and add policy evidence.

| Requirement | Private endpoint | Service endpoint |
|---|---|---|
| Private IP in consumer VNet | Yes | No |
| Service public endpoint remains traffic target | No for the private path | Yes |
| On-premises access through connected VNet | Supported with DNS/routing design | Generally not by presenting an on-prem source as the Azure subnet |
| Per-service/subresource endpoint resource | Yes | No endpoint NIC; subnet enables service type |
| Consumer/provider approval workflow | For applicable Private Link services | No equivalent endpoint approval |
| DNS change central to design | Yes | Usually public service DNS remains |

Do not choose solely on cost. Use reachability, exfiltration control, on-premises needs, DNS, supported services, operations and public-access requirements. **VERIFY CURRENT:** endpoint network policies, service support, cross-region behavior and service-specific firewall semantics.

> **Related item:** App Service/Functions VNet integration primarily provides outbound access from the app into a VNet; a private endpoint provides private inbound access. Similar directional distinctions apply to other delegated PaaS integrations.

#### Domain failure modes

- Disabling public access before private DNS works from every client location.
- Creating only the blob endpoint when the application also uses DFS or file endpoints.
- Granting a data role but forgetting the service network firewall, or vice versa.
- Expecting a service endpoint to assign the PaaS service a private VNet address.
- Assuming a private endpoint makes all client-to-service names resolve privately.
- Confusing PaaS outbound VNet integration with inbound private access.

---

## 6. Design and implement Azure network security services (15–20%)

### NSGs, ASGs and flow logs

Network security groups are stateful Layer 3/4 filters with prioritized inbound and outbound rules. They can apply to a subnet and NIC; traffic must be allowed through the effective evaluation. Default rules remain unless a higher-priority custom rule overrides them.

Use service tags for Microsoft-managed address sets and application security groups for logical groups of NICs. Neither is application identity. Rule design should include owner, purpose, source, destination, protocol/port, priority, expiry/review and logging evidence.

Azure Virtual Network Manager security admin rules can establish centrally managed allow, always-allow or deny intent across managed networks, evaluated in relation to NSGs according to documented order. Verify current semantics before rollout; a central rule can have broad impact.

Use virtual network flow logs and IP flow verification for evidence, but remember that an allowed flow does not prove route, listener, TLS or application success. Review the [NSG overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

### Azure Firewall and Firewall Manager

Azure Firewall is a managed, stateful network firewall with SKU-dependent network, application, NAT, TLS inspection, IDPS and threat-intelligence capabilities. Select SKU from requirements rather than “more is safer.” Plan:

- hub/Virtual WAN topology and dedicated subnet/public IP requirements;
- zone availability and scale/performance;
- route symmetry and forced-tunnel design;
- DNAT, network and application rule collection groups/priorities;
- FQDN tags, service tags, DNS proxy and custom DNS;
- TLS inspection certificates/trust where supported;
- IDPS mode, threat intelligence and false-positive workflow;
- egress SNAT and private ranges;
- policy hierarchy, regional deployment and diagnostics.

Rule processing order matters. DNAT, network and application rules serve different traffic and identity/name use cases. FQDN-based application rules depend on DNS consistency between client and firewall; DNS proxy can help align observations. A UDR to the firewall is insufficient if the return path bypasses it.

Firewall Manager centralizes policies for secured virtual hubs and hub VNets. Parent/child policy inheritance supports central baselines with scoped additions, but teams need ownership and change/testing boundaries. A secure Virtual WAN hub combines managed hub routing and security; inspect routing intent and effective routes to prevent bypass.

Use [Azure Firewall documentation](https://learn.microsoft.com/en-us/azure/firewall/) for current SKU and policy behavior.

### Web Application Firewall

WAF protects supported HTTP(S) traffic at Application Gateway or Front Door. It is not a general network firewall, vulnerability scanner or secure-coding replacement.

| Decision | Questions |
|---|---|
| Placement | Regional Application Gateway or global Front Door? Can either be bypassed? |
| Mode | Detection for tuning or prevention for blocking? What is the promotion process? |
| Managed rules | Which ruleset/version and exclusions are required? |
| Custom rules | Match variables, priorities, rate limits, geo/IP logic and false positives? |
| Policy scope | Global, listener/domain/path association as supported? |
| Evidence | Logs, metrics, alerting, request correlation and incident owner? |

Start with representative traffic, review detections, correct applications where possible, make narrow documented exclusions, then move to prevention with monitoring. Broadly disabling a rule group to fix one false positive creates an avoidable gap. **VERIFY CURRENT:** ruleset versions, bot/rate-limiting support, policy association and limits in [Azure WAF documentation](https://learn.microsoft.com/en-us/azure/web-application-firewall/).

> **Related item:** DDoS protection addresses volumetric/protocol attacks against supported public resources; WAF addresses HTTP(S) application requests; Azure Firewall/NSGs control other network paths. Defense in depth requires the right control at the right layer.

#### Domain failure modes

- Treating an NSG as a next-generation firewall or application identity system.
- Applying both subnet and NIC NSGs without evaluating their combined effective rules.
- Sending traffic to a firewall in one direction while the return path bypasses it.
- Writing an application FQDN rule while client and firewall resolve different answers.
- Deploying TLS inspection without certificate trust, privacy and unsupported-traffic planning.
- Switching WAF directly to prevention without observing representative traffic.
- Fixing one WAF false positive with an unnecessarily broad exclusion.

---

## 7. Integrated scenarios

### Scenario A — private hub-and-spoke application

Requirement: two application spokes, shared egress inspection, private PaaS data, on-premises connectivity and regional HTTPS ingress.

1. Allocate non-overlapping hub/spoke prefixes with dedicated gateway, firewall and application subnets plus room for private endpoints.
2. Peer hub and spokes with forwarded traffic and correct gateway-transit settings; do not assume spoke-to-spoke transit.
3. Put UDRs on spoke workload subnets for inspected egress/inter-spoke paths and prove symmetric return routing.
4. Connect on-premises with a resilient route-based/BGP VPN design; advertise only intended prefixes.
5. Use Application Gateway with private or public frontend as required, correct probe, backend DNS/TLS and WAF policy.
6. Create data-service private endpoints and central/private DNS links plus Private Resolver forwarding for on-premises clients.
7. Restrict PaaS public access after the private path and workload authorization are proven.
8. Centralize Firewall policy and diagnostics while keeping NSGs for subnet/tier boundaries.
9. Test DNS, effective routes, IP flow, firewall decisions, health probes and the application transaction in both directions.

### Scenario B — global resilient web service

Requirement: users in multiple geographies, two Azure regions, edge WAF, origin not directly public, and controlled failover.

1. Use Front Door for global Layer 7 entry, custom domains/TLS, WAF, routing and health.
2. Configure an origin group with priority/weight/latency behavior that matches active-active or active-passive intent.
3. Secure supported origins with Private Link or explicit origin restrictions; ensure the app validates the intended host/proxy path.
4. Make the health endpoint reflect critical readiness without causing expensive dependency load.
5. Define caching only for safe content and include query/header/key behavior and purge workflow.
6. Send logs/metrics to an owned monitoring path and alert on edge health, origin health, WAF blocks and user-flow symptoms.
7. Fail one origin and measure probe interval, routing convergence, capacity, data behavior and recovery/failback.

---

## 8. Hands-on labs

### Lab 1 — Address plan and subnet constraints

1. Create an IP inventory for on-premises, two regions, hubs and four spokes.
2. Allocate prefixes with growth and identify every service needing a dedicated/delegated subnet.
3. Calculate usable addresses and simulate autoscale/upgrade headroom.
4. Deploy a subset using Bicep or Terraform and export an IPAM-style record.

### Lab 2 — Hybrid private DNS

1. Create a private DNS zone, two VNet links and test records.
2. Deploy DNS Private Resolver inbound/outbound endpoints and a forwarding ruleset.
3. Simulate on-premises DNS with a VM or containerized resolver and configure conditional forwarding.
4. Break a link/rule, collect failed query evidence, repair it and document query paths.

### Lab 3 — Hub-spoke routing and NAT

1. Build hub and two spoke VNets with peering.
2. Insert a firewall/NVA or documented next-hop substitute and UDRs.
3. Inspect effective routes and prove spoke-to-spoke and internet paths.
4. Add NAT Gateway to a separate subnet, observe explicit egress IP and compare its role with the firewall.
5. Create an asymmetric route deliberately and diagnose it.

### Lab 4 — VPN design and troubleshooting

1. Implement VNet-to-VNet VPN gateways as a safe stand-in for two sites, or use a supported lab appliance.
2. Configure route-based connections and custom BGP where feasible.
3. Record gateway, local-network, connection and IPsec/IKE settings.
4. Break a prefix or policy, use gateway/route evidence to locate it, then restore.
5. Redesign for two customer devices/links and explain remaining shared failures.

### Lab 5 — Application delivery comparison

1. Deploy two simple backends and a Standard Load Balancer with probe/rule.
2. Configure Application Gateway with host/path routing and end-to-end TLS or document certificate dependencies.
3. Configure Traffic Manager or Front Door over two endpoints when budget permits.
4. Break backend readiness and compare health detection and client behavior.
5. Record layer, scope, proxy/DNS, client-IP, TLS, caching and failover differences.

### Lab 6 — Private endpoint end to end

1. Create a storage account and private endpoints for the subresources your test uses.
2. Configure recommended private DNS zones and hybrid-style resolution.
3. Prove identity authorization and network/DNS access separately.
4. Disable public access only after the private route works.
5. Break DNS, role assignment and firewall independently; capture distinct symptoms.

### Lab 7 — NSG, flow log and Network Watcher evidence

1. Apply subnet and NIC NSGs to two VMs.
2. Predict an effective rule, then verify it with effective rules and IP flow verify.
3. Enable current virtual network flow logs and inspect allowed/denied records.
4. Use next hop, connection troubleshoot and packet capture for one failed flow.
5. Explain what each tool proved and what it could not prove.

### Lab 8 — Firewall and WAF policy

1. Build an Azure Firewall policy with narrow network/application rules and diagnostics.
2. Route a workload subnet through it; verify both directions and DNS behavior.
3. Put WAF in detection mode before a sample web app and generate benign rule matches.
4. Design a narrow exclusion or application fix, then document prevention promotion criteria.
5. Compare the threats addressed by NSG, Firewall, WAF and DDoS protection.

---

## 9. Original knowledge checks

1. Why reserve more subnet space than today’s instance count? **Answer:** Azure reservations, autoscale, upgrades, blue-green capacity, private endpoints and future service constraints consume addresses.
2. Does subnet delegation make a PaaS endpoint private? **Answer:** No; it delegates subnet management to a service. Private access is a separate design.
3. What proves which route Azure actually selected? **Answer:** Effective routes/next-hop evidence on the relevant interface, plus return-path verification.
4. Is VNet peering transitive? **Answer:** No; A-to-B and B-to-C do not automatically connect A to C.
5. What two complementary gateway-transit settings are needed? **Answer:** The hub allows gateway transit and the spoke uses the remote gateway, subject to current constraints.
6. Route Server control plane or data plane? **Answer:** It exchanges BGP routes; the traffic flows through the selected NVA/gateway path, not Route Server as a forwarding appliance.
7. Does NAT Gateway permit unsolicited inbound traffic? **Answer:** No; it provides outbound SNAT for supported subnet flows.
8. Private endpoint works from one VNet but not on-premises. First likely design area? **Answer:** Hybrid DNS forwarding/resolution to the private address, then routes and filters.
9. A VPN tunnel shows connected but the app fails. Name four next checks. **Answer:** Advertised prefixes/routes, NSGs/firewalls, NAT, MTU/MSS, DNS, return path and listener are examples.
10. Route-based versus policy-based VPN? **Answer:** Route-based designs route traffic through a tunnel interface and generally fit modern multi-prefix/BGP needs; policy-based designs use static encryption domains for supported legacy cases.
11. Does ExpressRoute mean encrypted? **Answer:** No. Private connectivity and encryption are separate requirements.
12. What does Global Reach connect? **Answer:** Supported customer networks through the Microsoft backbone using ExpressRoute circuits; it is not simply a VNet-to-circuit connection.
13. Virtual WAN association versus propagation? **Answer:** Association chooses the route table used for a connection’s outbound routing; propagation determines which tables learn its routes.
14. Why can Traffic Manager failover appear slow? **Answer:** It is DNS-based; configured TTL plus recursive resolver and client caching affect convergence.
15. Load Balancer or Application Gateway for URL path routing? **Answer:** Application Gateway; Load Balancer is Layer 4.
16. Why does a healthy VM receive no Application Gateway traffic? **Answer:** The configured probe may fail due to path, host header, port, TLS trust/SNI, NSG, DNS or listener behavior.
17. Front Door Private Link makes clients private? **Answer:** No; clients use the public edge. Private Link secures supported edge-to-origin connectivity.
18. What must be true before disabling a PaaS public endpoint? **Answer:** Correct private endpoint/subresource, approval, DNS from every client, routes/filters and service authorization are proven.
19. Service endpoint gives the PaaS service a private VNet IP? **Answer:** No; it keeps the service public endpoint and identifies/optimizes access from the enabled subnet.
20. NSG rule allows a flow; is the transaction proven? **Answer:** No. Route, service firewall, proxy, TLS, listener, application and return path may still fail.
21. Why can a firewall UDR cause an outage even when rules allow traffic? **Answer:** The return path may bypass the stateful firewall, or platform/DNS/SNAT dependencies may be misrouted.
22. Detection versus prevention WAF? **Answer:** Detection logs matches; prevention can block them. Tune with representative traffic before enforcing.
23. Virtual network flow logs versus packet capture? **Answer:** Flow logs record metadata about flows; packet capture records packet-level data for supported interfaces and filters.
24. Best first troubleshooting artifact? **Answer:** A precise failing five-tuple and timestamp plus expected DNS/address/path, so every subsequent signal can be correlated.

---

## 10. Readiness checklist

You are approaching readiness when you can:

- design non-overlapping, scalable prefixes and service-appropriate subnets;
- explain public IP/prefix/BYOIP choices and explicit egress;
- trace public, private and hybrid DNS through zones, links, Resolver endpoints and rules;
- implement peering, gateway transit, UDR, forced tunneling, Route Server and NAT Gateway;
- select Network Watcher evidence and interpret current virtual network flow logs;
- design resilient S2S and P2S VPNs with routing, authentication and failure behavior;
- compare ExpressRoute models, peerings, SKUs, Global Reach, FastPath, Direct, encryption and BFD;
- configure Virtual WAN hubs, gateways, route associations/propagation and security integration;
- choose and implement Load Balancer, Traffic Manager, Application Gateway, Front Door and Gateway Load Balancer;
- build private endpoint, Private Link service and service endpoint designs with correct DNS;
- design NSG/ASG, Virtual Network Manager, Firewall/Manager, WAF and DDoS layers;
- troubleshoot both directions from DNS to application evidence without random changes;
- complete the labs and explain why each alternative does or does not meet requirements;
- answer the original checks from packet-path reasoning rather than memorization.

### Primary references

- [Official AZ-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)
- [Azure networking documentation](https://learn.microsoft.com/en-us/azure/networking/)
- [Azure DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview)
- [Azure virtual network routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)
- [VPN Gateway documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/)
- [ExpressRoute documentation](https://learn.microsoft.com/en-us/azure/expressroute/)
- [Azure Virtual WAN overview](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about)
- [Azure load-balancing decision guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)
- [Azure Private Link overview](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)
- [Azure Firewall documentation](https://learn.microsoft.com/en-us/azure/firewall/)

---

## Places to learn

This is a curated starting set, not a complete list. Do **not** consume every resource. Pick one structured spine, use current documentation for weak objectives, build and break the labs, and add one assessment source. Time estimates are planning ranges, not guarantees; playback speed, prior networking experience, gateway deployment time, exercises, cleanup, and vendor changes matter. Verify the current blueprint before buying or starting a course.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Microsoft Learn AZ-700 course](https://learn.microsoft.com/en-us/training/courses/az-700t00) | Free self-directed content; instructor delivery varies | Published: 3 instructor-led days; plan 18–28 hours reading or 30–45 with labs | Best official objective-aligned spine |
| [Microsoft free Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-network-engineer-associate/?practice-assessment-type=certification) | Free account | Plan 45–90 minutes including review | Baseline and gap finding; not a substitute for packet-path labs |
| [John Savill AZ-700 Study Super Guide](https://www.youtube.com/watch?v=nVZYDhB_M64) | Free | Published: about 2h 50m; plan 4–6 hours with pauses and current-objective reconciliation | High-density visual review; recording predates July 2026 additions |
| [John Savill AZ-700 whiteboard](https://github.com/johnthebrit/CertificationMaterials/blob/main/whiteboards/AZ-700-Whiteboard.png) | Free public GitHub resource | Plan 1–2 hours to annotate and redraw | Visual recall companion; check all terms against current docs |
| [Pluralsight AZ-700 certification path](https://www.pluralsight.com/paths/microsoft-certified-designing-and-implementing-microsoft-azure-networking-solutions-az-700) | Paid/trial or organization access | Published: 44 hours including legacy course, seven current courses and one lab; plan 18–30 hours if selecting the refreshed path only | Modular 2025–2026 videos, lab and practice exam; avoid duplicating legacy/current series |
| [O'Reilly AZ-700 course by Kirk Whetton](https://www.oreilly.com/videos/azure-network-engineer/0642572086336/) | Paid subscription | Published: 11h 2m; plan 16–24 hours with sandbox and notes | Current detailed video alternative with quizzes/sandbox |
| [O'Reilly/Packt Azure Networking book](https://www.oreilly.com/library/view/designing-and-implementing/9781803242033/) | Paid subscription/book | Published: 524 pages / platform estimate 11h 20m; plan 18–30 hours with exercises | Deep hands-on reference; 2023 publication needs current-doc checks |
| [Udemy AZ-700 course by Alan Rodrigues](https://www.udemy.com/course/azure-exam-700/) | Paid; frequent discounts | Published: 33h 23m and updated March 2026; plan 40–55 hours with labs | Extensive video/lab spine; compare with July 2026 objective additions |
| [Whizlabs AZ-700 course and practice resources](https://www.whizlabs.com/microsoft-azure-exam-az-700/) | Paid; samples may be free | Plan 12–25 hours based on selected video, lab and practice components | Targeted exercises and assessment; verify current bundle details |
| [MeasureUp AZ-700 practice test](https://www.measureup.com/microsoft-practice-test-az-700-designing-and-implementing-azure-networking-solutions.html) | Paid; free demo available | Plan 3–6 hours across timed attempt and explanation review | 118-question independent bank; page showed January 2025 update, so verify July 2026 alignment |

Practice products should contain independently authored questions and explanations, not recalled live-exam content. Use results by objective domain, reproduce failures in a lab, revisit primary documentation, then retest with unseen questions.
