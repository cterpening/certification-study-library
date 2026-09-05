---
exam_code: AB-650
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-650
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-05
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# AB-650 AI Services Administrator Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the beta objectives and cited public sources on September 1, 2026. It may still contain errors, and beta objectives or product surfaces can change quickly. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-650-coverage-record). The [official AB-650 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-650) is authoritative.

**Current baseline:** Beta blueprint page last updated July 27, 2026; Microsoft does not state a separate “skills measured as of” date on the page.<br>
**Upcoming blueprint change:** No dated change is announced, but beta content can change before general availability. Recheck the official page before studying or scheduling.<br>
**Official source:** [AB-650 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-650)

## How to use this guide

AB-650 is an operations exam. It asks whether you can make Microsoft 365 and its AI services usable, governed, secure, observable, and supportable—not merely define Copilot. For each scenario, follow this chain:

1. identify the tenant, workload, user or agent identity, and owning administrator;
2. verify the subscription, license or pay-as-you-go entitlement;
3. determine the effective role, resource permission, Conditional Access result, and agent/tool grant;
4. apply workload, Defender, Purview, SharePoint, Copilot, and Agent 365 controls at the correct layer;
5. deploy through a controlled lifecycle with owners, audiences, approvals, and rollback;
6. use service health, audit, security alerts, usage, cost, and outcome data to prove the result.

Do not solve a data-access problem only at the AI surface. Copilot and agents can make existing oversharing easier to discover, but source authorization, labels, encryption, DLP, lifecycle, and ownership remain distinct controls. Do not solve one failed sign-in by weakening Conditional Access tenant-wide. Start with evidence and find the failed gate.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Configure and manage Microsoft 365 tenants and workloads | 20–25% | Are tenant services, collaboration workloads, Copilot readiness, and operations configured correctly? |
| Govern and secure Microsoft 365 tenants and workloads | 40–45% | Are identities, access, threats, data, and AI activity governed with evidence? |
| Manage and secure AI services in Microsoft 365 | 35–40% | Can administrators control Copilot, agents, tools, lifecycle, security, cost, usage, and adoption? |

---

## 1. Configure and manage Microsoft 365 tenants and workloads

### Tenant foundation, domains, licenses, and operational health

A Microsoft 365 tenant uses Microsoft Entra ID as its identity boundary. Establish organization profile and branding, verify custom domains through DNS, set organization and release preferences, assign administrative responsibility, and document emergency and support paths. Domain verification proves control of the DNS namespace; it does not migrate mail or rewrite existing sign-in names automatically.

Trace entitlement as **subscription or pay-as-you-go billing → available product/service plan → direct or group-based assignment → workload provisioning → feature policy → resource permission**. A Microsoft 365 Copilot, Agent 365, or Copilot Studio entitlement makes a feature eligible; it does not grant access to a SharePoint site, publish an agent, approve an MCP server, or bypass Conditional Access. Group-based licensing can fail because of conflicting service plans, insufficient inventory, usage-location problems, or processing delays. Verify the assignment state.

Use the Microsoft 365 admin center for organization settings, licensing, health, reports, and cross-service administration. Use specialized centers for Entra, Exchange, Teams, SharePoint, Defender, Purview, Power Platform, and agent operations. Prefer the least-privileged role that owns the task. Record which team handles identity, data, security, AI deployment, billing, and incident escalation.

Service Health reports Microsoft-confirmed incidents and advisories; Message center communicates planned service changes; usage reports describe adoption; audit logs describe supported activity; security products describe threats. A user complaint is a signal, not proof that Microsoft has a service incident. Correlate time, tenant, workload, affected population, client, network path, health notice, configuration change, and error/correlation ID.

Microsoft 365 Backup protects supported Exchange, SharePoint, and OneDrive data with configured policies and restore workflows. Treat backup, retention, recycle-bin behavior, eDiscovery hold, and business continuity as different mechanisms. Define protected scope, retention/restore expectations, privileged roles, validation, and recovery evidence.

> **Related item:** Release preferences can expose selected users to changes earlier, but they are not a complete change-management system. Maintain test personas, communication, validation, support ownership, and rollback or mitigation plans.

### Workload administration

Exchange Online distinguishes user, shared, room/equipment, and other recipient types. A shared mailbox supports a team process and delegated access; it is not a normal shared user credential. Manage mailbox properties, permissions, forwarding, retention implications, and licensing requirements separately. For suspicious or failed mail flow, use message trace and Defender evidence rather than guessing from the inbox.

Teams combines a Microsoft 365 group, team membership, channels, meetings, apps, and linked SharePoint content. Standard, private, and shared channels have different membership and site behavior. Configure owners and members deliberately, preserve at least two accountable owners for important teams, and understand guest and external collaboration boundaries. Meeting policies govern capabilities such as transcription and recording; Copilot behavior in meetings depends on licensing, policy, meeting options, and the availability of transcript or other context. **VERIFY CURRENT:** meeting policy names and Copilot/transcription dependencies.

SharePoint sites, libraries, folders, files, groups, sharing links, and inheritance create the content-access graph used by people, search, Copilot, and agents. Manage site owners, members, visitors, external sharing, access requests, lifecycle, and sensitivity/container settings at the correct object. OneDrive is personal work storage governed by tenant controls, not a substitute for an owned team repository.

[SharePoint Advanced Management readiness guidance](https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management) emphasizes assessment, lifecycle, ownership, data access governance, restricted access, and restricted content discovery. Restricted Access Control narrows who can access a site even if other permissions or links exist. Restricted Content Discovery leaves direct site access unchanged but prevents site content from appearing in organization-wide search and Copilot/agent discovery for the restricted scenario. Neither is a reason to leave underlying permissions unmanaged.

Microsoft Search and [Microsoft Copilot Search administration](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience) can curate experiences such as acronyms and bookmarks. Search results remain security trimmed. Microsoft 365 Copilot connectors can bring external content into Microsoft Graph and search/Copilot experiences; administrators must govern connection identity, schema, permissions, crawl scope, update/delete behavior, ownership, and decommissioning.

### An operational troubleshooting sequence

For “Copilot cannot find the quarterly plan”:

1. verify the user and license, client/entry point, time, query, and expected source;
2. verify the source exists, is current, indexed or connected, and has a responsible owner;
3. verify the user can open the source directly and that encryption/permissions allow its use;
4. check whether Restricted Content Discovery, site exclusion, connector permissions, DLP, or other governance intentionally limits discovery;
5. compare with a controlled user and source;
6. inspect service health and current feature prerequisites;
7. fix the narrow failed layer and retest without granting broad access.

> **Related item:** Search visibility and direct authorization answer different questions. A resource can remain directly accessible while intentionally excluded from broad discovery; conversely, a search result does not grant permission to open its source.

---

## 2. Govern and secure Microsoft 365 tenants and workloads

### Identity lifecycle and delegated administration

Create, update, disable, and delete users with an accountable joiner-mover-leaver process. Separate account state, license removal, group membership, session revocation, mailbox/content preservation, ownership transfer, retention, and final deletion. Bulk operations through portals, CSV, Microsoft Graph, or PowerShell need scoped inputs, change evidence, error handling, and post-change verification.

Use security groups for authorization and policy targeting, Microsoft 365 groups for membership plus collaboration resources, and distribution groups for email distribution. Dynamic membership automates inclusion but can amplify an incorrect rule. Review rule logic, processing state, licensing, ownership, and the downstream permissions attached to the group.

External identities support collaboration without turning every guest into an internal account. Configure external collaboration and cross-tenant access intentionally; review sponsors, terms, access packages, group/team/site access, last activity, and removal. Contacts are directory/recipient objects, not authenticated workforce identities.

Microsoft Entra roles grant directory or service administration. Microsoft 365 and workload roles grant tasks in their owning services. Privileged Identity Management can make roles eligible and time-bound, requiring activation controls. Administrative units scope supported role assignments to subsets of directory objects. They are delegation boundaries, not generic network, licensing, or data-isolation containers.

Maintain least privilege, approval and notification for high-impact activation, audited emergency access accounts, separation between everyday and privileged identities, and periodic access reviews. Global Administrator is an exception path, not a default operating role.

### Authentication, Conditional Access, and risk

Authentication methods differ in phishing resistance, device dependency, recovery, and user experience. Prefer phishing-resistant methods where appropriate; control method registration; use Temporary Access Pass for bootstrapping rather than as a permanent credential. Self-service password reset requires correct scope, authentication methods, registration, writeback when hybrid reset is needed, and user support. Microsoft Entra Password Protection detects banned/common password patterns and can extend to on-premises AD DS with the required agents.

Conditional Access combines assignments (users/workload identities, resources, conditions) with access controls (block, MFA/authentication strength, compliant device, terms, session controls). Policies are cumulative. Build in report-only mode, exclude monitored emergency accounts, analyze impact, stage deployment, and confirm with sign-in logs. Identity Protection can contribute user or sign-in risk; a detection is evidence to investigate, not automatic proof of compromise.

Troubleshoot authentication in this order:

1. capture user, application/resource, UTC time, device, error, and correlation ID;
2. verify account state, entitlement, authentication-method registration, and workload access;
3. inspect sign-in logs and authentication details;
4. inspect every applied/not-applied Conditional Access policy and result;
5. inspect user/sign-in risk and remediation state;
6. reproduce with a controlled account and make the narrowest change;
7. preserve evidence and verify the intended and unintended paths.

> **Related item:** Authentication proves an identity; authorization permits an action. An MFA-successful user can still be correctly denied by Conditional Access, a SharePoint permission, a sensitivity-label encryption right, an agent audience, or a downstream tool.

### Defender for Office 365 and incident response

Defender for Office 365 layers anti-phishing, anti-spam, anti-malware, Safe Attachments, Safe Links, alerts, investigations, and response. Preset security policies provide Standard or Strict baselines; custom policies should have a documented requirement and priority. User submissions, quarantine, campaign views, Explorer/real-time detections, and message entity evidence help establish delivery, click, detonation, campaign, and remediation facts.

Start with the incident or alert and follow related users, mail, URLs, files, devices, applications, and activity. Determine scope before containing. Actions can include quarantining/remediating mail, blocking an indicator, disabling or protecting an account, revoking sessions, removing malicious inbox rules or application consent, isolating a device, and communicating with affected users. Preserve evidence and confirm the result.

Attack Simulation Training runs authorized simulations and education. Define learning goals, payload and technique, target population, privacy/communications, exclusion and help-desk plan, success measures, and follow-up training. Simulation metrics describe behavior in a controlled exercise; they are not a measure of individual worth or proof of compromise.

### Purview protection, lifecycle, and AI data security

Sensitive information types, trainable classifiers, exact data match, and document fingerprinting help identify content. Sensitivity labels classify and can protect supported content or containers. Publishing policy determines who sees labels and defaults/requirements; encryption rights can continue to control supported content beyond its original location.

DLP rules combine locations, conditions, exceptions, actions, user notifications, override/justification, and alerts. Design separately for Exchange, SharePoint, OneDrive, Teams, endpoints, Copilot, and supported AI locations because available conditions/actions differ. Begin in simulation, validate representative data and business processes, tune false positives, then enforce. DLP does not repair broad read permission by itself.

Retention policies and labels govern keeping and deleting content; Records Management adds record declaration, disposition, and stronger controls. Resolve conflicts using current Microsoft retention principles, legal obligations, and tested outcomes rather than an improvised “most recent policy wins” rule.

Microsoft Purview [Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) helps discover data/AI use, assess oversharing and risky activity, recommend protections, investigate incidents, and track posture. Use DLP alerts and DSPM evidence to find the identity, AI app/agent, source data, destination/action, applied policy, owner, and response. **VERIFY CURRENT:** the blueprint says DSPM and current documentation may distinguish current and classic AI-specific experiences.

Follow one governed file:

```text
classification → label/encryption → SharePoint permission/discovery
              → DLP decision → activity/alert → investigation
              → retention/record outcome → audit/eDiscovery evidence
```

Each control answers a different question. Classification says what data is; permissions say who can reach it; a label can protect it; DLP governs supported use; retention governs lifecycle; audit records activity; eDiscovery supports a matter.

---

## 3. Manage and secure AI services in Microsoft 365

### Copilot readiness and tenant controls

Microsoft 365 Copilot readiness includes eligible licensing, healthy identities and clients, network access, source permissions, SharePoint/OneDrive governance, information protection, adoption/support, and measurement. [Copilot architecture](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture) uses the signed-in user's context and Microsoft Graph-grounded organizational content within applicable permissions. “Copilot respects permissions” does not mean those permissions are correct.

Assess likely exposure before broad deployment. Find ownerless/inactive sites, organization-wide links, broad groups, broken inheritance, unlabeled sensitive data, and external sharing. Remediate the source, assign owners, narrow access, apply labels/DLP, and use temporary discovery restrictions only with a documented purpose. Test with least-privileged personas.

Tenant controls include Copilot license assignment, Copilot Chat and web search settings, self-service purchase, Copilot experiences in admin centers, release preferences, AI disclaimers, image/video generation, app settings, and supported third-party AI providers. [Microsoft Copilot app settings](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-admin-settings) and control names change frequently. **VERIFY CURRENT:** defaults, scope, licensing, role, portal, geography, and rollout state.

Copilot Cowork is an agentic work experience named in the beta objectives. Administer it through the same entitlement, identity, data, agent/tool, governance, and measurement chain rather than assuming it is merely another chat interface. Determine what it can plan or act on, which sources and tools it can reach, where human review occurs, and what evidence it records. **VERIFY CURRENT:** availability, licensing, entry point, supported actions, and admin controls.

Web grounding and work grounding have different data sources and governance implications. A web-search control does not change SharePoint permissions. Copilot Search administration can customize organization search while security trimming still applies. Treat generated output as a draft whose citations, facts, permissions, and downstream use require validation.

Microsoft describes [Copilot Control System](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/overview) as an integrated framework for security/governance, management controls, and measurement/reporting across Copilot and agents. Use it as an operating model, not as a single magic policy.

### Agent identity and access

An agent is an application/workload with owners, audiences, knowledge, instructions, tools, credentials, policies, usage, and lifecycle. [Microsoft Entra Agent ID administration](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin) gives supported agents a distinct identity type and separates an **agent identity blueprint** (the parent definition for a class of agents) from the individual agent identities created from it. Agent Registry answers which agents exist and how they are distributed; Entra Agent ID answers how an agent authenticates, what it can access, who is accountable for its identity, and when that access should end. Distinguish:

- the human user who requests an action;
- the agent identity represented and governed in the tenant;
- the builder/publisher/owner accountable for it;
- the tool or downstream service identity and permission;
- delegated/on-behalf-of access versus app-only autonomy.

On-behalf-of behavior remains bounded by the relevant user and application/tool grants. App-only or autonomous access can operate without the current user's resource permission and therefore requires tighter scope, credential protection, Conditional Access where supported, approval, monitoring, and revocation. An access package can bundle governed agent/resource access with request, approval, expiration, and review. Conditional Access for agent identities can enforce supported controls based on current capabilities. **VERIFY CURRENT:** supported identity types, policy targets, conditions, licensing, and enforcement limitations.

Operate the agent identity lifecycle as its own evidence chain:

1. **Discover and correlate:** match the registry record to its agent identity or blueprint; record object IDs, type, status, publisher, environment, and dependent tools.
2. **Establish accountability:** assign technical owners and an accountable human sponsor. Owners administer the artifact; sponsors make purpose, access, continuation, and retirement decisions.
3. **Bound access:** inspect granted permissions, prefer enumerated least-privilege scopes, use access packages for governed and expiring resource access, and evaluate Conditional Access in report-only mode before enforcement.
4. **Maintain sponsorship:** use supported Lifecycle Workflows mover/leaver tasks to notify the manager or cosponsors when sponsorship changes. Validate the new accountable sponsor; a notification alone does not transfer every business responsibility.
5. **Monitor:** review agent-filtered sign-in and audit logs, sponsor/owner state, access-package expiry, and risky-agent detections. Correlate the identity to the actual agent and tool invocation.
6. **Respond and retire:** disable the narrowest applicable layer, rotate compromised credentials, revoke access and consent, remove deployment, preserve required evidence, and verify that no child identity or dependent tool retains access. Blueprint- or tenant-wide disablement can affect many agents, so inventory blast radius first.

Do not assign a broad permission merely because an agent needs one operation. Define the minimum data set and actions, prefer read over write where possible, isolate high-impact tools, protect secrets/certificates/managed identities, and test negative paths. For each tool, document data read, action allowed, destination, identity used, consent model, owner, telemetry, emergency block, and dependency impact.

> **Related item:** Agent access and human access are connected but not identical. A user may be allowed to invoke an agent while the agent's tool is separately denied; conversely, an overprivileged app-only tool can exceed what the requesting user could do directly.

### Agent registry and lifecycle

The [Agent Registry lifecycle controls](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions?view=o365-worldwide) provide inventory and actions such as install/uninstall, block/unblock, delete, owner reassignment, and current workload-specific operations. The [Agent 365 overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide) surfaces requests, ownerless agents, risk, exceptions, inventory, and recent activity. Roles can differ between monitoring and governance actions.

Operate a lifecycle:

1. **Discover:** inventory existing, draft, requested, published, third-party, and unmanaged agents where supported.
2. **Assess:** verify publisher, business purpose, owner, knowledge, instructions, identity, tools, permissions, data flow, audience, cost, and support.
3. **Approve/publish:** choose allowed agent types, sharing settings, templates, user access, install/deploy scope, and conditions.
4. **Observe:** monitor usage, failures, cost, owner state, risk, data events, tool calls, exceptions, and user feedback.
5. **Respond:** block or uninstall, disable a risky tool, revoke grants/credentials, preserve logs, investigate data impact, and notify owners.
6. **Retire:** remove deployment and access, disable identity/tools, transfer or preserve required data/evidence, and verify dependencies.

Installation makes an approved agent available for selected users; publication makes it discoverable through a governed channel; sharing grants an audience; blocking affects supported use. These are not synonyms. Test the actual channel because a block can have product-specific limitations.

### Tenant agent settings and policy templates

The [Agent settings page](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide) controls the tenant boundary before an individual approval. **Allowed agent types** determines whether users can view and install Microsoft-built, organization-built, or external-publisher agents. **Sharing** determines who may share agents and how. **User access** determines which users or groups may use agents, but it does not grant source-data or tool permission. Treat external-publisher enablement as a data-processing and supply-chain decision, not merely a catalog preference.

[Agent 365 policy templates](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/policy-template) bundle supported controls from Entra, Purview, SharePoint, and Defender so new agent activations begin from a consistent baseline. Default templates can include audit, sensitive-information detection, AI compliance assessment, identity protection, lifecycle management, SharePoint access insights or restrictions, and Defender investigation. Custom templates can reference supported Entra Conditional Access, access-package, or custom-security-attribute policies under the documented roles and prerequisites.

For a template decision:

1. classify agent type, autonomy, data sensitivity, audience, external communication, and action impact;
2. select the smallest template that satisfies the risk tier and record any policies that still require configuration in their owning admin center;
3. confirm that the agent authenticates with the identity to which an Entra policy applies—assignment without runtime enforcement is not protection;
4. activate only to a pilot audience and test allowed, denied, sensitive-data, and failure paths;
5. record the template and policy versions with approval evidence;
6. reassess existing agents separately because current template changes and selections may apply only to new activations.

**VERIFY CURRENT:** template availability, Frontier/preview restrictions, licensing, default locked policies, supported agent types, and whether an update affects existing approvals.

### Agent tools, MCP servers, plugins, and skills

[Agent Tools administration](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-tools-for-agent?view=o365-worldwide) provides registry, request/approval, bring-your-own MCP server, plugin/skill, connector usage, and observation concepts. A tool gives an agent the ability to retrieve data or take action. MCP servers, connectors, plugins, and skills can package or expose those capabilities differently, but all need governance.

Review a tool before approval:

| Decision | Evidence to require |
|---|---|
| Purpose and owner | Supported business process, accountable owner, support and retirement plan |
| Trust | Publisher, provenance, code/service review, terms, data-processing location |
| Identity and permission | Delegated/app-only model, exact scopes/actions, secrets and rotation |
| Data path | Inputs, outputs, logging, retention, external destinations, DLP implications |
| Operational behavior | Availability, rate limits, retries, idempotency, failure modes, human confirmation |
| Response | Telemetry, alerting, emergency block, dependency inventory, rollback |

Blocking one shared tool can remove capability from every dependent agent. That is useful containment and a potential operational outage. Maintain dependency knowledge and an approved fallback. Reassess after scope, publisher, endpoint, permission, ownership, or behavior changes.

### Agent 365 security, compliance, cost, and monitoring

Use Defender, Purview, Entra, Agent 365, and workload evidence together. A suspicious agent incident may include anomalous sign-in, risky OAuth consent, sensitive source access, tool egress, DLP alert, agent action, user report, and downstream change. Correlate identity, agent, tool, session, source, action, destination, timestamp, and policy result.

[Microsoft Purview support for Agent 365](https://learn.microsoft.com/en-us/purview/ai-agent-365) distinguishes default onboarding from policies that still need explicit scope. Current Microsoft documentation says a new Agent 365 agent instance is automatically enabled for audit, sensitive-data detection through data classification, and AI-regulation assessments in Compliance Manager. Other supported capabilities—including sensitivity labels, DLP, Insider Risk Management, Communication Compliance, eDiscovery, and data lifecycle management—require the applicable agent instance to be included in policy as documented. Never infer full enforcement from the agent merely appearing in inventory.

Use this protection-and-gap workflow:

1. **Inventory:** reconcile Agent Registry and Entra identities with Purview DSPM **AI observability**; account for unsupported, inactive, third-party, and uninstrumented agents instead of treating missing telemetry as low risk.
2. **Classify exposure:** identify sensitive interactions, overshared grounding sources, external destinations, high-impact tools, autonomous access, and missing ownership.
3. **Map coverage:** for each agent type and interaction path, record whether audit, data classification, labels, DLP, retention, eDiscovery, risk policies, and Compliance Manager assessment apply automatically, require explicit inclusion, or are unsupported.
4. **Evaluate the gap:** inspect DSPM objectives/recommendations, AI activities, policy reports, audit evidence, and the applicable Compliance Manager AI assessment. A recommendation or improvement action is not proof of regulatory compliance.
5. **Protect:** correct source access, include the agent identity in supported policies, select an appropriate Agent 365 template, restrict tools or sharing, and assign an owner and exception expiry.
6. **Validate and sustain:** exercise a synthetic sensitive-data interaction and a denied path, confirm the expected activity/alert/audit evidence, rerun the assessment, and track residual gaps with owners and dates.

Contain at the narrowest effective layer: block the agent or tool, disable/restrict identity, revoke credentials/consent, remove deployment, protect the source, stop external sharing, quarantine affected content, or isolate a compromised endpoint. Preserve audit and investigation evidence. Then remove persistence, restore safe configuration, test negative and positive paths, and review why preventive or detective controls failed.

Cost controls require a billing model, owner, expected usage, budget/alert, allocation dimension, anomaly threshold, and response. Pay-as-you-go can enable services without a conventional per-user license; it is not “free” or ungoverned. Track consumption and forecast using current units and pricing, which can change.

[Copilot Control System measurement and reporting](https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-control-system/measurement-reporting) distinguishes operational reports for licensing, agents, deployment and usage from strategic adoption and business-value views. Usage is not value. Measure readiness, activation, active use, feature/agent success, failure, support demand, risk, cost, time or quality outcomes, and user sentiment against a baseline. Respect privacy and aggregation requirements.

Check Microsoft 365 service health for Copilot/agent incidents, but also inspect local license, policy, identity, data, tool, connector, and capacity dependencies. A healthy service does not prove the tenant configuration or third-party tool is healthy.

> **Related item:** An adoption dashboard can show that people used Copilot; it cannot by itself prove accuracy, safe use, productivity improvement, or business return. Pair activity with outcome, risk, cost, and quality measures.

---

## Integrated scenarios

### Scenario 1: Copilot surfaces a confidential plan

A pilot user receives a Copilot response citing a plan they should not need for their role. Do not begin by disabling Copilot for everyone. Preserve prompt/output/citation and timestamps, confirm the user can access the source directly, identify the site/file/link/group path, inspect label/encryption and DLP, and determine whether the authorization was legitimate but excessive. Remove broad access at the source, assign an owner, apply appropriate protection, review similar exposure, and retest with controlled identities. Restricted Content Discovery can be a temporary risk reduction, but it does not repair permission or ownership.

### Scenario 2: An agent requests a high-impact MCP tool

The agent needs to read customer cases and update resolution state. Require an owner, business purpose, data flow, exact read/write actions, delegated or app-only identity, approval conditions, error/idempotency behavior, telemetry, cost, and emergency block. Split read and write capabilities where supported, require human confirmation for destructive actions, scope to the minimum records, test unauthorized and duplicate requests, and document which agents depend on the server. Approve to a pilot audience; review activity before expansion.

### Scenario 3: Copilot adoption falls after a policy rollout

Correlate adoption time series with release, licensing, Conditional Access, client, network, DLP, SharePoint restrictions, and service-health changes. Segment by population and workload. Use sign-in logs, policy evaluation, support cases, usage reports, and test accounts. If the policy correctly blocks unmanaged devices, do not label lower usage an outage; provide a compliant path. If an unintended assignment blocks all pilot users, fix scope, validate both allowed and denied cases, and preserve the change record.

---

## Hands-on labs

Use a disposable developer/test tenant and synthetic data. Product licenses, preview access, and agent capabilities vary; document unavailable steps rather than weakening a production tenant.

### Lab 1 — Tenant and service operations

Inventory domains, subscriptions, license groups, administrative roles, release preferences, health/message-center responsibilities, and support contacts. Produce a RACI and one tested service-incident triage runbook. **Evidence:** sanitized inventory, role mapping, health-check record, and recovery/escalation decision.

### Lab 2 — Collaboration and Copilot-ready content

Create a test Team and SharePoint site with owners, members, visitors, and synthetic sensitive files. Test direct access, search/discovery, sharing, and permission inheritance with three personas. If available, inspect Advanced Management reports and a discovery restriction. **Evidence:** access matrix and before/after tests proving that discovery and authorization are distinct.

### Lab 3 — Identity lifecycle and delegated administration

Create test users/groups, group-based licensing, an administrative unit, and eligible privileged role if licensed. Run a mover and leaver sequence, including ownership and session decisions. **Evidence:** change log, failure/retry result, least-privilege rationale, and final access test.

### Lab 4 — Conditional Access and authentication support

Use report-only policy with a test population, protected resource, emergency exclusion, and explicit grant control. Capture sign-in evaluation, convert only after impact review, and test success/failure. **Evidence:** policy JSON/screenshots, sign-in details, rollback condition, and support flow.

### Lab 5 — Defender for Office 365 investigation

With safe simulation data, trace one alert or Attack Simulation event from message/campaign evidence through incident scope and response. **Evidence:** timeline, entities, containment choice, preserved evidence, and post-response verification. Never send an unapproved phishing simulation.

### Lab 6 — Purview policy design for AI data

Define synthetic sensitive information, a label, and a DLP scenario covering a collaboration and supported AI channel. Begin in simulation, test true/false positives and user notification, then document enforcement criteria. **Evidence:** requirement-to-rule map, test cases, alerts/activity, exception owner, and rollback.

### Lab 7 — Agent and tool approval

Model an agent with owner, accountable sponsor, audience, agent identity or blueprint, knowledge, and one read tool plus one write tool. Reconcile its registry and Entra records, define an access-package expiry or equivalent review point, and tabletop a sponsor leaver, risky sign-in, narrow disablement, and retirement. Complete the approval table above, test negative paths and human confirmation, and record dependency-aware block steps. If Agent 365 or Agent ID is unavailable, use an architecture worksheet and current official documentation. **Evidence:** identity correlation, owner/sponsor record, threat/data-flow model, permission matrix, dependency map, lifecycle event log, and go/no-go decision.

### Lab 8 — Agent 365 policy and Purview gap assessment

In a disposable tenant, select a harmless agent and synthetic sensitive data. Compare tenant allowed-type, sharing, user-access, and template settings; then build a matrix for audit, classification, labels, DLP, DSPM AI observability, retention, eDiscovery, and Compliance Manager. Use simulation or tabletop evidence where a license or preview is unavailable. Do not broaden production access to make a test pass. **Evidence:** selected template and versions, automatic-versus-explicit coverage matrix, synthetic allowed/denied results, activity or expected-event record, residual-gap owner, and rollback.

### Lab 9 — AI operations dashboard

Design a dashboard covering license/activation, active use, agent/tool success and failure, support cases, DLP/security events, spend, ownerless agents, and one business outcome. Define sources, aggregation/privacy, thresholds, owners, and response. **Evidence:** sample dashboard and an anomaly runbook that distinguishes service, tenant, and tool failures.

---

## Knowledge checks

1. **Does a Copilot license grant access to SharePoint content?** No. Entitlement enables service use; resource permissions and protection still govern content.
2. **What does domain verification prove?** Control of the DNS namespace, not completion of mail, identity, or application migration.
3. **Service Health is green but one user fails. Where do you start?** Capture the exact user, app, time, device, error/correlation ID, entitlement, sign-in and policy evidence.
4. **Why keep multiple accountable Team/site owners?** To reduce ownerless resources and support membership, lifecycle, recovery, and governance.
5. **Restricted Access Control versus Restricted Content Discovery?** The first narrows site access; the second limits broad discovery while leaving direct permissions unchanged.
6. **Does removing a license complete a leaver process?** No. Account, sessions, groups, data, ownership, retention, mailbox, and deletion are separate decisions.
7. **When is an administrative unit useful?** To scope supported directory role administration to a subset of objects.
8. **What is the safest Conditional Access rollout?** Explicit assignments and exclusions, report-only evidence, controlled pilot, validation, then staged enforcement.
9. **What does a risk detection establish?** A signal requiring investigation, not proof of compromise.
10. **Why inspect every applied Conditional Access policy?** Policies combine; the visible symptom may come from another policy or session control.
11. **Preset versus custom Defender policy?** Use a supported baseline where possible; create custom priority/scope only for a documented requirement.
12. **What should an attack simulation measure?** Authorized learning goals and behavior with privacy, support, and follow-up—not punishment.
13. **Sensitivity label versus DLP?** A label classifies and can protect; DLP evaluates supported use and applies rule actions.
14. **Retention versus backup?** Retention governs content lifecycle/compliance; backup supports recovery. Neither automatically replaces the other.
15. **Why is Copilot exposure often a permission problem?** AI can make content already accessible to a user easier to retrieve and summarize.
16. **Should DLP replace least privilege?** No. It governs supported data activity after access exists.
17. **What should precede broad Copilot deployment?** License/client/network readiness, source permission and ownership review, data protection, support, pilot, and measurement.
18. **Does turning off web search change work-data permission?** No. Web grounding and organizational authorization are separate controls.
19. **What identifies an agent operationally?** Owners, identity, audience, knowledge, instructions, tools, permissions, policy, usage, cost, and lifecycle.
20. **Delegated versus app-only tool access?** Delegated acts within applicable user and app grants; app-only can act without a current user's resource authorization.
21. **Why govern tools separately from agents?** A tool defines data and actions and can be shared by many agents.
22. **What should an MCP approval include?** Owner, trust, exact actions/scopes, identity, data path, failures, telemetry, dependency and emergency block.
23. **What is the consequence of blocking a shared tool?** It can contain risk across every dependent agent and simultaneously cause an outage.
24. **Install, publish, share, and block—same operation?** No. They address deployment, discoverability, audience/access, and supported execution respectively.
25. **What should happen to an ownerless production agent?** Assign accountable ownership promptly or restrict/retire it after impact review.
26. **What is the minimum incident correlation for an agent?** Human/user, agent identity, tool, session, source, action, destination, time, and policy result.
27. **Why test negative paths?** A successful intended action does not prove unauthorized or destructive actions are blocked.
28. **What makes pay-as-you-go governable?** Billing owner, expected units, budget/alerts, allocation, anomaly response, permissions, and service controls.
29. **Usage versus value?** Usage shows activity; value requires an outcome and baseline, with quality, risk, and cost considered.
30. **What does a healthy Microsoft service fail to prove?** That local licensing, policy, identities, connectors, agents, tools, and data are healthy.
31. **Why preserve incident evidence before remediation?** To determine scope/root cause and support audit, legal, recovery, and control improvement.
32. **What should a beta candidate recheck?** Objectives, exam status/language, product names, portals, licensing, defaults, and assessment availability.
33. **Can a search result grant file access?** No. Search is security trimmed and resource authorization remains decisive.
34. **Why use synthetic lab data?** To test governance and response without exposing production or regulated information.
35. **What is the best response to one Copilot oversharing citation?** Fix and verify source authorization/ownership/protection, assess similar exposure, and use narrow temporary containment if required.
36. **What proves an administrative change worked?** A controlled positive and negative test plus logs/reports showing intended scope and no unacceptable side effects.
37. **Owner versus sponsor for an agent identity?** The owner handles technical administration; the sponsor is accountable for purpose, continued access, and lifecycle decisions.
38. **Does an Agent 365 policy template prove enforcement?** No. Verify prerequisites, target identity, runtime authentication, owning-service configuration, activation scope, and allowed/denied outcomes.
39. **Which Purview controls are automatic for a new Agent 365 instance?** Current documentation identifies audit, data-classification detection, and inclusion in AI-regulation assessments; verify the current product and explicitly scope other supported policies as required.
40. **How do you find an Agent 365 compliance gap?** Reconcile inventory with AI observability, map every interaction to supported policies and evidence, inspect DSPM and Compliance Manager recommendations, test, and assign residual risk.

---

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary route that fits how you learn, build labs around weak objectives, and use assessments to diagnose gaps. Recheck dates and coverage because AB-650 and several Agent 365 features are beta or rapidly changing.

### Official primary route

- [Configure and manage Microsoft 365 tenants and workloads](https://learn.microsoft.com/en-us/training/paths/configure-manage-microsoft-365-tenants-workloads/) — 7 hours 2 minutes listed.
- [Govern and secure Microsoft 365 tenants and workloads](https://learn.microsoft.com/en-us/training/paths/govern-secure-microsoft-365-tenants-workloads/) — 7 hours 39 minutes listed.
- [Manage and secure Microsoft 365 AI services](https://learn.microsoft.com/en-us/training/paths/manage-secure-microsoft-365-ai-services/) — 8 hours 27 minutes listed.
- Combined official video/reading time is **23 hours 8 minutes**; allow roughly **35–55 hours** with notes, portal exploration, labs, and remediation.
- Use the [AB-650 credential page](https://learn.microsoft.com/en-us/credentials/certifications/ai-services-administrator-associate/) for beta status, scheduling, exam sandbox, language, and assessment availability. Microsoft had not published a Practice Assessment as of September 1, 2026.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official AB-650 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-650) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/ai-services-administrator-associate/) | Public | 1–2 hours initially; 15 minutes on each beta recheck |
| Three official Microsoft Learn paths | Public | 23 hours 8 minutes listed; allow about 35–55 hours with labs, notes, and remediation |
| Exam sandbox from the credential page | Public | 20–40 minutes; not a knowledge assessment |
| [Microsoft 365 Copilot documentation](https://learn.microsoft.com/en-us/microsoft-365-copilot/) and [Microsoft Agent 365 documentation](https://learn.microsoft.com/en-us/microsoft-agent-365/) | Public | 6–15 hours selectively for current behavior and limitations |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics) | Public | 2–6 hours selectively; no exact AB-650 path confirmed |
| [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor) | Public | 2–8 hours selectively; no exact AB-650 path confirmed |
| [John Savill's Technical Training](https://www.youtube.com/@NTFAQGuy) and [public repositories](https://github.com/johnthebrit) | Public | 2–8 hours selectively for identity, security, and architecture foundations |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use the event's published start/end time after sign-in |

### Complementary sources

- [Microsoft 365 Copilot documentation](https://learn.microsoft.com/en-us/microsoft-365-copilot/) and [Microsoft Agent 365 documentation](https://learn.microsoft.com/en-us/microsoft-agent-365/) — allow 6–15 hours selectively for current controls, limitations, and release changes.
- [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics) — allow 2–6 hours selectively for official product demonstrations; no fixed AB-650 course was confirmed.
- [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor) — allow 2–8 hours selectively for Microsoft 365, security, Copilot, and agent sessions; verify each video's date and objective fit.
- [John Savill's Technical Training](https://www.youtube.com/@NTFAQGuy) and [public whiteboard/code repositories](https://github.com/johnthebrit) — allow 2–8 hours selectively for Entra, security, identity, and architecture foundations; no complete AB-650-specific course was confirmed.
- [Partner Skilling Hub](https://www.skilling-hub.com/en-US) — Microsoft partner sign-in is required to confirm current AB-650 events and their start/end times; plan for the published live session length plus lab/review time.

No exact current AB-650 course or practice-exam page from Pluralsight, O'Reilly, Udemy, Whizlabs, or MeasureUp was independently verified during this review. Do not infer beta-exam coverage from a general Microsoft 365 Copilot course, and avoid products claiming real exam questions. Use the official blueprint as the coverage checklist.

## Final readiness checklist

- I can map every published subobjective to a configuration, evidence source, failure mode, and recovery action.
- I can distinguish license, authentication, Conditional Access, workload permission, data protection, agent audience, and tool authorization.
- I can operate domains, licenses, service health, Exchange, Teams, SharePoint, Search, Backup, Entra, Defender, and Purview at the expected scope.
- I can explain and demonstrate Copilot readiness without treating AI as a permission bypass.
- I can govern an agent from discovery and approval through monitoring, incident response, and retirement.
- I can correlate Agent Registry, Agent ID blueprint and identity records, owners, sponsors, access, sign-ins, lifecycle workflows, and disablement scope.
- I can configure allowed agent types, sharing, user access, and risk-based policy templates without confusing them with data or tool authorization.
- I can use Purview AI observability and Compliance Manager evidence to find, remediate, and retest Agent 365 protection and compliance gaps.
- I can assess MCP servers/connectors/plugins/skills by identity, actions, data flow, ownership, observability, and emergency response.
- I can interpret cost, usage, adoption, service-health, audit, DLP, and security signals without confusing activity with value or proof.
- I have rechecked the beta blueprint and credential page immediately before scheduling.
