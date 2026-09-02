---
exam_code: CC
vendor_id: isc2
official_blueprint: https://www.isc2.org/certifications/cc/cc-certification-exam-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# ISC2 Certified in Cybersecurity (CC) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 1, 2026 outline, material claims, links, credential lifecycle and exam-integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#cc-coverage-record).

**Current baseline:** The September 1, 2026 CC outline is active. The CAT exam is two hours, 100–125 items, multiple-choice and advanced item types, with 700/1000 passing at Pearson VUE. It is available in English, Chinese, Japanese, German and Spanish, with appointment-window limits stated for Chinese.<br>
**Upcoming change:** No later revision or retirement announcement was present on the checked outline September 2, 2026.<br>
**Credential boundary:** CC requires no work experience. Passing the exam is still followed by the ISC2 certification/member process, Code of Ethics and maintenance requirements. Current member policy lists 45 CPEs over three years and a USD 50 annual maintenance fee for CC-only members; verify policy and fees before registering.<br>
**Freshness warning:** Material mapped to the pre-September outline can miss the new Security Governance domain, revised IAM/network-cloud/operations structure, metrics/testing and embedded AI-security guidance. Match every resource to the 2026 outline.

## How to use this guide

Learn each term as part of a decision chain: asset or business process → threat and vulnerability → likelihood/impact → chosen control → implementation owner → observable evidence → response/recovery. CC tests foundational understanding, but “foundational” should not mean memorizing disconnected acronyms. Practice explaining why a control protects confidentiality, integrity or availability and what remains at risk.

Use only systems, accounts and labs you own or are authorized to test. Blue-team observation, configuration review, tabletop response and synthetic evidence are enough. Do not scan, phish, exploit or access another party's system without written authorization.

> **About related items:** A `Related item:` callout adds prerequisite, operational or adjacent context. It supports understanding but does not assert that ISC2 used that exact wording in the public CC outline.

## Domain map

| Current domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Security Principles | 24% | Explain CIA/AAA/privacy/non-repudiation, risk and governance hierarchy, control categories, due care/diligence and ethical escalation |
| 2. Security Governance | 17.3% | Connect GRC, BC/DR, awareness and metrics/KRIs to accountable decisions and tested resilience |
| 3. Identity and Access Management Concepts | 20% | Trace identity lifecycle and enforce least privilege, separation of duties and appropriate access-control models |
| 4. Networking and Cloud Security Concepts | 21.3% | Trace traffic through models, protocols and controls; explain segmentation, defense in depth, Zero Trust and shared cloud responsibility |
| 5. Security Operations and Incident Response | 17.3% | Handle data/assets, triage evidence, threat context, incident plans/exercises and authorized security testing |

---

## 1. Security Principles — 24%

### Protect the right property

Confidentiality limits disclosure to authorized subjects; integrity protects correctness, completeness and authorized change; availability keeps approved services/data usable when needed. Controls often affect more than one. Encryption can protect confidentiality and, with authenticated modes or signatures, support integrity/authenticity, but it does not ensure a service remains available. Backups support recovery only when protected, complete and tested.

Authentication establishes a claimed identity, authorization decides permitted access, and accounting records attributable activity. Non-repudiation supplies evidence strong enough that an action cannot credibly be denied, commonly through identity, digital signatures, protected audit trails and process controls. Privacy concerns the appropriate collection, use, sharing, retention and rights around personal data; security is necessary but not sufficient for privacy.

For AI systems, apply the same principles to models, training/retrieval data, prompts, tools, outputs and logs. Poisoned data threatens integrity; exposed prompts or training records threaten confidentiality/privacy; an uncontrolled agent action needs authentication, authorization and accounting. AI does not change the duty to follow policy and law.

### Reason about risk and controls

An asset has value; a threat can cause harm; a vulnerability is a weakness; a control changes likelihood or impact. Risk assessment identifies and analyzes risk against appetite/tolerance. Treatment options include avoid, mitigate, transfer/share and accept. Acceptance belongs to the authorized risk owner—not whoever found the issue or wants to close a ticket. Residual risk remains after controls; inherent risk is considered before them.

Administrative controls include policy, training and process; technical controls include identity, encryption and filtering; physical controls include locks, barriers, guards and environmental protection. Controls may also be preventive, detective, corrective, deterrent, compensating, recovery or directive. Classify by what the question asks: implementation form and security function are separate axes.

Defense in depth layers independent controls so one failure is not decisive. Least privilege grants only needed access for an appropriate time; separation of duties divides incompatible steps. Neither means “deny everyone.” Availability, usability, cost and business need still belong in the decision.

### Connect governance documents and conduct

Laws/regulations are externally imposed obligations; frameworks organize practices; policies state management intent; standards define mandatory requirements; procedures give repeatable steps; guidelines provide recommended discretion. A procedure should implement a policy/standard, and evidence should show it was followed. Know that ISO and CIS are examples in the outline, but study the purpose of a framework/control baseline rather than assuming one applies universally.

Due care is the reasonable protective action expected; due diligence is the continuing investigation, validation and attention that informs it. Follow the ISC2 Code of Ethics and organizational code, law and authorized process. Preserve evidence, avoid conflicts, escalate material risk and do not conceal a mistake. If obligations conflict, document and seek authorized legal/management guidance rather than improvising.

**Related item:** Risk appetite is the broad amount/type of risk an organization is willing to pursue or retain; tolerance defines acceptable variation or limits in a particular context.

---

## 2. Security Governance — 17.3%

### Plan GRC as an accountable system

Governance sets direction, decision rights and accountability. Risk management identifies/analyzes/treats/monitors uncertainty. Compliance demonstrates applicable obligations. A GRC tool can register risks, controls, evidence, exceptions and owners, but it does not create sound governance by itself.

Create a traceable chain from obligation/objective to policy/control, implementation owner, evidence, assessment result, exception, remediation and reporting. Record scope and date. Distinguish a missing control, a control that exists but is ineffective, and a control that works but lacks evidence. Key risk indicators warn about exposure; performance/control metrics show activity or effectiveness. A dashboard should name definition, source, time window, threshold, owner and action.

### Preserve business service through disruption

Business continuity keeps critical processes operating at an acceptable level; disaster recovery restores technology/data after disruption. A business impact analysis identifies critical processes, dependencies, impact over time and recovery priorities. Recovery time objective is the target duration to restore; recovery point objective is the acceptable data-loss window. Maximum tolerable downtime is a business limit, not automatically equal to RTO.

Redundancy reduces single points of failure across power, network, compute, storage, sites, people and suppliers, but replicated corruption or compromised credentials can also spread. Backups need protected copies, retention, restoration testing and accountable ownership. Hot/warm/cold recovery options trade readiness, cost and restoration effort. Plans must include communications, roles, alternate processes, dependencies and return-to-normal.

Exercise plans with walkthroughs/tabletops and technical recovery tests at authorized depth. A paper success does not prove data restores, identities work or dependencies start in order. Capture actual recovery time/point, missing contacts, failed dependencies and corrective actions.

### Build awareness and measure it

Security awareness is continuous and role-based. Teach reporting, password/MFA behavior, data handling, social engineering/phishing and safe AI use. Executives, developers, administrators and general users face different decisions. Culture improves when reporting is easy and people are not punished for raising a concern in good faith.

Measure outcomes, not only course completion: report rate, time to report, repeat risky behavior, overdue remediation, restore success, privileged-access review exceptions or phishing susceptibility—with privacy and interpretation controls. A single metric can be gamed or misunderstood; use trends and complementary measures.

**Related item:** An incident-response plan handles security events; BC keeps priority business services running; DR restores technology. One event can invoke all three, but their objectives and owners differ.

---

## 3. Identity and Access Management Concepts — 20%

### Manage the whole identity lifecycle

Define roles and entitlement needs before provisioning. Joiner/mover/leaver processes create, change, review and remove access using an authoritative identity source and approvals. Temporary, third-party, service and emergency accounts need owners, expiration and review. Deprovision interactive access, sessions/tokens/keys, group memberships, devices and downstream accounts; disabling one directory account may not revoke every path.

Authentication factors are something you know, have or are; multifactor authentication uses different factor types. Strong authentication still needs secure enrollment, recovery, device/token protection and resistance to social engineering. Federation lets one identity authority support another service; single sign-on improves usability and central control but increases dependency on the identity provider.

Access reviews compare current business need to actual entitlements. Review privileged, toxic combinations, inactive/orphaned and exception access with accountable decisions. Logs show use but do not prove continued need. Bots and AI agents are workload identities and require the same owner, lifecycle, minimum scope, credential rotation and traceability.

### Apply logical access-control principles and models

Least privilege limits permissions; need-to-know limits information access; separation of duties prevents one identity from controlling incompatible stages. Privileged access should be separately administered, monitored and time-bounded where appropriate. Default deny and explicit grants reduce accidental exposure.

Discretionary access control lets an owner determine access. Mandatory access control uses centrally enforced labels/classifications and clearances. Role-based access control grants through job functions; rule-based control evaluates system rules/conditions; attribute-based access control evaluates subject, resource, action and environment attributes. Real systems combine models. Select by governance, scale, context, sensitivity and auditability.

Authorization must be enforced at every material resource, not only the user interface. Test positive access and negative denial. Protect access logs from unauthorized change, synchronize time, and investigate impossible travel or anomalous behavior as signals rather than automatic proof of compromise.

**Related item:** Zero Trust is not an access-control model in this list. It is an architecture/strategy that continually evaluates explicit trust signals, uses least privilege and assumes breach across identity, device, workload and resource paths.

---

## 4. Networking and Cloud Security Concepts — 21.3%

### Trace the path before naming the control

The OSI and TCP/IP models are troubleshooting abstractions. At a practical level, relate physical/link media and frames/MACs, network-layer IP/routing, transport-layer TCP/UDP/ports and application protocols. IPv4 and IPv6 identify interfaces; routers forward between networks; switches commonly forward within a LAN/VLAN; DNS resolves names; DHCP supplies configuration. A port identifies a service endpoint, not proof that the service is safe.

TCP is connection-oriented and provides ordered reliable delivery; UDP is connectionless with lower protocol overhead and application-dependent reliability. VPNs protect traffic across an untrusted path when correctly authenticated/configured. TLS protects supported application sessions. Never equate “encrypted” with authorized or benign.

Firewalls apply policy to traffic by address, port, protocol, state, application or other context depending on capability. IDS detects/alerts; IPS can block inline. Proxies mediate application connections. Segmentation limits communication and blast radius with zones, VLANs, firewalls or micro-segmentation. Validate rules from intended and forbidden paths.

Wireless and Bluetooth add radio exposure, association/authentication and configuration risks. Prefer current secure protocols, strong identity/key management, protected administration and monitoring. Embedded/ICS/IoT systems may have long lifecycles, safety/availability constraints, weak update mechanisms and vendor dependencies; inventory and isolate them rather than applying risky generic remediation.

### Layer architecture and Zero Trust

Defense in depth combines identity, endpoint, network, application/data and physical controls. A DMZ or screened zone separates internet-facing services from internal networks. Network access control evaluates devices/users before or during access. High availability and redundancy reduce single failures but require independent failure domains and testing.

Zero Trust removes implicit trust based on network location. Verify explicitly using identity, device/workload/resource and context; grant least privilege; assume breach; observe and reevaluate. Micro-segmentation can help enforce it, but buying one product does not create the architecture.

### Understand cloud responsibility

Cloud characteristics include on-demand self-service, broad network access, resource pooling, rapid elasticity and measured service. SaaS supplies a managed application; PaaS supplies a managed application platform/runtime; IaaS supplies virtualized infrastructure. Public, private, hybrid and community describe deployment/ownership patterns. “Multi-cloud” describes use of multiple providers, not a separate service model.

Shared responsibility shifts with service and provider: the provider protects defined underlying facilities/services, while the customer retains responsibilities such as data, identities, configuration, workloads and use. Verify the specific service contract. Cloud elasticity can magnify misconfiguration and cost; centralized identity, logging, configuration guardrails and tested backup/recovery remain required.

**Related item:** Segmentation controls paths; encryption protects content in defined states; IAM controls subjects/actions. Strong architecture combines them instead of asking one to replace the others.

---

## 5. Security Operations and Incident Response — 17.3%

### Protect data and assets through their lifecycle

Classify data by sensitivity and obligation, label it, apply handling requirements and track creation/collection, use, storage, sharing, retention and destruction. Masking reduces exposed detail; sanitization makes media/data infeasible to recover at the required assurance. Symmetric cryptography uses a shared secret and is efficient for bulk data; asymmetric cryptography supports key exchange/signatures and other uses; hashing is one-way integrity support, not encryption. Use approved algorithms/key sizes and manage keys separately.

Maintain asset owner, purpose, classification, location, version/configuration, dependency, support and end-of-life status. Establish secure baselines and controlled changes. Unsupported/end-of-life assets create unpatchable risk; plan replacement, isolation or formally accepted compensating controls. Detect configuration drift and preserve change evidence.

### Triage events with evidence and context

Logs record activity; monitoring evaluates it; correlation joins related signals. A SIEM centralizes/searches/correlates security data, while other tools may detect endpoint or network behavior. Normalize time and identity, protect log integrity/access/retention, and avoid collecting unnecessary sensitive content.

An event is observable activity; an alert flags a rule/model condition; an incident is an event or series that threatens policy/business and requires response. Triage validates signal, asset/user/data scope, threat, severity/priority and immediate escalation. Threat actors include insiders, criminals, nation states, activists and others with distinct motivations/capabilities. Threat intelligence should have source, relevance, confidence and freshness. Frameworks organize behavior; they do not prove attribution.

Follow the incident-response plan: preparation; detection/analysis; containment; eradication; recovery; lessons learned (names vary by framework). Preserve evidence and chain of custody, record times/actions/decision makers, communicate through authorized channels and do not destroy artifacts to restore faster. Short- and long-term containment trade business continuity against investigation and risk.

### Test readiness safely

Tabletops exercise decisions/communications; simulations and technical recovery exercises test operation. Blue teams defend, red teams emulate an adversary under rules of engagement, and purple teaming emphasizes collaboration/learning. Vulnerability scanning identifies potential weaknesses; static analysis examines code/artifacts without executing; dynamic analysis tests running behavior; threat modeling identifies design risks. Physical assessments can test tailgating, impersonation or phishing only with explicit authorization and safety controls.

Testing requires scope, owner approval, rules, time, targets, allowed techniques, stop conditions, evidence handling, communication and remediation. A finding needs asset/context, evidence, risk and owner; a scan result is not automatically an exploitable incident.

**Related item:** AI can help correlate events and identify anomalies, but analysts must validate context, bias/error and authorization. Automated confidence is not incident proof.

---

## Integrated scenarios

### Scenario 1: New employee and cloud application

Classify application data; map SaaS shared responsibility; provision a role through an approved joiner workflow with MFA and separation of duties; validate allowed/denied access and logs. Simulate job change and departure, revoke sessions and downstream entitlements, and document residual risk.

### Scenario 2: Ransomware and continuity tabletop

Given synthetic endpoint/SIEM alerts, distinguish events from incident, prioritize critical services/data, preserve evidence and invoke containment/escalation. Use BIA-derived RTO/RPO to choose alternate operation and restore a clean tested backup. Record communications, actual recovery and lessons/remediation.

### Scenario 3: Small hybrid network review

Draw user, Wi-Fi, VPN, firewall, VLAN/zone, cloud service and IoT paths. Map identity, segmentation, encryption, logging and provider/customer responsibility. Identify an end-of-life device and overbroad rule, propose least-disruptive mitigation and define positive/negative verification plus rollback.

## Hands-on evidence labs

1. **Risk/control register:** Create five synthetic asset-threat-vulnerability risks; choose treatment, owner, control types, evidence and residual-risk authority.
2. **Policy hierarchy:** Map one regulation/business need through policy, standard, procedure, guideline, control and metric; identify due care/diligence evidence.
3. **BC/DR tabletop:** Build BIA dependencies, RTO/RPO and communications; restore a harmless backup and compare measured result to target.
4. **IAM lifecycle:** In a local lab, define roles, provision/review/change/deprovision accounts and prove least privilege, denied access and log attribution.
5. **Packet path:** Use Packet Tracer or a local authorized lab to trace DNS/DHCP/TCP/TLS/VPN/firewall/VLAN concepts and explain OSI/TCP-IP layers.
6. **Cloud responsibility:** Compare SaaS/PaaS/IaaS responsibility for identity, data, configuration, patching, logging and recovery; validate against a provider service contract.
7. **Triage:** Analyze synthetic logs/alerts; record source/time/asset/user/scope, enrich with dated intelligence, prioritize/escalate and preserve evidence.
8. **Security evidence pack:** Combine asset/configuration inventory, data flow, access review, metrics dashboard, change record, safe test report and incident/restore runbook.

## Readiness checks

1. Can you distinguish confidentiality, integrity and availability impacts?
2. How do authentication, authorization and accounting differ?
3. What evidence supports non-repudiation?
4. Why is privacy broader than security?
5. How do asset, threat, vulnerability, likelihood, impact and risk connect?
6. Who may accept residual risk?
7. How do avoid, mitigate, transfer and accept differ?
8. Can you classify controls by form and by function?
9. How do laws, frameworks, policies, standards, procedures and guidelines differ?
10. How do due care and due diligence differ?
11. How would the Code of Ethics affect escalation?
12. How do governance, risk and compliance interact?
13. What makes a KRI or metric actionable?
14. How do BC, DR and incident response differ?
15. How do BIA, RTO, RPO and maximum tolerable downtime relate?
16. Why can replication spread a failure?
17. What proves a backup is recoverable?
18. How do awareness completion and outcome measures differ?
19. What are joiner, mover, reviewer and leaver controls?
20. How do you remove sessions, keys and downstream access?
21. Why are two passwords not MFA?
22. How do least privilege, need-to-know and separation of duties differ?
23. When do DAC, MAC, RBAC, rules and attributes fit?
24. Can you test positive access and negative denial?
25. Can you map OSI/TCP-IP layers to a packet path?
26. How do TCP and UDP trade behavior?
27. What do firewall, IDS, IPS, proxy and VPN each do?
28. How do VLAN/zone/micro-segmentation limit blast radius?
29. What is Zero Trust beyond a product name?
30. What security constraints make ICS/IoT different?
31. What defines SaaS, PaaS and IaaS responsibility shifts?
32. What customer responsibility remains in every cloud model?
33. How do classification, labeling, masking and sanitization differ?
34. How do symmetric, asymmetric and hashing uses differ?
35. What belongs in an asset and end-of-life record?
36. How do event, alert and incident differ?
37. What context makes threat intelligence useful?
38. What evidence and chain-of-custody discipline applies during response?
39. How do tabletop, red, blue, purple, scanning, SAST, DAST and threat modeling differ?
40. Can you map the September 2026 domains to your lab evidence?

### Check key

- **Ready:** You can explain the decision, select the control and show safe evidence.
- **Review:** You recognize terms but cannot connect them to risk, implementation and outcome.
- **Gap:** You guessed or relied on an older outline. Return to the current official scope and lab.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Start with the current outline, choose one primary learning route, then use labs, flash cards, books or videos for gaps. Durations and access were checked September 2, 2026 and can change.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [Current CC exam outline](https://www.isc2.org/certifications/cc/cc-certification-exam-outline) | Public | 2–4h mapping + review | Canonical September 1, 2026 domains, weights, detailed topics and CAT delivery contract. |
| [ISC2 CC self-study resources](https://www.isc2.org/certifications/cc/cc-self-study-resources) | Public/free account/paid links | 1–2h selection; variable study | Official route to the outline, adaptive course, flash cards and Study Hub. Confirm account/program eligibility. |
| [Official adaptive CC self-paced training](https://www.isc2.org/training/online-self-paced/cc-online-self-paced) | Paid or program-dependent; account | About 14h + 15–25h labs/review | Current five-domain adaptive path with assessment, quizzes, flash cards and 90/180-day paid access options. Verify any free offer and exact bundle. |
| [ISC2 member policies](https://www.isc2.org/policies-procedures/member-policies) | Public | 45–90m | Current CPE, three-year cycle and AMF requirements. Policy, not exam study content. |
| [ISC2 Code of Ethics](https://www.isc2.org/ethics) | Public | 30–60m + scenarios | First-party ethical obligations; practice applying them to reporting, conflicts, competence and public trust. |
| [O'Reilly/Sybex — CC Study Guide, 2nd Edition](https://www.oreilly.com/library/view/cc-certified-in/9781394454907/) | Paid/trial or book | 6h17m + 15–25h practice | August 2026 edition explicitly mapped to 2026–2029 objectives, with labs/questions. Strong current book route. |
| [O'Reilly — Cert Prep: ISC2 CC, 2026 Edition](https://www.oreilly.com/videos/cert-prep-isc2/00001ISC2CC2026/) | Paid/trial | 4h56m + 10–20h labs/review | Mike Chapple video route aligned to the new five-domain structure. Verify page access and use practice to explain rationale. |
| [Udemy — Mike Chapple CC Complete Course](https://www.udemy.com/course/isc2-certified-in-cybersecurity-cc-complete-course/) | Paid | 4h55m + 10–20h labs/review | August 2026 course that explicitly covers the September revision. Validate all policy and fast-changing technical claims officially. |
| [Udemy — Thor Pedersen CC 2026](https://www.udemy.com/course/certifiedincybersecurity/) | Paid | Provider duration + 15–25h labs | Popular course updated June 2026 and claims the new objective map. Confirm the September domain/weight revision inside the course before relying on it. |

Avoid recalled questions, “actual exam” banks and guaranteed-pass claims. Ethical practice items are original, disclose their blueprint version and teach the reasoning; CAT delivery does not permit returning to earlier items, so practice making a defensible decision once and moving on.
