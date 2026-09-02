---
exam_code: CISSP
vendor_id: isc2
official_blueprint: https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# ISC2 Certified Information Systems Security Professional (CISSP) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The April 15, 2024 outline, claims, links, credential contract and exam-integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#cissp-coverage-record).

**Current baseline:** The April 15, 2024 CISSP outline remains active. The CAT exam is three hours with 100–150 multiple-choice/advanced items, 700/1000 passing, and Chinese, English, German, Japanese and Spanish delivery at selected authorized Pearson VUE centers; Chinese appointments use selected windows.<br>
**Upcoming change:** No later revision or retirement announcement was present on the checked outline September 2, 2026. The baseline is older than two years, so recheck it frequently rather than assuming age means retirement.<br>
**Exam versus certification:** ISC2 requires five cumulative years of experience in at least two current CISSP domains. A relevant degree or credential on the approved list can waive one year only; part-time work and internships may count. A passer without enough experience can become an Associate of ISC2 and has six years to earn it. Confirm endorsement/application rules.<br>
**Maintenance:** Current policy lists 120 CPEs over the three-year CISSP cycle and a USD 135 member AMF; Associates have separate annual requirements. Confirm current policy before registration.

## How to use this guide

CISSP tests broad security-leadership judgment, not only technical recall. For each scenario, identify mission and stakeholders, law/contract/policy, assets and owners, threats/vulnerabilities, likelihood/impact, risk appetite, candidate controls, human/safety/operational consequences, accountable decision, evidence and continuous improvement. Prefer governance and requirements before implementation; protect life and society; do not perform unapproved testing or confuse a tool output with a risk decision.

> **About related items:** A `Related item:` callout adds prerequisite, architectural or operational context. It supports the topic but does not assert that ISC2 used the wording in the public outline.

## Domain map

| Domain | Weight | Leadership evidence |
|---|---:|---|
| 1. Security and Risk Management | 16% | Ethical/governance decisions, risk and continuity records, supply-chain/personnel/awareness outcomes |
| 2. Asset Security | 10% | Owned inventory and data lifecycle, classification/handling, retention/destruction, privacy and control evidence |
| 3. Security Architecture and Engineering | 13% | Requirements-to-design traceability, trust/control model, crypto/facility/system lifecycle and failure analysis |
| 4. Communication and Network Security | 13% | Segmented resilient architecture, secured components/channels, identity/path/telemetry and safe failure/recovery |
| 5. Identity and Access Management | 13% | Physical/logical subject lifecycle, assurance/federation, authorization and accountable access evidence |
| 6. Security Assessment and Testing | 12% | Risk-based strategy, independent/authorized tests, representative evidence, analyzed findings and remediation |
| 7. Security Operations | 13% | Investigation/monitoring, protected resources, response/recovery/continuity, change and people/facility safety |
| 8. Software Development Security | 10% | Governed SDLC/ecosystem, assurance gates, acquisition/supply-chain risk and secure coding/release evidence |

---

## 1. Security and Risk Management — 16%

Apply the ISC2 Code of Ethics and organizational ethics when law, customer interest, employer direction and public safety compete. Establish authority, competence, due care/diligence, truthful evidence, privacy and responsible disclosure. Protect society first; document and escalate conflicts. Legal systems and requirements vary by jurisdiction: criminal, civil, administrative/regulatory, contract, intellectual property, privacy and import/export rules require qualified counsel, not improvised interpretation.

Security concepts connect confidentiality, integrity, availability, authenticity and non-repudiation to risk decisions. Governance establishes strategy, roles, policy, accountability and oversight aligned with mission; management plans and executes; operations runs controls. Use organizational, industry and international frameworks appropriately. Define policy, mandatory standards, procedures and advisory guidelines with ownership, exceptions and review. Acquisition/divestiture, committees, delegated authority and third-party relationships must preserve accountability.

Investigation types have different authority, evidence, burden and stakeholder requirements. Establish legal/HR/privacy/regulatory involvement, chain of custody, need-to-know and retention before evidence is needed. Do not assume an internal administrator may search, disclose or seize any system.

BC requirements come from BIA: critical processes, dependencies, maximum tolerable downtime, RTO, RPO and recovery service levels. Select strategies and exercises proportional to safety, mission and cost. Risk management establishes context, identifies threats/vulnerabilities, analyzes likelihood/impact, evaluates priority, treats risk and monitors change. Distinguish qualitative and quantitative methods, inherent and residual risk, appetite and tolerance. Authorized leadership accepts risk; security provides transparent evidence. Controls may be administrative/technical/physical and preventive/detective/corrective/deterrent/recovery/compensating/directive.

Threat modeling identifies assets, actors, flows, boundaries, threats and mitigations using a suitable method. Supply-chain risk covers suppliers, components, services, dependencies, provenance, concentration, tampering/counterfeit, support/EOL, contractual evidence and exit. Personnel controls include screening/agreement, onboarding, role change, termination, vendor/contractor handling, separation of duties, rotation/vacation and sanctions. Awareness/training is role- and threat-specific; measure reporting and safer behavior, not attendance alone.

**Related item:** Governance determines who may accept risk; architecture translates obligations into structure; operations produces evidence. A security leader should not bypass the accountable owner merely because the technical fix seems obvious.

---

## 2. Asset Security — 10%

Identify data, hardware, software, services, cloud resources, identities, keys/certificates, models/training data, facilities and business processes. Assign owner, custodian/processor and steward responsibilities. Classification considers value, sensitivity, criticality, legal/contractual obligations and impact. Labels and metadata help enforce handling but need governance, inheritance, validation and controlled reclassification.

Handling requirements span collection/create, transmission, processing/use, sharing, storage, archive, retention and destruction. Apply least privilege, encryption, DLP, rights management, privacy minimization and monitoring according to classification and jurisdiction. Map every dispersed copy: endpoints, queues, caches, logs, replicas, snapshots, backups, analytics/features, model context and vendor support data.

Provision securely through approved procurement/source, inventory, baseline, identity/ownership, configuration and acceptance. Manage change, maintenance, return, reuse and deprovision. Data lifecycle controls include location/residency, access, quality/integrity, retention schedule, legal hold, archive and deletion/sanitization. Media sanitization method—clear, purge, destroy or crypto erase—depends on medium, threat and reuse; verify the result and provider contract.

Retention balances mandatory minimum/maximum, business need, privacy, litigation/hold and technical limits. Track product/service EOL and end of support because unsupported assets change risk and treatment. Select controls from business and system requirements; map privacy requirements, data roles and cross-border handling with qualified stakeholders. Audit events need attributable actor/action/object/result/time/context and protected storage.

**Related item:** Inventory says what exists; classification says required protection; configuration management says expected state; asset management owns the whole lifecycle. None substitutes for the others.

---

## 3. Security Architecture and Engineering — 13%

Translate business, legal, safety, privacy and security requirements into architecture and acceptance criteria. Apply least privilege, defense in depth, secure defaults, fail secure, complete mediation, separation of duties, simplicity/small attack surface, Zero Trust, privacy by design, shared responsibility and secure access service edge where appropriate. Document trust boundaries, attack surfaces, dependencies and residual risk.

Security models express different goals: Bell–LaPadula emphasizes confidentiality, Biba integrity and other formal models state access or information-flow rules. Know their intent and limitations rather than blindly applying labels. Select controls from requirements and threat model. Information-system capabilities include memory/process isolation, protected boot/TPM, cryptographic services, secure update, logging and fault tolerance; verify implementation and lifecycle.

Assess clients, servers, databases, cryptographic systems, ICS/OT, cloud SaaS/PaaS/IaaS, distributed/high-performance/edge/embedded/IoT systems, microservices/APIs, containers/serverless and virtualized systems. Each shifts identity, management plane, isolation, patching, observability, timing/safety and recovery. Protect AI systems as assets and applications: training data, models/weights, prompts/context, tools, endpoints and outputs face poisoning, leakage, evasion, injection, theft and excessive-agency risks.

Choose symmetric/asymmetric encryption, hashes/HMAC, signatures, PKI/certificates and key management for defined confidentiality, integrity, authenticity or non-repudiation needs. Govern algorithm/mode/key size and full key lifecycle—generation, storage/HSM, distribution, use, rotation, backup/recovery where allowed, revocation, expiry and destruction. Build crypto inventory and agility for deprecation and post-quantum transition. Understand attack categories such as brute force, known/chosen data, side channel, implementation/protocol weakness and key compromise; never design custom cryptography.

Secure sites through location and threat assessment, layered perimeter/building/room/rack controls, badges/visitors, surveillance, locks/mantraps where justified, power/HVAC/fire/water protection, redundant/diverse utilities and safety procedures. Manage the information-system lifecycle from concept and requirements through design, acquisition/build, verification, operation/change, retirement and disposal with authorization and continuous monitoring.

**Related item:** A reference architecture is reusable structure; a security model states abstract rules; a pattern solves recurring design; a baseline is an approved configuration. Evidence must show the implemented system still satisfies the original requirement.

---

## 4. Communication and Network Security — 13%

Design network architecture from business/data flows and trust zones. Relate OSI/TCP-IP layers, encapsulation, Ethernet/wireless, IPv4/IPv6, switching/routing, TCP/UDP and application services. Use segmentation/microsegmentation, DMZ, VLAN/VRF, firewalls/proxies, IDS/IPS, NAC, VPN/Zero Trust access, resilient paths and protected management planes. Virtual/software-defined/cloud networks move control into APIs and policy but retain packet and route realities.

Account for endpoint, branch, remote/mobile, data center, cloud, edge, IoT/OT and third-party connectivity. Wireless/cellular/Bluetooth/NFC/satellite/media risks vary by range, spectrum, pairing/authentication, interference, update and safety. Content distribution, load balancing and redundant routes can improve availability but introduce certificate, DNS, cache and provider dependencies.

Harden network components with supported software, secure boot/configuration, centralized AAA/MFA, role separation, secure admin protocols, configuration backup, NTP, logs/telemetry, unused-feature shutdown and controlled rules/routes. Protect routers/switches, firewalls, WAF/API gateway, load balancers, DNS/DHCP/NTP, wireless controllers/APs and monitoring devices. A control that cannot report health may fail silently.

Secure communication channels according to sensitivity and threat: TLS, IPsec/VPN, SSH, secure email/messaging/file and wireless protocols operate at different layers. Validate peer identity, certificate chain/name/usage/time/revocation, algorithm configuration, key lifecycle, route/DNS and downgrade/replay risks. Trace user/workload → name resolution → route → policy/proxy → transport/TLS → service and return path before changing controls.

**Related item:** Segmentation constrains paths, IAM constrains subjects/actions, cryptography protects content/identity and monitoring detects behavior. Strong architecture layers these controls and designs for their failure.

---

## 5. Identity and Access Management — 13%

Control physical and logical access for people, devices, services/workloads, data, applications, facilities and management systems. Identification names a subject; authentication verifies; authorization decides permitted action; accounting records it. Choose assurance proportional to risk and protect enrollment, proofing, credential issuance, recovery, session and revocation.

Authentication factors include knowledge, possession and inherence, plus contextual signals. MFA should use independent factors and phishing-resistant methods where risk warrants. Biometrics require false acceptance/rejection, liveness, privacy and non-revocability analysis. Passwordless does not mean credentialless. Devices and workloads need unique, rotated, preferably short-lived identities rather than shared static secrets.

Federation delegates trust across domains; SSO reuses authentication across services. SAML, OAuth and OpenID Connect serve different assertion/delegation/authentication purposes. Validate issuer, audience, signature/encryption, redirect/replay, scopes, claims-to-role mapping, session and logout/revocation. Contract and monitor third-party identity availability and compromise response.

Apply DAC, MAC, RBAC, rule-based, attribute-based and risk/context-aware authorization appropriately. Use least privilege, need-to-know, default deny, separation of duties and time-bounded privileged access. Prevent confused deputy, object-level authorization and privilege-creep failures; test allowed and denied paths.

Operate joiner/mover/leaver for employees, contractors, partners, customers and workload/service accounts. Establish authoritative source, owner, approval, role/attribute, credential, expiration, access review and recertification. Deprovision sessions, tokens/keys/certificates, devices, groups and downstream/federated access. Govern emergency/break-glass and shared accounts with attribution and review.

**Related item:** Authentication strength cannot correct excessive authorization, and an accurate entitlement list cannot prove how an application enforces access. Test identity, policy decision, resource enforcement and audit evidence end to end.

---

## 6. Security Assessment and Testing — 12%

Design a risk-based strategy with objectives, criteria, scope, assets/data, authority/rules, independence, method, frequency/triggers, environment, tooling, evidence handling, safety/stop conditions, reporting and remediation ownership. Internal, external, regulatory and supplier audits answer different assurance questions. Sampling and point-in-time evidence limit conclusions.

Test technical, administrative and physical controls using documentation/architecture/configuration review, interviews/observation, access review, log/transaction analysis, vulnerability assessment, code/dependency/IaC/image analysis, penetration test, red/purple exercise, synthetic transaction and disaster/incident exercise. Scan identifies possible weakness; penetration testing safely validates exploit paths under authorization; neither alone measures business risk or all controls.

Software tests include unit/integration/system/acceptance, SAST, DAST, IAST, SCA, secret scanning, fuzzing and abuse cases. Validate backup restore, alert/telemetry health, identity denial, segmentation and key/certificate failure. Test AI systems for data/model provenance, privacy, injection/adversarial input, unsafe action, quality/drift/bias and human escalation.

Collect representative, accurate, protected process data: training/reporting behavior, incidents, vulnerabilities/age, patch/configuration compliance, access reviews, change failures, recovery results, control availability and supplier evidence. Define metrics/thresholds/owners and distinguish leading/lagging, count/rate and activity/outcome.

Analyze false positive/negative, severity, exploitability/exposure, business impact, root/systemic cause and compensating controls. Report evidence, limitation, risk and prioritized recommendation to the right audience; track owner/due date/exception and retest closure. Preserve auditor independence and resolve conflicts transparently.

**Related item:** Continuous monitoring supplies frequent evidence; an assessment evaluates controls against criteria; an audit provides independent assurance; a penetration test challenges exploitable paths. One cannot be marketed as all four.

---

## 7. Security Operations — 13%

Investigations require authority, scope, privacy/legal/HR coordination, evidence integrity and chain of custody. Identify, collect/acquire, preserve, examine, analyze and report without altering originals unnecessarily. Cloud, endpoint, network, mobile and volatile evidence differ; follow order of volatility and provider capabilities. Separate facts, hypotheses and conclusions.

Log and monitor identity, endpoint, network/DNS, application/API, database/data, cloud/control plane, physical and threat-intelligence sources. Synchronize time and normalize identity/asset/request context. SIEM aggregates/correlates; EDR observes/responds at endpoints; IDS/IPS observes/blocks network patterns; DLP controls defined sensitive movement. Verify collection health, protect access/retention/integrity and tune without hiding true paths.

Manage provisioning/baselines/automation/configuration drift. Apply need-to-know/least privilege, separation of duties, job rotation, dual control, change/record discipline and service continuity. Protect media, keys, credentials, backups, logs and sensitive work areas through complete lifecycle.

Incident management prepares authority, people, communications, tools and playbooks; detects/analyzes scope/impact; contains reversibly where possible; eradicates cause/persistence; recovers clean service; and learns. Operate firewalls, IDS/IPS, anti-malware/EDR, application control, sandbox/deception and other preventive/detective controls. Vulnerability and patch management inventories, assesses/prioritizes, tests, deploys/mitigates, verifies and handles exceptions/EOL. Change management preserves approval, impact/dependency, implementation, validation, rollback and records—including emergency retrospective review.

Recovery strategies include backup/restore, redundancy/failover, alternate processing/site, mutual/cloud services and manual workarounds. DR activates, communicates, restores dependencies/configuration/identity/data, validates integrity/security/function, returns/fails back and improves. Exercise checklist/walkthrough/tabletop/simulation/parallel/full interruption as risk permits; measure RTO/RPO and recovery service level. BC maintains business outcomes and people/supplier processes beyond IT.

Physical operations enforce badges/visitors, surveillance, media/device handling and environmental controls. Prioritize personnel safety: evacuation, emergency response, travel/workplace risks, duress, lone workers and crisis communication. Safety can override evidence or availability goals.

**Related item:** An event becomes an incident when analysis and policy determine material impact or response need. Good operations preserve the option to contain now, investigate accurately and recover safely.

---

## 8. Software Development Security — 10%

Integrate security into concept, requirements, design/threat model, development, build, test, deployment, operation/maintenance and retirement. Governance defines accountable product/data/security owners, risk acceptance, architecture standards, gates and metrics. Agile, DevOps and waterfall change cadence, not the need for traceability and evidence. Treat AI prompts/context/models/tools as software/data supply-chain components.

Secure development ecosystems include repository/branch/review, IDE and developer workstation, build runners, artifact/package registries, test data, secrets, IaC/configuration, CI/CD identity, deployment and production telemetry. Apply least privilege/segregation, isolated ephemeral builds, dependency pinning, reproducibility, artifact signing/provenance/SBOM, protected approvals and immutable promotion. Threat-model pipeline compromise and insider/supplier risk.

Assess effectiveness with requirements traceability, architecture/code review, SAST/DAST/IAST/SCA, unit/integration/security/abuse/fuzz tests, vulnerability metrics, penetration tests and production feedback. Risk-rank findings, manage exceptions and verify remediation; code coverage or zero scanner findings is not assurance.

Assess acquired commercial, open-source, outsourced and cloud software for supplier controls, ownership/licensing, data/subprocessor use, development/response practice, provenance, vulnerabilities, support/EOL, integration/access, assurance evidence, escrow/portability and exit. Contracts must assign remediation, notification, evidence and deletion duties.

Secure coding validates input/schema and authorization for every object/action; uses parameterized data access and context-aware output encoding; protects tokens/sessions/secrets; controls memory/concurrency/error conditions; prevents injection, traversal, SSRF, unsafe deserialization and logic abuse; logs safely without secrets; and fails securely. Review compiler/runtime/framework/container configuration and patch dependencies. Release with monitored canary/rollback where suitable and retire data, access, keys and artifacts deliberately.

**Related item:** DevSecOps is shared, automated security ownership across delivery and operation. It does not mean developers unilaterally accept enterprise risk or a scanner replaces professional review.

---

## Integrated scenarios

### Scenario 1: Acquisition and security-program integration

Assess an acquired SaaS company: mission, jurisdictions/contracts, assets/data/AI, people and suppliers, architecture/IAM/network/SDLC, monitoring/incidents and continuity. Prioritize risks, name accountable owners, protect evidence and staff, integrate policies/identity/logging without disrupting customers, and define measurable 30/60/90-day outcomes.

### Scenario 2: Ransomware and data-exfiltration response

Correlate synthetic identity, endpoint, DNS/network, cloud and DLP signals. Establish authority and facts, preserve chain of custody, contain privileged access and affected paths, coordinate legal/HR/privacy/customer decisions, recover clean systems/data to RTO/RPO, retest controls and update risk, architecture, training and supplier actions.

### Scenario 3: Secure digital-service launch

Classify data and obligations, threat-model web/API/CI-CD/cloud/third-party flows, select architecture/crypto/IAM/network controls, define assurance gates and operational telemetry, contract supplier evidence/response/exit, exercise failed deployment and regional outage, and present residual-risk choices to leadership.

## Hands-on evidence labs

1. **Governance/risk pack:** For a synthetic business service, build policy hierarchy, asset/threat/risk/control/owner evidence, treatment and awareness outcome; apply ethics to one conflict.
2. **Asset/data lifecycle:** Inventory/classify synthetic data and AI assets, map copies/flows/roles, enforce handling/retention/hold/deletion and record proof.
3. **Architecture/crypto/facility:** Create a requirements-to-design threat model; select isolation/crypto/key/facility controls and test one failure/rotation/recovery.
4. **Network/IAM:** Segment a virtual lab, configure protected administration and user/workload roles, test federation/MFA/allowed-denied paths, logging and deprovisioning.
5. **Assessment:** Define authorized scope and criteria, run safe configuration/vulnerability/code/dependency checks, analyze limitations/risk and retest remediation.
6. **Operations/incident:** Centralize synthetic signals, prove sensor health, triage/contain while preserving evidence, patch the cause and document stakeholders/lessons.
7. **DR/BC:** Restore clean identity/configuration/application/data in dependency order, measure RTO/RPO, validate security/function and tabletop a people/supplier failure.
8. **Secure delivery:** Threat-model a small API/AI-enabled app, protect CI/CD identity/secrets/artifacts, apply test gates, simulate rejected/failed release and roll back/retire cleanly.

## Readiness checks

1. Can you apply ethics when employer direction and public interest conflict?
2. Who governs, manages, operates and accepts risk?
3. How do law, contract, policy, standard, procedure and guideline differ?
4. How do investigation types change authority and evidence?
5. Can you calculate and use BIA/RTO/RPO/risk concepts without false precision?
6. How do threat modeling, SCRM, personnel and awareness connect?
7. Who owns, stewards and holds/custodies each asset?
8. Can you trace classification through handling, retention and sanitization?
9. Where do cloud, backup, log and AI copies hide?
10. How do design principles and formal security models differ?
11. Can you assess cloud/ICS/IoT/container/serverless/AI design by trust boundary?
12. What is the full cryptographic and key lifecycle?
13. How do facility controls and system lifecycle support requirements?
14. Can you trace packets, control planes and return paths by layer?
15. What makes segmentation, network components and secure channels verifiable?
16. How do identification, authentication, authorization and accounting connect?
17. What must federation and MFA validate end to end?
18. Can you govern human/device/workload/privileged identity lifecycle?
19. What makes an assessment strategy authorized and representative?
20. How do scan, penetration test, audit and continuous monitoring differ?
21. Which metrics measure security outcomes rather than activity?
22. How do you report evidence, limitations, risk and closure?
23. What preserves evidence and authority during investigations?
24. How do SIEM, EDR, IDS/IPS and DLP differ?
25. Can you prove baselines, automation and monitoring are healthy?
26. How do incident, problem, vulnerability, patch and change processes connect?
27. Can you recover cleanly to measured RTO/RPO and fail back?
28. How do DR exercises and BC scope differ?
29. When must personnel safety override other security goals?
30. Can you trace security through every SDLC phase?
31. What protects developer, repository, runner, artifact and deployment identities?
32. How do SAST, DAST, IAST, SCA, fuzzing and abuse tests differ?
33. What acquired-software and supplier evidence is needed before approval?
34. Can you explain and prevent injection, authz, SSRF, deserialization and logic flaws?
35. How do privacy and AI-specific assets appear across all eight domains?
36. Can you choose governance before tooling and requirements before configuration?
37. Can you state a decision’s human, safety and operational consequences?
38. Can you identify accountable owner, evidence and residual risk?
39. Can you map one scenario across all eight domains without siloing them?
40. Have you reconciled every resource with the April 2024 outline and current policy?

### Check key

- **Ready:** You can make and defend the leadership decision, assign accountable action, produce evidence and test failure/recovery.
- **Review:** You know terminology but cannot connect mission, risk, architecture, people, control, operations and assurance.
- **Gap:** You guessed, memorized a bank or relied on an older resource without reconciling the current outline.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Use the outline plus one primary route, then select labs, practice or references for gaps. Access, durations and revisions were checked September 2, 2026 and can change.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [Current CISSP exam outline](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) | Public | 8–12h mapping + review | Canonical April 15, 2024 domains, weights, detailed topics, CAT and experience contract; recheck often because of age. |
| [ISC2 CISSP self-study resources](https://www.isc2.org/certifications/cissp/cissp-self-study-resources) | Public/account/paid links | 1–2h selection; variable study | Official route to outline, adaptive training, flash cards and Study Hub. |
| [Official adaptive CISSP training](https://www.isc2.org/training/online-self-paced/cissp-online-self-paced) | Paid/account | 20–40h official range + 50–80h labs | Current adaptive route with textbook/questions, assessments and 90/180-day options. |
| [Pluralsight CISSP 2024 path](https://www.pluralsight.com/paths/cisspr-certified-information-systems-security-professional-certification) | Paid/trial | 37h including seven labs + further practice | Sixteen courses, seven refreshed labs and practice exam explicitly mapped to April 2024. |
| [LinkedIn Learning/Mike Chapple CISSP 2024 Cert Prep](https://www.linkedin.com/learning/isc2-certified-information-systems-security-professional-cissp-2024-cert-prep) | Paid/trial | 21h27m + 40–70h labs | Advanced eight-domain course with transcripts and separate practice; close post-release policy/technology changes. |
| [O'Reilly/Sybex CISSP Official Study Guide, 10th Edition](https://www.oreilly.com/library/view/isc2-cissp-certified/9781394254699/) | Paid/trial or book | 40h26m + 40–70h labs | 1,248-page June 2024 deep reference mapped to the active outline, with practice explanations and labs. |
| [Udemy/Andrew Ramdayal Complete CISSP Course, Exam and Mindset](https://www.udemy.com/course/cisspcertification/) | Paid | 41h27m + 35–60h labs | Popular October 2025 route claiming 2024 alignment. Verify every material claim officially and use practice for rationale, never memorization. |
| [Inside Cloud and Security CISSP resources](https://insidethemicrosoftcloud.com/cissp/) | Public/optional paid book | 10–14h selective video/addendum estimate | Pete Zerger’s visual cram, 2024 addendum and topic links are strong review—not a substitute for the blueprint or hands-on evidence. |
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Public | 4–8h selective mapping | Authoritative governance and outcome vocabulary for connecting Govern, Identify, Protect, Detect, Respond and Recover. |
| [ISC2 member policies](https://www.isc2.org/policies-procedures/member-policies) | Public | 45–90m | Current CISSP/Associate CPE, cycle and AMF requirements; policy rather than exam content. |
| [ISC2 Code of Ethics](https://www.isc2.org/ethics) | Public | 30–60m + scenarios | Apply first-party canons to authority, evidence, disclosure, competence, conflicts and public trust. |

Avoid recalled questions, “actual exam” banks and guaranteed passing. Practice should be original and teach why the best leadership decision satisfies mission, law, risk, people and operations. CAT delivery requires answering in sequence without backtracking, so practice making a defensible decision once and continuing.
