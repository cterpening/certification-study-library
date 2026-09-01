---
exam_code: FC0-U71
vendor_id: comptia
official_blueprint: https://www.comptia.org/en-us/certifications/tech/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# FC0-U71 CompTIA Tech+ Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#fc0-u71-coverage-record). The [official CompTIA Tech+ page](https://www.comptia.org/en-us/certifications/tech/) is authoritative.

**Current baseline:** Tech+ V6, exam series FC0-U71<br>
**Upcoming blueprint change:** None announced when checked September 1, 2026<br>
**Official delivery snapshot:** Maximum 70 questions, 60 minutes, passing score 650 on a 900-point scale; English and Japanese listed<br>
**Credential lifecycle detail:** The public page lists FC0-U71 as no-expiration and FC0-U71-CE as valid for five years. Confirm which series and renewal terms you are purchasing.<br>

## How to use this guide

Tech+ is a broad technology-literacy assessment. It rewards a connected mental model more than isolated acronym recall: data enters a device, components process and store it, an operating system exposes resources to applications, networks connect systems, databases organize persistent data, developers express logic, and security protects the whole flow.

For each concept, practice four moves:

1. define it in plain language without using the term itself;
2. identify it in a real device, diagram, operating system, application, or small data set;
3. compare it with the nearest alternative and state why the distinction matters;
4. troubleshoot one safe failure using identify → research/theory → test → implement → verify → document.

Do not turn a beginner guide into professional-level engineering trivia. You should recognize choices and reason about basic consequences, not memorize vendor-specific commands or configuration limits beyond the public V6 scope.

## Weighted objective map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Tech concepts and terminology | 13% | Explain computing, notation, units, and the troubleshooting method |
| 2. Infrastructure | 24% | Identify devices/components/storage/interfaces and reason about cloud, virtualization, and basic networks |
| 3. Applications and software | 18% | Distinguish operating systems, utilities, applications, browsers, files, and common AI uses |
| 4. Software development concepts | 13% | Read simple logic and distinguish language types, data types, control flow, functions, objects, and design representations |
| 5. Data and database fundamentals | 13% | Explain data value, relational/non-relational structure, queries/reports, scale, storage, and backups |
| 6. Security | 19% | Apply CIA, authentication/authorization, device hygiene, passwords, encryption, safe browsing, and physical protection |

## 1. Tech concepts and terminology — 13%

### The computing cycle

Computing transforms input into output through processing and often storage. A keyboard, camera, sensor, file, or network request provides input. A CPU/GPU and software apply instructions. A display, speaker, file, actuator, or network response provides output. Storage keeps data or instructions beyond the immediate operation.

Classify a component by its role in a particular flow rather than by a permanent label. A touchscreen is both input and output; a network adapter receives and transmits; a storage device can be read as input and written as output.

### Notation and measurement

Binary uses base 2, decimal base 10, octal base 8, and hexadecimal base 16. Understand positional value and convert small values, especially between binary and decimal and between a four-bit group and one hexadecimal digit. This explains why computing values, addresses, permissions, and colors often use representations other than ordinary decimal.

A bit is one binary value; a byte is commonly eight bits. Keep capacity, clock frequency, and transfer rate separate:

- KB/MB/GB/TB describe storage or memory quantities, subject to decimal/binary convention;
- MHz/GHz describe cycles per second, not guaranteed application performance;
- bps/Kbps/Mbps/Gbps describe bits transferred per second, not bytes stored;
- latency is delay, while bandwidth is potential volume per time.

Do not conclude that a higher number always makes a complete system faster. CPU architecture, core count, memory, storage, network, workload, thermal behavior, and software all contribute.

### Troubleshooting method

Start by identifying the problem: user report, symptoms, changes, scope, reproduction, and constraints. Establish a theory from evidence and research, test it with the least disruptive safe action, plan and implement the solution, verify full function and prevention, then document cause, action, and outcome. Escalate when access, risk, time, or expertise exceeds your boundary.

Changing several variables at once may accidentally restore service while destroying causal evidence. Back up important data and consider safety before opening hardware, removing software, resetting accounts, or changing network/security settings.

> **Related item:** Scientific-method thinking—hypothesis, controlled test, observation, revision—makes troubleshooting transferable even though the exam uses an IT workflow.

## 2. Infrastructure — 24%

### Devices and components

Recognize general-purpose desktops/laptops, smartphones/tablets, servers, gaming consoles, embedded systems, and Internet of Things devices. The form does not determine trust: a sensor or smart appliance is a networked computer with software, identity, updates, data, and failure modes.

| Component | Primary role | Useful distinction |
|---|---|---|
| Motherboard | connects components and buses | physical/socket/form-factor compatibility matters |
| CPU | executes general instructions | frequency alone is not total performance |
| RAM | fast volatile working memory | contents normally disappear without power |
| HDD | magnetic persistent storage | mechanical, usually cheaper/capacious but slower |
| SSD/NVMe | flash persistent storage | NVMe is a protocol/interface path, not a synonym for all SSDs |
| GPU | highly parallel graphics/compute | may be integrated or discrete; workload support matters |
| NIC | network interface | wired/wireless and link capability do not guarantee internet reachability |

Storage can be volatile or non-volatile, local/direct, network-attached, or cloud-delivered. “Cloud” describes remote service delivery and responsibility allocation; the data still resides on physical infrastructure. Compare capacity, speed/latency, connectivity, sharing, durability, portability, cost, privacy, and backup—not a single “best” label.

### Interfaces, peripherals, and drivers

USB connects many peripherals and can carry different combinations of data, display, and power depending on version/device/cable. HDMI commonly carries digital audio/video. Ethernet is a wired network technology. Bluetooth supports short-range wireless peripherals; NFC supports very short-range interactions. The connector's shape does not guarantee every optional feature or speed.

A driver lets an operating system communicate with hardware. Before replacing a “failed” peripheral, verify power, physical connection, correct port/input, operating-system detection, driver/status, configuration/default selection, permissions, and a known-good cable/device. Use safe electrostatic and electrical practices; do not work inside powered equipment unless trained and authorized.

### Virtualization and cloud

A hypervisor enables multiple virtual machines to share a host while maintaining logical separation. A container shares more of the host operating-system kernel and is not equivalent to a VM. Virtualization improves utilization and isolation but does not eliminate capacity, patching, backup, or security responsibilities.

In IaaS, the provider supplies lower-level infrastructure while the customer manages more of the OS and application stack. PaaS manages more runtime/platform layers. SaaS presents a finished application. On-premises infrastructure is operated in an organization's facilities; public cloud uses shared provider infrastructure; hybrid connects environments. Responsibility shifts rather than disappears.

### Networking fundamentals

A LAN connects a limited local area; a WAN connects locations over distance. A switch primarily connects devices within a local network. A router forwards traffic between IP networks. A firewall applies traffic policy. A wireless access point connects Wi-Fi clients to a network; a home “router” often combines all four roles.

A MAC address identifies a network interface at the local-link layer; an IP address enables logical routing. DNS translates names to records such as IP addresses. DHCP commonly supplies IP configuration. Test a path in layers: link/power, local configuration, local gateway, DNS, destination/service, then security policy. “The internet is down” can actually be one application, one name lookup, one device, one wireless channel, or one external service.

Wi-Fi performance depends on standard, band/channel, distance, obstructions, interference, client/access-point capability, contention, and upstream service. A theoretical maximum is not an application guarantee.

> **Related item:** The OSI and TCP/IP models are useful troubleshooting maps. Tech+ does not require professional packet analysis, but separating physical/link, addressing/routing, transport, and application failures prevents random fixes.

## 3. Applications and software — 18%

### Operating systems and files

An operating system manages hardware, processes, memory, storage/files, devices, users, security, and interfaces for applications. Desktop, mobile, server, and embedded operating systems emphasize different interaction and workload needs. A graphical interface and command line are alternate management surfaces, not different operating systems.

A file system organizes data and metadata on storage. NTFS and FAT32 illustrate different capability and compatibility tradeoffs; avoid assuming every file system supports the same permissions, size, journaling, encryption, or operating systems. Files have paths, names, extensions/types, ownership/permissions, timestamps, and content. An extension helps association but does not prove that a file is safe or that its content matches its name.

Utilities perform system-oriented tasks such as file management, backup, compression, security scanning, disk management, and monitoring. Drivers bridge the OS and hardware. Applications help the user perform work: word processing, spreadsheets, presentations, communication/collaboration, browsers, media, remote support, and specialized tools.

Install from trusted sources, confirm platform/version and resource compatibility, review permission needs, patch responsibly, and know how to remove or roll back. Licensing answers whether/how software may be used; it is separate from technical compatibility.

### Browsers and remote applications

Browsers render web applications and manage tabs, history, cookies/site data, cache, extensions, downloads, permissions, saved passwords, and private-browsing sessions. Private browsing mainly limits local session history; it does not make activity anonymous to networks, sites, accounts, employers, or providers. Clearing cache may resolve stale local content but can remove useful offline data and does not fix every server-side issue.

Treat extensions as software with permissions. Review publisher/source, requested access, updates, necessity, and removal. A password manager can create and store unique passwords, but it still needs a strong protected account and recovery plan.

### Artificial intelligence uses and limits

Chatbots and assistants accept requests and produce responses; generative AI creates text, images, audio, code, or other content; predictive systems estimate classifications or future outcomes. AI output can be plausible but wrong, biased, unsafe, copyrighted, or based on sensitive input. Verify important results, protect confidential data, cite sources where required, and keep accountable human judgment for consequential decisions.

> **Related item:** Automation follows encoded rules or learned behavior; intelligence and correctness should not be inferred merely because a system produces fluent output.

## 4. Software development concepts — 13%

Compiled languages are translated before execution; interpreted languages are executed through an interpreter/runtime; scripting languages often automate or glue tasks; markup describes document structure; assembly maps closely to processor instructions. Real ecosystems blur these categories, so learn the purpose of the comparison rather than absolute labels.

Data types constrain representation and operations: characters and strings hold text, integers whole numbers, floating-point types approximate fractional values, and Boolean values represent true/false. A variable names changeable state; a constant represents an intended unchanging value. An array/list groups values. A function packages reusable behavior with inputs/parameters and output/side effects. An object combines state and behavior according to a type/class model.

Branching chooses a path based on a condition; loops repeat while/for a condition or collection; errors/exceptions represent abnormal behavior. Read pseudocode by tracing one statement at a time and recording variable values. Check initial state, boundary/termination, input types, path condition, output, and error case.

Pseudocode communicates logic without strict language syntax. Flowcharts visualize sequence, decisions, input/output, and loops. Object-oriented design organizes responsibilities around objects/classes. These are design/communication tools; they do not automatically produce correct, secure, or maintainable code.

> **Related item:** Testing turns an expected behavior into evidence. For beginner logic, use a normal case, boundary case, invalid input, and repeated/empty case rather than only the happy path.

## 5. Data and database fundamentals — 13%

Data becomes useful when it is accurate enough, timely, relevant, understood, protected, and connected to a decision. Reports summarize; analytics identifies patterns; operational systems support transactions; organizations may create products or revenue from data only when rights, consent, ethics, quality, and security permit it.

In a relational database, tables contain rows/records and columns/fields. A primary key uniquely identifies a row; a foreign key relates it to another table. Normalized design can reduce duplication and inconsistency, while deliberate denormalization may help some reads. A query requests or changes data; a report presents selected information. Schema, constraints, indexes, permissions, transactions, and backups all affect behavior even if Tech+ treats them conceptually.

Non-relational databases may organize documents, key-value pairs, graphs, or wide columns. They are not simply “unstructured” or always faster. Choose based on data shape, access patterns, consistency, scale, operations, and tooling. Local versus cloud database placement changes responsibility, connectivity, scale, cost, control, and resilience considerations.

A file copy can protect selected content; an image/system backup captures broader state. Local backup restores quickly but can share the site's failure; cloud/remote backup improves separation but depends on connectivity, account security, cost, and restore process. A sync is not automatically a backup because deletion or corruption can propagate. Test restoration and define how much data loss and downtime are acceptable.

> **Related item:** The 3-2-1 principle—multiple copies, different media, one offsite—is a useful foundation, but backup quality is proven by protected, monitored restores.

## 6. Security — 19%

### Principles and identity

Confidentiality limits disclosure, integrity protects correctness/completeness, and availability keeps systems/data usable. Authentication proves an identity; authorization determines allowed actions; accounting/auditing records activity. A login can authenticate successfully yet be correctly denied a protected file because authorization is separate.

Use least privilege, separation of duties where practical, and layered controls. Physical access can bypass many software controls, so secure devices, screens, ports, removable media, and disposal. Lock unattended systems and report loss promptly.

### Device and user hygiene

Keep supported software patched, use anti-malware and host/network firewalls appropriately, install from trusted sources, remove unnecessary software, back up, and avoid running routinely as an administrator. Treat unexpected links, attachments, QR codes, support calls, MFA prompts, removable media, and urgent requests as potential social engineering. Verify through an independent trusted channel.

Passwords should be long, unique, private, and stored in a reputable password manager; do not reuse or share them. Multi-factor authentication combines different factor types and reduces—but does not eliminate—account risk. Never approve an unexpected prompt.

Encryption protects readable data with keys. Data at rest includes files/devices/backups; data in transit includes network communications. HTTPS protects the connection to an authenticated web endpoint when correctly used; a VPN protects traffic across a tunnel but does not make every destination trustworthy. Device encryption is weakened if an unlocked session or recovery key is exposed. Protect keys and recovery paths.

> **Related item:** Risk combines likelihood and impact. Security controls should reduce a real risk without making recovery or legitimate use impossible.

## Integrated scenarios

### Scenario 1: New-student workstation

A student receives a laptop, monitor, printer, cloud-storage account, and collaboration application. Identify ports/components, select trusted drivers/software, create a unique password and MFA, configure updates and backup, connect Wi-Fi, print a test page, and document the setup. Then diagnose a deliberately disconnected cable, wrong display input, and stale browser cache one at a time.

### Scenario 2: Small club data project

Model members and events as relational tables with keys, write plain-language queries/reports, trace pseudocode that counts attendance, back up/export the data, and explain which personal fields should not be broadly shared. Compare a local spreadsheet, relational database, and cloud application without declaring one universally best.

### Scenario 3: “Internet down” and suspicious message

One user cannot open a named site but other apps work. Test device/link, IP/gateway, DNS, browser, destination, and policy in order. During diagnosis, a message asks for an urgent password reset. Preserve the message, do not use its link, verify through an official channel, report it, and document both the technical and security outcomes.

## Hands-on labs

1. **Device inventory:** identify CPU, RAM, storage, NIC, OS, interfaces, peripherals, and capacity units on an authorized device; explain each role.
2. **Notation and rates:** convert small binary/decimal/hex values and calculate simple file-transfer estimates while distinguishing bits/bytes and bandwidth/latency.
3. **Peripheral troubleshooting:** install or inspect a printer/display/USB device, introduce one safe failure, use the method, verify, and document.
4. **Virtual/cloud comparison:** inspect a VM and one SaaS application; map provider/user responsibility, storage, identity, updates, and backup.
5. **Network path:** diagram device → Wi-Fi/AP/switch → router/firewall → DNS → service; test each reachable layer with built-in tools.
6. **Software and browser hygiene:** inspect trusted source, permissions, version/update, extension access, cache/cookies, password manager, and safe removal.
7. **Logic and data:** trace pseudocode with branches/loops, create two related tables, insert test rows, run simple queries, and explain keys and backup.
8. **Security/recovery capstone:** harden a disposable account/device, simulate a phishing report and lost file, restore the file, and produce a short evidence record.

Use only your own or explicitly authorized devices, accounts, networks, and test data. Do not scan, reset, open, or alter systems belonging to others.

## Original knowledge checks

1. In a video call, identify one input, process, output, and storage element.
2. Why can a touchscreen be both input and output?
3. Convert binary `1010` to decimal and hexadecimal.
4. Why is 100 Mbps not the same as 100 MB/s?
5. Which troubleshooting step should precede changing several settings?
6. When should a beginner escalate instead of continuing?
7. Why does more GHz not guarantee a faster computer?
8. Compare RAM with SSD storage after power loss.
9. What distinguishes an NVMe SSD from the general SSD category?
10. What should you check before replacing a failed peripheral?
11. Why can the same USB-shaped connector provide different capabilities?
12. Compare a VM and a container at a high level.
13. Which responsibilities remain with a SaaS user?
14. Distinguish switch, router, firewall, and access point.
15. What is the difference between MAC and IP addressing?
16. Why can DNS failure look like an internet outage?
17. Which factors make real Wi-Fi speed differ from its advertised maximum?
18. What does an operating system manage for applications?
19. Why does a filename extension not prove content or safety?
20. Distinguish driver, utility, and end-user application.
21. What does private browsing not hide?
22. Why should browser-extension permissions be reviewed?
23. Name two risks of using generative AI output without verification.
24. Distinguish compiled, interpreted, scripting, and markup languages.
25. What are variable, constant, array, function, and object used for?
26. How do branching and looping differ?
27. Which cases should test a simple input-validation function?
28. Distinguish pseudocode from a flowchart.
29. How do primary and foreign keys work together?
30. Why is non-relational not a synonym for unstructured or faster?
31. Why can synchronization fail as a backup strategy?
32. What proves that a backup is useful?
33. Apply confidentiality, integrity, and availability to a student record.
34. Distinguish authentication from authorization.
35. Why are unique long passwords and MFA complementary?
36. What should you do with an unexpected MFA prompt?
37. Compare encryption at rest and in transit.
38. Why does a VPN not make every website or download trustworthy?
39. What is the safest response to an urgent credential-reset message?
40. What is unusual about the lifecycle choice shown for FC0-U71 versus FC0-U71-CE?

## Answers and reasoning

1. Camera/microphone; codec/app/CPU; screen/speaker/network response; recording/cache/file.
2. It displays information and detects touch/gesture input.
3. Decimal 10 and hexadecimal A.
4. Network rates use bits per second; byte conversion and overhead also matter.
5. Identify/reproduce and form an evidence-based theory; preserve a baseline.
6. When authorization, safety, data risk, access, time, or expertise exceeds the task boundary.
7. Architecture, cores, memory, storage, thermals, workload, and software also constrain performance.
8. RAM is volatile working memory; an SSD retains stored data without power.
9. NVMe describes a high-performance storage protocol/interface path; SSD describes flash storage generally.
10. Power, cables/ports/input, OS detection, driver/status, configuration, permissions, and a known-good comparison.
11. Connector form and protocol/version/power/display capabilities are separate.
12. A VM virtualizes a full OS environment; a container shares the host kernel more directly.
13. Account/access, data handling, endpoints, configuration, acceptable use, and often backup/export choices.
14. Local forwarding, inter-network routing, policy enforcement, and wireless attachment.
15. MAC is local-link interface identity; IP is logical routed addressing.
16. Connections by address may work while human-readable names fail to resolve.
17. Standard/band/channel, interference, distance/obstacles, contention, client/AP capability, and upstream service.
18. Hardware, processes, memory, files/storage, devices, users/security, networking, and interfaces.
19. It can be renamed or misleading; inspect trusted source, type, signatures/scans, and behavior.
20. A driver connects OS to hardware; utility maintains/manages; application performs user work.
21. It does not hide traffic or identity from sites, accounts, networks, employers, or providers.
22. Extensions can read/change browsing data and expand attack or privacy exposure.
23. Hallucinated facts, bias, unsafe advice/code, sensitive-data leakage, and rights/copyright issues.
24. Pretranslated code, runtime-executed code, automation/glue code, and structural description.
25. Named changing state, intended fixed state, grouped values, reusable behavior, and bundled state/behavior.
26. A branch selects paths; a loop repeats based on a condition or collection.
27. Normal, boundary, invalid/type, empty, and repeated cases.
28. Pseudocode is language-neutral written logic; a flowchart is a graphical control/data-flow representation.
29. A primary key identifies a row; a foreign key points to a related table's key.
30. Non-relational systems have defined models and tradeoffs; performance depends on workload and design.
31. Deletion, corruption, or encryption can synchronize to every copy.
32. A protected, monitored backup that successfully restores within required loss/time limits.
33. Restrict disclosure, prevent/detect unauthorized change, and keep records accessible to authorized users.
34. Authentication proves who; authorization decides what that identity may do.
35. Uniqueness prevents reuse damage, length resists guessing, and MFA adds an independent barrier.
36. Deny it, inspect account activity, change credentials through a trusted path if needed, and report it.
37. At-rest encryption protects stored media/data; in-transit encryption protects communications.
38. It secures a tunnel segment, not the destination's honesty, content, account, or endpoint.
39. Do not click; verify through an independently located official channel and report/preserve it.
40. The official page lists FC0-U71 as no-expiration and FC0-U71-CE as five-year validity; verify purchase/renewal terms.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one coherent primary course or book, add hands-on practice and one explanation-led assessment, and use the official objectives as the final scope checklist.

| Resource | Access | Estimated time |
|---|---|---:|
| [CompTIA CertMaster Learn](https://www.comptia.org/en-us/resources/certmaster-training/learn/) | Paid official learning platform | About 20–35 selected hours plus notes |
| [CompTIA CertMaster Labs](https://www.comptia.org/en-us/resources/certmaster-training/labs/) | Paid official labs; availability/bundle varies | About 8–15 selected hours |
| [CompTIA CertMaster Practice](https://www.comptia.org/en-us/resources/certmaster-training/practice/) | Paid official adaptive practice | About 4–8 hours including remediation |
| [Pluralsight Tech+ FC0-U71 path](https://www.pluralsight.com/paths/comptia-tech-fc0-u71) | Subscription; 9 courses, 3 labs, practice exam | 13 listed hours plus 8–15 practice hours |
| [LinkedIn Learning Tech+ Cert Prep](https://www.linkedin.com/learning/comptia-tech-plus-fc0-u71-cert-prep) | Subscription; Total Seminars | 4 hours 50 minutes plus 8–15 practice hours |
| [O'Reilly TOTAL Tech+ FC0-U71](https://www.oreilly.com/library/view/total-comptia/9781837021550/) | Subscription video | About 5–8 hours estimated; verify current listed runtime |
| [Udemy Tech+ by Mike Chapple](https://www.udemy.com/course/certmike-comptia-it-fundamentals-itf/) | Paid marketplace course | 4 hours 6 minutes plus labs/review |
| [MeasureUp Tech+ practice test](https://www.measureup.com/comptia-tech-practice-test.html) | Paid; 171-question bank listed | About 4–8 hours across attempts and explanation review |
| [Technical Institute of America full course](https://www.youtube.com/watch?v=uk7uhpyNmhE) | Free YouTube course | Verify current video runtime; allow 8–15 hours with notes and labs |

No exact current Whizlabs Tech+ product was independently verified. Practice questions should diagnose concepts and explain alternatives, not promise recalled exam content. Provider prices, bundles, question counts, runtimes, access, and revision dates are volatile—verify before purchase.

## Source and freshness notes

- CompTIA controls the V6 domain weights, delivery details, languages, passing score, series/lifecycle wording, and official learning options.
- Hardware, wireless standards, operating-system behavior, browser/AI features, and security recommendations change; use supported current product documentation for implementation.
- This guide uses only the public domain outline and original scenarios/checks. It does not reproduce proprietary objective PDFs, course material, or exam questions.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.
