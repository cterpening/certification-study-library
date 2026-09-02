---
exam_code: 100-160
vendor_id: cisco
official_blueprint: https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-cybersecurity.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Cisco Certified Support Technician Cybersecurity (100-160) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#100-160-coverage-record). Cisco's [exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-cybersecurity.html) and [exam-topics page](https://learningnetwork.cisco.com/s/ccst-cybersecurity-exam-topics) are authoritative.

**Current baseline:** Active 100-160 CCST Cybersecurity exam; five public work areas and Cisco's complete current exam-aligned training objectives, checked September 2, 2026<br>
**Scheduled change:** None announced on the checked official pages<br>
**Official source:** [100-160 exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-cybersecurity.html) · [exam topics](https://learningnetwork.cisco.com/s/ccst-cybersecurity-exam-topics) · [training overview](https://www.cisco.com/c/dam/en_us/training-events/training/courses/ccst-cybersecurity.pdf)

## How to use this guide

Study every control and incident as a chain: valuable asset/business process → threat actor/event → vulnerability/exposure → likelihood and impact → preventive/detective/corrective control → observable evidence → authorized response → recovery and lessons learned. Be able to say what a tool or control proves, what it does not prove, and when an entry-level technician must escalate.

Cisco currently lists a 50-minute exam costing USD 125 and offered in English, Arabic, Chinese, Spanish, French, Japanese, and Portuguese. The [CCST FAQ](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/support-technician/faq.html) describes the credential as entry-level and lifetime, and estimates the free self-paced Junior Cybersecurity Analyst Career Path at about 120 hours. Recheck commercial and delivery facts before booking.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the published objectives.

## Objective map

Cisco's public material organizes the scope into five work areas but does not expose a stable weighted table in the checked server-rendered interface. This guide therefore does not invent percentages.

| Work area | Evidence that demonstrates understanding |
|---|---|
| Security principles | Classify assets, threats, vulnerabilities, risk, CIA goals, controls, access decisions, cryptography, ethics and attacker motives |
| Network security | Trace TCP/IP exposure and apply segmentation, filtering, secure management, wireless, identity and monitoring controls |
| Endpoint security | Establish an OS/device baseline, compare policy with state, interpret logs, update safely and follow malware procedure |
| Vulnerability assessment and risk management | Scope authorized discovery, validate findings, prioritize by context, assign treatment and connect continuity to risk |
| Incident handling | Triage events, preserve evidence/chain of custody, escalate, contain through authorization, recover and document lessons |

---

## 1. Security principles

### Assets, events, and risk

An **asset** has value: data, identity, endpoint, service, facility, reputation, or business process. A **threat** is a potential cause of harm; a **threat actor** can intentionally exploit weakness; a **vulnerability** is a weakness; an **exploit** uses a vulnerability; and **risk** combines uncertainty about occurrence with consequence. A security event is observable activity; an incident is an event or series of events that violates or threatens policy/business operation and requires coordinated handling.

Keep these pairs separate:

- **Likelihood** asks how plausible/frequent exploitation is in this context; **impact** asks what the consequence would be.
- **Inherent risk** exists before selected controls; **residual risk** remains afterward.
- **Risk acceptance** knowingly retains risk; **mitigation** reduces it; **transfer/share** allocates consequence; **avoidance** stops the risky activity.
- A **false positive** is an alert without the claimed harmful condition; a **false negative** is missed harmful activity.

### Security objectives and control types

Confidentiality prevents unauthorized disclosure, integrity protects correctness and authorized change, and availability keeps authorized capability usable. Authenticity supports confidence in identity/origin; accountability connects action to an identity; non-repudiation makes credible denial harder through trustworthy evidence.

Controls can be administrative (policy, training, process), technical (MFA, firewall, EDR, encryption), or physical (locks, guards, environmental protection). They can deter, prevent, detect, correct, recover, or compensate. MFA may prevent some account takeover, logging detects activity, isolation contains, restoration recovers, and a compensating control reduces exposure when the preferred control is unavailable. Defense in depth uses independent layers; duplicating one weak layer is not depth.

### Identity and access management

Identification claims an identity; authentication verifies it; authorization decides permitted action; accounting/auditing records activity. Factors include something known, possessed, or inherent; two passwords are not two factors. Least privilege limits permissions, need to know limits data access, separation of duties prevents one person from controlling a sensitive transaction end-to-end, and role-based access assigns permission through job functions.

Apply joiner–mover–leaver lifecycle: establish a unique approved identity, grant minimum role access, review/adjust after change, disable promptly at departure, and preserve required records. Avoid shared administrator accounts. Prefer MFA, password managers, long unique passwords/passphrases, and secure recovery. Privileged access should be separate, time-bounded where possible, monitored, and reviewed.

**Related item:** Zero trust is not a product or “trust nobody.” It continuously evaluates explicitly verified identity/device/context and limits access/blast radius. Network location alone is insufficient proof.

### Cryptography with the right purpose

Symmetric encryption uses one shared secret and is efficient for bulk data. Asymmetric cryptography uses a related public/private key pair and supports key exchange, encryption in appropriate designs, and digital signatures. A cryptographic hash produces a fixed-size digest for integrity comparison; hashing is not reversible encryption. Salts make equal passwords hash differently and hinder precomputed attacks.

TLS protects data in transit when certificate validation and endpoint trust are sound. Full-disk or database encryption protects defined data at rest but not necessarily data after an authorized user/application decrypts it. A digital signature supports origin/authenticity and integrity; it does not keep content secret by itself. Keys need generation, storage, access, rotation, backup/recovery, expiration, revocation, and destruction controls.

### Threats and ethics

Recognize phishing/spear phishing/whaling, vishing/smishing, impersonation, pretexting, baiting, tailgating, shoulder surfing, malware categories, credential attacks, on-path interception, denial of service, insider risk, physical theft, supply-chain compromise, and insecure Internet-of-Things devices. Classify by mechanism and evidence rather than dramatic label.

Security work is bounded by law, policy, permission, scope, and professional ethics. Never scan, capture, exploit, remove malware, or access an account merely because a tool makes it possible. Obtain written authorization, minimize collection, protect evidence and personal data, and stop/escalate when scope is uncertain.

---

## 2. Network security

### TCP/IP exposure and network evidence

An Ethernet frame delivers across a local link, an IP packet crosses networks, and TCP/UDP connects application endpoints through ports. DNS translates names, DHCP supplies configuration, ARP maps local IPv4 next-hop addresses to MAC addresses, routing selects paths, and NAT changes defined address/port representations. Attackers may abuse protocol trust, exposed services, weak authentication, spoofing, name resolution, insecure clear-text protocols, or misconfiguration.

Useful security questions are: Which source identity/address initiated what protocol and destination? Was the service expected? Was authentication successful? Did volume, time, geography, process, or sequence differ from baseline? One IP address may represent many users behind NAT, while one user may use many addresses; correlate multiple sources.

### Infrastructure and boundary controls

- **Router/Layer 3 switch:** moves traffic between networks; routing control and ACLs can constrain paths.
- **Firewall:** enforces policy based on addresses, ports, protocol, direction, state, zone, application, or identity depending on capability.
- **IDS/IPS:** detects suspicious traffic; an IPS can take inline prevention action and can also disrupt legitimate traffic if poorly tuned.
- **Proxy/security gateway:** mediates application requests and can apply authentication, filtering, inspection, or logging.
- **VPN:** creates a protected tunnel; it does not make a compromised endpoint trustworthy.
- **Network access control:** evaluates users/devices before or during access.
- **Segmentation:** separates trust zones and limits reachable services and blast radius.

Default deny permits only justified flows. Ingress controls inbound traffic; egress controls outbound traffic. Management interfaces belong on protected paths and should use SSH/HTTPS or another approved encrypted method rather than Telnet/HTTP. Disable unused services and ports, change defaults, update supported software, back up configuration securely, synchronize time, centralize logs, and validate both allowed and denied behavior.

**Related item:** An ACL is often stateless and order-sensitive, while a stateful firewall tracks connections. Product behavior varies; use the actual platform documentation and policy, not the label alone.

### Secure wireless and small-office design

Prefer WPA3 where supported or WPA2 with AES where compatibility requires it. Avoid WEP, deprecated cryptography, default administrator credentials, short shared secrets, unnecessary remote management, and insecure convenience features. Keep firmware supported, use guest isolation for untrusted devices, separate administration, record recovery, and restrict physical access.

Enterprise wireless may use 802.1X with individual identities and RADIUS/AAA rather than a shared passphrase. Rogue and evil-twin access points, deauthentication/disruption, weak onboarding, exposed management, and untrusted clients create different evidence and controls. SSID hiding is not a security control.

### Monitoring without overclaiming

Sources include firewall/IDS/IPS, DNS, DHCP, VPN, authentication, wireless controller, endpoint, proxy, application, cloud, vulnerability, and network-flow logs. Establish synchronized time, asset/identity context, retention, access control, integrity, and alert ownership. A denied connection can show a control working; repeated denials may show scanning, misconfiguration, or a broken application. Validate context before declaring an attack.

Packet capture can expose credentials, tokens, personal data, and business content. Capture only authorized interfaces/traffic, minimize duration and filters, protect files, record hash/time/collector where required, and follow retention/destruction policy.

---

## 3. Endpoint security

Endpoints include user devices, servers, phones, network appliances, virtual machines, and IoT/operational devices. Start with an expected baseline: approved owner/purpose, supported OS/firmware, secure configuration, required controls, allowed software/services, network zone, update state, encryption, backup, logging, and recovery method.

### Hardening and policy validation

Reduce attack surface: remove/disable unnecessary accounts, software, services, ports, macros, autorun, and default credentials; apply least privilege; enable host firewall, supported anti-malware/EDR, screen lock, secure boot where supported, storage protection, and trusted update sources. Configuration policy is intent; observed state proves implementation.

Useful authorized evidence includes:

- running processes, services, startup/persistence entries, installed software, users/groups and logged-on sessions;
- active/listening network connections and owning processes;
- patch/firmware/definition status and recent configuration change;
- authentication, system, security, application and endpoint-protection logs;
- file metadata and hashes, quarantine history, alerts and device health.

Windows Event Viewer, Task Manager, Services, Defender/EDR interfaces, `ipconfig`, `netstat`, `Get-Process`, and `Get-Service` expose different slices. Linux `journalctl`, authentication logs, `ps`, `systemctl`, package tools, `ip`, and `ss` do likewise. Tool names, permissions, and log locations vary—know the question first, then choose the least invasive evidence.

### Updating safely

Inventory assets and supported versions, rank risk/exposure, test representative systems, back up/prepare rollback, schedule/communicate, deploy in stages, monitor failures and security signals, verify installed state, and document exceptions. A “patch successful” console result is not enough if the endpoint did not restart when required or the vulnerable component remains reachable.

Firmware and hardware updates can have stricter power/recovery requirements. Unsupported systems need explicit containment, replacement, and risk ownership rather than indefinite silent exception.

### Suspected malware

Do not improvise deletion. Record alert/user/time/scope, follow the incident plan, preserve volatile evidence when directed, isolate using approved procedures, escalate, acquire/scan/remediate with approved tools, recover from a known-good state, reset exposed credentials through a clean path, patch the entry point, monitor recurrence, and document. Quarantine is containment, not proof that persistence, lateral movement, or data access did not occur.

**Related item:** Reimaging can restore a device faster and more confidently than manual cleanup, but only after required evidence is preserved and identity/data/network exposure is addressed.

---

## 4. Vulnerability assessment and risk management

A vulnerability program is a lifecycle, not a scanner report:

1. Define authorized scope, owners, exclusions, timing, safety constraints, credentials, and notification/escalation.
2. Discover assets and validate ownership/exposure.
3. Assess with appropriate authenticated/non-authenticated tools and configuration/compliance checks.
4. Validate findings and remove obvious false positives/duplicates without hiding uncertainty.
5. Prioritize using exploitability, exposure, asset/business criticality, data, existing controls, active threat intelligence, and consequence—not severity score alone.
6. Assign remediation/mitigation/acceptance/avoidance with owner and due date.
7. Retest the actual control/state and report residual risk and exceptions.

A vulnerability is not automatically an incident. A finding on an Internet-facing critical system with known exploitation may outrank a higher numeric score on an isolated disposable lab. Threat intelligence adds context about actors, indicators, tactics, vulnerabilities, campaigns, and observed exploitation; evaluate source reliability, relevance, timeliness, and confidence.

Risk records should identify asset/process, threat scenario, vulnerability, existing controls, likelihood, impact, treatment, owner, due date, residual risk, evidence, review date, and acceptance authority. Compliance says which obligations apply and provides minimum control/evidence expectations; compliance alone does not prove security.

### Continuity and recovery

Business impact analysis identifies critical processes, dependencies, disruption consequences, and recovery priorities. Business continuity sustains essential operation; disaster recovery restores technology/data; incident response manages the security event. Recovery time objective (RTO) is the target time to restore; recovery point objective (RPO) is the tolerable data-loss window. Backups must be protected, separated, monitored, and restore-tested.

**Related item:** The 3-2-1 backup pattern—three copies, two media/types, one offsite/isolated—is a useful baseline, not a guarantee. Immutability, identity separation, encryption, retention, capacity, application consistency, and recovery testing still matter.

---

## 5. Incident handling

### Event triage and escalation

Triage asks whether evidence is credible, what asset/identity/data is involved, current impact/scope, severity/urgency, whether activity continues, which playbook/owner applies, and what immediate safety/legal obligations exist. Preserve original alerts and timestamps. Escalate when the incident involves privileged identities, regulated/sensitive data, material business impact, active lateral movement/exfiltration, physical safety, legal/reporting requirements, unavailable authority, or uncertainty beyond your role.

The response lifecycle is preparation → detection/analysis → containment → eradication → recovery → post-incident improvement. Phases can overlap and loop. Short-term containment limits immediate harm; long-term containment supports stable operation while removal is planned. Eradication removes root cause/persistence; recovery restores known-good service and monitors it. Closing an alert without recovery validation is incomplete.

### Evidence and forensics

Digital forensics uses defensible methods to identify, collect, preserve, examine, analyze, and report evidence. Order of volatility matters because memory, connections, processes, and temporary data can disappear. Chain of custody records what was collected, when/where/by whom, how transferred/stored, and each access. Hashes support integrity comparison, not truth of the original content.

Do not power off, log in, run tools, copy files, or attribute an attacker unless the playbook/incident lead authorizes it. Every action can change evidence. Attribution requires multiple intelligence and investigative sources and is rarely an entry-level technician's decision.

### Communication and documentation

Maintain a UTC-aware timeline with source, observation, confidence, decision, approval, action, result, and next owner. Separate facts from hypotheses. Use approved out-of-band communication if the primary environment may be compromised. Share only with need-to-know roles and follow regulatory/customer/law-enforcement communication authority.

After recovery, identify root and contributing causes, control/detection/process gaps, what worked, corrective owners/dates, metrics, and how to test improvements. A blameless review still assigns accountable actions.

---

## Integrated scenarios

### Scenario 1: Repeated impossible-travel sign-ins

Preserve the identity-provider alert, times, source locations/addresses, user/device/session/MFA evidence and correlated mailbox/cloud activity. Verify travel/VPN context through approved channels. If compromise is credible, escalate and use the identity playbook for session revocation, account protection, clean-path credential recovery, scope review and monitoring. Do not claim location proves a person.

### Scenario 2: Endpoint protection quarantines a file

Record device/user/time/file/path/hash/detection and alert details. Determine business impact and whether execution, persistence, network activity or peer detections exist. Follow approved isolation and escalation. Preserve evidence before reimage/removal, address the delivery vector and credentials, recover known-good service, and monitor. Quarantine alone is not closure.

### Scenario 3: Critical scanner finding on an Internet service

Confirm authorization, asset ownership, exposed version/configuration and whether the finding applies. Combine severity with Internet exposure, business criticality, data, available exploit/threat evidence and compensating controls. Assign emergency mitigation/patch/change with rollback and validation. Preserve the risk decision and retest; never exploit production merely to “prove” it.

---

## Hands-on evidence labs

Use only disposable systems, accounts, captures, and logs you own or are explicitly authorized to inspect.

1. **Risk chain:** Create five asset–threat–vulnerability scenarios. Classify likelihood, impact, control type/function, residual risk, owner and validation evidence.
2. **Identity review:** In a lab tenant or local VMs, compare normal and privileged accounts, group/role membership, MFA/recovery, stale access and logging. Produce least-privilege recommendations without changing production.
3. **Crypto decisions:** For password storage, website transport, disk theft, software integrity and signed email, choose encryption/hash/signature/key controls and explain limitations.
4. **Network defense:** Build a small segmented Packet Tracer or VM topology. Document allowed flows, default-deny policy, secure management, DNS/DHCP evidence and both positive/negative tests.
5. **Endpoint baseline:** Collect sanitized process/service/listener/update/firewall/security-log evidence from a disposable Windows or Linux VM and compare it with a written baseline.
6. **Vulnerability lifecycle:** Run an authorized local vulnerability/configuration assessment, validate three findings, reprioritize with asset context, plan treatment, remediate one safely and retest.
7. **Event triage:** Generate benign failed logins and a blocked connection in a lab. Build a synchronized timeline across endpoint/authentication/firewall logs; document what each source can and cannot prove.
8. **Tabletop incident:** Work a simulated phishing-to-malware event. Record intake, severity, escalation, evidence/chain of custody, containment approval, recovery validation, communication and corrective actions.

## Readiness checks

1. Distinguish asset, threat, threat actor, vulnerability, exploit, event, incident and risk.
2. Compare inherent and residual risk with one concrete control chain.
3. Explain confidentiality, integrity, availability, authenticity, accountability and non-repudiation.
4. Classify controls by administrative/technical/physical and preventive/detective/corrective/recovery function.
5. Why is two passwords not MFA?
6. Apply least privilege, need to know, separation of duties and RBAC to one help-desk scenario.
7. Compare symmetric encryption, asymmetric cryptography, hashing, salting and digital signatures.
8. What does TLS protect, and what endpoint/certificate assumptions remain?
9. Classify phishing, on-path attack, credential stuffing, DDoS, insider risk and tailgating by mechanism/evidence.
10. State the authorization and ethical checks before a scan or capture.
11. Trace Ethernet/IP/TCP/HTTPS and identify a defensive observation at each layer.
12. Explain how DNS, DHCP, ARP, routing and NAT can appear in an investigation.
13. Compare router ACL, stateful firewall, IDS, IPS, proxy, VPN and NAC.
14. Why can a VPN protect transit while still admitting a compromised endpoint?
15. Design three network segments and justify the minimum flows between them.
16. Build a secure small-office wireless baseline with recovery.
17. Explain why SSID hiding is not access control.
18. What context must accompany a source IP before attributing user activity?
19. Choose logs for an authentication, DNS, malware and blocked-egress investigation.
20. Design a packet capture that is authorized, minimized, protected and disposable.
21. Write an endpoint baseline covering identity, software, services, network, update, protection, logging and recovery.
22. Distinguish policy/configuration intent from observed compliant state.
23. Plan a staged patch with test, backup, rollback and validation.
24. Why is malware quarantine not proof of full remediation?
25. What endpoint evidence is volatile, and why might collection order matter?
26. Describe a scoped vulnerability-assessment lifecycle from authorization through retest.
27. Why should business context sometimes override raw scanner severity order?
28. Assess threat intelligence for reliability, relevance, timeliness and confidence.
29. Build a risk record with treatment owner, due date, residual risk and acceptance authority.
30. Compare business continuity, disaster recovery and incident response.
31. Explain RTO and RPO using one recoverable service.
32. Walk through preparation, detection/analysis, containment, eradication, recovery and lessons learned.
33. Which conditions require immediate escalation from an entry-level technician?
34. What does chain of custody record, and what does a hash establish?
35. Write a timeline that separates observation, hypothesis, decision, approval, action and result.
36. Given an alert, can you state scope, evidence, confidence, safe next action, owner and closure criteria without overclaiming?

### Check key

Strong answers connect business/asset context to threat, exposure, control, evidence, response, recovery and residual risk. They distinguish detection from proof, containment from eradication, and scanner severity from contextual priority. Labs must show written authorization, minimized data, timestamps, original evidence, reversible changes, validation, escalation, and safe disposal.

---

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick the explanation, lab environment, book, or assessment that fits your gaps; keep Cisco's current topics and training objectives as authority. Times are provider values where published and otherwise labeled estimates.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [Cisco exam page and exam topics](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-cybersecurity.html) | Public | 30–60 min | Establish current exam identity, logistics and work areas before and after study |
| [Cisco Junior Cybersecurity Analyst Career Path](https://skillsforall.com/career-path/cybersecurity?courseLang=en-US&userLang=en-US) | Free account | About 120 h | Primary first-party path; account/region/language behavior can vary |
| [Cisco course objectives and outline](https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/ccst-cybersecurity.html) | Public | 20–40 min | Turn every official training outcome into an evidence checklist |
| [Cisco CCST Cybersecurity training overview](https://www.cisco.com/c/dam/en_us/training-events/training/courses/ccst-cybersecurity.pdf) | Public | 20–40 min | Compact first-party objective/outline and exam-description reference |
| [Cisco Networking Academy catalog](https://www.cisco.com/site/us/en/learn/training-certifications/training/netacad/index.html) | Free account | Choose by gap | Add networking/Packet Tracer foundations where TCP/IP and infrastructure are weak |
| [Cisco Press Official Cert Guide on O'Reilly](https://www.oreilly.com/library/view/cisco-certified-support/9780138204006/) | Paid | About 11 h 43 min reading estimate plus practice | Approved 2024 guide with Pearson practice and update program; verify live topics |
| [Pluralsight Information and Cyber Security Foundations](https://www.pluralsight.com/paths/information-and-cyber-security-foundations) | Paid/trial | About 37 h | Broader hands-on endpoint/network foundation with labs; not an exam-specific path |
| This guide's eight labs and 36 checks | Public | 14–22 h | Convert terminology into safe evidence, risk and response decisions |

Use practice assessments to locate gaps, not memorize item patterns. Prefer Cisco/NetAcad assessment and the companion Pearson practice from a legitimately obtained Cisco Press guide. Reject recalled/live questions, “verified exam” dumps, answer-only banks, stealth scanning labs, and any material that asks you to exceed written authorization.
