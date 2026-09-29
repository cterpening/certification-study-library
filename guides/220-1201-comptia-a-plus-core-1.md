---
exam_code: 220-1201
vendor_id: comptia
official_blueprint: https://www.comptia.org/en-us/certifications/a/core-1-v15/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-28
---

# 220-1201 CompTIA A+ Core 1 (V15) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#220-1201-coverage-record). The [official Core 1 V15 page](https://www.comptia.org/en-us/certifications/a/core-1-v15/) is authoritative.

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

The current exam page has **15 summary topic rows**. The publicly linked [220-1201 V15 objectives document, version 4.0](https://lecbyo.files.cmp.optimizely.com/download/34be017cb73211ef8985a6f347fbf652?checkExpiry=false) supplies **27 numbered objectives** with detailed bullets. It is available through [CompTIA’s resource portal](https://www.comptia.org/en-us/partner-portal/partner-resources/). Document version 4.0 is not a different exam from V15.

| Published objective IDs | Where to concentrate |
|---|---|
| 1.1–1.3 | Mobile hardware, accessories/connectivity and application/network support |
| 2.1–2.3 | Ports/protocols, wireless technologies and networked-host services |
| 2.4–2.6 | DNS/DHCP/VLAN/VPN concepts, network hardware and SOHO addressing |
| 2.7–2.8 | Internet/network types and diagnostic tools |
| 3.1–3.3 | Display attributes, cables/connectors and RAM |
| 3.4–3.6 | Storage/RAID, boards/CPUs/expansion and power supplies |
| 3.7–3.8 | Printer deployment/settings and maintenance |
| 4.1–4.2 | Virtualization and cloud concepts |
| 5.1–5.6 | Troubleshooting compute/power, storage/RAID, displays, mobile devices, networks and printers |

The full document explicitly says the **formal troubleshooting methodology is not tested as an objective in the 1200 series**. The practical troubleshooting tasks in domain 5 remain heavily weighted. Use a method to organize evidence and work safely; do not turn memorizing a numbered sequence into a claim about exam scope.

## 1. Mobile devices — 13%

### Laptop and mobile hardware

Laptop field-replaceable parts may include batteries, RAM, storage, keyboards, touchpads, speakers, cameras, microphones, wireless cards/antennas, and—in some designs—system boards or cooling. Begin with the service manual and exact model. Shut down, remove external power, handle lithium batteries safely, use ESD controls, track screws/cables, and do not assume a part that physically fits is electrically or firmware compatible.

Battery swelling, puncture, heat, smoke, odor or leakage requires stopping use and following the manufacturer’s safety/support procedure. The [Dell battery-handling document](https://dl.dell.com/topicspdf/swollenbattery-3_en-us.pdf) warns against pressure, puncturing, bending, prying or reinstalling a swollen pack. If it is stuck, obtain qualified help rather than forcing it free. Do not generalize a normal service-manual discharge step to a hot, smoking or otherwise actively failing battery. Firmware/BIOS and embedded-controller behavior can affect charging, docks, batteries, keyboards, displays, and thermal control.

LCD/OLED display assemblies can include panel, digitizer/touch layer, camera, microphone, Wi-Fi antennas, cables, hinges, sensors, and backlight-related parts. A dark screen can be power, brightness, output selection, cable, backlight/panel, GPU/driver, or sleep-state behavior. Test external display and illumination/output paths before replacing the panel.

### Accessories, networks, and synchronization

USB/USB-C, Thunderbolt, Bluetooth, NFC, docks, port replicators, stylus/headsets, external keyboards, storage, and hotspot/tethering have distinct power, data, display, distance, pairing, and compatibility needs. USB-C describes a connector, not guaranteed charging wattage, display alternate mode, Thunderbolt support, or maximum data rate. Check device, cable, charger and dock as a chain. The [USB-IF capability guidance](https://www.usb.org/sites/default/files/usb_type-c_language_product_and_packaging_guidelines_20230320.pdf) separates the connector, data protocol and USB Power Delivery. A USB 2.0 Type-C cable can carry power yet lack the high-speed/display signal paths a dock needs. A higher wattage printed on a charger does not prove that the laptop, cable and dock negotiate the required power profile.

| Symptom | Controlled comparison | What the result can show |
|---|---|---|
| Charging works, display does not | Use a documented display-capable cable/path and the correct monitor input | Power and display capabilities are independent |
| Display works directly but fails through the dock | Keep laptop/display fixed; check dock power, cable and supported mode | Narrows the failure to the added path; does not identify one component by itself |
| Battery drains under workload while connected | Compare negotiated supply and documented dock/laptop demand | Connected is not the same as adequate sustained charging |

Distinguish a physical SIM from an eSIM profile, the subscription from the radio, and radio availability from mobile-data authorization. Data caps and roaming policy can affect synchronization even when signal is present. Corporate-owned and BYOD devices can have different MDM application, permission and reset policies.

Configure Wi-Fi, Bluetooth, cellular, hotspot, VPN, email/account synchronization, location, and application permissions with least privilege. Synchronization can propagate a deletion or unwanted change; confirm direction, account, scope, conflict behavior, network/power conditions, and backup before resetting.

Diagnose mobile symptoms by layer: power/charging/temperature, physical damage, radio state and signal, saved network/pairing, IP/account configuration, app/service, and policy/management. Protect user data and get authorization before factory reset.

> **Related item:** Mobile device management can enforce configuration and remote actions, but a Core 1 troubleshooting decision still needs to distinguish hardware, connectivity, account, application, and policy causes.

## 2. Networking — 23%

### Protocols, ports, and services

The following covers the named ports in objective 2.1. The [IANA service/port registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv) is an assignment reference; a registered transport/number is not proof of what an observed application actually uses.

| Port | Common association | Diagnostic distinction |
|---:|---|---|
| 20 / 21 | FTP default data / control | Control reachability does not prove the separate data path works |
| 22 | SSH; SFTP runs over SSH | SFTP and FTP are different protocols |
| 23 | Telnet | Does not supply SSH’s encrypted remote-session protection |
| 25 | SMTP | Mail transport; not a mailbox-reading protocol |
| 53 | DNS | Uses both UDP and TCP; a UDP-only assumption can miss failures |
| 67 / 68 | DHCPv4 server / client | Lease/configuration exchange, commonly over UDP |
| 80 | HTTP | Web application traffic; a successful TCP connection is not a successful page |
| 110 / 143 | POP3 / IMAP | Mailbox access protocols with different synchronization behavior |
| 137 / 138 / 139 | NetBIOS name / datagram / session services | Legacy name/session functions; direct SMB uses 445 |
| 389 | LDAP | Directory queries/binds; connection alone does not prove authorization |
| 443 | HTTPS | Secure web transport still requires certificate/identity and application checks |
| 445 | SMB | File/print sharing depends on both path and permissions |
| 3389 | RDP | Remote desktop needs service, policy and authorized credentials |

Services can use nondefault ports. Treat a port number as a hypothesis to verify. NTP, SNMP and secure-mail variants are useful supporting context; do not replace the current objective list with an older or longer generic table.

TCP provides connection-oriented reliable ordered delivery; UDP reduces transport overhead and suits use cases that tolerate/handle loss or need low latency. IP routes packets, DNS resolves names, DHCP leases configuration, NTP aligns time, and SMB shares files/printers. Trace which dependency failed instead of treating “network” as one component.

### DNS, DHCP and host services

| DNS record | Purpose | Illustrative value or decision |
|---|---|---|
| A | Name to IPv4 address | `app.example.test` → `192.0.2.20` |
| AAAA | Name to IPv6 address | `app.example.test` → `2001:db8::20` |
| CNAME | Alias to another DNS name | `help.example.test` → `app.example.test` |
| MX | Mail exchanger and preference | Domain mail routing, not the mailbox password |
| TXT | Text used by a defined consuming protocol | Verification or email-authentication data, not executable code |

The [DNS record reference](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records) explains these data structures. The example names/addresses are documentation values, not a live deployment. DNS records supply information; they do not open firewall ports, serve pages or grant file permissions.

For the email terms in objective 2.4, SPF authorizes sending sources for an envelope domain; DKIM signs selected message content using a domain key; DMARC evaluates alignment with the visible From domain and publishes policy/reporting. A valid signature or SPF result alone is not the same as aligned DMARC success, and an authenticated message can still contain harmful content. Use the [email-authentication overview](https://learn.microsoft.com/en-us/defender-office-365/email-authentication-about) for these roles; this is not a recipe to publish production mail records.

A DHCP scope groups a subnet’s address range and options. A lease has a duration; a reservation consistently gives a DHCP client a selected address; an exclusion prevents the server from offering an address that may be set manually elsewhere. A reservation still relies on DHCP—it is not a static configuration written into the client. The [DHCP scope reference](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-scopes) explains the distinction. Avoid a blanket assumption that loss of the DHCP service instantly invalidates every existing lease.

Also recognize print/file/mail/database servers, syslog collection, AAA and time services. A proxy intermediates selected application traffic; a load balancer selects service backends; a spam gateway filters mail; a UTM appliance combines controls. SCADA/embedded/IoT systems may have strict availability and maintenance constraints. Identifying a device type is not permission to scan, reboot or change it.

### Devices, media, and configuration

A switch connects local Ethernet devices; router joins IP networks; firewall enforces policy; access point provides wireless attachment; modem/ONT terminates provider access; patch panel organizes fixed cabling; PoE supplies power over supported Ethernet; NIC provides the endpoint interface. Home gateways combine roles.

Managed switches expose configuration such as VLANs and monitoring; an unmanaged switch offers much less control. A VLAN separates a Layer 2 broadcast domain; a VPN protects a tunnel between endpoints. They solve different problems, and neither label alone proves all access paths are restricted. PoE requires a compatible standard, powered-device class and total switch/injector budget. A link light does not prove sufficient delivered power.

Copper Ethernet categories, coaxial, and fiber differ in connectors, reach, speed, interference, cost, and termination. Single-mode and multimode fiber have different optics/core/distance use. Inspect connector and cable specification rather than forcing or guessing. Cabling faults include opens, shorts, crossed/miswired pairs, poor termination, bend/damage, interference, and unsupported length/rate.

IPv4 and IPv6 are logical addressing systems. A subnet mask/prefix separates network and host portions; a default gateway reaches other networks. Private IPv4 ranges are not internet-routable directly. APIPA/link-local behavior signals missing configuration in some contexts. NAT translates addresses; port forwarding exposes a selected inbound service and increases risk. DNS server and address, gateway, and route information are separate settings.

### Original IPv4 and DHCP planning example

For the ordinary subnet `192.168.50.0/26`, the mask is `255.255.255.192`, the network address is `.0`, the broadcast is `.63`, and usable hosts are `.1` through `.62`. A `/26` boundary changes the local/remote decision: `.64` is in the next subnet even though the first three octets match. Gateways must be reachable on the client’s local link under this simple single-subnet design.

The three private IPv4 ranges are `10.0.0.0/8`, `172.16.0.0/12` and `192.168.0.0/16`. IPv4 link-local `169.254.0.0/16` is a different category, documented in [RFC 3927](https://www.rfc-editor.org/rfc/rfc3927.html). An unexpected link-local address can suggest failed DHCP configuration, but it is not proof that the NIC is broken. IPv6 has 128-bit addressing and does not use IPv4 broadcast behavior.

This original [Python ipaddress](https://docs.python.org/3.13/library/ipaddress.html) exercise calculates a plan without changing the host network. It does not allocate real leases.

```python
# A planning calculation only: no network settings are changed.
from ipaddress import ip_address, ip_network

network = ip_network("192.168.50.0/26")
gateway = ip_address("192.168.50.1")
pool = {ip_address(f"192.168.50.{i}") for i in range(10, 51)}
excluded = {ip_address(f"192.168.50.{i}") for i in range(10, 20)}
reserved = {ip_address("192.168.50.30")}  # printer uses DHCP reservation
ordinary_candidates = pool - excluded - reserved

assert all(address in network for address in pool)
assert gateway not in pool
print(network.netmask, network.broadcast_address)  # 255.255.255.192 192.168.50.63
print(len(list(network.hosts())))  # 62 usable addresses in this subnet
print(len(pool), len(ordinary_candidates))  # 41 total; 30 for other clients
print(ip_address("192.168.50.62") in network)  # True
print(ip_address("192.168.50.64") in network)  # False
```

The inclusive `.10`–`.50` pool has 41 addresses. Excluding `.10`–`.19` removes ten, and reserving `.30` for a DHCP printer leaves 30 candidates for other clients. That is the unoccupied planning capacity, not a claim that 30 leases are free on a running server. Setting another device manually to `.40` without excluding that address creates a collision risk. A reservation/exclusion is not authentication or a firewall rule.

### Wi-Fi, SOHO, IoT, and tools

Wireless standards/bands trade throughput, range, channel width, interference, compatibility, and congestion. Use current supported encryption, a strong unique administrative credential, safe firmware, a planned SSID/channel/band, guest/IoT separation, and disabled unnecessary exposure such as unsafe management or convenience features. WPA version and cipher support are compatibility and security decisions—verify current device support.

Keep radio band (2.4/5/6 GHz), channel width, Wi-Fi generation, regulatory availability and security mode separate. Bluetooth and NFC solve different proximity/pairing use cases; RFID identifies tagged objects and does not imply the same behavior as Wi-Fi networking. Wider channels can increase potential throughput while reducing reuse and increasing interference exposure.

SOHO setup includes ISP handoff, WAN, LAN addressing/DHCP, DNS, NAT/firewall, Ethernet switching, AP settings, guest/IoT segmentation, VPN need, updates, backup/export, and tested wired/wireless clients. Cloud-managed and software-defined controls change the management plane, not basic packet dependencies.

Compare access services—fiber, cable, DSL, satellite, cellular and WISP—by local availability, rates, latency, data limits and equipment requirements. Local Wi-Fi signal says little about provider access health. LAN/WLAN describe a local network and its wireless form; PAN links personal devices; MAN spans a metropolitan area; WAN connects broad areas; SAN serves storage networking and is not merely any shared folder.

Use a crimper/punchdown only with appropriate cable/connector and skill; cable tester for continuity/pinout; toner/probe for tracing; loopback plug for interface testing; Wi-Fi analyzer for channel/signal context; multimeter with training for electrical measurement. A cable stripper prepares the jacket without damaging conductors; a network tap supplies an authorized observation point. A continuity test does not certify the cable’s full signaling performance. Built-in tools can display address/route/DNS, test reachability and names, and trace paths. Never probe networks without authorization.

> **Related item:** A packet walk—source application, DNS, source IP/prefix/gateway, link/AP/switch, router/firewall/NAT, destination transport/service, return path—is the most reusable network troubleshooting model.

## 3. Hardware — 25%

### Display components and measurable attributes

Objective 3.1 separates the display from the rest of the computer. LCD families include IPS, TN and VA; compare the specific panel’s viewing angles, response, contrast and color performance rather than assuming every member is identical. OLED pixels emit light; Mini-LED commonly describes a finer-grained LCD backlight, not an OLED panel. A digitizer detects touch/pen input; a working image does not prove the digitizer works. An inverter belongs to applicable older backlight designs, not every current panel.

Resolution is the pixel dimensions; pixel density also depends on physical size. Refresh rate is how often the display can update, while application frame rate is how often the system renders. Color gamut describes a range of reproducible colors, not automatic calibration accuracy. Check cable/input capability, chosen resolution/rate, scaling and source output before replacing a display for blur, size or color problems.

### Compatibility before installation

Translate workload into constraints: CPU architecture/socket/chipset, motherboard form factor and firmware, RAM generation/type/speed/capacity/channel and board/CPU support, storage interface/form factor/protocol, GPU slot/power/space/thermals, PSU capacity/connectors/quality, case dimensions, cooling, ports, peripherals, operating-system support, and budget. A compatibility list and manuals beat visual resemblance.

Firmware settings may control boot order, virtualization extensions, secure boot/TPM, storage modes, fan/thermal behavior, and device enablement. Record the baseline and change only what the requirement needs. Firmware updates carry power and compatibility risk; follow vendor instructions and recovery requirements.

### CPU, memory, storage, power, and cooling

Install a CPU without touching contacts or forcing orientation; use approved thermal-interface material and cooler pressure. RAM goes in supported slots/configurations and may run at a fallback speed. ECC, registered/unbuffered, laptop/desktop form factors, and generations are not interchangeable merely because capacity matches.

SATA HDD/SSD, M.2 SATA, and M.2 NVMe may share familiar form factors while using different protocols/keys/lanes. RAID combines drives for performance and/or availability depending on level; it is not a backup and controller/metadata failure matters. Partition/file-system/OS setup occurs after the hardware is detected.

The [Dell RAID overview](https://www.dell.com/support/kbdoc/en-us/000128635/dell-servers-what-are-the-raid-levels-and-their-specifications) distinguishes striping, mirroring and parity. For traditional layouts with equal-size drives of capacity `S`, ignoring metadata, spare disks and filesystem overhead:

| Layout | Basic arrangement | Ideal usable capacity | Drive-failure boundary |
|---|---|---|---|
| RAID 0 | Stripe across at least two drives | `N × S` | No redundancy |
| RAID 1 | Two-drive mirror in this example | `S` | One of the pair |
| RAID 5 | Distributed single parity, at least three | `(N − 1) × S` | One drive |
| RAID 6 | Distributed dual parity, at least four | `(N − 2) × S` | Two drives |
| RAID 10 | Stripe across mirror pairs, at least four | `(N / 2) × S` | One per pair; failure placement matters |

Four 2 TB drives give ideal capacities of 8 TB in RAID 0, 6 TB in RAID 5 and 4 TB in RAID 6 or 10. Two 2 TB drives mirrored give 2 TB. In RAID 10 pairs `{0,1}` and `{2,3}`, failures `{0,2}` leave a member of each pair; failures `{0,1}` lose a whole pair. Do not describe RAID 10 as tolerating any two failures. Rebuilding consumes time and I/O and can expose additional failures; protect data before replacing/initializing the wrong drive. These calculations do not establish controller support, formatted capacity or measured performance.

Select a PSU for sustained component demand, transient headroom, efficiency/quality, connectors, form factor, and safety—not wattage label alone. A surge protector limits certain voltage events; a UPS provides temporary power and may condition power, but runtime/load/battery state matter. Check its supported AC input range and documented output/connectors: motherboard 20+4-pin, CPU/EPS and GPU/PCIe connections have different roles. Modular PSU cables are not universally interchangeable between models, even when connectors appear to fit. Redundant supplies require the supported system arrangement; two supplies are not automatically load sharing or failover. Never open a PSU. Cooling requires a complete airflow path, clean filters/heatsinks, correct fan/pump operation, good contact, and appropriate environment.

### Cables, peripherals, and specialized systems

Distinguish display/audio interfaces, USB generations/connectors, SATA/data/power, PCIe, Ethernet/fiber, and legacy connectors in scope. Confirm direction, protocol, resolution/rate, power, length, and adapter limitations. Adapters cannot create a signal or protocol the source does not provide.

Select specialized components by workload: gaming/graphics needs GPU/display/thermal emphasis; CAD/video may require CPU/GPU/RAM/fast storage and accurate displays; virtualization needs cores/RAM/storage/I/O and extension support; NAS emphasizes storage, RAID/network and backup; thin clients depend on network/remote services. Avoid oversimplified “more is always better.”

Recognize RJ11 versus RJ45, F-type coax, ST/SC/LC fiber, DB9 serial, SATA/eSATA and Molex power. Use the specified T568A/T568B termination consistently for the intended cable; do not assume connector fit proves pinout. Plenum and direct-burial ratings concern the installation environment, not just transmission speed.

Printers differ in imaging process and consumables. Laser flow includes processing, charging, exposing, developing, transferring, fusing, and cleaning; inkjet uses ink/printheads; thermal uses heat-sensitive media or ribbon; impact strikes a ribbon. Installation includes physical setup, consumables, safe transport locks, connection/IP, driver or print language, queue/defaults, test page, sharing, security, and maintenance.

For multifunction printers, distinguish PCL/PostScript driver-language compatibility from the physical connection. Duplex, orientation, quality and tray/media selections can produce “wrong output” without a failed print engine. ADF and flatbed scanning use different paper paths; scan-to-email/SMB/cloud additionally needs destination, credentials and policy. Badge/PIN release, authentication and logs protect shared printing; a working print queue does not prove scan delivery or secure release works.

For maintenance, match toner/maintenance-kit/calibration to laser, nozzles/ink/rollers to inkjet, specified media/heating-element cleaning to thermal, and ribbon/printhead/multipart paper to impact. Use the exact model’s manual and safe temperature/power state. Ghosting, repeated spots, skew and multipage feed are diagnostic clues rather than unique proofs of one failed part.

> **Related item:** Total cost of ownership includes energy, consumables, service life, support, downtime, and disposal, not just purchase price.

## 4. Virtualization and cloud computing — 11%

A type 1 hypervisor runs directly on hardware; type 2 runs above a host OS. A VM has virtual CPU, memory, storage, NICs, firmware/devices, and a guest OS. Containers share the host kernel more directly. Desktop virtualization/VDI presents a centrally hosted desktop or applications to endpoints. Virtualization provides isolation and flexibility but consumes physical resources and still requires patching, identity, network, storage, backup, and monitoring.

Before creating a VM, confirm CPU virtualization support/enabled firmware, RAM/storage capacity, network mode, image/license, and intended isolation. NAT, bridged/external, host-only/internal, and isolated virtual networks expose different paths. Snapshots/checkpoints are useful short-term state tools but are not automatically independent backups.

The [Hyper-V switch guide](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines) gives one concrete implementation: external connects to the selected physical network, internal connects guests and host, and private connects guests on that switch. The [manual WinNAT setup](https://learn.microsoft.com/virtualization/hyper-v-on-windows/user-guide/setup-nat-network) builds NAT on an internal switch and **does not automatically allocate guest IP addresses**; address, gateway and DNS setup remain separate. Creating a switch can disrupt the host connection. These are product-specific examples, not instructions executed by this review, and a “NAT” label alone is not a firewall policy or proof of isolation.

IaaS exposes infrastructure, PaaS a managed application platform, and SaaS a finished application. Public, private, community, and hybrid describe deployment/ownership patterns; on-demand, measured, elastic, pooled resources are common cloud traits. Shared responsibility shifts which party configures and secures each layer. Availability, internet dependency, data location, exit/portability, performance, subscription/consumption cost, identity, and backup remain customer decisions.

> **Related item:** High availability, backup, and disaster recovery solve different problems. A highly available wrong/deleted file still needs a protected recovery copy.

## 5. Hardware and network troubleshooting — 28%

> **Related item — practical support method:** The current objectives document excludes the formal methodology sequence itself from tested scope. Use it to organize the six tested troubleshooting areas:

Use the method consistently: identify; establish probable-cause theory; test theory; plan and implement or escalate; verify full function and preventive measures; document. Consider change history, scope, user impact, safety, backups, and corporate policy. Start with simple high-probability checks but do not skip evidence.

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

### Original local transport exercise

This small exercise uses the [Python socket reference](https://docs.python.org/3.13/library/socket.html) to distinguish reaching an endpoint from receiving an accepted application response. It speaks an invented `PING` protocol, not DNS, DHCP, HTTPS or an exam PBQ. It binds only to `127.0.0.1`, chooses a free port and closes sockets when finished. No administrator access or network reconfiguration is required.

```python
# Original toy request/response protocol, bound only to this computer.
from concurrent.futures import ThreadPoolExecutor
import socket

def exchange(transport, request):
    if transport not in ("tcp", "udp"):
        raise ValueError("Choose tcp or udp")
    if request not in (b"PING\n", b"NO\n"):
        raise ValueError("Use one of the two small exercise requests")
    kind = socket.SOCK_STREAM if transport == "tcp" else socket.SOCK_DGRAM
    with socket.socket(socket.AF_INET, kind) as service:
        service.bind(("127.0.0.1", 0))  # OS selects a free local port
        service.settimeout(3)
        endpoint = service.getsockname()
        if transport == "tcp":
            service.listen(1)

        def reply(data):
            return b"PONG\n" if data == b"PING\n" else b"ERROR\n"

        def serve_once():
            if transport == "tcp":
                connection, _ = service.accept()
                with connection:
                    connection.settimeout(3)
                    with connection.makefile("rwb") as stream:
                        stream.write(reply(stream.readline(64)))
                        stream.flush()
            else:
                data, peer = service.recvfrom(64)
                service.sendto(reply(data), peer)

        with ThreadPoolExecutor(max_workers=1) as workers:
            task = workers.submit(serve_once)
            with socket.socket(socket.AF_INET, kind) as client:
                client.settimeout(3)
                if transport == "tcp":
                    client.connect(endpoint)
                    client.sendall(request)
                    with client.makefile("rb") as stream:
                        response = stream.readline(64)
                else:
                    client.sendto(request, endpoint)
                    response, peer = client.recvfrom(64)
                    assert peer == endpoint
            task.result(timeout=4)
    return response

if __name__ == "__main__":
    for transport in ("tcp", "udp"):
        print(transport, exchange(transport, b"PING\n"))
        print(transport, exchange(transport, b"NO\n"))
```

Each transport returns `PONG` for `PING` and `ERROR` for `NO`. Receiving `ERROR` proves the toy application responded; it does not mean the transport was unreachable. TCP is a byte stream, so the example defines a newline as its message boundary; one send call is not a guaranteed one-receive message boundary. UDP preserves a datagram boundary, but this successful local exchange does not guarantee delivery, order or performance across a real network. A timeout could have several causes and is not itself proof of a firewall block.

**Actual review execution:** 34 local checks passed with Python 3.13.14. Both public examples ran; there were eight TCP/UDP loopback exchanges, including application rejections. IPv4/DHCP-capacity and RAID cases were calculations/models only. No actual DHCP leases, DNS service, routing, TLS, NAT, firewall change, Hyper-V switch, wireless network, printer, disk array, battery or hardware procedure was executed. All eight complete labs below remain proposed.

## Integrated scenarios

### Scenario 1: Hybrid-work laptop and dock

A laptop charges intermittently, an external display is blank, and office Ethernet disconnects. Inventory charger/cable/dock/ports/display input/NIC path, check power and capability compatibility, test each function directly and through the dock, inspect drivers/firmware/events, then replace only the failed link. Verify charging under load, display resolution, wired network/DNS/VPN, and mobile synchronization after restart.

### Scenario 2: Small-office refresh

Translate five users, a printer, guest devices, IoT cameras, backups, and remote access into router/firewall/AP/switch/cabling, IP/DHCP/DNS, secure Wi-Fi, guest/IoT separation, printer queue, UPS and documentation. Test wired/wireless clients, name resolution, printing, isolation, authorized VPN, backup restore, and recovery from a saved configuration.

### Scenario 3: Custom virtualization workstation

Select compatible board/CPU/RAM/NVMe/GPU/PSU/cooling for two VMs and creative work. Assemble safely, record firmware, test POST/memory/storage/thermals, enable virtualization, create segmented VM networks, and measure resource pressure. Introduce one RAM-seating, DNS, or virtual-network error and diagnose without changing multiple layers.

## Hands-on labs

1. **Laptop/mobile inventory:** map serviceable parts, display components, radios, ports, charger/dock capabilities, synchronization, and safe reset/backup boundaries.
2. **Protocol path:** distinguish A/AAAA/CNAME/MX/TXT, DHCP lease/reservation/exclusion, and the named port/service pairs; diagram and test DHCP, DNS, HTTPS, SMB, SSH/RDP or safe substitutes; explain ports, TCP/UDP, encryption, and failure symptoms.
3. **SOHO build:** configure an authorized router/AP with current encryption, admin security, addressing/DHCP/DNS, guest/IoT isolation, updates, and backup/export.
4. **Cable/tool bench:** identify/test safe copper cables and connectors; use a cable tester or simulator and document open/miswire/known-good results.
5. **PC build/upgrade:** compare display attributes and ideal RAID layouts, then use manuals to select/install RAM/storage or fully assemble an old PC; apply ESD/power safety and verify firmware/OS detection.
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

41. How do an A record, a DHCP reservation and a firewall rule affect different parts of a connection?
42. Why do two failed drives not always have the same effect in RAID 10?

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
13. Compare name resolution with an authorized service test and inspect the returned records. Ping success to one address does not prove TLS/application health; ping failure can reflect ICMP policy. DNS is a separate lookup, not a hop carrying all application traffic.
14. Interference, contention, upstream congestion, DNS/service, device capability, and application latency still matter.
15. Socket, chipset, firmware support, power, cooler, form factor, RAM/PCIe needs and workload.
16. Generation, form factor, ECC/buffering, voltage, speed/timing, density and board/CPU support differ.
17. M.2 is a form factor/connector family; SATA/NVMe are protocols, and NVMe commonly uses PCIe lanes.
18. It can preserve availability/performance but shares deletion/corruption, controller and site risks. Protection varies by layout: RAID 0 has none, RAID 5/6 tolerate one/two drive failures, and RAID 10 depends on which mirror members fail.
19. Sustained/transient load, connectors/rails, efficiency/quality, form factor, protections and headroom.
20. Stored high voltage is hazardous even disconnected; replace through qualified procedures.
21. Dust/blockage, reversed/poor airflow, failed pump, bad contact/paste, undersized cooler or high ambient temperature.
22. It cannot create a protocol/signal or sufficient bandwidth/power absent at the source.
23. A rotating drum/roller/fuser component whose circumference matches the repeat interval; inspect safely.
24. Correct queue/driver/IP, configuration/permissions, test output, sharing/security and restart/reconnect behavior.
25. Type 1 runs on hardware; type 2 relies on a host OS.
26. It may share the datastore/failure domain and create consistency/dependency/performance issues.
27. NAT translates through a configured host path, external/bridged joins a physical network, and isolation depends on the actual switch/routing policy. Manual Hyper-V NAT does not itself assign guest addresses; verify address, gateway, DNS and permitted paths separately.
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

41. A DNS A record returns an IPv4 address; a DHCP reservation gives a selected address to a matching DHCP client; a firewall rule permits or denies traffic. Success in one does not configure the others.
42. Two failures in different mirror pairs can leave each pair readable; losing both members of one pair loses that pair. The exact arrangement matters.

## 220-1101-to-220-1201 gap checklist

Older Core 1 material can teach durable concepts, but compare it line by line with V15. Specifically verify current mobile accessories/repair boundaries, USB and Wi-Fi generations, modern CPU/RAM/storage/GPU/firmware, AI-era hardware and cloud/virtualization terminology, SOHO security, current ports/protocols, printer coverage, PBQ expectations, and every public troubleshooting symptom/tool. Never combine an 1101 pass with 1202.

## Source and freshness notes

- The CompTIA page controls V15 weights, delivery, languages, score, same-version rule, and estimated lifecycle.
- Hardware standards, connectors, ports/protocols, Wi-Fi/security, product compatibility, and cloud behavior change. Use current manuals and standards/product documentation during hands-on work.
- This guide contains original scenarios, labs, checks, and explanations derived from public scope; the public version 4.0 objectives were read and mapped without reproducing the whole document. No paid course lessons, PBQs or exam items were used.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one current V15 path, spend comparable time on a safe hardware/network bench, and use explanation-led practice only to target weak domains.

| Resource | Access | Estimated time |
|---|---|---:|
| CompTIA [CertMaster Learn](https://www.comptia.org/en-us/resources/certmaster-training/learn/), Labs, and Practice | Paid official platform; select 220-1201 product/bundle | Provider estimates: Learn 25–40h, Labs 15–25h, Practice 10–20h; select what you need |
| [Pluralsight A+ Core 1 path](https://www.pluralsight.com/paths/comptia-a-core-1-220-1201) | Subscription; 6 courses and practice exam; public outline needs V15 comparison | 12 listed hours plus 20–40 lab/review hours |
| [LinkedIn Learning / Total Seminars Core 1](https://www.linkedin.com/learning/comptia-a-plus-core-1-220-1201-cert-prep) | Subscription; 21 quizzes; title/description exam-code discrepancy | 20 hours 14 minutes plus 20–40 lab/review hours |
| [Complete A+ Guide V15](https://www.oreilly.com/library/view/complete-a-guide/9780135439883/) | O'Reilly/Pearson subscription book covering both cores | About 25–45 selected reading/lab hours for Core 1 |
| [Udemy / Jason Dion Core 1](https://www.udemy.com/course/comptia-a-core-1/) | Paid marketplace course and practice exam | Current runtime unverified (page blocked); 20–40 lab/review hours estimated separately |
| [MeasureUp Core 1](https://www.measureup.com/comptia-a-core-1-practice-test.html) | Paid; 242 questions listed | About 6–12 hours across timed attempts and explanation review |
| [Professor Messer free 220-1201 course](https://www.professormesser.com/free-a-plus-training/220-1201/220-1201-video/220-1201-training-course/) | Free 63-video course; optional paid notes/practice | 10 hours 11 minutes plus 20–40 hands-on hours |

Pluralsight’s metadata lists 6 courses/12 hours, but its public “What You’ll Learn” includes older objective wording and the methodology item excluded by V15. LinkedIn lists a September 26, 2025 release and 20h14 runtime under a 220-1201 title, while its description explicitly says 220-1101. Treat these as catalog inconsistencies requiring a preview/full-objective comparison; paid lesson coverage was not verified. MeasureUp’s 242-question count and Professor Messer’s 63 videos/10h11 were confirmed from public listings. O'Reilly and Udemy blocked automated rechecking.

- **Practice method:** Damon M. Garn’s December 18, 2024 [CompTIA troubleshooting article](https://www.comptia.org/blog/troubleshooting-methodology) is useful for evidence, rollback and verification. Its broad discussion of methodology across certifications does not override the 1200-series exclusion.
- **Implementation references:** use the linked USB-IF, Dell, Microsoft, IANA and Python sources for a specific compatibility or lab question. The [Hyper-V overview](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/virtual-switch) is supporting context, not a requirement to build a Windows virtualization lab.

Whizlabs was not independently verified as an exact current 220-1201 source. Reject “actual questions” and dump sites. Vendor runtimes, prices, bundles, banks, revisions, and access change; verify before purchase.
