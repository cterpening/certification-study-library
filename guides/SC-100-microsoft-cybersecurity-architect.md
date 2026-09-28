---
exam_code: SC-100
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-27
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-27
---

# SC-100 Microsoft Cybersecurity Architect Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 27, 2026; all 81 published October objectives were separately mapped while retaining the accepted July baseline; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#sc-100-coverage-record). The [official SC-100 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) is authoritative.

**Current baseline:** Skills measured as of July 28, 2026; accepted objective snapshot retained; current live page presents October preparation.<br>
**Exam state:** Active; the official exam page lists no retirement date.<br>
**Upcoming blueprint change (checked September 27, 2026):** The English blueprint changes October 21, 2026. The revision expands SOAR as security orchestration, automation, and response and uses Microsoft 365 Copilot naming. Domain weights are unchanged. The current baseline below remains dated separately. See the [official revision](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100).<br>
**Localized exams:** Microsoft says localized versions normally follow the English update by approximately eight weeks; verify the language version before scheduling.<br>
**Official source:** [SC-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)

## How to use this guide

SC-100 is an architecture exam. It assumes that you can already administer or implement at least one security domain and asks you to join those domains into a defensible enterprise design. For every topic, practice this reasoning chain:

```text
business mission and critical assets
  → threat, regulation, and risk tolerance
  → identity, network, device, application, data, and operations boundaries
  → preventive, detective, responsive, and recovery controls
  → ownership, evidence, exception, and improvement loop
```

Read Sections 1–5, work through the three integrated scenarios, implement or tabletop the ten labs, and answer all 44 checks. Do not memorize a product list. Be able to explain why a control belongs at a particular layer, which signal proves it works, what fails open or closed, and how the organization recovers.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Exam profile and objective map

The certification is expert-level. To earn **Microsoft Certified: Cybersecurity Architect Expert**, Microsoft currently requires SC-100 plus one active prerequisite credential: Identity and Access Administrator Associate, Security Operations Analyst Associate, or **Cloud and AI Security Engineer Associate**. The current credential page has replaced the older Azure Security Engineer listing; an older course recommendation is not the current certification requirement. Confirm the current choices on the [credential page](https://learn.microsoft.com/en-us/credentials/certifications/cybersecurity-architect-expert/).

| Official domain | Weight | Architect's central question |
|---|---:|---|
| Design solutions that align with security best practices and priorities | 20–25% | How do business priorities, threats, resilience, Zero Trust, MCRA, MCSB, CAF, WAF, landing zones, AI, and DevSecOps become a coherent strategy? |
| Design security operations, identity, and compliance capabilities | 25–30% | How should telemetry, detection, response, identity, privilege, and compliance operate across the estate? |
| Design security solutions for infrastructure | 25–30% | How should posture, workload protection, endpoints, service models, AI workloads, networks, and SSE be secured across hybrid and multicloud environments? |
| Design security solutions for applications and data | 20–25% | How should Microsoft 365, applications, APIs, software delivery, data, encryption, and AI grounding be protected? |

### Complete objective-to-guide map

| Published objective area | Primary coverage | Practice evidence |
|---|---|---|
| Ransomware, business resiliency, BCDR, secure backup/restore, privileged access, and security updates | Section 1 | Scenarios 1 and 3; Labs 1 and 3 |
| MCRA, MCSB, attack categories, Zero Trust, CAF, WAF, secure AI adoption, landing zones, and DevSecOps | Section 1 | All scenarios; Labs 1–2 |
| XDR, SIEM, logging/auditing, multicloud monitoring, SOAR, workflows, incident response, hunting, and MITRE ATT&CK coverage | Section 2 | Scenarios 1 and 3; Labs 3–4 |
| Human, external, workload, and agent identity; Conditional Access; AD DS; secrets, keys, and certificates | Section 2 | All scenarios; Lab 5 |
| Enterprise access model, PIM, entitlement management, access reviews, tenant administration, CIEM, and privileged workstations | Section 2 | Scenarios 1 and 3; Lab 5 |
| Compliance translation, Purview, Azure Policy, Defender for Cloud standards and benchmarks | Section 2 | Scenarios 1–2; Lab 6 |
| Defender for Cloud, MCSB, Secure Score, multicloud CSPM/CWPP, Azure Arc, EASM, and Exposure Management | Section 3 | All scenarios; Labs 2 and 6 |
| Server/client/mobile/IoT/OT security, baselines, Defender for IoT, and Windows LAPS | Section 3 | Scenarios 1 and 3; Lab 3 |
| SaaS/PaaS/IaaS, web, container/orchestration, IoT, and Azure AI service security | Section 3 | Scenarios 1–2; Labs 2 and 7 |
| Network design plus Entra Internet Access and Private Access | Section 3 | All scenarios; Lab 7 |
| Microsoft 365 posture, Defender for Office 365, Defender for Cloud Apps, Intune, Purview, and Copilot controls | Section 4 | Scenario 2; Lab 8 |
| Application portfolios, threat modeling, secure lifecycle, DevSecOps, workload identities, APIs, and Azure WAF | Section 4 | Scenarios 1–2; Labs 2 and 7 |
| Data discovery/classification, threat priorities, encryption, Key Vault, AI data, Azure SQL/Synapse/Cosmos DB/Storage, and Defender plans | Section 4 | Scenarios 1–2; Labs 6 and 8 |

## 1. Align architecture with security priorities

### Start with mission, assets, threats, and accountability

An architecture is not a diagram of products. Establish:

- business services and the consequences of confidentiality, integrity, or availability failure;
- authoritative asset/identity/data inventories and business owners;
- adversaries and plausible paths, including insider, external, supply-chain, ransomware, and AI-specific threats;
- legal, regulatory, contractual, residency, recovery, and audit requirements;
- risk acceptance authority, exception expiry, and remediation ownership;
- measurable target state, milestones, and residual risk.

Threats should drive priorities, while frameworks reduce omissions. A benchmark is not a risk assessment, a secure score is not business impact, and a passed compliance test is not proof that an attack path is closed.

> **Related item:** Distinguish **risk owner** from **control owner**. A platform team might operate a policy, but the business owner accepts residual risk to the critical service.

### Design ransomware resilience as an end-to-end capability

Ransomware planning spans prevention, containment, detection, recovery, and business continuity:

1. Identify mission-critical services, dependencies, identity control planes, recovery time objectives (RTOs), and recovery point objectives (RPOs).
2. Protect privileged identities and administrative paths first. Separate accounts, use phishing-resistant authentication, just-in-time privilege, protected workstations, and emergency access.
3. Reduce exposure through patch/service-level objectives, hardening, segmentation, endpoint protection, and attack-surface reduction.
4. Protect backups with isolation, immutability where appropriate, separate authorization, soft delete/resource guards where supported, encryption, monitoring, and tested restore.
5. Detect destructive behavior across identity, endpoints, cloud control planes, workloads, backup systems, and data.
6. Predefine containment authority, communications, evidence handling, rebuild criteria, and recovery sequence.
7. Exercise restore and business operation—not just backup job success—and feed lessons into architecture and governance.

Secure backup design asks who can delete or encrypt recovery points, whether production compromise crosses the administrative boundary, and whether a clean identity/platform foundation can be restored before applications. Security updates require asset inventory, risk-based prioritization, deployment rings, exception handling, compensating controls, rollback, and compliance evidence.

> **Related item:** RTO is maximum acceptable service restoration time; RPO is maximum acceptable data loss measured in time. Neither proves that backups are clean, reachable during crisis, or restorable in dependency order.

### Prove the recovery boundary

[Azure Backup immutability](https://learn.microsoft.com/en-us/azure/backup/backup-azure-immutable-vault-concept) can be enabled reversibly and then locked irreversibly. Distinguish policy-retention-based protection from time-based immutability: the latter currently applies to Recovery Services vaults, and a retained recovery point can outlive its immutable period. Operational backups have different coverage. Service-enforced locked immutability and WORM storage availability also have workload/region distinctions; verify the matrix before asserting a storage-level property.

[Resource Guard authorization](https://learn.microsoft.com/en-us/azure/backup/multi-user-authorization) is a separate control over supported critical operations. Keep its administration independent of the backup administrator, with the guard in the same region as the vault. A separate subscription or tenant can improve separation, but inherited permissions can defeat it. Review protected-operation exclusions and grant the narrow Backup MUA Operator role only when needed, using PIM or another approved process. Do not assume every restore or every administrative action requires a new human approval.

**Worked example — dependency recovery:** A service has a three-hour RTO and 15-minute RPO. In a tabletop, clean identity recovery takes 45 minutes, dependent data restore 90, and application validation 60, sequentially: 195 minutes, 15 beyond the RTO. A failure at 08:00 with the last usable recovery point at 07:30 loses 30 minutes, exceeding RPO by 15. Faster backup jobs alone do not solve the recovery dependency or usable-point gap. These figures are synthetic, not an Azure performance prediction.

### Use MCRA, MCSB, and Zero Trust for different jobs

Microsoft's [MCRA](https://learn.microsoft.com/en-us/security/adoption/mcra) is an end-to-end reference architecture for a hybrid-of-everything estate. Use it to compare current and target capabilities, find integration gaps, and communicate relationships across identity, SecOps, data, endpoints, infrastructure, development, OT, IoT, AI, Microsoft, and third-party technology.

The [Microsoft Cloud Security Benchmark](https://learn.microsoft.com/en-us/security/benchmark/azure/overview) is control guidance with multicloud mappings. Use it to establish baselines, assign controls, map implementation evidence, and identify gaps. It does not replace workload threat modeling or a legal interpretation of a regulation.

Zero Trust supplies three persistent principles:

- **verify explicitly:** evaluate identity, device/workload, resource, network, location, risk, session, and data context;
- **use least privilege:** limit scope, duration, capability, and standing access;
- **assume breach:** segment, encrypt, observe, contain, and recover as if a control will fail.

Use the [Zero Trust adoption framework](https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview) to turn principles into cross-team scenarios, objectives, initiatives, and measurable progress. Applying MFA alone is not Zero Trust; the architecture must continuously enforce across every relevant plane.

| Tool | Primary use | Common misuse |
|---|---|---|
| MCRA | Target-state capability and integration map | Treating every Microsoft product as mandatory |
| MCSB | Baseline control and evidence map | Assuming benchmark compliance proves workload safety |
| Zero Trust | Decision principles across identity, endpoints, apps, data, infrastructure, and network | Renaming a perimeter design without changing trust decisions |
| Threat model | Workload-specific assets, trust boundaries, abuse paths, and mitigations | Running once after deployment |

The current MCSB overview describes **v2 as preview**, with Azure-focused implementation guidance. Its [AI domain](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-artificial-intelligence-security) covers approved models, layered filtering, system instructions, least-privilege tools, human review of critical actions, monitoring and adversarial testing. For each, record an owner and observable evidence. System instructions or a content filter cannot replace authorization on the called tool. The AI article explicitly says its content was last reviewed December 1, 2025 and is recommended guidance, not certification or compliance attestation. Use current service documentation to establish enforceable behavior; a control mapping does not mean Azure Policy implements every requirement.

### Connect CAF, WAF, landing zones, and workload architecture

The [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) guides organization-wide adoption: strategy, plan, ready, adopt, govern, secure, and manage. Its Secure methodology embeds security roles, modernization, incident readiness, confidentiality, integrity, availability, and sustainment across the journey.

The [Azure Well-Architected security checklist](https://learn.microsoft.com/en-us/azure/well-architected/security/checklist) evaluates a workload. It connects security requirements to identity, networking, data, hardening, secret management, monitoring, testing, and incident response while exposing tradeoffs with reliability, cost, performance, and operational excellence.

An Azure landing zone supplies shared platform structure: tenant/identity integration, management-group and subscription organization, policy, connectivity, logging, security, management, and automation. Platform landing zones provide shared governance and services; application landing zones inherit guardrails and host workloads. Do not put workload-specific authorization or threat controls solely in the platform layer.

```text
enterprise risk and operating model
  → CAF adoption, governance, security, and management
  → platform landing-zone guardrails and shared services
  → WAF workload design and tradeoffs
  → MCSB/service baselines + workload threat model
  → policy, deployment, telemetry, evidence, and improvement
```

### Design secure AI adoption and DevSecOps

Secure AI adoption begins with approved use cases, data classification, model/provider risk, identity, network and residency boundaries, human accountability, evaluation, monitoring, and incident response. Apply AI-specific MCSB guidance and service baselines; protect training/grounding data, models, prompts, tools, agents, outputs, and telemetry. Threats include prompt injection, poisoned or overshared grounding, excessive agency, unsafe tool arguments, model/supply-chain compromise, sensitive output, and untracked shadow AI.

DevSecOps puts requirements and evidence inside delivery:

- threat model and abuse cases before implementation;
- branch/repository/workflow/runner and artifact protection;
- dependency, secret, code, infrastructure-as-code, container, and cloud-configuration scanning;
- signed/provenanced artifacts and trusted registries;
- environment separation, least-privilege workload identity, approvals for high-risk change, and reproducible deployment;
- post-deployment validation, runtime protection, telemetry, vulnerability response, and rollback.

Security gates should be risk-based and actionable. A noisy scanner that teams bypass is not a strong control. Define severity thresholds, ownership, service-level objectives, exception evidence, expiry, and feedback from production incidents.

> **Related item:** Supply-chain security covers source, dependencies, build service, runner, credentials, artifacts, registry, deployment identity, and runtime. Scanning source code addresses only part of the chain.

## 2. Design operations, identity, privilege, and compliance

### Integrate XDR, SIEM, SOAR, and audit without duplicating everything

[Microsoft Defender XDR and Microsoft Sentinel](https://learn.microsoft.com/en-us/security/zero-trust/siem-xdr-overview) serve complementary roles. XDR correlates signals and response across integrated Defender domains. Sentinel supplies broad SIEM/SOAR ingestion, analytics, hunting, automation, and multicloud/non-Microsoft coverage. Current unified operations can surface Sentinel in the Defender portal; architecture still requires deliberate workspace, retention, connector, routing, access, and operating-model decisions.

Build telemetry from use cases, not “collect all logs”:

1. Define critical assets, attack hypotheses, response decisions, evidence, and regulatory needs.
2. Identify the authoritative signal and required fields, timestamps, identity/resource context, and correlation keys.
3. Choose native detection/XDR correlation versus SIEM analytics; avoid duplicate incidents and conflicting ownership.
4. Set collection tier, transformation, retention, archive, residency, access, integrity, and cost controls.
5. Map detections to Enterprise, Mobile, and ICS matrices in [MITRE ATT&CK](https://attack.mitre.org/) and record both coverage and tested effectiveness.
6. Automate bounded enrichment/containment; require approval for disruptive or ambiguous actions.
7. Measure mean time to acknowledge/contain/recover, false-positive burden, connector health, telemetry delay, automation failure, and detection test results.

Microsoft Purview Audit covers Microsoft 365 and compliance-relevant activities; Azure activity/resource logs cover control-plane and service events; endpoint/network/application/data sources add workload context. Centralization is a logical operating and evidence strategy, not necessarily one indefinitely retained workspace.

> **Related item:** A data connector being healthy proves transport, not detection. Test end to end: generate a known benign technique, confirm signal fields, alert/incident creation, ownership, automation, evidence preservation, and closure learning.

### Treat Sentinel portal migration as an operational change

[Sentinel in the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal) is available with or without Defender XDR/E5. The current Azure-portal support deadline is **March 31, 2027**. A portal change does not move all workspace logs out of Log Analytics or remove ingestion/retention design work.

The [migration guidance](https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender) identifies changes that require acceptance tests:

- Test connector routing, alert schema and primary/secondary-workspace visibility. Defender-product alerts route through XDR; duplicate standalone ingestion needs review.
- Test incident merging and automation conditions. XDR correlation can override prior grouping assumptions; incident titles are unstable identifiers.
- Inventory CMK requirements by data surface. Existing CMK workspace logs and Sentinel content retain that protection, while alerts/incidents do not; data-lake ingestion uses Microsoft-managed keys under the documented limitation.
- Validate latency and event completeness. Defender incidents can take five minutes to reach Sentinel, and changes within a 5–10-minute window can be delivered as one latest update. An incident-update playbook cannot reconstruct every intermediate change from that delivery alone.

**Worked example — response deadline:** If the service requires containment within four minutes, a route that can take five minutes merely to deliver the incident cannot guarantee that requirement, even with an instant playbook. Record the one-minute minimum gap for that worst-case delivery assumption and select a supported response path with measured end-to-end timing. Do not equate a fast portal display with completed containment.

### Design incident and hunting workflows

Define severity using business impact, asset criticality, identity privilege, confidence, spread, and regulatory triggers. A workflow should specify triage evidence, roles, escalation, containment authority, communications, legal/privacy involvement, forensics, recovery criteria, post-incident review, and backlog updates.

Threat hunting starts with a hypothesis and produces reusable value: a validated finding, improved visibility, a new/tuned analytic, or documented gap. SOAR playbooks should have scoped identities, validated inputs, idempotent operations, audit trails, timeouts/retries, and rollback or human intervention. Never allow untrusted alert content to become an unchecked command or query.

### Make identity the control plane

Design Microsoft Entra ID for availability, emergency access, hybrid identity, tenant boundaries, administrative units, external collaboration, workload identities, monitoring, and lifecycle. Choose authentication for resilience and attack resistance; prefer phishing-resistant methods for high-impact access. Treat AD DS as a separate high-value control plane requiring tiered administration, hardened domain controllers, privileged-path isolation, monitoring, patching, backup/recovery, and reduction of legacy protocols.

Modern access combines:

- subject: human, guest, service principal, managed/workload identity, agent identity, or agent user account;
- resource/audience and permissions;
- authentication strength and credential lifecycle;
- device/workload compliance and risk;
- Conditional Access conditions, exclusions, protected actions, and session controls;
- continuous access evaluation where supported;
- network/application controls and resource-side authorization.

External identity design separates tenant-to-tenant B2B collaboration, customer/external-tenant identity, and decentralized identity. B2B creates or represents an external principal so resource-tenant authorization, cross-tenant access settings, Conditional Access, terms, lifecycle, and access reviews can be applied. Decentralized identity uses verifiable credentials whose issuer, holder, verifier, trust policy, revocation/status, claims minimization, and wallet/recovery model must be designed; [Microsoft Entra Verified ID](https://learn.microsoft.com/en-us/entra/verified-id/decentralized-identifier-overview) is Microsoft's verifiable-credential capability. Do not choose decentralized identity merely to avoid governing guest access—the trust and lifecycle problem changes rather than disappears.

Roll out Conditional Access with report-only analysis, pilot groups, named emergency exclusions, dependency testing, and monitoring. A token is issued to one audience; APIs must still validate issuer, audience, signature, lifetime, scopes/roles, tenant, and business authorization.

### Include agents as first-class identities

[Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) distinguishes agent identity blueprints, agent identities, and optional agent user accounts. Design inventory, owner, purpose, lifecycle, attributes, permission boundaries, authentication flow, activity monitoring, and decommissioning at scale.

[Conditional Access for agents](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) depends on which principal acquires a token. Delegated/on-behalf-of access, autonomous application access, and agent user accounts have different subjects and policy targeting. API keys bypass Entra token issuance and therefore Entra Conditional Access. The current [targeting guide](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities) requires Agent 365 plus appropriate Entra licensing; several agent-user and risk controls remain preview. Record actual licensed capability and policy results.

> **Related item:** Human approval does not repair overprivileged agent identity. Apply least privilege and resource-side authorization before adding approval for high-impact or ambiguous actions.

### Map each agent request to its policy subject

An agent identity has no credential of its own; its blueprint holds the authentication material. A multitenant blueprint can create identities in multiple tenants, but each agent identity remains tenant-local. Inventory the blueprint, agent identity, optional agent user, sponsor, grants and downstream tools separately.

| Access flow | Token subject and policy target | Design consequence |
|---|---|---|
| On behalf of a signed-in person | Person; user/group policies | Exchange for the downstream audience; do not reuse a token issued for another API |
| App-only agent request | Agent identity | Target that identity or blueprint; current agent-identity controls support blocking, not interactive MFA remediation |
| Agent's own user account | Agent user | Target agent users explicitly; “All users,” agent-identity policies and blueprint targeting do not include these accounts |
| API-key request | Outside Entra token evaluation | Apply service-side key, network and authorization controls; Entra policy alone does not cover it |

Group membership does not currently target agent-user policies. Endpoint compliance/network signals require a supported endpoint; applying that requirement to a device-less cloud agent can block it without a remediation route. Use the preview execution-environment condition where supported, and verify what is excluded. Blueprint provisioning and intermediate token-exchange exceptions also mean a successful directory operation is not proof of a protected downstream access decision.

**Worked example — one assistant, three subjects:** Alex asks an assistant to read a document using delegated Graph access; a scheduled task later reads storage as the agent; the agent user then opens its own collaboration workspace. A human “All users” policy targets the first flow, not all three. Create three evidence rows with subject, audience, policy result and resource permissions. Apply the corresponding agent and agent-user policies; human approval does not supply a missing access-control boundary.

### Secure secrets, keys, and certificates

Prefer managed/workload identity and federation over stored credentials. Where secrets remain, use a managed vault with private/network boundaries where required, separate management and data-plane access, least privilege, soft delete and purge protection, rotation, expiry, audit, backup/recovery constraints, and application handling that does not leak values into code, logs, pipelines, or telemetry.

Treat keys and certificates as lifecycle objects: creation/import, algorithm/size, allowed use, HSM requirement, custody, issuance, distribution, rotation/renewal, revocation, recovery, evidence, and destruction. Separate application configuration from secret material.

For [Key Vault API version 2026-02-01 and later](https://learn.microsoft.com/en-us/azure/key-vault/general/access-control-default), new vaults default to Azure RBAC unless configured otherwise. Updating an existing vault with that API does **not** automatically migrate its access model, and access policies remain supported. Audit create and update paths separately.

The [control-plane API migration notice](https://learn.microsoft.com/en-us/azure/key-vault/general/migrate-api-version) retires versions before 2026-02-01 on **February 27, 2027**. This concerns vault-management calls, templates and management SDKs; it does not retire stable data-plane secret/key/certificate APIs or delete vaults. Updating management clients and migrating access control are distinct work items. Inspect the actual requested API version, including automation that differs from the portal.

### Apply the enterprise access model to privilege

Microsoft's [privileged access guidance](https://learn.microsoft.com/en-us/security/zero-trust/security-concept-privileged-access) treats the control plane, management plane, and data/workload planes as distinct security levels. Prevent lower-trust identities, devices, or intermediaries from controlling higher-trust assets.

Design:

- separate daily and administrative identities;
- minimal standing privilege, PIM eligibility, approval/MFA/context, time limits, notifications, and audit;
- role design and delegation at the narrowest useful scope;
- entitlement management for access packages and lifecycle;
- recurring access reviews with accountable reviewers and removal/default behavior;
- hardened privileged access workstations and bounded remote administration;
- emergency access with independent strong credentials, monitoring, testing, and post-use rotation;
- tenant and multicloud administration plus CIEM signals for excessive entitlements.

PIM makes assignments time-bound; it does not correct an overbroad role or compromised privileged workstation. Access reviews provide decisions; they are weak if reviewers lack context or nonresponses preserve access indefinitely.

### Translate compliance into enforceable controls and evidence

Decompose each requirement into scope, protected asset/data, control intent, implementation, owner, frequency, evidence, exception, and residual risk. Then map:

- Microsoft Purview Compliance Manager improvement actions and evidence;
- Purview information protection, DLP, retention, records, audit, eDiscovery, insider-risk, or communication controls where applicable;
- Azure Policy definitions/initiatives, assignment scope, effects, exemptions, remediation, managed identity, and compliance state;
- Defender for Cloud regulatory standards and posture evidence across supported cloud environments.

[Compliance Manager's multicloud integration](https://learn.microsoft.com/en-us/purview/compliance-manager-cloud-settings) consumes supported Defender for Cloud standards/signals. Similar names do not make a framework, Azure Policy initiative, Defender standard, and Compliance Manager regulation interchangeable. Automated compliance is evidence of configured/tested controls, not a legal certification.

> **Related item:** Azure Policy controls resource configuration and deployment. Microsoft Entra Conditional Access controls token issuance/access context. Purview DLP controls sensitive-data use. Defender detections identify threats. Strong architecture composes these layers instead of asking one to do every job.

With [Azure Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources), evaluation alone does not repair existing noncompliant resources. `deployIfNotExists` and `modify` require a remediation task and an appropriately authorized assignment identity for that work. Portal assignment can grant the declared roles; SDK-driven deployment must explicitly grant them. Changing a definition does not automatically revise existing identity permissions. Test existing and newly created resources, failed remediation and exemptions separately.

Keep the exact standard/version/cloud mapping in the evidence record. A similarly named Compliance Manager regulation may not accept every Defender for Cloud standard or version; compare the published supported list instead of assuming automatic equivalence.

## 3. Design infrastructure security

### Separate posture management from workload protection

Cloud security posture management (CSPM) inventories assets, evaluates configuration and relationships, prioritizes exposure, and drives remediation. Cloud workload protection (CWPP) detects and responds to runtime threats for particular workloads. [Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) provides foundational posture capabilities and optional Defender CSPM/workload plans; select plans from workload, threat, cloud, coverage, dependency, cost, and operating requirements rather than enabling names mechanically.

For hybrid/multicloud architecture:

- establish tenant/subscription/account/project and management hierarchy;
- onboard AWS/GCP and non-Azure machines with the appropriate connector or Azure Arc path;
- assign least-privilege connector identities and protect onboarding credentials;
- define region/residency, extension, agent, network, policy, update, and lifecycle behavior;
- normalize asset ownership, criticality, tags, and exception governance;
- route high-value recommendations/incidents to accountable teams and verify remediation.

Secure Score is a prioritization and measurement input. It can change as assets, recommendations, weighting, and product logic change. Pair it with business criticality, exploitability, exposure, threat intelligence, compliance, cost, and operational feasibility.

### Account for current posture and entitlement changes

The [Defender for Cloud release notes](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) announce that **new Azure subscriptions require opt-in to Foundational CSPM from October 27, 2026**. It remains free; existing Azure configuration and AWS/GCP are unaffected. Add explicit onboarding verification to landing-zone acceptance criteria. Individual recommendations now replace legacy grouped findings, and automation should use the current identifiers/schema. The grouped vulnerability-assessment coverage recommendation is scheduled for retirement December 14, 2026.

Current [CIEM guidance](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-permissions-management) retains overprovisioned-identity recommendations, but since August 6 AWS/GCP findings no longer supply the detailed unused-action list. Obtain the required usage evidence from the provider's native tools before deciding to remove a permission. A missing field is not proof that no permission is unused.

**Worked example — changing the denominator:** An onboarding inventory has 90 verified resources out of 100. Adding 50 unverified acquired resources changes verified coverage from 90% to 60%, although the original 90 have not become less secure. Report the new population, verification gap and critical assets. This is a simple inventory-coverage metric, not the formula for Microsoft Secure Score or Cloud Score.

### Use exposure context to prioritize paths, not isolated findings

[Microsoft Security Exposure Management attack paths](https://learn.microsoft.com/en-us/security-exposure-management/work-attack-paths-overview) connect entry points, identities, misconfigurations, vulnerabilities, and critical assets. Security insights and initiatives translate those relationships into outcomes and tracked improvement. Validate whether a remediation actually breaks the path and whether compensating paths remain.

[Defender EASM integration](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-easm) gives outside-in discovery of internet-facing assets; CSPM gives inside-out configuration/relationship context. Reconcile EASM discoveries with authoritative inventory and ownership. Unknown assets are a governance problem before they are merely a scanner finding.

> **Related item:** Attack-surface reduction usually means changing exposure or behavior at an endpoint/workload. Attack-path management reasons across relationships. EASM finds externally observable assets. These are related but not synonyms.

### Specify server, client, mobile, IoT, and OT controls

For servers and clients, set platform-specific baselines for supported OS, secure boot/hardware trust, encryption, local firewall, endpoint detection/protection, application control, vulnerability/configuration management, patching, logging, identity, remote administration, and recovery. Manage drift and explicitly retire unsupported systems.

Windows LAPS manages unique, rotated local administrator passwords and can protect/recover them through supported directory controls. It reduces shared/static local credential risk; it does not replace tiered administration, PIM, endpoint protection, or removal of unnecessary local administrators.

Mobile design distinguishes device enrollment/management, application protection, app configuration, compliance, Conditional Access, selective wipe, and personally owned constraints. A compliant-device decision depends on trustworthy enrollment and current signals.

IoT/embedded and OT/ICS environments require asset discovery, safety/availability-aware risk assessment, segmentation, protocol and vendor constraints, passive monitoring where active methods are unsafe, secure remote/vendor access, change windows, incident coordination, and compensating controls. Defender for IoT contributes visibility/detection; operational safety and engineering ownership remain essential.

The [Defender for IoT retirement notice](https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/edge-security-module-deprecation) plans **micro-agent retirement on June 1, 2027**. This is the device-builder micro agent, not a blanket retirement of OT network sensors or every Defender for IoT capability. Inventory the actual deployed component, supported version and replacement evidence before writing an OT migration plan.

### Design baselines by service model and workload

The customer/provider responsibility boundary changes across SaaS, PaaS, and IaaS, but the customer still owns data, identities, access, configuration, and appropriate monitoring.

| Model | Customer emphasis | Typical architecture mistake |
|---|---|---|
| SaaS | Tenant configuration, identity/session controls, app governance, data protection, audit, provider risk | Assuming provider security secures tenant permissions and data use |
| PaaS | Identity, data, private/public network exposure, service configuration, keys, logging, dependency security | Treating managed runtime as no-configuration/no-monitoring |
| IaaS | All above plus OS, software, patching, host hardening, endpoint protection, backup | Recreating a flat on-premises network in cloud |

Web workload requirements include ingress/egress, TLS, WAF, DDoS, identity, secrets, API authorization, dependency and runtime protection. Container design includes trusted/minimal images, registry and provenance, scanning, nonroot/restricted execution, secrets, network policies, admission controls, workload identity, orchestrator control-plane protection, node security, and runtime detection.

AI workloads add model/data provenance, grounding permissions, prompt/tool boundaries, content safety, private/network architecture, identity, encryption, evaluation/red teaming, abuse monitoring, and incident response. Use [Azure AI platform security guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/platform/security) and the service-specific baseline. **VERIFY CURRENT:** model, service, protection-plan, and preview capabilities change quickly.

### Evaluate network design and Security Service Edge

Begin with flows and trust boundaries, not appliances. Document source/destination identity, protocol/port, direction, sensitivity, public/private exposure, inspection, name resolution, routing, availability, performance, logging, and owner. Segment by function, trust, environment, and impact; deny or tightly scope unnecessary east-west and egress paths. Protect administrative paths and avoid management exposure to the public internet.

[Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access) combines:

- **Microsoft Entra Internet Access:** identity-aware secure web gateway controls for internet/SaaS and Microsoft traffic, including supported cross-tenant Microsoft traffic scenarios;
- **Microsoft Entra Private Access:** identity-aware per-app/quick access to private resources as a Zero Trust Network Access pattern;
- Defender for Cloud Apps CASB/session controls as an adjacent SaaS control.

Evaluate traffic acquisition/forwarding, client versus remote network, DNS/routes, cross-tenant needs, Conditional Access signaling, TLS inspection constraints, private connectors, high availability, user/device scope, bypass paths, logs, licensing, and phased rollout. SSE complements workload network controls such as Azure Firewall, NSGs, private endpoints, WAF, DDoS protection, and service firewalls; it does not erase them.

> **Related item:** A private endpoint changes the service's network path. Managed identity changes how the caller authenticates. RBAC/data-plane authorization changes what it may do. Use all three when the threat model requires them.

Current [Global Secure Access limitations](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-current-known-limitations) constrain the design. A branch IPsec tunnel can forward Microsoft/Internet traffic, but clientless forwarding does not itself enforce user Conditional Access for those profiles. Private Access requires the supported client and application-level policy targeting; compliant-network checking is not currently supported for Private Access apps. Verify acquisition, DNS, platform and bypass behavior instead of inferring enforcement from a connected tunnel.

[Universal tenant restrictions](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-universal-tenant-restrictions) uses TRv2 configuration plus the Microsoft traffic profile and client/remote-network acquisition. It restricts access using external tenant identities under its documented conditions; it is not a substitute for governing guests accessing resources in the resource tenant. Test home-tenant access, allowed partner identity, disallowed external identity and an existing guest separately.

## 4. Design application, Microsoft 365, and data security

### Evaluate Microsoft 365 as an integrated control plane

Use posture metrics to identify gaps and trends, then verify recommendations against business risk, license, deployment state, user impact, and compensating controls. Microsoft Secure Score spans Microsoft 365 security recommendations; Defender for Cloud has cloud posture scoring. Know which score, asset population, and control owner a scenario means.

Compose:

- Defender for Office 365 for email/collaboration threats, protection policies, investigation, response, attack simulation, and campaign context;
- Defender for Cloud Apps for discovery, SaaS posture, app governance, information protection, anomaly detection, and supported Conditional Access App Control;
- Intune for device/app configuration, compliance, endpoint security, enrollment, and app protection;
- Entra for identity, authentication, Conditional Access, governance, workload/agent identity;
- Purview for classification, labels, DLP, retention, audit, eDiscovery, insider risk, and compliance workflows;
- Defender XDR/Sentinel for correlated detection, investigation, response, and wider estate coverage.

Microsoft 365 Copilot uses existing permissions; it can therefore surface overshared content the user was already allowed to access. The [Copilot data-protection architecture](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture-data-protection-auditing) explains permission, sensitivity-label/encryption, SharePoint/OneDrive, audit, eDiscovery, and retention interactions. Secure rollout requires permission/oversharing remediation, identity/device controls, Purview protection, app/agent governance, audit, monitoring, adoption policy, and incident response—not a separate trust boundary around the model alone.

[Purview DLP for Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) has distinct actions. Blocking web search can still permit an internally grounded response; blocking a sensitive prompt prevents the response. Label-based exclusion can leave an item in citations while preventing content use. External-email exclusion is preview and evaluates sender-domain metadata, not email-body trustworthiness. Directly uploaded prompt-file contents are not scanned by this DLP location. Design separate test cases and source permissions; do not claim these controls prevent every prompt injection or every data route. Policies can take up to four hours to appear, and preview availability must be checked in the tenant.

### Secure the full application portfolio and lifecycle

Inventory applications, APIs, owners, business criticality, data, identities, internet exposure, dependencies, technology/support status, deployment path, telemetry, and recovery. Prioritize unsupported/high-impact/internet-facing and overprivileged applications.

Threat modeling identifies assets, entry points, trust boundaries, data flows, threats/abuse cases, mitigations, assumptions, residual risk, owners, and validation. Update it for architecture, identity, data-flow, dependency, or threat changes.

Lifecycle controls span requirements, design review, repository and branch policy, code/dependency/secret/IaC/image scanning, build provenance, artifact protection, environment separation, deployment identity, security testing, release approval, runtime protection, vulnerability response, rollback, and retirement.

For workload identities, prefer managed identities/federated credentials, select system-assigned versus user-assigned based on lifecycle/sharing requirements, grant minimal resource/data-plane permissions, constrain federated subjects, and monitor use. Never infer authorization solely from possession of a valid token.

### Design API and web application protection

API Management can provide a managed gateway, authentication/authorization policies, transformation, quotas/rate limiting, versioning, developer exposure, observability, network isolation, and backend abstraction. It does not replace API business authorization, secure code, input validation, backend identity, or data protection.

Use Azure WAF with Application Gateway for regional/private application delivery or Front Door for global edge delivery, based on topology, latency, origin, and availability needs. Choose policy scope, managed/custom rules, exclusions, bot/rate controls where supported, detection-before-prevention rollout, tuning, logs, and incident integration. Protect origins from bypass when the design requires gateway-only access.

> **Related item:** WAF filters supported web attacks at an HTTP boundary; DDoS protection addresses volumetric/protocol availability attacks; API authorization protects operations and objects; code fixes remove the vulnerability. One does not substitute for the others.

### Design data security from classification to recovery

Build a data inventory with owner, classification, residency, retention, permitted use, lineage, access paths, encryption/key requirements, backup, sharing, AI use, monitoring, and deletion. Discovery and classification inform controls; they do not themselves restrict access.

Prioritize threats such as public exposure, excessive privilege, shared keys, weak authentication, injection, unencrypted paths, unmanaged exports/copies, destructive changes, backup compromise, oversharing, insecure analytics, and AI grounding leakage.

Encryption architecture distinguishes:

- at rest versus in transit versus in use;
- service-managed versus customer-managed keys;
- envelope encryption and key hierarchy;
- software-protected versus managed HSM custody;
- access separation, rotation, revocation, backup/recovery, and availability;
- application/column/client-side encryption when platform encryption does not satisfy the threat model.

Customer-managed keys increase control but also create availability and operational dependencies. Document what happens when a key expires, is disabled, deleted, inaccessible, or cannot be recovered.

For Azure SQL, Synapse, Cosmos DB, and Storage, choose Entra authentication where supported, least-privilege data access, private/public network controls, firewall behavior, encryption/key ownership, auditing/diagnostics, classification, backup/recovery, replication/residency, and service-specific threat protection. Defender for Databases and Defender for Storage add detections/recommendations for supported services; they do not replace secure configuration or authorization.

AI data security must cover training, evaluation, grounding, vector/embedding stores, prompts, tool results, outputs, caches, logs, and human feedback. Preserve source ACLs where required, prevent cross-tenant/user retrieval, filter before generation, minimize telemetry, evaluate extraction/injection attacks, and establish retention/deletion and incident evidence.

### Protect the operation and the data version

An [Azure management lock](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources) constrains control-plane operations, not every data-plane write or delete. Storage keys also create a different authorization path from Entra user/RBAC access. Before [disallowing Shared Key](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent), inventory dependent clients and SAS types: account/service SAS depend on the key, while Blob user-delegation SAS uses Entra authorization. Validate application and Azure Files compatibility before rollout.

[Defender for Storage malware scanning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/introduction-malware-scanning) reports clean, malicious, error and not-scanned outcomes. Treat missing/error/unsupported/timeout results as unresolved, not clean. Blob index tags are mutable by authorized writers and cannot be the sole security gate. Use protected event/log evidence and isolate unapproved content; bind the decision to the object version or ETag so an overwrite cannot inherit an old clean result. On-upload scanning does not cover Azure Files, append/page blobs, client-encrypted blobs or NFS 3.0 uploads; on-demand coverage differs.

**Worked example — fail-closed release:** Of 100 uploads, 82 are clean, three malicious, five errors and ten unscanned. Only the 82 with validated results for the current content version qualify for release; 18 remain held for investigation/retry. If a clean ETag `v42` is overwritten by `v43`, the old result cannot approve `v43`. A later duplicate event for `v42` must not undo that hold. This is an application design exercise, not a claim that Defender automatically implements the complete release gate.

## 5. Apply an architect's decision method

### Use requirement-to-control traceability

For every material decision, record:

| Field | Question |
|---|---|
| Requirement | Which mission, threat, legal, data, resilience, or operating need exists? |
| Scope | Which identities, assets, clouds, tenants, subscriptions, networks, apps, and data are included/excluded? |
| Decision | Which control and architecture pattern is selected, and why? |
| Alternatives/tradeoffs | What was rejected; what cost, complexity, performance, usability, availability, or lock-in changes? |
| Ownership | Who approves, implements, operates, monitors, reviews, and accepts residual risk? |
| Evidence | Which policy state, configuration, log, test, score, incident, or recovery result proves operation? |
| Failure/recovery | What can fail, how is it detected/contained, and how does service/security recover? |
| Lifecycle | How is the control versioned, deployed, exempted, reviewed, and retired? |

### Recognize common distractor patterns

- A product is relevant but operates at the wrong control layer.
- A detection product is offered where prevention or recovery is required.
- A posture score is treated as a vulnerability, compliance certificate, or business-risk ranking.
- PIM is treated as role minimization; Conditional Access as API authorization; private networking as identity.
- A single-cloud answer is offered for an explicit hybrid/multicloud requirement.
- A control meets the technical requirement but lacks required evidence, residency, separation, or recovery.
- The design optimizes one workload while breaking enterprise governance or the control plane.

> **Related item:** The best exam answer usually satisfies every stated constraint with the fewest unsupported assumptions. In real architecture, document the assumptions and validate them with stakeholders.

## 6. Integrated architecture scenarios

### Scenario 1: Ransomware-resilient hybrid manufacturer

**Context:** A manufacturer has Entra ID, AD DS, Azure, on-premises plants, Linux/Windows servers, OT networks, remote vendors, and a small SOC. A ransomware event compromised a help-desk account and deleted reachable backups.

**Design:** Identify production, safety, identity, and recovery systems as critical. Separate control-plane administration with distinct identities, PIM, phishing-resistant authentication, PAWs, protected emergency access, and hardened AD DS. Use Intune/Defender for Endpoint for supported endpoints, Defender for IoT with safety-aware monitoring for OT, segmentation between enterprise/plant/control zones, and per-app remote access instead of broad VPN where feasible. Onboard hybrid servers through Azure Arc with governed extensions/policy and the selected Defender plans. Isolate/immutably protect backup paths, separate deletion authority, define clean-room identity/platform recovery, and exercise RTO/RPO.

Unify relevant Defender XDR and Sentinel incidents; ingest identity, endpoint, network, Arc/cloud, OT, backup, and privileged activity according to detection use cases. Map/test coverage against Enterprise and ICS ATT&CK, automate low-risk enrichment and account/device containment with appropriate approvals, and feed incident lessons into Exposure Management initiatives, patch SLAs, policy, and MCRA target state.

**Evidence:** privileged-role activation/access reviews, PAW compliance, restore exercise results, path-remediation proof, connector/detection tests, incident metrics, policy compliance, exceptions, and plant-owner signoff.

### Scenario 2: Regulated Microsoft 365 Copilot and AI rollout

**Context:** A financial firm wants Microsoft 365 Copilot and a customer-facing Azure AI application. Data is overshared, developers use static secrets, and regulators require retention, audit, residency, least privilege, and demonstrable control effectiveness.

**Design:** Inventory/classify data and owners; remediate SharePoint/OneDrive permissions and external sharing; apply Entra authentication/Conditional Access, device/app controls, Purview sensitivity labels, DLP, retention, audit/eDiscovery, and relevant insider-risk workflows. Govern Copilot apps/agents and monitor Defender/Purview/Entra signals. Record that Copilot honors existing access—so permission cleanup is a security prerequisite.

For the Azure AI application, threat-model prompt, grounding, vector store, agent/tool, API, model, and output boundaries. Use workload/agent identities and bounded delegated/autonomous flows, private service access where justified, Key Vault for unavoidable secrets, APIM for gateway controls, WAF for supported web threats, least-privilege data authorization, content-safety/evaluation/red-team gates, and end-to-end audit with sensitive telemetry minimized. Apply landing-zone policy and service/MCSB baselines; use WAF/CAF reviews and secure pipelines.

**Evidence:** data-owner access attestations, label/DLP tests, Copilot audit/retention search, agent identity inventory/CA results, threat-model mitigation tests, prompt-injection/tool-abuse evaluations, key-failure runbook, deployment provenance, and compliance control mappings.

### Scenario 3: Multicloud acquisition and unified security operations

**Context:** An enterprise acquires AWS and GCP estates plus another Entra tenant. Asset ownership is inconsistent, alerts are duplicated, admins use broad standing rights, and executives want one score.

**Design:** Establish management/tenant/cloud-account boundaries, ownership and criticality. Connect supported environments to Defender for Cloud with least-privilege identities and deliberate region/data handling; use Azure Arc only where its control/management benefits are required. Reconcile EASM outside-in discoveries with CSPM inventory and Exposure Management paths. Select Defender workload plans by resource/threat/coverage needs.

Define XDR/Sentinel responsibilities, source-of-truth incidents, log tiers/retention, routing, and coverage tests; do not simply duplicate every cloud log. Apply enterprise access levels, separate identities, PIM/access packages/reviews, PAWs, emergency access, and CIEM/exposure signals across clouds. Translate common regulatory intent into MCSB/cloud-native controls, Azure Policy where applicable, and evidence mappings while preserving platform-specific implementation.

**Evidence:** coverage and owner matrix, connector permissions/health, unknown-asset closure, tested attack-path breaks, normalized detection/use-case map, privilege reduction, access-review outcomes, and executive risk views that explain rather than collapse unlike scores.

## 7. Hands-on labs

Use a disposable tenant/subscription and synthetic data. Some Microsoft 365, Defender, Purview, Entra, and multicloud features require paid licenses or provider-managed lab environments; use a tabletop design when safe hands-on access is unavailable. The public [MicrosoftLearning SC-100 lab repository](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect) is designed for a preconfigured training tenant/subscription and may not run unchanged in a personal environment.

### Lab 1 — Strategy and ransomware architecture

1. Choose a three-tier business service and inventory identities, data, dependencies, admin paths, and backups.
2. Set impact, RTO/RPO, top five threats, risk owners, and recovery order.
3. Map current/target capabilities to MCRA and controls to MCSB/Zero Trust.
4. Draw separate production and recovery administration boundaries.
5. Tabletop credential theft, backup deletion, containment, clean recovery, and lessons.

**Evidence:** architecture, risk/control map, recovery dependency graph, restore test plan, and gaps with owners/dates.

### Lab 2 — Landing-zone and secure-delivery decision record

1. Create platform/application landing-zone responsibility and policy matrices.
2. Evaluate a workload against WAF security recommendations and its threat model.
3. Define DevSecOps gates for source, dependencies, IaC, images, secrets, artifacts, deployment identity, and runtime.
4. Add an AI use case and document data/model/tool/agent controls.
5. Record tradeoffs, exceptions, and evidence.

**Evidence:** decision record, policies, pipeline gate design, threat model, and exception workflow.

### Lab 3 — Detection and response validation

1. Define six detections across identity, endpoint, cloud control plane, data, network, and backup/OT.
2. Map each to ATT&CK, required fields, XDR/SIEM owner, severity, and response.
3. Design a bounded SOAR playbook with approval, retry, idempotency, and audit.
4. Generate or tabletop benign test events and trace signal to closure.
5. Record gaps and tune the use case.

**Evidence:** use-case matrix, query/analytic logic, playbook flow, test timestamps, incident record, and tuning decision.

### Lab 4 — Logging architecture and cost boundary

1. Inventory ten log sources and define security/audit use cases.
2. Choose collection, transformation, workspace/data-lake/archive, retention, residency, and access.
3. Identify duplicates and authoritative records.
4. Model daily volume and a cost spike; add budgets/alerts and a graceful degradation plan.
5. Test time sync, parsing, identity/resource context, and evidence export.

**Evidence:** data-flow diagram, tier/retention table, cost model, schema tests, and evidence chain.

### Lab 5 — Human, workload, agent, and privileged identity

1. Model a human admin, guest, managed identity, autonomous agent, and delegated agent.
2. Define token subject/audience, permissions, CA applicability, resource authorization, owner, and lifecycle.
3. Design PIM, entitlement, access-review, PAW, and emergency-access controls.
4. Test/report-only a Conditional Access policy without locking out the tenant.
5. Tabletop credential or agent compromise and offboarding.

**Evidence:** identity/permission matrix, token-flow diagrams, policy result, review decision, and recovery steps.

### Lab 6 — Compliance, policy, posture, and exposure

1. Translate five regulatory statements into control/evidence records.
2. Map each to Purview, Azure Policy, Defender for Cloud, manual procedure, or another cloud's native control.
3. Compare Secure Score/recommendations with asset criticality and attack paths.
4. Investigate one outside-in/unknown-asset scenario.
5. Verify remediation breaks a path and preserve evidence.

**Evidence:** traceability matrix, policy/initiative and exemption design, prioritization rationale, path before/after, and owner attestation.

### Lab 7 — Network, API, and application boundary

1. Draw a global web/API workload with users, admins, workloads, data, and dependencies.
2. Place Internet/Private Access, Front Door/Application Gateway WAF, firewall/NSG/private endpoints, APIM, identity, and resource authorization deliberately.
3. Threat-model bypass, injection, token misuse, egress, origin exposure, and component failure.
4. Define WAF detection-to-prevention tuning and API rate/auth controls.
5. Test or tabletop failover, false positive, and identity/network outage.

**Evidence:** flow/trust diagram, rule/policy plan, threat mitigations, test cases, and recovery decisions.

### Lab 8 — Microsoft 365, Copilot, and data protection

1. Create synthetic public/internal/confidential/highly confidential data and an overshared site scenario.
2. Design or test labels, DLP, retention, audit, device/app, external-sharing, and Copilot controls.
3. Model Azure SQL, Cosmos DB, and Storage access, network, encryption/key, Defender, audit, and recovery choices.
4. Test a user, guest, workload, and Copilot/AI retrieval against intended access.
5. Tabletop key loss, oversharing, malicious prompt, and destructive data action.

**Evidence:** classification/control matrix, access results, audit search, key/recovery plan, and incident findings.

### Lab 9 — Migration acceptance and recovery evidence

1. Draw production/recovery identities and the Resource Guard boundary; inspect operation scope and inherited permissions on paper or in a disposable environment.
2. Reproduce the RTO/RPO example and identify which dependency must change.
3. Inventory Sentinel connectors, workspace roles, CMK surfaces, incident conditions and latency assumptions before a proposed migration.
4. Test or tabletop a merged incident and batched updates; identify which workflow needs authoritative event history.
5. Inventory Key Vault management API versions separately from data-plane clients and access models.

**Evidence:** dated support matrix, permission scope, acceptance tests, recovery times, missing signals and owners. Do not lock a real vault irreversibly for this exercise.

### Lab 10 — Agent and upload authorization boundaries

1. Model the three agent requests above and explain which policy targets each subject.
2. Compare a managed endpoint agent user with a cloud agent that cannot supply device signals.
3. Trace the 100-upload result set and a later overwrite; retain unresolved files without treating tag text as trusted proof.
4. Test Copilot web-search blocking, prompt blocking and source exclusion separately with synthetic content, recording unavailable previews.
5. Revisit a compromised-service-principal tabletop: credential rotation, historical-use investigation, effective-role review and independent recovery protection.

**Evidence:** subject/audience/policy matrix, resource authorization, version-bound scan decisions and documented gaps. This review ran only offline arithmetic/set checks; no Azure/Microsoft 365 tenant, destructive action, agent, scanner or incident-response lab was executed.


## 8. Knowledge checks

These are original study questions, not recalled exam content.

1. **Why begin with business-critical assets instead of the product catalog?** Controls and recovery must be prioritized by mission impact and plausible threats; products only implement parts of that strategy.
2. **What is the difference between RTO and RPO?** RTO limits acceptable restoration time; RPO limits acceptable data loss measured in time.
3. **Why is successful backup insufficient ransomware evidence?** It does not prove isolation, clean restore, identity/platform dependency recovery, or achievement of RTO/RPO.
4. **What is MCRA's main architecture role?** It provides an end-to-end capability/integration reference for comparing current and target security across the hybrid estate.
5. **What does MCSB add?** Control guidance and mappings for building/evaluating cloud security baselines; it does not replace workload risk assessment.
6. **How do CAF and WAF differ?** CAF guides organization-wide cloud adoption/operating practices; WAF reviews workload design and tradeoffs.
7. **What does an application landing zone inherit?** Platform governance/security standards and shared capabilities, while retaining workload-specific controls and ownership.
8. **Name three AI-specific control surfaces.** Grounding data/permissions, agent/tool identity and authorization, and prompt/output evaluation/monitoring (among others).
9. **Why protect build identity and artifacts?** A trusted source scan can still be defeated by a compromised runner, deployment credential, registry, or substituted artifact.
10. **How do XDR and SIEM differ?** XDR correlates/responds across integrated security domains; SIEM provides broader log ingestion, analytics, hunting, retention, and multivendor/multicloud operations.
11. **What proves detection coverage better than a connector status?** A safe end-to-end technique test from signal generation through incident, response, evidence, and closure.
12. **Why map ATT&CK coverage with test results?** A mapping shows intent; tests show whether telemetry and analytics actually detect the technique in this environment.
13. **When should SOAR require human approval?** When an action is disruptive, irreversible, high-impact, ambiguous, or legally/business sensitive.
14. **Why is a valid token not sufficient authorization?** The resource must validate token properties and enforce scopes/roles plus object/business rules.
15. **Why use report-only Conditional Access first?** It exposes dependency, scope, and lockout risk before enforcement, enabling controlled pilot and tuning.
16. **Why do API keys matter for agent Conditional Access?** They bypass Entra token issuance, so Entra Conditional Access cannot evaluate that access.
17. **What does PIM not fix?** An overbroad role, excessive eligible population, compromised device, or weak resource authorization.
18. **Why are PAWs architectural controls?** Device trust bounds privileged sessions; a compromised daily-use device can undermine otherwise strong admin identity controls.
19. **What makes an access review meaningful?** Correct scope, decision context, accountable reviewer, explicit default/removal behavior, evidence, and follow-through.
20. **What is compliance translation?** Turning legal/contractual intent into scoped technical/procedural controls, ownership, frequency, evidence, exceptions, and residual risk.
21. **Why is Azure Policy not the same as Conditional Access?** Policy evaluates/governs Azure resource state; Conditional Access evaluates context during Entra token issuance.
22. **How do CSPM and CWPP differ?** CSPM manages configuration/exposure posture; CWPP protects running workloads with workload-specific threat detection/response.
23. **Why not rank only by Secure Score points?** Score weighting cannot fully represent business criticality, exploitability, active exposure, compensating controls, or remediation cost.
24. **How do EASM and attack paths complement each other?** EASM discovers outside-in exposed assets; attack paths connect exposure and relationships to potential critical impact.
25. **What is Azure Arc's security-design value?** It projects supported non-Azure resources into Azure management/governance and extension patterns; it also adds identity, agent, network, and lifecycle responsibilities.
26. **Why treat OT differently from ordinary endpoints?** Safety, availability, legacy protocols, vendor constraints, and change windows can make active scanning or immediate patching unsafe.
27. **What remains the customer's responsibility in SaaS?** Identities, access, tenant configuration, data governance, audit/monitoring, and appropriate provider-risk decisions.
28. **How do Entra Internet Access and Private Access differ?** Internet Access is an identity-aware secure web gateway for internet/SaaS/Microsoft traffic; Private Access is per-app/quick-access ZTNA for private resources.
29. **Why can a private endpoint not replace identity?** It constrains network reachability but does not authenticate the caller or authorize data/actions.
30. **What is the key Copilot oversharing risk?** Copilot can find/synthesize content users already have permission to access, exposing weak existing permissions more efficiently.
31. **When should threat models change?** When assets, trust boundaries, identity, data flows, dependencies, architecture, or threats change—and after relevant incidents.
32. **What does APIM not replace?** Backend/app business authorization, secure code, input validation, data protection, and workload identity.
33. **Why deploy WAF in detection mode before prevention?** To learn legitimate traffic, tune exclusions/rules, and reduce production false-positive impact before blocking.
34. **What tradeoff accompanies customer-managed keys?** More custody/control creates key availability, permission, rotation, recovery, and operational failure dependencies.
35. **Why classify data before selecting controls?** Sensitivity, ownership, permitted use, residency, and lifecycle determine proportionate access, encryption, DLP, monitoring, and recovery.
36. **What completes an architecture decision?** Requirement, scope, choice, alternatives/tradeoffs, ownership, operating evidence, failure/recovery, and lifecycle—not a diagram alone.

37. **Does “All users” Conditional Access protect agent user accounts?** No. Current guidance requires explicit agent-user targeting; identity and blueprint targeting also do not include agent users.
38. **Does updating the Key Vault management API migrate an existing vault to RBAC?** No. New-vault defaults and existing-vault access-model changes are separate; the February 2027 retirement concerns older management APIs.
39. **Does a retained backup remain immutable for its entire retention?** Not necessarily. Time-based immutability can expire earlier; identify the vault type, configured duration, lock state and recovery requirement.
40. **Can a Sentinel incident-update trigger prove every intermediate state change?** No. Batched delivery can contain only the latest update; use an appropriate evidence source and account for latency.
41. **Does new-subscription Foundational CSPM remain automatic after October 27, 2026?** The announced change requires opt-in for new Azure subscriptions; existing Azure and AWS/GCP behavior is outside that change.
42. **Does missing CIEM unused-action detail mean all permissions are needed?** No. AWS/GCP detail was removed; consult provider-native usage evidence and business requirements.
43. **Can a clean malware tag approve a later overwritten blob?** No. Tags are mutable, and the result must match the content version; hold errors, unscanned and changed content pending validation.
44. **Does removing a leaked secret from a public issue revoke it?** No. Revoke/rotate the credential and investigate use and downstream credentials; copies and issue history can remain.



## Places to learn

This is a curated starting point, not a complete list. Do **not** try to consume every resource. Pick a primary path that fits how you learn, use documentation and labs for weak areas, and use assessments to decide what to revisit. Verify every course against the July 28, 2026 blueprint—especially AI security, Entra Agent ID, Exposure Management, Copilot, and current SSE objectives.

### Time-planning summary

| Resource | Access | Estimated time |
|---|---|---:|
| Official blueprint, exam page, credential/prerequisite review | Free | 45–75 minutes |
| Four official Microsoft Learn paths | Free | 19 modules across four paths; earlier 20h58 duration is historical; allow 26–35 hours with notes and exercises |
| SC-100T00-A instructor-led course | Provider/schedule dependent | 4 days |
| Microsoft Learn free Practice Assessment | Free; launch from exam page | 45–75 minutes per attempt plus 1–3 hours reviewing sources |
| MicrosoftLearning public lab repository | Free; many labs expect a prepared tenant | 8–16 hours selected labs; full use varies by lab access |
| Microsoft Exam Readiness Zone SC-100 series | Free | 1–2 hours suggested review allocation; episode-one chapter list checked, total video runtime not verified |
| John Savill SC-100 Study Cram | Free | Earlier 1h38/2022 metadata is historical; current retrieval returned a shell, not a verified video |
| Pluralsight SC-100 path by Tim Warner | Paid/trial | 4h58 summed course durations (path rounds to five hours), plus labs/review |
| O'Reilly Exam Ref SC-100 book | Paid/trial | Earlier 10h37/February 2023 metadata; current retrieval blocked |
| O'Reilly/Packt SC-100 Exam Prep video | Paid/trial | Earlier 13h03/April 2023 metadata; current retrieval blocked |
| Udemy SC-100 by Alan Rodrigues | Paid | Earlier 11h38/March 2026 metadata; current retrieval blocked |
| Whizlabs-delivered Coursera SC-100 specialization | Paid/trial options vary | Five months at four hours/week is a provider pacing estimate, not measured lesson runtime |
| MeasureUp SC-100 practice test | Paid; demo available | About 6–10 hours for diagnostic, targeted practice, timed retest, and source review |
| Partner Skilling Hub SC-100 offering | Microsoft partner login required | Schedule-dependent; allow about 4–5 days for a certification-week format, verify event listing |

### Official Microsoft resources

- [SC-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) — authoritative objectives and change log.
- [SC-100 exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-100/) — language, retirement, scheduling, prep videos, and free Practice Assessment entry point.
- [Cybersecurity Architect Expert credential](https://learn.microsoft.com/en-us/credentials/certifications/cybersecurity-architect-expert/) — prerequisite credentials and renewal.
- [SC-100T00-A Microsoft Cybersecurity Architect](https://learn.microsoft.com/en-us/training/courses/sc-100t00) — four instructor-led days.
- [Security best practices and priorities](https://learn.microsoft.com/en-us/training/paths/sc-100-design-solutions-best-practices-priorities/) — four modules; September 1 duration of 4h33 is historical.
- [Security operations, identity, and compliance](https://learn.microsoft.com/en-us/training/paths/sc-100-design-operations-identity-compliance-capabilities/) — six modules; earlier 6h24 duration is historical.
- [Infrastructure security](https://learn.microsoft.com/en-us/training/paths/sc-100-design-security-solutions-infrastructure/) — five modules; earlier 5h42 duration is historical.
- [Application and data security](https://learn.microsoft.com/en-us/training/paths/sc-100-design-security-solutions-applications-data/) — four modules; earlier 4h19 duration is historical.
- [MicrosoftLearning SC-100 labs](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect) — public lab instructions; read its tenant/subscription prerequisites.
- [Exam Readiness Zone: part 1](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-sc-100-design-solutions-that-align-with-security-best-practices-and-priorities) — use the linked four-part series for concise orientation, then reconcile its 2025 weights/topics with the current blueprint.

### Video, books, and structured courses

- [John Savill SC-100 Study Cram](https://www.youtube.com/watch?v=2Qu5gQjNQh4) — previously cataloged 2022 architecture review; current page returned a shell, so runtime/content were not reverified. It predates the July 2026 blueprint; supplement rather than use as a complete course.
- [Pluralsight Microsoft Cybersecurity Architect (SC-100)](https://www.pluralsight.com/paths/microsoft-cybersecurity-architect-sc-100) — four Tim Warner courses totaling 4h58, rounded to five path hours, plus a practice exam. The courses date from December 2024–January 2025, so build a current-objective gap list.
- [O'Reilly Exam Ref SC-100](https://www.oreilly.com/library/view/exam-ref-sc-100/9780137997299/) by Yuri Diogenes, Sarah Young, Mark Simos, and Gladys Rodriguez — earlier catalog observation: 352 pages/10h37, February 2023. Current access was blocked; contents and current availability were not verified.
- [O'Reilly Microsoft Cybersecurity Architect — SC-100 Exam Prep](https://www.oreilly.com/videos/microsoft-cybersecurity-architect/9781805128816/) with Anand Rao Nednur — earlier catalog observation: 13h03, April 2023. Current access was blocked; compare current availability and scope before purchase.
- [Udemy SC-100 by Alan Rodrigues](https://www.udemy.com/course/azure200/) — earlier listing showed 11h38 and a March 2026 update; current access was blocked. Verify live metadata and July/October coverage before purchase.
- [Whizlabs SC-100 specialization on Coursera](https://www.coursera.org/specializations/exam-prep-sc100-microsoft-certified-cyber-security-architect-expert) — four course estimates of 9, 12, 12 and 6 hours total 39 hours. Its separate five-month/four-hours-weekly pacing estimate measures something different; neither figure verifies actual video runtime or July/October coverage. Sample the syllabus before committing.

### Assessment and partner resources

- Use the free Microsoft Practice Assessment from the [SC-100 exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-100/) as a diagnostic, not a question bank. Research each weak answer in the current documentation.
- [MeasureUp SC-100 practice test](https://www.measureup.com/microsoft-practice-test-sc-100-cybersecurity-architect-grc.html) — current public listing: **148 questions, last updated November 2025**, despite generic copy saying approximately 150. July/October 2026 completeness is unproven; no paid questions were reviewed. Use original practice legally and resolve conflicts against Microsoft sources.
- [Microsoft Partner Skilling Hub security playbook](https://media.skilling-hub.com/main/pdf/e95c2a9e-6e1c-4cb4-94a6-15a1c70ba1eb/fy26-partner-skilling-playbook.pdf) lists Cyber Security Architect (SC-100) among prioritized security credential offerings. Partner sign-in is required for underlying event content; dates and duration are schedule-specific.

### Useful blog reading with an architecture task

- **Rob Lefferts, September 23, 2026 — [ISOC in Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/).** The article announces a preview. Draw the signal → context → decision → action → feedback chain for one benign incident, assigning a human owner and permission boundary to each step. Compare it with your existing XDR/SIEM design. It does not establish tenant availability, an exam rename or measured autonomous-response performance. Allow 30–45 minutes for reading and the diagram.
- **Microsoft Security Research, Yossi Weizman and Tushar Mudi, September 25, 2026 — [Storm-3168 investigation](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/).** Tabletop workload-credential exposure, effective-role review, rotation, use investigation and protected recovery. Microsoft describes resource destruction and key collection, but does not confirm that the publicly exposed secret was the entry point or that exfiltration/ransom occurred. Do not turn the case into destructive reproduction commands. These compromised service principals are not automatically Entra Agent ID objects. Allow 45–60 minutes for a control/evidence map.

Public article text was reviewed; videos, gated intelligence, product previews and customer outcomes were not tested. Learn-path landing pages list 19 modules, but individual modules were not completed or timed. The lab README was read, not all lab instructions; no paid course or signed-in Practice Assessment was completed. Partner PDF retrieval succeeded, but its raw response did not provide reliable parsed event metadata, so current event availability remains unverified.

The [deep-review record](../docs/research/2026-09-27-sc-100-deep-review.md) retains source observations, October objective mapping, follow-up dates and execution limits. Human review remains pending.



Avoid sites selling “real questions,” dumps, guarantees based on recalled exam content, or unauthorized copies. Use original practice questions, official assessment, labs, and documentation to build transferable architecture judgment.
