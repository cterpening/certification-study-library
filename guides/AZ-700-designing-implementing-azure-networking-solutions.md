---
exam_code: AZ-700
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AZ-700 Designing and Implementing Microsoft Azure Networking Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-700-coverage-record). The [official AZ-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700) is authoritative.

**Current baseline:** Skills measured as of July 27, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Official source:** [AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)

> **Living-guide watch — September 7, 2026:** The current blueprint names virtual network flow logs and Network Watcher troubleshooting, but older learning material can still center NSG flow logs or assume the Network Watcher VM extension is always required. Microsoft no longer permits creation of new [NSG flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview) and will retire them on September 30, 2027; use [virtual network flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/vnet-flow-logs-overview) for new work and account for their scope, unsupported scenarios, storage, duplicate-ingestion, and cost boundaries. [Connection troubleshoot](https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview) now has an agentless experience, but Microsoft still labels it preview. Keep extension-based and agentless prerequisites separate, verify the live page before a lab, and treat third-party diagrams or courses as explanations rather than scope authority.

**September 28 deep review:** All 136 detailed objectives remain on the July 27 baseline. The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-network-engineer-associate/) lists a 100-minute assessment, ten exam languages and annual renewal. The three-day instructor course is a separate time commitment. See the [deep-review report](../docs/research/2026-09-28-az-700-deep-review.md) for objective mapping, source limitations and local checks; infrastructure labs and independent human review remain pending.

Current operational additions below cover explicit egress, StandardV2 NAT Gateway, hybrid DNS, VPN migration, private-endpoint policy exceptions and retired application-delivery SKUs. Preview features are labeled and are supporting context, not additions to the published exam objectives.

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

For ordinary IPv4 subnet planning, subtract Azure's first four and last reserved addresses, then budget service-specific reservations, upgrades and overlap separately. [Virtual Network FAQ](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-faq) explains the reservation rule. A service's required dedicated subnet size still applies even when your address arithmetic fits; see worked example 1.

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

#### Resolver direction, loops and negative answers

An inbound endpoint has a reachable private IP that clients or on-premises forwarders can query. An outbound endpoint connects a forwarding ruleset to destination DNS servers; it does not provide a client-facing DNS server IP. Keep the endpoint subnets dedicated. A ruleset link can enable DNS resolution without VNet peering, but that does not create a route to the application. A ruleset that forwards a zone to a hub inbound endpoint must not also link back to that endpoint's own VNet: that can loop. Use the [endpoint and ruleset guidance](https://learn.microsoft.com/en-us/azure/dns/private-resolver-endpoints-rulesets) to distinguish a distributed ruleset-link design from a centralized custom-DNS design.

For on-premises Private Link resolution, forward the service's public namespace, such as `blob.core.windows.net`, into Azure's resolver path; trace the CNAME chain to the private zone. Creating a private zone alone does not change a client's configured resolver. Check each service's [private-endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns).

[Internet fallback](https://learn.microsoft.com/en-us/azure/dns/private-dns-fallback) uses `resolutionPolicy: NxDomainRedirect` on an individual VNet link to a **Private Link private DNS zone**. An authoritative NXDOMAIN can then trigger public recursion. It is not a general fallback for every private zone, timeout or application error. A public answer neither grants service authorization nor changes disabled public-network access. Decide whether public resolution is intended before enabling it; a missing record for your own private endpoint may need repair instead.

### VNet connectivity, routing and egress

#### Peering and gateway transit

VNet peering supplies private IP connectivity over the Azure backbone. Peering is non-transitive: A-to-B and B-to-C do not automatically provide A-to-C. Each direction is a separate peering object with settings such as virtual-network access, forwarded traffic, and gateway use/transit.

Gateway transit lets a spoke use a compatible gateway in a hub when the hub allows transit and the spoke uses the remote gateway. A VNet cannot use multiple remote gateways in the same way; understand gateway and peering constraints before centralizing.

Azure Virtual Network Manager can group networks and deploy connectivity or security-admin configurations at scale. Mesh and hub-and-spoke topology intent does not eliminate address planning, DNS, route, gateway and application dependencies. Stage deployments and understand regional/scope/feature support.

#### Route selection

Azure creates system routes, learns BGP routes from gateways/Route Server, and applies user-defined routes (UDRs). Longest prefix match normally selects a route; for identical prefixes, UDR then BGP then system route is the general priority. Preferred VNet/peering/service-endpoint system routes and private-endpoint policies have documented exceptions. Inspect **effective routes** rather than only the route-table resource.

| Next hop | Use | Caution |
|---|---|---|
| Virtual network | Within VNet | Address space changes affect system routes |
| Virtual network gateway | Learned gateway path; explicit UDR next hop supported for a VPN gateway | Do not target ExpressRoute, Route Server or a Virtual WAN hub router with this UDR next-hop type |
| Virtual appliance | Firewall/router/NVA | Appliance IP forwarding, health and symmetric return path |
| Internet | Azure internet edge path | Public exposure and platform egress behavior remain separate |
| None | Drop matching traffic | More-specific routes can still win |

Forced tunneling sends selected internet-bound traffic through a central or on-premises inspection path. Account for control-plane/service dependencies, platform service tags, asymmetric routing, SNAT, throughput and outage behavior. Disabling gateway route propagation can prevent unintended learned routes but can also remove required connectivity.

Azure Route Server exchanges BGP routes with supported NVAs so routes can change dynamically. It does not forward data traffic itself. Design ASN, peering IPs, route limits, redundancy, branch-to-branch behavior and interaction with gateways. **VERIFY CURRENT:** coexistence, route exchange and supported NVA behavior.

Azure NAT Gateway provides scalable, explicit outbound SNAT for supported subnet flows. It does not accept unsolicited inbound connections or act as a firewall. Subnet association, public IP/prefix, idle timeout, zone model and port consumption matter. Avoid depending on implicit/default outbound access; design egress explicitly using [NAT Gateway guidance](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview).

> **Related item:** SNAT port exhaustion is a state-capacity problem. Connection reuse, destination tuple distribution, idle timeouts, scale and the number of frontend addresses affect it. Adding compute without fixing outbound translation can worsen pressure.

#### Explicit egress and NAT Gateway capacity

[Default outbound access guidance](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access) scopes the private-by-default change to new VNets using API version `2025-07-01` or later, released after March 31, 2026. Inspect the deployed subnet and tooling/API version; existing VNets did not all lose outbound connectivity on that date. Private subnets need an explicit method for required public dependencies. A `0.0.0.0/0` UDR to a firewall/NVA takes precedence over subnet NAT Gateway egress.

| NAT decision | Current boundary to explain |
|---|---|
| Standard versus StandardV2 | Standard is zonal; StandardV2 is zone redundant and supports IPv4/IPv6. Published aggregate throughput is 50 versus 100 Gbps; Standard has separate 25 Gbps outbound and response limits. These are ceilings, not measured application throughput. |
| Public IP compatibility | StandardV2 needs StandardV2 public IPs/prefixes. Moving from Standard requires a new gateway and reassociation; it is not an in-place SKU upgrade. |
| SNAT capacity | Ports are shared on demand across associated subnets. Each public IP supplies 64,512 ports per transport inventory, but the concurrent same-destination limit is 50,000 connections per public IP; do not equate the two numbers. |
| Ping | StandardV2 supports outbound IPv4/IPv6 Echo Request/Reply. Other ICMP types are unsupported; Standard does not gain this capability. A successful ping does not prove DNS, HTTPS or authorization. |
| IPv6-only clients to IPv4 services | NAT64 uses `64:ff9b::/96`; a separate third-party DNS64 service must synthesize the AAAA answer. NAT Gateway is not that DNS64 service. |
| Migration | Existing Load Balancer, Firewall or VM public-IP connections can be interrupted when adding StandardV2. IPv6 Load Balancer outbound rules also have a documented disruption limitation. Plan and test the cutover. |

Use the current [resource limits and protocols](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-gateway-resource), [SNAT reuse explanation](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-gateway-snat) and [overview limitations](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview). Different destinations can reuse a port; closed connections have reuse timers. Connection pooling, bursts, packets per second and total active flows still matter after adding IPs.

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

The July 2026 blueprint explicitly names **virtual network flow logs**. For new deployments, **flow logs** means virtual network flow logs. NSG flow logs are a retiring legacy source: new creation is disabled and retirement is September 30, 2027. Do not enable both log types over the same workload merely for comparison because duplicate recording and additional cost can result. Virtual network flow logs operate at VNet scope, record supported Layer 4 flows, and have documented exclusions; absence of a record is therefore not proof that no traffic existed. Flow logs show network-flow metadata, not payload capture or application logs. Plan storage/analytics destination, retention, schema, Traffic Analytics integration, cost, and access. Connection troubleshoot's agentless path is useful but remains preview, so record whether a result came from agentless platform APIs or the extension-based path.

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

#### VPN migration is scoped by gateway SKU and public-IP SKU

The [VPN Gateway consolidation guidance](https://learn.microsoft.com/en-us/azure/vpn-gateway/gateway-sku-consolidation) ends new non-AZ `VpnGw1`–`VpnGw5` creation and describes migration to AZ SKUs. Existing non-AZ gateways remain supported until migrated; the page schedules deprecation after September 2026. **Basic gateway SKU is not retiring**, and Gen1 has no announced retirement. Legacy Standard/HighPerformance gateways have a separate migration program.

Inventory gateway SKU, generation, public-IP SKU and region before selecting a procedure. A Basic gateway using a Basic public IP must not use the VpnGw migration tool. An AZ SKU in a region without availability zones is regional until zone support exists. SKU naming alone is not evidence of a deployed zone-resilient topology; rehearse verification and rollback for the actual combination.

### Azure Extended Network

[Azure Extended Network](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/azure/azure-extended-network) uses a bidirectional VXLAN tunnel between on-premises and Azure virtual appliances to stretch one selected on-premises subnet into an Azure VNet. Its narrow purpose is to let selected VMs retain on-premises private IP addresses during migration when renumbering is not possible. Prefer a normal routed migration into an Azure-only subnet when addresses can change.

Requirements drive the design:

- Provide site-to-site VPN or ExpressRoute connectivity between the Azure VNet and on-premises network.
- Create an Azure routable subnet and a subnet whose CIDR matches the on-premises subnet being extended; ensure the extended prefix introduces no other overlap in the routing domain.
- Deploy one appliance pair per extended subnet. The Azure appliance is a nested-virtualization-capable Windows Server 2022 Azure Edition VM with NICs on the routable and extended subnets. The on-premises appliance is a Windows Server 2019 or 2022 VM on a nested-virtualization-capable hypervisor with NICs on its routable and extended subnets.
- Enable Hyper-V and map external virtual switches to the two NICs on each appliance. Run an Azure-connected Windows Admin Center instance on another machine, install the Extended network extension, and add only the IPv4 addresses that must be reachable across the extension.
- If a firewall crosses the path, account for asymmetric routing and allow the chosen VXLAN UDP port in both directions (default 4789).

After deployment, require WAC status **OK**, `Get-Service extnwagent` running on both appliances, and successful transactions in both directions for each retained address. Diagnose with appliance OS/NIC/subnet checks, WAC remoting, route and firewall inspection, `pktmon` on both appliances, and MTU testing for intermittent failures. Remove extended addresses before removing the extension and appliances.

**Availability boundary (checked September 5, 2026):** Microsoft currently says the `msft.sme.subnet-stretch` extension is unavailable in the WAC 2410 extension feed. Verify WAC and extension availability before treating this as deployable; a design-only exercise is the safe substitute when it is unavailable. Scale, throughput, OS, extension and topology details are **VERIFY CURRENT**.

### Point-to-site VPN

P2S connects individual clients to a VNet. Select:

- gateway SKU and capacity;
- tunnel type such as OpenVPN, IKEv2 or SSTP according to client/authentication needs;
- certificate, RADIUS, or Microsoft Entra ID authentication where supported;
- client address pool that does not overlap VNet, on-premises or client-local networks;
- routes advertised to the client and transit expectations;
- client package/profile distribution, versioning and revocation;
- DNS resolution and access controls after tunnel establishment.

#### Always On device tunnel versus Entra user authentication

The [Always On device-tunnel procedure](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-howto-always-on-device-tunnel) uses the Windows built-in VPN client, IKEv2 and a computer certificate in the Local Machine store, configured under LOCAL SYSTEM on a domain-joined Enterprise/Education device. Only one device tunnel is supported per device. It connects before user sign-in; a user tunnel has a separate profile and purpose. Microsoft recommends Windows 11 following Windows 10's October 2025 end of support.

For Azure P2S, [Microsoft Entra authentication](https://learn.microsoft.com/en-us/azure/vpn-gateway/point-to-site-about) requires OpenVPN and Azure VPN Client. It is not an IKEv2 authentication option. Match tunnel, authentication, operating system, client and profile together; selecting multiple gateway authentication methods does not make every combination valid.

### Azure Network Adapter requirements

[Azure Network Adapter](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/azure/use-azure-network-adapter) is a WAC workflow that automates a certificate-authenticated P2S VPN for an individual Windows server. Use it when a branch, store, or other location has only a few servers that need Azure VNet access and a site-to-site VPN device or public-facing server address is unnecessary. It is not a whole-site connectivity or transit solution.

Specify an active Azure subscription, an existing VNet, internet access from the target server, a current WAC installation, and WAC Azure integration. In the target server's WAC **Networks** tool, **Add Azure Network Adapter** collects the subscription, location, VNet, gateway subnet/SKU, client address pool, and authentication certificate. The client pool must overlap neither the VNet nor the connecting on-premises network. If no virtual network gateway exists, WAC can create one; include its deployment time and cost in the plan.

Verify the resulting adapter state and assigned address, installed routes, private DNS answer, authorization path, and an application transaction—not only the wizard result. Troubleshoot target-server internet access, WAC Azure authorization, gateway state, trusted root/client certificate, address overlap, routes, DNS, NSGs, host firewall and listener. Disconnect the adapter in WAC when no longer needed, and delete a gateway only after proving no other connections use it. Always On VPN has a different client and operational model; do not treat the two labels as interchangeable.

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

Two connections in one ExpressRoute circuit still share a peering-location failure domain. [VPN failover guidance](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/expressroute-vpn-failover) treats the VPN as a potentially degraded-capacity path: test route convergence, session reconnection and failback. VPN backup carries private-peering traffic; Microsoft-peering traffic reaches services over the internet instead. Keep prefix advertisements aligned because a more-specific route can defeat the intended ExpressRoute preference.

**Related preview:** [ExpressRoute Resiliency Guard](https://learn.microsoft.com/en-us/azure/expressroute/resiliency-model) helps configure multi-homing through circuits at different physical locations or Metro circuits. It is public preview for ExpressRoute VNet gateways and does not currently support Virtual WAN gateways. The configuration aid does not prove backup capacity or application recovery. FastPath bypasses the gateway for supported data traffic while retaining the control-plane gateway; check the [Direct/provider feature matrix](https://learn.microsoft.com/en-us/azure/expressroute/about-fastpath) before assuming peering, UDR or Private Link support.

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

**Routing-intent boundary:** [Virtual WAN routing intent](https://learn.microsoft.com/en-us/azure/virtual-wan/how-to-routing-policies) manages connection associations and propagation. It requires removal of incompatible custom route tables and default-table static routes whose next hop is a VNet connection. Export the existing configuration before changing it; previous settings are not automatically restored. Internet/private policies and inter-hub inspection require a complete symmetric-path design.

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

[Application Gateway backend settings](https://learn.microsoft.com/en-us/azure/application-gateway/configuration-http-settings) distinguish client-to-gateway TLS from gateway-to-backend TLS. Check backend certificate chain, expiry and SNI/hostname, plus the custom probe's host, path and association. Keep production certificate validation enabled; suppressing validation can hide the cause of a failed backend handshake. A portal test probe can differ from periodic probe behavior. Configure connection draining for planned removal and allow enough time for expected transfers.

**Lifecycle:** [Application Gateway v1 retired April 28, 2026](https://learn.microsoft.com/en-us/azure/application-gateway/v1-retirement). Remaining v1 resources have no support/SLA and can lose traffic as hardware is decommissioned. New labs should use supported v2 configurations; a still-running v1 instance is not evidence of continued support.

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

For public Front Door origins, combine the `AzureFrontDoor.Backend` address restriction with validation of **your** `X-Azure-FDID`. Shared Front Door addresses alone do not identify your profile, while a header alone can be imitated on an unrestricted origin. [Origin security guidance](https://learn.microsoft.com/en-us/azure/frontdoor/origin-security) explains the combination. Front Door classic retires March 31, 2027; plan a [supported-tier migration](https://learn.microsoft.com/en-us/azure/frontdoor/migrate-tier) and verify DNS/certificates and origin access after cutover.

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

The conventional Private Link service design publishes a customer-owned service behind a Standard Load Balancer so consumers can create private endpoints to it. Design NAT/source behavior, visibility/auto-approval, alias, frontend/backend, health, quotas and provider/consumer responsibility. It is different from consuming a Microsoft PaaS private endpoint.

See the [Private Link overview](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview).

#### Endpoint network policies and the Direct Connect preview

For an ordinary private endpoint, enable the required NSG and/or route-table policy on its hosting subnet before expecting those policies to apply. The [private-endpoint routing exception](https://learn.microsoft.com/en-us/azure/private-link/disable-private-endpoint-network-policy) allows eligible UDRs with a prefix at least as specific as the endpoint VNet address space to override its default `/32` route when route policy is enabled. A catch-all `0.0.0.0/0` does not achieve this. Inspect effective routes and the return path; do not extrapolate from an ordinary longest-prefix exercise.

**Related preview:** [Private Link service Direct Connect](https://learn.microsoft.com/en-us/azure/private-link/configure-private-link-service-direct-connect) can target a privately routable static IP without a Standard Load Balancer. Current preview restrictions include limited regions, at least two IP configurations in pairs, no private endpoint as destination, same-region client/endpoint/service, and no enabled private-endpoint network policies for associated endpoints. ExpressRoute on-premises access requires the PLS and gateway in the same VNet. It needs a new PLS rather than migration of an existing service. Billing starts October 15, 2026; recheck current pricing and restrictions before a deployment.

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

For [Azure Storage service endpoint policies](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoint-policies-overview), an account/resource-group/subscription allowlist constrains destination accounts. An NSG Storage service tag alone permits a broader service address set. Keep the destination policy separate from the target account's own network rules and the caller's data permissions.

## 6. Design and implement Azure network security services (15–20%)

### NSGs, ASGs and flow logs

Network security groups are stateful Layer 3/4 filters with prioritized inbound and outbound rules. They can apply to a subnet and NIC; traffic must be allowed through the effective evaluation. Default rules remain unless a higher-priority custom rule overrides them.

Use service tags for Microsoft-managed address sets and application security groups for logical groups of NICs. Neither is application identity. Rule design should include owner, purpose, source, destination, protocol/port, priority, expiry/review and logging evidence.

Azure Virtual Network Manager security admin rules can establish centrally managed allow, always-allow or deny intent across managed networks, evaluated in relation to NSGs according to documented order. Verify current semantics before rollout; a central rule can have broad impact.

Use virtual network flow logs and IP flow verification for evidence, but remember that an allowed flow does not prove route, listener, TLS or application success. Review the [NSG overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

[Security admin rule evaluation](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-security-admins) precedes NSGs. **Allow** continues to NSG evaluation; **Always Allow** bypasses subsequent NSG evaluation; **Deny** terminates the flow. Verify deployment scope and service exclusions before relying on a central rule. For administrative access, [Bastion settings](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) require a dedicated `/26` or larger `AzureBastionSubnet` for current non-Developer deployments; ordinary deployments and private-only deployments have different public-IP requirements.

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

[Firewall rule processing](https://learn.microsoft.com/en-us/azure/firewall/rule-processing) evaluates DNAT, then network, then application rules; rule type order is not overridden by a lower numeric priority on an application collection. Parent-policy collections take precedence within that processing structure. A broad network allow can therefore prevent a narrower application rule from being reached. [SNAT private-range configuration](https://learn.microsoft.com/en-us/azure/firewall/snat-private-range) affects network rules; application rules always use SNAT through the proxy. Do not diagnose return routing using the network-rule source-preservation assumption for an application-rule flow.

For [Front Door WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview), Standard supports custom rules while Premium provides the full managed-rule capability. Custom rules normally precede managed rules, with a documented HTTP DDoS ruleset exception. Record tier, applicable policy scope, mode and rule action when explaining what protected a request.

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

### Worked example 1 — subnet growth and upgrade overlap

Assume 40 one-IP instances, 25% growth and an upgrade that temporarily doubles that grown fleet. Demand is `40 × 1.25 × 2 = 100` addresses. An ordinary Azure IPv4 `/26` offers `64 − 5 = 59`, so it fails; `/25` offers `128 − 5 = 123`, leaving 23 addresses before any additional service reservations. These are invented workload assumptions, not a universal service sizing rule.

### Worked example 2 — route source cannot beat every prefix

For an ordinary destination `10.20.1.9`, suppose eligible routes are UDR `0.0.0.0/0 → firewall`, BGP `10.20.0.0/16 → VPN` and UDR `10.20.1.0/24 → NVA`. The `/24` wins. Remove it and the BGP `/16` wins over the default UDR. Add an eligible UDR for the same `/16` and it wins the equal-prefix tie. This example excludes preferred system/service-endpoint routes and the private-endpoint exception. The observed effective route and return path remain the deployment evidence.

### Worked example 3 — SNAT ports versus same-destination capacity

Assume 120,000 concurrent TCP connections all reach one external IP and port. Using the documented 50,000-per-public-IP ceiling gives a theoretical minimum `ceil(120,000 / 50,000) = 3` public IPs. Two IPs provide 129,024 SNAT ports, yet their same-destination connection ceiling is only 100,000. Three provide a 150,000 ceiling, so this demand consumes 80% of that ceiling. This is a lower-bound capacity exercise, not a throughput guarantee: add burst/reuse headroom, validate distribution and consider total-flow, PPS, bandwidth and endpoint limits. Prefer connection reuse where the application supports it.

### Worked example 4 — a connected backup can still be undersized

An invented workload needs 1.2 Gbps during an ExpressRoute outage. A tested VPN path sustains 0.8 Gbps under the same traffic mix. The shortfall is 0.4 Gbps, or one third of demand. Defer a 0.5 Gbps batch workload and the remaining 0.7 Gbps fits with only 0.1 Gbps headroom. Check latency, encryption overhead, routes and session recovery as well as this arithmetic; no gateway SKU throughput is assumed here.

### Worked example 5 — DNS recovery is only one gate

| Observation | Meaning and next evidence |
|---|---|
| Private Link zone returns NXDOMAIN for a resource you own | Inspect the endpoint's record/zone group and the resolver's zone link before enabling public fallback. |
| Intended cross-tenant resource resolves publicly after `NxDomainRedirect` | DNS now has an answer; check whether public network access is permitted, then route/filter and service authorization. |
| Private IP resolves but TCP fails | Query success does not prove a route or allowed transport; inspect effective routes, policies and destination listener. |
| TCP succeeds but HTTPS fails | Inspect hostname/SNI, certificate trust/expiry and application response. |

### Worked example 6 — effective policy and layer boundaries

For a matching central admin **Allow** and a matching NSG **Deny**, the flow is denied. Change the applicable admin action to **Always Allow** and NSG evaluation is bypassed; this still does not prove the application's listener, TLS or authorization. Separately, a Firewall network allow for TCP 443 can terminate rule evaluation before an application FQDN deny. Tighten the correct rule layer instead of assigning the application rule an arbitrarily lower number.

### Three useful blog exercises

| Article and date | Exercise | Current-documentation boundary |
|---|---|---|
| [Private subnets by default](https://techcommunity.microsoft.com/blog/azurenetworkingblog/private-subnets-by-default-in-azure-virtual-networks-what-changed-and-how-to-use/4513778), Aimee Littleton, April 22, 2026 | Contrast an existing VNet and a new private VNet; identify explicit paths for updates and a public API, then draw a migration checklist. | Verify the actual API/provider version. Do not reuse the article's dated Terraform exception or its unconditional no-interruption statement: current StandardV2 documentation lists disruption cases. |
| [DNS in Azure landing zones](https://techcommunity.microsoft.com/blog/azurenetworkingblog/dns-best-practices-for-implementation-in-azure-landing-zones/4420567), Ashish Rana, June 12, 2025 | Draw centralized custom-DNS and distributed zone/ruleset-link alternatives; trace one query in each direction and identify a possible forwarding loop. | Hub-only zone links do not themselves force firewall inspection; routing must do that. Scope fallback to Private Link zones. Treat AD forwarder replication as an environment-specific design decision, not a universal prohibition. |
| [StandardV2 ICMP support](https://techcommunity.microsoft.com/blog/azurenetworkingblog/icmp-support-for-azure-standardv2-nat-gateway/4528374), Malaika Nazim, June 17, 2026 | Explain both “ping fails, HTTPS works” and “ping works, HTTPS fails”; list the next test for each. | Echo support is SKU-specific, not all ICMP. Independent NSG/firewall/destination filtering still applies; an Echo reply is not an application health check. |

The articles supply learning scenarios; the linked product documentation controls support, lifecycle and configuration details. Their complete main text was reviewed, including the qualifications above; linked deployments and media were not executed.

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
6. Build a requirements comparison for Azure Network Adapter and Azure Extended Network: connection scope, WAC/Azure dependencies, gateway/routing, address plan, certificates, appliances, firewall path, cost, verification, and cleanup.
7. Create a paper Azure Network Adapter design with a nonoverlapping client pool and a test transaction from one server to a private Azure VM. Optionally deploy it only in a cost-capped lab-owned resource group, then disconnect it and remove resources after checking dependencies.
8. Create an Extended Network paper design showing both two-NIC appliances, routable and matching extended subnets, VPN/ExpressRoute, bidirectional VXLAN, asymmetric routing, selected retained addresses, health evidence, and ordered removal. Deploy only when current Microsoft documentation confirms extension availability and the isolated environment supports nested virtualization.

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

### Lab 9 — Offline capacity and failure worksheet

1. Recalculate worked examples 1–4 with a 60-instance fleet, a different route and a second destination endpoint.
2. Explain why the NAT same-destination calculation cannot be replaced with a count of SNAT ports.
3. Draw normal, failover and failback paths, including DNS and stateful return routing.
4. Identify which assumptions require a load test or effective-route observation before deployment.

### Lab 10 — Blog claim and migration review

1. Complete the three blog exercises and keep a claim/source/date table.
2. Compare the NAT migration article with current StandardV2 interruption limitations.
3. Classify a VPN inventory by gateway SKU, generation, IP SKU and regional zone support; choose the appropriate current procedure without executing it.
4. Compare conventional PLS with Direct Connect preview; record region, endpoint policies, ExpressRoute placement, billing and cleanup constraints.
5. Write acceptance evidence for DNS, transport, TLS, authorization, telemetry and rollback separately. Use paper designs first; any later cloud exercise needs a cost-capped isolated environment.

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

25. How many ordinary Azure IPv4 addresses can a /25 allocate? **Answer:** 123 before additional service-specific reservations: 128 minus five.
26. Do 50 grown instances fit an overlapping double-size deployment in /26? **Answer:** No. One hundred addresses exceed its 59 usable addresses.
27. Does a default firewall UDR beat every more-specific BGP route? **Answer:** No. The ordinary longest-prefix decision comes first; inspect documented exceptions and effective routes.
28. Can a Virtual Network Gateway UDR target an ExpressRoute gateway? **Answer:** No. That explicit UDR next-hop type is supported for a VPN gateway, not ExpressRoute, Route Server or a Virtual WAN hub router.
29. Does a ruleset link establish application connectivity? **Answer:** No. It can enable DNS resolution without peering; the application still needs a routed, permitted path.
30. Where should a rule forwarding to a hub inbound endpoint not be linked? **Answer:** Its own endpoint VNet, where that rule can cause a DNS forwarding loop.
31. Does NXDOMAIN fallback repair every private DNS failure? **Answer:** No. NxDomainRedirect is a VNet-link policy for Private Link zones and an authoritative NXDOMAIN; it does not fix arbitrary timeouts or application access.
32. Does a public DNS answer override disabled public access? **Answer:** No. Service network access and identity permissions are separate gates.
33. Did every existing VNet lose default outbound access in March 2026? **Answer:** No. The change is scoped to new VNets and the newer API behavior; inspect actual subnet configuration.
34. Can two NAT public IPs sustain 120,000 concurrent connections to one destination? **Answer:** Not under the current 50,000-per-IP same-destination ceiling, even though their combined port inventory exceeds 120,000.
35. Does StandardV2 ping success prove HTTPS success? **Answer:** No. It proves an Echo request/reply path; TLS, HTTP and authorization are separate.
36. Does StandardV2 provide DNS64 automatically? **Answer:** No. NAT64 requires a separate DNS64 solution for synthesized IPv6 answers.
37. Is a Standard-to-StandardV2 gateway migration an in-place, interruption-free upgrade? **Answer:** No. Create the new gateway/IP resources and plan reassociation; documented existing-flow disruption cases apply.
38. Does non-AZ VpnGw consolidation retire Basic VPN Gateway? **Answer:** No. Basic is explicitly excluded from that retirement claim; use its own public-IP handling procedure.
39. Does an AZ gateway SKU guarantee zones in every region? **Answer:** No. It is regional in regions without availability-zone support.
40. Can Entra P2S authentication use IKEv2? **Answer:** No. It uses OpenVPN and Azure VPN Client; the Always On device tunnel instead uses IKEv2/computer certificates.
41. Are the two links of one standard ExpressRoute circuit two peering locations? **Answer:** No. A location-wide failure can affect both; plan a separate failure boundary.
42. Is a healthy VPN backup necessarily equivalent to ExpressRoute? **Answer:** No. Validate tested capacity, routing, sessions and degraded-mode priorities.
43. Can custom hub route tables remain unchanged when enabling routing intent? **Answer:** No. Check its prerequisites and export the current associations, propagation and routes for a deliberate rollback.
44. Does a default /0 UDR force ordinary private-endpoint traffic through a firewall? **Answer:** No. Enable the relevant endpoint subnet policy and use an eligible prefix under the documented endpoint-routing exception.
45. Does every current PLS design require a Standard Load Balancer? **Answer:** The conventional design does; Direct Connect public preview has a different destination model and explicit restrictions.
46. What happens after an admin Allow when an NSG denies? **Answer:** NSG evaluation still occurs and denies; Always Allow has different terminating semantics.
47. Does a lower-numbered Firewall application rule outrank a matching network rule? **Answer:** No. Rule-type processing order still evaluates network rules before application rules.
48. Are Front Door IP filtering alone or an unrestricted FDID header check enough? **Answer:** Use both for a public origin: address filtering constrains the sender network and the expected FDID identifies the intended Front Door profile.

## 10. Readiness checklist

You are approaching readiness when you can:

- design non-overlapping, scalable prefixes and service-appropriate subnets;
- explain public IP/prefix/BYOIP choices and explicit egress;
- trace public, private and hybrid DNS through zones, links, Resolver endpoints and rules;
- implement peering, gateway transit, UDR, forced tunneling, Route Server and NAT Gateway;
- select Network Watcher evidence and interpret current virtual network flow logs;
- design resilient S2S and P2S VPNs with routing, authentication and failure behavior;
- specify, verify and troubleshoot Azure Network Adapter and Azure Extended Network requirements without confusing per-server P2S, subnet stretch and routed site connectivity;
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
| [John Savill AZ-700 Study Super Guide](https://www.youtube.com/watch?v=nVZYDhB_M64) | Free | Earlier catalog estimate: about 2h 50m, not reverified in this pass; plan 4–6 hours with pauses and current-objective reconciliation | High-density visual review; recording predates July 2026 additions |
| [John Savill AZ-700 whiteboard](https://github.com/johnthebrit/CertificationMaterials/blob/main/whiteboards/AZ-700-Whiteboard.png) | Free public GitHub resource | Plan 1–2 hours to annotate and redraw | Visual recall companion; check all terms against current docs |
| [Pluralsight AZ-700 certification path](https://www.pluralsight.com/paths/microsoft-certified-designing-and-implementing-microsoft-azure-networking-solutions-az-700) | Paid/trial or organization access | Header: 44 hours; seven courses total, including one legacy course, plus one lab. Refreshed courses total 11h 08m, or 11h 38m with the lab; plan 18–30 hours with practice | Modular 2025–2026 videos, lab and practice exam; avoid duplicating legacy/current series |
| [O'Reilly AZ-700 course by Kirk Whetton](https://www.oreilly.com/videos/azure-network-engineer/0642572086336/) | Paid subscription | Published: 11h 2m; plan 16–24 hours with sandbox and notes | July 2025 video alternative with quizzes/sandbox; reconcile against July 2026 objectives |
| [O'Reilly/Packt Azure Networking book](https://www.oreilly.com/library/view/designing-and-implementing/9781803242033/) | Paid subscription/book | Published: 524 pages / platform estimate 11h 20m; plan 18–30 hours with exercises | Deep hands-on reference; 2023 publication needs current-doc checks |
| [Udemy AZ-700 course by Alan Rodrigues](https://www.udemy.com/course/azure-exam-700/) | Paid; frequent discounts | Published: 33h 23m and updated March 2026; plan 40–55 hours with labs | Extensive video/lab spine; compare with July 2026 objective additions |
| [Whizlabs AZ-700 course and practice resources](https://www.whizlabs.com/microsoft-azure-exam-az-700/) | Paid; samples may be free | Plan 12–25 hours based on selected video, lab and practice components | Targeted exercises and assessment; verify current bundle details |
| [MeasureUp AZ-700 practice test](https://www.measureup.com/microsoft-practice-test-az-700-designing-and-implementing-azure-networking-solutions.html) | Paid; free demo available | Plan 3–6 hours across timed attempt and explanation review | 118-question independent bank; page showed January 2025 update, so verify July 2026 alignment |

Practice products should contain independently authored questions and explanations, not recalled live-exam content. Use results by objective domain, reproduce failures in a lab, revisit primary documentation, then retest with unseen questions.

**Catalog check, September 28:** Official course metadata lists three instructor days and eight languages. Pluralsight’s six refreshed courses plus the 30-minute lab total 11h 38m; adding its 32h 27m legacy course yields 44h 05m, rounded to 44 hours in the header. O’Reilly public browser metadata confirms Kirk Whetton’s July 2025 11h 02m course and David Okeyode’s August 2023, 524-page book (11h 20m reading estimate). Udemy lists 13 sections, 368 lectures, 33h 23m and March 2026. Direct O’Reilly/Udemy retrieval was blocked; public metadata does not verify paid lessons. MeasureUp still lists 118 questions and January 2025. Savill media and Whizlabs bundle contents were not independently verified or consumed.
