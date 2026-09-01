---
exam_code: SC-401
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# SC-401 Administering Information Security in Microsoft 365 Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#sc-401-coverage-record). The [official SC-401 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) is authoritative.

**Current baseline:** Skills measured as of July 28, 2026.<br>
**Exam state:** Active; the credential page lists no retirement date.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Practice Assessment:** [Free official assessment](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/practice/assessment?assessment-type=practice&assessmentId=1801497482&practice-assessment-type=certification).<br>
**Official source:** [SC-401 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)

## How to use this guide

SC-401 tests operational data protection, not the ability to recognize portal names. For each requirement, identify the data, classifier, control, location, user or device experience, evidence, exception path, and recovery action. Practice proving both a match and a safe nonmatch; a policy that blocks everything is as poorly designed as one that detects nothing.

Use this chain throughout the guide:

```text
data and business requirement
  -> classifier, label, user/device, location, and risk context
  -> preventive or detective policy and precedence
  -> simulation, rollout, exception, and user experience
  -> alert, audit, investigation, retention, and recovery evidence
```

Read Sections 1–3, work all three integrated scenarios, complete or tabletop the eight labs, and answer the 36 original checks. Use a disposable Microsoft 365 developer or lab tenant with synthetic data. Purview, Microsoft 365 E5, Defender for Cloud Apps, Defender for Endpoint, OCR, Audit Premium, Insider Risk Management, forensic evidence, and AI security capabilities can require specific licenses, billing, roles, supported clients, and tenant configuration. Verify those prerequisites before a lab and remove test policies afterward.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

The certification is intermediate. Microsoft expects familiarity with Microsoft 365 services, PowerShell, Microsoft Entra, Microsoft Defender XDR, and Microsoft Defender for Cloud Apps. The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/) lists a 100-minute exam and annual renewal.

| Official domain | Weight | Operating question |
|---|---:|---|
| Implement information protection | 30–35% | How is sensitive data discovered, classified, labeled, encrypted, and protected across cloud, endpoint, on-premises, and email boundaries? |
| Implement data loss prevention and retention | 30–35% | How are risky actions controlled while required content is retained, disposed of, found, and recovered? |
| Manage risks, alerts, and activities | 30–35% | How are insider and AI-related data risks detected, investigated, evidenced, and reduced without bypassing privacy or due process? |

### Published objective-to-guide map

| Published objective area | Primary coverage | Practice evidence |
|---|---|---|
| Requirements, sensitive information types, fingerprinting, EDM, classifiers, explorers, and OCR | Section 1 | Scenarios 1 and 3; Labs 1–2 |
| Sensitivity-label roles, items, containers, protection, publishing, auto-labeling, and Defender for Cloud Apps | Section 1 | All scenarios; Labs 2–3 |
| Information Protection client/scanner, file operations, Message Encryption, and Advanced Message Encryption | Section 1 | Scenario 1; Labs 3–4 |
| DLP design, roles, policies, Adaptive Protection, precedence, and Cloud Apps file policies | Section 2 | All scenarios; Lab 5 |
| Endpoint prerequisites, advanced rules, settings, just-in-time protection, and activity monitoring | Section 2 | Scenarios 2–3; Lab 6 |
| Retention labels/policies, adaptive scopes, auto-apply, precedence, Policy lookup, disposition, and recovery | Section 2 | Scenarios 1–2; Lab 7 |
| Insider Risk roles, connectors, Defender integration, settings, indicators, templates, policies, forensic evidence, risk levels, alerts, cases, and notices | Section 3 | Scenario 2; Lab 8 |
| Audit licensing/search/retention, Activity explorer, DLP/insider/XDR/Cloud Apps alerts, and eDiscovery | Section 3 | All scenarios; Labs 5 and 8 |
| Purview and workload controls for AI plus DSPM prerequisites, roles, policies, and monitoring | Section 3 | Scenario 3; Labs 2, 5, and 8 |

## 1. Implement information protection

### Translate a business requirement into a classifier

Begin with an inventory: data owner, business purpose, locations, formats, jurisdictions, minimum detection quality, protection action, retention requirement, permitted sharing, exceptions, and evidence. “Find personal data” is incomplete until the team defines which records, acceptable false positives and false negatives, where detection must work, and what happens on a match.

Choose the smallest appropriate classifier:

| Classifier | Strong fit | Design and test concerns |
|---|---|---|
| Built-in sensitive information type (SIT) | Common regulated identifiers with maintained patterns and validation | regional variants, confidence, proximity, supporting evidence, false positives |
| Custom pattern-based SIT | Organization-specific structured identifiers | regex, keyword lists/dictionaries, primary/supporting elements, proximity and confidence |
| Document fingerprint | Completed instances of a standard form or template | representative blank form, text variability, threshold and template versioning |
| Exact Data Match (EDM) SIT | Exact or near-exact values from an authoritative data table | schema, primary/supporting fields, normalization, salted hashes, refresh and access to source data |
| Trainable classifier | Semantic category best learned from positive and negative examples | representative examples, privacy, training/testing split, retraining and match feedback |
| OCR-assisted classification | Sensitive text embedded in supported images and scanned content | supported locations/types/languages, billing, latency, image quality and client behavior |

A custom SIT pattern combines a primary element with optional supporting evidence inside a proximity window and assigns a confidence. Tight evidence raises precision but may lower recall. Test known positive, negative, malformed, localized, boundary, duplicate, and image samples. Record the classifier version and expected result so an update can be regression-tested.

Document fingerprinting learns the structure of a form; it is not an image hash and does not mean only byte-identical documents match. EDM uses an uploaded schema and hashed data so organization-specific values can be found more precisely than generic pattern matching. Protect the source dataset, choose primary fields that are sufficiently unique, normalize consistently, monitor upload status, and retest after source or schema changes. Microsoft's [EDM overview](https://learn.microsoft.com/en-us/purview/sit-learn-about-exact-data-match-based-sits) and [document-fingerprinting guide](https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting) document the different matching models.

Trainable classifiers recognize categories such as business or behavioral content using examples. Use only appropriately governed examples; validate on content the model did not train on and review matched items before using the classifier for irreversible action. OCR extends supported classifiers into supported image content and can add pay-as-you-go and location/client dependencies. **VERIFY CURRENT** against the [OCR documentation](https://learn.microsoft.com/en-us/purview/ocr-learn-about).

Data Explorer aggregates classification and label insights; Content Explorer lets sufficiently privileged reviewers inspect matched items. Activity Explorer focuses on events and actions. These are different evidence planes. Scope roles narrowly, account for indexing latency, verify coverage, and never treat an empty dashboard as proof that sensitive data does not exist.

> **Related item:** Precision is the share of matches that are correct; recall is the share of relevant content that the classifier found. A narrow classifier can look accurate while silently missing most sensitive data. Use a labeled test corpus to measure both.

### Design and operate sensitivity labels

A label communicates classification and can enforce protection. Define a simple taxonomy from business language, with an owner, examples, handling expectations, scope, protection settings, and review date. Separate labels for items (files/emails), containers (Teams, Microsoft 365 Groups, SharePoint sites), meetings/chats where supported, and data assets where supported; a similarly named label does not necessarily apply the same controls everywhere.

Item-label settings can include encryption, access restrictions, expiry/offline access, content marking, and user permissions. Container labels govern supported container settings such as privacy, external sharing, unmanaged-device access, or authentication context; they do not automatically label or encrypt every file already in the container. Power BI label propagation and enforcement also depend on supported paths and tenant settings. **VERIFY CURRENT** in the [sensitivity-label documentation](https://learn.microsoft.com/en-us/purview/sensitivity-labels).

Publishing policies determine who sees which labels and can configure defaults, mandatory labeling, downgrade justification, email inheritance, and other supported user experiences. Label priority and policy priority matter. Deploy to a pilot group, verify Office, web, mobile, email, SharePoint, Teams, and Power BI behavior as applicable, then widen scope. Give service desks a decision tree for protected content, external recipients, label mismatch, and lost access.

For auto-labeling, start in simulation, inspect matched and unmatched items, tune classifiers and scope, then enable. Client-side recommendations or automatic application and service-side auto-label policies have different execution locations, supported conditions, timing, and licensing. Record when protection becomes effective and how existing content is handled.

Microsoft Defender for Cloud Apps can inspect supported cloud-app files and apply governance actions or sensitivity labels. Confirm connector, app, file, ownership, label, encryption, and API limitations. A Cloud Apps file policy complements Purview label and DLP controls; it does not make every third-party SaaS action equivalent to a Microsoft 365 workload.

> **Related item:** Labels and DLP answer different questions. A label describes and may protect an item; DLP evaluates content, context, location, identity, device, and attempted action. Use both when classification must travel with data and risky movement must be controlled.

### Protect Windows, on-premises repositories, and email

The Microsoft Purview Information Protection client integrates labeling into supported Windows and Office experiences and provides file-management capabilities. Plan supported application versions, authentication, policy publishing, scanner needs, coexistence with legacy Azure Information Protection components, deployment/update method, logging, and rollback. Test interactive, automated, offline, and external-recipient behavior.

The Information Protection scanner extends discovery, classification, labeling, and supported DLP enforcement into on-premises file shares and SharePoint repositories. Design the scanner cluster, service identity, content-scan job, repositories, database, network access, policies, file-type handling, discovery/enforcement mode, schedules, logs, and remediation. Begin in discovery, establish the false-positive and access-denied baselines, then enable actions. A scanner that cannot read a repository does not prove that it contains no sensitive data.

Message Encryption protects supported mail using rights-management and transport/policy integration. Design who can decrypt, whether forwarding/printing/copying is allowed, external-recipient authentication, branding, transport rules, label integration, revocation, expiry, and journaling/eDiscovery needs. Advanced Message Encryption adds supported expiry/revocation and branding capabilities under qualifying licensing; verify which messages and recipient experiences support each action. Encryption controls use after delivery but does not correct a message sent to the wrong authorized recipient.

> **Related item:** Encryption, DLP, retention, and eDiscovery can all apply to one message. Test the full lifecycle—send, external access, forward attempt, audit, search, hold/retention, revoke, expire, and recover—instead of validating each feature alone.

## 2. Implement data loss prevention and retention

### Build DLP from the attempted action backward

Define the protected data, locations, users/groups, devices, applications, actions, severity, user guidance, business-justification path, incident evidence, responders, and exceptions. Purview DLP spans supported Exchange, SharePoint, OneDrive, Teams, endpoint, Power BI, Fabric, and other locations; conditions and actions vary by location. Confirm current support rather than assuming that a rule copied between locations behaves identically.

A DLP policy contains scoped rules with conditions, exceptions, actions, user notifications, policy tips, incident reports, alerts, and mode. Policy priority, rule priority, stopping behavior, and the most restrictive applicable outcome can all affect a transaction. When results surprise you, capture the content/classifier, location, identity, device, matching rules, priority, mode, action, and audit event. Use simulation first, tune, notify with policy tips, then restrict in stages.

Role separation matters: policy authors, investigators, content viewers, and global administrators do not need identical access. Use Purview role groups and administrative units where supported, document emergency access, and test the exact persona.

Adaptive Protection connects Insider Risk Management risk levels to preventive controls such as DLP and supported Conditional Access actions. Risk levels are not the same as alert severity. Define the insider-risk policy, user scope, thresholds, risk-level duration, DLP rule behavior, privacy controls, exception/appeal, and evidence. A dynamic block without a human workflow can disrupt legitimate high-volume work.

Defender for Cloud Apps file policies can inspect files in connected applications and apply supported governance, including DLP inspection. Validate API connector coverage, scan scope, existing-file behavior, quarantine/governance action, ownership, alert routing, and remediation. **VERIFY CURRENT** because supported apps and actions change.

> **Related item:** A policy tip is a control interaction, not proof of prevention. Capture whether the user saw it, could override it, supplied justification, completed the action, and produced an alert.

### Implement and monitor Endpoint DLP

Endpoint DLP requires eligible licensing, supported operating systems, device onboarding, connectivity, and supported browser/client extensions for some activities. Establish device groups, printer and removable-media groups, service domains, network-share groups, unallowed apps, browser restrictions, and evidence before advanced rules. The [Endpoint DLP overview](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about) is the current capability boundary.

Advanced endpoint rules can evaluate activities such as copy to removable media or network share, print, clipboard, RDP, Bluetooth, and upload to restricted cloud/service domains, subject to platform support. Configure audit, warn, block with override, or block according to risk. Include file path, application, browser, domain, device/user group, classifier/label, and exclusion logic. Test supported and unsupported clients: a browser extension or onboarded-device dependency can create a blind spot that a portal policy alone does not reveal.

Just-in-time protection provides temporary protective handling while policy evaluation catches up for newly created or changed content. Decide whether the environment should audit or block while classification is pending, account for user impact and supported files/activities, and monitor results. **VERIFY CURRENT** before deployment because behavior and prerequisites are fast-moving.

Use Activity Explorer, DLP alerts, device timeline, audit records, and local/client evidence to answer: what activity occurred, on which data, under which rule, from which app/device, what action was taken, whether override occurred, and whether the event reached the response workflow. Tune using real false-positive and false-negative evidence, not only alert volume.

### Design retention and recovery deliberately

Retention is not backup. A retention policy applies one set of retain/delete settings to supported locations. A retention label applies settings at item or record level and can support event-based retention, disposition review, proof of disposition, and regulatory records depending on configuration and licensing. Use a policy for broad location-level coverage; use labels when content needs differentiated, item-level lifecycle behavior.

Define the trigger, duration, start-of-retention event, retain/delete action, immutable or record behavior, disposition reviewer, conflict rule, exception, deletion path, recovery requirement, and legal/eDiscovery relationship. Static scopes enumerate users/sites/groups; adaptive scopes use attributes and queries to update membership. Validate scope membership and delay before assuming content is covered.

Publishing makes labels available for manual/application use; auto-apply finds qualifying content using supported conditions. Both are asynchronous. Retention-policy and label precedence resolves conflicting settings, generally favoring retention over deletion and longer retention over shorter retention in applicable conflicts, with explicit label behavior significant. Do not rely on a slogan: use Policy lookup for the item/location and confirm Microsoft's current rules.

Recovery depends on workload and retention state. Retained Exchange, SharePoint, or OneDrive content can be preserved in hidden recovery locations while users no longer see it. Know the supported restore/search route, permissions, time window, version behavior, and what happens after permanent deletion or retention expiry. Run a timed delete-and-recover test and preserve the evidence.

> **Related item:** A legal hold responds to a matter; a retention schedule enforces ordinary lifecycle. They can coexist, but neither substitutes for a tested backup/restore design or a documented disposition decision.

## 3. Manage risks, alerts, and activities

### Operate Insider Risk Management with privacy controls

Insider Risk Management combines signals, policy templates, analytics, alerts, cases, and response workflows. It does not establish intent or guilt. Create the program with legal, HR, privacy, security, compliance, and workforce stakeholders; define purpose, scope, minimization, pseudonymization, separation of duties, notice, access logging, evidence retention, escalation, and appeal.

Choose a template from the risk scenario and available trigger. Configure users/groups, triggering events, indicators, sequences, thresholds, priority content/users, exclusions, detection window, and alert volume. Connect supported HR, physical-security, healthcare, or other data only when lawful, necessary, secured, and monitored. Defender for Endpoint integration adds supported device signals; verify onboarding, licensing, data flow, and privacy.

Use analytics to estimate activity and tune policy before full activation. An alert aggregates potentially risky activity; a case is an investigator-controlled record for triage and action. Validate identity reveal permissions, activity context, false positives, linked evidence, case notes, escalation, and closure. Notice templates enable a governed user communication workflow but do not replace an organization's HR/legal process.

Forensic evidence can capture visual evidence from selected endpoint activity. Treat it as highly sensitive surveillance data. Require explicit authorization, narrow scope, role separation, secure reviewer access, retention, audit, employee/privacy review, and tested disablement. Never enable it merely to complete a lab in a real workforce tenant.

Adaptive Protection maps configured insider-risk evidence to Minor, Moderate, or Elevated risk levels, which supported preventive controls can consume. Define expiration and reset behavior, policy actions, monitoring, and a recovery/escalation path. Microsoft's [Adaptive Protection documentation](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) distinguishes risk levels from alert severity.

> **Related item:** The same activity may be a DLP event, an insider-risk indicator, an Audit event, and a Defender XDR alert. Correlate by user, device, item, time, policy, and action; duplicate records are not four independent incidents.

### Investigate alerts and activity with the correct evidence plane

| Evidence or workflow | Best use | Important boundary |
|---|---|---|
| Purview Audit | Search who did what, where, and when across supported Microsoft 365 and AI activity | event availability, license, audit retention, workload schema and search time |
| Activity Explorer | Analyze classification, label, DLP, endpoint, and supported AI events | visibility depends on role, event ingestion, filter, and retention |
| DLP alert | Triage a policy match and attempted action | alert aggregation/severity differs from raw events and policy tips |
| Insider-risk alert/case | Investigate user-centric risk indicators under privacy workflow | activity is a signal, not a conclusion; identity visibility is controlled |
| Defender XDR incident/alert | Correlate supported Purview signals with security incidents | not every Purview event becomes an XDR alert |
| Defender for Cloud Apps alert | Respond to connected-app file-policy and governance activity | API/app/action coverage differs from Microsoft 365 workloads |
| eDiscovery search | Find and preserve/export matter-relevant content under a case | case role, custodian/source, query, hold, review, export and audit requirements |

Audit Standard and Audit Premium differ in supported retention, investigation capabilities, and licensing. Assign eligible user licenses for Premium features, configure audit-retention policies by workload/user/record type/priority and duration, then test that a known event is searchable. Audit retention is not content retention.

Begin an investigation with an incident question and time range. Preserve alert and policy versions, user/device/item identifiers, workload, correlation IDs, raw audit events, actions, override/justification, and chain of custody. Search broadly enough to find related activity but minimize exposed data. Do not change or rerun the policy before preserving transient evidence.

Use eDiscovery for a governed content search: create/use the correct case, assign minimal roles, identify custodians and noncustodial sources, construct and validate the query, estimate/test results, preserve through holds when authorized, review/export securely, and audit every action. The current [eDiscovery overview](https://learn.microsoft.com/en-us/purview/ediscovery) is authoritative because portal and feature boundaries change.

### Protect data used by AI services

AI does not create a separate copy of the authorization model. Microsoft 365 Copilot and agents can surface content a user can already access, so oversharing, stale access, broad links, weak labels, missing DLP, and poor retention become AI-readiness risks. Reduce the reachable data first through permissions, access governance, SharePoint controls, labels, DLP, retention, audit, and eDiscovery; then validate prompts, responses, citations, plugins/connectors, agents, and sharing with test identities.

Purview controls can classify and label files/emails, apply DLP to supported Microsoft 365 and endpoint interactions, detect risky AI-site use, preserve/search AI activity, and provide investigation signals. Workload controls in SharePoint, Teams, Exchange, OneDrive, Power Platform, Copilot Studio, and agent administration govern what can be reached or shared. Confirm the exact workload and license: “protected by Purview” is not a universal statement across every model, prompt, agent, connector, browser, or third-party AI service.

Microsoft's current documentation distinguishes the newer [Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about) experience from DSPM and DSPM for AI **classic**. The July 2026 objective still says “DSPM for AI.” **VERIFY CURRENT** portal names, roles, prerequisites, default policies, supported AI applications/agents, assessments, and reports before practicing.

For DSPM, establish Purview permissions, classification/labels, audit/activity collection, relevant DLP and insider-risk foundations, supported workload onboarding, and optional Security Copilot prerequisites. Separate Data Security Viewer and administrative duties where supported. Review discovered sensitive data, oversharing, risky AI interaction, policy coverage, recommendations, assessments, alerts, and remediation; validate a recommendation before automating it.

For third-party generative AI accessed from endpoints, supported Endpoint DLP and browser controls can audit, warn, or block sensitive prompts/uploads. Test browser, domain, unmanaged application, copy/paste, file upload, label/classifier, override, and event flow. A blocked website in one browser is not proof that native clients, APIs, personal devices, or unsanctioned proxies are controlled.

> **Related item:** AI data security needs both an access question (“could this user or agent retrieve the item?”) and a use question (“could the item be pasted, uploaded, summarized, shared, or retained here?”). Permissions address the first; workload, Purview, endpoint, and AI governance controls address the second.

## Integrated scenarios

### Scenario 1 — Product designs across cloud, file shares, and email

Create a label taxonomy for product designs, a custom SIT/fingerprint for the standard design form, and an on-premises scanner discovery job. Publish labels to engineers, simulate auto-labeling, and encrypt external email to approved suppliers. Add DLP and retention without breaking approved collaboration. Prove positive/negative classification, label/container behavior, supplier access, scanner failures, audit, search, disposition, and recovery.

### Scenario 2 — Departing employee and high-volume downloads

An authorized HR signal triggers an insider-risk policy and Defender for Endpoint contributes device activity. Tune indicators and thresholds, protect priority content, map risk levels to staged DLP actions, and configure Endpoint DLP for removable media, print, browser upload, and network share. Preserve privacy and forensic-evidence approvals. Investigate the alert/case across Purview, XDR, Audit, and eDiscovery, then document closure and access to evidence.

### Scenario 3 — Generative AI rollout with sensitive client records

Inventory client data and overshared sites, implement EDM plus labels, simulate service and Endpoint DLP, and establish current DSPM prerequisites/roles. Test Microsoft 365 Copilot/agent access with least-privileged personas and a supported third-party AI site through managed browsers. Monitor prompts/uploads and alerts, validate remediation, preserve required AI activity, and prove that an unsupported client remains a documented gap rather than a hidden assumption.

## Hands-on labs

### Lab 1 — Classification regression corpus

Create synthetic positive, negative, boundary, localized, and malformed examples for a built-in and custom SIT, fingerprint, EDM design, classifier design, and OCR sample. **Evidence:** expected-versus-actual matrix, precision/recall notes, version, and tuning decision.

### Lab 2 — Explorer and AI data inventory

Seed synthetic labeled and unlabeled content, wait for indexing, and compare Data Explorer, Content Explorer, Activity Explorer, and current DSPM visibility using restricted personas. **Evidence:** coverage/latency map, permissions, blind spots, and remediation backlog.

### Lab 3 — Label and container rollout

Build item and container labels, protection/content marking, publishing, defaults, downgrade justification, and simulated auto-labeling. Test Office, SharePoint/Teams, Power BI or documented equivalent, external users, and Cloud Apps where licensed. **Evidence:** allow/deny/use matrix and rollback.

### Lab 4 — Scanner and encrypted mail

Design or deploy a scanner against synthetic file shares in discovery then enforcement mode. Configure a test encryption rule/label and external recipient flow. **Evidence:** repository access failures, match/action logs, recipient operations, expiry/revocation behavior, and teardown.

### Lab 5 — Unified DLP policy

Implement the same data requirement across Exchange, SharePoint/OneDrive, Teams, and one Cloud Apps or documented location. Start in simulation, tune precedence, add tips/override/alerts, then enforce one test cohort. **Evidence:** policy/rule trace for allowed, warned, overridden, and blocked actions.

### Lab 6 — Endpoint DLP control matrix

Onboard a disposable device and test removable media, print, clipboard, network share, RDP, restricted-service-domain upload, supported browsers/extensions, and just-in-time protection. **Evidence:** client action, event, alert, exception, unsupported path, and recovery.

### Lab 7 — Retention, precedence, and recovery

Apply broad retention plus a published or auto-applied label to synthetic Exchange and SharePoint/OneDrive content. Delete items, use Policy lookup, search/recover retained content, and tabletop disposition. **Evidence:** effective-policy reasoning, timestamps, restore result, and authorization record.

### Lab 8 — Insider and AI incident tabletop

Model an authorized insider-risk signal and synthetic AI exfiltration event. Trace alert, risk level, DLP action, Audit, Activity Explorer, XDR/Cloud Apps where supported, eDiscovery, notice/escalation, and current DSPM recommendation. **Evidence:** timeline, role/privacy controls, source records, decision, containment, and closure.

## Knowledge checks

1. **Built-in versus custom SIT?** Use maintained common detection versus organization-specific pattern/evidence logic.
2. **Fingerprint versus EDM?** Form-structure similarity versus exact/near-exact values from a governed reference table.
3. **Why supporting evidence?** It raises contextual confidence and reduces generic-pattern false positives.
4. **Why measure recall?** High precision can hide sensitive examples the classifier never finds.
5. **Trainable-classifier risk?** Unrepresentative examples create unreliable semantic matches; govern data and test independently.
6. **What does OCR change?** It exposes supported image text to classification, with location, format, billing, and quality dependencies.
7. **Data versus Content Explorer?** Aggregated classification insights versus privileged inspection of matched items.
8. **Item versus container label?** File/email protection versus supported site/team/group settings; one does not imply the other.
9. **Publishing versus auto-label policy?** Expose labels/user defaults versus service-side detection and application.
10. **Why simulate auto-labeling?** Inspect match quality, scope, and impact before protection is applied at scale.
11. **Scanner discovery first?** Establish access, coverage, unsupported files, and false positives before changing content.
12. **Encryption versus DLP?** Control authorized use of protected content versus decide whether an attempted data action is permitted.
13. **DLP policy versus rule priority?** Policies and rules both participate in evaluation; inspect the actual matching path and resulting restriction.
14. **What is a DLP override?** A permitted user continuation with justification and evidence—not an absence of policy.
15. **Adaptive Protection input?** Insider Risk Management-derived user risk levels, distinct from alert severity.
16. **Why test Cloud Apps separately?** Connected-app API, file, action, and governance coverage differs by service.
17. **Endpoint DLP prerequisite?** Eligible license, supported/onboarded device, connectivity, and required browser/client support.
18. **Just-in-time protection?** Temporary handling while classification/policy evaluation catches up; verify current scope and mode.
19. **Retention policy versus label?** Broad location-level lifecycle versus differentiated item-level lifecycle and record/disposition capabilities.
20. **Static versus adaptive scope?** Explicit membership versus query/attribute-driven membership that updates over time.
21. **Does retention equal backup?** No; retained content and independent point-in-time recovery solve different problems.
22. **Why Policy lookup?** Determine effective retention for an item/location instead of guessing from configured policies.
23. **Alert versus insider-risk case?** Detection aggregation versus investigator-managed evidence and action record.
24. **Does a risk alert prove intent?** No; it is a signal requiring privacy-aware investigation and context.
25. **Forensic-evidence prerequisite?** Explicit legal/privacy authorization, narrow scope, strong roles, retention, and audit.
26. **Audit retention versus content retention?** How long activity records remain searchable versus how long content is preserved.
27. **Activity Explorer versus Audit?** Focused data-protection activity analysis versus broader searchable workload activity evidence.
28. **Purview alert in XDR?** A supported correlated security signal; not every Purview event becomes an XDR incident.
29. **Why preserve policy version?** Investigation depends on the conditions, scope, priority, and actions active when the event occurred.
30. **eDiscovery search prerequisite?** Authorized case/roles, sources/custodians, tested query, handling plan, and audit.
31. **Primary Copilot data risk?** Existing oversharing or excessive access can make more data discoverable to authorized users.
32. **Does one Purview policy cover every AI service?** No; coverage varies by workload, endpoint, browser, app, connector, and license.
33. **Current DSPM versus classic?** Microsoft now documents a newer DSPM and separately names older DSPM/DSPM for AI classic experiences.
34. **DSPM recommendation versus remediation?** A posture finding/proposed action versus a validated, authorized control change.
35. **Why test unmanaged AI paths?** Managed-browser success does not prove native app, API, personal device, or proxy coverage.
36. **Best end-to-end evidence?** Requirement, classifier result, effective policy, user/device action, event/alert, investigation, recovery, and exception record.

## Places to learn

This is a curated starting set, **not a complete list** and not a recommendation to consume everything. Pick the formats that work for you, map them to the July 28, 2026 blueprint, and spend substantial time in a safe tenant. Durations are provider-listed runtimes where public; lab and reading times are planning estimates and access can change.

| Resource | Access | Estimated time | Best use / freshness note |
|---|---|---:|---|
| [Official SC-401 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) | Free | 30–45 min | Authoritative objective and change-log checklist; July 28, 2026 baseline. |
| Six official SC-401 Learn paths: [Information Protection](https://learn.microsoft.com/en-us/training/paths/purview-implement-information-protection/), [DLP](https://learn.microsoft.com/en-us/training/paths/purview-implement-manage-dlp/), [retention](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention/), [Insider Risk](https://learn.microsoft.com/en-us/training/paths/purview-implement-insider-risk-management/), [Audit/search](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/), and [AI](https://learn.microsoft.com/en-us/training/paths/purview-protect-ai/) | Free | 20h45 listed; allow 28–40h with exercises | Best current first-party sequence; repeat weak modules rather than racing the XP total. |
| [SC-401T00-A official course](https://learn.microsoft.com/en-us/training/courses/sc-401t00) | Paid instructor-led / free self-study links | 4 days | Structured current course and lab discussion; delivery varies by training partner. |
| [Official Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/practice/assessment?assessment-type=practice&assessmentId=1801497482&practice-assessment-type=certification) and exam sandbox | Free | 45–75 min per attempt plus review | Use diagnostically; research every weak answer in current documentation. |
| Official [Exam Readiness Zone videos](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/?terms=SC-401) | Free | About 1–2h; verify playlist | Orientation and blueprint review; confirm that each video reflects July 2026. |
| [John Christopher SC-401 course](https://www.udemy.com/course/sc-400-course-microsoft-information-protection-administrator/) | Paid | 8h26 video; allow 14–20h with simulations | Hands-on demonstrations and browser simulations; updated February 2026, so reconcile the July AI/audit changes. |
| [John Christopher SC-401 overview on YouTube](https://www.youtube.com/watch?v=CqYs-KtJoeQ) | Free | About 20 min; verify current runtime | Course orientation/sample teaching, not a complete July 2026 study path. This is not John Savill; no current Savill SC-401 end-to-end course was independently verified. |
| [MeasureUp SC-401 practice test](https://www.measureup.com/microsoft-sc-401-practice-test.html) | Paid; demo available | 146 questions; allow 6–10h across attempts/review | Independent assessment released September 2025; its listed objectives mostly match, but reconcile July 2026 changes and verify explanations. |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Microsoft partner login required | Schedule-dependent; allow the listed start/end time plus labs | Search SC-401, Purview, information security, and security workshops after sign-in; public pages did not expose a stable SC-401 listing or duration. |
| Microsoft Purview [documentation hub](https://learn.microsoft.com/en-us/purview/) | Free | Ongoing reference; 8–15h focused reading | Use for current prerequisites, supported locations, roles, licensing, limits, and portal changes. |

No current exam-specific Pluralsight, O'Reilly, or Whizlabs learning page with sufficiently stable public metadata was independently verified on September 1, 2026. That is a discovery gap, not a claim that those libraries contain no relevant Purview content. Search them by the exact exam code and compare the publication/update date and syllabus against all three current domains before purchasing.

## Final readiness checklist

- [ ] I can map every July 28, 2026 subobjective to a section, lab, and current first-party source.
- [ ] I can select and test built-in/custom SIT, fingerprint, EDM, trainable classifier, and OCR without conflating them.
- [ ] I can distinguish item/container labels, protection, publishing, auto-labeling, and Cloud Apps application.
- [ ] I can design scanner and encrypted-mail workflows with licensing, identity, evidence, failure, and recovery.
- [ ] I can trace DLP rule/policy precedence and user experience across cloud and endpoint locations.
- [ ] I can explain retention policy/label, static/adaptive scope, precedence, Policy lookup, disposition, and recovery.
- [ ] I can operate Insider Risk Management with privacy, connectors, endpoint signals, forensic-evidence governance, risk levels, alerts, cases, and notices.
- [ ] I can choose Audit, Activity Explorer, DLP/insider/XDR/Cloud Apps alerts, or eDiscovery for a specific investigation question.
- [ ] I can secure Microsoft and third-party AI use and distinguish current DSPM from classic experiences.
- [ ] I have completed the official assessment and independently researched every uncertain answer.
- [ ] I checked the official blueprint, credential page, licenses, portals, and **VERIFY CURRENT** items again shortly before the exam.

---

All knowledge checks and scenarios above are original study material, not recalled exam content. Product and exam names belong to their respective owners.
