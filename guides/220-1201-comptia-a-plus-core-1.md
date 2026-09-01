---
exam_code: 220-1201
vendor_id: comptia
official_blueprint: https://www.comptia.org/en-us/certifications/a/core-1-v15/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-01
---

# 220-1201 CompTIA A+ Core 1 (V15) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#220-1201-coverage-record). The [official Core 1 V15 page](https://www.comptia.org/en-us/certifications/a/core-1-v15/) is authoritative.

**Current baseline:** A+ V15, Core 1 exam 220-1201; launched March 25, 2025<br>
**Version rule:** Core 1 and Core 2 must be passed from the same version; do not mix 1200- and 1100-series exams<br>
**Lifecycle watch:** No exact retirement date is announced. CompTIA says usually three years after launch and estimates 2028; verify before scheduling.<br>
**Official delivery snapshot:** Maximum 90 questions, including multiple-choice, drag-and-drop, and performance-based questions; 90 minutes; 675/900 passing score; English, German, and Japanese listed

## How to use this guide

Core 1 is the physical-and-connectivity half of A+: mobile devices, networking, hardware, virtualization/cloud, and evidence-led troubleshooting. Core 2 covers operating systems, security, software troubleshooting, and operational procedures. Real support incidents cross that boundary, but do not let older 220-1101/1102 resources define the V15 scope.

Build a safe bench using an old authorized PC or virtual substitute, a laptop/mobile device, a small router/access point, cables/adapters, and a printer if available. For each objective, be able to:

1. identify the component, connector, service, protocol, or symptom;
2. choose a compatible and safe implementation from requirements;
3. install/configure or accurately simulate it;
4. diagnose one failure using the CompTIA method;
5. verify complete function and document evidence.

Performance-based readiness means doing and explaining. Memorizing a port table without tracing a client → network → service path is fragile; building hardware without ESD, power, data protection, or verification is unsafe.

## Weighted objective map

| Domain | Weight | Readiness evidence |
|---|---:|---|
| 1. Mobile devices | 13% | Service laptop parts, displays, accessories, connectivity/synchronization, and common failures |
| 2. Networking | 23% | Map protocols/ports, devices, media, IP/DNS/DHCP, Wi-Fi, SOHO/cloud/IoT, tools, and paths |
| 3. Hardware | 25% | Select/install cables, RAM, storage, boards, CPUs, power, cooling, peripherals, printers, and custom-PC parts |
| 4. Virtualization and cloud computing | 11% | Compare VM/container/VDI and cloud models, then size and verify a basic virtual workload |
| 5. Hardware and network troubleshooting | 28% | Use a controlled method, tools, symptoms, and verification across devices, printers, hardware, and networks |

## 1. Mobile devices — 13%

### Laptop and mobile hardware

Laptop field-replaceable parts may include batteries, RAM, storage, keyboards, touchpads, speakers, cameras, microphones, wireless cards/antennas, and—in some designs—system boards or cooling. Begin with the service manual and exact model. Shut down, remove external power, handle lithium batteries safely, use ESD controls, track screws/cables, and do not assume a part that physically fits is electrically or firmware compatible.

Battery swelling, puncture, heat, smoke, odor, or leakage requires isolation and approved handling—not pressure, reuse, ordinary trash, or improvised repair. Firmware/BIOS and embedded-controller behavior can affect charging, docks, batteries, keyboards, displays, and thermal control.

LCD/OLED display assemblies can include panel, digitizer/touch layer, camera, microphone, Wi-Fi antennas, cables, hinges, sensors, and backlight-related parts. A dark screen can be power, brightness, output selection, cable, backlight/panel, GPU/driver, or sleep-state behavior. Test external display and illumination/output paths before replacing the panel.

### Accessories, networks, and synchronization

USB/USB-C, Thunderbolt, Bluetooth, NFC, docks, port replicators, stylus/headsets, external keyboards, storage, and hotspot/tethering have distinct power, data, display, distance, pairing, and compatibility needs. USB-C describes a connector, not guaranteed charging wattage, display alternate mode, Thunderbolt support, or maximum data rate. Check device, cable, charger, and dock as a chain.

Configure Wi-Fi, Bluetooth, cellular, hotspot, VPN, email/account synchronization, location, and application permissions with least privilege. Synchronization can propagate a deletion or unwanted change; confirm direction, account, scope, conflict behavior, network/power conditions, and backup before resetting.

Diagnose mobile symptoms by layer: power/charging/temperature, physical damage, radio state and signal, saved network/pairing, IP/account configuration, app/service, and policy/management. Protect user data and get authorization before factory reset.

> **Related item:** Mobile device management can enforce configuration and remote actions, but a Core 1 troubleshooting decision still needs to distinguish hardware, connectivity, account, application, and policy causes.

## 2. Networking — 23%

### Protocols, ports, and services

Know common default associations and what the traffic accomplishes, including FTP 20/21, SSH/SFTP 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, POP3 110, IMAP 143, SNMP 161/162, LDAP 389, HTTPS 443, SMB 445, RDP 3389, secure mail variants, and modern encrypted alternatives. A port number is a clue, not proof of application identity or safety; services can use nondefault ports and encryption/authentication matter.

TCP provides connection-oriented reliable ordered delivery; UDP reduces transport overhead and suits use cases that tolerate/handle loss or need low latency. IP routes packets, DNS resolves names, DHCP leases configuration, NTP aligns time, and SMB shares files/printers. Trace which dependency failed instead of treating “network” as one component.

### Devices, media, and configuration

A switch connects local Ethernet devices; router joins IP networks; firewall enforces policy; access point provides wireless attachment; modem/ONT terminates provider access; patch panel organizes fixed cabling; PoE supplies power over supported Ethernet; NIC provides the endpoint interface. Home gateways combine roles.

Copper Ethernet categories, coaxial, and fiber differ in connectors, reach, speed, interference, cost, and termination. Single-mode and multimode fiber have different optics/core/distance use. Inspect connector and cable specification rather than forcing or guessing. Cabling faults include opens, shorts, crossed/miswired pairs, poor termination, bend/damage, interference, and unsupported length/rate.

IPv4 and IPv6 are logical addressing systems. A subnet mask/prefix separates network and host portions; a default gateway reaches other networks. Private IPv4 ranges are not internet-routable directly. APIPA/link-local behavior signals missing configuration in some contexts. NAT translates addresses; port forwarding exposes a selected inbound service and increases risk. DNS server and address, gateway, and route information are separate settings.

### Wi-Fi, SOHO, IoT, and tools

Wireless standards/bands trade throughput, range, channel width, interference, compatibility, and congestion. Use current supported encryption, a strong unique administrative credential, safe firmware, a planned SSID/channel/band, guest/IoT separation, and disabled unnecessary exposure such as unsafe management or convenience features. WPA version and cipher support are compatibility and security decisions—verify current device support.

SOHO setup includes ISP handoff, WAN, LAN addressing/DHCP, DNS, NAT/firewall, Ethernet switching, AP settings, guest/IoT segmentation, VPN need, updates, backup/export, and tested wired/wireless clients. Cloud-managed and software-defined controls change the management plane, not basic packet dependencies.

Use a crimper/punchdown only with appropriate cable/connector and skill; cable tester for continuity/pinout; toner/probe for tracing; loopback plug for interface testing; Wi-Fi analyzer for channel/signal context; multimeter with training for electrical measurement. Built-in tools can display address/route/DNS, test reachability and names, and trace paths. Never probe networks without authorization.

> **Related item:** A packet walk—source application, DNS, source IP/prefix/gateway, link/AP/switch, router/firewall/NAT, destination transport/service, return path—is the most reusable network troubleshooting model.

## 3. Hardware — 25%

### Compatibility before installation

Translate workload into constraints: CPU architecture/socket/chipset, motherboard form factor and firmware, RAM generation/type/speed/capacity/channel and board/CPU support, storage interface/form factor/protocol, GPU slot/power/space/thermals, PSU capacity/connectors/quality, case dimensions, cooling, ports, peripherals, operating-system support, and budget. A compatibility list and manuals beat visual resemblance.

Firmware settings may control boot order, virtualization extensions, secure boot/TPM, storage modes, fan/thermal behavior, and device enablement. Record the baseline and change only what the requirement needs. Firmware updates carry power and compatibility risk; follow vendor instructions and recovery requirements.

### CPU, memory, storage, power, and cooling

Install a CPU without touching contacts or forcing orientation; use approved thermal-interface material and cooler pressure. RAM goes in supported slots/configurations and may run at a fallback speed. ECC, registered/unbuffered, laptop/desktop form factors, and generations are not interchangeable merely because capacity matches.

SATA HDD/SSD, M.2 SATA, and M.2 NVMe may share familiar form factors while using different protocols/keys/lanes. RAID combines drives for performance and/or availability depending on level; it is not a backup and controller/metadata failure matters. Partition/file-system/OS setup occurs after the hardware is detected.

Select a PSU for sustained component demand, transient headroom, efficiency/quality, connectors, form factor, and safety—not wattage label alone. A surge protector limits certain voltage events; a UPS provides temporary power and may condition power, but runtime/load/battery state matter. Never open a PSU. Cooling requires a complete airflow path, clean filters/heatsinks, correct fan/pump operation, good contact, and appropriate environment.

### Cables, peripherals, and specialized systems

Distinguish display/audio interfaces, USB generations/connectors, SATA/data/power, PCIe, Ethernet/fiber, and legacy connectors in scope. Confirm direction, protocol, resolution/rate, power, length, and adapter limitations. Adapters cannot create a signal or protocol the source does not provide.

Select specialized components by workload: gaming/graphics needs GPU/display/thermal emphasis; CAD/video may require CPU/GPU/RAM/fast storage and accurate displays; virtualization needs cores/RAM/storage/I/O and extension support; NAS emphasizes storage, RAID/network and backup; thin clients depend on network/remote services. Avoid oversimplified “more is always better.”

Printers differ in imaging process and consumables. Laser flow includes processing, charging, exposing, developing, transferring, fusing, and cleaning; inkjet uses ink/printheads; thermal uses heat-sensitive media or ribbon; impact strikes a ribbon. Installation includes physical setup, consumables, safe transport locks, connection/IP, driver or print language, queue/defaults, test page, sharing, security, and maintenance.

> **Related item:** Total cost of ownership includes energy, consumables, service life, support, downtime, and disposal, not just purchase price.

## 4. Virtualization and cloud computing — 11%

A type 1 hypervisor runs directly on hardware; type 2 runs above a host OS. A VM has virtual CPU, memory, storage, NICs, firmware/devices, and a guest OS. Containers share the host kernel more directly. Desktop virtualization/VDI presents a centrally hosted desktop or applications to endpoints. Virtualization provides isolation and flexibility but consumes physical resources and still requires patching, identity, network, storage, backup, and monitoring.

Before creating a VM, confirm CPU virtualization support/enabled firmware, RAM/storage capacity, network mode, image/license, and intended isolation. NAT, bridged/external, host-only/internal, and isolated virtual networks expose different paths. Snapshots/checkpoints are useful short-term state tools but are not automatically independent backups.

IaaS exposes infrastructure, PaaS a managed application platform, and SaaS a finished application. Public, private, community, and hybrid describe deployment/ownership patterns; on-demand, measured, elastic, pooled resources are common cloud traits. Shared responsibility shifts which party configures and secures each layer. Availability, internet dependency, data location, exit/portability, performance, subscription/consumption cost, identity, and backup remain customer decisions.

> **Related item:** High availability, backup, and disaster recovery solve different problems. A highly available wrong/deleted file still needs a protected recovery copy.

## 5. Hardware and network troubleshooting — 28%

Use the six-step method consistently: identify; establish probable-cause theory; test theory; plan and implement or escalate; verify full function and preventive measures; document. Consider change history, scope, user impact, safety, backups, and corporate policy. Start with simple high-probability checks but do not skip evidence.

### Symptom-to-layer reasoning

| Symptom | First evidence | Do not assume |
|---|---|---|
| No power | outlet/strip/UPS, cable, PSU switch, indicators, known-good safe supply | motherboard is dead |
| Power but no boot/POST | beep/LED code, display path, RAM/CPU/power seating, minimal config | OS reinstall will help |
| Random shutdown | temperature, fans/pump, dust, PSU/load, event logs, environment | malware is the only cause |
| Slow system | CPU/RAM/storage/network utilization, thermals, startup/processes, capacity/health | one component upgrade fixes all |
| Missing drive | power/data/slot, firmware detection, controller/mode, disk tools | initialize/format before protecting data |
| Artifacts/no display | cable/input/display, GPU/power/seat, driver, external test, thermals | panel or GPU alone |
| No network | link/radio, address/prefix/gateway, DHCP, DNS, route, policy, service | internet provider outage |
| Intermittent Wi-Fi | signal/channel/interference/roaming/power/client/AP/upstream | advertised speed guarantees throughput |
| Printer not printing | power/errors, local/network path, correct queue/default, spooler, paper/consumable | reinstall everything |

### Mobile, printer, and network failures

For charging, test outlet, adapter wattage/protocol, cable, dock, port debris/damage, battery health, firmware, and temperature. For swelling/heat, stop using the battery safely. For connectivity, test radio state, range/interference, pairing/saved profile, IP configuration, account/sync, and policy.

Printer symptoms map to process: faded output may be consumable, density, printhead/nozzle, or imaging component; repeating marks suggest a rotating component; smearing may indicate media/fuser/ink drying; jams require correct media/path/rollers and removal direction; garbled output may be driver/language/data. Follow safety instructions around heat, high voltage, toner, ink, and moving parts.

For wired/wireless networks, isolate one client versus many, one service/name versus all, wired versus wireless, and local versus upstream. Verify physical/link, configuration, gateway/local service, DNS, remote reachability, application port, firewall/VPN/proxy, then performance. Rebooting can be a controlled test or recovery, but it erases transient evidence and is not a root-cause explanation.

> **Related item:** A known-good substitution is powerful only when it is truly compatible and changes one variable. Label results so you do not create a second unknown.

## Integrated scenarios

### Scenario 1: Hybrid-work laptop and dock

A laptop charges intermittently, an external display is blank, and office Ethernet disconnects. Inventory charger/cable/dock/ports/display input/NIC path, check power and capability compatibility, test each function directly and through the dock, inspect drivers/firmware/events, then replace only the failed link. Verify charging under load, display resolution, wired network/DNS/VPN, and mobile synchronization after restart.

### Scenario 2: Small-office refresh

Translate five users, a printer, guest devices, IoT cameras, backups, and remote access into router/firewall/AP/switch/cabling, IP/DHCP/DNS, secure Wi-Fi, guest/IoT separation, printer queue, UPS and documentation. Test wired/wireless clients, name resolution, printing, isolation, authorized VPN, backup restore, and recovery from a saved configuration.

### Scenario 3: Custom virtualization workstation

Select compatible board/CPU/RAM/NVMe/GPU/PSU/cooling for two VMs and creative work. Assemble safely, record firmware, test POST/memory/storage/thermals, enable virtualization, create segmented VM networks, and measure resource pressure. Introduce one RAM-seating, DNS, or virtual-network error and diagnose without changing multiple layers.

## Hands-on labs

1. **Laptop/mobile inventory:** map serviceable parts, display components, radios, ports, charger/dock capabilities, synchronization, and safe reset/backup boundaries.
2. **Protocol path:** diagram and test DHCP, DNS, HTTPS, SMB, SSH/RDP or safe substitutes; explain ports, TCP/UDP, encryption, and failure symptoms.
3. **SOHO build:** configure an authorized router/AP with current encryption, admin security, addressing/DHCP/DNS, guest/IoT isolation, updates, and backup/export.
4. **Cable/tool bench:** identify/test safe copper cables and connectors; use a cable tester or simulator and document open/miswire/known-good results.
5. **PC build/upgrade:** use manuals to select/install RAM/storage or fully assemble an old PC; apply ESD/power safety and verify firmware/OS detection.
6. **Printer lifecycle:** install a printer/virtual queue, set driver/defaults, print test pages, clear a safe fault, and map symptoms to imaging stages.
7. **VM/cloud comparison:** create a small VM, test NAT versus isolated networking and snapshot limits, then map its responsibility against IaaS/PaaS/SaaS.
8. **Troubleshooting capstone:** diagnose five injected single faults, keep an evidence timeline, verify complete function/restart, and write prevention/escalation notes.

## Original knowledge checks

1. Why must Core 1 and Core 2 come from the same A+ version?
2. What safety evidence comes before replacing a laptop battery?
3. How can an external display distinguish panel-path from GPU/system failure?
4. Why does USB-C shape not guarantee display, charge, or data capability?
5. What can synchronization propagate that a backup could recover?
6. Distinguish TCP and UDP without calling one universally better.
7. What do DNS, DHCP, and NTP each provide?
8. Why is a default port only a clue?
9. Distinguish switch, router, firewall, AP, and modem/ONT.
10. What faults can a cable tester expose?
11. How do IP address, prefix, gateway, and DNS settings differ?
12. What risk does port forwarding introduce?
13. Which evidence separates DNS failure from total connectivity loss?
14. Why can stronger Wi-Fi signal still produce poor application performance?
15. Which compatibility checks precede a CPU/motherboard purchase?
16. Why can two same-capacity RAM modules be incompatible?
17. Distinguish M.2 form factor, SATA, NVMe, and PCIe.
18. Why is RAID not backup?
19. Which factors matter beyond PSU wattage?
20. Why must you never open a PSU?
21. What causes poor cooling despite spinning fans?
22. Why can an adapter fail even when both connectors fit?
23. Map repeated laser-printer marks to a useful theory.
24. Which printer setup evidence goes beyond “device detected”?
25. Compare type 1 and type 2 hypervisors.
26. Why is a VM snapshot not necessarily a backup?
27. How do NAT, bridged, and isolated VM networks change exposure?
28. What customer duties remain with SaaS?
29. Which evidence comes first for a no-power PC?
30. Why is reinstalling the OS weak response to no POST?
31. Which evidence separates thermal shutdown from PSU/load trouble?
32. What should happen before initializing a missing drive?
33. Trace “one website will not open” through the network layers.
34. What does a known-good substitution prove—and not prove?
35. Why should a technician avoid several simultaneous changes?
36. When should troubleshooting be escalated?
37. Which verification proves a dock repair is complete?
38. How would guest/IoT segmentation be tested?
39. Which artifacts make a PC build reproducible?
40. What exactly is announced about the 220-1201 retirement?

## Answers and reasoning

1. CompTIA prohibits mixing versions; pass 220-1201 and 220-1202 together.
2. Exact model/manual, shutdown/power isolation, condition/temperature, authorization, ESD and approved disposal path.
3. A known-good external output can show whether rendering/system works beyond the internal panel/cable/backlight path.
4. Connector form is separate from negotiated protocols, cable rating, source/dock capability, and power delivery.
5. Deletion, corruption, or unwanted change; an independent retained backup can restore earlier state.
6. TCP adds reliable ordered connection semantics; UDP lowers transport overhead and leaves more handling to the application.
7. Name resolution, leased network configuration, and time synchronization.
8. Services can move ports or tunnel traffic; validate process, protocol, encryption, and path.
9. Local forwarding, routing, policy, wireless access, and provider-link termination.
10. Opens, shorts, pinout/miswire/crossed pairs and sometimes length/performance context depending on tool.
11. Endpoint identity, local-network boundary, next-hop route, and name resolver.
12. It makes an internal service reachable inbound and expands attack/misconfiguration exposure.
13. IP reachability may work while name lookup fails; inspect resolver configuration/results separately.
14. Interference, contention, upstream congestion, DNS/service, device capability, and application latency still matter.
15. Socket, chipset, firmware support, power, cooler, form factor, RAM/PCIe needs and workload.
16. Generation, form factor, ECC/buffering, voltage, speed/timing, density and board/CPU support differ.
17. M.2 is a form factor/connector family; SATA/NVMe are protocols, and NVMe commonly uses PCIe lanes.
18. It can preserve availability/performance but mirrors deletion/corruption and shares system/controller/site risks.
19. Sustained/transient load, connectors/rails, efficiency/quality, form factor, protections and headroom.
20. Stored high voltage is hazardous even disconnected; replace through qualified procedures.
21. Dust/blockage, reversed/poor airflow, failed pump, bad contact/paste, undersized cooler or high ambient temperature.
22. It cannot create a protocol/signal or sufficient bandwidth/power absent at the source.
23. A rotating drum/roller/fuser component whose circumference matches the repeat interval; inspect safely.
24. Correct queue/driver/IP, configuration/permissions, test output, sharing/security and restart/reconnect behavior.
25. Type 1 runs on hardware; type 2 relies on a host OS.
26. It may share the datastore/failure domain and create consistency/dependency/performance issues.
27. NAT hides behind a host path, bridged joins an external LAN, and isolated restricts external connectivity.
28. Identity/access, data/configuration, endpoints, acceptable use, export/backup and vendor-risk choices.
29. Safe outlet/strip/UPS/cable/PSU-switch/indicator and known-good compatible power-path checks.
30. Firmware/POST occurs before the OS; find power/component/display evidence first.
31. Temperature/fan/pump/sensor/load evidence versus voltage, event, substitution and load correlation.
32. Protect data, check physical/firmware/controller/OS detection and determine whether the disk is expected/existing.
33. Link/address/gateway → DNS for name → route/policy → destination/port → browser/application/cache/account.
34. It implicates one changed compatible variable but does not explain root cause or rule out intermittent interactions.
35. It destroys causal attribution and may create new faults/security or data loss.
36. At authorization, safety, data, policy, access, expertise, cost or time boundaries.
37. Charge under load, external display, Ethernet/IP/DNS/VPN, peripherals, restart/reconnect and documented result.
38. Verify intended internet/services work and unauthorized cross-segment initiation is denied, using authorized test hosts.
39. Requirements, compatibility/manifests, manuals, connections/photos, firmware settings, test results, temperatures and changes.
40. No exact date; the page says usually three years after launch and estimates 2028.

## 220-1101-to-220-1201 gap checklist

Older Core 1 material can teach durable concepts, but compare it line by line with V15. Specifically verify current mobile accessories/repair boundaries, USB and Wi-Fi generations, modern CPU/RAM/storage/GPU/firmware, AI-era hardware and cloud/virtualization terminology, SOHO security, current ports/protocols, printer coverage, PBQ expectations, and every public troubleshooting symptom/tool. Never combine an 1101 pass with 1202.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one current V15 path, spend comparable time on a safe hardware/network bench, and use explanation-led practice only to target weak domains.

| Resource | Access | Estimated time |
|---|---|---:|
| CompTIA [CertMaster Learn](https://www.comptia.org/en-us/resources/certmaster-training/learn/), Labs, and Practice | Paid official platform; select 220-1201 product/bundle | About 35–70 hours across learning, labs, and remediation |
| [Pluralsight A+ Core 1 path](https://www.pluralsight.com/paths/comptia-a-core-1-220-1201) | Subscription; 6 courses and practice exam | 12 listed hours plus 20–40 lab/review hours |
| [LinkedIn Learning / Total Seminars Core 1](https://www.linkedin.com/learning/comptia-a-plus-core-1-220-1201-cert-prep) | Subscription; 21 quizzes | 20 hours 14 minutes plus 20–40 lab/review hours |
| [Complete A+ Guide V15](https://www.oreilly.com/library/view/complete-a-guide/9780135439883/) | O'Reilly/Pearson subscription book covering both cores | About 25–45 selected reading/lab hours for Core 1 |
| [Udemy / Jason Dion Core 1](https://www.udemy.com/course/comptia-a-core-1/) | Paid marketplace course and practice exam | 26 hours 5 minutes plus 20–40 lab/review hours |
| [MeasureUp Core 1](https://www.measureup.com/comptia-a-core-1-practice-test.html) | Paid; 242 questions listed | About 6–12 hours across timed attempts and explanation review |
| [Professor Messer free 220-1201 course](https://www.professormesser.com/free-a-plus-training/220-1201/220-1201-video/220-1201-training-course/) | Free 63-video course; optional paid notes/practice | 10 hours 11 minutes plus 20–40 hands-on hours |

Whizlabs was not independently verified as an exact current 220-1201 source. Reject “actual questions” and dump sites. Vendor runtimes, prices, bundles, banks, revisions, and access change; verify before purchase.

## Source and freshness notes

- The CompTIA page controls V15 weights, delivery, languages, score, same-version rule, and estimated lifecycle.
- Hardware standards, connectors, ports/protocols, Wi-Fi/security, product compatibility, and cloud behavior change. Use current manuals and standards/product documentation during hands-on work.
- This guide contains original scenarios, labs, checks, and explanations derived from public scope; it does not copy proprietary objectives, PBQs, course labs, or exam items.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.
