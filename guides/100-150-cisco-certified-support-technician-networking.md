---
exam_code: 100-150
vendor_id: cisco
official_blueprint: https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-networking.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Cisco Certified Support Technician Networking (100-150) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#100-150-coverage-record). Cisco's [exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-networking.html) and [exam-topics page](https://learningnetwork.cisco.com/s/ccst-networking-exam-topics) are authoritative.

**Current baseline:** Active 100-150 CCST Networking exam; six public topic groups and Cisco's current exam-aligned training objectives, checked September 2, 2026<br>
**Scheduled change:** None announced on the checked official pages<br>
**Official source:** [100-150 exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-networking.html) · [exam topics](https://learningnetwork.cisco.com/s/ccst-networking-exam-topics) · [training overview](https://www.cisco.com/c/dam/en_us/training-events/training/courses/ccst-networking.pdf)

## How to use this guide

Treat networking as a packet-delivery story: application need → name and address → local medium → switch → default gateway/router → remote path → destination service → return path. At each step, identify the device, protocol, addressing information, observable evidence, likely failure, and safest next diagnostic action. Memorizing labels without being able to trace a packet is not enough.

Cisco currently lists a 50-minute exam costing USD 125 and offered in English, Arabic, Chinese, Spanish, French, Japanese, and Portuguese. The [CCST FAQ](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/support-technician/faq.html) describes CCST as an entry-level, lifetime certification and the free self-paced Network Technician Career Path as about 70 hours. Recheck price, delivery, language, and badge policy before booking.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the published objectives.

## Objective map

Cisco's public exam-topics interface names six groups but does not expose stable weights in the checked server-rendered page. This guide does not invent them. Allocate time from diagnostic evidence: start evenly, then spend more on areas where you cannot produce the listed proof.

| Topic group | Proof that you understand it |
|---|---|
| Standards and concepts | Trace encapsulation and distinguish network types, performance terms, applications, transports, and services |
| Addressing and subnet formats | Classify IPv4/IPv6 addresses and determine whether two endpoints are local or require a gateway |
| Endpoints and media types | Select and inspect endpoint, copper, fiber, wireless, connector, and interface choices |
| Infrastructure | Explain what switches, routers, access points, firewalls, services, and cloud/on-premises components do |
| Diagnosing problems | Follow a documented method, gather command/capture evidence, isolate a layer, test, and record the result |
| Security | Apply foundational confidentiality, integrity, availability, access, firewall, update, and WPA protections |

---

## 1. Standards and concepts

### Models are troubleshooting maps

The OSI model separates physical, data-link, network, transport, session, presentation, and application responsibilities. The TCP/IP model commonly groups these into link/network-access, internet, transport, and application layers. Use either model to ask a practical question:

- **Physical:** Is the interface powered, enabled, correctly cabled, and receiving a usable signal?
- **Data link:** Are Ethernet frames, MAC addresses, VLAN membership, and local switching correct?
- **Network:** Do IP address, prefix, gateway, and routing decisions place packets on a viable path?
- **Transport:** Is the application using TCP or UDP and the expected port? Is a firewall permitting it?
- **Application:** Does DNS resolve, and does the actual service respond correctly?

Encapsulation adds information as data moves down the stack: application data becomes a TCP segment or UDP datagram, an IP packet, then a frame and bits/signals. The receiver removes those wrappers. A switch normally forwards using MAC-address information inside a local Layer 2 domain; a router forwards IP packets between networks.

**Related item:** A protocol data unit's name helps locate evidence. Wireshark may show frame, packet, TCP/UDP, and application fields in one capture; those are nested views of the same communication, not four unrelated transmissions.

### Performance terms

- **Bandwidth** is a path's theoretical or provisioned capacity.
- **Throughput** is useful data transferred per unit of time.
- **Goodput** excludes protocol overhead and retransmitted data.
- **Latency** is delay; round-trip time includes travel out and back.
- **Jitter** is variation in delay and matters to voice/video.
- **Packet loss** forces recovery or reduces real-time quality.

A 1-Gbps access link does not guarantee 1-Gbps application throughput. A slower upstream link, contention, wireless interference, server limits, TCP behavior, encryption, loss, or latency can constrain the end-to-end result. Always measure at the appropriate point and time.

### Network types, layouts, and delivery models

LAN and WLAN serve a local area; PAN connects a person's nearby devices; CAN commonly spans a campus; MAN spans a metropolitan area; WAN joins geographically separated sites. A physical topology describes cables/radios and devices; a logical topology describes traffic relationships. Star layouts centralize access, while mesh adds alternate paths at greater cost and complexity.

On-premises hosting gives an organization direct responsibility for facilities and equipment. Cloud services shift defined responsibilities to a provider but do not remove customer responsibility for identities, data, configuration, endpoints, and service use. Hybrid designs join both. The correct choice follows latency, connectivity, control, scale, security, recovery, and cost requirements.

### Applications, transports, and ports

TCP is connection-oriented and provides ordered, acknowledged delivery; UDP has lower transport overhead and no built-in delivery/order guarantee. Applications choose according to their behavior—do not call UDP inherently unreliable at the application level, because an application can add its own recovery.

Know the purpose and usual transport/port for foundational services:

| Service | Common port(s) | Purpose and evidence |
|---|---:|---|
| DNS | UDP/TCP 53 | Translate names and addresses; inspect query, answer, and chosen server |
| DHCPv4 | UDP 67/68 | Lease address, mask, gateway, and DNS information |
| HTTP / HTTPS | TCP 80 / 443 | Web traffic; HTTPS protects the session with TLS |
| SSH / Telnet | TCP 22 / 23 | Secure versus clear-text remote terminal access |
| FTP / SFTP / TFTP | TCP 20/21 / TCP 22 / UDP 69 | Different file-transfer designs and security properties |
| SMTP / POP3 / IMAP | TCP 25 / 110 / 143 | Mail transfer and mailbox access; secure variants may use other ports |
| NTP | UDP 123 | Time synchronization, essential to trustworthy logs |
| SNMP | UDP 161/162 | Polling/management and traps/informs |

Port numbers identify application endpoints, not physical switch ports. A socket is commonly described by protocol plus IP address plus transport port.

---

## 2. Addressing and subnet formats

### IPv4 decisions

An IPv4 address is 32 bits shown as four decimal octets. A prefix length such as `/24` says how many leading bits identify the network. A subnet mask is another representation: `/24` equals `255.255.255.0`; `/25` equals `255.255.255.128`; `/26` equals `255.255.255.192`; `/27` equals `255.255.255.224`; `/28` equals `255.255.255.240`.

For an ordinary subnet, the network address has all host bits zero and the broadcast address has all host bits one. To decide whether a destination is local, apply the mask to both addresses. If the resulting network IDs match, use local Layer 2 delivery; otherwise send toward the default gateway.

Private IPv4 ranges are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`. They are not publicly routed on the Internet; NAT/PAT commonly translates between inside private addressing and public connectivity. `127.0.0.0/8` is loopback. A Windows self-assigned `169.254.x.x` address is strong evidence that normal DHCP configuration may have failed, but confirm intended design before changing anything.

Example: `192.168.10.70/26` uses blocks of 64. It belongs to network `192.168.10.64`; the broadcast is `.127`, and the ordinary usable range is `.65`–`.126`. A host `192.168.10.120/26` is local; `192.168.10.130/26` is in the next subnet and requires routing.

**Related item:** Class A/B/C language still appears in foundational material, but modern routing and allocation use classless prefixes. Prefer CIDR reasoning over assuming a mask from the first octet.

### IPv6 recognition

IPv6 addresses are 128 bits, written as eight hexadecimal groups. Leading zeros in a group may be omitted, and one run of all-zero groups may be compressed with `::`. Expand before comparing if compression makes the prefix unclear.

Recognize these anchors:

- `::1` is loopback; `::` is unspecified.
- `fe80::/10` is link-local and does not cross routers.
- `2000::/3` covers global unicast space.
- `ff00::/8` is multicast; IPv6 does not use broadcast.
- A `/64` is the normal LAN prefix size for many IPv6 designs.

The prefix identifies the network portion. The default gateway is still a routing decision, and an IPv6 host can have multiple addresses. Do not diagnose solely from the presence of a link-local address.

### Address assignment and supporting resolution

Static configuration is deliberate and persistent; DHCP provides leases dynamically. A usable host configuration normally needs address, prefix/mask, default gateway for remote networks, and DNS resolver information. ARP maps a local IPv4 next-hop address to a MAC address. IPv6 Neighbor Discovery performs related discovery and reachability work using ICMPv6.

When a user says “the Internet is down,” separate:

1. Does the interface have an expected address and prefix?
2. Can it reach its own gateway by IP?
3. Can it reach a remote IP?
4. Can DNS resolve the desired name?
5. Can the application reach its service and port?

That order distinguishes local, routed, naming, and application failures.

---

## 3. Endpoints and media types

Endpoints include workstations, phones, printers, servers, cameras, sensors, and mobile devices. They differ in interface type, power, operating system, address method, mobility, and security capability. Document the expected network and policy before connecting one.

### Copper, fiber, and radio

Twisted-pair copper Ethernet commonly uses an eight-position modular connector often called RJ-45. Category, negotiated speed, maximum supported distance, termination, electromagnetic interference, and damage matter. Fiber uses light, supports longer distance and electrical isolation, and may be single-mode or multimode; transceiver type, wavelength, connector, polarity, and cleanliness must match.

Wi-Fi uses radio and a shared medium. Signal strength alone is not quality: interference, channel use, client density, band, distance, obstacles, authentication, and backhaul capacity all matter. Cellular access depends on carrier radio coverage and service. Wired access usually offers stable dedicated link characteristics but limits mobility.

Patch panels organize permanent cabling; patch cables join panels, switches, and endpoints. A console connection is for device management, not user data forwarding. Ethernet switch ports, router interfaces, SFP/SFP+ transceiver cages, USB, serial/console, and power connectors serve different purposes. Read the diagram and labels before inserting a cable.

### Endpoint evidence

Useful read-only commands include:

| Platform | Address/interface | Reachability/path | Name and connection evidence |
|---|---|---|---|
| Windows | `ipconfig /all` | `ping`, `tracert` | `nslookup`, `netstat -ano` |
| Linux | `ip address`, `ip route` | `ping`, `tracepath` or `traceroute` | `dig`/`nslookup`, `ss -tupn` |
| macOS | Network settings, `ifconfig`, `route -n get default` | `ping`, `traceroute` | `dig`, `netstat`/`lsof` |

Android and iOS settings show SSID, IP details, privacy address behavior, and cellular/Wi-Fi state. Exact labels vary by release. Record outputs and timestamps; do not paste secrets or personal data into tickets.

Interface LEDs are model-specific evidence. A dark LED might mean no power, disabled interface, bad cable, inactive peer, or model-specific behavior. Color and blink rate can represent link, speed, activity, PoE, faults, or boot state—use the device documentation rather than guessing.

---

## 4. Infrastructure

A **hub** repeats signals and shares a collision domain. A **Layer 2 switch** learns source MAC addresses and forwards frames by destination MAC within VLANs. A **router/Layer 3 switch** selects paths between IP networks. An **access point** bridges wireless clients into a network. A **firewall** permits or denies traffic using policy and state; it does not automatically make every permitted application safe. A **modem/ONT** converts provider access signaling, while a home gateway may combine routing, switching, wireless, NAT, DHCP, DNS forwarding, and firewall functions.

### Switching and routing basics

When a switch receives a frame, it learns the source MAC on the incoming port. If the destination is known, it forwards toward that port; an unknown unicast or broadcast is flooded within the relevant broadcast domain, not across a router by default. VLANs create separate logical Layer 2 domains on shared switching hardware.

A host sends remote traffic to its default gateway's local MAC address while retaining the remote destination IP. The router removes the incoming frame, consults its routing table, decrements the IPv4 TTL or IPv6 hop limit, and builds a new frame for the next link. Each hop changes link-layer addressing; end-to-end IP addressing normally remains unless translation occurs.

**Related item:** A routing table chooses the most specific matching prefix, then uses route preference/metric rules. CCST requires basic routing reasoning; detailed dynamic-routing configuration belongs later in CCNA-level study.

### Safe Cisco device inspection

Console provides local out-of-band-style access; SSH provides encrypted remote CLI access; Telnet is clear text and should not be selected when SSH is available. Web interfaces, controllers, APIs, and network-management platforms are other access/data methods. Use authorized credentials and start with observation.

Common read-only Cisco IOS-style commands include:

- `show interfaces status` and `show interfaces` for link, state, counters, errors, speed, and duplex;
- `show ip interface brief` for interface/address/status summary;
- `show mac address-table` for learned MAC locations;
- `show arp` for IPv4 neighbor mappings;
- `show ip route` for known IPv4 routes;
- `show running-config` only when authorized, because output can expose sensitive configuration.

Interpret evidence together. “Administratively down” differs from a physical down state. Increasing CRC/input errors suggests a different path than a valid link with no route. A learned MAC on the wrong port may indicate topology/documentation or cabling issues.

---

## 5. Diagnosing problems

Use a repeatable method:

1. Define impact, scope, expected state, start time, recent change, and reproduction steps.
2. Gather endpoint, link, address, gateway, DNS, path, service, device, and log evidence.
3. Form the narrowest testable hypothesis.
4. Plan a safe test and rollback; obtain authorization for changes.
5. Change one controlled variable or run a non-mutating test.
6. Observe whether the result supports the hypothesis.
7. Escalate with evidence when ownership, privilege, risk, or complexity exceeds your role.
8. Restore service, validate with the user/monitoring, and document cause, action, evidence, and prevention.

Do not reboot or replace components before collecting volatile evidence unless safety or an approved restoration procedure requires it. Correlation is not cause: a recent change is a lead to test.

### Diagnostic tools

- `ping` tests ICMP reachability and timing when ICMP is allowed; a failed ping does not prove the target is down.
- `tracert`/`traceroute` reveals responding hops and where responses cease; filtering and asymmetric paths affect interpretation.
- `ipconfig`, `ip`, `ifconfig`, and route tools reveal local configuration.
- `nslookup`/`dig` tests DNS independently of the application.
- `netstat`/`ss` shows listeners and connections.
- Wireshark captures frames for authorized interfaces. Apply a narrow capture/display filter, reproduce once, record time, and protect credentials/content.

A three-way TCP handshake is SYN → SYN/ACK → ACK. Repeated SYNs without SYN/ACK point toward path, policy, service, or return-path trouble; a reset is different evidence. DNS query with no response differs from a valid “name does not exist” response.

Tickets should record asset/user, time zone, impact/scope, symptoms, expected versus actual state, topology/context, sanitized outputs, tests, changes/approvals, result, next owner, and closure validation. A concise timeline is more useful than “network fixed.”

---

## 6. Security

Confidentiality limits disclosure, integrity protects correctness, and availability keeps authorized services usable. Authentication establishes identity; authorization controls allowed action; accounting/auditing records activity. Least privilege, unique identities, multifactor authentication, secure defaults, updates, backups, segmentation, and logging reduce risk in different ways.

Firewalls filter by properties such as addresses, protocols, ports, direction, zone, application, and connection state. “Allow HTTPS” means permitting TCP 443 under a policy; it does not validate the site's legitimacy or content. Default-deny boundaries require explicit justified access.

Prefer WPA3 where supported or WPA2 with AES when compatibility requires it; avoid deprecated WEP and weak shared secrets. Change vendor-default administrator credentials, use a long unique passphrase, update firmware, separate guest/untrusted devices, disable unnecessary remote administration and insecure convenience features, and document recovery access. Enterprise wireless may use individual identities and centralized AAA instead of one shared key.

Social engineering, phishing, malware, password attacks, unpatched vulnerabilities, misconfiguration, rogue access, eavesdropping, and denial of service can affect a network. A support technician should preserve evidence, follow incident procedures, and escalate—not investigate beyond authorization or upload captures/configurations to unapproved services.

---

## Integrated scenarios

### Scenario 1: One user cannot reach an internal site

Confirm whether other users and sites work. Inspect link and IP configuration, then test loopback, own address, gateway, internal server IP, DNS resolution, and TCP service in that order. If IP works but name fails, capture resolver/server/error evidence. If the gateway fails, inspect local VLAN, Wi-Fi association, cabling, DHCP, and neighbor evidence. Document every comparison before escalation.

### Scenario 2: A meeting room has intermittent video

Separate reachability from quality. Record time, clients, SSID, band/channel, signal, loss, latency, jitter, link rate, utilization, and whether wired comparison improves the call. Check interference/client density and upstream constraints; do not conclude “low bandwidth” from one speed test. Propose the least disruptive authorized correction and validate under similar load.

### Scenario 3: A new printer works locally but not from another subnet

Confirm its address, mask, gateway, VLAN, DHCP reservation/static plan, and local reachability. Compare a working printer. If same-subnet clients succeed but remote clients fail, inspect gateway/routing/firewall policy rather than repeatedly changing cabling. Confirm the print service port and return path, then document the final configuration and access boundary.

---

## Hands-on evidence labs

Use only equipment, simulations, accounts, and traffic you own or are authorized to inspect.

1. **Packet journey:** In Packet Tracer or a home lab, draw an endpoint-switch-router-server path. Label source/destination MAC and IP at each routed link and explain every change.
2. **Subnet proof:** Create `/24` through `/28` examples. For ten random addresses, calculate mask, network, broadcast, usable range, and local/remote decision; verify with a calculator only afterward.
3. **Dual-stack inventory:** Record sanitized IPv4/IPv6 addresses, prefixes, gateways, DNS servers, and interface state on Windows or Linux. Explain every field without changing it.
4. **Service ladder:** Test gateway IP, remote IP, DNS name, and HTTPS. Save timestamped results showing how each test narrows the failure domain.
5. **Packet capture:** Capture your own DNS lookup and HTTPS TCP handshake. Identify Ethernet, IP, UDP/TCP, DNS, SYN/SYN-ACK/ACK, and encrypted application payload boundaries.
6. **Switch evidence:** In Packet Tracer or authorized IOS equipment, generate traffic and correlate interface state, counters, MAC table, ARP table, and route output with the diagram.
7. **Wi-Fi hardening review:** On a router you control, inventory firmware, administrator access, security mode, passphrase policy, guest isolation, remote management, and backup/recovery. Plan before changing and preserve rollback.
8. **Trouble ticket:** Introduce one safe fault in a disposable topology. Have another learner diagnose it using the eight-step method, then grade the evidence, communication, rollback, validation, and documentation—not just the fix.

## Readiness checks

Answer in your own words and produce evidence where requested.

1. How does bandwidth differ from throughput, goodput, latency, jitter, and loss?
2. Trace encapsulation from an HTTPS application to transmitted bits.
3. What does a switch learn from the source MAC, and how does it handle an unknown destination?
4. When does a host use its default gateway?
5. Compare LAN, WLAN, PAN, CAN, MAN, and WAN using one real example each.
6. Compare on-premises, cloud, and hybrid responsibility without saying cloud removes customer responsibility.
7. When would an application favor TCP, and when might it favor UDP?
8. Match DNS, DHCP, HTTP(S), SSH, Telnet, NTP, SNMP, and file-transfer protocols to purpose and common port.
9. Convert `/25`, `/26`, `/27`, and `/28` to masks.
10. For `10.20.30.141/27`, determine network, broadcast, and ordinary usable range.
11. List all RFC 1918 ranges and explain why private does not mean secure.
12. What evidence does a `169.254.x.x` address provide, and what does it not prove?
13. Expand and classify `fe80::21a:2bff:fe3c:4d5e`.
14. Why can an IPv6 host have link-local and global addresses simultaneously?
15. Distinguish ARP, Neighbor Discovery, DHCP, DNS, and NAT.
16. Select copper, multimode fiber, single-mode fiber, or Wi-Fi for four justified scenarios.
17. Why are connector shape, transceiver type, wavelength, polarity, and cleanliness separate checks?
18. What can an interface LED suggest, and why must you consult model documentation?
19. Gather address, route, DNS, and active-connection evidence on your operating system.
20. Explain a hub, switch, router, access point, firewall, modem/ONT, and multifunction home gateway.
21. What happens to MAC and IP addressing as a packet crosses a router?
22. Why are VLAN and IP subnet related but not identical concepts?
23. Interpret `up/up`, physical down, and administratively down as different starting points.
24. Which Cisco `show` outputs would you collect for a suspected local link issue, and why?
25. Compare console, SSH, Telnet, web, API, and controller access from function and security perspectives.
26. Apply the eight-step troubleshooting method to “the network is slow.”
27. How do you distinguish a DNS failure from IP-path failure?
28. What do repeated SYNs, a reset, and a completed handshake each suggest?
29. Why might traceroute stop even when the final application works?
30. Design a narrow authorized Wireshark capture that minimizes sensitive data.
31. Write a useful ticket timeline for an intermittent wireless incident.
32. Distinguish authentication, authorization, accounting, confidentiality, integrity, and availability.
33. Why does permitting TCP 443 not make all resulting traffic trustworthy?
34. Build a defensible home Wi-Fi baseline with recovery and rollback.
35. When should an entry-level technician escalate rather than continue testing?
36. Given an unfamiliar scenario, can you state expected state, evidence, hypothesis, safe test, result, and next action?

### Check key

Strong answers explain mechanism and limits. Calculations show binary/prefix reasoning, not only a calculator result. Diagnostics compare expected with actual state and preserve timestamps. Security answers name authorization, evidence handling, least privilege, rollback, and escalation. If an answer jumps directly from symptom to fix, redo it using the packet-delivery story.

---

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick the explanation, lab environment, book, or assessment that works for you; keep Cisco's live topics as the scope authority. Durations are page values where published and otherwise transparent reading/practice estimates, not promises.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [Cisco exam page and exam topics](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-networking.html) | Public | 30–60 min | Establish current identity, logistics, and scope before and after study |
| [Cisco Network Technician Career Path](https://www.netacad.com/career-paths/network-technician?courseLang=en-US) | Free account | About 70 h | Primary first-party path; four-course breakdown is 22 h + 22 h + 14 h + 12 h |
| [Cisco course objectives and outline](https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/ccst-networking.html) | Public | 20–40 min | Build a checklist against Cisco's exam-aligned training outcomes |
| [Cisco Packet Tracer introduction](https://www.cisco.com/site/us/en/learn/training-certifications/training/netacad/index.html) | Free account | About 2 h plus labs | Learn the simulator, then repeat this guide's labs; availability/account terms vary |
| [Cisco Press Official Cert Guide on O'Reilly](https://www.oreilly.com/library/view/cisco-certified-support/9780138213459/) | Paid | About 17 h 44 min reading estimate plus practice | Detailed 2023 approved guide, Pearson Test Prep and video mentoring; check its update program against live topics |
| [Sybex CCST Networking Study Guide on O'Reilly](https://www.oreilly.com/library/view/ccst-cisco-certified/9781394205806/) | Paid | About 12 h 25 min reading estimate plus practice | Alternative structured explanation and test-bank access; verify current objectives |
| [CCST Networking Certification Prep Course](https://www.udemy.com/course/cisco-ccst-100-150-certification-lab-training-2024/) | Paid | 5 h 14 min video plus 4–8 h labs/review | Current 2026 lecture/lab option; catalog details and quality can change |
| This guide's eight labs and 36 checks | Public | 12–20 h | Convert recognition into explainable, reproducible evidence |

Practice questions are useful only when they explain reasoning and reveal gaps. Avoid recalled/live exam items, “actual questions,” answer-only banks, and guarantees. Cisco U./NetAcad assessments and the companion Pearson/Sybex practice included with legitimately purchased books are preferable starting points; compare every disputed explanation with first-party training or product documentation.
