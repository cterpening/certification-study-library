---
exam_code: 200-301
vendor_id: cisco
official_blueprint: https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-02
---

# Cisco Certified Network Associate (200-301 CCNA) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#200-301-coverage-record). Cisco's [live exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html) and [v1.1 blueprint](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) are authoritative for exams through February 2, 2027.

**Current baseline:** 200-301 CCNA v1.1, six domains weighted 20/20/25/10/15/10; available through February 2, 2027<br>
**Scheduled change:** CCNA v2.0 launches February 3, 2027 with five reorganized 25/25/20/20/10 domains, more troubleshooting/configuration, OSPFv3, DNS records, secure file transfer, IPv6 RA Guard, agentic AI, prompting, and Ansible execution<br>
**Official source:** [current exam](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html) · [v1.1 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) · [v2.0 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf) · [transition date](https://blogs.cisco.com/learning/stay-on-track-get-certified-before-the-ccna-refresh)

## How to use this guide

For every feature, be able to move through requirement → packet/control-plane behavior → minimum configuration → verification output → likely fault → safe correction and rollback. Build a small repeatable Packet Tracer, CML, GNS3/EVE-NG, or authorized hardware lab; save topology, addressing plan, clean configuration, expected outputs, fault, diagnosis, repair, and post-change evidence.

The current exam page lists v1.1 as a 120-minute English/Japanese exam for USD 300. Cisco's newer marketing page presents future-facing information and a different price, so verify the actual scheduling checkout before purchase. The credential is generally valid for three years and can be renewed through Cisco's current recertification program. Logistics and policy can change independently of the blueprint.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the current published objectives. A `Related item — scheduled v2.0:` callout specifically identifies February 3, 2027 scope and must not be confused with current v1.1 exam coverage.

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

Subnetting must be fluent. Given an IPv4 address/prefix, find network, broadcast, usable range, host/subnet capacity and whether a destination is local. Know RFC 1918 private space and why NAT is not a security boundary. Configure and verify address/prefix/gateway on IOS interfaces and confirm Windows/macOS/Linux parameters.

For IPv6, recognize global unicast, unique local, link-local, multicast and anycast behavior; IPv6 has no broadcast. Configure/verify address and prefix, link-local behavior, and default route. Modified EUI-64 forms an interface identifier from a MAC-derived value; privacy/stable address methods also exist.

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

EtherChannel bundles compatible links into one logical port-channel. LACP is the v1.1 named negotiation method; active initiates and passive responds, while two passive sides do not form. Member parameters must agree (speed/duplex, access/trunk mode, VLAN settings and other platform requirements). Spanning Tree treats a functioning bundle logically, while the hashing algorithm distributes flows rather than splitting every packet equally.

Verify summary, neighbor, port-channel, member state, trunk/VLAN and counters. A suspended/member mismatch is not solved by blindly forcing mode; correct the configuration contract.

### Rapid PVST+

Spanning Tree prevents Layer 2 loops by electing a root bridge, selecting root/designated/alternate roles, and placing ports into forwarding/discarding states. Lower bridge ID wins root election. Each non-root switch chooses its best root port; each segment gets a designated port. Rapid PVST+ runs per VLAN.

PortFast accelerates a trusted edge port and does not disable STP. BPDU Guard protects edge assumptions by disabling an edge port receiving BPDUs. Root Guard prevents a port from becoming a root path; Loop Guard protects against certain missing-BPDU conditions; BPDU Filter can suppress BPDUs and is dangerous if it creates an unmanaged loop. Know mechanism and placement.

### Wireless architecture

Autonomous versus controller-based APs differ in management/control. Lightweight APs may form control/data tunnels to a WLC; local/flex modes alter forwarding/operation. Understand AP/WLC physical connections, access/trunk ports and link aggregation. Given a WLAN GUI, interpret SSID/profile, VLAN/interface mapping, security/authentication, QoS and advanced settings. Separate association, authentication, addressing, name resolution and application problems.

Management access includes console, SSH, Telnet, HTTP/HTTPS, TACACS+/RADIUS-backed AAA, and cloud-managed interfaces. Prefer encrypted, authenticated, least-privilege paths with logging and an emergency recovery plan.

**Related item — scheduled v2.0:** Edge-host and infrastructure port configuration becomes more explicit, discovery validates documentation, show/log/ping/extended-ping/traceroute/packet-capture troubleshooting is central, and Rapid PVST+ shifts from interpretation toward configuration. BPDU Filter drops from the named v2.0 guard list.

---

## 3. IP Connectivity — 25%

### Route interpretation and selection

A route contains source/protocol code, prefix/mask, next hop or exit interface, administrative distance, metric and age. Forwarding first uses longest-prefix match. If identical prefixes arrive from different sources, lower administrative distance normally selects the route; within a routing protocol, its metric selects among paths. A default route (`0.0.0.0/0` or `::/0`) is least specific and supplies a gateway of last resort.

Connected/local routes appear when interfaces are correctly addressed/up. A missing route may actually originate from a down interface, failed adjacency, filtering, wrong prefix, recursion or administrative distance. `show ip route`, `show ipv6 route`, interface/ARP/neighbor, protocol and ping/traceroute evidence must agree.

### Static routes

Configure/verify IPv4 and IPv6 default, network, host and floating static routes. A floating route uses a higher administrative distance than the preferred route. Fully specified next hop plus interface can help on multiaccess networks; platform/address-family syntax varies. Validate installation and actual forwarding/return path, then test primary failure and recovery.

Avoid recursive/next-hop errors, pointing to a local interface when a next hop is needed, wrong mask, absent reverse route, and a backup route that never becomes active. A successful ping to the next hop does not prove the full destination path.

### Single-area OSPFv2

OSPF is a link-state IGP. For v1.1, configure/verify single-area OSPFv2, neighbor adjacency, point-to-point and broadcast networks, DR/BDR election, and router ID. Neighbors need compatible area, network type, timers, authentication if used, and usable IP/subnet conditions; unique router IDs matter. Broadcast networks elect DR/BDR; point-to-point does not need that election.

Use `show ip ospf neighbor`, `show ip ospf interface`, `show ip protocols`, database and route outputs. Diagnose from state: no neighbor differs from 2-WAY on a broadcast segment, which differs from EXSTART/EXCHANGE. Confirm whether a route is advertised, learned, preferred and forwardable.

### First-hop redundancy

FHRPs provide a resilient virtual default gateway across routers. One device forwards as active/master while another can assume the shared virtual IP/MAC. Priority, preemption, tracking, timers and failure modes affect operation. v1.1 asks purpose/functions/concepts rather than named configuration.

**Related item — scheduled v2.0:** The routing share becomes 20%, but OSPFv3 for IPv6 is explicitly configured alongside OSPFv2. HSRP and VRRP operational status are named. Add an IPv6 OSPF lab before a February 2027 attempt.

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

**Related item — scheduled v2.0:** Services and security merge. NAT/PAT, local/central AAA, SFTP/SCP, detailed DNS record diagnosis, ACLs and Layer 2 controls become the core. NTP, DHCP configuration, QoS and TFTP/FTP leave the named v2.0 list, but remain operationally useful supporting knowledge.

---

## 5. Security Fundamentals — 15%

Threats can exploit vulnerabilities; mitigations reduce likelihood/impact. Security programs combine awareness/training, physical access, identity, configuration, monitoring, response, recovery and governance. Authentication proves identity, authorization permits action and accounting records it.

Use `enable secret`/strong stored alternatives, unique local users where appropriate, secure console/VTY policy, session limits, least privilege, MFA/certificates/biometrics through supporting systems, and centralized TACACS+/RADIUS when required. Password policy includes length, uniqueness, storage, lifecycle, recovery and attack protection—not arbitrary complexity alone.

IPsec can protect site-to-site or remote-access traffic; distinguish protected tunnel, peer/authentication, policy and routed reachability. Encryption does not validate endpoint health.

ACLs are ordered first-match rules with an implicit deny. Standard IPv4 ACLs match source; extended ACLs can match source/destination/protocol/ports. Numbered/named defines management syntax, not capability alone. Plan intent, place deliberately, account for required return/control traffic, apply correct direction/interface, inspect hit counts and test permitted and denied cases. Preserve recovery access.

DHCP snooping establishes trusted server-facing behavior and a binding database; Dynamic ARP Inspection can validate ARP against trusted bindings; port security limits learned/allowed MAC behavior. These controls depend on correct trust boundaries. Wireless options include WPA/WPA2/WPA3; v1.1 asks configuration of a WPA2-PSK WLAN in the GUI. Use strong PSK, AES, protected administration and segmentation.

**Related item — scheduled v2.0:** Storm control and IPv6 RA Guard join DHCP snooping, DAI and port security. Practice protecting IPv6 neighbor/router discovery without blocking legitimate control traffic.

---

## 6. Automation and Programmability — 10%

Automation improves repeatability, scale, auditability and feedback but can also multiply an error. Use source-controlled intent, validation, scoped credentials, idempotent/retry-aware behavior, staged deployment, telemetry and rollback.

Traditional device-by-device management distributes control. Controller-based/software-defined architecture separates control and data concerns, uses an underlay for transport and an overlay/fabric for logical connectivity/policy. Southbound interfaces connect controllers to infrastructure; northbound APIs expose intent/data to applications. Actual architectures may not fit a simplistic one-controller diagram.

REST APIs use resources/URIs, HTTP methods (GET/read, POST/create/action, PUT replace, PATCH modify, DELETE), status codes, headers, authentication and serialized data. CRUD maps conceptually to create/read/update/delete. JSON contains objects `{}`, arrays `[]`, key/value pairs, strings, numbers, booleans and null; indentation is presentation, while brackets/quotes/commas/colons define structure.

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
| AI, Network Operations and Management | 10% | Add agentic AI, prompt selection, management approach comparison, Ansible command execution and syslog interpretation |

The change is not merely renaming. Build a separate v2 checklist and labs; do not assume old course completion covers new troubleshooting depth.

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

1. **Addressing:** Design dual-stack addressing/VLSM for four VLANs, configure interfaces/hosts, and prove local/remote path and default behavior.
2. **Access layer:** Configure data/voice VLANs, trunks/native/allowed lists, inter-VLAN routing, CDP/LLDP and a deliberate mismatch; diagnose from outputs.
3. **Resilient Layer 2:** Build LACP EtherChannel and Rapid PVST+ across redundant links; set root placement and safely demonstrate PortFast/BPDU Guard behavior.
4. **Routing:** Configure IPv4/IPv6 static/default/host/floating routes and single-area OSPFv2; break adjacency/route preference and repair with evidence.
5. **Services:** Configure NAT static/pool/PAT, NTP, DHCP relay/client and SSH in a disposable topology; validate translations, time, lease, secure access and failure cases.
6. **Security:** Configure local access, standard/extended named ACLs, port security, DHCP snooping/DAI and a WPA2-PSK lab WLAN; test allowed and denied behavior.
7. **Automation:** Parse supplied JSON, make authenticated GET in a sandbox API, build a small Ansible/Terraform comparison, and validate every proposed change before execution.
8. **Capstone:** Given an unknown fault spanning VLAN, route, DNS/service or ACL, capture baseline/show/log/ping/traceroute/packet evidence, diagnose, repair, roll back/retest and write the change record. Add OSPFv3, DNS records, RA Guard and an AI-output verification step for a v2.0 variant.

## Readiness checks

1. Compare two-tier, three-tier, spine-leaf, WAN, SOHO, on-premises and cloud topologies.
2. Map routers, L2/L3 switches, firewall/IPS, AP/controller, endpoints/servers and PoE into one packet path.
3. Diagnose collision/error/CRC/drop/speed/duplex symptoms without assuming cause.
4. Calculate network/broadcast/range and VLSM plan without a calculator, then verify.
5. Configure/verify IPv4 and IPv6 address/prefix/gateway on IOS and a client OS.
6. Classify IPv6 global, unique-local, link-local, multicast, anycast and modified EUI-64.
7. Explain wireless channel, RF, interference, SSID, encryption and shared-medium behavior.
8. Compare VM, container and VRF isolation.
9. Trace MAC learning, known/unknown forwarding, flooding and aging.
10. Configure/verify access/data/voice VLANs, trunks, 802.1Q/native VLAN and inter-VLAN routing.
11. Use CDP/LLDP to validate rather than blindly trust a diagram.
12. Form and troubleshoot LACP EtherChannel.
13. Elect Rapid PVST+ root and identify every port role/state in a topology.
14. Place PortFast, BPDU Guard, Root Guard, Loop Guard and BPDU Filter safely.
15. Interpret AP/WLC connection and WLAN GUI security/QoS/VLAN settings.
16. Select console, SSH, HTTPS, TACACS+/RADIUS or cloud management appropriately.
17. Interpret protocol, prefix, next hop, AD, metric and default in a routing table.
18. Apply longest-prefix match, then AD and metric in the right order.
19. Configure/verify default/network/host/floating static routes for IPv4 and IPv6.
20. Configure/verify OSPFv2 adjacency on point-to-point and broadcast networks.
21. Diagnose OSPF neighbor state and explain DR/BDR/router ID.
22. Explain FHRP virtual gateway, priority/preemption and tracking behavior.
23. Configure/verify static/dynamic-pool NAT and explain PAT.
24. Configure/verify NTP, DHCP client/relay and SSH.
25. Explain DNS, SNMP, syslog facilities/severity and TFTP/FTP security limits.
26. Distinguish classification/marking/queuing/congestion/policing/shaping.
27. Turn threats/vulnerabilities/exploits into layered program mitigations.
28. Design local/central access with password, MFA/certificate and AAA considerations.
29. Configure/verify standard/extended, named/numbered ACL behavior including implicit deny.
30. Explain DHCP snooping → binding → DAI and port-security trust assumptions.
31. Compare WPA/WPA2/WPA3 and configure/verify a WPA2-PSK WLAN in a lab GUI.
32. Explain underlay/overlay/fabric, control/data planes and north/south APIs.
33. Map CRUD to HTTP methods/status/authentication and interpret nested JSON.
34. Compare Ansible and Terraform capability, state and safe delivery boundaries.
35. Validate a generative/predictive AI recommendation against sanitized source evidence and device output.
36. For an exam after February 2, 2027, can you additionally troubleshoot clients/DHCP, configure OSPFv3/central AAA/SFTP/SCP/storm control/RA Guard, diagnose DNS records, use Ansible commands and constrain an agentic assistant?

### Check key

Strong answers predict exact control/data-plane behavior before showing commands. Configuration answers include pre-state, minimal change, verification, negative test, failure interpretation and rollback. Route and STP answers apply selection order, not memorized output. AI/automation answers protect data and credentials, constrain scope, validate on a canary, and treat device telemetry—not generated prose—as authority.

---

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary explanation, one lab route, and one legitimate assessment; use the official versioned PDF to close gaps. Times are provider values where published and otherwise explicit estimates.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [Cisco v1.1 exam topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) and [v2.0 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf) | Public | 2–4 h to baseline/map | Choose by booked date; v1.1 through February 2, 2027, v2.0 from February 3 |
| [Cisco U. CCNA learning/practice route](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html) | Free/paid account tiers | 40–80 h selected learning plus labs | First-party path, hands-on practice and practice exam; catalog/entitlement/duration vary |
| [Cisco Networking Academy](https://www.cisco.com/site/us/en/learn/training-certifications/training/netacad/index.html) | Free account or academy | 70–210 h depending route | Strong structured networking and Packet Tracer route; align selected curriculum to booked version |
| [Cisco Modeling Labs](https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html) | Free tier/paid | 10–40 h deliberate labs | More realistic virtual Cisco images/topologies; licensing and resource requirements vary |
| [CCNA 200-301 Official Cert Guide Library, 2nd Edition](https://www.oreilly.com/library/view/ccna-200-301-official/9780138221539/) | Paid | About 63 h 6 min plus labs/practice | 2024 v1.1-aligned Cisco Press depth and companion practice; use publisher updates and a v2 delta after February 2 |
| [Pluralsight CCNA 200-301 path](https://www.pluralsight.com/paths/cisco-ccna-cisco-certified-network-associate-200-301) | Paid/trial | About 59 h plus labs | Broad course/lab/practice route; many modules are older, so close v1.1 AI/Terraform and all v2 deltas officially |
| [Jeremy's IT Lab free CCNA course](https://www.youtube.com/watch?v=H8W9oMNSuwo) | Public | About 60–90 h with labs/flashcards | Popular free explanation/lab sequence; verify version and add current/future deltas |
| [Neil Anderson complete CCNA course](https://www.udemy.com/course/ccna-complete/) | Paid | 42 h 42 min plus labs/review | Highly used v1.1 course updated August 2026; verify v2 coverage before a post-transition booking |
| This guide's eight labs and 36 checks | Public | 25–45 h | Evidence-led consolidation and version transition |

Use Cisco U./Cisco Press/Pearson or another reputable explanation-rich practice assessment to locate gaps. Avoid recalled/live items, “actual questions,” answer-only banks and pass guarantees. A high score achieved by memorizing a bank is not evidence that you can predict and repair a network.
