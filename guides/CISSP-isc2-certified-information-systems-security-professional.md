---
exam_code: CISSP
vendor_id: isc2
official_blueprint: https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# ISC2 Certified Information Systems Security Professional (CISSP) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The April 15, 2024 outline, claims, links, credential contract and exam-integrity boundary were checked September 29, 2026. This review maps all 62 numbered objectives and executes 23 local risk-register checks; independent human review and infrastructure activities remain pending. See the [coverage record](../docs/SOURCE-VALIDATION.md#cissp-coverage-record).

**Current baseline:** The April 15, 2024 CISSP outline remains active. The CAT exam is three hours with 100–150 multiple-choice/advanced items, 700/1000 passing, and Chinese, English, German, Japanese and Spanish delivery at selected authorized Pearson testing centers; Chinese appointments use selected windows.<br>
**Upcoming change:** No later revision or retirement announcement was present on the checked outline September 29, 2026. The baseline is older than two years, so recheck it frequently rather than assuming age means retirement.<br>
**Exam versus certification:** ISC2 requires five cumulative years of experience in at least two current CISSP domains. A relevant degree or credential on the approved list can waive one year only; part-time work and internships may count. A passer without enough experience can become an Associate of ISC2 and has six years to earn it. Confirm endorsement/application rules.<br>
**Maintenance — VERIFY CURRENT:** The [member policies](https://www.isc2.org/policies-procedures/member-policies) require 120 CPEs over three years: at least 90 Group A and another 30 Group A or B. Forty annually is suggested. Member AMF is USD 135; Associates instead have annual 15 Group A and USD 50 requirements. Verify your category and cycle.

**CURRENT BLUEPRINT:** The canonical web outline and its [15-page April 2024 PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/CISSP-Exam-Outline-April-2024-English.pdf) retain 62 numbered objectives across eight domains. The monitored change only shortened the testing-center label from Pearson VUE to Pearson. The [refresh FAQ](https://www.isc2.org/certifications/cissp/cissp-exam-refresh-faq) describes the already active 2024 change; its future-tense wording does not announce another refresh.

**VERIFY CURRENT:** The [May 18, 2026 waiver update](https://www.isc2.org/Insights/2026/05/CISSP-Experiene-Waiver-Updates) says the approved credential list changed April 1, 2026. Check the [current experience list](https://www.isc2.org/certifications/cissp/cissp-experience-requirements), including exact credential names; a degree and credential cannot stack into two waived years. Full-time experience accrues monthly at at least 35 hours/week for four weeks; qualifying part-time work is 20–34 hours/week, with 1,040 hours equated to six months. Document internships on organizational letterhead. These are public rules, not an individual eligibility determination.

The [CAT policy](https://www.isc2.org/certifications/computerized-adaptive-testing) explains unscored items, no answer review and breaks that consume examination time. A training completion percentage, number of items delivered or stopping point does not reveal the scaled exam result.

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

### Turn risk information into an accountable decision

**PRACTICAL DEPTH:** [NIST IR 8286 Rev. 1](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8286r1.pdf), finalized December 2025, connects cybersecurity records to enterprise objectives and decisions. Its [release announcement](https://www.nist.gov/news-events/news/2025/12/nist-revises-publications-integrating-cybersecurity-and-enterprise-risk) explains the alignment with CSF 2.0. Use strategic, operational, reporting and compliance consequences to communicate with leadership. Risk appetite sets broad willingness to take risk; tolerance makes the relevant boundary usable for an objective or service. Record owner, evidence, assumptions, time horizon and decision authority.

For an original single-event annual scenario, a 20% chance of a USD 100,000 loss has USD 20,000 expected annual loss. That number is neither the maximum loss nor a prediction that a USD 20,000 incident will happen. Annual event frequency is a different input from probability of at least one event; frequency can exceed one, probability cannot. A repeated-event model requires a justified frequency/severity model. Do not multiply unrelated ordinal “high = 3” labels and present the answer as dollars.

Suppose a control costs USD 5,000 annually and credibly reduces that single-event probability to 8%, leaving the same loss severity. Its modeled residual exposure is USD 8,000 and its modeled reduction net of cost is USD 7,000. Show the assumptions and uncertainty, then assess safety, mandatory obligations, operational impact and tolerance. The arithmetic does not authorize implementation or prove the control works. Transfer through insurance also leaves exclusions, deductibles, operational loss and reputational consequences to evaluate.

Normalize horizon, currency and loss definitions before combining registers. Two departments may describe the same outage under different risk IDs; unique IDs alone cannot detect that overlap. Shared suppliers may create correlated losses, and a mean total does not describe tail loss. Preserve the scenario relationships and uncertainty rather than mechanically summing every row. NIST's selected analysis and roll-up sections support consistent context and escalation; the local numerical assumptions below are original teaching choices.

The [CSF 2.0 portal](https://www.nist.gov/cyberframework) is a route to current governance resources. Its September 2026 AI-profile update is a draft consultation, not a replacement final CSF baseline. A framework outcome is not proof that a control is operating.

## 2. Asset Security — 10%

Identify data, hardware, software, services, cloud resources, identities, keys/certificates, models/training data, facilities and business processes. Assign owner, custodian/processor and steward responsibilities. Classification considers value, sensitivity, criticality, legal/contractual obligations and impact. Labels and metadata help enforce handling but need governance, inheritance, validation and controlled reclassification.

Handling requirements span collection/create, transmission, processing/use, sharing, storage, archive, retention and destruction. Apply least privilege, encryption, DLP, rights management, privacy minimization and monitoring according to classification and jurisdiction. Map every dispersed copy: endpoints, queues, caches, logs, replicas, snapshots, backups, analytics/features, model context and vendor support data.

Provision securely through approved procurement/source, inventory, baseline, identity/ownership, configuration and acceptance. Manage change, maintenance, return, reuse and deprovision. Data lifecycle controls include location/residency, access, quality/integrity, retention schedule, legal hold, archive and deletion/sanitization. Choose clear, purge or destroy according to medium, threat and reuse; cryptographic erase is a technique whose suitability depends on the encryption and key lifecycle. Verify the result and provider contract.

Retention balances mandatory minimum/maximum, business need, privacy, litigation/hold and technical limits. Track product/service EOL and end of support because unsupported assets change risk and treatment. Select controls from business and system requirements; map privacy requirements, data roles and cross-border handling with qualified stakeholders. Audit events need attributable actor/action/object/result/time/context and protected storage.

**Related item:** Inventory says what exists; classification says required protection; configuration management says expected state; asset management owns the whole lifecycle. None substitutes for the others.

---

### A deletion request needs an inventory and an outcome

[NIST SP 800-88 Rev. 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf) separates checking whether the sanitization operation completed from deciding whether its outcome satisfies the required protection. Crypto erase depends on the relevant data being encrypted appropriately and all applicable key copies being addressed; deleting one key reference does not retract exported plaintext, retained keys or backups. A legal hold, a retention rule and a user deletion request require an authorized resolution, followed by evidence about all in-scope copies. The exercise below does not sanitize media.

## 3. Security Architecture and Engineering — 13%

Translate business, legal, safety, privacy and security requirements into architecture and acceptance criteria. Apply least privilege, defense in depth, secure defaults, fail secure, complete mediation, separation of duties, simplicity/small attack surface, Zero Trust, privacy by design, shared responsibility and secure access service edge where appropriate. Document trust boundaries, attack surfaces, dependencies and residual risk.

Security models express different goals: Bell–LaPadula emphasizes confidentiality, Biba integrity and other formal models state access or information-flow rules. Know their intent and limitations rather than blindly applying labels. Select controls from requirements and threat model. Information-system capabilities include memory/process isolation, protected boot/TPM, cryptographic services, secure update, logging and fault tolerance; verify implementation and lifecycle.

Assess clients, servers, databases, cryptographic systems, ICS/OT, cloud SaaS/PaaS/IaaS, distributed/high-performance/edge/embedded/IoT systems, microservices/APIs, containers/serverless and virtualized systems. Each shifts identity, management plane, isolation, patching, observability, timing/safety and recovery. Protect AI systems as assets and applications: training data, models/weights, prompts/context, tools, endpoints and outputs face poisoning, leakage, evasion, injection, theft and excessive-agency risks.

Choose symmetric/asymmetric encryption, hashes/HMAC, signatures, PKI/certificates and key management for defined confidentiality, integrity, authenticity or non-repudiation needs. Govern algorithm/mode/key size and full key lifecycle—generation, storage/HSM, distribution, use, rotation, backup/recovery where allowed, revocation, expiry and destruction. Build crypto inventory and agility for deprecation and post-quantum transition. Understand attack categories such as brute force, known/chosen data, side channel, implementation/protocol weakness and key compromise; never design custom cryptography.

Secure sites through location and threat assessment, layered perimeter/building/room/rack controls, badges/visitors, surveillance, locks/mantraps where justified, power/HVAC/fire/water protection, redundant/diverse utilities and safety procedures. Manage the information-system lifecycle from concept and requirements through design, acquisition/build, verification, operation/change, retirement and disposal with authorization and continuous monitoring.

**Related item:** A reference architecture is reusable structure; a security model states abstract rules; a pattern solves recurring design; a baseline is an approved configuration. Evidence must show the implemented system still satisfies the original requirement.

---

### Separate a security claim from its evidence

A design principle, a formal model and a product label answer different questions. Start with the property to preserve, identify subjects/objects and trusted components, state allowed information flows, then test the implementation and its failure modes. “Fail secure” for access decisions does not justify trapping people during a fire. Facility safety and business recovery require their own acceptance criteria.

[NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) rejects implicit trust based only on location or ownership. A request from the office network still needs the applicable identity, device, resource and policy evaluation. Segmentation reduces reachable paths; it does not prove authorization inside a service.

For cryptography, distinguish key establishment, encryption and signatures. NIST's [first finalized post-quantum standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) include ML-KEM for key encapsulation and ML-DSA/SLH-DSA for signatures. Inventory protocols, certificates, libraries and data lifetimes before migration; algorithm names alone do not prove interoperable deployment. Post-quantum algorithms are distinct from quantum key distribution.

The [CMVP FAQ](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/faqs) says only FIPS 140-3 validations remain active from September 22, 2026. Historical status is different from revoked status. Check the exact module, version, environment and security policy; module validation does not certify the entire application, protocol or organization. No local example here demonstrates FIPS validation.

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

### Password policy, phishing resistance and authorization are separate

The selected verifier guidance in [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) requires at least 15 characters for a single-factor password and permits a minimum of eight when the password is part of MFA. It also addresses blocklists, rate limits and password managers rather than routine composition rules or periodic changes without evidence of compromise. These are scoped digital-identity requirements; a local activation PIN is a different mechanism. Apply the appropriate organizational and regulatory requirements explicitly.

Manually entering a one-time code does not by itself provide phishing resistance: an attacker can relay it. A stronger authenticator still cannot repair an application that authorizes the wrong object. Trace enrollment, authentication, session establishment, policy decision, enforcement, recovery and revocation. For a workload or AI agent, identify the issuing authority, credential lifetime, allowed tools/data and accountable owner; a model's proposed action is not permission to execute it.

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

### Response evidence must reach recovery and improvement

[NIST SP 800-61 Rev. 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) integrates incident response with CSF 2.0. Govern, Identify and Protect prepare the organization, while Detect, Respond and Recover support handling incidents; improvement informs all functions. Organizations may retain a suitable operational lifecycle. Do not interpret the framework as a mandatory rigid sequence or wait for perfect attribution before authorized containment.

For an original ransomware scenario, record what is known, which systems and identities are implicated, who can order isolation and which evidence may be lost. Restore identity and management dependencies as well as application data. An available backup is not a measured recovery: demonstrate a clean restore, business validation, elapsed recovery time, data loss and monitoring before closing the incident. A changed hash establishes a byte difference, not its cause or whether evidence was collected under valid authority.

## 8. Software Development Security — 10%

Integrate security into concept, requirements, design/threat model, development, build, test, deployment, operation/maintenance and retirement. Governance defines accountable product/data/security owners, risk acceptance, architecture standards, gates and metrics. Agile, DevOps and waterfall change cadence, not the need for traceability and evidence. Treat AI prompts/context/models/tools as software/data supply-chain components.

Secure development ecosystems include repository/branch/review, IDE and developer workstation, build runners, artifact/package registries, test data, secrets, IaC/configuration, CI/CD identity, deployment and production telemetry. Apply least privilege/segregation, isolated ephemeral builds, dependency pinning, reproducibility, artifact signing/provenance/SBOM, protected approvals and immutable promotion. Threat-model pipeline compromise and insider/supplier risk.

Assess effectiveness with requirements traceability, architecture/code review, SAST/DAST/IAST/SCA, unit/integration/security/abuse/fuzz tests, vulnerability metrics, penetration tests and production feedback. Risk-rank findings, manage exceptions and verify remediation; code coverage or zero scanner findings is not assurance.

Assess acquired commercial, open-source, outsourced and cloud software for supplier controls, ownership/licensing, data/subprocessor use, development/response practice, provenance, vulnerabilities, support/EOL, integration/access, assurance evidence, escrow/portability and exit. Contracts must assign remediation, notification, evidence and deletion duties.

Secure coding validates input/schema and authorization for every object/action; uses parameterized data access and context-aware output encoding; protects tokens/sessions/secrets; controls memory/concurrency/error conditions; prevents injection, traversal, SSRF, unsafe deserialization and logic abuse; logs safely without secrets; and fails securely. Review compiler/runtime/framework/container configuration and patch dependencies. Release with monitored canary/rollback where suitable and retire data, access, keys and artifacts deliberately.

**Related item:** DevSecOps is shared, automated security ownership across delivery and operation. It does not mean developers unilaterally accept enterprise risk or a scanner replaces professional review.

---

### AI context across the existing eight domains

The [ISC2 AI guidance](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/exam-guidance/ISC2-Exam-Guidance.pdf), CISSP printed pages 9–11, addresses AI through the existing domains. Map governance and suppliers to domain 1; data/model assets to 2; secure hosting and design to 3; training/inference paths to 4; nonhuman identity to 5; robustness and abuse testing to 6; monitored operation and response to 7; and generated code/dependencies to 8. It supplies context, not a ninth domain or new percentages.

Original application example: a support assistant can retrieve approved records, propose a refund and explain its evidence. The business service must independently authorize the customer record and refund action. Validate generated code and dependencies before release; test retrieval poisoning, cross-customer access and excessive tool permissions. Input filtering and explainability can help, but neither establishes that all prompt injection is prevented. Model drift or an anomaly score calls for investigation; it is not proof of compromise.

## Integrated scenarios

These are original reasoning scenarios, not recalled examination questions.

1. **Acquire a SaaS company.** Inventory data, identities, suppliers and obligations before merging privileged access. Obtain evidence of restore capability and software provenance; record unverified claims. Assign owners to integration risks and compare phased identity migration against customer disruption. A board presentation should show assumptions, time-limited decisions and measurable 30/60/90-day outcomes, not simply scanner counts.
2. **Ransomware with possible exfiltration.** Protect people and establish response authority, preserve available evidence, contain implicated access and verify telemetry health. Coordinate legal/privacy decisions without asserting that encryption proves data was not stolen. Restore clean dependencies and measure recovery. Close only after remediation and follow-up responsibilities are assigned.
3. **Launch an AI-assisted service.** Identify customer records, model/provider dependencies and privileged actions; set data and tool boundaries. Require negative authorization tests, dependency evidence and operational ownership. Compare release, restricted pilot and delay using service needs and residual risk. A passing schema check or persuasive model answer cannot approve the release.

## Executed local risk-register workbook

**PRACTICAL DEPTH — executed locally, synthetic data only.** The [IR 8286 Rev. 1 publication page](https://csrc.nist.gov/pubs/ir/8286/r1/final) links the [risk-register schema](https://csrc.nist.gov/files/pubs/ir/8286/r1/final/docs/risk_register_schema.json). The code preserves that schema and uses actual [jsonschema validation](https://python-jsonschema.readthedocs.io/en/stable/validate/) to distinguish structural checks from original data-quality and approval rules. It ran with Python 3.13.14 and the already installed jsonschema 4.26.0: **23 checks passed**. Running it performs no network requests, file writes or account changes.

The official schema requires fields, numeric types and an allowed, nonempty, unique response list. It does not constrain percentage ranges, require nonblank ownership, calculate exposure, restrict status values or forbid extra properties. The code therefore demonstrates both structural failures and structurally valid records that violate the stated local model. This is a boundary of the schema's assertions, not a claim that NIST recommends invalid estimates.

The separate [risk-detail schema](https://csrc.nist.gov/files/pubs/ir/8286/r1/final/docs/risk_detail_record_schema.json) was also inspected: `currentRiskAnalysis` is required without a corresponding property definition, while `plannedRiskResponse` is defined but not required. That is a valid JSON Schema structure. Presence, type constraints, business completeness and evidence quality require distinct checks; neither official schema was modified.

Copy the code into a Python file in an environment that already has the stated dependency. Its date, actor, ownership and tolerance are trusted synthetic fixtures. They demonstrate decision logic, not authenticated users, signatures, durable approvals or an enterprise GRC service. The negative-loss model uses USD and a one-year single-event horizon; opportunity analysis or repeated-event losses require different assumptions. Duplicate IDs are caught, but different IDs for the same scenario are not. No empirical probability, control effectiveness, legal conclusion or production readiness is established.

```python
# Original synthetic risk-data demonstration. Requires jsonschema 4.26.0.
# NIST risk-register schema downloaded 2026-09-29; unchanged JSON below.
# Source: https://csrc.nist.gov/files/pubs/ir/8286/r1/final/docs/risk_register_schema.json
from copy import deepcopy
from datetime import date
from decimal import Decimal
import json
from jsonschema import Draft202012Validator

SCHEMA = json.loads(r'''{
    "$id": "https://csrc.nist.gov/csrc/media/schema/olir/risk_register.v2.schema.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "description": "The use of cybersecurity risk registers provides consistency in capturing and communicating risk-related information (including risk response) throughout the ERM process. It provides a framework for organizing and communicating risk information from the individual system level up through the organizational level and finally to the highest enterprise level. The risk registers used at each level convey information about risk assessments, evaluation decisions, responses, and monitoring activities.",
    "title": "Risk Register",
    "type": "object",
    "properties": {
        "riskId": {
            "description": "Risk ID",
            "type": "string"
        },
        "riskDescription": {
            "description": "Risk Description",
            "type": "string"
        },
        "riskCategory": {
            "description": "Risk Category",
            "type": "string"
        },
        "riskLikelihood": {
            "description": "Current Assessment: Likelihood (%)",
            "type": "number"
        },
        "riskImpact": {
            "description": "Current Assessment: Impact ($)",
            "type": "number"
        },
        "exposureRating": {
            "description": "Current Assessment: Exposure Rating ($)",
            "type": "number"
        },
        "riskResponseType": {
            "description": "Planned Risk Response",
            "type": "array",
            "minItems": 1,
            "items": {
                "enum": [ "Accept", "Avoid", "Transfer", "Mitigate", "Realize", "Share", "Enhance" ]
            },
            "uniqueItems": true
          },
        "riskResponseCost": {
            "description": "Risk Response Cost ($)",
            "type": "number"
        },
        "riskResponseDescription": {
            "description": "Planned Risk Response Description",
            "type": "string"
        },
        "riskOwnerPointOfContact": {
            "description": "Risk owner(s) / point(s) of contact",
            "type": "string"
        },
        "status": {
            "description": "Status",
            "type": "string"
        }
    },
    "required": [ "riskId", "riskDescription", "riskCategory", "riskLikelihood", "riskImpact", "exposureRating", "riskResponseType", "riskResponseCost", "riskResponseDescription", "riskOwnerPointOfContact", "status" ]
}''')

Draft202012Validator.check_schema(SCHEMA)
validator = Draft202012Validator(SCHEMA)
base = dict(riskId="R-01", riskDescription="Single annual service outage",
            riskCategory="Operations", riskLikelihood=20, riskImpact=100000,
            exposureRating=20000, riskResponseType=["Mitigate"],
            riskResponseCost=5000, riskResponseDescription="Restore capacity",
            riskOwnerPointOfContact="service-owner", status="Open")


def schema_errors(row):
    return sorted(e.message for e in validator.iter_errors(row))


def quality_errors(row):
    # Original local rules: negative loss, USD, one event in a one-year horizon.
    # These rules supplement the official schema; they do not change it.
    errors = schema_errors(row)
    if errors:
        return errors
    for field in SCHEMA["required"]:
        if isinstance(row[field], str) and not row[field].strip():
            errors.append("blank:" + field)
    values = {k: Decimal(str(row[k])) for k in
              ("riskLikelihood", "riskImpact", "exposureRating", "riskResponseCost")}
    if not all(v.is_finite() for v in values.values()):
        return errors + ["non-finite number"]
    if not 0 <= values["riskLikelihood"] <= 100:
        errors.append("probability outside 0..100 percent")
    if any(values[k] < 0 for k in ("riskImpact", "exposureRating", "riskResponseCost")):
        errors.append("negative loss or cost")
    expected = (values["riskLikelihood"] / 100 * values["riskImpact"]).quantize(Decimal("0.01"))
    if values["exposureRating"] != expected:
        errors.append("exposure inconsistent with stated model")
    if row["status"] not in {"Open", "Monitoring", "Closed"}:
        errors.append("unknown local status")
    if not set(row["riskResponseType"]) <= {"Accept", "Avoid", "Transfer", "Mitigate"}:
        errors.append("opportunity response in negative-loss register")
    return errors


def portfolio_errors(rows):
    errors, seen = [], set()
    for row in rows:
        errors.extend(quality_errors(row))
        rid = row.get("riskId")
        if rid in seen:
            errors.append("duplicate risk ID")
        seen.add(rid)
    return errors


def acceptance_allowed(row, *, actor, expires, today, owner_by_id, tolerance):
    # actor, owner mapping, clock and tolerance are trusted fixtures, not authentication.
    return (not quality_errors(row)
            and row["riskResponseType"] == ["Accept"]
            and owner_by_id.get(row["riskId"]) == actor
            and row["riskOwnerPointOfContact"] == actor
            and today <= expires
            and Decimal(str(row["exposureRating"])) <= tolerance)


results = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    results.append(name)


check("valid original row", not schema_errors(base) and not quality_errors(base))
missing = deepcopy(base)
del missing["riskOwnerPointOfContact"]
check("required owner field", bool(schema_errors(missing)))
for name, patch in [
    ("number is not a numeric string", {"riskLikelihood": "20"}),
    ("boolean is not a number", {"riskLikelihood": True}),
    ("response enumeration", {"riskResponseType": ["Ignore"]}),
    ("response must be nonempty", {"riskResponseType": []}),
    ("responses must be unique", {"riskResponseType": ["Accept", "Accept"]}),
]:
    check(name, bool(schema_errors(base | patch)))
for name, patch in [
    ("percentage over 100", {"riskLikelihood": 150}),
    ("negative loss", {"riskImpact": -100000}),
    ("empty owner", {"riskOwnerPointOfContact": "  "}),
    ("incorrect exposure", {"exposureRating": 2}),
    ("unknown status", {"status": "Trust me"}),
    ("positive-risk response needs a different model", {"riskResponseType": ["Enhance"]}),
]:
    row = base | patch
    check(name + ": schema passes, local rules reject",
          not schema_errors(row) and bool(quality_errors(row)))
check("unexpected field is permitted by official schema",
      not schema_errors(base | {"unrecognizedField": "not an approval"}))
check("non-finite Python number rejected locally",
      bool(quality_errors(base | {"riskImpact": float("inf")})))
check("duplicate risk ID rejected at collection boundary",
      bool(portfolio_errors([base, deepcopy(base)])))
check("two distinct valid IDs pass local collection checks",
      not portfolio_errors([base, base | {"riskId": "R-02"}]))
accepted = base | {"riskResponseType": ["Accept"]}
context = dict(actor="service-owner", expires=date(2026, 12, 31),
               today=date(2026, 9, 29), owner_by_id={"R-01": "service-owner"},
               tolerance=Decimal("20000"))
check("authorized acceptance at tolerance", acceptance_allowed(accepted, **context))
check("analyst cannot self-approve", not acceptance_allowed(accepted, **(context | {"actor": "analyst"})))
check("forged owner field does not change trusted authority",
      not acceptance_allowed(accepted | {"riskOwnerPointOfContact": "analyst"},
                             **(context | {"actor": "analyst"})))
check("expired acceptance rejected", not acceptance_allowed(accepted, **(context | {"expires": date(2026, 9, 28)})))
check("above tolerance needs escalation", not acceptance_allowed(accepted, **(context | {"tolerance": Decimal("10000")})))
check("planned mitigation is not acceptance", not acceptance_allowed(base, **context))
print(json.dumps(results))
print(f"{len(results)} local risk-register checks passed")
```

Expected final line: `23 local risk-register checks passed`. Explain each rejected record and which layer rejected it before extending the model. A valid row still needs provenance, an appropriate horizon, uncertainty bounds, independent review and an accountable decision.

## Hands-on evidence labs

These eight activities are proposed; none was executed against infrastructure during this review. Use only an authorized disposable environment and synthetic data. Preserve expected versus observed results, cleanup and limitations.

| Activity | Produce and verify | Failure case and completion evidence |
|---|---|---|
| 1. Governance and risk | Build a service BIA, risk register, owner/authority map and treatment decision; compare two control choices. | Reject missing authority or incompatible time horizons. Include uncertainty, tolerance, approval expiry and a review trigger. |
| 2. Asset lifecycle | Map collection, processing, logs, replicas, backups, model context and retirement. | Introduce a legal hold and an unknown copy; resolve ownership before deletion. Record the approved handling/sanitization outcome and evidence limits. |
| 3. Architecture and facilities | Trace confidentiality/integrity/availability requirements to isolation, crypto, power and safety controls. | Lose a key, component or power source in a disposable design; show safe failure and recovery without claiming a module label validates the whole system. |
| 4. Network and identity | Trace DNS, routing, segmentation, authentication, authorization and return traffic for one service. | Attempt wrong-tenant access and use a revoked test identity. Preserve denial and audit evidence; remove temporary access afterward. |
| 5. Assessment | Define authorized scope, method, sampling, independence and stop conditions; assess a small test service. | Include a known defect and a known safe case. Explain false results, evidence limits, remediation ownership and retest closure. |
| 6. Operations and response | Correlate synthetic identity/network/endpoint events, verify sensor health and document response decisions. | Simulate a missing log source and an incorrect alert. Preserve facts separately from hypotheses and show containment authority. |
| 7. Continuity and recovery | Restore disposable identity, configuration, application and data dependencies; compare observed results with BIA objectives. | Make one backup unavailable or corrupt. Record elapsed recovery, actual data loss, business validation, fallback and cleanup. |
| 8. Secure delivery | Trace a requirement through code review, dependency provenance, build identity, artifact and deployment approval. | Reject an unauthorized object request and a substituted artifact; show rollback and retirement evidence. AI-generated code receives the same gates. |

## Readiness checks

Use these original answered prompts to explain a decision and its evidence. They are not an examination simulation or a guarantee of readiness.

### Domain 1: Security and Risk Management

1. **An employer requests concealed incident evidence. What leads?** Protect society and truthful evidence; use the authorized escalation and legal/privacy process. An employment instruction does not erase professional obligations.
2. **Who accepts residual risk?** The accountable authority designated by governance. The analyst estimates and recommends; a tool score or administrator privilege does not confer approval authority.
3. **Policy, standard, procedure or guideline?** Policy establishes direction, a standard sets mandatory requirements, a procedure specifies execution and a guideline advises. Record owners, exceptions and review triggers.
4. **How does a BIA differ from a threat assessment?** BIA examines disruption consequences and recovery needs for business processes; threat assessment examines adverse events and conditions. Use both to choose proportionate continuity controls.
5. **Appetite versus tolerance?** Appetite expresses broad willingness to take risk; tolerance defines a usable limit around a relevant objective. Escalate breaches rather than silently changing the threshold.
6. **Is 20% times USD 100,000 an annual frequency calculation?** Only under the stated single-event annual model is it USD 20,000 expected loss. A frequency/severity model is different; state the horizon and uncertainty.
7. **Does insurance transfer all risk?** No. Evaluate coverage, exclusions and recoverability alongside operational, safety and reputational consequences that remain.
8. **How do personnel, supply chain and awareness fit together?** Use screening/agreements and joiner-mover-leaver controls, supplier provenance and support evidence, and role-specific training. Measure safer behavior and reporting, then update the program as threats change.

### Domain 2: Asset Security

9. **Who decides classification?** The accountable asset/data owner under policy, with relevant privacy and business input. Custodians implement handling; their administrator access does not establish ownership.
10. **What must an inventory include beyond servers?** Data, applications, services, identities, keys, dependencies, models, suppliers and locations. Link records to owners and business purposes.
11. **Which data states need protection?** At rest, in transit and in use. Trace actual flows, access and copies rather than assuming storage encryption protects every state.
12. **What makes provisioning secure?** Approved source, known ownership, inventory, a validated baseline, least privilege and acceptance evidence before normal use.
13. **Can a deletion request override a hold?** Resolve applicable obligations through authorized stakeholders first; retain the decision and apply it consistently to copies and providers.
14. **Clear, purge, destroy or crypto erase?** Clear, purge and destroy are method categories; crypto erase is a technique with encryption/key assumptions. Choose for medium and protection need, then verify and validate the outcome.
15. **How does end of support affect retention?** An asset may still need retained information while its platform becomes unsupported. Plan migration, protected archival access and retirement rather than keeping an unsafe dependency indefinitely.
16. **Do labels, DLP and rights management prove compliance?** They support handling requirements. Assess coverage, exceptions, allowed access, retention and evidence against actual obligations.

### Domain 3: Security Architecture and Engineering

17. **What precedes choosing a control?** Business, safety, legal and security requirements plus a threat model. Trace the selected control to a property and an acceptance test.
18. **How do confidentiality and integrity models differ?** They constrain different information-flow goals. State the model assumptions and intended property before applying access rules; a model name alone is not implementation evidence.
19. **Does an internal network establish trust?** No. Evaluate subject/device identity, resource, context and policy; verify both policy decision and enforcement.
20. **What changes across cloud, OT and serverless?** Responsibility, control planes, timing/safety, isolation, visibility, patching and recovery constraints. Analyze each trust boundary instead of copying one architecture unchanged.
21. **KEM, encryption and signature?** They serve key establishment, confidentiality and authenticity/integrity purposes respectively. Choose compatible protocols and lifecycle controls, not merely algorithm labels.
22. **What evidence supports a validated-module claim?** The exact certificate, module/version, environment and security policy. Historical is different from revoked; validation does not extend automatically to the whole product.
23. **Why assess side channels and implementation attacks?** Mathematically strong algorithms can be undermined by timing, faults, key handling or protocol implementation. Architecture and operational controls must cover those paths.
24. **When does the system lifecycle end?** After approved retirement, data disposition, access/key revocation and dependency cleanup are verified. Facilities, power, fire response and personnel safety remain part of design and operation.

### Domain 4: Communication and Network Security

25. **Which path should a failed connection investigation trace?** Name resolution, route, policy/proxy, transport/TLS, service authorization and return path. Change the control implicated by evidence.
26. **Why distinguish data, control and management planes?** They carry different traffic and authority. A safe data path does not prove management APIs or routing changes are protected.
27. **What does segmentation prove?** Only the tested path restrictions. Test allowed flows, denied flows, bypass paths and actual enforcement; it does not replace object authorization.
28. **Do VLANs or overlays erase the physical network?** No. Media, routing, encapsulation, capacity and failure dependencies still matter and need visibility.
29. **Bandwidth, latency or jitter?** They describe capacity, delay and delay variation. Match measurement to the application, including voice/video and safety-sensitive systems.
30. **What belongs in network-component hardening?** Supported configuration, protected administration, AAA, accurate time, telemetry, backup and controlled changes. Test health and recovery as well as access denial.
31. **What is necessary beyond encrypted transport?** Correct peer identity and certificate validation, suitable configuration and key lifecycle, plus application authorization. Encryption to the wrong endpoint does not meet the requirement.
32. **How should wireless and third-party paths be assessed?** Evaluate range, pairing/authentication, interference, updates, ingress/egress, provider responsibility and alternate paths; verify the specific deployment.

### Domain 5: Identity and Access Management

33. **Identification, authentication, authorization and accounting?** Name the subject, verify the claim, decide permitted actions and record attributable activity. Each needs its own evidence.
34. **Is any two-step login phishing resistant?** No. Factor independence and resistance to relaying are different properties; manually entered codes can be relayed.
35. **What does a current password policy need?** Apply the appropriate assurance scope, length, blocklist, rate limiting and recovery controls. Distinguish passwords from local activation secrets and verify governing requirements.
36. **Federation versus SSO?** Federation establishes trust across identity domains; SSO reuses an authentication experience. Validate issuer, audience, token integrity, replay protections and role mapping.
37. **How does ABAC differ from RBAC?** ABAC evaluates attributes and policy conditions; RBAC assigns permissions through roles. Both need reliable inputs, least privilege and enforcement testing.
38. **What ends during offboarding?** Sessions, tokens, keys, groups, devices and downstream access, not only one account. Preserve required records and verify denial after revocation.
39. **How should emergency access work?** Predefined authority, limited scope/time, attributable use, monitoring and review. A shared password without attribution weakens accountability.
40. **Can an AI agent approve its own tool request?** The service must enforce trusted identity and authorization independently. Restrict tools/data, credential lifetime and escalation; the proposed action is untrusted input.

### Domain 6: Security Assessment and Testing

41. **What must precede an intrusive test?** Written authority, scope, rules, safety/stop conditions, evidence handling, reporting and accountable contacts.
42. **Scan, penetration test or audit?** A scan identifies potential weaknesses, an authorized penetration test investigates exploitable paths, and an audit assesses evidence against criteria with appropriate independence.
43. **Does a clean scan prove security?** No. Explain scope, coverage, tool limitations, false negatives and untested business logic or administrative controls.
44. **How do SAST, DAST, IAST and SCA differ?** They examine source/static artifacts, running application behavior, instrumented runtime behavior and component/dependency information respectively. Combine them with abuse and requirements-based tests.
45. **What makes process metrics meaningful?** Define denominator, period, source quality, owner and action threshold. Training attendance or closed tickets alone does not establish improved outcomes.
46. **Can sample evidence represent every system?** Only within justified scope and sampling limits. State exclusions, freshness and representativeness rather than generalizing a small successful sample.
47. **When is a finding closed?** After accountable remediation or an approved exception, supporting evidence and proportionate retest. Administrative status alone is insufficient.
48. **What did the local schema checks establish?** Specific structural, quality and fixture-policy outcomes for synthetic inputs. They did not verify real estimates, authenticated approvals or an operating GRC control.

### Domain 7: Security Operations

49. **What makes investigation evidence usable?** Authority, documented collection/handling, provenance, integrity, access control and retention. A hash alone does not establish lawful collection or a complete chain of custody.
50. **Can no alerts mean no incidents?** Only if sensor health, coverage and detection limits are understood; silent collection failures can hide events.
51. **What connects configuration and change management?** An approved expected state, controlled change, deployment verification, drift detection and rollback evidence, including emergency follow-up.
52. **How do privilege controls support operations?** Least privilege, separation of duties, monitored privileged access and attributable records reduce misuse while preserving service continuity.
53. **How does incident response connect to risk management?** Preparation and improvement span governance, assets and protection; detection, response and recovery feed new evidence into risk decisions and controls.
54. **What should drive patch priority?** Exposure, exploitability, business/safety impact, dependencies and available mitigations; then test deployment and verify remediation or a time-bounded exception.
55. **Backup, DR and BC?** Backup supplies recoverable data; DR restores technology capabilities; BC maintains business outcomes, people and suppliers. Exercise dependencies and measure actual recovery and data loss.
56. **When do personnel safety concerns take priority?** Emergency and duress procedures must protect people even when evidence or availability is affected. Record the decision and coordinate authorized response.

### Domain 8: Software Development Security

57. **Where does security enter the SDLC?** At requirements and design, continuing through development, build, test, release, operation and retirement. Keep traceability and owners throughout.
58. **What belongs in the development ecosystem threat model?** Developer devices, repositories, runners, dependencies, registries, secrets, test data, deployment identities and approval paths.
59. **Does signed provenance prove a safe artifact?** It provides evidence about origin and process under defined trust assumptions; vulnerable code or a compromised trusted builder still needs assessment.
60. **How is effectiveness assessed?** Requirements-based tests, review, abuse cases, dependency evidence and operational feedback. Coverage percentages and zero findings are incomplete indicators.
61. **What evidence is needed for acquired software?** Supplier practices, provenance, vulnerability response, support/EOL, data access, contract responsibilities and exit/portability; evaluate integration risk.
62. **Is schema validation sufficient input security?** No. Verify authorization, semantics and business invariants, and use suitable parameterization/encoding. The workbook shows valid structure with invalid estimates.
63. **What special treatment does generated code need?** Review and test it under the same release controls, including invented dependencies, insecure patterns, data handling and supply-chain evidence.
64. **What authorizes release and retirement?** Accountable approval using requirements, test evidence, exceptions and residual risk; then verify deployment/rollback or removal of data, access, keys and dependencies.

A useful readiness standard is being able to defend the decision, identify its owner, produce evidence and explain a failure or recovery path. Memorizing terminology without those connections leaves a gap.

## Places to learn

This is not a complete list. Start with the official scope and one teaching route, then use targeted practice and references. Public metadata was checked September 29, 2026; paid interiors, practice questions and completion quality were not inspected. Supplemental study times below are planning estimates, not provider promises.

| Resource | Access | Estimated time |
|---|---|---|
| [Current CISSP outline](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline): canonical April 2024 scope, eight weights and 62 objectives. | Public | 8–12h mapping and review estimate. |
| [ISC2 self-study resources](https://www.isc2.org/certifications/cissp/cissp-self-study-resources): route to the outline, adaptive study, cards and support resources. | Public links; some account/paid resources | 1–2h selection estimate; study varies. |
| [Official adaptive CISSP training](https://www.isc2.org/training/online-self-paced/cissp-online-self-paced): English, eight domains, assessments and eTextbook. Public completion threshold is 60% for domain/final assessments plus acknowledgement and survey; this is not an exam passing percentage. | Paid/account; 90/180-day access starts at purchase | No fixed runtime reverified; earlier “official 20–40h” claim removed. Plan additional practice. |
| [Pluralsight CISSP 2024 path](https://www.pluralsight.com/paths/cisspr-certified-information-systems-security-professional-certification): 16 course cards and seven labs; 14 certification courses plus two supplemental courses. Public alignment claim is April 2024. | Paid/trial; public catalog | Header 37h; listed course cards total 27h07m and labs 9h15m, or 36h22m combined. Dates span 2021–2026; no interior alignment validation. |
| [LinkedIn Learning / Mike Chapple CISSP 2024](https://www.linkedin.com/learning/isc2-certified-information-systems-security-professional-cissp-2024-cert-prep): advanced, April 25, 2024; public outline spans eight domains and lists 51 quizzes. | Paid/trial; public contents | Header 21h27m; 365 listed clips total exactly 21h27m. Add practice and current policy review; quizzes were not opened. |
| [O'Reilly / Sybex Official Study Guide, 10th edition](https://www.oreilly.com/library/view/isc2-cissp-certified/9781394254699/): access blocked HTTP 403. Earlier June 2024, 1,248-page and 40h26m metadata was not reverified. | Paid/trial or book; catalog blocked | Current duration and contents unverified; do not treat an old runtime as a current promise. |
| [Udemy / Andrew Ramdayal CISSP course](https://www.udemy.com/course/cisspcertification/): access blocked HTTP 403. Earlier October 2025 and 41h27m claims remain unverified. | Paid; catalog blocked | Current runtime and alignment unverified. |
| [Inside Cloud and Security CISSP hub](https://insidethemicrosoftcloud.com/cissp/): public creator page links cram material, a book, study/practice resources and optional flashcards. Videos and question interiors were not viewed. | Public hub; optional paid material | Runtime and revision unverified; select topics after blueprint mapping. |
| [NIST IR 8286 Rev. 1 and schemas](https://csrc.nist.gov/pubs/ir/8286/r1/final): enterprise risk context and original local workbook above. | Public | 3–5h selected reading/workbook estimate; not a complete CISSP course. |
| [NIST CSF 2.0 portal](https://www.nist.gov/cyberframework): governance and outcome references; check each publication's draft/final status. | Public | 4–8h selected mapping estimate. |
| [ISC2 member policies](https://www.isc2.org/policies-procedures/member-policies) and [Code of Ethics](https://www.isc2.org/ethics): credential obligations and professional judgment. | Public | 1–2h reading/scenarios estimate; individual eligibility remains separate. |

Use original practice that explains assumptions and decisions. Avoid recalled examination questions and guaranteed-pass claims. Course completion, a valid data file and a locally passing exercise are useful evidence within their limits; each still needs to be connected to the actual objective and accountable action.
