---
exam_code: AB-900
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-05
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AB-900 Microsoft 365 Copilot and Agent Administration Fundamentals Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 22, 2026 objectives and its cited public sources on August 31, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-900-coverage-record). The [official AB-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900) is authoritative.

**Current baseline:** Skills measured as of July 22, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Official source:** [AB-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900)

## How to use this guide

AB-900 connects ordinary Microsoft 365 administration with data governance and the new Copilot/agent control plane. For every scenario, trace the user or agent identity, license, data permission, policy, action, evidence, and administrator. “Copilot respects permissions” is a starting principle, not a substitute for fixing oversharing.

Use this administration sequence:

1. **Locate the object:** Is the issue about a user/group, mailbox, site/library/file, team/channel, application, policy, Copilot feature, agent, tool, or billing policy?
2. **Identify entitlement and identity:** Which license/service plan applies, who signs in or acts, and which authentication/Conditional Access result is relevant?
3. **Find authorization:** Which group, role, SharePoint permission, application grant, agent audience, or downstream tool permission permits the action?
4. **Apply protection/governance:** Which sensitivity, DLP, retention, risk, oversharing, or feature policy changes the behavior?
5. **Use the owning admin surface:** Microsoft 365, Entra, Exchange, SharePoint, Teams, Defender, Purview, Power Platform, and Agent 365 surfaces have different responsibilities.
6. **Prove the outcome:** Use sign-in/audit logs, reports, alerts, registry/operational signals, lower-privileged testing, adoption measures, and business outcomes.

Avoid “fixes” that erase evidence or lower protection broadly. If one user cannot sign in, investigate the event and policy result before disabling Conditional Access. If Copilot reveals an inappropriate document, fix the document/site authorization and ownership rather than treating the generated answer as the only problem.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Identify the core features and objects of Microsoft 365 services | 30–35% | How are users, collaboration services, identity, and security administered? |
| Understand data protection and governance tasks for Microsoft 365 and Copilot | 35–40% | How is organizational data discovered, protected, retained, and investigated—especially for AI? |
| Perform basic administrative tasks for Copilot and agents | 25–30% | How are Copilot and agents licensed, controlled, deployed, monitored, and governed? |

---

## 1. Microsoft 365 administration foundations

### Tenant, subscriptions, users, and groups

A Microsoft 365 tenant is the organization's cloud service boundary associated with Microsoft Entra ID. Subscriptions provide service entitlements. Licenses assigned directly or through groups enable eligible service plans for users. A custom domain must be verified before it can be used for sign-in and email addresses. The [Microsoft 365 admin documentation](https://learn.microsoft.com/en-us/microsoft-365/admin/) is the starting point for cross-service tenant administration.

| Object | Administration purpose |
|---|---|
| User | Human identity and service entitlement |
| Security group | Access and policy assignment |
| Microsoft 365 group | Membership and shared collaboration resources |
| Distribution group | Email distribution rather than general authorization |
| Shared mailbox | Mailbox used by several authorized users without ordinary personal sign-in |
| Dynamic group | Rule-based membership under applicable licensing |

Deleting or disabling a user, removing a license, blocking sign-in, revoking sessions, transferring data, preserving a mailbox, and retaining content are separate lifecycle actions. Design a leaver process rather than assuming one switch does everything.

Trace feature access as **subscription → assigned license → enabled service plan → user/group membership → sign-in policy → workload permission**. A license makes a service eligible; it does not add the user to a Team, grant access to a SharePoint site, approve an agent, or bypass Conditional Access. Group-based license changes can also take time to process and can fail, so confirm assignment state rather than assuming group membership completed the job.

The Microsoft 365 admin center provides broad tenant and service administration. Specialized admin centers expose deeper controls for Exchange, SharePoint, Teams, Microsoft Entra, Microsoft Defender, Microsoft Purview, Power Platform, and other workloads.

### Exchange Online, SharePoint, and Teams

Exchange Online manages mailboxes, mail flow, recipients, and related policies. Distribution groups distribute email; Microsoft 365 groups also underpin shared resources such as a group mailbox/calendar and can connect collaboration experiences.

SharePoint organizes content into sites, libraries, folders, files, lists, and pages. Permissions inherit by default but can be broken. Sharing links may grant access to specific people, people in the organization, existing access holders, or—in configured environments—anyone. Oversharing often comes from broad links, old group membership, broken inheritance, or content placed in an overly broad site.

Teams organizes collaboration into teams and channels. Standard channels are broadly available to team members; private and shared channels have distinct membership and site behavior. Teams policies control capabilities such as meetings, messaging, apps, and agents under the current service model. **VERIFY CURRENT:** policy names and admin surfaces.

> **Related item:** Collaboration membership and content permission are related but not always identical. Private/shared channels and linked SharePoint sites can create access boundaries that must be reviewed at the actual resource, not inferred only from the Teams UI.

#### Follow a collaboration object

A “project team” can involve several objects: a Microsoft 365 group for membership, a Team for collaboration, channels for conversation, SharePoint sites/libraries/files for content, and an Exchange group mailbox/calendar. A standard channel normally uses the team's primary SharePoint site, while private/shared channel designs create distinct membership and site considerations. Diagnose access at the object holding the data.

For example, adding a person to an email distribution group does not grant site access. Sharing a file does not necessarily add someone to the Team. Deleting a Team has different lifecycle and retention implications from removing one member. Map the dependency before changing it.

---

## 2. Identity and access for Microsoft 365

### Zero Trust and authorization

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

An access decision has several gates: authenticate the identity, evaluate Conditional Access signals and controls, authorize the workload/resource action, then record and govern continued access. SSO improves the session experience but is not another authorization grant. PIM can make a privileged role eligible and time-bound; it does not remove the need for approval context, audit, or incident response.

### Sign-in troubleshooting

Use evidence in this order; Microsoft documents the [sign-in log details](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-in-log-activity-details) and a [Conditional Access troubleshooting process](https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access):

1. identify user, application, time, correlation/request ID, and device;
2. check whether the account exists, is enabled, and has the required service/license;
3. inspect sign-in logs and failure reason;
4. inspect authentication-method and MFA detail;
5. inspect Conditional Access evaluation and report-only results;
6. inspect risk detections and remediation state;
7. inspect application assignment/consent and workload authorization;
8. change policy only after reproducing and understanding the failure.

Risky users and risky sign-ins are detections, not final verdicts. Identity Secure Score and recommendations prioritize improvements; they are not proof of compliance or absence of risk.

The same symptom can have different owners. “Copilot will not open” might be an unassigned license/service plan, blocked sign-in, Conditional Access failure, disabled Copilot feature, unsupported client, or missing data permission. Start with time, user, app/resource, correlation ID, and actual error; then identify the failed gate. Do not infer a licensing problem from HTTP 403 or an MFA problem from a generic access-denied page.

### Applications and consent

Enterprise applications/service principals represent applications in a tenant. Delegated permissions act on behalf of a signed-in user within both the app's grant and the user's access. Application permissions allow app-only access granted to the workload. Admin consent can approve broad access and must be governed.

An app registration is the global application definition in its home tenant; an enterprise application/service principal is the local representation used for tenant assignment, consent, SSO, and Conditional Access integration. One application definition can have service principals in multiple tenants. For exam scenarios, ask whether the administrator is defining the application, configuring its tenant instance, or reviewing its granted permission.

OAuth app consent and agent tools can create powerful routes to organizational data. Review publisher, requested scopes, credential lifecycle, owners, usage, data destination, and revocation path. Microsoft Defender capabilities can help discover and investigate risky OAuth applications.

> **Related item:** A user can authorize only the access represented by both the granted scopes and the user's own permissions in a delegated flow. App-only permissions change that boundary because the workload acts without the user's resource authorization.

---

## 3. Threat protection in Microsoft 365

[Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender) correlates supported identity, endpoint, email/collaboration, and cloud-app signals into incidents. Defender for Office 365 protects email and collaboration through capabilities such as anti-phishing, Safe Links, Safe Attachments, investigation, and campaign views under applicable licensing. Defender for Endpoint protects devices; Defender for Identity analyzes identity signals; Defender for Cloud Apps provides SaaS discovery and app/session governance.

Threat intelligence supplies context about adversaries, indicators, infrastructure, and techniques. A detection remains a signal requiring investigation. Incidents group alerts and entities so responders can determine scope and take action.

| Question | Evidence/control |
|---|---|
| Was a malicious attachment delivered or detonated? | Defender for Office 365 evidence |
| Did the endpoint execute suspicious code? | Defender for Endpoint evidence |
| Did a compromised account show abnormal identity behavior? | Entra/Defender for Identity evidence |
| Did a risky OAuth app access data? | Defender for Cloud Apps/app governance evidence |
| How are related alerts grouped? | Defender XDR incident |

Do not treat a user report, alert, incident, and confirmed breach as synonyms. Each represents a different point in the investigation.

Follow a signal as **telemetry → alert → correlated incident → investigation → containment/remediation → evidence**. Threat intelligence adds adversary and indicator context; it does not prove that a tenant entity is compromised. Audit activity and Defender alerts also answer different questions: an audit record can show an administrator changed a setting without claiming the change was malicious.

---

## 4. Microsoft Purview data protection and governance

### Discover and classify data

[Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview) supports information protection, DLP, data lifecycle/records, risk, audit, eDiscovery, and AI-related data security capabilities. Sensitive information types identify patterns such as regulated identifiers; trainable classifiers and other classification methods recognize content categories. Content Explorer shows classified/labeled items under restricted roles; Activity Explorer shows related user/system activity.

The current blueprint specifically names [Microsoft Purview Data Explorer](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer). Data Explorer presents a current snapshot of items that have a sensitivity label, retention label, or sensitive-information-type classification. Start at **Microsoft Purview portal → Solutions → Information Protection → Explorers → Data explorer**, select or filter by the relevant label, classifier, or sensitive information type, narrow the location, and inspect the matching items that the assigned role permits. Use it to answer **where the sensitive items are now**; confirm coverage, scan timing, and false matches before treating a count as complete.

Keep the explorers distinct:

| Explorer | Primary question | Evidence and access boundary |
|---|---|---|
| Data Explorer | Which individual classified or labeled items are present in the current snapshot? | Item/location list and, with separately assigned content-view permission, item content |
| Content Explorer (classic) | Where is classified or labeled content distributed by location and classification? | Aggregated drill-down and item views under its own restricted roles |
| Activity Explorer | What supported user or system activity occurred involving sensitive or labeled content? | Time-based activity records, operations, actors, locations, and policy context |

Data Explorer access is intentionally restricted because content viewing can expose files beyond their local permissions. **Data Explorer List viewer** permits item and location listing; **Data Explorer Content viewer** permits content inspection. The permissions are independent rather than cumulative, so assign both only when the task requires both. Use least privilege, a justified case, role review, and audit; do not grant broad explorer access merely to troubleshoot one DLP alert.

Sensitivity labels classify content and can apply protection such as encryption, markings, and container settings under configured policy. Auto-labeling can identify and label matching content after simulation/review. Labels travel with supported content more durably than a folder name.

### Data Loss Prevention

[DLP policies](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) detect and respond to sensitive-data activity across supported Microsoft 365 locations, endpoints, and other connected channels under current licensing. A rule combines location, conditions, exceptions, actions, user notifications, and incident/reporting choices.

Start in simulation or test mode. Tune false positives, user justification, business exceptions, and response ownership. DLP is not a replacement for least-privilege access; it addresses risky data use after access exists.

### Retention, records, and investigations

Retention policies and labels keep or delete content according to lifecycle rules. Records Management adds record declaration, disposition review, file-plan, and stronger controls. Audit searches supported activities. eDiscovery supports legal/investigation workflows for custodians, holds, collection, review, and export under applicable capabilities.

Insider Risk Management correlates configured indicators into privacy-aware risk workflows. Communication Compliance identifies policy matches in supported communications for reviewer workflows. These systems should use role separation, privacy controls, justified policy scope, and auditable investigation.

### Data Security Posture Management for AI

[Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) helps organize data-security objectives, discover AI/data activity, assess oversharing, apply protections, investigate risk, and track posture under current Microsoft Purview capabilities. The July 2026 blueprint uses the name **DSPM for AI**; Microsoft documentation now distinguishes newer DSPM experiences from [DSPM for AI (classic)](https://learn.microsoft.com/en-us/purview/dspm-for-ai). **VERIFY CURRENT:** portal naming, classic/current experience, supported AI apps, automatic assessments, policies, licensing, and data availability.

> **Related item:** AI increases the value of good permissions hygiene because natural-language retrieval can make broadly accessible content easier to find and synthesize. The root problem is often pre-existing oversharing, not a model “breaking” permissions.

#### Follow one governed document

1. Classification detects the content type; a sensitivity label communicates classification and may apply markings/encryption.
2. SharePoint/site/library/file authorization determines who can reach the source; the label's encryption rights can further constrain use.
3. DLP observes a supported sharing/use event and audits, warns, restricts, or alerts according to policy.
4. Retention keeps or deletes the item under lifecycle rules; a record label can add stronger governance.
5. Activity Explorer surfaces supported data activities; DLP alerts support response; Insider Risk or Communication Compliance can create their own privacy-aware review workflows.
6. Audit supplies activity evidence, while eDiscovery preserves, searches, collects, reviews, and exports governed content for a matter.
7. Compliance Manager maps improvement actions and evidence to assessments; its score is neither legal advice nor certification.

The controls can all apply to the same file without being duplicates. Classification says what it is; permissions say who can access it; protection/DLP govern handling; retention says how long it remains; audit says what occurred; eDiscovery governs investigation content.

---

## 5. Microsoft 365 Copilot architecture and governance

### Grounding and data access

[Microsoft 365 Copilot architecture](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture) uses the user's prompt, Microsoft Graph context, eligible organizational content, and model orchestration inside the Microsoft 365 service boundary. It operates within the user's access to Microsoft 365 content. It does not make existing broad permissions appropriate.

```text
user + license + sign-in policy
              ↓
prompt → orchestration → Graph-grounded context under user access
              ↓                       ↓
         model response ← protection, policy, citations, logging
```

Administrative readiness includes identity and sign-in, supported licenses, application update/channel requirements, network endpoints, privacy settings, information protection, oversharing assessment, adoption, support, and measurement. **VERIFY CURRENT:** licensing, applications, capacity, models, data processing locations, and feature controls.

Trace one grounded response:

1. The licensed/eligible user signs in through applicable Entra and Conditional Access controls.
2. The prompt enters Copilot; orchestration can use Microsoft Graph to retrieve context the user is authorized to access.
3. Source permissions, SharePoint/OneDrive controls, sensitivity labels/encryption, and applicable policies constrain discovery and extraction.
4. The model generates a response from the grounded prompt and other allowed context; citations or source references help the user inspect evidence where supported.
5. The response returns to the user's experience, and interaction data is handled under current Microsoft 365/Purview architecture.
6. Audit, retention, eDiscovery, DLP, and data-security tools can govern supported Copilot activity according to configuration and licensing. Review the current [Copilot data-protection architecture](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture-data-protection-auditing).

Grounding is use of context for the current interaction; model training is use of data to improve a model. Data storage/retention, abuse monitoring, feedback, web grounding, third-party models, and training commitments are separate questions. Use the applicable current product and contractual documentation instead of turning one statement into a universal promise.

### Responsible AI and security

Responsible AI principles include fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. Administrators translate them into data policy, feature controls, acceptable use, reporting, monitoring, human review, and incident response.

Microsoft states product commitments about commercial data protection and model training in its current documentation; wording and boundaries can change. Avoid universal claims such as “no prompt is ever retained.” Verify the relevant service, account type, feature, and contractual documentation.

### Oversharing controls

Use [data-access governance reports](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports) to find broadly accessible SharePoint content and permission patterns. SharePoint Advanced Management supplies reports and controls such as site access review/restriction and related Copilot readiness features under applicable licensing. [Restricted access control](https://learn.microsoft.com/en-us/sharepoint/restricted-access-control) limits site/content access to specified groups even when a user had prior permission or a sharing link, subject to current behavior.

Correct the ownership and permission model at the source. Removing a result from search or hiding a citation does not revoke underlying access.

Use an oversharing remediation loop:

1. **Discover:** run applicable reports or assessments for broad links, Everyone/Everyone-except-external-users access, excessive users, or risky sites.
2. **Validate:** involve site/data owners who understand legitimate business access; a large audience is not automatically wrong.
3. **Remediate:** remove stale membership/links, restore inheritance where appropriate, reorganize content, or apply a supported restriction.
4. **Contain when needed:** discovery restrictions can reduce broad search/Copilot surfacing during review, but do not confuse discoverability with source authorization.
5. **Verify:** test as affected lower-privileged identities and rerun reports after propagation.
6. **Sustain:** assign owners, expiration/review, sharing defaults, sensitivity/retention policies, and ongoing reporting.

> **Related item:** Restricted Content Discovery affects discovery in supported search/Copilot scenarios and is useful as temporary containment; restricted access control changes whether an out-of-group user can access the site/content. Know whether the requirement is “do not surface during review” or “deny access.”

---

## 6. Copilot and agent administration

### Licensing and consumption

Microsoft 365 Copilot and agents can use user licenses, capacity, and pay-as-you-go models depending on product and scenario. SharePoint agents and custom agents may have different entitlement and consumption paths. Use the Microsoft 365 admin center, Power Platform admin center, and billing/capacity surfaces according to the asset.

Never memorize a price for the exam. Understand the decision:

- which users need full Copilot capabilities;
- which scenario is covered by existing entitlements;
- which agent uses metered consumption;
- who owns the Azure subscription/billing policy if pay-as-you-go is used;
- how usage, capacity, budget, and business value will be monitored.

The [Copilot pay-as-you-go setup](https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/setup) uses a billing policy associated with eligible users/groups and a supported Copilot service, with Azure subscription/resource-group prerequisites under the current model. A budget can be an alerting/management mechanism rather than a hard stop, so monitor actual spending and know how to disable the service. **VERIFY CURRENT:** eligible services, meters/credits, included entitlements, roles, limits, propagation, billing surfaces, and budget behavior.

Separate four decisions: a base Microsoft 365 license supplies workload access; a Microsoft 365 Copilot user license supplies eligible per-user Copilot capabilities; pay-as-you-go enables eligible metered scenarios; an agent can also consume capacity or require its own prerequisites. Never infer data permission from any of these entitlements.

### Copilot capabilities and feature control

[Microsoft Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview) includes chat, search, and application-integrated experiences under applicable licenses and entitlements. The free-with-eligible-subscription Copilot Chat experience and the paid Microsoft 365 Copilot user license do not expose identical work-grounded/app capabilities. **VERIFY CURRENT:** product names, eligible subscriptions, included features, web/work grounding, agents, usage limits, and data-protection behavior.

[Researcher](https://learn.microsoft.com/en-us/microsoft-365/copilot/faq-researcher) is intended for deeper, multi-step research and synthesis. Analyst is intended for analysis of data and related work, including spreadsheet-oriented scenarios. They are Microsoft-built specialized agents, unlike a custom agent scoped to organization-specific instructions, knowledge, and tools. **VERIFY CURRENT:** availability, controls, limits, supported sources/file types, model choices, reporting, and license requirements.

Administrators manage licenses, settings, release controls, agents, reporting, and user readiness through documented admin surfaces. A feature control can disable an experience without removing the user's license; removing a license can remove entitlement without repairing data access; blocking an agent does not necessarily disable all Copilot. Identify the smallest object and policy that owns the requested change.

[Microsoft 365 Copilot reports](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-reports-for-admins) and Copilot Analytics can help distinguish readiness, activation, usage, adoption patterns, and deeper impact analysis under applicable roles/licenses. Prompt/response or interaction reporting is governed by privacy, role, retention, and licensing constraints. Adoption metrics do not by themselves prove that output is accurate or business value was achieved.

Measure a chain: **eligible → assigned → activated → active use → scenario adoption → quality/safety → business outcome → sustained value**. A low activation rate is a deployment/adoption signal; a high prompt count is not an ROI calculation. Pair usage data with process measures such as cycle time, rework, decision quality, satisfaction, and risk incidents.

Users can save, share, schedule, and delete prompts or prompt-related content in supported current experiences. Those actions have different objects and consequences: deleting a saved prompt/template does not necessarily delete historical interaction records; deleting a scheduled definition is different from deleting past runs; sharing a prompt can expose instructions without granting its referenced data. **VERIFY CURRENT:** Prompt Gallery/Copilot/Cowork surfaces, scheduling limits, retention, export, sharing scope, and administrative controls.

### Agent lifecycle

Agents may be supplied by Microsoft, built from SharePoint, created in Microsoft 365 Copilot or Copilot Studio, or provided by third parties. Agent creation defines purpose, instructions, knowledge, tools, and user experience under the selected authoring surface; agent administration decides whether and how that artifact enters the tenant and who can use it.

For a fundamentals-level creation path, [Agent Builder in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) provides a no-code route to a declarative agent:

1. **Define the task:** state the intended users, one bounded outcome, non-goals, approved knowledge, and whether the agent only answers or also needs capabilities. Use Copilot Studio when advanced actions or orchestration exceed Agent Builder's fit.
2. **Start safely:** in a permitted sandbox or private test context, select **New agent** and either describe the agent in natural language, start from a template, or use **Skip to configure**. Selecting a template currently creates the agent automatically, so keep that result private and test it immediately.
3. **Configure:** review the name, description, instructions, knowledge sources, capabilities, and starter prompts. Instructions guide behavior; they do not grant source or action permission. Add only synthetic or approved least-privilege knowledge.
4. **Test in the authoring experience:** use **Try it** before selecting **Create** on the describe/configure path, or immediately after template creation, with expected questions, unsupported questions, prompt-attack attempts, stale or absent knowledge, and a lower-privileged persona where possible. Inspect citations and verify source access directly.
5. **Create and control distribution:** on the describe/configure path, select **Create** only after the test meets its criteria. Microsoft documents that a [newly created Agent Builder agent is private and available only to its creator](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents); direct sharing, organizational-catalog submission and admin publication, and cross-channel deployment are later and distinct decisions governed by current tenant policy.
6. **Record and clean up:** retain the owner, purpose, configuration, test evidence, sharing state, and review date. Delete or retire the test artifact and synthetic content when the exercise ends unless it enters an approved lifecycle.

An administration lifecycle includes:

1. inventory and classify the agent;
2. verify owner, purpose, users, data, knowledge, tools, publisher, and environment;
3. assess authentication, authorization, DLP, connector, oversharing, and responsible-AI risk;
4. approve, block, deploy, assign, or publish under the appropriate workflow;
5. monitor usage, quality, tool actions, incidents, capacity, and stale ownership;
6. review changes and permissions;
7. suspend or retire safely.

The [agent workload in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview) provides registry, governance, deployment/approval, risk, operational, and lifecycle views under current Agent 365 capabilities. The Power Platform admin center exposes environments, Copilot Studio agents, connectors, DLP, capacity, and related platform administration. **VERIFY CURRENT:** Agent 365 naming, agent registry and approval features, roles, licenses, policy templates, admin-center navigation, integrations, and supported agent types.

Use approval as a risk decision, not a publishing click. Review the agent's owner/publisher, audience, data/knowledge, tools and MCP servers, delegated or app-only permissions, DLP, external data destinations, cost model, evaluation, incident disablement, and retirement. The current [agent request workflow](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests) can expose pending review/update/activation decisions and audience scoping; exact states and actions are volatile.

Monitor at two levels. The Microsoft 365 admin center/Agent 365 layer tracks the estate, ownership, deployment, access, risk, lifecycle, and operational insights. The Power Platform/Copilot Studio layer tracks the authoring environment, capacity, conversation/outcome analytics, tools, flow failures, and maker lifecycle. Evidence can overlap, but the portals do not have identical inventory or purpose.

> **Related item:** An agent is both an application and a potential actor. Govern its software supply chain, identity, knowledge permissions, tools, action authority, and operational behavior—not only its conversational content.

### Agent tools and actions

For an agent action, ask:

- Which user or workload identity reaches the tool?
- Does authorization occur at the target service?
- Can arguments be validated and constrained?
- Is human confirmation required?
- Can retries duplicate side effects?
- What is logged, and how are secrets/redaction handled?
- How is the action disabled during an incident?

A tool description helps the model select and call a capability. It does not enforce permission or business rules. Use least privilege, narrow actions, approval for consequential work, idempotency, timeouts, and audit evidence.

[Agent tool administration](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-tools-for-agent) can include registry and request/approval controls for supported tools such as MCP servers. Tool approval and agent approval answer different questions: a tool may be allowed in the tenant while a particular agent should not receive it, and an approved agent still needs narrow downstream authorization.

---

## 7. Objective-to-scenario drill

| Scenario clue | Best starting object or tool | Boundary to preserve |
|---|---|---|
| User is licensed but cannot open Copilot | User/service plan, sign-in log, Conditional Access, feature control | Entitlement, authentication/policy, feature availability, and data permission are separate gates |
| Send email to a list without creating collaboration resources | Distribution group | Microsoft 365 groups support shared collaboration resources and can authorize membership-based access |
| User can enter a Team but cannot open one linked file | Actual SharePoint site/library/file permission | Team/channel membership is not a complete view of every content permission |
| Explain why one sign-in was blocked | Entra sign-in log plus Conditional Access details | Do not disable tenant-wide protection before identifying the failed event/policy/control |
| Make an admin role eligible and time-bound | PIM | PIM governs privileged activation; the role defines the permission and audit records its use |
| Configure tenant consent/assignment/SSO for an application | Enterprise application/service principal | App registration defines the application; the service principal is its tenant instance |
| Correlate identity, endpoint, email, and cloud-app alerts | Defender XDR incident | Alerts are signals; an incident is the investigation container; neither alone proves breach |
| Encrypt and mark a confidential document | Sensitivity label | Retention governs lifecycle; DLP governs supported use/sharing; source permission grants access |
| Block external sharing of regulated identifiers and alert responders | Purview DLP | DLP is not the same as SharePoint authorization or a sensitivity label |
| Find potentially risky AI activity and overshared sensitive data | Purview DSPM/data-security objectives | Verify whether the scenario uses current DSPM or classic DSPM-for-AI terminology and capabilities |
| Determine which SharePoint sites a user can reach before Copilot rollout | Data access governance permission report | A report discovers state; the site/data owner validates and remediates legitimate access |
| Deny a site to users outside specified groups despite an old link | Restricted access control | Discovery restriction can hide broad results temporarily but does not replace access denial |
| Preserve prompts/interactions for investigation | Purview retention/eDiscovery/Audit as applicable | User history deletion, retention, audit evidence, and eDiscovery preservation are distinct |
| Enable metered Copilot Chat/SharePoint-agent use | Pay-as-you-go billing policy | Billing eligibility/cost does not grant source permission or approve every agent |
| Deep multi-source research rather than quick chat | Researcher | Analyst focuses data-analysis scenarios; a custom agent adds organization-specific knowledge/tools |
| Decide whether a custom agent becomes tenant-available | Agent request/approval and audience | Creation, approval, deployment, user access, tool approval, and downstream authorization differ |
| Find ownerless, risky, inactive, or failing agents across the tenant | Agent registry/Agent 365 operational and lifecycle views | Copilot Studio/Power Platform has deeper environment and maker/runtime details for applicable agents |

#### Integrated scenario: HR agent exposes an old compensation file

Do not conclude “the AI bypassed security.” Work the chain:

1. Confirm the affected user, agent, prompt/time, cited source, and whether the user can open the file directly.
2. Inspect site/library/file permissions, link type, group membership, broken inheritance, and ownership. If the user had source access, Copilot surfacing amplified pre-existing oversharing.
3. Contain appropriately: remove incorrect access or stale links, use restricted access control when group-scoped denial is required, and consider temporary discovery restriction during a wider review.
4. Run applicable data-access governance/DSPM assessments, involve the HR data owner, and find similar content rather than fixing one citation only.
5. Review sensitivity label/encryption, DLP, retention, audit, and agent knowledge/tool configuration. These controls address different portions of the event.
6. If malicious activity is suspected, use Defender/Purview/Entra evidence to scope identities, devices, apps, downloads, sharing changes, and agent actions.
7. Verify remediation as a lower-privileged user, rerun reports after propagation, record owner and prevention actions, and evaluate whether the agent's audience/approval remains valid.

The administrator's goal is durable authorization and governance, not merely making one answer disappear.

---

## 8. Hands-on and tabletop labs

### Lab 1: Microsoft 365 object map

In a permitted sandbox, map one user, security group, Microsoft 365 group, mailbox, team, channel, SharePoint site, and library. Trace which admin center owns the setting and where access is actually enforced.

### Lab 2: Sign-in investigation

Use a safe sample or documented sign-in event. Trace account, license, authentication, Conditional Access, risk, application consent, workload role, and audit evidence. Write the smallest safe fix rather than disabling a whole policy.

### Lab 3: Oversharing review

Create harmless files with intentionally different access in a test site. Compare membership, links, inheritance, and search/Copilot reachability. Remove access at the source and verify with a lower-privileged test user.

### Lab 4: Purview control map

For a public or synthetic sample document in a disposable tenant, propose classification, sensitivity label, DLP, retention, audit, and eDiscovery behavior. After classification is available, use Data Explorer with list-only permission to filter by label or sensitive information type and location; record what the result proves and its snapshot time. Tabletop content inspection unless separately authorized, then compare the evidence with Activity Explorer for a controlled labeling or DLP event. State what each control does and which license/role must be verified. **Evidence:** filtered item/location result, freshness and coverage caveats, list-versus-content role decision, related activity record, and cleanup.

### Lab 5: Create and test a private agent

In a permitted sandbox, use Agent Builder or a documented equivalent to create a private agent for a harmless onboarding FAQ. Define one purpose, intended test audience, and explicit non-goals; use synthetic or public knowledge; configure name, description, instructions, and starter prompts; and test expected, out-of-scope, uncited, prompt-attack, and lower-privileged cases. Do not share, publish, add write actions, or use production-sensitive content. Record the private state and the proposed audience plus approval/publication handoff criteria, then delete the test agent and content or hand them into an approved lifecycle. **Evidence:** configuration worksheet, source list and permissions, audience and handoff record, positive/negative test results, citation checks, creation state, and cleanup result.

### Lab 6: Agent approval record

Evaluate a hypothetical HR agent with SharePoint knowledge and a Power Automate action. Document owner, audience, data, permissions, DLP, action limits, approval, evaluation, monitoring, capacity, incident disablement, and retirement.

---

## 9. Knowledge checks and distinctions

1. A terminated employee's sign-in is blocked, but their shared content must remain discoverable. Which separate lifecycle actions are needed?
2. A user can open a source document and Copilot cites it. Why is this not a Copilot permission bypass, and what should be reviewed?
3. DLP allows a connector, but an agent's action receives HTTP 403. Which separate control likely denied it?
4. Usage reports show high Copilot adoption. What evidence is still required to claim business value?
5. A third-party agent requests broad application permissions. Which ownership, consent, and monitoring questions come before approval?
6. A sensitivity label protects a file, while retention preserves it. Why are both controls valid?
7. Data Explorer shows a sensitive item. What does that prove, which roles expose its list or content, and why does Activity Explorer answer a different question?
8. You tested a private FAQ agent successfully. Which separate creation, sharing, approval, deployment, source-permission, and cleanup decisions remain?

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

### Readiness checklist

- [ ] I can explain tenant, subscriptions, domains, licenses, users, groups, roles, and lifecycle.
- [ ] I can distinguish Exchange, SharePoint, Teams, and their access objects.
- [ ] I can explain Zero Trust, Entra, SSO, MFA, Conditional Access, PIM, risk, and sign-in troubleshooting.
- [ ] I can distinguish delegated and application access and assess OAuth app consent.
- [ ] I can describe Defender XDR and its core Microsoft 365 protection surfaces.
- [ ] I can distinguish Purview classification, labels, DLP, retention, records, audit, eDiscovery, insider risk, and DSPM for AI.
- [ ] I can use Data Explorer to locate sensitive items and distinguish its snapshot and restricted roles from Content Explorer and Activity Explorer.
- [ ] I can explain Microsoft 365 Copilot grounding and why source permissions matter.
- [ ] I can assess oversharing and choose source-level remediation.
- [ ] I can describe Copilot/agent licensing, pay-as-you-go, feature controls, usage, and analytics at a fundamental level.
- [ ] I can safely create and test a private agent, then distinguish creation from sharing, approval, deployment, downstream permission, monitoring, and retirement.
- [ ] I checked every **VERIFY CURRENT** item and current blueprint.

### Primary references

- [Official AB-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900)
- [Microsoft 365 admin documentation](https://learn.microsoft.com/en-us/microsoft-365/admin/)
- [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)
- [Microsoft Defender XDR documentation](https://learn.microsoft.com/en-us/defender-xdr/)
- [Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)
- [Microsoft 365 Copilot documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/)
- [Microsoft 365 Copilot architecture](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture)
- [Manage agents for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview)
- [SharePoint data access governance](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports)
- [Microsoft Purview Data Explorer](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer)
- [Build agents with Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — AB-900 course](https://learn.microsoft.com/en-us/training/courses/ab-900t00) | Free self-study; instructor-led options vary | 1 day (official course) | Current objective-aligned foundation for Microsoft 365, Purview, Copilot, and agent administration |
| [Microsoft — AB-900 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/copilot-and-agent-administration-fundamentals/practice/assessment?assessment-type=practice&assessmentId=428463062&practice-assessment-type=certification) | Free Microsoft account | About 1–2 hours for an attempt and review | Repeatable official readiness check with rationales and learning links; use after learning and verify fast-changing details in current Microsoft documentation |
| [Microsoft Learn AB-900 learning material](https://learn.microsoft.com/en-us/credentials/certifications/copilot-and-agent-administration-fundamentals/) | Free | About 10–14 hours | Official scope anchor; add tenant exploration where authorized |
| [Pluralsight — AB-900 path and practice exam](https://www.pluralsight.com/paths/microsoft-365-copilot-and-agent-administration-fundamentals-ab-900) | Subscription; practice access depends on plan/library | 9 hours plus about 2–4 hours for assessment and review | Three-course path published June–July 2026 by Vlad Catrinescu; public path explicitly includes a practice exam |
| [O'Reilly — Microsoft 365 Copilot and Agent Administration Fundamentals](https://www.oreilly.com/library/view/microsoft-365-copilot/9781807306519/) | Subscription | About 7 hours 22 minutes | Steve Miles, July 2026, 278 pages; broad book treatment aligned to the new credential |
| [O'Reilly — AB-900 Certification Course](https://www.oreilly.com/videos/ab-900-certification/9781807788490/) | Subscription | About 4 hours | Pavel Hrabec video course; useful compact review, then practice admin decisions |
| [Udemy — AB-900 by John Christopher](https://www.udemy.com/course/ab-900-copilot-agent-administration-fundamentals-course/) | Purchase or subscription | About 11 hours | Course shown as updated August 2026; inspect previews, hands-on tenant needs, and current objective mapping |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics) | Free | Select 2–4 hours by gap | Official product demos for Microsoft 365 Copilot, agents, identity, and governance; not a single exam course |
| [MeasureUp — AB-900 practice test](https://www.measureup.com/microsoft-ab-900-microsoft-365-copilot-agent-administration-fundamentals-practice-test.html) | Paid test or subscription; free demo available | About 4–8 hours for simulation and review | Tier 6 assessment with 115 questions, released April 2026; verify fast-changing Copilot administration details against current Microsoft Learn |
| [Whizlabs — AB-900 course and practice tests](https://www.whizlabs.com/ab-900-microsoft-365-copilot-and-agent-administration/) | Paid course or subscription | About 3–6 hours for assessment and review; instructional time not published | Whizlabs identifies a mixed course/practice offering, but its public product page does not expose a reliable item count or total runtime; pair it with explanatory official learning |

Whizlabs identifies its AB-900 listing as a course and practice-test offering, but its public page does not expose enough detail to validate the instructional depth. All assessment products above are gap-detection supplements, not technical authority. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
