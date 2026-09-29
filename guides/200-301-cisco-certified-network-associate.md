---
exam_code: 200-301
vendor_id: cisco
official_blueprint: https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-29
---

# Cisco Certified Network Associate (200-301 CCNA) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 29, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#200-301-coverage-record). Cisco's [live exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html) and [v1.1 blueprint](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) are authoritative for exams through February 2, 2027.

**Current baseline:** 200-301 CCNA v1.1, six domains weighted 20/20/25/10/15/10; available through February 2, 2027<br>
**Scheduled change:** CCNA v2.0 launches February 3, 2027 with five reorganized 25/25/20/20/10 domains, more troubleshooting/configuration, OSPFv3, DNS records, secure file transfer, IPv6 RA Guard, agentic AI, prompting, and Ansible execution<br>
**Official source:** [current exam](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html) · [v1.1 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) · [v2.0 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf) · [transition date](https://blogs.cisco.com/learning/stay-on-track-get-certified-before-the-ccna-refresh)

## How to use this guide

For every feature, be able to move through requirement → packet/control-plane behavior → minimum configuration → verification output → likely fault → safe correction and rollback. Build a small repeatable Packet Tracer, CML, GNS3/EVE-NG, or authorized hardware lab; save topology, addressing plan, clean configuration, expected outputs, fault, diagnosis, repair, and post-change evidence.

**VERIFY CURRENT — logistics:** The dedicated exam page lists v1.1 as a 120-minute English/Japanese exam for USD 300. [Cisco’s central exam-pricing table](https://www.cisco.com/site/us/en/learn/training-certifications/exams/index.html) corroborates the price, although other parts of that page retain older exam labels. The separate [CCNA credential page](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html), checked September 29, 2026, instead says USD 400 and English only. Because Cisco has not reconciled those first-party pages, this guide retains the discrepancy and uses the narrower exam page for planning; verify price, language availability, tax, and regional delivery in the actual scheduling checkout before purchase. The credential page says the certification is valid for three years and describes current recertification routes. The [recertification policy](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/recertification/index.html) currently lists 30 CE credits for Associate renewal and requires completion during the active period; qualifying exams are also described. Check the applicable policy and credential record before renewal. Logistics and policy can change independently of the blueprint.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the current published objectives. A `Related item — scheduled v2.0:` callout specifically identifies February 3, 2027 scope and must not be confused with current v1.1 exam coverage.

**CURRENT BLUEPRINT:** Both actual PDFs were read in full. Four-page v1.1 has **53 numbered objectives**, including all supporting bullets, distributed 13/9/5/9/10/7. Three-page v2.0 has **29**, distributed 7/5/4/7/6. Separate maps are retained in the review evidence. Cisco’s [May 20 announcement](https://blogs.cisco.com/learning/ai-updates-ccna-ccie-automation) and July 1 article agree on the February 3, 2027 launch. The unchanged canonical exam-page monitor does not itself contain the complete PDF scope or transition notice.

**PRACTICAL DEPTH:** The original local workbook below passed 48 checks. Eight device/network labs remain proposed and unexecuted; no simulator, IOS/IOS XE device, authenticated API or wireless controller was exercised. Local calculations cannot establish device configuration competence.

## Objective map — current v1.1

| Domain | Weight | Proof to produce |
|---|---:|---|
| Network Fundamentals | 20% | Explain components/topologies/media/transports; configure IPv4/IPv6; diagnose interfaces/clients; reason about wireless, virtualization and switching |
| Network Access | 20% | Configure/verify VLANs, trunks, CDP/LLDP, LACP EtherChannel; interpret Rapid PVST+, Cisco wireless architecture and WLAN GUI settings |
| IP Connectivity | 25% | Interpret route selection; configure/verify IPv4/IPv6 static routes and single-area OSPFv2; explain FHRP |
| IP Services | 10% | Configure/verify NAT, NTP, DHCP client/relay and SSH; explain DNS, SNMP, syslog, QoS and file transfer |
| Security Fundamentals | 15% | Connect risk/program/access policy to passwords, VPNs, ACLs, Layer 2 and wireless controls |
| Automation and Programmability | 10% | Explain automation/controller/fabric/API/AI concepts and interpret JSON; distinguish Ansible/Terraform capabilities |

---

## 1. Network Fundamentals — 20%

### Components and architectures

Routers forward between IP networks; Layer 2 switches forward frames within VLANs; Layer 3 switches also route; firewalls/IPS enforce and inspect security policy; access points bridge wireless clients; controllers centralize policy/control; endpoints consume/provide services; servers host capability; PoE carries power and data over supported Ethernet cabling.

Two-tier campus commonly collapses core/distribution above access; three-tier separates access, distribution, and core; spine-leaf gives predictable east-west data-center paths; WAN connects sites; SOHO combines functions; cloud/on-premises changes ownership and connectivity constraints. Diagram data, control, management, power, trust, and failure domains—not just boxes.

Single-mode fiber usually serves longer distance; multimode serves shorter optical runs; copper is common at the edge. Match medium, standard, transceiver, wavelength, connector, polarity, distance, speed and environment. Interface errors, collisions, runts/giants, CRC, drops, duplex/speed mismatch, signal/distance and wrong cable point to different layers. Compare counters over time.

TCP provides connection-oriented ordered acknowledged byte delivery; UDP offers connectionless datagrams without built-in recovery/order. Bandwidth is capacity; throughput/goodput, latency, jitter and loss describe observed service.

### Addressing and endpoints

Subnetting must be fluent. Given an IPv4 address/prefix, find network, broadcast, usable range, host/subnet capacity and whether a destination is local. Know RFC 1918 private space and why NAT is not a security boundary. Configure and verify address/prefix/gateway on IOS interfaces and confirm Windows/macOS/Linux parameters. For an ordinary subnet, `192.0.2.130/26` belongs to `192.0.2.128/26`: broadcast `.191`, host range `.129–.190`, 62 conventional hosts. Allocate VLSM prefixes on aligned boundaries without overlap; a summarizing route does not allocate addresses or create reachability.

On Windows inspect `ipconfig /all` and `route print`; on Linux inspect `ip address` and `ip route`; on macOS inspect `ifconfig` and `netstat -rn`. Compare address, prefix, interface state, gateway and resolver with the intended VLAN. Test each IP family separately; a working IPv4 connection does not verify IPv6.

For IPv6, recognize global unicast, unique local, link-local, multicast and anycast behavior; IPv6 has no broadcast. Configure/verify address and prefix, link-local behavior, and default route. Modified EUI-64 forms an interface identifier from a MAC-derived value; privacy/stable address methods also exist. [RFC 4291](https://www.rfc-editor.org/rfc/rfc4291.html) describes the address types and interface identifier construction. Modified EUI-64 inserts `ff:fe` between MAC halves and flips the universal/local bit: `00:11:22:33:44:55` yields `0211:22ff:fe33:4455`. This does not mean every current host uses it. Anycast assigns an address to multiple interfaces and routing chooses a reachable instance; it does not deliver to every instance. A link-local next hop needs an interface/zone context.

Wireless design includes band, RF, nonoverlapping channels, SSID, interference, power, roaming, encryption and shared-medium capacity. A strong signal does not prove low interference or valid authentication.

Virtual machines share a hypervisor; containers share an OS kernel while isolating processes/resources; VRFs create separate routing tables on one device. These solve different isolation/operation problems.

### Switching behavior

A switch learns source MAC/port/VLAN and ages entries. Known unicast follows the table; unknown unicast and broadcast flood within the VLAN; multicast behavior depends on features. The receiving host accepts frames addressed to it/broadcast/relevant multicast. A router rebuilds the Layer 2 frame at every hop while IP source/destination usually persist unless translated.

**Related item — scheduled v2.0:** Current “describe/identify” fundamentals become explicit interface/cable, IPv4/IPv6, wired/wireless client and DHCP troubleshooting. Practice evidence-led diagnosis now.

---

## 2. Network Access — 20%

### VLANs and trunks

An access port normally carries one data VLAN untagged; a voice VLAN supports phone/data edge behavior. A trunk carries multiple VLANs using 802.1Q tags; the native VLAN is normally untagged and must match deliberately across the link. The default VLAN and native VLAN are concepts that may coincide but are not synonyms.

Inter-VLAN traffic requires Layer 3 forwarding through router-on-a-stick or switch virtual interfaces/routed interfaces. Build an addressing/VLAN/trunk plan, then verify with `show vlan brief`, `show interfaces trunk`, interface status/configuration, MAC table, ARP and route outputs. Missing VLAN, wrong access assignment, disallowed VLAN, native mismatch, shutdown interface or absent gateway create distinct evidence.

CDP is Cisco-proprietary discovery; LLDP is standards-based. Both can reveal neighbor identity, local/remote port and capability, helping validate documentation. Discovery is not authentication and can expose topology, so enable deliberately.

### EtherChannel

EtherChannel bundles compatible links into one logical port-channel. LACP is the v1.1 named negotiation method; active initiates and passive responds, while two passive sides do not form. Member parameters must agree (speed/duplex, Layer 2 or Layer 3 mode, access/trunk and VLAN settings where applicable, addressing, and other platform requirements). Spanning Tree treats a functioning Layer 2 bundle logically, while the hashing algorithm distributes flows rather than splitting every packet equally.

For a Layer 2 bundle, configure switchport/trunk intent on the port-channel and compatible members. For a routed Layer 3 bundle, remove switchport behavior on the members and logical interface as the platform requires, assign the IP network to the port-channel rather than individual members, and route through that logical link. The current [Cisco EtherChannel configuration guide](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/etherchannel/etherchannel-configuration-guide/etherchannels.html) is platform-specific implementation evidence; verify the IOS/IOS XE image and syntax in your lab.

Verify summary, LACP neighbor, port-channel protocol, member flags/state, switchport or routed-interface state, trunk/VLAN or IP/route behavior, load distribution, and counters. Shut one authorized member, observe the result and restore it. The configured `min-links` threshold can take the whole bundle down when too few members remain; verify it before predicting continued service. A single flow need not consume the sum of member capacities. A suspended/member mismatch is not solved by blindly forcing mode; correct the configuration contract.

### Rapid PVST+

Spanning Tree prevents Layer 2 loops by electing a root bridge, selecting root/designated/alternate roles, and placing ports into discarding, learning or forwarding states in the [RSTP model](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html). [Cisco’s Rapid PVST+ state explanation](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/92x/Layer-2_switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-92x/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-92x_chapter_01001.html) uses platform labels including blocking and disabled; map those to the generic RSTP model and do not copy NX-OS commands into IOS. Learning can populate the MAC table without ordinary data forwarding; a role describes topology responsibility, while a state describes present activity. Lower bridge ID wins root election. Each non-root switch chooses its best root port; each segment gets a designated port. Rapid PVST+ runs per VLAN. Interpret root ID, bridge ID, path cost and port roles together using the selected platform’s [STP guide](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/stp/stp-configuration-guide/m-stp.html); an alternate role can be healthy. Compare the same VLAN on both ends.

PortFast accelerates a trusted edge port and does not disable STP. BPDU Guard protects edge assumptions by disabling an edge port receiving BPDUs. Root Guard prevents a port from becoming a root path; Loop Guard protects against certain missing-BPDU conditions; BPDU Filter can suppress BPDUs and is dangerous if it creates an unmanaged loop. Know mechanism and placement.

### Wireless architecture

Autonomous versus controller-based APs differ in management/control. Lightweight APs may form control/data tunnels to a WLC; local/flex modes alter forwarding/operation. Understand AP/WLC physical connections, access/trunk ports and link aggregation. Given a WLAN GUI, interpret SSID/profile, VLAN/interface mapping, security/authentication, QoS and advanced settings. Separate association, authentication, addressing, name resolution and application problems.

Management access includes console, SSH, Telnet, HTTP/HTTPS, TACACS+/RADIUS-backed AAA, and cloud-managed interfaces. Prefer encrypted, authenticated, least-privilege paths with logging and an emergency recovery plan.

**Related item — scheduled v2.0:** Edge-host and infrastructure port configuration becomes more explicit, discovery validates documentation, show/log/ping/extended-ping/traceroute/packet-capture troubleshooting is central, and Rapid PVST+ shifts from interpretation toward configuration. BPDU Filter drops from the named v2.0 guard list.

---

## 3. IP Connectivity — 25%

### Route interpretation and selection

A route contains source/protocol code, prefix/mask, next hop or exit interface, administrative distance, metric and age. Separate two stages. Each routing process selects candidates using its own metric; the routing table compares usable candidates for the **same prefix**, normally preferring lower AD across sources. Packet forwarding subsequently uses **longest-prefix match among installed routes**. AD and metric are not recalculated for each packet and do not override a more-specific installed prefix. A default route (`0.0.0.0/0` or `::/0`) is least specific and supplies a gateway of last resort. Cisco’s [route-selection explanation](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) distinguishes these stages.

A static `10.0.0.0/8` with AD 1 does not displace an installed OSPF `10.20.30.0/24` with AD 110 for destination `10.20.30.10`. For that same `/24`, a floating static with AD 200 waits for preferred candidates to disappear. An installed `/32` still wins for its host. Metrics from unrelated protocols do not have common units. Equal-cost paths may coexist; the platform determines how traffic uses them.

Connected/local routes appear when interfaces are correctly addressed/up. A missing route may actually originate from a down interface, failed adjacency, filtering, wrong prefix, recursion or administrative distance. `show ip route`, `show ipv6 route`, interface/ARP/neighbor, protocol and ping/traceroute evidence must agree.

### Static routes

Configure/verify IPv4 and IPv6 default, network, host and floating static routes. A floating route uses a higher administrative distance than the preferred route. Fully specified next hop plus interface can help on multiaccess networks; platform/address-family syntax varies. Validate installation and actual forwarding/return path, then test primary failure and recovery.

Avoid recursive/next-hop errors, pointing to a local interface when a next hop is needed, wrong mask, absent reverse route, and a backup route that never becomes active. A successful ping to the next hop does not prove the full destination path. An application outage does not automatically withdraw a static route; a floating route responds to route eligibility/installation. Upstream failure can remain undetected without appropriate tracking or routing evidence. AD 255 is not an installable backup.

### Single-area OSPFv2

OSPF is a link-state IGP. For v1.1, configure/verify single-area OSPFv2, neighbor adjacency, point-to-point and broadcast networks, DR/BDR election, and router ID. Neighbors need compatible area, network type, timers, authentication if used, and usable IP/subnet conditions; unique router IDs matter. Broadcast networks elect DR/BDR; point-to-point does not need that election.

Use `show ip ospf neighbor`, `show ip ospf interface`, `show ip protocols`, database and route outputs. Diagnose from state: no neighbor differs from 2-WAY on a broadcast segment, which differs from EXSTART/EXCHANGE. Confirm whether a route is advertised, learned, preferred and forwardable. Cisco’s [neighbor-state explanation](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) shows that broadcast DROTHER peers can normally remain 2-WAY, with full adjacencies to DR/BDR. INIT means one-way recognition; persistent EXSTART/EXCHANGE suggests database-description exchange problems. [Cisco’s MTU example](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html) demonstrates one possible cause. Verify actual MTUs and exchange evidence; `mtu-ignore` is not a general repair and MTU is not the only possible cause.

### First-hop redundancy

FHRPs provide a resilient virtual default gateway across routers. One device forwards as active/master while another can assume the shared virtual IP/MAC. Priority, preemption, tracking, timers and failure modes affect operation. v1.1 asks purpose/functions/concepts rather than named configuration.

**Related item — scheduled v2.0:** The routing share becomes 20%, but OSPFv3 for IPv6 is explicitly configured alongside OSPFv2. HSRP and VRRP operational status are named. For an attempt on or after February 3, 2027, add an IPv6 OSPF lab. The v2.0 adjacency objective explicitly excludes authentication; adjacent advice does not create a new authentication configuration objective.

---

## 4. IP Services — 10%

### NAT, time, address and name services

Inside-source NAT translates inside-local addresses to inside-global representations. Static NAT gives a fixed mapping; a pool supplies dynamic mappings; PAT/overload distinguishes flows with ports. Define inside/outside interfaces, match intended sources, select mapping/pool and verify translations/statistics plus actual end-to-end traffic. NAT does not create DNS, routes, firewall policy or return connectivity automatically.

NTP synchronizes clocks. Configure/verify client/server behavior, source/reachability, association/stratum and synchronized state; good time is essential to logs, certificates and troubleshooting.

DHCP uses a lease exchange to provide address, mask, gateway, DNS and other options. A relay forwards client broadcasts toward a server across routing boundaries. Configure/verify IOS DHCP client/relay, then inspect lease/client, interface, server and path evidence. DNS translates names; distinguish resolver reachability, query result, cache, record, authoritative service and application behavior.

### Management and observability

SNMP managers query agents and receive notifications; versions differ in security. Syslog severity ranges from 0 emergencies through 7 debugging, and facilities categorize sources. Logging needs synchronized time, suitable level/destination, access protection, retention and tested alert ownership.

QoS per-hop behavior classifies and marks traffic, queues under contention, manages congestion, and uses policing or shaping. Policing enforces a rate and may drop/remark; shaping buffers to smooth output. QoS prioritizes constrained resources—it does not manufacture bandwidth.

Configure secure remote access with hostname/domain context, local or centralized identity, RSA keys/platform equivalent, SSH version/line restrictions and least privilege; verify from an approved client. TFTP is simple/unauthenticated; FTP provides credentials but no inherent protection; secure transfer is preferable where supported.

**Related item — scheduled v2.0:** Services and security merge. NAT/PAT, local/central AAA, SFTP/SCP, detailed DNS record diagnosis, ACLs and Layer 2 controls become the core. DHCP **moves to domain 1 as troubleshooting of client, server and relay on IOS devices**. SNMP and syslog move to domain 5. NTP, QoS and TFTP/FTP are absent from the explicit v2.0 list but remain useful supporting knowledge; absence does not guarantee that related context cannot appear.

---

## 5. Security Fundamentals — 15%

Threats can exploit vulnerabilities; mitigations reduce likelihood/impact. Security programs combine awareness, training, physical access, identity, configuration, monitoring, response, recovery and governance. Authentication proves identity, authorization permits action and accounting records it.

Awareness explains why a risk matters and how to recognize/report it; role-based training builds the skill to respond correctly; exercises test whether behavior and escalation work. Physical controls deter, prevent, detect and recover from unauthorized access through locks/badges, visitor handling, guards/cameras/alarms, protected rooms/racks and environmental safeguards. Social engineering can cross digital and physical boundaries through phishing, pretexting, baiting or tailgating; the [Cisco overview](https://www.cisco.com/site/us/en/learn/topics/security/what-is-social-engineering.html) supplies current first-party context. Validate completion and reporting quality, access-list/visitor review, denied and revoked access, alert ownership, incident response and safe exception handling—not attendance alone.

Use `enable secret`/strong stored alternatives, unique local users where appropriate, secure console/VTY policy, session limits, least privilege, MFA/certificates/biometrics through supporting systems, and centralized TACACS+/RADIUS when required. Password policy includes length, uniqueness, storage, lifecycle, recovery and attack protection—not arbitrary complexity alone.

IPsec can protect site-to-site or remote-access traffic; distinguish protected tunnel, peer/authentication, policy and routed reachability. Encryption does not validate endpoint health.

ACLs are ordered first-match rules with an implicit deny. Standard IPv4 ACLs match source; extended ACLs can match source/destination/protocol/ports. Numbered/named defines management syntax, not capability alone. Plan intent, place deliberately, account for required return/control traffic, apply correct direction/interface, inspect hit counts and test permitted and denied cases. Preserve recovery access. In an IPv4 wildcard, a zero bit must match and a one bit is ignored; unlike subnet masks, wildcards may be noncontiguous. A client permit to TCP destination 443 does not also permit the reversed reply through an independently applied ACL. Ordinary extended ACLs do not maintain connection state: TCP `established` checks ACK/RST flags and can match without an earlier observed connection. See the [ACL overview](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_data_acl/configuration/15-mt/sec-data-acl-15-mt-book/sec-access-list-ov.html) and [creation guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_data_acl/configuration/15-sy/sec-data-acl-15-sy-book/sec-create-ip-apply.html); syntax/features depend on the platform.

DHCP snooping establishes trusted server-facing behavior and a binding database; Dynamic ARP Inspection can validate ARP against trusted bindings; port security limits learned/allowed MAC behavior. These controls depend on correct trust boundaries. [Catalyst 9300 DAI documentation](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-18/configuration_guide/sec/b_1718_sec_9300_cg/configuring_dynamic_arp_inspection.html) distinguishes learned DHCP bindings from configured ARP ACLs for static hosts. Trusted DAI interfaces bypass validation; do not repair a missing binding by trusting every host port. Test legitimate static hosts and invalid bindings separately. Wireless options include WPA/WPA2/WPA3; v1.1 asks configuration of a WPA2-PSK WLAN in the GUI. Use strong PSK, AES, protected administration and segmentation.

**Related item — scheduled v2.0:** Storm control and IPv6 RA Guard join DHCP snooping, DAI and port security. Practice protecting IPv6 neighbor/router discovery without blocking legitimate control traffic.

---

## 6. Automation and Programmability — 10%

Automation improves repeatability, scale, auditability and feedback but can also multiply an error. Use source-controlled intent, validation, scoped credentials, idempotent/retry-aware behavior, staged deployment, telemetry and rollback.

Traditional device-by-device management distributes control. Controller-based/software-defined architecture separates control and data concerns, uses an underlay for transport and an overlay/fabric for logical connectivity/policy. Southbound interfaces connect controllers to infrastructure; northbound APIs expose intent/data to applications. Actual architectures may not fit a simplistic one-controller diagram.

REST APIs use resources/URIs, HTTP methods (GET/read, POST/create/action, PUT replace, PATCH modify, DELETE), status codes, headers, authentication and serialized data. CRUD maps conceptually to create/read/update/delete. JSON contains objects `{}`, arrays `[]`, key/value pairs, strings, numbers, booleans and null; indentation is presentation, while brackets/quotes/commas/colons define structure.

Authentication is API-specific. HTTP Basic sends an encoded username/secret on requests and therefore requires protected TLS transport and tightly managed credentials; Base64 is not encryption. A Bearer token authorizes whoever possesses it, so scope, audience, expiry, storage, revocation and log redaction matter. API keys are provider-defined identifiers/secrets, and OAuth 2.0 is a framework for obtaining scoped access tokens through an appropriate grant rather than a synonym for the Bearer header. Cisco's [Secure Endpoint API overview](https://developer.cisco.com/docs/secure-endpoint/overview/) is one representative Basic-versus-Bearer example, not proof that every Cisco API supports those same methods. Read the selected API contract, use least privilege, verify TLS, and never place secrets in source code or URLs. This API also documents 400 for invalid requests, 401 for authentication failure, 429 for rate limits and paginated JSON results. One successful page does not establish complete inventory. Preserve pagination, bounded retries and redacted error evidence; generated configurations are not observed device responses.

Ansible commonly executes procedural/declarative automation using inventories, modules and playbooks; Terraform declares desired infrastructure and tracks state. Recognize capabilities and safe workflows rather than treating either as a universal device manager. API credentials belong in approved secret storage, not source files.

Generative AI can summarize or propose configurations; predictive ML can detect patterns/anomalies or forecast capacity. Both require trustworthy context, data handling, human verification, testing, provenance and controlled execution. Never paste secrets/configurations into an unapproved model or accept plausible output as device evidence.

**Related item — scheduled v2.0:** Agentic AI and digital network-assistant recommendations become explicit. Candidates must choose prompts using data classification, output format, persona and instructions; compare device/cloud/controller/automation/IaC management; use Ansible to execute commands; and interpret syslog. Require exact sanitized inputs, constrained output, cited evidence, validation commands and human approval.

---

## Scheduled v2.0 transition map

Do not mix versions on an exam booking. Until February 2, study v1.1 as primary. For an exam February 3, 2027 or later, use the official v2.0 PDF as authority.

| v2.0 domain | Weight | Most important change from v1.1 |
|---|---:|---|
| Network Infrastructure and Connectivity | 25% | Troubleshoot interfaces/cabling, IPv4/IPv6 clients, wireless and DHCP; virtualization remains, but evidence/action verbs deepen |
| Switching and Network Access | 25% | Configure edge/infrastructure attributes; validate docs with CDP/LLDP; troubleshoot with show/log/ping/capture; configure Rapid PVST+ |
| IP Routing | 20% | Troubleshoot static routing; add OSPFv3; interpret HSRP and VRRP status |
| Network Services and Security | 20% | Add central AAA client, SFTP/SCP, DNS records, storm control and RA Guard; consolidate NAT/VPN/ACL/Layer 2 security |
| AI, Network Operations and Management | 10% | Add agentic AI, prompt selection and Ansible execution; compare management approaches; retain SNMP and interpret syslog |

The future map also names A/AAAA/CNAME/MX/NS/PTR diagnosis, IPsec protocol/transport-mode concepts, IPv4 standard/extended/numbered/named ACLs, edge connectivity for phones/APs/virtual hosts/appliances, and show/log/ping/extended-ping/traceroute/capture interpretation. VRFs, Terraform and BPDU Filter are not explicitly named. Keep v1.1 study intact before transition and maintain a separate future checklist. A publisher update program does not establish coverage of all 29 future objectives.

---

## Integrated scenarios

### Scenario 1: New branch cannot reach headquarters

Start with topology/addressing and interface state. Verify VLAN/trunk, client gateway, ARP, connected routes, static/OSPF adjacency and route selection at each hop, then ACL/NAT/VPN/service and return route. Compare expected and actual tables. Fix one root cause, validate permitted and denied traffic, record rollback and update documentation.

### Scenario 2: One floor has intermittent voice and Wi-Fi

Correlate time, clients, AP/channel/RF, switch interface errors/drops, PoE, VLAN/voice VLAN, trunk, STP/EtherChannel and QoS evidence. Separate association/authentication/addressing from application quality. Do not raise transmit power or reboot before establishing the failure layer. Stage and validate a reversible correction under comparable load.

### Scenario 3: Automating a standard access switch

Define approved intent and inventory, render a candidate, lint/validate offline, protect credentials, collect pre-state, deploy to one lab/canary, run positive and negative tests, compare post-state, and roll back on failed gates. Use REST/JSON or Ansible only where the device contract supports it. AI may help explain sanitized output, but device evidence and human approval decide.

---

## Hands-on evidence labs

**Proposed, not executed in this review.** Use an isolated authorized topology and documentation for its exact platform/image. Retain topology/addressing, baseline, changed configuration, commands/output, expected/observed result, failure explanation and restored state. Record unsupported simulator features as limitations.

1. **Addressing and clients:** Build two routed client VLANs with dual-stack hosts. Allocate nonoverlapping prefixes and verify the worked `/26`. Introduce a wrong mask or gateway, predict which direction fails, inspect client settings, test both families and restore both forward and return paths.
2. **VLANs and discovery:** Configure data/voice access ports, an 802.1Q trunk with explicit native/allowed lists, and inter-VLAN routing. Capture `show vlan brief`, `show interfaces trunk`, CDP/LLDP, MAC and ARP evidence. Remove one intended VLAN from the trunk, identify the break, restore and compare same-VLAN versus routed traffic.
3. **LACP and STP:** Build separate Layer 2 and routed Layer 3 bundles, with routed addresses on the logical interface. Compare a member failure against minimum-links requirements; inspect summary/member/neighbor and route state. In a separate loop-safe STP topology interpret per-VLAN root, roles and states; test an approved edge BPDU-Guard case, then restore. Document substitutions for unsupported routed port-channels.
4. **Routing and OSPF:** Combine same-prefix OSPF/floating-static candidates with a covering static and a host route. Predict installed routes and forwarding separately. Withdraw/restore a primary route and compare traffic. Distinguish healthy broadcast DROTHER 2-WAY from an intentional MTU exchange failure. A separately labeled v2.0 variant adds OSPFv3 and HSRP/VRRP status evidence.
5. **Services:** Add NAT, DHCP relay/client, DNS, NTP and SSH. State the expected translation, lease, query, time association or authenticated session. Break one dependency, compare control-plane and application evidence, then restore. An existing translation or lease alone does not prove service. The v2.0 variant adds DNS record diagnosis and secure file transfer with an integrity comparison.
6. **Access and Layer 2 protection:** Use a permitted client, denied client and static host. Review an ACL before applying it; test order, both traffic directions and recovery access. Compare legitimate and invalid ARP against DHCP snooping/DAI bindings. Test port-security violations, local identity and a WPA2-PSK WLAN. For v2.0 separately add supported storm-control, RA-Guard and AAA-client cases.
7. **Automation:** In an authorized sandbox, inspect a read-only authenticated JSON response, pagination and an invalid request with secrets redacted. Compare Ansible tasks with Terraform desired state and identify an unintended proposed change. For v2.0 execute a documented harmless Ansible show command and verify against device evidence. This review executed only the synthetic local workbook below.
8. **Integrated fault and recovery:** Choose an undisclosed VLAN, route, resolver, ACL or service fault. Require a prediction, smallest discriminating observation, repair, positive/negative retest and baseline restoration. A v2.0 AI variant uses sanitized output in an approved assistant; reject invented interfaces/commands and verify recommendations before changing anything.

## Executed local routing and ACL workbook

**PRACTICAL DEPTH — 48 checks passed.** Save the exact standard-library Python program below and run it locally. It uses no sockets, credentials, device sessions or provider labs. Its synthetic RIB has six prefixes: two equal-cost OSPF candidates win for the `/24`, then a floating static after their supplied eligibility flags change. A more-specific host route still wins. ACL cases demonstrate shadowing, noncontiguous wildcards, a separately denied reply and ACK/RST matching without connection tracking.

The routing model supports one process and comparable metric class per source. It rejects mixed AD within that process and equal AD across sources instead of inventing universal tie behavior. It does not implement OSPF SPF/route types, recursive next-hop resolution, tracking, convergence, policy routing, hardware forwarding or ECMP hashing. `usable` is supplied evidence, not measured reachability. ACLs inspect selected parsed IPv4 fields; they do not parse IOS syntax or packets, reassemble fragments, model NAT/interface direction, authenticate traffic or track sessions. Rules are trusted fixtures; this is not a complete configuration validator.

```python
"""Original synthetic routing and IPv4 ACL workbook; no device or network I/O."""
import ipaddress as ip
import json
from dataclasses import dataclass, replace

checks = 0

def check(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1

def rejects(fn):
    global checks
    try:
        fn()
    except ValueError:
        checks += 1
    else:
        raise AssertionError('Expected a rejected fixture')

@dataclass(frozen=True)
class Route:
    name: str
    prefix: str
    source: str
    ad: int
    metric: int
    usable: bool = True


def install(candidates):
    # One routing process per source, one comparable metric class per process.
    # usable is supplied evidence, not a next-hop probe or recursive resolver.
    if len({r.name for r in candidates}) != len(candidates):
        raise ValueError('Duplicate route identity')
    by_prefix = {}
    for r in candidates:
        net = ip.ip_network(r.prefix)
        if not (0 <= r.ad <= 255) or r.metric < 0:
            raise ValueError('Invalid route preference')
        if r.usable and r.ad != 255:
            by_prefix.setdefault(net, []).append(r)
    rib = {}
    for net, rows in by_prefix.items():
        best_by_source = []
        for source in {r.source for r in rows}:
            same_source = [r for r in rows if r.source == source]
            if len({r.ad for r in same_source}) != 1:
                raise ValueError('Outside model: mixed AD in one process')
            best_metric = min(r.metric for r in same_source)
            best_by_source += [r for r in same_source if r.metric == best_metric]
        best_ad = min(r.ad for r in best_by_source)
        selected = [r for r in best_by_source if r.ad == best_ad]
        if len({r.source for r in selected}) != 1:
            raise ValueError('Outside model: cross-source AD tie')
        rib[net] = tuple(sorted(r.name for r in selected))
    return rib


def forward(rib, destination):
    address = ip.ip_address(destination)
    matches = [n for n in rib if n.version == address.version and address in n]
    return rib[max(matches, key=lambda n: n.prefixlen)] if matches else ()


def wildcard_match(address, pattern, wildcard):
    a, p, w = (int(ip.IPv4Address(v)) for v in (address, pattern, wildcard))
    care = (~w) & 0xffffffff
    return (a & care) == (p & care)


@dataclass(frozen=True)
class Rule:
    name: str
    action: str
    source: str = '0.0.0.0'
    source_wild: str = '255.255.255.255'
    destination: str = '0.0.0.0'
    destination_wild: str = '255.255.255.255'
    protocol: str = 'ip'
    destination_port: int | None = None
    established: bool = False


def acl(rules, packet):
    # Synthetic parsed fields, no fragments, NAT, connection table or IOS parser.
    ip.IPv4Address(packet['source'])
    ip.IPv4Address(packet['destination'])
    for r in rules:
        if r.action not in {'permit', 'deny'} or r.protocol not in {'ip', 'tcp', 'udp', 'icmp'}:
            raise ValueError('Invalid rule')
        if r.destination_port is not None and (
            r.protocol not in {'tcp', 'udp'} or not 0 <= r.destination_port <= 65535
        ):
            raise ValueError('Invalid port condition')
        if r.established and r.protocol != 'tcp':
            raise ValueError('established is a TCP flag condition')
        if r.protocol != 'ip' and r.protocol != packet['protocol']:
            continue
        if not wildcard_match(packet['source'], r.source, r.source_wild):
            continue
        if not wildcard_match(packet['destination'], r.destination, r.destination_wild):
            continue
        if r.destination_port is not None and packet.get('destination_port') != r.destination_port:
            continue
        if r.established and not (packet.get('tcp_flags', 0) & (0x10 | 0x04)):
            continue
        return r.action, r.name
    return 'deny', 'implicit'

routes = [
    Route('default', '0.0.0.0/0', 'static', 1, 0),
    Route('broad', '10.0.0.0/8', 'static', 1, 0),
    Route('ospf-a', '10.20.30.0/24', 'ospf', 110, 20),
    Route('ospf-b', '10.20.30.0/24', 'ospf', 110, 20),
    Route('ospf-slower', '10.20.30.0/24', 'ospf', 110, 30),
    Route('floating', '10.20.30.0/24', 'static', 200, 0),
    Route('host', '10.20.30.99/32', 'static', 240, 0),
    Route('unresolved', '10.20.30.50/32', 'static', 1, 0, False),
    Route('v6-default', '::/0', 'static', 1, 0),
    Route('v6-specific', '2001:db8:10::/64', 'ospf', 110, 30),
]
rib = install(routes)
check(forward(rib, '10.20.30.10'), ('ospf-a', 'ospf-b'))
check(forward(rib, '10.20.30.99'), ('host',))
check(forward(rib, '10.20.30.50'), ('ospf-a', 'ospf-b'))
check(forward(rib, '10.21.1.1'), ('broad',))
check(forward(rib, '198.51.100.8'), ('default',))
check(forward(rib, '2001:db8:10::9'), ('v6-specific',))
check(forward(rib, '2001:db8:20::9'), ('v6-default',))
check(forward(install(routes[:8]), '2001:db8::1'), ())
check(forward(install(routes[1:8]), '198.51.100.8'), ())
check(install(list(reversed(routes))), rib)
withdrawn = [replace(r, usable=False) if r.source == 'ospf' else r for r in routes]
check(forward(install(withdrawn), '10.20.30.10'), ('floating',))
check(forward(install(withdrawn), '10.20.30.99'), ('host',))
no_backup = [replace(r, usable=False) if r.name == 'floating' else r for r in withdrawn]
check(forward(install(no_backup), '10.20.30.10'), ('broad',))
check(forward(install(routes), '10.20.30.10'), ('ospf-a', 'ospf-b'))
one_path = [replace(r, usable=False) if r.name == 'ospf-a' else r for r in routes]
check(forward(install(one_path), '10.20.30.10'), ('ospf-b',))
# Give static alternatives their own preference test: avoid mixed AD in one process.
pair = [Route('static', '192.0.2.0/24', 'static', 1, 999),
        Route('ospf', '192.0.2.0/24', 'ospf', 110, 1)]
check(forward(install(pair), '192.0.2.5'), ('static',))
check(forward(install([replace(r, ad=255) if r.source == 'static' else r for r in pair]),
              '192.0.2.5'), ('ospf',))
check(forward(install([replace(pair[0], ad=255)]), '192.0.2.5'), ())
rejects(lambda: install([Route('bad', '192.0.2.1/24', 'static', 1, 0)]))
rejects(lambda: install([replace(pair[0], ad=256)]))
rejects(lambda: install([replace(pair[0], metric=-1)]))
rejects(lambda: install([pair[0], pair[0]]))
rejects(lambda: install([replace(pair[0], ad=110), pair[1]]))
rejects(lambda: install([pair[0], replace(pair[0], name='other', ad=10)]))

check(wildcard_match('192.0.2.12', '192.0.2.0', '0.0.0.255'), True)
check(wildcard_match('192.0.3.12', '192.0.2.0', '0.0.0.255'), False)
check(wildcard_match('192.0.2.10', '192.0.2.10', '0.0.0.0'), True)
check(wildcard_match('192.0.2.11', '192.0.2.10', '0.0.0.0'), False)
check(wildcard_match('203.0.113.9', '0.0.0.0', '255.255.255.255'), True)
# Noncontiguous wildcard: ignore only the low bit of octet 3, plus octet 4.
check(wildcard_match('10.20.3.80', '10.20.2.0', '0.0.1.255'), True)
check(wildcard_match('10.20.4.80', '10.20.2.0', '0.0.1.255'), False)

web = Rule('web', 'permit', '192.0.2.0', '0.0.0.255',
           '198.51.100.10', '0.0.0.0', 'tcp', 443)
blocked = Rule('blocked-host', 'deny', '192.0.2.66', '0.0.0.0')
policy = [blocked, web]
packet = dict(source='192.0.2.10', destination='198.51.100.10',
              protocol='tcp', source_port=53000, destination_port=443, tcp_flags=0x02)
check(acl(policy, packet), ('permit', 'web'))
check(acl(policy, dict(packet, source='192.0.2.66')), ('deny', 'blocked-host'))
check(acl(list(reversed(policy)), dict(packet, source='192.0.2.66')), ('permit', 'web'))
check(acl(policy, dict(packet, destination_port=80)), ('deny', 'implicit'))
check(acl(policy, dict(packet, destination='198.51.100.11')), ('deny', 'implicit'))
check(acl(policy, dict(packet, protocol='udp')), ('deny', 'implicit'))
reply = dict(packet, source=packet['destination'], destination=packet['source'],
             source_port=443, destination_port=53000, tcp_flags=0x12)
check(acl(policy, reply), ('deny', 'implicit'))
flags_only = [Rule('ack-or-rst', 'permit', protocol='tcp', established=True)]
check(acl(flags_only, packet), ('deny', 'implicit'))
check(acl(flags_only, reply), ('permit', 'ack-or-rst'))
check(acl(flags_only, dict(packet, tcp_flags=0x10)), ('permit', 'ack-or-rst'))
check(acl(flags_only, dict(packet, tcp_flags=0x04)), ('permit', 'ack-or-rst'))
check(acl(flags_only, dict(packet, protocol='udp', tcp_flags=0x10)), ('deny', 'implicit'))
rejects(lambda: acl([replace(web, destination_port=70000)], packet))
rejects(lambda: acl([replace(web, protocol='ip')], packet))
rejects(lambda: acl([replace(web, protocol='udp', established=True)], packet))
rejects(lambda: acl(policy, dict(packet, source='2001:db8::1')))
check(acl(policy, json.loads(json.dumps(packet))), ('permit', 'web'))
print(json.dumps(dict(installed_prefixes=len(rib), selected=forward(rib, '10.20.30.10'),
                      backup=forward(install(withdrawn), '10.20.30.10'),
                      denied=acl(policy, dict(packet, source='192.0.2.66')))))
print(f'{checks} local checks passed')
```

Expected summary: six installed prefixes; selected `ospf-a` and `ospf-b`; backup `floating`; blocked client denied by `blocked-host`; `48 local checks passed`. Counts include input-rejection and structural assertions. The result does not demonstrate live routing, failover or enforcement.

## Readiness checks

These are original teaching prompts, not recalled exam items. Explain the answer and then produce lab evidence where applicable.

1. **How do two-tier, three-tier and spine-leaf differ?** Two-tier combines core/distribution above access; three-tier separates them; leaf/spine gives a regular east-west fabric. Draw failure and oversubscription boundaries before judging suitability.
2. **How do network components divide work?** Switches ordinarily forward by VLAN/MAC, routers by destination prefix, and firewalls/IPS additionally inspect/enforce policy. Controllers manage/control, endpoints use/provide services and PoE powers supported devices.
3. **Does increasing CRC prove duplex mismatch?** No. Compare counter deltas, speed/duplex, medium/transceiver compatibility and peer evidence. CRC, drops, collisions and signal problems suggest different candidates.
4. **What is the worked `192.0.2.130/26` range?** Network `.128`, broadcast `.191`, conventional hosts `.129–.190`, 62 hosts. Allocate VLSM on block boundaries without overlap.
5. **Can working IPv4 prove IPv6 works?** No. Each family needs its own address, route, neighbor and policy evidence. IPv6 link-local presence does not establish global reachability.
6. **How do IPv6 address types differ?** Unicast targets an interface, multicast a subscribed group, and anycast a routed instance sharing an address. Link-local has link scope; unique-local does not promise Internet routing; IPv6 has no broadcast.
7. **What does modified EUI-64 do?** Insert `ff:fe` between MAC halves and invert the U/L bit. The worked MAC yields `0211:22ff:fe33:4455`; other host address-generation methods exist.
8. **Which client facts precede a DNS diagnosis?** Interface state, address/prefix, gateway/route and resolver. Compare permitted IP connectivity with name lookup before changing the resolver.
9. **Why can strong Wi-Fi signal coexist with poor service?** Interference, contention, authentication, DHCP or application paths can fail. Correlate RF and wired evidence and select channels for the actual band, width and local rules.
10. **Are VMs, containers and VRFs interchangeable?** No. Hypervisors host VMs, containers share a kernel with workload isolation, and VRFs separate routing tables. Their resource and trust boundaries differ.
11. **What does a switch learn?** Source MAC, ingress port and VLAN. Known unicast follows the table; unknown destinations can flood within the VLAN, subject to forwarding state and controls.
12. **Are default and native VLAN synonyms?** No. Native describes trunk tagging behavior; default describes initial/default VLAN use. Data, voice and allowed lists must match the design.
13. **What enables inter-VLAN traffic?** Layer 3 forwarding, an appropriate gateway/path, policy and a return path. A trunk transports VLANs without itself routing between them.
14. **What does CDP/LLDP prove?** A discovery observation useful for checking neighbors, ports and capabilities. It is not peer authentication or an end-to-end path test.
15. **Will two passive LACP ports form a bundle?** No; neither initiates. Active/active or active/passive can negotiate when other parameters agree. LACP does not repair VLAN or Layer 2/3 mismatches.
16. **Where does routed EtherChannel addressing belong?** On the logical port-channel, with compatible routed members and no conflicting member addresses. Verify platform support.
17. **Does one member failure always preserve service?** No. Remaining eligible members must satisfy minimum-links and other requirements. Aggregate capacity also differs from one flow’s throughput.
18. **How do STP role and state differ?** Root/designated/alternate/backup describe topology responsibilities; discarding/learning/forwarding describe activity. A healthy alternate path can withhold data forwarding.
19. **What do the named guard/filter features do?** BPDU Guard enforces edge assumptions; Root Guard prevents an unwanted root path; Loop Guard handles certain missing-BPDU conditions; BPDU Filter suppresses BPDUs and can expose loops. PortFast accelerates an edge transition without disabling STP.
20. **Which wireless stage failed?** Separate association, authentication, addressing, name lookup and application flow. Interpret SSID/VLAN/security/QoS with the AP/WLC forwarding mode.
21. **Why prefer SSH/HTTPS for management?** They protect properly authenticated transport. AAA authorization/accounting, least privilege, credential handling and console recovery remain separate requirements.
22. **When do metric, AD and longest-prefix match operate?** A process selects candidates using its metric; the RIB compares same-prefix sources using AD; forwarding selects the most specific installed prefix. Unrelated protocol metrics are not comparable units.
23. **Can static `/8` AD 1 beat installed OSPF `/24` for an address inside it?** No. The `/24` is more specific; AD compares competing sources for the same prefix at installation.
24. **When does a floating static take over?** When preferred same-prefix candidates cease qualifying and its own next hop/interface remains usable. An application outage need not remove a route; AD 255 is not an installed backup.
25. **Why does a host route affect only one destination?** A `/32` or IPv6 `/128` is most specific for that address. Its eligibility and return path still matter.
26. **Is OSPF 2-WAY always a fault?** No. It is normal between broadcast DROTHER peers, with full adjacencies to DR/BDR. Persistent EXSTART/EXCHANGE requires database-exchange diagnosis, including MTU evidence.
27. **Does matching MTU guarantee adjacency?** No. Interface state, area, timers, network type, router IDs and relevant policy/authentication also matter. A normal neighbor does not itself prove a destination route is installed.
28. **What does an FHRP virtual gateway provide?** A stable gateway identity with participating routers assuming forwarding responsibility. Check active/master state, tracking and failover; this does not remove all upstream failure modes.
29. **How do static NAT, pools and PAT differ?** Static gives a fixed mapping, pools allocate translations from available addresses and PAT can distinguish flows by ports. None automatically supplies routing, DNS or authorization.
30. **What distinguishes DHCP client/server/relay?** The client requests configuration, the server allocates/answers and a relay carries the exchange across routing boundaries. Check options and return traffic; a lease alone does not prove service.
31. **What proves usable NTP and DNS?** NTP needs synchronization/association evidence; DNS needs an appropriate reachable resolver and the intended answer. Configuration alone proves neither.
32. **How do SNMP and syslog support operations?** SNMP exposes managed observations/notifications; syslog records categorized messages with severity. Protect access, synchronize time and define ownership; severity 0 is more urgent than 7.
33. **How do policing and shaping differ?** Policing can drop/remark excess; shaping buffers to smooth transmission. Classification, marking and queuing manage contention without adding bandwidth.
34. **Why distinguish FTP/TFTP from secure transfer?** They lack inherent confidentiality for sensitive configuration transport. Verify supported alternatives, endpoint identity, permissions and file integrity.
35. **How do awareness, training and physical controls combine?** Recognition/reporting, role skills and access restriction/detection reinforce one another. Test denied/revoked access and recovery rather than attendance alone.
36. **What do authentication, authorization and accounting answer?** Who presents credentials, which actions are allowed and what occurred. MFA/certificates/biometrics do not replace permission, recovery or lifecycle controls.
37. **Does an IPsec tunnel prove safe endpoints?** No. It protects configured traffic under its peer/policy assumptions. Endpoint health, routing, access controls and service behavior remain separate.
38. **What does first-match ACL processing imply?** An early broad permit can hide a later deny. Test permitted, denied and unmatched flows on the right interface/direction, preserving recovery access.
39. **What does wildcard `0.0.1.255` ignore?** The low bit of octet three and all of octet four. Pattern `10.20.2.0` matches third octets 2 and 3, not 4; this is not a contiguous subnet mask.
40. **Does TCP `established` prove an observed session?** No. ACK/RST can match without previous traffic. An independent reply-direction ACL also needs its own permitted condition.
41. **Why might DAI block a legitimate static host?** Its binding may be absent from DHCP snooping. Use the documented static-host mechanism and precise trust boundaries; trusting all access ports bypasses validation.
42. **What remains beyond selecting WPA2-PSK in a GUI?** Correct SSID/VLAN, appropriate encryption/strong key, protected management, compatibility and allowed/denied tests. Device support for WPA/WPA2/WPA3 differs.
43. **How do underlay, overlay and controller APIs relate?** Underlay provides transport, overlay adds logical connectivity/policy and controllers expose control/management interfaces. Northbound/southbound describe participants, not automatic trust.
44. **How do REST, JSON and authentication differ?** REST describes resource interactions, JSON encodes data and authentication follows the API contract. Encoding is not encryption; successful authentication does not prove authorization or complete pagination.
45. **How do Ansible and Terraform differ?** Ansible executes tasks/modules against inventory; Terraform plans desired state through providers and state. Both need reviewed intent, scoped credentials, validation and recovery.
46. **How should AI output be checked?** Compare sanitized inputs, source version, interfaces and commands with authoritative documentation and observed state. Test controlled changes and reject unsupported recommendations; predictions are not certainty.
47. **Which v2.0 changes are moves?** DHCP becomes domain-1 troubleshooting; SNMP and syslog appear in domain 5. OSPFv3, DNS record diagnosis, secure transfer, RA Guard, storm control, agentic AI and Ansible execution add explicit scope/depth.
48. **What remains after the local checks pass?** Actual device/simulator configuration, exchanges, failover, wireless/AAA, authenticated API handling and restoration. A bounded workbook does not replace those labs or independent human review.

---

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary explanation, one lab route, and one legitimate assessment; use the official versioned PDF to close gaps. Times are provider values where published and otherwise explicit estimates.

| Resource | Access | Estimated time |
|---|---|---|
| [Cisco v1.1 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) and [v2.0 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf): choose by attempt date; 53 current versus 29 future numbered objectives | Public | 2–4 h mapping budget (editorial) |
| [Cisco U. learning/practice route](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html): guided learning, instructor-led options and assessment; full duration and entitlement not verified | Account; free/paid options | 40–80 h selected-study budget (editorial), plus labs |
| [Cisco Networking Academy](https://www.cisco.com/site/us/en/learn/training-certifications/training/netacad/index.html): networking and Packet Tracer prerequisites; this landing page does not establish a complete CCNA course total | Public catalog/account or academy | Networking Basics 22 h; Packet Tracer introduction 2 h; full CCNA route not verified |
| [Cisco Modeling Labs](https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html): advertises a five-node free experience and paid editions; version 2.10 lists beta wireless support, not proof of support for every WLAN lab | Free tier/paid; verify image/features | 10–40 h deliberate-lab budget (editorial) |
| [CCNA Official Cert Guide Library, second edition](https://www.ciscopress.com/store/ccna-200-301-official-cert-guide-library-9780138221393): July 25, 2024 publication by Wendell Odom, David Hucaby and Jason Gooley; two volumes, companion practice and update program; public catalog only | Paid; public description | More than 8 h companion video advertised; complete book study time not published |
| [O’Reilly library listing](https://www.oreilly.com/library/view/ccna-200-301-official/9780138221539/): blocked during review; no book interior read | Paid | Earlier 63 h 6 min estimate not currently verified |
| [Pluralsight CCNA path](https://www.pluralsight.com/paths/cisco-ccna-cisco-certified-network-associate-200-301): 22 course cards, largely 2020–2021 with two August 2024 updates and a September 11, 2026 IPv4 course; Core Tech library; no paid lessons/assessment read | Paid/trial; verify library | Cards total **57 h 41 min**; header **58 h**; add independent labs |
| [Jeremy’s IT Lab video route](https://www.youtube.com/watch?v=H8W9oMNSuwo): response was a shell; playlist, labs and current alignment not verified | Public | Current total not verified; earlier 60–90 h was a study budget |
| [Neil Anderson CCNA course](https://www.udemy.com/course/ccna-complete/): public page blocked; previous update/version claims not reconfirmed | Paid | Earlier 42 h 42 min listing not currently verified |
| This guide’s eight proposed labs, 48 answered prompts and executed local workbook | Public | 25–45 h practice budget (editorial); not a readiness guarantee |

This comparison uses public metadata, not paid lessons, book interiors, proprietary questions or subscriber labs. Dates/durations describe listings, not verified teaching quality or full v2.0 coverage. Use a legitimate explanation-rich assessment to locate gaps, then demonstrate behavior in your lab; avoid recalled/live items and answer-only banks.
