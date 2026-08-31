---
exam_code: SC-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# SC-900 Microsoft Security, Compliance, and Identity Fundamentals Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official SC-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) is authoritative.

**Current baseline:** Skills measured as of July 28, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [SC-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)

## How to use this guide

SC-900 is a control-map exam. For each scenario, identify the asset, identity, threat, control layer, evidence, and response owner. Learn product boundaries—especially the difference between identity protection, cloud posture, threat detection/response, and data compliance—instead of assuming every security portal does the same job.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe security, compliance, and identity concepts | 10–15% | Which foundational principle or responsibility applies? |
| Describe Microsoft Entra capabilities | 25–30% | How are identities authenticated, authorized, governed, and protected? |
| Describe Microsoft security solutions | 35–40% | How are cloud resources, endpoints, identities, apps, email, and incidents protected? |
| Describe Microsoft compliance solutions | 20–25% | How is data discovered, protected, retained, investigated, and governed? |

---

# 1. Security, compliance, and identity foundations

## Shared responsibility and defense in depth

The cloud provider secures the physical datacenter, physical network, and host infrastructure. Customer responsibility varies with SaaS, PaaS, and IaaS but consistently includes its data, identities, access choices, endpoints, and configurations to the applicable boundary. Review the [Azure shared responsibility model](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility).

Defense in depth places independent controls across layers: physical, identity, perimeter, network, compute, application, and data. A phishing-resistant sign-in method does not remove the need to patch an exposed application; encryption does not correct excessive authorization.

Zero Trust uses three principles:

1. verify explicitly using relevant signals;
2. use least-privilege access;
3. assume breach and reduce blast radius.

Zero Trust is not “trust nobody” and it is not one product. It is a decision model applied across identity, devices, applications, networks, infrastructure, and data. Microsoft's [Zero Trust guidance](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) maps those pillars.

## Encryption, hashing, and certificates

Encryption is reversible with an authorized key and protects confidentiality. Symmetric encryption uses one shared secret; asymmetric cryptography uses a public/private key pair and supports encryption, signing, and key agreement patterns. Hashing produces a fixed-length digest and is designed as a one-way integrity primitive; passwords should be stored with an appropriate slow salted password-hashing scheme, not plain fast hashing.

A digital signature combines hashing and asymmetric cryptography to provide integrity and signer authenticity. A certificate binds a public key to an identity through a certificate-authority trust chain. Transport encryption protects data in transit; storage/service capabilities protect data at rest; data still needs authorization and key governance.

> **Related item:** Key management includes creation, protection, rotation, access logging, backup/recovery, revocation, and destruction. “Encrypted” is incomplete without knowing who controls the keys and which identities can request decryption.

## Governance, risk, and compliance

- Governance establishes decision rights, policy, ownership, and oversight.
- Risk management identifies threats and vulnerabilities, estimates likelihood/impact, chooses treatment, and tracks residual risk.
- Compliance evaluates obligations and control evidence against laws, regulations, contracts, and standards.

Compliance is not identical to security, and passing an assessment does not guarantee that no breach can occur. Controls may be preventive, detective, or corrective. Risk can be avoided, mitigated, transferred, or accepted by an authorized owner.

## Identity concepts

An identity represents a user, workload, device, application, group, or—in the current blueprint—an agent. Authentication proves identity; authorization decides access. An identity provider authenticates identities and issues assertions or tokens. A directory stores identity objects and attributes. Federation establishes trust so one identity system can be used with another relying service.

Microsoft Entra ID is the cloud identity and access service. Windows Server Active Directory Domain Services is an on-premises directory/domain service. Microsoft Entra Domain Services provides managed domain services for Azure workloads. They are related but not interchangeable.

---

# 2. Microsoft Entra

## Identity types and hybrid identity

| Identity | Example | Lifecycle owner |
|---|---|---|
| Member user | Employee account | HR/identity process and tenant admins |
| External identity | Partner guest/customer | Sponsoring business plus identity governance |
| Workload identity | Service principal or managed identity | Application/platform owner |
| Device identity | Registered, joined, or hybrid-joined device | Endpoint/identity teams |
| Agent identity | Identity associated with an AI agent/workload | Agent owner plus identity/security governance |

Hybrid identity connects on-premises directory identities with Microsoft Entra. Synchronization, federation, or cloud authentication choices affect dependencies and recovery. A synchronized identity is not automatically authorized to every cloud resource.

Managed identities let supported Azure resources obtain tokens without the application storing a credential. System-assigned identity follows the resource lifecycle; user-assigned identity is a separately managed reusable resource. Both still need explicit role or application permission.

## Authentication

Authentication factors include something you know, have, and are. MFA requires evidence from more than one factor category; two passwords are not MFA. Passwordless methods can improve phishing resistance and user experience when deployed with appropriate enrollment and recovery controls.

| Capability | Purpose |
|---|---|
| Microsoft Authenticator | Push, number matching, passkey, and passwordless capabilities under current configuration |
| FIDO2/passkeys | Public-key, phishing-resistant authentication |
| Windows Hello for Business | Device-bound key-based user authentication |
| Temporary Access Pass | Time-limited bootstrap/recovery credential for supported onboarding |
| Self-service password reset | User password reset/unlock with configured verification |
| Password protection | Blocks weak or organization-specific banned passwords |

Single sign-on reduces repeated prompts by reusing an authenticated session/token relationship. It does not mean one password is copied among applications.

## Conditional Access and authorization

Conditional Access evaluates assignments (users/workload identities, resources, conditions) and applies access controls such as block, require an authentication strength, require compliant device, or require terms. Policies should be tested in report-only mode and exclude protected emergency accounts according to Microsoft's guidance.

Conditional Access runs after initial authentication signals exist. It is not a firewall and does not directly assign resource permissions.

Microsoft Entra roles administer directory resources. Azure RBAC authorizes Azure resource management/data actions. Application roles and scopes authorize application behavior. Microsoft 365 services also have workload-specific roles. Choose the control plane that owns the resource.

> **Related item:** Phishing-resistant MFA and device compliance solve different risks. One strengthens the sign-in ceremony; the other supplies a device-state signal. A Conditional Access policy can require both for a sensitive resource.

## Identity governance and protection

| Capability | Question answered |
|---|---|
| Entitlement management/access packages | How should users request and receive bundles of access with approvals/expiration? |
| Access reviews | Does a user still need existing access? |
| Privileged Identity Management | How should privileged role activation be time-bound, approved, and audited? |
| Lifecycle workflows | How should joiner/mover/leaver identity tasks be automated? |
| ID Protection | Which users/sign-ins are risky, and what response should policy require? |

PIM makes eligible role assignment activatable under controls; it does not make privileged activity harmless. Access reviews provide evidence and decisions; reviewers need context and follow-through. Risk detections are signals, not proof that every flagged user is compromised.

---

# 3. Azure infrastructure and cloud security

## Network and platform controls

| Control | Main purpose |
|---|---|
| Azure DDoS Protection | Helps protect public IP resources from volumetric/network attacks under applicable plan |
| Azure Firewall | Managed stateful network firewall with centralized policy |
| Web Application Firewall | Filters common web application attacks at HTTP/S layer |
| Network security group | Allows/denies network flows to subnets/interfaces using rules |
| Azure Bastion | Browser-based RDP/SSH access without exposing VM public management ports |
| Azure Key Vault | Protects and controls access to secrets, keys, and certificates |
| Private Link/private endpoint | Provides private VNet address to supported services |

Network controls are complementary. An NSG is not a WAF; a WAF does not replace application authentication; a private endpoint does not grant access.

## Microsoft Defender for Cloud

Defender for Cloud combines cloud security posture management (CSPM) with cloud workload protection (CWP) capabilities. Posture management assesses configurations, inventory, attack paths, standards, and recommendations. Workload-protection plans add threat-detection capabilities for eligible servers, storage, databases, containers, APIs, and other resources. **VERIFY CURRENT:** plans, included capabilities, coverage, and pricing.

Security policies and regulatory-compliance views organize expected controls and assessment. Secure score summarizes posture recommendations and relative improvement opportunities. A score is a prioritization tool, not certification or a guarantee.

Defender for Cloud can cover Azure and connected multicloud/on-premises resources under configured connectors and Azure Arc/plan prerequisites. Coverage must be verified; portal visibility alone does not prove every workload sends telemetry.

> **Related item:** Posture management asks whether a system is configured to reduce risk; threat protection asks whether suspicious activity is occurring. Mature programs need both prevention and detection/response.

---

# 4. Microsoft threat protection and security operations

## Microsoft Sentinel

Microsoft Sentinel is a cloud-native SIEM and security orchestration, automation, and response platform. Data connectors ingest relevant telemetry. Analytics rules and Microsoft detections create alerts/incidents. Hunting queries explore hypotheses. Automation rules and playbooks triage or respond under controlled conditions. Workbooks visualize data.

| Artifact | Role |
|---|---|
| Data connector | Brings data from a source |
| Analytics rule | Detects suspicious patterns and creates alerts/incidents |
| Incident | Groups evidence for investigation and response |
| Hunting query | Analyst-led search for threats |
| Automation rule | Applies incident automation/triage logic |
| Playbook | Logic Apps-based response workflow |
| Workbook | Interactive visualization/reporting |

A SIEM centralizes and correlates security evidence. A SOAR capability automates processes. Automation should protect against false positives, excessive privilege, repeated actions, and lost evidence.

## Microsoft Defender XDR

Defender XDR unifies detection, investigation, and response across supported endpoints, identities, email/collaboration, and cloud applications. The suite includes capabilities associated with:

- Defender for Endpoint;
- Defender for Office 365;
- Defender for Identity;
- Defender for Cloud Apps;
- vulnerability management;
- threat intelligence.

The Defender portal correlates alerts into incidents and supports investigation/response. Product boundaries and licensing evolve, so use current [Defender XDR documentation](https://learn.microsoft.com/en-us/defender-xdr/).

| Product focus | Typical evidence/control |
|---|---|
| Endpoint | Device process, file, network, vulnerability, isolation/remediation |
| Office 365 | Email, links, attachments, collaboration threats |
| Identity | On-premises/hybrid identity signals and suspicious behavior |
| Cloud Apps | SaaS discovery, session/app governance, risky OAuth apps |
| Threat intelligence | Adversary, indicator, and exposure context |

Sentinel and Defender XDR integrate but are not synonyms. Defender XDR centers Microsoft XDR signals and response; Sentinel provides broader SIEM/SOAR collection, correlation, hunting, and automation across Microsoft and third-party sources.

> **Related item:** An alert is a detection signal; an incident is an investigation container; a case outcome is an analyst conclusion. Suppressing noisy alerts without understanding why they fire can hide a coverage or configuration failure.

---

# 5. Microsoft Purview and compliance

## Trust, privacy, and compliance management

The Microsoft Service Trust Portal provides audit reports, certifications, and trust/compliance documentation. Microsoft privacy principles and contractual materials explain provider practices. Customers still determine their own legal obligations and configurations.

Compliance Manager maps controls and improvement actions to assessments and provides a compliance score. The score helps prioritize work; it is not a legal guarantee. Some actions are Microsoft-managed and others customer-managed.

## Information protection and data lifecycle

| Capability | Purpose |
|---|---|
| Sensitive information types/classifiers | Detect content patterns or categories |
| Sensitivity labels | Classify and apply protection/marking under policy |
| Data Loss Prevention | Detect and restrict risky sharing/use across supported locations |
| Retention labels/policies | Keep or delete content according to lifecycle requirements |
| Records Management | Apply stronger records controls and disposition processes |
| Content Explorer | Inspect classified/labeled content under restricted roles |
| Activity Explorer | Investigate activities involving sensitive/labeled content |

Classification identifies what data is. A sensitivity label communicates classification and can apply protection. DLP monitors/enforces usage rules. Retention answers how long data is kept or when it is deleted. These controls can interact, and retention may preserve content even after a user deletes it from the normal interface.

## Risk and investigation solutions

| Solution | Focus |
|---|---|
| Insider Risk Management | Signals and workflows for potentially risky insider activity with privacy controls |
| Communication Compliance | Policy review of risky/inappropriate communications in supported channels |
| Audit | Search and retain supported user/admin activity under applicable licensing |
| eDiscovery | Identify, preserve, collect, review, and export relevant content for investigations/legal matters |

eDiscovery is a governed legal/investigation workflow, not ordinary keyword search. Audit supplies activity evidence; it does not preserve every content item. Retention and holds affect whether content remains available.

> **Related item:** Data minimization reduces both privacy exposure and discovery/retention cost. Keeping everything forever can conflict with legal, privacy, and business requirements just as deleting too early can.

---

# 6. Hands-on labs

## Lab 1: Identity decision map

For an employee, contractor, Azure workload, device, and agent, identify identity type, authentication, Conditional Access, authorization plane, lifecycle owner, review, and emergency recovery.

## Lab 2: Conditional Access tabletop

Draft a report-only policy for administrators that requires phishing-resistant authentication and compliant devices. Define exclusions, break-glass monitoring, test users, expected logs, rollout, and rollback. Do not enforce in a real tenant without authorization.

## Lab 3: Posture to incident

Choose a hypothetical exposed VM. Trace preventive controls (NSG, patching, Key Vault, posture recommendations), detections (Defender), correlation/investigation (Defender XDR or Sentinel), response, and retained evidence.

## Lab 4: Data protection lifecycle

Classify a public sample document, propose a sensitivity label, DLP rule, retention requirement, and investigation path. Explain why each control answers a different question.

## Lab 5: Portal boundary tour

In a permitted tenant or documentation screenshots, locate Entra, Defender, Defender for Cloud, Sentinel, Purview, and Service Trust/Compliance Manager surfaces. Write the primary asset, signal, control, and owner for each.

---

# 7. Knowledge checks and distinctions

1. A storage account is encrypted but publicly readable. Which security property remains broken?
2. A user has valid credentials and passes MFA but is blocked from an app. Which Conditional Access evidence should be checked?
3. A Global Administrator needs Azure VM contributor access. Why is the directory role not necessarily sufficient?
4. Defender for Cloud reports a recommendation; Sentinel has no incident. Why is that not contradictory?
5. A DLP rule blocks sharing, but a retention policy keeps a deleted copy. Which separate goals are being enforced?
6. A risk detection flags an impossible-travel sign-in. Why should response use evidence rather than assume confirmed compromise?

| Contrast | Remember |
|---|---|
| Authentication vs authorization | Prove identity versus permit resource/action |
| Entra role vs Azure RBAC | Administer directory versus authorize Azure resources |
| MFA vs Conditional Access | Authentication evidence versus signal-driven access policy engine |
| Encryption vs hashing | Reversible confidentiality versus one-way integrity primitive |
| Zero Trust vs defense in depth | Access principles versus layered controls |
| CSPM vs CWP | Configuration/posture management versus workload threat protection |
| Defender XDR vs Sentinel | Microsoft XDR correlation/response versus broad SIEM/SOAR |
| Alert vs incident | Detection signal versus investigation container |
| Sensitivity vs retention label | Classification/protection versus lifecycle/records control |
| DLP vs access control | Governs risky data use/sharing versus permits resource access |
| Audit vs eDiscovery | Activity evidence versus content preservation/collection/review workflow |
| Compliance score vs certification | Prioritization metric versus formal assurance outcome |

## Readiness checklist

- [ ] I can explain shared responsibility, Zero Trust, defense in depth, encryption, hashing, and GRC.
- [ ] I can distinguish identity, authentication, authorization, directories, providers, and federation.
- [ ] I can describe Entra identity types, hybrid identity, authentication methods, Conditional Access, and SSO.
- [ ] I can distinguish Entra roles, Azure RBAC, and application permissions.
- [ ] I can explain ID Governance, access reviews, PIM, lifecycle workflows, and ID Protection.
- [ ] I can distinguish DDoS, Firewall, WAF, NSG, Bastion, Key Vault, and private access.
- [ ] I can distinguish Defender for Cloud posture/workload protection, Defender XDR, and Sentinel.
- [ ] I can explain Purview classification, labeling, DLP, retention, records, insider risk, communications, audit, and eDiscovery.
- [ ] I know that scores, alerts, and compliance mappings are evidence—not guarantees.
- [ ] I checked every **VERIFY CURRENT** item and the current blueprint.

## Primary references

- [Official SC-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)
- [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)
- [Microsoft Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/)
- [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/)
- [Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/)
- [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/)
- [Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)
- [Service Trust Portal](https://servicetrust.microsoft.com/)

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — SC-900 course](https://learn.microsoft.com/en-us/training/courses/sc-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation across identity, security, and compliance |
| [Microsoft — SC-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/practice/assessment?assessment-type=practice&assessmentId=11&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; start here before buying another assessment |
| [Microsoft Partner Skilling Hub — LevelUp SC-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058350) | Partner login required | 5 hours | No additional cost for eligible Microsoft partners; self-paced coverage includes security, Entra, Security Copilot, Azure security, Sentinel, Defender XDR, and Purview |
| [Microsoft Learn SC-900 learning paths](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/) | Free | About 10–14 hours | Official scope anchor and terminology; add portal exploration where permitted |
| [John Savill — SC-900 Study Cram v2](https://www.youtube.com/watch?v=-FJqb60wPSY) and [certification materials](https://github.com/johnthebrit/CertificationMaterials) | Free | About 3–4 hours plus whiteboard review | Strong visual synthesis with a public companion whiteboard; predates the July 2026 agent-identity and product changes, so use as review only. Link rather than republish the unlicensed repository artifact. |
| [Pluralsight — SC-900 path and practice exam](https://www.pluralsight.com/paths/microsoft-security-compliance-and-identity-fundamentals-sc-900) | Subscription; practice access depends on plan/library | 9 hours plus about 2–4 hours for assessment/review | Six-course path whose public page includes a practice exam; instruction is mostly 2023–2024, so cross-check every product boundary with current Learn |
| [O'Reilly — Exam Ref SC-900, 2nd Edition](https://www.oreilly.com/library/view/exam-ref-sc-900/9780138363727/) | Subscription | About 5 hours 41 minutes | 193-page May 2024 book; durable fundamentals but incomplete for July 2026 changes |
| [Udemy — SC-900 by Kevin Brown](https://www.udemy.com/course/sc-900-microsoft-security-compliance-and-identity/) | Purchase or subscription | About 8 hours | Course shown as updated October 2025; inspect current Entra, Defender, and Purview coverage |
| [LinkedIn Learning — SC-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-security-compliance-and-identity-fundamentals-sc-900-cert-prep-by-microsoft-press) | Subscription | 3 hours 32 minutes | Christopher Wojahn course released June 2024; concise fundamentals, but fill July 2026 changes from Learn |
| [Microsoft Security Virtual Training Days](https://events.microsoft.com/en-us/allevents/?search=security%20virtual%20training%20day) | Free registration when scheduled | Usually 1–2 half days | Live fundamentals sessions; schedule and exact SC-900 coverage vary |
| [MeasureUp — SC-900 practice test](https://www.measureup.com/microsoft-practice-test-sc-900-microsoft-security-compliance-and-identity-fundamentals.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 124 questions; public last update is August 2025, so compare with the July 2026 blueprint |
| [Whizlabs — SC-900 training and practice](https://www.whizlabs.com/microsoft-security-compliance-identity-fundamentals-sc-900-certification/) | Paid course or subscription | About 4–8 hours for assessment and review; course total not verified | Use the practice component for gap detection; current instructional runtime and July 2026 delta coverage were not independently verified |

The assessment products above supplement—not replace—explanatory learning and authorized portal exploration. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
