---
exam_code: MD-102
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# MD-102 Managing and Securing Microsoft 365 Endpoints by Using Intune Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 24, 2026 objectives and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#md-102-coverage-record). The [official MD-102 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102) is authoritative.

**Current baseline:** Skills measured as of July 24, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Official source:** [MD-102 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102)

## How to use this guide

MD-102 tests endpoint operations across Windows, Android, iOS/iPadOS, macOS, specialty devices, and Cloud PCs. The July 2026 blueprint adds substantial Intune Suite, automation, analytics, reporting, and Security Copilot agent depth. Older four-domain material remains useful but is incomplete.

For every scenario, trace:

1. **Ownership and platform:** corporate or personal, physical or Cloud PC, OS/device type, lifecycle stage.
2. **Identity and enrollment:** Entra registered/joined/hybrid joined, MDM/MAM enrollment, platform enrollment method.
3. **Targeting:** user/device group, assignment intent, filter, enrollment-time grouping, scope tag.
4. **Policy and application:** effective configuration, compliance, endpoint-security, update, app, and protection policies.
5. **Access decision:** authentication, Conditional Access, device compliance, app protection, resource authorization.
6. **Evidence and action:** Intune status, sign-in and Defender evidence, reports/KQL/logs, remote action, rollback and recovery.

Do not diagnose from one portal badge. A device can be Entra joined but not Intune enrolled, enrolled but noncompliant, compliant but blocked by another Conditional Access control, or allowed to sign in while a managed application fails. Record UTC time, user, device IDs, serial number, platform, policy, assignment and error before changing configuration.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Prepare infrastructure for devices | 20–25% | How do identity, enrollment, delegation, compliance and local privilege establish the management boundary? |
| Manage and maintain devices | 25–30% | How are devices provisioned, configured, supported and extended through Intune and Windows 365? |
| Protect devices | 15–20% | How do endpoint-security and update controls reduce risk while preserving operability? |
| Manage and secure applications | 15–20% | How are apps packaged, deployed, configured, protected, updated and troubleshot? |
| Optimize endpoint operations using automation, monitoring and reporting | 10–15% | How do Graph/PowerShell, agents, analytics, remediations and reporting improve fleet outcomes safely? |

---

## 1. Prepare infrastructure for devices

### Device identity: registered, joined, and hybrid joined

[Microsoft Entra device identity](https://learn.microsoft.com/en-us/entra/identity/devices/overview) connects a physical or virtual device to tenant access decisions. Choose the state from ownership, sign-in, application, management and dependency requirements:

| State | Typical use | Important boundary |
|---|---|---|
| Microsoft Entra registered | Personally owned/BYOD device using a work identity | User adds a work account; registration is not corporate Windows sign-in or full management by itself |
| Microsoft Entra joined | Organization-owned, cloud-first Windows device | User signs in with Entra identity; avoids an on-premises domain dependency |
| Microsoft Entra hybrid joined | Domain-joined Windows device also represented in Entra | Retains AD DS dependency and synchronization; more moving parts |

Join creates device identity; MDM enrollment creates the Intune management relationship; compliance evaluates configured requirements; Conditional Access uses signals to decide resource access. They are related but independent. Confirm all object IDs and ownership rather than matching only the display name.

Use assigned or dynamic device groups for staged policy/application deployment. A dynamic rule can automate scale and also spread a bad classification quickly. Validate attributes and syntax against representative devices, monitor processing, use pilots and exclusions, and document downstream assignments.

> **Related item:** A stale duplicate Entra device object can make troubleshooting look contradictory. Correlate Entra device ID, Intune managed-device ID, serial number, hardware hash, primary user and last check-in before deleting anything.

### Intune enrollment and platform choices

[Intune enrollment documentation](https://learn.microsoft.com/en-us/intune/device-enrollment/) covers authority, licensing, automatic MDM enrollment, platform restrictions, enrollment limits, corporate identifiers and platform-specific methods. Plan from ownership and experience:

- Windows corporate deployment can use Windows Autopilot/device preparation and automatic MDM enrollment.
- Windows BYOD can register/add a work account under allowed enrollment and management scope.
- Apple Automated Device Enrollment through Apple Business Manager supports supervised corporate enrollment; user/device enrollment choices address other ownership patterns.
- Android Enterprise provides fully managed, corporate-owned work profile, dedicated, and personally owned work-profile modes.
- Samsung Knox Mobile Enrollment and Android zero-touch can automate supported corporate provisioning.

Enrollment restrictions determine which platforms, versions and personally owned devices may enroll. Enrollment profiles and tokens connect external platform services. For Apple, maintain the Apple Push Notification service certificate and enrollment/program token ownership and renewal dates; token expiry can disrupt management. For Android, verify Managed Google Play connection and enrollment-profile status.

Troubleshoot enrollment as a pipeline:

```text
supported OS/device → user license and MDM scope → enrollment restriction/limit
→ platform token/profile → network/service reachability → authentication/CA
→ device identity/ownership → Intune managed-device record → policy check-in
```

Capture Company Portal or OOBE errors, Intune enrollment-failure reports, device-side management logs, time/correlation IDs, and platform service status. Avoid repeatedly deleting/re-enrolling until the failed stage is known; doing so can destroy evidence and create duplicate objects.

### Roles, scope tags, and multi-admin approval

Intune role-based access control combines role permissions, member groups, scope groups, and scope tags. Built-in roles accelerate common delegation; custom roles reduce permissions to an exact job. Windows 365 also has service roles. A role says what actions are allowed, scope groups say which users/devices can be managed, and scope tags control which Intune objects an admin can see/manage.

Test delegated administration with a real low-privilege persona. A scope tag on a configuration profile does not target that profile to devices; assignments do. Conversely, assignment to a device does not give every administrator permission to edit the policy.

Multi-admin approval creates a change-approval workflow for supported high-impact actions. Define request reviewers separately from submitters, approval SLAs, emergency process, change evidence, notification and post-change validation. [Security Copilot agents in Intune](https://learn.microsoft.com/en-us/intune/copilot/agents/) include a Change Review Agent that can make recommendations about approval requests. Administrators remain accountable for the decision; AI output is evidence to validate, not automatic authorization. **VERIFY CURRENT:** supported request types, roles, agent availability and licensing.

### Compliance and Conditional Access

[Intune compliance policies](https://learn.microsoft.com/en-us/intune/intune-service/protect/device-compliance-get-started) assess requirements such as OS version, password, encryption, jailbreak/root state and threat level where supported. The tenant-wide compliance-policy settings define behavior for devices without an assigned policy and the validity period. A grace period delays the noncompliant effect; it does not make the requirement disappear.

Conditional Access can require a device marked compliant. The access decision consumes compliance; it does not configure encryption or patching itself. Use report-only, explicit assignments, emergency exclusions, controlled pilots and sign-in logs. Plan BYOD carefully: an approved app plus app-protection requirement may meet a mobile data-access need without requiring full device enrollment, while sensitive workflows can require a managed/compliant device.

When a device is noncompliant, inspect the device's setting-level result, last check-in, applicable policy, grace period and platform applicability. Then inspect the Conditional Access result for the actual resource sign-in. Do not mark a device manually compliant to hide an unresolved control failure.

### Windows Hello, LAPS, and local groups

[Windows Hello for Business](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/) provides key- or certificate-based strong authentication tied to a user and device, protected by PIN/biometric gesture. Select the deployment trust model and configure via Intune based on identity/hybrid prerequisites. A PIN is local to the device and unlocks protected credentials; it is not a reusable domain password.

[Windows LAPS](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview) rotates a local administrator password and backs it up to Entra ID or AD DS under the chosen design. Define which account is managed, complexity/age, directory backup, authorized retrieval, audit, post-authentication rotation and recovery. Rotating a key/password is a privileged remote action; preserve change/incident context first.

Intune account-protection policies can manage local group membership. Prefer explicit additive/replacement behavior based on the supported setting, pilot carefully, and retain emergency recovery. Endpoint Privilege Management addresses controlled elevation and does not mean every user should be a standing local administrator.

---

## 2. Manage and maintain devices

### Windows Autopilot versus device preparation

[Windows Autopilot](https://learn.microsoft.com/en-us/autopilot/overview) uses a pre-registered device identity, deployment profile and OOBE flow for modes including user-driven, pre-provisioned and self-deploying. The Enrollment Status Page can block use until selected device/user setup completes. Use naming templates within documented limits, assign profiles to controlled groups and validate hardware-hash registration, profile status, network reachability and app dependencies.

The current [Autopilot comparison](https://learn.microsoft.com/en-us/autopilot/device-preparation/compare) distinguishes device preparation from classic Autopilot. Device preparation supports a simpler, near-real-time, Entra-join flow with device-preparation policy and provisioning group; classic Autopilot supports more modes, hybrid join and broader customization. **VERIFY CURRENT:** the comparison changed as recently as August 2026, including device association, automatic mode, limits and government support.

Choose from requirements, not novelty:

| Requirement | Likely design |
|---|---|
| Technician pre-provisions device before handoff | Autopilot pre-provisioned deployment |
| Shared/kiosk device without user credentials during setup | Autopilot self-deploying where supported |
| Hybrid Entra join dependency | Classic Autopilot hybrid deployment, while challenging whether the dependency is still necessary |
| Simpler Entra-join OOBE and near-real-time deployment evidence | Device preparation where current capabilities fit |
| Existing device wipe/reinstall migration | Autopilot for existing devices or other controlled deployment path |

Keep the initial required app/policy set small and reliable. A large blocking list turns one app failure into a provisioning failure. Separate day-zero access/security from day-one convenience. Troubleshoot device identity and policy assignment, then device ESP, user ESP, app detection/requirements/dependencies, certificate/network/time and log evidence.

### Windows 11 upgrades, Backup/Restore, and Cloud PCs

Before Windows 11 upgrade, assess hardware readiness, application and driver compatibility, firmware/security configuration, capacity, user data, rollback and support. Use update rings for servicing behavior and feature-update policies to control the target version. Pilot by representative hardware and workload rather than only IT volunteers.

Windows Backup for Organizations and restore settings in Intune can preserve supported user settings and facilitate organization-managed restore. Treat restore, OneDrive Known Folder Move, application redeployment, device reset and compliance recovery as separate dependencies. Test the user and device lifecycle, data boundary, retention and offboarding behavior. **VERIFY CURRENT:** supported Windows version, setting scope, tenant prerequisites and restore experience.

A [Windows 365 provisioning policy](https://learn.microsoft.com/en-us/windows-365/enterprise/provisioning) combines network choice, join type, image/configuration and assigned user groups to create Cloud PCs. Microsoft-hosted networking reduces customer network dependencies; an Azure network connection is required for specified customer-network and hybrid designs. Use gallery images when possible; custom images add capture, compatibility, replication, update and storage considerations. Validate licenses, policy assignment, ANC health, region/capacity, image state, Entra/AD join, Intune enrollment and user access.

> **Related item:** A Cloud PC is still an endpoint with identity, configuration, compliance, applications, updates, Defender, user-experience and lifecycle concerns. It moves hardware and network responsibility; it does not remove endpoint administration.

### Configuration profiles and targeting

[Intune device configuration](https://learn.microsoft.com/en-us/intune/intune-service/configuration/device-profiles) includes templates, Settings Catalog, custom settings and platform-specific profiles. Prefer current Settings Catalog controls when available. ADMX import can expose supported settings from third-party or Microsoft administrative templates; Group Policy analytics helps identify migration support and does not guarantee behavioral equivalence.

For each setting record requirement, platform/version, configuration service provider or management channel, user/device context, value, assignment, precedence/conflict, rollback and evidence. Separate baseline policies from exceptions. Avoid configuring the same setting through Settings Catalog, security baseline, endpoint-security policy, custom OMA-URI and Group Policy unless the ownership/precedence is deliberate.

Android, Apple and macOS expose platform-specific controls and enrollment dependencies. Specialty devices such as Teams Rooms, HoloLens 2 and Zebra devices require supported enrollment and profile types; do not assume a Windows desktop policy applies. Maintain a capability matrix by platform and version.

Assignment filters include or exclude devices at evaluation based on properties, refining a broad group assignment. Enrollment-time grouping can place supported newly enrolled devices into an appropriate group earlier in provisioning. A filter is not a security group and a scope tag is not a target. Test assignment evidence on the device.

### Intune Suite capabilities

The [Microsoft Intune Suite](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/intune-add-ons) packages advanced capabilities under applicable licensing. Know the problem each solves:

- **Endpoint Privilege Management:** standard users request or receive controlled elevation for approved files/processes; configure rules, evidence, settings and reporting.
- **Enterprise App Management:** Enterprise App Catalog helps discover, package and update supported applications; validate publisher/version, supersedence and deployment evidence.
- **Remote Help:** authenticated, role-controlled assistance with session controls and audit; distinguish view, full control and elevation capabilities.
- **Cloud PKI:** cloud-managed certification authorities and issuance through Intune; design roots/issuers, profiles, lifetime, revocation and recovery before issuing.
- **Microsoft Tunnel for MAM:** provides per-app access for supported unenrolled mobile application-management scenarios; operate gateways, sites, certificates, app/protection configuration and monitoring.
- **Advanced Analytics:** adds anomaly, performance and recommendation insight; validate sample size and act through controlled remediation.

Licensing and availability change. **VERIFY CURRENT:** add-on names, included plans, platform support, role requirements, limits and portal locations.

### Remote actions and support evidence

Choose a remote action from lifecycle intent:

| Action | Intent |
|---|---|
| Sync | Request policy/application check-in |
| Restart | Restart the endpoint; preserve user-work impact |
| Retire | Remove managed company data/settings while respecting platform behavior |
| Wipe | Reset/remove endpoint data according to selected options; high impact |
| Delete | Remove the Intune record; not necessarily erase the physical device |
| Rotate BitLocker recovery key / LAPS password | Replace exposed/retrieved recovery credential |
| Update Defender security intelligence | Accelerate antimalware signature currency |

Bulk actions amplify both benefit and mistake. Validate exact resolved targets, use approval where available, communicate, record the action ID/time/operator, and inspect completion/errors. Never treat “delete from portal” and “securely erase device” as synonyms.

Use device query for near-real-time supported device data with KQL syntax, Intune diagnostics and user-based Troubleshooting to gather state. Correlate Intune audit and operational logs with device-side MDM diagnostics, Windows event logs, app logs, Defender evidence and sign-ins. A stale last check-in often invalidates portal assumptions.

---

## 3. Protect devices

### Endpoint security policy stack

[Intune endpoint security](https://learn.microsoft.com/en-us/intune/intune-service/protect/endpoint-security) provides focused policy surfaces for antivirus, disk encryption, firewall, attack-surface reduction, EDR, account protection and security baselines. Configuration profiles can overlap. Assign each control an owner and avoid conflicting settings.

Microsoft Defender Antivirus policy controls real-time/cloud protection, scanning, exclusions, remediation and update behavior. Exclusions reduce inspection and require narrow documented justification, compensating detection and expiry. Monitor active mode and tamper protection dependencies rather than assuming a policy assignment made Defender the primary antivirus.

Disk encryption policy manages BitLocker and supported platform encryption. Validate silent-enablement prerequisites, TPM, encryption algorithm/startup authentication, escrowed recovery key, self-service recovery, rotation after disclosure and compliance status. A recovery key stored somewhere is not sufficient if unauthorized people can retrieve it or support cannot recover during an outage.

Firewall policies govern profiles, defaults and rules. Prefer default deny for unsolicited inbound traffic with narrow exceptions. Attack-surface reduction includes rules, controlled folder access, exploit protection, application/device controls and related features. Stage high-impact ASR rules in audit/warn where supported, analyze events and line-of-business compatibility, then enforce.

Security baselines provide Microsoft-recommended starting configurations with versioning. Duplicate and test a new baseline version; compare changed settings and exceptions. A baseline is not proof of compliance and does not replace risk analysis.

[Defender for Endpoint and Intune integration](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/overview) connects onboarding, threat signals, EDR policy, machine risk and response. Onboarding establishes telemetry/protection relationship; an EDR policy configures endpoint detection/response settings; compliance can consume machine-risk level; incidents correlate alerts. Diagnose connector state, license, onboarding status, sensor health, policy, network endpoints and device timeline.

App Control for Business uses policy to allow trusted code and constrain untrusted applications. Build from inventory/audit evidence, signer/publisher/file/reputation choices, managed installer and supplemental policy strategy. Poorly tested enforcement can block boot, support or business applications; maintain recovery.

> **Related item:** Zero Trust endpoint protection combines verified identity, device health/compliance, least privilege, application control, data protection and continuous evidence. No single baseline, EDR sensor or compliance badge supplies all of it.

### Update design across platforms

Windows servicing separates update-ring experience/deadlines/restart behavior from feature-update target version and expedited quality updates. Windows Autopatch manages deployment through service-managed groups and rings under current eligibility. Hotpatch can apply eligible security updates without restart on supported editions/builds/configuration, but it still requires a planned baseline and compatibility. **VERIFY CURRENT:** eligibility, licensing, supported releases and cadence.

Plan waves by criticality, hardware/model, application, geography, bandwidth and support. Define pause/rollback criteria and preserve enough pilot time to learn. Delivery Optimization reduces repeated content download by allowing controlled peer/cache behavior; configure mode, groups, cache/limits and network/privacy requirements.

Apple OS update policies through Settings Catalog and Android configuration or OEM/FOTA capabilities vary by enrollment mode, supervision, manufacturer and platform version. Record what is enforced, scheduled, deferred, user-controlled or only reported. Do not promise Windows-style semantics on another platform.

Monitor deployment errors, safeguard/compatibility holds, restart deadlines, version distribution, stale devices and support signals. An update percentage without denominators, exclusions and last check-in can mislead.

---

## 4. Manage and secure applications

### Application packaging, assignment, and troubleshooting

Choose the Intune app type from source and installation behavior:

- Win32 apps use the Intune content-preparation format with install/uninstall commands, requirements, detection rules, dependencies, supersedence and return codes.
- line-of-business apps use supported package types and simpler deployment behavior.
- Microsoft Store apps use current Store integration and application identifiers.
- Microsoft 365 Apps can be configured/deployed through Intune, Office Deployment Tool/configuration XML and current Microsoft 365 Apps management surfaces.
- Apple Apps and Books/Volume Purchase and Managed Google Play integrate store licensing and managed deployment.

Assignments can be required, available or uninstall for applicable targets. User/device context, architecture, OS version, dependencies and filter determine the actual path. Detection rules prove whether the desired version is installed; a weak file-exists rule can report success after an incomplete install. Supersedence describes upgrade/replacement relationships; dependencies describe prerequisites.

Troubleshoot app deployment:

1. verify assignment resolves to the user/device and no filter/exclusion wins;
2. verify app type, intent, install context, requirement and dependency;
3. inspect device check-in and Intune Management Extension state where applicable;
4. inspect download/network/storage/certificate and installation logs;
5. inspect command line, exit code and reboot behavior;
6. evaluate detection rule after installation;
7. compare a working device and validate rollback/uninstall.

Quiet Time policies for supported Android/iOS experiences suppress work notifications on configured schedules; they do not uninstall or block the application. Confirm platform/application support and user communication.

### Microsoft 365 Apps lifecycle

Define architecture, apps, languages, update channel, version, shared-computer activation and existing-install migration. Deploy during Autopilot only if reliable day-zero requirements justify provisioning delay. Office Deployment Tool can create controlled installation configurations; Intune and Microsoft 365 Apps admin center can deploy/manage policy and update behavior under current capabilities.

Separate install configuration from Office cloud policy and security baselines. Diagnose assignment, network/CDN, conflicting architecture/version, update channel, service plan/activation and application-health evidence. **VERIFY CURRENT:** Cloud Update, servicing profile and admin-center names/capabilities.

### App protection and app configuration

[Intune app protection policies](https://learn.microsoft.com/en-us/intune/intune-service/apps/app-protection-policy) manage organizational data in supported applications, including on enrolled and unenrolled devices. Controls can require PIN/biometric, encrypt app data, restrict copy/paste/save/open-in, require minimum app/OS state and selectively wipe corporate data. MAM protects an application data boundary; it does not make the entire personal device compliant.

Conditional Access can require an approved client app and/or app protection policy for supported mobile access. Build the app policy, deploy to a test population, validate supported applications and broker/authenticator prerequisites, then stage Conditional Access. Preserve a supported onboarding path so the policy does not block the user before protection can apply.

App configuration policies deliver application settings. Managed-device configuration uses the MDM channel; managed-app configuration can target the MAM/application channel. A configuration policy does not enforce data transfer rules unless the corresponding app-protection capability does. Confirm key/value schema, application version, target/context and result.

> **Related item:** Selective wipe removes organizational data managed by the app policy; device wipe resets the endpoint. Choose from ownership, incident scope, legal requirement and recoverability.

---

## 5. Optimize endpoint operations with automation, monitoring, and reporting

### PowerShell and Microsoft Graph automation

[Microsoft Graph Intune APIs](https://learn.microsoft.com/en-us/graph/api/resources/intune-graph-overview) expose supported device/app management objects and actions. Choose delegated access for an interactive operator or application access for unattended automation. Use the least permission, protected credentials or managed identity where available, controlled consent, owner, audit, change review and expiry.

Safe automation is idempotent, scoped, observable and recoverable:

1. query and export the candidate set;
2. validate stable object IDs, counts and protected exclusions;
3. use read-only/dry-run behavior where available;
4. handle pagination, throttling, retries and partial failure;
5. log request/time/operator/object/result without leaking secrets;
6. make the change in bounded batches;
7. verify desired and undesired outcomes and retain rollback input.

PowerShell can call Graph and device-management cmdlets/modules, but module names and API versions change. Prefer supported endpoints, pin/test dependencies and do not assume a portal feature is available through the same API or permission. Custom compliance uses a discovery script plus JSON rules under supported platforms: return deterministic, minimal data; sign/test scripts; handle errors; avoid secrets; and monitor failure separately from noncompliance.

### Security Copilot agents in Intune

The July objectives specifically require investigating threats, analyzing device performance and responding to recommendations from Security Copilot agents in Intune. The [official agent overview](https://learn.microsoft.com/en-us/intune/copilot/agents/) says agents operate within Intune with role-based access and administrator oversight. **VERIFY CURRENT:** available agents, permissions, data access, actions, capacity/licensing, preview/GA status and geography.

Treat a recommendation as a hypothesis with evidence:

- identify the agent, requested/observed inputs, time range and affected device set;
- inspect cited Intune/Defender/analytics evidence and compare with a known-good cohort;
- determine confidence, false-positive cost and blast radius;
- require approval for material changes and use pilots;
- record accept/reject rationale, actual change and measured result;
- report agent errors or unsafe recommendations and retain human override.

Do not paste sensitive device data into an unapproved AI service. Agent action remains constrained by identity, Intune roles, scope and current product controls; it does not transfer administrator accountability.

### Reporting, Endpoint Analytics, and remediations

Intune reports include operational, organizational and historical views with filters, export and platform-specific detail. Azure Monitor/Log Analytics integration and workbooks can support retained/custom analysis for exported diagnostic categories. Define report freshness, time zone, denominator, ownership and response before building a dashboard.

[Endpoint Analytics](https://learn.microsoft.com/en-us/intune/monitor-troubleshoot) measures supported startup, application reliability and user-experience signals and provides scores/insights. Compare cohorts and trends rather than treating one score as a verdict. Sampling, device eligibility, check-in and workload pattern affect interpretation.

Remediations use a detection script and a remediation script on a schedule under the configured context. Write detection to be side-effect free and return documented exit/output. Make remediation idempotent, narrowly scoped and logged; sign scripts when required; test locally and in a pilot; preserve rollback; monitor recurring failures. A “successful remediation” exit code must be confirmed by a subsequent desired-state check.

Advanced Analytics can surface anomalies and risk-based recommendations. Correlation is not root cause. Compare versions, hardware, apps, policy, location and time; reproduce; then pilot the proposed change.

Monitor tenant status and Intune service communications alongside Message center and Microsoft 365 Service Health. Establish operational baselines for enrollment success, compliance drift, policy conflicts, app failure, update currency, check-in, performance and support. Configure alerts/notifications where supported, but assign an owner and response runbook—an unread alert is not a control.

> **Related item:** Policy assignment success, device check-in, setting application, compliance, resource access and user experience are distinct outcomes. A mature endpoint dashboard shows the chain rather than one green percentage.

---

## Integrated scenarios

### Scenario 1: BYOD mobile access without full enrollment

The business permits Outlook and Teams on personal phones but forbids corporate data in personal apps/storage. Select supported apps, deploy app-protection and managed-app configuration to a pilot, require an approved/protected app with Conditional Access, validate broker/authentication prerequisites, copy/paste/save/open-in and selective wipe across Android/iOS. Test both allowed and denied flows. Do not call the device compliant unless it is actually enrolled and evaluated by compliance policy.

### Scenario 2: Autopilot provisioning fails after an app update

Identify device/hardware hash, assigned profile, deployment mode, group/filter and ESP stage. Inspect the blocking app's content version, requirements, dependencies, install context/command, exit code and detection. Compare a successful device. Restore a known-good package or make a justified nonessential app non-blocking, then retest positive and negative paths. Preserve logs before reset.

### Scenario 3: Security agent recommends a fleet-wide change

The agent reports application crashes and recommends removing an endpoint-security rule. Validate affected cohort/time/version, raw analytics and Defender evidence, current policy conflicts and a known-good group. Consider a scoped rule exception, application update or configuration correction before broad security reduction. Put the selected change through multi-admin approval, pilot it, measure reliability and risk, and record rejection/acceptance rationale.

---

## Hands-on labs

Use disposable tenants/devices or virtual machines and synthetic data. Licensing for Intune Suite, Windows 365, Defender and Security Copilot varies; tabletop an unavailable feature with official evidence rather than changing production.

### Lab 1 — Device identity and enrollment matrix

Register a BYOD device and join a corporate Windows test VM where supported. Enroll through Intune and record Entra device ID, managed-device ID, ownership, primary user, compliance and check-in. **Evidence:** matrix showing join, enrollment, compliance and access as separate states.

### Lab 2 — Delegation, compliance, and access

Create a limited Intune role assignment with scope group/tag, a compliance policy and report-only Conditional Access policy. Test with operator and device personas. **Evidence:** permission matrix, setting-level compliance, sign-in policy result, exception and rollback.

### Lab 3 — Autopilot design and failure analysis

Design classic Autopilot and device-preparation options for user-driven, shared and technician-prepared requirements. If hardware is available, deploy one flow with minimal essential apps. **Evidence:** requirement decision, assignments, deployment report, failure log and recovery.

### Lab 4 — Configuration and Intune Suite control

Deploy one Settings Catalog profile with a filter and model one EPM, Remote Help, Cloud PKI or Tunnel control. Introduce a safe test conflict and identify precedence/result. **Evidence:** resolved targets, per-setting result, operator/audit record and rollback.

### Lab 5 — Endpoint security and updates

Deploy antivirus/ASR in audit or safe pilot, encryption requirement and update-ring/feature policy. Verify Defender onboarding and recovery-key escrow with authorized roles. **Evidence:** policy/effective state, event/report, recovery test, update status and enforcement criteria.

### Lab 6 — Win32 app lifecycle

Package a harmless app with requirements, dependency, detection, install/uninstall and supersedence. Create a deliberate detection failure and troubleshoot it. **Evidence:** package contract, logs/exit code, resolved assignment, corrected detection and rollback.

### Lab 7 — MAM for an unmanaged device

Deploy app protection/configuration and report-only Conditional Access to test users. Validate corporate/personal copy, save, open-in, PIN and selective wipe. **Evidence:** test matrix and sign-in/app policy evidence with no production data.

### Lab 8 — Safe automation and operational dashboard

Use Graph/PowerShell to export a bounded device inventory, handling pagination and errors without mutation. Design a remediation detection/fix pair and dashboard for enrollment, compliance, update, app, reliability and service health. **Evidence:** sanitized code/output, dry-run target set, rollback plan, metrics and alert runbook.

---

## Knowledge checks

1. **Join versus enrollment?** Join/register creates Entra device identity; enrollment establishes Intune management.
2. **Can a joined device be noncompliant?** Yes. Compliance is a separate evaluated state.
3. **Best typical identity for a personal mobile device?** Entra registration, with MAM or enrollment selected from the data/control requirement.
4. **Why validate dynamic groups?** A wrong rule rapidly misassigns every downstream policy/app.
5. **First enrollment checks?** License/MDM scope, restrictions/limit, platform token/profile, authentication/network, identity and device logs.
6. **What does a scope tag do?** Controls delegated visibility/administration of tagged Intune objects; it does not target devices.
7. **What does a compliance policy do?** Evaluates device requirements and reports state; Conditional Access consumes that state for access.
8. **Why use report-only Conditional Access?** To observe policy impact before enforcement.
9. **Is Windows Hello PIN a password?** No; it unlocks device-bound key material.
10. **Why rotate LAPS after retrieval?** A disclosed recovery credential should have a bounded useful lifetime.
11. **EPM versus local administrator?** EPM enables governed elevation; standing local admin grants broad ongoing privilege.
12. **Autopilot device preparation versus classic Autopilot?** Device preparation favors simpler Entra-join flows/current near-real-time reporting; classic supports more modes/hybrid and customization.
13. **What should ESP block?** Only reliable, essential day-zero apps/settings needed before use.
14. **Why assess Windows 11 readiness by cohort?** Hardware, driver and application compatibility differ across fleet segments.
15. **What composes a Cloud PC provisioning policy?** Network/join choice, image/configuration and user-group assignment.
16. **Does Cloud PC remove endpoint management?** No; it remains an identity/configuration/security/app/update lifecycle.
17. **Filter versus group?** A filter refines an assignment during evaluation; it is not a membership container.
18. **Why avoid duplicate settings across policy surfaces?** Overlap causes conflict, unclear precedence and unsafe rollback.
19. **What does Cloud PKI require beyond creating a CA?** Hierarchy, issuance profiles, authorization, lifetime, revocation, monitoring and recovery.
20. **Retire versus wipe?** Retire removes managed corporate data/settings according to platform behavior; wipe resets/erases more broadly.
21. **Why are bulk actions dangerous?** A targeting error becomes a fleet-wide destructive change.
22. **What proves BitLocker readiness?** Effective encryption plus authorized, tested recovery-key escrow/retrieval.
23. **How should ASR enforcement begin?** Audit/warn and compatibility analysis where supported, followed by staged enforcement.
24. **Onboarding versus EDR policy?** Onboarding connects device telemetry/protection; EDR policy configures behavior.
25. **What is an update ring?** Servicing experience, deadlines and restart behavior—not the same as a feature-update target.
26. **Hotpatch means never restart?** No. Supported cycles still require baselines and current eligibility.
27. **What makes Win32 detection critical?** It is Intune's proof that the required application state exists.
28. **Dependency versus supersedence?** Dependency is prerequisite; supersedence upgrades/replaces another app.
29. **App protection versus app configuration?** Protection governs data/use; configuration supplies app settings.
30. **Selective wipe versus device wipe?** Selective wipe removes managed organizational app data; device wipe affects the endpoint broadly.
31. **Minimum safe Graph automation pattern?** Query/validate targets, least privilege, bounded batches, error/throttle handling, logs, verification and rollback.
32. **How should agent recommendations be used?** As evidence-backed hypotheses requiring role-appropriate human review and measured change.
33. **What does Endpoint Analytics show?** Supported performance/experience signals; it does not by itself prove root cause.
34. **Good remediation design?** Side-effect-free detection and idempotent, scoped, logged, tested fix with rollback.
35. **Why baseline operations?** An alert or score needs a known normal range and response owner.
36. **What proves endpoint policy success?** Intended target resolves, device checks in, setting applies, compliance/access behave, user outcome is acceptable and negative path remains blocked.

---

## Places to learn

This is a curated starting point, **not a complete list**. It is not meant to be consumed in full. Choose one current primary route, build a real lab, and use assessment results plus the July 2026 blueprint to select supplements. Older MD-102 courses may omit Intune Suite, device preparation changes, automation/reporting, and Security Copilot agents.

The eight official paths linked from the current MD-102 course total **29 hours 46 minutes** before labs and review.

They are [prepare infrastructure](https://learn.microsoft.com/en-us/training/paths/prepare-infrastructure-devices-intune-microsoft-entra-id/) (4h44), [manage and maintain devices](https://learn.microsoft.com/en-us/training/paths/manage-maintain-devices-intune/) (3h56), [manage applications](https://learn.microsoft.com/en-us/training/paths/manage-applications-intune/) (4h45), [protect devices](https://learn.microsoft.com/en-us/training/paths/protect-devices-intune/) (5h02), [automate and optimize](https://learn.microsoft.com/en-us/training/paths/automate-optimize-endpoint-management-intune/) (2h36), [support operational excellence](https://learn.microsoft.com/en-us/training/paths/support-operational-excellence-intune/) (2h15), [extend with Intune Suite](https://learn.microsoft.com/en-us/training/paths/extend-intune-suite/) (3h13), and [deliver cloud-hosted desktops](https://learn.microsoft.com/en-us/training/paths/deliver-cloud-hosted-desktops/) (3h15).

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MD-102 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/modern-desktop/) | Public | 1–2 hours initially; 15 minutes on each recheck |
| Eight self-paced paths from [MD-102T00](https://learn.microsoft.com/en-us/training/courses/md-102t00) | Public | 29 hours 46 minutes listed; allow 45–70 hours with exercises, device testing and notes |
| MD-102T00 instructor-led course | Paid/partner delivery | 5 days listed |
| [Microsoft MD-102 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/modern-desktop/practice/assessment?assessment-type=practice&assessmentId=76&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Pluralsight MD-102 path](https://www.pluralsight.com/paths/microsoft-windows-endpoint-administrator-md-102) with Glenn Weadock | Paid | 13 hours across five courses plus a practice exam; 2026 core courses are current, but verify July agent/automation coverage |
| [O'Reilly/Packt MD-102 video](https://www.oreilly.com/videos/md-102-endpoint-administrator/9781836208396/) | Paid | 23 hours 14 minutes; May 2024 foundation that needs all July 2026 changes supplemented |
| [Udemy MD-102 full course](https://www.udemy.com/course/microsoft-certified-endpoint-administrator-md-102/) | Paid | 15 hours 50 minutes; updated February 2026, so supplement the July blueprint changes |
| [Udemy current-blueprint practice](https://www.udemy.com/course/md-102-practice-exam-2026-6-endpoint-administrator-tests/) by Joshua Ravnjak | Paid | 180 original questions; allow about 6–10 hours for attempts and source-based remediation; updated August 2026 |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics) and [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor) | Public | 2–8 hours selectively for current Intune, Windows, Entra and Defender demonstrations; not a fixed MD-102 course |
| [John Savill's Technical Training](https://www.youtube.com/@NTFAQGuy) and [public repositories](https://github.com/johnthebrit) | Public | 2–8 hours selectively for Entra, Conditional Access, Windows 365, security and architecture foundations; no exact current MD-102 path confirmed |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use the listed event start/end times after partner sign-in |

No exact current Whizlabs or MeasureUp MD-102 product page was independently verified during this review, so neither is inferred. Never use resources claiming recalled live questions. Start with Microsoft's free Practice Assessment; add a paid bank only when its explanations and question style close a specific gap.

## Final readiness checklist

- I can explain every objective as a target, configuration, effective-state check, failure mode, evidence source and recovery.
- I can separate device identity, enrollment, ownership, compliance, application protection and resource access.
- I can enroll and troubleshoot Windows, Android, Apple and macOS using appropriate corporate/BYOD methods.
- I can choose and operate Autopilot/device preparation, profiles, Intune Suite controls, remote actions and Windows 365.
- I can deploy endpoint security/update policy with pilots, recovery and cross-platform limitations.
- I can package, assign, detect, update, protect, configure, selectively wipe and troubleshoot applications.
- I can automate with Graph/PowerShell safely and evaluate Security Copilot agent recommendations with human accountability.
- I can turn reporting, analytics, remediations, alerts and service communication into an owned operational loop.
- I completed or tabletop-tested all eight labs and can prove both allowed and denied outcomes.
- I passed an independent readiness check without relying on recalled live-exam content.
