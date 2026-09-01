---
exam_code: MS-102
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-102
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: retirement-announced
upcoming_change_checked: 2026-09-01
---

# MS-102 Microsoft 365 Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ms-102-coverage-record). The [official MS-102 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-102) is authoritative.

**Current baseline:** Skills measured as of April 28, 2026.<br>
**Retirement:** The exam and Microsoft 365 Certified: Administrator Expert certification retire November 30, 2026, at 11:59 PM Central Standard Time. They cannot be earned or renewed after that date.<br>
**Replacement:** Microsoft had not named a direct replacement on the official blueprint, credential page, or retirement page as of September 1, 2026. Do not infer one from a neighboring certification.<br>
**Upcoming blueprint change:** Retirement is announced; no separate pre-retirement objective revision is announced.<br>
**Practice Assessment:** A free Microsoft Practice Assessment is available.<br>
**Official source:** [MS-102 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-102)

## How to use this guide

MS-102 is an integration exam. A Microsoft 365 administrator must understand where tenant, identity, security, endpoint, application, and data controls meet—not merely recognize the admin portals. For every objective, practice this operating chain:

```text
business requirement
  -> tenant, user, device, application, or data object
  -> authoritative administration plane and least-privilege role
  -> policy configuration and license dependency
  -> staged deployment and negative test
  -> alert, audit, health, and usage evidence
  -> rollback, recovery, and owner
```

Read the four domain sections, work the three integrated scenarios, complete or tabletop all eight labs, and answer the 36 original checks. Use a disposable Microsoft 365 developer or test tenant where possible. Some Defender, Purview, Entra ID Governance, Backup, and advanced analytics features require specific licenses; never alter a production tenant simply to reproduce a lab.

This credential also requires one qualifying associate certification. Confirm the current prerequisite choices and completion rules on the [Administrator Expert credential page](https://learn.microsoft.com/en-us/credentials/certifications/m365-administrator-expert/) before scheduling.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Exam profile and complete objective map

| Official domain | Weight | Administrative question |
|---|---:|---|
| Deploy and manage a Microsoft 365 tenant | 25–30% | How is the tenant configured, delegated, licensed, monitored, updated, and recoverable? |
| Implement and manage Microsoft Entra identity and access | 25–30% | How are identities synchronized, authenticated, risk-evaluated, and granted secure access? |
| Manage security and threats by using Microsoft Defender XDR | 30–35% | How are exposure, email, endpoints, cloud apps, alerts, incidents, and response operated together? |
| Manage compliance by using Microsoft Purview | 10–15% | How are sensitive information, labels, retention, DLP, evidence, and response governed? |

### Published objective-to-guide map

| Published objective area | Primary coverage | Practice evidence |
|---|---|---|
| Tenant creation, domains, organization settings, Service Health, network insights, Microsoft 365 Apps updates, usage, and Backup | Section 1 | Scenarios 1 and 3; Labs 1 and 4 |
| Users, external users, contacts, groups, shared mailboxes, licensing, and bulk administration | Section 1 | All scenarios; Lab 2 |
| Microsoft 365, Entra, Defender, and Purview roles; administrative units; PIM | Section 1 | All scenarios; Lab 3 |
| Connect Sync, Cloud Sync, Connect Health, synchronization troubleshooting, and IdFix | Section 2 | Scenario 2; Lab 5 |
| Authentication methods, SSPR, Password Protection, and authentication troubleshooting | Section 2 | Scenarios 1–2; Lab 6 |
| Identity Protection, Conditional Access, and MFA | Section 2 | All scenarios; Lab 6 |
| Exposure Management, Secure Score, XDR incidents/alerts/reports, advanced hunting, and Threat Intelligence | Section 3 | All scenarios; Lab 7 |
| Defender for Office 365 policies, alerts, investigations, attack simulations, and restricted entities | Section 3 | Scenarios 1 and 3; Lab 7 |
| Defender for Endpoint onboarding, settings, and vulnerability management | Section 3 | Scenarios 2–3; Lab 7 |
| Defender for Cloud Apps connection, policies, activity log, Cloud Discovery, and response | Section 3 | Scenarios 1 and 3; Lab 7 |
| Sensitive information types, retention, sensitivity labels, explorers, and label reporting | Section 4 | All scenarios; Lab 8 |
| Workload and endpoint DLP, alerts, events, and reports | Section 4 | All scenarios; Lab 8 |

## 1. Deploy and manage a Microsoft 365 tenant

### Establish the tenant boundary before configuring workloads

A tenant is the primary identity and service boundary for Microsoft 365. Record its initial domain, verified custom domains, data residency commitments, subscriptions, service ownership, emergency access accounts, administrative model, naming conventions, and recovery contacts before adding production users. A custom domain is proved through DNS; adding the domain does not migrate mail, change every user's sign-in name, or automatically create the service records required by Exchange, Teams, and device enrollment. Microsoft's [domain guidance](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/domains-faq?view=o365-worldwide) should be checked before changing production DNS.

Separate four kinds of configuration evidence:

| Evidence | Question answered | Typical source |
|---|---|---|
| Desired configuration | What should exist? | Approved design, automation, change record |
| Effective configuration | What does the service currently enforce? | Admin center, Graph, workload PowerShell |
| Service condition | Is Microsoft reporting a current incident or advisory? | Service Health and message center |
| User experience | Can a representative client reach and use the service? | Connectivity test, synthetic transaction, support telemetry |

Service Health is tenant-specific and should have notification recipients and an incident process. A green service-health view does not prove that DNS, proxy, identity, device, or local network configuration is healthy. Network connectivity insights help locate Microsoft 365 egress and connectivity problems; they are not a substitute for packet-path, DNS, proxy, and client evidence. Start with Microsoft's [network connectivity overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-networking-overview?view=o365-worldwide), then correlate tenant insights with local telemetry.

Microsoft 365 Apps update management is a policy and rollout problem. Define channel, target groups, deadlines, exclusions, rollback, health signals, and support ownership. A dashboard can report update progress, but it cannot make a device reachable or repair an incompatible add-in. Review the current [Microsoft 365 Apps cloud-update guidance](https://learn.microsoft.com/en-us/microsoft-365-apps/admin-center/cloud-update-prepare) because supported controls and channel behavior change.

Usage reports measure service activity; Adoption Score adds organizational insights and recommendations. Neither proves business value or employee performance. Minimize report access, understand privacy settings, and combine aggregated adoption evidence with support, process, and outcome measures. Microsoft's [activity reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide) documents available reports and administrative access.

Microsoft 365 Backup is a separately configured recovery capability for supported workloads. Define protected scope, retention, restore permissions, recovery objectives, cost ownership, and test cadence. Native retention, recycle bins, version history, litigation requirements, and backup solve overlapping but different problems. Confirm current workload and restore behavior in the [Microsoft 365 Backup overview](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-overview?view=o365-worldwide).

> **Related item:** Configuration management matters even when the portal is the primary interface. Export role assignments, domains, policies, licenses, and health configuration on a schedule. Without a dated baseline, an administrator can observe drift but cannot prove when or why it occurred.

### Manage identities, collaboration objects, and licenses as lifecycles

For a user, distinguish the account object, authentication state, licenses, workload provisioning, group memberships, mailbox or collaboration resources, device relationships, data ownership, and retention obligations. A deletion request can affect each on a different timeline. Build joiner, mover, leaver, guest-expiration, legal-hold, mailbox-conversion, and data-transfer procedures rather than treating account deletion as the whole lifecycle.

Cloud users are mastered in Entra ID; synchronized users are normally mastered in the configured on-premises source for synchronized attributes. External users have a home identity outside the resource tenant and a guest or member representation inside it. Contacts are addressable directory objects without the same identity and sign-in behavior as users. A Microsoft 365 group supplies a membership and collaboration boundary across services; a distribution group primarily distributes messages; a security group grants access; a shared mailbox provides delegated mailbox access. Choose the object from the requirement, not from a familiar admin center.

Licensing is assignment plus successful downstream service provisioning. Direct assignment is simple for exceptions but becomes difficult to govern at scale. Group-based licensing connects entitlement to group membership and can expose assignment errors that must be resolved. Nested groups do not automatically become a safe entitlement design. Track available units, disabled service plans, conflicting assignments, usage location, group processing errors, and reclaimed licenses. Review [group-based licensing](https://learn.microsoft.com/en-us/entra/identity/users/licensing-groups-assign) before designing automation.

Bulk administration should be repeatable, scoped, logged, and idempotent. Prefer the current Microsoft Graph PowerShell SDK for new cross-service automation, request only required scopes, validate a small batch, record per-object results, and handle throttling and partial failures. The [Graph PowerShell overview](https://learn.microsoft.com/en-us/powershell/microsoftgraph/overview?view=graph-powershell-1.0) explains its authentication and command model. A successful command is not the same as successful service provisioning; query the resulting object and workload state.

```powershell
# Illustrative inventory pattern; test command names and permissions in a lab.
Connect-MgGraph -Scopes 'User.Read.All','Group.Read.All','Organization.Read.All'
Get-MgUser -All -Property Id,DisplayName,UserPrincipalName,AccountEnabled,AssignedLicenses |
  Select-Object Id,DisplayName,UserPrincipalName,AccountEnabled,AssignedLicenses
```

Do not place secrets in scripts, transcripts, or exported reports. Record tenant ID, Graph context, requested scopes, query timestamp, pagination, failures, and the secure storage location for output.

> **Related item:** Entitlement management and access reviews can govern some access packages and group membership beyond the explicit MS-102 wording. They do not replace the administrator's need to understand the underlying group, role, license, and workload effect.

### Delegate control without creating hidden global administrators

Microsoft 365 and Entra roles are different role systems. Defender XDR and Purview also have role and role-group models. Map each task to its authoritative plane and the narrowest supported role. Microsoft's [Microsoft 365 role overview](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide), [Defender XDR unified RBAC guidance](https://learn.microsoft.com/en-us/defender-xdr/manage-rbac), and [Purview permissions guidance](https://learn.microsoft.com/en-us/purview/purview-permissions) describe boundaries that can overlap during migration or coexistence. **VERIFY CURRENT** before changing a production role model.

Administrative units restrict the scope of supported Entra role assignments to selected users, groups, or devices. They do not partition the tenant or scope every Microsoft 365 workload role. Restricted-management administrative units add stronger protections and operational constraints; validate supported objects and recovery access. The [administrative-unit documentation](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units) is the source for current support.

PIM changes a supported role from permanent standing access to eligible or time-bound activation. Configure maximum duration, justification, approval where appropriate, authentication context or strong authentication, notifications, access reviews, and emergency recovery. PIM does not make an overpowered role least privileged and does not govern every workload role. Review the [PIM overview](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure).

Keep at least two tested, cloud-only emergency-access accounts protected and monitored according to Microsoft's current recommendations. Do not use them for routine administration. Exercise recovery without weakening Conditional Access for ordinary administrators.

> **Related item:** A delegated administrator can become effectively global through group ownership, application consent, role-management permission, or the ability to alter synchronization. Review privilege paths, not only direct role membership.

## 2. Implement and manage Microsoft Entra identity and access

### Treat synchronization as a data pipeline with authority and recovery

Microsoft Entra Connect Sync uses an on-premises synchronization engine and supports a broad set of hybrid identity scenarios. Microsoft Entra Cloud Sync uses lightweight provisioning agents and cloud-managed configuration, with different topology and feature support. Do not choose solely because one is newer. Compare authoritative source, forests and domains, object types, filtering, writeback requirements, custom rules, high availability, network constraints, and migration path against the current [Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis) and [Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync) documentation.

Before synchronization:

1. Inventory forests, UPN suffixes, accepted domains, duplicate attributes, unsupported characters, proxy addresses, object counts, and service accounts.
2. Decide source anchor and scoping rules; document which system masters every synchronized attribute.
3. Run IdFix and resolve findings deliberately rather than blindly accepting changes.
4. Stage a pilot organizational unit or group and define rollback.
5. Establish connector, agent, scheduler, export, accidental-delete, and credential monitoring.
6. Test create, update, disable, rename, move, soft-delete, restore, and source-of-authority behavior.

Use [Connect Health synchronization monitoring](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-sync) where supported, but also inspect connector-space, synchronization-service, provisioning, audit, and sign-in evidence. A healthy agent does not prove every object exported correctly. Troubleshoot in sequence: authoritative source object, scope/filter, import, join/metaverse, synchronization rule, export, cloud object, then workload effect. Preserve connector errors and object IDs before retrying.

> **Related item:** Password hash synchronization can provide sign-in resilience even when another authentication approach is primary, but enabling or changing it is a security and architecture decision. Test incident, outage, and rollback procedures instead of assuming the normal sign-in flow will always be available.

### Build authentication as registration, policy, recovery, and evidence

Authentication methods policy determines which methods groups may register and use. Prefer phishing-resistant methods for privileged and high-risk access where supported, then design bootstrap and recovery. Temporary Access Pass can help bootstrap passwordless registration; SSPR provides user-driven recovery only when registration, licensing, writeback, policy, and verification dependencies are satisfied. Review the current [authentication-methods policy](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage) and [SSPR behavior](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks).

Microsoft Entra Password Protection applies global and custom banned-password logic in the cloud and can extend protection to on-premises AD DS through proxy and DC agents. It is not a substitute for phishing-resistant authentication. Verify deployment, audit/enforce mode, agent health, proxy redundancy, and event logs using the [on-premises Password Protection guidance](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-password-ban-bad-on-premises).

For an authentication failure, capture correlation ID, timestamp, user, resource, client, device, network, authentication requirement, method attempted, Conditional Access result, risk, and error code. Then distinguish:

- authentication-method registration or availability;
- password, lockout, or source synchronization;
- token, session, or client behavior;
- Conditional Access grant/session control;
- device compliance or join state;
- workload authorization after successful sign-in.

Resetting a password or excluding a user from policy without identifying the failed control can turn a support case into a security gap.

> **Related item:** Authentication strength describes allowed combinations for a Conditional Access grant. It is more precise than merely requiring “MFA,” because not every MFA combination offers the same phishing resistance.

### Convert identity risk into controlled access decisions

Identity Protection detects supported user and sign-in risks and supports investigation, confirmation, dismissal, and policy-driven remediation. Risk detections are evidence signals, not proof of compromise. Validate the user, sign-in context, device, IP, correlated incidents, and remediation status in the [Identity Protection overview](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection).

Conditional Access evaluates identity, target resource, conditions, and access controls after primary authentication. Design a small composable policy set rather than one giant rule. Include explicit coverage for administrators, users, workload identities where supported, legacy authentication, device/platform, location, risk, authentication strength, sign-in frequency, and emergency access exclusions. Start in report-only mode, analyze results, pilot, enforce, and retain rollback. The [Conditional Access overview](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) and [session-controls reference](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-session) explain the current evaluation model.

Do not confuse these controls:

| Control | Primary purpose | It does not replace |
|---|---|---|
| Authentication method policy | Allow method registration/use | Conditional Access targeting |
| Conditional Access | Contextual access decision | Workload authorization |
| Identity Protection | Detect and remediate identity risk | Incident investigation |
| PIM | Time-bound privileged-role activation | Least-privilege role design |
| Device compliance | Report device state | Endpoint detection and response |

> **Related item:** Token theft and session persistence mean that successful MFA is not the end of identity defense. Correlate token/session behavior, continuous access evaluation where supported, Defender signals, and revocation during response.

## 3. Manage security and threats with Microsoft Defender XDR

### Operate from exposure to incident and verified remediation

Microsoft Security Exposure Management connects assets, initiatives, attack paths, recommendations, and exposure insights. Microsoft Secure Score measures improvement actions within its supported control model. Neither is a universal risk score or proof of compliance. Use asset criticality, exploitability, exposure, threat evidence, control ownership, business impact, and remediation cost to prioritize. Review [attack paths](https://learn.microsoft.com/en-us/security-exposure-management/work-attack-paths-overview) and [Microsoft Secure Score](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score) against current licensing and feature availability.

In Defender XDR, an alert represents a suspicious signal; an incident groups related alerts and entities into an investigation. Begin with scope and timeline, then examine affected users, devices, mailboxes, applications, cloud activities, evidence, and automated actions. Preserve evidence before containment when safe. Use advanced hunting to test hypotheses across available tables, not to search blindly. Validate query time range, schema, ingestion, joins, and null behavior. Microsoft maintains current product guidance in the [Defender XDR documentation](https://learn.microsoft.com/en-us/defender-xdr/).

Threat Intelligence provides actor, campaign, indicator, and vulnerability context. An indicator match is not automatically malicious in the local environment, and absence of a match is not proof of safety. Record source, confidence, validity period, affected assets, action, exception, and review date.

> **Related item:** Incident closure should include root cause, affected scope, containment, eradication, recovery, control improvement, and evidence retention. Changing status to resolved without validating recovery hides repeat exposure.

### Protect email and collaboration with layered policy

Exchange Online Protection provides baseline mail filtering; Defender for Office 365 adds supported Safe Links, Safe Attachments, investigation, simulation, and response capabilities by plan. Use preset Standard or Strict security policies as a known baseline where they fit, then document narrowly scoped exceptions. Review Microsoft's [recommended EOP and Defender for Office 365 settings](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365).

Understand the order and boundary of connection, anti-malware, anti-spam, anti-phishing, impersonation, Safe Attachments, Safe Links, quarantine, tenant allow/block, and mail-flow controls. An allow entry can bypass part of the protection chain and should have owner, scope, reason, expiry, monitoring, and revalidation. Advanced delivery is for controlled simulations and supported security operations—not a general allowlist.

Investigate email threats through message trace, Explorer or real-time detections where licensed, campaign and entity evidence, URL/file detonation, user submissions, and incident correlation. Remediation may include soft/hard delete, quarantine, block, account/session action, device investigation, and hunting for similar messages. Test the authorized path and the prohibited path after policy changes.

Attack Simulation Training should use approved payloads, audiences, privacy controls, safe landing pages, training assignments, and success measures. It is a behavior-improvement exercise, not a covert employee test. Start with the [attack-simulation guidance](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started). Restricted entities protect the service after suspicious outbound behavior; investigate and remediate the cause before following the [blocked-user recovery process](https://learn.microsoft.com/en-us/defender-office-365/outbound-spam-restore-restricted-users).

> **Related item:** SPF, DKIM, and DMARC establish domain-level sending and authentication signals. They strengthen anti-phishing decisions but do not inspect a safe-looking message body, attachment, OAuth grant, or compromised legitimate sender.

### Connect endpoint and cloud-app evidence to XDR

Defender for Endpoint onboarding establishes sensor and service connectivity; it does not automatically apply every prevention policy or guarantee that all devices are healthy. Choose an onboarding method, define supported operating systems, configure endpoint settings and integrations, pilot device groups, validate sensor health, and confirm tamper protection and EDR evidence. Use the current [Defender for Endpoint onboarding guidance](https://learn.microsoft.com/en-us/defender-endpoint/onboarding).

Vulnerability Management inventories supported software, weaknesses, recommendations, exposure, and remediation status. Prioritize using exploit availability, exposure, asset value, active alerts, compensating controls, and operational impact. A recommendation closed in the portal is not enough; prove the target version/configuration and watch for reappearance. Review [Defender Vulnerability Management](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management).

Defender for Cloud Apps connects supported services and ingests activity for investigation and policy. The Microsoft 365 connector enables supported visibility; verify included applications, audit prerequisites, data delay, and role permissions in the [connection guidance](https://learn.microsoft.com/en-us/defender-cloud-apps/connect-office-365). Policies can detect activity, anomalies, risky OAuth apps, files, and sessions according to type and licensing. Tune against known business behavior without broad exclusions.

Cloud Discovery analyzes supported network logs to identify sanctioned and unsanctioned cloud use and apply risk context. It does not prove that every discovered app contains company data or that blocking an app is safe. Validate owner, users, data, authentication, contract, integrations, and replacement path using [discovered-app guidance](https://learn.microsoft.com/en-us/defender-cloud-apps/discovered-apps).

> **Related item:** Defender for Endpoint, Defender for Office 365, Defender for Identity, Defender for Cloud Apps, and Entra signals become more useful when entity identifiers and timestamps correlate. Integration amplifies evidence; it does not erase each product's licensing, onboarding, retention, or sensor dependencies.

## 4. Manage compliance with Microsoft Purview

### Separate detection, labeling, protection, retention, and investigation

A sensitive information type detects content patterns through elements such as keywords, keyword lists, regular expressions, supporting evidence, proximity, confidence, and instance counts. Test custom types against representative positive, boundary, and negative samples. A match is classification evidence, not automatically a sensitivity label, retention decision, or DLP action.

Sensitivity labels classify and can apply protection or container settings according to supported scope. Label policy publishes labels and defaults to users or groups. Auto-labeling applies labels when conditions match. Plan label order, scope, encryption, content marking, group/site settings, user justification, downgrade behavior, coauthoring, and application support. Review the [sensitivity-label documentation](https://learn.microsoft.com/en-us/purview/sensitivity-labels) because capabilities differ across files, email, meetings, groups, sites, and applications.

Retention policies apply broad retention or deletion settings by location; retention labels classify individual items and can support records behavior, event-based retention, disposition review, and other item-level actions where licensed. Retention is not backup, and deletion is not immediate in every service. Use the [retention overview](https://learn.microsoft.com/en-us/purview/retention) to model preservation, deletion precedence, adaptive/static scope, record restrictions, and workload support.

Content Explorer shows classified content according to role and access controls; Activity Explorer shows detected and label-related events; reports show aggregate adoption and policy results. These tools contain sensitive metadata and sometimes content access, so use least privilege and audit their use. Review [Content Explorer](https://learn.microsoft.com/en-us/purview/data-classification-content-explorer) before granting access.

> **Related item:** eDiscovery, Audit, Communication Compliance, Insider Risk Management, and records management may consume the same data and labels. They are adjacent governance capabilities, not interchangeable with the MS-102 information-protection and DLP objectives.

### Design DLP from data path to response

DLP evaluates sensitive information and contextual conditions in supported locations, then can audit, warn, justify, restrict, or block according to configuration. Define the data to protect, business workflow, locations, users/groups, conditions, exclusions, action, user notification, policy tip, incident report, alert severity, override, and evidence retention. Begin in simulation where supported, inspect false positives and false negatives, then stage enforcement. Microsoft's [DLP overview](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) documents the policy model.

Microsoft 365 DLP can cover supported Exchange, SharePoint, OneDrive, Teams, Power BI, and Microsoft 365 Copilot locations. Coverage and available conditions/actions differ by location. A policy that works for email cannot be assumed to behave identically for a Teams message, Fabric/Power BI artifact, or grounded Copilot interaction. **VERIFY CURRENT** licensing, workload support, and evaluation behavior before deployment.

Endpoint DLP extends supported controls to activities on onboarded and properly configured devices, such as copying, printing, browser upload, application access, or removable media. It depends on device onboarding, supported platform/version, settings, indicators, browser/domain/service configuration, and policy distribution. Review [Endpoint DLP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about) and test the exact operation, application, destination, and device state.

Respond to a DLP alert by validating the rule, matched information, user, device, workload, destination, action, override, business context, and related events. Decide whether to close as expected behavior, tune the rule, educate the user, revoke access, contain a device/account, preserve evidence, or escalate. Do not globally weaken the policy to resolve one false positive; create the narrowest justified exception with owner and expiry.

> **Related item:** A sensitivity label can travel with and protect content, while DLP evaluates an attempted action. Using the label as a DLP condition connects classification to enforcement, but each policy still has its own scope, client, and licensing dependencies.

## Integrated scenarios

### Scenario 1: Regulated acquisition tenant

A company acquires a smaller business and must onboard 600 workers, preserve the acquired domain, restrict privileged administration, protect regulated documents, and maintain service continuity.

1. Inventory domains, authoritative directories, duplicate attributes, licenses, groups, workloads, records obligations, and recovery requirements.
2. Prove the domain and plan DNS without changing production mail flow prematurely. Pilot users and synchronization scope after IdFix remediation.
3. Use group-based licensing with exception handling; design Microsoft 365 groups, shared mailboxes, external users, and data ownership deliberately.
4. Delegate tasks through narrow roles, administrative units where supported, PIM, and emergency access. Record cross-workload privilege paths.
5. Stage Conditional Access and authentication registration. Test normal, high-risk, recovery, guest, and emergency access.
6. Publish sensitivity/retention labels and simulate DLP before enforcement. Verify workload differences and legal requirements.
7. Configure Service Health notifications, usage evidence, Backup scope, Defender integrations, and an incident route.

The common failure is changing DNS or synchronization broadly before identity collisions, role ownership, retention, and rollback are understood.

### Scenario 2: Hybrid identity compromise

An administrator receives a risky-sign-in alert while Connect Sync exports unexpected changes and an endpoint shows suspicious activity.

1. Preserve sign-in, audit, sync, endpoint, role, and incident evidence with identifiers and time range.
2. Determine whether the source is on-premises AD DS, synchronization rules/credentials, cloud administration, or a compromised endpoint.
3. Contain sessions, accounts, devices, roles, and synchronization only as required; retain tested emergency access.
4. Investigate Defender XDR incident entities and hunt for related users, devices, apps, and mail activity.
5. Remediate the authoritative object, credential, device, sync rule, and persistence path. Do not merely repair the cloud symptom.
6. Validate synchronization, authentication, Conditional Access, PIM, endpoint health, and restored business access.

The common failure is resetting the user's password while an overprivileged sync or application identity remains able to recreate the compromise.

### Scenario 3: Sensitive-data exfiltration through collaboration and a cloud app

Users report suspicious sharing links, a newly authorized SaaS application, and DLP alerts involving endpoint uploads.

1. Correlate Purview DLP events, sharing/audit evidence, Defender for Cloud Apps activity/OAuth findings, endpoint timeline, identity sign-ins, and XDR incidents.
2. Validate the sensitive-information match, label, item permissions, application grant, destination, user intent, and device state.
3. Contain the narrowest unsafe paths: session/account, OAuth grant, file sharing, endpoint activity, app access, or malicious mail.
4. Preserve evidence, revoke or remediate, search for related data and entities, and validate authorized collaboration still works.
5. Tune policies only from documented false-positive/negative evidence. Add owner, expiry, and review to exceptions.

The common failure is blocking one cloud app while the same data remains overshared through another authorized path.

## Hands-on labs

Use synthetic identities and data in an authorized test tenant. Record unavailable licenses as constraints and tabletop the same configuration, tests, evidence, and rollback rather than inventing results.

### Lab 1: Tenant, domain, health, network, update, and recovery baseline

Create a tenant operations workbook containing domain/DNS state, organization settings, Service Health notification routes, message-center ownership, network insight and local path evidence, Microsoft 365 Apps update policy, usage/privacy settings, Backup scope, recovery objectives, and a restore test plan. Make one safe configuration change and prove approval, effective state, monitoring, and rollback.

### Lab 2: User, group, shared mailbox, and license lifecycle

Create a cloud user, guest, contact, Microsoft 365 group, security group, and shared mailbox. Assign a group-based license, create one safe assignment error, resolve it, and verify workload provisioning. Use Graph PowerShell to inventory objects without changing them. Exercise mover, disabled-user, guest-expiry, mailbox-conversion, data-owner, and deletion/recovery decisions.

### Lab 3: Least-privilege administration

Build a task-to-role matrix across Microsoft 365, Entra, Defender XDR, and Purview. Configure a scoped administrative-unit assignment and a PIM-eligible lab role if licensing permits. Test activation, approval or justification, expiry, authorized action, denied action, audit event, and emergency recovery. Document unsupported scoping and indirect privilege paths.

### Lab 4: Service and backup evidence drill

Choose one supported workload. Capture service-health state, client and network health, usage evidence, protection scope, retention/version behavior, and backup configuration. Perform or tabletop an item-level restore and a larger recovery request. State what native retention, Backup, and legal preservation each do and do not recover.

### Lab 5: Synchronization pipeline

In a lab or tabletop environment, compare Connect Sync and Cloud Sync against a written topology. Run IdFix on sample data, define scope and source anchor, and trace a create, rename, disable, and deletion through import, join, synchronization, export, cloud object, and workload provisioning. Introduce a safe duplicate-attribute or scope error, capture evidence, remediate at the authoritative source, and retest.

### Lab 6: Authentication, risk, and Conditional Access

Register two authentication methods for test users, configure SSPR and Password Protection evidence, and stage Conditional Access in report-only mode. Test ordinary access, high-risk sign-in, privileged authentication strength, unmanaged device, excluded emergency account, and recovery. Record sign-in-log policy results and prove a rollback path before enforcement.

### Lab 7: Defender XDR control chain

Create a control-and-evidence map for Exposure Management/Secure Score, one Office 365 threat policy, an attack-simulation tabletop, endpoint onboarding/health/vulnerability response, Defender for Cloud Apps connection/policy, Cloud Discovery, and XDR incident investigation. Use safe simulations or existing lab alerts. Trace source signal to alert, incident, query, containment, remediation, validation, and closure.

### Lab 8: Purview classification, retention, and DLP

Create synthetic documents that provide positive, boundary, and negative matches for a sensitive information type. Design a sensitivity label, retention policy or label, and DLP policy in simulation. Include one supported collaboration location and an Endpoint DLP tabletop or test. Inspect explorer/report evidence, user notification/override, alert details, false-positive handling, enforcement rollout, exception expiry, and rollback.

## Original knowledge checks

These are original study questions, not recalled or reconstructed exam items. Answer in your own words, then verify against the cited official documentation and lab evidence.

1. Why does proving a custom domain not complete Microsoft 365 service configuration?
2. Which evidence distinguishes a Microsoft service incident from a tenant network or identity problem?
3. Why are usage reports not a direct measure of business value or employee performance?
4. How do retention, version history, recycle bins, legal preservation, and Microsoft 365 Backup solve different recovery needs?
5. When should you choose a Microsoft 365 group, security group, distribution group, contact, or shared mailbox?
6. What must be verified after a license assignment succeeds?
7. Why should bulk administration be idempotent and record partial failures?
8. How do Microsoft 365, Entra, Defender XDR, and Purview roles differ?
9. What can an administrative unit scope, and what does it not partition?
10. Why does PIM not make an overprivileged role safe?
11. Which requirements favor Connect Sync, and which favor Cloud Sync?
12. What does IdFix validate before synchronization?
13. How do you trace a synchronization failure from source object to workload result?
14. Why can a healthy synchronization agent coexist with individual object errors?
15. How do authentication-method policy, SSPR, Password Protection, and Temporary Access Pass differ?
16. Which evidence separates failed authentication from failed workload authorization?
17. Why is authentication strength more precise than a generic MFA requirement?
18. How should Identity Protection risk affect investigation and Conditional Access without being treated as proof of compromise?
19. What must be tested before enabling a tenant-wide Conditional Access policy?
20. Why should emergency-access accounts be cloud-only, monitored, and excluded deliberately?
21. How do an exposure recommendation, Secure Score improvement action, alert, and incident differ?
22. What makes an advanced-hunting result reliable enough to drive response?
23. Why is an email allow entry a time-bound risk decision rather than a convenient permanent fix?
24. How do EOP, Safe Attachments, Safe Links, and mail-flow rules protect different parts of a message path?
25. What must happen before a restricted sender is unblocked?
26. Why does endpoint onboarding not prove prevention settings and sensor health are complete?
27. Which factors should prioritize a vulnerability recommendation?
28. What does connecting Microsoft 365 to Defender for Cloud Apps add, and what prerequisites remain?
29. Why is a discovered cloud application not automatically unsafe or safe?
30. How do a sensitive information type, sensitivity label, retention label, and DLP rule differ?
31. When should you use a broad retention policy rather than an item-level retention label?
32. What access risks exist in Content Explorer and Activity Explorer?
33. Why must DLP behavior be tested separately for Exchange, SharePoint, OneDrive, Teams, Power BI, Copilot, and endpoints?
34. Which dependencies make an Endpoint DLP rule effective on a device?
35. How should a DLP false positive be resolved without creating an unbounded exception?
36. What evidence proves a cross-domain Microsoft 365 incident is contained, recovered, and unlikely to recur?

## Final readiness checklist

- [ ] I checked the official MS-102 page for retirement, blueprint, prerequisite, language, and scheduling changes.
- [ ] I understand that November 30, 2026 is the final earning and renewal date and that no direct replacement was officially named at this review.
- [ ] I can map every objective to its authoritative admin plane, least-privilege role, configuration, negative test, evidence, and rollback.
- [ ] I can operate domains, organization settings, Service Health, network insights, Apps updates, usage, and Backup as one tenant lifecycle.
- [ ] I can manage cloud, synchronized, and external users plus contacts, groups, shared mailboxes, licenses, and bulk changes.
- [ ] I can distinguish Microsoft 365, Entra, Defender, and Purview roles and use administrative units, PIM, and emergency access safely.
- [ ] I can choose, monitor, and troubleshoot Connect Sync or Cloud Sync from source object through workload provisioning.
- [ ] I can design authentication registration, SSPR, Password Protection, Identity Protection, MFA, and Conditional Access together.
- [ ] I can prioritize exposure and Secure Score findings and investigate XDR alerts/incidents using defensible evidence.
- [ ] I can configure and investigate Defender for Office 365, Endpoint, and Cloud Apps without confusing their boundaries.
- [ ] I can implement and distinguish sensitive information types, sensitivity labels, retention, explorers, and reporting.
- [ ] I can simulate, enforce, investigate, and tune workload and endpoint DLP with scoped exceptions.
- [ ] I completed or tabletop-tested all eight labs and can explain both allowed and denied outcomes.
- [ ] I passed an independent readiness check without relying on recalled live-exam content.

## Places to learn

This is a curated starting point, **not a complete list**. Do not try to consume every item. Pick the format and depth that work for you, use the current official blueprint as the coverage checklist, and reserve substantial time for tenant practice, negative tests, troubleshooting, and review. Because MS-102 retires November 30, 2026, verify that any planned course and exam date leave enough recovery time for rescheduling.

The nine official paths linked from the MS-102 course are [configure your tenant](https://learn.microsoft.com/en-us/training/paths/configure-microsoft-365-tenant/) (3h31), [manage your tenant](https://learn.microsoft.com/en-us/training/paths/manage-your-microsoft-365-tenant/) (3h33), [implement identity synchronization](https://learn.microsoft.com/en-us/training/paths/implement-identity-synchronization/) (2h38), [manage identity and access](https://learn.microsoft.com/en-us/training/paths/explore-security-metrics-microsoft-365-defender/) (4h28), [manage Defender XDR security services](https://learn.microsoft.com/en-us/training/paths/manage-security-services-microsoft-365-defender/) (2h59), [implement Defender XDR threat protection](https://learn.microsoft.com/en-us/training/paths/implement-threat-protection-use-microsoft-365-defender/) (3h05), [explore data governance](https://learn.microsoft.com/en-us/training/paths/explore-data-governance-microsoft-365/) (2h03), [implement compliance](https://learn.microsoft.com/en-us/training/paths/implement-compliance-microsoft-365/) (4h11), and [manage compliance](https://learn.microsoft.com/en-us/training/paths/ms-102-manage-compliance-microsoft-365/) (2h17). Listed times total 28h45 before labs, notes, prerequisite remediation, or spaced review.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MS-102 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-102) and [Administrator Expert credential page](https://learn.microsoft.com/en-us/credentials/certifications/m365-administrator-expert/) | Public | 1–2 hours initially; 15 minutes on each recheck |
| Nine official Microsoft Learn paths linked from the [MS-102T00 course syllabus](https://learn.microsoft.com/en-us/training/courses/ms-102t00) | Public | 28 hours 45 minutes listed; allow about 45–65 hours with exercises and notes |
| [MS-102T00 instructor-led course](https://learn.microsoft.com/en-us/training/courses/ms-102t00) | Paid/partner delivery | 5 days listed |
| [Microsoft MS-102 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/ms-102/practice/assessment?assessment-type=practice&assessmentId=75) | Public | 45–75 minutes per attempt plus source review |
| [O'Reilly MS-102 certification course](https://www.oreilly.com/videos/microsoft-365-administrator/0642572062019/) with Aaron Guilmette | Paid | 4 hours 23 minutes; January 2025, so reconcile the April 2026 changes and retirement baseline |
| [O'Reilly/Microsoft Press Exam Ref MS-102](https://www.oreilly.com/library/view/exam-ref-ms-102/9780138199517/) by Orin Thomas | Paid | 7 hours 37 minutes / 305 pages listed; November 2023 foundation with an updates chapter—verify all April 2026 objectives |
| [Udemy MS-102 course with simulations](https://www.udemy.com/course/ms100course/) by John Christopher | Paid | 15 hours 5 minutes listed; updated August 2026, but independently validate licensing-sensitive labs and exact objective coverage |
| [MeasureUp MS-102 practice test](https://www.measureup.com/practice-test-ms-102-microsoft-365-administrator-exam.html) | Paid | About 5–9 hours for diagnostic, targeted practice, source review, and timed retest; public page does not expose a reliable question count |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics) | Public | 2–8 hours selectively for current Microsoft 365, Entra, Defender, Purview, and admin demonstrations; not an objective-mapped MS-102 course |
| [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor) | Public | 2–8 hours selectively; use current Microsoft 365 security, identity, compliance, and Copilot sessions only where they close a mapped gap |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; partner sign-in is required to confirm a current MS-102 offering and exact session duration |

No exact current Pluralsight or Whizlabs MS-102 product page was independently verified during this review, so none is inferred from their broader Microsoft catalogs. Older MS-102 courses can still teach durable administration, identity, Defender, and Purview foundations, but they must be reconciled against the April 28, 2026 blueprint and the November 30 retirement.
