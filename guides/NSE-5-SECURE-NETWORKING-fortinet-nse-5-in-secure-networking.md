---
exam_code: NSE-5-SECURE-NETWORKING
vendor_id: fortinet
official_blueprint: https://training.fortinet.com/local/staticpage/view.php?page=nse_5_secure_networking
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: scheduled
upcoming_change_checked: 2026-10-28
---

# Fortinet NSE 5 in Secure Networking Study Guide

> **Independent AI-assisted resource — SOURCES + CURRENT PATH REQUIREMENTS CHECKED; HUMAN REVIEW PENDING.** Fortinet's live track page, current FortiSwitch, Secure Wireless LAN, and SD-WAN exam pages, Fortinet release notices, course library, and product documentation were rechecked October 28, 2026. The [official track page](https://training.fortinet.com/local/staticpage/view.php?page=nse_5_secure_networking) and the chosen exam page are authoritative.

**Current baseline:** This is a certification track, not one exam. Hold active NSE 4 FortiOS and pass **one** eligible NSE 5 Secure Networking exam within two years. Current routes are FortiSwitch 7.6 Administrator, Secure Wireless LAN 7.6 Administrator, or SD-WAN 7.6 Core Administrator.<br>
**Current available exams:** FortiSwitch 7.6 Administrator (70 minutes, 35–40 questions, English/Japanese), Secure Wireless LAN 7.6 Administrator (70 minutes, 30–40 questions, English), and SD-WAN 7.6 Core Administrator (60–70 minutes, 30–35 questions, English). Fortinet does not publish weights for the FortiSwitch or Secure Wireless routes; the SD-WAN page publishes three weighted groups.<br>
**Credential contract:** NSE 4 must be active when requirements are fulfilled. The credential is active for two years from the NSE 5 exam date. Retakes of failed proctored exams require 15 days; a passed exam cannot be retaken and cannot be reused to renew the same credential.<br>
**October 28, 2026 pathway check:** SD-WAN 7.6 Core Administrator is now an available route. Secure Wireless LAN 7.4 reached its August 31, 2026 final-delivery date; use 7.6. The Fortinet-owned Secure Wireless LAN 7.6 course materials page was updated April 15, 2026.<br>
**Integrity:** Pick and prepare for one current route. Do not combine its topics into a fictional weighted exam and do not use recalled questions.

> **September 17, 2026 contract check:** Current official exam and track pages were inspected; the exam times and prerequisite statements above reflect that check. Historical objective snapshots and full technical-review dates remain unchanged. See the [exam validation report](../docs/research/2026-09-17-exam-validation.md).

## How to use this guide

First verify that NSE 4 will remain active through the NSE 5 exam date. Then select one route based on job need and lab access. Read the chosen exam page line by line and treat its version as the technical baseline. The common foundations below connect routes; the route sections are not substitutes for that exam's exact published topics.

> **About related items:** A `Related item:` callout adds operational, security, or lifecycle context. It makes a published task more useful in production but does not enlarge the official exam scope.

## Route selector

| Route | Current status | Best fit | Authoritative scope |
|---|---|---|---|
| FortiSwitch 7.6 Administrator | Available | FortiLink/standalone switching, VLAN, STP, QoS, L2 security, operations | [Exam page](https://training.fortinet.com/local/staticpage/view.php?page=fortiswitch_administrator_exam) |
| Secure Wireless LAN 7.6 Administrator | Available | FortiAP, FortiGate controller, FortiEdge Cloud, RF/security/analytics | [Exam page](https://training.fortinet.com/local/staticpage/view.php?page=secure_wireless_lan_administrator_exam) |
| SD-WAN 7.6 Core Administrator | Available | Architecture, health checks, traffic control/routing, centralized management, visibility and troubleshooting | [Exam page](https://training.fortinet.com/local/staticpage/view.php?page=sd-wan_core_administrator_exam) |

The SD-WAN route publishes Architecture and Concept (15–25%), Traffic Control/Rules/Routing (35–45%), and Centralized Management/Visibility/Troubleshooting (35–45%). These are route-specific ranges; do not blend them with the other two exam paths.

## 1. Common secure-networking foundations

Maintain an inventory of sites, switches, access points, controllers/managers, FortiGate interfaces, firmware, licenses, owners, management paths, uplinks, VLANs/subnets, routing, authentication, certificates, logs, and dependencies. Establish supported version combinations before deployment or upgrade.

**Version-specific wireless example:** FortiAP 7.6.3 documents Wi-Fi 7 multi-link operation and preamble puncturing on selected models, with country, regulatory, and hardware support boundaries. Use the [FortiAP 7.6.3 release notes](https://docs.fortinet.com/document/fortiap/7.6.3/fortiap-release-notes/277928/new-features-or-enhancements) to verify eligibility before using these as lab examples; they are not additional exam objectives.

Separate management, control, and data planes. A reachable management GUI does not prove endpoint traffic, FortiLink, CAPWAP, VLAN trunking, routing, authentication, or inspection. Diagram discovery, authorization, provisioning, configuration, telemetry, and failure behavior for the chosen platform.

Apply least privilege to administrators and device trust. Restrict management protocols and source networks, use named roles and MFA, protect backups and credentials, synchronize time, export logs, and preserve a recovery path. Test both authorized and unauthorized access.

**Related item: physical dependencies.** Power, cabling, optics, RF placement, PoE budgets, upstream loops, and environment can defeat correct software configuration.

## 2. FortiSwitch route

### Switching, VLANs, and loop prevention

Understand access/untagged versus trunk/tagged VLAN behavior, native VLAN assumptions, allowed VLAN lists, inter-VLAN routing, MAC learning, and broadcast domains. Trace a frame through ingress classification, MAC lookup, forwarding/flooding, uplink, gateway, policy, and return path.

Spanning Tree Protocol prevents Layer 2 loops by electing topology roles and blocking redundant paths. Know root placement, path cost, port roles/states, edge/PortFast equivalents, BPDU protection, and the consequence of inconsistent settings. Link aggregation combines supported links but depends on member consistency and, for MCLAG, peer health and split-brain prevention.

QoS classifies and schedules traffic under contention; LLDP and LLDP-MED exchange neighbor/voice-network information. Prove markings and queue behavior during load, not by configuration alone. Validate supported optics, split-port mode, speed/duplex, and stack topology against hardware documentation.

### FortiLink, management modes, and tenancy

FortiSwitch can be FortiGate-managed over FortiLink, standalone, cloud-managed where supported, or managed through other supported patterns. FortiLink requires compatible versions, physical/logical path, discovery and authorization, management addressing, VLAN/provisioning state, and correct topology. Know which system owns the configuration before changing it.

Multi-tenancy and administrative-domain boundaries require explicit device, VLAN, port, policy, log, and role scope. Avoid assuming that a GUI view alone enforces traffic isolation; test data paths and administrative negative access.

### Layer 2 security and troubleshooting

Use port security, MAC limits/sticky behavior where supported, DHCP snooping, dynamic ARP inspection, IP source guard, ACLs, VLAN segmentation, 802.1X/NAC, and security profiles according to threat and topology. These controls depend on trusted-port classification and valid bindings; a mistake can block legitimate infrastructure or trust an attacker-facing port.

Troubleshoot physical status and counters, transceiver, speed/duplex, VLAN/tagging, MAC table, STP/LAG/MCLAG, FortiLink authorization/state, DHCP/ARP, ACL/port security, route/policy, and packet capture. Change one hypothesis at a time.

**Related item: rollback access.** VLAN, trunk, STP, and FortiLink changes can cut off management. Use console/out-of-band access and staged changes.

## 3. Secure Wireless LAN route

### RF and deployment fundamentals

Understand channels, frequency bands, channel width, attenuation, interference, signal strength, signal-to-noise ratio, airtime, contention, data rates, roaming, and client capability. More transmit power or wider channels can worsen contention. Design coverage and capacity from measured requirements and validate with surveys and client telemetry.

Deploy FortiAP through the FortiOS integrated wireless controller or FortiEdge Cloud under the exact route/version. Map discovery, authorization, CAPWAP/control and data tunneling/local bridge behavior, AP profiles, radio settings, SSIDs, VLANs, DHCP, firewall policy, and logs. FortiAIOps can assist analysis; verify inputs and recommendations before change.

### Access and segmentation

Select WPA2/WPA3 personal or enterprise modes based on current client and risk requirements. Enterprise authentication adds RADIUS/identity, server-certificate validation, EAP method, user/device lifecycle, and accounting. Never train users to accept arbitrary authentication certificates.

Map SSID to intended VLAN, NAC/identity posture, policy, address/DNS services, and isolation. Guest access needs onboarding, acceptable-use/privacy, expiry, rate/control, internal isolation, logging, and sponsor or identity governance. Test cross-VLAN denial and permitted services.

### Monitoring, threats, and diagnostics

Identify rogue, neighboring, impersonating, misconfigured, and interfering devices using evidence; automatic containment can disrupt legitimate networks and may be legally restricted. Monitor AP/controller/cloud health, adoption, radio/channel utilization, retries, interference, client RSSI/SNR/rate, authentication/DHCP, roaming, and application experience.

Troubleshoot in sequence: client/radio, association, authentication, address/DNS, VLAN/tunnel, policy/NAT, route, destination, and return path. Correlate controller, AP, RADIUS, DHCP, firewall, packet capture, and client evidence.

## 4. SD-WAN route readiness

Use the live SD-WAN 7.6 Core Administrator page for its published exam contract and weighted groups. The official SD-WAN course remains useful for members and zones, active/passive performance SLAs, rule matching and strategies, routing, sessions, direct internet access, monitoring, and failure; keep study aligned to the exam page's current outline.

For real deployments, distinguish underlay and overlay, routing eligibility, health measurement, SD-WAN rule, firewall policy/NAT, session persistence, and return path. Validate loss/latency/jitter and application reachability, stable failover/failback, and visibility.

**Availability check:** SD-WAN 7.6 Core Administrator is listed as an available route on the live track and exam pages as of October 28, 2026. Verify current scheduling and eligibility before booking.

## Integrated scenarios

### Resilient branch LAN

Design FortiGate-managed switches with separate employee, voice, guest, management, and infrastructure VLANs; redundant uplinks; intentional STP/MCLAG; access security; DHCP protections; QoS; logging; and console rollback. Prove a client path and one member/uplink failure.

### Secure office Wi-Fi

Plan measured RF coverage/capacity, AP profiles, enterprise and guest SSIDs, identity/certificates, VLAN/NAC policy, rogue monitoring, logs, and FortiEdge Cloud or controller ownership. Test failed RADIUS, DHCP exhaustion, wrong VLAN, interference, roam, and prohibited east-west access.

### New SD-WAN candidate path

Build two lab transports, relevant health probes, members/zones, routing and a business rule. Prove preferred path, brownout, outage, session behavior, return symmetry, and stable recovery. Use the SD-WAN 7.6 route's published exam outline to direct study.

## Hands-on labs

1. Build an authorized inventory/version/topology and recoverable management baseline.
2. Configure two VLANs and a routed/policy boundary; prove tagging, MAC learning, permitted and denied paths.
3. Create a redundant switching topology; observe STP or supported MCLAG behavior, then test a single-link failure safely.
4. Apply one Layer 2 protection to a lab access port; test legitimate and spoofed synthetic behavior and rollback.
5. Diagnose a FortiLink adoption or VLAN fault from physical state through packet path.
6. Design or deploy two APs with measured channels/power; collect RF and client evidence under load.
7. Configure enterprise and guest wireless in a lab; validate certificate, RADIUS, VLAN, DHCP, policy, isolation, and expiry.
8. Diagnose association, authentication, DHCP, DNS, policy, and interference failures one at a time.
9. Model an SD-WAN rule and SLA with two paths; capture healthy, brownout, outage, and recovery behavior.
10. Write a change and rollback runbook that preserves console/out-of-band access.

## Original readiness checks

1. What exact combination earns NSE 5 Secure Networking?
2. Must candidates pass every listed NSE 5 route exam?
3. Which exam routes are currently available in the NSE 5 Secure Networking track?
4. Why must the chosen exam page drive study scope?
5. What belongs in a secure-network inventory?
6. How do management, control, and data planes differ?
7. What proves compatible lifecycle planning?
8. How do access and trunk VLAN behavior differ?
9. Why can native-VLAN assumptions cause failures or exposure?
10. What problem does STP solve?
11. What makes link aggregation healthy?
12. When does QoS change packet experience?
13. What is FortiLink's role?
14. Why must configuration ownership be known?
15. Which controls reduce common Layer 2 spoofing risks?
16. Why does trusted-port classification matter?
17. What is a safe switching troubleshooting order?
18. Why is out-of-band access valuable?
19. How do coverage and capacity differ in Wi-Fi design?
20. Why can wider channels or more power hurt service?
21. What dependencies support FortiAP adoption?
22. What must enterprise wireless authentication validate?
23. How is a guest SSID safely separated?
24. Why can automatic rogue containment be risky?
25. Which metrics distinguish RF from identity or DHCP failure?
26. What is a useful wireless troubleshooting order?
27. How do SD-WAN routing and steering differ?
28. What makes a performance SLA application-relevant?
29. Why must failback stability be tested?
30. What should a candidate verify before booking the SD-WAN 7.6 exam?
31. What changed for Secure Wireless LAN 7.4?
32. What is the NSE 5 proctored-exam retake rule?
33. What does exam reuse mean for renewal?
34. What evidence makes a lab result reproducible?
35. What must be rechecked before booking?

## Answers and reasoning

1. An active NSE 4 FortiOS plus one eligible proctored NSE 5 Secure Networking exam within two years.
2. No. The live track requires one listed route exam, not all of them.
3. FortiSwitch 7.6, Secure Wireless LAN 7.6, and SD-WAN 7.6 Core Administrator; each is a currently listed route, with different exam contracts.
4. Each route has different products, versions, topics, question count, time, and experience assumptions.
5. Devices/sites, models/versions, ownership, management, links, VLANs/routes, trust, identities, licenses, logs, dependencies, backup, and support.
6. Management administers, control establishes topology/state, and data carries user/application traffic.
7. A documented support matrix, tested upgrade path, backups, staged validation, capacity, and rollback.
8. Access ports normally place untagged endpoint traffic into one VLAN; trunks carry multiple tagged VLANs under an allowed list/native convention.
9. Untagged frames may land in an unintended segment or fail between devices using different assumptions.
10. It creates a loop-free Layer 2 topology while preserving controlled redundancy.
11. Compatible members, same logical settings, correct peer/system state, hashing expectations, and tested failure/recovery.
12. Under contention; classification, marking trust, queues, scheduling, and drops must be measured during load.
13. Discovery, authorization, provisioning, configuration, and monitoring of supported FortiSwitches from FortiGate.
14. Changes made at the wrong manager can be overwritten or create drift and outage.
15. Port security, DHCP snooping, dynamic ARP inspection, IP source guard, ACLs, VLANs, NAC/802.1X, and BPDU protections where supported.
16. Binding and inspection controls exempt or trust infrastructure ports; a wrong designation bypasses defense or blocks legitimate service.
17. Physical/optics/counters, speed, VLAN/MAC, STP/LAG, FortiLink, DHCP/ARP, ACL/security, route/policy, and capture.
18. A VLAN, trunk, loop-prevention, or controller change can remove in-band management.
19. Coverage supplies usable signal; capacity supplies enough airtime and throughput for client/application demand.
20. They increase contention, co-channel interference, cell imbalance, or noise overlap depending on design.
21. Power/link, addressing/DNS/time, compatible firmware, discovery/control path, authorization, profile, VLAN/data path, and licensing/manager state.
22. Identity, EAP method, RADIUS trust/availability, server certificate/name, group policy, accounting, failure, and revocation.
23. Dedicated identity/onboarding and VLAN, internal isolation, least-privilege internet policy, expiry, logging, privacy, and tested denial.
24. It may disrupt an authorized neighboring AP and may violate policy or radio-regulatory/legal constraints.
25. RSSI/SNR/channel/retry/airtime show RF; association/auth logs show access; DHCP lease/exchange shows addressing.
26. Radio/client, association, authentication, DHCP/DNS, VLAN/tunnel, policy/NAT, route, server, return path.
27. Routing supplies eligible reachability; SD-WAN rules choose paths using source/destination/application/business and health context.
28. Representative target/path, relevant loss/latency/jitter, stable thresholds, probe source, frequency, and failure meaning.
29. A recovered but unstable path can cause flapping, loss, asymmetry, or repeated session moves.
30. Confirm the live route remains available, then verify its current schedule, language, delivery, prerequisites, and published topic groups.
31. Its last delivery date was August 31, 2026; the current route is 7.6.
32. Wait 15 days after a failed exam; a passed exam cannot be retaken.
33. Once counted for the certification, the same exam cannot simply be reused to renew that certification.
34. Baseline/version, topology/config, exact action, expected result, observed state/log/capture, negative test, rollback, and cleanup.
35. Active NSE 4, eligible exam/version/status, topics, contract, language, delivery, policy, cost, and renewal requirements.

## Key terms and phrases
These terms span several electives. Use the linked sections to find the ones that apply to your chosen exam.

**Common secure-networking foundations**

| Term or phrase | Meaning |
|---|---|
| [Authentication](#1-common-secure-networking-foundations) | The check that establishes who a user or device is. Authorization determines what that identity may do next. |
| [Authorization](#1-common-secure-networking-foundations) | Determining whether a given identity may perform a specific action on the particular resource requested. |
| [FortiAP](#1-common-secure-networking-foundations) | A Fortinet wireless access point. Radio settings, management connectivity and the client data path are distinct parts of its deployment. |
| [FortiGate](#1-common-secure-networking-foundations) | The Fortinet firewall platform that applies routing, access policy and security inspection to traffic traversing its interfaces. |
| [Least privilege](#1-common-secure-networking-foundations) | Giving an identity only the permissions needed for its task, for as long as it needs them. |
| [Multifactor authentication (MFA)](#1-common-secure-networking-foundations) | Authentication using factors from two or more categories. A password and a second password both use the same knowledge factor. |
| [Subnet](#1-common-secure-networking-foundations) | A portion of an IP address space sharing a network prefix. Hosts use the prefix to distinguish local delivery from traffic requiring a router. |
| [Telemetry](#1-common-secure-networking-foundations) | Logs, events and measurements supplied by managed systems. Customer attribution and collection health determine whether the records are usable. |
| [Trunk port](#1-common-secure-networking-foundations) | A switch link that can carry multiple VLANs. Tagging and native-VLAN treatment must agree at both ends. |

**FortiSwitch route**

| Term or phrase | Meaning |
|---|---|
| [Virtual LAN (VLAN)](#switching-vlans-and-loop-prevention) | A logical Layer 2 broadcast domain. A frame moving between VLANs normally crosses a routing boundary. |
| [Spanning Tree Protocol (STP)](#switching-vlans-and-loop-prevention) | A switching protocol that prevents forwarding loops by keeping selected redundant paths out of the active topology. |
| [Bridge protocol data unit (BPDU)](#switching-vlans-and-loop-prevention) | A control frame exchanged by spanning tree participants. Unexpected BPDUs on an edge port can signal the wrong device or topology. |
| [Broadcast domain](#switching-vlans-and-loop-prevention) | The set of interfaces that receive a Layer 2 broadcast. A VLAN divides a switched network into separate broadcast domains. |
| [Frame](#switching-vlans-and-loop-prevention) | A link-layer unit of transmission carrying a payload and addressing information for one local hop. Routers build a new link-layer frame for the next hop. |
| [Link aggregation](#switching-vlans-and-loop-prevention) | Treating compatible links as one logical interface for redundancy and load distribution. A single flow may still use only one physical member. |
| [Native VLAN](#switching-vlans-and-loop-prevention) | The VLAN associated with untagged traffic on an 802.1Q trunk under the applicable configuration. A mismatch can place traffic in different VLANs at each end. |
| [Quality of service (QoS)](#switching-vlans-and-loop-prevention) | Classifying and treating traffic differently under contention, such as protecting voice delay while bulk transfers share the link. |
| [Split brain](#switching-vlans-and-loop-prevention) | A failure in which peers lose coordination and more than one behaves as active, risking inconsistent state or conflicting forwarding. |
| [Link Aggregation Control Protocol (LACP)](#switching-vlans-and-loop-prevention) | A negotiation protocol that checks which links and peers can participate in the same aggregated connection. |
| [FortiLink](#fortilink-management-modes-and-tenancy) | The connection over which a FortiGate manages authorized FortiSwitch devices. |
| [Administrative domain (ADOM)](#fortilink-management-modes-and-tenancy) | A FortiManager boundary for managing a selected set of devices, policies and administrative permissions. |
| [FortiSwitch](#fortilink-management-modes-and-tenancy) | A Fortinet Ethernet switch that provides local Layer 2 connectivity and can use supported management arrangements such as FortiLink. |
| [Tenant](#fortilink-management-modes-and-tenancy) | An administrative or customer boundary in a shared service. Data, identities, configurations and actions must stay within the intended tenant. |
| [DHCP snooping](#layer-2-security-and-troubleshooting) | A switch feature that distinguishes trusted server-facing ports from untrusted ones and can maintain address bindings from observed DHCP traffic. |
| [Layer 2](#layer-2-security-and-troubleshooting) | The data-link layer, where local delivery uses frames and link-layer addressing, such as Ethernet switching within a VLAN. |
| [Security profile](#layer-2-security-and-troubleshooting) | A collection of threat or content inspection settings associated with a matching firewall policy, such as web filtering or intrusion prevention. |

**Secure Wireless LAN route**

| Term or phrase | Meaning |
|---|---|
| [Signal-to-noise ratio (SNR)](#rf-and-deployment-fundamentals) | Signal power relative to noise power. A received signal at −60 dBm and noise at −90 dBm give an SNR of −60 − (−90) = 30 dB. |
| [Channel width](#rf-and-deployment-fundamentals) | The amount of radio spectrum assigned to a wireless channel. Increasing width can increase capacity but leave fewer independent neighboring channels. |
| [Firewall policy](#rf-and-deployment-fundamentals) | A rule that identifies matching traffic and determines its treatment. Rule order can change which action applies. |
| [FortiOS](#rf-and-deployment-fundamentals) | The operating system used by FortiGate. Its configuration determines such behaviors as routing, policy matching, inspection and logging. |
| [Roaming](#rf-and-deployment-fundamentals) | A wireless client moving its association from one access point to another while using the network. |
| [Service set identifier (SSID)](#access-and-segmentation) | The name of a wireless network. Its configuration associates arriving clients with authentication and network access policies. |
| [Enterprise wireless authentication](#access-and-segmentation) | A Wi-Fi access model that verifies individual users or devices through an authentication service, commonly RADIUS. |
| [Network access control (NAC)](#access-and-segmentation) | A way to decide what connectivity a device receives using its identity, profile and applicable policy. |
| [Remote Authentication Dial-In User Service (RADIUS)](#access-and-segmentation) | A protocol used by network access equipment to consult a central authentication and authorization service and record accounting events. |
| [IEEE 802.1X port-based access control](#access-and-segmentation) | Port-based access control involving a supplicant, an authenticator such as a switch and an authentication server. |
| [Containment](#monitoring-threats-and-diagnostics) | Limiting the scope or ongoing effects of an incident, such as isolating the affected device under an approved response plan. |
| [Dynamic Host Configuration Protocol (DHCP)](#monitoring-threats-and-diagnostics) | The protocol clients use to obtain settings such as an IP address, gateway and DNS servers, typically for a bounded lease. |
| [Network address translation (NAT)](#monitoring-threats-and-diagnostics) | Rewriting source or destination addressing as traffic crosses a boundary. The translation and the permission to pass traffic are distinct decisions. |
| [Packet](#monitoring-threats-and-diagnostics) | A network-layer unit carrying a source and destination IP address. Routers use the destination and their forwarding tables to send it onward. |
| [Packet capture](#monitoring-threats-and-diagnostics) | An observation of traffic visible at a particular interface or tap. Position, direction and capture filters determine what it can show. |

**SD-WAN route readiness**

| Term or phrase | Meaning |
|---|---|
| [SD-WAN member](#4-sd-wan-route-readiness) | A network interface or connection made available to SD-WAN as a candidate path. |
| [Performance SLA](#4-sd-wan-route-readiness) | A measurement of member quality, such as latency or loss, that a steering rule can use to qualify paths. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Rollback](#resilient-branch-lan) | Returning a change to a known acceptable state when results do not meet defined conditions. A valid rollback also accounts for data changed in the meantime. |
| [East-west traffic](#secure-office-wi-fi) | Traffic among peer systems or workloads within an environment, such as a service calling its database. |
| [Software-defined WAN (SD-WAN)](#new-sd-wan-candidate-path) | A way to steer traffic among network connections according to policy and measured link conditions. |

## Places to learn

This is a selective starting set, not a complete list and not a prescription to consume everything. Choose the one exam route you intend to take, then use only resources that close measured gaps. Times are publisher-listed or planning estimates.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [NSE 5 Secure Networking track](https://training.fortinet.com/local/staticpage/view.php?page=nse_5_secure_networking) | Public | 20–30 min | Current prerequisites, eligible routes, validity, and renewal |
| [FortiSwitch exam page](https://training.fortinet.com/local/staticpage/view.php?page=fortiswitch_administrator_exam) | Public | 30–45 min | Exact 7.6 route contract and published topic checklist |
| [FortiSwitch 7.6 course](https://training.fortinet.com/local/staticpage/view.php?page=library_fortiswitch-administrator) | Free account; labs may cost | 12–20 hr estimate | Official route instruction and hands-on labs; verify displayed duration |
| [FortiSwitchOS 7.6.2 release notes](https://docs.fortinet.com/document/fortiswitch/7.6.2/fortiswitchos-administration-guide/35890/what-s-new-in-fortiswitchos-7-6-2) | Public | 15–30 hr selected | FortiLink/standalone, VLAN, STP, security, operations, CLI, and version-specific release details |
| [Secure Wireless LAN exam page](https://training.fortinet.com/local/staticpage/view.php?page=secure_wireless_lan_administrator_exam) | Public | 30–45 min | Exact current 7.6 route contract and topic checklist |
| [Secure Wireless LAN course](https://training.fortinet.com/local/staticpage/view.php?page=library_secure-wireless-lan-administrator) | Free account; labs may vary | 10–18 hr estimate | Official FortiAP/controller/FortiEdge Cloud preparation |
| [FortiAP/FortiWiFi 7.6 documentation](https://docs.fortinet.com/product/fortiap/7.6) | Public | 15–30 hr selected | RF, controller, AP profiles, access, monitoring, and diagnostics |
| [SD-WAN 7.6 Core Administrator exam](https://training.fortinet.com/local/staticpage/view.php?page=sd-wan_core_administrator_exam) | Public | 30–45 min | Current route contract and three weighted topic groups |
| [SD-WAN Core Operations course](https://training.fortinet.com/local/staticpage/view.php?page=library_sd-wan-core-operations-administrator) | Free account; labs/ILT may cost | 12 hr lecture+lab listed | Skills preparation for the current SD-WAN route |
| [FortiOS 7.6 SD-WAN documentation](https://docs.fortinet.com/sdwan) | Public | 10–20 hr selected | Members, SLA, routing, rules, sessions, design, and troubleshooting |
| [Fortinet exam release notices](https://helpdesk.training.fortinet.com/support/solutions/articles/73000659982-nse-exam-release-notices-new-and-discontinued-exams) | Public | 15–20 min | Releases and last-delivery dates before booking |
| [Fortinet YouTube](https://www.youtube.com/@Fortinet) | Free/YouTube | 4–10 hr selected | Official switching, wireless, and SD-WAN demonstrations; verify versions |
| Authorized FortiGate/FortiSwitch/FortiAP or SD-WAN lab | Entitlement/cost varies | 25–50 hr for one route | Required applied configuration, failure, evidence, rollback, and cleanup |

## Final preparation

- Confirm active NSE 4 and choose one currently eligible route; do not study all routes by default.
- Reopen that route's exam page and verify version, status, topic list, count, time, language, delivery, price, and policies.
- Complete official training and rebuild route labs from a clean authorized baseline with failures and rollback.
- Reject content marketed as real, recalled, leaked, or guaranteed-match questions.
