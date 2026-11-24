# Microsoft certification refresh, group 4

Checked November 20, 2026. [Scope and results](2026-11-20-microsoft-refresh.md)

## MS-102

[Study guide](../../guides/MS-102-microsoft-365-administrator.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-102)

Credential: Microsoft 365 Certified: Administrator Expert. Exam and credential retirement scheduled for November 30, 2026. The credential lists one of Endpoint Administrator Associate, Teams Administrator Associate, Identity and Access Administrator Associate and Information Security Administrator Associate. Partner Center names AB-650 for the Modern Work designation path; the roadmap pairs the retiring expert award with the new associate.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/m365-administrator-expert/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/ms-102/) · [Microsoft notice](https://learn.microsoft.com/en-us/partner-center/announcements/2026-october) · [Microsoft notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/microsoft-credentials-roundup-june-2026/4528350) · [Publisher evidence](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)

**Product documentation.** For a hybrid identity maintenance plan, record both the installed Entra Connect Sync version and how the connector authenticates. Microsoft requires version 2.6.84.0 or later and application-based authentication by April 7, 2027. Verify both before declaring the migration complete.

[Microsoft Entra Connect: Version release history - Microsoft Entra ID | Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history) · [Authenticate to Microsoft Entra ID by Using Application Identity - Microsoft Entra ID | Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/authenticate-application-id)

The version alone does not establish which credential the active connector uses. Tenant migration was not executed.

Additional product evidence: [Publisher documentation 1](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-rule-member-of)

**MS-102 Implement identity synchronization.** Four modules cover synchronization concepts, preparation, directory synchronization tools and management of synchronized identities. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). Implementation needs an appropriate hybrid environment; reading the path does not establish the right tool or topology for a particular deployment. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/implement-identity-synchronization/)

## MS-700

[Study guide](../../guides/MS-700-managing-microsoft-teams.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700)

Credential: Microsoft 365 Certified: Teams Administrator Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/m365-teams-administrator-associate/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/ms-700/)

**Product documentation.** For a Teams channel that receives application notifications, create a Workflows webhook and assign a co-owner. Connector-based Incoming Webhooks retired in May 2026, and a workflow belongs to its owners even when it posts to a team channel.

[Webhooks and connectors - Teams | Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors)

Confirm owner continuity and channel support for the chosen template. No webhook message was sent.

Additional product evidence: [Publisher documentation 1](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/)

**Manage meetings and calling in Microsoft Teams.** The public path covers meetings, rooms, calling, voice users, auto attendants, call queues and client troubleshooting. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). Voice provisioning and meetings policies need suitable licensing, phone connectivity and administrator access. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/manage-meetings-calling-microsoft-teams/)

## MS-721

[Study guide](../../guides/MS-721-collaboration-communications-systems-engineer.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-721)

Credential: Microsoft 365 Certified: Collaboration Communications Systems Engineer Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/m365-collaboration-communications-systems-engineer/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/ms-721/)

**Product documentation.** When two Teams Rooms show different capabilities, record the platform and installed app version, then look for a separate Teams web client release. A web client feature can reach a room through cloud delivery without installing another local app build.

[Release notes for Microsoft Teams Rooms - Microsoft Teams | Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/rooms/rooms-release-note)

Feature rollout and device licensing can differ even when local app builds match. A room was not inspected.

**MS-721 Manage Teams collaboration communications systems.** Eight modules include two guided projects, Teams policies, room preparation, voice users, device management, troubleshooting and bookable desks. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). Real room hardware, tenant licensing and administration are separate from public access to the project outlines. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/manage-teams-voice/)

## MD-102

[Study guide](../../guides/MD-102-managing-securing-microsoft-365-endpoints-intune.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102)

Credential: Microsoft 365 Certified: Endpoint Administrator Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/modern-desktop/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/md-102/)

**Product documentation.** The November 16 Intune service release describes sharing diagnostics during an attended Windows Remote Help session. The user can review and stop sharing the information. If the user declines, the helper can continue the session without those diagnostics.

[What's new in Microsoft Intune - Microsoft Intune | Microsoft Learn](https://learn.microsoft.com/en-us/intune/whats-new/)

Microsoft describes this as rolling out. Availability on one tenant cannot be assumed for another.

**Automate and optimize endpoint management using Microsoft Intune.** Three modules cover PowerShell/Graph, AI/Copilot tools and Intune endpoint monitoring. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). Reading does not confirm that the tenant has a particular Copilot capability, license or device enrollment state. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/automate-optimize-endpoint-management-intune/)

## SC-100

[Study guide](../../guides/SC-100-microsoft-cybersecurity-architect.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)

Credential: Microsoft Certified: Cybersecurity Architect Expert. Explicit prerequisite is one of Identity and Access Administrator Associate, Security Operations Analyst Associate or Cloud and AI Security Engineer Associate.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/cybersecurity-architect-expert/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-100/)

**Product documentation.** In an IoT architecture inventory, distinguish the legacy agent under IoT Hub from the later Defender for IoT micro agent. Microsoft's support page lists June 1, 2027 as the planned retirement of the micro agent. Review device dependencies and support dates for the specific component.

[Microsoft Defender for IoT Feature Support and Retirement - Microsoft Defender for IoT | Microsoft Learn](https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/edge-security-module-deprecation)

The component notice does not establish retirement of the whole Defender for IoT service or every operational technology deployment.

**Design solutions that align with security best practices and priorities.** Four modules connect Zero Trust, CAF and WAF, Microsoft reference architectures and benchmarks, and recovery planning. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). This path teaches architecture decisions. It does not independently demonstrate that an organization meets a benchmark or recovery target. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/sc-100-design-solutions-best-practices-priorities/)

## SC-200

[Study guide](../../guides/SC-200-microsoft-security-operations-analyst.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200)

Credential: Microsoft Certified: Security Operations Analyst Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-200/)

**Product documentation.** A Defender portal deployment connects one Microsoft Entra tenant to a primary Sentinel workspace and can also connect secondary workspaces. When only one workspace exists, it becomes primary. Record the primary workspace before assigning connectors that depend on it.

[Connect Microsoft Sentinel to the Microsoft Defender portal | Microsoft Learn](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard)

Microsoft states Sentinel portal access does not itself require a Defender XDR or E5 license. Entitlement for individual products and connector data remains separate.

**Create queries for Microsoft Sentinel using Kusto Query Language (KQL).** Four modules progress from basic KQL statements to analysis, joins across tables and work with Sentinel data. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). Tenant data access and retention affect a live Sentinel exercise. No investigation or workspace query was executed. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/sc-200-utilize-kql-for-azure-sentinel/)

## SC-300

[Study guide](../../guides/SC-300-microsoft-identity-access-administrator.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300)

Credential: Microsoft Certified: Identity and Access Administrator Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-300/)

**Product documentation.** Create separate Conditional Access policies for user risk and sign-in risk. When a policy expects self-remediation, verify the user has registered the required authentication method. For hybrid password changes, verify password writeback before enforcement.

[Risk policies - Microsoft Entra ID Protection | Microsoft Learn](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies)

Full Identity Protection functionality requires the documented license. Tenant policy testing remains necessary.

Additional product evidence: [Publisher documentation 1](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-rule-member-of) · [Publisher documentation 2](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/security-updates-pks) · [Publisher documentation 3](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history)

**Plan and implement an identity governance strategy.** Four modules cover entitlement management, access reviews, privileged access, and Entra monitoring. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). Hands-on governance exercises depend on tenant roles, available licensing and configuration. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/plan-implement-identity-governance-strategy/)

## SC-401

[Study guide](../../guides/SC-401-administering-information-security-microsoft-365.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)

Credential: Microsoft Certified: Information Security Administrator Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-401/)

**Product documentation.** Just-in-time Endpoint DLP can protect a monitored file while its policy evaluation is pending. Deploy the intended Endpoint DLP policies first, then evaluate whether pending actions should be blocked. The documented device list includes Windows 10, Windows 11, and the three most recent macOS versions.

[Get started with Endpoint DLP Just-in-time protection | Microsoft Learn](https://learn.microsoft.com/en-us/purview/endpoint-dlp-get-started-jit)

Check activity and platform limits in the product article. No endpoint action or policy evaluation was executed.

**Implement and manage Microsoft 365 retention and recovery.** The two modules cover retention labels and policies, scope, and Microsoft 365 retention and recovery. About 20–40 minutes to read the selected sections and produce the suggested comparison or checklist (editorial estimate; full path duration was not verified). Retention needs depend on workload and configuration. Completion of the reading does not demonstrate recovery or legal disposition. [Publisher resource](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention/)

## SC-500

[Study guide](../../guides/SC-500-microsoft-cloud-ai-security-engineer.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500)

Credential: Microsoft Certified: Cloud and AI Security Engineer Associate. July Partner Center names this credential as the successor for retired AZ-500.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/cloud-and-ai-security-engineer-associate/) · [Microsoft notice](https://learn.microsoft.com/en-us/partner-center/announcements/2026-july)

**Product documentation.** For a multicloud assessment, match each workload to a named Defender plan. Microsoft's matrix lists Defender for Servers and Defender for Containers as generally available on AWS and GCP. Azure-specific products such as Defender for Key Vault have separate coverage rows.

[Microsoft Defender for Cloud multicloud support matrix - Microsoft Defender for Cloud | Microsoft Learn](https://learn.microsoft.com/en-us/azure/defender-for-cloud/multicloud-support-matrix)

A supported plan on a non-Azure cloud does not establish support for every feature within that plan. Check the per-plan matrix.

Additional product evidence: [Publisher documentation 1](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes)

**Enable protection in Microsoft Defender.** The Defender training unit covers Security for AI settings, runtime protection, Power Platform coordination and connection verification. 7 minutes for the unit (publisher page). Opening this seven-minute unit does not establish protection coverage, license eligibility or administrative access for a tenant. Its refresh window is separate from lesson duration. [Publisher resource](https://learn.microsoft.com/en-us/training/modules/enable-protection-copilot-studio-agents/3-enable-protection-microsoft-defender)

**Resource follow-up.** The catalog entry `sc-500-pluralsight-az500-legacy` returned this result: 404 confirmed on retired AZ-500 path. [Available publisher resource](https://learn.microsoft.com/en-us/training/paths/implement-ai-security/)

## SC-900

[Study guide](../../guides/SC-900-microsoft-security-compliance-identity-fundamentals.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)

Credential: Microsoft Certified: Security, Compliance, and Identity Fundamentals. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-900/)

**Product documentation.** For a commercial Microsoft 365 scenario, use the new Microsoft Purview eDiscovery experience. The legacy solutions article identifies August 31, 2025 as retirement of classic Content Search, Standard, and Premium and limits its remaining instructions to Microsoft 365 operated by 21Vianet.

[Microsoft Purview eDiscovery legacy solutions | Microsoft Learn](https://learn.microsoft.com/en-us/purview/ediscovery)

The general overview for current exercises is [Microsoft Purview eDiscovery overview](https://learn.microsoft.com/en-us/purview/edisc) (opened from the publisher's legacy-page notice). The registered /purview/ediscovery page only supports the historical scope.

Additional product evidence: [Publisher documentation 1](https://learn.microsoft.com/en-us/purview/edisc)

**Introduction to Microsoft Security, Compliance, and Identity.** The public introductory course identifies identity, Microsoft security, and compliance capabilities as foundational study areas. 1 day of instructor-led training (publisher listing); provider scheduling and fees vary. The one-day duration is the published course length. Dates, fees and hands-on provider arrangements require a specific class listing. [Publisher resource](https://learn.microsoft.com/en-us/training/courses/sc-900t00)
