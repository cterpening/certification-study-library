---
exam_code: SSCP
vendor_id: isc2
official_blueprint: https://www.isc2.org/certifications/sscp/sscp-certification-exam-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# ISC2 Systems Security Certified Practitioner (SSCP) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The October 1, 2025 outline, claims, links, credential contract and exam-integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#sscp-coverage-record).

**Current baseline:** The October 1, 2025 SSCP outline is active. The CAT exam is two hours with 100–125 multiple-choice/advanced items, 700/1000 passing, and English, Japanese and Spanish delivery at Pearson VUE.<br>
**Upcoming change:** No later revision or retirement announcement was present on the checked outline September 2, 2026.<br>
**Exam versus certification:** ISC2 requires one year of full-time experience in at least one current SSCP domain; an applicable post-secondary degree can satisfy up to one year, and part-time work/internships may count under current rules. A passer without qualifying experience can become an Associate of ISC2 and has two years to earn it. Verify endorsement/application details.<br>
**Maintenance:** Current policy lists 60 CPEs over the three-year SSCP cycle and a USD 135 member AMF; Associates have separate annual requirements. Confirm fees and policy before registration.

## How to use this guide

SSCP is an operator credential. For each control, practice the complete loop: approved requirement → baseline/configuration → safe change → positive and negative validation → centralized evidence → alert/triage → repair/recovery → documented review. Use disposable local/cloud labs and synthetic data. Never scan, exploit, intercept or modify systems without explicit authorization and rules of engagement.

> **About related items:** A `Related item:` callout adds prerequisite, architectural or operational context. It supports the topic but does not assert that ISC2 used the wording in the public outline.

## Domain map

| Domain | Weight | Operator evidence |
|---|---:|---|
| 1. Security Concepts and Practices | 16% | Policy-to-control record, owned asset/configuration baseline, approved change, awareness/physical coordination and ethical evidence |
| 2. Access Controls | 15% | Identity lifecycle, authentication/federation/trust, entitlement decision, access review, denial and attributable logs |
| 3. Risk Identification, Monitoring and Analysis | 15% | Scoped assessment, contextual vulnerability/risk record, platform telemetry, correlation, threshold, escalation and remediation validation |
| 4. Incident Response and Recovery | 14% | Evidence-preserving response, forensic support, communications, clean recovery and BCP/DR measurement |
| 5. Cryptography | 9% | Approved algorithm/protocol/key lifecycle, certificate validation and failure/rotation/revocation evidence |
| 6. Network and Communication Security | 16% | Packet/control path, segmented policy, device/service configuration, monitoring and safe troubleshooting |
| 7. Systems and Application Security | 15% | Hardened endpoint/mobile/cloud/virtual baseline, malware/activity response, patch/change and recovery evidence |

---

## 1. Security Concepts and Practices — 16%

Apply the ISC2 and organizational codes of ethics when handling access, evidence, disclosure, competence and public trust. A technically possible action is not necessarily authorized or ethical. Stop when scope is unclear, preserve evidence, report conflicts and escalate material risk through approved channels.

Confidentiality, integrity and availability connect to accountability, authenticity, non-repudiation, privacy, least privilege and separation of duties. Map a threat/vulnerability to risk before selecting administrative, technical and physical controls. Classify controls by function—preventive, detective, corrective, deterrent, recovery, compensating or directive—and show what evidence demonstrates operation.

Document control owner, purpose, scope, dependency, configuration, test, exception and review date. Functional evidence is more than “enabled”: validate desired activity and denied/misuse paths, telemetry and failure behavior. Asset management covers procurement/onboarding, ownership/classification, inventory/configuration, use/change, maintenance and secure retirement/disposal for hardware, software and data. Include cloud resources, identities, certificates, containers and AI models/services.

Change management requires request, risk/impact, dependencies, approval, tested implementation, validation, communication, rollback and record update. Emergency change shortens the path but does not erase authorization or retrospective review. Configuration management establishes known baselines and detects drift.

Awareness is role- and threat-specific: phishing/social engineering, password/MFA, data/AI handling, reporting and exercises. Measure behavior and report time, not only attendance. Coordinate physical access, badges/visitors, device/media restrictions, environmental monitoring and safety with facilities; do not defeat a physical control to make IT administration easier.

**Related item:** Policies state management intent; standards define mandatory requirements; procedures explain execution; guidelines advise. Control evidence should trace back through this hierarchy.

---

## 2. Access Controls — 15%

Identification names an entity; authentication verifies it; authorization applies permissions; accounting records activity. Use MFA with independent factor types and protect enrollment, recovery, tokens and sessions. Compare passwords, hardware/software tokens, certificates, biometrics, one-time codes and passwordless methods by threat, assurance, usability and lifecycle—not novelty.

Federation establishes cross-domain identity trust; SSO reuses an authenticated session across services. Protocols such as SAML, OAuth and OpenID Connect serve different authentication/authorization delegation purposes. Validate issuer/audience, signing/encryption, redirect/replay/session behavior and claim-to-role mapping. A trusted identity provider compromise or bad claim mapping can expand blast radius.

Manage joiner/mover/leaver plus contractors, service/workload, privileged, shared and emergency accounts. Establish owner, source, approval, role/attribute, expiration, credential rotation and review. Deprovision active sessions, tokens/keys, groups, devices and downstream/federated accounts. Use privileged-access controls and just-in-time/time-bounded elevation when supported.

Apply DAC, MAC, RBAC, rule- and attribute-based models appropriately. Least privilege, need-to-know, separation of duties, default deny and periodic recertification limit excess access. Detect orphaned/dormant accounts and toxic combinations. Validate from both permitted and prohibited users; protect access logs and time sources.

**Related item:** Zero Trust continually evaluates identity, device/workload, resource and context and assumes breach. Federation, network location or a successful login alone should not create permanent implicit trust.

---

## 3. Risk Identification, Monitoring and Analysis — 15%

Maintain asset/business context, threat, vulnerability, likelihood, impact, existing control, inherent/residual risk, treatment, owner and due date. Quantitative approaches estimate loss/frequency; qualitative approaches use defined ratings. Neither removes uncertainty. Risk appetite/tolerance comes from authorized leadership; operators surface evidence and implement treatment.

Identify applicable jurisdiction, privacy, contractual, licensing, retention, notification and third-party requirements with legal/compliance input. Data location, cloud provider and user/customer geography can change obligations. Preserve minimum necessary evidence and approved chain of custody.

Security assessments include architecture/configuration review, control testing, vulnerability scanning, code/dependency analysis, penetration tests and audits at authorized scope. A scanner finding needs asset/version/reachability/exposure/control context and validation; CVSS is input, not business priority. Remediate, mitigate, accept, transfer or avoid under ownership, then rescan/retest and close with evidence. Do not test production exploitability merely to raise confidence.

Operate telemetry from endpoint, identity, network, DNS, cloud, application, database and physical systems. Normalize time/identity/asset context; protect collection, transport, access, retention and integrity. SIEM aggregates/searches/correlates; EDR observes/responds at endpoints; IDS/IPS and network analytics observe/control paths; DLP identifies/controls sensitive movement. Health monitoring must distinguish “sensor quiet” from “environment safe.”

Analyze baseline/deviation, rule/signature, behavior, threat-intelligence enrichment and multi-source correlation. Tune false positives without suppressing true attack paths. Define severity/priority, threshold, owner, runbook and escalation; retain query/event IDs. AI-assisted detection can rank or correlate but requires quality/drift/bias monitoring and human validation.

**Related item:** A risk register is forward-looking governance; vulnerability management handles weaknesses; detection engineering creates observable signals; incident response acts when evidence crosses a response threshold.

---

## 4. Incident Response and Recovery — 14%

Prepare policies, roles, severity, contacts, authority, tooling, logging, evidence storage, communications and playbooks. Detection/analysis validates what occurred, affected identities/assets/data, time and business impact. Containment limits harm with reversible short-term actions and durable long-term measures. Eradication removes cause/persistence; recovery restores clean service and heightened monitoring; lessons learned fixes control and plan gaps.

Record who did what, when, where and why. Preserve original evidence, hashes where appropriate, acquisition method, secure storage and every transfer. Volatile evidence may disappear quickly; follow authorized forensic procedure and order of volatility. Do not power off, image, interrogate or disclose a system outside authority. Separate facts, hypotheses and conclusions.

Support forensic acquisition/analysis across host, memory, network, mobile, cloud and logs while maintaining legal/HR/privacy coordination. Time synchronization and contextual identity/asset records are essential. Communicate by need-to-know through approved out-of-band channels if normal channels may be compromised.

BC keeps critical processes operating; DR restores technology/data. Use BIA, maximum tolerable downtime, RTO and RPO to prioritize. Test alternate process/site, dependency order, identity/DNS/network, immutable/offline backups and restoration. Validate integrity and security before returning service; monitor for recurrence. Exercises range from checklist/walkthrough/tabletop to simulation and technical failover/restoration.

**Related item:** Containment can destroy availability or evidence. Choose the least harmful action that satisfies authority and risk, document the tradeoff and preserve a path to recovery.

---

## 5. Cryptography — 9%

Select cryptography for confidentiality, integrity, authenticity, non-repudiation and data sensitivity/obligation. Symmetric encryption is efficient for bulk data but requires shared-key protection. Asymmetric cryptography enables key exchange/signatures and other cases but costs more. Hashes support integrity/password constructions and are not encryption; salts defeat precomputed password hashes; HMAC combines secret and hash for integrity/authentication.

Use approved algorithms, modes and key lengths; do not design custom crypto. Account for entropy/random generation and future quantum risk through inventory and crypto-agility, not unsupported “quantum-safe” claims. Encrypt data at rest, in transit and, where needed, in use with clear trust boundaries. TLS, IPsec/VPN, SSH, secure mail/file and Wi-Fi protocols have different layers and purposes.

PKI connects certificate subjects, public keys, issuers/CAs, registration/validation, chains, trust stores, validity, name/usage constraints and revocation/status. Validate the entire chain, hostname/identity, time and intended usage. Manage keys through generation, storage, distribution, rotation, backup/recovery where allowed, revocation, expiration and destruction. Protect CA/HSM/admin roles and log sensitive operations.

**Related item:** Encryption without authentication can permit tampering; signatures without protected private keys do not establish trustworthy origin; a valid certificate does not make application content safe.

---

## 6. Network and Communication Security — 16%

Trace user/workload → name resolution → route → transport → proxy/firewall/load balancer → service and return path. Relate OSI/TCP-IP layers, IPv4/IPv6, subnet/VLAN, switching/routing, TCP/UDP, ports, DNS/DHCP/NTP and application protocols. Capture read-only state and authorized packet/log evidence before changing configuration.

Recognize DDoS, on-path interception, spoofing, DNS poisoning, scanning, route/ARP manipulation, wireless attacks and protocol abuse by prerequisite, observable effect and defensive layer. Do not memorize attack names without detection/containment. Apply segmentation/DMZ/micro-segmentation, NAC, firewalls, proxies, IDS/IPS, VPN, DNS/email/web controls and secure management planes under least privilege and change control.

Harden routers, switches, firewalls and appliances: supported software, secure admin protocols, centralized AAA, role separation, configuration backup, NTP, logs/telemetry, unused-service/port shutdown, routing/control protection and reviewed rules. A rule needs business owner, source/destination/service/action, time/expiry and validation. Diagnose by layer and roll back if impact exceeds plan.

Secure wireless with current authentication/encryption, protected management, separate guest/IoT paths, RF/rogue monitoring and controlled provisioning. Treat Bluetooth/NFC/cellular/satellite and IoT/OT by range, pairing/identity, update, safety/availability and monitoring constraints.

**Related item:** Network segmentation limits paths and blast radius; identity limits subjects/actions; encryption protects content. None replaces endpoint/application security or monitoring.

---

## 7. Systems and Application Security — 15%

Analyze malicious code/activity—virus, worm, Trojan, ransomware, rootkit, backdoor, bot, script/macro/fileless behavior—by execution vector, persistence, privilege, command/control, impact and observable artifacts. Use layered prevention, application control, EDR/anti-malware, patching, least privilege, segmentation, backups and user reporting. Quarantine/contain under an incident plan; do not delete evidence first.

Build endpoint baselines for firmware/boot, OS support/patch, accounts/services, host firewall, storage encryption, application control, anti-malware/EDR, logging, backup, device/media controls and secure configuration. Manage vulnerability/change cycles and exceptions. Servers, desktops, kiosks and specialized/legacy systems need different availability and application constraints.

Mobile device management/unified endpoint management handles enrollment, inventory, policy, encryption, lock, application/work profile, update, compliance, remote action and retirement. Compare corporate-owned, BYOD and other ownership models by privacy, support and control. Protect loss/theft, insecure apps/networks, rooting/jailbreak and backup/cloud synchronization.

For cloud, map SaaS/PaaS/IaaS shared responsibility; secure tenant hierarchy, IAM/federation, network, data/key/secrets, compute/container/serverless configuration, logging/posture, image/dependency supply chain, backup and incident evidence. Do not assume provider certification secures customer configuration.

Virtualization separates guests through a hypervisor but adds management plane, image/snapshot, virtual network/storage, sprawl and escape risks. Containers share host kernel and need trusted minimal images, registry/provenance, runtime identity, secrets, network policy, resource limits and scanning. Test resilience and restore of configurations/data, not just instance restart.

Application security includes secure requirements/design/threat modeling, reviewed code/dependencies, SAST/DAST and controlled testing, input validation, parameterized queries, output encoding, session/authz, secrets, logging and release/rollback. Treat AI models/prompts/tools as application assets with data leakage, poisoning, injection and excessive-agency risks.

**Related item:** A golden image accelerates recovery only if its provenance, patches, secrets, configuration and deployment automation remain governed and tested.

---

## Integrated scenarios

### Scenario 1: Joiner-to-leaver operations

Provision a synthetic administrator through federation/MFA and time-bounded role access; record approval and positive/negative tests. Monitor authentication/admin/configuration logs, change one firewall rule through rollback-aware process, review access, then deprovision sessions, keys and downstream rights.

### Scenario 2: Endpoint ransomware incident

Triage synthetic EDR, identity, DNS and file events; validate severity/scope and contain with evidence preservation. Identify vulnerable configuration, coordinate communications, restore a clean system/data to RTO/RPO, heighten monitoring and retest the corrected baseline.

### Scenario 3: Hybrid service hardening

Map on-prem network, VPN, cloud IaaS/container and mobile access. Classify data, threat-model identities/paths/images/secrets, implement layered control plan, centralize logs, scan/configuration-review safely and tabletop provider/account compromise plus certificate rotation.

## Hands-on evidence labs

1. **Control/asset baseline:** Inventory a disposable host and data, map policy/control/owner, harden it, validate allowed/denied behavior and detect drift.
2. **IAM/trust:** Configure local or cloud-lab users/roles/MFA/federation simulation; test join/move/review/leave, privilege and logs.
3. **Risk/vulnerability:** Run an authorized scanner/configuration assessment, contextualize findings, choose treatment and prove remediation/retest.
4. **Monitoring:** Forward safe host/identity/network logs to a local analysis tool; build/tune one correlation and document sensor health, threshold and escalation.
5. **Incident/forensics:** Analyze provided images/logs, preserve hashes/chain of custody, write timeline/hypotheses and execute a tabletop containment/recovery.
6. **Crypto/PKI:** Create a lab CA/certificate, inspect chain/name/usage/expiry, configure TLS, simulate expiry/revocation/rotation and protect keys.
7. **Network/system:** Segment a virtual network, apply reviewed rules and secure administration; harden a VM/container/mobile-policy design and validate telemetry/recovery.
8. **Operator evidence pack:** Assemble asset/risk/access/change/vulnerability/log/incident/restore records, owners, exceptions and cleanup.

## Readiness checks

1. Can you apply ethics when authority or evidence is unclear?
2. Can you map CIA/accountability/privacy to a real control?
3. How do control form and function classifications differ?
4. What proves a control is functional?
5. What belongs in hardware/software/data asset lifecycles?
6. What separates standard and emergency change?
7. How do awareness outcome measures improve on completion counts?
8. What physical/facility dependencies require coordination?
9. How do identification, authentication, authorization and accounting connect?
10. Why do SSO and federation differ?
11. What must be validated in SAML/OAuth/OIDC trust?
12. Can you deprovision sessions, tokens, keys and downstream accounts?
13. How do access models and least privilege/SoD differ?
14. Who owns risk acceptance and exception expiration?
15. How do jurisdiction, privacy and contracts affect operation?
16. How do assessment, scan, penetration test and audit differ?
17. How do you prioritize and close a vulnerability with evidence?
18. How do SIEM, EDR, IDS/IPS and DLP differ?
19. How do you prove monitoring sensors are healthy?
20. What makes an alert actionable and tuned safely?
21. What authority and evidence belong in each response phase?
22. How do original evidence, hash and chain of custody connect?
23. How do BCP, DRP, BIA, RTO and RPO differ?
24. How do you validate clean recovery and recurrence monitoring?
25. When do symmetric, asymmetric, hash, salt and HMAC fit?
26. What makes an algorithm/protocol approved and configured safely?
27. What does a certificate chain validate?
28. What belongs in complete key lifecycle management?
29. Can you trace DNS/IP/route/TCP/firewall/TLS/service paths?
30. How do network attacks appear in evidence and controls?
31. What makes a firewall rule governed and testable?
32. What belongs in a secure appliance management plane?
33. How do wireless, IoT and OT constraints differ?
34. Can you classify malicious activity by behavior and artifact?
35. What belongs in an endpoint/mobile baseline?
36. How does cloud service model shift shared responsibility?
37. How do VM and container isolation/lifecycle differ?
38. What application security gates belong before release?
39. Can you map all seven domains to operator evidence?
40. Have you reconciled courses/books with the October 2025 outline?

### Check key

- **Ready:** You can implement, validate, monitor, fail and recover the control safely.
- **Review:** You recognize the control but cannot produce configuration/evidence or explain failure.
- **Gap:** You guessed or relied on an older outline. Return to the current official scope and lab.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Use the outline plus one primary route, then select labs, practice or references for gaps. Access, durations and revisions were checked September 2, 2026 and can change.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [Current SSCP exam outline](https://www.isc2.org/certifications/sscp/sscp-certification-exam-outline) | Public | 3–6h mapping + review | Canonical October 1, 2025 domains, weights, detailed topics, CAT and experience contract. |
| [ISC2 SSCP self-study resources](https://www.isc2.org/certifications/sscp/sscp-self-study-resources) | Public/account/paid links | 1–2h selection; variable study | Official path to outline, adaptive training, flash cards and Study Hub. |
| [Official adaptive SSCP training](https://www.isc2.org/training/online-self-paced/sscp-online-self-paced) | Paid/account | 35–50h estimate + 30–50h labs | Current adaptive route with official textbook/questions, assessments and 90/180-day options; no public fixed completion duration, so plan by progress. |
| [Pluralsight SSCP path](https://www.pluralsight.com/paths/sscpr-systems-security-certified-practitioner-certification) | Paid/trial | 14h + 25–40h labs | Eight courses plus practice. Page references a September 2024/older outline; close October 2025 and AI-security deltas officially. |
| [LinkedIn Learning/Cybrary SSCP Cert Prep](https://www.linkedin.com/learning/isc2-systems-security-certified-practitioner-sscp-cert-prep) | Paid/trial | 6h + 20–35h labs | August 2025 seven-domain overview with transcripts; verify October 2025 revisions and use its separate practice exams only for rationale. |
| [O'Reilly/Sybex SSCP Official Study Guide, 3rd Edition](https://www.oreilly.com/library/view/isc-2-sscp-systems/9781119854982/) | Paid/trial or book | 29h16m + 25–40h labs | Deep 2022 reference; substantially pre-dates the current outline, so use selectively and close every objective delta. |
| [Udemy — Ultimate ISC2 SSCP Masterclass](https://www.udemy.com/course/sscp-training-english-isc2/) | Paid | 27h15m + 25–40h labs | August 2026 operational course; confirm its objective map and validate technical claims with current authoritative sources. |
| [ISC2 member policies](https://www.isc2.org/policies-procedures/member-policies) | Public | 45–90m | Current SSCP/Associate CPE, cycle and AMF requirements; policy rather than exam content. |
| [ISC2 Code of Ethics](https://www.isc2.org/ethics) | Public | 30–60m + scenarios | Apply the first-party canons to authority, evidence, disclosure, competence, conflicts and public trust. |

Avoid recalled questions, “actual exam” banks and guaranteed passing. Practice should be original and teach the operational rationale. CAT delivery requires answering in sequence without backtracking, so practice making a defensible decision once and continuing.
