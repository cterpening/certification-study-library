---
exam_code: N10-009
vendor_id: comptia
official_blueprint: https://www.comptia.org/en-us/certifications/network/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-29
---

# N10-009 CompTIA Network+ (V9) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 29, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#n10-009-coverage-record). The [official Network+ page](https://www.comptia.org/en-us/certifications/network/) is authoritative.

**Current baseline:** Network+ V9, exam N10-009; launched June 20, 2024<br>
**Lifecycle watch:** No exact retirement date is announced. CompTIA says an exam usually retires three years after launch and estimates 2027; verify before scheduling.<br>
**Official delivery snapshot:** Maximum 90 multiple-choice and performance-based questions; 90 minutes; 720/900 passing score; English, German, Japanese, Portuguese, and Spanish listed<br>
**Experience guidance:** CompTIA recommends A+ knowledge plus 9–12 months of hands-on experience in a junior network administrator or network support role

## How to use this guide

Network+ is not a vocabulary contest. Its central mental model is the **packet walk**: follow a frame or packet from an application through name resolution, addressing, switching, routing, translation, filtering, a WAN or cloud boundary, and the return path. At each hop ask:

1. What address, protocol, port, route, policy, medium, and service should be used?
2. Which device owns that decision, and at which OSI layer is the evidence visible?
3. What changed, what is the blast radius, and what does a known-good comparison show?
4. Which read-only observation narrows the fault before a configuration change?
5. After repair, did the full application path, security, resiliency, monitoring, and documentation succeed?

Build a small authorized lab with virtual machines, virtual switches/routers or a network simulator, packet capture, and non-sensitive traffic. Draw the intended topology and addressing first. Introduce one fault at a time, form a theory, collect evidence, make the smallest reversible correction, verify, and document. Never scan, capture, disrupt, or reconfigure a network without explicit authorization.

## Weighted objective map

| Domain | Weight | Readiness evidence |
|---|---:|---|
| 1. Networking concepts | 23% | Explain layers, appliances, cloud, protocols, traffic types, media/connectors, topologies, IPv4 and modern network concepts through a packet path |
| 2. Network implementation | 20% | Select and reason about routing, switching, wireless, VLANs, interfaces, MTU, antennas, power and physical placement |
| 3. Network operations | 19% | Maintain documentation/configuration, monitor, recover, provide network services, and use secure access/management methods |
| 4. Network security | 14% | Apply identity, encryption, segmentation, physical controls and hardening; recognize concepts, attacks and compliance context |
| 5. Network troubleshooting | 24% | Use a repeatable method and appropriate evidence for cabling, switching, routing, addressing, wireless, performance and service faults |

**CURRENT BLUEPRINT:** The official page contains 34 summary rows. The [public N10-009 objectives PDF, document version 6.0](https://lecbyo.files.cmp.optimizely.com/download/35a7403ab73211ef9dcda6f347fbf652?checkExpiry=false) provides **25 numbered objectives**, in groups of 8/4/5/3/5, with substantially finer detail. Find it through [CompTIA’s resource portal](https://www.comptia.org/en-us/partner-portal/partner-resources/). The PDF’s document version 6.0 and the exam’s V9 label are separate identifiers.

| Published IDs | Coverage and evidence |
|---|---|
| 1.1–1.4 | OSI, appliances/functions, cloud, ports/protocols/traffic |
| 1.5–1.8 | Media/transceivers, topology, IPv4 planning, modern network environments |
| 2.1–2.4 | Routing, switching, wireless, physical installation |
| 3.1–3.5 | Processes/documentation, monitoring, disaster recovery, services, management |
| 4.1–4.3 | Security concepts, attacks, defenses |
| 5.1–5.5 | Methodology, cabling/interfaces, network services, performance, tools |

Unlike A+ V15’s scope note, this Network+ document explicitly includes troubleshooting methodology as objective 5.1. Use the correct exam’s outline.

## 1. Networking concepts — 23%

### Layers, encapsulation, devices, and traffic

Use the OSI model as an evidence map, not a rigid troubleshooting order. The physical layer moves signals; data link moves local frames using MAC addresses; network routes packets using logical addresses; transport supplies end-to-end delivery behavior and ports; session, presentation, and application describe conversation, representation, and user-facing protocols. Encapsulation adds headers as data travels down a stack; de-encapsulation removes them at the receiver. A switch usually forwards frames within a VLAN, while a router selects a path between IP networks. A firewall permits or denies flows; an IDS detects; an IPS can block; a load balancer distributes service traffic; a proxy intermediates; NAS generally presents file access while SAN presents block storage.

Unicast targets one receiver, broadcast all hosts in a broadcast domain, multicast an interested group, and anycast one suitable member of a distributed set. The destination can remain the same at one layer while another changes: across a routed path the end-to-end destination IP normally remains, but the source/destination MAC addresses are rebuilt for each local link. NAT/PAT can deliberately rewrite IP/port identity at a boundary.

> **Related item:** A packet capture shows what reached a capture point, not everything the user intended or every device did. Combine it with endpoint, switch, route, firewall, DNS, DHCP, application, and timing evidence.

### Protocol and service decisions

Learn ports as part of a service story: client/server roles, transport, secure alternative, discovery/configuration, authentication, and failure symptoms. DNS supplies records used in name resolution and other services; DHCP supplies configuration; NTP/PTP align time; HTTP/HTTPS carry web traffic; SSH provides encrypted administration; Telnet is plaintext; FTP is distinct from SFTP; SMTP transfers mail; SNMP supports monitoring; LDAP supports directory access; RDP provides remote desktop; SIP coordinates communications sessions. A listening port does not prove that an application is healthy, authorized, reachable through policy, or returning correct data.

TCP provides connection-oriented state, sequencing, acknowledgement, retransmission, and flow behavior; UDP has lower protocol overhead and no equivalent delivery guarantee. Choose based on application needs rather than assuming one is always superior. IPv4 private ranges are not Internet-routable by themselves; APIPA/link-local addressing commonly signals failed automatic configuration; loopback tests the local stack. A default gateway is the next hop for non-local destinations, not a general DNS or Internet setting.

### Addressing and subnetting

Given an address and prefix, determine network address, broadcast address, usable host range, host count, whether two endpoints are local, and the required route. A `/24` leaves eight host bits; a `/26` divides it into four 64-address blocks. VLSM allocates different prefix sizes to different needs; CIDR expresses prefix length and permits aggregation. Class A/B/C terminology can help recognize historical defaults but modern routing uses explicit prefixes.

For every subnetting problem, write the prefix, mask, block size, network boundary, last address, and usable range. Then relate the arithmetic to behavior: a wrong mask may make a remote address appear local, an exhausted DHCP pool can prevent allocation to a new client, and an incorrect gateway only breaks off-subnet traffic. IPv6 concepts still matter operationally even when the public summary emphasizes IPv4; distinguish link-local, global, multicast, SLAAC/DHCPv6 behavior, prefix and gateway/neighbor discovery rather than applying IPv4 broadcast/NAT assumptions.

### Ports and protocol boundaries

**CURRENT BLUEPRINT:** Learn the following assignments in a service conversation. The [IANA registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv) contains assignments, including transports that are not common implementations; a port number alone does not identify observed traffic.

| Service | Ports and operational distinction |
|---|---|
| FTP | TCP 21 control; TCP 20 is associated with active-mode data. Passive data uses a negotiated destination port. |
| SSH / SFTP | Usually TCP 22; SFTP is an SSH file-transfer protocol, distinct from FTP with TLS. |
| Telnet / SMTP | TCP 23 / TCP 25; recognize plaintext administration and mail-transfer roles. |
| DNS | UDP and TCP 53; TCP is useful beyond zone transfers. |
| DHCPv4 / TFTP | UDP 67 server and 68 client; TFTP initially contacts UDP 69 and uses transfer identifiers/ports thereafter. |
| HTTP / HTTPS | 80 / 443; conventional HTTP over TCP versus HTTPS with TLS, while HTTP/3 uses QUIC over UDP. |
| NTP / SNMP | Typically UDP 123; SNMP requests commonly 161 and notifications 162. |
| LDAP / LDAPS | 389 / 636; distinguish directory operations from the selected protected transport. |
| SMB / Syslog | TCP 445 / commonly UDP 514. Do not mistake TCP 514’s registry entry for the same service. |
| Mail submission | PDF lists “SMTPS” with 587. Operationally, distinguish STARTTLS submission on 587 from implicit TLS submission on 465. |
| SQL Server / RDP | Commonly TCP 1433 / 3389; actual instance and transport configuration can differ, including RDP UDP transport. |
| SIP | 5060 signaling; 5061 associated with TLS signaling. The media flow is a separate concern. |

[RFC 8314 section 3.3](https://www.rfc-editor.org/rfc/rfc8314.html) supports the submission distinction. Do not infer that opening port 587 proves encryption: require the intended TLS negotiation and server identity check. ICMP, GRE, IPsec AH and ESP are not application TCP/UDP services with ordinary port numbers. IKE negotiates IPsec security associations; a tunnel mechanism by itself does not guarantee confidentiality. IPv4 TTL and IPv6 Hop Limit constrain forwarding lifetime, not DNS cache duration.

### Original VLSM and forwarding exercise

The requirements below include all needed hosts, including a gateway. Allocate the largest broadcast LANs first inside `10.40.0.0/24`:

| Team | Hosts required | Allocation | Usable range | Broadcast |
|---|---:|---|---|---|
| Engineering | 90 | 10.40.0.0/25 | .1–.126 | .127 |
| Support | 50 | 10.40.0.128/26 | .129–.190 | .191 |
| Operations | 20 | 10.40.0.192/27 | .193–.222 | .223 |
| Guest | 10 | 10.40.0.224/28 | .225–.238 | .239 |

Two suitable point-to-point links can use `.240/31` and `.242/31`, with both addresses in each prefix usable under [RFC 3021](https://www.rfc-editor.org/rfc/rfc3021.html). That exception is not a rule for ordinary broadcast LANs. A `/32` identifies one IPv4 address. The `/24` summary includes 12 addresses not allocated above; advertising a summary does not make those addresses reachable. Class A/B/C labels are historical context, not a replacement for the actual CIDR prefix; class D denotes multicast and class E is reserved.

This original Python example uses the standard [ipaddress library](https://docs.python.org/3.13/library/ipaddress.html). It calculates a plan and performs longest-match lookup among already-installed routes. It does not configure interfaces, allocate leases or run a routing protocol.

```python
from ipaddress import ip_address, ip_network


def allocate_lans(pool_text, requirements):
    """Largest-first IPv4 LAN planning; each request counts all required hosts."""
    pool = ip_network(pool_text)
    if pool.version != 4 or not requirements:
        raise ValueError('Use an IPv4 pool and at least one LAN.')
    if any(type(n) is not int or n < 1 for n in requirements.values()):
        raise ValueError('Host counts must be positive integers.')
    cursor = int(pool.network_address)
    result = {}
    for name, hosts in sorted(requirements.items(), key=lambda item: -item[1]):
        # Conventional broadcast LANs reserve network and broadcast addresses.
        size = 1 << (hosts + 1).bit_length()
        cursor = ((cursor + size - 1) // size) * size
        if size > pool.num_addresses or cursor + size - 1 > int(pool.broadcast_address):
            raise ValueError('The pool cannot fit these LANs.')
        network = ip_network((cursor, 32 - (size.bit_length() - 1)))
        result[name] = network
        cursor += size
    return result


def forward(destination, installed_routes):
    """Longest match among already-installed routes; no route-learning model."""
    target = ip_address(destination)
    routes = [(ip_network(prefix), hop) for prefix, hop in installed_routes]
    matches = [(net, hop) for net, hop in routes
               if net.version == target.version and target in net]
    if not matches:
        return None
    longest = max(net.prefixlen for net, _ in matches)
    best = [(net, hop) for net, hop in matches if net.prefixlen == longest]
    if len(best) != 1:
        raise ValueError('Equal-prefix alternatives need a separate selection model.')
    return best[0][1]


if __name__ == '__main__':
    plan = allocate_lans('10.40.0.0/24',
                         {'engineering': 90, 'support': 50, 'operations': 20, 'guest': 10})
    for name, net in plan.items():
        print(name, net, net.network_address + 1, net.broadcast_address - 1)
    routes = [('0.0.0.0/0', 'upstream'), ('10.40.0.0/16', 'core'),
              ('10.40.0.0/24', 'branch'), ('10.40.0.128/26', 'support')]
    print('10.40.0.150 ->', forward('10.40.0.150', routes))
```

### Media, connectors, topology, and cloud

Match copper, fiber, coax, direct-attach copper, wireless, cellular, and satellite to distance, bandwidth, interference, latency, environment, cost, connector/transceiver and power needs. Know the roles of RJ11/RJ45, F/BNC, SC/LC/ST/MPO and compatible transceivers; a connector that physically fits is not proof of wavelength, fiber mode, speed, encoding, distance, polarity or vendor support. Structured cabling separates patch cords, horizontal runs, patch panels, intermediate/main distribution, and equipment rooms.

Recognize star, mesh, hub-and-spoke, point-to-point, three-tier, collapsed-core and spine-leaf designs. A diagram should reveal redundancy and failure domains, not just icons. In cloud networking, distinguish a virtual private cloud (VPC) boundary, subnets, route tables, security groups, cloud gateways, public/private/hybrid deployment, and SaaS/PaaS/IaaS responsibility. Network functions can be virtualized; software-defined control and infrastructure as code change how intent is deployed, but packets still traverse interfaces, routes and policies.

> **Related item:** Availability is an end-to-end property. Two links do not create resilience if they share power, conduit, provider, control plane, gateway, DNS, authentication, or an untested failover path.

### Modern environments — objective 1.8

**CURRENT BLUEPRINT:** The full PDF explicitly includes SDN/SD-WAN, VXLAN, zero trust, SASE/SSE, infrastructure as code and IPv6 addressing/transition. These are not merely provider marketing topics.

| Concept | Decision to explain |
|---|---|
| SDN / SD-WAN | Separate centrally expressed policy from forwarding; application-aware steering, transport independence and zero-touch provisioning still need connectivity, identity and verification. |
| VXLAN | Carry a Layer 2 segment across an IP underlay between tunnel endpoints. A VNI identifies an overlay; the underlay must route between endpoints and support encapsulation overhead. |
| Zero trust / SASE / SSE | Verify identity/context and least privilege. SASE combines networking and security functions; SSE describes the security-services subset. A product name does not prove a working access policy. |
| Infrastructure as code | Review templates/playbooks and inventory in source control, resolve conflicts, inspect the intended diff, test a limited deployment, monitor drift and prepare rollback. Repeated automation can repeat an error. |
| IPv6 transition | Dual stack runs both families; tunneling carries one protocol inside another; NAT64 translates between IPv6 and IPv4 contexts. Test name resolution, route, firewall and application support for the chosen method. |

The [VXLAN specification](https://www.rfc-editor.org/rfc/rfc7348.html) describes a 24-bit VNI and default UDP destination 4789. VXLAN encapsulation alone does not encrypt the carried frame. A CDN places content/service capacity nearer consumers; QoS classifies and schedules traffic under contention rather than creating extra physical bandwidth. Cloud network security groups/lists, gateways, VPN versus dedicated connectivity, elasticity and multitenancy each have provider-specific control boundaries; verify effective routes and policy on both directions.

## 2. Network implementation — 20%

### Routing and boundary behavior

A routing table maps prefixes to next hops/interfaces. Separate **route installation** from **packet forwarding**. Routing processes select candidate paths using their own rules; administrative preference helps choose between sources for the same prefix. Forwarding then selects the longest matching installed prefix. Do not compare OSPF cost directly with an unrelated protocol’s metric or make a low-distance default route override an installed specific route. Static routes are predictable but manually maintained. OSPF and EIGRP are dynamic interior routing approaches with different operational ecosystems; BGP exchanges reachability and policy between autonomous systems and in large environments. Know their purposes and evidence without assuming vendor-specific command syntax is universal.

Default routes cover destinations without a more specific match. Route aggregation reduces table size but can hide reachability mistakes. NAT maps addresses; PAT distinguishes sessions with ports. First-hop redundancy presents a virtual gateway backed by multiple devices. A virtual IP may also front a load-balanced service. A router subinterface can terminate multiple VLANs over one trunk; verify tagging, native/untagged expectations, addresses, ACLs, MTU and return routes.

**Worked route case:** Suppose `0.0.0.0/0`, `10.40.0.0/16`, `10.40.0.0/24` and `10.40.0.128/26` are installed. Destination `10.40.0.150` matches all four, so forwarding uses `/26`; `10.40.0.65` uses `/24`; `10.40.1.2` uses `/16`. A second candidate for the same `/26` belongs to the installation/path-selection question. Policy routing, equal-cost paths and platform rules require additional analysis. See [Cisco’s route-installation and forwarding explanation](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html); its platform distances and syntax are not universal vendor defaults.

### Switching and VLANs

Switches learn source MAC addresses and associate them with ports/VLANs, then forward known unicast, flood unknown unicast within the permitted VLAN forwarding topology, and age entries. VLANs create logical broadcast domains. An ordinary access-port data connection belongs to one VLAN; a trunk carries VLAN tags between compatible endpoints. A phone plus attached PC can use a separately configured voice VLAN, so inspect the actual port mode and tagging. An SVI provides a Layer 3 interface for a VLAN; creating a VLAN alone does not create routing. Inter-VLAN traffic needs routing and policy. A native-VLAN or allowed-VLAN mismatch can create one-way or partial symptoms.

Spanning Tree prevents Layer 2 loops by selecting a logical loop-free path; a blocked link can be healthy standby, while an unexpected root or topology change can disrupt service. Link aggregation combines compatible links but requires matching configuration. MTU mismatch can allow small tests while larger packets fail or fragment. Jumbo frames must be supported consistently along the relevant path.

**PRACTICAL DEPTH — MTU budget:** With an underlay IP MTU of 1500, an illustrative VXLAN packet using a 20-byte outer IPv4 header, 8-byte UDP header, 8-byte VXLAN header and 14-byte inner Ethernet header leaves **1450 bytes for the inner IP packet**. A 40-byte outer IPv6 header leaves 1430. This assumes no extra tags, options, extensions or IPsec overhead; outer Ethernet is outside the stated IP MTU. Verify the actual encapsulation and platform MTU definition.

[IPv6](https://www.rfc-editor.org/rfc/rfc8200.html) routers do not fragment forwarded packets; the source handles any fragmentation. [Path MTU Discovery](https://www.rfc-editor.org/rfc/rfc8201.html) uses ICMPv6 Packet Too Big feedback. Blocking that feedback can let a small handshake succeed while larger transfers stall. An observed stall still needs evidence; it is not proof of MTU trouble.

### Wireless and physical installation

Plan Wi-Fi by coverage, capacity, interference, channel reuse, frequency band, client capability, authentication/encryption, roaming, antenna pattern, power, backhaul and regulatory constraints. 2.4 GHz often travels farther but has fewer non-overlapping channels and more interference; 5/6 GHz offer more capacity/options with different range and compatibility. SSID is a network name, not a security boundary. Prefer supported strong encryption and enterprise authentication where requirements justify it; isolate guest and untrusted/IoT access.

Omnidirectional antennas radiate broadly around an axis; directional antennas focus energy. AP placement and orientation matter. Autonomous, controller-managed, and cloud-managed APs change operations, not radio physics. Survey before and after deployment using channel, signal, noise and utilization evidence rather than bars alone.

Physical installation includes rack units, airflow, grounding/bonding, UPS/PDU capacity, PoE standards/budget, cable management/radius, labeling, environmental sensors, fire suppression, locks and safe lifting. Verify maximum draw and redundancy, not only normal load. Document every port, patch, optic, circuit and owner before change.

> **Related item:** Intent-based automation and templates improve consistency only when prechecks, scoped credentials, review, canary deployment, telemetry and rollback protect against consistently deploying the wrong intent.

A BSSID identifies a particular wireless basic service set; an SSID is the advertised network name, and several APs can participate in the same extended service set. A captive portal governs a login/acceptance workflow and does not replace link encryption. Compare mesh backhaul, infrastructure, ad hoc and point-to-point uses. Wider channels consume more spectrum; band steering and a strong signal do not guarantee capacity. **VERIFY CURRENT:** channel availability, DFS/802.11h requirements, permitted power and 6 GHz deployment conditions depend on region and equipment.

**Original power-budget case:** A switch has a 370 W PoE budget. Reserve 15% for planning, leaving 314.5 W; four 30 W allocations plus eight 15.4 W allocations total 243.2 W, leaving 71.3 W under that planning ceiling. These are specified switch-side allocations, not a promise of delivered device power or an electrical-circuit rating. Check negotiated standards, startup draw, cable loss, supply-failure capacity and the manufacturer’s limits.

## 3. Network operations — 19%

### Documentation, lifecycle, configuration, and change

Maintain physical and logical diagrams, rack elevations, cable/port maps, inventory, IP address management, wireless surveys, circuit/provider records, configurations, owners and SLAs. A logical diagram answers addressing, VLAN, route, security-zone and dependency questions; a physical diagram answers location, cable, port, power and failure-domain questions. Date, version and reconcile both with observed state.

Lifecycle management tracks acquisition, warranty, licensing, firmware/software, support, end of sale/support/life, spares, replacement and approved decommission/data handling. Store production configuration plus versioned known-good backup and baseline. Change records need purpose, scope, risk/impact, approval, maintenance window, communication, implementation, validation, rollback and review. An emergency can shorten approval but should not erase evidence.

### Monitoring and observability

SNMP exposes structured device data and can send notifications; use supported secure versions. Flow records summarize conversations; packet captures reveal packet-level detail; logs record events; API queries/telemetry expose state; interface counters show errors, drops and utilization; port mirroring supplies traffic to an analyzer. Baselines make “normal” measurable. Correlate clocks, client/server/device logs, changes and monitoring rather than diagnosing from one alarm.

Define thresholds around service impact and expected variation. High utilization can be legitimate; low utilization can coexist with loss or policy failure. Monitor latency, jitter, packet loss, availability, errors/discards, CPU/memory, environment, wireless health, route/neighborhood changes, certificate/lease/capacity expiry, configuration drift and business service checks. Protect monitoring credentials and captured data.

For SNMP, distinguish community-based v2c from a correctly configured v3 security level. [SNMPv3’s user security model](https://www.rfc-editor.org/rfc/rfc3414.html) supports different authentication/privacy combinations; the string “v3” alone does not prove payload encryption. Keep credentials out of capture/ticket output. Flow records, counters, syslog/SIEM, API telemetry, discovery and mirrored packets answer different questions; discovery may actively probe and requires an approved scope.

### Availability, disaster recovery, and services

RPO is acceptable data loss measured backward; RTO is acceptable restoration time; MTTR measures average repair/restoration time; MTBF describes average time between failures for repairable systems. Cold, warm and hot sites trade cost against readiness. Active-active serves traffic from multiple systems; active-passive holds standby capacity. Neither label proves failover, data consistency or capacity—test it.

DHCP scopes/options/leases/relays distribute address configuration. SLAAC derives IPv6 configuration; DNS zones/records/resolvers/caches create the name path. NTP, PTP and NTS serve different precision and security needs. A service can be running but wrong: stale DNS, exhausted leases, incorrect option/gateway, time hierarchy failure or blocked relay produces real outages.

### DHCP, DNS and time boundaries

For DHCPv4, identify discovery/offer/request/acknowledgement, relay placement, subnet scope, options, reservations, exclusions and lease timers. A new client can fail when all allocatable addresses are occupied while an existing client renews its own lease. [RFC 2131’s renewal/rebinding rules](https://www.rfc-editor.org/rfc/rfc2131.html) distinguish contacting the original server, later contacting other servers, and stopping use when a lease expires without renewal. Do not diagnose exhaustion solely from one link-local address.

IPv6 SLAAC uses router-advertised information; [Neighbor Discovery](https://www.rfc-editor.org/rfc/rfc4861.html) also supplies router discovery and link-layer neighbor functions. DHCPv6 and DNS information are separate considerations. Do not assume that DHCPv6 supplies the default gateway or that IPv6 uses ARP/broadcast.

| DNS question | Record or evidence |
|---|---|
| Address for a name | A for IPv4, AAAA for IPv6 |
| Alternate name | CNAME, with the target’s separate address records |
| Mail routing or domain metadata | MX preference/target; TXT text interpreted by the relevant application |
| Delegation/server or reverse name | NS; PTR in the reverse namespace |
| Which server answered? | Authoritative zone versus recursive/cache answer; primary/secondary describes zone maintenance, not whether a cache is authoritative |
| No answer received | Distinguish timeout from an actual NXDOMAIN, NOERROR with no requested type, REFUSED or SERVFAIL response |

DNSSEC validates signed DNS data and denial of existence; it does **not** encrypt queries. [RFC 4033](https://www.rfc-editor.org/rfc/rfc4033.html) supplies that distinction. [DoT](https://www.rfc-editor.org/rfc/rfc7858.html) protects a DNS transport over TLS, normally TCP 853; [DoH](https://www.rfc-editor.org/rfc/rfc8484.html) carries DNS messages over HTTPS. Both require the intended resolver identity and protect a particular transport path. They do not by themselves make a resolver truthful, validate every upstream answer or encrypt the subsequent web application.

Peter Wu’s October 29, 2019 [DNS encryption article](https://blog.cloudflare.com/dns-encryption-explained/) is useful for the resolver/transport trust distinction and split-DNS implications. Its old browser, systemd and command examples are historical; use current product documentation for deployment. Approved enterprise resolver policy, private names and logging requirements must be considered when choosing an encrypted resolver.

NTP supplies clock synchronization; PTP serves precision-oriented environments with suitable network/timestamp support. [Network Time Security](https://www.rfc-editor.org/rfc/rfc8915.html) uses TLS-based key establishment separately from authenticated NTP exchanges. Authenticating a time source does not prove that the source is accurate or that the network meets a precision target.

Use approved VPN, SSH, HTTPS GUI/API, console and out-of-band management. Separate management traffic, require strong identity/MFA where supported, least privilege, encrypted protocols, source restrictions, logging and credential rotation. Console access is valuable during network failure but still needs physical and identity controls. Distinguish site-to-site from client-to-site VPN, split from full tunnel, clientless application access, and an authorized jump host. An out-of-band path should survive the failure being diagnosed; sharing the same failed power or uplink can defeat its purpose.

> **Related item:** A service-level objective should be tested from the consumer’s path. Device uptime alone misses failed name resolution, authentication, policy, application response, or upstream dependency.

### Original DNS exercise on loopback

Install `dnslib==0.9.26` and `dnspython==2.8.0` in a disposable Python virtual environment using its `python -m pip install` command. The [dnslib project](https://pypi.org/project/dnslib/) supplies packet/server primitives; [dnspython](https://pypi.org/project/dnspython/) supplies an independent client and its [query API](https://dnspython.readthedocs.io/en/stable/query.html). Save this original example as `dns_loopback.py` and run it with that environment’s Python.

The two listeners bind only `127.0.0.1`, each using an OS-selected port. Names and answers are synthetic; the resolver makes no upstream requests and does not change system DNS. It handles a small set of demonstration records, not a complete production DNS service. TCP and UDP use different selected ports here to avoid a same-port allocation race; ordinary DNS commonly uses 53 for both.

```python
from contextlib import contextmanager
from dnslib import A, AAAA, CNAME, NS, SOA, QTYPE, RCODE, RR
from dnslib.server import BaseResolver, DNSServer, DNSLogger
import dns.flags
import dns.message
import dns.query
import dns.rcode


class PracticeZone(BaseResolver):
    """Small nonrecursive zone for synthetic names; no upstream requests."""
    def resolve(self, request, handler):
        reply = request.reply(aa=1, ra=0)
        name = str(request.q.qname).lower()
        kind = request.q.qtype
        records = {
            'lab.test.': [(QTYPE.SOA, SOA('ns.lab.test.', 'hostmaster.lab.test.',
                                        (1, 3600, 600, 86400, 30))),
                          (QTYPE.NS, NS('ns.lab.test.'))],
            'ns.lab.test.': [(QTYPE.A, A('192.0.2.53'))],
            'router.lab.test.': [(QTYPE.A, A('192.0.2.10')),
                                 (QTYPE.AAAA, AAAA('2001:db8::10'))],
            'alias.lab.test.': [(QTYPE.CNAME, CNAME('router.lab.test.'))],
        }
        if name != 'lab.test.' and not name.endswith('.lab.test.'):
            reply.header.aa = 0
            reply.header.rcode = RCODE.REFUSED
            return reply
        if name not in records:
            reply.header.rcode = RCODE.NXDOMAIN
        else:
            for record_type, data in records[name]:
                if record_type == kind or record_type == QTYPE.CNAME:
                    reply.add_answer(RR(name, record_type, ttl=30, rdata=data))
                    if record_type == QTYPE.CNAME and kind in (QTYPE.A, QTYPE.AAAA):
                        for target_type, target_data in records['router.lab.test.']:
                            if target_type == kind:
                                reply.add_answer(RR('router.lab.test.', target_type,
                                                    ttl=30, rdata=target_data))
        if not reply.rr:
            # SOA distinguishes a useful negative answer from a silent timeout.
            reply.add_auth(RR('lab.test.', QTYPE.SOA, ttl=30,
                              rdata=records['lab.test.'][0][1]))
        return reply


@contextmanager
def practice_servers():
    """Bind only loopback, using a different OS-selected port per transport."""
    servers = []
    try:
        for tcp in (False, True):
            server = DNSServer(PracticeZone(), address='127.0.0.1', port=0,
                               tcp=tcp, logger=DNSLogger(logf=lambda *_: None))
            server.start_thread()
            servers.append(server)
        yield {('tcp' if i else 'udp'): server.server.server_address[1]
               for i, server in enumerate(servers)}
    finally:
        for server in servers:
            server.stop()
            server.server.server_close()
            server.thread.join(timeout=2)
            if server.thread.is_alive():
                raise RuntimeError('Practice listener did not stop.')


def ask(ports, name, kind='A', transport='udp'):
    query = dns.message.make_query(name, kind)
    query.flags &= ~dns.flags.RD
    method = {'udp': dns.query.udp, 'tcp': dns.query.tcp}[transport]
    return method(query, '127.0.0.1', port=ports[transport], timeout=2)


if __name__ == '__main__':
    with practice_servers() as ports:
        for transport in ('udp', 'tcp'):
            for name, kind in [('router.lab.test.', 'A'), ('alias.lab.test.', 'A'),
                               ('router.lab.test.', 'TXT'), ('missing.lab.test.', 'A'),
                               ('outside.test.', 'A')]:
                response = ask(ports, name, kind, transport)
                print(transport, name, kind, dns.rcode.to_text(response.rcode()),
                      [rrset.to_text() for rrset in response.answer])
```

Expected comparisons: `router` returns A data; `alias` returns CNAME plus target A; TXT for the existing router name returns NOERROR without that record type; a missing in-zone name returns NXDOMAIN; an outside name returns REFUSED. Negative in-zone responses include an SOA. A DNS error reply proves communication with this listener, unlike a timeout. All data has a 30-second TTL, but this example has no cache and does not test TTL expiry.

Both public examples ran with Python 3.13.14. A separate harness passed **72 checks**, including 14 real UDP/TCP DNS exchanges for A, AAAA, CNAME, missing type/name, refusal and case-insensitive names. The public DNS run added ten exchanges, for **24 total**. Listeners stopped and their sockets were released. Subnet, route, MTU, PoE and rate cases are calculations/models; the DNS exchanges are actual local protocol execution. No DHCP server, routing protocol, TLS, DNSSEC, cache, packet capture, Wi-Fi, switch, firewall, hosts file, system resolver or remote network was changed or tested. All eight complete labs remain proposed.

## 4. Network security — 14%

### Control model and identity

Confidentiality limits disclosure, integrity protects correctness, and availability preserves access. A threat can exploit a vulnerability and create risk to an asset; likelihood and impact guide treatment. Defense in depth layers preventive, detective, responsive and recovery controls. Encrypt data in transit and at rest, manage keys/certificates through PKI and lifecycle controls, and avoid confusing encryption with authentication or authorization.

Identity systems may use MFA, SSO, RADIUS, TACACS+, LDAP or SAML in different roles. Authentication proves identity; authorization applies least privilege or role-based access; accounting/audit records activity. Time synchronization matters to logs, certificates and time-based authentication. Network access control can assess identity/posture before or during admission. Physical locks, cameras and controlled rooms complement logical controls. Honeypots/honeynets are monitored decoys, not production trust zones.

### Segmentation, attacks, and hardening

Segment user, server, management, guest, BYOD, IoT/IIoT, SCADA/ICS and operational technology according to trust, safety, protocol and availability needs. Apply ACLs, firewall zones, screened subnets, filtering and micro/perimeter controls with explicit source, destination, service, direction and state. Test allowed and denied cases plus return traffic. Regulation and policy—such as PCI DSS or GDPR context—affect scope and handling; confirm current organizational/legal guidance rather than memorizing a universal configuration.

Recognize DoS/DDoS, VLAN hopping, MAC flooding, ARP poisoning/spoofing, DNS poisoning/spoofing, rogue services/devices, evil twins, on-path attacks and social engineering. Map each to preconditions, evidence and layers of mitigation. Hardening includes patch/firmware management, secure configuration, disabling unused interfaces/services/protocols, changing defaults, strong management identity, certificate/key management, segmentation, NAC, ACLs, monitoring, configuration backup and tested recovery.

> **Related item:** Zero trust is an architecture principle of explicit verification, least privilege and assumed breach; it is not a single appliance or permission to ignore network segmentation.

## 5. Network troubleshooting — 24%

### Method before command

Identify the problem: user, system, exact symptom, time, scope, impact, recent change, topology and expected behavior. Establish a theory from evidence, test it safely, create a plan with risk/approval/rollback, implement, verify full functionality and preventive measures, then document. Escalate when authority, safety, security, service impact or expertise requires it. Do not change several variables and then call the last one root cause.

Use a known-good comparison and narrow boundaries: local stack, link, VLAN, gateway, route, DNS/DHCP/authentication, policy, server/application and return path. `ipconfig`/`ifconfig`/`ip`, `ping`, `traceroute`/`tracert`, `arp`/neighbor tools, `route`, `nslookup`/`dig`, `netstat`/`ss`, packet capture, port/service tests and device show commands answer different questions. A successful ping does not prove DNS, TCP port, TLS, identity or application health.

### Physical, switching, addressing, and routing faults

Wrong cable/fiber/transceiver, bad termination, split pair, bend/damage, electromagnetic interference, crossed Tx/Rx/polarity, dirty fiber, excessive distance, speed/duplex mismatch, PoE budget and marginal signal can create errors, flaps, loss or no link. Inspect link state, negotiated speed/duplex, interface counters, optic diagnostics, PoE state, cable tester/certifier and known-good components. Never look into fiber; follow electrical, ladder and site safety.

For switching, inspect port/VLAN mode, allowed/native VLANs, MAC table, STP state/root/topology change, aggregation and ACL/port-security. For routing, inspect interface/subnet, routing table and longest match, next hop, default route, dynamic neighbor/status, NAT, ACL/firewall, asymmetry and return route. For addressing, distinguish duplicate/static error, wrong prefix/gateway/DNS, expired or exhausted DHCP, APIPA, relay and IPv6 neighbor/SLAAC issues.

### Performance, wireless, and service faults

Congestion, insufficient bandwidth, bottleneck, latency, jitter and loss are related but distinct. Measure at relevant times and both directions; compare interface, flow, packet, application and baseline data. Wireless failures can arise from interference, overlap, low signal-to-noise, attenuation, channel width, utilization, power/antenna/placement, roaming, authentication, encryption, DHCP/DNS or upstream capacity. A stronger signal can still be a worse busy channel.

For DNS, compare name and direct-address tests, resolver configuration, authoritative/delegation/record/caching and reachability. For DHCP, inspect link/VLAN/relay/server, scope capacity, lease and options. For NTP/authentication/VPN, check time, identity/certificate, reachability, policy and logs. When a repair works, repeat the user workflow, verify security and redundancy, monitor for recurrence, update diagrams/configuration/ticket, and record the actual cause and prevention.

> **Related item:** Root cause and trigger can differ. A routine change may expose an undocumented capacity, redundancy, MTU or policy weakness; fix the service, then address the systemic condition.

### Select a tool by the unresolved question

| Evidence needed | Tool and limit |
|---|---|
| Cable identity versus correctness | A toner locates a run; a wire-map tester finds basic faults; certification evaluates the stated cable standard. They do not answer the same question. |
| Fiber continuity versus full optical budget | A visual fault locator helps locate a break; appropriate measurement/optic diagnostics answer loss and signal questions. Follow fiber safety. |
| Frames at one observation point | Authorized tap/mirror plus protocol analyzer or `tcpdump`; dropped capture packets or a misplaced observation point can hide traffic. |
| Neighbor/device relationship | LLDP/CDP and switch MAC/VLAN/interface tables; discovery data is evidence, not proof of authorization or complete topology. |
| Listening services or reachability | Authorized Nmap/service probes, `netstat`/`ss` and endpoint tests; limit active discovery to agreed targets. No scan was performed here. |
| Port state and forwarding/power | Platform equivalents of `show interface`, `show route`, `show arp`, `show vlan`, `show config` and `show power`; exact syntax and privilege vary. |

Runts/giants, CRC errors and drops have different meanings; correlate them with platform counter definitions, speed/duplex, MTU and media. Administratively down, error-disabled and suspended ports also require different investigations. A throughput test consumes capacity; record endpoint capability, path, direction and load before interpreting it.

## Integrated scenarios

### Scenario 1: New branch with intermittent cloud access

Map clients, Wi-Fi, access VLANs, switch trunks, gateway, WAN/VPN, DNS, identity and cloud policy. Establish addressing, channel/utilization, errors/loss/latency, routes/NAT and service checks. A small ping working does not rule out MTU or application/TLS trouble. Correct one approved fault, validate wired/wireless and allowed/denied cloud workflows, test failover, update diagrams and baseline.

### Scenario 2: Voice quality degrades every afternoon

Define affected sites/users/times and measure latency, jitter, loss, utilization, queue/drop, wireless and provider evidence. Correlate flow and scheduled workload without capturing unnecessary content. Test the bandwidth/queue/path theory, apply an approved capacity or QoS correction, verify calls plus competing traffic and rollback, then document monitoring thresholds and ownership.

### Scenario 3: Rogue wireless and address failures

Users receive warnings and incorrect gateways. Preserve SSID/BSSID/channel, lease/server, ARP/DNS, authentication and physical evidence; involve security response. Do not connect broadly or attack the device. Locate through authorized wireless/switch/physical controls, contain per policy, restore trusted DHCP/DNS/access, rotate affected credentials if required, validate segmentation and report lessons learned.

## Hands-on labs

All eight full labs remain proposed. Use owned traffic, synthetic data and an authorized simulator or isolated environment; the limited loopback DNS execution above is recorded separately.

1. **Packet walk:** draw the intended name, address, VLAN, route and policy path; capture only your own test exchanges at a known point. Annotate DNS, ARP/neighbor discovery, transport and application boundaries. Success: explain one observed exchange and what the capture cannot establish; negative case: a successful ping with a failed application.
2. **Subnet plan:** allocate four LANs and two point-to-point links, record every gateway/range and check overlaps. Compare the original model above with manual binary boundaries. Success: all requirements fit with stated reservations; negative case: show why an oversized request fails and why a route summary can include unused space.
3. **Switching:** build access/voice/trunk VLANs, an SVI or router path, and STP redundancy in a simulator. Inject one allowed-VLAN or gateway mismatch. Success: permitted traffic and standby path behave as intended; demonstrate that a blocked STP port can be healthy and restore the baseline.
4. **Routing/services:** configure private static/default routes, DHCP and DNS, adding NAT/PAT only where the design needs it. Compare new lease allocation with existing-lease renewal, authoritative answers with cache behavior, and forward with return routes. Success: name and application work; distinguish negative DNS response from timeout and test a denied flow.
5. **Wireless survey:** compare two approved locations/bands/channels using signal, noise, utilization, client capability and measured throughput. Record local regulatory/equipment limits and guest policy. Success: explain a tradeoff and validate after one change; negative case: strong signal on a busy channel.
6. **Operations packet:** produce physical/logical diagrams, IPAM, asset/lifecycle records, configuration backup, baseline, change/rollback and recovery targets. Conduct a tabletop and a separate authorized restore test. Success: identify shared failure domains and show how recovery evidence meets or misses RPO/RTO.
7. **Security tabletop/simulator:** segment user, management, guest and IoT zones, define minimum allowed flows and test denied paths. Walk through invented rogue DHCP/AP or on-path indicators with evidence preservation and escalation. Success: distinguish detection from prevention and close temporary grants; do not attack a live network.
8. **Troubleshooting capstone:** introduce one reversible physical/interface, VLAN, addressing, DNS or performance fault at a time. Record theory, discriminating evidence, approved action and rollback. Success: original application, security and relevant failover work after repair; explain why the selected tool and counter actually support the diagnosis.

## Original knowledge checks

1. During a routed packet walk, which Layer 2 and Layer 3 addresses normally change at each hop?
2. What is the operational difference among a switch, router, firewall, IDS and IPS?
3. Why does an open TCP port not prove a healthy application?
4. When is UDP preferable even though it lacks TCP delivery behavior?
5. Distinguish unicast, broadcast, multicast and anycast.
6. What evidence would APIPA addressing suggest?
7. For `192.0.2.70/26`, what are the network, broadcast and usable range?
8. Why can a wrong subnet mask break only some destinations?
9. What must match besides connector shape for a fiber transceiver path?
10. How do spine-leaf and three-tier topologies differ conceptually?
11. What customer responsibilities remain in IaaS that may move to the provider in SaaS?
12. Why can two nominally redundant links share one failure domain?
13. How does longest-prefix matching affect route selection?
14. Distinguish NAT from PAT.
15. What purpose does a first-hop redundancy virtual address serve?
16. Why can an allowed/native VLAN mismatch create partial connectivity?
17. What does a blocked STP port mean in a healthy redundant design?
18. How can MTU mismatch pass small tests but fail applications?
19. Which data belongs in a Wi-Fi survey beyond signal strength?
20. Why must PoE budget include worst-case rather than current draw?
21. Which questions require a logical rather than physical diagram?
22. What must a configuration backup record to be useful?
23. How do flow records differ from packet capture?
24. Why is a baseline necessary before setting thresholds?
25. Distinguish RPO, RTO, MTTR and MTBF.
26. Why does active-passive not itself prove recoverability?
27. What symptoms can an exhausted DHCP scope create?
28. Why can incorrect time look like an identity or certificate failure?
29. Which controls belong on a management plane?
30. Distinguish threat, vulnerability, exploit and risk.
31. How do authentication, authorization and accounting differ?
32. Why segment guest, IoT and operational technology differently?
33. Which evidence distinguishes a rogue DHCP service from ordinary lease failure?
34. How can ARP poisoning support an on-path attack?
35. Why is zero trust not a replacement for segmentation?
36. What are the required stages of the troubleshooting method?
37. What does a successful ping fail to prove?
38. Which counters suggest duplex, media or congestion trouble?
39. How would you separate DNS failure from server failure?
40. Why can strong Wi-Fi signal coexist with poor performance?
41. What validation should follow a network repair?
42. What exactly is announced about N10-009 retirement?

43. Why are DNSSEC and DoH/DoT complementary rather than interchangeable?
44. What is wrong with treating port 587 as proof of implicit TLS?

## Answers and reasoning

1. Link-local source/destination MAC addresses are rebuilt; end-to-end IPs normally remain unless translation occurs.
2. Local frame forwarding, inter-network routing, policy enforcement, detection, and inline detection/blocking respectively.
3. The listener may be wrong, unhealthy, unauthorized, unreachable through another control, or returning invalid data.
4. When low overhead/timeliness or application-managed recovery matters more than TCP ordering/retransmission.
5. One receiver, all in a broadcast domain, an interested group, and one suitable distributed receiver.
6. Automatic IPv4 link-local use often indicates that the intended DHCP configuration was not obtained, but the address alone is not proof of the cause. Inspect interface state, lease history, VLAN, relay, server and scope; rule out manual configuration.
7. Network `192.0.2.64`, broadcast `.127`, usable `.65–.126`.
8. It changes which destinations the host treats as local versus requiring its gateway.
9. Fiber mode, wavelength, speed/encoding, reach, polarity, cable/optic type and platform support.
10. Spine-leaf gives predictable east-west paths; three-tier separates access, distribution and core roles.
11. Guest OS, applications/data, identity, configuration and network/security controls according to the service contract.
12. Common conduit, power, provider, gateway, control plane, DNS, identity or untested failover can remain.
13. Forwarding uses the longest matching installed prefix. Administrative preference and each routing protocol’s path-selection rules address which candidates get installed; they do not let a less-specific default override a specific installed route.
14. NAT maps addresses; PAT also uses transport ports to distinguish multiple sessions/translations.
15. Hosts keep one gateway address while multiple devices provide availability.
16. Some VLANs or untagged traffic may traverse while others are dropped or placed incorrectly.
17. STP intentionally removed that path from forwarding to prevent a Layer 2 loop; it may be standby.
18. Encapsulation can exceed the path MTU even when small probes pass. IPv4 behavior depends on fragmentation flags and implementation; IPv6 routers send Packet Too Big rather than fragmenting forwarded packets. Missing feedback can stall larger transfers.
19. Band/channel/width, noise, SNR, utilization, overlap, client capability, roaming, throughput and obstacles.
20. Devices can request more power during startup/load and redundant supplies/circuits need safe capacity.
21. Addressing, VLAN, route, security zone, dependency and service-flow questions.
22. Device/owner, timestamp, software version, integrity, secrets handling, restore procedure and tested result.
23. Flow summarizes conversations/metadata; capture exposes individual packet headers and possibly sensitive payload.
24. Normal ranges and cycles are needed to distinguish anomaly from legitimate variation.
25. Acceptable data loss, restoration time, average repair time, and average time between failures.
26. Standby capacity, state, dependencies, routing/DNS and procedures may fail unless exercised under load.
27. New allocation can fail while an existing client renews its current lease. Inspect actual lease/server/relay state and expiry; exhaustion alone does not prove every renewal must fail.
28. Tokens, logs, certificates and time-based authentication depend on acceptable clock alignment.
29. Segmentation, restricted sources, encrypted protocols, MFA/least privilege, logging, rotation and out-of-band protection.
30. Potential cause, weakness, method/use of weakness, and likelihood-impact exposure to an asset.
31. Prove identity, grant permitted actions, and record activity.
32. They have different trust, patchability, protocols, safety, availability and data consequences.
33. Unexpected server identifier/options/gateway plus captures, leases, switch location and server logs.
34. False IP-to-MAC mappings can redirect local traffic through an attacker-controlled system.
35. Explicit verification and least privilege still benefit from bounded paths and reduced blast radius.
36. Identify, theorize, test, plan, implement, verify/prevent, and document, with escalation where needed.
37. DNS, TCP/UDP service, TLS, identity, policy, application correctness, performance or resilience.
38. CRC/input errors suggest media; late collisions/duplex indicators suggest negotiation; drops/queues suggest congestion.
39. Compare name resolution and direct-address tests, then authoritative/cache/record evidence and application reachability.
40. The channel may be noisy, congested, overlapping, rate-limited or bottlenecked upstream.
41. Original workflow, allowed/denied security, performance, failover where relevant, monitoring and documentation.
42. No exact date; CompTIA says usually three years after launch and estimates 2027.

43. DNSSEC provides signed-data authenticity/integrity and authenticated denial; DoH/DoT protect a client-resolver transport. Encrypted transport alone does not validate all authoritative data, and DNSSEC does not hide the query.
44. Port 587 commonly uses explicit STARTTLS negotiation for submission; implicit TLS submission on 465 starts with TLS. Verify negotiation and certificate identity, not just the port number.

## N10-008-to-N10-009 gap checklist

Map older material line by line to V9 rather than assuming continuity. Verify current treatment of modern physical and virtual appliances, cloud and virtual networking, spine-leaf and collapsed-core designs, IPv4 subnetting/VLSM/CIDR, modern routing and first-hop behavior, wireless bands/security/deployment, physical power/environment, IPAM/lifecycle/change and configuration management, API/flow/log/capture monitoring, disaster-recovery measures, SLAAC and secure time, management methods, identity/federation/NAC, IoT/IIoT/SCADA/ICS/OT segmentation, current attacks/hardening, and the full troubleshooting/tool set. The public full PDF explicitly includes SD-WAN, VXLAN, SASE/SSE, zero trust, infrastructure as code and IPv6 transitions in objective 1.8; review these even when a summary or older path omits them.

## Source and freshness notes

- CompTIA controls the V9 domains, weights, delivery, score/languages, experience recommendation and estimated lifecycle.
- Protocol implementations, wireless standards/regulation, cloud responsibility, threats, firmware, security guidance, provider routes and practice banks change. Verify commands and configurations against the current product, vendor and organizational documentation.
- This guide contains original scenarios, labs, checks and explanations synthesized from public scope. It does not reproduce proprietary objectives, course labs, PBQs or recalled exam items.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one coherent N10-009 course or book, build an authorized lab, and use one explanation-led practice source to target weak domains.

| Resource | Access | Estimated time |
|---|---|---:|
| CompTIA [CertMaster Perform](https://www.comptia.org/en-us/resources/certmaster-training/perform/), [Learn](https://www.comptia.org/en-us/resources/certmaster-training/learn/), [Labs](https://www.comptia.org/en-us/resources/certmaster-training/labs/) and [Practice](https://www.comptia.org/en-us/resources/certmaster-training/practice/) | Paid official options; select exact N10-009 product/bundle | Provider estimates: Perform 30–60h; Learn 25–40h; Labs 15–25h; Practice 10–20h; avoid double-counting overlap |
| [Pluralsight Network+ path](https://www.pluralsight.com/paths/comptia-network-n10-009) | Subscription; 12 courses and practice exam; generic path text also mentions labs, without a verified lab count | 14 listed hours plus 25–50 lab/review hours |
| [LinkedIn Learning / Total Seminars N10-009](https://www.linkedin.com/learning/comptia-network-plus-n10-009-cert-prep) | Subscription; released April 25, 2025; public course outline available | 18 hours 51 minutes plus 25–50 lab/review hours |
| [O'Reilly/Pearson N10-009 Cert Guide](https://www.oreilly.com/library/view/comptia-network-n10-009/9780135367919/) | Subscription book; earlier listing reported 804 pages | Earlier 18h44 listing not reverified; allow 20–40 additional lab/review hours |
| [O'Reilly/Sybex Network+ Study Guide](https://www.oreilly.com/library/view/comptia-network-study/9781394235605/) | Subscription book; earlier listing reported 1,024 pages and an online bank | Earlier 27h27 listing not reverified; allow 20–40 additional lab/review hours |
| [Udemy / Jason Dion N10-009](https://www.udemy.com/course/comptia-network-009/) | Paid marketplace course with practice exam | Verify current runtime; allow 30–60 hours with labs/review |
| [MeasureUp N10-009 practice test](https://www.measureup.com/comptia-network-n10-009-practice-test.html) | Paid explanation-led practice; product-specific listing says 219 questions, released June 2024 | About 8–15 hours across attempts and remediation |
| [Professor Messer free N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) | Free 87-video course; optional paid notes/practice | 12 hours 55 minutes plus 25–50 hands-on hours |

No exact current Whizlabs N10-009 route was independently verified. Reject “actual questions” and dumps. Provider duration, price, bundle, bank, update and access details are volatile.

Public metadata was checked September 29, 2026. Pluralsight lists 12 courses/14 hours; LinkedIn 18h51; Messer 87 videos/12h55. MeasureUp’s product-specific 219-question count differs from generic FAQ wording about 150 questions; use the product-specific figure while checking current checkout details. Both O’Reilly pages and Udemy blocked automated rechecking. Paid interiors, book runtimes and complete lesson coverage were not verified. Extra practice times are planning estimates.
