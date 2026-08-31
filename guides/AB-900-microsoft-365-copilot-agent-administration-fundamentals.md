---
exam_code: AB-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AB-900 Microsoft 365 Copilot and Agent Administration Fundamentals Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official AB-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900) is authoritative.

**Current baseline:** Skills measured as of July 22, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [AB-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900)

## How to use this guide

AB-900 connects ordinary Microsoft 365 administration with data governance and the new Copilot/agent control plane. For every scenario, trace the user or agent identity, license, data permission, policy, action, evidence, and administrator. “Copilot respects permissions” is a starting principle, not a substitute for fixing oversharing.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Describe core Microsoft 365 services and concepts | 30–35% | How are users, collaboration services, identity, and security administered? |
| Describe data protection and governance in Microsoft 365 | 35–40% | How is organizational data discovered, protected, retained, and investigated—especially for AI? |
| Describe basic Microsoft 365 Copilot and agent administration tasks | 25–30% | How are Copilot and agents licensed, controlled, deployed, monitored, and governed? |

---

# 1. Microsoft 365 administration foundations

## Tenant, subscriptions, users, and groups

A Microsoft 365 tenant is the organization's cloud service boundary associated with Microsoft Entra ID. Subscriptions provide service entitlements. Licenses assigned directly or through groups enable eligible service plans for users. A custom domain must be verified before it can be used for sign-in and email addresses.

| Object | Administration purpose |
|---|---|
| User | Human identity and service entitlement |
| Security group | Access and policy assignment |
| Microsoft 365 group | Membership and shared collaboration resources |
| Distribution group | Email distribution rather than general authorization |
| Shared mailbox | Mailbox used by several authorized users without ordinary personal sign-in |
| Dynamic group | Rule-based membership under applicable licensing |

Deleting or disabling a user, removing a license, blocking sign-in, revoking sessions, transferring data, preserving a mailbox, and retaining content are separate lifecycle actions. Design a leaver process rather than assuming one switch does everything.

The Microsoft 365 admin center provides broad tenant and service administration. Specialized admin centers expose deeper controls for Exchange, SharePoint, Teams, Microsoft Entra, Microsoft Defender, Microsoft Purview, Power Platform, and other workloads.

## Exchange Online, SharePoint, and Teams

Exchange Online manages mailboxes, mail flow, recipients, and related policies. Distribution groups distribute email; Microsoft 365 groups also underpin shared resources such as a group mailbox/calendar and can connect collaboration experiences.

SharePoint organizes content into sites, libraries, folders, files, lists, and pages. Permissions inherit by default but can be broken. Sharing links may grant access to specific people, people in the organization, existing access holders, or—in configured environments—anyone. Oversharing often comes from broad links, old group membership, broken inheritance, or content placed in an overly broad site.

Teams organizes collaboration into teams and channels. Standard channels are broadly available to team members; private and shared channels have distinct membership and site behavior. Teams policies control capabilities such as meetings, messaging, apps, and agents under the current service model. **VERIFY CURRENT:** policy names and admin surfaces.

> **Related item:** Collaboration membership and content permission are related but not always identical. Private/shared channels and linked SharePoint sites can create access boundaries that must be reviewed at the actual resource, not inferred only from the Teams UI.

---

# 2. Identity and access for Microsoft 365

## Zero Trust and authorization

Zero Trust applies verify explicitly, least privilege, and assume breach. Authentication proves identity; authorization grants an action. Microsoft Entra ID supplies identities, sign-in, applications, authentication methods, Conditional Access, and governance. Microsoft 365 workload roles authorize service administration.

| Control | Purpose |
|---|---|
| MFA/authentication strength | Require stronger sign-in evidence |
| Single sign-on | Reuse trusted authentication across applications |
| Conditional Access | Apply access decisions from identity, device, risk, location, app, and other signals |
| Microsoft Entra roles | Delegate directory/identity administration |
| Microsoft 365 workload roles | Delegate Exchange, SharePoint, Teams, security, compliance, and related administration |
| Privileged Identity Management | Make privileged access eligible/time-bound with activation controls |

Use least-privileged roles and separate everyday accounts from highly privileged administration. Preserve monitored emergency access accounts. A role assignment tells what an administrator may do; an audit record tells what was done.

## Sign-in troubleshooting

Use evidence in this order:

1. identify user, application, time, correlation/request ID, and device;
2. check whether the account exists, is enabled, and has the required service/license;
3. inspect sign-in logs and failure reason;
4. inspect authentication-method and MFA detail;
5. inspect Conditional Access evaluation and report-only results;
6. inspect risk detections and remediation state;
7. inspect application assignment/consent and workload authorization;
8. change policy only after reproducing and understanding the failure.

Risky users and risky sign-ins are detections, not final verdicts. Identity Secure Score and recommendations prioritize improvements; they are not proof of compliance or absence of risk.

## Applications and consent

Enterprise applications/service principals represent applications in a tenant. Delegated permissions act on behalf of a signed-in user within both the app's grant and the user's access. Application permissions allow app-only access granted to the workload. Admin consent can approve broad access and must be governed.

OAuth app consent and agent tools can create powerful routes to organizational data. Review publisher, requested scopes, credential lifecycle, owners, usage, data destination, and revocation path. Microsoft Defender capabilities can help discover and investigate risky OAuth applications.

> **Related item:** A user can authorize only the access represented by both the granted scopes and the user's own permissions in a delegated flow. App-only permissions change that boundary because the workload acts without the user's resource authorization.

---

# 3. Threat protection in Microsoft 365

Microsoft Defender XDR correlates supported identity, endpoint, email/collaboration, and cloud-app signals into incidents. Defender for Office 365 protects email and collaboration through capabilities such as anti-phishing, Safe Links, Safe Attachments, investigation, and campaign views under applicable licensing. Defender for Endpoint protects devices; Defender for Identity analyzes identity signals; Defender for Cloud Apps provides SaaS discovery and app/session governance.

Threat intelligence supplies context about adversaries, indicators, infrastructure, and techniques. A detection remains a signal requiring investigation. Incidents group alerts and entities so responders can determine scope and take action.

| Question | Evidence/control |
|---|---|
| Was a malicious attachment delivered or detonated? | Defender for Office 365 evidence |
| Did the endpoint execute suspicious code? | Defender for Endpoint evidence |
| Did a compromised account show abnormal identity behavior? | Entra/Defender for Identity evidence |
| Did a risky OAuth app access data? | Defender for Cloud Apps/app governance evidence |
| How are related alerts grouped? | Defender XDR incident |

Do not treat a user report, alert, incident, and confirmed breach as synonyms. Each represents a different point in the investigation.

---

# 4. Microsoft Purview data protection and governance

## Discover and classify data

Microsoft Purview supports information protection, DLP, data lifecycle/records, risk, audit, eDiscovery, and AI-related data security capabilities. Sensitive information types identify patterns such as regulated identifiers; trainable classifiers and other classification methods recognize content categories. Content Explorer shows classified/labeled items under restricted roles; Activity Explorer shows related user/system activity.

Sensitivity labels classify content and can apply protection such as encryption, markings, and container settings under configured policy. Auto-labeling can identify and label matching content after simulation/review. Labels travel with supported content more durably than a folder name.

## Data Loss Prevention

DLP policies detect and respond to sensitive-data activity across supported Microsoft 365 locations, endpoints, and other connected channels under current licensing. A rule combines location, conditions, exceptions, actions, user notifications, and incident/reporting choices.

Start in simulation or test mode. Tune false positives, user justification, business exceptions, and response ownership. DLP is not a replacement for least-privilege access; it addresses risky data use after access exists.

## Retention, records, and investigations

Retention policies and labels keep or delete content according to lifecycle rules. Records Management adds record declaration, disposition review, file-plan, and stronger controls. Audit searches supported activities. eDiscovery supports legal/investigation workflows for custodians, holds, collection, review, and export under applicable capabilities.

Insider Risk Management correlates configured indicators into privacy-aware risk workflows. Communication Compliance identifies policy matches in supported communications for reviewer workflows. These systems should use role separation, privacy controls, justified policy scope, and auditable investigation.

## Data Security Posture Management for AI

DSPM for AI helps discover AI use and data risks, apply policies, assess oversharing, investigate activity, and improve the data security posture surrounding AI applications under current Microsoft Purview capabilities. It complements ordinary information protection and access cleanup rather than creating a separate AI data universe.

> **Related item:** AI increases the value of good permissions hygiene because natural-language retrieval can make broadly accessible content easier to find and synthesize. The root problem is often pre-existing oversharing, not a model “breaking” permissions.

---

# 5. Microsoft 365 Copilot architecture and governance

## Grounding and data access

Microsoft 365 Copilot uses the user's prompt, Microsoft Graph context, eligible organizational content, and model orchestration under the product's documented architecture. It operates within the user's access to Microsoft 365 content. It does not make existing broad permissions appropriate.

```text
user + license + sign-in policy
              ↓
prompt → orchestration → Graph-grounded context under user access
              ↓                       ↓
         model response ← protection, policy, citations, logging
```

Administrative readiness includes identity and sign-in, supported licenses, application update/channel requirements, network endpoints, privacy settings, information protection, oversharing assessment, adoption, support, and measurement. **VERIFY CURRENT:** licensing, applications, capacity, models, data processing locations, and feature controls.

## Responsible AI and security

Responsible AI principles include fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. Administrators translate them into data policy, feature controls, acceptable use, reporting, monitoring, human review, and incident response.

Microsoft states product commitments about commercial data protection and model training in its current documentation; wording and boundaries can change. Avoid universal claims such as “no prompt is ever retained.” Verify the relevant service, account type, feature, and contractual documentation.

## Oversharing controls

Use permissions reports and data-access governance capabilities to find broadly accessible SharePoint content. SharePoint Advanced Management supplies controls and reports such as data access governance, site access review/restriction, and related Copilot readiness features under applicable licensing. Restricted access control limits a site's access to specified groups even if a user has a sharing link or previous permission, subject to current behavior.

Correct the ownership and permission model at the source. Removing a result from search or hiding a citation does not revoke underlying access.

---

# 6. Copilot and agent administration

## Licensing and consumption

Microsoft 365 Copilot and agents can use user licenses, capacity, and pay-as-you-go models depending on product and scenario. SharePoint agents and custom agents may have different entitlement and consumption paths. Use the Microsoft 365 admin center, Power Platform admin center, and billing/capacity surfaces according to the asset.

Never memorize a price for the exam. Understand the decision:

- which users need full Copilot capabilities;
- which scenario is covered by existing entitlements;
- which agent uses metered consumption;
- who owns the Azure subscription/billing policy if pay-as-you-go is used;
- how usage, capacity, budget, and business value will be monitored.

## Copilot capabilities and feature control

Microsoft 365 Copilot experiences include chat and application-integrated assistance. Researcher and Analyst provide specialized reasoning/analysis experiences under current availability. Administrators manage licenses, settings, release controls, agents, reporting, and user readiness through documented admin surfaces.

Copilot Analytics and adoption/usage reports help understand activation and use. Prompt/response or interaction reporting may be governed by privacy, role, and licensing constraints. Adoption metrics do not by themselves prove that output is accurate or business value was achieved.

## Agent lifecycle

Agents may be supplied by Microsoft, built from SharePoint, created in Copilot Studio, or provided by third parties. An administration lifecycle includes:

1. inventory and classify the agent;
2. verify owner, purpose, users, data, knowledge, tools, publisher, and environment;
3. assess authentication, authorization, DLP, connector, oversharing, and responsible-AI risk;
4. approve, block, deploy, assign, or publish under the appropriate workflow;
5. monitor usage, quality, tool actions, incidents, capacity, and stale ownership;
6. review changes and permissions;
7. suspend or retire safely.

The Microsoft 365 admin center and Power Platform admin center expose different parts of agent inventory and control. **VERIFY CURRENT:** Agent 365 naming, agent registry/approval features, admin-center navigation, and supported agent types.

> **Related item:** An agent is both an application and a potential actor. Govern its software supply chain, identity, knowledge permissions, tools, action authority, and operational behavior—not only its conversational content.

## Agent tools and actions

For an agent action, ask:

- Which user or workload identity reaches the tool?
- Does authorization occur at the target service?
- Can arguments be validated and constrained?
- Is human confirmation required?
- Can retries duplicate side effects?
- What is logged, and how are secrets/redaction handled?
- How is the action disabled during an incident?

A tool description helps the model select and call a capability. It does not enforce permission or business rules. Use least privilege, narrow actions, approval for consequential work, idempotency, timeouts, and audit evidence.

---

# 7. Hands-on and tabletop labs

## Lab 1: Microsoft 365 object map

In a permitted sandbox, map one user, security group, Microsoft 365 group, mailbox, team, channel, SharePoint site, and library. Trace which admin center owns the setting and where access is actually enforced.

## Lab 2: Sign-in investigation

Use a safe sample or documented sign-in event. Trace account, license, authentication, Conditional Access, risk, application consent, workload role, and audit evidence. Write the smallest safe fix rather than disabling a whole policy.

## Lab 3: Oversharing review

Create harmless files with intentionally different access in a test site. Compare membership, links, inheritance, and search/Copilot reachability. Remove access at the source and verify with a lower-privileged test user.

## Lab 4: Purview control map

For a public sample document, propose classification, sensitivity label, DLP, retention, audit, and eDiscovery behavior. State what each control does and which license/role must be verified.

## Lab 5: Agent approval record

Evaluate a hypothetical HR agent with SharePoint knowledge and a Power Automate action. Document owner, audience, data, permissions, DLP, action limits, approval, evaluation, monitoring, capacity, incident disablement, and retirement.

---

# 8. Knowledge checks and distinctions

1. A terminated employee's sign-in is blocked, but their shared content must remain discoverable. Which separate lifecycle actions are needed?
2. A user can open a source document and Copilot cites it. Why is this not a Copilot permission bypass, and what should be reviewed?
3. DLP allows a connector, but an agent's action receives HTTP 403. Which separate control likely denied it?
4. Usage reports show high Copilot adoption. What evidence is still required to claim business value?
5. A third-party agent requests broad application permissions. Which ownership, consent, and monitoring questions come before approval?
6. A sensitivity label protects a file, while retention preserves it. Why are both controls valid?

| Contrast | Remember |
|---|---|
| License vs permission | Entitles capability versus authorizes data/action |
| Microsoft 365 group vs distribution group | Collaboration/access resources versus email distribution |
| Authentication vs authorization | Prove identity versus permit resource/action |
| Entra role vs workload role | Directory administration versus service-specific administration |
| Delegated vs application permission | Acts with user context versus app-only authority |
| Sensitivity vs retention | Classification/protection versus lifecycle preservation/deletion |
| DLP vs source permission | Controls risky data use versus grants underlying access |
| Audit vs eDiscovery | Activity evidence versus preserve/collect/review content |
| Copilot grounding vs model training | Context used for a response versus data used to improve/train a model |
| Adoption vs value | Use/activity versus measured business outcome |
| Agent tool schema vs authorization | Describes call versus permits action |
| Microsoft 365 admin vs Power Platform admin | Tenant/service management versus environments, agents, connectors, and capacity |

## Readiness checklist

- [ ] I can explain tenant, subscriptions, domains, licenses, users, groups, roles, and lifecycle.
- [ ] I can distinguish Exchange, SharePoint, Teams, and their access objects.
- [ ] I can explain Zero Trust, Entra, SSO, MFA, Conditional Access, PIM, risk, and sign-in troubleshooting.
- [ ] I can distinguish delegated and application access and assess OAuth app consent.
- [ ] I can describe Defender XDR and its core Microsoft 365 protection surfaces.
- [ ] I can distinguish Purview classification, labels, DLP, retention, records, audit, eDiscovery, insider risk, and DSPM for AI.
- [ ] I can explain Microsoft 365 Copilot grounding and why source permissions matter.
- [ ] I can assess oversharing and choose source-level remediation.
- [ ] I can describe Copilot/agent licensing, pay-as-you-go, feature controls, usage, and analytics at a fundamental level.
- [ ] I can govern agent access, approval, monitoring, actions, capacity, incidents, and retirement.
- [ ] I checked every **VERIFY CURRENT** item and current blueprint.

## Primary references

- [Official AB-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900)
- [Microsoft 365 admin documentation](https://learn.microsoft.com/en-us/microsoft-365/admin/)
- [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)
- [Microsoft Defender XDR documentation](https://learn.microsoft.com/en-us/defender-xdr/)
- [Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)
- [Microsoft 365 Copilot documentation](https://learn.microsoft.com/en-us/copilot/microsoft-365/)
- [Microsoft 365 Copilot architecture](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture)
- [Manage agents for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-agents-integrated-apps)
- [SharePoint data access governance](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports)

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AB-900 course](https://learn.microsoft.com/en-us/training/courses/ab-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation for Microsoft 365, Purview, Copilot, and agent administration |
| [Microsoft — AB-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/copilot-and-agent-administration-fundamentals/practice/assessment?assessment-type=practice&assessmentId=428463062&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; use after learning and verify fast-changing details in current Microsoft documentation |
| [Microsoft Learn AB-900 learning material](https://learn.microsoft.com/en-us/credentials/certifications/microsoft-365-copilot-and-agent-administration-fundamentals/) | Free | About 10–14 hours | Official scope anchor; add tenant exploration where authorized |
| [Pluralsight — AB-900 path and practice exam](https://www.pluralsight.com/paths/microsoft-365-copilot-and-agent-administration-fundamentals-ab-900) | Subscription; practice access depends on plan/library | 9 hours plus about 2–4 hours for assessment and review | Three-course path published June–July 2026 by Vlad Catrinescu; public path explicitly includes a practice exam |
| [O'Reilly — Microsoft 365 Copilot and Agent Administration Fundamentals](https://www.oreilly.com/library/view/microsoft-365-copilot/9781807306519/) | Subscription | About 7 hours 22 minutes | Steve Miles, July 2026, 278 pages; broad book treatment aligned to the new credential |
| [O'Reilly — AB-900 Certification Course](https://www.oreilly.com/videos/ab-900-certification/9781807788490/) | Subscription | About 4 hours | Pavel Hrabec video course; useful compact review, then practice admin decisions |
| [Udemy — AB-900 by John Christopher](https://www.udemy.com/course/ab-900-copilot-agent-administration-fundamentals-course/) | Purchase or subscription | About 11 hours | Course shown as updated August 2026; inspect previews, hands-on tenant needs, and current objective mapping |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics) | Free | Select 2–4 hours by gap | Official product demos for Microsoft 365 Copilot, agents, identity, and governance; not a single exam course |
| [MeasureUp — AB-900 practice test](https://www.measureup.com/microsoft-ab-900-microsoft-365-copilot-agent-administration-fundamentals-practice-test.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 115 questions, released April 2026; verify fast-changing Copilot administration details against current Microsoft Learn |
| [Whizlabs — AB-900 course and practice tests](https://www.whizlabs.com/ab-900-microsoft-365-copilot-and-agent-administration/) | Paid course or subscription | About 3–6 hours for assessment and review; instructional time not published | Whizlabs identifies a mixed course/practice offering, but its public product page does not expose a reliable item count or total runtime; pair it with explanatory official learning |

Whizlabs identifies its AB-900 listing as a course and practice-test offering, but its public page does not expose enough detail to validate the instructional depth. All assessment products above are gap-detection supplements, not technical authority. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
