---
exam_code: MD-102
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: review-required
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# MD-102 Managing and Securing Microsoft 365 Endpoints by Using Intune Study Guide

> **Independent AI-assisted resource — HUMAN REVIEW PENDING.** The October 28, 2026 team refresh reconciles the complete guide and detailed objectives with current public exam, product and learning evidence. See the [current group report](../docs/research/2026-10-28-microsoft-refresh-group-02.md#md-102) and [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#md-102-coverage-record). Source conflicts and unexecuted exercises remain explicit. This is not human review or live product validation. The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102) is authoritative.

**Current baseline:** Skills measured as of October 27, 2026.<br>
**Blueprint reconciliation (October 28, 2026):** The October 27, 2026 English outline is the accepted current scope. The revision clarifies Android work-profile ownership and current Windows Backup, Microsoft Tunnel VPN Gateway, Microsoft 365 apps, Apple Business Manager, Managed Google Play and Remediations wording. It corrects local-administrator-password terminology; weights are unchanged. Historical objective bytes and dated reviews are preserved. Recheck localized appointment timing separately.<br>
**Exam:** 100 minutes; seven exam languages; annual certification renewal. The official instructor-led course is five days.

**Official source:** [MD-102 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102)

## October 28 implementation notes

**Related item:** **Confirmed — VERIFY CURRENT (October 28, 2026).** On applicable Windows 11/Server 2025 systems with Credential Guard disabled, October 13 updates make an absent BlockNtlmv1SSO value enforce blocking of NTLMv1-derived SSO credentials. Check Wi-Fi/Ethernet/VPN MS-CHAPv2 dependencies and NTLM Operational events 4024/4025. An absent key no longer means audit-only, and manual credential entry may still work. Migrate toward supported certificate authentication; any temporary audit exception needs a scoped owner and removal date. [Windows message center](https://learn.microsoft.com/en-us/windows/release-health/windows-message-center) · [Manage NTLMv1 changes and prevent network authentication issues in Windows](https://support.microsoft.com/en-us/servicing/os/windows/docs/2025/08/upcoming-changes-to-ntlmv1-in-windows-11-version-24h2-and-windows-server-2025)

**Confirmed — VERIFY CURRENT (October 28, 2026).** Intune's Windows 11 26H2 security baseline is available; existing profiles do not automatically adopt it. For May 2023-or-later profiles, updating creates a new instance with a keep/discard-customizations choice; review settings and assign/test deliberately before retiring the old assignment. Do not assume the copy is deployed or every planned 26H2 setting is included. The October release excludes Configure NetBIOS settings pending supported in-market availability. [What's new in Microsoft Intune](https://learn.microsoft.com/en-us/intune/whats-new/) · [Configure security baseline policies in Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-security/security-baselines/configure-baselines)

These dated operational notes supplement the current objective treatment. Product and tenant exercises were not run; unresolved source and support gaps remain stated at the affected topic.

## How to use this guide

MD-102 tests endpoint operations across Windows, Android, iOS/iPadOS, macOS, specialty devices, and Cloud PCs. The current October outline retains the substantial July expansion in Intune Suite, automation, analytics, reporting, and Security Copilot agent depth. Older four-domain material remains useful but is incomplete.

For every scenario, trace:

1. **Ownership and platform:** corporate or personal, physical or Cloud PC, OS/device type, lifecycle stage.
2. **Identity and enrollment:** Entra registered/joined/hybrid joined, MDM/MAM enrollment, platform enrollment method.
3. **Targeting:** user/device group, assignment intent, filter, enrollment-time grouping, scope tag.
4. **Policy and application:** effective configuration, compliance, endpoint-security, update, app, and protection policies.
5. **Access decision:** authentication, Conditional Access, device compliance, app protection, resource authorization.
6. **Evidence and action:** Intune status, sign-in and Defender evidence, reports/KQL/logs, remote action, rollback and recovery.

Do not diagnose from one portal badge. A device can be Entra joined but not Intune enrolled, enrolled but noncompliant, compliant but blocked by another Conditional Access control, or allowed to sign in while a managed application fails. Record UTC time, user, device IDs, serial number, platform, policy, assignment and error before changing configuration.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

### Living-guide watch — September 27, 2026

Use [What's new in Microsoft Intune](https://learn.microsoft.com/en-us/intune/whats-new/) as a weekly service-change feed, not as an expanded exam outline. It currently labels the former Microsoft Intune Suite as **Advanced capabilities** and notes staged tenant rollout. Preserve the blueprint term where needed for recognition, then map it to the current label and verify tenant availability before a lab.

The [Agent 365 GA announcement](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) supplies adjacent control-plane context; it does not prove that every Security Copilot or Intune agent feature is GA. Independent endpoint training in Places to learn is useful for alternate demonstrations, with the weekly feed deciding volatile names and behavior.

The September review observed a **week of September 28** feed section before its rollout week. That timing observation is historical as of October 28; verify actual feature rollout and preview status in current documentation and the tenant. The September 21 deployment-plan observation was public preview at that review. Faster Windows compliance evaluation announced September 14 does not make every exported report real-time.

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

Conditional Access can require a device marked compliant. The access decision consumes compliance; it does not configure encryption or patching itself. Use report-only, explicit assignments, emergency exclusions, controlled pilots and sign-in logs. Plan BYOD carefully: an app-protection requirement in a supported app may meet a mobile data-access need without requiring full device enrollment, while sensitive workflows can require a managed/compliant device.

When a device is noncompliant, inspect the device's setting-level result, last check-in, applicable policy, grace period and platform applicability. Then inspect the Conditional Access result for the actual resource sign-in. Do not mark a device manually compliant to hide an unresolved control failure.

#### Worked example — compliance rate needs coverage and time

A report contains 90 compliant and 10 noncompliant devices, while the expected fleet is 120 devices. The reported-device compliance rate is **90/100 = 90%**; confirmed compliant coverage of the expected fleet is **90/120 = 75%**. The other 20 are unobserved, not automatically noncompliant or compliant. Deduplicate by stable device ID and state timestamp before counting. Keep stale, excluded and not-yet-evaluated cohorts visible.

[Client-driven evaluation](https://learn.microsoft.com/en-us/intune/device-security/compliance/create-policy) can request reevaluation after supported Windows state changes. That request is not completed enforcement, nor does it accelerate the daily Azure Monitor snapshot into an immediate feed. Some [health-attestation settings](https://learn.microsoft.com/en-us/intune/device-security/compliance/ref-windows-settings), such as the documented BitLocker compliance measurement, still depend on boot-time evidence. Validate the actual setting and sign-in result.

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

**Device-preparation limits — VERIFY CURRENT:** The [comparison](https://learn.microsoft.com/en-us/autopilot/device-preparation/compare) lists user-driven/automatic modes, Entra join, 25 essential apps, ten scripts and device-based OOBE. Its lower requirements table still conflicts on installing more than ten apps; the [January 30 release entry](https://learn.microsoft.com/en-us/autopilot/device-preparation/whats-new) explicitly confirms 25 for both modes. Keep deployment-timeout testing. Device preparation needs an Intune Provisioning Client-owned provisioning group. For a classic-registered device, **tenant association selects device preparation; without association the classic profile wins**. Supported old build rows do not prove lifecycle support.

**Proposed practice extension — not executed:** Lab 3: compare registered+associated versus registered+unassociated device designs, document selected flow and avoid deregistering real devices. Record app count, timeout and source-table discrepancy.

**Answer checkpoint:** Does classic Autopilot registration always take precedence? No: current comparison makes tenant association decisive for device preparation.

### Windows 11 upgrades, Backup/Restore, and Cloud PCs

Before Windows 11 upgrade, assess hardware readiness, application and driver compatibility, firmware/security configuration, capacity, user data, rollback and support. Use update rings for servicing behavior and feature-update policies to control the target version. Pilot by representative hardware and workload rather than only IT volunteers.

Windows Backup for Organizations and restore settings in Intune can preserve supported user settings and facilitate organization-managed restore. Treat restore, OneDrive Known Folder Move, application redeployment, device reset and compliance recovery as separate dependencies. Test the user and device lifecycle, data boundary, retention and offboarding behavior. **VERIFY CURRENT:** supported Windows version, setting scope, tenant prerequisites and restore experience.

A [Windows 365 provisioning policy](https://learn.microsoft.com/en-us/windows-365/enterprise/provisioning) combines network choice, join type, image/configuration and assigned user groups to create Cloud PCs. Microsoft-hosted networking reduces customer network dependencies; an Azure network connection is required for specified customer-network and hybrid designs. Use gallery images when possible; custom images add capture, compatibility, replication, update and storage considerations. Validate licenses, policy assignment, ANC health, region/capacity, image state, Entra/AD join, Intune enrollment and user access.

> **Related item:** A Cloud PC is still an endpoint with identity, configuration, compliance, applications, updates, Defender, user-experience and lifecycle concerns. It moves hardware and network responsibility; it does not remove endpoint administration.

#### Worked example — backup enabled does not mean restore ready

[Windows settings backup and restore](https://learn.microsoft.com/en-us/windows/configuration/windows-backup/) is the newer name for Windows Backup for Organizations. On an eligible 26H2 device, the announced default enables backup when policy is Not Configured; an explicit Disabled policy still wins. Restore remains separately enabled by an administrator. A second eligible device with backup Enabled but restore Disabled can collect a profile without offering the intended restore experience. Check version, region/cloud and identity rather than generalizing the default to every Windows PC.

The [backup FAQ](https://learn.microsoft.com/en-us/windows/configuration/windows-backup/faq) limits this feature to supported Windows settings and the Microsoft Store app list. Protect user files separately, for example with OneDrive; do not treat this as an image or arbitrary application-data backup. Backup supports joined/hybrid devices; OOBE restore requires Entra join and supported user-driven setup. The newer first-sign-in restore path can support joined/hybrid devices on specified builds after enrollment. Test these paths independently and use the same work account. For nonpersistent VDI/shared Cloud PCs, evaluate profile persistence instead of repeatedly restoring a disposable session.

### Configuration profiles and targeting

[Intune device configuration](https://learn.microsoft.com/en-us/intune/intune-service/configuration/device-profiles) includes templates, Settings Catalog, custom settings and platform-specific profiles. Prefer current Settings Catalog controls when available. ADMX import can expose supported settings from third-party or Microsoft administrative templates; Group Policy analytics helps identify migration support and does not guarantee behavioral equivalence.

For each setting record requirement, platform/version, configuration service provider or management channel, user/device context, value, assignment, precedence/conflict, rollback and evidence. Separate baseline policies from exceptions. Avoid configuring the same setting through Settings Catalog, security baseline, endpoint-security policy, custom OMA-URI and Group Policy unless the ownership/precedence is deliberate.

Android, Apple and macOS expose platform-specific controls and enrollment dependencies. Specialty devices such as Teams Rooms, HoloLens 2 and Zebra devices require supported enrollment and profile types; do not assume a Windows desktop policy applies. Maintain a capability matrix by platform and version.

Assignment filters include or exclude devices at evaluation based on properties, refining a broad group assignment. Enrollment-time grouping can place supported newly enrolled devices into an appropriate group earlier in provisioning. A filter is not a security group and a scope tag is not a target. Test assignment evidence on the device.

#### Worked profile selection — platform, enrollment and result

**Original example — proposed; service/tenant execution not performed.**

Use one synthetic requirement per supported platform and document the exact setting available in the tenant:

| Cohort | Pilot profile decision | Verification |
|---|---|---|
| Android dedicated corporate device | Supported Android Enterprise kiosk template and approved app set | One intended app works; escape/unapproved app path fails as designed |
| Supervised corporate iPad | A supported iOS/iPadOS Wi-Fi or device-restriction template | Enrollment/supervision prerequisite holds; setting-level result matches |
| Corporate macOS device | A macOS Wi-Fi or supported Settings Catalog configuration | Correct platform payload arrives and a clean connection succeeds |
| Teams Room, HoloLens or Zebra specialty device | Device-specific supported profile/OEM setting after checking its support matrix | Actual appliance function works; a desktop setting is not presumed applicable |

For each row, create the matching platform/profile type, set one supported value, assign a tiny test group refined by a filter if appropriate, and inspect device and per-setting status. Record Not applicable, Conflict, Error and Pending separately; do not recast them as success. Roll back the test assignment and verify the restored state. This is a design exercise unless the learner records actual device evidence.

**Related item:** custom/imported profile fields can expose embedded secrets to users/apps with profile-read permissions; Base64 is encoding, not protection. Prefer certificate-based access and restrict configuration-read roles.

**Question:** Does a scope tag deploy a profile to the macOS pilot?

**Answer:** No. Assignments and filters select devices; scope tags govern administrator visibility and management.

[Microsoft Intune device configuration profiles](https://learn.microsoft.com/en-us/intune/intune-service/configuration/device-profiles)

### Intune Suite capabilities

The [Microsoft Intune Suite](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/intune-add-ons) packages advanced capabilities under applicable licensing. Know the problem each solves:

- **Endpoint Privilege Management:** standard users request or receive controlled elevation for approved files/processes; configure rules, evidence, settings and reporting.
- **Enterprise App Management:** Enterprise App Catalog helps discover, package and update supported applications; validate publisher/version, supersedence and deployment evidence.
- **Remote Help:** authenticated, role-controlled assistance with session controls and audit; distinguish view, full control and elevation capabilities.
- **Cloud PKI:** cloud-managed certification authorities and issuance through Intune; design roots/issuers, profiles, lifetime, revocation and recovery before issuing.
- **Microsoft Tunnel for MAM:** provides per-app access for supported unenrolled mobile application-management scenarios; operate gateways, sites, certificates, app/protection configuration and monitoring.
- **Advanced Analytics:** adds anomaly, performance and recommendation insight; validate sample size and act through controlled remediation.

Licensing and availability change. **VERIFY CURRENT:** add-on names, included plans, platform support, role requirements, limits and portal locations.

**Remote Help scope:** [Unattended Windows support](https://learn.microsoft.com/en-us/intune/remote-help/plan) requires a physical, corporate-owned, Intune-managed x64 device with Entra join or hybrid join and a specifically scoped unattended remote-sign-in permission. Windows 365/AVD, BYOD and virtual devices are excluded from that mode even where attended help works. Validate IME, the required AVD agent/bootloader, Remote Desktop and power/network prerequisites. Ordinary full-control permission alone is insufficient; a sleeping device cannot accept the request.

#### Worked advanced-capability workflows

**Original example — proposed; service/tenant execution not performed.**

**VERIFY CURRENT:** licenses, supported platforms and tenant availability precede these disposable pilots.

- **EPM:** deploy an elevation-settings policy that enables EPM, then a narrowly identified elevation rule for a harmless signed utility. Prefer a protected path and user-confirmed or support-approved elevation. Inspect elevation reports and test an altered binary and child process. Permitting all elevated children bypasses their own rule evaluation, including deny rules.
- **Enterprise App Catalog:** select the exact publisher, architecture, language and version, inspect supplied install/requirements/detection defaults, assign a pilot, and verify detected installation. Catalog packaging is not a grant of the application's commercial rights or an organizational security approval. Review a new version and its supersedence separately.
- **Cloud PKI:** choose a cloud root/issuing hierarchy or BYOCA design, distribute the required trust chains, configure a SCEP device profile and target the test cohort. Verify issued subject, issuer, EKU, validity and the relying party's trust, then tabletop revocation. Issuing a client certificate does not supply the Wi-Fi/VPN server's TLS certificate.
- **Android Tunnel for MAM:** establish the existing gateway/site first, then deploy Defender app configuration, Edge app configuration and Edge app protection to the same test-user group. Install required client/broker apps even though the device remains unenrolled. Verify organizational access and work/personal identity switching. MAM Tunnel does not support Always-on VPN; its Edge Strict Tunnel Mode has a different scope from the enrolled-device setting.

For each workflow retain resolved targets, effective setting, user action, log/report, failure case and cleanup. Creation success alone proves neither elevation safety, installed app, trusted certificate nor reachable private resource.

**Question:** Can creating a Cloud PKI issuing CA alone make VPN authentication work?

**Answer:** No. Deploy the client certificate and both sides of the trust chain, configure the VPN/relying party, and test identity, EKU, validity and revocation.

[Creating elevation rules with Endpoint Privilege Management](https://learn.microsoft.com/en-us/intune/epm/create-elevation-rules) · [Add an Enterprise App Catalog App to Microsoft Intune](https://learn.microsoft.com/en-us/intune/intune-service/apps/apps-add-enterprise-app) · [Microsoft Cloud PKI deployment for Microsoft Intune](https://learn.microsoft.com/en-us/intune/cloud-pki/deployment-models) · [Microsoft Tunnel for Mobile Application Management for Android](https://learn.microsoft.com/en-us/intune/intune-service/protect/microsoft-tunnel-mam-android)

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

### Distinguish live device queries from fleet inventory

[Single-device query](https://learn.microsoft.com/en-us/intune/advanced-analytics/device-query) contacts a supported corporate Windows device through mandatory Windows Push Notification Services. It requires the appropriate query permission, supported join/management and Advanced Analytics entitlement. Failure to reach the device is not a zero-row statement about its health. KQL is a supported subset, with result truncation and query limits; do not blindly transplant a Sentinel query.

[Multiple-device query](https://learn.microsoft.com/en-us/intune/advanced-analytics/device-query-multiple-devices) examines collected inventory across supported corporate platforms. Windows needs a properties-catalog collection policy. Check inventory age and missing-device coverage before creating an assignment group from results. Tables can contain several components per device: counting CPU or disk rows is not necessarily counting distinct devices.

#### Worked device query — rows are not fleet coverage

**Original example — proposed; service/tenant execution not performed.**

Select one eligible, reachable corporate Windows device and run:

~~~kusto
OsVersion
| take 5
~~~

Then compare:

~~~kusto
DiskDrive
| count
~~~

The first inspects OS-version data on the selected endpoint; the second counts returned disk records. A result of 2 means two disk rows on that device, not two managed devices. Inspect the returned schema before projecting properties and preserve the selected device ID, time and result limits. A WNS/connectivity or permission failure is not a zero-disk result. **VERIFY CURRENT:** supported KQL subset, properties and truncation limits. This read-only example does not trigger a remote action.

**Question:** Does DiskDrive | count returning 2 prove two healthy devices?

**Answer:** No. It counts disk records from one selected device and says nothing about unqueried fleet members.

[Device query](https://learn.microsoft.com/en-us/intune/advanced-analytics/device-query)

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

#### Worked example — hotpatch eligibility is an intersection

For an illustrative 100-device group, 80 have the required baseline, 90 have VBS running, and 75 satisfy both. Only those **75** pass these two prerequisites, not `min(80, 90) = 80`; supported OS, architecture, licensing and policy must also hold. A September hotpatch policy cannot guarantee no restart for the other devices. [Hotpatch guidance](https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/manage/windows-autopatch-hotpatch-updates) explains standard cumulative-update fallback and baseline restarts; additional baseline months can occur.

For Arm64, inspect the CHPE requirement and 32-bit application compatibility before disabling CHPE. A supported device that needs incompatible legacy software may require exclusion from hotpatch. A feature-version upgrade during a hotpatch month can return the device to standard updates until the following baseline. Record actual eligibility and restart evidence; do not promise a restart-free year.

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

### Stage a payload with deployment plans

[Deployment plans](https://learn.microsoft.com/en-us/intune/device-management/deployments/overview) are reusable ring/timing templates; a deployment delivers one selected payload. This is **public preview** for supported Windows Win32/Enterprise App Catalog apps and Settings Catalog/endpoint-security policies. Apps use Required intent; Available/Uninstall are unsupported. Enterprise App Catalog automatic updates cannot be combined with deployments; use the supported supersedence path. Rings need at least one hour between activations.

#### Worked example — expanding assignments is not rollback

Pilot group A contains devices 1–20 and later group B contains devices 16–50. Once both rings activate, the union is **50 devices**, not 55. This device overlap is different from a collision where the same group already occurs in the payload assignments and a ring; Intune pauses that collision for correction. Check both group IDs and resolved device membership.

[Pausing or canceling](https://learn.microsoft.com/en-us/intune/device-management/deployments/create-deployment) stops future ring progression but retains prior assignments. It does not uninstall an app or restore an old policy. Editing the payload can update devices already assigned and later rings, so ring timing does not freeze a version. Define separate rollback and success checks. A final All devices/All users ring replaces prior Required include-group assignments while preserving exclusions; assess that broad scope before activation.

### Microsoft 365 Apps lifecycle

Define architecture, apps, languages, update channel, version, shared-computer activation and existing-install migration. Deploy during Autopilot only if reliable day-zero requirements justify provisioning delay. Office Deployment Tool can create controlled installation configurations; Intune and Microsoft 365 Apps admin center can deploy/manage policy and update behavior under current capabilities.

Separate install configuration from Office cloud policy and security baselines. Diagnose assignment, network/CDN, conflicting architecture/version, update channel, service plan/activation and application-health evidence. **VERIFY CURRENT:** Cloud Update, servicing profile and admin-center names/capabilities.

### App protection and app configuration

[Intune app protection policies](https://learn.microsoft.com/en-us/intune/intune-service/apps/app-protection-policy) manage organizational data in supported applications, including on enrolled and unenrolled devices. Controls can require PIN/biometric, encrypt app data, restrict copy/paste/save/open-in, require minimum app/OS state and selectively wipe corporate data. MAM protects an application data boundary; it does not make the entire personal device compliant.

For new Conditional Access policies, use **Require app protection policy** for supported mobile access. The [approved-client-app migration guidance](https://learn.microsoft.com/en-us/entra/identity/conditional-access/migrate-approved-client-app) says the old grant became read-only June 30, 2026: policies using it cannot be newly created or edited, but existing enabled policies still enforce and can be disabled/deleted. Earlier March retirement advice and migration instructions describing edits are historical. Plan a replacement policy and test protection/enforcement before retiring the old policy; do not assume its restrictions disappeared. Build the app policy, deploy to a test population, validate supported applications and broker/authenticator prerequisites, then stage Conditional Access. Preserve a supported onboarding path so the policy does not block the user before protection can apply.

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

The current October objectives specifically require investigating threats, analyzing device performance and responding to recommendations from Security Copilot agents in Intune. The [official agent overview](https://learn.microsoft.com/en-us/intune/copilot/agents/) says agents operate within Intune with role-based access and administrator oversight. **VERIFY CURRENT:** available agents, permissions, data access, actions, capacity/licensing, preview/GA status and geography.

Treat a recommendation as a hypothesis with evidence:

- identify the agent, requested/observed inputs, time range and affected device set;
- inspect cited Intune/Defender/analytics evidence and compare with a known-good cohort;
- determine confidence, false-positive cost and blast radius;
- require approval for material changes and use pilots;
- record accept/reject rationale, actual change and measured result;
- report agent errors or unsafe recommendations and retain human override.

Do not paste sensitive device data into an unapproved AI service. Agent action remains constrained by identity, Intune roles, scope and current product controls; it does not transfer administrator accountability.

**Agent-specific lifecycle and identity matter:** The general agent overview still lists Device Offboarding Agent, but its [specific lifecycle page](https://learn.microsoft.com/en-us/intune/copilot/agents/device-offboarding-agent) says it was removed June 1, 2026. Use current device-lifecycle/remediation workflows instead of building a lab around that retired agent.

The [Vulnerability Remediation Agent](https://learn.microsoft.com/en-us/intune/copilot/agents/vulnerability-remediation-agent) remains public preview with Windows/application scope, public-cloud and license/plugin prerequisites. It uses its own agentic user and delegated Intune/Defender permissions; an administrator's access does not automatically transfer. Runs remain disabled until permissions and the readiness check pass. The June release describes a 90-day transition from human identity; check the tenant banner and move existing agents rather than relying on indefinite human-token renewal. Transition is one-way and preserves run history. Marking a suggestion applied records the administrator's action; verify actual device remediation separately.

### Reporting, Endpoint Analytics, and remediations

Intune reports include operational, organizational and historical views with filters, export and platform-specific detail. Azure Monitor/Log Analytics integration and workbooks can support retained/custom analysis for exported diagnostic categories. Define report freshness, time zone, denominator, ownership and response before building a dashboard.

[Endpoint Analytics](https://learn.microsoft.com/en-us/intune/monitor-troubleshoot) measures supported startup, application reliability and user-experience signals and provides scores/insights. Compare cohorts and trends rather than treating one score as a verdict. Sampling, device eligibility, check-in and workload pattern affect interpretation.

Remediations use a detection script and a remediation script on a schedule under the configured context. Write detection to be side-effect free and return documented exit/output. Make remediation idempotent, narrowly scoped and logged; sign scripts when required; test locally and in a pilot; preserve rollback; monitor recurring failures. A “successful remediation” exit code must be confirmed by a subsequent desired-state check.

Advanced Analytics can surface anomalies and risk-based recommendations. Correlation is not root cause. Compare versions, hardware, apps, policy, location and time; reproduce; then pilot the proposed change.

Monitor tenant status and Intune service communications alongside Message center and Microsoft 365 Service Health. Establish operational baselines for enrollment success, compliance drift, policy conflicts, app failure, update currency, check-in, performance and support. Configure alerts/notifications where supported, but assign an owner and response runbook—an unread alert is not a control.

#### Worked example — detection, execution and verification are separate

For a harmless lab setting, use a detector with three outcomes: known correct → exit 0; known incorrect → exit 1; unable to read → a distinct error with diagnostic output. [Remediations](https://learn.microsoft.com/en-us/intune/device-management/tools/deploy-remediations) runs the fix only for detection exit **1**. An access-denied exception must not be casually translated into “setting absent, fix it.” Keep diagnostics short, avoid reboot commands, respect signature/encoding and execution-context requirements, and choose an explicit local-time or UTC schedule.

Of 12 lab devices, eight return correct, three incorrect and one unknown. Three are remediation candidates; the unknown remains an investigation. If all three fixes return success but subsequent detection finds only two corrected, confirmed healthy devices total **ten**, with one unresolved and one unknown. Job success is not proof of the desired state.

[Custom compliance](https://learn.microsoft.com/en-us/intune/device-security/compliance/custom-settings) uses a different contract: discovery output plus JSON comparison rules. It reports state for compliance/access decisions rather than automatically executing a paired fix. Current docs cover Windows PowerShell and Linux/macOS shell scripts with platform/cloud conditions. Windows discovery normally runs every eight hours; a user's Check Compliance runs discovery without fetching an updated script, and push notifications do not trigger it on demand. Keep this distinct from newer client-driven built-in compliance signals.

### Alert rules for compliance drift, enrollment failure, and configuration conflict

An Intune report is not automatically an alert. First define the supported evidence source and its freshness, then route or export that evidence to an alert-capable system. [Send Intune logs to Azure Monitor](https://learn.microsoft.com/en-us/intune/governance/integrate-azure-monitor) by creating a diagnostic setting and selecting only the categories the use case needs: **OperationalLogs** includes enrollment successes/failures and noncompliant-device activity; **DeviceComplianceOrg** and **IntuneDevices** provide organizational compliance and inventory snapshots. Those two snapshot categories can take up to 48 hours to reach Log Analytics and are exported once daily, so they are useful for sustained drift rather than rapid incident detection. Design the query to tolerate repeat records and identify the latest state per stable device ID.

Use the native [device-compliance reports](https://learn.microsoft.com/en-us/intune/device-security/compliance/monitor-policy) for policy, device, and setting-level investigation. For configuration conflict, start with the affected profile's device/user status and per-setting status, then inspect every configuration and [endpoint-security policy](https://learn.microsoft.com/en-us/intune/intune-service/protect/endpoint-security) assigning the same setting to that device. A conflict is evidence of overlapping effective assignments, not proof that one policy surface always wins. If a recurring conflict must generate a centralized alert, use a supported report/API export on a schedule, preserve the source timestamp and device/policy IDs in a governed store, and alert on that ingested result. Do not claim that an Intune portal report has a native Azure Monitor stream when it does not.

Map the three operational cases explicitly:

| Case | Evidence and query | Signal and response |
|---|---|---|
| Compliance drift | Latest `DeviceComplianceOrg`/`IntuneDevices` snapshot plus the current Intune compliance report; compare the noncompliant percentage and affected policy/setting with a known baseline | Alert only after a material count/rate or sustained cohort change; owner validates export age, grace period, stale check-in, and newly assigned policy before enforcement |
| Enrollment failures | `OperationalLogs`; group failures by platform, enrollment method, error, tenant restriction, user, and time bucket; use attempted enrollments as the denominator | Alert on an absolute failure count and/or failure rate over a rolling window; responder checks service health, token/profile state, limits, licensing, authentication, and a successful comparison device |
| Configuration conflicts | Native per-profile/per-setting result or a scheduled supported report/API export; correlate the same device and setting across effective assignments | Alert when new unresolved conflicts exceed the accepted baseline; responder identifies overlapping assignments, tests precedence/result on a pilot, changes one source of authority, and verifies the setting after check-in |

For a Log Analytics-backed signal, follow the [Azure Monitor log search alert rule](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-log-alert-rule) lifecycle:

1. choose the Log Analytics workspace and least-privileged readers, then confirm the selected Intune diagnostic categories are arriving;
2. write and save a time-bounded query that returns the affected device/cohort and a count or rate, deduplicating on stable IDs and latest timestamps;
3. run it over historical good and bad periods to set a defensible aggregation granularity, evaluation frequency, lookback window, threshold, and required consecutive failures;
4. create the alert rule with that scope and condition, then attach an owned action group and a runbook link that names triage, escalation, maintenance suppression, and closure evidence;
5. test with a disposable enrollment failure, noncompliant pilot, or synthetic conflict/report row—never by disrupting production—and confirm query result, alert firing, notification, ticket routing, and recovery/closure;
6. tune false positives, record data latency and blind spots, review ownership and permissions, and periodically revalidate the negative path and a missed-signal scenario.

Keep separate alerts when their source latency or response differs. A once-daily compliance export and near-real-time enrollment log should not share the same evaluation window or service-level promise.

> **Related item:** Policy assignment success, device check-in, setting application, compliance, resource access and user experience are distinct outcomes. A mature endpoint dashboard shows the chain rather than one green percentage.

---

## Integrated scenarios

### Scenario 1: BYOD mobile access without full enrollment

The business permits Outlook and Teams on personal phones but forbids corporate data in personal apps/storage. Select supported apps, deploy app-protection and managed-app configuration to a pilot, require app protection policy with Conditional Access in a supported app, validate broker/authentication prerequisites, copy/paste/save/open-in and selective wipe across Android/iOS. Test both allowed and denied flows. Do not call the device compliant unless it is actually enrolled and evaluated by compliance policy.

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

Use Graph/PowerShell to export a bounded device inventory, handling pagination and errors without mutation. Design a remediation detection/fix pair and dashboard for enrollment, compliance, update, app, reliability and service health. Configure Intune diagnostic settings in a disposable workspace, or tabletop the configuration if unavailable. Build separate draft alert specifications for enrollment failures, compliance drift, and configuration conflicts: name the source/category, query or export, time window, denominator, threshold, owner, action group, runbook, data-latency limit, and closure signal. Exercise one with synthetic/pilot evidence and verify notification plus recovery without changing production. **Evidence:** sanitized code/output, dry-run target set, rollback plan, source-to-signal matrix, query/export sample, alert-rule settings, test result, and owned runbook.

---

### Lab 9 — Model a staged rollout and its recovery

Create synthetic groups with overlapping device membership, a scoped exclusion and two rings. Calculate the unique target union. In a disposable licensed tenant, or as a tabletop, create a preview deployment for a harmless app; record payload/version, group IDs, timing, permission and approval evidence. Observe assignment versus installation separately. Pause before the later ring, prove earlier assignments remain, and design a separate uninstall/reversion path. Test a same-group assignment collision without expanding production scope.

**Evidence:** target set, exclusion, before/after assignment, installation/detection, pause/cancel and recovery results. **Cleanup:** remove disposable assignments and app/resources; canceling alone does not remove them.

### Lab 10 — Validate recovery and uncertain telemetry

Build a backup/restore matrix for version, join, account, policy and OOBE/first-sign-in path. Test one allowed and one unsupported/unconfigured case on disposable devices if available; separately verify file protection. Compare a single-device query with fleet inventory and label collection age, missing devices and duplicate component rows. Tabletop a detector that returns correct, incorrect and read-error states; verify that only the intended state requests remediation and rerun detection after a fix.

**Evidence:** policy/state matrix, restore scope, distinct-device denominator, detector outcomes and cleanup plan. No device, tenant, Graph mutation, script deployment, restore or preview feature was executed during this repository review.

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
37. **Which Intune Azure Monitor category fits enrollment failure?** `OperationalLogs`; query failures against attempts and group by platform, method, error, and time before choosing a threshold.
38. **Why not promise a fast compliance-drift alert from `DeviceComplianceOrg`?** The organizational snapshot is exported daily and can take up to 48 hours to arrive, so the rule and response target must reflect that latency.
39. **How should a configuration-conflict alert be investigated?** Confirm current per-setting status, find every effective assignment configuring the same setting, test the proposed single source of authority on a pilot, and verify after check-in.

---

### Additional reasoning checks

40. **Are 90 compliant devices out of 100 reported proof of 90% compliance across a 120-device fleet?** No: 90% of reported devices, 75% confirmed coverage of the expected fleet, and 20 unobserved.
41. **Does canceling a deployment revert earlier devices?** No; prior assignments remain and rollback is separate.
42. **Do groups 1–20 and 16–50 target 55 devices?** No, their union has 50 distinct devices.
43. **Does an eligible default-on backup imply restore is enabled?** No; restore remains independently configured and files need separate protection.
44. **Does old approved-client-app grant retirement mean existing policies stopped enforcing?** No; current guidance says enabled policies continue enforcing in read-only form. New policies use app protection.
45. **Can every nonzero detection exit code trigger a remediation?** No; only exit 1 triggers the fix. Preserve read errors as uncertainty rather than false detection.
46. **Does an empty live query prove no vulnerable devices?** No; first prove connectivity, permission, scope, collection/result completeness and freshness.
47. **Can 80 baseline-ready and 90 VBS-ready devices establish 80 hotpatch candidates?** No; their intersection may be smaller, and other prerequisites remain.

---


## Final readiness checklist

- I can explain every objective as a target, configuration, effective-state check, failure mode, evidence source and recovery.
- I can separate device identity, enrollment, ownership, compliance, application protection and resource access.
- I can enroll and troubleshoot Windows, Android, Apple and macOS using appropriate corporate/BYOD methods.
- I can choose and operate Autopilot/device preparation, profiles, Intune Suite controls, remote actions and Windows 365.
- I can deploy endpoint security/update policy with pilots, recovery and cross-platform limitations.
- I can package, assign, detect, update, protect, configure, selectively wipe and troubleshoot applications.
- I can automate with Graph/PowerShell safely and evaluate Security Copilot agent recommendations with human accountability.
- I can build, test, and operate distinct alert paths for enrollment failure, compliance drift, and configuration conflict while accounting for source latency and false positives.
- I completed or tabletop-tested all ten labs and can prove both allowed and denied outcomes.
- I passed an independent readiness check without relying on recalled live-exam content.

## Places to learn

### October 28 learning route and evidence task

Use [MD-102T00](https://learn.microsoft.com/en-us/training/courses/md-102t00) as the primary route: identity/enrollment first, then policy and applications, protection, operations and premium/cloud-desktop gaps. Its eight selected paths still list **34 modules**, and the course still lists five instructor-led days; the earlier 29h46 remains historical runtime metadata. Before attempting the [Foundation lab](https://github.com/MicrosoftLearning/MD-102T00-Microsoft-365-Endpoint-Administrator/blob/main/Instructions/Labs/Lab01-Foundation.md), budget for its prepared tenant, seeded licensed users and four VMs. The 90-minute lab estimate excludes unmeasured setup; trial availability and eligibility are **VERIFY CURRENT**. Only its prerequisites and initial user/group exercise were read in this pass.

**Original worksheet (about 30–45 minutes, editorial estimate):** Choose a harmless app assignment from your learning route and record separately the intended cohort, resolved targets, check-in time, detection evidence, effective policy and tested user result. Add a device that never checked in and one that reports an installation failure.

**Answer checkpoint:** Assignment success is not installation evidence, and a missing device is an observation gap rather than a successful outcome. A browser simulation can rehearse the workflow while tenant/device execution remains untested.

### October 28 learning-resource check

Additional options and access updates; choose relevant resources rather than consuming every route. New course availability, class delivery and licensing are **VERIFY CURRENT**. Published days describe instructor-led scope, not measured self-study time.

| Resource | Access | Estimated time |
|---|---|---|
| [Official MD-102 Foundation lab](https://github.com/MicrosoftLearning/MD-102T00-Microsoft-365-Endpoint-Administrator/blob/main/Instructions/Labs/Lab01-Foundation.md) | Public instructions; prepared disposable tenant, licenses and four VMs required; no hosted lab included | **90 published minutes plus unmeasured setup**; identity, enrollment, Autopilot and RBAC practice; not executed or audited against every October objective |


This is a curated starting point, **not a complete list**. It is not meant to be consumed in full. Choose one current primary route, build a real lab, and use assessment results plus the current October 27, 2026 blueprint to select supplements. Older MD-102 courses may omit Intune Suite, device preparation changes, automation/reporting, and Security Copilot agents.

The eight official paths currently list **34 modules**. The earlier **29 hours 46 minutes** and per-path times below are historical metadata; current pages did not expose runtimes in this retrieval. Budget separately for labs and review.

They are [prepare infrastructure](https://learn.microsoft.com/en-us/training/paths/prepare-infrastructure-devices-intune-microsoft-entra-id/) (4h44), [manage and maintain devices](https://learn.microsoft.com/en-us/training/paths/manage-maintain-devices-intune/) (3h56), [manage applications](https://learn.microsoft.com/en-us/training/paths/manage-applications-intune/) (4h45), [protect devices](https://learn.microsoft.com/en-us/training/paths/protect-devices-intune/) (5h02), [automate and optimize](https://learn.microsoft.com/en-us/training/paths/automate-optimize-endpoint-management-intune/) (2h36), [support operational excellence](https://learn.microsoft.com/en-us/training/paths/support-operational-excellence-intune/) (2h15), [extend with Intune Suite](https://learn.microsoft.com/en-us/training/paths/extend-intune-suite/) (3h13), and [deliver cloud-hosted desktops](https://learn.microsoft.com/en-us/training/paths/deliver-cloud-hosted-desktops/) (3h15).

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MD-102 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/modern-desktop/) | Public | 1–2 hours initially; 15 minutes on each recheck |
| Eight self-paced paths from [MD-102T00](https://learn.microsoft.com/en-us/training/courses/md-102t00) | Public | Historical 29 hours 46 minutes; allow an estimated 45–70 hours with exercises, device testing and notes |
| MD-102T00 instructor-led course | Paid/partner delivery | 5 days listed |
| [Microsoft MD-102 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/modern-desktop/practice/assessment?assessment-type=practice&assessmentId=76&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Pluralsight MD-102 path](https://www.pluralsight.com/paths/microsoft-windows-endpoint-administrator-md-102) with Glenn Weadock | Paid | 13h19 across five listed courses (path rounds to 13 hours), plus a practice exam; introduction September 2024, other courses March–May 2026. Public metadata only; July/October coverage unverified |
| [O'Reilly/Packt MD-102 video](https://www.oreilly.com/videos/md-102-endpoint-administrator/9781836208396/) | Paid | Historical 23h14, May 2024; retrieval blocked. Current availability/content unverified; supplement later objectives |
| [Udemy MD-102 full course](https://www.udemy.com/course/microsoft-certified-endpoint-administrator-md-102/) | Paid | Historical 15h50, February 2026; retrieval blocked. Current runtime/scope unverified |
| [Udemy current-blueprint practice](https://www.udemy.com/course/md-102-practice-exam-2026-6-endpoint-administrator-tests/) by Joshua Ravnjak | Paid | Historical listing: 180 questions and August 2026 update; retrieval blocked. Originality/coverage not independently established; 6–10 hours is a planning estimate |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics) and [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor) | Public | 2–8 hours selectively for current Intune, Windows, Entra and Defender demonstrations; not a fixed MD-102 course |
| [John Savill's Technical Training](https://www.youtube.com/@NTFAQGuy) and [public repositories](https://github.com/johnthebrit) | Public | 2–8 hours selectively for Entra, Conditional Access, Windows 365, security and architecture foundations; no exact current MD-102 path confirmed |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use the listed event start/end times after partner sign-in |

No exact current Whizlabs or MeasureUp MD-102 product page was independently verified during this review, so neither is inferred. Never use resources claiming recalled live questions. Start with Microsoft's free Practice Assessment; add a paid bank only when its explanations and question style close a specific gap.

### Two blog readings with a practical task

| Reading | Learning task | Boundaries |
|---|---|---|
| [Windows App Management in Microsoft Intune](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/windows-app-management-in-microsoft-intune/4515194), Zachary Cavanell, Microsoft Mechanics, April 27, 2026; demonstration by Nicole Zhao | Budget 20–30 minutes to read the public transcript and sketch inventory → package → assignment → installation → update evidence. Identify where a mutable payload can affect an earlier ring. | Article/transcript reviewed, video and tenant not tested. Its private-preview deployment label is historical; current detailed docs say public preview. The separate automatic-update and deployment demonstrations do not establish that those options can be combined. |
| [Windows settings backup becoming a new resilience baseline](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-settings-backup-becoming-a-new-resilience-baseline/4530757), Miranda Leschke, Windows IT Pro Blog, July 6, 2026 | Budget 20–30 minutes for a Not Configured/Enabled/Disabled backup-policy table and a separate restore column. Add OS, geography/cloud and file-protection checks. | Main article reviewed, linked video not watched. Default-on is scoped to eligible 26H2 behavior; explicit policy is honored, restore stays separate, and DMA/sovereign restrictions matter. Do not infer every tenant/device already received it. |

Public catalogs and official modules were inspected; paid lessons/questions were not accessed. O'Reilly and both Udemy pages were blocked in the earlier review; this learning-resource pass did not recheck those three exact listings. Channel/partner responses were shells or profile metadata, and the direct Practice Assessment did not expose question content. Use dated resource metadata to plan study, not as proof of complete current coverage. The existing Agent 365 announcement remains adjacent context, not an Intune-agent availability matrix.
