---
exam_code: SC-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-27
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-27
---

# SC-900 Microsoft Security, Compliance, and Identity Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 28, 2026 objectives and its cited public sources on September 27, 2026; all 58 October objectives were also mapped separately while retaining the accepted July baseline. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#sc-900-coverage-record). The [official SC-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) is authoritative.

**Current baseline:** Skills measured as of July 28, 2026<br>
**Upcoming blueprint change (checked September 27, 2026):** The English blueprint changes October 21, 2026. The revision names workload identities and Microsoft Threat Intelligence. Domain weights are unchanged. Study the broader identity category; the older agent-ID example alone is insufficient. The current baseline below remains dated separately. See the [official revision](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900).<br>
**Official source:** [SC-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)

## How to use this guide

SC-900 is a control-map exam. For each scenario, identify the asset, identity, threat, control layer, evidence, and response owner. Learn product boundaries—especially the difference between identity protection, cloud posture, threat detection/response, and data compliance—instead of assuming every security portal does the same job.

Use this repeatable reasoning sequence:

1. **Asset:** What is being protected—an identity, device, workload, network path, application, or data?
2. **Actor and identity:** Who or what is requesting access, and how is that identity represented?
3. **Threat or obligation:** Is the concern unauthorized access, vulnerable configuration, active attack, data misuse, retention, investigation, or regulatory evidence?
4. **Preventive control:** What can stop or reduce the event before it succeeds?
5. **Signal and evidence:** Which service records posture, risk, activity, an alert, or retained content?
6. **Decision and response:** Who owns the decision, and which service supports remediation, investigation, or proof?

For example, “protect a confidential file” is not one control. Entra can decide whether the user may enter the service; a sensitivity label can classify and protect the file; DLP can restrict risky use; retention can preserve or delete it according to policy; Audit can record supported activity; and eDiscovery can preserve and collect relevant content. Keep those jobs separate.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

The current credential page lists a **45-minute assessment** and thirteen exam languages; the introductory instructor-led course is one day. Course duration, exam duration and your own preparation time are different. Use the four worked examples, seven labs and eighteen answered checks below to test your reasoning; portal access is optional for the tabletop exercises.


## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe security, compliance, and identity concepts | 10–15% | Which foundational principle or responsibility applies? |
| Describe Microsoft Entra capabilities | 25–30% | How are identities authenticated, authorized, governed, and protected? |
| Describe Microsoft security solutions | 35–40% | How are cloud resources, endpoints, identities, apps, email, and incidents protected? |
| Describe Microsoft compliance solutions | 20–25% | How is data discovered, protected, retained, investigated, and governed? |

---

## 1. Security, compliance, and identity foundations

### Shared responsibility and defense in depth

The cloud provider secures the physical datacenter, physical network, and host infrastructure. Customer responsibility varies with SaaS, PaaS, and IaaS but consistently includes its data, identities, access choices, endpoints, and configurations to the applicable boundary. Review the [Azure shared responsibility model](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility). Moving from IaaS to PaaS or SaaS shifts more platform operation to Microsoft, but accountability for the organization's identities, data, and use of the service does not disappear.

Defense in depth places independent controls across layers: physical, identity, perimeter, network, compute, application, and data. A phishing-resistant sign-in method does not remove the need to patch an exposed application; encryption does not correct excessive authorization.

Zero Trust uses three principles:

1. verify explicitly using relevant signals;
2. use least-privilege access;
3. assume breach and reduce blast radius.

Zero Trust is not “trust nobody” and it is not one product. It is a decision model applied across identity, devices, applications, networks, infrastructure, and data. Microsoft's [Zero Trust guidance](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) maps those pillars.

### Encryption, hashing, and certificates

Encryption is reversible with an authorized key and protects confidentiality. Symmetric encryption uses one shared secret; asymmetric cryptography uses a public/private key pair and supports encryption, signing, and key agreement patterns. Hashing produces a fixed-length digest and is designed as a one-way integrity primitive; passwords should be stored with an appropriate slow salted password-hashing scheme, not plain fast hashing.

A digital signature combines hashing and asymmetric cryptography to provide integrity and signer authenticity. A certificate binds a public key to an identity through a certificate-authority trust chain. Transport encryption protects data in transit; storage/service capabilities protect data at rest; data still needs authorization and key governance.

> **Related item:** Key management includes creation, protection, rotation, access logging, backup/recovery, revocation, and destruction. “Encrypted” is incomplete without knowing who controls the keys and which identities can request decryption.

### Governance, risk, and compliance

- Governance establishes decision rights, policy, ownership, and oversight.
- Risk management identifies threats and vulnerabilities, estimates likelihood/impact, chooses treatment, and tracks residual risk.
- Compliance evaluates obligations and control evidence against laws, regulations, contracts, and standards.

Compliance is not identical to security, and passing an assessment does not guarantee that no breach can occur. Controls may be preventive, detective, or corrective. Risk can be avoided, mitigated, transferred, or accepted by an authorized owner.

### Identity concepts

An identity represents a user, workload, device, application, group, or—in the current blueprint—an agent. Authentication proves identity; authorization decides access. An identity provider authenticates identities and issues assertions or tokens. A directory stores identity objects and attributes. Federation establishes trust so one identity system can be used with another relying service.

Microsoft Entra ID is the cloud identity and access service; the [Entra overview](https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra) places it within the broader Entra family. Windows Server Active Directory Domain Services is an on-premises directory/domain service. Microsoft Entra Domain Services provides managed domain services for Azure workloads. They are related but not interchangeable.

An identity-centered security boundary is useful because an authenticated request can originate from outside a traditional corporate network and still be evaluated using identity, device, application, risk, and resource signals. It does not make network or data controls obsolete: identity is one control plane in a layered system.

---

## 2. Microsoft Entra

### Identity types and hybrid identity

| Identity | Example | Lifecycle owner |
|---|---|---|
| Member user | Employee account | HR/identity process and tenant admins |
| External identity | Partner guest/customer | Sponsoring business plus identity governance |
| Workload identity | Service principal or managed identity | Application/platform owner |
| Device identity | Registered, joined, or hybrid-joined device | Endpoint/identity teams |
| Agent identity | Identity associated with an AI agent/workload | Agent owner plus identity/security governance |

The accepted July blueprint names agent ID; October broadens the identity objective to workload identities. Study the broader category first, then place agent identities within the identity landscape. Microsoft describes [agent identities](https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities) as identities for AI agents, with agent identity blueprints used as reusable lifecycle and governance templates and agent identities representing deployed instances. Do not treat “agent” as merely a human user with a descriptive account name. **VERIFY CURRENT:** Microsoft Entra Agent ID terminology, availability, licensing, portal surfaces, and the exact distinction between an agent identity and other workload identities are evolving.

[Workload identities](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview) include application objects, service principals and managed identities. An application object describes an application; a service principal represents its instance in a particular tenant. A managed identity is a special service principal whose credentials the platform manages. A device identity represents hardware/device context, not every program running on it.

**Worked example — one app, two tenants:** a multitenant application has one application object in home tenant A, a service principal in A, and another service principal in consenting tenant B. Count one definition and two local instances, not three interchangeable permission records. Removing consent or assignment in A does not establish that B's separate grants were removed. For a managed identity, removing an application-held secret is unnecessary, but reviewing its resource permissions and lifecycle is still essential.

Hybrid identity connects on-premises directory identities with Microsoft Entra. Synchronization, federation, or cloud authentication choices affect dependencies and recovery. A synchronized identity is not automatically authorized to every cloud resource.

Managed identities let supported Azure resources obtain tokens without the application storing a credential. System-assigned identity follows the resource lifecycle; user-assigned identity is a separately managed reusable resource. Both still need explicit role or application permission.

The important lifecycle question is not only “can this identity sign in?” Ask who creates it, who owns it, which credentials or federation it uses, which permissions it holds, how access is reviewed, how suspicious use is detected, and what disables it when the employee, application, device, or agent is retired.

### Authentication

Authentication factors include something you know, have, and are. MFA requires evidence from more than one factor category; two passwords are not MFA. Passwordless methods can improve phishing resistance and user experience when deployed with appropriate enrollment and recovery controls. The [Microsoft Entra authentication overview](https://learn.microsoft.com/en-us/entra/identity/authentication/overview-authentication) is the current source for supported methods and their roles.

| Capability | Purpose |
|---|---|
| Microsoft Authenticator | Push, number matching, passkey, and passwordless capabilities under current configuration |
| FIDO2/passkeys | Public-key, phishing-resistant authentication |
| Windows Hello for Business | Device-bound key-based user authentication |
| Temporary Access Pass | Time-limited bootstrap/recovery credential for supported onboarding |
| Self-service password reset | User password reset/unlock with configured verification |
| Password protection | Blocks weak or organization-specific banned passwords |

**Preference, enrollment and enforcement are different.** [System-preferred authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-system-preferred-multifactor-authentication) can prompt for the strongest registered method while still allowing another method. It does not replace an authentication-strength policy. A registration campaign enables/prompts setup; it does not prove that the user registered or successfully used a passkey.

> **Related current change:** [Microsoft’s September 23 transition guidance](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) says passkey enablement/nudges began September 1 for SMS/voice-enabled users. Microsoft-provided SMS/voice delivery retires **February 1, 2027** for most users, including internal guests, and **July 1, 2027** for Global Administrators and external users. This is a provider-delivery transition, not the disappearance of every possible SMS/voice service. Customer-managed telephony has separate provider/preview requirements. Use the current population-specific Learn guidance rather than the July blog's earlier blanket February wording, and verify cloud/tenant rollout before planning changes.

Single sign-on reduces repeated prompts by reusing an authenticated session/token relationship. It does not mean one password is copied among applications.

### Conditional Access and authorization

Conditional Access evaluates assignments (users/workload identities, resources, conditions) and applies access controls such as block, require an authentication strength, require compliant device, or require terms. The [Conditional Access overview](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) describes it as Microsoft's Zero Trust policy engine. Policies should be tested in report-only mode and preserve protected emergency access according to Microsoft's guidance.

The controls above depend on the subject. [Conditional Access for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) targets supported single-tenant service principals directly and currently uses block controls; software cannot complete human MFA. This policy does not cover managed identities or third-party/multitenant SaaS apps. Putting a service principal in a targeted user group does not apply that policy to it. Keep agent-specific controls separate and check their current scope/licensing. For fundamentals, remember **the right identity, the right policy, then the right resource permission**.

Conditional Access runs after initial authentication signals exist. It is not a firewall and does not directly assign resource permissions.

Microsoft Entra roles administer directory resources. Azure RBAC authorizes Azure resource management/data actions. Application roles and scopes authorize application behavior. Microsoft 365 services also have workload-specific roles. Choose the control plane that owns the resource.

#### Follow an access request

Trace a request in this order; a later success does not repair an earlier failure:

1. **Identify the subject and resource.** A human, service principal, managed identity, device, or agent requests a cloud application or resource.
2. **Authenticate.** Entra validates the applicable credential, key, certificate, federated assertion, or authentication method and produces identity claims.
3. **Evaluate access policy.** Conditional Access combines assignments and signals such as resource, location, device, sign-in risk, or authentication strength, then blocks or imposes grant/session controls.
4. **Authorize.** The resource evaluates an Entra directory role, [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) assignment, application scope/role, or service-specific permission.
5. **Govern and observe.** Entitlement management, access reviews, PIM, sign-in/audit logs, and risk detections help keep access appropriate over time.

Passing MFA proves that configured authentication evidence was supplied. It does not prove the device is compliant, grant an Azure role, make the activity low risk, or show that the access is still needed. Conversely, a role assignment cannot bypass an applicable Conditional Access block.

> **Related item:** Phishing-resistant MFA and device compliance solve different risks. One strengthens the sign-in ceremony; the other supplies a device-state signal. A Conditional Access policy can require both for a sensitive resource.

### Identity governance and protection

| Capability | Question answered |
|---|---|
| Entitlement management/access packages | How should users request and receive bundles of access with approvals/expiration? |
| Access reviews | Does a user still need existing access? |
| Privileged Identity Management | How should privileged role activation be time-bound, approved, and audited? |
| Lifecycle workflows | How should joiner/mover/leaver identity tasks be automated? |
| ID Protection | Which users/sign-ins are risky, and what response should policy require? |

[Identity Governance](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview) addresses identity and access lifecycle at scale. [Access reviews](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview) re-evaluate existing access; they are different from approving the original request. PIM makes an eligible privileged role [activatable under configured controls](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure); it does not make privileged activity harmless. [ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) supplies risk detections that policies and investigators can use; a detection is not proof that every flagged user is compromised.

**Worked example — a decision is not removal:** three reviewed users are denied access: Ada has direct cloud-group membership, Ben inherits access through a nested group, and Cora belongs to a group synchronized from on-premises. With automatic application disabled, zero memberships have changed merely because reviewers selected Deny. After applying supported results, Ada's direct assignment can be removed; Ben's nested membership and Cora's source-directory membership require separate action. Validate effective access, not just a completed review. The [access-review results guidance](https://learn.microsoft.com/en-us/entra/id-governance/complete-access-review) documents these limits, including dynamic membership.

PIM also distinguishes eligible from active assignments. An eligible administrator must activate under configured controls; an already active assignment does not gain an activation gate simply because PIM exists. Separate role permission, eligibility, activation and review.

Use a joiner–mover–leaver lens. A joiner receives approved, time-bounded access; a mover has obsolete access removed as duties change; a leaver is disabled and deprovisioned promptly. Access packages and lifecycle workflows help orchestrate those changes, reviews challenge accumulated access, and PIM reduces standing privilege. Monitoring remains necessary because correct entitlement does not guarantee safe behavior.

---

## 3. Azure infrastructure and cloud security

### Network and platform controls

| Control | Main purpose |
|---|---|
| Azure DDoS Protection | Helps protect public IP resources from volumetric/network attacks under applicable plan |
| Azure Firewall | Managed stateful network firewall with centralized policy |
| Web Application Firewall | Filters common web application attacks at HTTP/S layer |
| Network security group | Allows/denies network flows to subnets/interfaces using rules |
| Azure Bastion | Browser-based RDP/SSH access without exposing VM public management ports |
| Azure Key Vault | Protects and controls access to secrets, keys, and certificates |
| Private Link/private endpoint | Provides private VNet address to supported services |

Network controls are complementary. [DDoS Protection](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview) addresses network-layer availability attacks against applicable public resources. [Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/overview) centrally filters network traffic, while [WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview) understands HTTP/S web-request patterns. [NSGs](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) filter flows at subnet or network-interface boundaries. [Bastion](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview) changes the administrative access path; [Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) protects secrets, keys, and certificates. An NSG is not a WAF; a WAF does not replace application authentication; a private endpoint does not grant access.

A [virtual network](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) provides a private networking boundary; subnets divide its address space. Subnet separation alone is not a deny rule: routes, peering, NSGs and firewalls determine permitted communication. Default NSG rules include virtual-network traffic allowances, so validate the intended trust boundary explicitly.

**Worked example — priority and connection state:** two inbound rules match a new TCP connection to port 443: Allow at priority 200 and Deny at 300. The lower number is evaluated first, so the new flow is allowed. Moving the deny to 100 blocks a new matching connection, but an already established flow is not automatically terminated by that NSG rule update. Test a new connection separately from an existing session. This illustrates stateful filtering, not a recommendation to run disruptive network changes.

[Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview) provide a private IP path to a supported service; connection approval and DNS must work. The application still needs resource authorization. Check the service's public-access setting separately rather than treating a private IP as proof of every exposure control.

Key Vault has a similar separation: configuring the vault is different from reading its secrets. [Current Key Vault defaults](https://learn.microsoft.com/en-us/azure/key-vault/general/access-control-default) use RBAC for new vaults created with API 2026-02-01 and later; existing vault updates retain their access model. A current creation default does not prove that an older vault has migrated.

#### Follow an inbound application request

Consider an internet client calling an Azure-hosted web application:

1. DDoS protections help maintain network availability during eligible attacks.
2. A WAF can inspect the HTTP/S request for common web exploits before it reaches the application.
3. Firewall and routing policy can control permitted network paths; an NSG can allow or deny flows at a subnet or interface.
4. The application still authenticates and authorizes the caller. Network reachability is not application permission.
5. The workload retrieves permitted secrets or cryptographic keys from Key Vault using an authorized identity; secrets should not be embedded in code.
6. Platform, application, identity, and security logs supply evidence for detection and investigation.

No single item in the sequence proves the application is secure. A private endpoint can reduce public exposure but cannot correct an overly broad identity permission; a WAF can block known request patterns but cannot patch flawed business logic.

### Microsoft Defender for Cloud

[Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) combines cloud security posture management (CSPM) with cloud workload protection (CWP) capabilities. Posture management assesses configurations, inventory, attack paths, standards, and recommendations. Workload-protection plans add threat-detection capabilities for eligible servers, storage, databases, containers, APIs, and other resources. **VERIFY CURRENT:** plans, included capabilities, coverage, and pricing.

Security policies and regulatory-compliance views organize expected controls and assessment. Secure score summarizes posture recommendations and relative improvement opportunities. A score is a prioritization tool, not certification or a guarantee.

Defender for Cloud can cover Azure and connected multicloud/on-premises resources under configured connectors and Azure Arc/plan prerequisites. Coverage must be verified; portal visibility alone does not prove every workload sends telemetry.

[Current Defender for Cloud release notes](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) distinguish classic Secure Score from the newer risk-based Cloud Score; always name the score and its assessed population. They also announce that free Foundational CSPM becomes opt-in for **new Azure subscriptions on October 27, 2026**. Existing Azure configuration and AWS/GCP are outside that default change. For a new subscription, verify enablement and coverage before interpreting a blank dashboard as a healthy environment.

> **Related item:** Posture management asks whether a system is configured to reduce risk; threat protection asks whether suspicious activity is occurring. Mature programs need both prevention and detection/response.

---

## 4. Microsoft threat protection and security operations

### Microsoft Sentinel

[Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview) is a cloud-native SIEM and security orchestration, automation, and response platform. Data connectors ingest relevant telemetry. Analytics rules and Microsoft detections create alerts/incidents. Hunting queries explore hypotheses. Automation rules and playbooks triage or respond under controlled conditions. Workbooks visualize data.

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

[Sentinel is available in the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal) without requiring Defender XDR or E5 just to use Sentinel there. Integrated Defender products still have their own prerequisites. Azure-portal support ends after March 31, 2027. Learn the SIEM/SOAR concepts and current Defender navigation; an older video's Azure screen does not establish the current setup path.

### Microsoft Defender XDR

[Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender) unifies detection, investigation, and response across supported endpoints, identities, email/collaboration, and cloud applications. The suite includes capabilities associated with:

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

[Defender Vulnerability Management](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management) discovers assets and software weaknesses, prioritizes them using exposure/business/threat context, and tracks remediation. A vulnerability recommendation is not proof that exploitation happened, and opening a remediation task does not install a patch. Its integration into Exposure Management includes a preview experience; licensing and portal layout vary.

[Microsoft Threat Intelligence in Defender](https://learn.microsoft.com/en-us/defender/threat-intelligence/what-is-microsoft-defender-threat-intelligence-defender-ti) supplies research about actors, campaigns, techniques, indicators and vulnerabilities and connects it with organizational evidence. Current guidance describes Overview, Intel explorer, entity enrichment and threat analytics reports. Some September experiences are prerelease; an ISOC workspace requirement applies to those ISOC features, not every threat-intelligence capability. Distinguish a report about a campaign, an indicator match in local telemetry and an analyst's confirmed incident. One does not automatically establish the others.

Sentinel and Defender XDR integrate but are not synonyms. Defender XDR centers Microsoft XDR signals and response; Sentinel provides broader SIEM/SOAR collection, correlation, hunting, and automation across Microsoft and third-party sources.

> **Related item:** An alert is a detection signal; an incident is an investigation container; a case outcome is an analyst conclusion. Suppressing noisy alerts without understanding why they fire can hide a coverage or configuration failure.

#### Follow a security signal

A useful operations path is **exposure → telemetry → detection → correlation → investigation → response → evidence**:

1. Defender for Cloud identifies a posture weakness such as exposed management access or a missing workload-protection prerequisite.
2. A preventive control is corrected, or the risk is accepted by the accountable owner. A recommendation alone is not an active attack.
3. If suspicious activity occurs, a workload, identity, endpoint, email, application, or third-party source emits telemetry.
4. A Defender product or Sentinel analytic creates an alert. Related alerts may be correlated into an incident.
5. Analysts establish scope and confidence using entities, timelines, device/user context, hunting, and threat intelligence.
6. Authorized responders contain and remediate—for example by isolating a device, disabling an identity, removing a malicious message, or blocking an indicator.
7. Audit trails, incident records, retained logs, and lessons learned support recovery and future control improvement.

This sequence explains several exam boundaries. Secure score and recommendations describe posture; alerts describe detected signals; incidents organize investigation; playbooks automate approved steps; threat intelligence adds context rather than proving compromise.

---

## 5. Microsoft Purview and compliance

### Trust, privacy, and compliance management

The [Microsoft Service Trust Portal](https://servicetrust.microsoft.com/) provides audit reports, certifications, and trust/compliance documentation, with authentication required for some material. Microsoft privacy principles and contractual materials explain provider practices. Customers still determine their own legal obligations and configurations. A provider audit report is evidence about the provider's controls, not proof that the customer configured its tenant or business process correctly.

Microsoft's [commercial-cloud privacy commitments](https://www.microsoft.com/en-us/trust-center/privacy) emphasize customer control, transparency about location/use, protection of data and controlled responses to data requests. For a learning exercise, map each promise to evidence you would seek: service settings, contractual scope, access controls or an assurance report. Do not turn a broad privacy statement into a claim that every workload stays in one chosen region or that a customer has met all obligations.

[Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager) maps controls and improvement actions to assessments and provides a compliance score. The score helps prioritize work; it is not a legal guarantee, formal certification, or legal advice. Some actions are Microsoft-managed and others customer-managed, echoing the shared-responsibility model.

### Information protection and data lifecycle

| Capability | Purpose |
|---|---|
| Sensitive information types/classifiers | Detect content patterns or categories |
| Sensitivity labels | Classify and apply protection/marking under policy |
| Data Loss Prevention | Detect and restrict risky sharing/use across supported locations |
| Retention labels/policies | Keep or delete content according to lifecycle requirements |
| Records Management | Apply stronger records controls and disposition processes |
| Content Explorer | Inspect classified/labeled content under restricted roles |
| Activity Explorer | Investigate activities involving sensitive/labeled content |

[Data classification](https://learn.microsoft.com/en-us/purview/data-classification-overview) identifies what data is through sensitive information types, trainable classifiers, labels, and related signals. A [sensitivity label](https://learn.microsoft.com/en-us/purview/sensitivity-labels) communicates classification and can apply protection such as encryption, markings, or container settings according to configuration. [DLP](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) detects governed information and can audit, warn, block, or otherwise restrict supported activities. [Retention](https://learn.microsoft.com/en-us/purview/retention) answers how long content must be kept or when it should be deleted. These controls can interact, and retention may preserve content even after a user deletes it from the normal interface.

A sensitivity **label** defines classification/protection settings; a [publishing policy](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels) makes selected labels and policy settings available to targeted users. Publishing a label is not proof that all existing files have received it. Manual, default and automatic application are separate choices. Likewise, a retention policy usually scopes a location, a retention label applies to an item, and a label policy distributes or automatically applies retention labels under its configured conditions.

**Worked example — compare retention end dates:** a SharePoint file was created in 2021 and last modified in 2026. One ordinary retention requirement keeps it seven years from creation (through 2028); another keeps it five years from modification (through 2031). The five-year setting produces the later endpoint. Under ordinary retention principles, retention wins over conflicting permanent deletion, and visible deletion can leave a preserved copy. Do not promise deletion on an exact date without checking holds, record settings and processing. Special priority-cleanup workflows have different rules; they are outside this exercise.

Content Explorer answers “where is classified or labeled content?” Activity Explorer answers “what supported activity happened to that content?” Neither is a replacement for least-privilege access, and access to explorer data is itself sensitive and role-controlled.

The blueprint still names Content explorer, while current Purview documentation also describes [Data explorer](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer). Learn the purpose as well as the label in the navigation. Data Explorer List viewer and Content viewer are separate permissions; opening the tab does not grant item/content access. Content viewing is privileged and can supersede the item's ordinary local permissions, subject to scope and documented encryption limits. Activity Explorer shows supported events rather than acting as a universal content search.

### Risk and investigation solutions

| Solution | Focus |
|---|---|
| Insider Risk Management | Signals and workflows for potentially risky insider activity with privacy controls |
| Communication Compliance | Policy review of risky/inappropriate communications in supported channels |
| Audit | Search and retain supported user/admin activity under applicable licensing |
| eDiscovery | Identify, preserve, collect, review, and export relevant content for investigations/legal matters |

[Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management) correlates configured signals into privacy-aware risk workflows; it does not declare a person guilty. [Audit](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) supplies searchable activity evidence under applicable service, retention, role, and licensing boundaries; it does not preserve every content item. [eDiscovery](https://learn.microsoft.com/en-us/purview/ediscovery) is a governed preservation, search, collection, review, and export workflow, not ordinary keyword search. Retention and holds affect whether content remains available.

> **Related item:** Data minimization reduces both privacy exposure and discovery/retention cost. Keeping everything forever can conflict with legal, privacy, and business requirements just as deleting too early can.

#### Follow a document through its lifecycle

Suppose a finance team creates a spreadsheet containing customer tax identifiers:

1. A sensitive information type or classifier detects regulated content; classification establishes what kind of data is present.
2. A sensitivity label marks the document and, if configured, applies protection such as encryption. The label travels with the content under supported conditions.
3. A DLP policy detects an attempted external share and warns or blocks according to policy. DLP governs the action; it does not decide the user's general entitlement to the SharePoint site.
4. A retention policy or label preserves the document for the required period and applies the configured disposition behavior. Retention is not the same as backup or sensitivity protection.
5. Audit records supported user or administrator activity. Activity Explorer can expose relevant data-use events; the exact event and retention depend on current configuration and licensing.
6. If litigation or an investigation begins, eDiscovery can identify custodians and locations, preserve relevant content, collect it into a review set where applicable, and export governed results.
7. Compliance Manager may track improvement actions and evidence for an assessment, while the Service Trust Portal supplies Microsoft assurance documentation. Neither makes the legal determination for the organization.

At every stage, define the data owner, compliance/legal decision owner, security operator, and service administrator. A tool can enforce a configured decision, but it does not invent the organization's classification, retention schedule, risk appetite, or legal obligation.

---

## 6. Objective-to-scenario drill

Use the wording in the scenario before choosing a product. The same asset can pass through several controls, so select the service that answers the question actually asked.

| Scenario clue | Best starting concept or capability | Boundary to preserve |
|---|---|---|
| Who secures the hypervisor for an Azure VM? | Shared responsibility; Microsoft | The customer still owns guest OS, application, data, identity, and configuration duties applicable to IaaS |
| Confirm the requester, then decide access from user, device, risk, and resource signals | Entra authentication plus Conditional Access | Authentication/CA do not create the application's or Azure resource's permission |
| Grant a vendor a time-limited bundle of group, app, and site access | Entitlement management/access package | Access review later asks whether granted access remains appropriate |
| Require approval and MFA only when an admin activates a privileged role | PIM | Azure RBAC or an Entra role defines permission; PIM governs eligible activation |
| Investigate leaked credentials or an anomalous sign-in | Entra ID Protection | A risk signal informs policy/investigation; it is not a final incident verdict |
| Reduce standing public RDP/SSH exposure while retaining browser-based administration | Azure Bastion | Bastion changes the management path; authorization and VM hardening still apply |
| Filter SQL injection-like HTTP requests | WAF | Azure Firewall/NSG filter network traffic but do not provide the same web-application inspection |
| Prioritize misconfigurations against a security standard | Defender for Cloud CSPM | A recommendation/secure score is posture evidence, not an active threat detection or certification |
| Detect suspicious behavior within a protected server or storage workload | Defender for Cloud workload protection | Coverage depends on enabled plan, supported resource, deployment, and telemetry |
| Correlate endpoint, identity, email, and SaaS alerts into one investigation | Defender XDR | Sentinel is broader SIEM/SOAR across Microsoft and third-party data sources |
| Ingest firewall and third-party logs, run analytics, and automate incident triage | Sentinel | A connector supplies data; a rule detects; an incident groups; a playbook acts |
| Apply encryption and markings based on document classification | Sensitivity label | The label is not a retention schedule or a general resource permission |
| Stop a user from sending a tax identifier externally | DLP | DLP governs data activity; it does not replace classification, access control, or retention |
| Keep a contract for seven years and then dispose of it | Retention/Records Management | Retention is not backup, encryption, DLP, or eDiscovery collection |
| Find who changed a policy yesterday | Audit | Audit records supported activity; eDiscovery handles governed content preservation/collection/review |
| Preserve and collect relevant mailbox and site content for a legal matter | eDiscovery | Search permissions, holds, review, and export need governed roles and procedures |
| Obtain Microsoft's independent audit reports for a supplier review | Service Trust Portal | Provider evidence does not validate the customer's implementation |

#### Integrated scenario: compromised administrator and sensitive export

An administrator signs in from an unfamiliar device, activates a privileged role, exports sensitive records, and attempts to upload them to an unsanctioned cloud app. Decompose it rather than naming one “security product”:

- Entra authentication establishes the administrator identity; Conditional Access can require stronger authentication, device state, or block based on applicable conditions.
- ID Protection can contribute user/sign-in risk. PIM controls role eligibility and activation. Directory and service audit logs record supported actions.
- Defender XDR products can contribute identity, endpoint, application, and other signals and correlate an incident. Sentinel can ingest broader sources, correlate detections, and run controlled automation.
- Classification identifies the records; sensitivity labels can protect them; DLP and supported cloud-app controls can detect or restrict the transfer.
- Retention determines whether content remains; Audit supports activity investigation; eDiscovery supports governed preservation and collection if the event becomes a legal matter.
- Security operations contains the threat, identity administrators remediate access, data/compliance owners assess disclosure and policy, and legal/privacy teams determine notification or preservation duties.

The products overlap through signals and integrations, but ownership and purpose remain distinct. This is why “which portal?” is usually a weaker question than “which decision, control, or evidence is needed?”

---

## 7. Hands-on labs

### Lab 1: Identity decision map

For an employee, contractor, Azure workload, device, and agent, identify identity type, authentication, Conditional Access, authorization plane, lifecycle owner, review, and emergency recovery.

### Lab 2: Conditional Access tabletop

Draft a report-only policy for administrators that requires phishing-resistant authentication and compliant devices. Define exclusions, break-glass monitoring, test users, expected logs, rollout, and rollback. Do not enforce in a real tenant without authorization.

### Lab 3: Posture to incident

Choose a hypothetical exposed VM. Trace preventive controls (NSG, patching, Key Vault, posture recommendations), detections (Defender), correlation/investigation (Defender XDR or Sentinel), response, and retained evidence.

### Lab 4: Data protection lifecycle

Classify a public sample document, propose a sensitivity label, DLP rule, retention requirement, and investigation path. Explain why each control answers a different question.

### Lab 5: Portal boundary tour

In a permitted tenant or documentation screenshots, locate Entra, Defender, Defender for Cloud, Sentinel, Purview, and Service Trust/Compliance Manager surfaces. Write the primary asset, signal, control, and owner for each.

### Lab 6: Verify identity and policy outcomes

Use synthetic records for the two-tenant application and three-person access review examples. Record the definition, local instance, permission owner, review decision, applied result and effective access. Compare a human MFA policy with supported workload-identity policy. **Expected evidence:** separate tenant grants, zero removals before application, and two unresolved inherited/source-managed paths afterward.

### Lab 7: Explain controls using current evidence

1. Draw a VNet with web and data subnets. Mark an explicit allowed path, denied path, private endpoint and resource permission.
2. Calculate the two retention endpoints. Explain why a published label, a retention hold and an audit event are different evidence.
3. Read the passkey announcement and selected social-engineering sections below. Design a legitimate enrollment communication with a known helpdesk verification channel.
4. Map a hypothetical suspicious sign-in to identity logs, local threat evidence, incident investigation and data-protection controls; label missing evidence.

**Expected evidence:** a control diagram, 2028/2031 comparison, dated user-population transition note and an incident evidence map. No live policy enforcement, credential reset or attack reproduction is required.


---

## 8. Knowledge checks and distinctions

These are original questions with explanations, not recalled exam content.

1. **Encrypted storage is publicly readable. What is still wrong?** Access control permits unauthorized readers; encryption at rest does not decide who may request readable data.
2. **A user passes MFA but an app is blocked. What should you inspect?** Applicable Conditional Access policies, authentication strength, device/risk/location signals and sign-in results; then verify the resource's permission independently.
3. **Does Global Administrator automatically grant Azure VM Contributor?** No. Directory administration and Azure resource authorization are different control planes; verify the actual resource role assignment.
4. **Why can a posture recommendation exist without an incident?** A weak configuration is exposure evidence. An incident requires relevant detected/correlated activity; neither a blank incident queue nor a recommendation alone proves compromise.
5. **DLP blocks sharing while retention keeps a deleted copy. Why?** DLP governs the data action; retention preserves content for its configured lifecycle. They serve different goals.
6. **Does impossible travel prove compromise?** No. Investigate identity, session, location and related activity; risk is a signal with possible benign explanations.
7. **One multitenant app serves two tenants. How many local instances?** Two service principals, one per tenant, with separately governed permissions; one application definition is not one universal grant.
8. **Can a managed identity satisfy a human MFA prompt?** No. Software identities need suitable authentication and authorization; the documented service-principal CA policy does not cover managed identities.
9. **Does system-preferred authentication enforce passkey-only access?** No. Preference, registration and an authentication-strength requirement are different controls.
10. **A reviewer denied access but membership remains. What next?** Check completion and result application, then nested, dynamic or on-premises membership and other independent grants. Verify effective access.
11. **Does an eligible PIM role already allow privileged work?** It requires activation under its configured controls. An active assignment is different; PIM does not erase the underlying role's privileges.
12. **Does placing servers in different subnets deny communication?** No. Evaluate routes and effective NSG/firewall rules; subnet boundaries alone are not deny policies.
13. **A new NSG deny blocks a fresh test but an old session continues. Why?** NSGs are stateful; updates affect new flows and do not automatically end established connections.
14. **Does a private endpoint authorize secret access?** No. Connection approval, DNS/network reachability and Key Vault data authorization are separate checks.
15. **Does a threat report's indicator match establish a confirmed incident?** No. Validate time, source, asset behavior, context and corroborating evidence before a conclusion or response.
16. **Does publishing a sensitivity label encrypt every existing document?** No. Publishing makes labels/settings available; actual application and configured protection must be verified.
17. **Which retains our example file longer: seven years from 2021 or five from 2026?** Five from 2026 ends in 2031, later than 2028. Compare actual start/end dates and applicable holds.
18. **What do explorer and provider-assurance access prove?** Access is role/scope controlled. Explorer content access can be privileged; a provider report concerns its stated controls and does not prove the customer's configuration or compliance.

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

### Readiness checklist

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

### Primary references

- [Official SC-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)
- [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)
- [Microsoft Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/)
- [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/)
- [Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/)
- [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/)
- [Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)
- [Service Trust Portal](https://servicetrust.microsoft.com/)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Published runtimes are distinguished from suggested study allocations and earlier metadata. Labs, note-taking, review and independent practice add time; no paid course or signed-in assessment was completed in this review.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — SC-900 course](https://learn.microsoft.com/en-us/training/courses/sc-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation across identity, security, and compliance |
| [Microsoft — SC-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/practice/assessment?assessment-type=practice&assessmentId=11&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Launch from the credential page; direct assessment retrieval returned no content, so signed-in questions and completion were not verified |
| [Microsoft Partner Skilling Hub — LevelUp SC-900](https://www.skilling-hub.com/en-US/listing/o::levelup::2058350) | Partner login required | Earlier five-hour metadata; current access returned a shell | Partner eligibility, current runtime and syllabus were not independently reverified |
| [Microsoft Learn SC-900 learning paths](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/) | Free | Suggested 10–14 hour study allocation; current module total not timed | Official scope anchor; use current syllabus and add portal exploration where permitted |
| [John Savill — SC-900 Study Cram v2](https://www.youtube.com/watch?v=-FJqb60wPSY) and [certification materials](https://github.com/johnthebrit/CertificationMaterials) | Free | Earlier 3–4 hour estimate; current video returned a shell | Public companion repository was accessible, but the video was not watched/timed; cross-check current identity/security changes. Link rather than republish the unlicensed artifact. |
| [Pluralsight — SC-900 path and practice exam](https://www.pluralsight.com/paths/microsoft-security-compliance-and-identity-fundamentals-sc-900) | Subscription; practice access depends on plan/library | 8h45 summed lessons (path rounds to nine hours), plus assessment/review | Six-course path whose public page includes a practice exam; instruction is mostly 2023–2024, so cross-check every product boundary with current Learn |
| [O'Reilly — Exam Ref SC-900, 2nd Edition](https://www.oreilly.com/library/view/exam-ref-sc-900/9780138363727/) | Subscription | Earlier 5h41 estimate | Earlier 193-page/May 2024 metadata; current O'Reilly access blocked, so contents and availability were not reverified |
| [Udemy — SC-900 by Kevin Brown](https://www.udemy.com/course/sc-900-microsoft-security-compliance-and-identity/) | Purchase or subscription | Earlier eight-hour estimate | Earlier October 2025 update metadata; current Udemy access blocked. Verify live syllabus before purchase |
| [LinkedIn Learning — SC-900 Cert Prep by Microsoft Press](https://www.linkedin.com/learning/microsoft-security-compliance-and-identity-fundamentals-sc-900-cert-prep-by-microsoft-press) | Subscription | 3 hours 32 minutes | Christopher Wojahn course released June 2024; concise fundamentals, but fill July 2026 changes from Learn |
| [Microsoft Security Virtual Training Days](https://www.microsoft.com/en-us/events/category/microsoft-virtual-training-days?filters=product%3Amicrosoft-security&scenario=mvtd) | Free registration when scheduled | Usually 1–2 half days | Live fundamentals sessions; schedule and exact SC-900 coverage vary |
| [MeasureUp — SC-900 practice test](https://www.measureup.com/microsoft-practice-test-sc-900-microsoft-security-compliance-and-identity-fundamentals.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | 124 questions; public last update remains August 2025, predating July/October 2026. No paid questions or demo reviewed; ignore generic 150-question FAQ copy for product counts |
| [Whizlabs — SC-900 training and practice](https://www.whizlabs.com/microsoft-security-compliance-identity-fundamentals-sc-900-certification/) | Paid course or subscription | About 4–8 hours for assessment and review; course total not verified | Current page returned a shell; runtime, product contents and July/October coverage were not verified |

### Useful blog reading with a learning task

- **Nadim Abdo, July 13, 2026 — [Entra passkey default announcement](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/).** Explain public-key authentication, then separate enabled, registered, preferred and required. Compare the announcement with September Learn guidance for the February/July 2027 population-specific dates. Avoid repeating the earlier blanket February deadline. Allow 20–30 minutes for reading and a transition sketch; tenant rollout was not tested.
- **Microsoft Security Research and named researchers, September 9, 2026 — [Passkey-themed social engineering](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/).** Read the opening attack-chain and mitigation sections, then practice independently verifying an unsolicited helpdesk request. A passkey-themed lure can lead to a different authentication flow; it is not proof that passkey cryptography was broken. Map authentication changes, cloud activity and response evidence across Entra, Defender and Purview. Allow 30–45 minutes; use a tabletop rather than reproducing the attack.

The first public article was read; the second's introduction, initial-access examples and mitigation sections were reviewed, not every query or indicator. Linked threat intelligence, videos and deployments were not tested. LinkedIn's current public listing confirms Christopher Wojahn/Microsoft Press, 3h32, June 11, 2024; Pluralsight's six Vlad Catrinescu lessons total 8h45 and date from December 2023–January 2024. These catalog checks do not establish lesson completeness for the current blueprint. Service Trust and partner pages require access to verify underlying content.

The [deep-review record](../docs/research/2026-09-27-sc-900-deep-review.md) maps all 58 October objectives, records source/access limits and schedules follow-ups. Human review remains pending.



The assessment products above supplement—not replace—explanatory learning and authorized portal exploration. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
