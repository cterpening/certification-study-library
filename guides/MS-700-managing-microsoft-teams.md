---
exam_code: MS-700
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# MS-700 Managing Microsoft Teams Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 29, 2026 objectives and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ms-700-coverage-record). The [official MS-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700) is authoritative.

**Current baseline:** Skills measured as of July 29, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Official source:** [MS-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700)

## How to use this guide

Teams is an experience assembled from Microsoft 365 groups, SharePoint, OneDrive, Exchange, Entra, Purview, Defender, apps, media services, telephony and endpoints. Diagnose the owning object and control—not merely the Teams client symptom.

Use this chain:

1. identify user/guest, license, role, client/device, network and intended experience;
2. identify the Team/group, channel, meeting/event, app, phone/resource account or policy object;
3. resolve tenant/global, group/batch and direct policy assignment and any meeting/team-specific setting;
4. inspect Entra, SharePoint/OneDrive, Exchange, Purview, Defender and cross-tenant dependencies;
5. inspect health, usage, Call Analytics/CQD, logs, alerts and effective configuration;
6. make a scoped, reversible change and prove both allowed and denied outcomes.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Configure and manage a Teams environment | 40–45% | Are networking, governance, security, external collaboration and devices ready and controlled? |
| Manage teams, channels, chats, and apps | 20–25% | Are collaboration containers, membership, messaging and extensions governed through their lifecycle? |
| Manage meetings and calling | 15–20% | Do event and Teams Phone designs meet audience, policy, number and call-flow requirements? |
| Monitor, report on, and troubleshoot Teams | 15–20% | Can administrators distinguish service, network, policy, client, identity, AI and media failures using evidence? |

---

## 1. Configure and manage a Teams environment

### Network readiness and media path

Teams signaling establishes sessions; real-time media carries audio, video and screen sharing. Media quality depends on endpoint, local network, Internet path, service edge and, for phone scenarios, PSTN/SBC/operator dependencies. Favor local Internet breakout, short paths, supported proxy behavior and UDP media; do not hairpin real-time traffic through a distant data center without a justified design.

[Prepare your network for Teams](https://learn.microsoft.com/en-us/microsoftteams/prepare-network) defines required endpoints, ports and protocols. Treat published URLs/IPs as maintained vendor data, not a list to copy once. QoS classifies media traffic and helps during contention; it does not create bandwidth or repair packet loss. Define client port ranges, DSCP markings and network-device trust consistently.

Calculate capacity by modality, expected concurrent sessions, direction and site population, then reserve headroom. Network planner models personas, sites and usage assumptions; validate assumptions with actual telemetry. Use the [Microsoft 365 network connectivity test](https://connectivity.office.com/) for path/egress/DNS insight and current Teams network assessment tooling for media readiness. **VERIFY CURRENT:** Microsoft has renamed or retired older Skype/Teams assessment utilities; use the blueprint-named current download and documentation.

Interpret media metrics together:

| Signal | Likely effect |
|---|---|
| Packet loss | Missing/choppy audio or video artifacts |
| Jitter | Variable arrival; buffer pressure and distortion |
| Round-trip time | Conversation delay and talk-over |
| Available bandwidth | Resolution/frame-rate reduction or media failure |
| Wi-Fi/CPU/device issue | Local quality degradation even when WAN is healthy |

> **Related item:** Call Quality Dashboard identifies fleet/site/subnet patterns; Call Analytics provides a user/session view. Neither replaces a client/network capture when the failing segment remains ambiguous.

### Roles, security, and compliance

Choose the least-privileged Teams role: Teams Administrator for broad service management, Teams Communications Administrator/Support Engineer/Specialist for communications/support scopes, Teams Devices Administrator for devices, and other workload roles for Purview, Defender, Entra, SharePoint and telephony responsibilities. Verify current role permissions before assignment.

Teams data is distributed. Channel messages and chats use Teams/Exchange-backed compliance substrates; standard channel files are in the parent team's SharePoint site; private and shared channels have separate SharePoint site/membership behavior; chat file sharing typically uses the sender's OneDrive. Meeting recordings, transcripts and artifacts follow current OneDrive/SharePoint and meeting policy behavior. Find the owning object before applying retention, eDiscovery or recovery.

Security/compliance controls solve different problems:

- Defender for Office 365 Safe Links/Safe Attachments and threat policies protect supported Teams messages/files/URLs.
- Purview retention governs message and content lifecycle under location-specific behavior.
- sensitivity labels can govern teams/groups and meetings under applicable licensing and policy.
- DLP evaluates sensitive-data activity in supported chat/channel and related locations.
- Information Barriers restrict communication/collaboration between segments.
- Communication Compliance supports privacy-aware review of policy matches in supported communications.
- Insider Risk Management correlates configured risk indicators into governed investigation workflows.
- Conditional Access controls sign-in/session access; it does not replace Teams, meeting or SharePoint authorization.

Start policies in simulation/audit where supported, test representative internal/guest/shared-channel/meeting cases, define alerts and reviewer roles, then enforce. Licensing, workload locations and policy precedence matter. **VERIFY CURRENT:** Copilot/AI, meeting-label and Teams Premium dependencies.

### Governance and policy assignment

A team normally uses a Microsoft 365 group for membership and lifecycle. Configure who may create groups, group naming prefix/suffix and blocked words, expiration/renewal, ownership and access reviews. Creation restrictions require correct Entra configuration/licensing and should include a supported request path.

Archive makes a team read-only for most activity while preserving it; unarchive restores activity. Delete starts a recoverable period under current Microsoft 365 group behavior; restoration requires the group and dependent resources to remain recoverable. Retention/hold can preserve compliance copies without making the user-facing team active. Test delete/restore and document ownership transfer.

Teams policies have global defaults, direct assignments, group assignment, batch operations and policy packages. A policy package is a collection of policies for a persona; changing package assignments/effective policy must be verified at the user. Precedence and processing time vary by policy workload. Record the effective assignment rather than assuming the last portal click won.

Update policies control which supported client features/users receive under the current release model. Pair with targeted validation and communication. Use Teams PowerShell and Microsoft Graph for repeatable operations with least privilege, object-ID safety, pagination/throttling, logs and rollback.

> **Related item:** A team sensitivity label can control container settings such as privacy/external sharing, while labels on documents protect the documents. Container and content controls complement rather than replace each other.

### External access, guest access, and shared channels

Choose the collaboration model deliberately:

| Model | Identity/resource boundary | Typical use |
|---|---|---|
| External/federated access | Each person remains in home tenant; chat/calling without team membership | Communication with another organization |
| Guest access (B2B collaboration) | Guest object enters resource tenant and can be team member | Broader collaboration in a team and its resources |
| Shared channel (B2B direct connect) | External participant accesses a channel through cross-tenant trust without conventional guest switching | Focused cross-tenant channel collaboration |
| Multitenant organization | Coordinated tenants configure member collaboration/trust for a broader organization | Mergers or organizations operating several tenants |

Guest success requires compatible Entra external collaboration/cross-tenant settings, Teams guest settings, team membership, SharePoint/OneDrive external sharing and resource permission. External/federated domain allow/block policy is separate. “Can chat externally” does not imply “can open this team's files.”

Shared channels use B2B direct connect cross-tenant access settings and their own membership/site. Both organizations' policy can affect access. Control External Access by Domain for Specific Users and Groups only where supported and validate policy precedence. For MTO, understand member tenant, synchronization/collaboration settings, identity lifecycle and user experience. **VERIFY CURRENT:** MTO capabilities, cross-tenant sync, shared-channel limitations and licensing.

Remove external access at every applicable layer: team/channel membership, guest object or cross-tenant access, sharing links/groups, app grants and sessions. Preserve required content/audit/retention evidence.

### Teams clients and devices

Teams Phone and resource accounts, Teams Rooms and device features have distinct license requirements. A resource account represents an auto attendant/call queue and typically needs the applicable resource-account license; users need Teams Phone and PSTN connectivity entitlements appropriate to the chosen model. Verify current licensing.

In Teams admin center, use configuration profiles, device tags, accounts, health, firmware/software updates, restart and diagnostic actions. Tags organize devices for operations/policy targeting under supported features; they are not Entra security boundaries. Remote sign-in/provisioning should protect codes, verify physical custody and remove stale credentials.

Teams Rooms design includes certified hardware, room/resource account, mailbox/calendar processing, licensing, network/media readiness, Conditional Access compatible with resource accounts, update rings, peripherals and support ownership. Do not apply ordinary-user MFA interactively to a room without a supported device-authentication design.

For VDI, plan supported platform/provider, client and optimization component, media offload, versions, peripherals, network, roaming profile/cache and feature limitations. An unoptimized VDI call can hairpin media through the virtual desktop and degrade quality.

---

## 2. Manage teams, channels, chats, and apps

### Team rollout and creation

Advisor for Teams can help plan rollout workloads, but adoption needs stakeholders, use cases, champions, training, governance, support and measures. Start with representative pilots and explicit success/stop criteria.

Create teams through client, admin center, PowerShell or Graph; automation needs owners, privacy, membership, classification, naming, lifecycle and idempotency. A team can be created from an existing Microsoft 365 group, SharePoint site or another team/template, but source artifacts and permissions do not always copy identically. Verify membership, settings, apps/tabs and files.

Templates standardize channels, tabs/apps and settings for repeatable scenarios; template policies control user visibility. They are starting configurations, not continuous enforcement. Team owners manage membership/settings within tenant constraints; admins manage service/policy and can remediate ownerless teams.

Frontline experiences can use dynamic team deployment and standardized configurations under supported licensing. Validate workforce source attributes, location boundaries, owners and offboarding before scaling.

### Channel and messaging decisions

Standard channels share team membership and the parent site. Private channels have restricted membership and a separate SharePoint site. Shared channels can include people outside the parent team and support cross-tenant collaboration with a separate site. Choose by the required membership boundary, not just convenience.

Deleting a channel affects conversations and related content under current lifecycle behavior; the separate SharePoint site for private/shared channels has its own lifecycle considerations. Manage membership and ownership at the channel where applicable. A user can be a shared-channel member without being a member of the host team.

Teams/channel policies govern who can create private/shared channels and share externally. Messaging policies control supported chat capabilities such as editing/deleting, read receipts, URL previews, translation and user experiences. Meeting chat behavior can also depend on meeting policy/options. Resolve effective user policy and scope before blaming client cache.

### Teams apps and extensibility

The app lifecycle is **discover/purchase → allow/block and permission/consent review → assignment/availability → setup/pin → use/monitor → update/respond/retire**. Org-wide app settings establish broad behavior; app-centric management or current app permission policies determine who can use an app; setup policies install/pin supported apps. Blocking an app and removing OAuth consent are separate actions.

Assess publisher, certification, permissions, delegated/application access, data destination, owners, audience, licensing/purchase, support, telemetry and revocation. Upload custom apps only through controlled review; verify manifest, domains, identity, permissions and versioning. Store customization affects discovery/branding, not security approval.

Choose extension point from interaction:

- tabs embed a web experience in team/chat/meeting context;
- bots/agents converse and act within their permissions;
- message extensions add search/action behavior in compose/message context;
- meeting apps integrate before/during/after meetings;
- workflows automate events/actions through Power Automate or supported app capabilities.

> **Related item:** A Teams app can be allowed by Teams policy yet fail because Entra consent, license, Conditional Access, resource permission or downstream service is missing.

---

## 3. Manage meetings and calling

### Meetings, appointments, webinars, and town halls

Choose the experience by interaction and scale:

| Experience | Best fit |
|---|---|
| Meeting | Interactive collaboration among participants |
| Appointments with Teams | Scheduled customer/client appointment workflow |
| Webinar | Registration-based structured presentation with attendee management |
| Town hall | One-to-many produced event for a larger audience |

Meeting settings establish tenant-wide defaults/capabilities; meeting policies govern users who organize/participate; templates package supported options for scenarios; template policies control availability; customization policies apply branding; per-meeting options refine an instance. Event policies/settings govern webinar/town-hall capabilities. Test organizer, presenter, attendee, guest/external and anonymous experiences.

Policies can control scheduling, recording, transcription, lobby, content sharing, chat, reactions, attendance, watermarking, end-to-end encryption and Copilot relationships under current licensing. Sensitivity labels/templates can enforce protected meeting configurations. **VERIFY CURRENT:** Teams Premium, Copilot, recording/transcript storage, AI notes and event-capacity behavior.

For Copilot in meetings, trace user license, meeting policy/option, transcript/recording context, client, organizer settings, data policy and service availability. Enabling transcription does not automatically authorize every recording or Copilot scenario; communicate privacy and retention.

### Teams Phone numbers, policies, and call flows

Separate the cloud phone system from PSTN connectivity. Microsoft Calling Plans, Operator Connect and Direct Routing provide different number/carrier/SBC/operating models. MS-700 focuses managing numbers and services; MS-721 goes deeper on systems engineering.

Number types include user/subscriber, service and conferencing bridge numbers under applicable availability. Assign the correct license and usage location, acquire/port/provision the number, assign to user or resource account, configure emergency/calling settings and test inbound/outbound/caller ID/emergency behavior.

Calling policies govern user call capabilities; voice-routing policy/PSTN usages/routes determine Direct Routing path; caller ID, dial plan and emergency policies solve other tasks. Voicemail policies govern cloud voicemail behavior.

Auto attendants provide menus, greetings, schedules/holidays and routing. Call queues distribute calls among agents using routing and presence/overflow/timeout settings. Both use licensed resource accounts and can transfer to people, queues, voicemail or external numbers as supported. Design a call-flow diagram and test business hours, after hours, holiday, no-answer, overflow, agent opt-in, delegation and failure.

> **Related item:** A resource account is an identity used to anchor voice service; an auto attendant or call queue is the call-flow application. Licensing the resource account does not build or validate the call flow.

---

## 4. Monitor, report on, and troubleshoot Teams

### Monitoring and reporting

[Teams meeting and call troubleshooting](https://learn.microsoft.com/en-us/microsoftteams/monitor-troubleshoot-teams-meetings-calls) spans service health, usage reports, CQD, Call Analytics, real-time telemetry, device/client health and diagnostics. Define audience, freshness, denominator, privacy and action for every report.

- CQD finds organization/site/build/network patterns and uses tenant data/reporting labels for meaningful locations.
- Call Analytics investigates a specific user's meetings/calls and device/network/system details.
- Real-Time Analytics supports live meeting troubleshooting under current availability/licensing.
- usage reports cover active users, team activity, apps, meetings, devices and other adoption signals.
- Microsoft 365 reports/storage views provide related group/SharePoint/OneDrive information.
- audit and group lifecycle evidence identify team creation/deletion and guest changes.

Configure alert rules for supported call-quality/device conditions and assign response ownership. Manage user feedback policy and review feedback as a signal, not proof. Correlate the Microsoft 365 network connectivity dashboard with actual affected sites and call evidence.

Usage is not business value. Combine adoption with quality, support demand, governance, risk and outcomes.

### Troubleshooting sequence

For every incident capture user, UTC time, meeting/call ID, tenant, client/version, device/peripherals, network/location, policy and error/correlation ID. Check scope: one user/device/network/site/tenant or all users. Check Service Health and recent changes, then walk the owning layer.

Client evidence includes Teams logs, media logs/current support bundles, OS event logs and device diagnostics. Clear cache only after preserving evidence and confirming cache corruption is plausible; cache paths/processes differ by client generation/OS. Reinstalling can hide a repeatable policy or service issue.

Sign-in troubleshooting covers account/license, client support, network/proxy, authentication method, Conditional Access evaluation, device compliance, session and service health. Meeting-join troubleshooting covers link/tenant, organizer/lobby/anonymous/federation policy, client/browser, network/media ports, meeting capacity and per-meeting options.

For poor media:

1. locate call/session in Call Analytics and compare each endpoint;
2. identify wired/Wi-Fi, device/peripheral, client/build, VPN/proxy/VDI and network path;
3. inspect loss, jitter, RTT, bitrate and system metrics by leg/time;
4. compare CQD cohort/site trends;
5. reproduce with known-good device/network and current network tests;
6. fix local device, WLAN/LAN/WAN/QoS/egress or service dependency; then verify.

Copilot/AI troubleshooting adds license/service plan, meeting policy/option, transcript/recording, supported client/language, source permission, Purview control and feature rollout. A missing transcript is not fixed by granting broad SharePoint access. **VERIFY CURRENT:** AI names, licenses, meeting prerequisites and admin surfaces.

---

## Integrated scenarios

### Scenario 1: Shared channel partner cannot access files

Confirm host tenant, partner tenant, user and shared-channel membership. Inspect B2B direct connect inbound/outbound cross-tenant settings in both tenants, MFA/device trust, Teams shared-channel policy, channel membership and the separate SharePoint site permission/sharing configuration. Capture sign-in/correlation evidence. Do not add a conventional guest or loosen tenant-wide external sharing until the failed layer is proven.

### Scenario 2: Global town hall has poor audio

Capture event/session IDs and affected locations. Separate presenter/producer contribution quality from attendee delivery. Use Call Analytics/real-time evidence for presenters, CQD/site/subnet trends, network connectivity and event configuration. Check Wi-Fi, VPN, CPU/peripheral, UDP/QoS/egress and capacity assumptions. Remediate the failing path and run a rehearsal; do not infer a Microsoft outage from attendee anecdotes.

### Scenario 3: Third-party app requests broad consent

Verify publisher, manifest, Teams permissions, Entra delegated/application permissions, data destination, user/admin consent, owner, purchase, audience, support and emergency revocation. Pilot with least privilege; compare requested access with the exact feature. If rejected, block app availability and address consent/grants separately. Record decision and revisit after version/permission change.

---

## Hands-on labs

Use a test tenant and synthetic data/phone plans where available. Do not test PSTN emergency calling casually; use carrier-approved validation procedures.

### Lab 1 — Network and media readiness

Model two sites and personas in Network planner/current tools, calculate concurrency/bandwidth, document ports/URLs/QoS and run connectivity tests. **Evidence:** assumptions, result, headroom and remediation.

### Lab 2 — Governance and data map

Create a team with standard/private/shared channels and synthetic files/chats. Map group, SharePoint sites, OneDrive/Exchange artifacts, owners, labels, retention and deletion/restore. **Evidence:** object map and lifecycle test.

### Lab 3 — External collaboration

Configure a guest and tabletop/shared-channel partner. Test federation, guest team/file access and B2B direct connect requirements with controlled policies. **Evidence:** cross-tenant matrix and positive/negative tests.

### Lab 4 — Policies, devices, and automation

Create a policy package/group assignment and inspect effective policy. Model a Teams Room account/profile/tag/update and export inventory using PowerShell/Graph read-only. **Evidence:** assignment precedence, device runbook and sanitized automation output.

### Lab 5 — Teams/channel/app lifecycle

Create from a template, change membership/roles, archive/unarchive and assess a harmless app/custom manifest. **Evidence:** lifecycle record, channel-boundary matrix and app approval worksheet.

### Lab 6 — Meetings and events

Configure a meeting policy, template and protected scenario; compare meeting, appointment, webinar and town-hall requirements. Test organizer/presenter/attendee/guest behavior. **Evidence:** effective policies and experience matrix.

### Lab 7 — Teams Phone call flow

Diagram user/service numbers, resource accounts, auto attendant, call queue, schedules, agents, timeout and overflow. If licensed, implement with test numbers. **Evidence:** license map and tested business/after-hours/failure paths.

### Lab 8 — Quality and client incident

Use a controlled test call/meeting and CQD/Call Analytics/client evidence. Introduce a safe local issue or compare known-good/bad networks. **Evidence:** timeline, metrics, root-cause decision, remediation and retest.

---

## Knowledge checks

1. **Where are standard channel files stored?** In the parent team's SharePoint site.
2. **Private/shared channel content boundary?** Separate membership and associated SharePoint site behavior.
3. **What does QoS solve?** Priority during contention; it does not add bandwidth.
4. **CQD versus Call Analytics?** CQD finds aggregate patterns; Call Analytics investigates a particular user/session.
5. **Why upload tenant network data to CQD?** To map telemetry to meaningful sites/subnets/buildings.
6. **Conditional Access versus Teams policy?** CA controls access/session; Teams policy controls service features.
7. **Retention versus archive?** Retention governs content lifecycle; archive changes collaboration state.
8. **Policy package purpose?** Apply a coherent set of Teams policies to a persona.
9. **Does a scope group assignment apply instantly?** Processing takes time; verify effective policy.
10. **External access versus guest access?** Federation communication versus resource-tenant membership/collaboration.
11. **Shared channel identity model?** B2B direct connect through compatible cross-tenant policy.
12. **Why can a guest chat but not open a file?** Teams guest/federation and SharePoint permission/sharing are separate.
13. **MTO purpose?** Coordinate collaboration/user experience across related tenants under current capabilities.
14. **Teams Room account needs?** Resource account/mailbox, license, device configuration, network and supported access policy.
15. **Why media optimization in VDI?** Offload media to endpoint and avoid poor virtual-desktop hairpin behavior.
16. **Template versus policy?** Template creates a starting structure; policies continually govern supported behavior.
17. **Standard/private/shared channel selection?** Choose from membership and cross-tenant boundary.
18. **App allow versus consent?** Teams availability and Entra/API authorization are separate.
19. **Tab versus message extension?** Embedded contextual UI versus compose/message search/action.
20. **What should app approval record?** Publisher, permissions, data, owner, audience, license, telemetry and revoke path.
21. **Meeting versus webinar versus town hall?** Interactive collaboration, registration event, and one-to-many produced event.
22. **Settings versus meeting policy?** Tenant-wide/default capability versus organizer/user policy.
23. **What affects meeting Copilot?** License, policy/options, transcript/recording context, client, data governance and rollout.
24. **Teams Phone versus PSTN connectivity?** Cloud calling control versus carrier/route to public network.
25. **Resource account versus queue?** Identity/number anchor versus routing application.
26. **Auto attendant versus call queue?** Menu/schedule routing versus agent distribution.
27. **Why test holidays and overflow?** Happy-path business-hours routing does not prove resilience.
28. **Usage report proves value?** No; combine activity with outcomes, quality, risk and support.
29. **First client incident step?** Capture exact user/time/session/client/device/network/policy/error before resetting.
30. **Why preserve logs before clearing cache?** Cache reset can destroy diagnostic evidence.
31. **What metrics indicate network media trouble?** Loss, jitter, RTT and bitrate in endpoint/path context.
32. **Why compare known-good endpoint/network?** It isolates device/client from network/service causes.
33. **One user cannot sign in; disable CA?** No; inspect sign-in and policy evaluation and change narrow scope only.
34. **Copilot missing in meeting; first checks?** Entitlement, effective meeting policy/options, transcript/context, supported client and rollout.
35. **What makes Graph automation safe?** Stable IDs, least privilege, bounded target preview, throttling/error handling, logs and rollback.
36. **What proves a Teams change?** Effective policy/object state plus controlled user experience, telemetry and a negative test.

---

## Places to learn

This is a curated starting point, **not a complete list**, and it is not meant to be consumed in full. Choose one primary path, practice in a tenant, and select supplements from measured gaps. Reconcile all older resources with the July 29, 2026 blueprint, especially MTO, Copilot/AI troubleshooting, current events, policies and external collaboration.

The four official paths are [get started](https://learn.microsoft.com/en-us/training/paths/get-started-managing-microsoft-teams/) (3h36), [prepare the environment](https://learn.microsoft.com/en-us/training/paths/prepare-environment-for-microsoft-teams-deployment/) (3h20), [manage chat/teams/channels/apps](https://learn.microsoft.com/en-us/training/paths/manage-chat-teams-channels-apps-microsoft-teams/) (3h02), and [manage meetings/calling](https://learn.microsoft.com/en-us/training/paths/manage-meetings-calling-microsoft-teams/) (9h03), totaling **19 hours 1 minute**.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MS-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/m365-teams-administrator-associate/) | Public | 1–2 hours initially; 15 minutes per recheck |
| Four official paths from [MS-700T00](https://learn.microsoft.com/en-us/training/courses/ms-700t00) | Public | 19 hours 1 minute listed; allow 30–50 hours with labs and notes |
| MS-700T00 instructor-led course | Paid/partner delivery | 4 days listed |
| [Microsoft MS-700 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/m365-teams-administrator-associate/practice/assessment?assessment-type=practice&assessmentId=55&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Pluralsight MS-700 path](https://www.pluralsight.com/paths/managing-microsoft-teams) | Paid | 19 hours; core material last refreshed 2024 and voice/device courses 2022—supplement July 2026 |
| [O'Reilly/Packt MS-700 Third Edition](https://www.oreilly.com/library/view/ms-700-managing-microsoft/9781835883945/) by Nate Chamberlain and Peter Rising | Paid | 10 hours 41 minutes / 502 pages listed; August 2024, supplement July 2026 |
| [O'Reilly/ACI MS-700 video](https://www.oreilly.com/videos/managing-microsoft-teams/9781836643135/) with Adam Gordon | Paid | 31 hours 3 minutes; August 2024, supplement July 2026 |
| [Udemy MS-700 with labs](https://www.udemy.com/course/microsoft-teams-examlabpractice/) by John Christopher | Paid | Verify runtime on page; updated February 2026, so supplement July changes; allow 20–35 hours including simulations/review |
| [MeasureUp MS-700](https://www.measureup.com/microsoft-practice-test-ms-700-managing-microsoft-teams.html) | Paid | 155 questions listed, last updated September 2025; allow 6–10 hours with remediation and verify July changes |
| [Udemy current-blueprint practice](https://www.udemy.com/course/ms-700-practice-tests-teams-administrator-2026/) by Dean Ellerby | Paid | 360 original questions; allow 10–16 hours with Microsoft Learn source review; updated August 2026 |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics), [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor), and [John Savill](https://www.youtube.com/@NTFAQGuy) | Public | 2–10 hours selectively; no complete current MS-700 playlist was confirmed |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use the published event start/end times after sign-in |

Start with Microsoft's free Practice Assessment. Add paid questions only for a different explanation style or measured gap; reject any provider claiming recalled live questions.

## Final readiness checklist

- I can map each objective to its owning Teams/Microsoft 365 object, role, policy, evidence and recovery.
- I can calculate and validate network/media readiness and use CQD versus Call Analytics correctly.
- I can govern team/group/data lifecycle, external/guest/shared-channel/MTO collaboration and device clients.
- I can manage teams, channels, chats, apps and extensibility without confusing Teams policy with Entra/resource authorization.
- I can select and configure meeting/event and Teams Phone objects, policies, licenses and call flows.
- I can troubleshoot client, sign-in, media, meeting and Copilot issues without erasing evidence or weakening policy broadly.
- I completed or tabletop-tested all eight labs and can prove positive and negative outcomes.
- I passed an independent readiness check without relying on recalled live-exam content.
